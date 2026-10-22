---
url: https://docs.cloud.google.com/data-fusion/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:51.913964+00:00
---

# Access control with IAM  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes access control options in Cloud Data Fusion.

You can control access to resources in Cloud Data Fusion in the following ways:

  * To control access for [control plane](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#data-fusion-web-interface) operations, such as creating and updating instances through the Google Cloud console, [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion), and [REST API](https://docs.cloud.google.com/data-fusion/docs/reference/rest), use Identity and Access Management (IAM), as described on this page.

  * To grant access to Google Cloud data services, such as BigQuery or Cloud Storage to a service account where pipelines are running, use IAM.

  * To control granular permissions for actions performed in the instance, known as [data plane](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#data-fusion-studio) operations, such as starting pipelines, use role-based access control ([RBAC](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac)).

**Note:** RBAC roles aren't typically assigned to pipeline service accounts.



For information about the architecture and resources involved in Cloud Data Fusion access control, see [Networking](https://docs.cloud.google.com/data-fusion/docs/concepts/networking). For information about granting roles and permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## About IAM in Cloud Data Fusion

You control access to Cloud Data Fusion features by granting IAM roles and permissions to [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) and other principals in your Google Cloud project.

To grant fine-grained access to user accounts so that they can use the Cloud Data Fusion web interface, use [RBAC](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac).

**Key Point:** You control access for Cloud Data Fusion at the _project level_. For example, you can grant access to all Cloud Data Fusion resources within a project to a group of developers.

By default, Cloud Data Fusion uses the following service accounts:

  * The Cloud Data Fusion Service Account
  * The Compute Engine default service account



### Cloud Data Fusion Service Account

The Cloud Data Fusion Service Account is a Google-managed service agent that can access customer resources at pipeline design time. This service agent is automatically added to a project when you enable the Cloud Data Fusion API. It's used for all instances in your project.

The service agent has the following responsibilities:

  * Communicating with other services, such as Cloud Storage, BigQuery, or Datastream during pipeline design.

  * Enabling execution by provisioning Managed Service for Apache Spark clusters and submitting pipeline jobs.




#### Roles for the Cloud Data Fusion Service Account

By default, the Cloud Data Fusion service account has only the [Cloud Data Fusion API Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`).

The principal name for this service agent is `service-CUSTOMER_PROJECT_NUMBER@gcp-sa-datafusion.iam.gserviceaccount.com`.

**Note:** To prevent access control issues, we recommend keeping the default role and permissions on the Cloud Data Fusion Service Account. You can add roles based on your use case.

The following default resources are associated with the Cloud Data Fusion API Service Agent role.

Role | Resource | Permissions  
---|---|---  
Cloud Data Fusion API Service Agent | Associated services:  


  * BigQuery
  * Bigtable
  * Compute Engine
  * Managed Service for Apache Spark
  * Cloud DNS
  * Firebase
  * Cloud Monitoring
  * Network Connectivity
  * Network Security Integration
  * Network Services API
  * Organization Policy
  * Recommender API
  * Cloud Resource Manager API
  * Service Networking
  * Service Usage
  * Spanner
  * Cloud Storage
  * Cloud Service Mesh

| See the [Cloud Data Fusion API Service Agent permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent).  
  
### Compute Engine default service account or custom service account

The Compute Engine service account is the default account that Cloud Data Fusion uses to deploy and run jobs that access other Google Cloud resources. By default, it attaches to a Managed Service for Apache Spark cluster VM to let Cloud Data Fusion access Managed Service for Apache Spark resources during a pipeline run.

You can choose a custom service account to attach to the Managed Service for Apache Spark cluster when creating a Cloud Data Fusion instance or by creating new Compute Profiles in the Cloud Data Fusion web interface.

For more information, see [Service accounts in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts).

#### Roles for the Compute Engine service account

By default, to access resources (such as sources and sinks) when you run a pipeline, Cloud Data Fusion uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

**Caution:** If your instance uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), don't remove roles. Removing them might cause problems with other Google Cloud services.

You can set up a _user-managed custom service account_ for Cloud Data Fusion instances and grant a role to this account. Afterwards, you can choose this service account when creating new instances.

**Note:** If you launch Managed Service for Apache Spark clusters in a different Google Cloud project, [grant the roles in the project where Managed Service for Apache Spark is running](https://docs.cloud.google.com/data-fusion/docs/use-case/dataproc-in-different-project#dataproc-iam). By default, you grant them in the project containing the Cloud Data Fusion instance.

#### Cloud Data Fusion Runner role

In the project containing the Cloud Data Fusion instance, for both default and user-managed custom service accounts, grant the Cloud Data Fusion Runner role (`datafusion.runner`).

Role | Description | Permission  
---|---|---  
Data Fusion Runner `(datafusion.runner)` | Lets the Compute Engine service account communicate with Cloud Data Fusion services in the [tenant project](https://docs.cloud.google.com/data-fusion/docs/concepts/networking#expandable-1) | `datafusion.instances.runtime`  
  
#### Service Account User role

On the default or user-managed service account in the project where Managed Service for Apache Spark clusters are launched when you run pipelines, grant the Cloud Data Fusion Service Account the Service Account User role (`roles/iam.serviceAccountUser`).

For more information, see [Grant service account permission](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission).

#### Dataproc Worker role

To run the jobs on Managed Service for Apache Spark clusters, grant the Dataproc Worker role (`roles/dataproc.worker`) to the default or user-managed service accounts used by your Cloud Data Fusion pipelines.

### Roles for users

To trigger any operation in Cloud Data Fusion, you (the principal) must have enough permissions. Individual permissions are grouped into roles, and you grant roles to that principal.

**Note:** The rest of this page describes managing permissions using IAM for access control. To use RBAC, see [RBAC roles and permissions](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac-roles-and-permissions).

If RBAC isn't enabled, or if you're using a Cloud Data Fusion edition that doesn't support RBAC, users with any Cloud Data Fusion IAM role have full access to the Cloud Data Fusion web interface. The Admin role only allows users to manage the instance, such as `Create`, `Update`, `Upgrade`, and `Delete` operations.

Grant the following roles to principals, depending on the permissions they need in Cloud Data Fusion.

Role | Description | Permissions  
---|---|---  
Cloud Data Fusion Admin (`roles/datafusion.admin`) | All viewer permissions, plus permissions to create, update, and delete Cloud Data Fusion instances. | 

  * `datafusion.instances.get`
  * `datafusion.instances.list`
  * `datafusion.instances.create`
  * `datafusion.instances.delete`
  * `datafusion.instances.update`
  * `datafusion.operations.get`
  * `datafusion.operations.list`
  * `datafusion.operations.cancel`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`

  
Cloud Data Fusion Viewer (`roles/datafusion.viewer`) | 

  * Can view the project's Cloud Data Fusion instances in the Google Cloud console.
  * Cannot create, update, or delete Cloud Data Fusion instances.

| 

  * `datafusion.instances.get`
  * `datafusion.instances.list`
  * `datafusion.operations.get`
  * `datafusion.operations.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`

  
  
## Access resources in another project at design time

This section describes access control on resources that are located in a different Google Cloud project than your Cloud Data Fusion instance at design time.

When you design pipelines in the Cloud Data Fusion web interface, you might use functions, such as Wrangler or Preview, which access resources in other projects.

The following sections describe how you determine the service account in your environment and then give the appropriate permissions.

### Determine the service account of your environment

The service account name is Cloud Data Fusion Service Account and the principal for this service agent is `service-CUSTOMER_PROJECT_NUMBER@gcp-sa-datafusion.iam.gserviceaccount.com`.

### Give permission to access resources in another project

To grant the roles that give permission to access various resources, follow these steps:

  1. In the project where the target resource exists, add the Cloud Data Fusion Service Account (`service-CUSTOMER_PROJECT_NUMBER@gcp-sa-datafusion.iam.gserviceaccount.com`) as a principal.
  2. Grant roles to the Cloud Data Fusion Service Account on the target resource in the project where the target resource exists.



After you grant the roles, you can access resources in a different project at design time in the same way that you access resources in the project where your instance is located.

## Access resources in another project at execution time

This section describes access control on resources that are located in a different Google Cloud project than your Cloud Data Fusion instance at execution time.

At execution time, you execute the pipeline on a Managed Service for Apache Spark cluster, which may access resources in other projects. By default, the Managed Service for Apache Spark cluster itself is launched in the same project as the Cloud Data Fusion instance, but you can use clusters in another project.

To access the resources in other Google Cloud projects, follow these steps:

  1. Determine the service account for your project.
  2. In the project where the resource is, grant IAM roles to the Compute Engine default service account to give it access to resources in another project.



### Determine the Compute Engine service account

For more information about the Compute Engine service account, see About IAM in Cloud Data Fusion.

### Grant IAM access resources in another project

The Compute Engine default service account requires permissions to access resources in another project. These roles and permissions can be different depending on the resource you want to access.

To access the resources, follow these steps:

  1. Grant roles and permissions, specifying your Compute Engine service account as a principal in the project where the target resource exists.
  2. Add appropriate roles to access the resource.

**Note:** For more information, see the related [use case](https://docs.cloud.google.com/data-fusion/docs/use-case/dataproc-in-different-project) for running Managed Service for Apache Spark clusters in another project. This use case has a service account that's defined in the other project and has access to BigQuery resources in that project. You can elaborate on the use case for other scenarios.

## Cloud Data Fusion API permissions

The following permissions are required to execute the [Cloud Data Fusion API](https://docs.cloud.google.com/data-fusion/docs/reference/rest).

API call | Permission  
---|---  
`instances.create` | `datafusion.instances.create`  
`instances.delete` | `datafusion.instances.delete`  
`instances.list` | `datafusion.instances.list`  
`instances.get` | `datafusion.instances.get`  
`instances.update` | `datafusion.instances.update`  
`operations.cancel` | `datafusion.operations.cancel`  
`operations.list` | `datafusion.operations.list`  
`operations.get` | `datafusion.operations.get`  
  
## Permissions for common tasks

Common tasks in Cloud Data Fusion require the following permissions:

Task | Permissions  
---|---  
Accessing the Cloud Data Fusion web interface | `datafusion.instances.get`  
Accessing the Cloud Data Fusion **Instances** page in the Google Cloud console | `datafusion.instances.list`  
Accessing the **Details** page for an instance | `datafusion.instances.get`  
Creating a new instance | `datafusion.instances.create`  
Updating labels and advanced options to customize an instance | `datafusion.instances.update`  
Deleting an instance | `datafusion.instances.delete`  
  
## What's next

  * Learn more about [access control between multiple projects](https://docs.cloud.google.com/data-fusion/docs/use-case/dataproc-in-different-project).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
