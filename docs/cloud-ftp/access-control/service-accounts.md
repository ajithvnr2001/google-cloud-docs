---
url: https://docs.cloud.google.com/cloud-ftp/access-control/service-accounts/
title: Cloud FTP service accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:51.455122+00:00
---

# Cloud FTP service accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/access-control/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Cloud FTP service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the service accounts that are relevant to Cloud FTP.

## User-managed service accounts

A [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) is a special type of account designed to provide an identity for non-human workloads, such as applications running on Compute Engine, virtual machines, containerized apps, or other automated services. These accounts enable non-human workloads to programmatically authenticate and make authorized API calls to Google Cloud services. 

User-managed service accounts are typically created and managed by you, but some are created by default when you enable a Google Cloud service. You still manage default service accounts directly. 

Service accounts act as both principals _and_ resources. [As a principal](https://docs.cloud.google.com/iam/docs/service-account-overview#service-accounts-identities), you can grant service accounts access to Google Cloud resources. [As a resource](https://docs.cloud.google.com/iam/docs/service-account-overview#service-accounts-resources), you can give other principals permission to access the service account. 

### Service accounts for SFTP users

Each SFTP user must be mapped to a service account. The service account accesses Cloud Storage resources on behalf of the user.

When you create an SFTP user, you also create a service account for the user, if a service account doesn't already exist. You also grant the service account the IAM roles that are necessary to read or write data in a Cloud Storage bucket, as follows:

  * Read-only access: [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)
  * Read and write access: [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)



We recommend that you use a dedicated service account for each user so that you can manage SFTP access separately for each user.

## Service agents

Service agents are service accounts that are created and managed by Google. Service agents act as an identity for Google Cloud services to access resources within your project on your behalf. 

Service agents are created at some point after you enable and use a Google Cloud API. Upon creation, Google often grants a specific, predefined IAM role to the service agent on your project. These roles contain the minimum permissions required for the service agent to function correctly. For a full list of service agents that are granted roles, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents) in the IAM documentation. 

### Cloud FTP Service Agent

Each SFTP server is associated with a service agent. The Cloud FTP Service Agent generates tokens for SFTP users' service accounts.

The Cloud FTP Service Agent is created after you create a server. When you add users to the server, you must grant the server's service agent the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role on each user's service account.

The email address of the Cloud FTP Service Agent uses a format like `p-PROJECT_ID-SERVICE_ACCOUNT_ID@gcp-sa-ftp.iam.gserviceaccount.com`. For steps to get the email address of a specific server's service agent, see [Get SFTP server information](https://docs.cloud.google.com/cloud-ftp/get-server-information).

## What's next

  * To learn more about service accounts, see [Service account overview](https://docs.cloud.google.com/iam/docs/service-account-overview) in the IAM documentation. 
  * To learn more about service agents, see [Service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) in the IAM documentation. 
  * To learn how to use service accounts securely, see [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) in the IAM documentation. 
  * [Create an external SFTP server](https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server) that can be accessed over the internet.
  * [Create an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/create-internal-sftp-server) that can be accessed only within your VPC network.
  * [Add users to an SFTP server](https://docs.cloud.google.com/cloud-ftp/add-sftp-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
