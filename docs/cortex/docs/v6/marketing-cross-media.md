---
url: https://docs.cloud.google.com/cortex/docs/v6/marketing-cross-media/
title: Cross Media & Product Connected Insights \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:54:03.119693+00:00
---

# Cross Media & Product Connected Insights  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/marketing-cross-media/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cross Media & Product Connected Insights

This page describes the required configurations to utilize Cross Media & Product Connected Insights (Cross Media) accelerator of Cortex Framework Data Foundation.

With this Cross Media accelerator, Cortex Framework Data Foundation is enriched with an initial set of KPIs to understand the effectiveness of marketing campaigns running across media platforms such as Google Ads, YouTube (with DV360), Meta, and TikTok for product and product category sales performance.

The following diagram describes how Cross Media insights are available through the marketing workloads of Cortex Framework Data Foundation:

![CM360 data source](https://docs.cloud.google.com/cortex/docs/images/cross-media-architecture.png)

**Figure 1**. Cross media architecture.

### Configuration file

The [config.json](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to connect to data sources for transferring data from various workloads. This file contains the following parameters for Cross Media:
    
    
      "k9": {
        "datasets": {... },
        "crossMedia": {
          "productHierarchyType": "",
          "maxProductHierarchyMatchLevel": 9,
          "targetCurrencies": ["USD"],
          "additionalPrompt": "",
          "lookbackWindowDays": 7
        }
      },
      "VertexAI": {
        "region": "us-central1",
        "processingDataset": "CORTEX_VERTEX_AI_PROCESSING"
      },
    ...
    
    

The following table describes the value for each parameter:

Parameter  | Meaning  | Default Value   
---|---|---  
`k9.deployCrossMedia` | Whether Cross Media will be deployed. Note that it requires at least one of Google Ads, YouTube (with DV360), Meta or TikTok to be deployed alongside, or the deployment will fail.  | `False`  
`k9.CrossMedia.productHierarchyType` | Which of the product hierarchies to use within the product dim. Dependent on the actual data. Set this value to the same value as your `productHierarchyType` value for the Product Hierarchy Dimension.  | `SAP`  
`k9.CrossMedia.maxProductHierarchyMatchLevel` | Limits the level of the product hierarchy for matching. Companies with a lot of SKUs may have hierarchies going too deep with specifics of packaging (for example, Coca Cola in glass or cans, packaged individually or in batches). Some systems, such as SAP, have their own limit of how deep you can go.  | 9   
`k9.CrossMedia.targetCurrencies` | Target currencies used for Reporting and BI purposes. All source currencies will be converted to these currencies.  | `["USD"]`  
`k9.CrossMedia.additionalPrompt` | Optional: Pass additional prompts to the LLM model.  |   
`k9.CrossMedia.lookbackWindowDays` | Amount of days to lookback when doing incremental refresh  | 7   
`VertexAI.region` | Vertex AI region (assuming source project for Vertex AI API). It must be co-located with BigQuery and must not be a multi-region. If BigQuery is in a multi-region, any region from the same multi-region is acceptable  | `us-central1` (which matches default BigQuery location `us`)   
`VertexAI.processingDataset` | BigQuery dataset for Vertex AI jobs, must be in `VertexAI.region` location and not a multi-region.  | `CORTEX_VERTEX_AI_PROCESSING`  
  
### Data Model

This section describes the Cross Media & Product Connected Insights Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for Cross Media](https://docs.cloud.google.com/cortex/docs/images/erd_cross_media.png)](https://docs.cloud.google.com/cortex/docs/images/erd_cross_media.png)

**Figure 2**. Cross Media & Product Connected Insights: Entity Relationship Diagram.

### Deploying Cross Media

  1. Create a BigQuery dataset in the source project for Vertex AI processing.

**Note:** The location of this dataset should be in the same general region as your datasets, but it can't be in a multi-region. For example, if your other datasets are in `us` then this dataset can be in `us-central1`, but not `us`.
  2. Configure one or more of the following Marketing data sources for deployment, following their own guides:

     1. [Google Ads](https://docs.cloud.google.com/cortex/docs/v6/marketing-googleads)
     2. [Meta](https://docs.cloud.google.com/cortex/docs/v6/marketing-meta)
     3. [Youtube (with DV360)](https://docs.cloud.google.com/cortex/docs/v6/marketing-dv360)
     4. [TikTok](https://docs.cloud.google.com/cortex/docs/v6/marketing-tiktok)
  3. Enable and configure required [Common Dimensions](https://docs.cloud.google.com/cortex/optional-step-common-dimensions):

     1. Country Dimension
     2. Product Dimension
     3. Currency Conversion
  4. Configure Cross Media settings:

     1. Set `k9.deployCrossMedia` to `True`.
     2. Set `k9.CrossMedia.productHierarchyType` to the same value as `dataSourceType` in the previous step.
     3. In `VertexAI` section, set the dataset to the one you created in step 1, and `region` should match where the Vertex AI processing dataset is.
  5. Adjust any other settings as necessary. Then you are ready to start the deployment.




### Running the DAGs

  1. Set up [Managed Service for Apache Airflow Airflow environment](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview) as required. Make sure the `k9_reporting` connection is [configured](https://docs.cloud.google.com/cortex/docs/v6/gathering-settings) correctly.
  2. [Load data](https://docs.cloud.google.com/cortex/optional-step-common-dimensions) into Currency Conversion and Product Hierarchy tables.
  3. Run the `cross_media` DAGs. There are two flavors: "Full refresh" or " Incremental refresh". Use whichever that fits your use case.



### Known issues

If the Currency Conversion table is not populated, `TotalCostInTargetCurrency` column of the final output table will be empty for all rows. In this case you can still use `TotalCostInSourceCurrency` column to report on costs in source currency.

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
