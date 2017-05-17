import requests

ACCIONES = ['EXITO', 'ECOPETROL', 'BCOLOMBIA']

for ACCION in ACCIONES:
    r = requests.get(('https://www.bvc.com.co/mercados/GraficosServlet?home=no&tipo=ACCION&mercInd=RV&nemo={0}&tiempo=ayer').format(ACCION))
    datos = r.content

    for line in datos.split(b"\n"):
        print(line)

