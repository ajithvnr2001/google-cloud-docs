---
url: https://docs.cloud.google.com/secure-access-connect/docs/delete-realms-attachments/
title: Delete realms and attachments \u00a0|\u00a0 Secure Access Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:22.895142+00:00
---

# Delete realms and attachments  |  Secure Access Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-access-connect/docs/delete-realms-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Access Connect ](https://docs.cloud.google.com/secure-access-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-access-connect/docs/overview)



Send feedback 

#  Delete realms and attachments Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to delete realms and attachments. After you create a realm, you can't edit it. If you want to make changes to the realm, you must delete it and create a new realm.

## Required roles

  * For all SSE providers:  


To get the permissions that you need to delete realms and attachments, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * For Symantec Cloud SWG ([Public preview)](https://cloud.google.com/products#product-launch-stages):  


To ensure that [Network Security Service Account](https://docs.cloud.google.com/iam/docs/service-agents#network-security-service-account) has the necessary permissions to delete attachments and their corresponding Symantec locations, ask your administrator to grant the [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) IAM role to [Network Security Service Account](https://docs.cloud.google.com/iam/docs/service-agents#network-security-service-account) on the project. **Important:** You must grant this role to [Network Security Service Account](https://docs.cloud.google.com/iam/docs/service-agents#network-security-service-account), _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give [Network Security Service Account](https://docs.cloud.google.com/iam/docs/service-agents#network-security-service-account) the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Additionally, make sure that the API credentials you stored in Secret Manager when you [created the realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms#create-realm) are still valid. If the credentials aren't valid, create and upload a new API key.




## Delete attachments

To delete attachments, do the following.

**Note:** If you use Symantec Cloud SWG (Public preview), deleting an attachment also deletes the Symantec location that is connected to the attachment.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect Attachments** page.

[Go to Secure Access Connect Attachments](https://console.cloud.google.com/net-security/sac/attachments/list)

  2. Select the attachment that you want to delete.

  3. Click delete**Delete**.




###  gcloud 

Run the [`gcloud network-security secure-access-connect attachments delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/attachments/delete):
    
    
    gcloud network-security secure-access-connect attachments delete ATTACHMENT_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `ATTACHMENT_ID`: the attachment ID
  * `PROJECT_ID`: the project that contains the attachment
  * `REGION`: the region where the attachment is located



###  API 

Use the [`projects.locations.sacAttachments.delete` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacAttachments/delete)
    
    
    DELETE https://networksecurity.googleapis.com/v1/{name=project/PROJECT_ID/locations/REGION}/sacAttachments/ATTACHMENT_ID
    

Replace the following:

  * `PROJECT_ID`: the project that contains the attachment
  * `REGION`: the region where the attachment is located
  * `ATTACHMENT_ID`: the attachment ID



## Delete realms

You must delete all attachments before you can delete a realm. To delete a realm, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect** page.

[Go to Secure Access Connect Realms](https://console.cloud.google.com/net-security/sac/realms)

  2. Choose the realm that you want to delete.

  3. Click delete**Delete**.




###  gcloud 

Run the [`gcloud network-security secure-access-connect realms delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/delete):
    
    
    gcloud network-security secure-access-connect realms delete REALM_ID \
        --project=PROJECT_ID
    

Replace the following:

  * `REALM_ID`: the realm ID
  * `PROJECT_ID`: the project that contains the realm



###  API 

Use the [`projects.locations.sacRealms.delete` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacRealms/delete)
    
    
    DELETE https://networksecurity.googleapis.com/v1/project/PROJECT_ID/locations/global/sacRealms/REALM_ID
    

Replace the following:

  * `PROJECT_ID`: the project that contains the realm
  * `REALM_ID`: the realm ID



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
