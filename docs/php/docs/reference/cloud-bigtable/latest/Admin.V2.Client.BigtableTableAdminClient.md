---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient
title: Cloud Bigtable V2 Client - Class BigtableTableAdminClient (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:32.974969+00:00
---

# Cloud Bigtable V2 Client - Class BigtableTableAdminClient (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class BigtableTableAdminClient (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class BigtableTableAdminClient.

Service Description: Service for creating, configuring, and deleting Cloud Bigtable tables.

Provides access to the table schemas only, not the data stored within the tables.

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\Bigtable\Admin\V2\BigtableTableAdminClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new BigtableTableAdminClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### checkConsistency

Checks replication consistency based on a consistency token, that is, if replication has caught up based on the conditions specified in the token and the check request.

The async variant is [BigtableTableAdminClient::checkConsistencyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__checkConsistencyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CheckConsistencyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CheckConsistencyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\CheckConsistencyResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CheckConsistencyResponse)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\CheckConsistencyRequest;
    use Google\Cloud\Bigtable\Admin\V2\CheckConsistencyResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    
    /**
     * @param string $formattedName    The unique name of the Table for which to check replication
     *                                 consistency. Values are of the form
     *                                 `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                                 {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     * @param string $consistencyToken The token created using GenerateConsistencyToken for the Table.
     */
    function check_consistency_sample(string $formattedName, string $consistencyToken): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new CheckConsistencyRequest())
            ->setName($formattedName)
            ->setConsistencyToken($consistencyToken);
    
        // Call the API and handle any network failures.
        try {
            /** @var CheckConsistencyResponse $response */
            $response = $bigtableTableAdminClient->checkConsistency($request);
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
        $consistencyToken = '[CONSISTENCY_TOKEN]';
    
        check_consistency_sample($formattedName, $consistencyToken);
    }
    

### copyBackup

Copy a Cloud Bigtable backup to a new backup in the destination cluster located in the destination instance and project.

