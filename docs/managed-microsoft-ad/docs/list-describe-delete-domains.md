---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domains/
title: Manage domains \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:54.765162+00:00
---

# Manage domains  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Manage domains Stay organized with collections  Save and categorize content based on your preferences. 

This article shows you how to list your existing Managed Service for Microsoft Active Directory domains, get information about them, and delete domains you no longer need.

## Getting domain info

You can query for more information about a specific domain, including its current state. This is especially useful when creating a new domain.

To get domain info:

###  Console 

  1. Open the Managed Microsoft AD page in the Google Cloud console.   
[ Open the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)

  2. Select a domain from the list to see detailed info on it.




###  gcloud 

Run the following command, replacing [DOMAIN-NAME] with the name of your domain (such as _ad.mycompany.com_):
    
    
    gcloud active-directory domains describe [DOMAIN-NAME]
    

The response is YAML describing the [domain](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains).
    
    
    admin: setupadmin
    authorizedNetworks:
    - projects/my-project/global/networks/my-vpc
    createTime: '2019-03-27T22:35:58.135726571Z'
    fqdn: ad.mycompany.com
    locations:
    - us-west1
    name: projects/my-project/locations/global/domains/ad.mycompany.com
    reservedIpRange: 172.16.0.0/26
    state: READY
    updateTime: '2019-03-29T23:58:12.249298693Z'
    

Possible domain states include:

State | Description  
---|---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | The domain is being created.  
`READY` | The domain has been created and is fully usable.  
`UPDATING` |  The domain's configuration is being updated. The domain is still usable. This status is only used for user-initiated changes to the domain.   
`DELETING` | The domain is being deleted.  
`REPAIRING` |  The domain is being repaired and may be unusable. Details can be found in the `statusMessage` field.   
`PERFORMING_MAINTENANCE` |  The domain is undergoing maintenance. The domain is still usable. This status is only used for changes to the domain initiated by the service. The status will not appear for any changes that have been initiated by users.   
`UNAVAILABLE` | The domain is not serving requests.  
  
## Listing domains

###  Console 

Open the Managed Microsoft AD page in the Google Cloud console. It contains a list of all domains in the project.   
[ Open the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)

###  gcloud 

Run the following command:
    
    
    gcloud active-directory domains list
    

The response is a list of domains in the project:
    
    
    DOMAIN_NAME             DOMAIN_STATE  RESERVED_IP_RANGE  REGIONS        LABELS  ADMIN_NAME        CREATE_TIME
    corporate.company.com   READY         172.16.0.0/26      [u'us-west1']          setupadmin        2019-01-01T22:00:00
    partners.company.com    READY         192.168.0.0/26     [u'us-east1']          CustomAdminName   2019-02-01T22:00:00
    

## Deleting a domain

**Warning:** Deleting a domain is permanent. All data associated with the domain will be permanently lost (including users, groups, backups, etc).

###  Console 

  1. Open the Managed Microsoft AD page in the Google Cloud console.  
[ Open the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)

  2. Select the domain to delete.

  3. Click the delete **Delete** button, and accept the confirmation prompt.




###  gcloud 

Run the following command, replacing [DOMAIN-NAME] with the name of your domain (such as _ad.mycompany.com_)
    
    
    gcloud active-directory domains delete [DOMAIN-NAME]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
