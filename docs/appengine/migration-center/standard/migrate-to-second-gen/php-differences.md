---
url: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/php-differences/
title: Migrate from PHP 5.5 to the latest PHP runtime \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:38.342240+00:00
---

# Migrate from PHP 5.5 to the latest PHP runtime  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/php-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate from PHP 5.5 to the latest PHP runtime Stay organized with collections  Save and categorize content based on your preferences. 

This page covers instructions for migrating from the [first-generation to the second-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) PHP runtimes. To upgrade your second-generation app to use the latest supported version of PHP, see [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/upgrade-php-runtime).

PHP 5 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated). You won't be able to deploy PHP 5 applications, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing PHP 5 applications will continue to run and receive traffic. We recommend that you migrate to the [latest supported version of PHP](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#php).

Migrating to a supported second-generation PHP runtime lets you use up-to-date language features and build apps that are more portable, with idiomatic code.

## Compatibility issues between PHP 5.5 and the second-generation PHP runtimes

The official PHP documentation provides information on migrating from different PHP versions:

  * [Migrating from PHP 5.5.x to PHP 5.6.x](https://php.net/manual/en/migration56.incompatible.php)
  * [Migrating from PHP 5.6.x to PHP 7.0.x](https://php.net/manual/en/migration70.incompatible.php)
  * [Migrating from PHP 7.0.x to PHP 7.1.x](https://php.net/manual/en/migration71.incompatible.php)
  * [Migrating from PHP 7.1.x to PHP 7.2.x](https://php.net/manual/en/migration72.incompatible.php)
  * [Migrating from PHP 7.2.x to PHP 7.3.x](https://php.net/manual/en/migration73.incompatible.php)
  * [Migrating from PHP 7.3.x to PHP 7.4.x](https://php.net/manual/en/migration74.incompatible.php)
  * [Migrating from PHP 7.4.x to PHP 8.0.x](https://php.net/manual/en/migration80.incompatible.php)
  * [Migrating from PHP 8.0.x to PHP 8.1.x](https://php.net/manual/en/migration81.incompatible.php)



## Key differences between PHP 5.5 and the second-generation PHP runtimes

The following is a summary of the differences between the PHP 5.5 and the second-generation PHP runtimes in the App Engine standard environment:

### Memory usage differences

Second-generation runtimes see a higher baseline of memory usage compared to first-generation runtimes. This is due to multiple factors, such as different base image versions, and differences in how the two generations calculate memory usage.

Second-generation runtimes calculate instance memory usage as the sum of what an application process uses, and the number of application files dynamically cached in memory. To avoid memory-intensive applications from experiencing instance shutdowns due to exceeding memory limits, upgrade to a larger [instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) with more memory.

### CPU usage differences

Second-generation runtimes can see a higher baseline of CPU usage upon instance cold-start. Depending on an application's scaling configuration, this might have unintended side effects, such as, a higher instance count than anticipated if an application is configured to scale based on CPU utilization. To avoid this issue, review and test application scaling configurations to ensure the number of instances are acceptable.

### Request header differences

First-generation runtimes allow request headers with underscores (e.g. `X-Test-Foo_bar`) to be forwarded to the application. Second-generation runtimes introduces Nginx into the host architecture. As a result of this change, second-generation runtimes are configured to automatically remove headers with underscores (`_`). To prevent application issues, avoid using underscores in application request headers.

## Migrate your `app.yaml` file

You must place a [front controller](https://wikipedia.org/wiki/Front_controller) to handle all routing in your application. For more information, see [Application startup](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#app_startup).

The second-generation PHP runtimes don't allow the `script` handler element to be customized. The only valid value is `auto`, because all traffic is served using the entrypoint command. All non-static URL handlers must include `script: auto` to deploy successfully.

The behavior of some elements in the `app.yaml` configuration file has been modified:

Element| Change type| Description  
---|---|---  
`entrypoint`| Added|  **Optionally** , use this field to [ specify the command that will run when your app starts](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#application_startup).  
`app_engine_bundled_services`| For apps using legacy bundled services|  Configure this field to access specific [legacy bundled services for supported PHP versions](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/services/access). For more information about the `app_engine_bundled_services` configuration settings, see the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=php#app_engine_bundled_services) file reference.  
`threadsafe`| Deprecated| All applications are presumed to be threadsafe, meaning an instance can handle multiple requests at the same time.  
`api_version`| Deprecated| Previously required but not needed in the second-generation PHP runtimes.  
`application_readable`| Deprecated|   
`builtins`| Deprecated|   
`libraries`| Deprecated| Arbitrary third party dependencies can be installed using a `composer.json` metadata file.  
`handlers`| Modified| 

  * The `script` field is optional and the only accepted value is `auto`. Use a web framework (like [`Laravel`](https://laravel.com), [`Symfony`](http://symfony.com/), [`Slim`](https://www.slimframework.com), or a similar option) with in-app routing to execute a script when a request hits a specific route
  * The `login` field is not supported. Use [Identity and Access Management (IAM)](https://cloud.google.com/iam/docs/) for user management.

  
  
If you use of any of the deprecated fields, there will be an error on app deployment.

For more information, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).

## Reduced runtime restrictions

The second-generation PHP runtimes have fewer restrictions compared to the PHP 5.5 runtime.

  * [Install third-party dependencies](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/specifying-dependencies).
  * The runtime includes a [full filesystem](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#filesystem_2).
  * Create background threads or processes that live beyond the scope of the request while the instance runs.
  * Use the [Google Cloud Client Library for PHP](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.68.0/servicebuilder) to integrate apps with other Google Cloud services. For more information, see the [Installing the Google Cloud Client Library](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/using-php-libraries) page.



For more information, see the [PHP runtime environment](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime).

## Migrate from the App Engine PHP SDK

To reduce runtime migration effort and complexity, the App Engine standard environment lets you [access many of legacy bundled services and APIs in the second-generation PHP runtime](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/services/access), such as Memcache. Your second-generation PHP app can call the bundled services APIs through the App Engine SDK, and access most of the same capabilities as on the PHP 5 runtime. Not all the legacy bundled services available for PHP 5 have a corresponding service in the second-generation PHP runtimes. For the full list of legacy bundled services APIs available for the second-generation PHP runtimes, see the [legacy bundled services API references documentation](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/index.html).

You also have the option to use Google Cloud products that offer similar capabilities as the legacy bundled services. These Google Cloud products provide idiomatic [Google Cloud CLI client library](https://github.com/googlecloudplatform/google-cloud-php). For the legacy bundled services that are not available as separate products in Google Cloud, such as search, you can use third-party providers or other workarounds. To learn more about migrating to unbundled services, see [Migrating from bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).

## Running your application locally

To test your application and run it locally:

  1. Locally install a [version of PHP](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#runtime_version) that corresponds to a second-generation PHP runtime available in the App Engine standard environment.

  2. Install a web server and use this to serve your app locally.




For example, start the HTTP server by running the following command:
    
    
    php -S localhost:8080
    

Then, view your application in your web browser at <http://localhost:8080>.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
