# filtro_cvs
# 🤖 Analizador y Filtro de Currículums con IA Local

¡Bienvenido al repositorio de **Coding con C**! Este script automatiza el proceso de Recursos Humanos evaluando cientos de currículums en formato PDF utilizando Inteligencia Artificial Local (Microsoft Phi-3) a través de Ollama. 

Al ejecutarse 100% de forma local, **garantiza la privacidad absoluta** de los datos sensibles de los candidatos.

⚙️ Cómo usarlo
Clona o descarga este repositorio.

Asegúrate de tener una carpeta llamada cvs_recibidos en la misma ruta que el script (el código la creará automáticamente si no existe).

Coloca todos los currículums en formato .pdf dentro de esa carpeta.

Modifica la variable PERFIL_BUSCADO en el script con las habilidades exactas que requiere tu vacante.

Ejecuta el script:

Bash
python filtro_cvs.py
Al finalizar, se generará un archivo llamado Reporte_Filtrado_HR.xlsx con la evaluación estructurada de cada candidato.

📺 Mira el Tutorial Completo
Si quieres ver la explicación paso a paso de cómo se construyó este código y cómo solucionar posibles errores, mira el video en mi canal de YouTube: 👉 https://www.youtube.com/watch?v=rw0CmUR9r2A

💬 Únete a la Comunidad
Si tienes dudas o quieres debatir sobre automatización, únete a nuestra comunidad: 👉 https://t.me/+aRGkH9vb369mM2Ex

## 🚀 Requisitos Previos

Para que este script funcione, necesitas tener instalados:

1. **Python 3.x**
2. **Ollama**: Descárgalo desde [ollama.com](https://ollama.com/).
3. **Modelo Phi-3**: Abre tu terminal y ejecuta: `ollama run phi3`

## 📦 Instalación de Librerías

Abre tu terminal y ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install ollama pdfplumber pandas openpyxl


