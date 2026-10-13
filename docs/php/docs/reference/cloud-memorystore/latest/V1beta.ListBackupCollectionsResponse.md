---
url: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.ListBackupCollectionsResponse
title: Google Cloud Memorystore V1beta Client - Class ListBackupCollectionsResponse (0.13.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:34.506927+00:00
---

# Google Cloud Memorystore V1beta Client - Class ListBackupCollectionsResponse (0.13.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.ListBackupCollectionsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Memorystore V1beta Client - Class ListBackupCollectionsResponse (0.13.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.3 (latest)  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Memorystore V1beta Client class ListBackupCollectionsResponse.

Response for `ListBackupCollections`.

Generated from protobuf message `google.cloud.memorystore.v1beta.ListBackupCollectionsResponse`

## Namespace

Google \ Cloud \ Memorystore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ backup_collections` |  `array<[BackupCollection](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.BackupCollection)>`   
A list of backupCollections in the project. If the `location_id` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder backupCollection entry is included in the response with the `name` field set to a value of the form `projects/{project_id}/locations/{location_id}/backupCollections/`\- and the `status` field set to ERROR and `status_message` field set to "location not available for ListBackupCollections".  
`↳ next_page_token` |  `string`   
Token to retrieve the next page of results, or empty if there are no more results in the list.  
`↳ unreachable` |  `string[]`   
Locations that could not be reached.  
  
### getBackupCollections

A list of backupCollections in the project.

If the `location_id` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder backupCollection entry is included in the response with the `name` field set to a value of the form `projects/{project_id}/locations/{location_id}/backupCollections/`\- and the `status` field set to ERROR and `status_message` field set to "location not available for ListBackupCollections".

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[BackupCollection](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.BackupCollection)>` |   
  
### setBackupCollections

A list of backupCollections in the project.

If the `location_id` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder backupCollection entry is included in the response with the `name` field set to a value of the form `projects/{project_id}/locations/{location_id}/backupCollections/`\- and the `status` field set to ERROR and `status_message` field set to "location not available for ListBackupCollections".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[BackupCollection](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.BackupCollection)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNextPageToken

Token to retrieve the next page of results, or empty if there are no more results in the list.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setNextPageToken

Token to retrieve the next page of results, or empty if there are no more results in the list.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUnreachable

Locations that could not be reached.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setUnreachable

Locations that could not be reached.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
