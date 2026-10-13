---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction/
title: Cloud Datastore Client - Class Transaction (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:02.886090+00:00
---

# Cloud Datastore Client - Class Transaction (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class Transaction (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class Transaction.

Represents a Transaction

A transaction is a set of Datastore operations on one or more entities. Each transaction is guaranteed to be atomic, which means that transactions are never partially applied. Either all of the operations in the transaction are applied, or none of them are applied.

It is highly recommended that users read and understand the underlying concepts in [Transactions](https://cloud.google.com/datastore/docs/concepts/transactions) before beginning.

Mutations (i.e. insert, update and delete) are not executed immediately. Calls to those methods (and their batch equivalents) will enqueue a new mutation. Calling [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) will execute all the mutations in the order they were enqueued, and end the transaction.

Lookups and queries can be run in a transaction, so long as they are run prior to committing or rolling back the transaction.

Transactions are an **optional** feature of Google Cloud Datastore. Queries, lookups and mutations can be executed outside of a Transaction from [DatastoreClient](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient).

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient();
    
    $transaction = $datastore->transaction();
    

## Namespace

Google \ Cloud \ Datastore

## Methods 

### insert

Insert an entity.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

If entities with incomplete keys are provided, this method will immediately trigger a service call to allocate IDs to the entities.

Example:
    
    
    $key = $datastore->key('Person', 'Bob');
    $entity = $datastore->entity($key, ['firstName' => 'Bob']);
    
    $transaction->insert($entity);
    $transaction->commit();
    

**Parameter**  
---  
**Name** | **Description**  
`entity` |  `[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)`   
The entity to insert.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### insertBatch

Insert multiple entities.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

If entities with incomplete keys are provided, this method will immediately trigger a service call to allocate IDs to the entities.

Example:
    
    
    $entities = [
        $datastore->entity('Person', ['firstName' => 'Bob']),
        $datastore->entity('Person', ['firstName' => 'John'])
    ];
    
    $transaction->insertBatch($entities);
    $transaction->commit();
    

**Parameter**  
---  
**Name** | **Description**  
`entities` |  `array<[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)>`   
The entities to insert.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### update

Update an entity.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

Example:
    
    
    $entity['firstName'] = 'Bob';
    
    $transaction->update($entity);
    $transaction->commit();
    

**Parameters**  
---  
**Name** | **Description**  
`entity` |  `[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)`   
The entity to update.  
`options` |  `array`   
Configuration Options  
`↳ allowOverwrite` |  `bool`   
Entities must be updated as an entire resource. Patch operations are not supported. Because entities can be created manually, or obtained by a lookup or query, it is possible to accidentally overwrite an existing record with a new one when manually creating an entity. To provide additional safety, this flag must be set to `true` in order to update a record when the entity provided was not obtained through a lookup or query. **Defaults to** `false`.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### updateBatch

Update multiple entities.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

Example:
    
    
    $entities[0]['firstName'] = 'Bob';
    $entities[1]['firstName'] = 'John';
    
    $transaction->updateBatch($entities);
    $transaction->commit();
    

**Parameters**  
---  
**Name** | **Description**  
`entities` |  `array<[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)>`   
The entities to update.  
`options` |  `array`   
Configuration Options  
`↳ allowOverwrite` |  `bool`   
Entities must be updated as an entire resource. Patch operations are not supported. Because entities can be created manually, or obtained by a lookup or query, it is possible to accidentally overwrite an existing record with a new one when manually creating an entity. To provide additional safety, this flag must be set to `true` in order to update a record when the entity provided was not obtained through a lookup or query. **Defaults to** `false`.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### upsert

Upsert an entity.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

Upsert will create a record if one does not already exist, or overwrite existing record if one already exists.

If entities with incomplete keys are provided, this method will immediately trigger a service call to allocate IDs to the entities.

Example:
    
    
    $key = $datastore->key('Person', 'Bob');
    $entity = $datastore->entity($key, ['firstName' => 'Bob']);
    
    $transaction->upsert($entity);
    $transaction->commit();
    

**Parameter**  
---  
**Name** | **Description**  
`entity` |  `[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)`   
The entity to upsert.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### upsertBatch

Upsert multiple entities.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

Upsert will create a record if one does not already exist, or overwrite existing record if one already exists.

If entities with incomplete keys are provided, this method will immediately trigger a service call to allocate IDs to the entities.

Example:
    
    
    $keys = [
        $datastore->key('Person', 'Bob'),
        $datastore->key('Person', 'John')
    ];
    
    $entities = [
        $datastore->entity($keys[0], ['firstName' => 'Bob']),
        $datastore->entity($keys[1], ['firstName' => 'John'])
    ];
    
    $transaction->upsertBatch($entities);
    $transaction->commit();
    

**Parameter**  
---  
**Name** | **Description**  
`entities` |  `array<[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)>`   
The entities to upsert.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### delete

Delete a record.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

Example:
    
    
    $key = $datastore->key('Person', 'Bob');
    
    $transaction->delete($key);
    $transaction->commit();
    

**Parameter**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)`   
The key to delete  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### deleteBatch

Delete multiple records.

Changes are not immediately committed to Cloud Datastore when calling this method. Use [Transaction::commit()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction#_Google_Cloud_Datastore_Transaction__commit__) to commit changes and end the transaction.

Example:
    
    
    $keys = [
        $datastore->key('Person', 'Bob'),
        $datastore->key('Person', 'John')
    ];
    
    $transaction->deleteBatch($keys);
    $transaction->commit();
    

**Parameter**  
---  
**Name** | **Description**  
`keys` |  `array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>`   
The keys to delete.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### commit

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration Options.  
**Returns**  
---  
**Type** | **Description**  
`array` | [Response Body](https://cloud.google.com/datastore/reference/rest/v1/projects/commit#response-body)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
