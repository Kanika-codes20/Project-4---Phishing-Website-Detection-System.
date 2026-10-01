import re
from urllib.parse import urlparse

MEDIUM_THRESHOLD = 2

def analyze_url(url):
    risk_score = 0
    reasons = []

    #Suspicious character.
    if "@" in url:
        risk_score += 1
        reasons.append("URL contains an @ symbol.")

    #URL length.
    if len(url) > 75:
        risk_score += 1
        reasons.append("URL exceeds length limit.")

    #IP address
    if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", url):
        risk_score += 1
        reasons.append("URL contains IP address.")

    # Hyphen.
    if "-" in url:
        risk_score += 1
        reasons.append("URL contains a hyphen.")

    #Hostname.
    suspicious_words = ["login", "verify", "account", "update"]

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    if hostname:
        for word in suspicious_words:
            if word in hostname.lower():
                risk_score += 1
                reasons.append("The Hostname contains security-related word: " + word)

    return risk_score, reasons

print("\n=====Phishing website detection system=====\n")
url = input("Enter the website URL: ").strip()
risk_score, reasons = analyze_url(url)

if risk_score == 0:
    risk_level = "LOW"

elif risk_score <= MEDIUM_THRESHOLD:
    risk_level = "MEDIUM"

else:
    risk_level = "HIGH"

print("\nRisk score:", risk_score)
print("Risk level:", risk_level)

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("- " + reason)
else:
    print("\nNo suspicious indicators detected.")

print("\nAnalysis complete.")