The async variant is [BigtableTableAdminClient::copyBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__copyBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CopyBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CopyBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Backup;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CopyBackupRequest;
    use Google\Protobuf\Timestamp;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent       The name of the destination cluster that will contain the backup
     *                                      copy. The cluster must already exist. Values are of the form:
     *                                      `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see
     *                                      {@see BigtableTableAdminClient::clusterName()} for help formatting this field.
     * @param string $backupId              The id of the new backup. The `backup_id` along with `parent`
     *                                      are combined as {parent}/backups/{backup_id} to create the full backup
     *                                      name, of the form:
     *                                      `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_id}`.
     *                                      This string must be between 1 and 50 characters in length and match the
     *                                      regex [_a-zA-Z0-9][-_.a-zA-Z0-9]*.
     * @param string $formattedSourceBackup The source backup to be copied from.
     *                                      The source backup needs to be in READY state for it to be copied.
     *                                      Copying a copied backup is not allowed.
     *                                      Once CopyBackup is in progress, the source backup cannot be deleted or
     *                                      cleaned up on expiration until CopyBackup is finished.
     *                                      Values are of the form:
     *                                      `projects/<project>/instances/<instance>/clusters/<cluster>/backups/<backup>`. Please see
     *                                      {@see BigtableTableAdminClient::backupName()} for help formatting this field.
     */
    function copy_backup_sample(
        string $formattedParent,
        string $backupId,
        string $formattedSourceBackup
    ): void {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $expireTime = new Timestamp();
        $request = (new CopyBackupRequest())
            ->setParent($formattedParent)
            ->setBackupId($backupId)
            ->setSourceBackup($formattedSourceBackup)
            ->setExpireTime($expireTime);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->copyBackup($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Backup $result */
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
        $formattedParent = BigtableTableAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
        $backupId = '[BACKUP_ID]';
        $formattedSourceBackup = BigtableTableAdminClient::backupName(
            '[PROJECT]',
            '[INSTANCE]',
            '[CLUSTER]',
            '[BACKUP]'
        );
    
        copy_backup_sample($formattedParent, $backupId, $formattedSourceBackup);
    }
    

### createAuthorizedView

Creates a new AuthorizedView in a table.

The async variant is [BigtableTableAdminClient::createAuthorizedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createAuthorizedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateAuthorizedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\AuthorizedView;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateAuthorizedViewRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent  This is the name of the table the AuthorizedView belongs to.
     *                                 Values are of the form
     *                                 `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                                 {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     * @param string $authorizedViewId The id of the AuthorizedView to create. This AuthorizedView must
     *                                 not already exist. The `authorized_view_id` appended to `parent` forms the
     *                                 full AuthorizedView name of the form
     *                                 `projects/{project}/instances/{instance}/tables/{table}/authorizedView/{authorized_view}`.
     */
    function create_authorized_view_sample(string $formattedParent, string $authorizedViewId): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $authorizedView = new AuthorizedView();
        $request = (new CreateAuthorizedViewRequest())
            ->setParent($formattedParent)
            ->setAuthorizedViewId($authorizedViewId)
            ->setAuthorizedView($authorizedView);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->createAuthorizedView($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AuthorizedView $result */
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
        $formattedParent = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
        $authorizedViewId = '[AUTHORIZED_VIEW_ID]';
    
        create_authorized_view_sample($formattedParent, $authorizedViewId);
    }
    

### createBackup

Starts creating a new Cloud Bigtable Backup. The returned backup long-running operation can be used to track creation of the backup. The metadata field type is [CreateBackupMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateBackupMetadata). The response field type is [Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup), if successful. Cancelling the returned operation will stop the creation and delete the backup.

The async variant is [BigtableTableAdminClient::createBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Backup;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateBackupRequest;
    use Google\Protobuf\Timestamp;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent   This must be one of the clusters in the instance in which this
     *                                  table is located. The backup will be stored in this cluster. Values are
     *                                  of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see
     *                                  {@see BigtableTableAdminClient::clusterName()} for help formatting this field.
     * @param string $backupId          The id of the backup to be created. The `backup_id` along with
     *                                  the parent `parent` are combined as {parent}/backups/{backup_id} to create
     *                                  the full backup name, of the form:
     *                                  `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_id}`.
     *                                  This string must be between 1 and 50 characters in length and match the
     *                                  regex [_a-zA-Z0-9][-_.a-zA-Z0-9]*.
     * @param string $backupSourceTable Immutable. Name of the table from which this backup was created.
     *                                  This needs to be in the same instance as the backup. Values are of the form
     *                                  `projects/{project}/instances/{instance}/tables/{source_table}`.
     */
    function create_backup_sample(
        string $formattedParent,
        string $backupId,
        string $backupSourceTable
    ): void {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $backupExpireTime = new Timestamp();
        $backup = (new Backup())
            ->setSourceTable($backupSourceTable)
            ->setExpireTime($backupExpireTime);
        $request = (new CreateBackupRequest())
            ->setParent($formattedParent)
            ->setBackupId($backupId)
            ->setBackup($backup);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->createBackup($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Backup $result */
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
        $formattedParent = BigtableTableAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
        $backupId = '[BACKUP_ID]';
        $backupSourceTable = '[SOURCE_TABLE]';
    
        create_backup_sample($formattedParent, $backupId, $backupSourceTable);
    }
    

### createSchemaBundle

Creates a new schema bundle in the specified table.

The async variant is [BigtableTableAdminClient::createSchemaBundleAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createSchemaBundleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateSchemaBundleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\SchemaBundle](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SchemaBundle)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateSchemaBundleRequest;
    use Google\Cloud\Bigtable\Admin\V2\SchemaBundle;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent The parent resource where this schema bundle will be created.
     *                                Values are of the form
     *                                `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                                {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     * @param string $schemaBundleId  The unique ID to use for the schema bundle, which will become the
     *                                final component of the schema bundle's resource name.
     */
    function create_schema_bundle_sample(string $formattedParent, string $schemaBundleId): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $schemaBundle = new SchemaBundle();
        $request = (new CreateSchemaBundleRequest())
            ->setParent($formattedParent)
            ->setSchemaBundleId($schemaBundleId)
            ->setSchemaBundle($schemaBundle);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->createSchemaBundle($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var SchemaBundle $result */
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
        $formattedParent = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
        $schemaBundleId = '[SCHEMA_BUNDLE_ID]';
    
        create_schema_bundle_sample($formattedParent, $schemaBundleId);
    }
    

### createTable

Creates a new table in the specified instance.

The table can be created with a full set of initial column families, specified in the request.

The async variant is [BigtableTableAdminClient::createTableAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createTableAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    
    /**
     * @param string $formattedParent The unique name of the instance in which to create the table.
     *                                Values are of the form `projects/{project}/instances/{instance}`. Please see
     *                                {@see BigtableTableAdminClient::instanceName()} for help formatting this field.
     * @param string $tableId         The name by which the new table should be referred to within the
     *                                parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`.
     *                                Maximum 50 characters.
     */
    function create_table_sample(string $formattedParent, string $tableId): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $table = new Table();
        $request = (new CreateTableRequest())
            ->setParent($formattedParent)
            ->setTableId($tableId)
            ->setTable($table);
    
        // Call the API and handle any network failures.
        try {
            /** @var Table $response */
            $response = $bigtableTableAdminClient->createTable($request);
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
        $formattedParent = BigtableTableAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
        $tableId = '[TABLE_ID]';
    
        create_table_sample($formattedParent, $tableId);
    }
    

### createTableFromSnapshot

Creates a new table from the specified snapshot. The target table must not exist. The snapshot and the table must be in the same instance.

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

The async variant is [BigtableTableAdminClient::createTableFromSnapshotAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createTableFromSnapshotAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateTableFromSnapshotRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableFromSnapshotRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\CreateTableFromSnapshotRequest;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent         The unique name of the instance in which to create the table.
     *                                        Values are of the form `projects/{project}/instances/{instance}`. Please see
     *                                        {@see BigtableTableAdminClient::instanceName()} for help formatting this field.
     * @param string $tableId                 The name by which the new table should be referred to within the
     *                                        parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`.
     * @param string $formattedSourceSnapshot The unique name of the snapshot from which to restore the table.
     *                                        The snapshot and the table must be in the same instance. Values are of the
     *                                        form
     *                                        `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`. Please see
     *                                        {@see BigtableTableAdminClient::snapshotName()} for help formatting this field.
     */
    function create_table_from_snapshot_sample(
        string $formattedParent,
        string $tableId,
        string $formattedSourceSnapshot
    ): void {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new CreateTableFromSnapshotRequest())
            ->setParent($formattedParent)
            ->setTableId($tableId)
            ->setSourceSnapshot($formattedSourceSnapshot);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->createTableFromSnapshot($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Table $result */
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
        $formattedParent = BigtableTableAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
        $tableId = '[TABLE_ID]';
        $formattedSourceSnapshot = BigtableTableAdminClient::snapshotName(
            '[PROJECT]',
            '[INSTANCE]',
            '[CLUSTER]',
            '[SNAPSHOT]'
        );
    
        create_table_from_snapshot_sample($formattedParent, $tableId, $formattedSourceSnapshot);
    }
    

### deleteAuthorizedView

Permanently deletes a specified AuthorizedView.

The async variant is [BigtableTableAdminClient::deleteAuthorizedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__deleteAuthorizedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteAuthorizedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteAuthorizedViewRequest;
    
    /**
     * @param string $formattedName The unique name of the AuthorizedView to be deleted.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}`. Please see
     *                              {@see BigtableTableAdminClient::authorizedViewName()} for help formatting this field.
     */
    function delete_authorized_view_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteAuthorizedViewRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableTableAdminClient->deleteAuthorizedView($request);
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
        $formattedName = BigtableTableAdminClient::authorizedViewName(
            '[PROJECT]',
            '[INSTANCE]',
            '[TABLE]',
            '[AUTHORIZED_VIEW]'
        );
    
        delete_authorized_view_sample($formattedName);
    }
    

### deleteBackup

Deletes a pending or completed Cloud Bigtable backup.

The async variant is [BigtableTableAdminClient::deleteBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__deleteBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteBackupRequest;
    
    /**
     * @param string $formattedName Name of the backup to delete.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup}`. Please see
     *                              {@see BigtableTableAdminClient::backupName()} for help formatting this field.
     */
    function delete_backup_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableTableAdminClient->deleteBackup($request);
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
        $formattedName = BigtableTableAdminClient::backupName(
            '[PROJECT]',
            '[INSTANCE]',
            '[CLUSTER]',
            '[BACKUP]'
        );
    
        delete_backup_sample($formattedName);
    }
    

### deleteSchemaBundle

Deletes a schema bundle in the specified table.

The async variant is [BigtableTableAdminClient::deleteSchemaBundleAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__deleteSchemaBundleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteSchemaBundleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteSchemaBundleRequest;
    
    /**
     * @param string $formattedName The unique name of the schema bundle to delete.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{schema_bundle}`
     *                              Please see {@see BigtableTableAdminClient::schemaBundleName()} for help formatting this field.
     */
    function delete_schema_bundle_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteSchemaBundleRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableTableAdminClient->deleteSchemaBundle($request);
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
        $formattedName = BigtableTableAdminClient::schemaBundleName(
            '[PROJECT]',
            '[INSTANCE]',
            '[TABLE]',
            '[SCHEMA_BUNDLE]'
        );
    
        delete_schema_bundle_sample($formattedName);
    }
    

### deleteSnapshot

Permanently deletes the specified snapshot.

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

The async variant is [BigtableTableAdminClient::deleteSnapshotAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__deleteSnapshotAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteSnapshotRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteSnapshotRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteSnapshotRequest;
    
    /**
     * @param string $formattedName The unique name of the snapshot to be deleted.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`. Please see
     *                              {@see BigtableTableAdminClient::snapshotName()} for help formatting this field.
     */
    function delete_snapshot_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteSnapshotRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableTableAdminClient->deleteSnapshot($request);
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
        $formattedName = BigtableTableAdminClient::snapshotName(
            '[PROJECT]',
            '[INSTANCE]',
            '[CLUSTER]',
            '[SNAPSHOT]'
        );
    
        delete_snapshot_sample($formattedName);
    }
    

### deleteTable

Permanently deletes a specified table and all of its data.

The async variant is [BigtableTableAdminClient::deleteTableAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__deleteTableAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteTableRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DeleteTableRequest;
    
    /**
     * @param string $formattedName The unique name of the table to be deleted.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                              {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function delete_table_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new DeleteTableRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableTableAdminClient->deleteTable($request);
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        delete_table_sample($formattedName);
    }
    

### dropRowRange

Permanently drop/delete a row range from a specified table. The request can specify whether to delete all rows in a table, or only those that match a particular prefix.

The async variant is [BigtableTableAdminClient::dropRowRangeAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__dropRowRangeAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DropRowRangeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DropRowRangeRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\DropRowRangeRequest;
    
    /**
     * @param string $formattedName The unique name of the table on which to drop a range of rows.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                              {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function drop_row_range_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new DropRowRangeRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $bigtableTableAdminClient->dropRowRange($request);
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        drop_row_range_sample($formattedName);
    }
    

### generateConsistencyToken

Generates a consistency token for a Table, which can be used in CheckConsistency to check whether mutations to the table that finished before this call started have been replicated. The tokens will be available for 90 days.

The async variant is [BigtableTableAdminClient::generateConsistencyTokenAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__generateConsistencyTokenAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GenerateConsistencyTokenRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GenerateConsistencyTokenRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\GenerateConsistencyTokenResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GenerateConsistencyTokenResponse)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GenerateConsistencyTokenRequest;
    use Google\Cloud\Bigtable\Admin\V2\GenerateConsistencyTokenResponse;
    
    /**
     * @param string $formattedName The unique name of the Table for which to create a consistency
     *                              token. Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                              {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function generate_consistency_token_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new GenerateConsistencyTokenRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var GenerateConsistencyTokenResponse $response */
            $response = $bigtableTableAdminClient->generateConsistencyToken($request);
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        generate_consistency_token_sample($formattedName);
    }
    

### getAuthorizedView

Gets information from a specified AuthorizedView.

The async variant is [BigtableTableAdminClient::getAuthorizedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__getAuthorizedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetAuthorizedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\AuthorizedView;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetAuthorizedViewRequest;
    
    /**
     * @param string $formattedName The unique name of the requested AuthorizedView.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}`. Please see
     *                              {@see BigtableTableAdminClient::authorizedViewName()} for help formatting this field.
     */
    function get_authorized_view_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new GetAuthorizedViewRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var AuthorizedView $response */
            $response = $bigtableTableAdminClient->getAuthorizedView($request);
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
        $formattedName = BigtableTableAdminClient::authorizedViewName(
            '[PROJECT]',
            '[INSTANCE]',
            '[TABLE]',
            '[AUTHORIZED_VIEW]'
        );
    
        get_authorized_view_sample($formattedName);
    }
    

### getBackup

Gets metadata on a pending or completed Cloud Bigtable Backup.

The async variant is [BigtableTableAdminClient::getBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__getBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Backup;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetBackupRequest;
    
    /**
     * @param string $formattedName Name of the backup.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup}`. Please see
     *                              {@see BigtableTableAdminClient::backupName()} for help formatting this field.
     */
    function get_backup_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new GetBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Backup $response */
            $response = $bigtableTableAdminClient->getBackup($request);
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
        $formattedName = BigtableTableAdminClient::backupName(
            '[PROJECT]',
            '[INSTANCE]',
            '[CLUSTER]',
            '[BACKUP]'
        );
    
        get_backup_sample($formattedName);
    }
    

### getIamPolicy

Gets the access control policy for a Bigtable resource.

Returns an empty policy if the resource exists but does not have a policy set.

The async variant is [BigtableTableAdminClient::getIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__getIamPolicyAsync__) .

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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\Policy;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being requested.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function get_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new GetIamPolicyRequest())
            ->setResource($resource);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $bigtableTableAdminClient->getIamPolicy($request);
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
    

### getSchemaBundle

Gets metadata information about the specified schema bundle.

The async variant is [BigtableTableAdminClient::getSchemaBundleAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__getSchemaBundleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetSchemaBundleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\SchemaBundle](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SchemaBundle)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetSchemaBundleRequest;
    use Google\Cloud\Bigtable\Admin\V2\SchemaBundle;
    
    /**
     * @param string $formattedName The unique name of the schema bundle to retrieve.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{schema_bundle}`
     *                              Please see {@see BigtableTableAdminClient::schemaBundleName()} for help formatting this field.
     */
    function get_schema_bundle_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new GetSchemaBundleRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var SchemaBundle $response */
            $response = $bigtableTableAdminClient->getSchemaBundle($request);
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
        $formattedName = BigtableTableAdminClient::schemaBundleName(
            '[PROJECT]',
            '[INSTANCE]',
            '[TABLE]',
            '[SCHEMA_BUNDLE]'
        );
    
        get_schema_bundle_sample($formattedName);
    }
    

### getSnapshot

Gets metadata information about the specified snapshot.

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

The async variant is [BigtableTableAdminClient::getSnapshotAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__getSnapshotAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetSnapshotRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetSnapshotRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Snapshot](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Snapshot)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetSnapshotRequest;
    use Google\Cloud\Bigtable\Admin\V2\Snapshot;
    
    /**
     * @param string $formattedName The unique name of the requested snapshot.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`. Please see
     *                              {@see BigtableTableAdminClient::snapshotName()} for help formatting this field.
     */
    function get_snapshot_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new GetSnapshotRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Snapshot $response */
            $response = $bigtableTableAdminClient->getSnapshot($request);
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
        $formattedName = BigtableTableAdminClient::snapshotName(
            '[PROJECT]',
            '[INSTANCE]',
            '[CLUSTER]',
            '[SNAPSHOT]'
        );
    
        get_snapshot_sample($formattedName);
    }
    

