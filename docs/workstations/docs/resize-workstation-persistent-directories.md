---
url: https://docs.cloud.google.com/workstations/docs/resize-workstation-persistent-directories/
title: Resize workstation persistent directories \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:08.205822+00:00
---

# Resize workstation persistent directories  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/resize-workstation-persistent-directories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Resize workstation persistent directories Stay organized with collections  Save and categorize content based on your preferences. 

To avoid running out of disk space, you can increase the size of a workstation's persistent directories without recreating the workstation.

## Before you begin

Before you resize a workstation's persistent directories, stop the workstation.

## Resize persistent directories

Use the following command to resize your persistent directory:
    
    
      gcloud beta workstations update WORKSTATION_NAME --pd-disk-size=TARGET_SIZE_GB \
        --project=PROJECT_ID --region=REGION --cluster=CLUSTER_NAME --config=CONFIG_NAME
    

Replace the following:

  * `WORKSTATION_NAME`: the name of the workstation.
  * `TARGET_SIZE_GB`: the new size, in GB, for the persistent directory. The value must be larger than the current size.
  * `PROJECT_ID`: the project that contains the workstation.
  * `REGION`: the region where the workstation resides.
  * `CLUSTER_NAME`: the name of the workstation cluster.
  * `CONFIG_NAME`: the name of the workstation configuration.



A successful update operation increases the size of the underlying persistent disk. However, the workstation's file system is expanded to match the new disk size only when the workstation is next started. You can verify that the storage capacity has been updated by running a command like `df -h` or `lsblk` inside your workstation terminal after starting it.

Every resize operation automatically generates a snapshot of the underlying persistent disk. This snapshot is created in case the resize operation fails or if you need to roll back your changes. The snapshot is automatically deleted after three weeks. Standard snapshot pricing applies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
