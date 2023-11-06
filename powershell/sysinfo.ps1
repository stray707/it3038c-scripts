function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
    }

$IP = getIP
$Username = $env:USERNAME
$Hostname = $env:COMPUTERNAME
$PSVersion = $HOST.Version.Major
$CurrentDate = Get-Date -Format "dddd, MMMM dd, yyyy"

$Body = "This machine's IP is $IPAddress. User is $Username. Hostname is $Hostname. PowerShell Version $PSVersion. Today's date is $CurrentDate."

write-host($Body)