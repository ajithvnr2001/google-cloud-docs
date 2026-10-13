---
url: https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Client.OperationsClient
title: Google LongRunning Client - Class OperationsClient (0.8.5) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:08.987718+00:00
---

# Google LongRunning Client - Class OperationsClient (0.8.5)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Client.OperationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google LongRunning Client - Class OperationsClient (0.8.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.5 (latest)  0.7.1  0.6.0  0.5.0  0.4.7  0.3.0  0.2.6 

Reference documentation and code samples for the Google LongRunning Client class OperationsClient.

Service Description: Manages long-running operations with an API service.

When an API method normally takes long time to complete, it can be designed to return [Operation](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation) to the client, and the client can use this interface to receive the real response asynchronously by polling the operation resource, or pass the operation resource to another API (such as Pub/Sub API) to receive the response. Any API service that returns long-running operations should implement the `Operations` interface so developers can have a consistent client experience.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

## Namespace

Google \ LongRunning \ Client

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array|Google\ApiCore\Options\ClientOptions`   
Optional. Options for configuring the service API wrapper.  
`↳ apiEndpoint` |  `string`   
The address of the API remote host. May optionally include the port, formatted as "  
`↳ credentials` |  `[Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html)|Google\ApiCore\CredentialsWrapper`   
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or Google\ApiCore\CredentialsWrapper object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\LongRunning\OperationsClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new OperationsClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
`↳ credentialsConfig` |  `array`   
Options used to configure credentials, including auth token caching, for the client. For a full list of supporting configuration options, see Google\ApiCore\CredentialsWrapper::build() .  
`↳ disableRetries` |  `bool`   
Determines whether or not retries defined by the client configuration should be disabled. Defaults to `false`.  
`↳ clientConfig` |  `string|array`   
Client method configuration, including retry settings. This option can be either a path to a JSON file, or a PHP array containing the decoded JSON data. By default this settings points to the default client config file, which is provided in the resources folder.  
`↳ transport` |  `string|Google\ApiCore\Transport\TransportInterface`   
The transport used for executing network requests. May be either the string `rest` or `grpc`. Defaults to `grpc` if gRPC support is detected on the system. _Advanced usage_ : Additionally, it is possible to pass in an already instantiated Google\ApiCore\Transport\TransportInterface object. Note that when this object is provided, any settings in $transportConfig, and any $apiEndpoint setting, will be ignored.  
`↳ transportConfig` |  `array`   
Configuration options that will be used to construct the transport. Options for each supported transport type should be passed in a key for that transport. For example: $transportConfig = [ 'grpc' => [...], 'rest' => [...], ]; See the Google\ApiCore\Transport\GrpcTransport::build() and Google\ApiCore\Transport\RestTransport::build() methods for the supported options.  
`↳ clientCertSource` |  `callable`   
A callable which returns the client cert as a string. This can be used to provide a certificate and private key to the transport layer for mTLS.  
`↳ logger` |  `false|Psr\Log\LoggerInterface`   
A PSR-3 compliant logger. If set to false, logging is disabled, ignoring the 'GOOGLE_SDK_PHP_LOGGING' environment flag  
`↳ universeDomain` |  `string`   
The service domain for the client. Defaults to 'googleapis.com'.  
  
### cancelOperation

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use [Operations.GetOperation](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.OperationsClient#_Google_LongRunning_OperationsClient__getOperation__) or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation#_Google_LongRunning_Operation__getError__) value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

The async variant is [OperationsClient::cancelOperationAsync()](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Client.OperationsClient#_Google_LongRunning_Client_OperationsClient__cancelOperationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\CancelOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.CancelOperationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `Google\ApiCore\RetrySettings|array`   
Retry settings to use for this call. Can be a Google\ApiCore\RetrySettings object, or an associative array of retry settings parameters. See the documentation on Google\ApiCore\RetrySettings for example usage.  
  
### deleteOperation

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

The async variant is [OperationsClient::deleteOperationAsync()](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Client.OperationsClient#_Google_LongRunning_Client_OperationsClient__deleteOperationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\DeleteOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.DeleteOperationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `Google\ApiCore\RetrySettings|array`   
Retry settings to use for this call. Can be a Google\ApiCore\RetrySettings object, or an associative array of retry settings parameters. See the documentation on Google\ApiCore\RetrySettings for example usage.  
  
### getOperation

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

The async variant is [OperationsClient::getOperationAsync()](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Client.OperationsClient#_Google_LongRunning_Client_OperationsClient__getOperationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\GetOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.GetOperationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `Google\ApiCore\RetrySettings|array`   
Retry settings to use for this call. Can be a Google\ApiCore\RetrySettings object, or an associative array of retry settings parameters. See the documentation on Google\ApiCore\RetrySettings for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\LongRunning\Operation](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation)` |   
  
### listOperations

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

The async variant is [OperationsClient::listOperationsAsync()](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Client.OperationsClient#_Google_LongRunning_Client_OperationsClient__listOperationsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\ListOperationsRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.ListOperationsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `Google\ApiCore\RetrySettings|array`   
Retry settings to use for this call. Can be a Google\ApiCore\RetrySettings object, or an associative array of retry settings parameters. See the documentation on Google\ApiCore\RetrySettings for example usage.  
**Returns**  
---  
**Type** | **Description**  
`Google\ApiCore\PagedListResponse` |   
  
### waitOperation

Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state. If the operation is already done, the latest state is immediately returned. If the timeout specified is greater than the default HTTP/RPC timeout, the HTTP/RPC timeout is used. If the server does not support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

Note that this method is on a best-effort basis. It may return the latest state before the specified timeout (including immediately), meaning even an immediate response is no guarantee that the operation is done.

The async variant is [OperationsClient::waitOperationAsync()](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Client.OperationsClient#_Google_LongRunning_Client_OperationsClient__waitOperationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\WaitOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.WaitOperationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `Google\ApiCore\RetrySettings|array`   
Retry settings to use for this call. Can be a Google\ApiCore\RetrySettings object, or an associative array of retry settings parameters. See the documentation on Google\ApiCore\RetrySettings for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\LongRunning\Operation](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation)` |   
  
### cancelOperationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\CancelOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.CancelOperationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteOperationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\DeleteOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.DeleteOperationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### getOperationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\GetOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.GetOperationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\LongRunning\Operation](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation)>` |   
  
### listOperationsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\ListOperationsRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.ListOperationsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<Google\ApiCore\PagedListResponse>` |   
  
### waitOperationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\LongRunning\WaitOperationRequest](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.WaitOperationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\LongRunning\Operation](https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
