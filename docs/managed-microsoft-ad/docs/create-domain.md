---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain/
title: Quickstart: Create a domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:17.889003+00:00
---

# Quickstart: Create a domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a domain

This page shows you how to create a domain with Managed Service for Microsoft Active Directory.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Managed Microsoft AD, Cloud DNS, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=managedidentities.googleapis.com,dns.googleapis.com,compute.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Managed Microsoft AD, Cloud DNS, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=managedidentities.googleapis.com,dns.googleapis.com,compute.googleapis.com)

  10. [Create a new Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) to deploy your domain to, or use an existing one. Managed Microsoft AD doesn't support [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy). Note down your VPC network's [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names), which you have to specify during the domain creation process. It is in the following format: `projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME`
     * Before you create a VPC network, make sure that you read [Select VPC networks](https://docs.cloud.google.com/managed-microsoft-ad/docs/update-networks).
     * Make sure that you enable the APIs and create the VPC in the same project where you have enabled billing.



### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Google Cloud Managed Identities Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.admin) (`roles/managedidentities.admin`)
  * [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to complete this quickstart. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to complete this quickstart:

  * `managedidentities.domains.create`
  * `compute.networks.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Gather information

You need the following information to create your domain:

  * A [fully qualified domain name (FQDN)](https://wikipedia.org/wiki/Fully_qualified_domain_name) such as `ad.example.com`. For more information, see [Microsoft's naming conventions in Active Directory](https://support.microsoft.com/en-us/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and).

  * A private IP address range that is not in use by any of the VPC subnetworks—for example, `172.16.0.0/24`, `192.168.0.0/24`, or `10.1.0.0/24`. Ideally, you should select a range that is not in use by _any_ of the VPC subnetworks where you can use the domain. For more information, see [Select IP address ranges](https://docs.cloud.google.com/managed-microsoft-ad/docs/selecting-ip-address-ranges).

  * A [region](https://cloud.google.com/about/locations/) to deploy the domain controller to—for example, `us-central1`. When you create a domain, you can deploy the domain controller in only one region. After you create the domain, you can [add domain controllers to additional regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions#add-region) to increase availability and be [resilient to regional outages](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional).

For information about the supported regions, see [Regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions#regions-list).

  * A [delegated administrator account username](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin). You can either use the default username (`setupadmin`) or modify it. However, you can't change this username after you complete the domain creation.

  * The [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the authorized VPC network, which is in the following format: ` projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME `




## Create the domain

To create a domain, complete the following steps:

###  Console 

  1. Go to the **Managed Microsoft AD** page.   
[Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)

  2. Select **Create New AD Domain**.

  3. On the **Create new domain** page, enter the gathered information.

     * Enter the **Fully qualified domain name (FQDN)** for your domain.
     * In the **Network details** section, select your VPC network name from the list. Select **OK**.
     * In the **CIDR Range** section, enter the IP address range for your domain.
     * In the **Regions** section, select a region from the list in which you want to deploy the domain controller.
     * In the **Admin name** field of the **Delegated admin** section, use the default username (`setupadmin`) or enter a username for your delegated administrator account.

This is your only opportunity to change the username for the delegated administrator account. After domain creation, you can't change the username for the delegated administrator account.

  4. Select **Create domain**.




It can take up to 60 minutes to create a domain. When the domain creation is complete, you receive a notification in the Google Cloud console.

You can view the status of this operation at any time under **Notifications** in the Google Cloud console. If the domain creation fails, click **See all activities** under **Notifications** to view the error message.

###  gcloud 

Run the following gcloud CLI command:
    
    
    gcloud active-directory domains create FULLY_QUALIFIED_DOMAIN_NAME \
        --reserved-ip-range=CIDR_RANGE --region=REGION \
        --authorized-networks=projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME
    

Replace the placeholder variables with the gathered information.

You receive the following response that indicates domain creation has started:
    
    
    Create request issued for: FULLY_QUALIFIED_DOMAIN_NAME
    Waiting for operation-1554140234884-5857b78a1a49e-02bc63a3-77e5c7ee to complete...
    

It can take up to 60 minutes to create a domain. The gcloud CLI operation status updates when the domain creation is complete.

If the domain creation fails, the gcloud CLI displays an error message on the command line.

You can repeat this process to create multiple independent domains in the same project.

**Note:** By default, you can create two independent domains in the same project. For more information, see [Limits](https://docs.cloud.google.com/managed-microsoft-ad/quotas#limits).

If you want to increase the number of independent domains that you can create in the same project, you can [contact Google Cloud support](https://docs.cloud.google.com/managed-microsoft-ad/docs/get-support).

To make the domain available on a network in a different project, you can configure [domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-peering).

You can't create [Active Directory sites](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-active-directory-site-topology) in Managed Microsoft AD because Managed Microsoft AD doesn't support the Active Directory Sites and Services feature.

You can't create a [child domain](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-) in Managed Microsoft AD. Also, Managed Microsoft AD can't be part of any other Active Directory domain deployed either on Google Cloud or on-premises. However, after you create a Managed Microsoft AD domain, you can [create a trust relationship](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust) between the Managed Microsoft AD domain and any other non-Managed Microsoft AD domain.

For information about the errors that you might encounter while creating a domain, see [Unable to create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#create-domain).

## What's next

  * [Join a Windows VM to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows)
  * [Join a Linux VM to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-linux)
  * [Connect to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain)
  * [Configure domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering)
  * [Deploy domain controllers in additional regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions)
  * [Deploy Managed Microsoft AD with cross-project access using domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/shared-vpc-managedad-cloudsql)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
