---
url: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/services/access/
title: Access legacy bundled services for PHP \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:09.766193+00:00
---

# Access legacy bundled services for PHP  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/services/access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Access legacy bundled services for PHP Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to install and use the bundled services with the [PHP runtime](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime) for the App Engine standard environment. Your app can access the bundled services through the **App Engine services SDK for PHP**.

## Before you begin

  1. Refer to the [list of legacy bundled services APIs](https://docs.cloud.google.com/appengine/docs/standard/services/overview?tab=php) you can call in the PHP runtime.

  2. Update your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=php#app_engine_bundled_services) file to specify one or more legacy bundled services. For example:
         
         app_engine_bundled_services:
         - memcache
         - urlfetch
         

  3. To test your PHP app, you must deploy it using [`gcloud app deploy`](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/building-app#deploy-app).




## Install the PHP App Engine SDK

You can find the PHP App Engine SDK on GitHub at [`appengine-php-sdk`](https://github.com/GoogleCloudPlatform/appengine-php-sdk). You must use version 2.1 or later for PHP 8.1+ and version 2.0.1 or later for PHP 7.x.

There are two ways to incorporate the SDK into your project:

  1. Execute the [Packagist](https://packagist.org/packages/google/appengine-php-sdk) command to add the SDK to your `composer.json` file:
         
         composer require google/appengine-php-sdk
         

  2. Manually create a `composer.json` file with the following details:

### PHP 7/8
         
         {
             "require": {
                 "google/appengine-php-sdk": "^2.1" // Or any later version
             }
         }
         




In PHP, App Engine APIs require explicit dependency specification. See [this](https://cloud.google.com/appengine/docs/standard/php-gen2/specifying-dependencies) doc for instructions on how to include `autoload.php`.

## Importing the libraries

Use the `use` operator to import the class you need from the list of [Available APIs](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/index.html). For example, `Google\AppEngine\Api\AppIdentity\ClassName` can be imported with the statement:
    
    
    use Google\AppEngine\Api\AppIdentity\ClassName;
    

## Migration considerations

### App Identity

You do not need to make changes to your app's configuration when upgrading to PHP. The behavior, features, and setup instructions for the App Identity API remain the same. Refer to the [API Identity Overview](https://docs.cloud.google.com/appengine/docs/standard/services/appidentity) and the [App Identity API reference guide](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/Google/AppEngine/Api/AppIdentity.html) for more details.

### Mail

The PHP [Mail API](https://docs.cloud.google.com/appengine/docs/standard/services/mail) remains mostly the same as the PHP 5 Mail API, with some slight differences on how to enable and disable the Mail services. The following sections cover the differences between both runtimes.

#### Message class

In PHP, the `Message` class works the same as it did in PHP 5.5, except the `use` imports have been updated. The differences are as follows:

### PHP 5.5
    
    
    use google\appengine\api\mail\Message;
    

### PHP 7/8
    
    
    use Google\AppEngine\Api\Mail\Message;
    

If you are unable to change the import statements, the original PHP 5.5 import statement will also work for PHP.

#### Mail function

In PHP 5.5, the native PHP [`mail()`](https://www.php.net/manual/en/function.mail.php) function was overloaded by [App Engine's Mail function](https://docs.cloud.google.com/appengine/docs/standard/services/mail/sending-mail-with-mail-api?tab=php#sending_mail_2).

In PHP, the App Engine Mail function is no longer overloaded by default, and must be explicitly enabled. This new behavior lets you repurpose the Mail function to better suit your needs. This change also allows you to have visibility into which implementation is currently being used for all Mail function calls.

If you prefer using the native PHP `mail()` function to send mail using the App Engine Mail API, you can enable it in your `php.ini` file as follows:
    
    
    extension = mailparse.so
    sendmail_path = "php ./vendor/google/appengine-php-sdk/src/Runtime/SendMail.php -t -i"
    

As shown in the preceding example, add the mailparse extension to enable the native PHP mail function, and set the `sendmail_path` runtime configuration to the App Engine Mail function implementation. After enabling this, all calls to `mail()` will work exactly as they did in PHP 5.5.

Reference the [Sending mail](https://docs.cloud.google.com/appengine/docs/standard/services/mail) and [Receiving mail](https://docs.cloud.google.com/appengine/docs/standard/services/mail/receiving-mail-with-mail-api) guides, and the [Mail API reference guide](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/Google/AppEngine/Api/Mail.html) for more details.

### Memcache

To use Memcache for PHP, you need to add an explicit declaration of the Memcache libraries. Previously, Memcache for PHP 5.5 did not require an explicit declaration. This explicit declaration enables flexibility to switch between the native PHP Memcache and the App Engine Memcache.

PHP Memcache classes have the same behavior as PHP 5 Memcache classes, with the exception of the explicit declaration. Refer to the [Memcache Overview](https://docs.cloud.google.com/appengine/docs/standard/services/memcache) for more details.

### PHP 5.5

Memcache for PHP 5.5 example:
    
    
    $memcache = new Memcache();
    return $memcache->get($key);
    

Memcached for PHP 5.5 example:
    
    
    $memcache = new Memcached();
    $memcache->set('who', $request->get('who'));
    return $twig->render('memcache.html.twig', [
        'who' => $request->get('who'),
        'count' => $memcache->increment('count', 1, 0),
        'host' => $request->getHost(),
    ]);
    

### PHP 7/8

Memcache API for PHP example:
    
    
    use Google\AppEngine\Api\Memcache\Memcache;
    
    $memcache = new Memcache();
    return $memcache->get($key);
    

Memcached API for PHP example:
    
    
    use Google\AppEngine\Api\Memcache\Memcached;
    
    $memcache = new Memcached();
    $memcache->set('who', $request->get('who'));
    return $twig->render('memcache.html.twig', [
        'who' => $request->get('who'),
        'count' => $memcache->increment('count', 1, 0),
        'host' => $request->getHost(),
    ]);
    

If you prefer using the original behavior of Memcache for PHP 5 in PHP, you can continue to call Memcache implicitly by including a few more lines in your `composer.json` file. After importing the `appengine-php-sdk` package from composer, add the folllowing opt-in file path to the `files` element in the `autoload` section:

### PHP 7/8
    
    
    {
      "require": {
        "google/appengine-php-sdk": "^2.1" // Or any later version
      },
      "autoload": {
        "files": [
        "./vendor/google/appengine-php-sdk/src/Api/Memcache/MemcacheOptIn.php"
        ]
      }
    }
    

### Modules

You do not need to make changes to your app's configuration when upgrading to PHP. The behavior, features, and setup instructions for the Modules API remain the same. Refer to the [Modules Overview](https://docs.cloud.google.com/appengine/docs/standard/services/modules) and the [Modules API reference guide](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/Google/AppEngine/Api/Modules.html) for more details.

### Session

[PHP Sessions](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#PHP_Sessions) works in the same way as PHP 5.5 Sessions. However, the setup instructions differ because PHP 5.5 Sessions used the `MemcacheSessionHandler` class by default.

To use Sessions for PHP, you must register the [`MemcacheSessionHandler`](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/Google/AppEngine/Ext/Session/MemcacheSessionHandler.html) class with [`session_set_save_handler()`](http://php.net/manual/en/function.session-set-save-handler.php) and configure [`session.save_path`](https://www.php.net/manual/en/function.session-save-path.php) to Memcache. You should also opt-in to Memcache when accessing Memcache information.

For example:

### PHP 7/8
    
    
    ini_set('session.save_path', 'Google\AppEngine\Api\Memcache\Memcache');
    session_set_save_handler(new Google\AppEngine\Ext\Session\MemcacheSessionHandler(), true);
    

Refer to the [Session API reference guide](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/Google/AppEngine/Ext/Session.html) for more details.

### Task Queue

You do not need to make changes to your app's configuration when upgrading to PHP. The behavior, features, and setup instructions for Task Queue remain the same. Refer to the Sessions section in the [Task Queue Overview](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue) guide and [Task Queue API reference guide](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/Google/AppEngine/Api/TaskQueue.html) for more details.

### URL Fetch

To use URL Fetch for PHP, you need to add an explicit declaration of the URL Fetch libraries. Previously, the URL Fetch service for PHP 5 did not require an explicit declaration and was used implicitly.

In PHP 5, App Engine's URL Fetch service was the only way to fetch internet content in PHP 5.5, so most PHP 5.5 functions that accessed the internet were patched to use `UrlFetch` automatically.

In PHP, native PHP networking can access the internet, so this automatic patching is not done. In some cases, you can use the original `UrlFetch` mechanism, in particular the mechanism that provides the [`X-Appengine-Inbound-Appid`](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/outbound-requests#request_headers) request header for identifying the App Engine app that is making a request to your App Engine app.

To enable URL Fetch for PHP, you can either use an explicit declaration in the stream wrapper, or use the `UrlFetch` class directly, described in the following sections.

#### Option 1a. Stream handlers

You can enable App Engine's URL Fetch service to make HTTP requests to both `http://` and `https://` PHP stream handlers. To do this:

  1. Unregister the native PHP stream handler for HTTP(S) by using [`stream_wrapper_unregister()`](https://www.php.net/manual/en/function.stream-wrapper-unregister.php).
  2. Register HTTP(S) to the `UrlFetchStream` class by using [`stream_wrapper_register()`](https://www.php.net/manual/en/function.stream-wrapper-register.php).
  3. Call [`file_get_contents()`](http://php.net/manual/en/function.file-get-contents.php) with the configuration you want to use the stream wrapper. 
     * If you want to switch back to the native PHP stream handler from the URL Fetch service, use [`stream_wrapper_unregister()`](https://www.php.net/manual/en/function.stream-wrapper-unregister.php) and then register using [`stream_wrapper_restore()`](https://www.php.net/manual/en/function.stream-wrapper-restore.php).



For comparison, see the equivalent examples for PHP 5 and PHP:

### PHP 5.5
    
    
    ...
    $context = [
        'http' => [
            'method' => 'POST',
            'header' => $headers,
            'content' => http_build_query($data),
        ]
    ];
    $context = stream_context_create($context);
    
    // Using Url Fetch service. No option to use the native php stream wrapper.
    $result = file_get_contents('http://example.com', false, $context);
    echo $result;
    

### PHP 7/8
    
    
    use google\appengine\api\urlfetch\UrlFetchStream;
    ...
    $context = [
        'http' => [
            'method' => 'POST',
            'header' => $headers,
            'content' => http_build_query($data),
        ]
    ];
    $context = stream_context_create($context);
    
    // Using the native php stream wrapper.
    $result = file_get_contents('http://example.com', false, $context);
    echo $result;
    
    stream_wrapper_unregister("http");
    stream_wrapper_register("http", "UrlFetchStream");
    
    // Now using the Url Fetch service.
    $result = file_get_contents('http://example.com', false, $context);
    echo $result;
    
    stream_wrapper_unregister("http");
    stream_wrapper_restore("http");
    
    // Now using the native php stream wrapper again.
    

#### Option 1b. HTTP response headers with stream handlers

The instructions for using HTTP(S) response headers with stream handlers is similar to the instructions for using stream handlers:

  1. Unregister the native PHP stream handler for HTTP(S) by using `stream_wrapper_unregister()`.
  2. Register HTTP(S) to the `UrlFetchStream`class by using `stream_wrapper_register()`.
  3. Use [`fopen()`](https://www.php.net/manual/en/function.fopen.php) instead of [`file_get_contents()`](https://www.php.net/manual/en/function.stream-get-meta-data.php) with the configuration you want.
  4. Call [`stream_get_meta_data()`](https://www.php.net/manual/en/function.stream-get-meta-data.php) and extract the response header information by indexing metadata for `'wrapper_data`. The response headers are returned in an array form similar to that of [`$http_response_header`](https://www.php.net/manual/en/reserved.variables.httpresponseheader.php) in PHP 5.5.



### PHP 5.5
    
    
    ...
    $context = [
        'http' => [
            'method' => 'POST',
            'header' => $headers,
            'content' => http_build_query($data),
        ]
    ];
    $context = stream_context_create($context);
    
    // Using file_get_contents and the Url Fetch service.
    $result = file_get_contents('http://example.com', false, $context);
    
    // Print Http Response Headers
    print_r($http_response_header);
    

### PHP 7/8
    
    
    use google\appengine\api\urlfetch\UrlFetchStream;
    ...
    $context = [
        'http' => [
            'method' => 'POST',
            'header' => $headers,
            'content' => http_build_query($data),
        ]
    ];
    $context = stream_context_create($context);
    
    stream_wrapper_unregister("http");
    stream_wrapper_register("http", "UrlFetchStream");
    
    // Now using fopen and the Url Fetch service.
    $result = fopen('http://example.com', 'r', false, $context);
    
    // Print Http Response Headers
    $meta_data = stream_get_meta_data($result);
    $headers = $meta_data['wrapper_data'];
    print_r($headers);
    
    stream_wrapper_unregister("http");
    stream_wrapper_restore("http");
    

#### Option 2. UrlFetch class

The `UrlFetch` class is a custom class that provides a more targeted way of using the URL Fetch service for a HTTP(S) request at a smaller scope. Unlike the stream handler option, the `UrlFetch` class does not override all HTTP(S) requests made from stream wrapper compatible functions to use the URL Fetch service. Compared to the stream handler option, the `UrlFetch` class configuration is also simpler, in that it does not require use of various PHP APIs such as:

  * `stream_context_create()`
  * `stream_wrapper_unregister()`
  * `stream_wrapper_register()`
  * `file_get_contents()`



The following `UrlFetch` Class example is equivalent to the stream handler example:

### PHP 7/8
    
    
    use google\appengine\api\urlfetch\UrlFetch;
    ...
    $urlfetch = new UrlFetch();
    $result = $urlfetch->fetch($url, 'POST', $headers, http_build_query($data));
    echo $result->getContent();
    

### Users

You do not need to make changes to your app's configuration when upgrading to PHP. The behavior, features, and setup instructions for the Users API remain the same. Reference the [Users API Overview](https://docs.cloud.google.com/appengine/docs/standard/services/users) and the [Users API reference guide](https://googlecloudplatform.github.io/appengine-php-sdk/2.1.0/Google/AppEngine/Api/Users.html) for more details.

### Community-contributed libraries

You can use the community-contributed API for [`datastore`](https://github.com/tomwalder/php-gds) when upgrading to PHP.

### Other considerations

  * To test the legacy bundled services functionality in your PHP app, you can use the [local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server). When running the `dev_appserver.py` command, set the `--php_executable_path` argument to a PHP executable. Note that this is different from PHP 5, which requires a php-cgi executable.

If the project has a `composer.json` file, set `--php-composer-path` to the path of the `composer.phar` file.

  * To deploy your app, use the [`gcloud app deploy`](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/building-app#deploy-app) command.

  * Logging in the PHP runtime follows the logging standard in [Cloud Logging](https://docs.cloud.google.com/logging). In the PHP runtime, app logs are no longer bundled with the request logs but are separated in different records. To learn more about reading and writing logs, see the [Writing and viewing logs guide](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).




## Examples

To see examples of how to use the legacy bundled services with PHP, download the [code samples](https://console.cloud.google.com/storage/browser/php7x-wormhole-api-samples).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
