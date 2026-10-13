---
url: https://docs.cloud.google.com/php/docs/reference/gax/latest/ApiStatus/
title: Google API Core Client - Class ApiStatus (1.51.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:36.400407+00:00
---

# Google API Core Client - Class ApiStatus (1.51.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/gax/latest/ApiStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Core Client - Class ApiStatus (1.51.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.51.0 (latest)  1.46.0  1.43.0  1.42.5  1.40.0  1.38.2  1.36.1  1.35.1 

## Namespace

Google \ ApiCore

## Methods 

### static::isValidStatus

**Parameter**  
---  
**Name** | **Description**  
`status` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### static::statusFromRpcCode

**Parameter**  
---  
**Name** | **Description**  
`code` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### static::rpcCodeFromStatus

**Parameter**  
---  
**Name** | **Description**  
`status` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### static::rpcCodeFromHttpStatusCode

Maps HTTP status codes to Google\Rpc\Code codes.

Some codes are left out because they map to multiple gRPC codes (e.g. 500).

**Parameter**  
---  
**Name** | **Description**  
`httpStatusCode` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`int` |   
  
## Constants 

### OK
    
    
    Value: 'OK'

### CANCELLED
    
    
    Value: 'CANCELLED'

### UNKNOWN
    
    
    Value: 'UNKNOWN'

### INVALID_ARGUMENT
    
    
    Value: 'INVALID_ARGUMENT'

### DEADLINE_EXCEEDED
    
    
    Value: 'DEADLINE_EXCEEDED'

### NOT_FOUND
    
    
    Value: 'NOT_FOUND'

### ALREADY_EXISTS
    
    
    Value: 'ALREADY_EXISTS'

### PERMISSION_DENIED
    
    
    Value: 'PERMISSION_DENIED'

### RESOURCE_EXHAUSTED
    
    
    Value: 'RESOURCE_EXHAUSTED'

### FAILED_PRECONDITION
    
    
    Value: 'FAILED_PRECONDITION'

### ABORTED
    
    
    Value: 'ABORTED'

### OUT_OF_RANGE
    
    
    Value: 'OUT_OF_RANGE'

### UNIMPLEMENTED
    
    
    Value: 'UNIMPLEMENTED'

### INTERNAL
    
    
    Value: 'INTERNAL'

### UNAVAILABLE
    
    
    Value: 'UNAVAILABLE'

### DATA_LOSS
    
    
    Value: 'DATA_LOSS'

### UNAUTHENTICATED
    
    
    Value: 'UNAUTHENTICATED'

### UNRECOGNIZED_STATUS
    
    
    Value: 'UNRECOGNIZED_STATUS'

### UNRECOGNIZED_CODE
    
    
    Value: -1

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