### getTable

Gets metadata information about the specified table.

The async variant is [BigtableTableAdminClient::getTableAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__getTableAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetTableRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\GetTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    
    /**
     * @param string $formattedName The unique name of the requested table.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                              {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function get_table_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new GetTableRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Table $response */
            $response = $bigtableTableAdminClient->getTable($request);
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        get_table_sample($formattedName);
    }
    

### listAuthorizedViews

Lists all AuthorizedViews from a specific table.

The async variant is [BigtableTableAdminClient::listAuthorizedViewsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__listAuthorizedViewsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListAuthorizedViewsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListAuthorizedViewsRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\AuthorizedView;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListAuthorizedViewsRequest;
    
    /**
     * @param string $formattedParent The unique name of the table for which AuthorizedViews should be
     *                                listed. Values are of the form
     *                                `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                                {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function list_authorized_views_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new ListAuthorizedViewsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableTableAdminClient->listAuthorizedViews($request);
    
            /** @var AuthorizedView $element */
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
        $formattedParent = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        list_authorized_views_sample($formattedParent);
    }
    

### listBackups

Lists Cloud Bigtable backups. Returns both completed and pending backups.

The async variant is [BigtableTableAdminClient::listBackupsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__listBackupsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListBackupsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Backup;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListBackupsRequest;
    
    /**
     * @param string $formattedParent The cluster to list backups from.  Values are of the
     *                                form `projects/{project}/instances/{instance}/clusters/{cluster}`.
     *                                Use `{cluster} = '-'` to list backups for all clusters in an instance,
     *                                e.g., `projects/{project}/instances/{instance}/clusters/-`. Please see
     *                                {@see BigtableTableAdminClient::clusterName()} for help formatting this field.
     */
    function list_backups_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new ListBackupsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableTableAdminClient->listBackups($request);
    
            /** @var Backup $element */
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
        $formattedParent = BigtableTableAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
    
        list_backups_sample($formattedParent);
    }
    

