---
url: https://docs.cloud.google.com/run/docs/runtimes/php/
title: The PHP runtime \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:55.907130+00:00
---

# The PHP runtime  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/php/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  The PHP runtime Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Run function runs in an environment consisting of an operating system version with add-on packages, language support, and the [PHP Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-php) library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime ID.

## Function preparation

You can prepare a function directly from the Google Cloud console or write it on your local machine and upload it. To prepare your local machine for PHP development, see [Use PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

## Supported PHP runtimes and base images

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
PHP 8.5 | php85 |  google-24-full (default)  |  [google-24-full/php85](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/php85) | 2029-12-31 | 2030-06-30  
PHP 8.4 | php84 |  google-22-full (default)  |  [google-22-full/php84](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php84) | 2028-12-31 | 2029-06-30  
PHP 8.3 | php83 |  google-22-full (default)  |  [google-22-full/php83](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php83) | 2027-12-31 | 2028-06-30  
PHP 8.2 | php82 |  google-22-full (default)  |  [google-22-full/php82](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php82) | 2026-12-31 | 2027-06-30  
PHP 8.1 | php81 |  google-18-full  |  [google-18-full/php81](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php81) | 2025-12-31 | 2026-06-30  
PHP 7.4 | php74 |  google-18-full  |  [google-18-full/php74](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php74) | 2024-01-30 | 2025-01-30  
  
## Select your runtime

You can select one of the supported PHP runtimes for your function during deployment. 

You can select a runtime version using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice:

###  gcloud 

Specify the [PHP base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) for your function using the `--base-image` flag, while deploying your function. For example:
    
    
    gcloud run deploy FUNCTION \
        --source . \
        --function FUNCTION_ENTRYPOINT \
        --base-image php85
    

Replace:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For detailed instructions on deploying a function using the gcloud CLI, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud).

###  Console 

You can select a runtime version when you create or update a Cloud Run function in the Google Cloud console. For detailed instructions on deploying a function, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#deploy-functions).

To select a runtime in the Google Cloud console when you create a function, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Write a function**.

  3. In the **Runtime** list, select a PHP runtime version.

  4. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  5. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.




For detailed instructions on updating the runtime version after your function is deployed, see [Re-deploy new source code](https://docs.cloud.google.com/run/docs/deploy-functions#update-code-functions).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions#php) for more information.

## PHP Configuration

You configure your PHP function with a [`php.ini` file](https://www.php.net/manual/en/configuration.file.php) in your function's root directory. You can view existing PHP configuration settings with the [`phpinfo()`](https://www.php.net/manual/en/function.phpinfo.php) function as shown in the following code sample:
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function phpInfoDemo(ServerRequestInterface $request): string
    {
        // phpinfo() displays its output directly in the function's
        // HTTP response, so we don't need to explicitly return it
        //
        // Note: we recommend deleting the deployed Cloud Function once you no
        // longer need it, as phpinfo() may broadcast potential security issues.
        phpinfo();
        return '';
    }
    

## Specifying dependencies

PHP uses Composer to manage dependencies. You specify dependencies for your function by adding the dependencies to a project file called `composer.json`.

The Cloud Run functions PHP runtime requires the Functions Framework to be an explicit dependency. To add Functions Framework as a dependency, run the following command in the directory containing your function code (this directory must also contain the `composer.json` file):
    
    
    composer require google/cloud-functions-framework
    

This adds the Functions Framework to your `composer.json` and installs the package in the `vendor/` directory.

### `autoload.php` file

One of the files contained in your `vendor/` directory is `autoload.php`.

Add the following line to the top of your PHP scripts to require the `autoload.php` file, which automatically `require`s your function's other dependencies:
    
    
    require_once __DIR__ . '/vendor/autoload.php';
    

By default, the `vendor/` directory is ignored in the generated [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file to reduce the number of files sent in deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
