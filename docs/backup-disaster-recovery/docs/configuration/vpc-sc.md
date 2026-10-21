---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/vpc-sc/
title: Configure VPC Service Controls for Backup and DR for appliance-managed backups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:41.027674+00:00
---

# Configure VPC Service Controls for Backup and DR for appliance-managed backups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure VPC Service Controls for Backup and DR for appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) and how you can integrate it with Backup and DR to secure your data and resources.

## About VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) helps mitigate the risk of data exfiltration from the Backup and DR appliance management console. You can use VPC Service Controls to create [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) that protect the resources and data of various services. If the Backup and DR is protected by a perimeter, resources from outside the perimeter cannot communicate with the appliance management console. However, you can allow resources from outside the service perimeter to access the management console and API. For more information, see [allow access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

For a general overview of VPC Service Controls, its security benefits, and its capabilities across [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) products, see the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

Before you begin to configure VPC Service Controls for Backup and DR, do the following:

  1. In the Google Cloud console, on the **Project Selector** page, select [create a ](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) project.
  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. Follow the instructions in the [Enable APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) section and enable the **Access Context Manager API** for your project.



## Configure access levels and direction policies for backup vault

If the backup/recovery appliance and backup vault are in the same VPC Service Controls perimeter, you don't need to configure access levels and direction policies. Otherwise choose from one of the following configuration scenarios based on your security perimeter configuration requirements.

  * **If the backup/recovery appliance and backup vault are in perimeters but they exist in different perimeters** : 
    * Configure ingress exceptions in the perimeter where backup vault resources exist. Add both `backupdr.googleapis.com` and `storage.googleapis.com` in the ingress rule. The source can be the [IP address](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access#limitations), or the network, or the project in which the backup/recovery appliance is present.
    * Configure egress exceptions in the perimeter where backup/recovery appliances exist. Add both `backupdr.googleapis.com` and `storage.googleapis.com` to the egress rule. The target is the project where the backup vault resource exists. You can combine that with the IP address of the backup/recovery appliance, or any other property.
  * **If only backup vault resources are in perimeter** : Configure ingress exceptions in the perimeter where backup vault resources exist. Add both `backupdr.googleapis.com` and `storage.googleapis.com` to the ingress rule. The source can be IP address, network, or project where the backup/recovery appliance is present.
  * **If only backup/recovery appliance exists in perimeter** : Configure egress exceptions in the perimeter where backup/recovery appliances exist. Add both `backupdr.googleapis.com` and `storage.googleapis.com` to the egress rule. The target is the project where the backup vault resource exists. You can combine that with the IP address of the backup/recovery appliance, or any other property.



## Configure access levels and direction policies for Compute Engine

If the administrator project and workload project are in the same VPC Service Controls perimeter, you don't need to configure access levels and direction policies. Otherwise choose from one of the following configuration scenarios based on your security perimeter configuration requirements.

  * **If both the administrator project and workload project exist in different service perimeters** : 
    * The administrator project needs to add an egress rule for the backup vault service agent to the workload project for both `backupdr.googleapis.com` and `compute.googleapis.com`.
    * The workload project needs to add an ingress rule to allow calls from the backup vault service agent and an egress rule for the backup vault service agent to the administrator project for both `backupdr.googleapis.com` and `compute.googleapis.com`.
  * **If only the administrator project has a service perimeter** : The administrator project needs to add an egress rule for the backup vault service agent to the workload project for both `backupdr.googleapis.com` and `compute.googleapis.com`.
  * **If only the workload project has a service perimeter** : The workload project needs to add an ingress rule to allow calls from the backup vault service agent and an egress rule for the backup vault service agent to the administrator project for both `backupdr.googleapis.com` and `compute.googleapis.com`.



## Configure access levels and direction policies for Cloud SQL and for AlloyDB

Both the administrator project and the workload project should be inside the same VPC Service Controls perimeter.

## Configure VPC Service Controls for Backup and DR

Use the following steps to configure VPC Service Controls for Backup and DR:

  1. Create a service perimeter
  2. Configure connectivity to Google APIs and services



The following sections describe these steps in detail.

## Create a service perimeter

Use the following instructions to create a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters):

  1. In the Google Cloud console, on the project selector page, select the Backup and DR project that you want the VPC service perimeter to protect.
  2. Create a service perimeter using the instructions described in [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).
  3. Add the following APIs to the [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) in the **Restricted Services** section:

     * Required: Backup and DR API - `backupdr.googleapis.com`
     * Optional: Compute Engine API - `compute.googleapis.com`
     * Optional: Resource Manager API - `cloudresourcemanager.googleapis.com`
     * Optional: Workflows API - `workflows.googleapis.com`
     * Optional: Cloud Key Management Service API - `cloudkms.googleapis.com`
     * Optional: Identity and Access Management API - `iam.googleapis.com`
     * Optional: Cloud Logging API - `logging.googleapis.com`
     * Optional: Cloud Storage API - `storage.googleapis.com`
     * Optional: Cloud SQL Admin API - `sqladmin.googleapis.com`
     * Optional: AlloyDB - `alloydb.googleapis.com`
  4. If you're using a Shared VPC, add the host and service projects in the **Add Resources** section.




