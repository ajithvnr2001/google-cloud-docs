---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc/latest/
title: Google Cloud Dataproc for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:05.268733+00:00
---

# Google Cloud Dataproc for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc for PHP Stay organized with collections  Save and categorize content based on your preferences. 

4.1.3 (latest)  4.0.0  3.14.0  3.13.4  3.12.0  3.11.0  3.10.1  3.9.0  3.8.1  3.7.1  3.6.1  3.5.1  3.4.0  3.3.0  3.2.2  2.12.0  2.11.0  2.10.0  2.9.1  2.8.2  2.7.0  2.6.1  2.5.0  2.3.0  2.2.3  2.1.0  2.0.0 

> Idiomatic PHP client for [Google Cloud Dataproc](https://cloud.google.com/dataproc/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-dataproc/v/stable)](https://packagist.org/packages/google/cloud-dataproc) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-dataproc.svg)](https://packagist.org/packages/google/cloud-dataproc)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

A managed Apache Spark and Apache Hadoop service that lets you take advantage of open source data tools for batch processing, querying, streaming, and machine learning. Cloud Dataproc automation helps you create clusters quickly, manage them easily, and save money by turning clusters off when you don't need them. With less time and money spent on administration, you can focus on your jobs and your data.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-dataproc
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Dataproc\V1\AutoscalingPolicy;
    use Google\Cloud\Dataproc\V1\Client\AutoscalingPolicyServiceClient;
    use Google\Cloud\Dataproc\V1\GetAutoscalingPolicyRequest;
    
    // Create a client.
    $autoscalingPolicyServiceClient = new AutoscalingPolicyServiceClient();
    
    // Prepare the request message.
    $request = (new GetAutoscalingPolicyRequest())
        ->setName($formattedName);
    
    // Call the API and handle any network failures.
    try {
        /** @var AutoscalingPolicy $response */
        $response = $autoscalingPolicyServiceClient->getAutoscalingPolicy($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

Take a look at and understand the [official documentation](https://cloud.google.com/dataproc/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
