---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient
title: Google Cloud Dataproc Metastore V1beta Client - Class DataprocMetastoreClient (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:50.890865+00:00
---

# Google Cloud Dataproc Metastore V1beta Client - Class DataprocMetastoreClient (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1beta Client - Class DataprocMetastoreClient (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1beta Client class DataprocMetastoreClient.

Service Description: Configures and manages metastore services.

Metastore services are fully managed, highly available, autoscaled, autohealing, OSS-native deployments of technical metadata management software. Each metastore service exposes a network endpoint through which metadata queries are served. Metadata queries can originate from a variety of sources, including Apache Hive, Apache Presto, and Apache Spark.

The Dataproc Metastore API defines the following resource model:

  * The service works with a collection of Google Cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*` (a location must refer to a Google Cloud `region`)
  * Each location has a collection of services, named: `/services/*`
  * Dataproc Metastore services are resources with names of the form:



`/projects/{project_number}/locations/{location_id}/services/{service_id}`.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Cloud \ Metastore \ V1beta \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\Metastore\V1beta\DataprocMetastoreClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new DataprocMetastoreClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### alterMetadataResourceLocation

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

The async variant is [DataprocMetastoreClient::alterMetadataResourceLocationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__alterMetadataResourceLocationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.AlterMetadataResourceLocationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.AlterMetadataResourceLocationResponse)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\AlterMetadataResourceLocationRequest;
    use Google\Cloud\Metastore\V1beta\AlterMetadataResourceLocationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedService The relative resource name of the metastore service to mutate
     *                                 metadata, in the following format:
     *
     *                                 `projects/{project_id}/locations/{location_id}/services/{service_id}`. Please see
     *                                 {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     * @param string $resourceName     The relative metadata resource name in the following format.
     *
     *                                 `databases/{database_id}`
     *                                 or
     *                                 `databases/{database_id}/tables/{table_id}`
     *                                 or
     *                                 `databases/{database_id}/tables/{table_id}/partitions/{partition_id}`
     * @param string $locationUri      The new location URI for the metadata resource.
     */
    function alter_metadata_resource_location_sample(
        string $formattedService,
        string $resourceName,
        string $locationUri
    ): void {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new AlterMetadataResourceLocationRequest())
            ->setService($formattedService)
            ->setResourceName($resourceName)
            ->setLocationUri($locationUri);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->alterMetadataResourceLocation($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AlterMetadataResourceLocationResponse $result */
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
        $formattedService = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
        $resourceName = '[RESOURCE_NAME]';
        $locationUri = '[LOCATION_URI]';
    
        alter_metadata_resource_location_sample($formattedService, $resourceName, $locationUri);
    }
    

### createBackup

Creates a new backup in a given project and location.

The async variant is [DataprocMetastoreClient::createBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__createBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\CreateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.CreateBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Backup)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Backup;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\CreateBackupRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent The relative resource name of the service in which to create a
     *                                backup of the following form:
     *
     *                                `projects/{project_number}/locations/{location_id}/services/{service_id}`. Please see
     *                                {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     * @param string $backupId        The ID of the backup, which is used as the final component of the
     *                                backup's name.
     *
     *                                This value must be between 1 and 64 characters long, begin with a letter,
     *                                end with a letter or number, and consist of alpha-numeric ASCII characters
     *                                or hyphens.
     */
    function create_backup_sample(string $formattedParent, string $backupId): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $backup = new Backup();
        $request = (new CreateBackupRequest())
            ->setParent($formattedParent)
            ->setBackupId($backupId)
            ->setBackup($backup);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->createBackup($request);
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
        $formattedParent = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
        $backupId = '[BACKUP_ID]';
    
        create_backup_sample($formattedParent, $backupId);
    }
    

### createMetadataImport

Creates a new MetadataImport in a given project and location.

The async variant is [DataprocMetastoreClient::createMetadataImportAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__createMetadataImportAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\CreateMetadataImportRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.CreateMetadataImportRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataImport)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\CreateMetadataImportRequest;
    use Google\Cloud\Metastore\V1beta\MetadataImport;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent  The relative resource name of the service in which to create a
     *                                 metastore import, in the following form:
     *
     *                                 `projects/{project_number}/locations/{location_id}/services/{service_id}`. Please see
     *                                 {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     * @param string $metadataImportId The ID of the metadata import, which is used as the final
     *                                 component of the metadata import's name.
     *
     *                                 This value must be between 1 and 64 characters long, begin with a letter,
     *                                 end with a letter or number, and consist of alpha-numeric ASCII characters
     *                                 or hyphens.
     */
    function create_metadata_import_sample(string $formattedParent, string $metadataImportId): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $metadataImport = new MetadataImport();
        $request = (new CreateMetadataImportRequest())
            ->setParent($formattedParent)
            ->setMetadataImportId($metadataImportId)
            ->setMetadataImport($metadataImport);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->createMetadataImport($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var MetadataImport $result */
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
        $formattedParent = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
        $metadataImportId = '[METADATA_IMPORT_ID]';
    
        create_metadata_import_sample($formattedParent, $metadataImportId);
    }
    

### createService

Creates a metastore service in a project and location.

The async variant is [DataprocMetastoreClient::createServiceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__createServiceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\CreateServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.CreateServiceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\Service](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\CreateServiceRequest;
    use Google\Cloud\Metastore\V1beta\Service;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent The relative resource name of the location in which to create a
     *                                metastore service, in the following form:
     *
     *                                `projects/{project_number}/locations/{location_id}`. Please see
     *                                {@see DataprocMetastoreClient::locationName()} for help formatting this field.
     * @param string $serviceId       The ID of the metastore service, which is used as the final
     *                                component of the metastore service's name.
     *
     *                                This value must be between 2 and 63 characters long inclusive, begin with a
     *                                letter, end with a letter or number, and consist of alpha-numeric
     *                                ASCII characters or hyphens.
     */
    function create_service_sample(string $formattedParent, string $serviceId): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $service = new Service();
        $request = (new CreateServiceRequest())
            ->setParent($formattedParent)
            ->setServiceId($serviceId)
            ->setService($service);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->createService($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Service $result */
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
        $formattedParent = DataprocMetastoreClient::locationName('[PROJECT]', '[LOCATION]');
        $serviceId = '[SERVICE_ID]';
    
        create_service_sample($formattedParent, $serviceId);
    }
    

### deleteBackup

Deletes a single backup.

The async variant is [DataprocMetastoreClient::deleteBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__deleteBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\DeleteBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.DeleteBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<null>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\DeleteBackupRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName The relative resource name of the backup to delete, in the
     *                              following form:
     *
     *                              `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`. Please see
     *                              {@see DataprocMetastoreClient::backupName()} for help formatting this field.
     */
    function delete_backup_sample(string $formattedName): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new DeleteBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->deleteBackup($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                printf('Operation completed successfully.' . PHP_EOL);
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
        $formattedName = DataprocMetastoreClient::backupName(
            '[PROJECT]',
            '[LOCATION]',
            '[SERVICE]',
            '[BACKUP]'
        );
    
        delete_backup_sample($formattedName);
    }
    

### deleteService

Deletes a single service.

The async variant is [DataprocMetastoreClient::deleteServiceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__deleteServiceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\DeleteServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.DeleteServiceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<null>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\DeleteServiceRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName The relative resource name of the metastore service to delete, in
     *                              the following form:
     *
     *                              `projects/{project_number}/locations/{location_id}/services/{service_id}`. Please see
     *                              {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     */
    function delete_service_sample(string $formattedName): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new DeleteServiceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->deleteService($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                printf('Operation completed successfully.' . PHP_EOL);
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
        $formattedName = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
    
        delete_service_sample($formattedName);
    }
    

### exportMetadata

Exports metadata from a service.

The async variant is [DataprocMetastoreClient::exportMetadataAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__exportMetadataAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ExportMetadataRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ExportMetadataRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\MetadataExport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataExport)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\ExportMetadataRequest;
    use Google\Cloud\Metastore\V1beta\MetadataExport;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedService The relative resource name of the metastore service to run
     *                                 export, in the following form:
     *
     *                                 `projects/{project_id}/locations/{location_id}/services/{service_id}`. Please see
     *                                 {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     */
    function export_metadata_sample(string $formattedService): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new ExportMetadataRequest())
            ->setService($formattedService);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->exportMetadata($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var MetadataExport $result */
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
        $formattedService = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
    
        export_metadata_sample($formattedService);
    }
    

### getBackup

Gets details of a single backup.

The async variant is [DataprocMetastoreClient::getBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__getBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\GetBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.GetBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Metastore\V1beta\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Backup)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Metastore\V1beta\Backup;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\GetBackupRequest;
    
    /**
     * @param string $formattedName The relative resource name of the backup to retrieve, in the
     *                              following form:
     *
     *                              `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`. Please see
     *                              {@see DataprocMetastoreClient::backupName()} for help formatting this field.
     */
    function get_backup_sample(string $formattedName): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new GetBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Backup $response */
            $response = $dataprocMetastoreClient->getBackup($request);
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
        $formattedName = DataprocMetastoreClient::backupName(
            '[PROJECT]',
            '[LOCATION]',
            '[SERVICE]',
            '[BACKUP]'
        );
    
        get_backup_sample($formattedName);
    }
    

### getMetadataImport

Gets details of a single import.

The async variant is [DataprocMetastoreClient::getMetadataImportAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__getMetadataImportAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\GetMetadataImportRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.GetMetadataImportRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Metastore\V1beta\MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataImport)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\GetMetadataImportRequest;
    use Google\Cloud\Metastore\V1beta\MetadataImport;
    
    /**
     * @param string $formattedName The relative resource name of the metadata import to retrieve, in
     *                              the following form:
     *
     *                              `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`. Please see
     *                              {@see DataprocMetastoreClient::metadataImportName()} for help formatting this field.
     */
    function get_metadata_import_sample(string $formattedName): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new GetMetadataImportRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var MetadataImport $response */
            $response = $dataprocMetastoreClient->getMetadataImport($request);
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
        $formattedName = DataprocMetastoreClient::metadataImportName(
            '[PROJECT]',
            '[LOCATION]',
            '[SERVICE]',
            '[METADATA_IMPORT]'
        );
    
        get_metadata_import_sample($formattedName);
    }
    

### getService

Gets the details of a single service.

The async variant is [DataprocMetastoreClient::getServiceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__getServiceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\GetServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.GetServiceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Metastore\V1beta\Service](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\GetServiceRequest;
    use Google\Cloud\Metastore\V1beta\Service;
    
    /**
     * @param string $formattedName The relative resource name of the metastore service to retrieve,
     *                              in the following form:
     *
     *                              `projects/{project_number}/locations/{location_id}/services/{service_id}`. Please see
     *                              {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     */
    function get_service_sample(string $formattedName): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new GetServiceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Service $response */
            $response = $dataprocMetastoreClient->getService($request);
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
        $formattedName = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
    
        get_service_sample($formattedName);
    }
    

### listBackups

Lists backups in a service.

The async variant is [DataprocMetastoreClient::listBackupsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__listBackupsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ListBackupsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ListBackupsRequest)`   
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
    use Google\Cloud\Metastore\V1beta\Backup;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\ListBackupsRequest;
    
    /**
     * @param string $formattedParent The relative resource name of the service whose backups to
     *                                list, in the following form:
     *
     *                                `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`. Please see
     *                                {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     */
    function list_backups_sample(string $formattedParent): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new ListBackupsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $dataprocMetastoreClient->listBackups($request);
    
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
        $formattedParent = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
    
        list_backups_sample($formattedParent);
    }
    

### listMetadataImports

Lists imports in a service.

The async variant is [DataprocMetastoreClient::listMetadataImportsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__listMetadataImportsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ListMetadataImportsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ListMetadataImportsRequest)`   
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
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\ListMetadataImportsRequest;
    use Google\Cloud\Metastore\V1beta\MetadataImport;
    
    /**
     * @param string $formattedParent The relative resource name of the service whose metadata imports
     *                                to list, in the following form:
     *
     *                                `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`. Please see
     *                                {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     */
    function list_metadata_imports_sample(string $formattedParent): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new ListMetadataImportsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $dataprocMetastoreClient->listMetadataImports($request);
    
            /** @var MetadataImport $element */
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
        $formattedParent = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
    
        list_metadata_imports_sample($formattedParent);
    }
    

### listServices

Lists services in a project and location.

The async variant is [DataprocMetastoreClient::listServicesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__listServicesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ListServicesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ListServicesRequest)`   
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
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\ListServicesRequest;
    use Google\Cloud\Metastore\V1beta\Service;
    
    /**
     * @param string $formattedParent The relative resource name of the location of metastore services
     *                                to list, in the following form:
     *
     *                                `projects/{project_number}/locations/{location_id}`. Please see
     *                                {@see DataprocMetastoreClient::locationName()} for help formatting this field.
     */
    function list_services_sample(string $formattedParent): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new ListServicesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $dataprocMetastoreClient->listServices($request);
    
            /** @var Service $element */
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
        $formattedParent = DataprocMetastoreClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_services_sample($formattedParent);
    }
    

### moveTableToDatabase

Move a table to another database.

The async variant is [DataprocMetastoreClient::moveTableToDatabaseAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__moveTableToDatabaseAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\MoveTableToDatabaseRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MoveTableToDatabaseRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\MoveTableToDatabaseResponse](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MoveTableToDatabaseResponse)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\MoveTableToDatabaseRequest;
    use Google\Cloud\Metastore\V1beta\MoveTableToDatabaseResponse;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedService  The relative resource name of the metastore service to mutate
     *                                  metadata, in the following format:
     *
     *                                  `projects/{project_id}/locations/{location_id}/services/{service_id}`. Please see
     *                                  {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     * @param string $tableName         The name of the table to be moved.
     * @param string $dbName            The name of the database where the table resides.
     * @param string $destinationDbName The name of the database where the table should be moved.
     */
    function move_table_to_database_sample(
        string $formattedService,
        string $tableName,
        string $dbName,
        string $destinationDbName
    ): void {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new MoveTableToDatabaseRequest())
            ->setService($formattedService)
            ->setTableName($tableName)
            ->setDbName($dbName)
            ->setDestinationDbName($destinationDbName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->moveTableToDatabase($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var MoveTableToDatabaseResponse $result */
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
        $formattedService = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
        $tableName = '[TABLE_NAME]';
        $dbName = '[DB_NAME]';
        $destinationDbName = '[DESTINATION_DB_NAME]';
    
        move_table_to_database_sample($formattedService, $tableName, $dbName, $destinationDbName);
    }
    

### queryMetadata

Query DPMS metadata.

The async variant is [DataprocMetastoreClient::queryMetadataAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__queryMetadataAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\QueryMetadataRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.QueryMetadataRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\QueryMetadataResponse](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.QueryMetadataResponse)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\QueryMetadataRequest;
    use Google\Cloud\Metastore\V1beta\QueryMetadataResponse;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedService The relative resource name of the metastore service to query
     *                                 metadata, in the following format:
     *
     *                                 `projects/{project_id}/locations/{location_id}/services/{service_id}`. Please see
     *                                 {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     * @param string $query            A read-only SQL query to execute against the metadata database.
     *                                 The query cannot change or mutate the data.
     */
    function query_metadata_sample(string $formattedService, string $query): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new QueryMetadataRequest())
            ->setService($formattedService)
            ->setQuery($query);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->queryMetadata($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var QueryMetadataResponse $result */
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
        $formattedService = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
        $query = '[QUERY]';
    
        query_metadata_sample($formattedService, $query);
    }
    

### removeIamPolicy

Removes the attached IAM policies for a resource

The async variant is [DataprocMetastoreClient::removeIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__removeIamPolicyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\RemoveIamPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.RemoveIamPolicyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Metastore\V1beta\RemoveIamPolicyResponse](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.RemoveIamPolicyResponse)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\RemoveIamPolicyRequest;
    use Google\Cloud\Metastore\V1beta\RemoveIamPolicyResponse;
    
    /**
     * @param string $resource The relative resource name of the dataplane resource to remove
     *                         IAM policy, in the following form:
     *
     *                         `projects/{project_id}/locations/{location_id}/services/{service_id}/databases/{database_id}`
     *                         or
     *                         `projects/{project_id}/locations/{location_id}/services/{service_id}/databases/{database_id}/tables/{table_id}`.
     */
    function remove_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new RemoveIamPolicyRequest())
            ->setResource($resource);
    
        // Call the API and handle any network failures.
        try {
            /** @var RemoveIamPolicyResponse $response */
            $response = $dataprocMetastoreClient->removeIamPolicy($request);
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
    
        remove_iam_policy_sample($resource);
    }
    

### restoreService

Restores a service from a backup.

The async variant is [DataprocMetastoreClient::restoreServiceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__restoreServiceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\RestoreServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.RestoreServiceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\Restore](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Restore)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\Restore;
    use Google\Cloud\Metastore\V1beta\RestoreServiceRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedService The relative resource name of the metastore service to run
     *                                 restore, in the following form:
     *
     *                                 `projects/{project_id}/locations/{location_id}/services/{service_id}`. Please see
     *                                 {@see DataprocMetastoreClient::serviceName()} for help formatting this field.
     * @param string $formattedBackup  The relative resource name of the metastore service backup to
     *                                 restore from, in the following form:
     *
     *                                 `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`. Please see
     *                                 {@see DataprocMetastoreClient::backupName()} for help formatting this field.
     */
    function restore_service_sample(string $formattedService, string $formattedBackup): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new RestoreServiceRequest())
            ->setService($formattedService)
            ->setBackup($formattedBackup);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->restoreService($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Restore $result */
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
        $formattedService = DataprocMetastoreClient::serviceName('[PROJECT]', '[LOCATION]', '[SERVICE]');
        $formattedBackup = DataprocMetastoreClient::backupName(
            '[PROJECT]',
            '[LOCATION]',
            '[SERVICE]',
            '[BACKUP]'
        );
    
        restore_service_sample($formattedService, $formattedBackup);
    }
    

### updateMetadataImport

Updates a single import.

Only the description field of MetadataImport is supported to be updated.

The async variant is [DataprocMetastoreClient::updateMetadataImportAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__updateMetadataImportAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\UpdateMetadataImportRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.UpdateMetadataImportRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataImport)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\MetadataImport;
    use Google\Cloud\Metastore\V1beta\UpdateMetadataImportRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_metadata_import_sample(): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $metadataImport = new MetadataImport();
        $request = (new UpdateMetadataImportRequest())
            ->setUpdateMask($updateMask)
            ->setMetadataImport($metadataImport);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->updateMetadataImport($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var MetadataImport $result */
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
    

### updateService

Updates the parameters of a single service.

The async variant is [DataprocMetastoreClient::updateServiceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__updateServiceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\UpdateServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.UpdateServiceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\Metastore\V1beta\Service](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    use Google\Cloud\Metastore\V1beta\Service;
    use Google\Cloud\Metastore\V1beta\UpdateServiceRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_service_sample(): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $service = new Service();
        $request = (new UpdateServiceRequest())
            ->setUpdateMask($updateMask)
            ->setService($service);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $dataprocMetastoreClient->updateService($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var Service $result */
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
    

### getLocation

Gets information about a location.

The async variant is [DataprocMetastoreClient::getLocationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__getLocationAsync__) .

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
    use Google\Cloud\Location\GetLocationRequest;
    use Google\Cloud\Location\Location;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    
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
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = new GetLocationRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var Location $response */
            $response = $dataprocMetastoreClient->getLocation($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### listLocations

Lists information about the supported locations for this service.

The async variant is [DataprocMetastoreClient::listLocationsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__listLocationsAsync__) .

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
    use Google\Cloud\Location\ListLocationsRequest;
    use Google\Cloud\Location\Location;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    
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
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = new ListLocationsRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $dataprocMetastoreClient->listLocations($request);
    
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

The async variant is [DataprocMetastoreClient::getIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__getIamPolicyAsync__) .

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
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\Policy;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being requested.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function get_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $request = (new GetIamPolicyRequest())
            ->setResource($resource);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $dataprocMetastoreClient->getIamPolicy($request);
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

The async variant is [DataprocMetastoreClient::setIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__setIamPolicyAsync__) .

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
    use Google\Cloud\Iam\V1\Policy;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being specified.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function set_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $policy = new Policy();
        $request = (new SetIamPolicyRequest())
            ->setResource($resource)
            ->setPolicy($policy);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $dataprocMetastoreClient->setIamPolicy($request);
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

The async variant is [DataprocMetastoreClient::testIamPermissionsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__testIamPermissionsAsync__) .

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
    use Google\Cloud\Iam\V1\TestIamPermissionsRequest;
    use Google\Cloud\Iam\V1\TestIamPermissionsResponse;
    use Google\Cloud\Metastore\V1beta\Client\DataprocMetastoreClient;
    
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
        $dataprocMetastoreClient = new DataprocMetastoreClient();
    
        // Prepare the request message.
        $permissions = [$permissionsElement,];
        $request = (new TestIamPermissionsRequest())
            ->setResource($resource)
            ->setPermissions($permissions);
    
        // Call the API and handle any network failures.
        try {
            /** @var TestIamPermissionsResponse $response */
            $response = $dataprocMetastoreClient->testIamPermissions($request);
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
    

### alterMetadataResourceLocationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.AlterMetadataResourceLocationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\CreateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.CreateBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createMetadataImportAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\CreateMetadataImportRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.CreateMetadataImportRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createServiceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\CreateServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.CreateServiceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\DeleteBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.DeleteBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteServiceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\DeleteServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.DeleteServiceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### exportMetadataAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ExportMetadataRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ExportMetadataRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### getBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\GetBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.GetBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Metastore\V1beta\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Backup)>` |   
  
### getMetadataImportAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\GetMetadataImportRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.GetMetadataImportRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Metastore\V1beta\MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataImport)>` |   
  
### getServiceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\GetServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.GetServiceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Metastore\V1beta\Service](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service)>` |   
  
### listBackupsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ListBackupsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ListBackupsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listMetadataImportsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ListMetadataImportsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ListMetadataImportsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listServicesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\ListServicesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ListServicesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### moveTableToDatabaseAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\MoveTableToDatabaseRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MoveTableToDatabaseRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### queryMetadataAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\QueryMetadataRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.QueryMetadataRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### removeIamPolicyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\RemoveIamPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.RemoveIamPolicyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Metastore\V1beta\RemoveIamPolicyResponse](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.RemoveIamPolicyResponse)>` |   
  
### restoreServiceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\RestoreServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.RestoreServiceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateMetadataImportAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\UpdateMetadataImportRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.UpdateMetadataImportRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateServiceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Metastore\V1beta\UpdateServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.UpdateServiceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
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
  
### static::backupName

Formats a string containing the fully-qualified path to represent a backup resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`service` |  `string`   
  
`backup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted backup resource.  
  
### static::lakeName

Formats a string containing the fully-qualified path to represent a lake resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`lake` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted lake resource.  
  
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
  
### static::metadataImportName

Formats a string containing the fully-qualified path to represent a metadata_import resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`service` |  `string`   
  
`metadataImport` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted metadata_import resource.  
  
### static::networkName

Formats a string containing the fully-qualified path to represent a network resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`network` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted network resource.  
  
### static::serviceName

Formats a string containing the fully-qualified path to represent a service resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`service` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted service resource.  
  
### static::subnetworkName

Formats a string containing the fully-qualified path to represent a subnetwork resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`region` |  `string`   
  
`subnetwork` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted subnetwork resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * backup: projects/{project}/locations/{location}/services/{service}/backups/{backup}
  * lake: projects/{project}/locations/{location}/lakes/{lake}
  * location: projects/{project}/locations/{location}
  * metadataImport: projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}
  * network: projects/{project}/global/networks/{network}
  * service: projects/{project}/locations/{location}/services/{service}
  * subnetwork: projects/{project}/regions/{region}/subnetworks/{subnetwork}



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
