#!/bin/bash

while getopts N:n:l:b:d: flag  
do
  case "${flag}" in
    N) number=${OPTARG};;
    n) name=${OPTARG};;
    l) language=${OPTARG};;
    b) badge=${OPTARG};;
    d) directory=${OPTARG};;
  esac
done

solution_image_path="${directory}/images/screenshot.png"


echo "

## [${number}.${name}](${directory}/README.md) Solution language ![${language}]${badge} 
![Solution image ${number}](${solution_image_path})" >> "README.md"
