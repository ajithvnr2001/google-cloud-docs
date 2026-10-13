---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricDescriptor.ValueType
title: Google API Common Protos Client - Class ValueType (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:33.177798+00:00
---

# Google API Common Protos Client - Class ValueType (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricDescriptor.ValueType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class ValueType (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class ValueType.

The value type of a metric.

Protobuf type `google.api.MetricDescriptor.ValueType`

## Namespace

Google \ Api \ MetricDescriptor

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

### VALUE_TYPE_UNSPECIFIED
    
    
    Value: 0

Do not use this default value.

Generated from protobuf enum `VALUE_TYPE_UNSPECIFIED = 0;`

### BOOL
    
    
    Value: 1

The value is a boolean.

This value type can be used only if the metric kind is `GAUGE`.

Generated from protobuf enum `BOOL = 1;`

### INT64
    
    
    Value: 2

The value is a signed 64-bit integer.

Generated from protobuf enum `INT64 = 2;`

### DOUBLE
    
    
    Value: 3

The value is a double precision floating point number.

Generated from protobuf enum `DOUBLE = 3;`

### STRING
    
    
    Value: 4

The value is a text string.

This value type can be used only if the metric kind is `GAUGE`.

Generated from protobuf enum `STRING = 4;`

### DISTRIBUTION
    
    
    Value: 5

The value is a [`Distribution`](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Distribution).

Generated from protobuf enum `DISTRIBUTION = 5;`

### MONEY
    
    
    Value: 6

The value is money.

Generated from protobuf enum `MONEY = 6;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
