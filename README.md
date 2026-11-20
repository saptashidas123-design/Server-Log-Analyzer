# Automated Server Log Analyzer 🛠️

A Python-based log parsing and troubleshooting utility designed to scan server logs, categorize log severity levels (`INFO`, `WARNING`, `ERROR`, `CRITICAL`), and isolate actionable system failures.

## Features
- Parses large server log files in linear time $O(N)$
- Counts event frequencies by severity level
- Extracts and highlights `ERROR` and `CRITICAL` incidents with timestamps for rapid root-cause analysis

## How to Run
```bash
python3 analyzer.py
=== SERVER LOG SUMMARY ===
INFO: 3
WARNING: 2
ERROR: 3
CRITICAL: 1

=== ACTIONABLE ALERTS (ERROR & CRITICAL) ===
[2026-11-20 10:05:10] ERROR: Database connection timeout on port 5432
[2026-11-20 10:08:01] CRITICAL: Disk space critically low on /dev/sda1 (98% full)
[2026-11-20 10:10:15] ERROR: Failed to authenticate token for IP 192.168.1.45
[2026-11-20 10:14:00] ERROR: Database connection timeout on port 5432
