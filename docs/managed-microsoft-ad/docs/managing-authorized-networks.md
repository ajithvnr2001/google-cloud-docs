---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/managing-authorized-networks/
title: Manage authorized networks \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:24.682630+00:00
---

# Manage authorized networks  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/managing-authorized-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Manage authorized networks Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to add or remove authorized networks from your Managed Service for Microsoft Active Directory domain. Authorized networks are Virtual Private Cloud (VPC) networks that are permitted to access the domain. VPC peering enables this access. Managed Microsoft AD supports adding up to 5 VPC networks to the authorized network list. These networks must meet [VPC peering requirements](https://docs.cloud.google.com/vpc/docs/vpc-peering#restrictions).

## Adding authorized networks during domain creation

To add an authorized network when you're [creating a new Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-create-domain), complete the following steps.

###  Console 

  1. Go to the [Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad) page in the Google Cloud console.   
[Go to the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)
  2. Select **Create new AD domain**.
  3. On the **Create new domain page** , under **Network details** , open the **Select networks** list. Select the name of the VPC network you want to authorize.
  4. Select **OK**.
  5. Complete [creating a new domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-create-domain).



###  gcloud 

Run the following gcloud CLI command.
    
    
    gcloud active-directory domains create domain-name \
     --region=region --reserved-ip-range="ip-range" \
     --authorized-networks=projects/project-name/global/networks/network
    

## Adding authorized networks to an existing domain

To add an authorized network to an existing Managed Microsoft AD domain, complete the following steps.

###  Console 

  1. Go to the [Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad) page in the Google Cloud console.   
[Go to the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)
  2. From the domain list, select the domain name.
  3. On the **Basic details** page, select edit Edit.
  4. Under **Network details** , open the **Select networks** list. Select the networks you want to authorize.
  5. Select **Save Changes**.



###  gcloud 

Run the following gcloud CLI command.
    
    
    gcloud active-directory domains update domain-name \
     --add-authorized-networks=projects/project-name/global/networks/network
    

## Removing authorized networks

To remove an authorized network from a Managed Microsoft AD domain, complete the following steps.

###  Console 

  1. Go to the [Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad) page in the Google Cloud console.   
[Go to the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)
  2. From the domain list, select the domain name.
  3. On the **Basic details** page, select edit Edit.
  4. Under **Network details** , open the **Select networks** list. Select the networks you want to remove.
  5. Select **Save Changes**.



###  gcloud 

Run the following gcloud CLI command.
    
    
    gcloud active-directory domains update domain-name \
     --remove-authorized-networks=projects/project-name/global/networks/network
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
