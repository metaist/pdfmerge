; Installer for pdfmerge

#define appName "pdfmerge"
#define Version() ParseVersion("..\dist\pdfmerge.exe", Local[0], Local[1], Local[2], Local[3]), str(Local[0]) + "." + str(Local[1]) + "." + str(Local[2])
#define appVersion Version()

[Setup]
AppId=com.metaist.pdfmerge
AppName={#appName}
AppVersion={#appVersion}
DefaultDirName={pf}\Metaist\pdfmerge
DefaultGroupName=Metaist\pdfmerge
ChangesEnvironment=true

Compression=lzma
SolidCompression=yes
OutputDir=.
OutputBaseFilename={#appName}-{#appVersion}-setup

AppPublisher=Metaist
AppCopyright=(C) 2013 Metaist (MIT License)
AppPublisherURL=https://github.com/metaist/pdfmerge
AppSupportURL=https://github.com/metaist/pdfmerge/issues
AppUpdatesURL=https://github.com/metaist/pdfmerge

; Disable the extraneous pages.
DisableWelcomePage=yes
DisableReadyMemo=yes
DisableReadyPage=yes
DisableDirPage=yes
DisableProgramGroupPage=yes
DisableFinishedPage=yes

[Messages]
BeveledLabel=Metaist

[Icons]
Name: "{group}\Readme"; Filename: "{app}\README.markdown"
Name: "{group}\{cm:UninstallProgram,{#appName}}"; Filename: "{uninstallexe}"

[Tasks]
Name: modifypath; Description: &Add {#appName} to system path (recommended)

[Files]
; NOTE: Don't use "Flags: ignoreversion" on any shared system files
Source: "..\*.markdown"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\*"; DestDir: "{app}\bin"; Flags: ignoreversion

[Code]
const
	ModPathName = 'modifypath';
	ModPathType = 'system';

function ModPathDir(): TArrayOfString;
begin
	setArrayLength(Result, 1)
	Result[0] := ExpandConstant('{app}\bin');
end;
#include "modpath.iss"