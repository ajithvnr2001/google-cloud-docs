---
url: https://docs.cloud.google.com/memorystore/docs/valkey/use-vpc-service-controls/
title: Use VPC Service Controls with Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:31.972831+00:00
---

# Use VPC Service Controls with Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/use-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Use VPC Service Controls with Memorystore for Valkey Stay organized with collections  Save and categorize content based on your preferences. 

You can protect your Memorystore for Valkey instances using VPC Service Controls.

VPC Service Controls protect against data exfiltration and provide an extra layer of security for your instances. For more information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Once the Memorystore for Valkey API is protected by your service perimeter, Memorystore for Valkey API requests coming from clients outside of the perimeter must have the proper access level rules.

**Note:** Modifications to VPC Service Controls settings for Memorystore for Valkey take on the order of minutes to take effect.

## Protect your Valkey instances using VPC Service Controls

  1. [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  2. Add the Memorystore for Valkey API to your service perimeter. For instructions on adding a service to your service perimeter, see [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).




## Configuration requirements

If you use both Shared VPC and VPC Service Controls, you must have the host project that provides the network and the service project that contains the Valkey instance inside the same perimeter in order for Valkey requests to succeed. Otherwise, requests between the service project instance and the host project network are blocked by the VPC Service Controls service perimeter.

At any time, separating the host project and service project with a perimeter can cause a Valkey instance failure, in addition to blocked requests.

For more information about limitations when using VPC Service Controls with Memorystore for Valkey, see [Memorystore for Valkey](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_memorystore_for_valkey).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
