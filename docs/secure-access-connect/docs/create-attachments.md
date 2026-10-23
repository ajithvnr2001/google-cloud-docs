---
url: https://docs.cloud.google.com/secure-access-connect/docs/create-attachments/
title: Create attachments \u00a0|\u00a0 Secure Access Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:23.604652+00:00
---

# Create attachments  |  Secure Access Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-access-connect/docs/create-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Access Connect ](https://docs.cloud.google.com/secure-access-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-access-connect/docs/overview)



Send feedback 

#  Create attachments Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create Secure Access Connect attachments. A Secure Access Connect attachment enables [NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview) to process traffic with an SSE product.

## Before you begin

Before you begin, do the following:

  * [Create a realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms)
  * [Create an NCC Gateway spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke)



### Required roles

To get the permissions that you need to create attachments, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Secure Access Connect attachment

Create a Secure Access Connect attachment by following the instructions that correspond with your SSE provider.

### Palo Alto Networks Prisma Access

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect Attachments** page.

[Go to Secure Access Connect Attachments](https://console.cloud.google.com/net-security/sac/attachments/list)

  2. Click **Create Attachment**.

  3. Enter a name for the attachment that you want to create.

  4. Choose the region for your attachment.

  5. Choose the realm ID for your attachment. The realm you choose must be attached to Palo Alto Networks Prisma Access.

If you haven't created a realm, in the **Realm** field, click **Create Realm**. Follow the instructions to [Create a realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms#create-realm-for-palo-alto-networks-prisma-access).

  6. Choose the NCC Gateway spoke to connect your attachment to.

  7. Click **Create**.




###  gcloud 

Create an attachment by running the [`gcloud network-security secure-access-connect attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/attachments/create):
    
    
      gcloud network-security secure-access-connect attachments create ATTACHMENT_ID \
          --project=PROJECT_ID \
          --location=REGION \
          --realm=REALM_ID \
          --gateway=NCC_GATEWAY_SPOKE_ID
    

Replace the following:

  * `ATTACHMENT_ID`: the name for the attachment
  * `PROJECT_ID`: your project ID
  * `REGION`: the region for the attachment
  * `REALM_ID`: the ID of your realm
  * `NCC_GATEWAY_SPOKE_ID`: the ID of your NCC Gateway spoke



###  API 

To create an attachment in a given project and location, use the [`projects.locations.sacAttachments.create` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacAttachments/create).
    
    
    POST https://networksecurity.googleapis.com/v1/{parent=project/PROJECT_ID/locations/REGION}/sacAttachments
    {
      "sacRealm": "REALM_ID",
      "nccGateway": "NCC_GATEWAY_SPOKE_ID"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region for the attachment
  * `REALM_ID`: the ID of your realm
  * `NCC_GATEWAY_SPOKE_ID`: the ID of your NCC Gateway spoke



### Symantec Cloud SWG

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create an attachment, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Secure Access Connect Attachments** page.

[Go to Secure Access Connect Attachments](https://console.cloud.google.com/net-security/sac/attachments/list)

  2. Click **Create Attachment**.

  3. Enter a name for the attachment that you want to create.

  4. Choose the region for your attachment.

  5. Choose the realm ID for your attachment. The realm you choose must be attached to Symantec Cloud SWG.

If you haven't created a realm, in the **Realm** field, click **Create Realm**. Follow the instructions to [Create a realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms#create-realm-for-symantec).

  6. Choose the NCC Gateway spoke to connect your attachment to.

  7. (Optional) Choose the **Localization** country for your attachment.

  8. (Optional) Choose the appropriate **Timezone** for your localization.

  9. Click **Create**.




###  gcloud 

  1. Identify the Symantec site that you want to connect your attachment to by running the [`gcloud network-security secure-access-connect realms describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/describe):
         
         gcloud network-security secure-access-connect realms describe REALM_ID \
               --project=PROJECT_ID
         

Replace the following:

     * `REALM_ID`: the name of your realm
     * `PROJECT_ID`: your project ID

The output is similar to the following:
    
    name: projects/project-id/locations/global/sacRealms/realm-id
    createTime: '...'
    updateTime: '...'
    securityService: SYMANTEC_CLOUD_SWG
    state: PARTNER_ATTACHED
    symantecOptions:
      availableSymantecSites:
                   SYMANTEC_SITE_1
                   SYMANTEC_SITE_2
      secretPath:SECRET_PATH
     symantecConnectionState: SUCCEEDED
    

The `availableSymantecSites` field contains the Symantec Cloud SWG sites that are available for you to connect to.

  2. Create an attachment by running the [`gcloud network-security secure-access-connect attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/attachments/create):
         
         gcloud network-security secure-access-connect attachments create ATTACHMENT_ID \
               --project=PROJECT_ID \
               --location=REGION \
               --realm=REALM_ID \
               --gateway=NCC_GATEWAY_SPOKE_ID \
               --symantec-site=SYMANTEC_SITE \
               --symantec-location-name=SYMANTEC_LOCATION_NAME
               --country=COUNTRY \
               --timezone=TIMEZONE
         

Replace the following:

     * `ATTACHMENT_ID`: the name for the attachment
     * `PROJECT_ID`: your project ID
     * `REALM_ID`: the ID of your realm
     * `NCC_GATEWAY_SPOKE_ID`: the ID of your NCC Gateway spoke
     * `SYMANTEC_SITE`: the Symantec site that you want to connect the attachment to

Must be one of the `availableSymantecSites` from the previous step.

     * `SYMANTEC_LOCATION_NAME`: the name to give to the Symantec location

For more information about naming requirements, see the `Location schema` in the [Symantec Location Management API documentation](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/location-management-api.html).

     * `COUNTRY`: an optional country code in the ISO 3166 alpha-2 country code format

     * `TIMEZONE`: an optional timezone in the IANA timezone format




###  API 

To create an attachment in a given project and location, use the [`projects.locations.sacAttachments.create` method](https://docs.cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacAttachments/create).
    
    
    POST https://networksecurity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/sacAttachments
    {
      "name": "ATTACHMENT_ID",
      "sacRealm": "REALM_ID",
      "nccGateway": "NCC_GATEWAY_SPOKE_ID",
      "country": "COUNTRY",
      "timeZone": "TIMEZONE",
      "symantecOptions": {
        "symantecLocationName": "SYMANTEC_LOCATION_NAME",
        "symantecSite": "SYMANTEC_SITE"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region for the attachment
  * `ATTACHMENT_ID`: the name for the attachment
  * `REALM_ID`: the ID of your realm
  * `NCC_GATEWAY_SPOKE_ID`: the ID of your NCC Gateway spoke
  * `COUNTRY`: an optional country code in the ISO 3166 alpha-2 country code format
  * `TIMEZONE`: an optional timezone in the IANA timezone format
  * `SYMANTEC_SITE`: the Symantec site that you want to connect the attachment to

Must be one of the `availableSymantecSites` from the previous step.

  * `SYMANTEC_LOCATION_NAME`: the name to give to the Symantec location

For more information about naming requirements, see the `Location schema` in the [Symantec Location Management API documentation](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/location-management-api.html).




## What's next

  * [Add hybrid connections to NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
