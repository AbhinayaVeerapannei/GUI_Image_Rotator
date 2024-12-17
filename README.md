# Drug Data Scraping from Medicare

### Project Overview
This project automates web scraping of drug data from a Medicare website. Using Selenium with the Firefox web driver, the script scrapes over 8000+ drugs and extracts details such as:
- **Drug_Name**
- **Generic_Name**
- **Dosage**
- **Dosage_ndc**
- **Package**
- **Package_ndc**
- **Frequency**
- **Quantity**

The scraped data is stored in a CSV file for reference.

---

### How the Code Works
The script extracts data for drugs listed alphabetically (A-Z) on the target website.

1. **Customizable Extraction:**
   ```python
   extractor.run(start_letter='A', end_letter='Z', start_index=249)
   ```
   - `start_letter` - Set the starting alphabet to scrape drugs (e.g., 'A', 'J', etc.).
   - `end_letter` - Set the ending alphabet.
   - `start_index` - Begin scraping from a specific drug number within the letter.

   **Example:**
   - To scrape drugs starting from letter **J**:
     ```python
     extractor.run(start_letter='J', end_letter='Z', start_index=1)
     ```
   - If a letter contains 250 drugs and you set `start_index=100`, it will scrape from the 100th drug.

   **Important Note:** 
   - Ensure the `start_index` matches a valid drug number within the letter. If the index exceeds the total count (e.g., 300 for 250 drugs), the script skips to the next letter.
   - You can check the number of drugs available under each letter directly on the website.

2. **Appending Data:**
   - Scraped drug data is appended **line by line** into a CSV file.
   - If the script stops unexpectedly, the previously scraped data is saved. Simply follow these steps to continue:
     - Check the terminal logs to find the **letter** and **drug index** where it stopped.
     - Save the current CSV to a **new file** to prevent overwriting data.
     - Restart the script with updated parameters for `start_letter` and `start_index`.

   **Example:**
   ```python
   extractor.run(start_letter='B', end_letter='Z', start_index=150)
   ```

3. **Internet Connectivity:**
   - Ensure a **stable and fast internet connection** during execution.
   - If the connection drops or slows, the script may:
     - Skip drugs and move forward.
     - Stop execution entirely.
   - In such cases:
     - Verify your network connection.
     - Customize the script using the steps above to resume from where it stopped.

---

### Prerequisites
1. Python 3.x
2. Selenium
3. Firefox browser
4. Stable internet connection

---

### Requirements
- Install dependencies using pip:
   ```bash
   pip install selenium
   ```

- Make sure **Firefox** is installed (no need to install Gecko drivers).

---

### How to Run the Code
1. Clone the repository.
   ```bash
   git clone <repo-link>
   cd <repo-folder>
   ```
2. Install required packages:
   ```bash
   pip install selenium
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Customize the scraping process as needed:
   ```python
   extractor.run(start_letter='A', end_letter='Z', start_index=1)
   ```

---

### Important Points
- **Customizable Parameters:** Easily adjust `start_letter`, `end_letter`, and `start_index` to target specific drugs.
- **Resume on Failure:** The script appends data to the CSV, allowing you to restart from where it stopped.
- **Manual Backup:** Always save scraped data in a separate CSV file before restarting the script.
- **Network Dependency:** A fast, stable internet connection is crucial to avoid script interruptions.

---

### Output
The final output will be stored in a CSV file with 8 columns: `Drug_Name`, `Generic_Name`, `Dosage`, `Dosage_ndc`, `Package`, `Package_ndc`, `Frequency`, `Quantity`.

---

### References
- Sample scraped data: [drugs_data.csv](path/to/drugs_data.csv)
