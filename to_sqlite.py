import sqlite3
import pandas as pd
from pathlib import Path

DATABASE = 'mlb-data.sqlite'

path_to_data = Path.cwd()
dir_paths = [x for x in path_to_data.iterdir() if x.is_dir() and x.name in ['core','contrib']]
csv_files = [[f for f in x.iterdir() if f.suffix =='.csv'] for x in dir_paths]
csv_files = [f for l in csv_files for f in l]

conn = sqlite3.connect(DATABASE)
for csv in csv_files:
    df = pd.read_csv(csv)
    df.columns = [c.replace('.','_') for c in df.columns]
    df.to_sql(csv.stem,conn,if_exists='replace',index = False)
conn.close()