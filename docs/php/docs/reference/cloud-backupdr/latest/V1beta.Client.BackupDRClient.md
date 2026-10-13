---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient
title: Google Cloud Backup Dr V1beta Client - Class BackupDRClient (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:01.657734+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupDRClient (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupDRClient (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupDRClient.

Service Description: The BackupDR Service

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\BackupDR\V1beta\BackupDRClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new BackupDRClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### createAutoProtectionPolicy

Creates a new AutoProtectionPolicy in a given project and location.

The async variant is [BackupDRClient::createAutoProtectionPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__createAutoProtectionPolicyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateAutoProtectionPolicyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy;
    use Google\Cloud\BackupDR\V1beta\BackupPlanDetail;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\CreateAutoProtectionPolicyRequest;
    use Google\Cloud\BackupDR\V1beta\Criteria;
    use Google\Cloud\BackupDR\V1beta\MatchingCondition;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent                                          The parent resource where this policy will be created.
     *                                                                         Format: projects/{project}/locations/{location}
     *                                                                         Please see {@see BackupDRClient::locationName()} for help formatting this field.
     * @param string $autoProtectionPolicyId                                   The ID to use for the policy.
     *                                                                         This will become the final component of the policy's resource name.
     * @param string $autoProtectionPolicyBackupPlanDetailsResourceType        The type of resource that this policy will automatically protect.
     *                                                                         For MVP, `compute.googleapis.com/Instance` and
     *                                                                         `compute.googleapis.com/Disk` are supported.
     * @param string $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan The resource name of the BackupPlan to apply to resources that
     *                                                                         match the policy's criteria. This backup plan must be in the same location
     *                                                                         as AutoProtectionPolicy. Format:
     *                                                                         projects/{project}/locations/{location}/backupPlans/{backupPlanId}
     *                                                                         Please see {@see BackupDRClient::backupPlanName()} for help formatting this field.
     */
    function create_auto_protection_policy_sample(
        string $formattedParent,
        string $autoProtectionPolicyId,
        string $autoProtectionPolicyBackupPlanDetailsResourceType,
        string $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $backupPlanDetail = (new BackupPlanDetail())
            ->setResourceType($autoProtectionPolicyBackupPlanDetailsResourceType)
            ->setBackupPlan($formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan);
        $autoProtectionPolicyBackupPlanDetails = [$backupPlanDetail,];
        $autoProtectionPolicyCriteriaMatchingConditions = [new MatchingCondition()];
        $autoProtectionPolicyCriteria = (new Criteria())
            ->setMatchingConditions($autoProtectionPolicyCriteriaMatchingConditions);
        $autoProtectionPolicy = (new AutoProtectionPolicy())
            ->setBackupPlanDetails($autoProtectionPolicyBackupPlanDetails)
            ->setCriteria($autoProtectionPolicyCriteria);
        $request = (new CreateAutoProtectionPolicyRequest())
            ->setParent($formattedParent)
            ->setAutoProtectionPolicyId($autoProtectionPolicyId)
            ->setAutoProtectionPolicy($autoProtectionPolicy);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->createAutoProtectionPolicy($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AutoProtectionPolicy $result */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
        $autoProtectionPolicyId = '[AUTO_PROTECTION_POLICY_ID]';
        $autoProtectionPolicyBackupPlanDetailsResourceType = '[RESOURCE_TYPE]';
        $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan = BackupDRClient::backupPlanName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN]'
        );
    
        create_auto_protection_policy_sample(
            $formattedParent,
            $autoProtectionPolicyId,
            $autoProtectionPolicyBackupPlanDetailsResourceType,
            $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan
        );
    }
    

### createAutoProtectionPolicyBinding

Creates a new AutoProtectionPolicyBinding in a given project and location.

The async variant is [BackupDRClient::createAutoProtectionPolicyBindingAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__createAutoProtectionPolicyBindingAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateAutoProtectionPolicyBindingRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\CreateAutoProtectionPolicyBindingRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent                  The parent resource where this binding will be created.
     *                                                 Format:
     *                                                 projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
     *                                                 Please see {@see BackupDRClient::autoProtectionPolicyName()} for help formatting this field.
     * @param string $autoProtectionPolicyBindingId    The ID to use for the binding.
     *                                                 This will become the final component of the binding's resource name.
     * @param string $autoProtectionPolicyBindingScope Immutable. Resource Id of target container on which policy will
     *                                                 be applied. Format: projects/{project_id}
     */
    function create_auto_protection_policy_binding_sample(
        string $formattedParent,
        string $autoProtectionPolicyBindingId,
        string $autoProtectionPolicyBindingScope
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $autoProtectionPolicyBinding = (new AutoProtectionPolicyBinding())
            ->setScope($autoProtectionPolicyBindingScope);
        $request = (new CreateAutoProtectionPolicyBindingRequest())
            ->setParent($formattedParent)
            ->setAutoProtectionPolicyBindingId($autoProtectionPolicyBindingId)
            ->setAutoProtectionPolicyBinding($autoProtectionPolicyBinding);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->createAutoProtectionPolicyBinding($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AutoProtectionPolicyBinding $result */
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
        $formattedParent = BackupDRClient::autoProtectionPolicyName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]'
        );
        $autoProtectionPolicyBindingId = '[AUTO_PROTECTION_POLICY_BINDING_ID]';
        $autoProtectionPolicyBindingScope = '[SCOPE]';
    
        create_auto_protection_policy_binding_sample(
            $formattedParent,
            $autoProtectionPolicyBindingId,
            $autoProtectionPolicyBindingScope
        );
    }
    

### createBackupPlan

Create a BackupPlan

The async variant is [BackupDRClient::createBackupPlanAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__createBackupPlanAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateBackupPlanRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\BackupPlan](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\BackupPlan;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\CreateBackupPlanRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent                The `BackupPlan` project and location in the format
     *                                               `projects/{project}/locations/{location}`. In Google Cloud Backup and DR
     *                                               locations map to Google Cloud regions, for example **us-central1**. Please see
     *                                               {@see BackupDRClient::locationName()} for help formatting this field.
     * @param string $backupPlanId                   The name of the `BackupPlan` to create. The name must be unique
     *                                               for the specified project and location.The name must start with a lowercase
     *                                               letter followed by up to 62 lowercase letters, numbers, or hyphens.
     *                                               Pattern, /[a-z][a-z0-9-]{,62}/.
     * @param string $backupPlanResourceType         The resource type to which the `BackupPlan` will be applied.
     *                                               Examples include, "compute.googleapis.com/Instance",
     *                                               "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster",
     *                                               "compute.googleapis.com/Disk".
     * @param string $formattedBackupPlanBackupVault Resource name of backup vault which will be used as storage
     *                                               location for backups. Format:
     *                                               projects/{project}/locations/{location}/backupVaults/{backupvault}
     *                                               Please see {@see BackupDRClient::backupVaultName()} for help formatting this field.
     */
    function create_backup_plan_sample(
        string $formattedParent,
        string $backupPlanId,
        string $backupPlanResourceType,
        string $formattedBackupPlanBackupVault
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $backupPlan = (new BackupPlan())
            ->setResourceType($backupPlanResourceType)
            ->setBackupVault($formattedBackupPlanBackupVault);
        $request = (new CreateBackupPlanRequest())
            ->setParent($formattedParent)
            ->setBackupPlanId($backupPlanId)
            ->setBackupPlan($backupPlan);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->createBackupPlan($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var BackupPlan $result */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
        $backupPlanId = '[BACKUP_PLAN_ID]';
        $backupPlanResourceType = '[RESOURCE_TYPE]';
        $formattedBackupPlanBackupVault = BackupDRClient::backupVaultName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]'
        );
    
        create_backup_plan_sample(
            $formattedParent,
            $backupPlanId,
            $backupPlanResourceType,
            $formattedBackupPlanBackupVault
        );
    }
    

### createBackupPlanAssociation

Create a BackupPlanAssociation

The async variant is [BackupDRClient::createBackupPlanAssociationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__createBackupPlanAssociationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateBackupPlanAssociationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\BackupPlanAssociation](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\BackupPlanAssociation;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\CreateBackupPlanAssociationRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent                          The backup plan association project and location in the format
     *                                                         `projects/{project_id}/locations/{location}`. In Backup and DR locations
     *                                                         map to Google Cloud regions, for example **us-central1**. Please see
     *                                                         {@see BackupDRClient::locationName()} for help formatting this field.
     * @param string $backupPlanAssociationId                  The name of the backup plan association to create. The name must
     *                                                         be unique for the specified project and location.
     * @param string $backupPlanAssociationResourceType        Immutable. Resource type of workload on which backupplan is
     *                                                         applied
     * @param string $backupPlanAssociationResource            Immutable. Resource name of workload on which the backup plan is
     *                                                         applied.
     *
     *                                                         The format can either be the resource name (e.g.,
     *                                                         "projects/my-project/zones/us-central1-a/instances/my-instance") or the
     *                                                         full resource URI (e.g.,
     *                                                         "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance").
     * @param string $formattedBackupPlanAssociationBackupPlan Resource name of backup plan which needs to be applied on
     *                                                         workload. Format:
     *                                                         projects/{project}/locations/{location}/backupPlans/{backupPlanId}
     *                                                         Please see {@see BackupDRClient::backupPlanName()} for help formatting this field.
     */
    function create_backup_plan_association_sample(
        string $formattedParent,
        string $backupPlanAssociationId,
        string $backupPlanAssociationResourceType,
        string $backupPlanAssociationResource,
        string $formattedBackupPlanAssociationBackupPlan
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $backupPlanAssociation = (new BackupPlanAssociation())
            ->setResourceType($backupPlanAssociationResourceType)
            ->setResource($backupPlanAssociationResource)
            ->setBackupPlan($formattedBackupPlanAssociationBackupPlan);
        $request = (new CreateBackupPlanAssociationRequest())
            ->setParent($formattedParent)
            ->setBackupPlanAssociationId($backupPlanAssociationId)
            ->setBackupPlanAssociation($backupPlanAssociation);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->createBackupPlanAssociation($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var BackupPlanAssociation $result */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
        $backupPlanAssociationId = '[BACKUP_PLAN_ASSOCIATION_ID]';
        $backupPlanAssociationResourceType = '[RESOURCE_TYPE]';
        $backupPlanAssociationResource = '[RESOURCE]';
        $formattedBackupPlanAssociationBackupPlan = BackupDRClient::backupPlanName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN]'
        );
    
        create_backup_plan_association_sample(
            $formattedParent,
            $backupPlanAssociationId,
            $backupPlanAssociationResourceType,
            $backupPlanAssociationResource,
            $formattedBackupPlanAssociationBackupPlan
        );
    }
    

### createBackupVault

Creates a new BackupVault in a given project and location.

The async variant is [BackupDRClient::createBackupVaultAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__createBackupVaultAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateBackupVaultRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\BackupVault](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\BackupVault;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\CreateBackupVaultRequest;
    use Google\Protobuf\Duration;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent Value for parent. Please see
     *                                {@see BackupDRClient::locationName()} for help formatting this field.
     * @param string $backupVaultId   ID of the requesting object
     *                                If auto-generating ID server-side, remove this field and
     *                                backup_vault_id from the method_signature of Create RPC
     */
    function create_backup_vault_sample(string $formattedParent, string $backupVaultId): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $backupVaultBackupMinimumEnforcedRetentionDuration = new Duration();
        $backupVault = (new BackupVault())
            ->setBackupMinimumEnforcedRetentionDuration($backupVaultBackupMinimumEnforcedRetentionDuration);
        $request = (new CreateBackupVaultRequest())
            ->setParent($formattedParent)
            ->setBackupVaultId($backupVaultId)
            ->setBackupVault($backupVault);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->createBackupVault($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var BackupVault $result */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
        $backupVaultId = '[BACKUP_VAULT_ID]';
    
        create_backup_vault_sample($formattedParent, $backupVaultId);
    }
    

### createManagementServer

Creates a new ManagementServer in a given project and location.

The async variant is [BackupDRClient::createManagementServerAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__createManagementServerAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateManagementServerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateManagementServerRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\ManagementServer](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ManagementServer)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\CreateManagementServerRequest;
    use Google\Cloud\BackupDR\V1beta\ManagementServer;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedParent    The management server project and location in the format
     *                                   'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR
     *                                   locations map to Google Cloud regions, for example **us-central1**. Please see
     *                                   {@see BackupDRClient::locationName()} for help formatting this field.
     * @param string $managementServerId The name of the management server to create. The name must be
     *                                   unique for the specified project and location.
     */
    function create_management_server_sample(
        string $formattedParent,
        string $managementServerId
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $managementServer = new ManagementServer();
        $request = (new CreateManagementServerRequest())
            ->setParent($formattedParent)
            ->setManagementServerId($managementServerId)
            ->setManagementServer($managementServer);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->createManagementServer($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var ManagementServer $result */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
        $managementServerId = '[MANAGEMENT_SERVER_ID]';
    
        create_management_server_sample($formattedParent, $managementServerId);
    }
    

### deleteAutoProtectionPolicy

Deletes a single AutoProtectionPolicy.

The async variant is [BackupDRClient::deleteAutoProtectionPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__deleteAutoProtectionPolicyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteAutoProtectionPolicyRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DeleteAutoProtectionPolicyRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName The name of the policy to delete.
     *                              Format:
     *                              projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
     *                              Please see {@see BackupDRClient::autoProtectionPolicyName()} for help formatting this field.
     */
    function delete_auto_protection_policy_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new DeleteAutoProtectionPolicyRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->deleteAutoProtectionPolicy($request);
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
        $formattedName = BackupDRClient::autoProtectionPolicyName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]'
        );
    
        delete_auto_protection_policy_sample($formattedName);
    }
    

### deleteBackup

Deletes a Backup.

The async variant is [BackupDRClient::deleteBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__deleteBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Backup)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\Backup;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DeleteBackupRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName Name of the resource. Please see
     *                              {@see BackupDRClient::backupName()} for help formatting this field.
     */
    function delete_backup_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new DeleteBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->deleteBackup($request);
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
        $formattedName = BackupDRClient::backupName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]',
            '[DATASOURCE]',
            '[BACKUP]'
        );
    
        delete_backup_sample($formattedName);
    }
    

