---
url: https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings/
title: Google API Core Client - Class RetrySettings (1.51.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:51.693482+00:00
---

# Google API Core Client - Class RetrySettings (1.51.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Core Client - Class RetrySettings (1.51.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.51.0 (latest)  1.46.0  1.43.0  1.42.5  1.40.0  1.38.2  1.36.1  1.35.1 

Reference documentation and code samples for the Google API Core Client class RetrySettings.

The RetrySettings class is used to configure retrying and timeouts for RPCs.

This class can be passed as an optional parameter to RPC methods, or as part of an optional array in the constructor of a client object. In addition, many RPCs and API clients accept a PHP array in place of a RetrySettings object. This can be used to change particular retry parameters without needing to construct a complete RetrySettings object.

## Constructing a RetrySettings object

See the RetrySettings constructor for documentation about parameters that can be passed to RetrySettings.

Example of creating a RetrySettings object using the constructor:
    
    
    $retrySettings = new RetrySettings([
        'initialRetryDelayMillis' => 100,
        'retryDelayMultiplier' => 1.3,
        'maxRetryDelayMillis' => 60000,
        'initialRpcTimeoutMillis' => 20000,
        'rpcTimeoutMultiplier' => 1.0,
        'maxRpcTimeoutMillis' => 20000,
        'totalTimeoutMillis' => 600000,
        'retryableCodes' => [ApiStatus::DEADLINE_EXCEEDED, ApiStatus::UNAVAILABLE],
    ]);
    

It is also possible to create a new RetrySettings object from an existing object using the [RetrySettings::with()](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings#_Google_ApiCore_RetrySettings__with__) method.

Example modifying an existing RetrySettings object using `with()`:
    
    
    $newRetrySettings = $retrySettings->with([
        'totalTimeoutMillis' => 700000,
    ]);
    

## Modifying the retry behavior of an RPC method

RetrySettings objects can be used to control retries for many RPC methods in [google-cloud-php](https://github.com/googleapis/google-cloud-php). The examples below make use of the [GroupServiceClient](https://cloud.google.com/php/docs/reference/cloud-monitoring/latest/V3.Client.GroupServiceClient) from the [Monitoring V3 API](https://github.com/googleapis/google-cloud-php/tree/master/src/Monitoring/V3), but they can be applied to other APIs in the [google-cloud-php](https://github.com/googleapis/google-cloud-php) repository.

It is possible to specify the retry behavior to be used by an RPC via the `retrySettings` field in the `optionalArgs` parameter. The `retrySettings` field can contain either a RetrySettings object, or a PHP array containing the particular retry parameters to be updated.

Example of disabling retries for a single call to the [listGroups](https://cloud.google.com/php/docs/reference/cloud-monitoring/latest/V3.Client.GroupServiceClient#_Google_Cloud_Monitoring_V3_Client_GroupServiceClient__listGroups__) method, and setting a custom timeout:
    
    
    $result = $client->listGroups($name, [
        'retrySettings' => [
            'retriesEnabled' => false,
            'noRetriesRpcTimeoutMillis' => 5000,
        ]
    ]);
    

Example of creating a new RetrySettings object and using it to override the retry settings for a call to the [listGroups](https://cloud.google.com/php/docs/reference/cloud-monitoring/latest/V3.Client.GroupServiceClient#_Google_Cloud_Monitoring_V3_Client_GroupServiceClient__listGroups__) method:
    
    
    $customRetrySettings = new RetrySettings([
        'initialRetryDelayMillis' => 100,
        'retryDelayMultiplier' => 1.3,
        'maxRetryDelayMillis' => 60000,
        'initialRpcTimeoutMillis' => 20000,
        'rpcTimeoutMultiplier' => 1.0,
        'maxRpcTimeoutMillis' => 20000,
        'totalTimeoutMillis' => 600000,
        'retryableCodes' => [ApiStatus::DEADLINE_EXCEEDED, ApiStatus::UNAVAILABLE],
    ]);
    
    $result = $client->listGroups($name, [
        'retrySettings' => $customRetrySettings
    ]);
    

## Modifying the default retry behavior for RPC methods on a Client object

It is also possible to specify the retry behavior for RPC methods when constructing a client object using the 'retrySettingsArray'. The examples below again make use of the [GroupServiceClient](https://cloud.google.com/php/docs/reference/cloud-monitoring/latest/V3.Client.GroupServiceClient) from the [Monitoring V3 API](https://github.com/googleapis/google-cloud-php/tree/main/Monitoring/src/V3), but they can be applied to other APIs in the [google-cloud-php](https://github.com/googleapis/google-cloud-php) repository.

The GroupServiceClient object accepts an optional `retrySettingsArray` parameter, which can be used to specify retry behavior for RPC methods on the client. The `retrySettingsArray` accepts a PHP array in which keys are the names of RPC methods on the client, and values are either a RetrySettings object or a PHP array containing the particular retry parameters to be updated.

Example updating the retry settings for four methods of GroupServiceClient:
    
    
    use Google\Cloud\Monitoring\V3\GroupServiceClient;
    
    $customRetrySettings = new RetrySettings([
        'initialRetryDelayMillis' => 100,
        'retryDelayMultiplier' => 1.3,
        'maxRetryDelayMillis' => 60000,
        'initialRpcTimeoutMillis' => 20000,
        'rpcTimeoutMultiplier' => 1.0,
        'maxRpcTimeoutMillis' => 20000,
        'totalTimeoutMillis' => 600000,
        'retryableCodes' => [ApiStatus::DEADLINE_EXCEEDED, ApiStatus::UNAVAILABLE],
    ]);
    
    $updatedCustomRetrySettings = $customRetrySettings->with([
        'totalTimeoutMillis' => 700000
    ]);
    
    $client = new GroupServiceClient([
        'retrySettingsArray' => [
            'listGroups' => ['retriesEnabled' => false],
            'getGroup' => [
                'initialRpcTimeoutMillis' => 10000,
                'maxRpcTimeoutMillis' => 30000,
                'totalTimeoutMillis' => 60000,
            ],
            'deleteGroup' => $customRetrySettings,
            'updateGroup' => $updatedCustomRetrySettings
        ],
    ]);
    

## Configure the use of logical timeout

To configure the use of a logical timeout, where a logical timeout is the duration a method is given to complete one or more RPC attempts, with each attempt using only the time remaining in the logical timeout, use [RetrySettings::logicalTimeout()](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings#_Google_ApiCore_RetrySettings__logicalTimeout__) combined with [RetrySettings::with()](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings#_Google_ApiCore_RetrySettings__with__).
    
    
    $timeoutSettings = RetrySettings::logicalTimeout(30000);
    
    $customRetrySettings = $customRetrySettings->with($timeoutSettings);
    
    $result = $client->listGroups($name, [
        'retrySettings' => $customRetrySettings
    ]);
    

[RetrySettings::logicalTimeout()](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings#_Google_ApiCore_RetrySettings__logicalTimeout__) can also be used on a method call independent of a RetrySettings instance.
    
    
    $timeoutSettings = RetrySettings::logicalTimeout(30000);
    
    $result = $client->listGroups($name, [
        'retrySettings' => $timeoutSettings
    ]);
    

## Namespace

Google \ ApiCore

## Methods 

### __construct

Constructs an instance.

**Parameters**  
---  
**Name** | **Description**  
`settings` |  `array`   
Required. Settings for configuring the retry behavior. All parameters are required except $retriesEnabled and $noRetriesRpcTimeoutMillis, which are optional and have defaults determined based on the other settings provided.  
`↳ retriesEnabled` |  `bool`   
Optional. Enables retries. If not specified, the value is determined using the $retryableCodes setting. If $retryableCodes is empty, then $retriesEnabled is set to false; otherwise, it is set to true.  
`↳ noRetriesRpcTimeoutMillis` |  `int`   
Optional. The timeout of the rpc call to be used if $retriesEnabled is false, in milliseconds. It not specified, the value of $initialRpcTimeoutMillis is used.  
`↳ retryableCodes` |  `array`   
The Status codes that are retryable. Each status should be either one of the string constants defined on [ApiStatus](https://docs.cloud.google.com/php/docs/reference/gax/latest/ApiStatus) or an integer constant defined on [Google\Rpc\Code](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Code.html).  
`↳ initialRetryDelayMillis` |  `int`   
The initial delay of retry in milliseconds.  
`↳ retryDelayMultiplier` |  `int`   
The exponential multiplier of retry delay.  
`↳ maxRetryDelayMillis` |  `int`   
The max delay of retry in milliseconds.  
`↳ initialRpcTimeoutMillis` |  `int`   
The initial timeout of rpc call in milliseconds.  
`↳ rpcTimeoutMultiplier` |  `int`   
The exponential multiplier of rpc timeout.  
`↳ maxRpcTimeoutMillis` |  `int`   
The max timeout of rpc call in milliseconds.  
`↳ totalTimeoutMillis` |  `int`   
The max accumulative timeout in total.  
`↳ maxRetries` |  `int`   
The max retries allowed for an operation. Defaults to the value of the DEFAULT_MAX_RETRIES constant. This option is experimental.  
`↳ retryFunction` |  `callable`   
This function will be used to decide if we should retry or not. Callable signature: `function (Exception $e, array $options): bool` This option is experimental.  
  
### with

Creates a new instance of RetrySettings that updates the settings in the existing instance with the settings specified in the $settings parameter.

**Parameter**  
---  
**Name** | **Description**  
`settings` |  `array`   
Settings for configuring the retry behavior. Supports all of the options supported by the constructor; see [RetrySettings::__construct()](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings#_Google_ApiCore_RetrySettings____construct__). All parameters are optional - all unset parameters will default to the value in the existing instance.  
**Returns**  
---  
**Type** | **Description**  
`[RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings)` |   
  
### retriesEnabled

**Returns**  
---  
**Type** | **Description**  
`bool` | Returns true if retries are enabled, otherwise returns false.  
  
### getNoRetriesRpcTimeoutMillis

**Returns**  
---  
**Type** | **Description**  
`int` | The timeout of the rpc call to be used if $retriesEnabled is false, in milliseconds.  
  
### getRetryableCodes

**Returns**  
---  
**Type** | **Description**  
`int[]` | Status codes to retry  
  
### getInitialRetryDelayMillis

**Returns**  
---  
**Type** | **Description**  
`int` | The initial retry delay in milliseconds. If $this->retriesEnabled() is false, this setting is unused.  
  
### getRetryDelayMultiplier

**Returns**  
---  
**Type** | **Description**  
`float` | The retry delay multiplier. If $this->retriesEnabled() is false, this setting is unused.  
  
### getMaxRetryDelayMillis

**Returns**  
---  
**Type** | **Description**  
`int` | The maximum retry delay in milliseconds. If $this->retriesEnabled() is false, this setting is unused.  
  
### getInitialRpcTimeoutMillis

**Returns**  
---  
**Type** | **Description**  
`int` | The initial rpc timeout in milliseconds. If $this->retriesEnabled() is false, this setting is unused - use noRetriesRpcTimeoutMillis to set the timeout in that case.  
  
### getRpcTimeoutMultiplier

**Returns**  
---  
**Type** | **Description**  
`float` | The rpc timeout multiplier. If $this->retriesEnabled() is false, this setting is unused.  
  
### getMaxRpcTimeoutMillis

**Returns**  
---  
**Type** | **Description**  
`int` | The maximum rpc timeout in milliseconds. If $this->retriesEnabled() is false, this setting is unused - use noRetriesRpcTimeoutMillis to set the timeout in that case.  
  
### getTotalTimeoutMillis

**Returns**  
---  
**Type** | **Description**  
`int` | The total time in milliseconds to spend on the call, including all retry attempts and delays between attempts. If $this->retriesEnabled() is false, this setting is unused - use noRetriesRpcTimeoutMillis to set the timeout in that case.  
  
### getMaxRetries

### getRetryFunction

### static::load

Constructs an array mapping method names to CallSettings.

**Parameters**  
---  
**Name** | **Description**  
`serviceName` |  `string`   
The fully-qualified name of this service, used as a key into the client config file.  
`clientConfig` |  `array`   
An array parsed from the standard API client config file.  
`disableRetries` |  `bool`   
Disable retries in all loaded RetrySettings objects. Defaults to false.  
**Returns**  
---  
**Type** | **Description**  
`array<[RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings)>` | $retrySettings  
  
### static::constructDefault

### static::logicalTimeout

Creates an associative array of the [RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings) timeout fields configured with the given timeout specified in the $timeout parameter interpreted as a logical timeout.

**Parameter**  
---  
**Name** | **Description**  
`timeout` |  `int`   
The timeout in milliseconds to be used as a logical call timeout.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
## Constants 

### DEFAULT_MAX_RETRIES
    
    
    Value: 0

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
