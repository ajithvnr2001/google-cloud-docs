---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-upg/
title: Upgrade orchestrator (UPG) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:29:18.697060+00:00
---

# Upgrade orchestrator (UPG)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-upg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Upgrade orchestrator (UPG) Stay organized with collections  Save and categorize content based on your preferences. 

Name and description  |  Type  |  Emit duration  |  Labels   
---|---|---|---  
` upgrade_status `  
The status of an upgrade.  |  StateSet  |  1 m  | 

  * **step:** the step in the upgrade 
  * **parentStep:** the parent step for this upgrade step 
  * **name:** the name of the user cluster upgrade 
  * **current_version:** the current version of GDC 
  * **target_version:** the target version for GDC to upgrade to 

  
` upgrade_duration `  
The number of minutes a step in the upgrade has taken.  |  Gauge  |  1 m  | 

  * **step:** the step in the upgrade 
  * **parentStep:** the parent step for this upgrade step 
  * **name:** the name of the user cluster upgrade 
  * **current_version:** the current version of GDC 
  * **target_version:** the target version for GDC to upgrade to 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
