---
url: https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities/
title: Resource types with built-in identities \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:31:08.700647+00:00
---

# Resource types with built-in identities  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Resource types with built-in identities Stay organized with collections  Save and categorize content based on your preferences. 

Some Google Cloud resources have [built-in identities](https://docs.cloud.google.com/iam/docs/built-in-resource-identities). These identities let the resources act like [principals](https://docs.cloud.google.com/iam/docs/principals-overview). As a result, resources with built-in identities can do the following:

  * Be [granted IAM roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) using the resource's principal identifier
  * Access other resources without using [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)



## Principal identifiers for single resources

The following table lists the resource types that have built-in identities. It also lists the accepted formats for the resource's principal identifier. Use one of the accepted formats for the principal identifier in your allow policies to grant roles to the resource.

Resource type | Principal identifier format  
---|---  
[Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview) parameters |  `principal://parametermanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/global/parameters/PARAMETER_UID`  
[Workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) [ (preview)](https://cloud.google.com/products#product-launch-stages) |  ` principal://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/WORKLOAD_IDENTITY_POOL_NAME`  
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs) data domains [ (preview)](https://cloud.google.com/products#product-launch-stages) |  `principal://dataplex.googleapis.com/projects/PROJECT_NUMBER/name/locations/LOCATION/dataDomains/DATA_DOMAIN_ID`  
  
## Principal identifiers for sets of resources

Use the following formats in your allow policies to grant roles to sets of resources with built-in identities:

**Note:** These principal sets don't include resources that don't have built-in identities.Description | Format  
---|---  
All resources for the specified service in the specified project | `principalSet://RESOURCE_SERVICE/projects/PROJECT_NUMBER/*`  
All resources in the specified project with the specified type | `principalSet://RESOURCE_SERVICE/projects/PROJECT_NUMBER/type/RESOURCE_TYPE/*`  
All resources with the specified ancestor |  `principalSet://RESOURCE_SERVICE/projects/PROJECT_NUMBER/ancestor.name/ANCESTOR_RESOURCE_TYPE/ANCESTOR_RESOURCE_NAME` `principalSet://RESOURCE_SERVICE/projects/PROJECT_NUMBER/ancestor.uid/ANCESTOR_RESOURCE_TYPE/ANCESTOR_RESOURCE_UID`  
All resources with the specified type and the specified ancestor |  `principalSet://RESOURCE_SERVICE/projects/PROJECT_NUMBER/type/RESOURCE_TYPE/ancestor.name/ANCESTOR_RESOURCE_TYPE/ANCESTOR_RESOURCE_NAME` `principalSet://RESOURCE_SERVICE/projects/PROJECT_NUMBER/type/RESOURCE_TYPE/ancestor.uid/ANCESTOR_RESOURCE_TYPE/ANCESTOR_RESOURCE_UID`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