### deleteBackupPlan

Deletes a single BackupPlan.

The async variant is [BackupDRClient::deleteBackupPlanAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__deleteBackupPlanAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupPlanRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DeleteBackupPlanRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName The resource name of the `BackupPlan` to delete.
     *
     *                              Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`
     *                              Please see {@see BackupDRClient::backupPlanName()} for help formatting this field.
     */
    function delete_backup_plan_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new DeleteBackupPlanRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->deleteBackupPlan($request);
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
        $formattedName = BackupDRClient::backupPlanName('[PROJECT]', '[LOCATION]', '[BACKUP_PLAN]');
    
        delete_backup_plan_sample($formattedName);
    }
    

### deleteBackupPlanAssociation

Deletes a single BackupPlanAssociation.

The async variant is [BackupDRClient::deleteBackupPlanAssociationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__deleteBackupPlanAssociationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupPlanAssociationRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DeleteBackupPlanAssociationRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName Name of the backup plan association resource, in the format
     *                              `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
     *                              Please see {@see BackupDRClient::backupPlanAssociationName()} for help formatting this field.
     */
    function delete_backup_plan_association_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new DeleteBackupPlanAssociationRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->deleteBackupPlanAssociation($request);
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
        $formattedName = BackupDRClient::backupPlanAssociationName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN_ASSOCIATION]'
        );
    
        delete_backup_plan_association_sample($formattedName);
    }
    

