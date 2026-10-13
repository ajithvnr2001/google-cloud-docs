---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query
title: Cloud Datastore Client - Class Query (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:39.930285+00:00
---

# Cloud Datastore Client - Class Query (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class Query (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class Query.

Represents a Cloud [Datastore Query](https://cloud.google.com/datastore/docs/concepts/queries)

Queries can be created either by using the builder pattern, or by providing a [Query](https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#query) when creating this object.

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient();
    
    $query = $datastore->query();
    $query->kind('Companies');
    $query->filter('companyName', '=', 'Google');
    
    $res = $datastore->runQuery($query);
    foreach ($res as $company) {
        echo $company['companyName']; // Google
    }
    
    
    
    // Queries can also be constructed using a
    // [Query Object](https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#query):
    $query = $datastore->query([
        'query' => [
            'kind' => [
                [
                    'name' => 'Companies'
                ]
            ],
            'filter' => [
                'propertyFilter' => [
                    'op' => 'EQUAL',
                    'property' => [
                        'name' => 'companyName'
                    ],
                    'value' => [
                        'stringValue' => 'Google'
                    ]
                ]
            ]
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
`query` |  `array`   
optional(<https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#query>)  
  
### projection

Set the Query Projection.

Accepts an array of properties. If set, only these properties will be returned.

Example:
    
    
    $query->projection(['firstName', 'lastName']);
    

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `array|string`   
The property or properties to include in the result.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### keysOnly

Set the query to return only keys (no properties).

Example:
    
    
    $query->keysOnly();
    

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### kind

Set the Kind to query.

If empty, returns entities of all kinds. Must be set in order to filter results. While you may supply as many kinds as you wish, datastore currently only accepts one at a time.

Example:
    
    
    $query->kind('Person');
    

**Parameter**  
---  
**Name** | **Description**  
`kinds` |  `array|string`   
The kind or kinds to return. Only a single kind is currently supported.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### filter

See also:

  * [Allowed Operators](https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#operator_1)



**Parameters**  
---  
**Name** | **Description**  
`filterOrProperty` |  `string|array`   
Either a string property name or an array representation of Property/Composite filter returned by Filter::and(), Filter::or() and Filter::where().  
`operator` |  `string|null`   
[optional] The operator to use in the filter if property name is used in the first argument. A list of allowed operators may be found [here](https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#operator_1). Short comparison operators are provided for convenience and are mapped to their datastore-compatible equivalents. Available short operators are `=`, `!=`, `<`, `<=`, `>`, `>=`, `IN` and `NOT IN`.  
`value` |  `mixed`   
[optional] The value to check if property name is used in the first argument.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### hasAncestor

Query for entities by their ancestors.

Keys can be provided either via a [Google\Cloud\Datastore\Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key) object, or by providing a kind, identifier and (optionally) an identifier type.

Example:
    
    
    $key = $datastore->key('Person', 'Bob');
    $query->hasAncestor($key);
    
    
    
    // Specifying an identifier type
    $key = $datastore->key('Robots', '1337', [
        'identifierType' => Key::TYPE_NAME
    ]);
    $query->hasAncestor($key);
    

**Parameter**  
---  
**Name** | **Description**  
`key` |  `[Google\Cloud\Datastore\Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)`   
The ancestor Key instance.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### order

See also:

  * [Allowed Directions](https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#Direction)



**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
The property to order by.  
`direction` |  `int`   
[optional] The direction to order in. Google Cloud PHP provides class constants which map to allowed Datastore values. Those constants are `Query::ORDER_DESCENDING` and `Query::ORDER_ASCENDING`. **Defaults to** `Query::ORDER_ACENDING`.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### distinctOn

The properties to make distinct.

The query results will contain the first result for each distinct combination of values for the given properties (if empty, all results are returned).

Example:
    
    
    $query->distinctOn('lastName');
    

**Parameter**  
---  
**Name** | **Description**  
`property` |  `array|string`   
The property or properties to make distinct.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### start

See also:

  * [Cursors, Limits and Offsets](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets)



**Parameter**  
---  
**Name** | **Description**  
`cursor` |  `string`   
The cursor on which to start the result.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### end

See also:

  * [Cursors, Limits and Offsets](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets)



**Parameter**  
---  
**Name** | **Description**  
`cursor` |  `string`   
The cursor on which to end the result.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### offset

See also:

  * [Cursors, Limits and Offsets](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets)



**Parameter**  
---  
**Name** | **Description**  
`num` |  `int`   
The number of results to skip.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### limit

See also:

  * [Cursors, Limits and Offsets](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets)



**Parameter**  
---  
**Name** | **Description**  
`num` |  `int`   
The number of results to return.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### canPaginate

Indicate that this type does support automatic pagination.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### queryObject

Return a service-compliant array.

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

**Parameter**  
---  
**Name** | **Description**  
`aggregation` |  `[Aggregation](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Aggregation)`   
  
  
### jsonSerialize

## Constants 

### OP_DEFAULT
    
    
    Value: self::OP_EQUALS

### OP_LESS_THAN
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::LESS_THAN

### OP_LESS_THAN_OR_EQUAL
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::LESS_THAN_OR_EQUAL

### OP_GREATER_THAN
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::GREATER_THAN

### OP_GREATER_THAN_OR_EQUAL
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::GREATER_THAN_OR_EQUAL

### OP_EQUALS
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::EQUAL

### OP_NOT_EQUALS
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::NOT_EQUAL

### OP_IN
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::IN

### OP_NOT_IN
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::NOT_IN

### OP_HAS_ANCESTOR
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyFilter\Operator::HAS_ANCESTOR

### ORDER_DEFAULT
    
    
    Value: self::ORDER_ASCENDING

### ORDER_DESCENDING
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyOrder\Direction::DESCENDING

### ORDER_ASCENDING
    
    
    Value: \Google\Cloud\Datastore\V1\PropertyOrder\Direction::ASCENDING

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
