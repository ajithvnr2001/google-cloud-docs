---
url: https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.IssueStats
title: Google Cloud Database Center V1beta Client - Class IssueStats (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:51.362790+00:00
---

# Google Cloud Database Center V1beta Client - Class IssueStats (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.IssueStats

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Database Center V1beta Client - Class IssueStats (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Database Center V1beta Client class IssueStats.

IssueStats holds stats for a particular signal category.

Generated from protobuf message `google.cloud.databasecenter.v1beta.IssueStats`

## Namespace

Google \ Cloud \ DatabaseCenter \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ signal_type` |  `int`   
Type of signal which is an issue.  
`↳ resource_count` |  `int`   
Number of resources having issues of a given type.  
`↳ delta_details` |  `[DeltaDetails](https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.DeltaDetails)`   
Optional. Delta counts and details of resources for which issue was raised or fixed.  
`↳ issue_severity` |  `int`   
Severity of the issue.  
  
### getSignalType

Type of signal which is an issue.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [SignalType](https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.SignalType).  
  
### setSignalType

Type of signal which is an issue.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [SignalType](https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.SignalType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResourceCount

Number of resources having issues of a given type.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setResourceCount

Number of resources having issues of a given type.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeltaDetails

Optional. Delta counts and details of resources for which issue was raised or fixed.

**Returns**  
---  
**Type** | **Description**  
`[DeltaDetails](https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.DeltaDetails)|null` |   
  
### hasDeltaDetails

### clearDeltaDetails

### setDeltaDetails

Optional. Delta counts and details of resources for which issue was raised or fixed.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DeltaDetails](https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.DeltaDetails)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIssueSeverity

Severity of the issue.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasIssueSeverity

### clearIssueSeverity

### setIssueSeverity

Severity of the issue.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
