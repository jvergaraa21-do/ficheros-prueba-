import folium
from geopy.geocoders import Nominatim

# Crear geolocalizador
geolocator = Nominatim(user_agent="mapa_rutas")

# Dirección de la universidad
direccion = "Universidad Rafael Núñez, Cartagena de Indias, Colombia"
ubicacion = geolocator.geocode(direccion)

# Coordenadas de la universidad
lat, lon = ubicacion.latitude, ubicacion.longitude

# Crear mapa centrado en la universidad
mapa = folium.Map(location=[lat, lon], zoom_start=17)

# Marcador de la universidad
folium.Marker(
    [lat, lon],
    popup="Universidad Rafael Núñez - Sede Principal",
    icon=folium.Icon(color="red", icon="university", prefix="fa")
).add_to(mapa)

# Coordenadas que simulan una vuelta alrededor del edificio
# (unos metros alrededor del punto central)
ruta = [
    [lat + 0.0010, lon - 0.0010],
    [lat + 0.0010, lon + 0.0010],
    [lat - 0.0010, lon + 0.0010],
    [lat - 0.0010, lon - 0.0010],
    [lat + 0.0010, lon - 0.0010]  # Cierra el ciclo
]

# Dibujar la ruta (una vuelta alrededor)
folium.PolyLine(
    locations=ruta,
    color="blue",
    weight=5,
    opacity=0.8,
    tooltip="Ruta alrededor de la universidad"
).add_to(mapa)

# Guardar el mapa
mapa.save("ruta_universidad.html")

print("✅ Mapa creado: abre 'ruta_universidad.html' en tu navegador.")
