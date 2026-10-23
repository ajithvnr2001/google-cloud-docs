---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance/
title: Create a public instance \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:18.974740+00:00
---

# Create a public instance  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create a public instance Stay organized with collections  Save and categorize content based on your preferences. 

A public Cloud Data Fusion [instance](https://docs.cloud.google.com/data-fusion/docs/concepts/overview) lets you build and manage data integration pipelines that connect to publicly accessible endpoints. This default instance type uses your project's default VPC network to run execution clusters and connect to external endpoints over the public internet.

## Before you begin

  * [Enable the Cloud Data Fusion API](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-service).
  * The following permission is required to create Cloud Data Fusion instances: `instances.create`. For more information, see [Access control](https://docs.cloud.google.com/data-fusion/docs/access-control).
  * Cloud Data Fusion instances run as the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_default_service_account). For information about the types and roles available, see [Service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed_service_accounts).
  * By default, Cloud Data Fusion executes pipelines using a Managed Service for Apache Spark cluster in your project. Ensure that your project meets the [Managed Service for Apache Spark networking requirements](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network).
  * New projects start with a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network). The default network is pre-populated with a firewall rule [default-allow-ssh](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc), that allows incoming connections on TCP port 22 from any source to any instance in the network. In versions earlier than 6.2.0, if this rule to allow ingress on TCP port 22 doesn't exist in the network used by your Cloud Data Fusion instance, you must [create this rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).



## Create an instance

**Caution:** After you create a Cloud Data Fusion instance, you cannot change its edition.

### Console

If the [API is enabled](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-service), the Cloud Data Fusion section in the Google Cloud console shows an **Instances** page, where you can create and manage your Cloud Data Fusion instances.

  1. In the console, go to the Cloud Data Fusion page.
  2. Click **Instances** , and then click **Create an instance**. 

[ Create an instance](https://console.cloud.google.com/data-fusion/instance-create)

  3. Enter an **Instance name**.
  4. Enter a **Description** for your instance.
  5. Specify the **Region** in which to create the instance.
  6. Specify the Cloud Data Fusion [**Version**](https://docs.cloud.google.com/data-fusion/docs/release-notes).
  7. Select an [**Edition**](https://cloud.google.com/data-fusion/pricing). The default is **Basic**.
  8. Optional: Click **Add accelerators** to select accelerators to use in your instance.
  9. Specify the [**Managed Service for Apache Spark service account**](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts) to use for running your Cloud Data Fusion pipeline in Managed Service for Apache Spark. The default is the Compute Engine account. Regardless of version, make sure that a service account has appropriate Identity and Access Management roles for your needs. For more information, see [Granting service account user permission](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission).
  10. Optional: Specify any advanced options. If you don't specify anything, the following defaults are used:

Category | Setting | Description | Default  
---|---|---|---  
**Private IP** | Enable internal IP addresses | [Create the Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip) with an internal IP address.  | Disabled  
**Advanced monitoring and logging** | Enable Managed Service for Apache Spark Cloud Logging Enable Managed Service for Apache Spark Cloud Monitoring | [View advanced pipeline logs in Cloud Logging](https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs).  | Disabled  
**Knowledge Catalog data lineage integration** | Enable or disable integration with Knowledge Catalog data lineage | [View lineage in Knowledge Catalog](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex). | Disabled  
**Encryption** | Use a customer-managed encryption key (CMEK) | Use [ role-based access control](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac) in versions 6.5 and later. | Disabled  
**Labels** | A key-value pair | The resource labels for the instance to use to annotate any related underlying resources, such as Compute Engine VMs. Label keys and label values can only contain letters, numbers, dashes, and underscores. Label keys must start with a letter or number. | None  
**Maintenance** | Enable maintenance window | Set the window of time when Cloud Data Fusion can perform maintenance operations on the instance. For more information, see [ Configure maintenance windows](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-maintenance-windows). | Disabled  
  11. Click **Create**. It takes up to 30 minutes for the instance creation process to complete.




While Cloud Data Fusion creates your instance, a progress wheel displays next to the instance name on the **Instances** page. After completion, it turns into a green check mark and indicates that you can start using the instance.

After you create an instance, you cannot add or remove the options for [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs#enabling-stackdriver) or [Private IP](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip). To update these options with the Cloud Data Fusion API, call the [ `PATCH`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/patch) method. 

### API

Create an instance:

To create a Cloud Data Fusion instance with the [Cloud Data Fusion REST API](https://docs.cloud.google.com/data-fusion/docs/reference/rest), construct an [`instances.create`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/create) API request, filling in the [`Instance`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Instance) resource with your configuration information.

## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview).
  * Work through a [tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials/targeting-campaign-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
