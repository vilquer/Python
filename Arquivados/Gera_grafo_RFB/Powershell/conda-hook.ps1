$Env:CONDA_EXE = "C:/Users/IEUser/anaconda3\Scripts\conda.exe"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "C:/Users/IEUser/anaconda3"
$Env:_CONDA_EXE = "C:/Users/IEUser/anaconda3\Scripts\conda.exe"

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1"
Add-CondaEnvironmentToPrompt

cd D:\CNPJ-full-master
conda activate D:\CNPJ-full-master\env
python Pesquisa.py
exit