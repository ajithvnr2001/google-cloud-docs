---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreSessionHandler/
title: Cloud Datastore Client - Class DatastoreSessionHandler (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:38.689211+00:00
---

# Cloud Datastore Client - Class DatastoreSessionHandler (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreSessionHandler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class DatastoreSessionHandler (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class DatastoreSessionHandler.

Custom session handler backed by Cloud Datastore.

Instead of storing the session data in a local file, this handler stores the data in Cloud Datastore. The biggest benefit of doing this is the data can be shared by multiple instances, making it suitable for cloud applications.

The downside of using Cloud Datastore is that write operations will cost you some money, so it is highly recommended to minimize the write operations while using this handler. In order to do so, keep the data in the session as limited as possible; for example, it is ok to put only signed-in state and the user id in the session with this handler. However, for example, it is definitely not recommended that you store your application's whole undo history in the session, because every user operation will cause a Datastore write, potentially costing you a lot of money.

This handler doesn't provide pessimistic lock for session data. Instead, it uses Datastore Transaction for data consistency. This means that if multiple requests are modifying the same session data simultaneously, there will be more probablity that some of the `write` operations will fail.

If you are building an ajax application which may issue multiple requests to the server, please design your session data carefully in order to avoid possible data contentions. Also please see the 2nd example below for how to properly handle errors on `write` operations.

The handler sets the Datastore namespace to the value of session.save_path, isolating the session data from your application data, it also uses the session.name as the Datastore kind, and the session id as the Datastore id. By default, it does nothing on gc for reducing the cost. Pass positive value up to 1000 for $gcLimit parameter to delete entities in gc.

Note: The datastore transaction only lasts 60 seconds. If this handler is used for long running requests, it will fail on `write`.

The first example automatically writes the session data. It's handy, but the code doesn't stop even if it fails to write the session data, because the `write` happens when the code exits. If you want to know whether the session data is correctly written to the Datastore, you need to call `session_write_close()` explicitly and then handle `E_USER_WARNING` properly. See the second example for a demonstration.

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    use Google\Cloud\Datastore\DatastoreSessionHandler;
    
    $datastore = new DatastoreClient();
    
    $handler = new DatastoreSessionHandler($datastore);
    
    session_set_save_handler($handler, true);
    session_save_path('sessions');
    session_start();
    
    // Then write and read the $_SESSION array.
    $_SESSION['name'] = 'Bob';
    echo $_SESSION['name'];
    
    
    
    // Session Handler with Error Handling
    use Google\Cloud\Datastore\DatastoreClient;
    use Google\Cloud\Datastore\DatastoreSessionHandler;
    
    $datastore = new DatastoreClient();
    
    $handler = new DatastoreSessionHandler($datastore);
    session_set_save_handler($handler, true);
    session_save_path('sessions');
    session_start();
    
    // Then read and write the $_SESSION array.
    $_SESSION['name'] = 'Bob';
    
    function handle_session_error($errNo, $errStr, $errFile, $errLine) {
        // We throw an exception here, but you can do whatever you need.
        throw new RuntimeException("$errStr in $errFile on line $errLine", $errNo);
    }
    
    set_error_handler('handle_session_error', E_USER_WARNING);
    // If `write` fails for any reason, an exception will be thrown.
    session_write_close();
    restore_error_handler();
    
    // You can still read the $_SESSION array after closing the session.
    echo $_SESSION['name'];
    

## Namespace

Google \ Cloud \ Datastore

## Implements

\SessionHandlerInterface

## Methods 

### __construct

Create a custom session handler backed by Cloud Datastore.

**Parameters**  
---  
**Name** | **Description**  
`datastore` |  `[DatastoreClient](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient)`   
Datastore client.  
`gcLimit` |  `int`   
[optional] A number of entities to delete in the garbage collection. Defaults to 0 which means it does nothing. The value larger than 1000 will be cut down to 1000.  
`options` |  `array`   
Configuration Options  
`↳ entityOptions` |  `array`   
Default options to be passed to the [DatastoreClient::entity()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient#_Google_Cloud_Datastore_DatastoreClient__entity__) method when writing session data to Datastore. If not specified, defaults to `['excludeFromIndexes' => ['data']]`.  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
  
### open

Start a session, by creating a transaction for the later `write`.

**Parameters**  
---  
**Name** | **Description**  
`savePath` |  `string`   
The value of `session.save_path` setting will be used here. It will use this value as the Datastore namespaceId.  
`sessionName` |  `string`   
The value of `session.name` setting will be used here. It will use this value as the Datastore kind.  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### close

Just return true for this implementation.

### read

Read the session data from Cloud Datastore.

**Parameter**  
---  
**Name** | **Description**  
`id` |  `mixed`   
  
  
### write

Write the session data to Cloud Datastore.

**Parameters**  
---  
**Name** | **Description**  
`id` |  `string`   
Identifier used to construct a [Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key) for the [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity) to be written.  
`data` |  `string`   
The session data to write to the [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### destroy

Delete the session data from Cloud Datastore.

**Parameter**  
---  
**Name** | **Description**  
`id` |  `mixed`   
  
  
### gc

Delete the old session data from Cloud Datastore.

**Parameter**  
---  
**Name** | **Description**  
`maxlifetime` |  `mixed`   
  
  
## Constants 

### DEFAULT_GC_LIMIT
    
    
    Value: 0

### NAMESPACE_ALLOWED_PATTERN
    
    
    Value: '/^[A-Za-z\d\.\-_]{0,100}$/'

### NAMESPACE_RESERVED_PATTERN
    
    
    Value: '/^__.*__$/'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
