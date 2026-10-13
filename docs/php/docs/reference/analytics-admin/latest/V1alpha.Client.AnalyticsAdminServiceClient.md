---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient
title: Google Analytics Admin V1alpha Client - Class AnalyticsAdminServiceClient (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:44.355509+00:00
---

# Google Analytics Admin V1alpha Client - Class AnalyticsAdminServiceClient (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class AnalyticsAdminServiceClient (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class AnalyticsAdminServiceClient.

Service Description: Service Interface for the Google Analytics Admin API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Analytics \ Admin \ V1alpha \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Analytics\Admin\V1alpha\AnalyticsAdminServiceClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new AnalyticsAdminServiceClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### acknowledgeUserDataCollection

Acknowledges the terms of user data collection for the specified property.

This acknowledgement must be completed (either in the Google Analytics UI or through this API) before MeasurementProtocolSecret resources may be created.

The async variant is [AnalyticsAdminServiceClient::acknowledgeUserDataCollectionAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__acknowledgeUserDataCollectionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\AcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AcknowledgeUserDataCollectionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AcknowledgeUserDataCollectionResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AcknowledgeUserDataCollectionRequest;
    use Google\Analytics\Admin\V1alpha\AcknowledgeUserDataCollectionResponse;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedProperty The property for which to acknowledge user data collection. Please see
     *                                  {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $acknowledgement   An acknowledgement that the caller of this method understands the
     *                                  terms of user data collection.
     *
     *                                  This field must contain the exact value:
     *                                  "I acknowledge that I have the necessary privacy disclosures and rights
     *                                  from my end users for the collection and processing of their data,
     *                                  including the association of such data with the visitation information
     *                                  Google Analytics collects from my site and/or app property."
     */
    function acknowledge_user_data_collection_sample(
        string $formattedProperty,
        string $acknowledgement
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new AcknowledgeUserDataCollectionRequest())
            ->setProperty($formattedProperty)
            ->setAcknowledgement($acknowledgement);
    
        // Call the API and handle any network failures.
        try {
            /** @var AcknowledgeUserDataCollectionResponse $response */
            $response = $analyticsAdminServiceClient->acknowledgeUserDataCollection($request);
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
        $formattedProperty = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $acknowledgement = '[ACKNOWLEDGEMENT]';
    
        acknowledge_user_data_collection_sample($formattedProperty, $acknowledgement);
    }
    

### approveDisplayVideo360AdvertiserLinkProposal

Approves a DisplayVideo360AdvertiserLinkProposal.

The DisplayVideo360AdvertiserLinkProposal will be deleted and a new DisplayVideo360AdvertiserLink will be created.

The async variant is [AnalyticsAdminServiceClient::approveDisplayVideo360AdvertiserLinkProposalAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__approveDisplayVideo360AdvertiserLinkProposalAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ApproveDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ApproveDisplayVideo360AdvertiserLinkProposalRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ApproveDisplayVideo360AdvertiserLinkProposalResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ApproveDisplayVideo360AdvertiserLinkProposalResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\ApproveDisplayVideo360AdvertiserLinkProposalRequest;
    use Google\Analytics\Admin\V1alpha\ApproveDisplayVideo360AdvertiserLinkProposalResponse;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DisplayVideo360AdvertiserLinkProposal to approve.
     *                              Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678
     *                              Please see {@see AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName()} for help formatting this field.
     */
    function approve_display_video360_advertiser_link_proposal_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ApproveDisplayVideo360AdvertiserLinkProposalRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var ApproveDisplayVideo360AdvertiserLinkProposalResponse $response */
            $response = $analyticsAdminServiceClient->approveDisplayVideo360AdvertiserLinkProposal($request);
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
        $formattedName = AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName(
            '[PROPERTY]',
            '[DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL]'
        );
    
        approve_display_video360_advertiser_link_proposal_sample($formattedName);
    }
    

### archiveAudience

Archives an Audience on a property.

The async variant is [AnalyticsAdminServiceClient::archiveAudienceAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__archiveAudienceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ArchiveAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ArchiveAudienceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\ArchiveAudienceRequest;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Example format: properties/1234/audiences/5678
     *                              Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function archive_audience_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ArchiveAudienceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->archiveAudience($request);
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
        $formattedName = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        archive_audience_sample($formattedName);
    }
    

### archiveCustomDimension

Archives a CustomDimension on a property.

The async variant is [AnalyticsAdminServiceClient::archiveCustomDimensionAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__archiveCustomDimensionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ArchiveCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ArchiveCustomDimensionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\ArchiveCustomDimensionRequest;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the CustomDimension to archive.
     *                              Example format: properties/1234/customDimensions/5678
     *                              Please see {@see AnalyticsAdminServiceClient::customDimensionName()} for help formatting this field.
     */
    function archive_custom_dimension_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ArchiveCustomDimensionRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->archiveCustomDimension($request);
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
        $formattedName = AnalyticsAdminServiceClient::customDimensionName(
            '[PROPERTY]',
            '[CUSTOM_DIMENSION]'
        );
    
        archive_custom_dimension_sample($formattedName);
    }
    

### archiveCustomMetric

Archives a CustomMetric on a property.

The async variant is [AnalyticsAdminServiceClient::archiveCustomMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__archiveCustomMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ArchiveCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ArchiveCustomMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\ArchiveCustomMetricRequest;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the CustomMetric to archive.
     *                              Example format: properties/1234/customMetrics/5678
     *                              Please see {@see AnalyticsAdminServiceClient::customMetricName()} for help formatting this field.
     */
    function archive_custom_metric_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ArchiveCustomMetricRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->archiveCustomMetric($request);
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
        $formattedName = AnalyticsAdminServiceClient::customMetricName('[PROPERTY]', '[CUSTOM_METRIC]');
    
        archive_custom_metric_sample($formattedName);
    }
    

### batchCreateAccessBindings

Creates information about multiple access bindings to an account or property.

This method is transactional. If any AccessBinding cannot be created, none of the AccessBindings will be created.

The async variant is [AnalyticsAdminServiceClient::batchCreateAccessBindingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__batchCreateAccessBindingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchCreateAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchCreateAccessBindingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\BatchCreateAccessBindingsResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchCreateAccessBindingsResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AccessBinding;
    use Google\Analytics\Admin\V1alpha\BatchCreateAccessBindingsRequest;
    use Google\Analytics\Admin\V1alpha\BatchCreateAccessBindingsResponse;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateAccessBindingRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent         The account or property that owns the access bindings. The parent
     *                                        field in the CreateAccessBindingRequest messages must either be empty or
     *                                        match this field. Formats:
     *                                        - accounts/{account}
     *                                        - properties/{property}
     *                                        Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     * @param string $formattedRequestsParent Formats:
     *                                        - accounts/{account}
     *                                        - properties/{property}
     *                                        Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     */
    function batch_create_access_bindings_sample(
        string $formattedParent,
        string $formattedRequestsParent
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $requestsAccessBinding = new AccessBinding();
        $createAccessBindingRequest = (new CreateAccessBindingRequest())
            ->setParent($formattedRequestsParent)
            ->setAccessBinding($requestsAccessBinding);
        $requests = [$createAccessBindingRequest,];
        $request = (new BatchCreateAccessBindingsRequest())
            ->setParent($formattedParent)
            ->setRequests($requests);
    
        // Call the API and handle any network failures.
        try {
            /** @var BatchCreateAccessBindingsResponse $response */
            $response = $analyticsAdminServiceClient->batchCreateAccessBindings($request);
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
        $formattedParent = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
        $formattedRequestsParent = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
    
        batch_create_access_bindings_sample($formattedParent, $formattedRequestsParent);
    }
    

### batchDeleteAccessBindings

Deletes information about multiple users' links to an account or property.

The async variant is [AnalyticsAdminServiceClient::batchDeleteAccessBindingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__batchDeleteAccessBindingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchDeleteAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchDeleteAccessBindingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\BatchDeleteAccessBindingsRequest;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteAccessBindingRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent       The account or property that owns the access bindings. The parent
     *                                      of all provided values for the 'names' field in DeleteAccessBindingRequest
     *                                      messages must match this field. Formats:
     *                                      - accounts/{account}
     *                                      - properties/{property}
     *                                      Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     * @param string $formattedRequestsName Formats:
     *                                      - accounts/{account}/accessBindings/{accessBinding}
     *                                      - properties/{property}/accessBindings/{accessBinding}
     *                                      Please see {@see AnalyticsAdminServiceClient::accessBindingName()} for help formatting this field.
     */
    function batch_delete_access_bindings_sample(
        string $formattedParent,
        string $formattedRequestsName
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $deleteAccessBindingRequest = (new DeleteAccessBindingRequest())
            ->setName($formattedRequestsName);
        $requests = [$deleteAccessBindingRequest,];
        $request = (new BatchDeleteAccessBindingsRequest())
            ->setParent($formattedParent)
            ->setRequests($requests);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->batchDeleteAccessBindings($request);
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
        $formattedParent = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
        $formattedRequestsName = AnalyticsAdminServiceClient::accessBindingName(
            '[ACCOUNT]',
            '[ACCESS_BINDING]'
        );
    
        batch_delete_access_bindings_sample($formattedParent, $formattedRequestsName);
    }
    

### batchGetAccessBindings

Gets information about multiple access bindings to an account or property.

The async variant is [AnalyticsAdminServiceClient::batchGetAccessBindingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__batchGetAccessBindingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchGetAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchGetAccessBindingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\BatchGetAccessBindingsResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchGetAccessBindingsResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\BatchGetAccessBindingsRequest;
    use Google\Analytics\Admin\V1alpha\BatchGetAccessBindingsResponse;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent       The account or property that owns the access bindings. The parent
     *                                      of all provided values for the 'names' field must match this field.
     *                                      Formats:
     *                                      - accounts/{account}
     *                                      - properties/{property}
     *                                      Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     * @param string $formattedNamesElement The names of the access bindings to retrieve.
     *                                      A maximum of 1000 access bindings can be retrieved in a batch.
     *                                      Formats:
     *                                      - accounts/{account}/accessBindings/{accessBinding}
     *                                      - properties/{property}/accessBindings/{accessBinding}
     *                                      Please see {@see AnalyticsAdminServiceClient::accessBindingName()} for help formatting this field.
     */
    function batch_get_access_bindings_sample(
        string $formattedParent,
        string $formattedNamesElement
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $formattedNames = [$formattedNamesElement,];
        $request = (new BatchGetAccessBindingsRequest())
            ->setParent($formattedParent)
            ->setNames($formattedNames);
    
        // Call the API and handle any network failures.
        try {
            /** @var BatchGetAccessBindingsResponse $response */
            $response = $analyticsAdminServiceClient->batchGetAccessBindings($request);
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
        $formattedParent = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
        $formattedNamesElement = AnalyticsAdminServiceClient::accessBindingName(
            '[ACCOUNT]',
            '[ACCESS_BINDING]'
        );
    
        batch_get_access_bindings_sample($formattedParent, $formattedNamesElement);
    }
    

### batchUpdateAccessBindings

Updates information about multiple access bindings to an account or property.

The async variant is [AnalyticsAdminServiceClient::batchUpdateAccessBindingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__batchUpdateAccessBindingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchUpdateAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchUpdateAccessBindingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\BatchUpdateAccessBindingsResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchUpdateAccessBindingsResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AccessBinding;
    use Google\Analytics\Admin\V1alpha\BatchUpdateAccessBindingsRequest;
    use Google\Analytics\Admin\V1alpha\BatchUpdateAccessBindingsResponse;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\UpdateAccessBindingRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent The account or property that owns the access bindings. The parent
     *                                of all provided AccessBinding in UpdateAccessBindingRequest messages must
     *                                match this field.
     *                                Formats:
     *                                - accounts/{account}
     *                                - properties/{property}
     *                                Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     */
    function batch_update_access_bindings_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $requestsAccessBinding = new AccessBinding();
        $updateAccessBindingRequest = (new UpdateAccessBindingRequest())
            ->setAccessBinding($requestsAccessBinding);
        $requests = [$updateAccessBindingRequest,];
        $request = (new BatchUpdateAccessBindingsRequest())
            ->setParent($formattedParent)
            ->setRequests($requests);
    
        // Call the API and handle any network failures.
        try {
            /** @var BatchUpdateAccessBindingsResponse $response */
            $response = $analyticsAdminServiceClient->batchUpdateAccessBindings($request);
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
        $formattedParent = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
    
        batch_update_access_bindings_sample($formattedParent);
    }
    

### cancelDisplayVideo360AdvertiserLinkProposal

Cancels a DisplayVideo360AdvertiserLinkProposal.

Cancelling can mean either:

  * Declining a proposal initiated from Display & Video 360
  * Withdrawing a proposal initiated from Google Analytics After being cancelled, a proposal will eventually be deleted automatically.



The async variant is [AnalyticsAdminServiceClient::cancelDisplayVideo360AdvertiserLinkProposalAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__cancelDisplayVideo360AdvertiserLinkProposalAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CancelDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CancelDisplayVideo360AdvertiserLinkProposalRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\CancelDisplayVideo360AdvertiserLinkProposalRequest;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DisplayVideo360AdvertiserLinkProposal to cancel.
     *                              Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678
     *                              Please see {@see AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName()} for help formatting this field.
     */
    function cancel_display_video360_advertiser_link_proposal_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new CancelDisplayVideo360AdvertiserLinkProposalRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DisplayVideo360AdvertiserLinkProposal $response */
            $response = $analyticsAdminServiceClient->cancelDisplayVideo360AdvertiserLinkProposal($request);
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
        $formattedName = AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName(
            '[PROPERTY]',
            '[DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL]'
        );
    
        cancel_display_video360_advertiser_link_proposal_sample($formattedName);
    }
    

### createAccessBinding

Creates an access binding on an account or property.

The async variant is [AnalyticsAdminServiceClient::createAccessBindingAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createAccessBindingAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateAccessBindingRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AccessBinding](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessBinding)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AccessBinding;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateAccessBindingRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Formats:
     *                                - accounts/{account}
     *                                - properties/{property}
     *                                Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     */
    function create_access_binding_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $accessBinding = new AccessBinding();
        $request = (new CreateAccessBindingRequest())
            ->setParent($formattedParent)
            ->setAccessBinding($accessBinding);
    
        // Call the API and handle any network failures.
        try {
            /** @var AccessBinding $response */
            $response = $analyticsAdminServiceClient->createAccessBinding($request);
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
        $formattedParent = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
    
        create_access_binding_sample($formattedParent);
    }
    

### createAdSenseLink

Creates an AdSenseLink.

The async variant is [AnalyticsAdminServiceClient::createAdSenseLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createAdSenseLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateAdSenseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateAdSenseLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AdSenseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AdSenseLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AdSenseLink;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateAdSenseLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent The property for which to create an AdSense Link.
     *                                Format: properties/{propertyId}
     *                                Example: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_ad_sense_link_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $adsenseLink = new AdSenseLink();
        $request = (new CreateAdSenseLinkRequest())
            ->setParent($formattedParent)
            ->setAdsenseLink($adsenseLink);
    
        // Call the API and handle any network failures.
        try {
            /** @var AdSenseLink $response */
            $response = $analyticsAdminServiceClient->createAdSenseLink($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_ad_sense_link_sample($formattedParent);
    }
    

### createAudience

Creates an Audience.

The async variant is [AnalyticsAdminServiceClient::createAudienceAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createAudienceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateAudienceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Audience;
    use Google\Analytics\Admin\V1alpha\AudienceFilterClause;
    use Google\Analytics\Admin\V1alpha\AudienceFilterClause\AudienceClauseType;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateAudienceRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent                 Example format: properties/1234
     *                                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $audienceDisplayName             The display name of the Audience.
     * @param string $audienceDescription             The description of the Audience.
     * @param int    $audienceMembershipDurationDays  Immutable. The duration a user should stay in an Audience. It
     *                                                cannot be set to more than 540 days.
     * @param int    $audienceFilterClausesClauseType Specifies whether this is an include or exclude filter clause.
     */
    function create_audience_sample(
        string $formattedParent,
        string $audienceDisplayName,
        string $audienceDescription,
        int $audienceMembershipDurationDays,
        int $audienceFilterClausesClauseType
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $audienceFilterClause = (new AudienceFilterClause())
            ->setClauseType($audienceFilterClausesClauseType);
        $audienceFilterClauses = [$audienceFilterClause,];
        $audience = (new Audience())
            ->setDisplayName($audienceDisplayName)
            ->setDescription($audienceDescription)
            ->setMembershipDurationDays($audienceMembershipDurationDays)
            ->setFilterClauses($audienceFilterClauses);
        $request = (new CreateAudienceRequest())
            ->setParent($formattedParent)
            ->setAudience($audience);
    
        // Call the API and handle any network failures.
        try {
            /** @var Audience $response */
            $response = $analyticsAdminServiceClient->createAudience($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $audienceDisplayName = '[DISPLAY_NAME]';
        $audienceDescription = '[DESCRIPTION]';
        $audienceMembershipDurationDays = 0;
        $audienceFilterClausesClauseType = AudienceClauseType::AUDIENCE_CLAUSE_TYPE_UNSPECIFIED;
    
        create_audience_sample(
            $formattedParent,
            $audienceDisplayName,
            $audienceDescription,
            $audienceMembershipDurationDays,
            $audienceFilterClausesClauseType
        );
    }
    

### createBigQueryLink

Creates a BigQueryLink.

The async variant is [AnalyticsAdminServiceClient::createBigQueryLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createBigQueryLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateBigQueryLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\BigQueryLink;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateBigQueryLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent             Example format: properties/1234
     *                                            Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $bigqueryLinkDatasetLocation Immutable. The geographic location where the created BigQuery
     *                                            dataset should reside. See https://cloud.google.com/bigquery/docs/locations
     *                                            for supported locations.
     */
    function create_big_query_link_sample(
        string $formattedParent,
        string $bigqueryLinkDatasetLocation
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $bigqueryLink = (new BigQueryLink())
            ->setDatasetLocation($bigqueryLinkDatasetLocation);
        $request = (new CreateBigQueryLinkRequest())
            ->setParent($formattedParent)
            ->setBigqueryLink($bigqueryLink);
    
        // Call the API and handle any network failures.
        try {
            /** @var BigQueryLink $response */
            $response = $analyticsAdminServiceClient->createBigQueryLink($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $bigqueryLinkDatasetLocation = '[DATASET_LOCATION]';
    
        create_big_query_link_sample($formattedParent, $bigqueryLinkDatasetLocation);
    }
    

### createCalculatedMetric

Creates a CalculatedMetric.

The async variant is [AnalyticsAdminServiceClient::createCalculatedMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createCalculatedMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateCalculatedMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\CalculatedMetric;
    use Google\Analytics\Admin\V1alpha\CalculatedMetric\MetricUnit;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateCalculatedMetricRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent             Format: properties/{property_id}
     *                                            Example: properties/1234
     *                                            Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $calculatedMetricId          The ID to use for the calculated metric which will become the
     *                                            final component of the calculated metric's resource name.
     *
     *                                            This value should be 1-80 characters and valid characters are
     *                                            /[a-zA-Z0-9_]/, no spaces allowed. calculated_metric_id must be unique
     *                                            between all calculated metrics under a property. The calculated_metric_id
     *                                            is used when referencing this calculated metric from external APIs, for
     *                                            example, "calcMetric:{calculated_metric_id}".
     * @param string $calculatedMetricDisplayName Display name for this calculated metric as shown in the
     *                                            Google Analytics UI. Max length 82 characters.
     * @param int    $calculatedMetricMetricUnit  The type for the calculated metric's value.
     * @param string $calculatedMetricFormula     The calculated metric's definition. Maximum number of unique
     *                                            referenced custom metrics is 5. Formulas supports the following operations:
     *                                            + (addition),  - (subtraction), - (negative),  * (multiplication), /
     *                                            (division), () (parenthesis). Any valid real numbers are acceptable that
     *                                            fit in a Long (64bit integer) or a Double (64 bit floating point number).
     *                                            Example formula:
     *                                            "( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0"
     */
    function create_calculated_metric_sample(
        string $formattedParent,
        string $calculatedMetricId,
        string $calculatedMetricDisplayName,
        int $calculatedMetricMetricUnit,
        string $calculatedMetricFormula
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $calculatedMetric = (new CalculatedMetric())
            ->setDisplayName($calculatedMetricDisplayName)
            ->setMetricUnit($calculatedMetricMetricUnit)
            ->setFormula($calculatedMetricFormula);
        $request = (new CreateCalculatedMetricRequest())
            ->setParent($formattedParent)
            ->setCalculatedMetricId($calculatedMetricId)
            ->setCalculatedMetric($calculatedMetric);
    
        // Call the API and handle any network failures.
        try {
            /** @var CalculatedMetric $response */
            $response = $analyticsAdminServiceClient->createCalculatedMetric($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $calculatedMetricId = '[CALCULATED_METRIC_ID]';
        $calculatedMetricDisplayName = '[DISPLAY_NAME]';
        $calculatedMetricMetricUnit = MetricUnit::METRIC_UNIT_UNSPECIFIED;
        $calculatedMetricFormula = '[FORMULA]';
    
        create_calculated_metric_sample(
            $formattedParent,
            $calculatedMetricId,
            $calculatedMetricDisplayName,
            $calculatedMetricMetricUnit,
            $calculatedMetricFormula
        );
    }
    

### createChannelGroup

Creates a ChannelGroup.

The async variant is [AnalyticsAdminServiceClient::createChannelGroupAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createChannelGroupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateChannelGroupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\ChannelGroup;
    use Google\Analytics\Admin\V1alpha\ChannelGroupFilterExpression;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateChannelGroupRequest;
    use Google\Analytics\Admin\V1alpha\GroupingRule;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent                     The property for which to create a ChannelGroup.
     *                                                    Example format: properties/1234
     *                                                    Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $channelGroupDisplayName             The display name of the Channel Group. Max length of 80
     *                                                    characters.
     * @param string $channelGroupGroupingRuleDisplayName Customer defined display name for the channel.
     */
    function create_channel_group_sample(
        string $formattedParent,
        string $channelGroupDisplayName,
        string $channelGroupGroupingRuleDisplayName
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $channelGroupGroupingRuleExpression = new ChannelGroupFilterExpression();
        $groupingRule = (new GroupingRule())
            ->setDisplayName($channelGroupGroupingRuleDisplayName)
            ->setExpression($channelGroupGroupingRuleExpression);
        $channelGroupGroupingRule = [$groupingRule,];
        $channelGroup = (new ChannelGroup())
            ->setDisplayName($channelGroupDisplayName)
            ->setGroupingRule($channelGroupGroupingRule);
        $request = (new CreateChannelGroupRequest())
            ->setParent($formattedParent)
            ->setChannelGroup($channelGroup);
    
        // Call the API and handle any network failures.
        try {
            /** @var ChannelGroup $response */
            $response = $analyticsAdminServiceClient->createChannelGroup($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $channelGroupDisplayName = '[DISPLAY_NAME]';
        $channelGroupGroupingRuleDisplayName = '[DISPLAY_NAME]';
    
        create_channel_group_sample(
            $formattedParent,
            $channelGroupDisplayName,
            $channelGroupGroupingRuleDisplayName
        );
    }
    

### createConversionEvent

Deprecated: Use `CreateKeyEvent` instead.

Creates a conversion event with the specified attributes.

The async variant is [AnalyticsAdminServiceClient::createConversionEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createConversionEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateConversionEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ConversionEvent;
    use Google\Analytics\Admin\V1alpha\CreateConversionEventRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent The resource name of the parent property where this conversion
     *                                event will be created. Format: properties/123
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_conversion_event_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $conversionEvent = new ConversionEvent();
        $request = (new CreateConversionEventRequest())
            ->setConversionEvent($conversionEvent)
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var ConversionEvent $response */
            $response = $analyticsAdminServiceClient->createConversionEvent($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_conversion_event_sample($formattedParent);
    }
    

### createCustomDimension

Creates a CustomDimension.

The async variant is [AnalyticsAdminServiceClient::createCustomDimensionAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createCustomDimensionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateCustomDimensionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateCustomDimensionRequest;
    use Google\Analytics\Admin\V1alpha\CustomDimension;
    use Google\Analytics\Admin\V1alpha\CustomDimension\DimensionScope;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent              Example format: properties/1234
     *                                             Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $customDimensionParameterName Immutable. Tagging parameter name for this custom dimension.
     *
     *                                             If this is a user-scoped dimension, then this is the user property name.
     *                                             If this is an event-scoped dimension, then this is the event parameter
     *                                             name.
     *
     *                                             If this is an item-scoped dimension, then this is the parameter
     *                                             name found in the eCommerce items array.
     *
     *                                             May only contain alphanumeric and underscore characters, starting with a
     *                                             letter. Max length of 24 characters for user-scoped dimensions, 40
     *                                             characters for event-scoped dimensions.
     * @param string $customDimensionDisplayName   Display name for this custom dimension as shown in the Analytics
     *                                             UI. Max length of 82 characters, alphanumeric plus space and underscore
     *                                             starting with a letter. Legacy system-generated display names may contain
     *                                             square brackets, but updates to this field will never permit square
     *                                             brackets.
     * @param int    $customDimensionScope         Immutable. The scope of this dimension.
     */
    function create_custom_dimension_sample(
        string $formattedParent,
        string $customDimensionParameterName,
        string $customDimensionDisplayName,
        int $customDimensionScope
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $customDimension = (new CustomDimension())
            ->setParameterName($customDimensionParameterName)
            ->setDisplayName($customDimensionDisplayName)
            ->setScope($customDimensionScope);
        $request = (new CreateCustomDimensionRequest())
            ->setParent($formattedParent)
            ->setCustomDimension($customDimension);
    
        // Call the API and handle any network failures.
        try {
            /** @var CustomDimension $response */
            $response = $analyticsAdminServiceClient->createCustomDimension($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $customDimensionParameterName = '[PARAMETER_NAME]';
        $customDimensionDisplayName = '[DISPLAY_NAME]';
        $customDimensionScope = DimensionScope::DIMENSION_SCOPE_UNSPECIFIED;
    
        create_custom_dimension_sample(
            $formattedParent,
            $customDimensionParameterName,
            $customDimensionDisplayName,
            $customDimensionScope
        );
    }
    

### createCustomMetric

Creates a CustomMetric.

The async variant is [AnalyticsAdminServiceClient::createCustomMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createCustomMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateCustomMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateCustomMetricRequest;
    use Google\Analytics\Admin\V1alpha\CustomMetric;
    use Google\Analytics\Admin\V1alpha\CustomMetric\MeasurementUnit;
    use Google\Analytics\Admin\V1alpha\CustomMetric\MetricScope;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent             Example format: properties/1234
     *                                            Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $customMetricParameterName   Immutable. Tagging name for this custom metric.
     *
     *                                            If this is an event-scoped metric, then this is the event parameter
     *                                            name.
     *
     *                                            May only contain alphanumeric and underscore charactes, starting with a
     *                                            letter. Max length of 40 characters for event-scoped metrics.
     * @param string $customMetricDisplayName     Display name for this custom metric as shown in the Analytics UI.
     *                                            Max length of 82 characters, alphanumeric plus space and underscore
     *                                            starting with a letter. Legacy system-generated display names may contain
     *                                            square brackets, but updates to this field will never permit square
     *                                            brackets.
     * @param int    $customMetricMeasurementUnit The type for the custom metric's value.
     * @param int    $customMetricScope           Immutable. The scope of this custom metric.
     */
    function create_custom_metric_sample(
        string $formattedParent,
        string $customMetricParameterName,
        string $customMetricDisplayName,
        int $customMetricMeasurementUnit,
        int $customMetricScope
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $customMetric = (new CustomMetric())
            ->setParameterName($customMetricParameterName)
            ->setDisplayName($customMetricDisplayName)
            ->setMeasurementUnit($customMetricMeasurementUnit)
            ->setScope($customMetricScope);
        $request = (new CreateCustomMetricRequest())
            ->setParent($formattedParent)
            ->setCustomMetric($customMetric);
    
        // Call the API and handle any network failures.
        try {
            /** @var CustomMetric $response */
            $response = $analyticsAdminServiceClient->createCustomMetric($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $customMetricParameterName = '[PARAMETER_NAME]';
        $customMetricDisplayName = '[DISPLAY_NAME]';
        $customMetricMeasurementUnit = MeasurementUnit::MEASUREMENT_UNIT_UNSPECIFIED;
        $customMetricScope = MetricScope::METRIC_SCOPE_UNSPECIFIED;
    
        create_custom_metric_sample(
            $formattedParent,
            $customMetricParameterName,
            $customMetricDisplayName,
            $customMetricMeasurementUnit,
            $customMetricScope
        );
    }
    

### createDataStream

Creates a DataStream.

The async variant is [AnalyticsAdminServiceClient::createDataStreamAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createDataStreamAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateDataStreamRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateDataStreamRequest;
    use Google\Analytics\Admin\V1alpha\DataStream;
    use Google\Analytics\Admin\V1alpha\DataStream\DataStreamType;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param int    $dataStreamType  Immutable. The type of this DataStream resource.
     */
    function create_data_stream_sample(string $formattedParent, int $dataStreamType): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $dataStream = (new DataStream())
            ->setType($dataStreamType);
        $request = (new CreateDataStreamRequest())
            ->setParent($formattedParent)
            ->setDataStream($dataStream);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataStream $response */
            $response = $analyticsAdminServiceClient->createDataStream($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $dataStreamType = DataStreamType::DATA_STREAM_TYPE_UNSPECIFIED;
    
        create_data_stream_sample($formattedParent, $dataStreamType);
    }
    

### createDisplayVideo360AdvertiserLink

Creates a DisplayVideo360AdvertiserLink.

This can only be utilized by users who have proper authorization both on the Google Analytics property and on the Display & Video 360 advertiser. Users who do not have access to the Display & Video 360 advertiser should instead seek to create a DisplayVideo360LinkProposal.

The async variant is [AnalyticsAdminServiceClient::createDisplayVideo360AdvertiserLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createDisplayVideo360AdvertiserLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateDisplayVideo360AdvertiserLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateDisplayVideo360AdvertiserLinkRequest;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_display_video360_advertiser_link_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $displayVideo360AdvertiserLink = new DisplayVideo360AdvertiserLink();
        $request = (new CreateDisplayVideo360AdvertiserLinkRequest())
            ->setParent($formattedParent)
            ->setDisplayVideo360AdvertiserLink($displayVideo360AdvertiserLink);
    
        // Call the API and handle any network failures.
        try {
            /** @var DisplayVideo360AdvertiserLink $response */
            $response = $analyticsAdminServiceClient->createDisplayVideo360AdvertiserLink($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_display_video360_advertiser_link_sample($formattedParent);
    }
    

### createDisplayVideo360AdvertiserLinkProposal

Creates a DisplayVideo360AdvertiserLinkProposal.

The async variant is [AnalyticsAdminServiceClient::createDisplayVideo360AdvertiserLinkProposalAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createDisplayVideo360AdvertiserLinkProposalAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateDisplayVideo360AdvertiserLinkProposalRequest;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_display_video360_advertiser_link_proposal_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $displayVideo360AdvertiserLinkProposal = new DisplayVideo360AdvertiserLinkProposal();
        $request = (new CreateDisplayVideo360AdvertiserLinkProposalRequest())
            ->setParent($formattedParent)
            ->setDisplayVideo360AdvertiserLinkProposal($displayVideo360AdvertiserLinkProposal);
    
        // Call the API and handle any network failures.
        try {
            /** @var DisplayVideo360AdvertiserLinkProposal $response */
            $response = $analyticsAdminServiceClient->createDisplayVideo360AdvertiserLinkProposal($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_display_video360_advertiser_link_proposal_sample($formattedParent);
    }
    

### createEventCreateRule

Creates an EventCreateRule.

The async variant is [AnalyticsAdminServiceClient::createEventCreateRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createEventCreateRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateEventCreateRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateEventCreateRuleRequest;
    use Google\Analytics\Admin\V1alpha\EventCreateRule;
    use Google\Analytics\Admin\V1alpha\MatchingCondition;
    use Google\Analytics\Admin\V1alpha\MatchingCondition\ComparisonType;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent                              Example format: properties/123/dataStreams/456
     *                                                             Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     * @param string $eventCreateRuleDestinationEvent              The name of the new event to be created.
     *
     *                                                             This value must:
     *                                                             * be less than 40 characters
     *                                                             * consist only of letters, digits or _ (underscores)
     *                                                             * start with a letter
     * @param string $eventCreateRuleEventConditionsField          The name of the field that is compared against for the condition.
     *                                                             If 'event_name' is specified this condition will apply to the name of the
     *                                                             event.  Otherwise the condition will apply to a parameter with the
     *                                                             specified name.
     *
     *                                                             This value cannot contain spaces.
     * @param int    $eventCreateRuleEventConditionsComparisonType The type of comparison to be applied to the value.
     * @param string $eventCreateRuleEventConditionsValue          The value being compared against for this condition.  The runtime
     *                                                             implementation may perform type coercion of this value to evaluate this
     *                                                             condition based on the type of the parameter value.
     */
    function create_event_create_rule_sample(
        string $formattedParent,
        string $eventCreateRuleDestinationEvent,
        string $eventCreateRuleEventConditionsField,
        int $eventCreateRuleEventConditionsComparisonType,
        string $eventCreateRuleEventConditionsValue
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $matchingCondition = (new MatchingCondition())
            ->setField($eventCreateRuleEventConditionsField)
            ->setComparisonType($eventCreateRuleEventConditionsComparisonType)
            ->setValue($eventCreateRuleEventConditionsValue);
        $eventCreateRuleEventConditions = [$matchingCondition,];
        $eventCreateRule = (new EventCreateRule())
            ->setDestinationEvent($eventCreateRuleDestinationEvent)
            ->setEventConditions($eventCreateRuleEventConditions);
        $request = (new CreateEventCreateRuleRequest())
            ->setParent($formattedParent)
            ->setEventCreateRule($eventCreateRule);
    
        // Call the API and handle any network failures.
        try {
            /** @var EventCreateRule $response */
            $response = $analyticsAdminServiceClient->createEventCreateRule($request);
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
        $eventCreateRuleDestinationEvent = '[DESTINATION_EVENT]';
        $eventCreateRuleEventConditionsField = '[FIELD]';
        $eventCreateRuleEventConditionsComparisonType = ComparisonType::COMPARISON_TYPE_UNSPECIFIED;
        $eventCreateRuleEventConditionsValue = '[VALUE]';
    
        create_event_create_rule_sample(
            $formattedParent,
            $eventCreateRuleDestinationEvent,
            $eventCreateRuleEventConditionsField,
            $eventCreateRuleEventConditionsComparisonType,
            $eventCreateRuleEventConditionsValue
        );
    }
    

### createEventEditRule

Creates an EventEditRule.

The async variant is [AnalyticsAdminServiceClient::createEventEditRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createEventEditRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateEventEditRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EventEditRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateEventEditRuleRequest;
    use Google\Analytics\Admin\V1alpha\EventEditRule;
    use Google\Analytics\Admin\V1alpha\MatchingCondition;
    use Google\Analytics\Admin\V1alpha\MatchingCondition\ComparisonType;
    use Google\Analytics\Admin\V1alpha\ParameterMutation;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent                               Example format: properties/123/dataStreams/456
     *                                                              Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     * @param string $eventEditRuleDisplayName                      The display name of this event edit rule. Maximum of 255
     *                                                              characters.
     * @param string $eventEditRuleEventConditionsField             The name of the field that is compared against for the condition.
     *                                                              If 'event_name' is specified this condition will apply to the name of the
     *                                                              event.  Otherwise the condition will apply to a parameter with the
     *                                                              specified name.
     *
     *                                                              This value cannot contain spaces.
     * @param int    $eventEditRuleEventConditionsComparisonType    The type of comparison to be applied to the value.
     * @param string $eventEditRuleEventConditionsValue             The value being compared against for this condition.  The runtime
     *                                                              implementation may perform type coercion of this value to evaluate this
     *                                                              condition based on the type of the parameter value.
     * @param string $eventEditRuleParameterMutationsParameter      The name of the parameter to mutate.
     *                                                              This value must:
     *                                                              * be less than 40 characters.
     *                                                              * be unique across across all mutations within the rule
     *                                                              * consist only of letters, digits or _ (underscores)
     *                                                              For event edit rules, the name may also be set to 'event_name' to modify
     *                                                              the event_name in place.
     * @param string $eventEditRuleParameterMutationsParameterValue The value mutation to perform.
     *                                                              * Must be less than 100 characters.
     *                                                              * To specify a constant value for the param, use the value's string.
     *                                                              * To copy value from another parameter, use syntax like
     *                                                              "[[other_parameter]]" For more details, see this [help center
     *                                                              article](https://support.google.com/analytics/answer/10085872#modify-an-event&zippy=%2Cin-this-article%2Cmodify-parameters).
     */
    function create_event_edit_rule_sample(
        string $formattedParent,
        string $eventEditRuleDisplayName,
        string $eventEditRuleEventConditionsField,
        int $eventEditRuleEventConditionsComparisonType,
        string $eventEditRuleEventConditionsValue,
        string $eventEditRuleParameterMutationsParameter,
        string $eventEditRuleParameterMutationsParameterValue
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $matchingCondition = (new MatchingCondition())
            ->setField($eventEditRuleEventConditionsField)
            ->setComparisonType($eventEditRuleEventConditionsComparisonType)
            ->setValue($eventEditRuleEventConditionsValue);
        $eventEditRuleEventConditions = [$matchingCondition,];
        $parameterMutation = (new ParameterMutation())
            ->setParameter($eventEditRuleParameterMutationsParameter)
            ->setParameterValue($eventEditRuleParameterMutationsParameterValue);
        $eventEditRuleParameterMutations = [$parameterMutation,];
        $eventEditRule = (new EventEditRule())
            ->setDisplayName($eventEditRuleDisplayName)
            ->setEventConditions($eventEditRuleEventConditions)
            ->setParameterMutations($eventEditRuleParameterMutations);
        $request = (new CreateEventEditRuleRequest())
            ->setParent($formattedParent)
            ->setEventEditRule($eventEditRule);
    
        // Call the API and handle any network failures.
        try {
            /** @var EventEditRule $response */
            $response = $analyticsAdminServiceClient->createEventEditRule($request);
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
        $eventEditRuleDisplayName = '[DISPLAY_NAME]';
        $eventEditRuleEventConditionsField = '[FIELD]';
        $eventEditRuleEventConditionsComparisonType = ComparisonType::COMPARISON_TYPE_UNSPECIFIED;
        $eventEditRuleEventConditionsValue = '[VALUE]';
        $eventEditRuleParameterMutationsParameter = '[PARAMETER]';
        $eventEditRuleParameterMutationsParameterValue = '[PARAMETER_VALUE]';
    
        create_event_edit_rule_sample(
            $formattedParent,
            $eventEditRuleDisplayName,
            $eventEditRuleEventConditionsField,
            $eventEditRuleEventConditionsComparisonType,
            $eventEditRuleEventConditionsValue,
            $eventEditRuleParameterMutationsParameter,
            $eventEditRuleParameterMutationsParameterValue
        );
    }
    

### createExpandedDataSet

Creates a ExpandedDataSet.

The async variant is [AnalyticsAdminServiceClient::createExpandedDataSetAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createExpandedDataSetAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateExpandedDataSetRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateExpandedDataSetRequest;
    use Google\Analytics\Admin\V1alpha\ExpandedDataSet;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent            Example format: properties/1234
     *                                           Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $expandedDataSetDisplayName The display name of the ExpandedDataSet.
     *                                           Max 200 chars.
     */
    function create_expanded_data_set_sample(
        string $formattedParent,
        string $expandedDataSetDisplayName
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $expandedDataSet = (new ExpandedDataSet())
            ->setDisplayName($expandedDataSetDisplayName);
        $request = (new CreateExpandedDataSetRequest())
            ->setParent($formattedParent)
            ->setExpandedDataSet($expandedDataSet);
    
        // Call the API and handle any network failures.
        try {
            /** @var ExpandedDataSet $response */
            $response = $analyticsAdminServiceClient->createExpandedDataSet($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $expandedDataSetDisplayName = '[DISPLAY_NAME]';
    
        create_expanded_data_set_sample($formattedParent, $expandedDataSetDisplayName);
    }
    

### createFirebaseLink

Creates a FirebaseLink.

Properties can have at most one FirebaseLink.

The async variant is [AnalyticsAdminServiceClient::createFirebaseLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createFirebaseLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateFirebaseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateFirebaseLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\FirebaseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.FirebaseLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateFirebaseLinkRequest;
    use Google\Analytics\Admin\V1alpha\FirebaseLink;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Format: properties/{property_id}
     *
     *                                Example: `properties/1234`
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_firebase_link_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $firebaseLink = new FirebaseLink();
        $request = (new CreateFirebaseLinkRequest())
            ->setParent($formattedParent)
            ->setFirebaseLink($firebaseLink);
    
        // Call the API and handle any network failures.
        try {
            /** @var FirebaseLink $response */
            $response = $analyticsAdminServiceClient->createFirebaseLink($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_firebase_link_sample($formattedParent);
    }
    

### createGoogleAdsLink

Creates a GoogleAdsLink.

The async variant is [AnalyticsAdminServiceClient::createGoogleAdsLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createGoogleAdsLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateGoogleAdsLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateGoogleAdsLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateGoogleAdsLinkRequest;
    use Google\Analytics\Admin\V1alpha\GoogleAdsLink;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_google_ads_link_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $googleAdsLink = new GoogleAdsLink();
        $request = (new CreateGoogleAdsLinkRequest())
            ->setParent($formattedParent)
            ->setGoogleAdsLink($googleAdsLink);
    
        // Call the API and handle any network failures.
        try {
            /** @var GoogleAdsLink $response */
            $response = $analyticsAdminServiceClient->createGoogleAdsLink($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_google_ads_link_sample($formattedParent);
    }
    

### createKeyEvent

Creates a Key Event.

The async variant is [AnalyticsAdminServiceClient::createKeyEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createKeyEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateKeyEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateKeyEventRequest;
    use Google\Analytics\Admin\V1alpha\KeyEvent;
    use Google\Analytics\Admin\V1alpha\KeyEvent\CountingMethod;
    use Google\ApiCore\ApiException;
    
    /**
     * @param int    $keyEventCountingMethod The method by which Key Events will be counted across multiple
     *                                       events within a session.
     * @param string $formattedParent        The resource name of the parent property where this Key Event
     *                                       will be created. Format: properties/123
     *                                       Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_key_event_sample(int $keyEventCountingMethod, string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $keyEvent = (new KeyEvent())
            ->setCountingMethod($keyEventCountingMethod);
        $request = (new CreateKeyEventRequest())
            ->setKeyEvent($keyEvent)
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var KeyEvent $response */
            $response = $analyticsAdminServiceClient->createKeyEvent($request);
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
        $keyEventCountingMethod = CountingMethod::COUNTING_METHOD_UNSPECIFIED;
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_key_event_sample($keyEventCountingMethod, $formattedParent);
    }
    

### createMeasurementProtocolSecret

Creates a measurement protocol secret.

The async variant is [AnalyticsAdminServiceClient::createMeasurementProtocolSecretAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createMeasurementProtocolSecretAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateMeasurementProtocolSecretRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateMeasurementProtocolSecretRequest;
    use Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent                      The parent resource where this secret will be created.
     *                                                     Format: properties/{property}/dataStreams/{dataStream}
     *                                                     Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     * @param string $measurementProtocolSecretDisplayName Human-readable display name for this secret.
     */
    function create_measurement_protocol_secret_sample(
        string $formattedParent,
        string $measurementProtocolSecretDisplayName
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $measurementProtocolSecret = (new MeasurementProtocolSecret())
            ->setDisplayName($measurementProtocolSecretDisplayName);
        $request = (new CreateMeasurementProtocolSecretRequest())
            ->setParent($formattedParent)
            ->setMeasurementProtocolSecret($measurementProtocolSecret);
    
        // Call the API and handle any network failures.
        try {
            /** @var MeasurementProtocolSecret $response */
            $response = $analyticsAdminServiceClient->createMeasurementProtocolSecret($request);
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
        $measurementProtocolSecretDisplayName = '[DISPLAY_NAME]';
    
        create_measurement_protocol_secret_sample($formattedParent, $measurementProtocolSecretDisplayName);
    }
    

### createProperty

Creates a Google Analytics property with the specified location and attributes.

The async variant is [AnalyticsAdminServiceClient::createPropertyAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createPropertyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreatePropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreatePropertyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreatePropertyRequest;
    use Google\Analytics\Admin\V1alpha\Property;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $propertyDisplayName Human-readable display name for this property.
     *
     *                                    The max allowed display name length is 100 UTF-16 code units.
     * @param string $propertyTimeZone    Reporting Time Zone, used as the day boundary for reports,
     *                                    regardless of where the data originates. If the time zone honors DST,
     *                                    Analytics will automatically adjust for the changes.
     *
     *                                    NOTE: Changing the time zone only affects data going forward, and is not
     *                                    applied retroactively.
     *
     *                                    Format: https://www.iana.org/time-zones
     *                                    Example: "America/Los_Angeles"
     */
    function create_property_sample(string $propertyDisplayName, string $propertyTimeZone): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $property = (new Property())
            ->setDisplayName($propertyDisplayName)
            ->setTimeZone($propertyTimeZone);
        $request = (new CreatePropertyRequest())
            ->setProperty($property);
    
        // Call the API and handle any network failures.
        try {
            /** @var Property $response */
            $response = $analyticsAdminServiceClient->createProperty($request);
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
        $propertyDisplayName = '[DISPLAY_NAME]';
        $propertyTimeZone = '[TIME_ZONE]';
    
        create_property_sample($propertyDisplayName, $propertyTimeZone);
    }
    

### createReportingDataAnnotation

Creates a Reporting Data Annotation.

The async variant is [AnalyticsAdminServiceClient::createReportingDataAnnotationAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createReportingDataAnnotationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateReportingDataAnnotationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateReportingDataAnnotationRequest;
    use Google\Analytics\Admin\V1alpha\ReportingDataAnnotation;
    use Google\Analytics\Admin\V1alpha\ReportingDataAnnotation\Color;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent              The property for which to create a Reporting Data Annotation.
     *                                             Format: properties/property_id
     *                                             Example: properties/123
     *                                             Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param string $reportingDataAnnotationName  Identifier. Resource name of this Reporting Data Annotation.
     *                                             Format:
     *                                             'properties/{property_id}/reportingDataAnnotations/{reporting_data_annotation}'
     *                                             Format: 'properties/123/reportingDataAnnotations/456'
     * @param string $reportingDataAnnotationTitle Human-readable title for this Reporting Data Annotation.
     * @param int    $reportingDataAnnotationColor The color used for display of this Reporting Data Annotation.
     */
    function create_reporting_data_annotation_sample(
        string $formattedParent,
        string $reportingDataAnnotationName,
        string $reportingDataAnnotationTitle,
        int $reportingDataAnnotationColor
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $reportingDataAnnotation = (new ReportingDataAnnotation())
            ->setName($reportingDataAnnotationName)
            ->setTitle($reportingDataAnnotationTitle)
            ->setColor($reportingDataAnnotationColor);
        $request = (new CreateReportingDataAnnotationRequest())
            ->setParent($formattedParent)
            ->setReportingDataAnnotation($reportingDataAnnotation);
    
        // Call the API and handle any network failures.
        try {
            /** @var ReportingDataAnnotation $response */
            $response = $analyticsAdminServiceClient->createReportingDataAnnotation($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $reportingDataAnnotationName = '[NAME]';
        $reportingDataAnnotationTitle = '[TITLE]';
        $reportingDataAnnotationColor = Color::COLOR_UNSPECIFIED;
    
        create_reporting_data_annotation_sample(
            $formattedParent,
            $reportingDataAnnotationName,
            $reportingDataAnnotationTitle,
            $reportingDataAnnotationColor
        );
    }
    

### createRollupProperty

Create a roll-up property and all roll-up property source links.

The async variant is [AnalyticsAdminServiceClient::createRollupPropertyAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createRollupPropertyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateRollupPropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateRollupPropertyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CreateRollupPropertyResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateRollupPropertyResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateRollupPropertyRequest;
    use Google\Analytics\Admin\V1alpha\CreateRollupPropertyResponse;
    use Google\Analytics\Admin\V1alpha\Property;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $rollupPropertyDisplayName Human-readable display name for this property.
     *
     *                                          The max allowed display name length is 100 UTF-16 code units.
     * @param string $rollupPropertyTimeZone    Reporting Time Zone, used as the day boundary for reports,
     *                                          regardless of where the data originates. If the time zone honors DST,
     *                                          Analytics will automatically adjust for the changes.
     *
     *                                          NOTE: Changing the time zone only affects data going forward, and is not
     *                                          applied retroactively.
     *
     *                                          Format: https://www.iana.org/time-zones
     *                                          Example: "America/Los_Angeles"
     */
    function create_rollup_property_sample(
        string $rollupPropertyDisplayName,
        string $rollupPropertyTimeZone
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $rollupProperty = (new Property())
            ->setDisplayName($rollupPropertyDisplayName)
            ->setTimeZone($rollupPropertyTimeZone);
        $request = (new CreateRollupPropertyRequest())
            ->setRollupProperty($rollupProperty);
    
        // Call the API and handle any network failures.
        try {
            /** @var CreateRollupPropertyResponse $response */
            $response = $analyticsAdminServiceClient->createRollupProperty($request);
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
        $rollupPropertyDisplayName = '[DISPLAY_NAME]';
        $rollupPropertyTimeZone = '[TIME_ZONE]';
    
        create_rollup_property_sample($rollupPropertyDisplayName, $rollupPropertyTimeZone);
    }
    

### createRollupPropertySourceLink

Creates a roll-up property source link.

Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

The async variant is [AnalyticsAdminServiceClient::createRollupPropertySourceLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createRollupPropertySourceLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateRollupPropertySourceLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateRollupPropertySourceLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\RollupPropertySourceLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RollupPropertySourceLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateRollupPropertySourceLinkRequest;
    use Google\Analytics\Admin\V1alpha\RollupPropertySourceLink;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Format: properties/{property_id}
     *                                Example: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_rollup_property_source_link_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $rollupPropertySourceLink = new RollupPropertySourceLink();
        $request = (new CreateRollupPropertySourceLinkRequest())
            ->setParent($formattedParent)
            ->setRollupPropertySourceLink($rollupPropertySourceLink);
    
        // Call the API and handle any network failures.
        try {
            /** @var RollupPropertySourceLink $response */
            $response = $analyticsAdminServiceClient->createRollupPropertySourceLink($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_rollup_property_source_link_sample($formattedParent);
    }
    

### createSKAdNetworkConversionValueSchema

Creates a SKAdNetworkConversionValueSchema.

The async variant is [AnalyticsAdminServiceClient::createSKAdNetworkConversionValueSchemaAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createSKAdNetworkConversionValueSchemaAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSKAdNetworkConversionValueSchemaRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateSKAdNetworkConversionValueSchemaRequest;
    use Google\Analytics\Admin\V1alpha\PostbackWindow;
    use Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent The parent resource where this schema will be created.
     *                                Format: properties/{property}/dataStreams/{dataStream}
     *                                Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     */
    function create_sk_ad_network_conversion_value_schema_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $skadnetworkConversionValueSchemaPostbackWindowOne = new PostbackWindow();
        $skadnetworkConversionValueSchema = (new SKAdNetworkConversionValueSchema())
            ->setPostbackWindowOne($skadnetworkConversionValueSchemaPostbackWindowOne);
        $request = (new CreateSKAdNetworkConversionValueSchemaRequest())
            ->setParent($formattedParent)
            ->setSkadnetworkConversionValueSchema($skadnetworkConversionValueSchema);
    
        // Call the API and handle any network failures.
        try {
            /** @var SKAdNetworkConversionValueSchema $response */
            $response = $analyticsAdminServiceClient->createSKAdNetworkConversionValueSchema($request);
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
    
        create_sk_ad_network_conversion_value_schema_sample($formattedParent);
    }
    

### createSearchAds360Link

Creates a SearchAds360Link.

The async variant is [AnalyticsAdminServiceClient::createSearchAds360LinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createSearchAds360LinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSearchAds360LinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateSearchAds360LinkRequest;
    use Google\Analytics\Admin\V1alpha\SearchAds360Link;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function create_search_ads360_link_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $searchAds360Link = new SearchAds360Link();
        $request = (new CreateSearchAds360LinkRequest())
            ->setParent($formattedParent)
            ->setSearchAds360Link($searchAds360Link);
    
        // Call the API and handle any network failures.
        try {
            /** @var SearchAds360Link $response */
            $response = $analyticsAdminServiceClient->createSearchAds360Link($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        create_search_ads360_link_sample($formattedParent);
    }
    

### createSubpropertyEventFilter

Creates a subproperty Event Filter.

The async variant is [AnalyticsAdminServiceClient::createSubpropertyEventFilterAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__createSubpropertyEventFilterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSubpropertyEventFilterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SubpropertyEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertyEventFilter)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CreateSubpropertyEventFilterRequest;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilter;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilterClause;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilterClause\FilterClauseType;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilterExpression;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent                                     The ordinary property for which to create a subproperty event
     *                                                                    filter. Format: properties/property_id Example: properties/123
     *                                                                    Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     * @param int    $subpropertyEventFilterFilterClausesFilterClauseType The type for the filter clause.
     */
    function create_subproperty_event_filter_sample(
        string $formattedParent,
        int $subpropertyEventFilterFilterClausesFilterClauseType
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $subpropertyEventFilterFilterClausesFilterExpression = new SubpropertyEventFilterExpression();
        $subpropertyEventFilterClause = (new SubpropertyEventFilterClause())
            ->setFilterClauseType($subpropertyEventFilterFilterClausesFilterClauseType)
            ->setFilterExpression($subpropertyEventFilterFilterClausesFilterExpression);
        $subpropertyEventFilterFilterClauses = [$subpropertyEventFilterClause,];
        $subpropertyEventFilter = (new SubpropertyEventFilter())
            ->setFilterClauses($subpropertyEventFilterFilterClauses);
        $request = (new CreateSubpropertyEventFilterRequest())
            ->setParent($formattedParent)
            ->setSubpropertyEventFilter($subpropertyEventFilter);
    
        // Call the API and handle any network failures.
        try {
            /** @var SubpropertyEventFilter $response */
            $response = $analyticsAdminServiceClient->createSubpropertyEventFilter($request);
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
        $subpropertyEventFilterFilterClausesFilterClauseType = FilterClauseType::FILTER_CLAUSE_TYPE_UNSPECIFIED;
    
        create_subproperty_event_filter_sample(
            $formattedParent,
            $subpropertyEventFilterFilterClausesFilterClauseType
        );
    }
    

### deleteAccessBinding

Deletes an access binding on an account or property.

The async variant is [AnalyticsAdminServiceClient::deleteAccessBindingAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteAccessBindingAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteAccessBindingRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteAccessBindingRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Formats:
     *                              - accounts/{account}/accessBindings/{accessBinding}
     *                              - properties/{property}/accessBindings/{accessBinding}
     *                              Please see {@see AnalyticsAdminServiceClient::accessBindingName()} for help formatting this field.
     */
    function delete_access_binding_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteAccessBindingRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteAccessBinding($request);
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
        $formattedName = AnalyticsAdminServiceClient::accessBindingName('[ACCOUNT]', '[ACCESS_BINDING]');
    
        delete_access_binding_sample($formattedName);
    }
    

### deleteAccount

Marks target Account as soft-deleted (ie: "trashed") and returns it.

This API does not have a method to restore soft-deleted accounts. However, they can be restored using the Trash Can UI.

If the accounts are not restored before the expiration time, the account and all child resources (eg: Properties, GoogleAdsLinks, Streams, AccessBindings) will be permanently purged. <https://support.google.com/analytics/answer/6154772>

Returns an error if the target is not found.

The async variant is [AnalyticsAdminServiceClient::deleteAccountAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteAccountAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteAccountRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteAccountRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteAccountRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the Account to soft-delete.
     *                              Format: accounts/{account}
     *                              Example: "accounts/100"
     *                              Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     */
    function delete_account_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteAccountRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteAccount($request);
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
        $formattedName = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
    
        delete_account_sample($formattedName);
    }
    

### deleteAdSenseLink

Deletes an AdSenseLink.

The async variant is [AnalyticsAdminServiceClient::deleteAdSenseLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteAdSenseLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteAdSenseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteAdSenseLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteAdSenseLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Unique identifier for the AdSense Link to be deleted.
     *                              Format: properties/{propertyId}/adSenseLinks/{linkId}
     *                              Example: properties/1234/adSenseLinks/5678
     *                              Please see {@see AnalyticsAdminServiceClient::adSenseLinkName()} for help formatting this field.
     */
    function delete_ad_sense_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteAdSenseLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteAdSenseLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::adSenseLinkName('[PROPERTY]', '[ADSENSE_LINK]');
    
        delete_ad_sense_link_sample($formattedName);
    }
    

### deleteBigQueryLink

Deletes a BigQueryLink on a property.

The async variant is [AnalyticsAdminServiceClient::deleteBigQueryLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteBigQueryLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteBigQueryLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteBigQueryLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The BigQueryLink to delete.
     *                              Example format: properties/1234/bigQueryLinks/5678
     *                              Please see {@see AnalyticsAdminServiceClient::bigQueryLinkName()} for help formatting this field.
     */
    function delete_big_query_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteBigQueryLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteBigQueryLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::bigQueryLinkName('[PROPERTY]', '[BIGQUERY_LINK]');
    
        delete_big_query_link_sample($formattedName);
    }
    

### deleteCalculatedMetric

Deletes a CalculatedMetric on a property.

The async variant is [AnalyticsAdminServiceClient::deleteCalculatedMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteCalculatedMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteCalculatedMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteCalculatedMetricRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the CalculatedMetric to delete.
     *                              Format: properties/{property_id}/calculatedMetrics/{calculated_metric_id}
     *                              Example: properties/1234/calculatedMetrics/Metric01
     *                              Please see {@see AnalyticsAdminServiceClient::calculatedMetricName()} for help formatting this field.
     */
    function delete_calculated_metric_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteCalculatedMetricRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteCalculatedMetric($request);
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
        $formattedName = AnalyticsAdminServiceClient::calculatedMetricName(
            '[PROPERTY]',
            '[CALCULATED_METRIC]'
        );
    
        delete_calculated_metric_sample($formattedName);
    }
    

### deleteChannelGroup

Deletes a ChannelGroup on a property.

The async variant is [AnalyticsAdminServiceClient::deleteChannelGroupAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteChannelGroupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteChannelGroupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteChannelGroupRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The ChannelGroup to delete.
     *                              Example format: properties/1234/channelGroups/5678
     *                              Please see {@see AnalyticsAdminServiceClient::channelGroupName()} for help formatting this field.
     */
    function delete_channel_group_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteChannelGroupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteChannelGroup($request);
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
        $formattedName = AnalyticsAdminServiceClient::channelGroupName('[PROPERTY]', '[CHANNEL_GROUP]');
    
        delete_channel_group_sample($formattedName);
    }
    

### deleteConversionEvent

Deprecated: Use `DeleteKeyEvent` instead.

Deletes a conversion event in a property.

The async variant is [AnalyticsAdminServiceClient::deleteConversionEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteConversionEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteConversionEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteConversionEventRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The resource name of the conversion event to delete.
     *                              Format: properties/{property}/conversionEvents/{conversion_event}
     *                              Example: "properties/123/conversionEvents/456"
     *                              Please see {@see AnalyticsAdminServiceClient::conversionEventName()} for help formatting this field.
     */
    function delete_conversion_event_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteConversionEventRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteConversionEvent($request);
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
        $formattedName = AnalyticsAdminServiceClient::conversionEventName(
            '[PROPERTY]',
            '[CONVERSION_EVENT]'
        );
    
        delete_conversion_event_sample($formattedName);
    }
    

### deleteDataStream

Deletes a DataStream on a property.

The async variant is [AnalyticsAdminServiceClient::deleteDataStreamAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteDataStreamAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteDataStreamRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteDataStreamRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DataStream to delete.
     *                              Example format: properties/1234/dataStreams/5678
     *                              Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     */
    function delete_data_stream_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteDataStreamRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteDataStream($request);
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
        $formattedName = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
    
        delete_data_stream_sample($formattedName);
    }
    

### deleteDisplayVideo360AdvertiserLink

Deletes a DisplayVideo360AdvertiserLink on a property.

The async variant is [AnalyticsAdminServiceClient::deleteDisplayVideo360AdvertiserLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteDisplayVideo360AdvertiserLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteDisplayVideo360AdvertiserLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteDisplayVideo360AdvertiserLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DisplayVideo360AdvertiserLink to delete.
     *                              Example format: properties/1234/displayVideo360AdvertiserLinks/5678
     *                              Please see {@see AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkName()} for help formatting this field.
     */
    function delete_display_video360_advertiser_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteDisplayVideo360AdvertiserLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteDisplayVideo360AdvertiserLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkName(
            '[PROPERTY]',
            '[DISPLAY_VIDEO_360_ADVERTISER_LINK]'
        );
    
        delete_display_video360_advertiser_link_sample($formattedName);
    }
    

### deleteDisplayVideo360AdvertiserLinkProposal

Deletes a DisplayVideo360AdvertiserLinkProposal on a property.

This can only be used on cancelled proposals.

The async variant is [AnalyticsAdminServiceClient::deleteDisplayVideo360AdvertiserLinkProposalAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteDisplayVideo360AdvertiserLinkProposalAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteDisplayVideo360AdvertiserLinkProposalRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteDisplayVideo360AdvertiserLinkProposalRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DisplayVideo360AdvertiserLinkProposal to delete.
     *                              Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678
     *                              Please see {@see AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName()} for help formatting this field.
     */
    function delete_display_video360_advertiser_link_proposal_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteDisplayVideo360AdvertiserLinkProposalRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteDisplayVideo360AdvertiserLinkProposal($request);
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
        $formattedName = AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName(
            '[PROPERTY]',
            '[DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL]'
        );
    
        delete_display_video360_advertiser_link_proposal_sample($formattedName);
    }
    

### deleteEventCreateRule

Deletes an EventCreateRule.

The async variant is [AnalyticsAdminServiceClient::deleteEventCreateRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteEventCreateRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteEventCreateRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteEventCreateRuleRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Example format:
     *                              properties/123/dataStreams/456/eventCreateRules/789
     *                              Please see {@see AnalyticsAdminServiceClient::eventCreateRuleName()} for help formatting this field.
     */
    function delete_event_create_rule_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteEventCreateRuleRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteEventCreateRule($request);
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
        $formattedName = AnalyticsAdminServiceClient::eventCreateRuleName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[EVENT_CREATE_RULE]'
        );
    
        delete_event_create_rule_sample($formattedName);
    }
    

### deleteEventEditRule

Deletes an EventEditRule.

The async variant is [AnalyticsAdminServiceClient::deleteEventEditRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteEventEditRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteEventEditRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteEventEditRuleRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Example format: properties/123/dataStreams/456/eventEditRules/789
     *                              Please see {@see AnalyticsAdminServiceClient::eventEditRuleName()} for help formatting this field.
     */
    function delete_event_edit_rule_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteEventEditRuleRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteEventEditRule($request);
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
        $formattedName = AnalyticsAdminServiceClient::eventEditRuleName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[EVENT_EDIT_RULE]'
        );
    
        delete_event_edit_rule_sample($formattedName);
    }
    

### deleteExpandedDataSet

Deletes a ExpandedDataSet on a property.

The async variant is [AnalyticsAdminServiceClient::deleteExpandedDataSetAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteExpandedDataSetAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteExpandedDataSetRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteExpandedDataSetRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Example format: properties/1234/expandedDataSets/5678
     *                              Please see {@see AnalyticsAdminServiceClient::expandedDataSetName()} for help formatting this field.
     */
    function delete_expanded_data_set_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteExpandedDataSetRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteExpandedDataSet($request);
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
        $formattedName = AnalyticsAdminServiceClient::expandedDataSetName(
            '[PROPERTY]',
            '[EXPANDED_DATA_SET]'
        );
    
        delete_expanded_data_set_sample($formattedName);
    }
    

### deleteFirebaseLink

Deletes a FirebaseLink on a property

The async variant is [AnalyticsAdminServiceClient::deleteFirebaseLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteFirebaseLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteFirebaseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteFirebaseLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteFirebaseLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Format: properties/{property_id}/firebaseLinks/{firebase_link_id}
     *
     *                              Example: `properties/1234/firebaseLinks/5678`
     *                              Please see {@see AnalyticsAdminServiceClient::firebaseLinkName()} for help formatting this field.
     */
    function delete_firebase_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteFirebaseLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteFirebaseLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::firebaseLinkName('[PROPERTY]', '[FIREBASE_LINK]');
    
        delete_firebase_link_sample($formattedName);
    }
    

### deleteGoogleAdsLink

Deletes a GoogleAdsLink on a property

The async variant is [AnalyticsAdminServiceClient::deleteGoogleAdsLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteGoogleAdsLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteGoogleAdsLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteGoogleAdsLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Example format: properties/1234/googleAdsLinks/5678
     *                              Please see {@see AnalyticsAdminServiceClient::googleAdsLinkName()} for help formatting this field.
     */
    function delete_google_ads_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteGoogleAdsLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteGoogleAdsLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::googleAdsLinkName('[PROPERTY]', '[GOOGLE_ADS_LINK]');
    
        delete_google_ads_link_sample($formattedName);
    }
    

### deleteKeyEvent

Deletes a Key Event.

The async variant is [AnalyticsAdminServiceClient::deleteKeyEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteKeyEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteKeyEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteKeyEventRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The resource name of the Key Event to delete.
     *                              Format: properties/{property}/keyEvents/{key_event}
     *                              Example: "properties/123/keyEvents/456"
     *                              Please see {@see AnalyticsAdminServiceClient::keyEventName()} for help formatting this field.
     */
    function delete_key_event_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteKeyEventRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteKeyEvent($request);
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
        $formattedName = AnalyticsAdminServiceClient::keyEventName('[PROPERTY]', '[KEY_EVENT]');
    
        delete_key_event_sample($formattedName);
    }
    

### deleteMeasurementProtocolSecret

Deletes target MeasurementProtocolSecret.

The async variant is [AnalyticsAdminServiceClient::deleteMeasurementProtocolSecretAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteMeasurementProtocolSecretAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteMeasurementProtocolSecretRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteMeasurementProtocolSecretRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the MeasurementProtocolSecret to delete.
     *                              Format:
     *                              properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret}
     *                              Please see {@see AnalyticsAdminServiceClient::measurementProtocolSecretName()} for help formatting this field.
     */
    function delete_measurement_protocol_secret_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteMeasurementProtocolSecretRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteMeasurementProtocolSecret($request);
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
        $formattedName = AnalyticsAdminServiceClient::measurementProtocolSecretName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[MEASUREMENT_PROTOCOL_SECRET]'
        );
    
        delete_measurement_protocol_secret_sample($formattedName);
    }
    

### deleteProperty

Marks target Property as soft-deleted (ie: "trashed") and returns it.

This API does not have a method to restore soft-deleted properties. However, they can be restored using the Trash Can UI.

If the properties are not restored before the expiration time, the Property and all child resources (eg: GoogleAdsLinks, Streams, AccessBindings) will be permanently purged. <https://support.google.com/analytics/answer/6154772>

Returns an error if the target is not found.

The async variant is [AnalyticsAdminServiceClient::deletePropertyAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deletePropertyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeletePropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeletePropertyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeletePropertyRequest;
    use Google\Analytics\Admin\V1alpha\Property;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the Property to soft-delete.
     *                              Format: properties/{property_id}
     *                              Example: "properties/1000"
     *                              Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function delete_property_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeletePropertyRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Property $response */
            $response = $analyticsAdminServiceClient->deleteProperty($request);
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
        $formattedName = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        delete_property_sample($formattedName);
    }
    

### deleteReportingDataAnnotation

Deletes a Reporting Data Annotation.

The async variant is [AnalyticsAdminServiceClient::deleteReportingDataAnnotationAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteReportingDataAnnotationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteReportingDataAnnotationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteReportingDataAnnotationRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Resource name of the Reporting Data Annotation to delete.
     *                              Format:
     *                              properties/property_id/reportingDataAnnotations/reporting_data_annotation
     *                              Example: properties/123/reportingDataAnnotations/456
     *                              Please see {@see AnalyticsAdminServiceClient::reportingDataAnnotationName()} for help formatting this field.
     */
    function delete_reporting_data_annotation_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteReportingDataAnnotationRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteReportingDataAnnotation($request);
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
        $formattedName = AnalyticsAdminServiceClient::reportingDataAnnotationName(
            '[PROPERTY]',
            '[REPORTING_DATA_ANNOTATION]'
        );
    
        delete_reporting_data_annotation_sample($formattedName);
    }
    

### deleteRollupPropertySourceLink

Deletes a roll-up property source link.

Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

The async variant is [AnalyticsAdminServiceClient::deleteRollupPropertySourceLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteRollupPropertySourceLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteRollupPropertySourceLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteRollupPropertySourceLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteRollupPropertySourceLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Format:
     *                              properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_link_id}
     *                              Example: properties/1234/rollupPropertySourceLinks/5678
     *                              Please see {@see AnalyticsAdminServiceClient::rollupPropertySourceLinkName()} for help formatting this field.
     */
    function delete_rollup_property_source_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteRollupPropertySourceLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteRollupPropertySourceLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::rollupPropertySourceLinkName(
            '[PROPERTY]',
            '[ROLLUP_PROPERTY_SOURCE_LINK]'
        );
    
        delete_rollup_property_source_link_sample($formattedName);
    }
    

### deleteSKAdNetworkConversionValueSchema

Deletes target SKAdNetworkConversionValueSchema.

The async variant is [AnalyticsAdminServiceClient::deleteSKAdNetworkConversionValueSchemaAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteSKAdNetworkConversionValueSchemaAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteSKAdNetworkConversionValueSchemaRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteSKAdNetworkConversionValueSchemaRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the SKAdNetworkConversionValueSchema to delete.
     *                              Format:
     *                              properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSchema/{skadnetwork_conversion_value_schema}
     *                              Please see {@see AnalyticsAdminServiceClient::sKAdNetworkConversionValueSchemaName()} for help formatting this field.
     */
    function delete_sk_ad_network_conversion_value_schema_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteSKAdNetworkConversionValueSchemaRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteSKAdNetworkConversionValueSchema($request);
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
        $formattedName = AnalyticsAdminServiceClient::sKAdNetworkConversionValueSchemaName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[SKADNETWORK_CONVERSION_VALUE_SCHEMA]'
        );
    
        delete_sk_ad_network_conversion_value_schema_sample($formattedName);
    }
    

### deleteSearchAds360Link

Deletes a SearchAds360Link on a property.

The async variant is [AnalyticsAdminServiceClient::deleteSearchAds360LinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteSearchAds360LinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteSearchAds360LinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteSearchAds360LinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the SearchAds360Link to delete.
     *                              Example format: properties/1234/SearchAds360Links/5678
     *                              Please see {@see AnalyticsAdminServiceClient::searchAds360LinkName()} for help formatting this field.
     */
    function delete_search_ads360_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteSearchAds360LinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteSearchAds360Link($request);
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
        $formattedName = AnalyticsAdminServiceClient::searchAds360LinkName(
            '[PROPERTY]',
            '[SEARCH_ADS_360_LINK]'
        );
    
        delete_search_ads360_link_sample($formattedName);
    }
    

### deleteSubpropertyEventFilter

Deletes a subproperty event filter.

The async variant is [AnalyticsAdminServiceClient::deleteSubpropertyEventFilterAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__deleteSubpropertyEventFilterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteSubpropertyEventFilterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DeleteSubpropertyEventFilterRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Resource name of the subproperty event filter to delete.
     *                              Format:
     *                              properties/property_id/subpropertyEventFilters/subproperty_event_filter
     *                              Example: properties/123/subpropertyEventFilters/456
     *                              Please see {@see AnalyticsAdminServiceClient::subpropertyEventFilterName()} for help formatting this field.
     */
    function delete_subproperty_event_filter_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteSubpropertyEventFilterRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->deleteSubpropertyEventFilter($request);
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
        $formattedName = AnalyticsAdminServiceClient::subpropertyEventFilterName(
            '[PROPERTY]',
            '[SUB_PROPERTY_EVENT_FILTER]'
        );
    
        delete_subproperty_event_filter_sample($formattedName);
    }
    

### getAccessBinding

Gets information about an access binding.

The async variant is [AnalyticsAdminServiceClient::getAccessBindingAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getAccessBindingAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAccessBindingRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AccessBinding](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessBinding)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AccessBinding;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetAccessBindingRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the access binding to retrieve.
     *                              Formats:
     *                              - accounts/{account}/accessBindings/{accessBinding}
     *                              - properties/{property}/accessBindings/{accessBinding}
     *                              Please see {@see AnalyticsAdminServiceClient::accessBindingName()} for help formatting this field.
     */
    function get_access_binding_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetAccessBindingRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var AccessBinding $response */
            $response = $analyticsAdminServiceClient->getAccessBinding($request);
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
        $formattedName = AnalyticsAdminServiceClient::accessBindingName('[ACCOUNT]', '[ACCESS_BINDING]');
    
        get_access_binding_sample($formattedName);
    }
    

### getAccount

Lookup for a single Account.

The async variant is [AnalyticsAdminServiceClient::getAccountAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getAccountAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAccountRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAccountRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Account](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Account)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Account;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetAccountRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the account to lookup.
     *                              Format: accounts/{account}
     *                              Example: "accounts/100"
     *                              Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     */
    function get_account_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetAccountRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Account $response */
            $response = $analyticsAdminServiceClient->getAccount($request);
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
        $formattedName = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
    
        get_account_sample($formattedName);
    }
    

### getAdSenseLink

Looks up a single AdSenseLink.

The async variant is [AnalyticsAdminServiceClient::getAdSenseLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getAdSenseLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAdSenseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAdSenseLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AdSenseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AdSenseLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AdSenseLink;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetAdSenseLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Unique identifier for the AdSense Link requested.
     *                              Format: properties/{propertyId}/adSenseLinks/{linkId}
     *                              Example: properties/1234/adSenseLinks/5678
     *                              Please see {@see AnalyticsAdminServiceClient::adSenseLinkName()} for help formatting this field.
     */
    function get_ad_sense_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetAdSenseLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var AdSenseLink $response */
            $response = $analyticsAdminServiceClient->getAdSenseLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::adSenseLinkName('[PROPERTY]', '[ADSENSE_LINK]');
    
        get_ad_sense_link_sample($formattedName);
    }
    

### getAttributionSettings

Lookup for a AttributionSettings singleton.

The async variant is [AnalyticsAdminServiceClient::getAttributionSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getAttributionSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAttributionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAttributionSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AttributionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AttributionSettings;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetAttributionSettingsRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the attribution settings to retrieve.
     *                              Format: properties/{property}/attributionSettings
     *                              Please see {@see AnalyticsAdminServiceClient::attributionSettingsName()} for help formatting this field.
     */
    function get_attribution_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetAttributionSettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var AttributionSettings $response */
            $response = $analyticsAdminServiceClient->getAttributionSettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::attributionSettingsName('[PROPERTY]');
    
        get_attribution_settings_sample($formattedName);
    }
    

### getAudience

Lookup for a single Audience.

Audiences created before 2020 may not be supported. Default audiences will not show filter definitions.

The async variant is [AnalyticsAdminServiceClient::getAudienceAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getAudienceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAudienceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Audience;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetAudienceRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the Audience to get.
     *                              Example format: properties/1234/audiences/5678
     *                              Please see {@see AnalyticsAdminServiceClient::audienceName()} for help formatting this field.
     */
    function get_audience_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetAudienceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Audience $response */
            $response = $analyticsAdminServiceClient->getAudience($request);
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
        $formattedName = AnalyticsAdminServiceClient::audienceName('[PROPERTY]', '[AUDIENCE]');
    
        get_audience_sample($formattedName);
    }
    

### getBigQueryLink

Lookup for a single BigQuery Link.

The async variant is [AnalyticsAdminServiceClient::getBigQueryLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getBigQueryLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetBigQueryLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\BigQueryLink;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetBigQueryLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the BigQuery link to lookup.
     *                              Format: properties/{property_id}/bigQueryLinks/{bigquery_link_id}
     *                              Example: properties/123/bigQueryLinks/456
     *                              Please see {@see AnalyticsAdminServiceClient::bigQueryLinkName()} for help formatting this field.
     */
    function get_big_query_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetBigQueryLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var BigQueryLink $response */
            $response = $analyticsAdminServiceClient->getBigQueryLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::bigQueryLinkName('[PROPERTY]', '[BIGQUERY_LINK]');
    
        get_big_query_link_sample($formattedName);
    }
    

### getCalculatedMetric

Lookup for a single CalculatedMetric.

The async variant is [AnalyticsAdminServiceClient::getCalculatedMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getCalculatedMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetCalculatedMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\CalculatedMetric;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetCalculatedMetricRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the CalculatedMetric to get.
     *                              Format: properties/{property_id}/calculatedMetrics/{calculated_metric_id}
     *                              Example: properties/1234/calculatedMetrics/Metric01
     *                              Please see {@see AnalyticsAdminServiceClient::calculatedMetricName()} for help formatting this field.
     */
    function get_calculated_metric_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetCalculatedMetricRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var CalculatedMetric $response */
            $response = $analyticsAdminServiceClient->getCalculatedMetric($request);
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
        $formattedName = AnalyticsAdminServiceClient::calculatedMetricName(
            '[PROPERTY]',
            '[CALCULATED_METRIC]'
        );
    
        get_calculated_metric_sample($formattedName);
    }
    

### getChannelGroup

Lookup for a single ChannelGroup.

The async variant is [AnalyticsAdminServiceClient::getChannelGroupAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getChannelGroupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetChannelGroupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\ChannelGroup;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetChannelGroupRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The ChannelGroup to get.
     *                              Example format: properties/1234/channelGroups/5678
     *                              Please see {@see AnalyticsAdminServiceClient::channelGroupName()} for help formatting this field.
     */
    function get_channel_group_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetChannelGroupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var ChannelGroup $response */
            $response = $analyticsAdminServiceClient->getChannelGroup($request);
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
        $formattedName = AnalyticsAdminServiceClient::channelGroupName('[PROPERTY]', '[CHANNEL_GROUP]');
    
        get_channel_group_sample($formattedName);
    }
    

### getConversionEvent

Deprecated: Use `GetKeyEvent` instead.

Retrieve a single conversion event.

The async variant is [AnalyticsAdminServiceClient::getConversionEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getConversionEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetConversionEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ConversionEvent;
    use Google\Analytics\Admin\V1alpha\GetConversionEventRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The resource name of the conversion event to retrieve.
     *                              Format: properties/{property}/conversionEvents/{conversion_event}
     *                              Example: "properties/123/conversionEvents/456"
     *                              Please see {@see AnalyticsAdminServiceClient::conversionEventName()} for help formatting this field.
     */
    function get_conversion_event_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetConversionEventRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var ConversionEvent $response */
            $response = $analyticsAdminServiceClient->getConversionEvent($request);
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
        $formattedName = AnalyticsAdminServiceClient::conversionEventName(
            '[PROPERTY]',
            '[CONVERSION_EVENT]'
        );
    
        get_conversion_event_sample($formattedName);
    }
    

### getCustomDimension

Lookup for a single CustomDimension.

The async variant is [AnalyticsAdminServiceClient::getCustomDimensionAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getCustomDimensionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetCustomDimensionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CustomDimension;
    use Google\Analytics\Admin\V1alpha\GetCustomDimensionRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the CustomDimension to get.
     *                              Example format: properties/1234/customDimensions/5678
     *                              Please see {@see AnalyticsAdminServiceClient::customDimensionName()} for help formatting this field.
     */
    function get_custom_dimension_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetCustomDimensionRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var CustomDimension $response */
            $response = $analyticsAdminServiceClient->getCustomDimension($request);
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
        $formattedName = AnalyticsAdminServiceClient::customDimensionName(
            '[PROPERTY]',
            '[CUSTOM_DIMENSION]'
        );
    
        get_custom_dimension_sample($formattedName);
    }
    

### getCustomMetric

Lookup for a single CustomMetric.

The async variant is [AnalyticsAdminServiceClient::getCustomMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getCustomMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetCustomMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CustomMetric;
    use Google\Analytics\Admin\V1alpha\GetCustomMetricRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the CustomMetric to get.
     *                              Example format: properties/1234/customMetrics/5678
     *                              Please see {@see AnalyticsAdminServiceClient::customMetricName()} for help formatting this field.
     */
    function get_custom_metric_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetCustomMetricRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var CustomMetric $response */
            $response = $analyticsAdminServiceClient->getCustomMetric($request);
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
        $formattedName = AnalyticsAdminServiceClient::customMetricName('[PROPERTY]', '[CUSTOM_METRIC]');
    
        get_custom_metric_sample($formattedName);
    }
    

### getDataRedactionSettings

Lookup for a single DataRedactionSettings.

The async variant is [AnalyticsAdminServiceClient::getDataRedactionSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getDataRedactionSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataRedactionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataRedactionSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataRedactionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRedactionSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataRedactionSettings;
    use Google\Analytics\Admin\V1alpha\GetDataRedactionSettingsRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the settings to lookup.
     *                              Format:
     *                              properties/{property}/dataStreams/{data_stream}/dataRedactionSettings
     *                              Example: "properties/1000/dataStreams/2000/dataRedactionSettings"
     *                              Please see {@see AnalyticsAdminServiceClient::dataRedactionSettingsName()} for help formatting this field.
     */
    function get_data_redaction_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetDataRedactionSettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataRedactionSettings $response */
            $response = $analyticsAdminServiceClient->getDataRedactionSettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::dataRedactionSettingsName(
            '[PROPERTY]',
            '[DATA_STREAM]'
        );
    
        get_data_redaction_settings_sample($formattedName);
    }
    

### getDataRetentionSettings

Returns the singleton data retention settings for this property.

The async variant is [AnalyticsAdminServiceClient::getDataRetentionSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getDataRetentionSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataRetentionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataRetentionSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataRetentionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataRetentionSettings;
    use Google\Analytics\Admin\V1alpha\GetDataRetentionSettingsRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the settings to lookup.
     *                              Format:
     *                              properties/{property}/dataRetentionSettings
     *                              Example: "properties/1000/dataRetentionSettings"
     *                              Please see {@see AnalyticsAdminServiceClient::dataRetentionSettingsName()} for help formatting this field.
     */
    function get_data_retention_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetDataRetentionSettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataRetentionSettings $response */
            $response = $analyticsAdminServiceClient->getDataRetentionSettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::dataRetentionSettingsName('[PROPERTY]');
    
        get_data_retention_settings_sample($formattedName);
    }
    

### getDataSharingSettings

Get data sharing settings on an account.

Data sharing settings are singletons.

The async variant is [AnalyticsAdminServiceClient::getDataSharingSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getDataSharingSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataSharingSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataSharingSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataSharingSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataSharingSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataSharingSettings;
    use Google\Analytics\Admin\V1alpha\GetDataSharingSettingsRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the settings to lookup.
     *                              Format: accounts/{account}/dataSharingSettings
     *
     *                              Example: `accounts/1000/dataSharingSettings`
     *                              Please see {@see AnalyticsAdminServiceClient::dataSharingSettingsName()} for help formatting this field.
     */
    function get_data_sharing_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetDataSharingSettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataSharingSettings $response */
            $response = $analyticsAdminServiceClient->getDataSharingSettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::dataSharingSettingsName('[ACCOUNT]');
    
        get_data_sharing_settings_sample($formattedName);
    }
    

### getDataStream

Lookup for a single DataStream.

The async variant is [AnalyticsAdminServiceClient::getDataStreamAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getDataStreamAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataStreamRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataStream;
    use Google\Analytics\Admin\V1alpha\GetDataStreamRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DataStream to get.
     *                              Example format: properties/1234/dataStreams/5678
     *                              Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     */
    function get_data_stream_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetDataStreamRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataStream $response */
            $response = $analyticsAdminServiceClient->getDataStream($request);
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
        $formattedName = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
    
        get_data_stream_sample($formattedName);
    }
    

### getDisplayVideo360AdvertiserLink

Look up a single DisplayVideo360AdvertiserLink

The async variant is [AnalyticsAdminServiceClient::getDisplayVideo360AdvertiserLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getDisplayVideo360AdvertiserLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDisplayVideo360AdvertiserLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink;
    use Google\Analytics\Admin\V1alpha\GetDisplayVideo360AdvertiserLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DisplayVideo360AdvertiserLink to get.
     *                              Example format: properties/1234/displayVideo360AdvertiserLink/5678
     *                              Please see {@see AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkName()} for help formatting this field.
     */
    function get_display_video360_advertiser_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetDisplayVideo360AdvertiserLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DisplayVideo360AdvertiserLink $response */
            $response = $analyticsAdminServiceClient->getDisplayVideo360AdvertiserLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkName(
            '[PROPERTY]',
            '[DISPLAY_VIDEO_360_ADVERTISER_LINK]'
        );
    
        get_display_video360_advertiser_link_sample($formattedName);
    }
    

### getDisplayVideo360AdvertiserLinkProposal

Lookup for a single DisplayVideo360AdvertiserLinkProposal.

The async variant is [AnalyticsAdminServiceClient::getDisplayVideo360AdvertiserLinkProposalAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getDisplayVideo360AdvertiserLinkProposalAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDisplayVideo360AdvertiserLinkProposalRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal;
    use Google\Analytics\Admin\V1alpha\GetDisplayVideo360AdvertiserLinkProposalRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the DisplayVideo360AdvertiserLinkProposal to get.
     *                              Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678
     *                              Please see {@see AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName()} for help formatting this field.
     */
    function get_display_video360_advertiser_link_proposal_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetDisplayVideo360AdvertiserLinkProposalRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DisplayVideo360AdvertiserLinkProposal $response */
            $response = $analyticsAdminServiceClient->getDisplayVideo360AdvertiserLinkProposal($request);
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
        $formattedName = AnalyticsAdminServiceClient::displayVideo360AdvertiserLinkProposalName(
            '[PROPERTY]',
            '[DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL]'
        );
    
        get_display_video360_advertiser_link_proposal_sample($formattedName);
    }
    

### getEnhancedMeasurementSettings

Returns the enhanced measurement settings for this data stream.

Note that the stream must enable enhanced measurement for these settings to take effect.

The async variant is [AnalyticsAdminServiceClient::getEnhancedMeasurementSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getEnhancedMeasurementSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetEnhancedMeasurementSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings;
    use Google\Analytics\Admin\V1alpha\GetEnhancedMeasurementSettingsRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the settings to lookup.
     *                              Format:
     *                              properties/{property}/dataStreams/{data_stream}/enhancedMeasurementSettings
     *                              Example: "properties/1000/dataStreams/2000/enhancedMeasurementSettings"
     *                              Please see {@see AnalyticsAdminServiceClient::enhancedMeasurementSettingsName()} for help formatting this field.
     */
    function get_enhanced_measurement_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetEnhancedMeasurementSettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var EnhancedMeasurementSettings $response */
            $response = $analyticsAdminServiceClient->getEnhancedMeasurementSettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::enhancedMeasurementSettingsName(
            '[PROPERTY]',
            '[DATA_STREAM]'
        );
    
        get_enhanced_measurement_settings_sample($formattedName);
    }
    

### getEventCreateRule

Lookup for a single EventCreateRule.

The async variant is [AnalyticsAdminServiceClient::getEventCreateRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getEventCreateRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetEventCreateRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EventCreateRule;
    use Google\Analytics\Admin\V1alpha\GetEventCreateRuleRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the EventCreateRule to get.
     *                              Example format: properties/123/dataStreams/456/eventCreateRules/789
     *                              Please see {@see AnalyticsAdminServiceClient::eventCreateRuleName()} for help formatting this field.
     */
    function get_event_create_rule_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetEventCreateRuleRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var EventCreateRule $response */
            $response = $analyticsAdminServiceClient->getEventCreateRule($request);
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
        $formattedName = AnalyticsAdminServiceClient::eventCreateRuleName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[EVENT_CREATE_RULE]'
        );
    
        get_event_create_rule_sample($formattedName);
    }
    

### getEventEditRule

Lookup for a single EventEditRule.

The async variant is [AnalyticsAdminServiceClient::getEventEditRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getEventEditRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetEventEditRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EventEditRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EventEditRule;
    use Google\Analytics\Admin\V1alpha\GetEventEditRuleRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the EventEditRule to get.
     *                              Example format: properties/123/dataStreams/456/eventEditRules/789
     *                              Please see {@see AnalyticsAdminServiceClient::eventEditRuleName()} for help formatting this field.
     */
    function get_event_edit_rule_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetEventEditRuleRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var EventEditRule $response */
            $response = $analyticsAdminServiceClient->getEventEditRule($request);
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
        $formattedName = AnalyticsAdminServiceClient::eventEditRuleName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[EVENT_EDIT_RULE]'
        );
    
        get_event_edit_rule_sample($formattedName);
    }
    

### getExpandedDataSet

Lookup for a single ExpandedDataSet.

The async variant is [AnalyticsAdminServiceClient::getExpandedDataSetAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getExpandedDataSetAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetExpandedDataSetRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ExpandedDataSet;
    use Google\Analytics\Admin\V1alpha\GetExpandedDataSetRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the ExpandedDataSet to get.
     *                              Example format: properties/1234/expandedDataSets/5678
     *                              Please see {@see AnalyticsAdminServiceClient::expandedDataSetName()} for help formatting this field.
     */
    function get_expanded_data_set_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetExpandedDataSetRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var ExpandedDataSet $response */
            $response = $analyticsAdminServiceClient->getExpandedDataSet($request);
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
        $formattedName = AnalyticsAdminServiceClient::expandedDataSetName(
            '[PROPERTY]',
            '[EXPANDED_DATA_SET]'
        );
    
        get_expanded_data_set_sample($formattedName);
    }
    

### getGlobalSiteTag

Returns the Site Tag for the specified web stream.

Site Tags are immutable singletons.

The async variant is [AnalyticsAdminServiceClient::getGlobalSiteTagAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getGlobalSiteTagAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetGlobalSiteTagRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetGlobalSiteTagRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\GlobalSiteTag](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GlobalSiteTag)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetGlobalSiteTagRequest;
    use Google\Analytics\Admin\V1alpha\GlobalSiteTag;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the site tag to lookup.
     *                              Note that site tags are singletons and do not have unique IDs.
     *                              Format: properties/{property_id}/dataStreams/{stream_id}/globalSiteTag
     *
     *                              Example: `properties/123/dataStreams/456/globalSiteTag`
     *                              Please see {@see AnalyticsAdminServiceClient::globalSiteTagName()} for help formatting this field.
     */
    function get_global_site_tag_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetGlobalSiteTagRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var GlobalSiteTag $response */
            $response = $analyticsAdminServiceClient->getGlobalSiteTag($request);
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
        $formattedName = AnalyticsAdminServiceClient::globalSiteTagName('[PROPERTY]', '[DATA_STREAM]');
    
        get_global_site_tag_sample($formattedName);
    }
    

### getGoogleSignalsSettings

Lookup for Google Signals settings for a property.

The async variant is [AnalyticsAdminServiceClient::getGoogleSignalsSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getGoogleSignalsSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetGoogleSignalsSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetGoogleSignalsSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\GoogleSignalsSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleSignalsSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetGoogleSignalsSettingsRequest;
    use Google\Analytics\Admin\V1alpha\GoogleSignalsSettings;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the google signals settings to retrieve.
     *                              Format: properties/{property}/googleSignalsSettings
     *                              Please see {@see AnalyticsAdminServiceClient::googleSignalsSettingsName()} for help formatting this field.
     */
    function get_google_signals_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetGoogleSignalsSettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var GoogleSignalsSettings $response */
            $response = $analyticsAdminServiceClient->getGoogleSignalsSettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::googleSignalsSettingsName('[PROPERTY]');
    
        get_google_signals_settings_sample($formattedName);
    }
    

### getKeyEvent

Retrieve a single Key Event.

The async variant is [AnalyticsAdminServiceClient::getKeyEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getKeyEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetKeyEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetKeyEventRequest;
    use Google\Analytics\Admin\V1alpha\KeyEvent;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The resource name of the Key Event to retrieve.
     *                              Format: properties/{property}/keyEvents/{key_event}
     *                              Example: "properties/123/keyEvents/456"
     *                              Please see {@see AnalyticsAdminServiceClient::keyEventName()} for help formatting this field.
     */
    function get_key_event_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetKeyEventRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var KeyEvent $response */
            $response = $analyticsAdminServiceClient->getKeyEvent($request);
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
        $formattedName = AnalyticsAdminServiceClient::keyEventName('[PROPERTY]', '[KEY_EVENT]');
    
        get_key_event_sample($formattedName);
    }
    

### getMeasurementProtocolSecret

Lookup for a single MeasurementProtocolSecret.

The async variant is [AnalyticsAdminServiceClient::getMeasurementProtocolSecretAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getMeasurementProtocolSecretAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetMeasurementProtocolSecretRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetMeasurementProtocolSecretRequest;
    use Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the measurement protocol secret to lookup.
     *                              Format:
     *                              properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret}
     *                              Please see {@see AnalyticsAdminServiceClient::measurementProtocolSecretName()} for help formatting this field.
     */
    function get_measurement_protocol_secret_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetMeasurementProtocolSecretRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var MeasurementProtocolSecret $response */
            $response = $analyticsAdminServiceClient->getMeasurementProtocolSecret($request);
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
        $formattedName = AnalyticsAdminServiceClient::measurementProtocolSecretName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[MEASUREMENT_PROTOCOL_SECRET]'
        );
    
        get_measurement_protocol_secret_sample($formattedName);
    }
    

### getProperty

Lookup for a single GA Property.

The async variant is [AnalyticsAdminServiceClient::getPropertyAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getPropertyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetPropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetPropertyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetPropertyRequest;
    use Google\Analytics\Admin\V1alpha\Property;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the property to lookup.
     *                              Format: properties/{property_id}
     *                              Example: "properties/1000"
     *                              Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function get_property_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetPropertyRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Property $response */
            $response = $analyticsAdminServiceClient->getProperty($request);
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
        $formattedName = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        get_property_sample($formattedName);
    }
    

### getReportingDataAnnotation

Lookup a single Reporting Data Annotation.

The async variant is [AnalyticsAdminServiceClient::getReportingDataAnnotationAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getReportingDataAnnotationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetReportingDataAnnotationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetReportingDataAnnotationRequest;
    use Google\Analytics\Admin\V1alpha\ReportingDataAnnotation;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Resource name of the Reporting Data Annotation to lookup.
     *                              Format:
     *                              properties/property_id/reportingDataAnnotations/reportingDataAnnotation
     *                              Example: properties/123/reportingDataAnnotations/456
     *                              Please see {@see AnalyticsAdminServiceClient::reportingDataAnnotationName()} for help formatting this field.
     */
    function get_reporting_data_annotation_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetReportingDataAnnotationRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var ReportingDataAnnotation $response */
            $response = $analyticsAdminServiceClient->getReportingDataAnnotation($request);
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
        $formattedName = AnalyticsAdminServiceClient::reportingDataAnnotationName(
            '[PROPERTY]',
            '[REPORTING_DATA_ANNOTATION]'
        );
    
        get_reporting_data_annotation_sample($formattedName);
    }
    

### getReportingIdentitySettings

Returns the reporting identity settings for this property.

The async variant is [AnalyticsAdminServiceClient::getReportingIdentitySettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getReportingIdentitySettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetReportingIdentitySettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetReportingIdentitySettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ReportingIdentitySettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingIdentitySettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetReportingIdentitySettingsRequest;
    use Google\Analytics\Admin\V1alpha\ReportingIdentitySettings;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the settings to lookup.
     *                              Format:
     *                              properties/{property}/reportingIdentitySettings
     *                              Example: "properties/1000/reportingIdentitySettings"
     *                              Please see {@see AnalyticsAdminServiceClient::reportingIdentitySettingsName()} for help formatting this field.
     */
    function get_reporting_identity_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetReportingIdentitySettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var ReportingIdentitySettings $response */
            $response = $analyticsAdminServiceClient->getReportingIdentitySettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::reportingIdentitySettingsName('[PROPERTY]');
    
        get_reporting_identity_settings_sample($formattedName);
    }
    

### getRollupPropertySourceLink

Lookup for a single roll-up property source Link.

Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

The async variant is [AnalyticsAdminServiceClient::getRollupPropertySourceLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getRollupPropertySourceLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetRollupPropertySourceLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetRollupPropertySourceLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\RollupPropertySourceLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RollupPropertySourceLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetRollupPropertySourceLinkRequest;
    use Google\Analytics\Admin\V1alpha\RollupPropertySourceLink;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the roll-up property source link to lookup.
     *                              Format:
     *                              properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_link_id}
     *                              Example: properties/123/rollupPropertySourceLinks/456
     *                              Please see {@see AnalyticsAdminServiceClient::rollupPropertySourceLinkName()} for help formatting this field.
     */
    function get_rollup_property_source_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetRollupPropertySourceLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var RollupPropertySourceLink $response */
            $response = $analyticsAdminServiceClient->getRollupPropertySourceLink($request);
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
        $formattedName = AnalyticsAdminServiceClient::rollupPropertySourceLinkName(
            '[PROPERTY]',
            '[ROLLUP_PROPERTY_SOURCE_LINK]'
        );
    
        get_rollup_property_source_link_sample($formattedName);
    }
    

### getSKAdNetworkConversionValueSchema

Looks up a single SKAdNetworkConversionValueSchema.

The async variant is [AnalyticsAdminServiceClient::getSKAdNetworkConversionValueSchemaAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getSKAdNetworkConversionValueSchemaAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSKAdNetworkConversionValueSchemaRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetSKAdNetworkConversionValueSchemaRequest;
    use Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The resource name of SKAdNetwork conversion value schema to look
     *                              up. Format:
     *                              properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSchema/{skadnetwork_conversion_value_schema}
     *                              Please see {@see AnalyticsAdminServiceClient::sKAdNetworkConversionValueSchemaName()} for help formatting this field.
     */
    function get_sk_ad_network_conversion_value_schema_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetSKAdNetworkConversionValueSchemaRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var SKAdNetworkConversionValueSchema $response */
            $response = $analyticsAdminServiceClient->getSKAdNetworkConversionValueSchema($request);
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
        $formattedName = AnalyticsAdminServiceClient::sKAdNetworkConversionValueSchemaName(
            '[PROPERTY]',
            '[DATA_STREAM]',
            '[SKADNETWORK_CONVERSION_VALUE_SCHEMA]'
        );
    
        get_sk_ad_network_conversion_value_schema_sample($formattedName);
    }
    

### getSearchAds360Link

Look up a single SearchAds360Link

The async variant is [AnalyticsAdminServiceClient::getSearchAds360LinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getSearchAds360LinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSearchAds360LinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetSearchAds360LinkRequest;
    use Google\Analytics\Admin\V1alpha\SearchAds360Link;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the SearchAds360Link to get.
     *                              Example format: properties/1234/SearchAds360Link/5678
     *                              Please see {@see AnalyticsAdminServiceClient::searchAds360LinkName()} for help formatting this field.
     */
    function get_search_ads360_link_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetSearchAds360LinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var SearchAds360Link $response */
            $response = $analyticsAdminServiceClient->getSearchAds360Link($request);
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
        $formattedName = AnalyticsAdminServiceClient::searchAds360LinkName(
            '[PROPERTY]',
            '[SEARCH_ADS_360_LINK]'
        );
    
        get_search_ads360_link_sample($formattedName);
    }
    

### getSubpropertyEventFilter

Lookup for a single subproperty Event Filter.

The async variant is [AnalyticsAdminServiceClient::getSubpropertyEventFilterAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getSubpropertyEventFilterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSubpropertyEventFilterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SubpropertyEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertyEventFilter)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetSubpropertyEventFilterRequest;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilter;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Resource name of the subproperty event filter to lookup.
     *                              Format:
     *                              properties/property_id/subpropertyEventFilters/subproperty_event_filter
     *                              Example: properties/123/subpropertyEventFilters/456
     *                              Please see {@see AnalyticsAdminServiceClient::subpropertyEventFilterName()} for help formatting this field.
     */
    function get_subproperty_event_filter_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetSubpropertyEventFilterRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var SubpropertyEventFilter $response */
            $response = $analyticsAdminServiceClient->getSubpropertyEventFilter($request);
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
        $formattedName = AnalyticsAdminServiceClient::subpropertyEventFilterName(
            '[PROPERTY]',
            '[SUB_PROPERTY_EVENT_FILTER]'
        );
    
        get_subproperty_event_filter_sample($formattedName);
    }
    

### getSubpropertySyncConfig

Lookup for a single `SubpropertySyncConfig`.

The async variant is [AnalyticsAdminServiceClient::getSubpropertySyncConfigAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getSubpropertySyncConfigAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSubpropertySyncConfigRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSubpropertySyncConfigRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SubpropertySyncConfig](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertySyncConfig)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetSubpropertySyncConfigRequest;
    use Google\Analytics\Admin\V1alpha\SubpropertySyncConfig;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName Resource name of the SubpropertySyncConfig to lookup.
     *                              Format:
     *                              properties/{ordinary_property_id}/subpropertySyncConfigs/{subproperty_id}
     *                              Example: properties/1234/subpropertySyncConfigs/5678
     *                              Please see {@see AnalyticsAdminServiceClient::subpropertySyncConfigName()} for help formatting this field.
     */
    function get_subproperty_sync_config_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetSubpropertySyncConfigRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var SubpropertySyncConfig $response */
            $response = $analyticsAdminServiceClient->getSubpropertySyncConfig($request);
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
        $formattedName = AnalyticsAdminServiceClient::subpropertySyncConfigName(
            '[PROPERTY]',
            '[SUBPROPERTY_SYNC_CONFIG]'
        );
    
        get_subproperty_sync_config_sample($formattedName);
    }
    

### getUserProvidedDataSettings

Looks up settings related to user-provided data for a property.

The async variant is [AnalyticsAdminServiceClient::getUserProvidedDataSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__getUserProvidedDataSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetUserProvidedDataSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetUserProvidedDataSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\UserProvidedDataSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UserProvidedDataSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GetUserProvidedDataSettingsRequest;
    use Google\Analytics\Admin\V1alpha\UserProvidedDataSettings;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the user provided data settings to retrieve.
     *                              Format: properties/{property}/userProvidedDataSettings
     *                              Please see {@see AnalyticsAdminServiceClient::userProvidedDataSettingsName()} for help formatting this field.
     */
    function get_user_provided_data_settings_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetUserProvidedDataSettingsRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var UserProvidedDataSettings $response */
            $response = $analyticsAdminServiceClient->getUserProvidedDataSettings($request);
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
        $formattedName = AnalyticsAdminServiceClient::userProvidedDataSettingsName('[PROPERTY]');
    
        get_user_provided_data_settings_sample($formattedName);
    }
    

### listAccessBindings

Lists all access bindings on an account or property.

The async variant is [AnalyticsAdminServiceClient::listAccessBindingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listAccessBindingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAccessBindingsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\AccessBinding;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListAccessBindingsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Formats:
     *                                - accounts/{account}
     *                                - properties/{property}
     *                                Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     */
    function list_access_bindings_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListAccessBindingsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listAccessBindings($request);
    
            /** @var AccessBinding $element */
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
        $formattedParent = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
    
        list_access_bindings_sample($formattedParent);
    }
    

### listAccountSummaries

Returns summaries of all accounts accessible by the caller.

The async variant is [AnalyticsAdminServiceClient::listAccountSummariesAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listAccountSummariesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAccountSummariesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAccountSummariesRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\AccountSummary;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListAccountSummariesRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function list_account_summaries_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = new ListAccountSummariesRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listAccountSummaries($request);
    
            /** @var AccountSummary $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### listAccounts

Returns all accounts accessible by the caller.

Note that these accounts might not currently have GA properties. Soft-deleted (ie: "trashed") accounts are excluded by default. Returns an empty list if no relevant accounts are found.

The async variant is [AnalyticsAdminServiceClient::listAccountsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listAccountsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAccountsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAccountsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Account;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListAccountsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function list_accounts_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = new ListAccountsRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listAccounts($request);
    
            /** @var Account $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### listAdSenseLinks

Lists AdSenseLinks on a property.

The async variant is [AnalyticsAdminServiceClient::listAdSenseLinksAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listAdSenseLinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAdSenseLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAdSenseLinksRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\AdSenseLink;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListAdSenseLinksRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Resource name of the parent property.
     *                                Format: properties/{propertyId}
     *                                Example: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_ad_sense_links_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListAdSenseLinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listAdSenseLinks($request);
    
            /** @var AdSenseLink $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_ad_sense_links_sample($formattedParent);
    }
    

### listAudiences

Lists Audiences on a property.

Audiences created before 2020 may not be supported. Default audiences will not show filter definitions.

The async variant is [AnalyticsAdminServiceClient::listAudiencesAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listAudiencesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAudiencesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAudiencesRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Audience;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListAudiencesRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_audiences_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListAudiencesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listAudiences($request);
    
            /** @var Audience $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_audiences_sample($formattedParent);
    }
    

### listBigQueryLinks

Lists BigQuery Links on a property.

The async variant is [AnalyticsAdminServiceClient::listBigQueryLinksAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listBigQueryLinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListBigQueryLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListBigQueryLinksRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\BigQueryLink;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListBigQueryLinksRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The name of the property to list BigQuery links under.
     *                                Format: properties/{property_id}
     *                                Example: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_big_query_links_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListBigQueryLinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listBigQueryLinks($request);
    
            /** @var BigQueryLink $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_big_query_links_sample($formattedParent);
    }
    

### listCalculatedMetrics

Lists CalculatedMetrics on a property.

The async variant is [AnalyticsAdminServiceClient::listCalculatedMetricsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listCalculatedMetricsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListCalculatedMetricsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListCalculatedMetricsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\CalculatedMetric;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListCalculatedMetricsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_calculated_metrics_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListCalculatedMetricsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listCalculatedMetrics($request);
    
            /** @var CalculatedMetric $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_calculated_metrics_sample($formattedParent);
    }
    

### listChannelGroups

Lists ChannelGroups on a property.

The async variant is [AnalyticsAdminServiceClient::listChannelGroupsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listChannelGroupsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListChannelGroupsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListChannelGroupsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\ChannelGroup;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListChannelGroupsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The property for which to list ChannelGroups.
     *                                Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_channel_groups_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListChannelGroupsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listChannelGroups($request);
    
            /** @var ChannelGroup $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_channel_groups_sample($formattedParent);
    }
    

### listConversionEvents

Deprecated: Use `ListKeyEvents` instead.

Returns a list of conversion events in the specified parent property.

Returns an empty list if no conversion events are found.

The async variant is [AnalyticsAdminServiceClient::listConversionEventsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listConversionEventsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListConversionEventsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListConversionEventsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ConversionEvent;
    use Google\Analytics\Admin\V1alpha\ListConversionEventsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The resource name of the parent property.
     *                                Example: 'properties/123'
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_conversion_events_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListConversionEventsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listConversionEvents($request);
    
            /** @var ConversionEvent $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_conversion_events_sample($formattedParent);
    }
    

### listCustomDimensions

Lists CustomDimensions on a property.

The async variant is [AnalyticsAdminServiceClient::listCustomDimensionsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listCustomDimensionsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListCustomDimensionsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListCustomDimensionsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CustomDimension;
    use Google\Analytics\Admin\V1alpha\ListCustomDimensionsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_custom_dimensions_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListCustomDimensionsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listCustomDimensions($request);
    
            /** @var CustomDimension $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_custom_dimensions_sample($formattedParent);
    }
    

### listCustomMetrics

Lists CustomMetrics on a property.

The async variant is [AnalyticsAdminServiceClient::listCustomMetricsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listCustomMetricsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListCustomMetricsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListCustomMetricsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CustomMetric;
    use Google\Analytics\Admin\V1alpha\ListCustomMetricsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_custom_metrics_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListCustomMetricsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listCustomMetrics($request);
    
            /** @var CustomMetric $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_custom_metrics_sample($formattedParent);
    }
    

### listDataStreams

Lists DataStreams on a property.

The async variant is [AnalyticsAdminServiceClient::listDataStreamsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listDataStreamsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListDataStreamsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListDataStreamsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataStream;
    use Google\Analytics\Admin\V1alpha\ListDataStreamsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_data_streams_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListDataStreamsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listDataStreams($request);
    
            /** @var DataStream $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_data_streams_sample($formattedParent);
    }
    

### listDisplayVideo360AdvertiserLinkProposals

Lists DisplayVideo360AdvertiserLinkProposals on a property.

The async variant is [AnalyticsAdminServiceClient::listDisplayVideo360AdvertiserLinkProposalsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listDisplayVideo360AdvertiserLinkProposalsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListDisplayVideo360AdvertiserLinkProposalsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListDisplayVideo360AdvertiserLinkProposalsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal;
    use Google\Analytics\Admin\V1alpha\ListDisplayVideo360AdvertiserLinkProposalsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_display_video360_advertiser_link_proposals_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListDisplayVideo360AdvertiserLinkProposalsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listDisplayVideo360AdvertiserLinkProposals($request);
    
            /** @var DisplayVideo360AdvertiserLinkProposal $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_display_video360_advertiser_link_proposals_sample($formattedParent);
    }
    

### listDisplayVideo360AdvertiserLinks

Lists all DisplayVideo360AdvertiserLinks on a property.

The async variant is [AnalyticsAdminServiceClient::listDisplayVideo360AdvertiserLinksAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listDisplayVideo360AdvertiserLinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListDisplayVideo360AdvertiserLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListDisplayVideo360AdvertiserLinksRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink;
    use Google\Analytics\Admin\V1alpha\ListDisplayVideo360AdvertiserLinksRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_display_video360_advertiser_links_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListDisplayVideo360AdvertiserLinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listDisplayVideo360AdvertiserLinks($request);
    
            /** @var DisplayVideo360AdvertiserLink $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_display_video360_advertiser_links_sample($formattedParent);
    }
    

### listEventCreateRules

Lists EventCreateRules on a web data stream.

The async variant is [AnalyticsAdminServiceClient::listEventCreateRulesAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listEventCreateRulesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListEventCreateRulesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListEventCreateRulesRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EventCreateRule;
    use Google\Analytics\Admin\V1alpha\ListEventCreateRulesRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/123/dataStreams/456
     *                                Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     */
    function list_event_create_rules_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListEventCreateRulesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listEventCreateRules($request);
    
            /** @var EventCreateRule $element */
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
    
        list_event_create_rules_sample($formattedParent);
    }
    

### listEventEditRules

Lists EventEditRules on a web data stream.

The async variant is [AnalyticsAdminServiceClient::listEventEditRulesAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listEventEditRulesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListEventEditRulesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListEventEditRulesRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EventEditRule;
    use Google\Analytics\Admin\V1alpha\ListEventEditRulesRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/123/dataStreams/456
     *                                Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     */
    function list_event_edit_rules_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListEventEditRulesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listEventEditRules($request);
    
            /** @var EventEditRule $element */
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
    
        list_event_edit_rules_sample($formattedParent);
    }
    

### listExpandedDataSets

Lists ExpandedDataSets on a property.

The async variant is [AnalyticsAdminServiceClient::listExpandedDataSetsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listExpandedDataSetsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListExpandedDataSetsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListExpandedDataSetsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ExpandedDataSet;
    use Google\Analytics\Admin\V1alpha\ListExpandedDataSetsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_expanded_data_sets_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListExpandedDataSetsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listExpandedDataSets($request);
    
            /** @var ExpandedDataSet $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_expanded_data_sets_sample($formattedParent);
    }
    

### listFirebaseLinks

Lists FirebaseLinks on a property.

Properties can have at most one FirebaseLink.

The async variant is [AnalyticsAdminServiceClient::listFirebaseLinksAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listFirebaseLinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListFirebaseLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListFirebaseLinksRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\FirebaseLink;
    use Google\Analytics\Admin\V1alpha\ListFirebaseLinksRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Format: properties/{property_id}
     *
     *                                Example: `properties/1234`
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_firebase_links_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListFirebaseLinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listFirebaseLinks($request);
    
            /** @var FirebaseLink $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_firebase_links_sample($formattedParent);
    }
    

### listGoogleAdsLinks

Lists GoogleAdsLinks on a property.

The async variant is [AnalyticsAdminServiceClient::listGoogleAdsLinksAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listGoogleAdsLinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListGoogleAdsLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListGoogleAdsLinksRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GoogleAdsLink;
    use Google\Analytics\Admin\V1alpha\ListGoogleAdsLinksRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_google_ads_links_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListGoogleAdsLinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listGoogleAdsLinks($request);
    
            /** @var GoogleAdsLink $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_google_ads_links_sample($formattedParent);
    }
    

### listKeyEvents

Returns a list of Key Events in the specified parent property.

Returns an empty list if no Key Events are found.

The async variant is [AnalyticsAdminServiceClient::listKeyEventsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listKeyEventsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListKeyEventsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListKeyEventsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\KeyEvent;
    use Google\Analytics\Admin\V1alpha\ListKeyEventsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The resource name of the parent property.
     *                                Example: 'properties/123'
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_key_events_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListKeyEventsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listKeyEvents($request);
    
            /** @var KeyEvent $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_key_events_sample($formattedParent);
    }
    

### listMeasurementProtocolSecrets

Returns child MeasurementProtocolSecrets under the specified parent Property.

The async variant is [AnalyticsAdminServiceClient::listMeasurementProtocolSecretsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listMeasurementProtocolSecretsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListMeasurementProtocolSecretsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListMeasurementProtocolSecretsRequest;
    use Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The resource name of the parent stream.
     *                                Format:
     *                                properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets
     *                                Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     */
    function list_measurement_protocol_secrets_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListMeasurementProtocolSecretsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listMeasurementProtocolSecrets($request);
    
            /** @var MeasurementProtocolSecret $element */
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
    
        list_measurement_protocol_secrets_sample($formattedParent);
    }
    

### listProperties

Returns child Properties under the specified parent Account.

Properties will be excluded if the caller does not have access. Soft-deleted (ie: "trashed") properties are excluded by default. Returns an empty list if no relevant properties are found.

The async variant is [AnalyticsAdminServiceClient::listPropertiesAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listPropertiesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListPropertiesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListPropertiesRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListPropertiesRequest;
    use Google\Analytics\Admin\V1alpha\Property;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $filter An expression for filtering the results of the request.
     *                       Fields eligible for filtering are:
     *                       `parent:`(The resource name of the parent account/property) or
     *                       `ancestor:`(The resource name of the parent account) or
     *                       `firebase_project:`(The id or number of the linked firebase project).
     *                       Some examples of filters:
     *
     *                       ```
     *                       | Filter                      | Description                               |
     *                       |-----------------------------|-------------------------------------------|
     *                       | parent:accounts/123         | The account with account id: 123.       |
     *                       | parent:properties/123       | The property with property id: 123.       |
     *                       | ancestor:accounts/123       | The account with account id: 123.         |
     *                       | firebase_project:project-id | The firebase project with id: project-id. |
     *                       | firebase_project:123        | The firebase project with number: 123.    |
     *                       ```
     */
    function list_properties_sample(string $filter): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListPropertiesRequest())
            ->setFilter($filter);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listProperties($request);
    
            /** @var Property $element */
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
        $filter = '[FILTER]';
    
        list_properties_sample($filter);
    }
    

### listReportingDataAnnotations

List all Reporting Data Annotations on a property.

The async variant is [AnalyticsAdminServiceClient::listReportingDataAnnotationsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listReportingDataAnnotationsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListReportingDataAnnotationsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListReportingDataAnnotationsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListReportingDataAnnotationsRequest;
    use Google\Analytics\Admin\V1alpha\ReportingDataAnnotation;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Resource name of the property.
     *                                Format: properties/property_id
     *                                Example: properties/123
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_reporting_data_annotations_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListReportingDataAnnotationsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listReportingDataAnnotations($request);
    
            /** @var ReportingDataAnnotation $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_reporting_data_annotations_sample($formattedParent);
    }
    

### listRollupPropertySourceLinks

Lists roll-up property source Links on a property.

Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

The async variant is [AnalyticsAdminServiceClient::listRollupPropertySourceLinksAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listRollupPropertySourceLinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListRollupPropertySourceLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListRollupPropertySourceLinksRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListRollupPropertySourceLinksRequest;
    use Google\Analytics\Admin\V1alpha\RollupPropertySourceLink;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The name of the roll-up property to list roll-up property source
     *                                links under. Format: properties/{property_id} Example: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_rollup_property_source_links_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListRollupPropertySourceLinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listRollupPropertySourceLinks($request);
    
            /** @var RollupPropertySourceLink $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_rollup_property_source_links_sample($formattedParent);
    }
    

### listSKAdNetworkConversionValueSchemas

Lists SKAdNetworkConversionValueSchema on a stream.

Properties can have at most one SKAdNetworkConversionValueSchema.

The async variant is [AnalyticsAdminServiceClient::listSKAdNetworkConversionValueSchemasAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listSKAdNetworkConversionValueSchemasAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSKAdNetworkConversionValueSchemasRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSKAdNetworkConversionValueSchemasRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListSKAdNetworkConversionValueSchemasRequest;
    use Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The DataStream resource to list schemas for.
     *                                Format:
     *                                properties/{property_id}/dataStreams/{dataStream}
     *                                Example: properties/1234/dataStreams/5678
     *                                Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     */
    function list_sk_ad_network_conversion_value_schemas_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListSKAdNetworkConversionValueSchemasRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listSKAdNetworkConversionValueSchemas($request);
    
            /** @var SKAdNetworkConversionValueSchema $element */
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
    
        list_sk_ad_network_conversion_value_schemas_sample($formattedParent);
    }
    

### listSearchAds360Links

Lists all SearchAds360Links on a property.

The async variant is [AnalyticsAdminServiceClient::listSearchAds360LinksAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listSearchAds360LinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSearchAds360LinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSearchAds360LinksRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListSearchAds360LinksRequest;
    use Google\Analytics\Admin\V1alpha\SearchAds360Link;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Example format: properties/1234
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_search_ads360_links_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListSearchAds360LinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listSearchAds360Links($request);
    
            /** @var SearchAds360Link $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_search_ads360_links_sample($formattedParent);
    }
    

### listSubpropertyEventFilters

List all subproperty Event Filters on a property.

The async variant is [AnalyticsAdminServiceClient::listSubpropertyEventFiltersAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listSubpropertyEventFiltersAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSubpropertyEventFiltersRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSubpropertyEventFiltersRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListSubpropertyEventFiltersRequest;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilter;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Resource name of the ordinary property.
     *                                Format: properties/property_id
     *                                Example: properties/123
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_subproperty_event_filters_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListSubpropertyEventFiltersRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listSubpropertyEventFilters($request);
    
            /** @var SubpropertyEventFilter $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_subproperty_event_filters_sample($formattedParent);
    }
    

### listSubpropertySyncConfigs

List all `SubpropertySyncConfig` resources for a property.

The async variant is [AnalyticsAdminServiceClient::listSubpropertySyncConfigsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__listSubpropertySyncConfigsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSubpropertySyncConfigsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSubpropertySyncConfigsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ListSubpropertySyncConfigsRequest;
    use Google\Analytics\Admin\V1alpha\SubpropertySyncConfig;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent Resource name of the property.
     *                                Format: properties/property_id
     *                                Example: properties/123
     *                                Please see {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function list_subproperty_sync_configs_sample(string $formattedParent): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListSubpropertySyncConfigsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->listSubpropertySyncConfigs($request);
    
            /** @var SubpropertySyncConfig $element */
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
        $formattedParent = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        list_subproperty_sync_configs_sample($formattedParent);
    }
    

### provisionAccountTicket

Requests a ticket for creating an account.

The async variant is [AnalyticsAdminServiceClient::provisionAccountTicketAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__provisionAccountTicketAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ProvisionAccountTicketRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionAccountTicketRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ProvisionAccountTicketResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionAccountTicketResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ProvisionAccountTicketRequest;
    use Google\Analytics\Admin\V1alpha\ProvisionAccountTicketResponse;
    use Google\ApiCore\ApiException;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function provision_account_ticket_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = new ProvisionAccountTicketRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var ProvisionAccountTicketResponse $response */
            $response = $analyticsAdminServiceClient->provisionAccountTicket($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### provisionSubproperty

Create a subproperty and a subproperty event filter that applies to the created subproperty.

The async variant is [AnalyticsAdminServiceClient::provisionSubpropertyAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__provisionSubpropertyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ProvisionSubpropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionSubpropertyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ProvisionSubpropertyResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionSubpropertyResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\Property;
    use Google\Analytics\Admin\V1alpha\ProvisionSubpropertyRequest;
    use Google\Analytics\Admin\V1alpha\ProvisionSubpropertyResponse;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $subpropertyDisplayName Human-readable display name for this property.
     *
     *                                       The max allowed display name length is 100 UTF-16 code units.
     * @param string $subpropertyTimeZone    Reporting Time Zone, used as the day boundary for reports,
     *                                       regardless of where the data originates. If the time zone honors DST,
     *                                       Analytics will automatically adjust for the changes.
     *
     *                                       NOTE: Changing the time zone only affects data going forward, and is not
     *                                       applied retroactively.
     *
     *                                       Format: https://www.iana.org/time-zones
     *                                       Example: "America/Los_Angeles"
     */
    function provision_subproperty_sample(
        string $subpropertyDisplayName,
        string $subpropertyTimeZone
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $subproperty = (new Property())
            ->setDisplayName($subpropertyDisplayName)
            ->setTimeZone($subpropertyTimeZone);
        $request = (new ProvisionSubpropertyRequest())
            ->setSubproperty($subproperty);
    
        // Call the API and handle any network failures.
        try {
            /** @var ProvisionSubpropertyResponse $response */
            $response = $analyticsAdminServiceClient->provisionSubproperty($request);
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
        $subpropertyDisplayName = '[DISPLAY_NAME]';
        $subpropertyTimeZone = '[TIME_ZONE]';
    
        provision_subproperty_sample($subpropertyDisplayName, $subpropertyTimeZone);
    }
    

### reorderEventEditRules

Changes the processing order of event edit rules on the specified stream.

The async variant is [AnalyticsAdminServiceClient::reorderEventEditRulesAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__reorderEventEditRulesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ReorderEventEditRulesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReorderEventEditRulesRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ReorderEventEditRulesRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent       Example format: properties/123/dataStreams/456
     *                                      Please see {@see AnalyticsAdminServiceClient::dataStreamName()} for help formatting this field.
     * @param string $eventEditRulesElement EventEditRule resource names for the specified data stream, in
     *                                      the needed processing order. All EventEditRules for the stream must be
     *                                      present in the list.
     */
    function reorder_event_edit_rules_sample(
        string $formattedParent,
        string $eventEditRulesElement
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $eventEditRules = [$eventEditRulesElement,];
        $request = (new ReorderEventEditRulesRequest())
            ->setParent($formattedParent)
            ->setEventEditRules($eventEditRules);
    
        // Call the API and handle any network failures.
        try {
            $analyticsAdminServiceClient->reorderEventEditRules($request);
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
        $formattedParent = AnalyticsAdminServiceClient::dataStreamName('[PROPERTY]', '[DATA_STREAM]');
        $eventEditRulesElement = '[EVENT_EDIT_RULES]';
    
        reorder_event_edit_rules_sample($formattedParent, $eventEditRulesElement);
    }
    

### runAccessReport

Returns a customized report of data access records. The report provides records of each time a user reads Google Analytics reporting data. Access records are retained for up to 2 years.

Data Access Reports can be requested for a property. Reports may be requested for any property, but dimensions that aren't related to quota can only be requested on Google Analytics 360 properties. This method is only available to Administrators.

These data access records include GA UI Reporting, GA UI Explorations, GA Data API, and other products like Firebase & Admob that can retrieve data from Google Analytics through a linkage. These records don't include property configuration changes like adding a stream or changing a property's time zone. For configuration change history, see [searchChangeHistoryEvents](https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/searchChangeHistoryEvents).

To give your feedback on this API, complete the [Google Analytics Access Reports feedback](https://docs.google.com/forms/d/e/1FAIpQLSdmEBUrMzAEdiEKk5TV5dEHvDUZDRlgWYdQdAeSdtR4hVjEhw/viewform) form.

The async variant is [AnalyticsAdminServiceClient::runAccessReportAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__runAccessReportAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\RunAccessReportRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RunAccessReportRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\RunAccessReportResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RunAccessReportResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\RunAccessReportRequest;
    use Google\Analytics\Admin\V1alpha\RunAccessReportResponse;
    use Google\ApiCore\ApiException;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function run_access_report_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = new RunAccessReportRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var RunAccessReportResponse $response */
            $response = $analyticsAdminServiceClient->runAccessReport($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### searchChangeHistoryEvents

Searches through all changes to an account or its children given the specified set of filters.

Only returns the subset of changes supported by the API. The UI may return additional changes.

The async variant is [AnalyticsAdminServiceClient::searchChangeHistoryEventsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__searchChangeHistoryEventsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\SearchChangeHistoryEventsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchChangeHistoryEventsRequest)`   
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
    
    
    use Google\Analytics\Admin\V1alpha\ChangeHistoryEvent;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\SearchChangeHistoryEventsRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedAccount The account resource for which to return change history
     *                                 resources. Format: accounts/{account}
     *
     *                                 Example: `accounts/100`
     *                                 Please see {@see AnalyticsAdminServiceClient::accountName()} for help formatting this field.
     */
    function search_change_history_events_sample(string $formattedAccount): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new SearchChangeHistoryEventsRequest())
            ->setAccount($formattedAccount);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $analyticsAdminServiceClient->searchChangeHistoryEvents($request);
    
            /** @var ChangeHistoryEvent $element */
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
        $formattedAccount = AnalyticsAdminServiceClient::accountName('[ACCOUNT]');
    
        search_change_history_events_sample($formattedAccount);
    }
    

### submitUserDeletion

Submits a request for user deletion for a property.

The async variant is [AnalyticsAdminServiceClient::submitUserDeletionAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__submitUserDeletionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\SubmitUserDeletionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubmitUserDeletionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SubmitUserDeletionResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubmitUserDeletionResponse)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\SubmitUserDeletionRequest;
    use Google\Analytics\Admin\V1alpha\SubmitUserDeletionResponse;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the property to submit user deletion for. Please see
     *                              {@see AnalyticsAdminServiceClient::propertyName()} for help formatting this field.
     */
    function submit_user_deletion_sample(string $formattedName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $request = (new SubmitUserDeletionRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var SubmitUserDeletionResponse $response */
            $response = $analyticsAdminServiceClient->submitUserDeletion($request);
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
        $formattedName = AnalyticsAdminServiceClient::propertyName('[PROPERTY]');
    
        submit_user_deletion_sample($formattedName);
    }
    

### updateAccessBinding

Updates an access binding on an account or property.

The async variant is [AnalyticsAdminServiceClient::updateAccessBindingAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateAccessBindingAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAccessBindingRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AccessBinding](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessBinding)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AccessBinding;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\UpdateAccessBindingRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_access_binding_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $accessBinding = new AccessBinding();
        $request = (new UpdateAccessBindingRequest())
            ->setAccessBinding($accessBinding);
    
        // Call the API and handle any network failures.
        try {
            /** @var AccessBinding $response */
            $response = $analyticsAdminServiceClient->updateAccessBinding($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateAccount

Updates an account.

The async variant is [AnalyticsAdminServiceClient::updateAccountAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateAccountAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAccountRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAccountRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Account](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Account)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Account;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\UpdateAccountRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $accountDisplayName Human-readable display name for this account.
     */
    function update_account_sample(string $accountDisplayName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $account = (new Account())
            ->setDisplayName($accountDisplayName);
        $updateMask = new FieldMask();
        $request = (new UpdateAccountRequest())
            ->setAccount($account)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var Account $response */
            $response = $analyticsAdminServiceClient->updateAccount($request);
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
        $accountDisplayName = '[DISPLAY_NAME]';
    
        update_account_sample($accountDisplayName);
    }
    

### updateAttributionSettings

Updates attribution settings on a property.

The async variant is [AnalyticsAdminServiceClient::updateAttributionSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateAttributionSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAttributionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAttributionSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AttributionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\AttributionSettings;
    use Google\Analytics\Admin\V1alpha\AttributionSettings\AcquisitionConversionEventLookbackWindow;
    use Google\Analytics\Admin\V1alpha\AttributionSettings\AdsWebConversionDataExportScope;
    use Google\Analytics\Admin\V1alpha\AttributionSettings\OtherConversionEventLookbackWindow;
    use Google\Analytics\Admin\V1alpha\AttributionSettings\ReportingAttributionModel;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\UpdateAttributionSettingsRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param int $attributionSettingsAcquisitionConversionEventLookbackWindow The lookback window configuration for acquisition conversion
     *                                                                         events. The default window size is 30 days.
     * @param int $attributionSettingsOtherConversionEventLookbackWindow       The lookback window for all other, non-acquisition conversion
     *                                                                         events. The default window size is 90 days.
     * @param int $attributionSettingsReportingAttributionModel                The reporting attribution model used to calculate conversion
     *                                                                         credit in this property's reports.
     *
     *                                                                         Changing the attribution model will apply to both historical and future
     *                                                                         data. These changes will be reflected in reports with conversion and
     *                                                                         revenue data. User and session data will be unaffected.
     * @param int $attributionSettingsAdsWebConversionDataExportScope          The Conversion Export Scope for data exported to linked Ads
     *                                                                         Accounts.
     */
    function update_attribution_settings_sample(
        int $attributionSettingsAcquisitionConversionEventLookbackWindow,
        int $attributionSettingsOtherConversionEventLookbackWindow,
        int $attributionSettingsReportingAttributionModel,
        int $attributionSettingsAdsWebConversionDataExportScope
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $attributionSettings = (new AttributionSettings())
            ->setAcquisitionConversionEventLookbackWindow(
                $attributionSettingsAcquisitionConversionEventLookbackWindow
            )
            ->setOtherConversionEventLookbackWindow($attributionSettingsOtherConversionEventLookbackWindow)
            ->setReportingAttributionModel($attributionSettingsReportingAttributionModel)
            ->setAdsWebConversionDataExportScope($attributionSettingsAdsWebConversionDataExportScope);
        $updateMask = new FieldMask();
        $request = (new UpdateAttributionSettingsRequest())
            ->setAttributionSettings($attributionSettings)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var AttributionSettings $response */
            $response = $analyticsAdminServiceClient->updateAttributionSettings($request);
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
        $attributionSettingsAcquisitionConversionEventLookbackWindow = AcquisitionConversionEventLookbackWindow::ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED;
        $attributionSettingsOtherConversionEventLookbackWindow = OtherConversionEventLookbackWindow::OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED;
        $attributionSettingsReportingAttributionModel = ReportingAttributionModel::REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED;
        $attributionSettingsAdsWebConversionDataExportScope = AdsWebConversionDataExportScope::ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED;
    
        update_attribution_settings_sample(
            $attributionSettingsAcquisitionConversionEventLookbackWindow,
            $attributionSettingsOtherConversionEventLookbackWindow,
            $attributionSettingsReportingAttributionModel,
            $attributionSettingsAdsWebConversionDataExportScope
        );
    }
    

### updateAudience

Updates an Audience on a property.

The async variant is [AnalyticsAdminServiceClient::updateAudienceAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateAudienceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAudienceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Audience;
    use Google\Analytics\Admin\V1alpha\AudienceFilterClause;
    use Google\Analytics\Admin\V1alpha\AudienceFilterClause\AudienceClauseType;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\UpdateAudienceRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $audienceDisplayName             The display name of the Audience.
     * @param string $audienceDescription             The description of the Audience.
     * @param int    $audienceMembershipDurationDays  Immutable. The duration a user should stay in an Audience. It
     *                                                cannot be set to more than 540 days.
     * @param int    $audienceFilterClausesClauseType Specifies whether this is an include or exclude filter clause.
     */
    function update_audience_sample(
        string $audienceDisplayName,
        string $audienceDescription,
        int $audienceMembershipDurationDays,
        int $audienceFilterClausesClauseType
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $audienceFilterClause = (new AudienceFilterClause())
            ->setClauseType($audienceFilterClausesClauseType);
        $audienceFilterClauses = [$audienceFilterClause,];
        $audience = (new Audience())
            ->setDisplayName($audienceDisplayName)
            ->setDescription($audienceDescription)
            ->setMembershipDurationDays($audienceMembershipDurationDays)
            ->setFilterClauses($audienceFilterClauses);
        $updateMask = new FieldMask();
        $request = (new UpdateAudienceRequest())
            ->setAudience($audience)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var Audience $response */
            $response = $analyticsAdminServiceClient->updateAudience($request);
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
        $audienceDisplayName = '[DISPLAY_NAME]';
        $audienceDescription = '[DESCRIPTION]';
        $audienceMembershipDurationDays = 0;
        $audienceFilterClausesClauseType = AudienceClauseType::AUDIENCE_CLAUSE_TYPE_UNSPECIFIED;
    
        update_audience_sample(
            $audienceDisplayName,
            $audienceDescription,
            $audienceMembershipDurationDays,
            $audienceFilterClausesClauseType
        );
    }
    

### updateBigQueryLink

Updates a BigQueryLink.

The async variant is [AnalyticsAdminServiceClient::updateBigQueryLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateBigQueryLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateBigQueryLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\BigQueryLink;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\UpdateBigQueryLinkRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $bigqueryLinkDatasetLocation Immutable. The geographic location where the created BigQuery
     *                                            dataset should reside. See https://cloud.google.com/bigquery/docs/locations
     *                                            for supported locations.
     */
    function update_big_query_link_sample(string $bigqueryLinkDatasetLocation): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $bigqueryLink = (new BigQueryLink())
            ->setDatasetLocation($bigqueryLinkDatasetLocation);
        $updateMask = new FieldMask();
        $request = (new UpdateBigQueryLinkRequest())
            ->setBigqueryLink($bigqueryLink)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var BigQueryLink $response */
            $response = $analyticsAdminServiceClient->updateBigQueryLink($request);
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
        $bigqueryLinkDatasetLocation = '[DATASET_LOCATION]';
    
        update_big_query_link_sample($bigqueryLinkDatasetLocation);
    }
    

### updateCalculatedMetric

Updates a CalculatedMetric on a property.

The async variant is [AnalyticsAdminServiceClient::updateCalculatedMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateCalculatedMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateCalculatedMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\CalculatedMetric;
    use Google\Analytics\Admin\V1alpha\CalculatedMetric\MetricUnit;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\UpdateCalculatedMetricRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $calculatedMetricDisplayName Display name for this calculated metric as shown in the
     *                                            Google Analytics UI. Max length 82 characters.
     * @param int    $calculatedMetricMetricUnit  The type for the calculated metric's value.
     * @param string $calculatedMetricFormula     The calculated metric's definition. Maximum number of unique
     *                                            referenced custom metrics is 5. Formulas supports the following operations:
     *                                            + (addition),  - (subtraction), - (negative),  * (multiplication), /
     *                                            (division), () (parenthesis). Any valid real numbers are acceptable that
     *                                            fit in a Long (64bit integer) or a Double (64 bit floating point number).
     *                                            Example formula:
     *                                            "( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0"
     */
    function update_calculated_metric_sample(
        string $calculatedMetricDisplayName,
        int $calculatedMetricMetricUnit,
        string $calculatedMetricFormula
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $calculatedMetric = (new CalculatedMetric())
            ->setDisplayName($calculatedMetricDisplayName)
            ->setMetricUnit($calculatedMetricMetricUnit)
            ->setFormula($calculatedMetricFormula);
        $updateMask = new FieldMask();
        $request = (new UpdateCalculatedMetricRequest())
            ->setCalculatedMetric($calculatedMetric)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var CalculatedMetric $response */
            $response = $analyticsAdminServiceClient->updateCalculatedMetric($request);
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
        $calculatedMetricDisplayName = '[DISPLAY_NAME]';
        $calculatedMetricMetricUnit = MetricUnit::METRIC_UNIT_UNSPECIFIED;
        $calculatedMetricFormula = '[FORMULA]';
    
        update_calculated_metric_sample(
            $calculatedMetricDisplayName,
            $calculatedMetricMetricUnit,
            $calculatedMetricFormula
        );
    }
    

### updateChannelGroup

Updates a ChannelGroup.

The async variant is [AnalyticsAdminServiceClient::updateChannelGroupAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateChannelGroupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateChannelGroupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\ChannelGroup;
    use Google\Analytics\Admin\V1alpha\ChannelGroupFilterExpression;
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GroupingRule;
    use Google\Analytics\Admin\V1alpha\UpdateChannelGroupRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $channelGroupDisplayName             The display name of the Channel Group. Max length of 80
     *                                                    characters.
     * @param string $channelGroupGroupingRuleDisplayName Customer defined display name for the channel.
     */
    function update_channel_group_sample(
        string $channelGroupDisplayName,
        string $channelGroupGroupingRuleDisplayName
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $channelGroupGroupingRuleExpression = new ChannelGroupFilterExpression();
        $groupingRule = (new GroupingRule())
            ->setDisplayName($channelGroupGroupingRuleDisplayName)
            ->setExpression($channelGroupGroupingRuleExpression);
        $channelGroupGroupingRule = [$groupingRule,];
        $channelGroup = (new ChannelGroup())
            ->setDisplayName($channelGroupDisplayName)
            ->setGroupingRule($channelGroupGroupingRule);
        $updateMask = new FieldMask();
        $request = (new UpdateChannelGroupRequest())
            ->setChannelGroup($channelGroup)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var ChannelGroup $response */
            $response = $analyticsAdminServiceClient->updateChannelGroup($request);
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
        $channelGroupDisplayName = '[DISPLAY_NAME]';
        $channelGroupGroupingRuleDisplayName = '[DISPLAY_NAME]';
    
        update_channel_group_sample($channelGroupDisplayName, $channelGroupGroupingRuleDisplayName);
    }
    

### updateConversionEvent

Deprecated: Use `UpdateKeyEvent` instead.

Updates a conversion event with the specified attributes.

The async variant is [AnalyticsAdminServiceClient::updateConversionEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateConversionEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateConversionEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ConversionEvent;
    use Google\Analytics\Admin\V1alpha\UpdateConversionEventRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_conversion_event_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $conversionEvent = new ConversionEvent();
        $updateMask = new FieldMask();
        $request = (new UpdateConversionEventRequest())
            ->setConversionEvent($conversionEvent)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var ConversionEvent $response */
            $response = $analyticsAdminServiceClient->updateConversionEvent($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateCustomDimension

Updates a CustomDimension on a property.

The async variant is [AnalyticsAdminServiceClient::updateCustomDimensionAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateCustomDimensionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateCustomDimensionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CustomDimension;
    use Google\Analytics\Admin\V1alpha\UpdateCustomDimensionRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_custom_dimension_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $request = (new UpdateCustomDimensionRequest())
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var CustomDimension $response */
            $response = $analyticsAdminServiceClient->updateCustomDimension($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateCustomMetric

Updates a CustomMetric on a property.

The async variant is [AnalyticsAdminServiceClient::updateCustomMetricAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateCustomMetricAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateCustomMetricRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\CustomMetric;
    use Google\Analytics\Admin\V1alpha\UpdateCustomMetricRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_custom_metric_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $request = (new UpdateCustomMetricRequest())
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var CustomMetric $response */
            $response = $analyticsAdminServiceClient->updateCustomMetric($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateDataRedactionSettings

Updates a DataRedactionSettings on a property.

The async variant is [AnalyticsAdminServiceClient::updateDataRedactionSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateDataRedactionSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDataRedactionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDataRedactionSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataRedactionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRedactionSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataRedactionSettings;
    use Google\Analytics\Admin\V1alpha\UpdateDataRedactionSettingsRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_data_redaction_settings_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $dataRedactionSettings = new DataRedactionSettings();
        $updateMask = new FieldMask();
        $request = (new UpdateDataRedactionSettingsRequest())
            ->setDataRedactionSettings($dataRedactionSettings)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataRedactionSettings $response */
            $response = $analyticsAdminServiceClient->updateDataRedactionSettings($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateDataRetentionSettings

Updates the singleton data retention settings for this property.

The async variant is [AnalyticsAdminServiceClient::updateDataRetentionSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateDataRetentionSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDataRetentionSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataRetentionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataRetentionSettings;
    use Google\Analytics\Admin\V1alpha\DataRetentionSettings\RetentionDuration;
    use Google\Analytics\Admin\V1alpha\UpdateDataRetentionSettingsRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param int $dataRetentionSettingsEventDataRetention The length of time that event-level data is retained.
     * @param int $dataRetentionSettingsUserDataRetention  The length of time that user-level data is retained.
     */
    function update_data_retention_settings_sample(
        int $dataRetentionSettingsEventDataRetention,
        int $dataRetentionSettingsUserDataRetention
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $dataRetentionSettings = (new DataRetentionSettings())
            ->setEventDataRetention($dataRetentionSettingsEventDataRetention)
            ->setUserDataRetention($dataRetentionSettingsUserDataRetention);
        $updateMask = new FieldMask();
        $request = (new UpdateDataRetentionSettingsRequest())
            ->setDataRetentionSettings($dataRetentionSettings)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataRetentionSettings $response */
            $response = $analyticsAdminServiceClient->updateDataRetentionSettings($request);
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
        $dataRetentionSettingsEventDataRetention = RetentionDuration::RETENTION_DURATION_UNSPECIFIED;
        $dataRetentionSettingsUserDataRetention = RetentionDuration::RETENTION_DURATION_UNSPECIFIED;
    
        update_data_retention_settings_sample(
            $dataRetentionSettingsEventDataRetention,
            $dataRetentionSettingsUserDataRetention
        );
    }
    

### updateDataStream

Updates a DataStream on a property.

The async variant is [AnalyticsAdminServiceClient::updateDataStreamAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateDataStreamAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDataStreamRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DataStream;
    use Google\Analytics\Admin\V1alpha\UpdateDataStreamRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_data_stream_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $request = (new UpdateDataStreamRequest())
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataStream $response */
            $response = $analyticsAdminServiceClient->updateDataStream($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateDisplayVideo360AdvertiserLink

Updates a DisplayVideo360AdvertiserLink on a property.

The async variant is [AnalyticsAdminServiceClient::updateDisplayVideo360AdvertiserLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateDisplayVideo360AdvertiserLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDisplayVideo360AdvertiserLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink;
    use Google\Analytics\Admin\V1alpha\UpdateDisplayVideo360AdvertiserLinkRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_display_video360_advertiser_link_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $request = (new UpdateDisplayVideo360AdvertiserLinkRequest())
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var DisplayVideo360AdvertiserLink $response */
            $response = $analyticsAdminServiceClient->updateDisplayVideo360AdvertiserLink($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateEnhancedMeasurementSettings

Updates the enhanced measurement settings for this data stream.

Note that the stream must enable enhanced measurement for these settings to take effect.

The async variant is [AnalyticsAdminServiceClient::updateEnhancedMeasurementSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateEnhancedMeasurementSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateEnhancedMeasurementSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings;
    use Google\Analytics\Admin\V1alpha\UpdateEnhancedMeasurementSettingsRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $enhancedMeasurementSettingsSearchQueryParameter URL query parameters to interpret as site search parameters.
     *                                                                Max length is 1024 characters. Must not be empty.
     */
    function update_enhanced_measurement_settings_sample(
        string $enhancedMeasurementSettingsSearchQueryParameter
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $enhancedMeasurementSettings = (new EnhancedMeasurementSettings())
            ->setSearchQueryParameter($enhancedMeasurementSettingsSearchQueryParameter);
        $updateMask = new FieldMask();
        $request = (new UpdateEnhancedMeasurementSettingsRequest())
            ->setEnhancedMeasurementSettings($enhancedMeasurementSettings)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var EnhancedMeasurementSettings $response */
            $response = $analyticsAdminServiceClient->updateEnhancedMeasurementSettings($request);
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
        $enhancedMeasurementSettingsSearchQueryParameter = '[SEARCH_QUERY_PARAMETER]';
    
        update_enhanced_measurement_settings_sample($enhancedMeasurementSettingsSearchQueryParameter);
    }
    

### updateEventCreateRule

Updates an EventCreateRule.

The async variant is [AnalyticsAdminServiceClient::updateEventCreateRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateEventCreateRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateEventCreateRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EventCreateRule;
    use Google\Analytics\Admin\V1alpha\MatchingCondition;
    use Google\Analytics\Admin\V1alpha\MatchingCondition\ComparisonType;
    use Google\Analytics\Admin\V1alpha\UpdateEventCreateRuleRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $eventCreateRuleDestinationEvent              The name of the new event to be created.
     *
     *                                                             This value must:
     *                                                             * be less than 40 characters
     *                                                             * consist only of letters, digits or _ (underscores)
     *                                                             * start with a letter
     * @param string $eventCreateRuleEventConditionsField          The name of the field that is compared against for the condition.
     *                                                             If 'event_name' is specified this condition will apply to the name of the
     *                                                             event.  Otherwise the condition will apply to a parameter with the
     *                                                             specified name.
     *
     *                                                             This value cannot contain spaces.
     * @param int    $eventCreateRuleEventConditionsComparisonType The type of comparison to be applied to the value.
     * @param string $eventCreateRuleEventConditionsValue          The value being compared against for this condition.  The runtime
     *                                                             implementation may perform type coercion of this value to evaluate this
     *                                                             condition based on the type of the parameter value.
     */
    function update_event_create_rule_sample(
        string $eventCreateRuleDestinationEvent,
        string $eventCreateRuleEventConditionsField,
        int $eventCreateRuleEventConditionsComparisonType,
        string $eventCreateRuleEventConditionsValue
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $matchingCondition = (new MatchingCondition())
            ->setField($eventCreateRuleEventConditionsField)
            ->setComparisonType($eventCreateRuleEventConditionsComparisonType)
            ->setValue($eventCreateRuleEventConditionsValue);
        $eventCreateRuleEventConditions = [$matchingCondition,];
        $eventCreateRule = (new EventCreateRule())
            ->setDestinationEvent($eventCreateRuleDestinationEvent)
            ->setEventConditions($eventCreateRuleEventConditions);
        $updateMask = new FieldMask();
        $request = (new UpdateEventCreateRuleRequest())
            ->setEventCreateRule($eventCreateRule)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var EventCreateRule $response */
            $response = $analyticsAdminServiceClient->updateEventCreateRule($request);
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
        $eventCreateRuleDestinationEvent = '[DESTINATION_EVENT]';
        $eventCreateRuleEventConditionsField = '[FIELD]';
        $eventCreateRuleEventConditionsComparisonType = ComparisonType::COMPARISON_TYPE_UNSPECIFIED;
        $eventCreateRuleEventConditionsValue = '[VALUE]';
    
        update_event_create_rule_sample(
            $eventCreateRuleDestinationEvent,
            $eventCreateRuleEventConditionsField,
            $eventCreateRuleEventConditionsComparisonType,
            $eventCreateRuleEventConditionsValue
        );
    }
    

### updateEventEditRule

Updates an EventEditRule.

The async variant is [AnalyticsAdminServiceClient::updateEventEditRuleAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateEventEditRuleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateEventEditRuleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\EventEditRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\EventEditRule;
    use Google\Analytics\Admin\V1alpha\MatchingCondition;
    use Google\Analytics\Admin\V1alpha\MatchingCondition\ComparisonType;
    use Google\Analytics\Admin\V1alpha\ParameterMutation;
    use Google\Analytics\Admin\V1alpha\UpdateEventEditRuleRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $eventEditRuleDisplayName                      The display name of this event edit rule. Maximum of 255
     *                                                              characters.
     * @param string $eventEditRuleEventConditionsField             The name of the field that is compared against for the condition.
     *                                                              If 'event_name' is specified this condition will apply to the name of the
     *                                                              event.  Otherwise the condition will apply to a parameter with the
     *                                                              specified name.
     *
     *                                                              This value cannot contain spaces.
     * @param int    $eventEditRuleEventConditionsComparisonType    The type of comparison to be applied to the value.
     * @param string $eventEditRuleEventConditionsValue             The value being compared against for this condition.  The runtime
     *                                                              implementation may perform type coercion of this value to evaluate this
     *                                                              condition based on the type of the parameter value.
     * @param string $eventEditRuleParameterMutationsParameter      The name of the parameter to mutate.
     *                                                              This value must:
     *                                                              * be less than 40 characters.
     *                                                              * be unique across across all mutations within the rule
     *                                                              * consist only of letters, digits or _ (underscores)
     *                                                              For event edit rules, the name may also be set to 'event_name' to modify
     *                                                              the event_name in place.
     * @param string $eventEditRuleParameterMutationsParameterValue The value mutation to perform.
     *                                                              * Must be less than 100 characters.
     *                                                              * To specify a constant value for the param, use the value's string.
     *                                                              * To copy value from another parameter, use syntax like
     *                                                              "[[other_parameter]]" For more details, see this [help center
     *                                                              article](https://support.google.com/analytics/answer/10085872#modify-an-event&zippy=%2Cin-this-article%2Cmodify-parameters).
     */
    function update_event_edit_rule_sample(
        string $eventEditRuleDisplayName,
        string $eventEditRuleEventConditionsField,
        int $eventEditRuleEventConditionsComparisonType,
        string $eventEditRuleEventConditionsValue,
        string $eventEditRuleParameterMutationsParameter,
        string $eventEditRuleParameterMutationsParameterValue
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $matchingCondition = (new MatchingCondition())
            ->setField($eventEditRuleEventConditionsField)
            ->setComparisonType($eventEditRuleEventConditionsComparisonType)
            ->setValue($eventEditRuleEventConditionsValue);
        $eventEditRuleEventConditions = [$matchingCondition,];
        $parameterMutation = (new ParameterMutation())
            ->setParameter($eventEditRuleParameterMutationsParameter)
            ->setParameterValue($eventEditRuleParameterMutationsParameterValue);
        $eventEditRuleParameterMutations = [$parameterMutation,];
        $eventEditRule = (new EventEditRule())
            ->setDisplayName($eventEditRuleDisplayName)
            ->setEventConditions($eventEditRuleEventConditions)
            ->setParameterMutations($eventEditRuleParameterMutations);
        $updateMask = new FieldMask();
        $request = (new UpdateEventEditRuleRequest())
            ->setEventEditRule($eventEditRule)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var EventEditRule $response */
            $response = $analyticsAdminServiceClient->updateEventEditRule($request);
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
        $eventEditRuleDisplayName = '[DISPLAY_NAME]';
        $eventEditRuleEventConditionsField = '[FIELD]';
        $eventEditRuleEventConditionsComparisonType = ComparisonType::COMPARISON_TYPE_UNSPECIFIED;
        $eventEditRuleEventConditionsValue = '[VALUE]';
        $eventEditRuleParameterMutationsParameter = '[PARAMETER]';
        $eventEditRuleParameterMutationsParameterValue = '[PARAMETER_VALUE]';
    
        update_event_edit_rule_sample(
            $eventEditRuleDisplayName,
            $eventEditRuleEventConditionsField,
            $eventEditRuleEventConditionsComparisonType,
            $eventEditRuleEventConditionsValue,
            $eventEditRuleParameterMutationsParameter,
            $eventEditRuleParameterMutationsParameterValue
        );
    }
    

### updateExpandedDataSet

Updates a ExpandedDataSet on a property.

The async variant is [AnalyticsAdminServiceClient::updateExpandedDataSetAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateExpandedDataSetAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateExpandedDataSetRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ExpandedDataSet;
    use Google\Analytics\Admin\V1alpha\UpdateExpandedDataSetRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $expandedDataSetDisplayName The display name of the ExpandedDataSet.
     *                                           Max 200 chars.
     */
    function update_expanded_data_set_sample(string $expandedDataSetDisplayName): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $expandedDataSet = (new ExpandedDataSet())
            ->setDisplayName($expandedDataSetDisplayName);
        $updateMask = new FieldMask();
        $request = (new UpdateExpandedDataSetRequest())
            ->setExpandedDataSet($expandedDataSet)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var ExpandedDataSet $response */
            $response = $analyticsAdminServiceClient->updateExpandedDataSet($request);
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
        $expandedDataSetDisplayName = '[DISPLAY_NAME]';
    
        update_expanded_data_set_sample($expandedDataSetDisplayName);
    }
    

### updateGoogleAdsLink

Updates a GoogleAdsLink on a property

The async variant is [AnalyticsAdminServiceClient::updateGoogleAdsLinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateGoogleAdsLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateGoogleAdsLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GoogleAdsLink;
    use Google\Analytics\Admin\V1alpha\UpdateGoogleAdsLinkRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_google_ads_link_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $request = (new UpdateGoogleAdsLinkRequest())
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var GoogleAdsLink $response */
            $response = $analyticsAdminServiceClient->updateGoogleAdsLink($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateGoogleSignalsSettings

Updates Google Signals settings for a property.

The async variant is [AnalyticsAdminServiceClient::updateGoogleSignalsSettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateGoogleSignalsSettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateGoogleSignalsSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateGoogleSignalsSettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\GoogleSignalsSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleSignalsSettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\GoogleSignalsSettings;
    use Google\Analytics\Admin\V1alpha\UpdateGoogleSignalsSettingsRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_google_signals_settings_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $googleSignalsSettings = new GoogleSignalsSettings();
        $updateMask = new FieldMask();
        $request = (new UpdateGoogleSignalsSettingsRequest())
            ->setGoogleSignalsSettings($googleSignalsSettings)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var GoogleSignalsSettings $response */
            $response = $analyticsAdminServiceClient->updateGoogleSignalsSettings($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateKeyEvent

Updates a Key Event.

The async variant is [AnalyticsAdminServiceClient::updateKeyEventAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateKeyEventAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateKeyEventRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\KeyEvent;
    use Google\Analytics\Admin\V1alpha\KeyEvent\CountingMethod;
    use Google\Analytics\Admin\V1alpha\UpdateKeyEventRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param int $keyEventCountingMethod The method by which Key Events will be counted across multiple
     *                                    events within a session.
     */
    function update_key_event_sample(int $keyEventCountingMethod): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $keyEvent = (new KeyEvent())
            ->setCountingMethod($keyEventCountingMethod);
        $updateMask = new FieldMask();
        $request = (new UpdateKeyEventRequest())
            ->setKeyEvent($keyEvent)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var KeyEvent $response */
            $response = $analyticsAdminServiceClient->updateKeyEvent($request);
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
        $keyEventCountingMethod = CountingMethod::COUNTING_METHOD_UNSPECIFIED;
    
        update_key_event_sample($keyEventCountingMethod);
    }
    

### updateMeasurementProtocolSecret

Updates a measurement protocol secret.

The async variant is [AnalyticsAdminServiceClient::updateMeasurementProtocolSecretAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateMeasurementProtocolSecretAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateMeasurementProtocolSecretRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret;
    use Google\Analytics\Admin\V1alpha\UpdateMeasurementProtocolSecretRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $measurementProtocolSecretDisplayName Human-readable display name for this secret.
     */
    function update_measurement_protocol_secret_sample(
        string $measurementProtocolSecretDisplayName
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $measurementProtocolSecret = (new MeasurementProtocolSecret())
            ->setDisplayName($measurementProtocolSecretDisplayName);
        $updateMask = new FieldMask();
        $request = (new UpdateMeasurementProtocolSecretRequest())
            ->setMeasurementProtocolSecret($measurementProtocolSecret)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var MeasurementProtocolSecret $response */
            $response = $analyticsAdminServiceClient->updateMeasurementProtocolSecret($request);
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
        $measurementProtocolSecretDisplayName = '[DISPLAY_NAME]';
    
        update_measurement_protocol_secret_sample($measurementProtocolSecretDisplayName);
    }
    

### updateProperty

Updates a property.

The async variant is [AnalyticsAdminServiceClient::updatePropertyAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updatePropertyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdatePropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdatePropertyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\Property;
    use Google\Analytics\Admin\V1alpha\UpdatePropertyRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $propertyDisplayName Human-readable display name for this property.
     *
     *                                    The max allowed display name length is 100 UTF-16 code units.
     * @param string $propertyTimeZone    Reporting Time Zone, used as the day boundary for reports,
     *                                    regardless of where the data originates. If the time zone honors DST,
     *                                    Analytics will automatically adjust for the changes.
     *
     *                                    NOTE: Changing the time zone only affects data going forward, and is not
     *                                    applied retroactively.
     *
     *                                    Format: https://www.iana.org/time-zones
     *                                    Example: "America/Los_Angeles"
     */
    function update_property_sample(string $propertyDisplayName, string $propertyTimeZone): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $property = (new Property())
            ->setDisplayName($propertyDisplayName)
            ->setTimeZone($propertyTimeZone);
        $updateMask = new FieldMask();
        $request = (new UpdatePropertyRequest())
            ->setProperty($property)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var Property $response */
            $response = $analyticsAdminServiceClient->updateProperty($request);
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
        $propertyDisplayName = '[DISPLAY_NAME]';
        $propertyTimeZone = '[TIME_ZONE]';
    
        update_property_sample($propertyDisplayName, $propertyTimeZone);
    }
    

### updateReportingDataAnnotation

Updates a Reporting Data Annotation.

The async variant is [AnalyticsAdminServiceClient::updateReportingDataAnnotationAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateReportingDataAnnotationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateReportingDataAnnotationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ReportingDataAnnotation;
    use Google\Analytics\Admin\V1alpha\ReportingDataAnnotation\Color;
    use Google\Analytics\Admin\V1alpha\UpdateReportingDataAnnotationRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $reportingDataAnnotationName  Identifier. Resource name of this Reporting Data Annotation.
     *                                             Format:
     *                                             'properties/{property_id}/reportingDataAnnotations/{reporting_data_annotation}'
     *                                             Format: 'properties/123/reportingDataAnnotations/456'
     * @param string $reportingDataAnnotationTitle Human-readable title for this Reporting Data Annotation.
     * @param int    $reportingDataAnnotationColor The color used for display of this Reporting Data Annotation.
     */
    function update_reporting_data_annotation_sample(
        string $reportingDataAnnotationName,
        string $reportingDataAnnotationTitle,
        int $reportingDataAnnotationColor
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $reportingDataAnnotation = (new ReportingDataAnnotation())
            ->setName($reportingDataAnnotationName)
            ->setTitle($reportingDataAnnotationTitle)
            ->setColor($reportingDataAnnotationColor);
        $request = (new UpdateReportingDataAnnotationRequest())
            ->setReportingDataAnnotation($reportingDataAnnotation);
    
        // Call the API and handle any network failures.
        try {
            /** @var ReportingDataAnnotation $response */
            $response = $analyticsAdminServiceClient->updateReportingDataAnnotation($request);
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
        $reportingDataAnnotationName = '[NAME]';
        $reportingDataAnnotationTitle = '[TITLE]';
        $reportingDataAnnotationColor = Color::COLOR_UNSPECIFIED;
    
        update_reporting_data_annotation_sample(
            $reportingDataAnnotationName,
            $reportingDataAnnotationTitle,
            $reportingDataAnnotationColor
        );
    }
    

### updateReportingIdentitySettings

Updates the reporting identity settings for this property.

The async variant is [AnalyticsAdminServiceClient::updateReportingIdentitySettingsAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateReportingIdentitySettingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateReportingIdentitySettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateReportingIdentitySettingsRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\ReportingIdentitySettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingIdentitySettings)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\ReportingIdentitySettings;
    use Google\Analytics\Admin\V1alpha\UpdateReportingIdentitySettingsRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_reporting_identity_settings_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $reportingIdentitySettings = new ReportingIdentitySettings();
        $request = (new UpdateReportingIdentitySettingsRequest())
            ->setReportingIdentitySettings($reportingIdentitySettings);
    
        // Call the API and handle any network failures.
        try {
            /** @var ReportingIdentitySettings $response */
            $response = $analyticsAdminServiceClient->updateReportingIdentitySettings($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateSKAdNetworkConversionValueSchema

Updates a SKAdNetworkConversionValueSchema.

The async variant is [AnalyticsAdminServiceClient::updateSKAdNetworkConversionValueSchemaAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateSKAdNetworkConversionValueSchemaAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSKAdNetworkConversionValueSchemaRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\PostbackWindow;
    use Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema;
    use Google\Analytics\Admin\V1alpha\UpdateSKAdNetworkConversionValueSchemaRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_sk_ad_network_conversion_value_schema_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $skadnetworkConversionValueSchemaPostbackWindowOne = new PostbackWindow();
        $skadnetworkConversionValueSchema = (new SKAdNetworkConversionValueSchema())
            ->setPostbackWindowOne($skadnetworkConversionValueSchemaPostbackWindowOne);
        $updateMask = new FieldMask();
        $request = (new UpdateSKAdNetworkConversionValueSchemaRequest())
            ->setSkadnetworkConversionValueSchema($skadnetworkConversionValueSchema)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var SKAdNetworkConversionValueSchema $response */
            $response = $analyticsAdminServiceClient->updateSKAdNetworkConversionValueSchema($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateSearchAds360Link

Updates a SearchAds360Link on a property.

The async variant is [AnalyticsAdminServiceClient::updateSearchAds360LinkAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateSearchAds360LinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSearchAds360LinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\SearchAds360Link;
    use Google\Analytics\Admin\V1alpha\UpdateSearchAds360LinkRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_search_ads360_link_sample(): void
    {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $request = (new UpdateSearchAds360LinkRequest())
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var SearchAds360Link $response */
            $response = $analyticsAdminServiceClient->updateSearchAds360Link($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateSubpropertyEventFilter

Updates a subproperty Event Filter.

The async variant is [AnalyticsAdminServiceClient::updateSubpropertyEventFilterAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateSubpropertyEventFilterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSubpropertyEventFilterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SubpropertyEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertyEventFilter)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilter;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilterClause;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilterClause\FilterClauseType;
    use Google\Analytics\Admin\V1alpha\SubpropertyEventFilterExpression;
    use Google\Analytics\Admin\V1alpha\UpdateSubpropertyEventFilterRequest;
    use Google\ApiCore\ApiException;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param int $subpropertyEventFilterFilterClausesFilterClauseType The type for the filter clause.
     */
    function update_subproperty_event_filter_sample(
        int $subpropertyEventFilterFilterClausesFilterClauseType
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $subpropertyEventFilterFilterClausesFilterExpression = new SubpropertyEventFilterExpression();
        $subpropertyEventFilterClause = (new SubpropertyEventFilterClause())
            ->setFilterClauseType($subpropertyEventFilterFilterClausesFilterClauseType)
            ->setFilterExpression($subpropertyEventFilterFilterClausesFilterExpression);
        $subpropertyEventFilterFilterClauses = [$subpropertyEventFilterClause,];
        $subpropertyEventFilter = (new SubpropertyEventFilter())
            ->setFilterClauses($subpropertyEventFilterFilterClauses);
        $updateMask = new FieldMask();
        $request = (new UpdateSubpropertyEventFilterRequest())
            ->setSubpropertyEventFilter($subpropertyEventFilter)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var SubpropertyEventFilter $response */
            $response = $analyticsAdminServiceClient->updateSubpropertyEventFilter($request);
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
        $subpropertyEventFilterFilterClausesFilterClauseType = FilterClauseType::FILTER_CLAUSE_TYPE_UNSPECIFIED;
    
        update_subproperty_event_filter_sample($subpropertyEventFilterFilterClausesFilterClauseType);
    }
    

### updateSubpropertySyncConfig

Updates a `SubpropertySyncConfig`.

The async variant is [AnalyticsAdminServiceClient::updateSubpropertySyncConfigAsync()](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Client.AnalyticsAdminServiceClient#_Google_Analytics_Admin_V1alpha_Client_AnalyticsAdminServiceClient__updateSubpropertySyncConfigAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSubpropertySyncConfigRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSubpropertySyncConfigRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\SubpropertySyncConfig](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertySyncConfig)` |   
**Example**
    
    
    use Google\Analytics\Admin\V1alpha\Client\AnalyticsAdminServiceClient;
    use Google\Analytics\Admin\V1alpha\SubpropertySyncConfig;
    use Google\Analytics\Admin\V1alpha\SubpropertySyncConfig\SynchronizationMode;
    use Google\Analytics\Admin\V1alpha\UpdateSubpropertySyncConfigRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param int $subpropertySyncConfigCustomDimensionAndMetricSyncMode Specifies the Custom Dimension / Metric synchronization mode for
     *                                                                   the subproperty.
     *
     *                                                                   If set to ALL, Custom Dimension / Metric synchronization will be
     *                                                                   immediately enabled.  Local configuration of Custom Dimensions / Metrics
     *                                                                   will not be allowed on the subproperty so long as the synchronization mode
     *                                                                   is set to ALL.
     *
     *                                                                   If set to NONE, Custom Dimensions / Metric synchronization is disabled.
     *                                                                   Custom Dimensions / Metrics must be configured explicitly on the
     *                                                                   Subproperty.
     */
    function update_subproperty_sync_config_sample(
        int $subpropertySyncConfigCustomDimensionAndMetricSyncMode
    ): void {
        // Create a client.
        $analyticsAdminServiceClient = new AnalyticsAdminServiceClient();
    
        // Prepare the request message.
        $subpropertySyncConfig = (new SubpropertySyncConfig())
            ->setCustomDimensionAndMetricSyncMode($subpropertySyncConfigCustomDimensionAndMetricSyncMode);
        $request = (new UpdateSubpropertySyncConfigRequest())
            ->setSubpropertySyncConfig($subpropertySyncConfig);
    
        // Call the API and handle any network failures.
        try {
            /** @var SubpropertySyncConfig $response */
            $response = $analyticsAdminServiceClient->updateSubpropertySyncConfig($request);
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
        $subpropertySyncConfigCustomDimensionAndMetricSyncMode = SynchronizationMode::SYNCHRONIZATION_MODE_UNSPECIFIED;
    
        update_subproperty_sync_config_sample($subpropertySyncConfigCustomDimensionAndMetricSyncMode);
    }
    

### acknowledgeUserDataCollectionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\AcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AcknowledgeUserDataCollectionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AcknowledgeUserDataCollectionResponse)>` |   
  
### approveDisplayVideo360AdvertiserLinkProposalAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ApproveDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ApproveDisplayVideo360AdvertiserLinkProposalRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ApproveDisplayVideo360AdvertiserLinkProposalResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ApproveDisplayVideo360AdvertiserLinkProposalResponse)>` |   
  
### archiveAudienceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ArchiveAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ArchiveAudienceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### archiveCustomDimensionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ArchiveCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ArchiveCustomDimensionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### archiveCustomMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ArchiveCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ArchiveCustomMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### batchCreateAccessBindingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchCreateAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchCreateAccessBindingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\BatchCreateAccessBindingsResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchCreateAccessBindingsResponse)>` |   
  
### batchDeleteAccessBindingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchDeleteAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchDeleteAccessBindingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### batchGetAccessBindingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchGetAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchGetAccessBindingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\BatchGetAccessBindingsResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchGetAccessBindingsResponse)>` |   
  
### batchUpdateAccessBindingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\BatchUpdateAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchUpdateAccessBindingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\BatchUpdateAccessBindingsResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BatchUpdateAccessBindingsResponse)>` |   
  
### cancelDisplayVideo360AdvertiserLinkProposalAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CancelDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CancelDisplayVideo360AdvertiserLinkProposalRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)>` |   
  
### createAccessBindingAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateAccessBindingRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AccessBinding](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessBinding)>` |   
  
### createAdSenseLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateAdSenseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateAdSenseLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AdSenseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AdSenseLink)>` |   
  
### createAudienceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateAudienceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)>` |   
  
### createBigQueryLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateBigQueryLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)>` |   
  
### createCalculatedMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateCalculatedMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)>` |   
  
### createChannelGroupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateChannelGroupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)>` |   
  
### createConversionEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateConversionEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)>` |   
  
### createCustomDimensionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateCustomDimensionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)>` |   
  
### createCustomMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateCustomMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)>` |   
  
### createDataStreamAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateDataStreamRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)>` |   
  
### createDisplayVideo360AdvertiserLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateDisplayVideo360AdvertiserLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)>` |   
  
### createDisplayVideo360AdvertiserLinkProposalAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)>` |   
  
### createEventCreateRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateEventCreateRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)>` |   
  
### createEventEditRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateEventEditRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EventEditRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule)>` |   
  
### createExpandedDataSetAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateExpandedDataSetRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)>` |   
  
### createFirebaseLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateFirebaseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateFirebaseLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\FirebaseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.FirebaseLink)>` |   
  
### createGoogleAdsLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateGoogleAdsLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateGoogleAdsLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink)>` |   
  
### createKeyEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateKeyEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)>` |   
  
### createMeasurementProtocolSecretAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateMeasurementProtocolSecretRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)>` |   
  
### createPropertyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreatePropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreatePropertyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)>` |   
  
### createReportingDataAnnotationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateReportingDataAnnotationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)>` |   
  
### createRollupPropertyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateRollupPropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateRollupPropertyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CreateRollupPropertyResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateRollupPropertyResponse)>` |   
  
### createRollupPropertySourceLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateRollupPropertySourceLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateRollupPropertySourceLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\RollupPropertySourceLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RollupPropertySourceLink)>` |   
  
### createSKAdNetworkConversionValueSchemaAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSKAdNetworkConversionValueSchemaRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)>` |   
  
### createSearchAds360LinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSearchAds360LinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)>` |   
  
### createSubpropertyEventFilterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\CreateSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSubpropertyEventFilterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SubpropertyEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertyEventFilter)>` |   
  
### deleteAccessBindingAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteAccessBindingRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteAccountAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteAccountRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteAccountRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteAdSenseLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteAdSenseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteAdSenseLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteBigQueryLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteBigQueryLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteCalculatedMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteCalculatedMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteChannelGroupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteChannelGroupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteConversionEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteConversionEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteDataStreamAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteDataStreamRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteDisplayVideo360AdvertiserLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteDisplayVideo360AdvertiserLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteDisplayVideo360AdvertiserLinkProposalAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteDisplayVideo360AdvertiserLinkProposalRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteEventCreateRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteEventCreateRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteEventEditRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteEventEditRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteExpandedDataSetAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteExpandedDataSetRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteFirebaseLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteFirebaseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteFirebaseLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteGoogleAdsLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteGoogleAdsLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteKeyEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteKeyEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteMeasurementProtocolSecretAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteMeasurementProtocolSecretRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deletePropertyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeletePropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeletePropertyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)>` |   
  
### deleteReportingDataAnnotationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteReportingDataAnnotationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteRollupPropertySourceLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteRollupPropertySourceLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteRollupPropertySourceLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteSKAdNetworkConversionValueSchemaAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteSKAdNetworkConversionValueSchemaRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteSearchAds360LinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteSearchAds360LinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteSubpropertyEventFilterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\DeleteSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DeleteSubpropertyEventFilterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### getAccessBindingAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAccessBindingRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AccessBinding](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessBinding)>` |   
  
### getAccountAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAccountRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAccountRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Account](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Account)>` |   
  
### getAdSenseLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAdSenseLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAdSenseLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AdSenseLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AdSenseLink)>` |   
  
### getAttributionSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAttributionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAttributionSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AttributionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings)>` |   
  
### getAudienceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetAudienceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)>` |   
  
### getBigQueryLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetBigQueryLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)>` |   
  
### getCalculatedMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetCalculatedMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)>` |   
  
### getChannelGroupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetChannelGroupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)>` |   
  
### getConversionEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetConversionEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)>` |   
  
### getCustomDimensionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetCustomDimensionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)>` |   
  
### getCustomMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetCustomMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)>` |   
  
### getDataRedactionSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataRedactionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataRedactionSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataRedactionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRedactionSettings)>` |   
  
### getDataRetentionSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataRetentionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataRetentionSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataRetentionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings)>` |   
  
### getDataSharingSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataSharingSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataSharingSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataSharingSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataSharingSettings)>` |   
  
### getDataStreamAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDataStreamRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)>` |   
  
### getDisplayVideo360AdvertiserLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDisplayVideo360AdvertiserLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)>` |   
  
### getDisplayVideo360AdvertiserLinkProposalAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetDisplayVideo360AdvertiserLinkProposalRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal)>` |   
  
### getEnhancedMeasurementSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetEnhancedMeasurementSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings)>` |   
  
### getEventCreateRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetEventCreateRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)>` |   
  
### getEventEditRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetEventEditRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EventEditRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule)>` |   
  
### getExpandedDataSetAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetExpandedDataSetRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)>` |   
  
### getGlobalSiteTagAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetGlobalSiteTagRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetGlobalSiteTagRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\GlobalSiteTag](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GlobalSiteTag)>` |   
  
### getGoogleSignalsSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetGoogleSignalsSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetGoogleSignalsSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\GoogleSignalsSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleSignalsSettings)>` |   
  
### getKeyEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetKeyEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)>` |   
  
### getMeasurementProtocolSecretAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetMeasurementProtocolSecretRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)>` |   
  
### getPropertyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetPropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetPropertyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)>` |   
  
### getReportingDataAnnotationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetReportingDataAnnotationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)>` |   
  
### getReportingIdentitySettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetReportingIdentitySettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetReportingIdentitySettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ReportingIdentitySettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingIdentitySettings)>` |   
  
### getRollupPropertySourceLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetRollupPropertySourceLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetRollupPropertySourceLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\RollupPropertySourceLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RollupPropertySourceLink)>` |   
  
### getSKAdNetworkConversionValueSchemaAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSKAdNetworkConversionValueSchemaRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)>` |   
  
### getSearchAds360LinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSearchAds360LinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)>` |   
  
### getSubpropertyEventFilterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSubpropertyEventFilterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SubpropertyEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertyEventFilter)>` |   
  
### getSubpropertySyncConfigAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetSubpropertySyncConfigRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetSubpropertySyncConfigRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SubpropertySyncConfig](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertySyncConfig)>` |   
  
### getUserProvidedDataSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\GetUserProvidedDataSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GetUserProvidedDataSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\UserProvidedDataSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UserProvidedDataSettings)>` |   
  
### listAccessBindingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAccessBindingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAccessBindingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listAccountSummariesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAccountSummariesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAccountSummariesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listAccountsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAccountsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAccountsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listAdSenseLinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAdSenseLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAdSenseLinksRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listAudiencesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListAudiencesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListAudiencesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBigQueryLinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListBigQueryLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListBigQueryLinksRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listCalculatedMetricsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListCalculatedMetricsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListCalculatedMetricsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listChannelGroupsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListChannelGroupsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListChannelGroupsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listConversionEventsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListConversionEventsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListConversionEventsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listCustomDimensionsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListCustomDimensionsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListCustomDimensionsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listCustomMetricsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListCustomMetricsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListCustomMetricsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listDataStreamsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListDataStreamsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListDataStreamsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listDisplayVideo360AdvertiserLinkProposalsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListDisplayVideo360AdvertiserLinkProposalsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListDisplayVideo360AdvertiserLinkProposalsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listDisplayVideo360AdvertiserLinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListDisplayVideo360AdvertiserLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListDisplayVideo360AdvertiserLinksRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listEventCreateRulesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListEventCreateRulesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListEventCreateRulesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listEventEditRulesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListEventEditRulesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListEventEditRulesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listExpandedDataSetsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListExpandedDataSetsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListExpandedDataSetsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listFirebaseLinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListFirebaseLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListFirebaseLinksRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listGoogleAdsLinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListGoogleAdsLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListGoogleAdsLinksRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listKeyEventsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListKeyEventsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListKeyEventsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listMeasurementProtocolSecretsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListMeasurementProtocolSecretsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listPropertiesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListPropertiesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListPropertiesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listReportingDataAnnotationsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListReportingDataAnnotationsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListReportingDataAnnotationsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listRollupPropertySourceLinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListRollupPropertySourceLinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListRollupPropertySourceLinksRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listSKAdNetworkConversionValueSchemasAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSKAdNetworkConversionValueSchemasRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSKAdNetworkConversionValueSchemasRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listSearchAds360LinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSearchAds360LinksRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSearchAds360LinksRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listSubpropertyEventFiltersAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSubpropertyEventFiltersRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSubpropertyEventFiltersRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listSubpropertySyncConfigsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ListSubpropertySyncConfigsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListSubpropertySyncConfigsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### provisionAccountTicketAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ProvisionAccountTicketRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionAccountTicketRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ProvisionAccountTicketResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionAccountTicketResponse)>` |   
  
### provisionSubpropertyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ProvisionSubpropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionSubpropertyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ProvisionSubpropertyResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ProvisionSubpropertyResponse)>` |   
  
### reorderEventEditRulesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\ReorderEventEditRulesRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReorderEventEditRulesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### runAccessReportAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\RunAccessReportRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RunAccessReportRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\RunAccessReportResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.RunAccessReportResponse)>` |   
  
### searchChangeHistoryEventsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\SearchChangeHistoryEventsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchChangeHistoryEventsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### submitUserDeletionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\SubmitUserDeletionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubmitUserDeletionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SubmitUserDeletionResponse](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubmitUserDeletionResponse)>` |   
  
### updateAccessBindingAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAccessBindingRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAccessBindingRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AccessBinding](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessBinding)>` |   
  
### updateAccountAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAccountRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAccountRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Account](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Account)>` |   
  
### updateAttributionSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAttributionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAttributionSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\AttributionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AttributionSettings)>` |   
  
### updateAudienceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateAudienceRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateAudienceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Audience](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience)>` |   
  
### updateBigQueryLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateBigQueryLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateBigQueryLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\BigQueryLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink)>` |   
  
### updateCalculatedMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateCalculatedMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateCalculatedMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CalculatedMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric)>` |   
  
### updateChannelGroupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateChannelGroupRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateChannelGroupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ChannelGroup](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroup)>` |   
  
### updateConversionEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateConversionEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateConversionEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ConversionEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionEvent)>` |   
  
### updateCustomDimensionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateCustomDimensionRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateCustomDimensionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CustomDimension](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomDimension)>` |   
  
### updateCustomMetricAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateCustomMetricRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateCustomMetricRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\CustomMetric](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CustomMetric)>` |   
  
### updateDataRedactionSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDataRedactionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDataRedactionSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataRedactionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRedactionSettings)>` |   
  
### updateDataRetentionSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDataRetentionSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataRetentionSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings)>` |   
  
### updateDataStreamAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDataStreamRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDataStreamRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DataStream](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream)>` |   
  
### updateDisplayVideo360AdvertiserLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateDisplayVideo360AdvertiserLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLink)>` |   
  
### updateEnhancedMeasurementSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateEnhancedMeasurementSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EnhancedMeasurementSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings)>` |   
  
### updateEventCreateRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateEventCreateRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateEventCreateRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EventCreateRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventCreateRule)>` |   
  
### updateEventEditRuleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateEventEditRuleRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateEventEditRuleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\EventEditRule](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule)>` |   
  
### updateExpandedDataSetAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateExpandedDataSetRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateExpandedDataSetRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ExpandedDataSet](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet)>` |   
  
### updateGoogleAdsLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateGoogleAdsLinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\GoogleAdsLink](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleAdsLink)>` |   
  
### updateGoogleSignalsSettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateGoogleSignalsSettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateGoogleSignalsSettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\GoogleSignalsSettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.GoogleSignalsSettings)>` |   
  
### updateKeyEventAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateKeyEventRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateKeyEventRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\KeyEvent](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent)>` |   
  
### updateMeasurementProtocolSecretAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateMeasurementProtocolSecretRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\MeasurementProtocolSecret](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MeasurementProtocolSecret)>` |   
  
### updatePropertyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdatePropertyRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdatePropertyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\Property](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Property)>` |   
  
### updateReportingDataAnnotationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateReportingDataAnnotationRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateReportingDataAnnotationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ReportingDataAnnotation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingDataAnnotation)>` |   
  
### updateReportingIdentitySettingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateReportingIdentitySettingsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateReportingIdentitySettingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\ReportingIdentitySettings](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ReportingIdentitySettings)>` |   
  
### updateSKAdNetworkConversionValueSchemaAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSKAdNetworkConversionValueSchemaRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SKAdNetworkConversionValueSchema)>` |   
  
### updateSearchAds360LinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSearchAds360LinkRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)>` |   
  
### updateSubpropertyEventFilterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSubpropertyEventFilterRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSubpropertyEventFilterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SubpropertyEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertyEventFilter)>` |   
  
### updateSubpropertySyncConfigAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Analytics\Admin\V1alpha\UpdateSubpropertySyncConfigRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.UpdateSubpropertySyncConfigRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Analytics\Admin\V1alpha\SubpropertySyncConfig](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SubpropertySyncConfig)>` |   
  
### static::accessBindingName

Formats a string containing the fully-qualified path to represent a access_binding resource.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`accessBinding` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted access_binding resource.  
  
### static::accountName

Formats a string containing the fully-qualified path to represent a account resource.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted account resource.  
  
### static::accountAccessBindingName

Formats a string containing the fully-qualified path to represent a account_access_binding resource.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`accessBinding` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted account_access_binding resource.  
  
### static::adSenseLinkName

Formats a string containing the fully-qualified path to represent a ad_sense_link resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`adsenseLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted ad_sense_link resource.  
  
### static::attributionSettingsName

Formats a string containing the fully-qualified path to represent a attribution_settings resource.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted attribution_settings resource.  
  
### static::audienceName

Formats a string containing the fully-qualified path to represent a audience resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`audience` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted audience resource.  
  
### static::bigQueryLinkName

Formats a string containing the fully-qualified path to represent a big_query_link resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`bigqueryLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted big_query_link resource.  
  
### static::calculatedMetricName

Formats a string containing the fully-qualified path to represent a calculated_metric resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`calculatedMetric` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted calculated_metric resource.  
  
### static::channelGroupName

Formats a string containing the fully-qualified path to represent a channel_group resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`channelGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted channel_group resource.  
  
### static::conversionEventName

Formats a string containing the fully-qualified path to represent a conversion_event resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`conversionEvent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted conversion_event resource.  
  
### static::customDimensionName

Formats a string containing the fully-qualified path to represent a custom_dimension resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`customDimension` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted custom_dimension resource.  
  
### static::customMetricName

Formats a string containing the fully-qualified path to represent a custom_metric resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`customMetric` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted custom_metric resource.  
  
### static::dataRedactionSettingsName

Formats a string containing the fully-qualified path to represent a data_redaction_settings resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted data_redaction_settings resource.  
  
### static::dataRetentionSettingsName

Formats a string containing the fully-qualified path to represent a data_retention_settings resource.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted data_retention_settings resource.  
  
### static::dataSharingSettingsName

Formats a string containing the fully-qualified path to represent a data_sharing_settings resource.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted data_sharing_settings resource.  
  
### static::dataStreamName

Formats a string containing the fully-qualified path to represent a data_stream resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted data_stream resource.  
  
### static::displayVideo360AdvertiserLinkName

Formats a string containing the fully-qualified path to represent a display_video360_advertiser_link resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`displayVideo360AdvertiserLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted display_video360_advertiser_link resource.  
  
### static::displayVideo360AdvertiserLinkProposalName

Formats a string containing the fully-qualified path to represent a display_video360_advertiser_link_proposal resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`displayVideo360AdvertiserLinkProposal` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted display_video360_advertiser_link_proposal resource.  
  
### static::enhancedMeasurementSettingsName

Formats a string containing the fully-qualified path to represent a enhanced_measurement_settings resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted enhanced_measurement_settings resource.  
  
### static::eventCreateRuleName

Formats a string containing the fully-qualified path to represent a event_create_rule resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
`eventCreateRule` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted event_create_rule resource.  
  
### static::eventEditRuleName

Formats a string containing the fully-qualified path to represent a event_edit_rule resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
`eventEditRule` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted event_edit_rule resource.  
  
### static::expandedDataSetName

Formats a string containing the fully-qualified path to represent a expanded_data_set resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`expandedDataSet` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted expanded_data_set resource.  
  
### static::firebaseLinkName

Formats a string containing the fully-qualified path to represent a firebase_link resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`firebaseLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted firebase_link resource.  
  
### static::globalSiteTagName

Formats a string containing the fully-qualified path to represent a global_site_tag resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted global_site_tag resource.  
  
### static::googleAdsLinkName

Formats a string containing the fully-qualified path to represent a google_ads_link resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`googleAdsLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted google_ads_link resource.  
  
### static::googleSignalsSettingsName

Formats a string containing the fully-qualified path to represent a google_signals_settings resource.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted google_signals_settings resource.  
  
### static::keyEventName

Formats a string containing the fully-qualified path to represent a key_event resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`keyEvent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted key_event resource.  
  
### static::measurementProtocolSecretName

Formats a string containing the fully-qualified path to represent a measurement_protocol_secret resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
`measurementProtocolSecret` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted measurement_protocol_secret resource.  
  
### static::organizationName

Formats a string containing the fully-qualified path to represent a organization resource.

**Parameter**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted organization resource.  
  
### static::propertyName

Formats a string containing the fully-qualified path to represent a property resource.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted property resource.  
  
### static::propertyAccessBindingName

Formats a string containing the fully-qualified path to represent a property_access_binding resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`accessBinding` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted property_access_binding resource.  
  
### static::reportingDataAnnotationName

Formats a string containing the fully-qualified path to represent a reporting_data_annotation resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`reportingDataAnnotation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted reporting_data_annotation resource.  
  
### static::reportingIdentitySettingsName

Formats a string containing the fully-qualified path to represent a reporting_identity_settings resource.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted reporting_identity_settings resource.  
  
### static::rollupPropertySourceLinkName

Formats a string containing the fully-qualified path to represent a rollup_property_source_link resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`rollupPropertySourceLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted rollup_property_source_link resource.  
  
### static::sKAdNetworkConversionValueSchemaName

Formats a string containing the fully-qualified path to represent a sk_ad_network_conversion_value_schema resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
`skadnetworkConversionValueSchema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted sk_ad_network_conversion_value_schema resource.  
  
### static::searchAds360LinkName

Formats a string containing the fully-qualified path to represent a search_ads360_link resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`searchAds360Link` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted search_ads360_link resource.  
  
### static::subpropertyEventFilterName

Formats a string containing the fully-qualified path to represent a subproperty_event_filter resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`subPropertyEventFilter` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted subproperty_event_filter resource.  
  
### static::subpropertySyncConfigName

Formats a string containing the fully-qualified path to represent a subproperty_sync_config resource.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`subpropertySyncConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted subproperty_sync_config resource.  
  
### static::userProvidedDataSettingsName

Formats a string containing the fully-qualified path to represent a user_provided_data_settings resource.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted user_provided_data_settings resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * accessBinding: accounts/{account}/accessBindings/{access_binding}
  * account: accounts/{account}
  * accountAccessBinding: accounts/{account}/accessBindings/{access_binding}
  * adSenseLink: properties/{property}/adSenseLinks/{adsense_link}
  * attributionSettings: properties/{property}/attributionSettings
  * audience: properties/{property}/audiences/{audience}
  * bigQueryLink: properties/{property}/bigQueryLinks/{bigquery_link}
  * calculatedMetric: properties/{property}/calculatedMetrics/{calculated_metric}
  * channelGroup: properties/{property}/channelGroups/{channel_group}
  * conversionEvent: properties/{property}/conversionEvents/{conversion_event}
  * customDimension: properties/{property}/customDimensions/{custom_dimension}
  * customMetric: properties/{property}/customMetrics/{custom_metric}
  * dataRedactionSettings: properties/{property}/dataStreams/{data_stream}/dataRedactionSettings
  * dataRetentionSettings: properties/{property}/dataRetentionSettings
  * dataSharingSettings: accounts/{account}/dataSharingSettings
  * dataStream: properties/{property}/dataStreams/{data_stream}
  * displayVideo360AdvertiserLink: properties/{property}/displayVideo360AdvertiserLinks/{display_video_360_advertiser_link}
  * displayVideo360AdvertiserLinkProposal: properties/{property}/displayVideo360AdvertiserLinkProposals/{display_video_360_advertiser_link_proposal}
  * enhancedMeasurementSettings: properties/{property}/dataStreams/{data_stream}/enhancedMeasurementSettings
  * eventCreateRule: properties/{property}/dataStreams/{data_stream}/eventCreateRules/{event_create_rule}
  * eventEditRule: properties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_rule}
  * expandedDataSet: properties/{property}/expandedDataSets/{expanded_data_set}
  * firebaseLink: properties/{property}/firebaseLinks/{firebase_link}
  * globalSiteTag: properties/{property}/dataStreams/{data_stream}/globalSiteTag
  * googleAdsLink: properties/{property}/googleAdsLinks/{google_ads_link}
  * googleSignalsSettings: properties/{property}/googleSignalsSettings
  * keyEvent: properties/{property}/keyEvents/{key_event}
  * measurementProtocolSecret: properties/{property}/dataStreams/{data_stream}/measurementProtocolSecrets/{measurement_protocol_secret}
  * organization: organizations/{organization}
  * property: properties/{property}
  * propertyAccessBinding: properties/{property}/accessBindings/{access_binding}
  * reportingDataAnnotation: properties/{property}/reportingDataAnnotations/{reporting_data_annotation}
  * reportingIdentitySettings: properties/{property}/reportingIdentitySettings
  * rollupPropertySourceLink: properties/{property}/rollupPropertySourceLinks/{rollup_property_source_link}
  * sKAdNetworkConversionValueSchema: properties/{property}/dataStreams/{data_stream}/sKAdNetworkConversionValueSchema/{skadnetwork_conversion_value_schema}
  * searchAds360Link: properties/{property}/searchAds360Links/{search_ads_360_link}
  * subpropertyEventFilter: properties/{property}/subpropertyEventFilters/{sub_property_event_filter}
  * subpropertySyncConfig: properties/{property}/subpropertySyncConfigs/{subproperty_sync_config}
  * userProvidedDataSettings: properties/{property}/userProvidedDataSettings



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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
