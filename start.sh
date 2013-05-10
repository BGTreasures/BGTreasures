source bin/activate
pip install -r requirements.txt
python bgtreasures/manage.py syncdb
python bgtreasures/manage.py runserver
