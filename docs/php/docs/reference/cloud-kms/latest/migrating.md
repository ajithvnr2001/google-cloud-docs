---
url: https://docs.cloud.google.com/php/docs/reference/cloud-kms/latest/migrating/
title: Migrating Google Cloud Clients to the New Surface \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:15.367553+00:00
---

# Migrating Google Cloud Clients to the New Surface  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-kms/latest/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Migrating Google Cloud Clients to the New Surface Stay organized with collections  Save and categorize content based on your preferences. 

2.13.1 (latest)  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.0  2.3.1  2.2.0  2.1.6  2.0.0  1.23.0  1.22.1  1.21.4  1.20.3  1.19.0  1.18.1  1.17.0  1.16.4  1.15.3 

**Document Summary**

  * Google Cloud PHP Client Libraries are releasing new major versions (v2) to introduce new surface changes.
  * The PHP Team at Google has developed a tool to automatically upgrade clients (see [`ClientUpgradeFixer`](https://github.com/GoogleCloudPlatform/php-tools/blob/main/src/Fixers/ClientUpgradeFixer/README.md)).



## WHAT are the new Cloud Clients?

The new Cloud Clients are in the namespace `\Client\`, whereas the previous clients are one directory above with the same name. For example:
    
    
    // This is the "new" client
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    
    // This is the deprecated client (marked with @deprecated)
    use Google\Cloud\Kms\V1\KeyManagementServiceClient;
    

The main difference is that RPC methods which used to take a varying number of required arguments plus an array of optional arguments, now only take a _single_ `Request` object:
    
    
    // Create a client.
    $keyManagementServiceClient = new KeyManagementServiceClient();
    
    // Prepare the request message.
    $request = new GetLocationRequest();
    
    // Call the API and handle any network failures.
    try {
        /** @var Location $response */
        $response = $keyManagementServiceClient->getLocation($request);
        printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
    

### RPCs use CallOptions

The new surface RPC methods take an optional array of [CallOptions](https://github.com/googleapis/gax-php/blob/main/src/Options/CallOptions.php) as the second argument. These are similar to how the `$optionalArgs` were used in the previous surface, but the new `CallOptions` _only_ contain options for the call itself, whereas the previous `$optionalArgs` also held the optional fields for the request body:
    
    
    // To set call-time options, such as headers, timeouts, and retry options,
    // pass them in as the second argument
    $callOptions = ['timeoutMillis' => 20];
    $response = $keyManagementServiceClient->getLocation($request, $callOptions);
    

### Requests have static `::build` methods

Using Request objects directly can make it more difficult to quickly draft out the necessary code to deliver an RPC. To mitigate this friction, a static `::build` method is now generated when one or more [method signature annotations](https://google.aip.dev/client-libraries/4232) exist on the RPC.

Any request which has recommended parameters defined in its proto will include a `::build` method, so that these parameters are easily discoverable:
    
    
    // Create the RPC request using the static "::build" method
    $request = ListInfoTypesRequest::build($parent);
    $response = $keyManagementServiceClient->getLocation($request);
    

## HOW should I upgrade?

The changes are mostly straightforward, and at a minimum require the following:

  * Update Google Cloud clients to use the new client namespace by appending `\Client` to the existing namespace.
  * Update RPC calls to accept the corresponding `Request` object.



**NOTE** : Client streaming calls do not require a `Request` object.

### Automatically upgrade code using the `ClientUpgradeFixer` tool

To help migrate code to the new client surface, we've written a [ClientUpgradeFixer](https://github.com/GoogleCloudPlatform/php-tools/blob/main/src/Fixers/ClientUpgradeFixer/README.md) to scan code and upgrade it to match the new client surface. This tool is not guaranteed to work, so be sure to test everything that it changes thoroughly. Read more about how to install and run the tool in its [README](https://github.com/GoogleCloudPlatform/php-tools/blob/main/src/Fixers/ClientUpgradeFixer/README.md).

The ClientUpgradeFixer uses [PHP Coding Standards Fixer](https://cs.symfony.com/) to upgrade code to use the new client surface:
    
    
    # run the CS fixer for that directory using the config above
    vendor/bin/php-cs-fixer fix --config=.php-cs-fixer.google.php --dry-run --diff /path/to/my/project
    

This will output a diff of the changes. Remove `--dry-run` from the above command to apply the changes automatically.
    
    
    -use Google\Cloud\Dlp\V2\DlpServiceClient;
    +use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    +use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
     use Google\Cloud\Dlp\V2\InspectConfig;
     use Google\Cloud\Dlp\V2\InspectJobConfig;
     use Google\Cloud\Dlp\V2\Likelihood;
    +use Google\Cloud\Dlp\V2\ListInfoTypesRequest;
     use Google\Cloud\Dlp\V2\StorageConfig;
    
     // Instantiate a client.
     $dlp = new DlpServiceClient();
    
     // optional args array (variable)
    -$infoTypes = $dlp->listInfoTypes($parent);
    +$request = (new ListInfoTypesRequest());
    +$infoTypes = $dlp->listInfoTypes($request);
    
     // optional args array (inline array)
    -$job = $dlp->createDlpJob($parent, ['jobId' => 'abc', 'locationId' => 'def']);
    +$request2 = (new CreateDlpJobRequest())
    +    ->setParent($parent)
    +    ->setJobId('abc')
    +    ->setLocationId('def');
    +$job = $dlp->createDlpJob($request2);
    

## Feedback

Your feedback is important to us! Please continue to provide us with any thoughts and questions in the [Issues](https://github.com/googleapis/google-cloud-php/issues) section of this repository.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
