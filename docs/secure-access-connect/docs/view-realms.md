---
url: https://docs.cloud.google.com/secure-access-connect/docs/view-realms/
title: View realm details \u00a0|\u00a0 Secure Access Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:21.742642+00:00
---

# View realm details  |  Secure Access Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-access-connect/docs/view-realms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Access Connect ](https://docs.cloud.google.com/secure-access-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-access-connect/docs/overview)



Send feedback 

#  View realm details Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view Secure Access Connect realms and realm details.

## Required roles

To get the permissions that you need to view realm details, ask your administrator to grant you the [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View all realms in a project

To view all realms in a project, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect Realms** page.

[Go to Secure Access Connect Realms](https://console.cloud.google.com/net-security/sac/realms)

  2. On the top left, choose the project that you want to view realms for. The realms are displayed on the page.




###  gcloud 

Run the [`gcloud network-security secure-access-connect realms list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/list).
    
    
      gcloud network-security secure-access-connect realms list \
          --project=PROJECT_ID
    

Replace `PROJECT_ID` with your project ID.

###  API 

Use the [`projects.locations.sacRealms.list` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacRealms/list)
    
    
    GET https://networksecurity.googleapis.com/v1/project/PROJECT_ID/locations/global/sacRealms
    

Replace `PROJECT_ID` with your project ID.

## View realm details

To view the details of a specific realm, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect Realms** page.

[Go to Secure Access Connect Realms](https://console.cloud.google.com/net-security/sac/realms)

  2. Click the realm that you want to view details for.




###  gcloud 

Run the [`gcloud network-security secure-access-connect realms describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/describe):
    
    
      gcloud network-security secure-access-connect realms describe REALM_ID \
          --project=PROJECT_ID
    

Replace the following:

  * `REALM_ID`: the ID of the realm
  * `PROJECT_ID`: your project ID



###  API 

Use the [`projects.locations.sacRealms.get` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacRealms/get)
    
    
    GET https://networksecurity.googleapis.com/v1/project/PROJECT_ID/locations/global/sacRealms/REALM_ID
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REALM_ID`: the ID of the realm



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
