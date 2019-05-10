@echo off  
set sdsiosloginfo="%~dp0\sdsiosloginfo.exe"
set xcodelog="%~dp0\xcode.log"
echo "¹Ø±Õ´°¿ÚÍ£Ö¹"
%sdsiosloginfo% -d >%xcodelog%
 
pause