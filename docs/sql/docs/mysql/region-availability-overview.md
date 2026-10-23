---
url: https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview/
title: Region availability overview \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:36.950491+00:00
---

# Region availability overview  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Region availability overview Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/region-availability-overview "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview "View this page for the SQL Server database engine")

You can choose any available region for your Cloud SQL instance. The region you choose affects the [Cloud SQL edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) and [machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview) available for your instance.

When you can create a new instance, you must select a region for the instance. If you don't select a region when you create an instance, then the region is set to `us-central1` by default.

For more information on the requirements and decisions you need to make prior to creating a new instance, see [Plan and prepare overview](https://docs.cloud.google.com/sql/docs/mysql/plan-prepare-overview).

## Cloud SQL Enterprise edition region support

Cloud SQL Enterprise edition supports the following [regions](https://docs.cloud.google.com/docs/geography-and-regions) and [machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview):

Region | General purpose shared core | General purpose dedicated core | N4 machine series  
---|---|---|---  
`africa-south1` — Johannesburg | ✔ 1 | ✔ 1 | ✔  
`asia-east1` — Taiwan | ✔ | ✔ | ✔  
`asia-east2` — Hong Kong | ✔ | ✔ | ✔  
`asia-northeast1` — Tokyo | ✔ | ✔ | ✔  
`asia-northeast2` — Osaka | ✔ | ✔ | ✔  
`asia-northeast3` — Seoul | ✔ | ✔ | ✔  
`asia-south1` — Mumbai | ✔ | ✔ | ✔  
`asia-south2` — Delhi | ✔ | ✔ | ✔  
`asia-southeast1` — Singapore | ✔ | ✔ | ✔  
`asia-southeast2` — Jakarta | ✔ | ✔ | ✔  
`asia-southeast3` — Bangkok | ✔ | ✔ 2 | ✔  
`australia-southeast1` — Sydney | ✔ | ✔ | ✔  
`australia-southeast2` — Melbourne | ✔ | ✔ | ✔  
`europe-central2` — Warsaw | ✔ | ✔ | ✔  
`europe-north1` \- Finland | ✔ | ✔ | ✔  
`europe-north2` \- Stockholm | ✔ 1 | ✔ 1 | ✔  
`europe-southwest1` \- Madrid | ✔ 1 | ✔ 1 | ✔  
`europe-west1` — Belgium | ✔ | ✔ | ✔  
`europe-west2` — London | ✔ | ✔ | ✔  
`europe-west3` — Frankfurt | ✔ | ✔ | ✔  
`europe-west4` — Netherlands | ✔ | ✔ | ✔  
`europe-west6` — Zürich | ✔ | ✔ | ✔  
`europe-west8` \- Milan | ✔ 1 | ✔ 1 | ✔  
`europe-west9` \- Paris | ✔ 1 | ✔ 1 | ✔  
`europe-west10` \- Berlin | ✔ 1 | ✔ 1 |   
`europe-west12` \- Turin | ✔ 1 | ✔ 1 |   
`me-central1` \- Doha | ✔ 1 | ✔ 1 | ✔  
`me-central2` \- Dammam | ✔ 1 | ✔ 1 | ✔  
`me-west1` \- Tel Aviv | ✔ 1 | ✔ 1 | ✔  
`northamerica-northeast1` — Montréal | ✔ | ✔ | ✔  
`northamerica-northeast2` — Toronto | ✔ | ✔ | ✔  
`northamerica-south1` \- Queretaro | ✔ 1 | ✔ 1 | ✔  
`southamerica-east1` — San Paulo | ✔ | ✔ | ✔  
`southamerica-west1` \- Santiago | ✔ 1 | ✔ 1 | ✔  
`us-central1` — Iowa | ✔ | ✔ | ✔  
`us-east1` — South Carolina | ✔ | ✔ | ✔  
`us-east4` — Northern Virginia | ✔ | ✔ | ✔  
`us-east5` \- Columbus | ✔ 1 | ✔ 1 | ✔  
`us-south1` \- Dallas | ✔ 1 | ✔ 1 | ✔  
`us-west1` — Oregon | ✔ | ✔ | ✔  
`us-west2` — Los Angeles | ✔ | ✔ | ✔  
`us-west3` — Salt Lake City | ✔ | ✔ | ✔  
`us-west4` — Las Vegas | ✔ | ✔ | ✔  
  
1 These regions don't support instances created with 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, and 82 or more [virtual CPUs (vCPUs)](https://docs.cloud.google.com/compute/docs/cpu-platforms).

2 This region only supports the creation of dedicated core instances with one vCPU.

## Cloud SQL Enterprise Plus edition region support

Cloud SQL Enterprise Plus edition supports the following [regions](https://docs.cloud.google.com/docs/geography-and-regions) and [machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview):

Region | N2 machine series | C4A machine series | C4 machine series  
---|---|---|---  
`africa-south1` — Johannesburg | ✔ |  | ✔  
`asia-east1` — Taiwan | ✔ | ✔ |   
`asia-east2` — Hong Kong | ✔ |  | ✔  
`asia-northeast1` — Tokyo | ✔ | ✔ |   
`asia-northeast2` — Osaka | ✔ |  |   
`asia-northeast3` — Seoul | ✔ |  | ✔  
`asia-south1` — Mumbai | ✔ | ✔ |   
`asia-south2` — Delhi | ✔ |  | ✔  
`asia-southeast1` — Singapore | ✔ | ✔ | ✔  
`asia-southeast2` — Jakarta | ✔ | ✔ | ✔  
`australia-southeast1` — Sydney | ✔ |  |   
`australia-southeast2` — Melbourne | ✔ | ✔ | ✔  
`europe-central2` — Warsaw | ✔ |  |   
`europe-north1` \- Finland | ✔ | ✔ |   
`europe-southwest1` — Madrid | ✔ |  |   
`europe-west1` — Belgium | ✔ | ✔ |   
`europe-west2` — London | ✔ | ✔ | ✔  
`europe-west3` — Frankfurt | ✔ | ✔ | ✔  
`europe-west4` — Netherlands | ✔ | ✔ | ✔  
`europe-west6` — Zürich | ✔ |  | ✔  
`europe-west8` — Milan | ✔ |  | ✔  
`europe-west9` — Paris | ✔ |  |   
`europe-west10` — Berlin | ✔ |  |   
`europe-west12` — Turin | ✔ |  |   
`me-central1` — Doha | ✔ |  |   
`me-central2` — Dammam | ✔ |  |   
`me-west1` — Tel Aviv | ✔ |  |   
`northamerica-northeast1` — Montréal | ✔ | ✔ |   
`northamerica-northeast2` — Toronto | ✔ | ✔ |   
`northamerica-south1` — Queretaro |  | ✔ |   
`southamerica-east1` — San Paulo | ✔ | ✔ |   
`southamerica-west1` — Santiago | ✔ | ✔ | ✔  
`us-central1` — Iowa | ✔ | ✔ |   
`us-east1` — South Carolina | ✔ | ✔ |   
`us-east4` — Northern Virginia | ✔ | ✔ |   
`us-east5` — Columbus | ✔ | ✔ | ✔  
`us-south1` — Dallas | ✔ | ✔ | ✔  
`us-west1` — Oregon | ✔ | ✔ |   
`us-west2` — Los Angeles | ✔ | ✔ |   
`us-west3` — Salt Lake City | ✔ |  | ✔  
`us-west4` — Las Vegas | ✔ | ✔ | ✔  
**Note:** C4 machine series may not be available in all zones of the regions listed.

## What's next

  * [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
