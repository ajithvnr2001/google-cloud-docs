---
url: https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc/
title: Configure VPC Service Controls for cloud object storage transfers \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:42.488253+00:00
---

# Configure VPC Service Controls for cloud object storage transfers  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure VPC Service Controls for cloud object storage transfers Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service supports transfers to Cloud Storage buckets protected by VPC Service Controls.

Storage Transfer Service requires access to Cloud Storage buckets in order to move data into or between Cloud Storage buckets. If you have buckets within a VPC Service Controls service perimeter, extra setup is required to use Storage Transfer Service to transfer data to Cloud Storage.

To protect your [`TransferJob`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs) and [`TransferOperation`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations) requests, you can add the Storage Transfer Service API as a protected service to your service perimeters. To protect the underlying Cloud Storage buckets and objects, you also need to add the Cloud Storage API as a protected service to your service perimeter.

To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

For information about using VPC Service Controls with file system transfers, see [Configure VPC Service Controls for file system transfers](https://docs.cloud.google.com/storage-transfer/docs/on-prem-vpc-sc).

## Supported configurations

You can configure Storage Transfer Service to work with Cloud Storage buckets protected by VPC Service Controls with the following methods:

  * You can add your Storage Transfer Service project to the service perimeter of your Cloud Storage buckets if either of the following are true:

    * You can configure your Cloud Storage buckets within a single service perimeter.
    * All of your Cloud Storage buckets are within the same service perimeter.

This option is the easiest option to set up and manage.

  * Create a perimeter bridge to all projects that contain the Cloud Storage buckets you're using in a transfer if either of the following are true:

    * You cannot change the service perimeters of your Cloud Storage buckets.
    * You have Cloud Storage buckets in different service perimeters.

This option allows your Storage Transfer Service project to transfer data between your Cloud Storage projects, even if both projects are in different service perimeters. This option also ensures that access to your Cloud Storage bucket perimeters is from a restricted set of services and resources.

  * Add the Storage Transfer Service service account to an access level if any of the following apply to you:

    * Your Storage Transfer Service project is outside of your Cloud Storage bucket's service perimeter.
    * Your service account doesn't fit the form `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`, even if the service account belongs to a project inside a perimeter.

To find your service account's format, use the [`googleServiceAccounts.get`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get) API call.

This option doesn't require you to place the Storage Transfer Service project within a service perimeter. It also lets you configure the access level to only allow requests from the Storage Transfer Service service account.




### Service perimeter

To use a service perimeter, follow the instructions in [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) to include the following projects and services:

  * The `TransferJob` project
  * Cloud Storage bucket projects
  * Cloud Storage API (storage.googleapis.com)
  * Storage Transfer Service API (storagetransfer.googleapis.com)



### Perimeter bridge

**Note:** A perimeter bridge is necessary only if the projects are in different perimeters.

To use a perimeter bridge:

  1. Create a service perimeter for Storage Transfer Service.

  2. [Create a perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/create-perimeter-bridges) to connect:

     * The `TransferJob` project
     * Cloud Storage bucket projects



### Access level

To use an access level, follow the instructions in [Creating an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) to grant access to the [`TransferJob` service account](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts).

After you create your access level, [add the access level to your service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level) that restricts access to the Google Cloud projects containing your Cloud Storage buckets.

## External data sources

VPC Service Controls is designed to protect Google Cloud resources and prevent unauthorized data exfiltration out of a service perimeter.

By design, VPC Service Controls does not block data transfers from external data sources outside of Google Cloud (such as Amazon S3, Microsoft Azure Blob Storage, or HTTP/HTTPS URLs) into Cloud Storage buckets within a service perimeter. VPC Service Controls does not evaluate perimeter boundaries or require egress rules for external data sources.

If you want to restrict transfers from external data sources:

  * Enforce [custom organization policy constraints](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints). For example, you can create a constraint to restrict transfers to only allow Cloud Storage to Cloud Storage transfers.



## Troubleshooting

For help troubleshooting, see [VPC Service Controls Troubleshooting](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
