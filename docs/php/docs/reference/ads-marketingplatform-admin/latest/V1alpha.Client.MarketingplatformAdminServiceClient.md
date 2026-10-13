---
url: https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Client.MarketingplatformAdminServiceClient
title: Google Ads Marketing Platform Admin V1alpha Client - Class MarketingplatformAdminServiceClient (0.1.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:17.703139+00:00
---

# Google Ads Marketing Platform Admin V1alpha Client - Class MarketingplatformAdminServiceClient (0.1.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Client.MarketingplatformAdminServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Ads Marketing Platform Admin V1alpha Client - Class MarketingplatformAdminServiceClient (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Ads Marketing Platform Admin V1alpha Client class MarketingplatformAdminServiceClient.

Service Description: Service Interface for the Google Marketing Platform Admin API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Ads \ MarketingPlatform \ Admin \ V1alpha \ Client

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
The credentials to be used by the client to authorize API calls. This option accepts either a path to a credentials file, or a decoded credentials file as a PHP array. _Advanced usage_ : In addition, this option can also accept a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://googleapis.github.io/google-auth-library-php/main/Google/Auth/FetchAuthTokenInterface) object or [Google\ApiCore\CredentialsWrapper](https://googleapis.github.io/gax-php#Google/ApiCore/CredentialsWrapper) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored.  
`↳ credentialsConfig` |  `array`   
Options used to configure credentials, including auth token caching, for the client. For a full list of supporting configuration options, see [Google\ApiCore\CredentialsWrapper::build()](https://googleapis.github.io/gax-php#Google/ApiCore/CredentialsWrapper#method_build) .  
`↳ disableRetries` |  `bool`   
Determines whether or not retries defined by the client configuration should be disabled. Defaults to `false`.  
`↳ clientConfig` |  `string|array`   
Client method configuration, including retry settings. This option can be either a path to a JSON file, or a PHP array containing the decoded JSON data. By default this settings points to the default client config file, which is provided in the resources folder.  
`↳ transport` |  `string|TransportInterface`   
The transport used for executing network requests. May be either the string `rest` or `grpc`. Defaults to `grpc` if gRPC support is detected on the system. _Advanced usage_ : Additionally, it is possible to pass in an already instantiated [Google\ApiCore\Transport\TransportInterface](https://googleapis.github.io/gax-php#Google/ApiCore/Transport/TransportInterface) object. Note that when this object is provided, any settings in $transportConfig, and any $apiEndpoint setting, will be ignored.  
`↳ transportConfig` |  `array`   
Configuration options that will be used to construct the transport. Options for each supported transport type should be passed in a key for that transport. For example: $transportConfig = [ 'grpc' => [...], 'rest' => [...], ]; See the [Google\ApiCore\Transport\GrpcTransport::build()](https://googleapis.github.io/gax-php#Google/ApiCore/Transport/GrpcTransport#method_build) and [Google\ApiCore\Transport\RestTransport::build()](https://googleapis.github.io/gax-php#Google/ApiCore/Transport/RestTransport#method_build) methods for the supported options.  
`↳ clientCertSource` |  `callable`   
A callable which returns the client cert as a string. This can be used to provide a certificate and private key to the transport layer for mTLS.  
  
### createAnalyticsAccountLink

Creates the link between the Analytics account and the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

The async variant is [Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient::createAnalyticsAccountLinkAsync()](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Client.MarketingplatformAdminServiceClient#_Google_Ads_MarketingPlatform_Admin_V1alpha_Client_MarketingplatformAdminServiceClient__createAnalyticsAccountLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\CreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.CreateAnalyticsAccountLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Ads\MarketingPlatform\Admin\V1alpha\AnalyticsAccountLink](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.AnalyticsAccountLink)` |   
**Example**
    
    
    use Google\Ads\MarketingPlatform\Admin\V1alpha\AnalyticsAccountLink;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\CreateAnalyticsAccountLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedParent                               The parent resource where this Analytics account link will be
     *                                                              created. Format: organizations/{org_id}
     *                                                              Please see {@see MarketingplatformAdminServiceClient::organizationName()} for help formatting this field.
     * @param string $formattedAnalyticsAccountLinkAnalyticsAccount Immutable. The resource name of the AnalyticsAdmin API account.
     *                                                              The account ID will be used as the ID of this AnalyticsAccountLink
     *                                                              resource, which will become the final component of the resource name.
     *
     *                                                              Format: analyticsadmin.googleapis.com/accounts/{account_id}
     *                                                              Please see {@see MarketingplatformAdminServiceClient::accountName()} for help formatting this field.
     */
    function create_analytics_account_link_sample(
        string $formattedParent,
        string $formattedAnalyticsAccountLinkAnalyticsAccount
    ): void {
        // Create a client.
        $marketingplatformAdminServiceClient = new MarketingplatformAdminServiceClient();
    
        // Prepare the request message.
        $analyticsAccountLink = (new AnalyticsAccountLink())
            ->setAnalyticsAccount($formattedAnalyticsAccountLinkAnalyticsAccount);
        $request = (new CreateAnalyticsAccountLinkRequest())
            ->setParent($formattedParent)
            ->setAnalyticsAccountLink($analyticsAccountLink);
    
        // Call the API and handle any network failures.
        try {
            /** @var AnalyticsAccountLink $response */
            $response = $marketingplatformAdminServiceClient->createAnalyticsAccountLink($request);
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
        $formattedParent = MarketingplatformAdminServiceClient::organizationName('[ORGANIZATION]');
        $formattedAnalyticsAccountLinkAnalyticsAccount = MarketingplatformAdminServiceClient::accountName(
            '[ACCOUNT]'
        );
    
        create_analytics_account_link_sample(
            $formattedParent,
            $formattedAnalyticsAccountLinkAnalyticsAccount
        );
    }
    

### deleteAnalyticsAccountLink

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account in order to delete the link.

The async variant is [Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient::deleteAnalyticsAccountLinkAsync()](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Client.MarketingplatformAdminServiceClient#_Google_Ads_MarketingPlatform_Admin_V1alpha_Client_MarketingplatformAdminServiceClient__deleteAnalyticsAccountLinkAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\DeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.DeleteAnalyticsAccountLinkRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) for example usage.  
**Example**
    
    
    use Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\DeleteAnalyticsAccountLinkRequest;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the Analytics account link to delete.
     *                              Format:
     *                              organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}
     *                              Please see {@see MarketingplatformAdminServiceClient::analyticsAccountLinkName()} for help formatting this field.
     */
    function delete_analytics_account_link_sample(string $formattedName): void
    {
        // Create a client.
        $marketingplatformAdminServiceClient = new MarketingplatformAdminServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteAnalyticsAccountLinkRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            $marketingplatformAdminServiceClient->deleteAnalyticsAccountLink($request);
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
        $formattedName = MarketingplatformAdminServiceClient::analyticsAccountLinkName(
            '[ORGANIZATION]',
            '[ANALYTICS_ACCOUNT_LINK]'
        );
    
        delete_analytics_account_link_sample($formattedName);
    }
    

### getOrganization

Lookup for a single organization.

The async variant is [Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient::getOrganizationAsync()](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Client.MarketingplatformAdminServiceClient#_Google_Ads_MarketingPlatform_Admin_V1alpha_Client_MarketingplatformAdminServiceClient__getOrganizationAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\GetOrganizationRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.GetOrganizationRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Ads\MarketingPlatform\Admin\V1alpha\Organization](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Organization)` |   
**Example**
    
    
    use Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\GetOrganizationRequest;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\Organization;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $formattedName The name of the Organization to retrieve.
     *                              Format: organizations/{org_id}
     *                              Please see {@see MarketingplatformAdminServiceClient::organizationName()} for help formatting this field.
     */
    function get_organization_sample(string $formattedName): void
    {
        // Create a client.
        $marketingplatformAdminServiceClient = new MarketingplatformAdminServiceClient();
    
        // Prepare the request message.
        $request = (new GetOrganizationRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var Organization $response */
            $response = $marketingplatformAdminServiceClient->getOrganization($request);
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
        $formattedName = MarketingplatformAdminServiceClient::organizationName('[ORGANIZATION]');
    
        get_organization_sample($formattedName);
    }
    

### listAnalyticsAccountLinks

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

The async variant is [Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient::listAnalyticsAccountLinksAsync()](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Client.MarketingplatformAdminServiceClient#_Google_Ads_MarketingPlatform_Admin_V1alpha_Client_MarketingplatformAdminServiceClient__listAnalyticsAccountLinksAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.ListAnalyticsAccountLinksRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\ApiCore\PagedListResponse](https://googleapis.github.io/gax-php#Google/ApiCore/PagedListResponse)` |   
**Example**
    
    
    use Google\Ads\MarketingPlatform\Admin\V1alpha\AnalyticsAccountLink;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\ListAnalyticsAccountLinksRequest;
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    
    /**
     * @param string $formattedParent The parent organization, which owns this collection of Analytics
     *                                account links. Format: organizations/{org_id}
     *                                Please see {@see MarketingplatformAdminServiceClient::organizationName()} for help formatting this field.
     */
    function list_analytics_account_links_sample(string $formattedParent): void
    {
        // Create a client.
        $marketingplatformAdminServiceClient = new MarketingplatformAdminServiceClient();
    
        // Prepare the request message.
        $request = (new ListAnalyticsAccountLinksRequest())
            ->setParent($formattedParent);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $marketingplatformAdminServiceClient->listAnalyticsAccountLinks($request);
    
            /** @var AnalyticsAccountLink $element */
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
        $formattedParent = MarketingplatformAdminServiceClient::organizationName('[ORGANIZATION]');
    
        list_analytics_account_links_sample($formattedParent);
    }
    

### setPropertyServiceLevel

Updates the service level for an Analytics property.

The async variant is [Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient::setPropertyServiceLevelAsync()](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.Client.MarketingplatformAdminServiceClient#_Google_Ads_MarketingPlatform_Admin_V1alpha_Client_MarketingplatformAdminServiceClient__setPropertyServiceLevelAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\SetPropertyServiceLevelRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.SetPropertyServiceLevelRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `RetrySettings|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://googleapis.github.io/gax-php#Google/ApiCore/RetrySettings) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Ads\MarketingPlatform\Admin\V1alpha\SetPropertyServiceLevelResponse](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.SetPropertyServiceLevelResponse)` |   
**Example**
    
    
    use Google\Ads\MarketingPlatform\Admin\V1alpha\AnalyticsServiceLevel;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\Client\MarketingplatformAdminServiceClient;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\SetPropertyServiceLevelRequest;
    use Google\Ads\MarketingPlatform\Admin\V1alpha\SetPropertyServiceLevelResponse;
    use Google\ApiCore\ApiException;
    
    /**
     * @param string $analyticsAccountLink       The parent AnalyticsAccountLink scope where this property is in.
     *                                           Format:
     *                                           organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}
     * @param string $formattedAnalyticsProperty The Analytics property to change the ServiceLevel setting. This
     *                                           field is the name of the Google Analytics Admin API property resource.
     *
     *                                           Format: analyticsadmin.googleapis.com/properties/{property_id}
     *                                           Please see {@see MarketingplatformAdminServiceClient::propertyName()} for help formatting this field.
     * @param int    $serviceLevel               The service level to set for this property.
     */
    function set_property_service_level_sample(
        string $analyticsAccountLink,
        string $formattedAnalyticsProperty,
        int $serviceLevel
    ): void {
        // Create a client.
        $marketingplatformAdminServiceClient = new MarketingplatformAdminServiceClient();
    
        // Prepare the request message.
        $request = (new SetPropertyServiceLevelRequest())
            ->setAnalyticsAccountLink($analyticsAccountLink)
            ->setAnalyticsProperty($formattedAnalyticsProperty)
            ->setServiceLevel($serviceLevel);
    
        // Call the API and handle any network failures.
        try {
            /** @var SetPropertyServiceLevelResponse $response */
            $response = $marketingplatformAdminServiceClient->setPropertyServiceLevel($request);
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
        $analyticsAccountLink = '[ANALYTICS_ACCOUNT_LINK]';
        $formattedAnalyticsProperty = MarketingplatformAdminServiceClient::propertyName('[PROPERTY]');
        $serviceLevel = AnalyticsServiceLevel::ANALYTICS_SERVICE_LEVEL_UNSPECIFIED;
    
        set_property_service_level_sample(
            $analyticsAccountLink,
            $formattedAnalyticsProperty,
            $serviceLevel
        );
    }
    

### createAnalyticsAccountLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\CreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.CreateAnalyticsAccountLinkRequest)`   
  
`optionalArgs = []` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`GuzzleHttp\Promise\PromiseInterface` |   
  
### deleteAnalyticsAccountLinkAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\DeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.DeleteAnalyticsAccountLinkRequest)`   
  
`optionalArgs = []` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`GuzzleHttp\Promise\PromiseInterface` |   
  
### getOrganizationAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\GetOrganizationRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.GetOrganizationRequest)`   
  
`optionalArgs = []` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`GuzzleHttp\Promise\PromiseInterface` |   
  
### listAnalyticsAccountLinksAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.ListAnalyticsAccountLinksRequest)`   
  
`optionalArgs = []` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`GuzzleHttp\Promise\PromiseInterface` |   
  
### setPropertyServiceLevelAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Ads\MarketingPlatform\Admin\V1alpha\SetPropertyServiceLevelRequest](https://docs.cloud.google.com/php/docs/reference/ads-marketingplatform-admin/latest/V1alpha.SetPropertyServiceLevelRequest)`   
  
`optionalArgs = []` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`GuzzleHttp\Promise\PromiseInterface` |   
  
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
  
### static::analyticsAccountLinkName

Formats a string containing the fully-qualified path to represent a analytics_account_link resource.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`analyticsAccountLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted analytics_account_link resource.  
  
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
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * account: accounts/{account}
  * analyticsAccountLink: organizations/{organization}/analyticsAccountLinks/{analytics_account_link}
  * organization: organizations/{organization}
  * property: properties/{property}



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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
