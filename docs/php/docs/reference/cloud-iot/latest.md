---
url: https://docs.cloud.google.com/php/docs/reference/cloud-iot/latest/
title: Google Cloud IoT Core for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:11.166523+00:00
---

# Google Cloud IoT Core for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-iot/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud IoT Core for PHP Stay organized with collections  Save and categorize content based on your preferences. 

1.7.5 (latest)  1.7.4  1.6.4  1.5.12 

> Idiomatic PHP client for [Google Cloud IoT Core](https://cloud.google.com/iot-core/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-iot/v/stable)](https://packagist.org/packages/google/cloud-iot) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-iot.svg)](https://packagist.org/packages/google/cloud-iot)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

A fully managed service for securely connecting and managing IoT devices, from a few to millions. Ingest data from connected devices and build rich applications that integrate with the other big data services of Google Cloud Platform.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-iot
    

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    require 'vendor/autoload.php';
    
    use Google\Cloud\Iot\V1\DeviceManagerClient;
    
    $deviceManager = new DeviceManagerClient();
    
    $projectId = '[MY_PROJECT_ID]';
    $location = 'us-central1';
    $registryId = '[MY_REGISTRY_ID]';
    $registryName = $deviceManager->registryName($projectId, $location, $registryId);
    $devices = $deviceManager->listDevices($registryName);
    foreach ($devices->iterateAllElements() as $device) {
        printf('Device: %s : %s' . PHP_EOL,
            $device->getNumId(),
            $device->getId()
        );
    }
    

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/iot/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/iot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
