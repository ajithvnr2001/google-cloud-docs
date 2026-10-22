---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-default-service-accounts/
title: Troubleshooting default service accounts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:27.857223+00:00
---

# Troubleshooting default service accounts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-default-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting default service accounts Stay organized with collections  Save and categorize content based on your preferences. 

To access Google Cloud resources, Compute Engine virtual machine (VM) instances use [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview). If you accidentally delete the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), applications that run on your VMs might not be able to make calls to Google Cloud APIs.

This document explains how to recover the Compute Engine default service account after it is deleted.

## Recover the Compute Engine default service account

When you delete a service account, Identity and Access Management (IAM) permanently removes the service account after 30 days. If you accidentally delete the Compute Engine default service account, Google Cloud cannot recover the service account after it is permanently removed and then the VMs will no longer have access to resources in the project. In such cases, if you want to assign a Compute Engine default service account for the VM, create a service account and set it as the default service account.

To get the permissions that you need to perform this task, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To recover a deleted Compute Engine default service account, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

Use the following query to validate when the Compute Engine default service account was deleted:
         
         resource.type="service_account"
         protoPayload.methodName="google.iam.admin.v1.DeleteServiceAccount"
         "PROJECT_NUMBER-compute@developer.gserviceaccount.com"
         

Replace `PROJECT_NUMBER` with the project number of your project.

**If the default service account was deleted less than 30 days ago** :

Use the `undelete` command to recover the service account. For more information, see [Undelete a service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting).

**If the default service account was deleted more than 30 days ago** :

     1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) or select an existing service account to set as the new Compute Engine default service account.
  2. If you want VMs to use the newly created default service account, [follow these steps](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes):

     1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the VM instance name for which you want to use the service account.

     3. If the VM is running, click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

     4. Click **Edit**.

     5. Scroll down to the **Service Account** section.

     6. From the drop-down list, select the service account to assign to the instance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
