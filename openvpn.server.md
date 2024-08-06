# Introduction
Setting up an OpenVPN server on Ubuntu 24.04 is a great way to ensure secure and private connections to your network.
Below, I'll guide you through the steps to install and configure an OpenVPN server on an Ubuntu 24.04 machine.

# Prerequisites
- Ubuntu 24.04 server: Make sure your server is up-to-date.
- Root access: You should have root privileges or be able to use sudo for administrative tasks.
- Public IP address: Ensure your server has a public IP address.
- Firewall: Adjustments may be necessary based on your firewall configuration.

# Installation
**Step 1: Update the System**

First, update your package index and upgrade your system to ensure all packages are up-to-date.

- `sudo apt update`
- `sudo apt upgrade -y`

**Step 2: Install OpenVPN and Easy-RSA**

OpenVPN is available in Ubuntu's default repositories, and Easy-RSA is a utility for managing X.509 PKI (Public Key Infrastructure).

- `sudo apt install openvpn easy-rsa -y`

**Step 3: Set Up the CA Directory**

Easy-RSA needs a directory to work in. Create a directory and initialize the PKI (Public Key Infrastructure).

- `make-cadir ~/openvpn-ca`
- `cd ~/openvpn-ca`

Edit the vars file in the Easy-RSA directory to set the default values for your certificates:

- `vi vars`

Find and edit the following lines with your information:

```
set_var EASYRSA_REQ_COUNTRY     "FR"
set_var EASYRSA_REQ_PROVINCE    "France"
set_var EASYRSA_REQ_CITY        "Massy"
set_var EASYRSA_REQ_ORG         "Loti"
set_var EASYRSA_REQ_EMAIL       "tho.nk1325@gmail.com"
set_var EASYRSA_REQ_OU          "IT"
```

**Step 4: Build the Certificate Authority**

Now, we can create the root certificate authority (CA) that we will use to sign client/server certificates.

***Clean and initialize the PKI:***

- `./easyrsa clean-all`
- `./easyrsa init-pki`

***Build the CA:***

- `./easyrsa build-ca`

You will be prompted to enter a password for the CA. Choose something secure and remember it, as you'll need it later.

**Step 5: Generate Server Certificate and Key**

Generate the server certificate and key. Replace server with your desired server name.

- `./easyrsa gen-req server nopass`
- `./easyrsa sign-req server server`

**Step 6: Generate Diffie-Hellman Key Exchange**

The Diffie-Hellman key exchange is used to establish secure connections.

- `./easyrsa gen-dh`
  
**Step 7: Create HMAC Key**
To enhance the server's security, create an HMAC key to help defend against DoS attacks.

`openvpn --genkey --secret ta.key`

**Step 8: Configure the OpenVPN Server**

Copy the necessary files to the /etc/openvpn directory.

`sudo cp pki/ca.crt pki/issued/server.crt pki/private/server.key pki/dh.pem ta.key /etc/openvpn`

Create and edit the OpenVPN server configuration file.
- `cp /usr/share/doc/openvpn/examples/sample-config-files/server.conf /etc/openvpn/server.conf`
- `sudo vi /etc/openvpn/server.conf`

Modify the serve.conf

```
port 1194
proto udp
dev tun

ca ca.crt
cert server.crt
key server.key  # This file should be kept secret
dh dh2048.pem

topology subnet
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist /var/log/openvpn/ipp.txt
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"
keepalive 10 120

tls-auth ta.key 0 # This file is secret

user nobody
group nogroup
persist-key
persist-tun
status /var/log/openvpn/openvpn-status.log
log         /var/log/openvpn/openvpn.log
log-append  /var/log/openvpn/openvpn.log
verb 3
explicit-exit-notify 1
```

**Step 9: Enable IP Forwarding**
Edit the sysctl configuration to enable IP forwarding.


- `sudo vi /etc/sysctl.conf`

Uncomment or add the following line:

- `net.ipv4.ip_forward = 1`

Apply the changes:

- `sudo sysctl -p`

**Step 10: Configure the UFW Firewall**

If you use UFW (Uncomplicated Firewall), configure it to allow OpenVPN traffic.

***Allow OpenVPN through UFW:***

- `sudo ufw allow 1194/udp`

***Allow traffic to be forwarded from the VPN:***

- `sudo vi /etc/default/ufw`

