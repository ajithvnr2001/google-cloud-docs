---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity/
title: Cloud Datastore Client - Class Entity (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:38.768305+00:00
---

# Cloud Datastore Client - Class Entity (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class Entity (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class Entity.

A Datastore Entity

Entity implements PHP's [ArrayAccess](http://php.net/arrayaccess), allowing access via the array syntax (example below).

Properties are mapped automatically to their corresponding Datastore value types. Refer to the table below for a guide to how types are stored.

**PHP Type** | **Datastore Value Type**  
---|---  
`\DateTimeInterface` | `timestampValue`  
[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key) | `keyValue`  
[GeoPoint](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/GeoPoint) | `geoPointValue`  
[Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity) | `entityValue`  
[Blob](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Blob) | `blobValue`  
[Google\Cloud\Core\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Int64.html) | `integerValue`  
Associative Array | `entityValue` (No Key)  
Non-Associative Array | `arrayValue`  
`float` | `doubleValue`  
`int` | `integerValue`  
`string` | `stringValue`  
`resource` | `blobValue`  
`NULL` | `nullValue`  
`bool` | `booleanValue`  
`object` (Outside types specified above) | **ERROR** `InvalidArgumentException`  
  
Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient();
    
    $key = $datastore->key('Person', 'Bob');
    $entity = $datastore->entity($key, [
        'firstName' => 'Bob',
        'lastName' => 'Testguy'
    ]);
    
    $firstName = $entity['firstName']; // 'Bob'
    $entity['location'] = 'Detroit, MI';
    
    
    
    // Custom entity types can be created by implementing the datastore entity interface.
    // You can also define mappings to correctly fetch embedded entities.
    use Google\Cloud\Datastore\EntityTrait;
    use Google\Cloud\Datastore\EntityInterface;
    
    class Business implements EntityInterface
    {
        use EntityTrait;
    
        public static function mappings(): array
        {
            return [
                'parent' => Business::class
            ];
        }
    }
    
    $alphabet = new Business;
    $alphabet->set([
        'companyName' => 'Alphabet'
    ]);
    
    $key = $datastore->key('Business', 'Google');
    $google = $datastore->entity($key, [
        'companyName' => 'Google',
        'parent' => $alphabet
    ], [
        'className' => Business::class
    ]);
    
    $datastore->insert($google);
    
    $google = $datastore->lookup($key, ['className' => Business::class]);
    echo get_class($google); // `Business`
    echo get_class($google->get()['parent']); // `Business`
    

## Namespace

Google \ Cloud \ Datastore

## Implements

\ArrayAccess

[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)

## Methods 

### offsetSet

**Parameters**  
---  
**Name** | **Description**  
`key` |  `string`   
The value name.  
`val` |  `mixed`   
The value.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### offsetExists

**Parameter**  
---  
**Name** | **Description**  
`key` |  `string`   
the value to check.  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### offsetUnset

**Parameter**  
---  
**Name** | **Description**  
`key` |  `string`   
the value to remove.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### offsetGet

**Parameter**  
---  
**Name** | **Description**  
`key` |  `string`   
the value to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`mixed` |   
  
### __get

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`mixed` |   
  
### __set

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`value` |  `mixed`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### __unset

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### __isset

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
