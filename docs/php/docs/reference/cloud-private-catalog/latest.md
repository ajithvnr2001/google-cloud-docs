---
url: https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/
title: Google Cloud Private Catalog for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:16.346821+00:00
---

# Google Cloud Private Catalog for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Private Catalog for PHP Stay organized with collections  Save and categorize content based on your preferences. 

0.7.3 (latest)  0.6.3  0.5.3  0.4.6  0.3.3  0.2.13 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages).

> Idiomatic PHP client for [Google Cloud Private Catalog](https://cloud.google.com/private-catalog).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-private-catalog/v/stable)](https://packagist.org/packages/google/cloud-private-catalog) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-private-catalog.svg)](https://packagist.org/packages/google/cloud-private-catalog)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-private-catalog
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\PrivateCatalog\V1beta1\Client\PrivateCatalogClient;
    use Google\Cloud\PrivateCatalog\V1beta1\Product;
    use Google\Cloud\PrivateCatalog\V1beta1\SearchProductsRequest;
    
    // Create a client.
    $privateCatalogClient = new PrivateCatalogClient();
    
    // Prepare the request message.
    $request = (new SearchProductsRequest())
        ->setResource($resource);
    
    // Call the API and handle any network failures.
    try {
        /** @var PagedListResponse $response */
        $response = $privateCatalogClient->searchProducts($request);
    
        /** @var Product $element */
        foreach ($response as $element) {
            printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
        }
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered beta. As such, it should be expected to be mostly stable and we're working towards a release candidate. We will address issues and requests with a higher priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/private-catalog/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
