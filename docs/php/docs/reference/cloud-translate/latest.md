---
url: https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest/
title: Google Cloud Translation for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:50.210905+00:00
---

# Google Cloud Translation for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Translation for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.3.6 (latest)  2.3.1  2.2.0  2.1.2  2.0.3  1.21.0  1.20.2  1.19.0  1.18.1  1.17.7  1.16.0  1.15.4  1.14.3  1.13.3  1.12.12 

> Idiomatic PHP client for [Translation](https://cloud.google.com/translate/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-translate/v/stable)](https://packagist.org/packages/google/cloud-translate) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-translate.svg)](https://packagist.org/packages/google/cloud-translate)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Dynamically translates text between thousands of language pairs. The Cloud Translation API lets websites and programs integrate with the translation service programmatically. The Google Translation API is part of the larger Cloud Machine Learning API family.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-translate
    

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Translate\V3\AdaptiveMtDataset;
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\GetAdaptiveMtDatasetRequest;
    
    // Create a client.
    $translationServiceClient = new TranslationServiceClient();
    
    // Prepare the request message.
    $request = (new GetAdaptiveMtDatasetRequest())
        ->setName($formattedName);
    
    // Call the API and handle any network failures.
    try {
        /** @var AdaptiveMtDataset $response */
        $response = $translationServiceClient->getAdaptiveMtDataset($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/translation/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/translate/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
