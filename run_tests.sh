#!/bin/bash

echo 'CLEAR REPORTS FOLDER'
rm -r reports/*
ehco 'END CLEARING OLD REPORTS'

echo 'START TEST EXECUTION'
mvn gatling:test
echo 'END TEST EXECUTION'

echo 'START PREPARING REPORTS'
ls target/gatling
for dirName in $(ls target/gatling | grep -o "[a-z]*scenario" | sort -u);
do
  if [ -d reports/$dirName ];
  then
     echo "Directory $dirName exists"
  else
    echo "Creating directory $dirName"
    mkdir reports/$dirName;
  fi

cp -r target/gatling/$dirName-* reports/$dirName
done
echo 'END PREPARING REPORTS'