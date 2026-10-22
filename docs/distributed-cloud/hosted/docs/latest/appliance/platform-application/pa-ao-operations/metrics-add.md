---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-add/
title: AddOn Manager (ADD) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:06.151530+00:00
---

# AddOn Manager (ADD)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  AddOn Manager (ADD) Stay organized with collections  Save and categorize content based on your preferences. 

Name and description  |  Type  |  Emit duration  |  Labels   
---|---|---|---  
` add_addon_count `  
Number of AddOn custom resources (CR) in a cluster.  |  Gauge  |  1 m  | 

  * **addon_cluster**
  * **addonset**
  * **addon**
  * **gdch_version**
  * **cluster_version**
  * **chart_version**
  * **addon_status**
  * **addon_drifted**

  
` add_addonset_count `  
Number of AddOnSet CRs in a cluster.  |  Gauge  |  1 m  | 

  * **addon_cluster**
  * **addonset**
  * **gdch_version**
  * **cluster_version**

  
` add_addonsettemplate_count `  
Number of AddOnSetTemplate CRs in a cluster.  |  Gauge  |  1 m  | 

  * **gdch_version**
  * **cluster_version**

  
` add_install_reconcile_time `  
Time to install AddOn.  |  Counter  |  1 m  | 

  * **addon_cluster**
  * **addonset**
  * **addon**
  * **gdch_version**
  * **cluster_version**
  * **addon_operation**
  * **upgrade_from**

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