### deleteBackupVault

Deletes a BackupVault.

The async variant is [BackupDRClient::deleteBackupVaultAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__deleteBackupVaultAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupVaultRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DeleteBackupVaultRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName Name of the resource. Please see
     *                              {@see BackupDRClient::backupVaultName()} for help formatting this field.
     */
    function delete_backup_vault_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new DeleteBackupVaultRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->deleteBackupVault($request);
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
        $formattedName = BackupDRClient::backupVaultName('[PROJECT]', '[LOCATION]', '[BACKUPVAULT]');
    
        delete_backup_vault_sample($formattedName);
    }
    

### deleteManagementServer

Deletes a single ManagementServer.

The async variant is [BackupDRClient::deleteManagementServerAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__deleteManagementServerAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteManagementServerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteManagementServerRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DeleteManagementServerRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName Name of the resource
     *                              Please see {@see BackupDRClient::managementServerName()} for help formatting this field.
     */
    function delete_management_server_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new DeleteManagementServerRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->deleteManagementServer($request);
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
        $formattedName = BackupDRClient::managementServerName(
            '[PROJECT]',
            '[LOCATION]',
            '[MANAGEMENTSERVER]'
        );
    
        delete_management_server_sample($formattedName);
    }
    

### fetchBackupPlanAssociationsForResourceType

List BackupPlanAssociations for a given resource type.

The async variant is [BackupDRClient::fetchBackupPlanAssociationsForResourceTypeAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__fetchBackupPlanAssociationsForResourceTypeAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchBackupPlanAssociationsForResourceTypeRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\BackupPlanAssociation;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\FetchBackupPlanAssociationsForResourceTypeRequest;
    
    /**
     * @param string $formattedParent The parent resource name.
     *                                Format: projects/{project}/locations/{location}
     *                                Please see {@see BackupDRClient::locationName()} for help formatting this field.
     * @param string $resourceType    The type of the Google Cloud resource.
     *                                Ex: sql.googleapis.com/Instance
     */
    function fetch_backup_plan_associations_for_resource_type_sample(
        string $formattedParent,
        string $resourceType
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new FetchBackupPlanAssociationsForResourceTypeRequest())
            ->setParent($formattedParent)
            ->setResourceType($resourceType);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->fetchBackupPlanAssociationsForResourceType($request);
    
            /** @var BackupPlanAssociation $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
        $resourceType = '[RESOURCE_TYPE]';
    
        fetch_backup_plan_associations_for_resource_type_sample($formattedParent, $resourceType);
    }
    

### fetchBackupsForResourceType

Fetch Backups for a given resource type.

The async variant is [BackupDRClient::fetchBackupsForResourceTypeAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__fetchBackupsForResourceTypeAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchBackupsForResourceTypeRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Backup;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\FetchBackupsForResourceTypeRequest;
    
    /**
     * @param string $formattedParent Datasources are the parent resource for the backups.
     *                                Format:
     *                                projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}
     *                                Please see {@see BackupDRClient::dataSourceName()} for help formatting this field.
     * @param string $resourceType    The type of the GCP resource.
     *                                Ex: sqladmin.googleapis.com/Instance
     */
    function fetch_backups_for_resource_type_sample(
        string $formattedParent,
        string $resourceType
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new FetchBackupsForResourceTypeRequest())
            ->setParent($formattedParent)
            ->setResourceType($resourceType);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->fetchBackupsForResourceType($request);
    
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
        $formattedParent = BackupDRClient::dataSourceName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]',
            '[DATASOURCE]'
        );
        $resourceType = '[RESOURCE_TYPE]';
    
        fetch_backups_for_resource_type_sample($formattedParent, $resourceType);
    }
    

### fetchDataSourceReferencesForResourceType

Fetch DataSourceReferences for a given project, location and resource type.

The async variant is [BackupDRClient::fetchDataSourceReferencesForResourceTypeAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__fetchDataSourceReferencesForResourceTypeAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchDataSourceReferencesForResourceTypeRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DataSourceReference;
    use Google\Cloud\BackupDR\V1beta\FetchDataSourceReferencesForResourceTypeRequest;
    
    /**
     * @param string $formattedParent The parent resource name.
     *                                Format: projects/{project}/locations/{location}
     *                                Please see {@see BackupDRClient::locationName()} for help formatting this field.
     * @param string $resourceType    The type of the Google Cloud resource.
     *                                Ex: sql.googleapis.com/Instance
     */
    function fetch_data_source_references_for_resource_type_sample(
        string $formattedParent,
        string $resourceType
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new FetchDataSourceReferencesForResourceTypeRequest())
            ->setParent($formattedParent)
            ->setResourceType($resourceType);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->fetchDataSourceReferencesForResourceType($request);
    
            /** @var DataSourceReference $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
        $resourceType = '[RESOURCE_TYPE]';
    
        fetch_data_source_references_for_resource_type_sample($formattedParent, $resourceType);
    }
    

### fetchUsableBackupVaults

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

The async variant is [BackupDRClient::fetchUsableBackupVaultsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__fetchUsableBackupVaultsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchUsableBackupVaultsRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\BackupVault;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\FetchUsableBackupVaultsRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve backupvault stores
     *                                information, in the format 'projects/{project_id}/locations/{location}'. In
     *                                Google Cloud Backup and DR, locations map to Google Cloud regions, for
     *                                example
     *                                **us-central1**.
     *                                To retrieve backupvault stores for all locations, use "-" for the
     *                                '{location}' value. Please see
     *                                {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function fetch_usable_backup_vaults_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new FetchUsableBackupVaultsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->fetchUsableBackupVaults($request);
    
            /** @var BackupVault $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        fetch_usable_backup_vaults_sample($formattedParent);
    }
    

### getAutoProtectionPolicy

Gets details of a single AutoProtectionPolicy.

The async variant is [BackupDRClient::getAutoProtectionPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getAutoProtectionPolicyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetAutoProtectionPolicyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetAutoProtectionPolicyRequest;
    
    /**
     * @param string $formattedName The name of the policy to retrieve.
     *                              Format:
     *                              projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
     *                              Please see {@see BackupDRClient::autoProtectionPolicyName()} for help formatting this field.
     */
    function get_auto_protection_policy_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetAutoProtectionPolicyRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var AutoProtectionPolicy $response */
            $response = $backupDRClient->getAutoProtectionPolicy($request);
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
        $formattedName = BackupDRClient::autoProtectionPolicyName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]'
        );
    
        get_auto_protection_policy_sample($formattedName);
    }
    

### getAutoProtectionPolicyBinding

Returns the auto protection policy binding read from the CCFE tables.

The async variant is [BackupDRClient::getAutoProtectionPolicyBindingAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getAutoProtectionPolicyBindingAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetAutoProtectionPolicyBindingRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetAutoProtectionPolicyBindingRequest;
    
    /**
     * @param string $formattedName The name of the binding to retrieve.
     *                              Format:
     *                              projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
     *                              Please see {@see BackupDRClient::autoProtectionPolicyBindingName()} for help formatting this field.
     */
    function get_auto_protection_policy_binding_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetAutoProtectionPolicyBindingRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var AutoProtectionPolicyBinding $response */
            $response = $backupDRClient->getAutoProtectionPolicyBinding($request);
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
        $formattedName = BackupDRClient::autoProtectionPolicyBindingName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]',
            '[BINDING]'
        );
    
        get_auto_protection_policy_binding_sample($formattedName);
    }
    

### getBackup

Gets details of a Backup.

