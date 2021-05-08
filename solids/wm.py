import pandas as pd
from dagster import solid
from sqlalchemy import create_engine
from dotenv import dotenv_values

config = dotenv_values('.env')
db = create_engine(config['DATABASE_URL'])
filename = config['WM_FILENAME']

@solid
def load(_):
    df = pd.read_csv(filename, index_col=0)
    df.to_sql(con=db, name='wm', if_exists='replace')