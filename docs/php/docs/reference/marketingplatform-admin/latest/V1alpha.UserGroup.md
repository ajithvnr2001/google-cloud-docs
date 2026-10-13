---
url: https://docs.cloud.google.com/php/docs/reference/marketingplatform-admin/latest/V1alpha.UserGroup
title: Google Ads Marketing Platform Admin V1alpha Client - Class UserGroup (0.6.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:32.413868+00:00
---

# Google Ads Marketing Platform Admin V1alpha Client - Class UserGroup (0.6.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/marketingplatform-admin/latest/V1alpha.UserGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Ads Marketing Platform Admin V1alpha Client - Class UserGroup (0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.4.2  0.3.1  0.2.1  0.1.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Ads Marketing Platform Admin V1alpha Client class UserGroup.

A resource message representing a user group in a GMP organization.

Generated from protobuf message `google.marketingplatform.admin.v1alpha.UserGroup`

## Namespace

Google \ Ads \ MarketingPlatform \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Resource name of this UserGroup. Format: organizations/{org_id}/userGroups/{user_group_id} Example: "organizations/123abc/userGroups/456def"  
`↳ display_name` |  `string`   
Optional. The human-readable name for the user group.  
`↳ description` |  `string`   
Optional. The description of the user group.  
  
### getName

Identifier. Resource name of this UserGroup.

Format: organizations/{org_id}/userGroups/{user_group_id} Example: "organizations/123abc/userGroups/456def"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Resource name of this UserGroup.

Format: organizations/{org_id}/userGroups/{user_group_id} Example: "organizations/123abc/userGroups/456def"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Optional. The human-readable name for the user group.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Optional. The human-readable name for the user group.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. The description of the user group.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. The description of the user group.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
