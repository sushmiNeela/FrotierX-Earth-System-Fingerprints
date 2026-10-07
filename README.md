# 🌍 Earth System Fingerprints

### Detecting and Characterizing Contrasting Multi-Variable Environmental Trends Using NASA Earth Observations

![NASA](https://img.shields.io/badge/Data-NASA%20Earth%20Observations-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Streamlit](https://img.shields.io/badge/App-Streamlit-red)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

---

## 🌎 Overview

**Earth System Fingerprints** is a NASA Earth observation-based project that investigates how multiple environmental variables change together across space and time.

The project combines three core environmental variables:

- **Land Surface Temperature (LST)**
- **Vegetation (NDVI)**
- **Soil Moisture**

Rather than analyzing each variable independently, the project aims to identify **contrasting multi-variable environmental patterns** and represent them as interpretable **Earth System Fingerprints**.

**Bangladesh** is the primary deep-dive study area, while the overall workflow is designed to be adaptable to other geographic regions.

---

## 🎯 Key Questions

The project addresses four core questions:

- **What is changing?**
- **Where is it changing?**
- **How much is it changing?**
- **Is the change statistically significant?**

---

## 🛰️ NASA Data

| Variable | NASA Product | Version | Native Resolution | Temporal Type |
|---|---|---|---|---|
| Land Surface Temperature | MODIS MOD11A1 | V061 | 1 km | Daily |
| Vegetation / NDVI | MODIS MOD13A3 | V061 | 1 km | Monthly |
| Soil Moisture | SMAP SPL3SMP_E | V006 | ~9 km | Daily |

Data are obtained through **NASA Earthdata / AppEEARS** and will be quality-controlled and harmonized before multi-variable analysis.

---

## 🔬 Methodology

The planned workflow is:

```text
NASA Earth Observation Data
            ↓
Data Acquisition
            ↓
QA/QC
            ↓
Temporal Harmonization
            ↓
Spatial Harmonization
            ↓
Trend Analysis
            ↓
Statistical Significance
            ↓
Feature Extraction
            ↓
Multi-Variable Pattern Discovery
            ↓
Earth System Fingerprints
            ↓
Interactive Dashboard

