---
url: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.ErrorStatsServiceClient
title: Stackdriver Error Reporting V1beta1 Client - Class ErrorStatsServiceClient (0.25.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:22.106138+00:00
---

# Stackdriver Error Reporting V1beta1 Client - Class ErrorStatsServiceClient (0.25.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.ErrorStatsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Stackdriver Error Reporting V1beta1 Client - Class ErrorStatsServiceClient (0.25.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.3 (latest)  0.26.1  0.25.3  0.24.0  0.23.1  0.22.10  0.21.1  0.20.2  0.19.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Stackdriver Error Reporting V1beta1 Client class ErrorStatsServiceClient.

Service Description: An API for retrieving and managing error statistics as well as data for individual events.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
    $errorStatsServiceClient = new ErrorStatsServiceClient();
    try {
        $formattedProjectName = $errorStatsServiceClient->projectName('[PROJECT]');
        $response = $errorStatsServiceClient->deleteEvents($formattedProjectName);
    } finally {
        $errorStatsServiceClient->close();
    }
    

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Cloud \ ErrorReporting \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Optional. Options for configuring the service API wrapper.  
`↳ apiEndpoint` |  `string`   
The address of the API remote host. May optionally include the port, formatted as "  
`↳ credentials` |  `string|array|FetchAuthTokenInterface|CredentialsWrapper`   
The credentials to be used by the client to authorize API calls. This option accepts either a path to a credentials file, or a decoded credentials file as a PHP array. _Advanced usage_ : In addition, this option can also accept a pre-constructed Google\Auth\FetchAuthTokenInterface object or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored.  
`↳ credentialsConfig` |  `array`   
Options used to configure credentials, including auth token caching, for the client. For a full list of supporting configuration options, see [Google\ApiCore\CredentialsWrapper::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html#_Google_ApiCore_CredentialsWrapper__build__) .  
`↳ disableRetries` |  `bool`   
Determines whether or not retries defined by the client configuration should be disabled. Defaults to `false`.  
`↳ clientConfig` |  `string|array`   
Client method configuration, including retry settings. This option can be either a path to a JSON file, or a PHP array containing the decoded JSON data. By default this settings points to the default client config file, which is provided in the resources folder.  
`↳ transport` |  `string|TransportInterface`   
The transport used for executing network requests. May be either the string `rest` or `grpc`. Defaults to `grpc` if gRPC support is detected on the system. _Advanced usage_ : Additionally, it is possible to pass in an already instantiated Google\ApiCore\Transport\TransportInterface object. Note that when this object is provided, any settings in $transportConfig, and any $apiEndpoint setting, will be ignored.  
`↳ transportConfig` |  `array`   
Configuration options that will be used to construct the transport. Options for each supported transport type should be passed in a key for that transport. For example: $transportConfig = [ 'grpc' => [...], 'rest' => [...], ]; See the [Google\ApiCore\Transport\GrpcTransport::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.GrpcTransport.html#_Google_ApiCore_Transport_GrpcTransport__build__) and [Google\ApiCore\Transport\RestTransport::build()](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.RestTransport.html#_Google_ApiCore_Transport_RestTransport__build__) methods for the supported options.  
`↳ clientCertSource` |  `callable`   
A callable which returns the client cert as a string. This can be used to provide a certificate and private key to the transport layer for mTLS.  
  
### deleteEvents

Deletes all error events of a given project.

**Parameters**  
---  
**Name** | **Description**  
`projectName` |  `string`   
Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectID}/locations/{location}`, where `{projectID}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840) and `{location}` is a Cloud region. Examples: `projects/my-project-123`, `projects/my-project-123/locations/global`. For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.  
`optionalArgs` |  `array`   
Optional.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\ErrorReporting\V1beta1\DeleteEventsResponse](https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.DeleteEventsResponse)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\ErrorReporting\V1beta1\Client\ErrorStatsServiceClient;
    use Google\Cloud\ErrorReporting\V1beta1\DeleteEventsRequest;
    use Google\Cloud\ErrorReporting\V1beta1\DeleteEventsResponse;
    
    /**
     * @param string $formattedProjectName The resource name of the Google Cloud Platform project. Written
     *                                     as `projects/{projectID}` or `projects/{projectID}/locations/{location}`,
     *                                     where `{projectID}` is the [Google Cloud Platform project
     *                                     ID](https://support.google.com/cloud/answer/6158840) and `{location}` is
     *                                     a Cloud region.
     *
     *                                     Examples: `projects/my-project-123`,
     *                                     `projects/my-project-123/locations/global`.
     *
     *                                     For a list of supported locations, see [Supported
     *                                     Regions](https://cloud.google.com/logging/docs/region-support). `global` is
     *                                     the default when unspecified. Please see
     *                                     {@see ErrorStatsServiceClient::projectName()} for help formatting this field.
     */
    function delete_events_sample(string $formattedProjectName): void
    {
        // Create a client.
        $errorStatsServiceClient = new ErrorStatsServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteEventsRequest())
            ->setProjectName($formattedProjectName);
    
        // Call the API and handle any network failures.
        try {
            /** @var DeleteEventsResponse $response */
            $response = $errorStatsServiceClient->deleteEvents($request);
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
        $formattedProjectName = ErrorStatsServiceClient::projectName('[PROJECT]');
    
        delete_events_sample($formattedProjectName);
    }
    

