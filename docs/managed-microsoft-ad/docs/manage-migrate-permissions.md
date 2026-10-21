---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-migrate-permissions/
title: Manage permissions required for migrating an on-premises domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:24.556313+00:00
---

# Manage permissions required for migrating an on-premises domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-migrate-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Manage permissions required for migrating an on-premises domain Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Existing domain migration**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to check if the permissions that are required to migrate an existing Active Directory domain from on-premises to Managed Service for Microsoft Active Directory with SID history are enabled. This page also explains how to disable these permissions after you complete the migration.

## Before you begin

Make sure that you have any one of the following Identity and Access Management ( IAM) user roles:

  * Google Cloud Managed Identities Domain Admin (`roles/managedidentities.domainAdmin`)
  * Google Cloud Managed Identities Admin (`roles/managedidentities.admin`)



For more information, see [Cloud Managed Identities roles](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities).

## Check permissions

You can check if the permissions that are required to migrate domains with SID history are available on a Managed Microsoft AD domain.

To validate the permissions, run the following gcloud CLI command:
    
    
    gcloud beta active-directory domains migration check-permissions DOMAIN_NAME
    

Replace DOMAIN_NAME with the name of your Managed Microsoft AD domain. For example, `my-domain.com`.

This operation validates if the Managed Microsoft AD has the `Cloud Service Migrate SID Administrators` group created and the state of SID filtering on all the trusted domains.

The response lists the SID filtering state of all the trusted domains and the state of permissions required in your Managed Microsoft AD domain:
    
    
    onpremDomains:
    - name: domain-one.com
      sidFilteringState: ENABLED
    - name: domain-two.com
      sidFilteringState: DISABLED
    state: ENABLED
    

Your Managed Microsoft AD domain can have anyone of the following states:

State | Description  
---|---  
`DISABLED` | Managed Microsoft AD domain doesn't have the permissions required to migrate the on-premises domain with SID history. SID filtering is enabled on all the trusted domains.  
`ENABLED` | Managed Microsoft AD domain has the permissions required to migrate the on-premises domain with SID history. To check the SID filtering state, see the `sidFilteringState` field for all the trusted domains in the response.  
`NEEDS MAINTENANCE` | Permissions seem to be in intermittent state for your Managed Microsoft AD domain. To reset the state, either [enable permissions](https://docs.cloud.google.com/managed-microsoft-ad/docs/enable-migrate-permissions#enable-permissions) or [disable permissions](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-migrate-permissions#disable-permissions) as you require.  
  
## Disable permissions on the Managed Microsoft AD domain

After you complete the migration, you must disable the permissions provided for migrating your on-premises domain with SID history.

To disable the permissions, run the following gcloud CLI command:
    
    
    gcloud beta active-directory domains migration disable DOMAIN_NAME
    

Replace DOMAIN_NAME with the name of your Managed Microsoft AD domain. For example, `my-domain.com`.

This operation disables the permissions provided to your domain by deleting the `Cloud Service Migrate SID Administrators` group from Managed Microsoft AD and enables SID filtering on all the trusted domains.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
