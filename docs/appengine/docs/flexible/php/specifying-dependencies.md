---
url: https://docs.cloud.google.com/appengine/docs/flexible/php/specifying-dependencies/
title: Specifying dependencies \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:35.054913+00:00
---

# Specifying dependencies  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/php/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Specifying dependencies Stay organized with collections  Save and categorize content based on your preferences. 

You can declare dependencies for PHP in a standard [`composer.json`](https://getcomposer.org/doc/01-basic-usage.md#composer-json-project-setup) file. For example:
    
    
    {
        "require": {
            "google/cloud": "^0.72"
        }
    }
    

You can use any Linux-compatible PHP package in App Engine. The runtime looks for a [`composer.json`](https://getcomposer.org/doc/01-basic-usage.md#composer-json-project-setup) file in your application's source directory and uses [`composer`](https://getcomposer.org) to install any dependencies before starting your application.

For information about the PHP versions that are supported in this runtime, see [The PHP Runtime](https://docs.cloud.google.com/appengine/docs/flexible/php/runtime).

## Installing and running locally

Use [composer](https://getcomposer.org) to install your dependencies locally:
    
    
    composer install
    

To pin your dependencies to their current version, commit the [`composer.lock`](https://getcomposer.org/doc/01-basic-usage.md#commit-your-composer-lock-file-to-version-control) file to your application.

You can test your application using your web server of choice. App Engine flexible environment uses [NGINX](https://www.nginx.com/resources/wiki/start/index.html) in production. To quickly run your application, you can use [PHP's built-in web server](http://php.net/manual/en/features.commandline.webserver.php).

## Installing a web framework

By default, NGINX is configured to serve all requests through `index.php`. A framework is not required, but is encouraged. You can use any web framework with App Engine flexible environments, including the following:

  * [Symfony](https://symfony.com/)
  * [Laravel](https://laravel.com/)
  * [CodeIgniter](https://www.codeigniter.com/)
  * [WordPress](https://wordpress.com/)
  * [Drupal](https://drupal.com/)
  * [Joomla!](https://www.joomla.com/)



To use a particular web framework, just add it to `composer.json`:
    
    
    {
        "require": {
            "symfony/symfony": " ^3.0"
        }
    }
    

## Installing the Cloud Client Libraries

The [Google Cloud Client Library for PHP](https://googleapis.github.io/google-cloud-php/#/) is a client library for accessing Google Cloud services that reduces the boilerplate code you have to write. The library provides high-level, easy to understand API abstractions. It embraces idioms of PHP, works well with the standard library, and has tighter integration with your codebase. All of this means you spend more time creating code that matters to you.

  1. Install the library locally:
         
         composer require google/cloud
         

  2. You can handle authentication locally by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). If you want your local application to temporarily use your own user credentials for API access, run:
         
         gcloud auth application-default login
         

For details on configuring Cloud Client Libraries for PHP to handle authentication automatically, see [Authenticate to Cloud services using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).




## Using private repositories

To use libraries in private repositories, you must complete the following tasks:

  * Configure the repository.
  * Give `composer` the secret to access the private repository.



The following example illustrates how to access a private repository in GitHub.

  1. Configure the repository in `composer.json` using `vcs` for the type:
         
         "repositories": [
             {
                 "type": "vcs",
                 "url": "https://github.com/username/private_package"
             }
         ]
         

  2. Create a file named `auth.json` in your project root directory:
         
         {
             "github-oauth": {
                 "github.com": "<your-github-auth-token>"
             }
         }
         




You can obtain the GitHub auth token from GitHub's administrative UI.

Here is another example that illustrates how to access a private repository for Bitbucket.

  1. Configure the repository in `composer.json` using `vcs` for the type:
         
         "repositories": [
             {
                 "type": "vcs",
                 "url":  "https://bitbucket.org/username/private_git"
             }
         ]
         

  2. Create a file named `auth.json` in your project root directory:
         
         {
             "bitbucket-oauth": {
                 "bitbucket.org": {
                     "consumer-key": "<your-oauth-consumer-key>",
                     "consumer-secret": "<your-oauth-consumer-secret>"
                 }
             }
         }
         


**Note:** Since the `auth.json` file contains secrets, you should configure `document_root` to point to a subdirectory in your project root so your secret isn't publicly served.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
