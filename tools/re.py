#coding=utf-8 
import re

text = r"""
comctl32.dll	User Experience Controls Library	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll
xpsp2res.dll	Service Pack 2 Messages	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\xpsp2res.dll
wtsapi32.dll	Windows Terminal Server SDK APIs	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\wtsapi32.dll
ws2help.dll	Windows Socket 2.0 Helper for Windows NT	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\ws2help.dll
ws2_32.dll	Windows Socket 2.0 32-Bit DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\ws2_32.dll
wldap32.dll	Win32 LDAP API DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\wldap32.dll
wintrust.dll	Microsoft Trust Verification APIs	Microsoft Corporation	5.131.2600.5512	C:\WINDOWS\system32\wintrust.dll
winsta.dll	Winstation Library	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\winsta.dll
wininet.dll	Internet Extensions for Win32	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\wininet.dll
winhttp.dll	Windows HTTP Services	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\winhttp.dll
wbemsvc.dll	WMI	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\wbem\wbemsvc.dll
wbemprox.dll	WMI	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\wbem\wbemprox.dll
wbemcomn.dll	WMI	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\wbem\wbemcomn.dll
fastprox.dll	WMI	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\wbem\fastprox.dll
version.dll	Version Checking and File Installation Libraries	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\version.dll
uxtheme.dll	Microsoft UxTheme Library	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\uxtheme.dll
userenv.dll	Userenv	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\userenv.dll
user32.dll	Windows XP USER API Client DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\user32.dll
unicode.nls				C:\WINDOWS\system32\unicode.nls
sxs.dll	Fusion 2.5	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\sxs.dll
sorttbls.nls				C:\WINDOWS\system32\sorttbls.nls
sortkey.nls				C:\WINDOWS\system32\sortkey.nls
shlwapi.dll	Shell Light-weight Utility Library	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\shlwapi.dll
shell32.dll	Windows Shell Common Dll	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\shell32.dll
shdocvw.dll	Shell Doc Object and Control Library	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\shdocvw.dll
setupapi.dll	Windows Setup API	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\setupapi.dll
secur32.dll	Security Support Provider Interface	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\secur32.dll
samlib.dll	SAM Library DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\samlib.dll
rpcrt4.dll	Remote Procedure Call Runtime	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\rpcrt4.dll
psapi.dll	Process Status Helper	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\psapi.dll
powrprof.dll	Power Profile Helper DLL	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\powrprof.dll
oleaut32.dll		Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\oleaut32.dll
ole32.dll	Microsoft OLE for Windows	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\ole32.dll
ntshrui.dll	Shell extensions for sharing	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\ntshrui.dll
ntmarta.dll	Windows NT MARTA provider	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\ntmarta.dll
ntdsapi.dll	NT5DS	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\ntdsapi.dll
ntdll.dll	NT Layer DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\ntdll.dll
netapi32.dll	Net Win32 API DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\netapi32.dll
msvcrt.dll	Windows NT CRT DLL	Microsoft Corporation	7.0.2600.5512	C:\WINDOWS\system32\msvcrt.dll
msvcp60.dll	Microsoft (R) C++ Runtime Library	Microsoft Corporation	6.2.3104.0	C:\WINDOWS\system32\msvcp60.dll
mstask.dll	Task Scheduler interface DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\mstask.dll
msi.dll	Windows Installer	Microsoft Corporation	3.1.4001.5512	C:\WINDOWS\system32\msi.dll
msasn1.dll	ASN.1 Runtime APIs	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\msasn1.dll
mpr.dll	Multiple Provider Router DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\mpr.dll
locale.nls				C:\WINDOWS\system32\locale.nls
linkinfo.dll	Windows Volume Tracking	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\linkinfo.dll
kernel32.dll	Windows NT BASE API Client DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\kernel32.dll
iphlpapi.dll	IP Helper API	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\iphlpapi.dll
imagehlp.dll	Windows NT Image Helper	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\imagehlp.dll
gdi32.dll	GDI Client DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\gdi32.dll
dnsapi.dll	DNS Client API DLL	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\dnsapi.dll
dbghelp.dll	Windows Image Helper	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\dbghelp.dll
ctype.nls				C:\WINDOWS\system32\ctype.nls
cscui.dll	Client Side Caching UI	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\cscui.dll
cscdll.dll	Offline Network Agent	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\cscdll.dll
cryptui.dll	Microsoft Trust UI Provider	Microsoft Corporation	5.131.2600.5512	C:\WINDOWS\system32\cryptui.dll
crypt32.dll	Crypto API32	Microsoft Corporation	5.131.2600.5512	C:\WINDOWS\system32\crypt32.dll
credui.dll	Credential Manager User Interface	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\credui.dll
comres.dll		Microsoft Corporation	2001.12.4414.700	C:\WINDOWS\system32\comres.dll
comdlg32.dll	Common Dialogs DLL	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\comdlg32.dll
clbcatq.dll		Microsoft Corporation	2001.12.4414.700	C:\WINDOWS\system32\clbcatq.dll
browseui.dll	Shell Browser UI Library	Microsoft Corporation	6.0.2900.5512	C:\WINDOWS\system32\browseui.dll
atl.dll	ATL Module for Windows XP (Unicode)	Microsoft Corporation	3.5.2284.1	C:\WINDOWS\system32\atl.dll
apphelp.dll	Application Compatibility Client Library	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\apphelp.dll
advapi32.dll	Advanced Windows 32 Base API	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\advapi32.dll
aclui.dll	Security Descriptor Editor	Microsoft Corporation	5.1.2600.5512	C:\WINDOWS\system32\aclui.dll
Perflib_Perfdata_70c.dat				C:\Documents and Settings\Administrator\Local Settings\Temp\Perflib_Perfdata_70c.dat
Procexp.exe	Sysinternals Process Explorer	Sysinternals - www.sysinternals.com	16.4.0.0	C:\Documents and Settings\Administrator\Desktop\Procexp.exe
"""

m = re.findall(r"\w+\.dll(?=\t)", text)

for i in m:
    print i
    
