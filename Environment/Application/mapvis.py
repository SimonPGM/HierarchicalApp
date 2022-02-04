import folium
import pandas as pd

def city_corrector(city: str):
    
    if city == "MEDELLIN":
        return "Medellín"
    
    elif city == "ITAGUI":
        return "Itagüí"
    
    elif city == "LA ESTRELLA":
        return "La Estrella"
        
    return city.capitalize()

def filter_df(path:str, year:int, month:int):
    
    df = pd.read_csv(path)
    df = df[(df.Anio == year) & (df.Mes == month) & (df.Clase == "Predicho")]
    df = df.loc[:, ["Recuperados", "Municipio"]]
    
    return df

def gen_map(path:str, year:int, month:int):
    
    init_coords = [6.25, -75.6, 0]
    m = folium.Map(location=init_coords[:2])
    folium.GeoJson("Application/static/json/valle_aburra.geojson", name="geojson").add_to(m)

    tooltips = {"ENVIGADO": [6.17591, -75.59174, 0],
           "ITAGUI": [6.18461, -75.59913, 0],
            "CALDAS": [6.09106, -75.63569, 0],
            "SABANETA": [6.15153, -75.61657, 0],
            "COPACABANA": [6.34633, -75.50888, 0],
            "BARBOSA": [6.43809, -75.33136, 0],
            "BELLO": [6.33732, -75.55795, 0],
            "GIRARDOTA": [6.37747, -75.44883, 0],
            "MEDELLIN": init_coords,
            "LA ESTRELLA": [6.15769, -75.64317, 0]
           }

    temp = filter_df(path, year, month)

    for i in range(len(temp)):
        tooltips[temp.Municipio.values[i]][-1] = temp.Recuperados.values[i]

    for city, coordinates in tooltips.items():
        marker = folium.Marker(coordinates[:2], popup=f"<i>{city_corrector(city)}</i><br><i>{coordinates[-1]}</i>", tooltip="¡Haz click en mi!")
        marker.add_to(m)

    m.save("./Application/templates/mapfolium.html")
