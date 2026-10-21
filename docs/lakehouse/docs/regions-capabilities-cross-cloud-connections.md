---
url: https://docs.cloud.google.com/lakehouse/docs/regions-capabilities-cross-cloud-connections/
title: Supported regions and CCI capabilities \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:54.318883+00:00
---

# Supported regions and CCI capabilities  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/regions-capabilities-cross-cloud-connections/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Supported regions and CCI capabilities Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, email [biglake-help@google.com](mailto:biglake-help@google.com).

This section maps AWS regions to _Google Cloud_ regions for querying remote data and outlines the _Cross-Cloud Interconnect_ (CCI) capabilities.

## Interconnect classifications

Each AWS region has the following interconnect types, based on physical proximity and service capabilities:

  * **Partner CCI:** These regions are officially pre-provisioned, jointly engineered pairs with Google Cloud partners using the Partner Interconnect (Partner CCI) service.
  * **Low Latency Dedicated:** The AWS region, the interconnect facility, and the closest Google Cloud region are in the same geographical metropolitan area. This offers the lowest latencies.
  * **Standard Dedicated CCI** : These AWS regions are globally supported through a Dedicated CCI, but do not exist in the same metropolitan area as both a Google Cloud interconnect facility and a Google Cloud region.



#### Considerations

  * AWS regions that are not designated as **Partner CCI** or **Low Latency Dedicated** are considered **Standard Dedicated CCI**. These regions are globally supported through Dedicated CCI, but are not located in the same area as both a Google Cloud interconnect facility and a Google Cloud region.

  * If possible, choose regions with **Low Latency Dedicated** or **Partner CCI** to ensure optimal performance when you federate large datasets across clouds.




## AWS to Google Cloud region mapping

AWS Region Name | AWS Region Metro | Closest Google Cloud Region Name | Closest Google Cloud Region Metro | Partner CCI | Low Latency | Top 3 Alternative Google Cloud Regions  
---|---|---|---|---|---|---  
**`us-east-1`** | N. Virginia | `us-east4` | Ashburn, VA | ✓ | ✓ | us-east1, us-east5, us-central1  
**`us-east-2`** | Ohio | `us-east5` | Columbus, OH |  | ✓ | us-east4, us-east1, us-central1  
**`us-west-1`** | N. California | `us-west2` | Los Angeles, CA | ✓ |  | us-west4, us-west1, us-west3  
**`us-west-2`** | Oregon | `us-west1` | The Dalles, OR | ✓ | ✓ | us-west3, us-west4, us-west2  
**`ca-central-1`** | Montreal | `northamerica-northeast1` | Montreal |  | ✓ | northamerica-northeast2, us-east4, us-east5  
**`sa-east-1`** | São Paulo | `southamerica-east1` | São Paulo |  | ✓ | southamerica-west1, us-east1, us-south1  
**`eu-west-1`** | Ireland | `europe-west1` | Belgium |  |  | europe-west2, europe-west9, europe-west4  
**`eu-west-2`** | London | `europe-west2` | London | ✓ | ✓ | europe-west1, europe-west9, europe-west4  
**`eu-west-3`** | Paris | `europe-west9` | Paris |  | ✓ | europe-west1, europe-west2, europe-west3  
**`eu-central-1`** | Frankfurt | `europe-west3` | Frankfurt | ✓ | ✓ | europe-west4, europe-west1, europe-west6  
**`eu-central-2`** | Zurich | `europe-west6` | Zurich |  |  | europe-west8, europe-west12, europe-west3  
**`eu-north-1`** | Stockholm | `europe-north2` | Stockholm | ✓ | ✓ | europe-north1, europe-west4, europe-central2  
**`eu-south-1`** | Milan | `europe-west8` | Milan |  |  | europe-west12, europe-west6, europe-west3  
**`eu-south-2`** | Spain (Aragon) | `europe-southwest1` | Madrid |  |  | europe-west9, europe-west1, europe-west8  
**`me-central-1`** | UAE | `me-central1` | Doha |  |  | me-central2, me-west1, asia-south1  
**`me-south-1`** | Bahrain | `me-central2` | Dammam |  |  | me-central1, me-west1, asia-south1  
**`af-south-1`** | Cape Town | `europe-southwest1` | Madrid |  |  | me-central2, me-west1, europe-west1  
**`ap-east-1`** | Hong Kong | `asia-east2` | Hong Kong |  | ✓ | asia-east1, asia-southeast3, asia-southeast1  
**`ap-northeast-1`** | Tokyo | `asia-northeast1` | Tokyo |  | ✓ | asia-northeast2, asia-northeast3, asia-east1  
**`ap-northeast-2`** | Seoul | `asia-northeast3` | Seoul |  | ✓ | asia-northeast2, asia-northeast1, asia-east1  
**`ap-northeast-3`** | Osaka | `asia-northeast2` | Osaka |  | ✓ | asia-northeast1, asia-northeast3, asia-east1  
**`ap-south-1`** | Mumbai | `asia-south1` | Mumbai |  | ✓ | asia-south2, me-central1, asia-southeast1  
**`ap-south-2`** | Hyderabad | `asia-south2` | Delhi |  |  | asia-south1, asia-southeast1, me-central1  
**`ap-southeast-1`** | Singapore | `asia-southeast1` | Singapore | ✓ | ✓ | asia-southeast2, asia-southeast3, asia-east1  
**`ap-southeast-2`** | Sydney | `australia-southeast1` | Sydney | ✓ | ✓ | australia-southeast2, asia-southeast2, asia-southeast1  
**`ap-southeast-3`** | Jakarta | `asia-southeast2` | Jakarta |  | ✓ | asia-southeast1, asia-southeast3, australia-southeast1  
  
## What's next

  * Set up a cross-cloud connection for [AWS Glue](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue), [Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks), [Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake), [Workday Data Lake](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday), or [SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
