import csv
from app.models import User
import pandas as pd

def rename_columns(filename='SOCIOS'):
        # read xlsx file
    df = pd.read_excel(f'{filename}.xlsx')

    # Read the CSV file
    # df = pd.read_csv('SOCIOS.csv')

    print('columns:', df.columns)

    # Rename the columns
    df.rename(columns={
        'Marca temporal': 'time_stamp',
        'RUT Sin puntos, con guion (12345678-9) ': 'rut',
        'EMAIL': 'email',
        'NOMBRE': 'name',
        'APELLIDOS': 'last_name',
        'SOCIO': 'member_type',
        'OBSERVACIONES': 'observation'
    }, inplace=True)

    # format timestamp column from 7/10/2024 19:28:17 to standard SQL DATETIME


    df['time_stamp'] = pd.to_datetime(df['time_stamp'], format='%d/%m/%Y %H:%M:%S')

    print('doneee!\nHEAD:\n', df.head())
    # Save the CSV file
    df.to_csv(f'{filename}.csv', index=False)

# Path to your CSV file
filename = 'SOCIOS'

rename_columns(filename)

# Open and read the CSV file
with open(f'{filename}.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate through the CSV rows
    for row in reader:
        # Create a new User object for each row
        user = User(
            rut=row['rut'],
            email=row['email'],
            name=row['name'],
            last_name=row['last_name'],
            member_type=row['member_type'],
            observation=row['observation']  # Optional field
        )
        # Save the object to the database
        user.save(force_update=True)

print("Data imported successfully.")
