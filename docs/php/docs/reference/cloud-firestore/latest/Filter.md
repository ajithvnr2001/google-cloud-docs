---
url: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/Filter/
title: Cloud Firestore Client - Class Filter (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:48.137756+00:00
---

# Cloud Firestore Client - Class Filter (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/Filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Firestore Client - Class Filter (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0-RC1  2.1.0  2.0.2-RC1  1.55.0  1.54.4  1.53.1  1.52.0  1.51.0  1.50.0  1.48.1  1.47.3  1.46.0  1.45.2  1.44.1  1.43.3  1.40.0  1.39.0  1.38.0  1.37.7  1.36.1  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.28.0  1.27.3 

Reference documentation and code samples for the Cloud Firestore Client class Filter.

A Query Filter class.

This class helps the user to create filters for complex queries.

Example:
    
    
    use Google\Cloud\Firestore\Filter;
    
    // Filtering with Filter::or and Filter::field
    $result = $query->where(Filter::or([
        Filter::field('firstName', '=', 'John'),
        Filter::field('firstName', '=', 'Monica')
    ]));
    

## Namespace

Google \ Cloud \ Firestore

## Methods 

### static::and

Helper function for `and` filter.

Example:
    
    
    use Google\Cloud\Firestore\Filter;
    
    $result = $query->where(Filter::and([
        Filter::field('firstName', '=', 'John'),
        Filter::field('age', '>', '25')
    ]));
    

**Parameter**  
---  
**Name** | **Description**  
`filters` |  `array`   
A filter array.  
**Returns**  
---  
**Type** | **Description**  
`array` | A composite filter array.  
  
### static::or

Helper function for `or` filter.

Example:
    
    
    use Google\Cloud\Firestore\Filter;
    
    $result = $query->where(Filter::or([
        Filter::field('firstName', '=', 'John'),
        Filter::field('firstName', '=', 'Monica')
    ]));
    

**Parameter**  
---  
**Name** | **Description**  
`filters` |  `array`   
A filter array.  
**Returns**  
---  
**Type** | **Description**  
`array` | A composite Filter array.  
  
### static::field

Helper function for field filter.

Example:
    
    
    use Google\Cloud\Firestore\Filter;
    
    $result = $query->where(Filter::field('firstName', '=', 'John'));
    

**Parameters**  
---  
**Name** | **Description**  
`fieldPath` |  `string|[FieldPath](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/FieldPath)`   
A field to filter by.  
`operator` |  `string|int`   
An operator to filter by.  
`value` |  `mixed`   
A value to compare to.  
**Returns**  
---  
**Type** | **Description**  
`array` | A field Filter array.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