The async variant is [BackupDRClient::getBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Backup)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Backup;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetBackupRequest;
    
    /**
     * @param string $formattedName Name of the data source resource name, in the format
     *                              'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}'
     *                              Please see {@see BackupDRClient::backupName()} for help formatting this field.
     */
    function get_backup_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Backup $response */
            $response = $backupDRClient->getBackup($request);
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
        $formattedName = BackupDRClient::backupName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]',
            '[DATASOURCE]',
            '[BACKUP]'
        );
    
        get_backup_sample($formattedName);
    }
    

### getBackupPlan

Gets details of a single BackupPlan.

The async variant is [BackupDRClient::getBackupPlanAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getBackupPlanAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupPlanRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\BackupPlan](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\BackupPlan;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetBackupPlanRequest;
    
    /**
     * @param string $formattedName The resource name of the `BackupPlan` to retrieve.
     *
     *                              Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`
     *                              Please see {@see BackupDRClient::backupPlanName()} for help formatting this field.
     */
    function get_backup_plan_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetBackupPlanRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var BackupPlan $response */
            $response = $backupDRClient->getBackupPlan($request);
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
        $formattedName = BackupDRClient::backupPlanName('[PROJECT]', '[LOCATION]', '[BACKUP_PLAN]');
    
        get_backup_plan_sample($formattedName);
    }
    

### getBackupPlanAssociation

Gets details of a single BackupPlanAssociation.

The async variant is [BackupDRClient::getBackupPlanAssociationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getBackupPlanAssociationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupPlanAssociationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\BackupPlanAssociation](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\BackupPlanAssociation;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetBackupPlanAssociationRequest;
    
    /**
     * @param string $formattedName Name of the backup plan association resource, in the format
     *                              `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
     *                              Please see {@see BackupDRClient::backupPlanAssociationName()} for help formatting this field.
     */
    function get_backup_plan_association_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetBackupPlanAssociationRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var BackupPlanAssociation $response */
            $response = $backupDRClient->getBackupPlanAssociation($request);
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
        $formattedName = BackupDRClient::backupPlanAssociationName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN_ASSOCIATION]'
        );
    
        get_backup_plan_association_sample($formattedName);
    }
    

### getBackupPlanRevision

Gets details of a single BackupPlanRevision.

The async variant is [BackupDRClient::getBackupPlanRevisionAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getBackupPlanRevisionAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupPlanRevisionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupPlanRevisionRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\BackupPlanRevision](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanRevision)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\BackupPlanRevision;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetBackupPlanRevisionRequest;
    
    /**
     * @param string $formattedName The resource name of the `BackupPlanRevision` to retrieve.
     *
     *                              Format:
     *                              `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`
     *                              Please see {@see BackupDRClient::backupPlanRevisionName()} for help formatting this field.
     */
    function get_backup_plan_revision_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetBackupPlanRevisionRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var BackupPlanRevision $response */
            $response = $backupDRClient->getBackupPlanRevision($request);
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
        $formattedName = BackupDRClient::backupPlanRevisionName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN]',
            '[REVISION]'
        );
    
        get_backup_plan_revision_sample($formattedName);
    }
    

### getBackupVault

Gets details of a BackupVault.

The async variant is [BackupDRClient::getBackupVaultAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getBackupVaultAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupVaultRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\BackupVault](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\BackupVault;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetBackupVaultRequest;
    
    /**
     * @param string $formattedName Name of the backupvault store resource name, in the format
     *                              'projects/{project_id}/locations/{location}/backupVaults/{resource_name}'
     *                              Please see {@see BackupDRClient::backupVaultName()} for help formatting this field.
     */
    function get_backup_vault_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetBackupVaultRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var BackupVault $response */
            $response = $backupDRClient->getBackupVault($request);
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
        $formattedName = BackupDRClient::backupVaultName('[PROJECT]', '[LOCATION]', '[BACKUPVAULT]');
    
        get_backup_vault_sample($formattedName);
    }
    

### getBindingMatchingResource

Gets details of a single Binding Matching Resource.

The async variant is [BackupDRClient::getBindingMatchingResourceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getBindingMatchingResourceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBindingMatchingResourceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBindingMatchingResourceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\BindingMatchingResource](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingMatchingResource)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\BindingMatchingResource;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetBindingMatchingResourceRequest;
    
    /**
     * @param string $formattedName The name of the matching resource to retrieve.
     *                              Format:
     *                              projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}
     *                              Please see {@see BackupDRClient::bindingMatchingResourceName()} for help formatting this field.
     */
    function get_binding_matching_resource_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetBindingMatchingResourceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var BindingMatchingResource $response */
            $response = $backupDRClient->getBindingMatchingResource($request);
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
        $formattedName = BackupDRClient::bindingMatchingResourceName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]',
            '[BINDING]',
            '[MATCHING_RESOURCE]'
        );
    
        get_binding_matching_resource_sample($formattedName);
    }
    

### getDataSource

Gets details of a DataSource.

The async variant is [BackupDRClient::getDataSourceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getDataSourceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetDataSourceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetDataSourceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\DataSource](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DataSource)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DataSource;
    use Google\Cloud\BackupDR\V1beta\GetDataSourceRequest;
    
    /**
     * @param string $formattedName Name of the data source resource name, in the format
     *                              'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}'
     *                              Please see {@see BackupDRClient::dataSourceName()} for help formatting this field.
     */
    function get_data_source_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetDataSourceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataSource $response */
            $response = $backupDRClient->getDataSource($request);
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
        $formattedName = BackupDRClient::dataSourceName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]',
            '[DATASOURCE]'
        );
    
        get_data_source_sample($formattedName);
    }
    

### getDataSourceReference

Gets details of a single DataSourceReference.

The async variant is [BackupDRClient::getDataSourceReferenceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getDataSourceReferenceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetDataSourceReferenceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetDataSourceReferenceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\DataSourceReference](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DataSourceReference)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DataSourceReference;
    use Google\Cloud\BackupDR\V1beta\GetDataSourceReferenceRequest;
    
    /**
     * @param string $formattedName The name of the DataSourceReference to retrieve.
     *                              Format:
     *                              projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}
     *                              Please see {@see BackupDRClient::dataSourceReferenceName()} for help formatting this field.
     */
    function get_data_source_reference_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetDataSourceReferenceRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DataSourceReference $response */
            $response = $backupDRClient->getDataSourceReference($request);
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
        $formattedName = BackupDRClient::dataSourceReferenceName(
            '[PROJECT]',
            '[LOCATION]',
            '[DATA_SOURCE_REFERENCE]'
        );
    
        get_data_source_reference_sample($formattedName);
    }
    

### getManagementServer

Gets details of a single ManagementServer.

The async variant is [BackupDRClient::getManagementServerAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getManagementServerAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetManagementServerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetManagementServerRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\BackupDR\V1beta\ManagementServer](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ManagementServer)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\GetManagementServerRequest;
    use Google\Cloud\BackupDR\V1beta\ManagementServer;
    
    /**
     * @param string $formattedName Name of the management server resource name, in the format
     *                              'projects/{project_id}/locations/{location}/managementServers/{resource_name}'
     *                              Please see {@see BackupDRClient::managementServerName()} for help formatting this field.
     */
    function get_management_server_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetManagementServerRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var ManagementServer $response */
            $response = $backupDRClient->getManagementServer($request);
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
        $formattedName = BackupDRClient::managementServerName(
            '[PROJECT]',
            '[LOCATION]',
            '[MANAGEMENTSERVER]'
        );
    
        get_management_server_sample($formattedName);
    }
    

### initializeService

Initializes the service related config for a project.

