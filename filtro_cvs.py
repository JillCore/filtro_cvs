import os
import pdfplumber
import ollama
import pandas as pd

# 1. Configuración de la carpeta y perfil buscado
CARPETA_CVS = 'cvs_recibidos'
PERFIL_BUSCADO = "Estratega digital experto en SEO, Google Ads y análisis de métricas."

def extraer_texto_pdf(ruta_pdf):
    texto_completo = ""
    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            for pagina in pdf.pages:
                texto_completo += pagina.extract_text() + "\n"
    except Exception as e:
        print(f"Error al leer {ruta_pdf}: {e}")
    return texto_completo

def evaluar_candidato_ia(texto_cv):
    prompt = f"""
    Eres un asistente de Recursos Humanos haciendo un filtrado inicial rápido. 
    Tu objetivo BÁSICO es buscar este perfil: '{PERFIL_BUSCADO}'
    
    REGLA ESTRICTA: Si el currículum menciona explícitamente la experiencia o las tecnologías de ese perfil, debes marcarlo como Apto: Sí. NO inventes requisitos técnicos avanzados ni exijas frameworks específicos que no estén literalmente escritos en el perfil buscado.
    
    Responde ÚNICAMENTE en el siguiente formato exacto:
    Nombre: [Nombre del candidato o 'No especificado']
    Apto: [Sí/No]
    Razón: [Una sola oración justificando la decisión basándote solo en el texto]
    
    Currículum:
    {texto_cv}
    """
    
    respuesta = ollama.chat(model='phi3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return respuesta['message']['content']

def procesar_curriculums():
    resultados = []
    
    print(f"Iniciando filtrado de CVs buscando el perfil: {PERFIL_BUSCADO}\n")
    
    for archivo in os.listdir(CARPETA_CVS):
        if archivo.endswith('.pdf'):
            ruta_completa = os.path.join(CARPETA_CVS, archivo)
            print(f"Analizando: {archivo}...")
            
            # Extraer texto del PDF
            texto_cv = extraer_texto_pdf(ruta_completa)
            
            # Pasar el texto a la IA Local
            evaluacion = evaluar_candidato_ia(texto_cv)
            
            # Guardar resultados en bruto (puedes estructurarlo más adelante si lo deseas)
            resultados.append({
                "Archivo": archivo,
                "Evaluación de IA": evaluacion
            })
            
    # Exportar el reporte a Excel
    df = pd.DataFrame(resultados)
    df.to_excel('Reporte_Filtrado_HR.xlsx', index=False)
    print("\n¡Proceso finalizado! Reporte guardado en 'Reporte_Filtrado_HR.xlsx'")

if __name__ == "__main__":
    procesar_curriculums()