### listSchemaBundles

Lists all schema bundles associated with the specified table.

The async variant is [BigtableTableAdminClient::listSchemaBundlesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__listSchemaBundlesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListSchemaBundlesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListSchemaBundlesRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListSchemaBundlesRequest;
    use Google\Cloud\Bigtable\Admin\V2\SchemaBundle;
    
    /**
     * @param string $formattedParent The parent, which owns this collection of schema bundles.
     *                                Values are of the form
     *                                `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                                {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function list_schema_bundles_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new ListSchemaBundlesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableTableAdminClient->listSchemaBundles($request);
    
            /** @var SchemaBundle $element */
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
        $formattedParent = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        list_schema_bundles_sample($formattedParent);
    }
    

### listSnapshots

Lists all snapshots associated with the specified cluster.

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

The async variant is [BigtableTableAdminClient::listSnapshotsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__listSnapshotsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListSnapshotsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListSnapshotsRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListSnapshotsRequest;
    use Google\Cloud\Bigtable\Admin\V2\Snapshot;
    
    /**
     * @param string $formattedParent The unique name of the cluster for which snapshots should be
     *                                listed. Values are of the form
     *                                `projects/{project}/instances/{instance}/clusters/{cluster}`.
     *                                Use `{cluster} = '-'` to list snapshots for all clusters in an instance,
     *                                e.g., `projects/{project}/instances/{instance}/clusters/-`. Please see
     *                                {@see BigtableTableAdminClient::clusterName()} for help formatting this field.
     */
    function list_snapshots_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new ListSnapshotsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableTableAdminClient->listSnapshots($request);
    
            /** @var Snapshot $element */
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
        $formattedParent = BigtableTableAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
    
        list_snapshots_sample($formattedParent);
    }
    

