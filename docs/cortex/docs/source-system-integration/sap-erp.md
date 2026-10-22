---
url: https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp/
title: SAP ERP integration for Cortex Framework. \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:37.735567+00:00
---

# SAP ERP integration for Cortex Framework.  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAP ERP integration for Cortex Framework.

**Important:** The steps outlined on this page are required for the Cortex Framework [deployment](https://docs.cloud.google.com/cortex/docs/deployment). For the [demo deployment](https://docs.cloud.google.com/cortex/docs/demo-deployment), you can skip this page.

Google Cloud Cortex Framework [data foundation layer](https://docs.cloud.google.com/cortex/docs/overview#data_foundation_layer) for SAP ERP requires connectivity to the source system raw data. Both SAP ECC and SAP S/4HANA are supported.

Prior to deploying Cortex Framework content, relevant SAP ERP tables must be replicated into BigQuery. You can achieve this by landing data in a dedicated [raw layer](https://docs.cloud.google.com/cortex/docs/overview#raw_layer) dataset for Change Data Capture (CDC) processing or by using established CDC pipelines to feed the data foundation layer directly. For more information, see [Technical requirements for replicating SAP ERP data](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp#technical_requirements_for_replicating_sap_erp_data).

You may use any replication tool of your choice, provided it can replicate data in raw table format to BigQuery. For example, Google Cloud solutions include the [BigQuery Connector for SAP (requires SAP SLT),](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview) and the [BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview).

To ensure compatibility between the replicated raw datasets from SAP ERP and Cortex Framework data foundation layer, ensure you meet the following requirements.

## Technical requirements for replicating SAP ERP data

Make sure to review and complete the following technical requirements for replicating SAP data into Cortex Framework in BigQuery.

  1. **Raw data structure** : Data from ECC or S/4HANA should land in BigQuery with the same structure as the base tables in SAP and without business transformations. Tables must be replicated with the required field names, types, and granularity as they exist in SAP.

  2. **Table configuration** : The list of tables to be transformed is defined in the `table_settings.yaml` file (located under `config/cortex/data_foundation/sap`). If a required table is missing during deployment, the specific data products depending on it will fail.

  3. **Metadata requirements** : You must replicate metadata tables like `DD03L` from your SAP source to the raw dataset (configured as the source for your foundation module in `config/config.yaml`). Note that while these metadata tables must exist in the raw dataset, they must not be included in the data foundation `table_settings.yaml` file and isn't processed by the data foundation layer. Ensure that the replicated `DD03L` table contains the field metadata records for any tables you plan to ingest (such as custom or supplementary tables like `sflight`). The Cortex Framework build scripts and dependency resolver read these metadata rows to identify column lists, data types, and primary key relationships between tables.

  4. **Casing** : Names of the replicated SAP tables in BigQuery **must be in lowercase** for Cortex Framework data model compatibility (for example, the SAP table `MARA` becomes `mara` in BigQuery).

  5. **Object names (columns) and special characters** : For object names (columns) containing special characters (like `/`, `-`, or leading underscores `_`), Cortex expects a generic sanitization pattern:

     * All non-alphanumeric characters are replaced with an underscore `_`.
     * Leading underscores and digits are not allowed. For example, `/GOOG/TEST` becomes `goog_test`, and `_DATAAGING` becomes `dataaging`. If your replication tool lands data with leading underscores preserved, a normalization step (aliasing) in the Data Foundation layer is required.
  6. **Data propagation fields** : To support CDC (Change Data Capture) and data propagation, replicated SAP tables need to have:

     * An operation flag named `operation_flag` (`L` = initial load, `I` = insert, `U` = update, `D` = delete).
     * A timestamp named `recordstamp` (populated with the current timestamp at the time of the load).
     * _Optional_ : An additional field `is_deleted` (BOOLEAN) is chosen in replicated `_DS_RAW` tables (defaulting to false on initial load). Runtime views generated by Cortex reference this column, but it can be removed from the CDC and view templates prior to execution if the replication tool doesn't produce it.
  7. **Data types** : Necessary mapping of SAP data types with BigQuery data types for compatibility:

**Necessary for standard operations:**

Data type SAP | Data type BigQuery | Description  
---|---|---  
DATS | `DATE` | Date data type  
TIMS | `TIME` | Time data type  
  8. **Highly Recommended for precision and compatibility:**

     * `CURR` (Currency) and `QUAN` (Quantity) mapped to `NUMERIC` or `BIGNUMERIC` (Avoid `FLOAT64` to prevent rounding errors in financial calculations).
     * `NUMC` (Numeric Character) mapped to `STRING` (To preserve leading zeros for document numbers and item numbers, ensuring successful joins).
**Note:** Generally, you can assume the default mapping as long as the same operations on the target field can be applied. If the mappings are changed, customers can manually `CAST` datatypes in the templates.
  9. **Payload Compression** : To prevent empty SAP columns (initial values like spaces or zeros) from being filled with `NULL` in BigQuery, ensure that **payload compression is deactivated** in the connector configuration (or "Send Uncompressed" is enabled). This ensures that empty strings or zeros are preserved as such in the target rather than defaulting to `NULL`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
