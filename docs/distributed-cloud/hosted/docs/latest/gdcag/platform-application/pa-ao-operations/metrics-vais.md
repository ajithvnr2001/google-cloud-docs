---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-vais/
title: Agent Search (VAIS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:18.082148+00:00
---

# Agent Search (VAIS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-vais/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Agent Search (VAIS) Stay organized with collections  Save and categorize content based on your preferences. 

Name and description  |  Type  |  Emit duration  |  Labels   
---|---|---|---  
`vaisearch_task_processing_latency`:  
Ingestion task execution time   
The time it takes for an ingestion task to complete (0.95 quantile).  |  Gauge  |  1 m  |  **task** : `IngestDocument`  
`vaisearch_task_processing_count_total`:  
TASK success versus failure rate   
The number of successes and failures for a task.  |  Gauge  |  1 m  | 

  * **task** : for example, `IngestDocument`
  * **status** : `Success` or `Failure`

  
`gdcai_api_latency_bucket`:  
SERVICE_NAME service API latency   
The time it takes for the service to respond (0.95 quantile).  |  Gauge  |  1 m  | 

  * **service** : for example, `DatasetService`
  * **method** : for example, `ListDatasets`

  
`gdcai_api_requests_total`:  
SERVICE_NAME service request   
The total number of requests to a service.  |  Gauge  |  1 m  | 

  * **service** : for example, `DatasetService`
  * **method** : for example, `ListDatasets`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
