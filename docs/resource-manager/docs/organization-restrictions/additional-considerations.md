---
url: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/additional-considerations/
title: Additional considerations \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:30.453991+00:00
---

# Additional considerations  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/additional-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Additional considerations Stay organized with collections  Save and categorize content based on your preferences. 

This page lists additional considerations you must be aware of when using organization restrictions.

### Multi-resource access

Google Cloud API requests might involve operations on multiple resources. Organization restrictions header service checks whether all resources that are part of the request are in the list of authorized organizations. If any resource is not part of the list of authorized organizations, the request is denied.

### Allow download for Vault users

[Google Vault](https://support.google.com/vault/answer/2462365) is an information governance and eDiscovery tool for Google Workspace. Vault administrators access Google Workspace user data stored in Google-owned Cloud Storage buckets.

By default, the organization restrictions feature restricts Vault administrators from downloading an exported Google Workspace user data from a Google-owned Cloud Storage bucket. To allow requests that originate from the Vault administrators, ensure that organization ID `organizations/433637338589`, which stores Vault data, is added to the organization restrictions header.

We recommend to add this ID of the organization, which stores Vault data, only in headers for requests from Vault administrators.

### Enable access to Google-owned resources

To enable developers to use Google Cloud services, such as BigQuery, Compute Engine, or Cloud Workstations, Google Cloud provides Google-owned public resources. For example, Compute Engine provides [public OS images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that help developers quickly get started with building their own image or leverage one of the images in the public OS images repository to host their workloads. Other Google Cloud services employ similar public resource patterns. These public resources are hosted in a Google-owned Google Cloud organization. In addition, some services use resources or [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/manage-tenant-projects) managed under the Google-owned organization. For example, Cloud Workstations runs on tenant projects under the Google-owned organization.

To ensure that users of your Google Cloud organization continue to have access to these public resources after you enforce organization restrictions, add the following Google-owned Google Cloud organization ID to the list of authorized organizations in the organization restrictions header:
    
    
       organizations/433637338589
    

## What's next

  * Learn about [using organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/examples-org-restrictions).
  * Learn about the [services supported by organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/supported-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