### listTables

Lists all tables served from a specified instance.

The async variant is [BigtableTableAdminClient::listTablesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__listTablesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListTablesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListTablesRequest)`   
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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ListTablesRequest;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    
    /**
     * @param string $formattedParent The unique name of the instance for which tables should be
     *                                listed. Values are of the form `projects/{project}/instances/{instance}`. Please see
     *                                {@see BigtableTableAdminClient::instanceName()} for help formatting this field.
     */
    function list_tables_sample(string $formattedParent): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new ListTablesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $bigtableTableAdminClient->listTables($request);
    
            /** @var Table $element */
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
        $formattedParent = BigtableTableAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
    
        list_tables_sample($formattedParent);
    }
    

### modifyColumnFamilies

Performs a series of column family modifications on the specified table.

Either all or none of the modifications will occur before this method returns, but data requests received prior to that point may see a table where only some modifications have taken effect.

The async variant is [BigtableTableAdminClient::modifyColumnFamiliesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__modifyColumnFamiliesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ModifyColumnFamiliesRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest;
    use Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest\Modification;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    
    /**
     * @param string $formattedName The unique name of the table whose families should be modified.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                              {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function modify_column_families_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $modifications = [new Modification()];
        $request = (new ModifyColumnFamiliesRequest())
            ->setName($formattedName)
            ->setModifications($modifications);
    
        // Call the API and handle any network failures.
        try {
            /** @var Table $response */
            $response = $bigtableTableAdminClient->modifyColumnFamilies($request);
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        modify_column_families_sample($formattedName);
    }
    

### restoreTable

Create a new table by restoring from a completed backup. The returned table long-running operation can be used to track the progress of the operation, and to cancel it. The metadata field type is [RestoreTableMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreTableMetadata). The response type is [Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table), if successful.

The async variant is [BigtableTableAdminClient::restoreTableAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__restoreTableAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\RestoreTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreTableRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\RestoreTableRequest;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent The name of the instance in which to create the restored
     *                                table. Values are of the form `projects/<project>/instances/<instance>`. Please see
     *                                {@see BigtableTableAdminClient::instanceName()} for help formatting this field.
     * @param string $tableId         The id of the table to create and restore to. This
     *                                table must not already exist. The `table_id` appended to
     *                                `parent` forms the full table name of the form
     *                                `projects/<project>/instances/<instance>/tables/<table_id>`.
     */
    function restore_table_sample(string $formattedParent, string $tableId): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new RestoreTableRequest())
            ->setParent($formattedParent)
            ->setTableId($tableId);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->restoreTable($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Table $result */
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
        $formattedParent = BigtableTableAdminClient::instanceName('[PROJECT]', '[INSTANCE]');
        $tableId = '[TABLE_ID]';
    
        restore_table_sample($formattedParent, $tableId);
    }
    

### setIamPolicy

Sets the access control policy on a Bigtable resource.

Replaces any existing policy.

The async variant is [BigtableTableAdminClient::setIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__setIamPolicyAsync__) .

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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Iam\V1\Policy;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being specified.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function set_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $policy = new Policy();
        $request = (new SetIamPolicyRequest())
            ->setResource($resource)
            ->setPolicy($policy);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $bigtableTableAdminClient->setIamPolicy($request);
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
    

### snapshotTable

Creates a new snapshot in the specified cluster from the specified source table. The cluster and the table must be in the same instance.

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

The async variant is [BigtableTableAdminClient::snapshotTableAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__snapshotTableAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\SnapshotTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SnapshotTableRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Snapshot](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Snapshot)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Snapshot;
    use Google\Cloud\Bigtable\Admin\V2\SnapshotTableRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName    The unique name of the table to have the snapshot taken.
     *                                 Values are of the form
     *                                 `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                                 {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     * @param string $formattedCluster The name of the cluster where the snapshot will be created in.
     *                                 Values are of the form
     *                                 `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see
     *                                 {@see BigtableTableAdminClient::clusterName()} for help formatting this field.
     * @param string $snapshotId       The ID by which the new snapshot should be referred to within the
     *                                 parent cluster, e.g., `mysnapshot` of the form:
     *                                 `[_a-zA-Z0-9][-_.a-zA-Z0-9]*` rather than
     *                                 `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/mysnapshot`.
     */
    function snapshot_table_sample(
        string $formattedName,
        string $formattedCluster,
        string $snapshotId
    ): void {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new SnapshotTableRequest())
            ->setName($formattedName)
            ->setCluster($formattedCluster)
            ->setSnapshotId($snapshotId);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->snapshotTable($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Snapshot $result */
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
        $formattedCluster = BigtableTableAdminClient::clusterName('[PROJECT]', '[INSTANCE]', '[CLUSTER]');
        $snapshotId = '[SNAPSHOT_ID]';
    
        snapshot_table_sample($formattedName, $formattedCluster, $snapshotId);
    }
    

### testIamPermissions

Returns permissions that the caller has on the specified Bigtable resource.

The async variant is [BigtableTableAdminClient::testIamPermissionsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__testIamPermissionsAsync__) .

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
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
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
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $permissions = [$permissionsElement,];
        $request = (new TestIamPermissionsRequest())
            ->setResource($resource)
            ->setPermissions($permissions);
    
        // Call the API and handle any network failures.
        try {
            /** @var TestIamPermissionsResponse $response */
            $response = $bigtableTableAdminClient->testIamPermissions($request);
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
    

### undeleteTable

Restores a specified table which was accidentally deleted.

The async variant is [BigtableTableAdminClient::undeleteTableAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__undeleteTableAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UndeleteTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UndeleteTableRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    use Google\Cloud\Bigtable\Admin\V2\UndeleteTableRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName The unique name of the table to be restored.
     *                              Values are of the form
     *                              `projects/{project}/instances/{instance}/tables/{table}`. Please see
     *                              {@see BigtableTableAdminClient::tableName()} for help formatting this field.
     */
    function undelete_table_sample(string $formattedName): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $request = (new UndeleteTableRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->undeleteTable($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Table $result */
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
        $formattedName = BigtableTableAdminClient::tableName('[PROJECT]', '[INSTANCE]', '[TABLE]');
    
        undelete_table_sample($formattedName);
    }
    

### updateAuthorizedView

Updates an AuthorizedView in a table.

The async variant is [BigtableTableAdminClient::updateAuthorizedViewAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__updateAuthorizedViewAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateAuthorizedViewRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\AuthorizedView;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\UpdateAuthorizedViewRequest;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_authorized_view_sample(): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $authorizedView = new AuthorizedView();
        $request = (new UpdateAuthorizedViewRequest())
            ->setAuthorizedView($authorizedView);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->updateAuthorizedView($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AuthorizedView $result */
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
    

### updateBackup

Updates a pending or completed Cloud Bigtable Backup.

The async variant is [BigtableTableAdminClient::updateBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__updateBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Bigtable\Admin\V2\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Backup;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\UpdateBackupRequest;
    use Google\Protobuf\FieldMask;
    use Google\Protobuf\Timestamp;
    
    /**
     * @param string $backupSourceTable Immutable. Name of the table from which this backup was created.
     *                                  This needs to be in the same instance as the backup. Values are of the form
     *                                  `projects/{project}/instances/{instance}/tables/{source_table}`.
     */
    function update_backup_sample(string $backupSourceTable): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $backupExpireTime = new Timestamp();
        $backup = (new Backup())
            ->setSourceTable($backupSourceTable)
            ->setExpireTime($backupExpireTime);
        $updateMask = new FieldMask();
        $request = (new UpdateBackupRequest())
            ->setBackup($backup)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var Backup $response */
            $response = $bigtableTableAdminClient->updateBackup($request);
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
        $backupSourceTable = '[SOURCE_TABLE]';
    
        update_backup_sample($backupSourceTable);
    }
    

### updateSchemaBundle

Updates a schema bundle in the specified table.

The async variant is [BigtableTableAdminClient::updateSchemaBundleAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__updateSchemaBundleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateSchemaBundleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\SchemaBundle](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SchemaBundle)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\SchemaBundle;
    use Google\Cloud\Bigtable\Admin\V2\UpdateSchemaBundleRequest;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_schema_bundle_sample(): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $schemaBundle = new SchemaBundle();
        $request = (new UpdateSchemaBundleRequest())
            ->setSchemaBundle($schemaBundle);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->updateSchemaBundle($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var SchemaBundle $result */
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
    

### updateTable

Updates a specified table.

The async variant is [BigtableTableAdminClient::updateTableAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__updateTableAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateTableRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableTableAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Table;
    use Google\Cloud\Bigtable\Admin\V2\UpdateTableRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_table_sample(): void
    {
        // Create a client.
        $bigtableTableAdminClient = new BigtableTableAdminClient();
    
        // Prepare the request message.
        $table = new Table();
        $updateMask = new FieldMask();
        $request = (new UpdateTableRequest())
            ->setTable($table)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $bigtableTableAdminClient->updateTable($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Table $result */
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
    

### checkConsistencyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CheckConsistencyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CheckConsistencyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\CheckConsistencyResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CheckConsistencyResponse)>` |   
  
### copyBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CopyBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CopyBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createAuthorizedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateAuthorizedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createSchemaBundleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateSchemaBundleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createTableAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)>` |   
  
### createTableFromSnapshotAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\CreateTableFromSnapshotRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableFromSnapshotRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteAuthorizedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteAuthorizedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteSchemaBundleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteSchemaBundleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteSnapshotAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteSnapshotRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteSnapshotRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### deleteTableAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DeleteTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DeleteTableRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### dropRowRangeAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\DropRowRangeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.DropRowRangeRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### generateConsistencyTokenAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GenerateConsistencyTokenRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GenerateConsistencyTokenRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\GenerateConsistencyTokenResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GenerateConsistencyTokenResponse)>` |   
  
### getAuthorizedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetAuthorizedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)>` |   
  
### getBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)>` |   
  
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
  
### getSchemaBundleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetSchemaBundleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\SchemaBundle](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SchemaBundle)>` |   
  
### getSnapshotAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetSnapshotRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetSnapshotRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Snapshot](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Snapshot)>` |   
  
### getTableAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\GetTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.GetTableRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)>` |   
  
### listAuthorizedViewsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListAuthorizedViewsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListAuthorizedViewsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBackupsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListBackupsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listSchemaBundlesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListSchemaBundlesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListSchemaBundlesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listSnapshotsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListSnapshotsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListSnapshotsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listTablesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ListTablesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListTablesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### modifyColumnFamiliesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\ModifyColumnFamiliesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ModifyColumnFamiliesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)>` |   
  
### restoreTableAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\RestoreTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.RestoreTableRequest)`   
  
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
  
### snapshotTableAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\SnapshotTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.SnapshotTableRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
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
  
### undeleteTableAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UndeleteTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UndeleteTableRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateAuthorizedViewAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateAuthorizedViewRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Bigtable\Admin\V2\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup)>` |   
  
### updateSchemaBundleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateSchemaBundleRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateSchemaBundleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateTableAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Bigtable\Admin\V2\UpdateTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateTableRequest)`   
  
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
  
### static::authorizedViewName

Formats a string containing the fully-qualified path to represent a authorized_view resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`table` |  `string`   
  
`authorizedView` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted authorized_view resource.  
  
### static::backupName

Formats a string containing the fully-qualified path to represent a backup resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`cluster` |  `string`   
  
`backup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted backup resource.  
  
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
  
### static::cryptoKeyVersionName

Formats a string containing the fully-qualified path to represent a crypto_key_version resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`keyRing` |  `string`   
  
`cryptoKey` |  `string`   
  
`cryptoKeyVersion` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted crypto_key_version resource.  
  
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
  
### static::schemaBundleName

Formats a string containing the fully-qualified path to represent a schema_bundle resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`table` |  `string`   
  
`schemaBundle` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted schema_bundle resource.  
  
### static::snapshotName

Formats a string containing the fully-qualified path to represent a snapshot resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`cluster` |  `string`   
  
`snapshot` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted snapshot resource.  
  
### static::tableName

Formats a string containing the fully-qualified path to represent a table resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
`table` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted table resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * authorizedView: projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}
  * backup: projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup}
  * cluster: projects/{project}/instances/{instance}/clusters/{cluster}
  * cryptoKeyVersion: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}
  * instance: projects/{project}/instances/{instance}
  * location: projects/{project}/locations/{location}
  * schemaBundle: projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{schema_bundle}
  * snapshot: projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}
  * table: projects/{project}/instances/{instance}/tables/{table}



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
