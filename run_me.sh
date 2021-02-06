echo Runs the server in dev enviroment
echo To test it open any browser and  go to:
echo       http://localhost:8080/
echo       http://localhost:8080/fib/1
echo       http://localhost:8080/fib/2
echo       http://localhost:8080/fib/3
echo       etc...
echo       Expected response to http://localhost:8080/fib/10
echo       {"desc": "fibonacci number", "index": 10, "value": 55}
source venv/bin/activate

python fibb_serv.py 




