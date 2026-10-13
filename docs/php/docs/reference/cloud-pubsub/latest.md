---
url: https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/
title: Google Cloud PubSub for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:16.506514+00:00
---

# Google Cloud PubSub for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud PubSub for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.22.1 (latest)  2.19.4  2.18.0  2.17.0  2.16.2  2.15.1  2.14.0  2.13.2  2.12.0  2.11.3  2.10.1  2.9.1  2.8.2  2.7.0  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.2  1.50.0  1.49.0  1.48.0  1.47.0  1.46.5  1.45.2  1.44.0  1.43.2  1.42.1  1.41.3  1.40.1  1.39.3 

> Idiomatic PHP client for [Cloud Pub/Sub](https://cloud.google.com/pubsub/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-pubsub/v/stable)](https://packagist.org/packages/google/cloud-pubsub) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-pubsub.svg)](https://packagist.org/packages/google/cloud-pubsub)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

A fully-managed real-time messaging service that allows you to send and receive messages between independent applications.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-pubsub
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\PubSub\V1\Client\PublisherClient;
    use Google\Cloud\PubSub\V1\GetTopicRequest;
    use Google\Cloud\PubSub\V1\Topic;
    
    // Create a client.
    $publisherClient = new PublisherClient();
    
    // Prepare the request message.
    $request = (new GetTopicRequest())
        ->setTopic($formattedTopic);
    
    // Call the API and handle any network failures.
    try {
        /** @var Topic $response */
        $response = $publisherClient->getTopic($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

Please see the [migration guide](https://docs.cloud.google.com/php/docs/reference/cloud-pubsub/latest/MIGRATING.md) to upgrade from **V1** of the library to **V2**.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/pubsub/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/pubsub/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
