---
url: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.Client.PredictionApiKeyRegistryClient
title: Google Cloud Recommendation Engine V1beta1 Client - Class PredictionApiKeyRegistryClient (0.10.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:37.283380+00:00
---

# Google Cloud Recommendation Engine V1beta1 Client - Class PredictionApiKeyRegistryClient (0.10.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.Client.PredictionApiKeyRegistryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Recommendation Engine V1beta1 Client - Class PredictionApiKeyRegistryClient (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.9.3  0.8.2  0.7.7  0.6.4  0.5.0  0.4.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Recommendation Engine V1beta1 Client class PredictionApiKeyRegistryClient.

Service Description: Service for registering API keys for use with the `predict` method. If you use an API key to request predictions, you must first register the API key.

Otherwise, your prediction request is rejected. If you use OAuth to authenticate your `predict` method call, you do not need to register an API key. You can register up to 20 API keys per project.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Cloud \ RecommendationEngine \ V1beta1 \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\RecommendationEngine\V1beta1\PredictionApiKeyRegistryClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new PredictionApiKeyRegistryClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### createPredictionApiKeyRegistration

Register an API key for use with predict method.

The async variant is [PredictionApiKeyRegistryClient::createPredictionApiKeyRegistrationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.Client.PredictionApiKeyRegistryClient#_Google_Cloud_RecommendationEngine_V1beta1_Client_PredictionApiKeyRegistryClient__createPredictionApiKeyRegistrationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Google\Cloud\RecommendationEngine\V1beta1\CreatePredictionApiKeyRegistrationRequest`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\RecommendationEngine\V1beta1\PredictionApiKeyRegistration](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.PredictionApiKeyRegistration)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\RecommendationEngine\V1beta1\Client\PredictionApiKeyRegistryClient;
    use Google\Cloud\RecommendationEngine\V1beta1\CreatePredictionApiKeyRegistrationRequest;
    use Google\Cloud\RecommendationEngine\V1beta1\PredictionApiKeyRegistration;
    
    /**
     * @param string $formattedParent The parent resource path.
     *                                `projects/&#42;/locations/global/catalogs/default_catalog/eventStores/default_event_store`. Please see
     *                                {@see PredictionApiKeyRegistryClient::eventStoreName()} for help formatting this field.
     */
    function create_prediction_api_key_registration_sample(string $formattedParent): void
    {
        // Create a client.
        $predictionApiKeyRegistryClient = new PredictionApiKeyRegistryClient();
    
        // Prepare the request message.
        $predictionApiKeyRegistration = new PredictionApiKeyRegistration();
        $request = (new CreatePredictionApiKeyRegistrationRequest())
            ->setParent($formattedParent)
            ->setPredictionApiKeyRegistration($predictionApiKeyRegistration);
    
        // Call the API and handle any network failures.
        try {
            /** @var PredictionApiKeyRegistration $response */
            $response = $predictionApiKeyRegistryClient->createPredictionApiKeyRegistration($request);
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
        $formattedParent = PredictionApiKeyRegistryClient::eventStoreName(
            '[PROJECT]',
            '[LOCATION]',
            '[CATALOG]',
            '[EVENT_STORE]'
        );
    
        create_prediction_api_key_registration_sample($formattedParent);
    }
    

### deletePredictionApiKeyRegistration

Unregister an apiKey from using for predict method.

The async variant is [PredictionApiKeyRegistryClient::deletePredictionApiKeyRegistrationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.Client.PredictionApiKeyRegistryClient#_Google_Cloud_RecommendationEngine_V1beta1_Client_PredictionApiKeyRegistryClient__deletePredictionApiKeyRegistrationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Google\Cloud\RecommendationEngine\V1beta1\DeletePredictionApiKeyRegistrationRequest`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\RecommendationEngine\V1beta1\Client\PredictionApiKeyRegistryClient;
    use Google\Cloud\RecommendationEngine\V1beta1\DeletePredictionApiKeyRegistrationRequest;
    
    /**
     * @param string $formattedName The API key to unregister including full resource path.
     *                              `projects/&#42;/locations/global/catalogs/default_catalog/eventStores/default_event_store/predictionApiKeyRegistrations/<YOUR_API_KEY>`
     *                              Please see {@see PredictionApiKeyRegistryClient::predictionApiKeyRegistrationName()} for help formatting this field.
     */
    function delete_prediction_api_key_registration_sample(string $formattedName): void
    {
        // Create a client.
        $predictionApiKeyRegistryClient = new PredictionApiKeyRegistryClient();
    
        // Prepare the request message.
        $request = (new DeletePredictionApiKeyRegistrationRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $predictionApiKeyRegistryClient->deletePredictionApiKeyRegistration($request);
            printf('Call completed successfully.' . PHP_EOL);
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
        $formattedName = PredictionApiKeyRegistryClient::predictionApiKeyRegistrationName(
            '[PROJECT]',
            '[LOCATION]',
            '[CATALOG]',
            '[EVENT_STORE]',
            '[PREDICTION_API_KEY_REGISTRATION]'
        );
    
        delete_prediction_api_key_registration_sample($formattedName);
    }
    

### listPredictionApiKeyRegistrations

List the registered apiKeys for use with predict method.

The async variant is [PredictionApiKeyRegistryClient::listPredictionApiKeyRegistrationsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.Client.PredictionApiKeyRegistryClient#_Google_Cloud_RecommendationEngine_V1beta1_Client_PredictionApiKeyRegistryClient__listPredictionApiKeyRegistrationsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\RecommendationEngine\V1beta1\ListPredictionApiKeyRegistrationsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ListPredictionApiKeyRegistrationsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\RecommendationEngine\V1beta1\Client\PredictionApiKeyRegistryClient;
    use Google\Cloud\RecommendationEngine\V1beta1\ListPredictionApiKeyRegistrationsRequest;
    use Google\Cloud\RecommendationEngine\V1beta1\PredictionApiKeyRegistration;
    
    /**
     * @param string $formattedParent The parent placement resource name such as
     *                                `projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store`
     *                                Please see {@see PredictionApiKeyRegistryClient::eventStoreName()} for help formatting this field.
     */
    function list_prediction_api_key_registrations_sample(string $formattedParent): void
    {
        // Create a client.
        $predictionApiKeyRegistryClient = new PredictionApiKeyRegistryClient();
    
        // Prepare the request message.
        $request = (new ListPredictionApiKeyRegistrationsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $predictionApiKeyRegistryClient->listPredictionApiKeyRegistrations($request);
    
            /** @var PredictionApiKeyRegistration $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
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
        $formattedParent = PredictionApiKeyRegistryClient::eventStoreName(
            '[PROJECT]',
            '[LOCATION]',
            '[CATALOG]',
            '[EVENT_STORE]'
        );
    
        list_prediction_api_key_registrations_sample($formattedParent);
    }
    

### createPredictionApiKeyRegistrationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Google\Cloud\RecommendationEngine\V1beta1\CreatePredictionApiKeyRegistrationRequest`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\RecommendationEngine\V1beta1\PredictionApiKeyRegistration](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.PredictionApiKeyRegistration)>` |   
  
### deletePredictionApiKeyRegistrationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Google\Cloud\RecommendationEngine\V1beta1\DeletePredictionApiKeyRegistrationRequest`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### listPredictionApiKeyRegistrationsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\RecommendationEngine\V1beta1\ListPredictionApiKeyRegistrationsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ListPredictionApiKeyRegistrationsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### static::eventStoreName

Formats a string containing the fully-qualified path to represent a event_store resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`eventStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted event_store resource.  
  
### static::predictionApiKeyRegistrationName

Formats a string containing the fully-qualified path to represent a prediction_api_key_registration resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`eventStore` |  `string`   
  
`predictionApiKeyRegistration` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted prediction_api_key_registration resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * eventStore: projects/{project}/locations/{location}/catalogs/{catalog}/eventStores/{event_store}
  * predictionApiKeyRegistration: projects/{project}/locations/{location}/catalogs/{catalog}/eventStores/{event_store}/predictionApiKeyRegistrations/{prediction_api_key_registration}



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
