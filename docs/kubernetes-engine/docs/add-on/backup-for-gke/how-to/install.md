---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install/
title: Enable Backup for GKE API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:30.400713+00:00
---

# Enable Backup for GKE API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Enable Backup for GKE API Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to enable [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.

* Ensure that you have the [Service Usage Admin](https://docs.cloud.google.com/service-usage/docs/access-control) (`roles/serviceusage.serviceUsageAdmin`) role on your project. This role is required to enable the Backup for GKE API. 

## Enable the Backup for GKE API

The Backup for GKE service is automatically enabled in any project where the GKE API is enabled. This lets you to improve the data protection posture of your GKE clusters by making use of the Backup for GKE service.

Enabling the Backup for GKE API alone doesn't modify any existing GKE cluster configurations or affect the running workloads. Also, it doesn't automatically create backups or incur additional costs. Costs are only incurred when you create and store backups using the Backup for GKE service.

If you manually disabled the Backup for GKE service, you can enable the Backup for GKE service by using the Google Cloud CLI, Google Cloud console, or Terraform.

### gcloud

To enable the Backup for GKE service, run the following command:
    
    
    gcloud services enable gkebackup.googleapis.com
    

### Console

In the Google Cloud console, enable the Backup for GKE API:

[Enable the API](https://console.cloud.google.com/apis/library/gkebackup.googleapis.com)

### Terraform

Create an appropriate `"google_project_service"` resource to enable the `gkebackup.googleapis.com` service:
    
    
    resource "google_project_service" "my_service" {
       project = "my_project"
       service = "gkebackup.googleapis.com"
    }
    

For more information, see [google_project_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service).

## What's next

  * Learn more about [defining custom backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application).
  * Learn more about [planning a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