The async variant is [BackupDRClient::initializeServiceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__initializeServiceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\InitializeServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.InitializeServiceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\InitializeServiceResponse](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.InitializeServiceResponse)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\InitializeServiceRequest;
    use Google\Cloud\BackupDR\V1beta\InitializeServiceResponse;
    use Google\Rpc\Status;
    
    /**
     * @param string $name         The resource name of the serviceConfig used to initialize the
     *                             service. The location must be the location of the BackupVault.
     *                             Format: `projects/{project_id}/locations/{location}/serviceConfig`.
     * @param string $resourceType The resource type to which the default service config will be
     *                             applied. Examples include, "compute.googleapis.com/Instance" and
     *                             "storage.googleapis.com/Bucket".
     */
    function initialize_service_sample(string $name, string $resourceType): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new InitializeServiceRequest())
            ->setName($name)
            ->setResourceType($resourceType);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->initializeService($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var InitializeServiceResponse $result */
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
        $resourceType = '[RESOURCE_TYPE]';
    
        initialize_service_sample($name, $resourceType);
    }
    

### initiateDeleteAutoProtectionPolicyBinding

InitiateDeleteAutoProtectionPolicyBinding initiates delete for AutoProtectionPolicy Binding

The async variant is [BackupDRClient::initiateDeleteAutoProtectionPolicyBindingAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__initiateDeleteAutoProtectionPolicyBindingAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\InitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.InitiateDeleteAutoProtectionPolicyBindingRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\InitiateDeleteAutoProtectionPolicyBindingRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName The name of the binding to delete.
     *                              Format:
     *                              projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
     *                              Please see {@see BackupDRClient::autoProtectionPolicyBindingName()} for help formatting this field.
     */
    function initiate_delete_auto_protection_policy_binding_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new InitiateDeleteAutoProtectionPolicyBindingRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->initiateDeleteAutoProtectionPolicyBinding($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AutoProtectionPolicyBinding $result */
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
        $formattedName = BackupDRClient::autoProtectionPolicyBindingName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]',
            '[BINDING]'
        );
    
        initiate_delete_auto_protection_policy_binding_sample($formattedName);
    }
    

### listAppliedAutoProtectionPolicies

Lists AppliedAutoProtectionPolicies in a given project and location.

The async variant is [BackupDRClient::listAppliedAutoProtectionPoliciesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listAppliedAutoProtectionPoliciesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListAppliedAutoProtectionPoliciesRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\AppliedAutoProtectionPolicy;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListAppliedAutoProtectionPoliciesRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve the list of
     *                                applied policies. Format: projects/{project}/locations/{location}
     *                                Please see {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function list_applied_auto_protection_policies_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListAppliedAutoProtectionPoliciesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listAppliedAutoProtectionPolicies($request);
    
            /** @var AppliedAutoProtectionPolicy $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_applied_auto_protection_policies_sample($formattedParent);
    }
    

### listAutoProtectionPolicies

Lists AutoProtectionPolicies for a given project and location.

The async variant is [BackupDRClient::listAutoProtectionPoliciesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listAutoProtectionPoliciesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListAutoProtectionPoliciesRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListAutoProtectionPoliciesRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve the list of
     *                                policies. Format: projects/{project}/locations/{location}
     *                                Please see {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function list_auto_protection_policies_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListAutoProtectionPoliciesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listAutoProtectionPolicies($request);
    
            /** @var AutoProtectionPolicy $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_auto_protection_policies_sample($formattedParent);
    }
    

### listAutoProtectionPolicyBindings

Returns the auto protection policy bindings read from the CCFE tables.

The async variant is [BackupDRClient::listAutoProtectionPolicyBindingsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listAutoProtectionPolicyBindingsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListAutoProtectionPolicyBindingsRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListAutoProtectionPolicyBindingsRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve the list of
     *                                policies. Format: projects/{project}/locations/{location}
     *                                Please see {@see BackupDRClient::autoProtectionPolicyName()} for help formatting this field.
     */
    function list_auto_protection_policy_bindings_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListAutoProtectionPolicyBindingsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listAutoProtectionPolicyBindings($request);
    
            /** @var AutoProtectionPolicyBinding $element */
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
        $formattedParent = BackupDRClient::autoProtectionPolicyName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]'
        );
    
        list_auto_protection_policy_bindings_sample($formattedParent);
    }
    

### listBackupPlanAssociations

Lists BackupPlanAssociations in a given project and location.

The async variant is [BackupDRClient::listBackupPlanAssociationsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listBackupPlanAssociationsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupPlanAssociationsRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\BackupPlanAssociation;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListBackupPlanAssociationsRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve backup Plan
     *                                Associations information, in the format
     *                                `projects/{project_id}/locations/{location}`. In Backup and DR, locations
     *                                map to Google Cloud regions, for example **us-central1**. To retrieve
     *                                backup plan associations for all locations, use "-" for the
     *                                `{location}` value. Please see
     *                                {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function list_backup_plan_associations_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListBackupPlanAssociationsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listBackupPlanAssociations($request);
    
            /** @var BackupPlanAssociation $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_backup_plan_associations_sample($formattedParent);
    }
    

### listBackupPlanRevisions

Lists BackupPlanRevisions in a given project and location.

The async variant is [BackupDRClient::listBackupPlanRevisionsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listBackupPlanRevisionsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupPlanRevisionsRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\BackupPlanRevision;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListBackupPlanRevisionsRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve
     *                                `BackupPlanRevisions` information. Format:
     *                                `projects/{project}/locations/{location}/backupPlans/{backup_plan}`. In
     *                                Google Cloud Backup and DR, locations map to Google Cloud regions, for e.g.
     *                                **us-central1**. Please see
     *                                {@see BackupDRClient::backupPlanName()} for help formatting this field.
     */
    function list_backup_plan_revisions_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListBackupPlanRevisionsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listBackupPlanRevisions($request);
    
            /** @var BackupPlanRevision $element */
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
        $formattedParent = BackupDRClient::backupPlanName('[PROJECT]', '[LOCATION]', '[BACKUP_PLAN]');
    
        list_backup_plan_revisions_sample($formattedParent);
    }
    

### listBackupPlans

Lists BackupPlans in a given project and location.

The async variant is [BackupDRClient::listBackupPlansAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listBackupPlansAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupPlansRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupPlansRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\BackupPlan;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListBackupPlansRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve `BackupPlans`
     *                                information. Format: `projects/{project}/locations/{location}`. In Google
     *                                Cloud Backup and DR, locations map to Google Cloud regions, for e.g.
     *                                **us-central1**. To retrieve backup plans for all locations, use "-" for
     *                                the
     *                                `{location}` value. Please see
     *                                {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function list_backup_plans_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListBackupPlansRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listBackupPlans($request);
    
            /** @var BackupPlan $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_backup_plans_sample($formattedParent);
    }
    

### listBackupVaults

Lists BackupVaults in a given project and location.

The async variant is [BackupDRClient::listBackupVaultsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listBackupVaultsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupVaultsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupVaultsRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\BackupVault;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListBackupVaultsRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve backupvault stores
     *                                information, in the format 'projects/{project_id}/locations/{location}'. In
     *                                Google Cloud Backup and DR, locations map to Google Cloud regions, for
     *                                example
     *                                **us-central1**.
     *                                To retrieve backupvault stores for all locations, use "-" for the
     *                                '{location}' value. Please see
     *                                {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function list_backup_vaults_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListBackupVaultsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listBackupVaults($request);
    
            /** @var BackupVault $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_backup_vaults_sample($formattedParent);
    }
    

### listBackups

Lists Backups in a given project and location.

The async variant is [BackupDRClient::listBackupsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listBackupsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupsRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Backup;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListBackupsRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve backup
     *                                information, in the format
     *                                'projects/{project_id}/locations/{location}'. In Google Cloud Backup and
     *                                DR, locations map to Google Cloud regions, for example
     *                                **us-central1**.
     *                                To retrieve data sources for all locations, use "-" for the
     *                                '{location}' value. Please see
     *                                {@see BackupDRClient::dataSourceName()} for help formatting this field.
     */
    function list_backups_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListBackupsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listBackups($request);
    
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
        $formattedParent = BackupDRClient::dataSourceName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]',
            '[DATASOURCE]'
        );
    
        list_backups_sample($formattedParent);
    }
    

