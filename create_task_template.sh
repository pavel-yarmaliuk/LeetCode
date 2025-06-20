#!/bin/bash

while getopts t:N:n:l:u:s: flag  
do
  case "${flag}" in
    t) type=${OPTARG};;
    N) number=${OPTARG};;
    n) name=${OPTARG};;
    l) language=${OPTARG#[$'\r\t\n ']%};;
    u) url=${OPTARG};;
    s) src=${OPTARG};;
  esac
done

if [ "$type" == "alg" ]; then
  directory="Algorithms"
elif [ "$type" == "sql" ]; then
  directory="SQL"
else
  echo "Incorrect type of task! (allowable task types are [alg, sql])"
  exit 1
fi

echo "Writing into current subdirectory ${directory}"

if [ "$src" == "leetcode" ]; then
    directory+="/Leetcode"
elif [ "$src" == "codeforcess" ]; then 
    directory+="/Codeforcess"
elif [ "$src" == "codewars" ]; then 
    directory+="/Codewars"
elif [ "$src" == "hackerrank" ]; then 
    directory+="/Hackerrank"
else
    echo "Incorrect source type! (supported sources [leetcode, codeforcess, codewars, hackerrank])"
    exit 1
fi

echo "Writing into current subdirectory ${directory}"

if [ "$language" == "python" ]; then
  filetype="py"
  badge="(https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)"
elif [ "$language" == "sql" ]; then
  filetype="sql"
  badge="(https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)"
elif [ "$language" == "c++" ]; then
  filetype="cpp"
  badge="(https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)"
elif [ "$language" == "java" ]; then
  filetype="java"
  badge="(https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)"
elif [ "$language" == "scala" ]; then
  filetype="scala"
  badge="(https://img.shields.io/badge/scala-%23DC322F.svg?style=for-the-badge&logo=scala&logoColor=white)"
else
  echo "Incorrect Language! (allowable languages are [python, sql, c++, java, scala])"
  echo $language
  exit 1
fi

mkdir -p "${directory}/${number}${name}"
mkdir -p "${directory}/${number}${name}/images"
sed "s/ProblemName.ProblemNumber/${number}.${name}/" "template.md" > "${directory}/${number}${name}/temp.md"
sed -i "s|problemUrl|${url}|" "${directory}/${number}${name}/temp.md"
mv "${directory}/${number}${name}/temp.md" "${directory}/${number}${name}/README.md"
touch "${directory}/${number}${name}/${number}${name}.${filetype}"

echo $badge
echo $directory
echo $language

./update_readme.sh -N "${number}" -n "${name}" -l "${language}" -b "${badge}" -d "${directory}" -s "${src}"
