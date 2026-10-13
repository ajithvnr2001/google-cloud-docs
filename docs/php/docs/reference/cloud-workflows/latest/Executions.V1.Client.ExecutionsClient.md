---
url: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Client.ExecutionsClient
title: Google Cloud Workflows V1 Client - Class ExecutionsClient (1.4.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:30.610759+00:00
---

# Google Cloud Workflows V1 Client - Class ExecutionsClient (1.4.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Client.ExecutionsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Workflows V1 Client - Class ExecutionsClient (1.4.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.4 (latest)  1.3.0  1.2.1  1.1.1  1.0.3  0.5.5  0.4.2  0.3.0  0.2.17 

Reference documentation and code samples for the Google Cloud Workflows V1 Client class ExecutionsClient.

Service Description: Executions is used to start and manage running instances of [Workflows](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/V1.Workflow) called executions.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Cloud \ Workflows \ Executions \ V1 \ Client

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array|[Google\ApiCore\Options\ClientOptions](https://docs.cloud.google.com/php/docs/reference/gax/latest/Options.ClientOptions.html)`   
Optional. Options for configuring the service API wrapper.  
`↳ apiEndpoint` |  `string`   
The address of the API remote host. May optionally include the port, formatted as "  
`↳ credentials` |  `[Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html)|[Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html)`   
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\Workflows\Executions\V1\ExecutionsClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new ExecutionsClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
`↳ credentialsConfig` |  `array`   
Options used to configure credentials, including auth token caching, for the client. For a full list of supporting configuration options, see [Google\ApiCore\CredentialsWrapper::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html#_Google_ApiCore_CredentialsWrapper__build__) .  
`↳ disableRetries` |  `bool`   
Determines whether or not retries defined by the client configuration should be disabled. Defaults to `false`.  
`↳ clientConfig` |  `string|array`   
Client method configuration, including retry settings. This option can be either a path to a JSON file, or a PHP array containing the decoded JSON data. By default this settings points to the default client config file, which is provided in the resources folder.  
`↳ transport` |  `string|[Google\ApiCore\Transport\TransportInterface](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.TransportInterface.html)`   
The transport used for executing network requests. May be either the string `rest` or `grpc`. Defaults to `grpc` if gRPC support is detected on the system. _Advanced usage_ : Additionally, it is possible to pass in an already instantiated [Google\ApiCore\Transport\TransportInterface](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.TransportInterface.html) object. Note that when this object is provided, any settings in $transportConfig, and any $apiEndpoint setting, will be ignored.  
`↳ transportConfig` |  `array`   
Configuration options that will be used to construct the transport. Options for each supported transport type should be passed in a key for that transport. For example: $transportConfig = [ 'grpc' => [...], 'rest' => [...], ]; See the [Google\ApiCore\Transport\GrpcTransport::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.GrpcTransport.html#_Google_ApiCore_Transport_GrpcTransport__build__) and [Google\ApiCore\Transport\RestTransport::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.RestTransport.html#_Google_ApiCore_Transport_RestTransport__build__) methods for the supported options.  
`↳ clientCertSource` |  `callable`   
A callable which returns the client cert as a string. This can be used to provide a certificate and private key to the transport layer for mTLS.  
`↳ logger` |  `false|Psr\Log\LoggerInterface`   
A PSR-3 compliant logger. If set to false, logging is disabled, ignoring the 'GOOGLE_SDK_PHP_LOGGING' environment flag  
`↳ universeDomain` |  `string`   
The service domain for the client. Defaults to 'googleapis.com'.  
  
### cancelExecution

Cancels an execution of the given name.

The async variant is [ExecutionsClient::cancelExecutionAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Client.ExecutionsClient#_Google_Cloud_Workflows_Executions_V1_Client_ExecutionsClient__cancelExecutionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\CancelExecutionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.CancelExecutionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Workflows\Executions\V1\Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)` |   
  
### createExecution

Creates a new execution using the latest revision of the given workflow.

The async variant is [ExecutionsClient::createExecutionAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Client.ExecutionsClient#_Google_Cloud_Workflows_Executions_V1_Client_ExecutionsClient__createExecutionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\CreateExecutionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.CreateExecutionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Workflows\Executions\V1\Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)` |   
  
### getExecution

Returns an execution of the given name.

The async variant is [ExecutionsClient::getExecutionAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Client.ExecutionsClient#_Google_Cloud_Workflows_Executions_V1_Client_ExecutionsClient__getExecutionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\GetExecutionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.GetExecutionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Workflows\Executions\V1\Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)` |   
  
### listExecutions

Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

The async variant is [ExecutionsClient::listExecutionsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Client.ExecutionsClient#_Google_Cloud_Workflows_Executions_V1_Client_ExecutionsClient__listExecutionsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\ListExecutionsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ListExecutionsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)` |   
  
### cancelExecutionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\CancelExecutionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.CancelExecutionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Workflows\Executions\V1\Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)>` |   
  
### createExecutionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\CreateExecutionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.CreateExecutionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Workflows\Executions\V1\Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)>` |   
  
### getExecutionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\GetExecutionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.GetExecutionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Workflows\Executions\V1\Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)>` |   
  
### listExecutionsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Workflows\Executions\V1\ListExecutionsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ListExecutionsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### static::executionName

Formats a string containing the fully-qualified path to represent a execution resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`workflow` |  `string`   
  
`execution` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted execution resource.  
  
### static::workflowName

Formats a string containing the fully-qualified path to represent a workflow resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`workflow` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted workflow resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * execution: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
  * workflow: projects/{project}/locations/{location}/workflows/{workflow}



The optional $template argument can be supplied to specify a particular pattern, and must match one of the templates listed above. If no $template argument is provided, or if the $template argument does not match one of the templates listed, then parseName will check each of the supported templates, and return the first match.

**Parameters**  
---  
**Name** | **Description**  
`formattedName` |  `string`   
The formatted name string  
`template` |  `?string`   
Optional name of template to match  
**Returns**  
---  
**Type** | **Description**  
`array` | An associative array from name component IDs to component values.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
