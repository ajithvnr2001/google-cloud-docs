---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/migrating/
title: Migrating Google Datastore from V1 to V2 \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:38.159086+00:00
---

# Migrating Google Datastore from V1 to V2  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Migrating Google Datastore from V1 to V2 Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

## How to upgrade

Update your `google/cloud-datastore` dependency to `^2.0`:
    
    
    {
        "require": {
            "google/cloud-datastore": "^2.0"
        }
    }
    

## Breaking Changes

### Version constant removed

Removed `DatastoreClient::VERSION`, use the `VERSION` file in the library root instead.

### EntityInterface changes

Types have been added to the methods in [`EntityInterface`](https://docs.cloud.google.com/static/php/docs/reference/cloud-datastore/latest/src/EntityInterface.php). This means that any classes implementing this interface will need to be updated to match the new method signatures:
    
    
     class Business implements EntityInterface
     {
         use EntityTrait;
    
    -     public static function mappings()
    +     public static function mappings(): array
         {
             return [
                 'parent' => Business::class
             ];
         }
     }
    

### Client Options changes

The following [`ClientOptions`](https://cloud.google.com/php/docs/reference/gax/latest/Options.ClientOptions) have been reorganized. This was done to ensure client options are consistent across all Google Cloud clients.

  * `authCache` -> Moved to `credentialsConfig.authCache`
  * `authCacheOptions` -> Moved to `credentialsConfig.authCacheOptions`
  * `credentialsFetcher` -> Moved to `credentials`
  * `keyFile` -> Moved to `credentials`
  * `keyFilePath` -> Moved to `credentials`
  * `requestTimeout` -> Removed from client options and moved to a call option `timeoutMillis`
  * `scopes` -> Moved to `credentialsConfig.scopes`
  * `defaultScopes` -> Moved to `credentialsConfig.defaultScopes`
  * `quotaProject` -> Moved to `credentialsConfig.quotaProject`
  * `httpHandler` -> Moved to `transportConfig.rest.httpHandler`
  * `authHttpHandler` -> Moved to `credentialsConfig.authHttpHandler`
  * `asyncHttpHandler` -> Removed in favor of a single httpHandler option.
  * `restOptions` -> Moved to `transportConfig.rest`
  * `grpcOptions` -> Moved to `transportConfig.grpc`
  * `accessToken` -> Removed - This option is no longer supported. Use the `$credentialsFetcher` option instead.
  * `shouldSignRequest` -> Removed - obsolete
  * `preferNumericProjectId` -> Removed - obsolete



### Retry Options changes

The retry options have been moved to use [`RetrySettings`](https://cloud.google.com/php/docs/reference/gax/latest/RetrySettings) in Client Options and in call options.

  * `retries` -> Renamed to `retrySettings.maxRetries`
  * `restRetryFunction` -> Renamed to `retrySettings.retryFunction`
  * `grpcRetryFunction` -> Renamed to `retrySettings.retryFunction`
  * `delayFunc`/`calcDelayFunction` -> Removed in favor of the properties `retrySettings.initialRetryDelayMillis`, `retrySettings.retryDelayMultiplier` and `retrySettings.maxRetryDelayMillis`.



## Internal changes

We expect these changes to not break existing code, as they have been done in classes marked `@internal` or as part of refactoring, but to be safe, these changes have been released in a major version.

### Types for properties, parameters, and return types.

Types have been added for all properties, parameters and return types. This means that any classes implementing interfaces in this library (specifically, `EntityInterface` as mentioned above), will need to be updated to match the new method signatures. Typing constraints may have other effects where the incorrect types had been previously applied.

### Options array validation

Previously, if unrecognized array keys were passed into methods, these additional arguments would be ignored. Now, a `LogicException` will be thrown in the `OptionsValidator` class with the message "Unexpected option(s) provided: [OPTION-NAME]". If you see this exception, and you believe it to be an error, please file an issue in the [google-cloud-php repo](https://github.com/googleapis/google-cloud-php/issues) and let us know.

### Connection classes are not used anymore.

The following classes are removed, and have been replaced with the generated GAPIC client `Google\Cloud\Datastore\V1\Client\DatastoreClient`:

  * `Google\Cloud\Datastore\Connection\ConnectionInterface` is removed
  * `Google\Cloud\Datastore\Connection\Rest` is removed
  * `Google\Cloud\Datastore\Connection\Grpc` is removed



Additionally, the previously generated GAPIC client (`Google\Cloud\Datastore\V1\DatastoreClient`, which has a similar name to `Google\Cloud\Datastore\V1\Client\DatastoreClient`, but without the `Client` namespace) has been removed. For more information, see [Migrating to V2](https://cloud.google.com/php/docs/reference/help/migrating).

### Constants in `Query\Query` have been changed from string to int

These constants are used internally, but if they are being used in any code, they will need to be updated:

  * `Google\Cloud\Datastore\Query\Query::OP_DEFAULT` changed from `'EQUAL'` to `5`
  * `Google\Cloud\Datastore\Query\Query::OP_LESS_THAN` changed from `'LESS_THAN'` to `1`
  * `Google\Cloud\Datastore\Query\Query::OP_LESS_THAN_OR_EQUAL` changed from `'LESS_THAN_OR_EQUAL'` to `2`
  * `Google\Cloud\Datastore\Query\Query::OP_GREATER_THAN` changed from `'GREATER_THAN'` to `3`
  * `Google\Cloud\Datastore\Query\Query::OP_GREATER_THAN_OR_EQUAL` changed from `'GREATER_THAN_OR_EQUAL'` to `4`
  * `Google\Cloud\Datastore\Query\Query::OP_EQUALS` changed from `'EQUAL'` to `5`
  * `Google\Cloud\Datastore\Query\Query::OP_NOT_EQUALS` changed from `'NOT_EQUAL'` to `9`
  * `Google\Cloud\Datastore\Query\Query::OP_IN` changed from `'IN'` to `6`
  * `Google\Cloud\Datastore\Query\Query::OP_NOT_IN` changed from `'NOT_IN'` to `13`
  * `Google\Cloud\Datastore\Query\Query::OP_HAS_ANCESTOR` changed from `'HAS_ANCESTOR'` to `11`
  * `Google\Cloud\Datastore\Query\Query::ORDER_DEFAULT` changed from `'ASCENDING'` to `1`
  * `Google\Cloud\Datastore\Query\Query::ORDER_DESCENDING` changed from `'DESCENDING'` to `2`
  * `Google\Cloud\Datastore\Query\Query::ORDER_ASCENDING` changed from `'ASCENDING'` to `1`



### Protobuf backwards compatibility files have been removed

These class aliases have been deprecated for a very long time, and are finally being removed. Update to the namespaced version (replacing `_` with `\`) to upgrade.

  * `Google\Cloud\Datastore\V1\PropertyFilter_Operator` has been removed
  * `Google\Cloud\Datastore\V1\EntityResult_ResultType` has been removed
  * `Google\Cloud\Datastore\V1\CommitRequest_Mode` has been removed
  * `Google\Cloud\Datastore\V1\CompositeFilter_Operator` has been removed
  * `Google\Cloud\Datastore\V1\TransactionOptions_ReadWrite` has been removed
  * `Google\Cloud\Datastore\V1\QueryResultBatch_MoreResultsType` has been removed
  * `Google\Cloud\Datastore\V1\TransactionOptions_ReadOnly` has been removed
  * `Google\Cloud\Datastore\V1\PropertyOrder_Direction` has been removed
  * `Google\Cloud\Datastore\V1\AggregationQuery_Aggregation` has been removed
  * `Google\Cloud\Datastore\V1\ReadOptions_ReadConsistency` has been removed
  * `Google\Cloud\Datastore\V1\Key_PathElement` has been removed
  * `Google\Cloud\Datastore\V1\AggregationQuery_Aggregation_Count` has been removed



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
