---
url: https://docs.cloud.google.com/cloud-ftp/configure-vpc-service-controls/
title: Configure VPC Service Controls for Cloud FTP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:51.499780+00:00
---

# Configure VPC Service Controls for Cloud FTP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Configure VPC Service Controls for Cloud FTP Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud FTP requires access to Cloud Storage buckets in order to upload and download data in the buckets. If your organization uses VPC Service Controls to help protect Cloud Storage, then extra setup is required to use Cloud FTP to transfer data. This document describes how to create a VPC Service Controls service perimeter with ingress rules that allow Cloud FTP to transfer Cloud Storage data that is stored within the perimeter.

For background information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Required roles

To get the permissions that you need to create a service perimeter, ask your administrator to grant you the [Access Context Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure the service perimeter

To allow an SFTP server to transfer Cloud Storage data in a perimeter, follow the steps to [create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters). Provide the following information:

  * **Perimeter type** : select **Regular**.
  * **Resources to protect** : add the following projects to the perimeter: 
    * The projects that contain the Cloud Storage buckets that you want to help protect
    * The project that contains the SFTP server
  * **Restricted services** : add the following services to the perimeter: 
    * Cloud FTP API (`ftp.googleapis.com`)
    * Cloud Storage API (`storage.googleapis.com`)
  * **VPC accessible services** : select **All restricted services**.
  * **Access levels** : add an access level with the following conditions: 
    * **When condition is met, return** : select **True**.
    * Select **Public IP**.
    * **IP subnetworks** : the IP addresses or CIDR ranges of the SFTP clients that connect to the server.
  * **Ingress policy** : 
    * In the **From** section, provide the following values: 
      * **Identities** : select **Any identity** to provide access to all users of the SFTP server. Or, if you want to limit access only to specific users, then provide the email addresses of the users' service accounts. For steps to get a user's service account, see [Get details about a user](https://docs.cloud.google.com/cloud-ftp/get-user-information#get-user).
      * **Sources:** select the access level that you created.
    * In the **To** section, provide the following values: 
      * **Resources** : select the projects that contain the Cloud Storage buckets that you want to help protect.
      * **Operations or IAM roles** : 
        * Add an ingress rule targeting `ftp.googleapis.com`.
        * If Cloud Storage (`storage.googleapis.com`) is protected by device posture access levels, such as Chrome Enterprise Premium, then also add a method-level ingress rule targeting `storage.googleapis.com`. Restrict the API methods to Cloud FTP long-running operations: `ftp.googleapis.com/operations.*`



## Other configuration options

  * If the project that contains the Cloud Storage buckets is in an existing service perimeter, then you can update the perimeter's [access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) and [ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) to add protection for the Cloud FTP API service.
  * If your Cloud Storage and Cloud FTP resources are in different service perimeters, then [create a perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/create-perimeter-bridges) to allow projects and services in different perimeters to communicate.



## Limitations

  * For external servers, perimeter enforcement applies dynamically whenever the `ftp.googleapis.com` service is included in the perimeter's restricted services list.
  * For internal servers, perimeter enforcement is validated only when the server is created. This behavior means that if you change a perimeter after you create an internal server, any perimeter changes (such as perimeter membership, ingress policies, or network associations) aren't detected or enforced on the existing internal server. You must recreate the internal server to enforce the updated perimeter controls.
  * SFTP and SSH sessions don't carry device posture metadata, such as Chrome Enterprise Premium device attributes or Endpoint Verification certificates. This behavior means that ingress rules can enforce only IP address and identity conditions.



## Troubleshooting

For help troubleshooting, see [VPC Service Controls troubleshooting](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).

## What's next

  * [Create an external SFTP server](https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server)
  * [Create an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/create-internal-sftp-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
