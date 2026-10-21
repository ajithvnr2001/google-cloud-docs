---
url: https://docs.cloud.google.com/secure-access-connect/docs/view-attachments/
title: View attachments details \u00a0|\u00a0 Secure Access Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:17.636566+00:00
---

# View attachments details  |  Secure Access Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-access-connect/docs/view-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Access Connect ](https://docs.cloud.google.com/secure-access-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-access-connect/docs/overview)



Send feedback 

#  View attachments details Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view Secure Access Connect attachments and attachment details.

## Required roles

To get the permissions that you need to view attachments details, ask your administrator to grant you the [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View all attachments in a region

To view all attachments in a region, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect Attachments** page.

[Go to Secure Access Connect Attachments](https://console.cloud.google.com/net-security/sac/attachments/list)

  2. On the top left, choose the project that you want to view attachments for. The attachments are displayed on the page.




###  gcloud 

Run the [`gcloud network-security secure-access-connect attachments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/attachments/list):
    
    
    gcloud network-security secure-access-connect attachments list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where the attachments are located



###  API 

Use the [`projects.locations.sacAttachments.list` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacAttachments/list)
    
    
    GET https://networksecurity.googleapis.com/v1/{parent=project/PROJECT_ID/locations/REGION}/sacAttachments
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where the attachment is located



## View attachment details

To view details about an attachment, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect Attachments** page.

[Go to Secure Access Connect Attachments](https://console.cloud.google.com/net-security/sac/attachments/list)

  2. Click the attachment that you want to view details for.




###  gcloud 

Run the [`gcloud network-security secure-access-connect attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/attachments/describe):
    
    
    gcloud network-security secure-access-connect attachments describe ATTACHMENT_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `ATTACHMENT_ID`: the ID of the attachment
  * `PROJECT_ID`: your project ID
  * `REGION`: the region where the attachments are located



###  API 

Use the [`projects.locations.sacAttachments.get` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacAttachments/get)
    
    
    GET https://networksecurity.googleapis.com/v1/{parent=project/PROJECT_ID/locations/REGION}/sacAttachments/ATTACHMENT_ID
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where the attachment is located
  * `ATTACHMENT_ID`: the ID of the attachment



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
