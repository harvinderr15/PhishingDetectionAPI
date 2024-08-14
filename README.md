# PhishingDetectionAPI


## Overview

This project focuses on detecting phishing websites using machine learning models. It involves data preprocessing, model training, evaluation, and deployment of a phishing detection model as a web service. The model is deployed using Flask and Docker, and its functionality is verified using Postman.

## Repository Structure

```
PhishingDetectionAPI/
│
├── test/
│   ├── legitimate POST Request.txt               # POST Request URL with features of Legitimate input
│   ├── legitimate POST Request.txt               # POST Request URL with features of Phishing input
│   └── Docker Pull and run command.txt           # Commands to access and test docker image 
│
├── Testing models/
│   ├── PhishingDetectionModels.ipynb             # Jupyter notebook for model evaluation, analysis and saving best model
│   ├── Dataset_phishing.csv                      # Kaggle Dataset for training and testing model
│   └── xgb_model.pkl                             # Pickled XGBoost model
│
├── xgb_model.pkl                                 # Pickled XGBoost model
├── Dockerfile                                    # Dockerfile for containerizing the Flask application
├── requirements.txt                              # Python dependencies
├── README.md                                     # This README file
└── .gitignore                                    # Git ignore file to exclude unnecessary files
```

## Getting Started

To get started with the project, follow the instructions below:

### Prerequisites

- Python 3.x
- Docker (for containerization)
- Postman (for testing the API)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/harvinderr15/PhishingDetectionAPI.git
   cd PhishingDetectionAPI
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Jupyter Notebook

1. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Open the `Testing Models/PhishingDetectionModelsn.ipynb` file to view and run the notebook for model evaluation. The trained model will be saved as `xgb_model.pkl` in the same directory.

### Deploying the Flask API

1. Build the Docker image:

   ```bash
   docker build -t phishing-detection-api .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 5000:5000 phishing-detection-api
   ```

3. The Flask API will be available at `http://localhost:5000/predict`.

OR 

1. Pull Docker repository
   ```bash
   docker pull kanikaan/phishing-detection-api:1.0
   ```
2. Run Docker Container
   ```bash
   docker run -p 5000:5000 kanikaan/phishing-detection-api:1.0
   ```



