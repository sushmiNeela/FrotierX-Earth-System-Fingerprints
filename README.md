# 🌍 Earth System Fingerprints

### NASA Space Apps Challenge 2026

### Detecting and Characterizing Contrasting Multi-Variable Environmental Trends Using NASA Earth Observations

![NASA](https://img.shields.io/badge/Data-NASA%20Earth%20Observations-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Streamlit](https://img.shields.io/badge/App-Streamlit-red)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)


## 👋 Meet Our Team

We are **Team FrontierX**, a team of five participating in the NASA Space Apps Challenge 2026. We are interested in exploring how NASA Earth observation data can help us understand environmental changes across different regions of our planet.

Through **Earth System Fingerprints**, we aim to investigate patterns in land surface temperature (LST), vegetation health (NDVI), and soil moisture. By combining satellite data, statistical trend analysis, interactive visualization, and planned machine-learning techniques, we seek to compare environmental trends across Bangladesh, the Indo-Gangetic Plain, and the Amazon deforestation frontier.

Our goal is to transform complex Earth observation data into meaningful and accessible visual insights while clearly communicating the limitations of our analysis.

---

## 🚀 About the Project

Earth System Fingerprints explores how multiple environmental variables can be combined to characterize regional patterns of environmental change. Instead of examining each variable in isolation, the project aims to develop a multi-variable environmental fingerprint for each study region.

By analyzing changes in land surface temperature, vegetation health, and soil moisture, we aim to explore contrasting environmental trends and make them easier to understand through interactive visualizations and data-driven analysis.


**NASA Space Apps Challenge 2026**  
**Challenge:** Be An Earth System Trend Detective!  
**Project Type:** Interactive Web Prototype and Environmental Trend Analysis  
**Project Status:** Working Prototype

> Exploring environmental change through the combined patterns of land surface temperature, vegetation greenness, and soil moisture.

---
## 1. Project Overview

**Earth System Fingerprints** is an environmental science project that
explores how multiple satellite-derived indicators can be combined to
characterize environmental trends across different regions of Earth.

The project focuses on three variables:

-   **Land Surface Temperature (LST):** Indicates the temperature of the
    land surface.
-   **Normalized Difference Vegetation Index (NDVI):** Provides an
    indicator of vegetation greenness.
-   **Soil Moisture:** Measures the water content of soil and helps
    characterize surface wetness and drying conditions.

We call the combined pattern of these environmental trends a region's
**Earth System Fingerprint**. By examining the variables together, the
project aims to investigate how environmental patterns differ between
selected regions.

## 2. Problem Statement

Environmental change cannot always be understood by examining a single
variable. Temperature, vegetation, and soil moisture describe different
components of the Earth system. Their combined trends may provide a more
informative view of changing environmental conditions.

Our project aims to investigate:

1.  What environmental variables are changing?
2.  Where are the changes occurring?
3.  How large are the observed trends?
4.  What statistical evidence supports these trends?
5.  How do combined environmental patterns differ across regions?

## 3. Proposed Solution

The proposed workflow combines NASA satellite observations with
statistical trend analysis and interactive visualization.

1.  Acquire satellite data for the selected study regions.
2.  Apply product-specific scale factors, fill-value handling, and
    quality-control filters.
3.  Harmonize the datasets to a documented common spatial grid and
    analysis period.
4.  Estimate trend direction and magnitude using Sen's slope.
5.  Evaluate monotonic trends using the Mann--Kendall test.
6.  Combine the results into regional multi-variable fingerprints.
7.  Compare and visualize the results through an interactive dashboard.

## 4. NASA Earth Observation Datasets

  -----------------------------------------------------------------------
  Variable                Product                 Purpose
  ----------------------- ----------------------- -----------------------
  Land Surface            MODIS/Terra MOD11A1     Analyze land surface
  Temperature             V061                    temperature trends

  Vegetation Greenness    MODIS/Terra MOD13Q1     Analyze vegetation
                          V061                    greenness trends

  Soil Moisture           SMAP SPL3SMP_E V006     Analyze soil moisture
                                                  trends
  -----------------------------------------------------------------------

### MODIS Land Surface Temperature --- MOD11A1 V061

-   Platform: Terra
-   Native spatial resolution: approximately 1 km
-   Temporal resolution: Daily
-   Relevant layers: `LST_Day_1km` and `QC_Day`
-   DOI: https://doi.org/10.5067/MODIS/MOD11A1.061

### MODIS Vegetation Index --- MOD13Q1 V061

-   Platform: Terra
-   Native spatial resolution: 250 m
-   Temporal resolution: 16-day composite
-   Relevant science layer: NDVI
-   Product information: https://lpdaac.usgs.gov/products/mod13q1v061/

### SMAP Soil Moisture --- SPL3SMP_E V006

-   Platform: NASA Soil Moisture Active Passive (SMAP)
-   Spatial grid: approximately 9 km EASE-Grid 2.0
-   Temporal resolution: Daily
-   Selected retrieval layer:
    `Soil_Moisture_Retrieval_Data_AM_soil_moisture_dca`
-   Product information: https://nsidc.org/data/spl3smp_e/versions/6

### Data Quality and Harmonization

The products differ in native resolution, temporal sampling, and
retrieval quality. The analysis must account for:

-   Product-specific scale factors and fill values.
-   Relevant quality flags and retrieval-quality information.
-   Missing observations and valid sample counts.
-   A consistent analysis period supported by all required datasets.
-   Spatial harmonization to a documented common grid of approximately 9
    km.
-   Documented temporal aggregation and resampling methods.

A common grid does not remove the limitations or uncertainty of the
original observations.

## 5. Selected Study Regions

### Region 1: Bangladesh

Bangladesh is the focal study region. The analysis aims to examine
changes in land surface temperature, vegetation greenness, and soil
moisture over the selected study period.

### Region 2: Indo-Gangetic Plain (IGP) Analysis Region

This region provides a second case study for comparing environmental
trends across a major agricultural and densely populated landscape. The
exact analysis boundary will be documented in the project files.

### Region 3: Amazon Deforestation Frontier

This candidate region provides a contrasting forest-frontier setting for
investigating environmental trends. The selected polygon and its
geographic definition will be documented for reproducibility.

### Why Compare These Regions?

The regions represent different environmental and land-use contexts.
Their comparison may reveal similarities or differences in observed
temperature, vegetation, and soil moisture trends.

Regional labels such as warming, drying, or vegetation stress will be
assigned only when supported by processed data and clearly defined
criteria. They are not assumed in advance.

## 6. Methodology

### Stage 1: Data Acquisition

Retrieve the selected MODIS and SMAP products for each study region and
analysis period.

### Stage 2: Quality Control

Apply the relevant quality filters, scale factors, and fill-value
handling. Document missing data and exclusions.

### Stage 3: Spatial and Temporal Harmonization

Prepare comparable time series using a documented common grid of
approximately 9 km and a consistent analysis period. Record how daily
observations and 16-day NDVI composites are aligned or aggregated.

### Stage 4: Statistical Trend Analysis

**Sen's slope:** Estimates the magnitude and direction of a trend using
the median of pairwise slopes.

**Mann--Kendall test:** Evaluates statistical evidence for a monotonic
trend. The implementation must consider ties, temporal dependence,
sample size, and relevant assumptions.

The analysis will document the test statistic, p-value, significance
threshold, and limitations. Statistical significance alone does not
establish causation or practical importance.

### Stage 5: Earth System Fingerprint

The project combines the trend direction, magnitude, and statistical
evidence for LST, NDVI, and soil moisture into a regional summary.

Illustrative example:

`LST ↑ + NDVI ↓ + Soil Moisture ↓`

This pattern could be consistent with warming, drying, and declining
vegetation greenness. It is an illustration of the concept, not a
verified finding for any selected region.

### Stage 6: Regional Comparison

Compare the regional results through maps, time-series charts, summary
indicators, and documented criteria for classifying similarities or
contrasts.

## 7. Interactive Demo Application

The project includes an HTML-based interactive prototype intended to
communicate the Earth System Fingerprints concept.

The prototype is designed to include:

-   Three-dimensional Earth visualization.
-   Study-region markers and selection controls.
-   LST, NDVI, and soil moisture views.
-   Regional comparison components.
-   Time-series charts and trend summaries.

**Important prototype limitation:** The current HTML prototype includes
illustrative synthetic time-series data. Its displayed charts, Sen's
slope values, and p-values are not validated results derived from NASA
satellite observations. The prototype requires further testing and
integration with quality-controlled satellite data before it can be
presented as a validated scientific analysis application.

## 8. Technology Stack

## 🧰 Technology Stack

### 🌐 Web Development and Visualization
- **HTML, CSS, and JavaScript** — Interactive web interface.
- **Three.js** — Three-dimensional Earth visualization.
- **Plotly and Matplotlib** — Interactive charts and scientific visualization.
- **Streamlit** — Interactive data-analysis dashboard.

### 🛰️ Data Processing and Geospatial Analysis
- **Python** — Scientific data processing and analysis.
- **NumPy and Pandas** — Numerical computation and data manipulation.
- **xarray and netCDF4** — Multidimensional satellite data processing.
- **Rasterio** — Raster data processing.
- **GeoPandas** — Geographic data handling.

### 📈 Statistical Trend Analysis
- **SciPy** — Statistical calculations and numerical methods.
- **Sen's Slope** — Estimation of environmental trend magnitude and direction.
- **Mann–Kendall Trend Test** — Evaluation of evidence for monotonic environmental trends.

### 🤖 Machine Learning and Pattern Discovery
- **Scikit-learn** — Machine-learning workflows, feature scaling, clustering, and model evaluation.
- **K-Means Clustering** — A candidate unsupervised learning method for grouping locations with similar environmental trend features.
- **Principal Component Analysis (PCA)** — An optional technique for exploring patterns in multi-variable environmental data.

Machine learning will be explored after the satellite observations have been quality-controlled and statistical trend features have been calculated. The final choice of algorithms will depend on data availability, the research question, and validation results.

> **Implementation Note:** Technologies and algorithms listed as planned are not necessarily implemented in the current prototype. Their status will be updated as development and testing progress.

## 9. Expected Outputs

## 🎯 Expected Outputs

The *Earth System Fingerprints* project aims to produce the following outputs using NASA Earth observation data:

###  Multi-Variable Environmental Trend Analysis
- Analyze Land Surface Temperature (LST), vegetation health (NDVI), and soil moisture across three selected study regions: Bangladesh, the Indo-Gangetic Plain, and the Amazon deforestation frontier.
- Estimate the direction and magnitude of environmental trends using Sen's slope.
- Apply the Mann–Kendall trend test to assess evidence of monotonic trends.
- Account for data quality, missing observations, and differences in the native spatial resolutions of the datasets.

### Regional Earth System Fingerprints
- Develop a combined trend profile for each study region using the three environmental variables.
- Identify patterns such as warming, vegetation decline, and soil moisture reduction where supported by the processed observations.
- Compare the regional fingerprints to explore similarities and differences in environmental change.

### Interactive Visualization
- Provide a 3D Earth visualization with selectable study regions.
- Display environmental variables and regional trend summaries through charts and visual indicators.
- Present the estimated trend direction, magnitude, and statistical significance where valid results are available.

### Data-Driven Pattern Discovery
- Explore whether locations can be grouped according to their multi-variable trend patterns.
- Evaluate suitable unsupervised learning methods, such as K-Means clustering, if the processed data supports their use.
- Interpret discovered patterns alongside the statistical trend results rather than treating clusters as proof of environmental causes.

### Research and Demonstration Outputs
- An interactive prototype demonstrating the project's workflow.
- A documented data-processing and trend-analysis pipeline.
- Regional comparison results, visualizations, and an explanation of the methodology.
- A public GitHub repository containing the source code, documentation, and instructions for reproducing the analysis.

> **Important:** The current prototype uses illustrative data for its trend charts. The regional trend values, statistical significance, and environmental fingerprint classifications will be treated as scientific findings only after they have been calculated and checked using processed NASA observations.
## 10. Current Development Status

The project is under development. The current HTML application
demonstrates the visualization concept, but the prototype's illustrative
data must not be confused with validated satellite-derived findings.

  -----------------------------------------------------------------------
  Component                           Status
  ----------------------------------- -----------------------------------
  Project concept and variables       Defined

  Interactive HTML prototype          Available; requires further testing

  Illustrative charts                 Available; synthetic data

  NASA product selection              Documented

  Quality-controlled data processing  Requires verification

  Spatial and temporal harmonization  In development

  Validated regional trend statistics Not yet established by the
                                      prototype

  Data-driven regional comparison     Pending validated results
  -----------------------------------------------------------------------

Update this table as work is completed and verified.

## 11 Limitations

The current version of Earth System Fingerprints is an early-stage prototype. Several limitations remain:

- **Illustrative Data:** The current prototype uses illustrative time-series data for its trend charts. These values must be replaced with trends calculated from quality-controlled NASA satellite observations before drawing scientific conclusions.

- **Limited Study Regions:** The initial analysis focuses on three selected regions: Bangladesh, the Indo-Gangetic Plain, and the Amazon deforestation frontier. These regions do not represent all global environmental conditions.

- **Different Spatial and Temporal Resolutions:** MODIS LST, MODIS NDVI, and SMAP soil moisture products have different native spatial and temporal resolutions. Harmonization is necessary before combining their trends.

- **Data Quality and Missing Observations:** Cloud contamination, retrieval uncertainty, quality flags, and missing observations may affect the reliability of the estimated trends.

- **Statistical Interpretation:** Sen's slope and the Mann–Kendall test characterize trend magnitude and statistical evidence, but they do not establish causal relationships between environmental variables.

- **Machine Learning Validation:** Unsupervised pattern discovery is a planned extension. Any resulting clusters will require appropriate evaluation and environmental interpretation before being considered meaningful.

## 12 Future Work

Future development will focus on improving the scientific reliability, scalability, and usability of Earth System Fingerprints.

- **Integrate Processed NASA Observations:** Replace illustrative values with quality-controlled LST, NDVI, and soil moisture data from the selected NASA Earth observation products.

- **Strengthen Trend Analysis:** Implement and validate Sen's slope and the Mann–Kendall trend test, including appropriate treatment of missing data, ties, and potential temporal autocorrelation.

- **Improve Spatial Harmonization:** Establish a consistent analysis grid and documented resampling procedures for combining the three environmental variables.

- **Expand Regional Coverage:** Extend the workflow to additional regions and, where feasible, broader spatial coverage.

- **Explore Unsupervised Learning:** Evaluate methods such as K-Means clustering to discover locations with similar multi-variable environmental trend patterns.

- **Improve Interactive Visualization:** Develop an interactive dashboard that allows users to explore regional fingerprints, compare variables, and inspect trend statistics.

- **Enhance Reproducibility:** Document data sources, processing steps, quality-control rules, parameter choices, and analysis outputs so that results can be independently reproduced.

- **Validate Environmental Interpretations:** Compare detected patterns with relevant environmental evidence and independent datasets where available.

## 13. Team and Contributions

**Official Team Name:** FrontierX

Our team developed *Earth System Fingerprints* for the NASA Space Apps Challenge 2026. The project explores multi-variable environmental trends using NASA Earth observation data, statistical analysis, interactive visualization, and machine learning.

### Team Members and Roles

| Team Member | Role | Responsibilities |
|---|---|---|
| [Sushmita Chowdhury] | Team Leader, Lead Developer & ML Engineer | Project coordination, Python development, satellite data processing, statistical trend analysis, and machine-learning-based environmental pattern discovery. |
| [Antika Das] | NASA Data Analyst | Researching NASA datasets, collecting satellite observations, and documenting data sources and quality requirements. |
| [Saima Akter] | Geospatial Analyst | Preparing study regions, handling spatial data, and supporting spatial harmonization and regional comparisons. |
| [Arpita Barua] | Visualization & Dashboard Developer | Developing interactive visualizations, charts, and dashboard components. |
| [Saima AKhter] | Research & Documentation Lead | Supporting background research, methodology documentation, README preparation, and project video development. |

### Collaboration

Team members collaborate on project development, testing, documentation, and presentation. Responsibilities may overlap as needed.

Machine-learning methods, including K-Means clustering, will be explored to identify locations with similar multi-variable environmental trend patterns, subject to data availability and validation.
## 14. Running the HTML Prototype

The Earth System Fingerprints interactive prototype can be run locally using a modern web browser.

### Prerequisites
- A modern web browser, such as Google Chrome, Microsoft Edge, or Firefox.
- An internet connection if the prototype relies on externally hosted libraries or resources.

### Steps to Run

1. Clone or download this repository.
2. Locate the `Earth_System_Fingerprints.html` file in the project directory.
3. Open the HTML file in a modern web browser.
4. Check that the 3D Earth visualization, interactive controls, and charts load correctly.

### Clone the Repository

```bash
git clone <YOUR_PUBLIC_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
## 15. Data Sources and References

-   NASA MODIS/Terra MOD11A1 V061:
    https://doi.org/10.5067/MODIS/MOD11A1.061
-   MODIS/Terra MOD13Q1 V061:
    https://lpdaac.usgs.gov/products/mod13q1v061/
-   NASA SMAP SPL3SMP_E V006:
    https://nsidc.org/data/spl3smp_e/versions/6
-   NASA Earthdata: https://www.earthdata.nasa.gov/
-   NASA Space Apps Challenge: https://www.spaceappschallenge.org/

Document product versions, selected layers, access dates, study
boundaries, and processing decisions to support reproducibility.

## 16. Acknowledgments

We acknowledge NASA and the relevant data-product teams for providing
Earth-observation data for scientific research and exploration.



**Earth System Fingerprints --- Exploring the stories hidden in Earth's
changing environmental signals.**
