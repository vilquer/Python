## Configurações para usar PowerShell do Windows 10 com Anaconda 3

#### Ativando o PowerShell no Anaconda

Abra o Anaconda Prompt se for seu caso entre no seu enviroment e use o seguinte comando:

```
conda init powershel
```


Após este comando será criado automaticamente em %USERPROFILE%\Documents\ uma pasta chamada "PowerShell"(PowerShell 7.0) ou "WindowsPowerShell"(Windows PowerShell 1.0 - Nativo no Windows) com um arquivo chamado profile.ps1

O Arquivo profile.ps1 terá um conteúdo similar a este:

```
#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\ProgramData\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion
```

#### Abrindo seu enviroment automaticamente 

Podemos editar o arquivo profile.ps1 e colocar nele uma nova linha depois do "#endregion"

com o comando para ativar seu enviroment como o exemplo abaixo:

```
#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\ProgramData\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion

conda activate meu_enviroment
```

Troque o "meu_enviroment" pelo nome do seu enviroment.

## Criando um a atalho no Windows para o Jupyter

#### Criando um novo arquivo de profile para personalizar seu atalho

Crie uma pasta chamada "conf" em "%USERPROFILE%\Documents\PowerShell\".
Copie o arquivo profile.ps1 para "%USERPROFILE%\Documents\PowerShell\conf\" e renomear como "conf.ps1"
Edite este arquivo para que tenha este conteúdo:


```
#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\ProgramData\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion

# Abre seu enviroment (altere o "meu_env" abaixo pelo nome do seu enviroment de trabalho)
conda activate meu_env

# Edite aqui para ir sua pasta de trabalho (isso também poderá ser feito no arquivo de configurações do Jupyter)
# Obs.: o PowerShell, diferente do CMD, não trabalha com "%USERPROFILE%\" mas sim com "$home\"
cd $home\Documents\GitHub

# Exemplo de caminho para criação do atalho no Windows
# %SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe -executionpolicy bypass -noexit -File %USERPROFILE%\Documents\PowerShell\conf\conf.Ps1

# Aqui ciamos uma mensagem na tela. (Tambem pode ser feito com o comando: Echo “Aguarde! O Jupyter ja vai abrir!”)
Write-Output ""
Write-Output ""
Write-Output "Aguarde! O Jupyter ja vai abrir!"
Write-Output ""
Write-Output ""

# aqui você escolhe "jupyter lab" ou "jupter notebook" conforme sua preferência.
jupyter lab
```


#### Criando um atalho para powershell apontando para o arquivo de profile que abre o Jupyter

Crie um novo atalho no windows apontando destino: 

##### Windows PoweShel 1.0 (Nativo no Windows)
%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe -executionpolicy bypass -noexit -File %USERPROFILE%\Documents\PowerShell\conf\conf.Ps1

##### PowerShell 7.0 
"C:\Program Files\PowerShell\7\pwsh.exe" -executionpolicy bypass -noexit -File %USERPROFILE%\Documents\PowerShell\conf\conf.Ps1





