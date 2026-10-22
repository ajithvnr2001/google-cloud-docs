---
url: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-demo/
title: CLI Cortex Framework demo deploy \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:36.705092+00:00
---

# CLI Cortex Framework demo deploy  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-demo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CLI Cortex Framework demo deploy

**NAME**

`uv run cortex-demo` \- Deploy Cortex Framework demo scenario with pre populated sample data.

**SYNOPSIS**
    
    
    uv run cortex-demo [-h] --project_id PROJECT_ID
        [--dataform_region DATAFORM_REGION] 
        [--bigquery_location BIGQUERY_LOCATION] 
        [--service_account SERVICE_ACCOUNT]
        [--sap_version SAP_VERSION] 
        [--source_sap_raw_dataset_id SOURCE_SAP_RAW_DATASET_ID]
        [--target_sap_foundation_dataset_id TARGET_SAP_FOUNDATION_DATASET_ID]
        [--target_dp_dataset_id TARGET_DP_DATASET_ID] 
        [--repository_name REPOSITORY_NAME] 
        [--workspace_name WORKSPACE_NAME] [--create_workflow_configs] 
        [--enable-apis] [--create-datasets] [--disable-telemetry]
    

## Global flags

Flag | Description | Default  
---|---|---  
`-h` | Show help message and exit. |   
`--project_id=PROJECT_ID` | The Google Cloud project ID to use for this invocation. |   
`--dataform_region DATAFORM_REGION` | The Google Cloud region where the Dataform repository and workspace will be hosted. For more information, see [Supported Dataform regions](https://docs.cloud.google.com/cortex/docs/supported-locations#supported-Dataform-regions). | `us-central1`  
`--bigquery_location BIGQUERY_LOCATION` | The BigQuery location to use for all datasets. BigQuery is the native execution environment for all transformations. For more information, see [Supported BigQuery locations](https://docs.cloud.google.com/cortex/docs/supported-locations#supported-BigQuery-locations). | `US`  
`--service_account SERVICE_ACCOUNT` | The service account Dataform will use to run the transformation graphs. This is required for creating scheduled workflow configurations. |   
`--sap_version SAP_VERSION` | The SAP source system version (for example, `ecc` or `s4`) to use for the demo deployment. | `s4`  
`--source_sap_raw_dataset_id SOURCE_SAP_RAW_DATASET_ID` | The BigQuery dataset ID containing the raw SAP tables. | `cortex_demo_sap_s4_raw`  
`--target_sap_foundation_dataset_id TARGET_SAP_FOUNDATION_DATASET_ID` | The BigQuery dataset ID for the Data Foundation Layer (the cleaned, standardized representation of source data). | `cortex_demo_sap_s4_data_foundation`  
`--target_dp_dataset_id TARGET_DP_DATASET_ID` | The BigQuery dataset ID for the Data Product Layer (domain-oriented interfaces aggregated for consumption). | `cortex_demo_data_product`  
`--target_samples_dataset_id TARGET_SAMPLES_DATASET_ID` | The BigQuery dataset ID for the target samples. | `cortex_demo_samples`  
`--repository_name REPOSITORY_NAME` | The name of the Dataform repository to create or deploy the assets to. | `cortex-framework-demo`  
`--workspace_name WORKSPACE_NAME` | The name of the Dataform workspace where the assets will be pushed. | `demo`  
`--create_workflow_configs` | Optional flag to automatically create the Dataform Workflow Configurations (schedules) for the deployed assets. |   
`--enable-apis` | Optional flag to automatically enable the required Google Cloud APIs (for example, BigQuery, Dataform) for the project. |   
`--create-datasets` | Optional flag to automatically provision the necessary target BigQuery datasets (Raw, Foundation, Data Product). |   
`--disable-telemetry` | Temporarily disable telemetry event logging during execution. For more information, see [Cortex Framework Telemetry](https://docs.cloud.google.com/cortex/docs/telemetry). |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
