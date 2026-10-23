---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/vpc-sc/
title: Protect Backup for GKE resources using VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:44.490929+00:00
---

# Protect Backup for GKE resources using VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Protect Backup for GKE resources using VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to use VPC Service Controls to protect Backup for GKE resources. For more information about VPC Service Controls, read the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

Ensure that you have the [required IAM permissions](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) to administer VPC Service Controls.

## Create a service perimeter to protect Backup for GKE resources

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your Organization.

  3. On the **VPC Service Controls** page, click **New Perimeter**.

  4. On the **New VPC Service Perimeter** page, in the **Perimeter Name** box, type a name for the perimeter.

  5. Select the projects that you want to secure within the perimeter:

     1. Click **Add Projects** button.

     2. To add a project to the perimeter, in the **Add Projects** dialog, select that project's checkbox.

     3. Click **Add n Projects** button, where n is the number of projects you selected in the previous step.

  6. Select Backup for GKE to secure within the perimeter:

     1. Click **Add Services** button.

     2. To secure Backup for GKE within the perimeter, in the **Specify services to restrict** dialog, select Backup for GKE's checkbox.

     3. Click **Add Backup for GKE API** button.

  7. Click **Save** button.




You've created a service perimeter that restricts access to Backup for GKE resources. The service perimeter may take up to 30 minutes to propagate and take effect. When the changes have propagated, access to Backup for GKE will be limited for the projects you added to the perimeter. For example, no backup plan or backup can be created from outside of the perimeter, unless otherwise explicitly allowed by an ingress rule.

## Details about how Backup for GKE works with service perimeters

  1. If Backup for GKE is not among the list of VPC accessible services of a service perimeter, backup and restore may fail even if you are able to create backup or restore using the Google Cloud console or gcloud CLI. This is because the Backup for GKE agent is running in your GKE cluster (within the service perimeter) and requires access to Backup for GKE to perform backup and restore.

  2. To perform cross-project backups and restores successfully, the `backup_project`, `cluster_project`, and `restore_project` should be within the same VPC Service Controls perimeter.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
