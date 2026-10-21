---
url: https://docs.cloud.google.com/memorystore/docs/memcached/regions/
title: Regions and zones \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:01:02.077808+00:00
---

# Regions and zones  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/regions/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/memcached/resources)



Send feedback 

#  Regions and zones Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** In order to connect to a Memorystore for Memcached instance, the connecting client must be located within the same region as the instance.

Memorystore for Memcached instances live in zones within regions. A region is a specific geographical location where you can run your resources. Each region is subdivided into several zones. For example, the `us-central1` region in the central United States has zones `us-central1-a`, `us-central1-b`, `us-central1-c`, and `us-central1-f`.

For more information, see [Geography and Regions](https://docs.cloud.google.com/docs/geography-and-regions).

Some Google Cloud APIs, including the [Memorystore API](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest), use the concept of locations, which can represent either regions or zones. For the Memorystore API, locations map to regions.

Although you can connect resources in different zones within the same region, you should provision resources in the same zone to improve network performance.

## Supported regions

Memorystore for Memcached is available in the following regions and zones:

Region Name | Region Description | Zones  
---|---|---  
`africa-south1` | Johannesburg | 

  * `africa-south1-a`
  * `africa-south1-b`
  * `africa-south1-c`

  
`asia-east1` | Taiwan | 

  * `asia-east1-a`
  * `asia-east1-b`
  * `asia-east1-c`

  
`asia-east2` | Hong Kong | 

  * `asia-east2-a`
  * `asia-east2-b`
  * `asia-east2-c`

  
`asia-northeast1` | Tokyo | 

  * `asia-northeast1-a`
  * `asia-northeast1-b`
  * `asia-northeast1-c`

  
`asia-northeast2` | Osaka | 

  * `asia-northeast2-a`
  * `asia-northeast2-b`
  * `asia-northeast2-c`

  
`asia-northeast3` | Seoul | 

  * `asia-northeast3-a`
  * `asia-northeast3-b`
  * `asia-northeast3-c`

  
`asia-south1` | Mumbai | 

  * `asia-south1-a`
  * `asia-south1-b`
  * `asia-south1-c`

  
`asia-south2` | Delhi | 

  * `asia-south2-a`
  * `asia-south2-b`
  * `asia-south2-c`

  
`asia-southeast1` | Singapore | 

  * `asia-southeast1-a`
  * `asia-southeast1-b`
  * `asia-southeast1-c`

  
`asia-southeast2` | Jakarta | 

  * `asia-southeast2-a`
  * `asia-southeast2-b`
  * `asia-southeast2-c`

  
`asia-southeast3` | Bangkok | 

  * `asia-southeast3-a`
  * `asia-southeast3-b`
  * `asia-southeast3-c`

  
`australia-southeast1` | Sydney | 

  * `australia-southeast1-a`
  * `australia-southeast1-b`
  * `australia-southeast1-c`

  
`australia-southeast2` | Melbourne | 

  * `australia-southeast2-a`
  * `australia-southeast2-b`
  * `australia-southeast2-c`

  
`europe-central2` | Warsaw | 

  * `europe-central2-a`
  * `europe-central2-b`
  * `europe-central2-c`

  
`europe-north1` | Finland | 

  * `europe-north1-a`
  * `europe-north1-b`
  * `europe-north1-c`

  
`europe-north2` | Stockholm | 

  * `europe-north2-a`
  * `europe-north2-b`
  * `europe-north2-c`

  
`europe-southwest1` | Madrid | 

  * `europe-southwest1-a`
  * `europe-southwest1-b`
  * `europe-southwest1-c`

  
`europe-west1` | Belgium | 

  * `europe-west1-b`
  * `europe-west1-c`
  * `europe-west1-d`

  
`europe-west2` | London | 

  * `europe-west2-a`
  * `europe-west2-b`
  * `europe-west2-c`

  
`europe-west3` | Frankfurt | 

  * `europe-west3-a`
  * `europe-west3-b`
  * `europe-west3-c`

  
`europe-west4` | Netherlands | 

  * `europe-west4-a`
  * `europe-west4-b`
  * `europe-west4-c`

  
`europe-west6` | Zurich | 

  * `europe-west6-a`
  * `europe-west6-b`
  * `europe-west6-c`

  
`europe-west8` | Milan | 

  * `europe-west8-a`
  * `europe-west8-b`
  * `europe-west8-c`

  
`europe-west9` | Paris | 

  * `europe-west9-a`
  * `europe-west9-b`
  * `europe-west9-c`

  
`europe-west10` | Berlin | 

  * `europe-west10-a`
  * `europe-west10-b`
  * `europe-west10-c`

| `europe-west12` | Turin | 

  * `europe-west12-a`
  * `europe-west12-b`
  * `europe-west12-c`

  
`me-central1` | Doha | 

  * `me-central1-a`
  * `me-central1-b`
  * `me-central1-c`

  
`me-central2` | Dammam | 

  * `me-central2-a`
  * `me-central2-b`
  * `me-central2-c`

  
`me-west1` | Tel Aviv | 

  * `me-west1-a`
  * `me-west1-b`
  * `me-west1-c`

  
`northamerica-northeast1` | Montreal | 

  * `northamerica-northeast1-a`
  * `northamerica-northeast1-b`
  * `northamerica-northeast1-c`

  
`northamerica-northeast2` | Toronto | 

  * `northamerica-northeast2-a`
  * `northamerica-northeast2-b`
  * `northamerica-northeast2-c`

  
`northamerica-south1` | Querétaro | 

  * `northamerica-south1-a`
  * `northamerica-south1-b`
  * `northamerica-south1-c`

  
`southamerica-east1` | São Paulo | 

  * `southamerica-east1-a`
  * `southamerica-east1-b`
  * `southamerica-east1-c`

  
`us-central1` | Iowa | 

  * `us-central1-a`
  * `us-central1-b`
  * `us-central1-c`

  
`us-east1` | South Carolina | 

  * `us-east1-b`
  * `us-east1-c`
  * `us-east1-d`

  
`us-east4` | Northern Virginia | 

  * `us-east4-a`
  * `us-east4-b`
  * `us-east4-c`

  
`us-east5` | Columbus | 

  * `us-east5-a`
  * `us-east5-b`
  * `us-east5-c`

  
`us-south1` | Dallas | 

  * `us-south1-a`
  * `us-south1-b`
  * `us-south1-c`

  
`us-west1` | Oregon | 

  * `us-west1-a`
  * `us-west1-b`
  * `us-west1-c`

  
`us-west2` | Los Angeles | 

  * `us-west2-a`
  * `us-west2-b`
  * `us-west2-c`

  
`us-west3` | Salt Lake City | 

  * `us-west3-a`
  * `us-west3-b`
  * `us-west3-c`

  
`us-west4` | Las Vegas | 

  * `us-west4-a`
  * `us-west4-b`
  * `us-west4-c`

  
  
## What's next

  * [Create a Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/creating-managing-instances).
  * Learn about Memorystore for Memcached [Instance and node properties](https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
