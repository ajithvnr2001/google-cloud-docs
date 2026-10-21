---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-logging/
title: Enable GKE logging \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:24.862648+00:00
---

# Enable GKE logging  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-logging/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Enable GKE logging Stay organized with collections  Save and categorize content based on your preferences. 

## Job driver logs

See [Managed Service for Apache Spark job logs in Logging](https://docs.cloud.google.com/managed-spark/docs/guides/logging#job_logs_in) for information on configuring and viewing Managed Service for Apache Spark on GKE Spark job driver logs.

## Cloud Logging

[Enable Logging](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing) to view, search, filter, and archive Managed Service for Apache Spark on GKE logs in Cloud Logging.

You can search for Spark driver and executor logs in Cloud Logging using the following labels:

  * dataproc.googleapis.com/cluster-uuid = Managed Service for Apache Spark cluster UUID
  * dataproc.googleapis.com/job-uuid = Managed Service for Apache Spark job UUID
  * dataproc.googleapis.com/role



Sample queries:
    
    
    labels."k8s-pod/dataproc_googleapis_com/cluster-uuid"="Managed Service for Apache Spark cluster UUID"
    
    
    
    labels."k8s-pod/dataproc_googleapis_com/job-uuid"="Managed Service for Apache Spark job UUID"
    
    
    
    labels."k8s-pod/dataproc_googleapis_com/role"="driver"
    

## What's next

  * Learn how to [access Managed Service for Apache Spark on GKE job and cluster logs in Logging](https://docs.cloud.google.com/managed-spark/docs/guides/logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
