---
url: https://docs.cloud.google.com/php/docs/reference/cloud-language/latest/
title: Google Cloud PHP Natural Language \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:09.854551+00:00
---

# Google Cloud PHP Natural Language  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-language/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud PHP Natural Language Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.1  1.1.4  1.0.1  0.34.3  0.33.0  0.32.7  0.31.3  0.30.2  0.29.0  0.28.5 

> Idiomatic PHP client for [Cloud Natural Language](https://cloud.google.com/natural-language/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-language/v/stable)](https://packagist.org/packages/google/cloud-language) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-language.svg)](https://packagist.org/packages/google/cloud-language)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Provides natural language understanding technologies to developers, including sentiment analysis, entity analysis, entity sentiment analysis, content classification, and syntax analysis. This API is part of the larger Cloud Machine Learning API family.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-language
    

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Language\V2\AnalyzeSentimentRequest;
    use Google\Cloud\Language\V2\AnalyzeSentimentResponse;
    use Google\Cloud\Language\V2\Client\LanguageServiceClient;
    use Google\Cloud\Language\V2\Document;
    
    // Create a client.
    $languageServiceClient = new LanguageServiceClient();
    
    // Prepare the request message.
    $document = new Document();
    $request = (new AnalyzeSentimentRequest())
        ->setDocument($document);
    
    // Call the API and handle any network failures.
    try {
        /** @var AnalyzeSentimentResponse $response */
        $response = $languageServiceClient->analyzeSentiment($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/natural-language/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/language).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
