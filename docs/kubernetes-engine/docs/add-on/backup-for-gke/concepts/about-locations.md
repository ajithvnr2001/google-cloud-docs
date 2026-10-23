---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations/
title: Backup for GKE locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:12.808148+00:00
---

# Backup for GKE locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Backup for GKE locations Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how resource locations impact the operation of the Backup for GKE service.

Backup for GKE provides two types of top-level resources (`BackupPlans` and `RestorePlans`). These resources are always created within a resource hierarchy that includes project ID and location. As a regional service, Backup for GKE locations are always [Google Cloud regions](https://docs.cloud.google.com/compute/docs/regions-zones).

Backup for GKE resource regions have these implications:

  * **`BackupPlan`**

    * Defines the region where all backup artifacts produced by the `BackupPlan` will be stored (both config backups and volume backups). If the cluster being backed up using a `BackupPlan`is in a different region than the `BackupPlan`, this could incur inter-region data transfer fees when performing those backups.

**Note:** `VolumeBackup` resources (nested below `BackupPlan` and `Backup` resources) may contain a reference to a global snapshot resource. However, even though the resource location is global, the data associated with that snapshot is restricted to the `BackupPlan` resource's region.
    * Defines the allowed region for CMEK keys (see [About CMEK encryption](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek)). If you want to register a CMEK key for encrypting backup artifacts, the key must have the same region as the `BackupPlan`.

  * **`RestorePlan`**

    * Defines the region where backup artifacts will be restored. The target cluster referenced in a `RestorePlan` must be either a zonal or regional cluster within the same region as the `RestorePlan`. If the `RestorePlan` region is different than the `BackupPlan` region, this could incur inter-region data transfer fees when performing those restores.



Backup for GKE is available in the following regions:

###  Northern America 

Region Name | Region Description  
---|---  
northamerica-northeast1 | Montréal  
northamerica-northeast2 | Toronto  
northamerica-south1 | Queretaro  
us-central1 | Iowa  
us-east1 | South Carolina  
us-east4 | Northern Virginia  
us-east5 | Columbus  
us-south1 | Dallas  
us-west1 | Oregon  
us-west2 | Los Angeles  
us-west3 | Salt Lake City  
us-west4 | Las Vegas  
us-west8 | Phoenix  
  
###  Europe 

Region Name | Region Description  
---|---  
europe-central2 | Warsaw  
europe-north1 | Finland  
europe-north2 | Stockholm  
europe-southwest1 | Madrid  
europe-west1 | Belgium  
europe-west10 | Berlin  
europe-west12 | Turin  
europe-west2 | London  
europe-west3 | Frankfurt  
europe-west4 | Netherlands  
europe-west6 | Zurich  
europe-west8 | Milan  
europe-west9 | Paris  
  
###  Asia 

Region Name | Region Description  
---|---  
asia-east1 | Taiwan  
asia-east2 | Hong Kong  
asia-northeast1 | Tokyo  
asia-northeast2 | Osaka  
asia-northeast3 | Seoul  
asia-south1 | Mumbai  
asia-south2 | Delhi  
asia-southeast1 | Singapore  
asia-southeast3 | Bangkok  
  
###  Indonesia 

Region Name | Region Description  
---|---  
asia-southeast2 | Jakarta  
  
###  Oceania 

Region Name | Region Description  
---|---  
australia-southeast1 | Sydney  
australia-southeast2 | Melbourne  
  
###  Middle East 

Region Name | Region Description  
---|---  
me-central1 | Doha  
me-central2 | Dammam  
me-west1 | Tel Aviv  
  
###  Latin America 

Region Name | Region Description  
---|---  
southamerica-east1 | São Paulo  
southamerica-west1 | Santiago  
  
###  Africa 

Region Name | Region Description  
---|---  
africa-south1 | Johannesburg  
  
You can also get a list of current regions supported by Backup for GKE by running the following command:
    
    
    gcloud beta container backup-restore locations list \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with the ID of your Google Cloud project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
