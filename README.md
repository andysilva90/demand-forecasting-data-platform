Project Title:
Demand Forecasting Data Platform Using External Signals (AWS)

1. Project Overview:

This project demonstrates an end-to-end data engineering pipeline designed to support a machine learning demand forecasting use case.
The platform ingests historical sales data and enriches it with external signals such as weather conditions and macro-economic indicators. The processed data is transformed into analytics- and ML-ready datasets and stored in the cloud, where it can be consumed by downstream machine learning models.

The primary goal of this project is to showcase production-style data engineering practices, including data modeling, automation, data quality checks, and clear separation between raw, processed, and curated data layers.

2. Business Problem:

Retail and supply chain teams need accurate demand forecasts to make informed inventory and replenishment decisions.
However, demand is influenced not only by historical sales patterns, but also by external factors such as:

* Weather conditions
* Economic trends
* Seasonality and calendar effects

Without a reliable data platform that combines these signals, forecasting models tend to be inaccurate or difficult to maintain.

3. Business Value:

This platform enables:

* Centralized and reliable access to historical and enriched sales data
* Consistent feature generation for machine learning models
* Improved forecast accuracy by incorporating external signals
* Reproducible and automated data pipelines

Business stakeholders who would benefit include:

* Inventory planners
* Supply chain managers
* Operations leadership
* Data science teams

4. Data Sources

This project uses a combination of historical internal data and external public APIs.

4.1 Historical Sales Data (Internal Source)

* Source: Kaggle retail sales dataset
* Description: Represents a historical extract from a transactional sales system
* Usage: One-time historical backfill
* Provides sufficient history for trend analysis and ML training

In a real-world scenario, this dataset represents an initial data migration from an OLTP system.

4.2 Weather Data (External API)

* Source: Open-Meteo API
* Type: Public, no authentication required
* Data: Daily temperature, Precipitation, Wind speed
* Usage: Continuous ingestion, Demand signal enrichment

4.3 Economic Indicators (External API)

* Source: World Bank API
* Indicators: Inflation rate, GDP growth
* Usage: Monthly/quarterly enrichment, Long-term demand trend context

5. Solution Architecture

The platform follows a cloud-based, layered data architecture deployed on AWS.

High-level components:

* Python-based ingestion scripts
* Amazon S3 as a data lake
* Layered data modeling (Bronze / Silver / Gold)
* dbt for transformations and data quality tests
* Orchestration for automation
* Machine learning pipeline consuming curated data

An architecture diagram is provided in the docs/architecture/ folder.

6. Data Pipeline Flow

* Extract data from source systems and APIs
* Load raw data into Amazon S3 (Bronze layer)
* Clean and standardize data (Silver layer)
* Create analytics- and ML-ready datasets (Gold layer)
* Generate feature tables for forecasting models
* Train and evaluate ML models
* Store predictions for downstream consumption

7. Data Modeling Approach

The data platform follows a layered modeling strategy:

* Bronze: Raw, immutable data as received from sources
* Silver: Cleaned and standardized datasets
* Gold: Business-aligned, feature-rich tables optimized for analytics and ML

This approach ensures traceability, auditability, and scalability.

8. Machine Learning Objective

The curated Gold-layer datasets are used to train a demand forecasting model that predicts future sales quantities at a daily granularity.

Key aspects:

* Time-series feature engineering
* Lagged variables and rolling averages
* External signal enrichment
* Model evaluation using standard regression metrics

The ML pipeline is intentionally decoupled from ingestion and transformation logic.

9. Data Quality & Assumptions

Data quality checks are applied during transformation, including:

* Null value checks
* Schema validation
* Freshness checks
* Volume anomaly detection

Key assumptions:

* Historical sales data is complete but static
* External API data is assumed to be authoritative
* Forecasts are intended for planning purposes, not real-time decisioning
* Near-real-time weather was intentionally excluded as unnecessary for the business use case

10. Tech Stack

* Cloud: AWS (S3)
* Programming Language: Python
* Data Transformation: dbt Core
* Orchestration: Airflow / Prefect
* Data Storage: Parquet on S3
* Machine Learning: scikit-learn / XGBoost
* Version Control: Git & GitHub

11. How to Run the Project

(Section to be completed as the project is implemented)

12. Future Improvements

Potential enhancements include:

* Streaming ingestion for near-real-time data
* Feature store integration
* Model versioning and monitoring
* Cost optimization strategies
* CI/CD for data pipelines