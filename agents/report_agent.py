def generate_report(target, findings):
    report = f"# Security Report for {target}\n\n"
    for f in findings:
        report += f"- {f['issue']} ({f['severity']}) -> {f['url']}\n"
    return report
