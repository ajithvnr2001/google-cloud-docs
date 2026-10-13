---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient/
title: Cloud Datastore Client - Class DatastoreClient (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:38.596820+00:00
---

# Cloud Datastore Client - Class DatastoreClient (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class DatastoreClient (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class DatastoreClient.

Google Cloud Datastore is a highly-scalable NoSQL database for your applications. Find more information at the [Google Cloud Datastore docs](https://cloud.google.com/datastore/docs/).

Cloud Datastore supports [multi-tenant](https://cloud.google.com/datastore/docs/concepts/multitenancy) applications through use of data partitions. A partition ID can be supplied when creating an instance of Cloud Datastore, and will be used in all operations executed in that instance.

To enable the [Google Cloud Datastore Emulator](https://cloud.google.com/datastore/docs/tools/datastore-emulator), set the [`DATASTORE_EMULATOR_HOST`](https://goo.gl/vCVZrY) environment variable.

Example:
    
    
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient();
    
    
    
    // Multi-tenant applications can supply a namespace ID.
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient([
        'namespaceId' => 'my-application-namespace'
    ]);
    
    
    
    // Using the Datastore Emulator
    use Google\Cloud\Datastore\DatastoreClient;
    
    // Be sure to use the port specified when starting the emulator.
    // `8900` is used as an example only.
    putenv('DATASTORE_EMULATOR_HOST=localhost:8900');
    
    $datastore = new DatastoreClient();
    
    
    
    // Multi-database applications can supply a database ID.
    use Google\Cloud\Datastore\DatastoreClient;
    
    $datastore = new DatastoreClient([
        'namespaceId' => 'my-application-namespace',
        'databaseId' => 'my-database'
    ]);
    

## Namespace

Google \ Cloud \ Datastore

## Methods 

### __construct

Create a Datastore client.

**Parameters**  
---  
**Name** | **Description**  
`config` |  `array`   
Configuration Options. Some of this options details on [Google\ApiCore\Options\ClientOptions](https://docs.cloud.google.com/php/docs/reference/gax/latest/Options.ClientOptions.html).  
`↳ projectId` |  `string`   
The project ID from the Google Developer's Console.  
`↳ namespaceId` |  `string`   
Partitions data under a namespace. Useful for [Multitenant Projects](https://cloud.google.com/datastore/docs/concepts/multitenancy).  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
`↳ returnInt64AsObject` |  `bool`   
If true, 64 bit integers will be returned as a [Google\Cloud\Core\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Int64.html) object for 32 bit platform compatibility. **Defaults to** false.  
`↳ datastoreClient` |  `[V1\Client\DatastoreClient](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/V1.Client.DatastoreClient)`   
A client that is of type [V1\Client\DatastoreClient](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/V1.Client.DatastoreClient)  
`↳ apiEndpoint` |  `string`   
The address of the API remote host. May optionally include the port, formatted as "  
`↳ credentials` |  `[Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html)|[Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html)`   
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\Datastore\V1\DatastoreClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new DatastoreClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
`↳ credentialsConfig` |  `array`   
Options used to configure credentials, including auth token caching, for the client. For a full list of supporting configuration options, see [Google\ApiCore\CredentialsWrapper::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html#_Google_ApiCore_CredentialsWrapper__build__) .  
`↳ disableRetries` |  `bool`   
Determines whether or not retries defined by the client configuration should be disabled. Defaults to `false`.  
`↳ clientConfig` |  `string|array`   
Client method configuration, including retry settings. This option can be either a path to a JSON file, or a PHP array containing the decoded JSON data. By default this settings points to the default client config file, which is provided in the resources folder.  
`↳ transport` |  `string|TransportInterface`   
The transport used for executing network requests. May be either the string `rest` or `grpc`. Defaults to `grpc` if gRPC support is detected on the system. _Advanced usage_ : Additionally, it is possible to pass in an already instantiated [Google\ApiCore\Transport\TransportInterface](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.TransportInterface.html) object. Note that when this object is provided, any settings in $transportConfig, and any $apiEndpoint setting, will be ignored.  
`↳ transportConfig` |  `array`   
Configuration options that will be used to construct the transport. Options for each supported transport type should be passed in a key for that transport. For example: $transportConfig = [ 'grpc' => [...], 'rest' => [...], ]; See the [Google\ApiCore\Transport\GrpcTransport::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.GrpcTransport.html#_Google_ApiCore_Transport_GrpcTransport__build__) and [Google\ApiCore\Transport\RestTransport::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.RestTransport.html#_Google_ApiCore_Transport_RestTransport__build__) methods for the supported options.  
`↳ clientCertSource` |  `callable`   
A callable which returns the client cert as a string. This can be used to provide a certificate and private key to the transport layer for mTLS.  
`↳ logger` |  `false|LoggerInterface`   
A PSR-3 compliant logger. If set to false, logging is disabled, ignoring the 'GOOGLE_SDK_PHP_LOGGING' environment flag  
`↳ universeDomain` |  `string`   
The service domain for the client. Defaults to 'googleapis.com'.  
  
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
[optional] The key used to identify the record, or a string $kind. The key may be null only if the entity will be used as an embedded entity within another entity. Attempting to use keyless entities as root entities will result in error. _Defaults to_ * `null`.  
`entity` |  `array`   
[optional] The data, provided as an array of keys and values to fill the entity with. **Defaults to** `[]`.  
`options` |  `array`   
Configuration Options  
`↳ className` |  `string`   
If set, the given class will be returned. Value must be the name of a class implementing [EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface). **Defaults to** [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
`↳ excludeFromIndexes` |  `array`   
A list of entity keys to exclude from datastore indexes.  
**Returns**  
---  
**Type** | **Description**  
`[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)` |   
  
### geoPoint

See also:

  * [LatLng](https://cloud.google.com/datastore/reference/rest/Shared.Types/LatLng)



**Parameters**  
---  
**Name** | **Description**  
`latitude` |  `float`   
The latitude  
`longitude` |  `float`   
The longitude  
`allowNull` |  `bool`   
[optional] Whether null values are allowed. _Defaults to_ * `false`.  
**Returns**  
---  
**Type** | **Description**  
`[GeoPoint](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/GeoPoint)` |   
  
### blob

Create a new Blob

Example:
    
    
    $blob = $datastore->blob('hello world');
    
    
    
    // Blobs can be used to store binary data
    $blob = $datastore->blob(file_get_contents(__DIR__ .'/family-photo.jpg'));
    

**Parameter**  
---  
**Name** | **Description**  
`value` |  `string|resource|Psr\Http\Message\StreamInterface`   
The value to store in a blob.  
**Returns**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Blob)` |   
  
### int64

Create an Int64 object. This can be used to work with 64 bit integers as a string value while on a 32 bit platform.

Example:
    
    
    $int64 = $datastore->int64('9223372036854775807');
    

**Parameter**  
---  
**Name** | **Description**  
`value` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Int64.html)` |   
  
### cursor

Create a Cursor.

A cursor points to a position within a set of entities. Cloud Datastore uses Cursors for paginating query results.

Example:
    
    
    $cursor = $datastore->cursor($cursorValue);
    

**Parameter**  
---  
**Name** | **Description**  
`cursorValue` |  `string|int`   
  
**Returns**  
---  
**Type** | **Description**  
`[Cursor](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Cursor)` |   
  
### allocateId

See also:

  * [allocateIds](https://cloud.google.com/datastore/reference/rest/v1/projects/allocateIds)



**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)`   
The incomplete key.  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)` |   
  
### allocateIds

See also:

  * [allocateIds](https://cloud.google.com/datastore/reference/rest/v1/projects/allocateIds)



**Parameters**  
---  
**Name** | **Description**  
`keys` |  `array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>`   
The incomplete keys.  
`options` |  `array`   
Configuration Options.
    
    
     string $databaseId The ID of the database against which to make the request.
    

}  
**Returns**  
---  
**Type** | **Description**  
`array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>` |   
  
### transaction

See also:

  * [Datastore Transactions](https://cloud.google.com/datastore/docs/concepts/transactions)
  * [beginTransaction](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/beginTransaction)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ transactionOptions` |  `array`   
Transaction configuration. See [ReadWrite](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/beginTransaction#ReadWrite).  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Transaction)` |   
  
### readOnlyTransaction

See also:

  * [Datastore Transactions](https://cloud.google.com/datastore/docs/concepts/transactions)
  * [beginTransaction](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/beginTransaction)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ transactionOptions` |  `array`   
See [ReadOnly](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/beginTransaction#ReadOnly).  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
**Returns**  
---  
**Type** | **Description**  
`[ReadOnlyTransaction](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/ReadOnlyTransaction)` |   
  
### insert

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`entity` |  `[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)`   
The entity to be inserted.  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`string` | The entity version.  
  
### insertBatch

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`entities` |  `array<[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)>`   
The entities to be inserted.  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`array` | [Response Body](https://cloud.google.com/datastore/reference/rest/v1/projects/commit#response-body)  
  
### update

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`entity` |  `[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)`   
The entity to be updated.  
`options` |  `array`   
Configuration Options  
`↳ allowOverwrite` |  `bool`   
Entities must be updated as an entire resource. Patch operations are not supported. Because entities can be created manually, or obtained by a lookup or query, it is possible to accidentally overwrite an existing record with a new one when manually creating an entity. To provide additional safety, this flag must be set to `true` in order to update a record when the entity provided was not obtained through a lookup or query. **Defaults to** `false`.  
**Returns**  
---  
**Type** | **Description**  
`string` | The entity version.  
  
### updateBatch

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`entities` |  `array<[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)>`   
The entities to be updated.  
`options` |  `array`   
Configuration Options  
`↳ allowOverwrite` |  `bool`   
Entities must be updated as an entire resource. Patch operations are not supported. Because entities can be created manually, or obtained by a lookup or query, it is possible to accidentally overwrite an existing record with a new one when manually creating an entity. To provide additional safety, this flag must be set to `true` in order to update a record when the entity provided was not obtained through a lookup or query. **Defaults to** `false`.  
**Returns**  
---  
**Type** | **Description**  
`array` | [Response Body](https://cloud.google.com/datastore/reference/rest/v1/projects/commit#response-body)  
  
### upsert

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`entity` |  `[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)`   
The entity to be upserted.  
`options` |  `array`   
[optional] Configuration Options.  
**Returns**  
---  
**Type** | **Description**  
`string` | The entity version.  
  
### upsertBatch

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`entities` |  `array<[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)>`   
The entities to be upserted.  
`options` |  `array`   
[optional] Configuration Options.  
**Returns**  
---  
**Type** | **Description**  
`array` | [Response Body](https://cloud.google.com/datastore/reference/rest/v1/projects/commit#response-body)  
  
### delete

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)`   
The identifier to delete.  
`options` |  `array`   
Configuration options  
`↳ baseVersion` |  `string`   
Provides concurrency control. The version of the entity that this mutation is being applied to. If this does not match the current version on the server, the mutation conflicts.  
**Returns**  
---  
**Type** | **Description**  
`string` | The updated entity version number.  
  
### deleteBatch

See also:

  * [Commit API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/commit)



**Parameters**  
---  
**Name** | **Description**  
`keys` |  `array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>`   
The identifiers to delete.  
`options` |  `array`   
Configuration options  
`↳ baseVersion` |  `string`   
Provides concurrency control. The version of the entity that this mutation is being applied to. If this does not match the current version on the server, the mutation conflicts.  
**Returns**  
---  
**Type** | **Description**  
`array` | [Response Body](https://cloud.google.com/datastore/reference/rest/v1/projects/commit#response-body)  
  
### lookup

See also:

  * [Lookup API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/lookup)



**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)`   
The identifier to use to locate a desired entity.  
`options` |  `array`   
Configuration Options  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
`↳ className` |  `string`   
If set, the given class will be returned. Value must be the name of a class implementing [EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface). **Defaults to** [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
`↳ databaseId` |  `string`   
ID of the database to which the entities belong.  
`↳ readTime` |  `Timestamp`   
Reads entities as they were at the given timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)|null` |   
  
### lookupBatch

See also:

  * [Lookup API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/lookup)



**Parameters**  
---  
**Name** | **Description**  
`keys` |  `array<[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)>`   
The identifiers to look up.  
`options` |  `array`   
Configuration Options  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
`↳ className` |  `string|array`   
If a string, the given class will be returned. Value must be the name of a class implementing [EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface). If an array is given, it must be an associative array, where the key is a Kind and the value must implement [EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface). **Defaults to** [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
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
  
### query

Create a Query object.

The Query class can be used as a builder, or it can accept a query representation at instantiation.

Example:
    
    
    $query = $datastore->query();
    

**Parameter**  
---  
**Name** | **Description**  
`query` |  `array`   
[Query](https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#query)  
**Returns**  
---  
**Type** | **Description**  
`[Query\Query](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.Query)` |   
  
### aggregationQuery

Create an AggregationQuery object.

In addition to Query features, it supports aggregations.

Example:
    
    
    $query = $datastore->aggregationQuery();
    

**Parameter**  
---  
**Name** | **Description**  
`query` |  `array`   
[Query](https://cloud.google.com/datastore/reference/rest/v1/projects/runQuery#query)  
**Returns**  
---  
**Type** | **Description**  
`[Query\AggregationQuery](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery)` |   
  
### gqlQuery

Create a GqlQuery object.

Returns a Query object which can be executed using [DatastoreClient::runQuery()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/DatastoreClient#_Google_Cloud_Datastore_DatastoreClient__runQuery__).

Example:
    
    
    $query = $datastore->gqlQuery('SELECT * FROM Companies');
    
    
    
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
    

**Parameters**  
---  
**Name** | **Description**  
`query` |  `string`   
The [GQL Query](https://cloud.google.com/datastore/docs/apis/gql/gql_reference) string.  
`options` |  `array`   
Configuration Options  
`↳ allowLiterals` |  `bool`   
Whether literal values will be allowed in the query string. Parameter binding is strongly encouraged over literals. **Defaults to** `false`.  
`↳ bindings` |  `array`   
An array of values to bind to the query string. Queries using Named Bindings should provide a key/value set, while queries using Positional Bindings must provide a simple array. Query cursors may be provided using instances of [Cursor](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Cursor).  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
**Returns**  
---  
**Type** | **Description**  
`[Query\GqlQuery](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.GqlQuery)` |   
  
### runQuery

See also:

  * [RunQuery API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/runQuery)



**Parameters**  
---  
**Name** | **Description**  
`query` |  `[Query\QueryInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.QueryInterface)`   
A query object.  
`options` |  `array`   
Configuration Options  
`↳ className` |  `string`   
If set, the given class will be returned. Value must be the name of a class implementing [EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface). **Defaults to** [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
`↳ readTime` |  `Timestamp`   
Reads entities as they were at the given timestamp.  
**Returns**  
---  
**Type** | **Description**  
`[EntityIterator](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityIterator)<[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)>` |   
  
### runAggregationQuery

See also:

  * [RunAggregationQuery API documentation](https://cloud.google.com/datastore/docs/reference/rest/v1/projects/runAggregationQuery)



**Parameters**  
---  
**Name** | **Description**  
`query` |  `[Query\AggregationQuery](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQuery)`   
A query object.  
`options` |  `array`   
Configuration Options  
`↳ readConsistency` |  `string`   
See [ReadConsistency](https://cloud.google.com/datastore/reference/rest/v1/ReadOptions#ReadConsistency).  
`↳ readTime` |  `Timestamp`   
Reads entities as they were at the given timestamp.  
`↳ explainOptions` |  `ExplainOptions`   
An ExplainOptions instance. V1\ExplainOptions} </xref  
**Returns**  
---  
**Type** | **Description**  
`[Query\AggregationQueryResult](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Query.AggregationQueryResult)` |   
  
## Constants 

### FULL_CONTROL_SCOPE
    
    
    Value: 'https://www.googleapis.com/auth/datastore'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
