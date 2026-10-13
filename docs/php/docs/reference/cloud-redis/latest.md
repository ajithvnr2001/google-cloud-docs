---
url: https://docs.cloud.google.com/php/docs/reference/cloud-redis/latest/
title: Google Cloud Redis for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:17.449836+00:00
---

# Google Cloud Redis for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-redis/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Redis for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.3  2.1.6  2.0.0  1.9.5  1.8.4  1.7.0  1.6.12 

> Idiomatic PHP client for [Google Cloud Redis](https://cloud.google.com/memorystore/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-redis/v/stable)](https://packagist.org/packages/google/cloud-redis) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-redis.svg)](https://packagist.org/packages/google/cloud-redis)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

A fully managed Redis service for the Google Cloud Platform. Applications running on Google Cloud Platform can achieve extreme performance by leveraging the highly scalable, available, secure Redis service without the burden of managing complex Redis deployments.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-redis
    

This component requires the gRPC extension. Please see our [gRPC installation guide](https://cloud.google.com/php/grpc) for more information on how to configure the extension.

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Redis\V1\Client\CloudRedisClient;
    use Google\Cloud\Redis\V1\GetInstanceRequest;
    use Google\Cloud\Redis\V1\Instance;
    
    // Create a client.
    $cloudRedisClient = new CloudRedisClient();
    
    // Prepare the request message.
    $request = (new GetInstanceRequest())
        ->setName($formattedName);
    
    // Call the API and handle any network failures.
    try {
        /** @var Instance $response */
        $response = $cloudRedisClient->getInstance($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

Take a look at and understand the [official documentation](https://cloud.google.com/memorystore/docs/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
