#!/bin/bash

while getopts N:n:l:b:d:s: flag  
do
  case "${flag}" in
    N) number=${OPTARG};;
    n) name=${OPTARG};;
    l) language=${OPTARG};;
    b) badge=${OPTARG};;
    d) directory=${OPTARG};;
    s) src=${OPTARG};;
  esac
done


if [ "${src}" == "leetcode" ]; then
    source_badge="![Leetcode](https://img.shields.io/badge/LeetCode-000000?logo=LeetCode&logoColor=#d16c06)"
elif [ "${src}" == "codeforcess" ]; then
    source_badge="![Codeforcess](https://img.shields.io/badge/Codeforces-1F8ACB?style=flat&logo=Codeforces&logoColor=white)"
elif [ "${src}" == "codewars" ]; then
    source_badge="![Codewars](https://img.shields.io/badge/Codewars-B1361E?style=flat&logo=Codewars&logoColor=white)"
elif [ "${src}" == "hackerrank" ]; then
    source_badge="![Hackerrank](https://img.shields.io/badge/-Hackerrank-00EA64?style=flat&logo=HackerRank&logoColor=white)"
else
    echo "Incorrect source type! supported sources [leetcode, codeforcess, hackerrank, codewars]"
    exit 1
fi

solution_image_path="${directory}/${number}${name}/images/screenshot.png"


echo "

## ${source_badge} ![${language}]${badge} [${number}.${name}](${directory}/${number}${name}/README.md) 
![Solution image ${number}](${solution_image_path})" >> "README.md"