### listBindingMatchingResources

Lists Binding Matching Resources for a given AutoProtectionPolicyBinding.

The async variant is [BackupDRClient::listBindingMatchingResourcesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listBindingMatchingResourcesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBindingMatchingResourcesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBindingMatchingResourcesRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\BindingMatchingResource;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListBindingMatchingResourcesRequest;
    
    /**
     * @param string $formattedParent The project, location, auto protection policy and binding for
     *                                which to retrieve `BindingMatchingResources` information. Format:
     *                                `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}`.
     *                                In Google Cloud Backup and DR, locations map to Google Cloud regions, for
     *                                example **us-central1**. Please see
     *                                {@see BackupDRClient::autoProtectionPolicyBindingName()} for help formatting this field.
     */
    function list_binding_matching_resources_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListBindingMatchingResourcesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listBindingMatchingResources($request);
    
            /** @var BindingMatchingResource $element */
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
        $formattedParent = BackupDRClient::autoProtectionPolicyBindingName(
            '[PROJECT]',
            '[LOCATION]',
            '[AUTO_PROTECTION_POLICY]',
            '[BINDING]'
        );
    
        list_binding_matching_resources_sample($formattedParent);
    }
    

### listDataSourceReferences

Lists DataSourceReferences for a given project and location.

The async variant is [BackupDRClient::listDataSourceReferencesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listDataSourceReferencesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListDataSourceReferencesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListDataSourceReferencesRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DataSourceReference;
    use Google\Cloud\BackupDR\V1beta\ListDataSourceReferencesRequest;
    
    /**
     * @param string $formattedParent The parent resource name.
     *                                Format: projects/{project}/locations/{location}
     *                                Please see {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function list_data_source_references_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListDataSourceReferencesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listDataSourceReferences($request);
    
            /** @var DataSourceReference $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_data_source_references_sample($formattedParent);
    }
    

### listDataSources

Lists DataSources in a given project and location.

The async variant is [BackupDRClient::listDataSourcesAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listDataSourcesAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListDataSourcesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListDataSourcesRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DataSource;
    use Google\Cloud\BackupDR\V1beta\ListDataSourcesRequest;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve data
     *                                sources information, in the format
     *                                'projects/{project_id}/locations/{location}'. In Google Cloud Backup and
     *                                DR, locations map to Google Cloud regions, for example
     *                                **us-central1**.
     *                                To retrieve data sources for all locations, use "-" for the
     *                                '{location}' value. Please see
     *                                {@see BackupDRClient::backupVaultName()} for help formatting this field.
     */
    function list_data_sources_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListDataSourcesRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listDataSources($request);
    
            /** @var DataSource $element */
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
        $formattedParent = BackupDRClient::backupVaultName('[PROJECT]', '[LOCATION]', '[BACKUPVAULT]');
    
        list_data_sources_sample($formattedParent);
    }
    

### listManagementServers

Lists ManagementServers in a given project and location.

The async variant is [BackupDRClient::listManagementServersAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listManagementServersAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListManagementServersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListManagementServersRequest)`   
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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\ListManagementServersRequest;
    use Google\Cloud\BackupDR\V1beta\ManagementServer;
    
    /**
     * @param string $formattedParent The project and location for which to retrieve management servers
     *                                information, in the format 'projects/{project_id}/locations/{location}'.
     *                                In Google Cloud Backup and DR, locations map to Google Cloud regions, for
     *                                example
     *                                **us-central1**. To retrieve management servers for all locations, use "-"
     *                                for the
     *                                '{location}' value. Please see
     *                                {@see BackupDRClient::locationName()} for help formatting this field.
     */
    function list_management_servers_sample(string $formattedParent): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new ListManagementServersRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listManagementServers($request);
    
            /** @var ManagementServer $element */
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
        $formattedParent = BackupDRClient::locationName('[PROJECT]', '[LOCATION]');
    
        list_management_servers_sample($formattedParent);
    }
    

### restoreBackup

Restore from a Backup

The async variant is [BackupDRClient::restoreBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__restoreBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\RestoreBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.RestoreBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\RestoreBackupResponse](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.RestoreBackupResponse)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\RestoreBackupRequest;
    use Google\Cloud\BackupDR\V1beta\RestoreBackupResponse;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName The resource name of the Backup instance, in the format
     *                              'projects/&#42;/locations/&#42;/backupVaults/&#42;/dataSources/&#42;/backups/'. Please see
     *                              {@see BackupDRClient::backupName()} for help formatting this field.
     */
    function restore_backup_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new RestoreBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->restoreBackup($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var RestoreBackupResponse $result */
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
        $formattedName = BackupDRClient::backupName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]',
            '[DATASOURCE]',
            '[BACKUP]'
        );
    
        restore_backup_sample($formattedName);
    }
    

### triggerBackup

Triggers a new Backup.

The async variant is [BackupDRClient::triggerBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__triggerBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\TriggerBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.TriggerBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\BackupPlanAssociation](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\BackupPlanAssociation;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\TriggerBackupRequest;
    use Google\Rpc\Status;
    
    /**
     * @param string $formattedName Name of the backup plan association resource, in the format
     *                              `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
     *                              Please see {@see BackupDRClient::backupPlanAssociationName()} for help formatting this field.
     */
    function trigger_backup_sample(string $formattedName): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new TriggerBackupRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->triggerBackup($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var BackupPlanAssociation $result */
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
        $formattedName = BackupDRClient::backupPlanAssociationName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN_ASSOCIATION]'
        );
    
        trigger_backup_sample($formattedName);
    }
    

### updateAutoProtectionPolicy

Updates the parameters of a single AutoProtectionPolicy.

The async variant is [BackupDRClient::updateAutoProtectionPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__updateAutoProtectionPolicyAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateAutoProtectionPolicyRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy;
    use Google\Cloud\BackupDR\V1beta\BackupPlanDetail;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\Criteria;
    use Google\Cloud\BackupDR\V1beta\MatchingCondition;
    use Google\Cloud\BackupDR\V1beta\UpdateAutoProtectionPolicyRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * @param string $autoProtectionPolicyBackupPlanDetailsResourceType        The type of resource that this policy will automatically protect.
     *                                                                         For MVP, `compute.googleapis.com/Instance` and
     *                                                                         `compute.googleapis.com/Disk` are supported.
     * @param string $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan The resource name of the BackupPlan to apply to resources that
     *                                                                         match the policy's criteria. This backup plan must be in the same location
     *                                                                         as AutoProtectionPolicy. Format:
     *                                                                         projects/{project}/locations/{location}/backupPlans/{backupPlanId}
     *                                                                         Please see {@see BackupDRClient::backupPlanName()} for help formatting this field.
     */
    function update_auto_protection_policy_sample(
        string $autoProtectionPolicyBackupPlanDetailsResourceType,
        string $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $backupPlanDetail = (new BackupPlanDetail())
            ->setResourceType($autoProtectionPolicyBackupPlanDetailsResourceType)
            ->setBackupPlan($formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan);
        $autoProtectionPolicyBackupPlanDetails = [$backupPlanDetail,];
        $autoProtectionPolicyCriteriaMatchingConditions = [new MatchingCondition()];
        $autoProtectionPolicyCriteria = (new Criteria())
            ->setMatchingConditions($autoProtectionPolicyCriteriaMatchingConditions);
        $autoProtectionPolicy = (new AutoProtectionPolicy())
            ->setBackupPlanDetails($autoProtectionPolicyBackupPlanDetails)
            ->setCriteria($autoProtectionPolicyCriteria);
        $updateMask = new FieldMask();
        $request = (new UpdateAutoProtectionPolicyRequest())
            ->setAutoProtectionPolicy($autoProtectionPolicy)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->updateAutoProtectionPolicy($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var AutoProtectionPolicy $result */
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
        $autoProtectionPolicyBackupPlanDetailsResourceType = '[RESOURCE_TYPE]';
        $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan = BackupDRClient::backupPlanName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN]'
        );
    
        update_auto_protection_policy_sample(
            $autoProtectionPolicyBackupPlanDetailsResourceType,
            $formattedAutoProtectionPolicyBackupPlanDetailsBackupPlan
        );
    }
    

