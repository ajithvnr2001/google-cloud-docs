---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery
title: Cloud Datastore Client - Class AggregationQuery (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:39.250590+00:00
---

# Cloud Datastore Client - Class AggregationQuery (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class AggregationQuery (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class AggregationQuery.

Represents an [Aggregation Query](https://cloud.google.com/datastore/docs/aggregation-queries).

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    use Google\Cloud\Datastore\Query\Aggregation;
    
    $datastore = new DatastoreClient();
    
    $query = $datastore->query();
    $query->kind('Companies');
    $query->filter('companyName', '=', 'Google');
    $aggregationQuery = $query->aggregation(Aggregation::count()->alias('total'));
    
    $res = $datastore->runAggregationQuery($aggregationQuery);
    echo $res->get('total');
    

Example (aggregated using over method):
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    use Google\Cloud\Datastore\Query\Aggregation;
    
    $datastore = new DatastoreClient();
    
    $query = $datastore->query();
    $query->kind('Companies');
    $query->filter('companyName', '=', 'Google');
    $query->limit(100);
    $aggregationQuery = $datastore->aggregationQuery();
    $aggregationQuery->over($query)->addAggregation(Aggregation::count()->alias('total_upto_100'));
    
    $res = $datastore->runAggregationQuery($aggregationQuery);
    echo $res->get('total_upto_100');
    

## Namespace

Google \ Cloud \ Datastore \ Query

## Methods 

### __construct

Create an aggregation query.

**Parameters**  
---  
**Name** | **Description**  
`query` |  `[QueryInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.QueryInterface)|null`   
  
`aggregates` |  `array`   
  
  
### addAggregation

Adds a Query Aggregation.

Accepts an array of properties for aggregation.

Example:
    
    
    $query = $datastore->AggregationQuery();
    $query->kind('Companies');
    $query->filter('companyName', '=', 'Google');
    $query->addAggregation(Aggregation::count()->alias('total'));
    echo json_encode($query->queryObject());
    

**Parameter**  
---  
**Name** | **Description**  
`aggregation` |  `[Aggregation](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation)`   
The Aggregation to be included.  
**Returns**  
---  
**Type** | **Description**  
`[AggregationQuery](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery)` |   
  
### over

Set the Query Projection.

Accepts an array of properties. If set, only these properties will be returned.

Example:
    
    
    $query = $datastore->query();
    $query->kind('Companies');
    $query->filter('companyName', '=', 'Google');
    
    $pipeline = $datastore->AggregationQuery()
        ->over($query)
        ->addAggregation(Aggregation::count()->alias('total'));
    

**Parameter**  
---  
**Name** | **Description**  
`query` |  `[QueryInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.QueryInterface)`   
The query whose properties to include.  
**Returns**  
---  
**Type** | **Description**  
`[AggregationQuery](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery)` |   
  
### queryObject

Format the query for use in the API.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
