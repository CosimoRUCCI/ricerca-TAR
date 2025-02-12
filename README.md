```markdown
# Ricorsi TAR Roma - Web Scraper

Uno script Python che utilizza Selenium per cercare automaticamente numeri progressivi sul portale dei ricorsi del TAR Roma e verificare la presenza di un testo specifico nei risultati.

## Requisiti

- **Python 3.x**: Installato sul tuo sistema.
- **Selenium**: Libreria per l'automazione del browser.
  ```bash
  pip install selenium
  ```
- **ChromeDriver**: Scarica la versione compatibile con il tuo browser Chrome:
  - [ChromeDriver Download](https://sites.google.com/chromium.org/driver/)
  - Assicurati che il file `chromedriver` sia nel tuo PATH o nella stessa directory dello script.

## Installazione

1. Clona il repository o scarica il file `ricorsi.py`.
2. Installa le dipendenze:
   ```bash
   pip install selenium
   ```
3. Scarica ChromeDriver e posizionalo nella cartella del progetto o aggiungi il suo percorso al sistema.

## Utilizzo

1. Modifica i parametri nello script (se necessario):
   - **Intervallo numeri progressivi**: Modifica `range(2040, 2080)` nella riga `for numero_progressivo in range(...)`.
   - **Anno di ricerca**: Cambia `"2025"` nel campo `anno_field.send_keys("2025")`.
2. Esegui lo script:
   ```bash
   python ricorsi.py
   ```
3. I risultati verranno salvati in `risultati.csv`.

## Configurazione Avanzata

- **Percorso personalizzato per ChromeDriver**:
  - Sostituisci `driver = webdriver.Chrome()` con:
    ```python
    driver = webdriver.Chrome(executable_path='/percorso/chromedriver')
    ```

## Note Importanti

- **Delay e Timeout**: Lo script include `time.sleep()` per attendere il caricamento degli elementi. Potrebbe essere necessario regolare questi valori in base alla velocità della connessione.
- **Struttura del sito**: Se il sito web del TAR Roma cambia la sua interfaccia, lo script potrebbe richiedere aggiornamenti.
- **Uso Etico**: Evita di eseguire troppe richieste in breve tempo per non sovraccaricare il server.

## Risultati

I numeri progressivi con il "TESTO DA CERCARE" verranno salvati nel file CSV e stampati a schermo.
```
