---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle/
title: Prerequisites for deploying an Oracle Database workload \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:28.903419+00:00
---

# Prerequisites for deploying an Oracle Database workload  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Prerequisites for deploying an Oracle Database workload Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the prerequisites for deploying an Oracle Database workload on Google Cloud using Workload Manager.

You must first meet the [prerequisites for using the Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites) tool before deploying an Oracle Database workload.

Prerequisite | Description  
---|---  
**Google Cloud network resources** | Create or select a VPC network and subnetwork for your Oracle Database deployment, and enable Private Google Access.  
**Service accounts** | Create the required service accounts for the deployment and make sure that the service accounts have all the roles required for deploying your workload. For more information, see Service accounts.  
**Secrets for Oracle Database workload** | To store and manage passwords for your database, you must use secrets created using Secret Manager. For more information, see Secrets for Oracle Database workload.  
**Quotas** | Make sure that you have sufficient resource quota in your project to deploy the Oracle database. For more information, see Quotas.  
**Cloud Storage bucket** | Create a Cloud Storage bucket in the project in which you want to host your Oracle software installation files. For more information, see Cloud Storage bucket.  
  
## VPC network and subnet

If your project has a default VPC network, don't use it for creating a deployment. Instead, we recommend that you create your own VPC network so that the only firewall rules in effect are those that you create explicitly for the network. [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and subnet or contact your Google Cloud organization's networking team.

During the deployment process, Workload Manager automatically creates the necessary firewall rules for the deployment.

### Enable Private Google Access

To make sure that your VM can access Google Cloud APIs and services, such as Cloud Monitoring, without needing an internet route you must enable Private Google Access for the VM's subnet.

**Note:** If you've a high availability deployment, make sure that you enable Private Google Access on the subnets for both primary and secondary locations.

To learn how to enable Private Google Access, see [Private Google Access configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).

## Service accounts

**Note:** Workload Manager service account and user-managed service account are only required for deployment, and can be removed after the deployment is complete.

Workload Manager uses the following service accounts for your Oracle deployment:

  * [Workload Manager service account](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#wlm-service-account): This service account is used to grant required IAM roles and permissions to the Workload Manager for creating deployments. Workload Manager service account requires the following roles for an Oracle deployment:

**Service account** | **Required roles**  
---|---  
Service-PROJECT_ID@gcp-sa-workloadmanager.iam.gserviceaccount.com | 
    * Cloud Infrastructure Manager Admin (`roles/config.admin`)
    * Logs Viewer (`roles/logging.viewer`)
    * Service Account User (`roles/iam.serviceAccountUser`)
    * Workload Manager Service Agent (`roles/workloadmanager.serviceAgent`)
    * Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)
    * Storage Object Viewer (`roles/storage.objectViewer`)
    * Compute Network Viewer (`roles/compute.networkViewer`)  
  * [User-managed service account](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#user-service-account): This service account is attached to your deployment and it calls other APIs and services to create the Google Cloud resources required for the deployment, such as VMs, disks, firewall rules, and Artifact Registry repositories.

  * Compute Engine service account: This service account is attached to the database VMs that are created during the deployment process.

**Caution:** We recommend creating a new Compute Engine service account. Using the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) and giving the account access to Secret Manager significantly increases the security risk. Instead, we recommend that you create a [single-purpose service account](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#single-purpose) and [limit user's shell access to VMs](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#shell-access).



Depending on your application and configuration, Workload Manager might prompt you to grant any missing IAM roles and permissions to your service account.

## Secrets for Oracle Database workloads

The Guided Deployment Automation tool uses [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store passwords needed during the deployment process, such as the passwords for user accounts. Plain text passwords are prohibited in accordance with our [Terraform best practices](https://cloud.google.com/docs/terraform/best-practices-for-terraform#secrets).

Before creating an Oracle Database deployment, create the following two secrets:

  * Secret for Oracle database credentials. This includes passwords for `SYS` and `SYSTEM` users. If you're using Oracle multitenant, this includes the password for the `PDBADMIN` user.
  * Secret for database monitoring credentials. If you're using Cloud Monitoring, this secret includes the password that is used by the Agent for Compute Workloads to authenticate your database for metric collection.



You must create secrets in the same project in which you're deploying the Oracle workload. To learn how to create a secret, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

To ensure that the secrets meet the Oracle password requirements, follow these guidelines:

  * Password must be between 8 to 30 characters.
  * Must contain at least one uppercase letter.
  * Must contain at least one lowercase letter.
  * Must contain at least one digit.
  * Must contain at least one special character. The allowed special characters are: `# $ @ % * _ + = -`.
  * Must not contain common disallowed words, such as "oracle".



After successful deployment, you can modify or assign new passwords to these users.

## Quotas

Google Cloud uses quotas to protect and control the number of resources that a particular account or organization can use. Oracle Database workloads often consume a large portion of resources. Given the size of the databases and applications, you might experience quota issues during the deployment process.

To avoid quota issues, do the following:

  1. [View available resource quota for your project](https://docs.cloud.google.com/docs/quotas/view-manage).
  2. If needed, [request a higher quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) or contact your project administrator.



## Cloud Storage bucket

[Create an empty Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/discover-object-storage-console) to be used to host the Oracle software installation files during the deployment process. The bucket must exist within the project in which you're creating the deployment.

## What's next

  * Learn how to [deploy an Oracle Database workload](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/deploy-oracle).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
