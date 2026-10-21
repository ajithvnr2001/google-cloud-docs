---
url: https://docs.cloud.google.com/secure-access-connect/docs/create-realms/
title: Create a realm \u00a0|\u00a0 Secure Access Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:18.739166+00:00
---

# Create a realm  |  Secure Access Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-access-connect/docs/create-realms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Access Connect ](https://docs.cloud.google.com/secure-access-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-access-connect/docs/overview)



Send feedback 

#  Create a realm Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Secure Access Connect realm. A Secure Access Connect realm establishes a connection between your Google Cloud project and an SSE service.

## Before you begin

Before you begin, do the following:

  * Set up one of the following SSE partner services:

    * [Palo Alto Networks Prisma Access](https://docs.paloaltonetworks.com/prisma-access/integration/ncc-gateway-integration-in-prisma-access)
    * [Symantec Cloud Secure Web Gateway (Cloud SWG)](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/conn-matrix/adm_addlocation_st/express-connect.html) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * [Set up NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview) and [create a global hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-hub)




### Required roles

To get the permissions that you need to create realms, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Secure Access Connect realm

Create a Secure Access Connect realm by following the instructions that correspond with your SSE provider.

**Note:** When you create a realm, Secure Access Connect attachments must be in the same project and region as the NCC Gateway spoke.

### Palo Alto Networks Prisma Access

To create a realm, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect** page.

[Go to Secure Access Connect Realms](https://console.cloud.google.com/net-security/sac/realms)

  2. Click **Create Realm**.

  3. Enter a name for the realm that you want to create.

  4. In the **Security service** field, choose **Palo Alto Networks Prisma Access**.

  5. Click **Create**.




###  gcloud 

  1. Create a realm by running the [`gcloud network-security secure-access-connect realms create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/create):
         
         gcloud network-security secure-access-connect realms create REALM_ID \
               --security-service=prisma-access
         

Replace `REALM_ID` with a name for your realm.

  2. Identify the pairing key for the realm by running the [`gcloud network-security secure-access-connect realms describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/describe):
         
         gcloud network-security secure-access-connect realms describe REALM_ID \
               --project=PROJECT_ID
         

Replace the following:

     * `REALM_ID`: the name of your realm
     * `PROJECT_ID`: your project ID

The output is similar to the following:
    
    createTime: '...'
    name: ...
    pairingKey:
      expireTime: '...'
      key: 12345678-0000-4321-1234-abcdefghijkl
    securityService: PALO_ALTO_PRISMA_ACCESS
    state: UNATTACHED
    updateTime: '...'
    

The `key` field contains the pairing key.

  3. Use the pairing key to set up a Managed Cloud WAN in Prisma Access. 




###  API 

Use the [`projects.locations.sacRealms.create` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacRealms/create).
    
    
      POST https://networksecurity.googleapis.com/v1/project/PROJECT_ID/locations/global/sacRealms
      {
        "name": "REALM_ID",
        "securityService": "PALO_ALTO_PRISMA_ACCESS"
      }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REALM_ID`: the name of your realm



### Symantec Cloud SWG

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create a realm, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect** page.

[Go to Secure Access Connect Realms](https://console.cloud.google.com/net-security/sac/realms)

  2. Click **Create Realm**.

  3. Enter a name for the realm that you want to create.

  4. In the **Security service** field, choose **Symantec Cloud SWG**.

  5. If you already have the secret key from Symantec, in the **Secret** field, enter the Symantec secret key. If you don't have the secret key, you can get the secret key by following these steps:

     * Click **Enter secret manually**.
     * Store the API key in Secret Manager by doing the following:

**Note:** Secret Manager is a separate Google Cloud product that has its own [pricing](https://cloud.google.com/secret-manager/pricing).
       1. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create-a-secret) in the same project that you want to create the realm in.

       2. [Add a secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version) that contains the secret key. There must not be any extra blank spaces in the contents of the secret. Use the following format: `projects/<var>PROJECT_NUMBER</var>/secrets/<var>SECRET_NAME</var>`.

  6. Click **Create**.




###  gcloud 

  1. If you haven't already done so, provide the Symantec API key to Secure Access Connect by doing the following:

     1. In Symantec Cloud SWG, [create an API key](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-keys.html) and set **Access** to **Location Management**.

     2. Store the API key in Secret Manager by doing the following:

**Note:** Secret Manager is a separate Google Cloud product that has its own [pricing](https://cloud.google.com/secret-manager/pricing).
        1. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) in the same project that you want to create the realm in.

        2. [Add a secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version) that contains the API key. There must not be any extra blank spaces in the contents of the secret. Use the following format:
               
               USERNAME:PASSWORD
               

Replace the following:

           * `USERNAME`: the username from the API key
           * `PASSWORD`: the password from the API key
  2. Create a realm by running the [`gcloud network-security secure-access-connect realms create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/create):
         
         gcloud network-security secure-access-connect realms create REALM_ID \
               --security-service=symantec-cloud-swg \
               --project=PROJECT_ID \
               --symantec-secret=SECRET_ID
         

Replace the following:

     * `REALM_ID`: a name for your realm
     * `PROJECT_ID`: [your project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
     * `SECRET_ID`: the ID of the secret that contains the API key
  3. Grant the network security service account access to the API key by running the [`gcloud secrets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/add-iam-policy-binding):
         
         gcloud secrets add-iam-policy-binding SECRET_ID \
               --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-networksecurity.iam.gserviceaccount.com  \
               --role roles/secretmanager.secretAccessor
         

Replace the following:

     * `SECRET_ID`: the ID of the secret that contains the API key
     * `PROJECT_NUMBER`: [your project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)



###  API 

Use the [`projects.locations.sacRealms.create` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacRealms/create).
    
    
    POST https://networksecurity.googleapis.com/v1/projects/PROJECT_ID/locations/global/sacRealms
    {
      "name": "REALM_ID",
      "securityService": "SYMANTEC_CLOUD_SWG",
      "symantecOptions": {
        "secretPath": "SECRET_ID"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: [your project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `REALM_ID`: a name for your realm
  * `SECRET_ID`: the ID of the secret that contains the API key



## What's next

  * [Configure an NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview)
  * [Create Secure Access Connect attachments](https://docs.cloud.google.com/secure-access-connect/docs/create-attachments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