Once you set up a perimeter, by default, access to the Backup and DR appliance management console and API is only allowed from within the security perimeter.

If a backup/recovery appliance makes cloud API requests to the outside of the service perimeter, for example, to recover a Compute Engine instance to a project or VPC network that is not in the same perimeter, you may see a VPC Service Controls access violation. To allow API requests, you must create appropriate [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) in the VPC Service Controls service perimeter for the backup/recovery appliance service account.

## Configure connectivity to Google APIs and services

In a VPC Service Controls configuration, to control network traffic, configure access to Google APIs and services through the `restricted.googleapis.com` domain. This domain blocks access to Google APIs and services that don't support VPC Service Controls. For more information, see [domain options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options).

If you don't configure DNS rules for Google APIs and services, they are resolved using the [domain option](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) for default domains.

Backup and DR uses the following domains:

  * `*.backupdr.cloud.google.com` is used to access the appliance management console.
  * `*.googleapis.com` is used to access other Google services.



Configure connectivity to the following `restricted.googleapis.com` endpoints in the DNS record section.

**Domain** | **DNS name** | **CNAME Record** | **A Record**  
---|---|---|---  
`*.googleapis.com` | `googleapis.com.` | DNS Name: `*.googleapis.com.` | Resource record type: `A`  
|  | Resource record type: `CNAME` | IPv4 addresses:  
|  | Canonical name: `googleapis.com.` | `199.36.153.4,`  
|  |  | `199.36.153.5,`  
|  |  | `199.36.153.6,`  
|  |  | `199.36.153.7`  
`*.backupdr.cloud.google.com` | `backupdr.cloud.google.com.` | DNS Name: `*.backupdr.cloud.google.com.` | Resource record type: `A`  
|  | Resource record type: `CNAME` | IPv4 addresses:  
|  | Canonical name: `backupdr.cloud.google.com.` | `199.36.153.4,`  
|  |  | `199.36.153.5,`  
|  |  | `199.36.153.6,`  
|  |  | `199.36.153.7`  
`*.backupdr.googleusercontent.com` | `backupdr.googleusercontent.com` | DNS Name: `*.backupdr.googleusercontent.com.` | Resource record type: `A`  
|  | Resource record type: `CNAME` | IPv4 addresses:  
|  | Canonical name: `backupdr.googleusercontent.com.` | `199.36.153.4,`  
|  |  | `199.36.153.5,`  
|  |  | `199.36.153.6,`  
|  |  | `199.36.153.7`  
  
### Create a DNS record

Use the following instructions to create a DNS record:

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Private**.

  3. In the **Zone name** field, enter a name. For example, `backup-dr-new-zone`.

  4. In the **DNS name** field, enter a name for the zone using a domain name that you own, for example, `backupdr.cloud.google.com`.

  5. Optional: Add a description.

  6. Under **Options** , select **Default (private)**.

  7. Click **Create**.

  8. In the **Zone details** page, click **Add Standard**.

  9. In the **Create record set** page, use the following steps to add a record set for CNAME Record:

     1. In the **DNS Name** field, enter `*.backupdr.cloud.google.com`.
     2. For the **Resource record type** , select **CNAME**.
     3. In the **Canonical name** field, enter `backupdr.cloud.google.com`.
     4. Click **Create**.
  10. In the **Zone details** page, click **Add Standard** and use the following steps to add a record set with IP addresses:

     1. In the **DNS Name** field, enter `*.backupdr.cloud.google.com`.
     2. Select **A** as the **Resource record type**.
     3. In the **IPv4 addresses** field, enter **199.36.153.4** , **199.36.153.5** , **199.36.153.6** , **199.36.153.7**.
     4. Click **Create**.



For more information, see [Set up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

## Troubleshoot

If you encounter any issues while configuring VPC Service Controls for Backup and DR, then refer to VPC Service Controls [troubleshooting](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting) section.

## Limitations

If you have removed the internet default route from the service producer project using `gcloud` command: `gcloud services vpc-peerings enable-vpc-service-controls`, then you may not be able to access or create the appliance management console. Contact [Google Cloud Customer Care](https://cloud.google.com/support) if you run into this issue.

Before you [mount a Compute Engine backup image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances), add the service and host projects to the same perimeter. Otherwise, you may not see the available networks.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
