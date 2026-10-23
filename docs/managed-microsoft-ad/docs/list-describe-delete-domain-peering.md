---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domain-peering/
title: Manage domain peerings \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:50.138460+00:00
---

# Manage domain peerings  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domain-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Manage domain peerings Stay organized with collections  Save and categorize content based on your preferences. 

This article shows you how to do the following tasks in Managed Service for Microsoft Active Directory (Managed Microsoft AD):

  * List the domain peerings available in your project.
  * Get information about a specific domain peering.
  * Update labels for your domain peering.
  * Delete domain peerings which you no longer need.



## Before you begin

  * Familiarize yourself with [domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-peering).
  * Make sure that you read [Configure domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering).



## List domain peerings

To list the domain peerings available in a project, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)
  2. Click the **Peerings** tab to view the list of domain peerings.



###  gcloud 

Run the following gcloud CLI command: 
    
    
    gcloud active-directory peerings list
    

You receive a response with the list of domain peerings.
    
    
    PEERING_NAME   DOMAIN_NAME                                                 AUTHORIZED_NETWORK                              PEERING_STATE   CREATE_TIME
    mypeering      projects/my-project/locations/global/domains/mydomain.com   project/my-project/global/networks/my-network   CONNECTED       2021-01-01T22:00:00
    

## Get domain peering information

You can retrieve all the information specific to a domain peering including its current state, name, domain resource, authorized network. This information is useful in multiple scenarios such as verifying if a domain peering is configured with the intended resources and checking the status of domain peering.

To retrieve the information about a domain peering, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)
  2. Click the **Peerings** tab to view the information about domain peerings.



###  gcloud 

Run the following gcloud CLI command:
    
    
    gcloud active-directory peerings describe [PEERING_NAME]
    

Replace [PEERING_NAME] with the name of your domain peering. For example, `mypeering`.

You receive a YAML as a response describing the peering.
    
    
    authorizedNetwork: projects/my-project/global/networks/my-vpc
    createTime: '2019-03-27T22:35:58.135726571Z'
    domainResource: projects/my-project/locations/global/domains/ad.mycompany.com
    name: projects/my-project/locations/global/peerings/mypeering
    state: CONNECTED
    updateTime: '2019-03-29T23:58:12.249298693Z'
    

Possible domain peering states include:

State | Description  
---|---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | The domain peering is being created.  
`CONNECTED` | The domain peering is connected and fully usable.  
`DELETING` | The domain peering is being deleted.  
`DISCONNECTED` | The domain peering isn't connected yet. There are a few possible causes: 

  * If the state of the domain resource project is `DISCONNECTED`, it means that the domain peering isn't yet created from the VPC resource project. 
  * If the state of the VPC resource project is `DISCONNECTED`, it means that the domain peering isn't yet created from the domain resource project. 

  
  
## Update labels for a domain peering

You can update the labels for an existing domain peering. To update the labels for a domain peering, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)
  2. Click the **Peerings** tab.
  3. Select the checkbox next to the domain peering that you want to update.
  4. Click **Labels**.
  5. In the **Labels for resource** pane, do the following: 
     1. To add a new label, click **Add label** , and then enter the key-value pairs.
     2. To modify an existing label, enter a new value for the required key-value pair.
     3. To delete a label, click **delete Delete item** next to the key-value pair that you want to delete.
  6. Click **Save**.



###  gcloud 

Run the following gcloud CLI command:
    
    
    gcloud active-directory peerings update [PEERING_NAME] \
      --update-labels=[KEY]=[VALUE],[KEY]=[VALUE] \
      --remove-labels=[KEY],[KEY]
    

Replace the following:

  * `[PEERING_NAME]`: The name of your domain peering. For example, `mypeering`.
  * `[KEY]` and `[VALUE]`: The key-value pair that you want to add, modify, or delete. For example, `count=8`.
  * `--update-labels`: You can use this flag to specify the key-value pairs that you want to add or modify. If a key already exists, Managed Microsoft AD modifies the existing value. Otherwise, it adds a new label.
  * `--remove-labels`: You can use this flag to specify the labels that you want to delete.



## Delete a domain peering

**Warning:** Deleting a domain peering is permanent and cannot be undone. After you delete a domain peering, it cannot be recovered or restored.

To delete a domain peering, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)
  2. Click the **Peerings** tab.
  3. Click **more_vert Menu** next to the domain peering that you want to remove.
  4. Select **Delete**.
  5. In the **Delete peering** dialog, enter the name of your peering resource.
  6. Click **Delete**.



###  gcloud 

Run the following gcloud CLI command: 
    
    
    gcloud active-directory peerings delete [PEERING_NAME]
    

Replace [PEERING_NAME] with the name of your domain peering. For example, `mypeering`.

## What's next

  * [Join a Windows VM to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows)
  * [Join a Linux VM to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-linux)
  * [Connect to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
