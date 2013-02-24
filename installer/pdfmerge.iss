; Installer for pdfmerge

#define appName "pdfmerge"
#define appVersion "0.0.2"

[Setup]
AppId=com.metaist.pdfmerge
AppName={#appName}
AppVersion=0.0.2
DefaultDirName={pf}\Metaist\pdfmerge
DefaultGroupName=Metaist\pdfmerge
ChangesEnvironment=true

Compression=lzma
SolidCompression=yes
OutputDir=..\releases
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