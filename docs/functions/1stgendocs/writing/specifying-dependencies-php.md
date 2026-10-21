---
url: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-php/
title: Specify dependencies in PHP \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:32.375348+00:00
---

# Specify dependencies in PHP  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-php/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Specify dependencies in PHP

You use [Composer](https://getcomposer.org/) to manage dependencies in PHP.

## Installing Composer

If you don't already have Composer installed, you can do so as follows:

  1. [Download Composer](https://getcomposer.org/download/) to any location you desire.

  2. Once it is downloaded, move the `composer.phar` file to a directory that is in your system path, for example:
         
         mv composer.phar /usr/local/bin/composer
         




## Creating a `composer.json` file

The `composer.json` file lists your function's dependencies. You can either create it by hand, or you can run the following command:
    
    
    composer init
    

When you run this command, it interactively asks you to fill in the fields, while offering some smart defaults.

## Declaring dependencies

To declare dependencies, add a `composer.json` file containing dependencies to your function code directory. In this example, we require the [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-php) and add a `start` script:
    
    
    {
        "require": {
            "php": ">= 8.1",
            "google/cloud-functions-framework": "^1.1"
        },
        "scripts": {
            "start": [
               "Composer\\Config::disableProcessTimeout",
               "FUNCTION_TARGET=helloHttp php -S localhost:${PORT:-8080} vendor/google/cloud-functions-framework/router.php"
            ]
        }
    }

Note that scripts defined in your [`composer.json` file](https://getcomposer.org/doc/articles/scripts.md) will not run when Composer can use a cached result.

## Add Functions Framework as a dependency

The Cloud Run functions PHP runtime requires the Functions Framework to be an explicit dependency. To add Functions Framework as a dependency, run the following command in the directory containing your function code (this directory must also contain the `composer.json` file):
    
    
    composer require google/cloud-functions-framework
    

This adds the Functions Framework to your `composer.json` and installs the package in the `vendor/` directory.

### `autoload.php` file

One of the files contained in your `vendor/` directory is `autoload.php`.

Add the following line to the top of your PHP scripts to require the `autoload.php` file, which automatically `require`s your function's other dependencies:
    
    
    require_once __DIR__ . '/vendor/autoload.php';
    

By default, the `vendor/` directory is ignored in the generated [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file to reduce the number of files sent in deployment.

## Updating dependencies

To update your function's dependencies and the `composer.lock` file, use the [`update` command](https://getcomposer.org/doc/03-cli.md#update-u):
    
    
    composer update
    

This resolves all dependencies of the project and writes their exact versions into `composer.lock`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
