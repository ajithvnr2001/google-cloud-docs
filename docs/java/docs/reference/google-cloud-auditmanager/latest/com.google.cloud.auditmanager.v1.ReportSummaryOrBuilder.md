---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.ReportSummaryOrBuilder
title: Interface ReportSummaryOrBuilder (0.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:53.581010+00:00
---

# Interface ReportSummaryOrBuilder (0.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.ReportSummaryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReportSummaryOrBuilder (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.13.0  0.12.0  0.11.0  0.9.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public interface ReportSummaryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCompliantCount()
    
    
    public abstract int getCompliantCount()

Number of compliant checks.

`int32 compliant_count = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The compliantCount.  
  
### getErrorCount()
    
    
    public abstract int getErrorCount()

Number of checks that can't be performed due to errors.

`int32 error_count = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The errorCount.  
  
### getManualReviewNeededCount()
    
    
    public abstract int getManualReviewNeededCount()

Number of checks that require a manual review.

`int32 manual_review_needed_count = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The manualReviewNeededCount.  
  
### getTotalCount()
    
    
    public abstract int getTotalCount()

Total number of evaluated checks.

`int32 total_count = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalCount.  
  
### getViolationCount()
    
    
    public abstract int getViolationCount()

Number of checks with violations.

`int32 violation_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The violationCount.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
