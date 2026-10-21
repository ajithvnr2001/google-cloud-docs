---
url: https://docs.cloud.google.com/assured-workloads/docs/control-packages/switzerland-data-boundary-access-justifications/
title: Switzerland Data Boundary with Access Justifications \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:32:08.894839+00:00
---

# Switzerland Data Boundary with Access Justifications  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/control-packages/switzerland-data-boundary-access-justifications/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Switzerland Data Boundary with Access Justifications

This page describes the set of controls that are applied on Switzerland Data Boundary with Access Justifications workloads in Assured Workloads. It provides detailed information about [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency), supported Google Cloud products and their API endpoints, and any applicable restrictions or limitations on those products. The following additional information applies to Switzerland Data Boundary with Access Justifications:

  * **Data residency** : The Switzerland Data Boundary with Access Justifications control package sets data location controls to support [Switzerland-only regions](https://docs.cloud.google.com/assured-workloads/docs/locations#europe). See the Google Cloud-wide organization policy constraints section for more information.
  * **Support** : Technical support services for Switzerland Data Boundary with Access Justifications workloads are available with Enhanced or Premium [Cloud Customer Care](https://docs.cloud.google.com/support) subscriptions. Switzerland Data Boundary with Access Justifications workloads support cases are routed to EU personnel located in the EU. For more information, see [Getting support](https://docs.cloud.google.com/assured-workloads/docs/getting-support#eu-data-boundary-access-justifications).
  * **Pricing** : The Switzerland Data Boundary with Access Justifications control package is included in the Assured Workloads _Premium tier_ , which incurs a 5% additional charge. For more information, see [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing).



## Prerequisites

Verify that you meet and have completed the following prerequisites before deploying workloads to Switzerland Data Boundary with Access Justifications:

  * Create an Switzerland Data Boundary with Access Justifications folder using Assured Workloads and deploy your workloads only in that folder.
  * Don't change the default organization policy constraint values unless you understand and are willing to accept the data residency risks that might occur.
  * Don't use [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) unless otherwise noted. Switzerland Data Boundary with Access Justifications doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page.
  * When accessing the Google Cloud console for Switzerland Data Boundary with Access Justifications workloads, you must use one of the following Switzerland-specific [Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console) URLs: 
    * [console.ch.cloud.google.com](https://console.ch.cloud.google.com)
    * [console.ch.cloud.google](https://console.ch.cloud.google) for federated identity users
  * Consider adopting the general security best practices provided in the [Google Cloud security best practices center](https://cloud.google.com/security/best-practices).



## Supported products and API endpoints

Unless otherwise noted, users can access all supported products through the Google Cloud console. Restrictions or limitations that affect the features of a supported product, including those that are enforced through [organization policy constraint settings](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#how_organization_policy_works), are listed in the following table.

If a product is not listed, that product is unsupported and has not met the control requirements for Switzerland Data Boundary with Access Justifications. Unsupported products are not recommended for use without due diligence and a thorough understanding of your responsibilities in the [shared responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility). Before using an unsupported product, ensure that you are aware of and are willing to accept any associated risks involved, such as negative impacts to data residency or data sovereignty. 

**Note** : Unsupported products may share an API service endpoint with supported products, making them available to all users.**Important** : [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) aren't supported for any Switzerland Data Boundary with Access Justifications products unless otherwise noted. Switzerland Data Boundary with Access Justifications doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. It's your responsibility to ensure that Google Cloud MCP servers endpoints aren't used with any Switzerland Data Boundary with Access Justifications products. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page. 

Supported product | API endpoints | Restrictions or limitations  
---|---|---  
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) |  `iam.googleapis.com`  
`policytroubleshooter.googleapis.com`  
|  None   
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview) |  `cloudresourcemanager.googleapis.com`  
|  None   
  
## Restrictions and limitations

The following sections describe Google Cloud-wide or product-specific restrictions or limitations for features, including any organization policy constraints that are set by default on Switzerland Data Boundary with Access Justifications folders. Other applicable organization policy constraints—even if not set by default—can provide additional defense-in-depth to further protect your organization's Google Cloud resources.

We strongly recommend not changing the values of the required organization policy constraints listed in the following sections. Doing so may undermine data residency. When such a change has been made, the effects of the change are difficult or impossible to reverse. Ensure that you understand the ramifications of changing an organization policy constraint's value before proceeding.   
  
Additionally, ensure that any automated mechanisms your organization uses to manage organization policies are updated to prevent these values from being changed unintentionally.

### Google Cloud-wide

#### Affected Google Cloud-wide features

Feature | Description  
---|---  
Google Cloud console | To access the Google Cloud console when using the Switzerland Data Boundary with Access Justifications control package, you must use one of the following URLs:  


  * [console.ch.cloud.google.com](https://console.ch.cloud.google.com)
  * [console.ch.cloud.google](https://console.ch.cloud.google) for federated identity users

  
  
#### Google Cloud-wide organization policy constraints

The following [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) apply across Google Cloud. 

Organization policy constraint | Description  
---|---  
[`gcp.resourceLocations`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) | Set to the following locations in the `allowedValues` list: 

  * `europe-west6`

This value restricts creation of new resources to the selected values. When set, no resources can be created in any other regions, multi-regions, or locations outside of the selection. See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and cannot be restricted.  
  
Changing this value by making it less restrictive potentially undermines data residency by allowing data to be created or stored outside of a compliant data boundary.   
`gcp.restrictCmekCryptoKeyProjects` | Set to `under:organizations/your-organization-name`, which is your Assured Workloads organization. You can further restrict this value by specifying a project or folder.  
  
Limits the scope of approved folders or projects that can provide [Cloud KMS keys](https://docs.cloud.google.com/kms/docs/algorithms) for encrypting at-rest data using CMEK. This constraint prevents unapproved folders or projects from providing encryption keys, thus helping to guarantee data sovereignty for in-scope services' at-rest data.   
[`gcp.restrictServiceUsage`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) | Set to allow all supported products and API endpoints.  
  
Determines which services can be used by restricting runtime access to their resources. For more information, see [Restricting resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources).   
[`gcp.restrictTLSVersion`](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions) | Set to deny the following TLS versions:  


  * `TLS_1_0`
  * `TLS_1_1`

For more information, see [Restrict TLS versions](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions).   
  
## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder)
  * Understand [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
