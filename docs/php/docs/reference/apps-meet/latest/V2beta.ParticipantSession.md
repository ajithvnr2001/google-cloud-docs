---
url: https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.ParticipantSession
title: Google Apps Meet V2beta Client - Class ParticipantSession (0.7.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:17.031054+00:00
---

# Google Apps Meet V2beta Client - Class ParticipantSession (0.7.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.ParticipantSession

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Meet V2beta Client - Class ParticipantSession (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.5.4  0.4.1  0.3.0  0.2.6  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Apps Meet V2beta Client class ParticipantSession.

Refers to each unique join or leave session when a user joins a conference from a device. Note that any time a user joins the conference a new unique ID is assigned. That means if a user joins a space multiple times from the same device, they're assigned different IDs, and are also be treated as different participant sessions.

Generated from protobuf message `google.apps.meet.v2beta.ParticipantSession`

## Namespace

Google \ Apps \ Meet \ V2beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Session id.  
`↳ start_time` |  `Google\Protobuf\Timestamp`   
Output only. Timestamp when the user session starts.  
`↳ end_time` |  `Google\Protobuf\Timestamp`   
Output only. Timestamp when the user session ends. Unset if the user session hasn’t ended.  
  
### getName

Identifier. Session id.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Session id.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartTime

Output only. Timestamp when the user session starts.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasStartTime

### clearStartTime

### setStartTime

Output only. Timestamp when the user session starts.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndTime

Output only. Timestamp when the user session ends. Unset if the user session hasn’t ended.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEndTime

### clearEndTime

### setEndTime

Output only. Timestamp when the user session ends. Unset if the user session hasn’t ended.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
