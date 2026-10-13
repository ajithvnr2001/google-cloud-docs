---
url: https://docs.cloud.google.com/php/docs/reference/cloud-text-to-speech/latest/
title: Cloud Text-to-Speech for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:50.017490+00:00
---

# Cloud Text-to-Speech for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-text-to-speech/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Text-to-Speech for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.8.4 (latest)  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.2  2.0.1  1.12.2  1.11.0  1.10.0  1.9.1  1.8.5  1.7.2  1.6.1  1.5.6  1.4.5 

> Idiomatic PHP client for [Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-text-to-speech/v/stable)](https://packagist.org/packages/google/cloud-text-to-speech) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-text-to-speech.svg)](https://packagist.org/packages/google/cloud-text-to-speech)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-text-to-speech
    

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\TextToSpeech\V1\Client\TextToSpeechClient;
    use Google\Cloud\TextToSpeech\V1\ListVoicesRequest;
    use Google\Cloud\TextToSpeech\V1\ListVoicesResponse;
    
    // Create a client.
    $textToSpeechClient = new TextToSpeechClient();
    
    // Prepare the request message.
    $request = new ListVoicesRequest();
    
    // Call the API and handle any network failures.
    try {
        /** @var ListVoicesResponse $response */
        $response = $textToSpeechClient->listVoices($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/text-to-speech/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
