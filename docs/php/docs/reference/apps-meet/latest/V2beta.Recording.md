---
url: https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Recording
title: Google Apps Meet V2beta Client - Class Recording (0.7.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:41.008938+00:00
---

# Google Apps Meet V2beta Client - Class Recording (0.7.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Recording

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Meet V2beta Client - Class Recording (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.5.4  0.4.1  0.3.0  0.2.6  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Apps Meet V2beta Client class Recording.

Metadata about a recording created during a conference.

Generated from protobuf message `google.apps.meet.v2beta.Recording`

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
`↳ drive_destination` |  `[DriveDestination](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.DriveDestination)`   
Output only. Recording is saved to Google Drive as an MP4 file. The `drive_destination` includes the Drive `fileId` that can be used to download the file using the `files.get` method of the Drive API.  
`↳ name` |  `string`   
Output only. Resource name of the recording. Format: `conferenceRecords/{conference_record}/recordings/{recording}` where `{recording}` is a 1:1 mapping to each unique recording session during the conference.  
`↳ state` |  `int`   
Output only. Current state.  
`↳ start_time` |  `Google\Protobuf\Timestamp`   
Output only. Timestamp when the recording started.  
`↳ end_time` |  `Google\Protobuf\Timestamp`   
Output only. Timestamp when the recording ended.  
  
### getDriveDestination

Output only. Recording is saved to Google Drive as an MP4 file. The `drive_destination` includes the Drive `fileId` that can be used to download the file using the `files.get` method of the Drive API.

**Returns**  
---  
**Type** | **Description**  
`[DriveDestination](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.DriveDestination)|null` |   
  
### hasDriveDestination

### setDriveDestination

Output only. Recording is saved to Google Drive as an MP4 file. The `drive_destination` includes the Drive `fileId` that can be used to download the file using the `files.get` method of the Drive API.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DriveDestination](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.DriveDestination)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Output only. Resource name of the recording.

Format: `conferenceRecords/{conference_record}/recordings/{recording}` where `{recording}` is a 1:1 mapping to each unique recording session during the conference.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Resource name of the recording.

Format: `conferenceRecords/{conference_record}/recordings/{recording}` where `{recording}` is a 1:1 mapping to each unique recording session during the conference.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. Current state.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Recording.State).  
  
### setState

Output only. Current state.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Recording.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartTime

Output only. Timestamp when the recording started.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasStartTime

### clearStartTime

### setStartTime

Output only. Timestamp when the recording started.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndTime

Output only. Timestamp when the recording ended.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEndTime

### clearEndTime

### setEndTime

Output only. Timestamp when the recording ended.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDestination

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
