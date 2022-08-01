#This command is used to unzip all zip files in a folder as zip *.zip throws an error.

find . -name "*.zip" -exec unzip {} \;


