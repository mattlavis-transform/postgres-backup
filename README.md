Database backup

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python3 -m venv venv/`
  `source venv/bin/activate`

- Install necessary Python modules 

  - autopep8==1.5.4
  - psycopg2==2.8.6
  - pycodestyle==2.6.0
  - python-dotenv==0.15.0
  - sh==1.14.1
  - toml==0.10.2

  via `pip3 install -r requirements.txt`


## Usage

`python3 backup.py <dbname>`

e.g.

`python3 backup.py tariff_uk_production`