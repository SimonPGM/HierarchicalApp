import pandas as pd
import json
import plotly
import plotly.express as px

MONTHS = ["Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
    "Octubre", "Noviembre", "Diciembre"
]

def city_corrector(city: str):
    
    if city == "MEDELLIN":
        return "Medellín"
    
    elif city == "ITAGUI":
        return "Itagüí"
    
    elif city == "LA ESTRELLA":
        return "La Estrella"
        
    return city.capitalize()

def title_generator(year: int, municiple: str):
    return f"Comparación entre el modelo y los datos reales en el municipio de {municiple} en el {year}"

def plot(year: int, path: str, municiple: str):
    
    municiple = municiple.upper()
    print(municiple)
    df = pd.read_csv(path)
    df = df[(df.Municipio == municiple) & (df.Anio == year)]
    df.Mes = df.Mes.apply(lambda x: MONTHS[x-1])
    
    fig = px.line(df, x="Mes", y="Recuperados", color="Clase",
    line_dash="Clase", hover_name="Clase", title=title_generator(year, city_corrector(municiple)))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
