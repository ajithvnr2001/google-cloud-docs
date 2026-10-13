---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityIterator/
title: Cloud Datastore Client - Class EntityIterator (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:23.762197+00:00
---

# Cloud Datastore Client - Class EntityIterator (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityIterator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class EntityIterator (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class EntityIterator.

Iterates over a set of [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity) items.

## Namespace

Google \ Cloud \ Datastore

## Implements

\Iterator

## Methods 

### moreResultsType

See also:

  * [MoreResultsType Documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/runQuery#MoreResultsType)



**Returns**  
---  
**Type** | **Description**  
`string|null` |   
  
### getExplainMetrics

Returns a ExplainMetrics object from the query.

By default, the query does not get executed and the explain metrics object contains only the planning statistics [V1\ExplainMetrics](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/V1.ExplainMetrics).

If the request was configured with the ExplainOptions object `Analyze` attribute to true the request then also gets executed, including the ExecutionStats on the ExplainMetrics object

Contrary to looping through the result of run query, this method caches the first metrics to avoid variations when analyzing said metrics.

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    use Google\Cloud\Datastore\V1\ExplainOptions;
    
    $datastore = new DatastoreClient();
    
    explainOptions = (new ExplainOptions())->setAnalyze(false);
    $queryOptions = [
        'explainOptions' => $explainOptions
    ];
    
    // The query does not get executed
    $res = $datastore->runQuery($query, $queryOptions);
    
    $explainMetrics = $res->getExplainMetrics();
    
    // This is populated
    $explainMetrics->planningSummary
    
    // This is not populated
    $explainMetrics->executionStats
    

Example:
    
    
    explainOptions = (new ExplainOptions())->setAnalyze(true);
    $queryOptions = [
        'explainOptions' => $explainOptions
    ];
    
    // The query does not get executed
    $res = $datastore->runQuery($query, $queryOptions);
    
    $explainMetrics = $res->getExplainMetrics();
    
    // This is populated
    $explainMetrics->getPlanSummary()
    
    // This is also populated
    $explainMetrics->getExecutionStats()
    

**Returns**  
---  
**Type** | **Description**  
`null|[V1\ExplainMetrics](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/V1.ExplainMetrics)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
