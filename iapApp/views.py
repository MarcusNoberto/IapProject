from django.shortcuts import render, HttpResponse

import os
import pandas as pd
from .models import IAP, Jogo

def process_data_files(request):
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    arquivos = os.listdir(data_path)

    for arquivo in arquivos:
        jogo = None
        if 'tennis' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="TennisClash")
        elif 'zooba' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="Zooba")
        elif 'battle' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="BattleTanks")
        elif 'sniper' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="Sniper3D")
        elif 'sky' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="SkyWarriors")
        elif 'number' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="ColorByNumber")
        elif 'blockcraft' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="BlockCraft")
        elif 'colorfy' in arquivo:
            jogo, _ = Jogo.objects.get_or_create(nome="Colorfy")

        if jogo:
            df = pd.read_csv(os.path.join(data_path, arquivo))
            delimiter = ";"
            for index, row in df.iterrows():
                row_elements = row['Price'].split(delimiter)
                us_index = next((i for i, elem in enumerate(row_elements) if 'US' in elem), None)
                if us_index is not None:
                    iap_name = row[0]
                    value = row_elements[us_index + 1].strip()
                    value = float(value) / 1000000
                    if not IAP.objects.filter(nome=iap_name, jogo=jogo).exists():
                        iap = IAP(nome=iap_name, valor_us=value, price=row['Price'], jogo=jogo)
                        iap.save()
    return HttpResponse("Data processed successfully")


    



    
    