### updateBackup

Updates the settings of a Backup.

The async variant is [BackupDRClient::updateBackupAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__updateBackupAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Backup)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\Backup;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\UpdateBackupRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_backup_sample(): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $backup = new Backup();
        $request = (new UpdateBackupRequest())
            ->setUpdateMask($updateMask)
            ->setBackup($backup);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->updateBackup($request);
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
    

### updateBackupPlan

Update a BackupPlan.

The async variant is [BackupDRClient::updateBackupPlanAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__updateBackupPlanAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupPlanRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\BackupPlan](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\BackupPlan;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\UpdateBackupPlanRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * @param string $backupPlanResourceType         The resource type to which the `BackupPlan` will be applied.
     *                                               Examples include, "compute.googleapis.com/Instance",
     *                                               "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster",
     *                                               "compute.googleapis.com/Disk".
     * @param string $formattedBackupPlanBackupVault Resource name of backup vault which will be used as storage
     *                                               location for backups. Format:
     *                                               projects/{project}/locations/{location}/backupVaults/{backupvault}
     *                                               Please see {@see BackupDRClient::backupVaultName()} for help formatting this field.
     */
    function update_backup_plan_sample(
        string $backupPlanResourceType,
        string $formattedBackupPlanBackupVault
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $backupPlan = (new BackupPlan())
            ->setResourceType($backupPlanResourceType)
            ->setBackupVault($formattedBackupPlanBackupVault);
        $updateMask = new FieldMask();
        $request = (new UpdateBackupPlanRequest())
            ->setBackupPlan($backupPlan)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->updateBackupPlan($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var BackupPlan $result */
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
        $backupPlanResourceType = '[RESOURCE_TYPE]';
        $formattedBackupPlanBackupVault = BackupDRClient::backupVaultName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUPVAULT]'
        );
    
        update_backup_plan_sample($backupPlanResourceType, $formattedBackupPlanBackupVault);
    }
    

### updateBackupPlanAssociation

Update a BackupPlanAssociation.

