$downloadPath = $browser.SelectedPath
echo $downloadPath

Add-Type -AssemblyName System.Windows.Forms
$FolderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog
$FolderBrowser.Description = 'Select the Destination Folder'
$result = $FolderBrowser.ShowDialog((New-Object System.Windows.Forms.Form -Property @{TopMost = $true }))
if ($result -eq [Windows.Forms.DialogResult]::OK) {
    $downloadPath = $FolderBrowser.SelectedPath
} else {
    exit
}

$repo = "singh-ramanpreet/wrapper-gcode-ci"
$version = "main"
$filesUrl = "https://raw.githubusercontent.com/$repo/$version"
$filesToDownload = (curl https://api.github.com/repos/singh-ramanpreet/wrapper-gcode-ci/contents `
                    | ConvertFrom-Json).name | Where-Object {($_ -like 'R*.PIT')}
foreach ($file_ in $filesToDownload)
{
    Invoke-WebRequest -Uri $filesUrl/$file_ -Out $downloadPath/$file_
}
