---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/flow-control/
title: Cloud Data Fusion flow control overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:32.007446+00:00
---

# Cloud Data Fusion flow control overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/flow-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Cloud Data Fusion flow control overview Stay organized with collections  Save and categorize content based on your preferences. 

A flow control mechanism in Cloud Data Fusion prevents you from submitting too many requests, which can cause stuck or failed pipeline runs. This mechanism applies to start (`Launch`) requests for the following pipelines and jobs in all editions of Cloud Data Fusion, versions 6.6 and later:

  * Batch pipelines
  * Real-time pipelines
  * Replication jobs



## Thresholds

To control the number of outstanding start requests in Cloud Data Fusion, flow control relies on two thresholds:

Launch threshold
    Limits the number of launch requests being made. If the number of launch requests received by Cloud Data Fusion that are not yet in `Running` state is greater than the launch threshold (number of launch requests that aren't running yet > launch threshold), the request is rejected. The number includes batch pipelines, real-time pipelines, and replication jobs.
Runs threshold
    Limits the number of outstanding launch requests in the system. If the number of outstanding launch requests received by Cloud Data Fusion that have not yet finished is greater than a specified runs threshold (number of outstanding requests that aren't finished yet > runs threshold), the request is rejected.

## Rejected requests

If either threshold is met, every new start request gets rejected. For example, a rejected batch pipeline has a `Rejected` status in the logs, and a dialog in the UI describes why the launch was rejected.

## Metrics

The number of launching and running pipelines along with the number of rejected pipelines in the system can be accessed through the metrics service as follows.

### `Launching` metric

Reports the number of launching requests in the system. That is, it reports the number of launch requests that are in `Provisioning` or `Starting` states.

Metrics name: `flowcontrol.launching.count`
    
    
    POST /v3/metrics/query?metric=system.flowcontrol.launching.count
    

### `Running` metric

Reports the number of running pipelines and jobs in the system. The run threshold is based on the sum of the `Launching` and `Running` metrics values.

Metrics name: `flowcontrol.running.count`
    
    
    POST /v3/metrics/query?metric=system.flowcontrol.running.count
    

### `Rejected` metric

Reports the number of rejected runs due to the flow control mechanism.

Metrics name: `program.rejected.runs`
    
    
    POST /v3/metrics/query?metric=system.program.rejected.runs
    

## What's next

  * For examples of providing tags and aggregating the `Rejected` metric for different pipelines, see [CDAP Metrics Microservices](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692194/Metrics+Microservices#Querying-a-Metric).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