The async variant is [BackupDRClient::updateBackupPlanAssociationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__updateBackupPlanAssociationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupPlanAssociationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\BackupPlanAssociation](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\BackupPlanAssociation;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\UpdateBackupPlanAssociationRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * @param string $backupPlanAssociationResourceType        Immutable. Resource type of workload on which backupplan is
     *                                                         applied
     * @param string $backupPlanAssociationResource            Immutable. Resource name of workload on which the backup plan is
     *                                                         applied.
     *
     *                                                         The format can either be the resource name (e.g.,
     *                                                         "projects/my-project/zones/us-central1-a/instances/my-instance") or the
     *                                                         full resource URI (e.g.,
     *                                                         "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance").
     * @param string $formattedBackupPlanAssociationBackupPlan Resource name of backup plan which needs to be applied on
     *                                                         workload. Format:
     *                                                         projects/{project}/locations/{location}/backupPlans/{backupPlanId}
     *                                                         Please see {@see BackupDRClient::backupPlanName()} for help formatting this field.
     */
    function update_backup_plan_association_sample(
        string $backupPlanAssociationResourceType,
        string $backupPlanAssociationResource,
        string $formattedBackupPlanAssociationBackupPlan
    ): void {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $backupPlanAssociation = (new BackupPlanAssociation())
            ->setResourceType($backupPlanAssociationResourceType)
            ->setResource($backupPlanAssociationResource)
            ->setBackupPlan($formattedBackupPlanAssociationBackupPlan);
        $updateMask = new FieldMask();
        $request = (new UpdateBackupPlanAssociationRequest())
            ->setBackupPlanAssociation($backupPlanAssociation)
            ->setUpdateMask($updateMask);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->updateBackupPlanAssociation($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var BackupPlanAssociation $result */
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
        $backupPlanAssociationResourceType = '[RESOURCE_TYPE]';
        $backupPlanAssociationResource = '[RESOURCE]';
        $formattedBackupPlanAssociationBackupPlan = BackupDRClient::backupPlanName(
            '[PROJECT]',
            '[LOCATION]',
            '[BACKUP_PLAN]'
        );
    
        update_backup_plan_association_sample(
            $backupPlanAssociationResourceType,
            $backupPlanAssociationResource,
            $formattedBackupPlanAssociationBackupPlan
        );
    }
    

### updateBackupVault

Updates the settings of a BackupVault.

The async variant is [BackupDRClient::updateBackupVaultAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__updateBackupVaultAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupVaultRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\BackupVault](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\BackupVault;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\UpdateBackupVaultRequest;
    use Google\Protobuf\Duration;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_backup_vault_sample(): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $backupVaultBackupMinimumEnforcedRetentionDuration = new Duration();
        $backupVault = (new BackupVault())
            ->setBackupMinimumEnforcedRetentionDuration($backupVaultBackupMinimumEnforcedRetentionDuration);
        $request = (new UpdateBackupVaultRequest())
            ->setUpdateMask($updateMask)
            ->setBackupVault($backupVault);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->updateBackupVault($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var BackupVault $result */
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
    

### updateDataSource

Updates the settings of a DataSource.

The async variant is [BackupDRClient::updateDataSourceAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__updateDataSourceAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateDataSourceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateDataSourceRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)<[Google\Cloud\BackupDR\V1beta\DataSource](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DataSource)>` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\BackupDR\V1beta\DataSource;
    use Google\Cloud\BackupDR\V1beta\UpdateDataSourceRequest;
    use Google\Protobuf\FieldMask;
    use Google\Rpc\Status;
    
    /**
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function update_data_source_sample(): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $updateMask = new FieldMask();
        $dataSource = new DataSource();
        $request = (new UpdateDataSourceRequest())
            ->setUpdateMask($updateMask)
            ->setDataSource($dataSource);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $backupDRClient->updateDataSource($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var DataSource $result */
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

The async variant is [BackupDRClient::getLocationAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getLocationAsync__) .

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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
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
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = new GetLocationRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var Location $response */
            $response = $backupDRClient->getLocation($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    

### listLocations

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Location.ListLocationsRequest.html#_Google_Cloud_Location_ListLocationsRequest__getName__) field: * **Global locations** : If `name` is empty, the method lists the public locations available to all projects. * **Project-specific locations** : If `name` follows the format `projects/{project}`, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the `name` field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

The async variant is [BackupDRClient::listLocationsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__listLocationsAsync__) .

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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
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
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = new ListLocationsRequest();
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $backupDRClient->listLocations($request);
    
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

The async variant is [BackupDRClient::getIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__getIamPolicyAsync__) .

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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\Policy;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being requested.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function get_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $request = (new GetIamPolicyRequest())
            ->setResource($resource);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $backupDRClient->getIamPolicy($request);
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

The async variant is [BackupDRClient::setIamPolicyAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__setIamPolicyAsync__) .

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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
    use Google\Cloud\Iam\V1\Policy;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    
    /**
     * @param string $resource REQUIRED: The resource for which the policy is being specified.
     *                         See the operation documentation for the appropriate value for this field.
     */
    function set_iam_policy_sample(string $resource): void
    {
        // Create a client.
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $policy = new Policy();
        $request = (new SetIamPolicyRequest())
            ->setResource($resource)
            ->setPolicy($policy);
    
        // Call the API and handle any network failures.
        try {
            /** @var Policy $response */
            $response = $backupDRClient->setIamPolicy($request);
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

The async variant is [BackupDRClient::testIamPermissionsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Client.BackupDRClient#_Google_Cloud_BackupDR_V1beta_Client_BackupDRClient__testIamPermissionsAsync__) .

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
    use Google\Cloud\BackupDR\V1beta\Client\BackupDRClient;
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
        $backupDRClient = new BackupDRClient();
    
        // Prepare the request message.
        $permissions = [$permissionsElement,];
        $request = (new TestIamPermissionsRequest())
            ->setResource($resource)
            ->setPermissions($permissions);
    
        // Call the API and handle any network failures.
        try {
            /** @var TestIamPermissionsResponse $response */
            $response = $backupDRClient->testIamPermissions($request);
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
    

### createAutoProtectionPolicyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateAutoProtectionPolicyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createAutoProtectionPolicyBindingAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateAutoProtectionPolicyBindingRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createBackupPlanAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateBackupPlanRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createBackupPlanAssociationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateBackupPlanAssociationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createBackupVaultAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateBackupVaultRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### createManagementServerAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\CreateManagementServerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CreateManagementServerRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteAutoProtectionPolicyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteAutoProtectionPolicyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteBackupPlanAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupPlanRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteBackupPlanAssociationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupPlanAssociationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteBackupVaultAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteBackupVaultRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### deleteManagementServerAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\DeleteManagementServerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DeleteManagementServerRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### fetchBackupPlanAssociationsForResourceTypeAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchBackupPlanAssociationsForResourceTypeRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### fetchBackupsForResourceTypeAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchBackupsForResourceTypeRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### fetchDataSourceReferencesForResourceTypeAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchDataSourceReferencesForResourceTypeRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### fetchUsableBackupVaultsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.FetchUsableBackupVaultsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### getAutoProtectionPolicyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetAutoProtectionPolicyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicy](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy)>` |   
  
### getAutoProtectionPolicyBindingAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetAutoProtectionPolicyBindingRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\AutoProtectionPolicyBinding](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding)>` |   
  
### getBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\Backup](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Backup)>` |   
  
### getBackupPlanAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupPlanRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\BackupPlan](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan)>` |   
  
### getBackupPlanAssociationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupPlanAssociationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\BackupPlanAssociation](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation)>` |   
  
### getBackupPlanRevisionAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupPlanRevisionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupPlanRevisionRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\BackupPlanRevision](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanRevision)>` |   
  
### getBackupVaultAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBackupVaultRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\BackupVault](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault)>` |   
  
### getBindingMatchingResourceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetBindingMatchingResourceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetBindingMatchingResourceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\BindingMatchingResource](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingMatchingResource)>` |   
  
### getDataSourceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetDataSourceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetDataSourceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\DataSource](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DataSource)>` |   
  
### getDataSourceReferenceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetDataSourceReferenceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetDataSourceReferenceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\DataSourceReference](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DataSourceReference)>` |   
  
### getManagementServerAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\GetManagementServerRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GetManagementServerRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\BackupDR\V1beta\ManagementServer](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ManagementServer)>` |   
  
### initializeServiceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\InitializeServiceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.InitializeServiceRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### initiateDeleteAutoProtectionPolicyBindingAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\InitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.InitiateDeleteAutoProtectionPolicyBindingRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### listAppliedAutoProtectionPoliciesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListAppliedAutoProtectionPoliciesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listAutoProtectionPoliciesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListAutoProtectionPoliciesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listAutoProtectionPolicyBindingsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListAutoProtectionPolicyBindingsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBackupPlanAssociationsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupPlanAssociationsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBackupPlanRevisionsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupPlanRevisionsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBackupPlansAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupPlansRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupPlansRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBackupVaultsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupVaultsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupVaultsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBackupsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBackupsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBackupsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listBindingMatchingResourcesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListBindingMatchingResourcesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListBindingMatchingResourcesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listDataSourceReferencesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListDataSourceReferencesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListDataSourceReferencesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listDataSourcesAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListDataSourcesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListDataSourcesRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### listManagementServersAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\ListManagementServersRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ListManagementServersRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### restoreBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\RestoreBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.RestoreBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### triggerBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\TriggerBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.TriggerBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateAutoProtectionPolicyAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateAutoProtectionPolicyRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateBackupAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateBackupPlanAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupPlanRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupPlanRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateBackupPlanAssociationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupPlanAssociationRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateBackupVaultAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateBackupVaultRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateBackupVaultRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\OperationResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/OperationResponse.html)>` |   
  
### updateDataSourceAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\BackupDR\V1beta\UpdateDataSourceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.UpdateDataSourceRequest)`   
  
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
  
### static::autoProtectionPolicyName

Formats a string containing the fully-qualified path to represent a auto_protection_policy resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`autoProtectionPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted auto_protection_policy resource.  
  
### static::autoProtectionPolicyBindingName

Formats a string containing the fully-qualified path to represent a auto_protection_policy_binding resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`autoProtectionPolicy` |  `string`   
  
`binding` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted auto_protection_policy_binding resource.  
  
### static::backupName

Formats a string containing the fully-qualified path to represent a backup resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupvault` |  `string`   
  
`datasource` |  `string`   
  
`backup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted backup resource.  
  
### static::backupPlanName

Formats a string containing the fully-qualified path to represent a backup_plan resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupPlan` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted backup_plan resource.  
  
### static::backupPlanAssociationName

Formats a string containing the fully-qualified path to represent a backup_plan_association resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupPlanAssociation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted backup_plan_association resource.  
  
### static::backupPlanRevisionName

Formats a string containing the fully-qualified path to represent a backup_plan_revision resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupPlan` |  `string`   
  
`revision` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted backup_plan_revision resource.  
  
### static::backupVaultName

Formats a string containing the fully-qualified path to represent a backup_vault resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupvault` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted backup_vault resource.  
  
### static::bindingMatchingResourceName

Formats a string containing the fully-qualified path to represent a binding_matching_resource resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`autoProtectionPolicy` |  `string`   
  
`binding` |  `string`   
  
`matchingResource` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted binding_matching_resource resource.  
  
### static::clusterName

Formats a string containing the fully-qualified path to represent a cluster resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
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
  
`ring` |  `string`   
  
`key` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted crypto_key resource.  
  
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
  
### static::dataSourceName

Formats a string containing the fully-qualified path to represent a data_source resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupvault` |  `string`   
  
`datasource` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted data_source resource.  
  
### static::dataSourceReferenceName

Formats a string containing the fully-qualified path to represent a data_source_reference resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataSourceReference` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted data_source_reference resource.  
  
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
  
### static::managementServerName

Formats a string containing the fully-qualified path to represent a management_server resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`managementserver` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted management_server resource.  
  
### static::storagePoolName

Formats a string containing the fully-qualified path to represent a storage_pool resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`zone` |  `string`   
  
`storagePool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted storage_pool resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * autoProtectionPolicy: projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
  * autoProtectionPolicyBinding: projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
  * backup: projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup}
  * backupPlan: projects/{project}/locations/{location}/backupPlans/{backup_plan}
  * backupPlanAssociation: projects/{project}/locations/{location}/backupPlanAssociations/{backup_plan_association}
  * backupPlanRevision: projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}
  * backupVault: projects/{project}/locations/{location}/backupVaults/{backupvault}
  * bindingMatchingResource: projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}
  * cluster: projects/{project}/locations/{location}/clusters/{cluster}
  * cryptoKey: projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}
  * cryptoKeyVersion: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}
  * dataSource: projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}
  * dataSourceReference: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}
  * instance: projects/{project}/instances/{instance}
  * location: projects/{project}/locations/{location}
  * managementServer: projects/{project}/locations/{location}/managementServers/{managementserver}
  * storagePool: projects/{project}/zones/{zone}/storagePools/{storage_pool}



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
