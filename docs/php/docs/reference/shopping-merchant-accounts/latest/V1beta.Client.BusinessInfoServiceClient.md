---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Client.BusinessInfoServiceClient
title: Google Shopping Merchant Accounts V1beta Client - Class BusinessInfoServiceClient (1.4.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:08.759748+00:00
---

# Google Shopping Merchant Accounts V1beta Client - Class BusinessInfoServiceClient (1.4.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Client.BusinessInfoServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Accounts V1beta Client - Class BusinessInfoServiceClient (1.4.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.6 (latest)  1.4.1  1.3.1  1.2.2  1.1.0  1.0.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.3  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Accounts V1beta Client class BusinessInfoServiceClient.

Service Description: Service to support business info API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Shopping \ Merchant \ Accounts \ V1beta \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Shopping\Merchant\Accounts\V1beta\BusinessInfoServiceClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new BusinessInfoServiceClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### getBusinessInfo

Retrieves the business info of an account.

The async variant is [BusinessInfoServiceClient::getBusinessInfoAsync()](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Client.BusinessInfoServiceClient#_Google_Shopping_Merchant_Accounts_V1beta_Client_BusinessInfoServiceClient__getBusinessInfoAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Accounts\V1beta\GetBusinessInfoRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.GetBusinessInfoRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Merchant\Accounts\V1beta\BusinessInfo](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.BusinessInfo)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Shopping\Merchant\Accounts\V1beta\BusinessInfo;
    use Google\Shopping\Merchant\Accounts\V1beta\Client\BusinessInfoServiceClient;
    use Google\Shopping\Merchant\Accounts\V1beta\GetBusinessInfoRequest;
    
    /**
     * @param string $formattedName The resource name of the business info.
     *                              Format: `accounts/{account}/businessInfo`
     *                              Please see {@see BusinessInfoServiceClient::businessInfoName()} for help formatting this field.
     */
    function get_business_info_sample(string $formattedName): void
    {
        // Create a client.
        $businessInfoServiceClient = new BusinessInfoServiceClient();
    
        // Prepare the request message.
        $request = (new GetBusinessInfoRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var BusinessInfo $response */
            $response = $businessInfoServiceClient->getBusinessInfo($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedName = BusinessInfoServiceClient::businessInfoName('[ACCOUNT]');
    
        get_business_info_sample($formattedName);
    }
    

### updateBusinessInfo

Updates the business info of an account. Executing this method requires admin access.

The async variant is [BusinessInfoServiceClient::updateBusinessInfoAsync()](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Client.BusinessInfoServiceClient#_Google_Shopping_Merchant_Accounts_V1beta_Client_BusinessInfoServiceClient__updateBusinessInfoAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Accounts\V1beta\UpdateBusinessInfoRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.UpdateBusinessInfoRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Merchant\Accounts\V1beta\BusinessInfo](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.BusinessInfo)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    use Google\Shopping\Merchant\Accounts\V1beta\BusinessInfo;
    use Google\Shopping\Merchant\Accounts\V1beta\Client\BusinessInfoServiceClient;
    use Google\Shopping\Merchant\Accounts\V1beta\UpdateBusinessInfoRequest;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_business_info_sample(): void
    {
        // Create a client.
        $businessInfoServiceClient = new BusinessInfoServiceClient();
    
        // Prepare the request message.
        $businessInfo = new BusinessInfo();
        $updateMask = new FieldMask();
        $request = (new UpdateBusinessInfoRequest())
            ->setBusinessInfo($businessInfo)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var BusinessInfo $response */
            $response = $businessInfoServiceClient->updateBusinessInfo($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### getBusinessInfoAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Accounts\V1beta\GetBusinessInfoRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.GetBusinessInfoRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Shopping\Merchant\Accounts\V1beta\BusinessInfo](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.BusinessInfo)>` |   
  
### updateBusinessInfoAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Accounts\V1beta\UpdateBusinessInfoRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.UpdateBusinessInfoRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Shopping\Merchant\Accounts\V1beta\BusinessInfo](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.BusinessInfo)>` |   
  
### static::businessInfoName

Formats a string containing the fully-qualified path to represent a business_info resource.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted business_info resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * businessInfo: accounts/{account}/businessInfo



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
