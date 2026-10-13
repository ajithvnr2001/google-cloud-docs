---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Numeric/
title: BigQuery Client - Class Numeric (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:48.353341+00:00
---

# BigQuery Client - Class Numeric (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Numeric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class Numeric (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class Numeric.

Represents a value with a data type of [Numeric](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_type).

It supports a fixed 38 decimal digits of precision and 9 decimal digits of scale, and values are in the range of -99999999999999999999999999999.999999999 to 99999999999999999999999999999.999999999.

Example:
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    $bigQuery = new BigQueryClient();
    
    $numeric = $bigQuery->numeric('99999999999999999999999999999999999999.999999999');
    

## Namespace

Google \ Cloud \ BigQuery

## Implements

[ValueInterface](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueInterface)

## Methods 

### __construct

**Parameter**  
---  
**Name** | **Description**  
`value` |  `string|int|float`   
The NUMERIC value.  
  
### get

Get the underlying value.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### type

Get the type.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### formatAsString

Format the value as a string.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### __toString

Format the value as a string.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
