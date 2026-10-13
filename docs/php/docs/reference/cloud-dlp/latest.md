---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dlp/latest/
title: Data Loss Prevention for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:06.463406+00:00
---

# Data Loss Prevention for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dlp/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Data Loss Prevention for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.15.2 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.2  2.8.1  2.7.0  2.6.1  2.4.1  2.3.0  2.2.3  2.1.0  2.0.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.1  1.14.0  1.13.2  1.12.0  1.11.0  1.10.2  1.9.0  1.8.6 

> Idiomatic PHP client for [Google DLP](https://cloud.google.com/dlp/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-dlp/v/stable)](https://packagist.org/packages/google/cloud-dlp) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-dlp.svg)](https://packagist.org/packages/google/cloud-dlp)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

The DLP API lets you understand and manage sensitive data.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-dlp
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ColumnDataProfile;
    use Google\Cloud\Dlp\V2\GetColumnDataProfileRequest;
    
    // Create a client.
    $dlpServiceClient = new DlpServiceClient();
    
    // Prepare the request message.
    $request = (new GetColumnDataProfileRequest())
        ->setName($formattedName);
    
    // Call the API and handle any network failures.
    try {
        /** @var ColumnDataProfile $response */
        $response = $dlpServiceClient->getColumnDataProfile($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/dlp/docs).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/dlp).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
