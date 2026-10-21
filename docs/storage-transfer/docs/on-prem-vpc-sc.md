---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-vpc-sc/
title: Configure VPC Service Controls for file system transfers \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:37.801871+00:00
---

# Configure VPC Service Controls for file system transfers  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure VPC Service Controls for file system transfers Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service supports on-premises transfers to Cloud Storage buckets protected by VPC Service Controls, under the following conditions:

  * Creating a transfer with [Storage Transfer Service API](https://docs.cloud.google.com/storage-transfer/docs/reference/rest) protects all transferred data.

  * Creating a transfer with Google Cloud console protects only file contents. File metadata, such as file names and file sizes, are not protected.




This guide describes the setup required to use Storage Transfer Service to transfer to Cloud Storage buckets within security perimeters.

To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

For information about using VPC Service Controls with Storage Transfer Service, see [Using Storage Transfer Service with VPC Service Controls](https://docs.cloud.google.com/storage-transfer/docs/transfer-with-vpc-sc).

## Prerequisites

To use Storage Transfer Service with VPC Service Controls, the following items need to be located within the same service perimeter:

  * The project used to create on-premises transfer jobs
  * The destination Cloud Storage bucket.



## Supported configurations

Use either of the following methods to configure transfer agents to work with VPC Service Controls:

  * If transfer agents must remain outside of the service perimeter that contains your Cloud Storage bucket and Storage Transfer Service project, add the agents to an access level.

This method is easier to set up, and allows transfer agents to access Google Cloud resources inside and outside the service perimeter.

**Important:** This option does not prevent transfers to buckets outside of the service perimeter. If you are concerned about transfers from on-premises to Cloud Storage buckets outside of the service perimeter, you need to configure Private Google Access with VPC Service Controls to prevent agents from accessing buckets outside of the service perimeter.
  * If transfer agents can be added to the service perimeter that contains your Cloud Storage bucket and Storage Transfer Service project, configure Private Google Access with VPC Service Controls for the on-premises network used by transfer agents.

This method requires more steps to complete, and transfer agents are able to access only the Google Cloud resources within the service perimeter.




### Adding agents to an access level

To add transfer agents to an access level:

  1. Determine how you will add agents to an [access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels): by IP address or by service accounts.

  2. Add the agents to an access level:

     * To add agents' IP addresses to an access level, follow the instructions in [Limit access on a corporate network](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#corporate-network-example).

     * To add agents' service account to an access level, follow the instructions in [Limit access by user or service account](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example).




### Using Private Google Access with VPC Service Controls

To use Private Google Access with VPC Service Controls:

  1. [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#creating_a_service_perimeter) to restrict the following services:

     * Cloud Storage
     * Storage Transfer Service
  2. [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

  3. [Create transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#create-transfer) in a project that is within the service perimeter.




### Troubleshooting

To troubleshoot errors, see [Troubleshooting VPC Service Controls errors](https://docs.cloud.google.com/storage-transfer/docs/troubleshooting-on-prem#vpcsc).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
