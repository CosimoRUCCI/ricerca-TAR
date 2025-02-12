"""
MIT License

Copyright (c) 2025 CosimoRUCCI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software...
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv  # Importa il modulo csv

# Configura il driver di Selenium (ad esempio, Chrome)
driver = webdriver.Chrome()

# Lista per memorizzare i numeri progressivi trovati
numeri_trovati = []

# Ciclo per numeri progressivi da 1 a 2050
for numero_progressivo in range(1, 2050):
    try:
        print(f"\n--- Inizio ricerca per numero: {numero_progressivo} ---")

        # Vai alla pagina dei ricorsi TAR Roma
        driver.get("https://www.giustizia-amministrativa.it/ricorsi-tar-roma")

        # Attendi che la pagina si carichi completamente
        wait = WebDriverWait(driver, 15)  # Aumenta il timeout

        # Trova l'iframe principale e passa al suo contesto
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)

        # Attesa di 5 secondi prima di inserire i dati (anno e numero)
        time.sleep(5)  # Attesa per il caricamento dei campi di input

        # Trova i campi di ricerca
        anno_field = wait.until(EC.presence_of_element_located((By.NAME, "anno")))  # Campo per l'anno
        numero_field = wait.until(EC.presence_of_element_located((By.NAME, "numero")))  # Campo per il numero progressivo

        # Pulisci e inserisci l'anno
        anno_field.send_keys(Keys.CONTROL + "a")  # Seleziona tutto il testo nel campo
        anno_field.send_keys(Keys.DELETE)  # Cancella il contenuto del campo
        anno_field.send_keys("2025")  # Inserisci l'anno desiderato
        time.sleep(1)  # Attesa per assicurarsi che l'anno sia stato inserito

        # Pulisci e inserisci il numero progressivo
        numero_field.send_keys(Keys.CONTROL + "a")  # Seleziona tutto il testo nel campo
        numero_field.send_keys(Keys.DELETE)  # Cancella il contenuto del campo
        numero_field.send_keys(str(numero_progressivo))  # Inserisci il numero progressivo
        time.sleep(1)  # Attesa per assicurarsi che il numero sia stato inserito

        # Clicca il pulsante di ricerca (usando JavaScript per sicurezza)
        try:
            search_button = wait.until(EC.element_to_be_clickable((By.NAME, "search")))  # Pulsante di ricerca
            driver.execute_script("arguments[0].click();", search_button)  # Clicca via JavaScript
        except:
            # Premere Invio immediatamente dopo l'inserimento dei valori
            numero_field.send_keys(Keys.ENTER)  # Fallback: tasto Invio

        # Attendi il caricamento dei risultati
        time.sleep(2)  # Attesa aggiuntiva per risultati dinamici (aumenta se necessario)

        # Verifica se il testo è presente (con regex flessibile)
        body_text = driver.find_element(By.TAG_NAME, "body").text
        if re.search(r"STRINGA\s*CERCATA", body_text, re.IGNORECASE):
            print(f"✅ Trovato! Numero: {numero_progressivo}")
            numeri_trovati.append(numero_progressivo)
        else:
            print(f"❌ Testo non trovato per numero: {numero_progressivo}")

        # Ritorno al ciclo iniziale subito dopo la verifica della stringa
        driver.switch_to.default_content()  # Ritorna al contesto principale
        time.sleep(1)  # Attesa per il caricamento della pagina principale
        continue  # Ritorna al ciclo iniziale

    except Exception as e:
        print(f"⚠️ Errore durante la ricerca del numero {numero_progressivo}: {str(e)}")
        # Ripristina il contesto in caso di errore
        driver.switch_to.default_content()
        time.sleep(1)  # Attesa per il caricamento della pagina principale

# Chiudi il browser alla fine
driver.quit()

# Salva i risultati in un file CSV
with open("risultati.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Scrivi l'intestazione del file CSV
    writer.writerow(["Numero Progressivo", "Risultato"])
    # Scrivi i risultati nel file CSV
    for numero in numeri_trovati:
        writer.writerow([numero, "Trovato"])

# Stampa i risultati finali
print("\n--- Risultati Finali ---")
print("Numeri con testo 'STRINGA CERCATA:", numeri_trovati)
print("Risultati salvati nel file 'risultati.csv'")