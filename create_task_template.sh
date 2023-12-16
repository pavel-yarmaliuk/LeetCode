#!/bin/bash

while getopts t:N:n:l:u: flag  
do
  case "${flag}" in
    t) type=${OPTARG};;
    N) number=${OPTARG};;
    n) name=${OPTARG};;
    l) language=${OPTARG};;
    u) url=${OPTARG};;
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

if [ "$language" == "python" ]; then
  filetype="py"
elif [ "$language" == "sql" ]; then
  filetype="sql"
elif [ "$language" == "c++" ]; then
  filetype="cpp"
elif [ "$language" == "java" ]; then
  filetype="java"
elif [ "$language" == "scala" ]; then
  filetype="scala"
else
  echo "Incorrect Language! (allowable languages are [python, sql, c++, java, scala])"
  exit 1
fi

mkdir -p "${directory}/${number}${name}"
sed "s/ProblemName.ProblemNumber/${name}/" "template.md" > "${directory}/${number}${name}/temp.md"
sed -i "s/problemName/${url}/" "${directory}/${number}${name}/temp.md"
mv "${directory}/${number}${name}/temp.md" "${directory}/${number}${name}/${number}${name}Solution.md"
touch "${directory}/${number}${name}/${number}${name}.${filetype}"
