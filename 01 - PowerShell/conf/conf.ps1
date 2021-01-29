#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\ProgramData\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion
# Abre seu enviroment (altere o "meu_env" abaixo pelo nome do seu enviroment de trabalho)
conda activate teste
# Edite aqui para ir sua pasta de trabalho(isso tambem poderá ser feito no arquivo de configurações do Jupyter)
# Obs.: o PowerShell, diferente do CMD, não trabalha com "%USERPROFILE%\" mas sim com "$home\"
cd $home\Documents\GitHub
# Exemplo de caminho para criação do ataho no Windows
# %SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe -executionpolicy bypass -noexit -File %USERPROFILE%\Documents\PowerShell\conf\conf.Ps1
# Aqui ciamos uma mensagem na tela.(Tambem pode ser feito com o comando: Echo “Aguarde! O Jupyter ja vai abrir!”)
Write-Output ""
Write-Output ""
Write-Output "Aguarde! O Jupyter ja vai abrir!"
Write-Output ""
Write-Output ""

# aqui você escolhe "jupyter lab" ou "jupter notebook" conforme sua preferência.
jupyter lab