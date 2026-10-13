---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key/
title: Cloud Datastore Client - Class Key (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:39.336425+00:00
---

# Cloud Datastore Client - Class Key (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class Key (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class Key.

Keys are unique identifiers for entities.

Keys may be considered either "named" or "incomplete". A named Key is one in which each element of the Key path specify a Kind and a Name or ID. An incomplete Key omits the Name or ID from the final path element.

Named Keys are required for any lookup, update, upsert or delete operations. They may also be used for inserting records, so long as you are certain that the identifier is available in Datastore.

Incomplete Keys may be used for inserting records into Datastore. When an incomplete Key is used, Datastore will allocate an ID before inserting.

Incomplete Keys are useful for guaranteeing the availability of an identifier without requiring an additional operation to check whether a given name or ID is available.

Key state can be checked by calling `Key::state()`. The return will be one of `Key::STATE_NAMED` or `Key::STATE_INCOMPLETE`.

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient();
    
    $key = $datastore->key('Person', 'Bob');
    
    
    
    // Keys with complex paths can be constructed with additional method calls.
    
    $key = $datastore->key('Person', 'Bob');
    $key->ancestor('Parents', 'Joe');
    $key->ancestor('Grandparents', 'Barb');
    
    
    
    // Path elements can also be appended, so long as the current last path
    // element contains a kind and identifier.
    
    $key = $datastore->key('Grandparents', 'Barb');
    $key->pathElement('Parents', 'Joe');
    $key->pathElement('Person');
    $key->pathElement('Child', 'Dave'); // Error here.
    

## Namespace

Google \ Cloud \ Datastore

## Implements

\JsonSerializable

## Methods 

### __construct

Create a Key.

**Parameters**  
---  
**Name** | **Description**  
`projectId` |  `string`   
The project ID.  
`options` |  `array`   
Configuration Options  
`↳ namespaceId` |  `string`   
Partitions data under a namespace. Useful for [Multitenant Projects](https://cloud.google.com/datastore/docs/concepts/multitenancy). Applications with no need for multitenancy should not set this value.  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
`↳ path` |  `array`   
The initial Key path.  
  
### pathElement

See also:

  * [PathElement](https://cloud.google.com/datastore/reference/rest/v1/Key#PathElement)



**Parameters**  
---  
**Name** | **Description**  
`kind` |  `string|Google\Protobuf\RepeatedField`   
The kind.  
`identifier` |  `string|int`   
[optional] The name or ID of the object.  
`options` |  `array`   
Configuration Options  
`↳ identifierType` |  `string`   
If omitted, the type will be determined internally. Setting this to either `Key::TYPE_ID` or `Key::TYPE_NAME` will force the pathElement identifier type.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)` |   
  
### ancestor

See also:

  * [PathElement](https://cloud.google.com/datastore/reference/rest/v1/Key#PathElement)



**Parameters**  
---  
**Name** | **Description**  
`kind` |  `string`   
The kind.  
`identifier` |  `string|int`   
The name or ID of the object.  
`options` |  `array`   
Configuration Options  
`↳ identifierType` |  `string`   
If omitted, the type will be determined internally. Setting this to either `Key::TYPE_ID` or `Key::TYPE_NAME` will force the pathElement identifier type.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)` |   
  
### ancestorKey

Use another Key's path as the current Key's ancestor

Given key path will be prepended to any path elements on the current key.

Example:
    
    
    $parent = $datastore->key('Person', 'Dad');
    $key->ancestorKey($parent);
    

**Parameter**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)`   
The ancestor Key.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)` |   
  
### state

Check if the Key is considered Named or Incomplete.

Use `Key::STATE_NAMED` and `Key::STATE_INCOMPLETE` to check value.

Example:
    
    
    // An incomplete key does not have an ID on its last path element.
    $key = $datastore->key('parent', 1234)
        ->pathElement('child');
    
    if ($key->state() === Key::STATE_INCOMPLETE) {
        echo 'Key is incomplete!';
    }
    
    
    
    // A named key has a kind and an identifier on each path element.
    $key = $datastore->key('parent', 1234)
        ->pathElement('child', 4321);
    
    if ($key->state() === Key::STATE_NAMED) {
        echo 'Key is named!';
    }
    

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLastElementIdentifier

Set the value of the last path element in a Key

This method is used internally when IDs are allocated to existing instances of a Key. It should not generally be used externally.

Example:
    
    
    $key = $datastore->key('Person');
    $key->setLastElementIdentifier('Bob', Key::TYPE_NAME);
    

**Parameters**  
---  
**Name** | **Description**  
`value` |  `string`   
The value of the ID or Name.  
`type` |  `string`   
[optional] 'id' or 'name'. **Defaults to** `"id"`.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### path

Get the key path

Example:
    
    
    $path = $key->path();
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### pathEnd

Get the last pathElement in the key

Example:
    
    
    $lastPathElement = $key->pathEnd();
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### pathEndIdentifier

Get the last pathElement identifier.

If the key is incomplete, returns `null`.

Example:
    
    
    $lastPathElementIndentifier = $key->pathEndIdentifier();
    

**Returns**  
---  
**Type** | **Description**  
`string|int|null` |   
  
### pathEndIdentifierType

Get the last pathElement identifier type.

If the key is incomplete, returns `null`.

Example:
    
    
    $lastPathElementIdentifierType = $key->pathEndIdentifierType();
    

**Returns**  
---  
**Type** | **Description**  
`string|null` |   
  
### keyObject

Get the key object formatted for the datastore service.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### jsonSerialize

### __toString

Represent the path as a string.

## Constants 

### TYPE_NAME
    
    
    Value: 'name'

### TYPE_ID
    
    
    Value: 'id'

### STATE_NAMED
    
    
    Value: 'named'

### STATE_INCOMPLETE
    
    
    Value: 'incomplete'

### STATE_COMPLETE
    
    
    Value: self::STATE_NAMED

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
