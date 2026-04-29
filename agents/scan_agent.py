import requests

def scan_target(urls):
    findings = []
    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            if "X-Frame-Options" not in r.headers:
                findings.append({"url": url, "issue": "Missing X-Frame-Options", "severity": "Medium"})
        except:
            continue
    return findings
