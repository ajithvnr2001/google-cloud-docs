---
url: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.ErrorGroupOrder
title: Stackdriver Error Reporting V1beta1 Client - Class ErrorGroupOrder (0.27.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:25.351385+00:00
---

# Stackdriver Error Reporting V1beta1 Client - Class ErrorGroupOrder (0.27.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.ErrorGroupOrder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Stackdriver Error Reporting V1beta1 Client - Class ErrorGroupOrder (0.27.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.3 (latest)  0.26.1  0.25.3  0.24.0  0.23.1  0.22.10  0.21.1  0.20.2  0.19.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Stackdriver Error Reporting V1beta1 Client class ErrorGroupOrder.

A sorting order of error groups.

Protobuf type `google.devtools.clouderrorreporting.v1beta1.ErrorGroupOrder`

## Namespace

Google \ Cloud \ ErrorReporting \ V1beta1

## Methods 

### static::name

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
  
  
### static::value

**Parameter**  
---  
**Name** | **Description**  
`name` |  `mixed`   
  
  
## Constants 

### GROUP_ORDER_UNSPECIFIED
    
    
    Value: 0

No group order specified.

Generated from protobuf enum `GROUP_ORDER_UNSPECIFIED = 0;`

### COUNT_DESC
    
    
    Value: 1

Total count of errors in the given time window in descending order.

Generated from protobuf enum `COUNT_DESC = 1;`

### LAST_SEEN_DESC
    
    
    Value: 2

Timestamp when the group was last seen in the given time window in descending order.

Generated from protobuf enum `LAST_SEEN_DESC = 2;`

### CREATED_DESC
    
    
    Value: 3

Timestamp when the group was created in descending order.

Generated from protobuf enum `CREATED_DESC = 3;`

### AFFECTED_USERS_DESC
    
    
    Value: 4

Number of affected users in the given time window in descending order.

Generated from protobuf enum `AFFECTED_USERS_DESC = 4;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
