---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient
title: Google Cloud Backup Dr V1beta Client - Class BackupDrProtectionSummaryClient (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:02.438986+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupDrProtectionSummaryClient (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupDrProtectionSummaryClient (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupDrProtectionSummaryClient.

Service Description: The Protection Summary service.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Cloud \ BackupDR \ V1beta \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\BackupDR\V1beta\BackupDrProtectionSummaryClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new BackupDrProtectionSummaryClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### listResourceBackupConfigs

Lists ResourceBackupConfigs.

The async variant is [BackupDrProtectionSummaryClient::listResourceBackupConfigsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDrProtectionSummaryClient__listResourceBackupConfigsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListResourceBackupConfigsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListResourceBackupConfigsRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDrProtectionSummaryClient;
    use Google\Cloud\BackupDR\V1beta\ListResourceBackupConfigsRequest;
    use Google\Cloud\BackupDR\V1beta\ResourceBackupConfig;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve resource backup
     *                                configs. Format: 'projects/{project_id}/locations/{location}'. In Google
     *                                Cloud Backup and DR, locations map to Google Cloud regions, for example
     *                                **us-central1**. Please see
     *                                {@see BackupDrProtectionSummaryClient::locationName()} for help formatting this field.
     */
    function list_resource_backup_configs_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDrProtectionSummaryClient = new BackupDrProtectionSummaryClient();
    
        // Prepare the request message.
        $request = (new ListResourceBackupConfigsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDrProtectionSummaryClient->listResourceBackupConfigs($request);
    
            /** @var ResourceBackupConfig $element */
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
        $formattedParent = BackupDrProtectionSummaryClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_resource_backup_configs_sample($formattedParent);
    }
    

### getLocation

Gets information about a location.

The async variant is [BackupDrProtectionSummaryClient::getLocationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDrProtectionSummaryClient__getLocationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Location\GetLocationRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.GetLocationRequest.html)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Location\Location](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.Location.html)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDrProtectionSummaryClient;
    use Google\Cloud\Location\GetLocationRequest;
    use Google\Cloud\Location\Location;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function get_location_sample(): void
    {
        // Create a client.
        $backupDrProtectionSummaryClient = new BackupDrProtectionSummaryClient();
    
        // Prepare the request message.
        $request = new GetLocationRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var Location $response */
            $response = $backupDrProtectionSummaryClient->getLocation($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### listLocations

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.ListLocationsRequest.html#_Google_Cloud_Location_ListLocationsRequest__getName__) field: * **Global locations** : If `name` is empty, the method lists the public locations available to all projects. * **Project-specific locations** : If `name` follows the format `projects/{project}`, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the `name` field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

The async variant is [BackupDrProtectionSummaryClient::listLocationsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDrProtectionSummaryClient__listLocationsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Location\ListLocationsRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.ListLocationsRequest.html)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDrProtectionSummaryClient;
    use Google\Cloud\Location\ListLocationsRequest;
    use Google\Cloud\Location\Location;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function list_locations_sample(): void
    {
        // Create a client.
        $backupDrProtectionSummaryClient = new BackupDrProtectionSummaryClient();
    
        // Prepare the request message.
        $request = new ListLocationsRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDrProtectionSummaryClient->listLocations($request);
    
            /** @var Location $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### getIamPolicy

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

The async variant is [BackupDrProtectionSummaryClient::getIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDrProtectionSummaryClient__getIamPolicyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Iam\V1\GetIamPolicyRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.GetIamPolicyRequest.html)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Iam\V1\Policy](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.Policy.html)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDrProtectionSummaryClient;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\Policy;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being requested.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function get_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $backupDrProtectionSummaryClient = new BackupDrProtectionSummaryClient();
    
        // Prepare the request message.
        $request = (new GetIamPolicyRequest())
            ->setResource($resource);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $backupDrProtectionSummaryClient->getIamPolicy($request);
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
        $resource = '[RESOURCE]';
    
        get_iam_policy_sample($resource);
    }
    

### setIamPolicy

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

The async variant is [BackupDrProtectionSummaryClient::setIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDrProtectionSummaryClient__setIamPolicyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Iam\V1\SetIamPolicyRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.SetIamPolicyRequest.html)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Iam\V1\Policy](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.Policy.html)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDrProtectionSummaryClient;
    use Google\Cloud\Iam\V1\Policy;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being specified.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function set_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $backupDrProtectionSummaryClient = new BackupDrProtectionSummaryClient();
    
        // Prepare the request message.
        $policy = new Policy();
        $request = (new SetIamPolicyRequest())
            ->setResource($resource)
            ->setPolicy($policy);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $backupDrProtectionSummaryClient->setIamPolicy($request);
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
        $resource = '[RESOURCE]';
    
        set_iam_policy_sample($resource);
    }
    

### testIamPermissions

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

The async variant is [BackupDrProtectionSummaryClient::testIamPermissionsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDrProtectionSummaryClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDrProtectionSummaryClient__testIamPermissionsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Iam\V1\TestIamPermissionsRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.TestIamPermissionsRequest.html)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Iam\V1\TestIamPermissionsResponse](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.TestIamPermissionsResponse.html)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDrProtectionSummaryClient;
    use Google\Cloud\Iam\V1\TestIamPermissionsRequest;
    use Google\Cloud\Iam\V1\TestIamPermissionsResponse;
    
    /**
     * @param string $resource           REQUIRED: The resource for which the policy detail is being requested.
     *                                   See the operation documentation for the appropriate value for this field.
     * @param string $permissionsElement The set of permissions to check for the `resource`. Permissions with
     *                                   wildcards (such as '*' or 'storage.*') are not allowed. For more
     *                                   information see
     *                                   [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).
     */
    function test_iam_permissions_sample(string $resource, string $permissionsElement): void
    {
        // Create a client.
        $backupDrProtectionSummaryClient = new BackupDrProtectionSummaryClient();
    
        // Prepare the request message.
        $permissions = [$permissionsElement,];
        $request = (new TestIamPermissionsRequest())
            ->setResource($resource)
            ->setPermissions($permissions);
    
        // Call the API and handle any network failures.
        try {
            /** @var TestIamPermissionsResponse $response */
            $response = $backupDrProtectionSummaryClient->testIamPermissions($request);
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
        $resource = '[RESOURCE]';
        $permissionsElement = '[PERMISSIONS]';
    
        test_iam_permissions_sample($resource, $permissionsElement);
    }
    

### listResourceBackupConfigsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListResourceBackupConfigsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListResourceBackupConfigsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### getLocationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Location\GetLocationRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.GetLocationRequest.html)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Location\Location](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.Location.html)>` |   
  
### listLocationsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Location\ListLocationsRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.ListLocationsRequest.html)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### getIamPolicyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Iam\V1\GetIamPolicyRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.GetIamPolicyRequest.html)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Iam\V1\Policy](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.Policy.html)>` |   
  
### setIamPolicyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Iam\V1\SetIamPolicyRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.SetIamPolicyRequest.html)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Iam\V1\Policy](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.Policy.html)>` |   
  
### testIamPermissionsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Iam\V1\TestIamPermissionsRequest](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.TestIamPermissionsRequest.html)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Iam\V1\TestIamPermissionsResponse](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.TestIamPermissionsResponse.html)>` |   
  
### static::locationName

Formats a string containing the fully-qualified path to represent a location resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted location resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * location: projects/{project}/locations/{location}



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
