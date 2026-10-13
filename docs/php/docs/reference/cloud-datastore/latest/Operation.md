---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Operation/
title: Cloud Datastore Client - Class Operation (1.34.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:35.132554+00:00
---

# Cloud Datastore Client - Class Operation (1.34.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class Operation (1.34.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class Operation.

Run lookups and queries and commit changes.

This class is used by [DatastoreClient](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient) and [Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction) and is not intended to be used directly.

Examples are omitted for brevity. Detailed usage examples can be found in [DatastoreClient](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient) and [Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction).

## Namespace

Google \ Cloud \ Datastore

## Methods 

### __construct

Create an operation

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `Connection\ConnectionInterface`   
A connection to Google Cloud Platform's Datastore API. This object is created by DatastoreClient, and should not be instantiated outside of this client.  
`projectId` |  `string`   
The Google Cloud Platform project ID.  
`namespaceId` |  `string`   
The namespace to use for all service requests.  
`entityMapper` |  `[EntityMapper](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityMapper)`   
A Datastore Entity Mapper instance.  
`databaseId` |  `string`   
ID of the database to which the entities belong.  
  
### key

See also:

  * [Key](https://cloud.google.com/datastore/reference/rest/v1/Key)
  * [PathElement](https://cloud.google.com/datastore/reference/rest/v1/Key#PathElement)



**Parameters**  
---  
**Name** | **Description**  
`kind` |  `string`   
The kind.  
`identifier` |  `string|int`   
[optional] The ID or name.  
`options` |  `array`   
Configuration Options  
`↳ identifierType` |  `string`   
If omitted, type will be determined internally. In cases where any ambiguity can be expected (i.e. if you want to create keys with `name` but your values may pass PHP's `is_numeric()` check), this value may be explicitly set using `Key::TYPE_ID` or `Key::TYPE_NAME`.  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)` |   
  
### keys

See also:

  * [Key](https://cloud.google.com/datastore/reference/rest/v1/Key)
  * [PathElement](https://cloud.google.com/datastore/reference/rest/v1/Key#PathElement)



**Parameters**  
---  
**Name** | **Description**  
`kind` |  `string`   
The kind to use in the final path element.  
`options` |  `array`   
Configuration Options  
`↳ ancestors` |  `array[]`   
An array of [PathElement](https://cloud.google.com/datastore/reference/rest/v1/Key#PathElement) arrays. Use to create [ancestor paths](https://cloud.google.com/datastore/docs/concepts/entities#ancestor_paths).  
`↳ number` |  `int`   
The number of keys to generate.  
`↳ id` |  `string|int`   
The ID for the last pathElement.  
`↳ name` |  `string`   
The Name for the last pathElement.  
**Returns**  
---  
**Type** | **Description**  
`array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>` |   
  
### entity

See also:

  * [Entity](https://cloud.google.com/datastore/reference/rest/v1/Entity)



**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)|string|null`   
[optional] The key used to identify the record, or a string $kind. The key may be null only if the entity will be used as an embedded entity within another entity. Attempting to use keyless entities as root entities will result in error.  
`entity` |  `array`   
[optional] The data to fill the entity with.  
`options` |  `array`   
Configuration Options  
`↳ className` |  `string`   
If set, the given class will be returned. Value must be the name of a class implementing EntityInterface. **Defaults to** [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
`↳ excludeFromIndexes` |  `array`   
A list of entity keys to exclude from datastore indexes.  
**Returns**  
---  
**Type** | **Description**  
`EntityInterface` |   
  
### beginTransaction

Begin a Datastore Transaction.

**Parameters**  
---  
**Name** | **Description**  
`transactionOptions` |  `array`   
[Transaction Options](https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/beginTransaction#TransactionOptions)  
`options` |  `array`   
Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### allocateIds

See also:

  * [allocateIds](https://cloud.google.com/datastore/reference/rest/v1/projects/allocateIds)



**Parameters**  
---  
**Name** | **Description**  
`keys` |  `array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>`   
The incomplete keys.  
`options` |  `array`   
[optional] Configuration Options.  
**Returns**  
---  
**Type** | **Description**  
`array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>` |   
  
### lookup

Lookup records by key

**Parameters**  
---  
**Name** | **Description**  
`keys` |  `array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>`   
The identifiers to look up.  
`options` |  `array`   
Configuration Options  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
`↳ transaction` |  `string`   
The transaction ID, if the query should be run in a transaction.  
`↳ className` |  `string|array`   
If a string, the given class will be returned. Value must be the name of a class implementing EntityInterface. If an array is given, it must be an associative array, where the key is a Kind and the value must implement EntityInterface. **Defaults to** [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
`↳ sort` |  `bool`   
If set to true, results in each set will be sorted to match the order given in $keys. **Defaults to** `false`.  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
`↳ readTime` |  `Timestamp`   
Reads entities as they were at the given timestamp.  
**Returns**  
---  
**Type** | **Description**  
`array` | Returns an array with keys [`found`, `missing`, and `deferred`]. Members of `found` will be instance of {@see \Google\Cloud\Datastore\Entity}. Members of `missing` and `deferred` will be instance of {@see \Google\Cloud\Datastore\Key}.  
  
### runQuery

Run a query and return entities

**Parameters**  
---  
**Name** | **Description**  
`query` |  `Query\QueryInterface`   
The query object.  
`options` |  `array`   
Configuration Options  
`↳ transaction` |  `string`   
The transaction ID, if the query should be run in a transaction.  
`↳ className` |  `string`   
If set, the given class will be returned. Value must be the name of a class implementing EntityInterface. **Defaults to** [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
`↳ readTime` |  `Timestamp`   
Reads entities as they were at the given timestamp.  
`↳ explainMetrics` |  `ExplainMetrics`   
The ExplainMetrics object for query stats. V1\ExplainOptions} </xref  
**Returns**  
---  
**Type** | **Description**  
`[EntityIterator](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityIterator)<EntityInterface>` |   
  
### runAggregationQuery

Run an aggregation query and return aggregated results.

**Parameters**  
---  
**Name** | **Description**  
`runQueryObj` |  `[Query\AggregationQuery](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery)`   
  
`options` |  `array`   
Configuration Options  
`↳ transaction` |  `string`   
The transaction ID, if the query should be run in a transaction.  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
`↳ readTime` |  `Timestamp`   
Reads entities as they were at the given timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[Query\AggregationQueryResult](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQueryResult)` |   
  
### commit

Commit all mutations

Calling this method will end the operation (and close the transaction, if one is specified).

**Parameters**  
---  
**Name** | **Description**  
`mutations` |  `array`   
[Mutation[]](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit#Mutation).  
`options` |  `array`   
Configuration Options  
`↳ transaction` |  `string`   
The transaction ID, if the query should be run in a transaction.  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
**Returns**  
---  
**Type** | **Description**  
`array` | [Response Body](https://cloud.google.com/datastore/reference/rest/v1/projects/commit#response-body)  
  
### allocateIdsToEntities

Patch any incomplete keys in the given array of entities

Any incomplete keys will be allocated an ID. Named keys in the input will remain unchanged.

**Parameter**  
---  
**Name** | **Description**  
`entities` |  `array<EntityInterface>`   
A list of entities  
**Returns**  
---  
**Type** | **Description**  
`array<EntityInterface>` |   
  
### mutation

See also:

  * [Limits](https://cloud.google.com/datastore/docs/concepts/limits)



**Parameters**  
---  
**Name** | **Description**  
`operation` |  `string`   
The operation to execute. "Insert", "Upsert", "Update" or "Delete".  
`input` |  `EntityInterface|[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)`   
The entity or key to mutate.  
`type` |  `string`   
The type of the input array.  
`baseVersion` |  `string`   
[optional] The version of the entity that this mutation is being applied to. If this does not match the current version on the server, the mutation conflicts.  
**Returns**  
---  
**Type** | **Description**  
`array` | [Mutation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit#Mutation).  
  
### rollback

Roll back a transaction

**Parameter**  
---  
**Name** | **Description**  
`transactionId` |  `string`   
The transaction to roll back  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkOverwrite

Check whether an update or upsert operation may proceed safely

**Parameters**  
---  
**Name** | **Description**  
`entities` |  `array<EntityInterface>`   
the entities to be updated or upserted.  
`allowOverwrite` |  `bool`   
If `true`, entities may be overwritten. _Defaults to_ * `false`.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
