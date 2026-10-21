---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites/
title: Prerequisites for using the Guided Deployment Automation tool \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:09:39.701531+00:00
---

# Prerequisites for using the Guided Deployment Automation tool  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Prerequisites for using the Guided Deployment Automation tool Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the prerequisites for using the Guided Deployment Automation tool in Workload Manager.

In addition, you must meet the following prerequisites that are specific to the application you're deploying:

  * [Prerequisites for deploying an SAP S/4HANA application](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap)
  * [Prerequisites for deploying a SQL Server workload](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/prerequisites-sql)
  * [Prerequisites for deploying an Oracle Database workload](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle)



Prerequisite | Description  
---|---  
**Google Cloud billing account** | You must have a Google Cloud account that is part of your organization with active billing. For more information, see [Create a new billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account#create_a_new_billing_account).  
**Google Cloud project** |  A Google Cloud project in which you want to deploy the application. See [Create and manage projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Make sure that [ the project is linked to the billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).  
**Enable APIs** | Enable the following APIs in your project:  


  * [Workload Manager API](https://console.cloud.google.com/apis/library/workloadmanager.googleapis.com)
  * [Infrastructure Manager API](https://console.cloud.google.com/apis/library/config.googleapis.com)
  * [Cloud Resource Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com)

During the deployment process, Workload Manager automatically enables additional required APIs if they're not enabled in your project.  
**Grant IAM roles to Workload Manager service account** | Workload Manager uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) that needs to be granted the required roles before you can deploy an application. For more information, see  Workload Manager service account.  
**Grant IAM roles to a user-managed service account** | Create a service account and grant all the required roles for deploying your application. For more information, see User-managed service account.  
**IAM roles and permissions** | Users who deploy a workload using the Guided Deployment Automation tool must have or be granted the required roles and permissions to configure the deployment. These users also need permissions to create the necessary service accounts during deployment. For more information, see IAM roles and permissions.  
**Cloud Build private pool** | Optional. If your organization enforces VPC Service Controls perimeter settings for protecting Workload Manager resources and data, then set up a Cloud Build private worker pool to use in your deployment environment. For more information, see Use a Cloud Build private worker pool.  
**Quotas** | Make sure that you have sufficient resource quota in your project to deploy the workload. For more information, see Quotas.  
  
### Workload Manager service account

The Guided Deployment Automation tool uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) for deploying applications.

When you create a deployment, Workload Manager prompts you to grant the required roles to this service account if they're not already granted. If you don't have the permission to grant these roles, ask an administrator to grant the following roles to the Workload Manager service account before creating a deployment.

**Service account** | **Required roles**  
---|---  
Service-PROJECT_ID@gcp-sa-workloadmanager.iam.gserviceaccount.com | 

  * Cloud Infrastructure Manager Admin (`roles/config.admin`)
  * Logs Viewer (`roles/logging.viewer`)
  * Service Account User (`roles/iam.serviceAccountUser`)
  * Workload Manager Service Agent (`roles/workloadmanager.serviceAgent`)

  
  
### User-managed service account

Workload Manager uses the service account attached to your deployment to call other APIs and services for creating resources required for the deployment.

You can either attach an existing service account or create a service account when you configure the deployment. Depending on your application and configuration, Workload Manager prompts you to grant any of the missing roles to your service account.

For more information about granting roles to service accounts, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

### IAM roles and permissions

Access control in Workload Manager is controlled using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam). Workload Manager provides a specific set of [predefined IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#role-types) where each role contains a set of permissions. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.  
The following permission is required to enable the Workload Manager API in the selected project. This task only needs to be performed once in each project. An administrator or another user with the permission can enable the API and after that other users can access Workload Manager.

**Action** | **Permission Required** | **Example Role**  
---|---|---  
Enable Workload Manager API | `serviceusage.services.enable` | `roles/editor`  
`roles/service.Usage.Admin`  
  
Workload Manager also has roles to control who can access the deployment features and determine who can deploy, manage, and view deployments. Each role has the necessary permissions to perform the stated tasks.

For more information, see [Access control with IAM](https://docs.cloud.google.com/workload-manager/docs/access-control). When granting IAM roles to principals, Google recommends that you apply the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Role** | **Deployment task**  
---|---  
Workload Manager Deployment AdminBeta | Create, modify, deploy, and view deployments.  
Workload Manager Deployment ViewerBeta | View deployments.  
  
### Use a Cloud Build private worker pool

If your organization enforces VPC Service Controls compliance, then you must use a private worker pool for your deployment.

Private pools are hosted in a Google-owned Virtual Private Cloud network called the _service producer network_. Before creating a private pool, [set up a private connection between the service producer network and the VPC network that contains your resources](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-to-use-in-vpc-network#setup-private-connection).

To create and use a Cloud Build private pool, follow the instructions in [Create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).

Consider the following requirements when you set up a private worker pool to use with Workload Manager:

  * You must use a Cloud Build private worker pool for the deployment. You cannot use the default Cloud Build worker pool. For more information, see [Limitations](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#limitations) in the Cloud Build documentation.
  * To download the Terraform configuration, the Cloud Build private pool must have [public internet calls enabled](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#enable-public-internet).



You must also ensure that the following resources are in the same [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters):

  * Cloud Build private worker pool.
  * [Workload Manager service account](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#wlm-service-account).
  * The [Cloud Storage bucket](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-install-files#upload-install-files) that Workload Manager uses for deployment.



### Quotas

Google Cloud uses quotas to protect and control the number of resources that a particular account or organization can use. The supported applications often consume a large portion of resources. Given the size of the databases and applications, you might experience quota issues during the deployment process.

To avoid quota issues, do the following:

  1. [View your quota values and usage](https://docs.cloud.google.com/docs/quotas/view-manage).
  2. If needed, [request a higher quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) or contact your project administrator.



## What's next

  * Learn how to [prepare SAP installation files for deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sap-install-files).
  * Learn how to [deploy a SAP S/4HANA workload](https://docs.cloud.google.com/workload-manager/docs/deploy/deploy-sap).
  * Learn how to [deploy an Oracle Database workload](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/oracle-deploy-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