Change:

```
DEFAULT_FORWARD_POLICY="ACCEPT"
```

***Configure NAT:***

- `sudo nano /etc/ufw/before.rules`

Add these lines at the top (Replace eth0 with your actual network interface):

```
# START OPENVPN RULES
# NAT table rules
*nat
:POSTROUTING ACCEPT [0:0]
# Allow traffic from OpenVPN client to eth0 (change to the interface you discovered!)
-A POSTROUTING -s 10.8.0.0/8 -o eno1 -j MASQUERADE
COMMIT
# END OPENVPN RULES
```

***Enable UFW:***

- `sudo ufw enable`

**Step 11: Start and Enable OpenVPN**

Start the OpenVPN service and enable it to start on boot.

- `sudo systemctl start openvpn@server`
- `sudo systemctl enable openvpn@server`

Restart
- `sudo systemctl restart openvpn@server.service`


Verify the service status:

- `sudo systemctl status openvpn@server`

**Step 12: Generate Client Certificates and Keys**

Now, let's create client certificates and keys. We'll also configure a client configuration file.

Generate a client certificate and key. Replace client1 with your desired client name.

- `cd ~/openvpn-ca`
- `./easyrsa gen-req client1 nopass`
- `./easyrsa sign-req client client1`

Copy the client files to a new directory for easy packaging:

- `mkdir -p ~/client-configs/keys`
- `cp pki/ca.crt pki/issued/client1.crt pki/private/client1.key ta.key ~/client-configs/keys/`

**Step 13: Create the Client Configuration**

Create a base configuration file that will be used to generate client-specific files.

Create and edit base.conf:

- `vi ~/client-configs/base.conf`

Replace yyour_ip<public_or_local> with the public IP address of your OpenVPN server.
Add the following configuration:

```
client
dev tun
proto udp
# remote your_ip<public_or_local> 1194
remote 192.168.1.40 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
# tls-auth ta.key 1
cipher AES-256-GCM
auth SHA256
key-direction 1
verb 3
```

***Create a script to build the client configuration file:***

- `vi ~/client-configs/make_config.sh`

Add the following script:

```
#!/bin/bash
 
# First argument: Client identifier
 
KEY_DIR=~/client-configs/keys
OUTPUT_DIR=~/client-configs/files
BASE_CONFIG=~/client-configs/base.conf
 
cat ${BASE_CONFIG} \
    <(echo -e '<ca>') \
    ${KEY_DIR}/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    ${KEY_DIR}/${1}.crt \
    <(echo -e '</cert>\n<key>') \
    ${KEY_DIR}/${1}.key \
    <(echo -e '</key>\n<tls-auth>') \
    ${KEY_DIR}/ta.key \
    <(echo -e '</tls-auth>') \
    > ${OUTPUT_DIR}/${1}.ovpn
```

Make the script executable:

- `chmod 700 ~/client-configs/make_config.sh`

Create a directory for the client files:

- `mkdir ~/client-configs/files`

Generate a client configuration file:
- `~/client-configs/make_config.sh client1`

The generated .ovpn file will be located in the ~/client-configs/files directory.

**Step 14: Test the OpenVPN Connection**
Transfer the .ovpn file to your client machine (using SCP, SFTP, etc.) and import it into your OpenVPN client application. Connect and verify that you have a secure VPN connection.

# Troubleshooting
Conclusion
You have successfully set up an OpenVPN server on Ubuntu 24.04! This server allows clients to securely connect to your network from remote locations. You can create additional client configuration files as needed for more users.

If you encounter any issues, make sure to check the OpenVPN logs for troubleshooting:

bash
Copy code
sudo less /var/log/openvpn.log
Additionally, verify that your firewall and network settings are correctly configured to allow VPN traffic.

Mac openvpn client traffic error udp:
```
https://forums.openvpn.net/viewtopic.php?t=35547
Sounds like the openVPN connect launch daemon is not working.
Can you run the following command in the terminal and see if you get an output:
Code: Select all

sudo launchctl list | grep org.openvpn.client
If there are no outputs then you can try loading it manually via the command:
Code: Select all

sudo launchctl load /Library/LaunchDaemons/org.openvpn.client.plist
But, in case if it will stop working again you may want to check if there is any other 3rd party application that is preventing the ovpn client agent from starting.
```