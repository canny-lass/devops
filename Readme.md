To run the application python3 must be installed on the system.
Once python is installed run the following 

python3 -m venv venv
source venv/bin/activate

navigate to the src directory and run the following: 

pip3 install -R requirements.txt

Once the requirements are installed, run the following

python .\manage.py migrate

python .\manage.py runserver

To deploy to the test environment push to the dev brabch, for the production push to master branch.
