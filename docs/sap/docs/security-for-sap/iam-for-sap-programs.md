---
url: https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs/
title: Identity and access management for SAP programs on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:01.397419+00:00
---

# Identity and access management for SAP programs on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Identity and access management for SAP programs on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Any application programs that use Google Cloud resources need a Google Cloud identity and permissions before they can access the resources.

## IAM service accounts

On Google Cloud, Identity and Access Management (IAM) uses _service accounts_ to establish identities for programs and _roles_ to grant permissions to the service accounts of the programs.

For SAP systems and related programs that run on Compute Engine virtual machines (VMs), create a VM service account that contains only the roles that the SAP systems and other programs need.

Programs that don't run on Google Cloud can use service accounts when they connect to Google Cloud APIs and use a service account key for authentication.

Programs that run on a Compute Engine VM can use the service account of the VM, as long as the VM service account has the roles the program needs. For programs that are running on a Compute Engine VM, using a service account key for authentication is not recommended.

When you create a VM instance using the Google Cloud CLI or the [Google Cloud console](https://console.cloud.google.com/), you can specify a service account for the VM instance to use, accept the project default service account, or specify no service account.

When you create an instance by making a request to the API directly without using the Google Cloud CLI or the Google Cloud console, the default service account does not come enabled with the instance.

If a VM service account doesn't have the roles the program needs, you can add roles to the VM service account or replace the service account with a new VM service account.

The Compute Engine default service account for a project is initially granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic), which might be too permissive for many enterprise environments.

For more information about the use of roles, permissions, and service accounts by Compute Engine, see:

  * [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts)
  * [Creating and enabling service accounts for instances](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)



For information that applies more broadly across Google Cloud, see the IAM documentation:

  * [IAM overview](https://docs.cloud.google.com/iam/docs/overview)
  * [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
  * [Understanding service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts)



### Deployment automation and service accounts

If you are deploying your SAP infrastructure by using the Terraform configuration files that are provided by Google Cloud, then you can specify a service account in the `DEPLOYMENT_TYPE.tf` file.

If you don't specify a service account, then Terraform deploys the compute instances with the default service account of your Google Cloud project.

## IAM roles and permissions

IAM provides predefined roles for each Google Cloud resource. Each role contains a set of permissions for the resource that are appropriate to the level of the role. You can add these roles to the service accounts that you create.

For the most restrictive or granular control, you can create custom roles with one or more permissions.

For a list of the predefined roles and the permissions that each contains, see [Understanding roles](https://docs.cloud.google.com/iam/docs/roles-permissions).

For more information about custom roles, see [Understanding custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

For more information about roles that are specific to Compute Engine, see [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam) in the Compute Engine documentation.

## IAM roles for SAP systems

The IAM roles that your SAP programs need depends on the resources that the programs use and on the tasks that the programs perform.

For example, if you use Terraform to deploy your SAP system and specify a service account in the Terraform configuration file, then the service account that you specify must include at least the following roles:

  * Service Account User - always required.
  * Compute Instance Admin - always required.
  * Storage Object Viewer - required to download installation media from a Cloud Storage bucket during deployment.
  * Logs Writer - required to write deployment or other messages to Logging.



After the SAP system deploys, the host VM and your SAP programs might not need all of the same permissions that were required during deployment. You can edit the VM service account to remove roles, or change the service account that the VM uses.

Some SAP or related programs require additional roles and, if they are not running on Google Cloud, might require a separate service account. For example:

  * Google Cloud's Agent for SAP requires roles such as Compute Viewer, Monitoring Viewer, and Monitoring Metric Writer. For more information, see [Required IAM roles](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#required_roles).
  * SAP Data Services, when it is configured to [replicate SAP data to BigQuery](https://docs.cloud.google.com/sap/docs/bigquery-replication-from-sap-apps), requires both the BigQuery Data Editor role and the BigQuery Job User role.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
