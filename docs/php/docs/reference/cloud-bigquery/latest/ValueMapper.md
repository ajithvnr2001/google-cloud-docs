---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueMapper/
title: BigQuery Client - Class ValueMapper (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:49.187608+00:00
---

# BigQuery Client - Class ValueMapper (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueMapper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class ValueMapper (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class ValueMapper.

Maps values to their expected BigQuery types. This class is intended for internal use only.

## Namespace

Google \ Cloud \ BigQuery

## Methods 

### __construct

**Parameter**  
---  
**Name** | **Description**  
`returnInt64AsObject` |  `bool`   
If true, 64 bit integers will be returned as a [Google\Cloud\Core\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Int64.html) object for 32 bit platform compatibility.  
  
### fromBigQuery

Maps a value coming from BigQuery to the expected format for use in the library.

**Parameters**  
---  
**Name** | **Description**  
`value` |  `array`   
The value to map.  
`schema` |  `array`   
The schema describing the value.  
  
### toBigQuery

Maps a user provided value to the expected BigQuery format.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
The value to map.  
**Returns**  
---  
**Type** | **Description**  
`mixed` |   
  
### toParameter

Maps a value to the expected parameter format.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
The value to map.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
## Constants 

### TYPE_BOOL
    
    
    Value: 'BOOL'

### TYPE_BOOLEAN
    
    
    Value: 'BOOLEAN'

### TYPE_INT64
    
    
    Value: 'INT64'

### TYPE_INTEGER
    
    
    Value: 'INTEGER'

### TYPE_FLOAT64
    
    
    Value: 'FLOAT64'

### TYPE_FLOAT
    
    
    Value: 'FLOAT'

### TYPE_NUMERIC
    
    
    Value: 'NUMERIC'

### TYPE_BIGNUMERIC
    
    
    Value: 'BIGNUMERIC'

### TYPE_STRING
    
    
    Value: 'STRING'

### TYPE_BYTES
    
    
    Value: 'BYTES'

### TYPE_DATE
    
    
    Value: 'DATE'

### TYPE_DATETIME
    
    
    Value: 'DATETIME'

### TYPE_TIME
    
    
    Value: 'TIME'

### TYPE_TIMESTAMP
    
    
    Value: 'TIMESTAMP'

### TYPE_ARRAY
    
    
    Value: 'ARRAY'

### TYPE_STRUCT
    
    
    Value: 'STRUCT'

### TYPE_RECORD
    
    
    Value: 'RECORD'

### TYPE_GEOGRAPHY
    
    
    Value: 'GEOGRAPHY'

### TYPE_JSON
    
    
    Value: 'JSON'

### DATETIME_FORMAT
    
    
    Value: 'Y-m-d H:i:s.u'

### DATETIME_FORMAT_INSERT
    
    
    Value: 'Y-m-d\TH:i:s.u'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