### listEvents

Lists the specified events.

**Parameters**  
---  
**Name** | **Description**  
`projectName` |  `string`   
Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectID}/locations/{location}`, where `{projectID}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840) and `{location}` is a Cloud region. Examples: `projects/my-project-123`, `projects/my-project-123/locations/global`. For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.  
`groupId` |  `string`   
Required. The group for which events shall be returned. The `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).  
`optionalArgs` |  `array`   
Optional.  
`↳ serviceFilter` |  `ServiceContextFilter`   
Optional. List only ErrorGroups which belong to a service context that matches the filter. Data for all service contexts is returned if this field is not specified.  
`↳ timeRange` |  `QueryTimeRange`   
Optional. List only data for the given time range. If not set a default time range is used. The field time_range_begin in the response will specify the beginning of this time range.  
`↳ pageSize` |  `int`   
The maximum number of resources contained in the underlying API response. The API may return fewer values in a page, even if there are additional values to be retrieved.  
`↳ pageToken` |  `string`   
A page token is used to specify a page of values to be returned. If no page token is specified (the default), the first page of values will be returned. Any page token used here must have been generated by a previous call to the API.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\ErrorReporting\V1beta1\Client\ErrorStatsServiceClient;
    use Google\Cloud\ErrorReporting\V1beta1\ErrorEvent;
    use Google\Cloud\ErrorReporting\V1beta1\ListEventsRequest;
    
    /**
     * @param string $formattedProjectName The resource name of the Google Cloud Platform project. Written
     *                                     as `projects/{projectID}` or `projects/{projectID}/locations/{location}`,
     *                                     where `{projectID}` is the [Google Cloud Platform project
     *                                     ID](https://support.google.com/cloud/answer/6158840) and `{location}` is
     *                                     a Cloud region.
     *
     *                                     Examples: `projects/my-project-123`,
     *                                     `projects/my-project-123/locations/global`.
     *
     *                                     For a list of supported locations, see [Supported
     *                                     Regions](https://cloud.google.com/logging/docs/region-support). `global` is
     *                                     the default when unspecified. Please see
     *                                     {@see ErrorStatsServiceClient::projectName()} for help formatting this field.
     * @param string $groupId              The group for which events shall be returned.
     *                                     The `group_id` is a unique identifier for a particular error group. The
     *                                     identifier is derived from key parts of the error-log content and is
     *                                     treated as Service Data. For information about how Service Data
     *                                     is handled, see [Google Cloud Privacy
     *                                     Notice](https://cloud.google.com/terms/cloud-privacy-notice).
     */
    function list_events_sample(string $formattedProjectName, string $groupId): void
    {
        // Create a client.
        $errorStatsServiceClient = new ErrorStatsServiceClient();
    
        // Prepare the request message.
        $request = (new ListEventsRequest())
            ->setProjectName($formattedProjectName)
            ->setGroupId($groupId);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $errorStatsServiceClient->listEvents($request);
    
            /** @var ErrorEvent $element */
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
        $formattedProjectName = ErrorStatsServiceClient::projectName('[PROJECT]');
        $groupId = '[GROUP_ID]';
    
        list_events_sample($formattedProjectName, $groupId);
    }
    

### listGroupStats

Lists the specified groups.

**Parameters**  
---  
**Name** | **Description**  
`projectName` |  `string`   
Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectNumber}`, where `{projectID}` and `{projectNumber}` can be found in the [Google Cloud console](https://support.google.com/cloud/answer/6158840). It may also include a location, such as `projects/{projectID}/locations/{location}` where `{location}` is a cloud region. Examples: `projects/my-project-123`, `projects/5551234`, `projects/my-project-123/locations/us-central1`, `projects/5551234/locations/us-central1`. For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified. Use `-` as a wildcard to request group stats from all regions.  
`optionalArgs` |  `array`   
Optional.  
`↳ groupId` |  `string[]`   
Optional. List all [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] with these IDs. The `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).  
`↳ serviceFilter` |  `ServiceContextFilter`   
Optional. List only [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] which belong to a service context that matches the filter. Data for all service contexts is returned if this field is not specified.  
`↳ timeRange` |  `QueryTimeRange`   
Optional. List data for the given time range. If not set, a default time range is used. The field [time_range_begin] [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsResponse.time_range_begin] in the response will specify the beginning of this time range. Only [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] with a non-zero count in the given time range are returned, unless the request contains an explicit [group_id] [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsRequest.group_id] list. If a [group_id] [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsRequest.group_id] list is given, also [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] with zero occurrences are returned.  
`↳ timedCountDuration` |  `Duration`   
Optional. The preferred duration for a single returned [TimedCount] [google.devtools.clouderrorreporting.v1beta1.TimedCount]. If not set, no timed counts are returned.  
`↳ alignment` |  `int`   
Optional. The alignment of the timed counts to be returned. Default is `ALIGNMENT_EQUAL_AT_END`. For allowed values, use constants defined on [Google\Cloud\ErrorReporting\V1beta1\TimedCountAlignment](https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.TimedCountAlignment)  
`↳ alignmentTime` |  `Timestamp`   
Optional. Time where the timed counts shall be aligned if rounded alignment is chosen. Default is 00:00 UTC.  
`↳ order` |  `int`   
Optional. The sort order in which the results are returned. Default is `COUNT_DESC`. For allowed values, use constants defined on [Google\Cloud\ErrorReporting\V1beta1\ErrorGroupOrder](https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.ErrorGroupOrder)  
`↳ pageSize` |  `int`   
The maximum number of resources contained in the underlying API response. The API may return fewer values in a page, even if there are additional values to be retrieved.  
`↳ pageToken` |  `string`   
A page token is used to specify a page of values to be returned. If no page token is specified (the default), the first page of values will be returned. Any page token used here must have been generated by a previous call to the API.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\PagedListResponse](https://docs.cloud.google.com/php/docs/reference/gax/latest/PagedListResponse.html)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\ErrorReporting\V1beta1\Client\ErrorStatsServiceClient;
    use Google\Cloud\ErrorReporting\V1beta1\ErrorGroupStats;
    use Google\Cloud\ErrorReporting\V1beta1\ListGroupStatsRequest;
    
    /**
     * @param string $formattedProjectName The resource name of the Google Cloud Platform project. Written
     *                                     as `projects/{projectID}` or `projects/{projectNumber}`, where
     *                                     `{projectID}` and `{projectNumber}` can be found in the
     *                                     [Google Cloud console](https://support.google.com/cloud/answer/6158840).
     *                                     It may also include a location, such as
     *                                     `projects/{projectID}/locations/{location}` where `{location}` is a cloud
     *                                     region.
     *
     *                                     Examples: `projects/my-project-123`, `projects/5551234`,
     *                                     `projects/my-project-123/locations/us-central1`,
     *                                     `projects/5551234/locations/us-central1`.
     *
     *                                     For a list of supported locations, see [Supported
     *                                     Regions](https://cloud.google.com/logging/docs/region-support). `global` is
     *                                     the default when unspecified. Use `-` as a wildcard to request group stats
     *                                     from all regions. Please see
     *                                     {@see ErrorStatsServiceClient::projectName()} for help formatting this field.
     */
    function list_group_stats_sample(string $formattedProjectName): void
    {
        // Create a client.
        $errorStatsServiceClient = new ErrorStatsServiceClient();
    
        // Prepare the request message.
        $request = (new ListGroupStatsRequest())
            ->setProjectName($formattedProjectName);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $errorStatsServiceClient->listGroupStats($request);
    
            /** @var ErrorGroupStats $element */
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
        $formattedProjectName = ErrorStatsServiceClient::projectName('[PROJECT]');
    
        list_group_stats_sample($formattedProjectName);
    }
    

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

  * project: projects/{project}



The optional $template argument can be supplied to specify a particular pattern, and must match one of the templates listed above. If no $template argument is provided, or if the $template argument does not match one of the templates listed, then parseName will check each of the supported templates, and return the first match.

**Parameters**  
---  
**Name** | **Description**  
`formattedName` |  `string`   
The formatted name string  
`template` |  `string`   
Optional name of template to match  
**Returns**  
---  
**Type** | **Description**  
`array` | An associative array from name component IDs to component values.  
  
## Constants 

### SERVICE_NAME
    
    
    Value: 'google.devtools.clouderrorreporting.v1beta1.ErrorStatsService'

The name of the service.

### SERVICE_ADDRESS
    
    
    Value: 'clouderrorreporting.googleapis.com'

The default address of the service.

### DEFAULT_SERVICE_PORT
    
    
    Value: 443

The default port of the service.

### CODEGEN_NAME
    
    
    Value: 'gapic'

The name of the code generator, to be included in the agent header.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
