---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/connect-to-managed-service-for-microsoft-ad/
title: Connect to Managed Service for Microsoft Active Directory \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:57.530123+00:00
---

# Connect to Managed Service for Microsoft Active Directory  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/connect-to-managed-service-for-microsoft-ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Connect to Managed Service for Microsoft Active Directory Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to connect to Managed Service for Microsoft Active Directory.

NetApp Volumes supports Managed Microsoft AD.

Managed Microsoft AD uses private services access to connect to consumer projects, similar to NetApp Volumes. Private services access uses Virtual Private Cloud (VPC) peering, which blocks transitive traffic between VPCs. NetApp Volumes can't communicate with Managed Microsoft AD through a consumer VPC, so you need a [domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering) to establish this connection.

## Before you begin

Make sure you meet the prerequisites mentioned in [Managed Microsoft AD - Before you begin](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering#before-you-begin).

## Establish a domain peering

Use the following instructions to establish a domain peering:

  1. Identify the project name of the NetApp Volumes tenant project that owns your NetApp Volumes resources:
         
         gcloud compute networks peerings list --project=project_owning_NetAppVolumes --flatten=peerings --filter="peerings.name=sn-netapp-prod"
         

The `PEER_PROJECT` parameter shows the name of the NetApp Volumes tenant project. The `PEER_NETWORK` parameter shows the tenant project VPC name, which should be _netapp-prod-network_.

  2. Follow the instructions in [Configure domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering#configure_domain_peering) to create a domain peering from Managed Microsoft AD to NetApp Volumes, using the tenant project ID and network you identified from the previous step.

Note that you can only establish the peering from the domain resource project to the NetApp Volumes tenant project. The reverse peering from the VPC resource project (NetApp Volumes tenant project) to the domain resource project requires a support case with [Google Cloud Customer Care](https://cloud.google.com/support-hub/).

  3. Open a support case with [Google Cloud Customer Care](https://cloud.google.com/support-hub/) to establish the reverse peering from NetApp Volumes to Managed Microsoft AD. Provide the output of the following command to Google Cloud Customer Care to identify which peering to accept.
         
         gcloud active-directory peerings list --project=project_owning_ManagedAD
         

  4. After Google Cloud Customer Care establishes the two-way peering, the status of your peering shows **CONNECTED**. Verify the peering status:
         
         gcloud active-directory peerings list --project=project_owning_ManagedAD
         

  5. [Create an Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy) in the same region where you plan to create volumes using Managed Microsoft AD. You need to specify the following parameters:

     * **DNS servers** IP address:

       * For the Flex Unified and Flex File service level, use `169.254.169.254` for the DNS servers IP address in the policy.

       * For Standard, Premium, and Extreme service levels, follow the instructions in [Using IP address for DNS resolution](https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain#using_ip_address_for_dns_resolution). You will use the entry point IP addresses created by Cloud DNS in your Active Directory policy.

     * **Organizational Unit** (OU): Managed Microsoft AD puts all objects into `OU=cloud` by [default](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects). You need to specify a correct organizational unit parameter for your environment. For example, if you have a Windows domain called _engineering.example.com_ , the default organizational unit to specify would be `CN=Computers,OU=Cloud,DC=engineering,DC=example,DC=com`.

  6. Attach the Active Directory policy to the storage pool to be used.

For the Flex File service level, test Active Directory policy connection by creating a volume which uses the Active Directory.

For Standard, Premium, and Extreme service levels, test [Active Directory policy connection](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection) before creating a volume.




## What's next

[Use Active Directory as LDAP server for NFS](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/ad-ldap-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
