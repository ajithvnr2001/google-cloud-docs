---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.Client.ProductInputsServiceClient
title: Google Shopping Merchant Products V1beta Client - Class ProductInputsServiceClient (1.8.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:20.525844+00:00
---

# Google Shopping Merchant Products V1beta Client - Class ProductInputsServiceClient (1.8.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.Client.ProductInputsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Products V1beta Client - Class ProductInputsServiceClient (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.5  1.6.0  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Products V1beta Client class ProductInputsServiceClient.

Service Description: Service to use ProductInput resource.

This service works for products with online channel only.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parseName method to extract the individual identifiers contained within formatted names that are returned by the API.

## Namespace

Google \ Shopping \ Merchant \ Products \ V1beta \ Client

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
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Shopping\Merchant\Products\V1beta\ProductInputsServiceClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new ProductInputsServiceClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
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
  
### deleteProductInput

Deletes a product input from your Merchant Center account.

After inserting, updating, or deleting a product input, it may take several minutes before the processed product can be retrieved.

The async variant is [ProductInputsServiceClient::deleteProductInputAsync()](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.Client.ProductInputsServiceClient#_Google_Shopping_Merchant_Products_V1beta_Client_ProductInputsServiceClient__deleteProductInputAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Products\V1beta\DeleteProductInputRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.DeleteProductInputRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Shopping\Merchant\Products\V1beta\Client\ProductInputsServiceClient;
    use Google\Shopping\Merchant\Products\V1beta\DeleteProductInputRequest;
    
    /**
     * @param string $formattedName The name of the product input resource to delete.
     *                              Format: `accounts/{account}/productInputs/{product}`
     *                              where the last section `product` consists of 4 parts:
     *                              `channel~content_language~feed_label~offer_id`
     *                              example for product name is
     *                              `accounts/123/productInputs/online~en~US~sku123`. Please see
     *                              {@see ProductInputsServiceClient::productInputName()} for help formatting this field.
     * @param string $dataSource    The primary or supplemental data source from which the product
     *                              input should be deleted. Format:
     *                              `accounts/{account}/dataSources/{datasource}`. For example,
     *                              `accounts/123456/dataSources/104628`.
     */
    function delete_product_input_sample(string $formattedName, string $dataSource): void
    {
        // Create a client.
        $productInputsServiceClient = new ProductInputsServiceClient();
    
        // Prepare the request message.
        $request = (new DeleteProductInputRequest())
            ->setName($formattedName)
            ->setDataSource($dataSource);
    
        // Call the API and handle any network failures.
        try {
            $productInputsServiceClient->deleteProductInput($request);
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
        $formattedName = ProductInputsServiceClient::productInputName('[ACCOUNT]', '[PRODUCTINPUT]');
        $dataSource = '[DATA_SOURCE]';
    
        delete_product_input_sample($formattedName, $dataSource);
    }
    

### insertProductInput

[Uploads a product input to your Merchant Center account](https://docs.cloud.google.com/merchant/api/guides/products/overview#upload-product-input). You must have a products data source to be able to insert a product. The unique identifier of the data source is passed as a query parameter in the request URL.

If an input with the same contentLanguage, offerId, and dataSource already exists, this method replaces that entry.

After inserting, updating, or deleting a product input, it may take several minutes before the processed product can be retrieved.

The async variant is [ProductInputsServiceClient::insertProductInputAsync()](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.Client.ProductInputsServiceClient#_Google_Shopping_Merchant_Products_V1beta_Client_ProductInputsServiceClient__insertProductInputAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Products\V1beta\InsertProductInputRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.InsertProductInputRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Merchant\Products\V1beta\ProductInput](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductInput)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Shopping\Merchant\Products\V1beta\Client\ProductInputsServiceClient;
    use Google\Shopping\Merchant\Products\V1beta\InsertProductInputRequest;
    use Google\Shopping\Merchant\Products\V1beta\ProductInput;
    
    /**
     * @param string $formattedParent             The account where this product will be inserted.
     *                                            Format: `accounts/{account}`
     *                                            Please see {@see ProductInputsServiceClient::accountName()} for help formatting this field.
     * @param string $productInputOfferId         Immutable. Your unique identifier for the product. This is the
     *                                            same for the product input and processed product. Leading and trailing
     *                                            whitespaces are stripped and multiple whitespaces are replaced by a single
     *                                            whitespace upon submission. See the [products data
     *                                            specification](https://support.google.com/merchants/answer/188494#id) for
     *                                            details.
     * @param string $productInputContentLanguage Immutable. The two-letter [ISO
     *                                            639-1](http://en.wikipedia.org/wiki/ISO_639-1) language code for the
     *                                            product.
     * @param string $productInputFeedLabel       Immutable. The label that lets you categorize and identify your
     *                                            products. The maximum allowed characters are 20, and the supported
     *                                            characters are `A-Z`, `0-9`, hyphen, and underscore. The feed label must
     *                                            not include any spaces. For more information, see [Using feed
     *                                            labels](//support.google.com/merchants/answer/14994087).
     * @param string $dataSource                  The primary or supplemental product data source name. If the
     *                                            product already exists and data source provided is different, then the
     *                                            product will be moved to a new data source. For more information, see
     *                                            [Overview of Data sources
     *                                            sub-API](/merchant/api/guides/data-sources/overview).
     *
     *                                            Only API data sources are supported.
     *
     *                                            Format: `accounts/{account}/dataSources/{datasource}`. For example,
     *                                            `accounts/123456/dataSources/104628`.
     */
    function insert_product_input_sample(
        string $formattedParent,
        string $productInputOfferId,
        string $productInputContentLanguage,
        string $productInputFeedLabel,
        string $dataSource
    ): void {
        // Create a client.
        $productInputsServiceClient = new ProductInputsServiceClient();
    
        // Prepare the request message.
        $productInput = (new ProductInput())
            ->setOfferId($productInputOfferId)
            ->setContentLanguage($productInputContentLanguage)
            ->setFeedLabel($productInputFeedLabel);
        $request = (new InsertProductInputRequest())
            ->setParent($formattedParent)
            ->setProductInput($productInput)
            ->setDataSource($dataSource);
    
        // Call the API and handle any network failures.
        try {
            /** @var ProductInput $response */
            $response = $productInputsServiceClient->insertProductInput($request);
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
        $formattedParent = ProductInputsServiceClient::accountName('[ACCOUNT]');
        $productInputOfferId = '[OFFER_ID]';
        $productInputContentLanguage = '[CONTENT_LANGUAGE]';
        $productInputFeedLabel = '[FEED_LABEL]';
        $dataSource = '[DATA_SOURCE]';
    
        insert_product_input_sample(
            $formattedParent,
            $productInputOfferId,
            $productInputContentLanguage,
            $productInputFeedLabel,
            $dataSource
        );
    }
    

### updateProductInput

Updates the existing product input in your Merchant Center account.

After inserting, updating, or deleting a product input, it may take several minutes before the processed product can be retrieved.

The async variant is [ProductInputsServiceClient::updateProductInputAsync()](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.Client.ProductInputsServiceClient#_Google_Shopping_Merchant_Products_V1beta_Client_ProductInputsServiceClient__updateProductInputAsync__) .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Products\V1beta\UpdateProductInputRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.UpdateProductInputRequest)`   
A request to house fields associated with the call.  
`callOptions` |  `array`   
Optional.  
`↳ retrySettings` |  `[Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html)|array`   
Retry settings to use for this call. Can be a [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) object, or an associative array of retry settings parameters. See the documentation on [Google\ApiCore\RetrySettings](https://docs.cloud.google.com/php/docs/reference/gax/latest/RetrySettings.html) for example usage.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Merchant\Products\V1beta\ProductInput](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductInput)` |   
**Example**
    
    
    use Google\ApiCore\ApiException;
    use Google\Shopping\Merchant\Products\V1beta\Client\ProductInputsServiceClient;
    use Google\Shopping\Merchant\Products\V1beta\ProductInput;
    use Google\Shopping\Merchant\Products\V1beta\UpdateProductInputRequest;
    
    /**
     * @param string $productInputOfferId         Immutable. Your unique identifier for the product. This is the
     *                                            same for the product input and processed product. Leading and trailing
     *                                            whitespaces are stripped and multiple whitespaces are replaced by a single
     *                                            whitespace upon submission. See the [products data
     *                                            specification](https://support.google.com/merchants/answer/188494#id) for
     *                                            details.
     * @param string $productInputContentLanguage Immutable. The two-letter [ISO
     *                                            639-1](http://en.wikipedia.org/wiki/ISO_639-1) language code for the
     *                                            product.
     * @param string $productInputFeedLabel       Immutable. The label that lets you categorize and identify your
     *                                            products. The maximum allowed characters are 20, and the supported
     *                                            characters are `A-Z`, `0-9`, hyphen, and underscore. The feed label must
     *                                            not include any spaces. For more information, see [Using feed
     *                                            labels](//support.google.com/merchants/answer/14994087).
     * @param string $dataSource                  The primary or supplemental product data source where
     *                                            `data_source` name identifies the product input to be updated.
     *
     *                                            Only API data sources are supported.
     *
     *                                            Format: `accounts/{account}/dataSources/{datasource}`. For example,
     *                                            `accounts/123456/dataSources/104628`.
     */
    function update_product_input_sample(
        string $productInputOfferId,
        string $productInputContentLanguage,
        string $productInputFeedLabel,
        string $dataSource
    ): void {
        // Create a client.
        $productInputsServiceClient = new ProductInputsServiceClient();
    
        // Prepare the request message.
        $productInput = (new ProductInput())
            ->setOfferId($productInputOfferId)
            ->setContentLanguage($productInputContentLanguage)
            ->setFeedLabel($productInputFeedLabel);
        $request = (new UpdateProductInputRequest())
            ->setProductInput($productInput)
            ->setDataSource($dataSource);
    
        // Call the API and handle any network failures.
        try {
            /** @var ProductInput $response */
            $response = $productInputsServiceClient->updateProductInput($request);
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
        $productInputOfferId = '[OFFER_ID]';
        $productInputContentLanguage = '[CONTENT_LANGUAGE]';
        $productInputFeedLabel = '[FEED_LABEL]';
        $dataSource = '[DATA_SOURCE]';
    
        update_product_input_sample(
            $productInputOfferId,
            $productInputContentLanguage,
            $productInputFeedLabel,
            $dataSource
        );
    }
    

### deleteProductInputAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Products\V1beta\DeleteProductInputRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.DeleteProductInputRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<void>` |   
  
### insertProductInputAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Products\V1beta\InsertProductInputRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.InsertProductInputRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Shopping\Merchant\Products\V1beta\ProductInput](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductInput)>` |   
  
### updateProductInputAsync

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[Google\Shopping\Merchant\Products\V1beta\UpdateProductInputRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.UpdateProductInputRequest)`   
  
`optionalArgs` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[GuzzleHttp\Promise\PromiseInterface](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-GuzzleHttp.Promise.Promise.html)<[Google\Shopping\Merchant\Products\V1beta\ProductInput](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductInput)>` |   
  
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
  
### static::productInputName

Formats a string containing the fully-qualified path to represent a product_input resource.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`productinput` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | The formatted product_input resource.  
  
### static::parseName

Parses a formatted name string and returns an associative array of the components in the name.

The following name formats are supported: Template: Pattern

  * account: accounts/{account}
  * productInput: accounts/{account}/productInputs/{productinput}



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
