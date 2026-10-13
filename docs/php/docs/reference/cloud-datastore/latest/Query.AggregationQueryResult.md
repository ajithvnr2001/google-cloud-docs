---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQueryResult
title: Cloud Datastore Client - Class AggregationQueryResult (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:39.718877+00:00
---

# Cloud Datastore Client - Class AggregationQueryResult (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQueryResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class AggregationQueryResult (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class AggregationQueryResult.

Represents the result of an [Aggregation Query](https://cloud.google.com/datastore/docs/aggregation-queries)

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient();
    
    $query = $datastore->AggregationQuery();
    $query->kind('Companies');
    $query->filter('companyName', '=', 'Google');
    $query->limit(100);
    $query->addAggregation(Aggregation::count()->alias('total_upto_100'));
    
    $res = $datastore->runAggregationQuery($query);
    echo $res->get('total_upto_100');
    

## Namespace

Google \ Cloud \ Datastore \ Query

## Methods 

### __construct

Create AggregationQueryResult object.

**Parameters**  
---  
**Name** | **Description**  
`result` |  `array`   
Response of [RunAggregationQuery](https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/runAggregationQuery)  
`mapper` |  `[Google\Cloud\Datastore\EntityMapper](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityMapper)`   
[Optional] Entity mapper to map datastore values to their equivalent php values incase of `null`, `NAN`, `INF` and `-INF`  
  
### get

Get the Query Aggregation value.

Example:
    
    
    $query = $datastore->AggregationQuery();
    $query->kind('Companies');
    $query->filter('companyName', '=', 'Google');
    $query->addAggregation(Aggregation::count()->alias('total'));
    $res = $client->runAggregationQuery($query);
    echo $res->get('total');
    

**Parameter**  
---  
**Name** | **Description**  
`alias` |  `string`   
The aggregation alias.  
**Returns**  
---  
**Type** | **Description**  
`mixed` |   
  
### getQuery

Gets the value of query for example in case of a GqlQuery.

**Returns**  
---  
**Type** | **Description**  
`[AggregationQuery](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery)|null` |   
  
### getTransaction

Gets the transaction id when Aggregation is associated with a Transaction.

**Returns**  
---  
**Type** | **Description**  
`string|null` |   
  
### getReadTime

Gets the timestamp when Aggregation was executed.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Timestamp](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Timestamp.html)` |   
  
### getExplainMetrics

Gets the ExplainMetrics object if the explainOptions parameter was set for the query

**Returns**  
---  
**Type** | **Description**  
`null|[Google\Cloud\Datastore\V1\ExplainMetrics](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/V1.ExplainMetrics)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
