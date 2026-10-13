---
url: https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest/
title: Google Cloud Video Intelligence for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:50.583371+00:00
---

# Google Cloud Video Intelligence for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Video Intelligence for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.3.4 (latest)  2.2.0  2.1.2  2.0.5  1.15.5  1.14.2  1.13.1  1.12.16 

> Idiomatic PHP client for [Cloud Video Intelligence](https://cloud.google.com/video-intelligence/)

[![Latest Stable Version](https://poser.pugx.org/google/cloud-videointelligence/v/stable)](https://packagist.org/packages/google/cloud-videointelligence) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-videointelligence.svg)](https://packagist.org/packages/google/cloud-videointelligence)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Allows developers to use Google video analysis technology as part of their applications. The REST API enables users to annotate videos stored locally or in Google Cloud Storage with contextual information at the level of the entire video, per segment, per shot, and per frame.

**NOTE:** This documentation covers the most recent stable release (V1). There is an additional beta release included in this component. To check out its documentation, see the link below:

  * [VideoIntelligence](https://cloud.google.com/php/docs/reference/cloud-videointelligence/latest))



### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-videointelligence
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoResponse;
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Rpc\Status;
    
    // Create a client.
    $videoIntelligenceServiceClient = new VideoIntelligenceServiceClient();
    
    // Prepare the request message.
    $request = new AnnotateVideoRequest();
    
    // Call the API and handle any network failures.
    try {
        /** @var OperationResponse $response */
        $response = $videoIntelligenceServiceClient->annotateVideo($request);
        $response->pollUntilComplete();
    
        if ($response->operationSucceeded()) {
            /** @var AnnotateVideoResponse $result */
            $result = $response->getResult();
            printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
        } else {
            /** @var Status $error */
            $error = $response->getError();
            printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
        }
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/video-intelligence/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/video/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
