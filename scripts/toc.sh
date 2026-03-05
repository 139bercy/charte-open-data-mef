#!/bin/bash

file=$1

echo "Delete ToC"

sed -i "" '/^## Table$/,/^## Introduction$/{/^## Introduction$/!d;}'  $file
markdown-toc -h 3 -t github --table-of-contents-style "## Table" $file
mdformat src
