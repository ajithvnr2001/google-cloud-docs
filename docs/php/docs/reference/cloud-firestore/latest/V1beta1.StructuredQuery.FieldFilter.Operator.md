---
url: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.FieldFilter.Operator
title: Cloud Firestore V1beta1 Client - Class Operator (2.2.0-RC1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:51.576339+00:00
---

# Cloud Firestore V1beta1 Client - Class Operator (2.2.0-RC1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.StructuredQuery.FieldFilter.Operator

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Firestore V1beta1 Client - Class Operator (2.2.0-RC1) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0-RC1  2.1.0  2.0.2-RC1  1.55.0  1.54.4  1.53.1  1.52.0  1.51.0  1.50.0  1.48.1  1.47.3  1.46.0  1.45.2  1.44.1  1.43.3  1.40.0  1.39.0  1.38.0  1.37.7  1.36.1  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.28.0  1.27.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Cloud Firestore V1beta1 Client class Operator.

A field filter operator.

Protobuf type `google.firestore.v1beta1.StructuredQuery.FieldFilter.Operator`

## Namespace

Google \ Cloud \ Firestore \ V1beta1 \ StructuredQuery \ FieldFilter

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

### OPERATOR_UNSPECIFIED
    
    
    Value: 0

Unspecified. This value must not be used.

Generated from protobuf enum `OPERATOR_UNSPECIFIED = 0;`

### LESS_THAN
    
    
    Value: 1

Less than. Requires that the field come first in `order_by`.

Generated from protobuf enum `LESS_THAN = 1;`

### LESS_THAN_OR_EQUAL
    
    
    Value: 2

Less than or equal. Requires that the field come first in `order_by`.

Generated from protobuf enum `LESS_THAN_OR_EQUAL = 2;`

### GREATER_THAN
    
    
    Value: 3

Greater than. Requires that the field come first in `order_by`.

Generated from protobuf enum `GREATER_THAN = 3;`

### GREATER_THAN_OR_EQUAL
    
    
    Value: 4

Greater than or equal. Requires that the field come first in `order_by`.

Generated from protobuf enum `GREATER_THAN_OR_EQUAL = 4;`

### EQUAL
    
    
    Value: 5

Equal.

Generated from protobuf enum `EQUAL = 5;`

### ARRAY_CONTAINS
    
    
    Value: 7

Contains. Requires that the field is an array.

Generated from protobuf enum `ARRAY_CONTAINS = 7;`

### IN
    
    
    Value: 8

In. Requires that `value` is a non-empty ArrayValue with at most 10 values.

Generated from protobuf enum `IN = 8;`

### ARRAY_CONTAINS_ANY
    
    
    Value: 9

Contains any. Requires that the field is an array and `value` is a non-empty ArrayValue with at most 10 values.

Generated from protobuf enum `ARRAY_CONTAINS_ANY = 9;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
