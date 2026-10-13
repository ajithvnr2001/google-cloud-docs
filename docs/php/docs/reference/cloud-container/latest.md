---
url: https://docs.cloud.google.com/php/docs/reference/cloud-container/latest/
title: Google Cloud Container for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:04.308063+00:00
---

# Google Cloud Container for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-container/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Container for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.12.3 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.4  2.2.1  2.1.0  2.0.0  1.33.0  1.32.0  1.31.0  1.30.3  1.24.0  1.23.0  1.22.0  1.21.1  1.20.0  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.0  1.13.1  1.12.1  1.10.3  1.9.1 

> Idiomatic PHP client for [Google Cloud Container](https://cloud.google.com/kubernetes-engine/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-container/v/stable)](https://packagist.org/packages/google/cloud-container) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-container.svg)](https://packagist.org/packages/google/cloud-container)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Kubernetes Engine is a managed, production-ready environment for deploying containerized applications. It brings our latest innovations in developer productivity, resource efficiency, automated operations, and open source flexibility to accelerate your time to market.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-container
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Container\V1\Client\ClusterManagerClient;
    use Google\Cloud\Container\V1\Cluster;
    use Google\Cloud\Container\V1\GetClusterRequest;
    
    // Create a client.
    $clusterManagerClient = new ClusterManagerClient();
    
    // Prepare the request message.
    $request = new GetClusterRequest();
    
    // Call the API and handle any network failures.
    try {
        /** @var Cluster $response */
        $response = $clusterManagerClient->getCluster($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

Take a look at and understand the [official documentation](https://cloud.google.com/kubernetes-engine/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
