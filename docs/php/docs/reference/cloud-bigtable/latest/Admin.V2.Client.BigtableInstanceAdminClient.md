---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient
title: Cloud Bigtable V2 Client - Class BigtableInstanceAdminClient (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:31.940144+00:00
---

# Cloud Bigtable V2 Client - Class BigtableInstanceAdminClient (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class BigtableInstanceAdminClient (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class BigtableInstanceAdminClient.

Service Description: Service for creating, configuring, and deleting Cloud Bigtable Instances and Clusters. Provides access to the Instance and Cluster schemas only, not the tables' metadata or data stored in those tables.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2 \ Client

## Methods 

### __construct

Constructor.

Setting the "BIGTABLE_EMULATOR_HOST" environment variable will automatically set the API Endpoint to the value specified in the variable, as well as ensure that empty credentials are used in the transport layer.

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array|[Google\ApiCore\Options\ClientOptions](https://docs.cloud.google.com/php/docs/reference/gax/latest/Options.ClientOptions.html)`   
Optional. Options for configuring the service API wrapper.  
`↳ apiEndpoint` |  `string`   
The address of the API remote host. May optionally include the port, formatted as "  
`↳ credentials` |  `[Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html)|[Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html)`   
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\Bigtable\Admin\V2\BigtableInstanceAdminClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new BigtableInstanceAdminClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### createAppProfile

Creates an app profile within an instance.

The async variant is [BigtableInstanceAdminClient::createAppProfileAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__createAppProfileAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateAppProfileRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\AppProfile](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\AppProfile;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateAppProfileRequest;
    
    /**
     * @param string $formattedParent The unique name of the instance in which to create the new app
     *                                profile. Values are of the form `projects/{project}/instances/{instance}`. Please see
     *                                {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     * @param string $appProfileId    The ID to be used when referring to the new app profile within
     *                                its instance, e.g., just `myprofile` rather than
     *                                `projects/myproject/instances/myinstance/appProfiles/myprofile`.
     */
    function create_app_profile_sample(string $formattedParent, string $appProfileId): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $appProfile = new AppProfile();
        $request = (new CreateAppProfileRequest())
            ->setParent($formattedParent)
            ->setAppProfileId($appProfileId)
            ->setAppProfile($appProfile);
    
        // Call the API and handle any network failures.
        try {
            /** @var AppProfile $response */
            $response = $bigtableInstanceAdminClient->createAppProfile($request);
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
        $appProfileId = '[APP_PROFILE_ID]';
    
        create_app_profile_sample($formattedParent, $appProfileId);
    }
    

### createCluster

Creates a cluster within an instance.

Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled.

The async variant is [BigtableInstanceAdminClient::createClusterAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__createClusterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateClusterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Cluster;
    use Google\Cloud\Bigtable\Admin\V2\CreateClusterRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent The unique name of the instance in which to create the new
     *                                cluster. Values are of the form `projects/{project}/instances/{instance}`. Please see
     *                                {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     * @param string $clusterId       The ID to be used when referring to the new cluster within its
     *                                instance, e.g., just `mycluster` rather than
     *                                `projects/myproject/instances/myinstance/clusters/mycluster`.
     */
    function create_cluster_sample(string $formattedParent, string $clusterId): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $cluster = new Cluster();
        $request = (new CreateClusterRequest())
            ->setParent($formattedParent)
            ->setClusterId($clusterId)
            ->setCluster($cluster);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->createCluster($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Cluster $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
        $clusterId = '[CLUSTER_ID]';
    
        create_cluster_sample($formattedParent, $clusterId);
    }
    

### createInstance

Create an instance within a project.

Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled.

The async variant is [BigtableInstanceAdminClient::createInstanceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__createInstanceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateInstanceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\Instance;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent     The unique name of the project in which to create the new
     *                                    instance. Values are of the form `projects/{project}`. Please see
     *                                    {@see BigtableInstanceAdminClient::projectName()} for help formatting this field.
     * @param string $instanceId          The ID to be used when referring to the new instance within its
     *                                    project, e.g., just `myinstance` rather than
     *                                    `projects/myproject/instances/myinstance`.
     * @param string $instanceDisplayName The descriptive name for this instance as it appears in UIs.
     *                                    Can be changed at any time, but should be kept globally unique
     *                                    to avoid confusion.
     */
    function create_instance_sample(
        string $formattedParent,
        string $instanceId,
        string $instanceDisplayName
    ): void {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $instance = (new Instance())
            ->setDisplayName($instanceDisplayName);
        $clusters = [];
        $request = (new CreateInstanceRequest())
            ->setParent($formattedParent)
            ->setInstanceId($instanceId)
            ->setInstance($instance)
            ->setClusters($clusters);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->createInstance($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Instance $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $formattedParent = BigtableInstanceAdminClient::projectName('[PROJECT]');
        $instanceId = '[INSTANCE_ID]';
        $instanceDisplayName = '[DISPLAY_NAME]';
    
        create_instance_sample($formattedParent, $instanceId, $instanceDisplayName);
    }
    

### createLogicalView

Creates a logical view within an instance.

The async variant is [BigtableInstanceAdminClient::createLogicalViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__createLogicalViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateLogicalViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\LogicalView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.LogicalView)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateLogicalViewRequest;
    use Google\Cloud\Bigtable\Admin\V2\LogicalView;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent  The parent instance where this logical view will be created.
     *                                 Format: `projects/{project}/instances/{instance}`. Please see
     *                                 {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     * @param string $logicalViewId    The ID to use for the logical view, which will become the final
     *                                 component of the logical view's resource name.
     * @param string $logicalViewQuery The logical view's select query.
     */
    function create_logical_view_sample(
        string $formattedParent,
        string $logicalViewId,
        string $logicalViewQuery
    ): void {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $logicalView = (new LogicalView())
            ->setQuery($logicalViewQuery);
        $request = (new CreateLogicalViewRequest())
            ->setParent($formattedParent)
            ->setLogicalViewId($logicalViewId)
            ->setLogicalView($logicalView);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->createLogicalView($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var LogicalView $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
        $logicalViewId = '[LOGICAL_VIEW_ID]';
        $logicalViewQuery = '[QUERY]';
    
        create_logical_view_sample($formattedParent, $logicalViewId, $logicalViewQuery);
    }
    

### createMaterializedView

Creates a materialized view within an instance.

The async variant is [BigtableInstanceAdminClient::createMaterializedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__createMaterializedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateMaterializedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\MaterializedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MaterializedView)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateMaterializedViewRequest;
    use Google\Cloud\Bigtable\Admin\V2\MaterializedView;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent       The parent instance where this materialized view will be created.
     *                                      Format: `projects/{project}/instances/{instance}`. Please see
     *                                      {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     * @param string $materializedViewId    The ID to use for the materialized view, which will become the
     *                                      final component of the materialized view's resource name.
     * @param string $materializedViewQuery Immutable. The materialized view's select query.
     */
    function create_materialized_view_sample(
        string $formattedParent,
        string $materializedViewId,
        string $materializedViewQuery
    ): void {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $materializedView = (new MaterializedView())
            ->setQuery($materializedViewQuery);
        $request = (new CreateMaterializedViewRequest())
            ->setParent($formattedParent)
            ->setMaterializedViewId($materializedViewId)
            ->setMaterializedView($materializedView);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->createMaterializedView($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var MaterializedView $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
        $materializedViewId = '[MATERIALIZED_VIEW_ID]';
        $materializedViewQuery = '[QUERY]';
    
        create_materialized_view_sample($formattedParent, $materializedViewId, $materializedViewQuery);
    }
    

### deleteAppProfile

Deletes an app profile from an instance.

The async variant is [BigtableInstanceAdminClient::deleteAppProfileAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__deleteAppProfileAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteAppProfileRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteAppProfileRequest;
    
    /**
     * @param string $formattedName  The unique name of the app profile to be deleted. Values are of
     *                               the form
     *                               `projects/{project}/instances/{instance}/appProfiles/{app_profile}`. Please see
     *                               {@see BigtableInstanceAdminClient::appProfileName()} for help formatting this field.
     * @param bool   $ignoreWarnings If true, ignore safety checks when deleting the app profile.
     */
    function delete_app_profile_sample(string $formattedName, bool $ignoreWarnings): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteAppProfileRequest())
            ->setName($formattedName)
            ->setIgnoreWarnings($ignoreWarnings);
    
        // Call the API and handle any network failures.
        try {
            $bigtableInstanceAdminClient->deleteAppProfile($request);
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
        $formattedName = BigtableInstanceAdminClient::appProfileName(
            '[PROJECT]',
            '[INSTANCE]',
            '[APP_PROFILE]'
        );
        $ignoreWarnings = false;
    
        delete_app_profile_sample($formattedName, $ignoreWarnings);
    }
    

### deleteCluster

Deletes a cluster from an instance.

The async variant is [BigtableInstanceAdminClient::deleteClusterAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__deleteClusterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteClusterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteClusterRequest;
    
    /**
     * @param string $formattedName The unique name of the cluster to be deleted. Values are of the
     *                              form `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see
     *                              {@see BigtableInstanceAdminClient::clusterName()} for help formatting this field.
     */
    function delete_cluster_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteClusterRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableInstanceAdminClient->deleteCluster($request);
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
        $formattedName = BigtableInstanceAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
    
        delete_cluster_sample($formattedName);
    }
    

### deleteInstance

Delete an instance from a project.

The async variant is [BigtableInstanceAdminClient::deleteInstanceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__deleteInstanceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteInstanceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteInstanceRequest;
    
    /**
     * @param string $formattedName The unique name of the instance to be deleted.
     *                              Values are of the form `projects/{project}/instances/{instance}`. Please see
     *                              {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     */
    function delete_instance_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteInstanceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableInstanceAdminClient->deleteInstance($request);
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
        $formattedName = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
    
        delete_instance_sample($formattedName);
    }
    

### deleteLogicalView

Deletes a logical view from an instance.

The async variant is [BigtableInstanceAdminClient::deleteLogicalViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__deleteLogicalViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteLogicalViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteLogicalViewRequest;
    
    /**
     * @param string $formattedName The unique name of the logical view to be deleted.
     *                              Format:
     *                              `projects/{project}/instances/{instance}/logicalViews/{logical_view}`. Please see
     *                              {@see BigtableInstanceAdminClient::logicalViewName()} for help formatting this field.
     */
    function delete_logical_view_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteLogicalViewRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableInstanceAdminClient->deleteLogicalView($request);
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
        $formattedName = BigtableInstanceAdminClient::logicalViewName(
            '[PROJECT]',
            '[INSTANCE]',
            '[LOGICAL_VIEW]'
        );
    
        delete_logical_view_sample($formattedName);
    }
    

### deleteMaterializedView

Deletes a materialized view from an instance.

The async variant is [BigtableInstanceAdminClient::deleteMaterializedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__deleteMaterializedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteMaterializedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteMaterializedViewRequest;
    
    /**
     * @param string $formattedName The unique name of the materialized view to be deleted.
     *                              Format:
     *                              `projects/{project}/instances/{instance}/materializedViews/{materialized_view}`. Please see
     *                              {@see BigtableInstanceAdminClient::materializedViewName()} for help formatting this field.
     */
    function delete_materialized_view_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteMaterializedViewRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableInstanceAdminClient->deleteMaterializedView($request);
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
        $formattedName = BigtableInstanceAdminClient::materializedViewName(
            '[PROJECT]',
            '[INSTANCE]',
            '[MATERIALIZED_VIEW]'
        );
    
        delete_materialized_view_sample($formattedName);
    }
    

### getAppProfile

Gets information about an app profile.

The async variant is [BigtableInstanceAdminClient::getAppProfileAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__getAppProfileAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetAppProfileRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\AppProfile](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\AppProfile;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetAppProfileRequest;
    
    /**
     * @param string $formattedName The unique name of the requested app profile. Values are of the
     *                              form `projects/{project}/instances/{instance}/appProfiles/{app_profile}`. Please see
     *                              {@see BigtableInstanceAdminClient::appProfileName()} for help formatting this field.
     */
    function get_app_profile_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new GetAppProfileRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var AppProfile $response */
            $response = $bigtableInstanceAdminClient->getAppProfile($request);
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
        $formattedName = BigtableInstanceAdminClient::appProfileName(
            '[PROJECT]',
            '[INSTANCE]',
            '[APP_PROFILE]'
        );
    
        get_app_profile_sample($formattedName);
    }
    

### getCluster

Gets information about a cluster.

The async variant is [BigtableInstanceAdminClient::getClusterAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__getClusterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetClusterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Cluster;
    use Google\Cloud\Bigtable\Admin\V2\GetClusterRequest;
    
    /**
     * @param string $formattedName The unique name of the requested cluster. Values are of the form
     *                              `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see
     *                              {@see BigtableInstanceAdminClient::clusterName()} for help formatting this field.
     */
    function get_cluster_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new GetClusterRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Cluster $response */
            $response = $bigtableInstanceAdminClient->getCluster($request);
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
        $formattedName = BigtableInstanceAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
    
        get_cluster_sample($formattedName);
    }
    

### getIamPolicy

Gets the access control policy for an instance resource. Returns an empty policy if an instance exists but does not have a policy set.

The async variant is [BigtableInstanceAdminClient::getIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__getIamPolicyAsync__) .

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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\Policy;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being requested.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function get_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new GetIamPolicyRequest())
            ->setResource($resource);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $bigtableInstanceAdminClient->getIamPolicy($request);
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
    

### getInstance

Gets information about an instance.

The async variant is [BigtableInstanceAdminClient::getInstanceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__getInstanceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetInstanceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\Instance;
    
    /**
     * @param string $formattedName The unique name of the requested instance. Values are of the form
     *                              `projects/{project}/instances/{instance}`. Please see
     *                              {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     */
    function get_instance_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new GetInstanceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Instance $response */
            $response = $bigtableInstanceAdminClient->getInstance($request);
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
        $formattedName = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
    
        get_instance_sample($formattedName);
    }
    

### getLogicalView

Gets information about a logical view.

The async variant is [BigtableInstanceAdminClient::getLogicalViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__getLogicalViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetLogicalViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\LogicalView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.LogicalView)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetLogicalViewRequest;
    use Google\Cloud\Bigtable\Admin\V2\LogicalView;
    
    /**
     * @param string $formattedName The unique name of the requested logical view. Values are of the
     *                              form `projects/{project}/instances/{instance}/logicalViews/{logical_view}`. Please see
     *                              {@see BigtableInstanceAdminClient::logicalViewName()} for help formatting this field.
     */
    function get_logical_view_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new GetLogicalViewRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var LogicalView $response */
            $response = $bigtableInstanceAdminClient->getLogicalView($request);
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
        $formattedName = BigtableInstanceAdminClient::logicalViewName(
            '[PROJECT]',
            '[INSTANCE]',
            '[LOGICAL_VIEW]'
        );
    
        get_logical_view_sample($formattedName);
    }
    

### getMaterializedView

Gets information about a materialized view.

The async variant is [BigtableInstanceAdminClient::getMaterializedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__getMaterializedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetMaterializedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\MaterializedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MaterializedView)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetMaterializedViewRequest;
    use Google\Cloud\Bigtable\Admin\V2\MaterializedView;
    
    /**
     * @param string $formattedName The unique name of the requested materialized view. Values are of
     *                              the form
     *                              `projects/{project}/instances/{instance}/materializedViews/{materialized_view}`. Please see
     *                              {@see BigtableInstanceAdminClient::materializedViewName()} for help formatting this field.
     */
    function get_materialized_view_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new GetMaterializedViewRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var MaterializedView $response */
            $response = $bigtableInstanceAdminClient->getMaterializedView($request);
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
        $formattedName = BigtableInstanceAdminClient::materializedViewName(
            '[PROJECT]',
            '[INSTANCE]',
            '[MATERIALIZED_VIEW]'
        );
    
        get_materialized_view_sample($formattedName);
    }
    

### getMemoryLayer

Gets information about the memory layer of a cluster.

The async variant is [BigtableInstanceAdminClient::getMemoryLayerAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__getMemoryLayerAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetMemoryLayerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetMemoryLayerRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\MemoryLayer](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetMemoryLayerRequest;
    use Google\Cloud\Bigtable\Admin\V2\MemoryLayer;
    
    /**
     * @param string $formattedName The unique name of the requested cluster's memory layer. Values
     *                              are of the form
     *                              `projects/{project}/instances/{instance}/clusters/{cluster}/memoryLayer`. Please see
     *                              {@see BigtableInstanceAdminClient::memoryLayerName()} for help formatting this field.
     */
    function get_memory_layer_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new GetMemoryLayerRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var MemoryLayer $response */
            $response = $bigtableInstanceAdminClient->getMemoryLayer($request);
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
        $formattedName = BigtableInstanceAdminClient::memoryLayerName(
            '[PROJECT]',
            '[INSTANCE]',
            '[CLUSTER]'
        );
    
        get_memory_layer_sample($formattedName);
    }
    

### listAppProfiles

Lists information about app profiles in an instance.

The async variant is [BigtableInstanceAdminClient::listAppProfilesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__listAppProfilesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListAppProfilesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListAppProfilesRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\AppProfile;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListAppProfilesRequest;
    
    /**
     * @param string $formattedParent The unique name of the instance for which a list of app profiles
     *                                is requested. Values are of the form
     *                                `projects/{project}/instances/{instance}`.
     *                                Use `{instance} = '-'` to list AppProfiles for all Instances in a project,
     *                                e.g., `projects/myproject/instances/-`. Please see
     *                                {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     */
    function list_app_profiles_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new ListAppProfilesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableInstanceAdminClient->listAppProfiles($request);
    
            /** @var AppProfile $element */
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
    
        list_app_profiles_sample($formattedParent);
    }
    

### listClusters

Lists information about clusters in an instance.

The async variant is [BigtableInstanceAdminClient::listClustersAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__listClustersAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListClustersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListClustersRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\ListClustersResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListClustersResponse)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListClustersRequest;
    use Google\Cloud\Bigtable\Admin\V2\ListClustersResponse;
    
    /**
     * @param string $formattedParent The unique name of the instance for which a list of clusters is
     *                                requested. Values are of the form
     *                                `projects/{project}/instances/{instance}`. Use `{instance} = '-'` to list
     *                                Clusters for all Instances in a project, e.g.,
     *                                `projects/myproject/instances/-`. Please see
     *                                {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     */
    function list_clusters_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new ListClustersRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var ListClustersResponse $response */
            $response = $bigtableInstanceAdminClient->listClusters($request);
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
    
        list_clusters_sample($formattedParent);
    }
    

### listHotTablets

Lists hot tablets in a cluster, within the time range provided. Hot tablets are ordered based on CPU usage.

The async variant is [BigtableInstanceAdminClient::listHotTabletsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__listHotTabletsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListHotTabletsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListHotTabletsRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\HotTablet;
    use Google\Cloud\Bigtable\Admin\V2\ListHotTabletsRequest;
    
    /**
     * @param string $formattedParent The cluster name to list hot tablets.
     *                                Value is in the following form:
     *                                `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see
     *                                {@see BigtableInstanceAdminClient::clusterName()} for help formatting this field.
     */
    function list_hot_tablets_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new ListHotTabletsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableInstanceAdminClient->listHotTablets($request);
    
            /** @var HotTablet $element */
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
        $formattedParent = BigtableInstanceAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
    
        list_hot_tablets_sample($formattedParent);
    }
    

### listInstances

Lists information about instances in a project.

The async variant is [BigtableInstanceAdminClient::listInstancesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__listInstancesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListInstancesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListInstancesRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListInstancesResponse)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListInstancesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ListInstancesResponse;
    
    /**
     * @param string $formattedParent The unique name of the project for which a list of instances is
     *                                requested. Values are of the form `projects/{project}`. Please see
     *                                {@see BigtableInstanceAdminClient::projectName()} for help formatting this field.
     */
    function list_instances_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new ListInstancesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var ListInstancesResponse $response */
            $response = $bigtableInstanceAdminClient->listInstances($request);
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
        $formattedParent = BigtableInstanceAdminClient::projectName('[PROJECT]');
    
        list_instances_sample($formattedParent);
    }
    

### listLogicalViews

Lists information about logical views in an instance.

The async variant is [BigtableInstanceAdminClient::listLogicalViewsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__listLogicalViewsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListLogicalViewsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListLogicalViewsRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListLogicalViewsRequest;
    use Google\Cloud\Bigtable\Admin\V2\LogicalView;
    
    /**
     * @param string $formattedParent The unique name of the instance for which the list of logical
     *                                views is requested. Values are of the form
     *                                `projects/{project}/instances/{instance}`. Please see
     *                                {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     */
    function list_logical_views_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new ListLogicalViewsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableInstanceAdminClient->listLogicalViews($request);
    
            /** @var LogicalView $element */
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
    
        list_logical_views_sample($formattedParent);
    }
    

### listMaterializedViews

Lists information about materialized views in an instance.

The async variant is [BigtableInstanceAdminClient::listMaterializedViewsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__listMaterializedViewsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListMaterializedViewsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListMaterializedViewsRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListMaterializedViewsRequest;
    use Google\Cloud\Bigtable\Admin\V2\MaterializedView;
    
    /**
     * @param string $formattedParent The unique name of the instance for which the list of
     *                                materialized views is requested. Values are of the form
     *                                `projects/{project}/instances/{instance}`. Please see
     *                                {@see BigtableInstanceAdminClient::instanceName()} for help formatting this field.
     */
    function list_materialized_views_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new ListMaterializedViewsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableInstanceAdminClient->listMaterializedViews($request);
    
            /** @var MaterializedView $element */
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
        $formattedParent = BigtableInstanceAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
    
        list_materialized_views_sample($formattedParent);
    }
    

### listMemoryLayers

Lists information about memory layers.

The async variant is [BigtableInstanceAdminClient::listMemoryLayersAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__listMemoryLayersAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListMemoryLayersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListMemoryLayersRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListMemoryLayersRequest;
    use Google\Cloud\Bigtable\Admin\V2\MemoryLayer;
    
    /**
     * @param string $formattedParent The unique name of the cluster for which a list of memory layers
     *                                is requested. Values are of the form
     *                                `projects/{project}/instances/{instance}/clusters/{cluster}`.
     *                                Use `{cluster} = '-'` to list MemoryLayers for all Clusters in an instance,
     *                                e.g., `projects/myproject/instances/myinstance/clusters/-`. Please see
     *                                {@see BigtableInstanceAdminClient::clusterName()} for help formatting this field.
     */
    function list_memory_layers_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new ListMemoryLayersRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableInstanceAdminClient->listMemoryLayers($request);
    
            /** @var MemoryLayer $element */
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
        $formattedParent = BigtableInstanceAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
    
        list_memory_layers_sample($formattedParent);
    }
    

### partialUpdateCluster

Partially updates a cluster within a project. This method is the preferred way to update a Cluster.

To enable and update autoscaling, set cluster_config.cluster_autoscaling_config. When autoscaling is enabled, serve_nodes is treated as an OUTPUT_ONLY field, meaning that updates to it are ignored. Note that an update cannot simultaneously set serve_nodes to non-zero and cluster_config.cluster_autoscaling_config to non-empty, and also specify both in the update_mask.

To disable autoscaling, clear cluster_config.cluster_autoscaling_config, and explicitly set a serve_node count via the update_mask.

The async variant is [BigtableInstanceAdminClient::partialUpdateClusterAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__partialUpdateClusterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\PartialUpdateClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.PartialUpdateClusterRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Cluster;
    use Google\Cloud\Bigtable\Admin\V2\PartialUpdateClusterRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function partial_update_cluster_sample(): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $cluster = new Cluster();
        $updateMask = new FieldMask();
        $request = (new PartialUpdateClusterRequest())
            ->setCluster($cluster)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->partialUpdateCluster($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Cluster $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### partialUpdateInstance

Partially updates an instance within a project. This method can modify all fields of an Instance and is the preferred way to update an Instance.

The async variant is [BigtableInstanceAdminClient::partialUpdateInstanceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__partialUpdateInstanceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\PartialUpdateInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.PartialUpdateInstanceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Instance;
    use Google\Cloud\Bigtable\Admin\V2\PartialUpdateInstanceRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * @param string $instanceDisplayName The descriptive name for this instance as it appears in UIs.
     *                                    Can be changed at any time, but should be kept globally unique
     *                                    to avoid confusion.
     */
    function partial_update_instance_sample(string $instanceDisplayName): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $instance = (new Instance())
            ->setDisplayName($instanceDisplayName);
        $updateMask = new FieldMask();
        $request = (new PartialUpdateInstanceRequest())
            ->setInstance($instance)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->partialUpdateInstance($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Instance $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $instanceDisplayName = '[DISPLAY_NAME]';
    
        partial_update_instance_sample($instanceDisplayName);
    }
    

### setIamPolicy

Sets the access control policy on an instance resource. Replaces any existing policy.

The async variant is [BigtableInstanceAdminClient::setIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__setIamPolicyAsync__) .

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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Iam\V1\Policy;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being specified.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function set_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $policy = new Policy();
        $request = (new SetIamPolicyRequest())
            ->setResource($resource)
            ->setPolicy($policy);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $bigtableInstanceAdminClient->setIamPolicy($request);
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

Returns permissions that the caller has on the specified instance resource.

The async variant is [BigtableInstanceAdminClient::testIamPermissionsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__testIamPermissionsAsync__) .

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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
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
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $permissions = [$permissionsElement,];
        $request = (new TestIamPermissionsRequest())
            ->setResource($resource)
            ->setPermissions($permissions);
    
        // Call the API and handle any network failures.
        try {
            /** @var TestIamPermissionsResponse $response */
            $response = $bigtableInstanceAdminClient->testIamPermissions($request);
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
    

### updateAppProfile

Updates an app profile within an instance.

The async variant is [BigtableInstanceAdminClient::updateAppProfileAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__updateAppProfileAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateAppProfileRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\AppProfile](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\AppProfile;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\UpdateAppProfileRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_app_profile_sample(): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $appProfile = new AppProfile();
        $updateMask = new FieldMask();
        $request = (new UpdateAppProfileRequest())
            ->setAppProfile($appProfile)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->updateAppProfile($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AppProfile $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### updateCluster

Updates a cluster within an instance.

Note that UpdateCluster does not support updating cluster_config.cluster_autoscaling_config. In order to update it, you must use PartialUpdateCluster.

The async variant is [BigtableInstanceAdminClient::updateClusterAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__updateClusterAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Cluster;
    use Google\Rpc\Status;
    
    /**
     * @param string $name       The unique name of the cluster. Values are of the form
     *                           `projects/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*`.
     * @param int    $serveNodes The number of nodes in the cluster. If no value is set,
     *                           Cloud Bigtable automatically allocates nodes based on your data footprint
     *                           and optimized for 50% storage utilization.
     */
    function update_cluster_sample(string $name, int $serveNodes): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $request = (new Cluster())
            ->setName($name)
            ->setServeNodes($serveNodes);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->updateCluster($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Cluster $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $name = '[NAME]';
        $serveNodes = 0;
    
        update_cluster_sample($name, $serveNodes);
    }
    

### updateInstance

Updates an instance within a project. This method updates only the display name and type for an Instance. To update other Instance properties, such as labels, use PartialUpdateInstance.

The async variant is [BigtableInstanceAdminClient::updateInstanceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__updateInstanceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Instance;
    use Google\Cloud\Bigtable\Admin\V2\Instance\Type;
    
    /**
     * @param string $name        The unique name of the instance. Values are of the form
     *                            `projects/{project}/instances/[a-z][a-z0-9\\-]+[a-z0-9]`.
     * @param string $displayName The descriptive name for this instance as it appears in UIs.
     *                            Can be changed at any time, but should be kept globally unique
     *                            to avoid confusion.
     * @param int    $type        The type of the instance. Defaults to `PRODUCTION`.
     */
    function update_instance_sample(string $name, string $displayName, int $type): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $labels = [];
        $request = (new Instance())
            ->setName($name)
            ->setDisplayName($displayName)
            ->setType($type)
            ->setLabels($labels);
    
        // Call the API and handle any network failures.
        try {
            /** @var Instance $response */
            $response = $bigtableInstanceAdminClient->updateInstance($request);
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
        $name = '[NAME]';
        $displayName = '[DISPLAY_NAME]';
        $type = Type::TYPE_UNSPECIFIED;
    
        update_instance_sample($name, $displayName, $type);
    }
    

### updateLogicalView

Updates a logical view within an instance.

The async variant is [BigtableInstanceAdminClient::updateLogicalViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__updateLogicalViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateLogicalViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\LogicalView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.LogicalView)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\LogicalView;
    use Google\Cloud\Bigtable\Admin\V2\UpdateLogicalViewRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $logicalViewQuery The logical view's select query.
     */
    function update_logical_view_sample(string $logicalViewQuery): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $logicalView = (new LogicalView())
            ->setQuery($logicalViewQuery);
        $request = (new UpdateLogicalViewRequest())
            ->setLogicalView($logicalView);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->updateLogicalView($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var LogicalView $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $logicalViewQuery = '[QUERY]';
    
        update_logical_view_sample($logicalViewQuery);
    }
    

### updateMaterializedView

Updates a materialized view within an instance.

The async variant is [BigtableInstanceAdminClient::updateMaterializedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__updateMaterializedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateMaterializedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\MaterializedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MaterializedView)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\MaterializedView;
    use Google\Cloud\Bigtable\Admin\V2\UpdateMaterializedViewRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $materializedViewQuery Immutable. The materialized view's select query.
     */
    function update_materialized_view_sample(string $materializedViewQuery): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $materializedView = (new MaterializedView())
            ->setQuery($materializedViewQuery);
        $request = (new UpdateMaterializedViewRequest())
            ->setMaterializedView($materializedView);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->updateMaterializedView($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var MaterializedView $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
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
        $materializedViewQuery = '[QUERY]';
    
        update_materialized_view_sample($materializedViewQuery);
    }
    

### updateMemoryLayer

Updates the memory layer of a cluster.

To enable the memory layer, set the memory_config. To disable the memory layer, unset the memory_config.

The async variant is [BigtableInstanceAdminClient::updateMemoryLayerAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableInstanceAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableInstanceAdminClient__updateMemoryLayerAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateMemoryLayerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateMemoryLayerRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\MemoryLayer](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\MemoryLayer;
    use Google\Cloud\Bigtable\Admin\V2\UpdateMemoryLayerRequest;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_memory_layer_sample(): void
    {
        // Create a client.
        $bigtableInstanceAdminClient = new BigtableInstanceAdminClient();
    
        // Prepare the request message.
        $memoryLayer = new MemoryLayer();
        $request = (new UpdateMemoryLayerRequest())
            ->setMemoryLayer($memoryLayer);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableInstanceAdminClient->updateMemoryLayer($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var MemoryLayer $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### createAppProfileAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateAppProfileRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\AppProfile](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile)>` |   
  
### createClusterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateClusterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createInstanceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateInstanceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createLogicalViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateLogicalViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createMaterializedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateMaterializedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteAppProfileAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteAppProfileRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteClusterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteClusterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteInstanceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteInstanceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteLogicalViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteLogicalViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteMaterializedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteMaterializedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### getAppProfileAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetAppProfileRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\AppProfile](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile)>` |   
  
### getClusterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetClusterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)>` |   
  
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
  
### getInstanceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetInstanceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)>` |   
  
### getLogicalViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetLogicalViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\LogicalView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.LogicalView)>` |   
  
### getMaterializedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetMaterializedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\MaterializedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MaterializedView)>` |   
  
### getMemoryLayerAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetMemoryLayerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetMemoryLayerRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\MemoryLayer](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer)>` |   
  
### listAppProfilesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListAppProfilesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListAppProfilesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listClustersAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListClustersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListClustersRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\ListClustersResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListClustersResponse)>` |   
  
### listHotTabletsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListHotTabletsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListHotTabletsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listInstancesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListInstancesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListInstancesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListInstancesResponse)>` |   
  
### listLogicalViewsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListLogicalViewsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListLogicalViewsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listMaterializedViewsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListMaterializedViewsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListMaterializedViewsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listMemoryLayersAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListMemoryLayersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListMemoryLayersRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### partialUpdateClusterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\PartialUpdateClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.PartialUpdateClusterRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### partialUpdateInstanceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\PartialUpdateInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.PartialUpdateInstanceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
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
  
### updateAppProfileAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateAppProfileRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateAppProfileRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateClusterAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateInstanceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)>` |   
  
### updateLogicalViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateLogicalViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateLogicalViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateMaterializedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateMaterializedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateMaterializedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateMemoryLayerAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateMemoryLayerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateMemoryLayerRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### getOperationsClient

Return an OperationsClient object with the same endpoint as $this.

**Returns**  
---  
**Type** | **Description**  
`Google\LongRunning\Client\OperationsClient` |   
  
### resumeOperation

Resume an existing long running operation that was previously started by a long running API method. If $methodName is not provided, or does not match a long running API method, then the operation can still be resumed, but the OperationResponse object will not deserialize the final response.

**Parameters**  
---  
**Name** | **Description**  
`operationName` |  `string`   
The name of the long running operation  
`methodName` |  `string`   
The name of the method used to start the operation  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)` |   
  
### static::appProfileName

Formats a string containing the fully-qualified path to represent a app_profile resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`appProfile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted app_profile resource.  
  
### static::clusterName

Formats a string containing the fully-qualified path to represent a cluster resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`cluster` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted cluster resource.  
  
### static::cryptoKeyName

Formats a string containing the fully-qualified path to represent a crypto_key resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`keyRing` |  `string`   
  
`cryptoKey` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted crypto_key resource.  
  
### static::instanceName

Formats a string containing the fully-qualified path to represent a instance resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted instance resource.  
  
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
  
### static::logicalViewName

Formats a string containing the fully-qualified path to represent a logical_view resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`logicalView` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted logical_view resource.  
  
### static::materializedViewName

Formats a string containing the fully-qualified path to represent a materialized_view resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`materializedView` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted materialized_view resource.  
  
### static::memoryLayerName

Formats a string containing the fully-qualified path to represent a memory_layer resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`cluster` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted memory_layer resource.  
  
### static::projectName

Formats a string containing the fully-qualified path to represent a project resource.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted project resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * appProfile: projects/{project}/instances/{instance}/appProfiles/{app_profile}
  * cluster: projects/{project}/instances/{instance}/clusters/{cluster}
  * cryptoKey: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}
  * instance: projects/{project}/instances/{instance}
  * location: projects/{project}/locations/{location}
  * logicalView: projects/{project}/instances/{instance}/logicalViews/{logical_view}
  * materializedView: projects/{project}/instances/{instance}/materializedViews/{materialized_view}
  * memoryLayer: projects/{project}/instances/{instance}/clusters/{cluster}/memoryLayer
  * project: projects/{project}



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

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
