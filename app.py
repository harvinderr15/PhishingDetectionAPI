import pickle
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    
    # Ensure that all features are present in the DataFrame
    features = [
        'url', 'length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens', 'nb_at',
        'nb_qm', 'nb_and', 'nb_or', 'nb_eq', 'nb_underscore', 'nb_tilde', 'nb_percent',
        'nb_slash', 'nb_star', 'nb_colon', 'nb_comma', 'nb_semicolumn', 'nb_dollar',
        'nb_space', 'nb_www', 'nb_com', 'nb_dslash', 'http_in_path', 'https_token',
        'ratio_digits_url', 'ratio_digits_host', 'punycode', 'port', 'tld_in_path',
        'tld_in_subdomain', 'abnormal_subdomain', 'nb_subdomains', 'prefix_suffix',
        'random_domain', 'shortening_service', 'path_extension', 'nb_redirection',
        'nb_external_redirection', 'length_words_raw', 'char_repeat', 'shortest_words_raw',
        'shortest_word_host', 'shortest_word_path', 'longest_words_raw', 'longest_word_host',
        'longest_word_path', 'avg_words_raw', 'avg_word_host', 'avg_word_path',
        'phish_hints', 'domain_in_brand', 'brand_in_subdomain', 'brand_in_path',
        'suspecious_tld', 'statistical_report', 'nb_hyperlinks', 'ratio_intHyperlinks',
        'ratio_extHyperlinks', 'ratio_nullHyperlinks', 'nb_extCSS', 'ratio_intRedirection',
        'ratio_extRedirection', 'ratio_intErrors', 'ratio_extErrors', 'login_form',
        'external_favicon', 'links_in_tags', 'submit_email', 'ratio_intMedia', 'ratio_extMedia',
        'sfh', 'iframe', 'popup_window', 'safe_anchor', 'onmouseover', 'right_clic',
        'empty_title', 'domain_in_title', 'domain_with_copyright', 'whois_registered_domain',
        'domain_registration_length', 'domain_age', 'web_traffic', 'dns_record',
        'google_index', 'page_rank'
    ]
    
    # Fill missing features with default values (if any)
    for feature in features:
        if feature not in df:
            df[feature] = 0
    
    # Convert necessary columns to numeric types
    df[features] = df[features].apply(pd.to_numeric, errors='coerce')
    
    # Make prediction
    prediction = model.predict(df)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
