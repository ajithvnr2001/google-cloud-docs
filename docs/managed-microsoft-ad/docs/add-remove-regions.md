---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions/
title: Deploy domain controllers in additional regions \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:09.260412+00:00
---

# Deploy domain controllers in additional regions  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Deploy domain controllers in additional regions Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a list of regions that you can add to your domain in Managed Service for Microsoft Active Directory (Managed Microsoft AD). This page also shows you how to add or remove a region from your domain.

Managed Microsoft AD supports multiple regions. Combined with the multi-regional nature of Virtual Private Clouds, you can quickly scale your Active Directory infrastructure across Google Cloud. For more information about regions, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Before you begin

Before you add or remove domain controllers to additional regions, make sure that you have any one of the following IAM user roles:

  * Google Cloud Managed Identities Domain Admin (`roles/managedidentities.domainAdmin`)
  * Google Cloud Managed Identities Admin (`roles/managedidentities.admin`)



For more information, see [Cloud Managed Identities roles](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities).

For information about granting an IAM role to a principal, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## Regions

Managed Microsoft AD supports the following regions:

Region name | Region description  
---|---  
`africa-south1` | Johannesburg  
`asia-east1` | Taiwan  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo  
`asia-northeast2` | Osaka  
`asia-northeast3` | Seoul  
`asia-south1` | Mumbai  
`asia-south2` | Delhi  
`asia-southeast1` | Singapore  
`asia-southeast2` | Jakarta  
`australia-southeast1` | Sydney  
`australia-southeast2` | Melbourne  
`europe-central2` | Warsaw  
`europe-north1` | Finland  
`europe-southwest1` | Madrid  
`europe-west1` | Belgium  
`europe-west2` | London  
`europe-west3` | Frankfurt  
`europe-west4` | Netherlands  
`europe-west6` | Zürich  
`europe-west8` | Milan  
`europe-west9` | Paris  
`europe-west10` | Berlin  
`europe-west12` | Turin  
`me-central1` | Doha  
`me-central2` | Dammam  
`me-west1` | Tel Aviv  
`northamerica-northeast1` | Montréal  
`northamerica-northeast2` | Toronto  
`southamerica-east1` | São Paulo  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | Northern Virginia  
`us-east5` | Columbus  
`us-south1` | Dallas  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
## Add a region

Managed Microsoft AD uses a single [Active Directory site](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts#BKMK_5). The site is not constrained to a specific VPC subnet; it spans all regions and subnets of your VPC. For example, consider you have domain controllers located in `us-west1` and your VPC spans `us-west1`, `us-east1`, and `us-central1`. Your domain is available in all these three regions and not limited to `us-west1`.

However, to increase availability and be [resilient to regional outages](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional), we recommend that you deploy domain controllers in additional regions. Each domain supports up to 4 regions.

You can only add domain controllers to the [supported regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions#regions-list). Note that doesn't affect the access to your Managed Microsoft AD domain, which is available in all regions where your VPC has a presence.

To add domain controllers to an additional region, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[ Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)

  2. Select the domain to add a region to, then click edit**Edit**.

  3. Click **Add Region** and choose the region to add from the menu.

  4. Select **Save Changes**.




###  gcloud 

Run the following command:
    
    
    gcloud active-directory domains update DOMAIN_NAME \
      --add-region=REGION
    

Replace the following:

  * `DOMAIN_NAME`: The name of your domain. For example, `ad.mycompany.com`.
  * `REGION`: The region to add. For example, `us-west1`.



**Note:** You can only add a single region at a time.

## Remove a region

As your business needs evolve, you can easily retire domain controllers from a region. All the data is replicated, so removing a region doesn't result in data loss.

To remove domain controllers from a region, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[ Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)

  2. Select the domain to remove a region from, then click edit**Edit**.

  3. Under the **Regions** section, click the delete **Delete** icon next to the region that you want to remove.

  4. Select **Save Changes**.




###  gcloud 

Run the following command:
    
    
    gcloud active-directory domains update DOMAIN_NAME \
      --remove-region=REGION
    

Replace the following:

  * `DOMAIN_NAME`: The name of your domain. For example, `ad.mycompany.com`.
  * `REGION`: The region to remove. For example, `us-west1`.



**Note:** You can only remove a single region at a time, and there must always be at least 1 region associated with a domain.

## What's next

  * [Create a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
