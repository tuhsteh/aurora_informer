# aurora_informer

Dependencies:
- lxml 3.4.4+
- requests  2.7.0+
- Flask==0.10.1
- Flask-WTF==0.12
- Jinja2==2.8
- MarkupSafe==0.23
- WTForms==2.0.2
- Werkzeug==0.10.4
- argparse==1.2.1
- itsdangerous==0.24
- wsgiref==0.1.2

Before running, be sure to install dependencies using pip or your favorite package manager for python.

# quick start

1. Create & activate a virtual environment
  1. virtualenv ENV_NAME
  2. source ENV_NAME/bin/activate
  3. which python (to verify it's working)
2. Install the requirements.txt file.
  1. pip install -r requirements.txt
3. Start the application
  1. python run.py

**note**

If you make a change to the application which modifies the dependencies be sure to update the requirements.txt file with:
```
pip freeze > requirements.txt
```
