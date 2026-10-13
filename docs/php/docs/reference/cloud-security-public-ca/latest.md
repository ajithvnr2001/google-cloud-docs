---
url: https://docs.cloud.google.com/php/docs/reference/cloud-security-public-ca/latest/
title: Google Cloud Public Certificate Authority for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:20.349260+00:00
---

# Google Cloud Public Certificate Authority for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-security-public-ca/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Public Certificate Authority for PHP Stay organized with collections  Save and categorize content based on your preferences. 

1.2.5 (latest)  1.2.0  1.1.2  1.0.5  0.4.1  0.3.4  0.2.3  0.1.6 

> Idiomatic PHP client for [Google Cloud Public Certificate Authority for PHP](https://cloud.google.com/certificate-manager/docs/public-ca).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-security-public-ca/v/stable)](https://packagist.org/packages/google/cloud-security-public-ca) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-security-public-ca.svg)](https://packagist.org/packages/google/cloud-security-public-ca)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now to install just this component:
    
    
    $ composer require google/cloud-security-public-ca
    

This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Security\PublicCA\V1\Client\PublicCertificateAuthorityServiceClient;
    use Google\Cloud\Security\PublicCA\V1\CreateExternalAccountKeyRequest;
    use Google\Cloud\Security\PublicCA\V1\ExternalAccountKey;
    
    // Create a client.
    $publicCertificateAuthorityServiceClient = new PublicCertificateAuthorityServiceClient();
    
    // Prepare the request message.
    $externalAccountKey = new ExternalAccountKey();
    $request = (new CreateExternalAccountKeyRequest())
        ->setParent($formattedParent)
        ->setExternalAccountKey($externalAccountKey);
    
    // Call the API and handle any network failures.
    try {
        /** @var ExternalAccountKey $response */
        $response = $publicCertificateAuthorityServiceClient->createExternalAccountKey($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/certificate-manager/docs/public-ca).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
