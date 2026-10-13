---
url: https://docs.cloud.google.com/php/docs/reference/cloud-document-ai/latest/
title: Google Cloud Document Ai for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:06.751565+00:00
---

# Google Cloud Document Ai for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-document-ai/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Document Ai for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.8.3 (latest)  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.2  2.1.3  2.0.0  1.14.0  1.13.1  1.12.2  1.9.0  1.8.2  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.1  1.0.1 

> Idiomatic PHP client for [Google Cloud Document Ai](https://cloud.google.com/document-ai).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-document-ai/v/stable)](https://packagist.org/packages/google/cloud-document-ai) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-document-ai.svg)](https://packagist.org/packages/google/cloud-document-ai)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-document-ai
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\DocumentAI\V1\Client\DocumentProcessorServiceClient;
    use Google\Cloud\DocumentAI\V1\Evaluation;
    use Google\Cloud\DocumentAI\V1\GetEvaluationRequest;
    
    // Create a client.
    $documentProcessorServiceClient = new DocumentProcessorServiceClient();
    
    // Prepare the request message.
    $request = (new GetEvaluationRequest())
        ->setName($formattedName);
    
    // Call the API and handle any network failures.
    try {
        /** @var Evaluation $response */
        $response = $documentProcessorServiceClient->getEvaluation($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/document-ai/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
