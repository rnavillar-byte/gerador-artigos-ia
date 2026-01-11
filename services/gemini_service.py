
import requests

def gerar_texto_gemini(prompt, api_key):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    data = {"contents":[{"parts":[{"text": prompt}]}]}
    response = requests.post(url, headers=headers, params=params, json=data, timeout=60)
    response.raise_for_status()
    result = response.json()
    return result["candidates"][0]["content"]["parts"][0]["text"]
