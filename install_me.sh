echo Installation - dev env
echo Prerequisite:  you have python3 and python-venv3 installed in your system

python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt

echo Done!
