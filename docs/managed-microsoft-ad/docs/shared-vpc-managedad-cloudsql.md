---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/shared-vpc-managedad-cloudsql/
title: Deploy Managed Microsoft AD with cross-project access using domain peering \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:00.362253+00:00
---

# Deploy Managed Microsoft AD with cross-project access using domain peering  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/shared-vpc-managedad-cloudsql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Deploy Managed Microsoft AD with cross-project access using domain peering Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to configure domain peering between Managed Service for Microsoft Active Directory (Managed Microsoft AD) and Shared VPC. This allows you to make Managed Microsoft AD available to service projects attached to Shared VPC.

## Overview

[Domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-peering) in Managed Microsoft AD creates a domain peering resource in each domain resource and VPC resource projects. Managed Microsoft AD domain can be made available to all the projects attached to the Shared VPC by creating a domain peering between Managed Microsoft AD and Shared VPC. For example, you can authenticate and login to SQL Server using Managed Microsoft AD domain, where SQL Server and Managed Microsoft AD are in different service projects that are attached to the Shared VPC.

## Before you begin

Before you begin, do the following:

  1. In the Google Cloud console, on the project selector page, select or create three Google Cloud projects. They are called host and service projects. The host project is where the Shared VPC is enabled. Managed Microsoft AD domain and Cloud SQL instances must reside in different service projects. The VMs could reside in one of the service projects.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable billing for your Cloud project(s). For more information, see [Check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project).

  3. Enable Shared VPC on the host project. For more information, see [Enable a host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host).

  4. Attach the service project(s) to the Shared VPC network. Each of the projects need to have Compute Engine API enabled. For the purpose of this example, we recommend creating separate subnets in the Shared VPC. While attaching the project, choose the appropriate subnet for each of the project(s). For more information, see [Attach service projects](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared).

  5. [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain) in the service project. The VPC network authorized while creating the Managed Microsoft AD domain is independent of the Shared VPC networks. To create a Managed Microsoft AD domain without an authorized network, use the gcloud CLI command.




## Configure domain peering

  1. Create domain peering from the service project having the domain resource to the Shared VPC network. For more information about domain peering, see [Configure domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering#configure_domain_peering).
         
         gcloud active-directory peerings create PEERING-RESOURCE-NAME \
         --domain=DOMAIN-RESOURCE-NAME \
         --authorized-network=SHARED-VPC-NAME
         

Replace the following:

     * `PEERING-RESOURCE-NAME`: A name for your domain peering resource (such as `my-domain-peering`).
     * `DOMAIN-RESOURCE-NAME`: The [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Managed Microsoft AD domain, in the form of: `projects/PROJECT-ID/locations/global/domains/DOMAIN-NAME`.
     * `SHARED-VPC-NAME`: The [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Shared VPC network, in the form of: `projects/PROJECT-ID/global/networks/NETWORK-NAME`.
  2. List the domain peerings to verify the state. Run the following gcloud CLI command:
         
         gcloud active-directory peerings list --project=PROJECT_ID
         

Replace PROJECT_ID with the project ID of the service project that is used to create your domain peering resource.

It returns the state as `DISCONNECTED`.

  3. Create the reverse domain peering from the host project.
         
         gcloud active-directory peerings create PEERING-RESOURCE-NAME \
         --domain=DOMAIN-RESOURCE-NAME \
         --authorized-network=SHARED-VPC-NAME \
         --project=VPC-RESOURCE-PROJECT-ID
         

Replace the following:

     * `PEERING-RESOURCE-NAME`: A name for your domain peering resource (such as `my-domain-peering`).
     * `DOMAIN-RESOURCE-NAME`: The [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Managed Microsoft AD domain, in the form of: `projects/PROJECT-ID/locations/global/domains/DOMAIN-NAME`.
     * `SHARED-VPC-NAME`: The [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Shared VPC network, in the form of: `projects/PROJECT-ID/global/networks/NETWORK-NAME`.
     * `VPC-RESOURCE-PROJECT-ID`: The project ID of the host project that is hosting the Shared VPC.
  4. List the domain peerings again to verify the state. Run the following gcloud CLI command:
         
         gcloud active-directory peerings list --project=PROJECT_ID
         

Replace PROJECT_ID with the project ID of the service project that is used to create your domain peering resource.

It returns the state as `CONNECTED` from both the host and service projects.




## Configure the Cloud SQL (SQL Server) instance

  1. Create the Cloud SQL (SQL Server) instance in the service project with Private IP enabled and select the network of the Shared VPC. For more information, see [Create an instance with Windows Authentication](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#creating-an-instance-with-windows-authentication).

  2. After the domain peering is complete, modify the Cloud SQL (SQL Server) configuration to use your Managed Microsoft AD domain for authentication. Run the following gcloud CLI command:
         
         gcloud beta sql instances patch INSTANCE-NAME \
         --active-directory-domain=DOMAIN-RESOURCE-NAME
         

Replace the following:

     * `INSTANCE-NAME`: The name of your Cloud SQL instance in the service project.
     * `DOMAIN-RESOURCE-NAME`: The [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Managed Microsoft AD domain that you want to use for authentication. Full resource name format: `projects/PROJECT-ID/locations/global/domains/DOMAIN-NAME`.

For more information, see [Enable cross-project Windows authentication](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#enable-cross-project-auth).




The SQL Server is now configured with Windows authentication enabled.

## Test the setup

  1. Create a Windows or Linux VM in the service project. While creating the VM, select the Shared VPC and the subnet which is shared in the Shared VPC with this service project.
  2. Join the VM to a domain. For more information about joining a Windows VM to a domain, see [Join a Windows VM to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows).
  3. Create a SQL Server login based on a Windows user or group. For more information, see [Connect to an instance with a user](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#connecting-to-an-instance-with-a-user).
  4. Connect using the SQL Server's instance DNS name. For more information, see Step 2 in [Connect to an instance with a user](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#connecting-to-an-instance-with-a-user).



## Summary

You have domain peered a Managed Microsoft AD domain with the Shared VPC host and created SQL Server on the Shared VPC. With this domain peering, cross-project Windows authentication is enabled for SQL Server.

While in the above scenario Managed Microsoft AD and SQL Server are in different service projects, configuring them in the same service project is also supported.

Alternatively, you can also have the Managed Microsoft AD domain in the host project. In this case, Shared VPC needs to be added as an authorized network to the Managed Microsoft AD domain. For more information, see [Adding authorized networks to an existing domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/managing-authorized-networks#adding_authorized_networks_to_an_existing_domain).

In all these scenarios through peering with Shared VPC, the domain is available to the service project(s) attached to the Shared VPC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
