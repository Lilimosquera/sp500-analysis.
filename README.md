# sp500-analysis.
o Título del proyecto: S&P 500 Analysis Project.
o Descripción del proyecto: Este proyecto tuvo como objetivo poner en práctica las diferentes etapas del análisis de datos para las empresas del S&P500. El análisi contempla desde la extracción de datos, análisis estadistico, visualización, hasta análisis de volatilidad. 
o Requisitos: `pandas`, `sqlalchemy`, `pyodbc`, `scikit-learn`, - Power BI Desktop, SQL Server.
o Estructura del proyecto: 
- `data/`: Contiene los archivos CSV con los datos de las empresas y perfiles.
- `scripts/`: Contiene los scripts Python para las diferentes fases del
proyecto.
- `dashboards/`: Contiene el archivo .pbix de Power BI.
- `README.md`: Documento explicativo del proyecto.
o Instrucciones de instalación y uso: Pasos detallados para instalar
las dependencias, configurar el entorno y ejecutar el proyecto.
o Descripción de cada fase del proyecto:
▪ Fase 1: Extracción de datos de las empresas del S&P 500.
▪ Fase 2: Análisis estadístico descriptivo e inferencial.
▪ Fase 3: Almacenamiento de datos en SQL Server.
▪ Fase 4: Creación del dashboard en Power BI.
▪ Fase 5: Clusterización de las acciones según la volatilidad.
▪ Fase 6: Publicación en GitHub.



## Instrucciones de Instalación y Uso
1. Clona este repositorio:

git clone https://github.com/tuusuario/sp500-analysis.git
cd sp500-analysis
2. Instala las dependencias necesarias:
pip install -r requirements.txt
3. Configura la conexión a SQL Server en los scripts de las fases
correspondientes.
4. Ejecuta los scripts en orden para realizar el análisis completo.
Fases del Proyecto
Fase 1: Extracción de Datos
• Obtención de datos de empresas del S&P 500 desde Wikipedia.
• Descarga de los precios de cotización del último año.
Fase 2: Análisis Estadístico
• Análisis descriptivo e inferencial de los precios de las acciones.
Fase 3: Almacenamiento en SQL Server
• Carga de los datos limpios en una base de datos SQL Server.
Fase 4: Dashboard en Power BI
• Creación de un dashboard interactivo con KPIs, tooltips y bookmarks.
Fase 5: Clusterización de las Acciones
• Agrupamiento de las acciones en clusters según indicadores de volatilidad.
Fase 6: Publicación en GitHub
• Subida del proyecto al repositorio de GitHub y documentación en este
archivo README.md.
