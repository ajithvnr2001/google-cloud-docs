---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/
title: Google Cloud Bigtable for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:31.529491+00:00
---

# Google Cloud Bigtable for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Bigtable for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

> Idiomatic PHP client for [Google Cloud Bigtable](https://cloud.google.com/bigtable/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-bigtable/v/stable)](https://packagist.org/packages/google/cloud-bigtable) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-bigtable.svg)](https://packagist.org/packages/google/cloud-bigtable)

  * [API Documentation](https://cloud.google.com/php/docs/reference/cloud-bigtable/latest)



**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

A high performance NoSQL database service for large analytical and operational workloads.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-bigtable
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Notable Client Differences

The handwritten client offered by this package differs from the others in `google-cloud-php` in that it more directly wraps our generated clients. This means some of the idioms and configuration options you are used to may differ slightly. The most notable differences are outlined below:

  * A key file is now provided through the `credentials` configuration option as opposed to either `keyFile` or `keyFilePath`.
  * There is now more granular control over retry logic. Please see [the `bigtable_client_config.json` file](https://github.com/googleapis/google-cloud-php/blob/main/Bigtable/src/V2/resources/bigtable_client_config.json) for an example of the configuration which can be passed into the client at construction time.
  * Exceptions triggered at the network level utilize the base class `Google\ApiCore\ApiException` as opposed to `Google\Cloud\Core\ServiceException`.
  * The `authHttpHandler` and `httpHandler` client configuration options are now provided through `$credentialsConfig['authHttpHandler']` and `$transportConfig['httpHandler']`, respectively. Additionally, please note the `httpHandler` should now return an implementation of [Guzzle's `PromiseInterface`](https://github.com/guzzle/promises/blob/master/src/PromiseInterface.php).



### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

When going through the authentication guide, please take note that the handwritten client for this package will more closely follow the conventions outlined for the generated clients.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\V2\Client\BigtableClient;
    use Google\Cloud\Bigtable\V2\PingAndWarmRequest;
    use Google\Cloud\Bigtable\V2\PingAndWarmResponse;
    
    // Create a client.
    $bigtableClient = new BigtableClient();
    
    // Prepare the request message.
    $request = (new PingAndWarmRequest())
        ->setName($formattedName);
    
    // Call the API and handle any network failures.
    try {
        /** @var PingAndWarmResponse $response */
        $response = $bigtableClient->pingAndWarm($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

Please see the [migration guide](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/MIGRATING.md) to upgrade from **V1** of the library to **V2**.

### Next Steps

Take a look at and understand the [official documentation](https://cloud.google.com/bigtable/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
