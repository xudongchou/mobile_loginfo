@echo off  
set sdsiosloginfo="%~dp0\sdsiosloginfo.exe"
set xcodelog="%~dp0\xcode.log"
echo "�رմ���ֹͣ"
%sdsiosloginfo% -d >%xcodelog%
 
pause