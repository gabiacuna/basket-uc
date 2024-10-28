from django.core.management.base import BaseCommand
import csv
from app.models import User
import pandas as pd
import gdown

class Command(BaseCommand):
    help = 'Imports users from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def rename_columns(self, filename='SOCIOS', debug=False):
        # read xlsx file
        df = pd.read_excel(f'{filename}.xlsx')

        # Read the CSV file
        # df = pd.read_csv('SOCIOS.csv')

        if debug: print('columns:', df.columns)

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

        if debug: print('doneee!\nHEAD:\n', df.head())
        # Save the CSV file
        df.to_csv(f'{filename}.csv', index=False)

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']

        # Download the file from Google Drive
        # gdown --id 1oaPgWIBu5dfxcv1GFjhoHTRzlN_XDHfPHUmO3DDb0Qw -O SOCIOS.xlsx   
        id = '1oaPgWIBu5dfxcv1GFjhoHTRzlN_XDHfPHUmO3DDb0Qw'
        output = f'{csv_file_path[:-4]}.xlsx'
        gdown.download(id=id, output=output)

        # Rename the columns
        self.rename_columns(csv_file_path[:-4])

        # Open and read the CSV file
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Iterate through the CSV rows
            for row in reader:
                # check if the user already exists
                if User.objects.filter(rut=row['rut']).exists():
                    # self.stdout.write(self.style.WARNING(f'User with rut {row["rut"]} already exists'))
                    continue
                user = User(
                    rut=row['rut'],
                    email=row['email'],
                    name=row['name'],
                    last_name=row['last_name'],
                    member_type=row['member_type'],
                    observation=row['observation']
                )
                user.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
