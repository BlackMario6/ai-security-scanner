from agents.asset_agent import discover_assets
from agents.scan_agent import scan_target
from agents.report_agent import generate_report

def run(target_url):
    print(f"[+] Target: {target_url}")
    assets = discover_assets(target_url)
    findings = scan_target(assets)
    report = generate_report(target_url, findings)

    os.makedirs("reports/output", exist_ok=True)
    with open("reports/output/security_report.md", "w") as f:
        f.write(report)

    print("[+] Report generated!")

if __name__ == "__main__":
    run("https://example.com")
