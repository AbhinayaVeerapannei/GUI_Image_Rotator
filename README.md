# Drug_Data Scraping Automation Project

This project automates the process of web scraping over **8000+ drugs** with details like **Drug Name**, **Generic Name**, **Dosage**, **Package**, and other attributes from a **Medicare website** using **Selenium** and **Firefox WebDriver**.

---
## **Project Overview**
- **Purpose**: Automate drug data scraping to collect and store information in a CSV file.
- **Language**: Python
- **Automation Tool**: Selenium (WebDriver)
- **Output**: CSV file containing 8000+ drugs with 8 columns:
  - `Drug_Name`
  - `Generic_Name`
  - `Dosage`
  - `Dosage_ndc`
  - `Package`
  - `Package_ndc`
  - `Frequency`
  - `Quantity`

---
## **Code Process**
1. **Setup**:
   - Uses Selenium WebDriver with Firefox for automated scraping.
   - No need to install GeckoDriver separately; WebDriver integration handles it.
2. **Accessing the Website**:
   - The script navigates to the Medicare website.
   - Note: Sometimes the website may not be accessible due to server issues.
3. **Data Scraping**:
   - Iterates through drug records on the website.
   - Extracts relevant information such as name, dosage, and package details.
4. **Data Storage**:
   - All scraped data is stored in a CSV file for future use.

---
## **How to Run the Code**

### **Requirements**
- Python (3.7+ recommended)
- Selenium package
- Firefox browser
- CSV library (built-in with Python)

### **Steps to Run**
1. **Clone the Repository**
   ```bash
   !git clone <repository-link>
   cd <repository-folder>
   ```
2. **Install Required Libraries**
   Run the following command to install Selenium:
   ```bash
   pip install selenium
   ```
3. **Run the Script**
   Execute the Python script:
   ```bash
   python drug_scraper.py
   ```
4. **Output**
   - A CSV file (e.g., `scraped_drug_data.csv`) will be created with all the scraped drug details.

---
## **Important Notes**
- Ensure that the **Firefox browser** is installed and up-to-date.
- If the Medicare website is inaccessible, re-run the script after some time.
- The scraping process may take a few hours depending on the total number of records.

---
## **Output File**
- The project generates a CSV file with the scraped drug details.
- **Sample File**: `scraped_drug_data.csv` (attached for reference).

---
## **References**
- Selenium Documentation: [https://selenium.dev/](https://selenium.dev/)
- Python Official Documentation: [https://python.org](https://python.org)

---
