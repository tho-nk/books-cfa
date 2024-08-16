./immich-go \
  -server=http://192.168.1.40:2283/photos \
  -key=ye6fkFibKM1b4fOhEZbBQfsayCEhMCIjOfUrdG1yEL4 \
  upload \
  -dry-run \
  -create-albums \
  -google-photos \
  Takeout/


  https://www.devroom.io/2024/03/21/import-google-photos-takeout-into-immich/


  ./immich-go \
  -server=http://192.168.1.40:2283/ \
  -key=ye6fkFibKM1b4fOhEZbBQfsayCEhMCIjOfUrdG1yEL4 \
  upload \
  -dry-run \
  -create-albums \
  Takeout/takeout*zip


  ./immich-go \
  -server=http://192.168.1.40:2283/ \
  -key=ye6fkFibKM1b4fOhEZbBQfsayCEhMCIjOfUrdG1yEL4 \
  upload \
  -create-albums \
  Takeout/takeout*zip