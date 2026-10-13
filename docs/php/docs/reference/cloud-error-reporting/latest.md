---
url: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/
title: Stackdriver Error Reporting for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:07.084048+00:00
---

# Stackdriver Error Reporting for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Stackdriver Error Reporting for PHP Stay organized with collections  Save and categorize content based on your preferences. 

0.27.3 (latest)  0.26.1  0.25.3  0.24.0  0.23.1  0.22.10  0.21.1  0.20.2  0.19.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages).

> Idiomatic PHP client for [Stackdriver Error Reporting](https://cloud.google.com/error-reporting/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-error-reporting/v/stable)](https://packagist.org/packages/google/cloud-error-reporting) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-error-reporting.svg)](https://packagist.org/packages/google/cloud-error-reporting)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Stackdriver Error Reporting counts, analyzes and aggregates the crashes in your running cloud services.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-error-reporting
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\ErrorReporting\V1beta1\Client\ErrorGroupServiceClient;
    use Google\Cloud\ErrorReporting\V1beta1\ErrorGroup;
    use Google\Cloud\ErrorReporting\V1beta1\GetGroupRequest;
    
    // Create a client.
    $errorGroupServiceClient = new ErrorGroupServiceClient();
    
    // Prepare the request message.
    $request = (new GetGroupRequest())
        ->setGroupName($formattedGroupName);
    
    // Call the API and handle any network failures.
    try {
        /** @var ErrorGroup $response */
        $response = $errorGroupServiceClient->getGroup($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered beta. As such, it should be expected to be mostly stable and we're working towards a release candidate. We will address issues and requests with a higher priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/error-reporting/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/error_reporting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
