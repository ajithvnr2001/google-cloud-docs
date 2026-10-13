---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation
title: Cloud Datastore Client - Class Aggregation (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:39.446115+00:00
---

# Cloud Datastore Client - Class Aggregation (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class Aggregation (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class Aggregation.

Represents Aggregation properties.

Example:
    
    
    $count = Aggregation::count();
    $count->alias('count');
    $count->limit(100);
    
    echo json_encode($count->getProps());
    

Aggregations considers non existing property name as an empty query set

## Namespace

Google \ Cloud \ Datastore \ Query

## Methods 

### alias

Set the aggregation alias.

Example:
    
    
    $count = Aggregation->count();
    $count->alias('total');
    
    echo $count->props()['count']['alias'];
    

**Parameter**  
---  
**Name** | **Description**  
`alias` |  `string`   
The alias for aggregation.  
**Returns**  
---  
**Type** | **Description**  
`[Aggregation](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation)` |   
  
### getProps

Get the array representation for the aggregation.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### static::count

Creates count aggregation properties.

Example:
    
    
    $count = Aggregation::count();
    

**Returns**  
---  
**Type** | **Description**  
`[Aggregation](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation)` |   
  
### static::sum

Creates sum aggregation properties.

Example:
    
    
    $sum = Aggregate::sum('property_to_aggregate_upon');
    

Result of SUM aggregation can be a integer or a float. Sum of integers which exceed maxinum integer value returns a float. Sum of numbers exceeding max float value returns `INF`. Sum of data which contains `NaN` returns `NaN`. Non numeric values are ignored.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
The relative path of the field to aggregate upon.  
**Returns**  
---  
**Type** | **Description**  
`[Aggregation](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation)` |   
  
### static::avg

Creates average aggregation properties.

Example:
    
    
    $avg = Aggregate::avg('property_to_aggregate_upon');
    

Result of AVG aggregation can be a float or a null. Average of empty valid data set return `null`. Average of numbers exceeding max float value returns `INF`. Average of data which contains `NaN` returns `NaN`. Non numeric values are ignored.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
The relative path of the field to aggregate upon.  
**Returns**  
---  
**Type** | **Description**  
`[Aggregation](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
