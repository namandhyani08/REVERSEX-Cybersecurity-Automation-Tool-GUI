# REVERSEX-Cybersecurity-Automation-Tool-GUI
Streamlit GUI demonstrating dynamic payload-string generation, sidebar config, and subprocess integration — for authorized security testing/lab use only.

🛡️ REVERSEX — Interactive GUI Wrapper for CLI Security Tools

A Streamlit-based graphical front-end that demonstrates how to wrap command-line security tooling (like msfvenom and standard networking one-liners) in an interactive, configurable dashboard.

🧩 What This Project Demonstrates
🔄 Dynamic form-driven code generation — user inputs (host/port) feed into template strings that update live as selections change
🎛️ Sidebar-based configuration pattern — persistent settings panel separate from the main content area, a common pattern for “studio” or “generator” style tools
📊 Metric dashboards — st.metric used to surface current config state at a glance
⚙️ Subprocess integration — shelling out to external binaries (msfvenom) from a Python web app, capturing stdout/stderr, and surfacing results/errors back to the UI
🧭 Conditional multi-engine UI — a single selectbox branching into entirely different generator “engines” with their own input schemas
🛠️ Tech Stack
🐍 Python 3
🎨 Streamlit (UI framework)
🌑 Custom CSS injection for dark/cyberpunk theming

🚀 Setup
bash
pip install streamlit --break-system-packages

streamlit run app.py

⚠️ Important

This code shells out to msfvenom and generates reverse shell connection strings. Anyone using or adapting this must only do so in contexts they’re authorized to test (their own lab, systems they own, or engagements with explicit written permission). Repos that publish working exploit/payload generators without this framing are frequently taken down or flagged by GitHub and hosting providers — so if you publish this, lead with your authorization scope clearly, and consider whether the actual generator logic belongs in a private/educational-only repo versus the public one showcasing the UI pattern.
