#!/bin/bash
whatweb $1
echo "---NIKTO---:"
nikto -h $1
echo "---Dirbuster---:"
dirb $1 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
