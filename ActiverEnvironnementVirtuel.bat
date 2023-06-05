ECHO OFF

mkdir env
python -m venv env
call env\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r ./requirements.txt 
dotnet tool install -g Microsoft.dotnet-interactive
dotnet interactive jupyter install
echo "Python venv activated"