<div align="center">

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=FF3621&height=180&section=header&text=VirtueAudit&fontSize=72&fontColor=fff&animation=fadeIn&fontAlignY=45" width="100%"/>

# 🤖 VirtueAudit: AI-Automated Medical Infrastructure Verification & Risk Assessment

[![Stars](https://img.shields.io/github/stars/OmSinha07/VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment?style=for-the-badge&color=FF3621&labelColor=0d1117)](https://github.com/OmSinha07/VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment/stargazers)
[![Forks](https://img.shields.io/github/forks/OmSinha07/VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment?style=for-the-badge&color=FF3621&labelColor=0d1117)](https://github.com/OmSinha07/VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment/network)
[![Issues](https://img.shields.io/github/issues/OmSinha07/VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment?style=for-the-badge&color=FF3621&labelColor=0d1117)](https://github.com/OmSinha07/VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment/issues)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&labelColor=0d1117)](LICENSE)

<br/>

[![Databricks](https://img.shields.io/badge/🔴_LIVE_ON_DATABRICKS_APPS-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://virtue-audit-dashboard-7474646237305242.aws.databricksapps.com/)
&nbsp;&nbsp;
[![Streamlit](https://img.shields.io/badge/🟢_LIVE_ON_STREAMLIT_CLOUD-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ghana-medical-audit.streamlit.app/)

<br/>

> **An end-to-end AI-powered auditing pipeline for automated medical infrastructure verification and risk assessment.**
> *Built for the Accenture × Databricks Hackathon*

</div>

---

## 📖 Overview

**VirtueAudit** automates the verification and risk assessment of medical infrastructure by processing large-scale facility data from the **Virtue Foundation (Ghana)**. It leverages **Llama 3.1 via Groq** for sophisticated natural language understanding and **Databricks** for scalable data processing — enabling automatic extraction of clinical capabilities and proactive flagging of infrastructure risks.

The project runs in two modes:
- 🔴 **Full Apache Spark pipeline** on Databricks for production scale
- 🟢 **Pandas-based local fallback** for development

Both modes feed the same interactive **Streamlit dashboard**, deployed on Databricks Apps and Streamlit Cloud.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **AI Risk Assessment** | Llama 3.1 via Groq analyzes descriptions and flags infrastructure risks |
| 🏥 **Capability Extraction** | Auto-extracts and categorizes clinical services per facility |
| ⚡ **Dual Execution Engine** | Apache Spark on Databricks + automatic Pandas fallback |
| 📊 **Interactive Dashboard** | Streamlit app with KPIs, Plotly charts, and per-facility case views |
| 📄 **Structured Audit Reports** | Outputs `Virtue_Final_Audit.csv` with 6 fields including `is_suspicious` |
| 🐳 **Containerized Dev** | `.devcontainer` for consistent, one-click developer setup |

---

## 🌐 Live Deployments

<div align="center">

| Platform | URL | Engine |
|:---:|:---:|:---:|
| 🔴 **Databricks Apps** | [virtue-audit-dashboard-...databricksapps.com](https://virtue-audit-dashboard-7474646237305242.aws.databricksapps.com/) | Apache Spark |
| 🟢 **Streamlit Cloud** | [ghana-medical-audit.streamlit.app](https://ghana-medical-audit.streamlit.app/) | Pandas |

</div>

---

## 🛠️ Tech Stack

<div align="center">

**Core AI / ML**

![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Llama](https://img.shields.io/badge/Llama_3.1-8B5CF6?style=flat-square)
![Groq](https://img.shields.io/badge/Groq_API-FF4081?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-FF6100?style=flat-square&logo=jupyter&logoColor=white)

**Dashboard**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

**Cloud Infrastructure**

![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)

**Dev Environment**

![DevContainers](https://img.shields.io/badge/Dev_Containers-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)

</div>

---

## 📂 Project Structure
📦 VirtueAudit-AI
│
├── 🧠 Accenture_Databricks_Virtue_Agent.ipynb   # Core AI pipeline
│                                                # ├─ LLaMA 3.1 extraction via Groq
│                                                # ├─ Apache Spark (Databricks)
│                                                # └─ Pandas fallback (local)
│
├── 🖥️  app.py                                    # Streamlit dashboard
│                                                # ├─ KPI metrics & Plotly charts
│                                                # ├─ Searchable data explorer
│                                                # └─ Per-facility case detail view
│
├── 📥 Virtue Foundation Ghana v0.3 - Sheet1.csv  # INPUT  · Raw unstructured facility data
├── 📤 Virtue_Final_Audit.csv                     # OUTPUT · Pandas → local root
│                                                #         · Spark  → Databricks DBFS
│
├── 📋 requirements.txt
├── ☁️  databricks_apps/
├── 🐳 .devcontainer/
└── 📝 Drafts/

---

## 📥 Dataset & Output Files

| File | Type | Engine | Description |
|---|---|---|---|
| `Virtue Foundation Ghana v0.3 - Sheet1.csv` | **Input** | — | Raw medical facility records from Virtue Foundation, Ghana |
| `Virtue_Final_Audit.csv` | **Output** | Pandas | Saved to project root when Spark unavailable |
| `Virtue_Final_Audit.csv` (DBFS) | **Output** | Apache Spark | Saved to DBFS on Databricks production runs |

> **Output schema:** `facility_name` · `specialty` · `equipment` · `capability` · `is_suspicious` · `suspicion_reason`

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** and **pip**
- **Groq API Key** → Free, no credit card required — get yours at [console.groq.com/keys](https://console.groq.com/keys)
- **Databricks Workspace** (for full pipeline only)
- **Git**

> 💡 **Groq is completely free to use!** Sign up at [console.groq.com](https://console.groq.com), navigate to **API Keys → Create API Key**, and copy your key. No billing setup needed.

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/OmSinha07/VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment.git
cd VirtueAudit-AI-Automated-Medical-Infrastructure-Verification-Risk-Assessment

# 2. Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Generate your FREE Groq API Key
#    → Go to https://console.groq.com/keys
#    → Sign up / Log in (no credit card needed)
#    → Click "Create API Key" → Copy it

# 4. Paste your key inside the notebook:
#    Open Accenture_Databricks_Virtue_Agent.ipynb and set:
#    GROQ_API_KEY = "your_groq_api_key_here"   ← paste here
```

---

## ⚙️ Running the Pipeline

### 🔴 Option 1 — Databricks (Recommended)

1. Import `Accenture_Databricks_Virtue_Agent.ipynb` into your Databricks workspace
2. Upload `Virtue Foundation Ghana v0.3 - Sheet1.csv` to DBFS
3. Ensure `groq` is installed on your cluster; set `GROQ_API_KEY`
4. Run all cells → output written to **DBFS** via Apache Spark

### 🟢 Option 2 — Local (Dev / Testing)

```bash
pip install groq jupyter
jupyter notebook
# Open the notebook, run all cells
# Pandas fallback activates automatically → output saved to project root
```

### 🖥️ Running the Dashboard

```bash
# Ensure Virtue_Final_Audit.csv exists first, then:
streamlit run app.py
# Visit http://localhost:8501
```

---

## ⚙️ Configuration

| Variable | Description | How to Get | Required |
|---|---|---|:---:|
| `GROQ_API_KEY` | Groq Llama 3.1 inference key | Free at [console.groq.com/keys](https://console.groq.com/keys) — no card needed | ✅ |
| `DATABRICKS_HOST` | Your Databricks workspace URL | From your Databricks workspace settings | Databricks only |
| `DATABRICKS_TOKEN` | Personal Access Token | Generated in Databricks user settings | Databricks only |

---

## 🧪 Testing & Validation

1. After running the notebook, inspect `Virtue_Final_Audit.csv` — verify `is_suspicious` and `suspicion_reason` columns
2. Launch the dashboard and use the **Deep Dive Investigation** section to search and filter facility audits
3. The **Case Detail View** renders the full audit verdict:
   - ✅ `AUDIT PASSED`
   - 🚨 `AUDIT ALERT`

---

## 🚀 Deployment

<details>
<summary><strong>🔴 Databricks Apps (Production)</strong></summary>

1. Navigate to **Databricks Apps** in your workspace
2. Create a new app pointing to `app.py`
3. Add `streamlit`, `pandas`, `plotly` as dependencies
4. Ensure `Virtue_Final_Audit.csv` (from DBFS) is accessible to the app runtime
5. Deploy

🔴 **Live:** https://virtue-audit-dashboard-7474646237305242.aws.databricksapps.com/

</details>

<details>
<summary><strong>🟢 Streamlit Cloud (Public / Lightweight)</strong></summary>

1. Push your repo (with `Virtue_Final_Audit.csv` committed) to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New App**
3. Select your repo, set `app.py` as the entry point → **Deploy**

🟢 **Live:** https://ghana-medical-audit.streamlit.app/

</details>

---

## 🤝 Contributing

Contributions are welcome! Areas to improve:

- 🎯 Accuracy of LLM risk detection prompts
- 🛡️ More robust data validation
- 🖼️ Enhanced Streamlit UI
- 🔌 Additional LLM providers or data sources

Use the `.devcontainer` setup in VS Code for a consistent dev environment.

---

## 📄 License

Distributed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

| Contributor | Role |
|---|---|
| **Accenture × Databricks** | Hackathon organizers |
| **Virtue Foundation Ghana** | Medical infrastructure dataset |
| **Groq** | High-performance LLM inference (free tier available) |
| **Databricks** | Unified data analytics platform |
| **Meta / Llama 3.1** | Underlying large language model |

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ by [OmSinha07](https://github.com/OmSinha07) for the **Accenture × Databricks Hackathon**

<br/>

[![Open Databricks Dashboard](https://img.shields.io/badge/🔴_Open_Databricks_Dashboard-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://virtue-audit-dashboard-7474646237305242.aws.databricksapps.com/)
&nbsp;&nbsp;
[![Open Streamlit Dashboard](https://img.shields.io/badge/🟢_Open_Streamlit_Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ghana-medical-audit.streamlit.app/)

<img src="https://capsule-render.vercel.app/api?type=waving&color=FF3621&height=100&section=footer" width="100%"/>

</div>
