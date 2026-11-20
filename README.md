# REVERSEX-Cybersecurity-Automation-Tool-GUI
Streamlit GUI demonstrating dynamic payload-string generation, sidebar config, and subprocess integration — for authorized security testing/lab use only.

# 🛡️ REVERSEX

A Streamlit-based graphical front-end in Python that demonstrates how to wrap command-line security utilities (such as `msfvenom` and standard connection strings) in an interactive, configurable dashboard.

## 🧩 What This Project Demonstrates

* **Dynamic Form-Driven Generation:** Sidebar `LHOST` and `LPORT` inputs feed into payload templates and `msfvenom` commands.
* **Sidebar Configuration Pattern:** Keeps connection settings persistent in a sidebar while keeping the main workspace focused on generation.
* **Metric Dashboards:** Uses `st.metric` cards to surface active configuration values and framework status at a glance.
* **Subprocess Integration:** Executes `msfvenom` via `subprocess.run`, captures `stdout`/`stderr`, and generates a companion `handler.rc` file.
* **Conditional Multi-Engine UI:** Branches from a single selector into either standard connection strings or `msfvenom` platform/format options.

## 🛠️ Tech Stack

* **Python 3**
* **Streamlit**
* **Custom CSS** (dark/cyberpunk styling and compact spacing)

## 🚀 Setup

```bash
https://github.com/namandhyani08/REVERSEX-Cybersecurity-Automation-Tool-GUI.git
cd revx.py
pip install streamlit --break-system-packages
streamlit run revx.py
