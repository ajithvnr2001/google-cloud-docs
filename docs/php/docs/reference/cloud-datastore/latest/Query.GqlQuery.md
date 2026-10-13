---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.GqlQuery
title: Cloud Datastore Client - Class GqlQuery (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:39.787812+00:00
---

# Cloud Datastore Client - Class GqlQuery (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.GqlQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class GqlQuery (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class GqlQuery.

Query Google Cloud Datastore using [GQL](https://cloud.google.com/datastore/docs/apis/gql/gql_reference).

By default, parameters MUST be bound using named or positional bindings. Literals are disabled by default, and must be enabled by setting `$options['allowLiterals']` to `true`. As with any SQL dialect, using parameter binding is highly recommended.

Idiomatic usage is via [Google\Cloud\Datastore\DatastoreClient::gqlQuery()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient#_Google_Cloud_Datastore_DatastoreClient__gqlQuery__).

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient();
    
    $query = $datastore->gqlQuery('SELECT * FROM Companies');
    $res = $datastore->runQuery($query);
    
    foreach ($res as $company) {
        echo $company['companyName'] . PHP_EOL;
    }
    
    
    
    // Literals must be provided as bound parameters by default:
    $query = $datastore->gqlQuery('SELECT * FROM Companies WHERE companyName = @companyName', [
        'bindings' => [
            'companyName' => 'Google'
        ]
    ]);
    
    
    
    // Positional binding is also supported:
    $query = $datastore->gqlQuery('SELECT * FROM Companies WHERE companyName = @1 LIMIT 1', [
        'bindings' => [
            'Google'
        ]
    ]);
    
    
    
    // While not recommended, you can use literals in your query string:
    $query = $datastore->gqlQuery('SELECT * FROM Companies WHERE companyName = \'Google\'', [
        'allowLiterals' => true
    ]);
    
    
    
    // Using cursors as query bindings:
    $cursor = $datastore->cursor($cursorValue);
    
    $query = $datastore->gqlQuery('SELECT * FROM Companies OFFSET @offset', [
        'bindings' => [
            'offset' => $cursor
        ]
    ]);
    

## Namespace

Google \ Cloud \ Datastore \ Query

## Implements

[QueryInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.QueryInterface)

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`entityMapper` |  `[Google\Cloud\Datastore\EntityMapper](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityMapper)`   
An instance of EntityMapper  
`query` |  `string`   
The GQL Query string.  
`options` |  `array`   
Configuration Options  
`↳ allowLiterals` |  `bool`   
Whether literal values will be allowed in the query string. Parameter binding is strongly encouraged over literals. **Defaults to** `false`.  
`↳ bindings` |  `array`   
An array of values to bind to the query string. Queries using Named Bindings should provide a key/value set, while queries using Positional Bindings must provide a simple array. Applications with no need for multitenancy should not set this value.  
  
### queryObject

Format the query for use in the API.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### queryKey

Return the query_type union field name.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### aggregation

### canPaginate

Indicate that this type does not support automatic pagination.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### start

Fulfill the interface, but cursors are handled inside the query string.

**Parameter**  
---  
**Name** | **Description**  
`cursor` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### jsonSerialize

Define the json representation of the object.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
## Constants 

### BINDING_NAMED
    
    
    Value: 'namedBindings'

### BINDING_POSITIONAL
    
    
    Value: 'positionalBindings'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
