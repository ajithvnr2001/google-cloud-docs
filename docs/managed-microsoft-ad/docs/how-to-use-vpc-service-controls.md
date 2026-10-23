---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-controls/
title: Configure VPC Service Controls \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:37.687731+00:00
---

# Configure VPC Service Controls  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls provides additional security for the Managed Service for Microsoft Active Directory service and its resources. For more information, see [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Additional configuration

Enabling on-premises access to Managed Microsoft AD API and using a Shared VPC with the Managed Microsoft AD domain require additional configuration.

### Enabling on-premises access to Managed Microsoft AD API

To enable on-premises access to the Managed Microsoft AD API, you must [set up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

### Using a Shared VPC

When using a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), the Managed Microsoft AD domain must be created in the host project and the Shared VPC network host must be located within the same service perimeter as the projects connected to the network.

For information about how to deploy Managed Microsoft AD with cross-project access using Shared VPC, see [Deploy Managed Microsoft AD with cross-project access using domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/shared-vpc-managedad-cloudsql).

## What's next

  * Learn more about the [VPC Service Controls support for Managed Microsoft AD](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_ad)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
