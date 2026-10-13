---
url: https://docs.cloud.google.com/php/docs/reference/cloud-debugger/latest/
title: Google PHP Stackdriver Debugger \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:05.812896+00:00
---

# Google PHP Stackdriver Debugger  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-debugger/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google PHP Stackdriver Debugger Stay organized with collections  Save and categorize content based on your preferences. 

1.9.5 (latest)  1.9.4  1.8.8  1.7.0  1.6.4  1.5.1  1.4.16 

> Idiomatic PHP client for [Stackdriver Debugger](https://cloud.google.com/debugger/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-debugger/v/stable)](https://packagist.org/packages/google/cloud-debugger) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-debugger.svg)](https://packagist.org/packages/google/cloud-debugger)

**IMPORTANT** : This library has been deprecated. See [Cloud Debugger Deprecation](https://cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

A feature of Google Cloud Platform that lets you inspect the state of an application, at any code location, without stopping or slowing down the running app. Stackdriver Debugger makes it easier to view the application state without adding logging statements.

### Installation

  1. Install the PHP extension from PECL.
         
         $ pecl install stackdriver_debugger-alpha
         

On Windows, you can download pre-built .dll files [from PECL](https://pecl.php.net/package/stackdriver_debugger).

You may also need to enable the extension in your `php.ini` file:
         
         # on Unix
         extension=stackdriver_debugger.so
         
         # on Windows
         extension=php_stackdriver_debugger.dll
         

  2. Install with `composer` or add to your `composer.json`.
         
         $ composer require google/cloud-debugger
         

  3. Run the batch daemon script in the background.

On Unix-based systems that have [semaphore extensions](http://php.net/manual/en/book.sem.php) installed, run the [BatchDaemon](https://github.com/googleapis/google-cloud-php/blob/main/Core/src/Batch/BatchDaemon.php):
         
         $ vendor/bin/google-cloud-batch daemon
         

On Windows or systems that do not have [semaphore extensions](http://php.net/manual/en/book.sem.php) installed, run the Debugger [Daemon](https://cloud.google.com/php/docs/reference/debugger/latest/Daemon):
         
         $ vendor/bin/google-cloud-debugger -s <SOURCE_ROOT>
         

The `SOURCE_ROOT` is the base location of your deployed application.

Alternatively, you can provide a configuration script:
         
         $ vendor/bin/google-cloud-debugger -c <CONFIG_FILE>
         

  4. Include and start the debugger `Agent` as the first action in your application:
         
         $agent = new Google\Cloud\Debugger\Agent();
         

If this file is not in your source root, you will need to provide the path to your application's source root as an optional parameter:
         
         $agent = new Google\Cloud\Debugger\Agent([
             'sourceRoot' => '/path/to/source/root'
         ]);
         




This component supports both REST over HTTP/1.1 and gRPC. In order to take advantage of the benefits offered by gRPC (such as streaming methods) please see our [gRPC installation guide](https://cloud.google.com/php/grpc).

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\Cloud\Debugger\DebuggerClient;
    
    $debugger = new DebuggerClient();
    $debuggee = $debugger->debugee();
    $debuggee->register();
    

### Configuration

#### Snapshots

Debugger snapshots allow you to capture and inspect the call stack and local variables in your application without stopping or slowing it down. In general, you will set breakpoints via the Stackdriver Debugger UI in the [Cloud Platform Console](https://console.cloud.google.com/debug).

See [Using Debug Snapshots](https://cloud.google.com/debugger/docs/debugging) for more information on snapshots.

#### Logpoints

Debugger logpoints allow you to inject logging into running services without restarting or interfering with the normal function of the service. This can be useful for debugging production issues without having to add log statements and redeploy.

By default, we will send all log messages to Stackdriver Logging, but you can customize this by providing any PSR-3 compatible logger. For example, to use `monolog`:
    
    
    $agent = new Google\Cloud\Debugger\Agent([
        'logger' => new Monolog\Logger('name')
    ]);
    

See [Using Debug Logpoints](https://cloud.google.com/debugger/docs/logpoints) for more information on logpoints.

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/debugger/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/debugger).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
