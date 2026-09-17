import numpy as np

def get_clean_offer_url(url: str) -> str:
    url_str = str(url).strip()
    return url_str[: url_str.find("-ID")] if "-ID" in url_str else url_str

def calculate_spread(group):
    return np.std(group['UMAP 1']) + np.std(group['UMAP 2'])