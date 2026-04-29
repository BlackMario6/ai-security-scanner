                    ┌──────────────────────┐
                    │      User Input       │
                    │   target website URL  │
                    └──────────┬───────────┘
                               │
                               ▼
               ┌──────────────────────────┐
               │  Planner / Orchestrator  │
               └──────────┬───────────────┘
                          │
      ┌───────────────────┼───────────────────┐
      │                   │                   │
      ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Asset Agent  │   │ Scan Agent   │   │ Memory Agent │
│ discover URLs│   │ run checks   │   │ store history│
└──────┬───────┘   └──────┬───────┘   └──────────────┘
       │                  │
       ▼                  ▼
┌───────────────────────────────────────┐
│ Vulnerability Analysis / RAG Engine   │
│ match findings with vuln knowledge    │
└──────────────────┬────────────────────┘
                   │
                   ▼
         ┌──────────────────┐
         │ Report Generator │
         └────────┬─────────┘
                  │
                  ▼
        security_report.md / json
