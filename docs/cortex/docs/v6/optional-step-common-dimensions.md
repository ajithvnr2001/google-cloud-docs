---
url: https://docs.cloud.google.com/cortex/docs/v6/optional-step-common-dimensions/
title: Configure Common Dimensions \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:21.811738+00:00
---

# Configure Common Dimensions  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/optional-step-common-dimensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Common Dimensions

This page describes an optional step to configure Common Dimensions for the Cortex Framework Data Foundation deployment. Cortex Framework Common Dimensions are utility views and tables created within the Data Foundation to enable advanced use cases across different data sources, such as Cross Media & Product Connected Insights.

Configuration for all Common Dimensions are under the `k9` section of the [configuration file](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json).

## Country Dimension

Cortex Framework Country Dimension provides a unified way of connecting ISO-3166 country codes to their respective long names.

To enable it, set `k9.deployCountryDim` to `true` in the configuration file.

## Product Hierarchy Dimension

Product Hierarchy Dimension provides an abstract schema that allows ingesting the source data from any arbitrary source. It can then be used in fueling advanced use cases such as product hierarchy matching.

Cortex Framework also provides a sample ingestion DAG if you have a SAP deployment ready.

To enable it, set `k9.deployProductDim` to `true` in the configuration file. Then configure the following settings:

Parameter  | Meaning  | Default Value   
---|---|---  
`k9.ProductDim.dataSourceType` | Data source type for the product hierarchy.  
If set to `"SAP"`, Data Foundations will deploy a DAG that loads product hierarchy from the SAP data source. If this is the case, SAP deployment must be enabled.  
If you are using other data sources, set this value to `BYOD` and you may then populate the product hierarchy table manually.  | `-`  
`k9.ProductDim.textLanguage` | Language of product hierarchy. It should follow the same language code convention from the data source. Cortex Framework doesn´t prescribe this convention. However, customers should understand the meaning of their chosen `textLanguage` value.  
If using SAP, the value must also be one of the `SAP.languages` settings within the current `config.json`.  
This value can't be empty.  | `-`  
  
### Ingesting product hierarchy dimension data from SAP

If you have specified `k9.ProductDim.dataSourceType` to `SAP` and deployed SAP, you may use the `load_product_hierarchy_from_SAP` DAG to load SAP hierarchy, after you have fully populated your SAP Reporting views. Make sure to properly [configure](https://docs.cloud.google.com/cortex/docs/v6/gathering-settings) the `k9_reporting` Managed Service for Apache Airflow connection.

### Ingesting product hierarchy dimension data from other sources

You may also manually ingest product hierarchy information from other sources of your choosing (for example, [Google product category](https://support.google.com/merchants/answer/6324436?hl)). Make sure the data conforms to the schema of `ProductHierarchy` table.

## Currency Conversion

Currency Conversion provides an abstract schema that allows ingesting the source data from any arbitrary source. It can then be used in fueling advanced use cases for other data sources that don't provide currency conversion capability out-of-the-box.

Cortex Framework also provides a sample ingestion DAG if you have a SAP deployment ready. To enable it, set `k9.deployCurrencyConversion` to `true` in the configuration file. Then configure the following settings:

Parameter  | Meaning  | Default Value   
---|---|---  
`k9.CurrencyConversion.dataSourceType` | Data source type for the product hierarchy.  
If set to `"SAP"`, Data Foundations will deploy a DAG that loads currency conversion rates from the SAP data source. If this is the case, SAP deployment must be enabled.  
If you are using other data sources, set this value to `BYOD` and you may then populate the currency conversion table manually.  | `-`  
`k9.CurrencyConversion.rateType` | Default currency conversion rate type as defined in the source system.  
If you are using SAP, `"M"` corresponds to SAP default rate type.  
This value can't be empty.  | `-`  
  
### Ingesting currency conversion data from SAP

If you have specified `k9.CurrencyConversion.dataSourceType` to `SAP` and deployed SAP, you may use the `load_currency_conversion_from_SAP` DAG to load SAP currency conversion rates, after you have fully populated your SAP Reporting views. Make sure to properly [configure](https://docs.cloud.google.com/cortex/docs/v6/gathering-settings) the `k9_reporting` Managed Airflow connection.

### Ingesting currency conversion data from other sources

You may also manually ingest currency conversion information from other sources of your choosing (for example, using [GOOGLEFINANCE function in Google Docs](https://support.google.com/docs/answer/3093281?hl), or [BigQuery public datasets](https://cloud.google.com/bigquery/public-data)). Make sure the data conforms to the schema of `CurrencyConversion` table.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
