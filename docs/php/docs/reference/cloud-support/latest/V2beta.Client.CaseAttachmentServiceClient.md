---
url: https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Client.CaseAttachmentServiceClient
title: Google Cloud Support V2beta Client - Class CaseAttachmentServiceClient (1.8.5) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:54.680877+00:00
---

# Google Cloud Support V2beta Client - Class CaseAttachmentServiceClient (1.8.5)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Client.CaseAttachmentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Support V2beta Client - Class CaseAttachmentServiceClient (1.8.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.5 (latest)  1.7.0  1.6.0  1.5.0  1.4.2  1.3.0  1.2.1  1.1.0  1.0.3  0.2.5  0.1.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Support V2beta Client class CaseAttachmentServiceClient.

Service Description: A service to manage file attachments for Google Cloud support cases.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Cloud \ Support \ V2beta \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\Support\V2beta\CaseAttachmentServiceClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new CaseAttachmentServiceClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### getAttachment

Retrieve an attachment.

The async variant is [CaseAttachmentServiceClient::getAttachmentAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Client.CaseAttachmentServiceClient#_Google_Cloud_Support_V2beta_Client_CaseAttachmentServiceClient__getAttachmentAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Support\V2beta\GetAttachmentRequest](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.GetAttachmentRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Support\V2beta\Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Support\V2beta\Attachment;
    use Google\Cloud\Support\V2beta\Client\CaseAttachmentServiceClient;
    use Google\Cloud\Support\V2beta\GetAttachmentRequest;
    
    /**
     * @param string $formattedName The name of the attachment to get. Please see
     *                              {@see CaseAttachmentServiceClient::attachmentName()} for help formatting this field.
     */
    function get_attachment_sample(string $formattedName): void
    {
        // Create a client.
        $caseAttachmentServiceClient = new CaseAttachmentServiceClient();
    
        // Prepare the request message.
        $request = (new GetAttachmentRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Attachment $response */
            $response = $caseAttachmentServiceClient->getAttachment($request);
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
        $formattedName = CaseAttachmentServiceClient::attachmentName(
            '[ORGANIZATION]',
            '[CASE]',
            '[ATTACHMENT_ID]'
        );
    
        get_attachment_sample($formattedName);
    }
    

### listAttachments

List all the attachments associated with a support case.

The async variant is [CaseAttachmentServiceClient::listAttachmentsAsync()](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Client.CaseAttachmentServiceClient#_Google_Cloud_Support_V2beta_Client_CaseAttachmentServiceClient__listAttachmentsAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Support\V2beta\ListAttachmentsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.ListAttachmentsRequest)`   
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
    use Google\Cloud\Support\V2beta\Attachment;
    use Google\Cloud\Support\V2beta\Client\CaseAttachmentServiceClient;
    use Google\Cloud\Support\V2beta\ListAttachmentsRequest;
    
    /**
     * @param string $formattedParent The name of the case for which attachments should be listed. Please see
     *                                {@see CaseAttachmentServiceClient::caseName()} for help formatting this field.
     */
    function list_attachments_sample(string $formattedParent): void
    {
        // Create a client.
        $caseAttachmentServiceClient = new CaseAttachmentServiceClient();
    
        // Prepare the request message.
        $request = (new ListAttachmentsRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $caseAttachmentServiceClient->listAttachments($request);
    
            /** @var Attachment $element */
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
        $formattedParent = CaseAttachmentServiceClient::caseName('[ORGANIZATION]', '[CASE]');
    
        list_attachments_sample($formattedParent);
    }
    

### getAttachmentAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Support\V2beta\GetAttachmentRequest](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.GetAttachmentRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Cloud\Support\V2beta\Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)>` |   
  
### listAttachmentsAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Cloud\Support\V2beta\ListAttachmentsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.ListAttachmentsRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)>` |   
  
### static::attachmentName

Formats a string containing the fully-qualified path to represent a attachment resource.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`case` |  `string`   
  
`attachmentId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted attachment resource.  
  
### static::caseName

Formats a string containing the fully-qualified path to represent a case resource.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`case` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted case resource.  
  
### static::organizationCaseName

Formats a string containing the fully-qualified path to represent a organization_case resource.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`case` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted organization_case resource.  
  
### static::organizationCaseAttachmentIdName

Formats a string containing the fully-qualified path to represent a organization_case_attachment_id resource.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`case` |  `string`   
  
`attachmentId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted organization_case_attachment_id resource.  
  
### static::projectCaseName

Formats a string containing the fully-qualified path to represent a project_case resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`case` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted project_case resource.  
  
### static::projectCaseAttachmentIdName

Formats a string containing the fully-qualified path to represent a project_case_attachment_id resource.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`case` |  `string`   
  
`attachmentId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted project_case_attachment_id resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * attachment: organizations/{organization}/cases/{case}/attachments/{attachment_id}
  * case: organizations/{organization}/cases/{case}
  * organizationCase: organizations/{organization}/cases/{case}
  * organizationCaseAttachmentId: organizations/{organization}/cases/{case}/attachments/{attachment_id}
  * projectCase: projects/{project}/cases/{case}
  * projectCaseAttachmentId: projects/{project}/cases/{case}/attachments/{attachment_id}



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