2. Here are examples of JSON data for both legitimate and phishing websites:

   **Legitimate Website Example:**
   ```json
   {
       "url": "https://www.example.com",
       "length_url": 19,
       "length_hostname": 15,
       "ip": 0,
       "nb_dots": 2,
       "nb_hyphens": 0,
       "nb_at": 0,
       "nb_qm": 0,
       "nb_and": 0,
       "nb_or": 0,
       "nb_eq": 0,
       "nb_underscore": 0,
       "nb_tilde": 0,
       "nb_percent": 0,
       "nb_slash": 1,
       "nb_star": 0,
       "nb_colon": 0,
       "nb_comma": 0,
       "nb_semicolumn": 0,
       "nb_dollar": 0,
       "nb_space": 0,
       "nb_www": 1,
       "nb_com": 1,
       "nb_dslash": 1,
       "http_in_path": 0,
       "https_token": 1,
       "ratio_digits_url": 0.0,
       "ratio_digits_host": 0.0,
       "punycode": 0,
       "port": 0,
       "tld_in_path": 0,
       "tld_in_subdomain": 0,
       "abnormal_subdomain": 0,
       "nb_subdomains": 1,
       "prefix_suffix": 0,
       "random_domain": 0,
       "shortening_service": 0,
       "path_extension": 0,
       "nb_redirection": 0,
       "nb_external_redirection": 0,
       "length_words_raw": 15,
       "char_repeat": 0,
       "shortest_words_raw": 3,
       "shortest_word_host": 3,
       "shortest_word_path": 3,
       "longest_words_raw": 10,
       "longest_word_host": 10,
       "longest_word_path": 10,
       "avg_words_raw": 6.0,
       "avg_word_host": 6.0,
       "avg_word_path": 6.0,
       "phish_hints": 0,
       "domain_in_brand": 1,
       "brand_in_subdomain": 0,
       "brand_in_path": 0,
       "suspecious_tld": 0,
       "statistical_report": 0,
       "nb_hyperlinks": 5,
       "ratio_intHyperlinks": 0.5,
       "ratio_extHyperlinks": 0.5,
       "ratio_nullHyperlinks": 0.0,
       "nb_extCSS": 0,
       "ratio_intRedirection": 0.0,
       "ratio_extRedirection": 0.0,
       "ratio_intErrors": 0.0,
       "ratio_extErrors": 0.0,
       "login_form": 0,
       "external_favicon": 0,
       "links_in_tags": 0,
       "submit_email": 0,
       "ratio_intMedia": 0.0,
       "ratio_extMedia": 0.0,
       "sfh": 1,
       "iframe": 0,
       "popup_window": 0,
       "safe_anchor": 1,
       "onmouseover": 0,
       "right_clic": 0,
       "empty_title": 0,
       "domain_in_title": 1,
       "domain_with_copyright": 0,
       "whois_registered_domain": 1,
       "domain_registration_length": 10,
       "domain_age": 5,
       "web_traffic": 1,
       "dns_record": 1,
       "google_index": 1,
       "page_rank": 3
   }
   ```

   **Phishing Website Example:**
   ```json
   {
       "url": "http://phishing-example.com",
       "length_url": 23,
       "length_hostname": 20,
       "ip": 1,
       "nb_dots": 2,
       "nb_hyphens": 1,
       "nb_at": 0,
       "nb_qm": 0,
       "nb_and": 0,
       "nb_or": 0,
       "nb_eq": 0,
       "nb_underscore": 0,
       "nb_tilde": 0,
       "nb_percent": 0,
       "nb_slash": 1,
       "nb_star": 0,
       "nb_colon": 0,
       "nb_comma": 0,
       "nb_semicolumn": 0,
       "nb_dollar": 0,
       "nb_space": 0,
       "nb_www": 0,
       "nb_com": 1,
       "nb_dslash": 1,
       "http_in_path": 1,
       "https_token": 0,
       "ratio_digits_url": 0.1,
       "ratio_digits_host": 0.1,
       "punycode": 1,
       "port": 0,
       "tld_in_path": 1,
       "tld_in_subdomain": 1,
       "abnormal_subdomain": 1,
       "nb_subdomains": 2,
       "prefix_suffix": 1,
       "random_domain": 1,
       "shortening_service": 1,
       "path_extension": 1,
       "nb_redirection": 2,
       "nb_external_redirection": 1,
       "length_words_raw": 10,
       "char_repeat": 1,
       "shortest_words_raw": 4,
       "shortest_word_host": 4,
       "shortest_word_path": 4,
       "longest_words_raw": 15,
       "longest_word_host": 15,
       "longest_word_path": 15,
       "avg_words_raw": 8.0,
       "avg_word_host": 8.0,
       "avg_word_path": 8.0,
       "phish_hints": 1,
       "domain_in_brand": 0,
       "brand_in_subdomain": 1,
       "brand_in_path": 1,
       "suspecious_tld": 1,
       "statistical_report": 1,
       "nb_hyperlinks": 10,
       "ratio_intHyperlinks": 0.2,
       "ratio_extHyperlinks": 0.8,
       "ratio_nullHyperlinks": 0.0,
       "nb_extCSS": 1,
       "ratio_intRedirection": 0.5,
       "ratio_extRedirection": 0.5,
       "ratio_intErrors": 0.3,
       "ratio_extErrors": 0.7,
       "login_form": 1,
       "external_favicon": 1,
       "links_in_tags": 1,
       "submit_email": 1,
       "ratio_intMedia": 0.2,
       "ratio_extMedia": 0.8,
       "sfh": 0,
       "iframe": 1,
       "popup_window": 1,
       "safe_anchor": 0,
       "onmouseover": 1,
       "right_clic": 1,
       "empty_title": 1,
       "domain_in_title": 0,
       "domain_with_copyright": 1,
       "whois_registered_domain": 0,
       "domain_registration_length": 1,
       "domain_age": 1,
       "web_traffic": 0,
       "dns_record": 0,
       "google_index": 0,
       "page_rank": 0
   }
   ```

