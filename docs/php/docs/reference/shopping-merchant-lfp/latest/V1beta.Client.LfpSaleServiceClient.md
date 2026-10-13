---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.Client.LfpSaleServiceClient
title: Google Shopping Merchant Lfp V1beta Client - Class LfpSaleServiceClient (1.2.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:10.154756+00:00
---

# Google Shopping Merchant Lfp V1beta Client - Class LfpSaleServiceClient (1.2.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.Client.LfpSaleServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Lfp V1beta Client - Class LfpSaleServiceClient (1.2.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.6 (latest)  1.2.1  1.1.3  1.0.0  0.4.0  0.3.2  0.2.0  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Lfp V1beta Client class LfpSaleServiceClient.

Service Description: Service for a [LFP partner](https://support.google.com/merchants/answer/7676652) to submit sales data for a merchant.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Shopping \ Merchant \ Lfp \ V1beta \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Shopping\Merchant\Lfp\V1beta\LfpSaleServiceClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new LfpSaleServiceClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### insertLfpSale

Inserts a `LfpSale` for the given merchant.

The async variant is [LfpSaleServiceClient::insertLfpSaleAsync()](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.Client.LfpSaleServiceClient#_Google_Shopping_Merchant_Lfp_V1beta_Client_LfpSaleServiceClient__insertLfpSaleAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Lfp\V1beta\InsertLfpSaleRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.InsertLfpSaleRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Merchant\Lfp\V1beta\LfpSale](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpSale)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Protobuf\Timestamp;
    use Google\Shopping\Merchant\Lfp\V1beta\Client\LfpSaleServiceClient;
    use Google\Shopping\Merchant\Lfp\V1beta\InsertLfpSaleRequest;
    use Google\Shopping\Merchant\Lfp\V1beta\LfpSale;
    use Google\Shopping\Type\Price;
    
    /**
     * @param string $parent                 The LFP provider account.
     *                                       Format: `accounts/{lfp_partner}`
     * @param int    $lfpSaleTargetAccount   The Merchant Center ID of the merchant to submit the sale for.
     * @param string $lfpSaleStoreCode       The identifier of the merchant's store. Either a `storeCode`
     *                                       inserted through the API or the code of the store in the Business Profile.
     * @param string $lfpSaleOfferId         A unique identifier for the product. If both inventories and
     *                                       sales are submitted for a merchant, this id should match for the same
     *                                       product.
     *
     *                                       **Note**: if the merchant sells the same product new and used, they should
     *                                       have different IDs.
     * @param string $lfpSaleRegionCode      The [CLDR territory
     *                                       code](https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml)
     *                                       for the country where the product is sold.
     * @param string $lfpSaleContentLanguage The two-letter ISO 639-1 language code for the item.
     * @param string $lfpSaleGtin            The Global Trade Item Number of the sold product.
     * @param int    $lfpSaleQuantity        The relative change of the available quantity. Negative for items
     *                                       returned.
     */
    function insert_lfp_sale_sample(
        string $parent,
        int $lfpSaleTargetAccount,
        string $lfpSaleStoreCode,
        string $lfpSaleOfferId,
        string $lfpSaleRegionCode,
        string $lfpSaleContentLanguage,
        string $lfpSaleGtin,
        int $lfpSaleQuantity
    ): void {
        // Create a client.
        $lfpSaleServiceClient = new LfpSaleServiceClient();
    
        // Prepare the request message.
        $lfpSalePrice = new Price();
        $lfpSaleSaleTime = new Timestamp();
        $lfpSale = (new LfpSale())
            ->setTargetAccount($lfpSaleTargetAccount)
            ->setStoreCode($lfpSaleStoreCode)
            ->setOfferId($lfpSaleOfferId)
            ->setRegionCode($lfpSaleRegionCode)
            ->setContentLanguage($lfpSaleContentLanguage)
            ->setGtin($lfpSaleGtin)
            ->setPrice($lfpSalePrice)
            ->setQuantity($lfpSaleQuantity)
            ->setSaleTime($lfpSaleSaleTime);
        $request = (new InsertLfpSaleRequest())
            ->setParent($parent)
            ->setLfpSale($lfpSale);
    
        // Call the API and handle any network failures.
        try {
            /** @var LfpSale $response */
            $response = $lfpSaleServiceClient->insertLfpSale($request);
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
        $parent = '[PARENT]';
        $lfpSaleTargetAccount = 0;
        $lfpSaleStoreCode = '[STORE_CODE]';
        $lfpSaleOfferId = '[OFFER_ID]';
        $lfpSaleRegionCode = '[REGION_CODE]';
        $lfpSaleContentLanguage = '[CONTENT_LANGUAGE]';
        $lfpSaleGtin = '[GTIN]';
        $lfpSaleQuantity = 0;
    
        insert_lfp_sale_sample(
            $parent,
            $lfpSaleTargetAccount,
            $lfpSaleStoreCode,
            $lfpSaleOfferId,
            $lfpSaleRegionCode,
            $lfpSaleContentLanguage,
            $lfpSaleGtin,
            $lfpSaleQuantity
        );
    }
    

### insertLfpSaleAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Lfp\V1beta\InsertLfpSaleRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.InsertLfpSaleRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Shopping\Merchant\Lfp\V1beta\LfpSale](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpSale)>` |   
  
### static::lfpSaleName

Formats a string containing the fully-qualified path to represent a lfp_sale resource.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`sale` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted lfp_sale resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * lfpSale: accounts/{account}/lfpSales/{sale}



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
