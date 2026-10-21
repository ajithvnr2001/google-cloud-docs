---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-diagnose-cluster/
title: Diagnose GKE clusters \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:46.038978+00:00
---

# Diagnose GKE clusters  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-diagnose-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Diagnose GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark provides a [gcloud CLI dataproc clusters diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/diagnose) command to help you troubleshoot Managed Service for Apache Spark on GKE cluster and job issues. This command gathers and archives cluster-related configuration files, logs, and outputs into an archive file. and then uploads the archive to the Cloud Storage staging bucket you specified when you [created your Managed Service for Apache Spark on GKE cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/dataproc-gke-quickstart-create-cluster#create_a_on_cluster).

## Diagnose archive file

The following tables list metrics and other information included in the `dataproc clusters diagnose` command archive file.

### System information

Item | Archive location  
---|---  
**GKE node metrics where virtual Managed Service for Apache Spark on GKE pods run:**  
  
  * CPU usage
  * Memory usage

|  `/system/NODE_NAME.json`  
**Network metrics and file system status of running pods:**  
  
  * CPU usage
  * Memory usage
  * Network status
  * Filesystem status

| `/system/POD_NAME.json`  
  
### Configuration information

Item | Archive location  
---|---  
Cluster configmap | `/conf/configmap`  
Kubernetes deployment | `/conf/deployment`  
[Role Based Access Control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac) | 

  * `/conf/role`
  * `/conf/rolebind`
  * `/conf/serviceaccount`

  
  
### Logs

Item | Archive location  
---|---  
Agent log | `/logs/agent.log`  
Spark engine log | `/logs/sparkengine.log`  
Spark driver running and completed job logs over the last 24 hours | `/logs/DRIVER_ID`  
  
## Job and pod information

Item | Archive location  
---|---  
JobAttempt object | `/jobattempts`  
Kubernetes Pod object | `/pods`  
  
## What's next

  * See [Diagnose Managed Service for Apache Spark clusters](https://docs.cloud.google.com/managed-spark/docs/support/diagnose-command#sharing_the_data_gathered_by_diagnose).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
