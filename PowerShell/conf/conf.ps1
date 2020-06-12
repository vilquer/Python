
#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\ProgramData\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion
# muda o enviroment
conda activate teste
# vai para pasta correta
cd $home\Documents\GitHub
# PowerShell -executionpolicy bypass -noexit -File %USERPROFILE%\Documents\PowerShell\conf\conf.Ps1
# tambem pode ser feito com o comando: Echo “Aguarde! O Jupyter ja vai abrir!”
Write-Output ""
Write-Output ""
Write-Output "Aguarde! O Jupyter ja vai abrir!"
Write-Output ""
Write-Output ""
jupyter lab