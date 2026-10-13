---
url: https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest/
title: Google Compute for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:03.588764+00:00
---

# Google Compute for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Compute for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.15.0 (latest)  2.14.1  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.1  2.0.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.1  1.21.0  1.20.0  1.19.0  1.18.1  1.17.0  1.16.2  1.14.0  1.13.0  1.12.1  1.11.1  1.10.1  1.9.1  1.8.3  1.7.1  1.6.1  1.5.0 

> Idiomatic PHP client for [Google Compute](https://cloud.google.com/compute/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-compute/v/stable)](https://packagist.org/packages/google/cloud-compute) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-compute.svg)](https://packagist.org/packages/google/cloud-compute)

  * [API Documentation](https://cloud.google.com/php/docs/reference/cloud-compute/latest)



**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Allows you to create, manage, share and query data.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-compute
    

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Compute\V1\AcceleratorType;
    use Google\Cloud\Compute\V1\Client\AcceleratorTypesClient;
    use Google\Cloud\Compute\V1\GetAcceleratorTypeRequest;
    
    // Create a client.
    $acceleratorTypesClient = new AcceleratorTypesClient();
    
    // Prepare the request message.
    $request = (new GetAcceleratorTypeRequest())
        ->setAcceleratorType($acceleratorType)
        ->setProject($project)
        ->setZone($zone);
    
    // Call the API and handle any network failures.
    try {
        /** @var AcceleratorType $response */
        $response = $acceleratorTypesClient->get($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/compute/docs).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/compute).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
