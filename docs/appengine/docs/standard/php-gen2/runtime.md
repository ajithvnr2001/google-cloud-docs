---
url: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime/
title: PHP runtime environment \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:59.447427+00:00
---

# PHP runtime environment  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  PHP runtime environment Stay organized with collections  Save and categorize content based on your preferences. 

The PHP runtime is the software stack responsible for installing your web service's code and its dependencies and running your service.

To specify PHP for the App Engine standard environment, declare the runtime in the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/configuring-your-app-with-app-yaml) file. For example:
    
    
    runtime: phpVERSION

Where VERSION is the PHP `MAJOR` and `MINOR` version numbers. For example, to use the latest PHP version, PHP 8.5, specify `85`.

For other supported PHP versions, and the corresponding Ubuntu version for your PHP version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#php).

## PHP version

The latest supported PHP version is 8.5. The PHP runtime uses the latest stable release of the version that is specified in your `app.yaml` file. App Engine automatically updates to new patch release versions, but will not automatically update the minor version.

For example, your app might be deployed at PHP 7.3.0 and later automatically updated to version 7.3.1, but it will not be automatically updated to PHP 7.4.0.

**Note:** If you have a required PHP version specified in your `composer.json` file, you will have to remove the element for a successful deployment.

## App startup

You will need to deploy a [front controller](https://wikipedia.org/wiki/Front_controller) to handle all request routing.

The following examples show different ways to serve your app:

  * If your app contains a `public/index.php` or `index.php` file, App Engine uses this file to serve your app.

We recommend you use a framework, such as Laravel, Symfony, or [Slim](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/appengine/standard/slim-framework), because it provides lightweight routing for writing and deploying PHP apps quickly. See an [example Slim front controller](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/master/appengine/standard/slim-framework/index.php).

However, if you are migrating a legacy app, see the following sample `index.php` file to import the PHP files you need and implement the front controller manually:
        
        switch (@parse_url($_SERVER['REQUEST_URI'])['path']) {
            case '/':
                require 'homepage.php';
                break;
            case '/contact.php':
                require 'contact.php';
                break;
            default:
                http_response_code(404);
                exit('Not Found');
        }

  * If you specify the optional `entrypoint` element in your `app.yaml` file, App Engine uses the command in the `entrypoint` element to serve your app instead of using `public/index.php` or `index.php`:
        
        entrypoint: serve path/to/my/front/controller.php
        

The `entrypoint` field uses the built-in `serve` command, which is a program within the PHP runtimes that starts up the `php-fpm` implementation and a webserver in the background. This webserver routes all traffic to the provided PHP file using the front controller design pattern.

The `serve` command has two optional flags:

    * `--workers=N`: specifies the N number of `php-fpm` workers. If you don't set the `--workers` flag, the `serve` command guesses the number of workers based on the amount of memory available. For best results, set the values for the `--workers` flag on the `serve` command and the `max_concurrent_requests` element to be the same number.

    * `--enable-dynamic-workers`: specifies that you'd like the `php-fpm` workers to be spawned only as needed. The default is to use a static policy for the `php-fpm` workers. You can change the number maximum number of spawned workers by using the `--workers=N` flag. By default the maximum number of spawned workers defaults to that set by the static policy.

The optional flags must come before the front controller path:
    
    entrypoint: serve --workers=2 --enable-dynamic-workers path/to/index.php
    

  * You can deploy a long-running worker process by setting the `entrypoint` element to the filepath of the worker process:
        
        entrypoint: php long-running-worker-file.php
        

If the `entrypoint` element executes a script with a long-running process, such as a Pub/Sub Worker subscribed to a topic, do not use the `serve` command.




For more information, see the [`app.yaml` reference ](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).

## Enabled extensions

The following extensions have been enabled in the PHP runtimes for App Engine:

  * `BCMath`
  * `bz2`
  * `Calendar`
  * `core`
  * `cgi`
  * `ctype`
  * `cURL`
  * `date`
  * `dba`
  * `dom`
  * `enchant`
  * `Exif`
  * `fcgi`
  * `fileinfo`
  * `filter`
  * `FTP`
  * `GD`
  * `gettext`
  * `GMP`
  * `hash`
  * `iconv`
  * `intl`
  * `json`
  * `LDAP`
  * `libxml`
  * `mbstring`
  * `MYSQLi`
  * `mysqlnd`
  * `MySQL (PDO)`
  * `OPcache`
  * `OpenSSL`
  * `PCNTL`
  * `pcre`
  * `PDO`
  * `pgsql`
  * `Phar`
  * `posix`
  * `PostgreSQL (PDO)`
  * `Reflection`
  * `session`
  * `Shmop`
  * `SimpleXML`
  * `SOAP`
  * `Sockets`
  * `sodium (PHP 8.x only, not available for PHP 7.x)`
  * `SPL`
  * `SQLite (PDO)`
  * `SQLite3`
  * `standard`
  * `test`
  * `tidy`
  * `tokenizer`
  * `XML`
  * `XMLreader`
  * `XMLrpc (PHP 7.x only, not available for PHP 8.x)`
  * `XMLwriter`
  * `XSL`
  * `zend`
  * `Zip`
  * `Zlib`



## Dynamically loadable extensions

The following extensions are dynamically loadable by configuring [`php.ini`](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/config/php_ini):

  * [Memcached](https://pecl.php.net/package/memcached)
  * [gRPC](https://grpc.io/docs/quickstart/php.html)
  * [protobuf](https://github.com/google/protobuf/tree/master/php)
  * [MongoDB](https://secure.php.net/manual/en/set.mongodb.php)
  * [ImageMagick](https://php.net/manual/en/book.imagick.php)
  * [OpenCensus](https://github.com/census-instrumentation/opencensus-php)
  * [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-php)
  * [PHPRedis](https://pecl.php.net/package/redis)



To enable these extensions, add directives for them in your `php.ini` file under `extension`, for example:
    
    
    extension=memcached.so
    extension=grpc.so
    extension=protobuf.so
    extension=mongodb.so
    extension=imagick.so
    extension=opencensus.so
    extension=redis.so
    
    [opentelemetry]
    extension=opentelemetry.so
    

## Environment variables

The following environment variables are set by the runtime:

Environment variable | Description  
---|---  
`GAE_APPLICATION` | The ID of your App Engine application. This ID is prefixed with 'region code~' such as 'e~' for applications deployed in Europe.  
`GAE_DEPLOYMENT_ID` | The ID of the current deployment.  
`GAE_ENV` | The App Engine environment. Set to `standard`.  
`GAE_INSTANCE` | The ID of the instance on which your service is currently running.  
`GAE_MEMORY_MB` | The amount of memory available to the application process, in MB.  
`GAE_RUNTIME` | The runtime specified in your `app.yaml` file.  
`GAE_SERVICE` | The service name specified in your `app.yaml` file. If no service name is specified, it is set to `default`.  
`GAE_VERSION` | The current version label of your service.  
`GOOGLE_CLOUD_PROJECT` | The Google Cloud project ID associated with your application.  
`PORT` | The port that receives HTTP requests.  
`NODE_ENV` (Only available in the Node.js runtime) | Set to `production` when your service is deployed.  
  
You can [define additional environment variables in your `app.yaml` file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#environment_variables), but the above values cannot be overridden, except for `NODE_ENV`. 

## HTTPS and forwarding proxies

App Engine terminates HTTPS connections at the load balancer and forwards requests to your application. Some applications need to determine the original request IP and protocol. The user's IP address is available in the standard `X-Forwarded-For` header. Applications that require this information should configure their web framework to trust the proxy.

## Filesystem

The runtime includes a writable `/tmp` directory, with all other directories having read-only access. Writing to `/tmp` takes up system memory. For more information, see [`tempnam()` and `sys_get_temp_dir()` support](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#tempnam_and_sys_get_temp_dir_support).

## Metadata server

Each instance of your application can use the App Engine metadata server to query information about the instance and your project.

**Note:** Custom metadata is not supported in the standard environment.

You can access the metadata server through the following endpoints:

  * `http://metadata`
  * `http://metadata.google.internal`



Requests sent to the metadata server must include the request header `Metadata-Flavor: Google`. This header indicates that the request was sent with the intention of retrieving metadata values.

The following table lists the endpoints where you can make HTTP requests for specific metadata:

Metadata endpoint | Description  
---|---  
`/computeMetadata/v1/project/numeric-project-id` | The project number assigned to your project.  
`/computeMetadata/v1/project/project-id` | The project ID assigned to your project.  
`/computeMetadata/v1/instance/region` | The region the instance is running in.  
`/computeMetadata/v1/instance/service-accounts/default/aliases` |   
`/computeMetadata/v1/instance/service-accounts/default/email` | The default service account email assigned to your project.  
`/computeMetadata/v1/instance/service-accounts/default/` | Lists all the default service accounts for your project.  
`/computeMetadata/v1/instance/service-accounts/default/scopes` | Lists all the supported scopes for the default service accounts.  
`/computeMetadata/v1/instance/service-accounts/default/token` | Returns the auth token that can be used to authenticate your application to other Google Cloud APIs.  
  
For example, to retrieve your project ID, send a request to `http://metadata.google.internal/computeMetadata/v1/project/project-id`.

The following is an example of how to call the metadata endpoints using cURL or the Google Cloud Client Library:
    
    
    /**
     * Requests a key from the Metadata server using the Google Cloud SDK. Install
     * the Google Cloud SDK by running "composer install google/cloud"
     *
     * @param $metadataKey the key for the metadata server
     */
    function request_metadata_using_google_cloud($metadataKey)
    {
        $metadata = new Google\Cloud\Core\Compute\Metadata();
        $metadataValue = $metadata->get($metadataKey);
    
        return $metadataValue;
    }
    
    /**
     * Requests a key from the Metadata server using cURL.
     *
     * @param $metadataKey the key for the metadata server
     */
    function request_metadata_using_curl($metadataKey)
    {
        $url = 'http://metadata/computeMetadata/v1/' . $metadataKey;
    
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Metadata-Flavor: Google'));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        return curl_exec($ch);
    }

## Sessions

PHP provides a session management layer that allows web apps to preserve user-state information between requests. Sessions in App Engine work much like sessions in any other PHP app.

To set a variable in a user's session, you can use the following code:
    
    
    session_start();
    $_SESSION['Foo'] = 'Bar';
    

The following code will print `Bar`, on a subsequent request by the same user:
    
    
    session_start();
    print $_SESSION['Foo']; // prints Bar
    

For longer-lived sessions, use an alternative storage service such as [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine).

## Special $_SERVER keys

PHP makes the special `$_SERVER[]` array available in the request scope. In addition to the standard CGI parameters, App Engine adds some additional useful keys:

  * `GAE_APPLICATION` \- Current app's Google Cloud project ID.
  * `GAE_DEPLOYMENT_ID` \- Deployed source code's ID.
  * `GAE_ENV` \- The App Engine environment (standard or flexible) where your app runs.
  * `GAE_INSTANCE` \- Current executing instance name.
  * `GAE_MEMORY_MB` \- Amount of memory available to the app process, in MB.
  * `GAE_RUNTIME` \- The runtime specified in your `app.yaml` file, such as php72.
  * `GAE_SERVICE` \- Currently deployed service name.
  * `GAE_VERSION` \- Currently deployed version name.
  * `GOOGLE_CLOUD_PROJECT` \- Google Cloud project ID.
  * `HTTP_X_APPENGINE_CITY` \- Name of the city from which the request originated. For example, a request from the city of Mountain View might have the header value mountain view.
  * `HTTP_X_APPENGINE_CITYLATLONG` \- Latitude and longitude of the city from which the request originated. This string might look like "37.386051,-122.083851" for a request from Mountain View.
  * `HTTP_X_APPENGINE_COUNTRY` \- Country from which the request originated, as an ISO 3166-1 alpha-2 country code. App Engine determines this code from the client's IP address.
  * `HTTP_X_APPENGINE_HTTPS` \- Verifies HTTPS usage.
  * `HTTP_X_APPENGINE_REGION` \- Name of the region from which the request originated. This value only makes sense in the context of the country in `X-Appengine-Country`. For example, if the country is "US" and the region is "ca", that "ca" means "California", not Canada.
  * `HTTP_X_APPENGINE_USER_IP` \- Client's IP address. Note that `$_SERVER['HTTP_X_APPENGINE_USER_IP']` is the only way your app can retrieve the client's IP address. The `$_SERVER['REMOTE_ADDR']` variable isn't available in App Engine.



## Directives with new initialization defaults

The following table specifies directives whose initialization defaults differ from those supplied with the standard PHP interpreter available from [php.net](http://php.net/). To find the default values for directives not specified in the following table, refer to [php.ini directives](https://www.php.net/manual/en/ini.list.php).

Directive | Default Value in App Engine  
---|---  
`expose_php` | `Off`  
`memory_limit` | `-1`  
`max_execution_time` | `0`  
`error_reporting` | `E_ALL & ~E_DEPRECATED & ~E_STRICT`  
`display_errors` | `Off`  
`display_startup_errors` | `Off`  
`log_errors` | `On`  
`log_errors_max_len` | `0`  
`ignore_repeated_errors` | `Off`  
`ignore_repeated_source` | `Off`  
`html_errors` | `Off`  
`opcache.enable` | `On`  
`opcache.validate_timestamps` | `Off`  
`opcache.memory_consumption` | `32`  
  
Override these default directives by including them in a [`php.ini`](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/config/php_ini) file for your app.

### `tempnam()` and `sys_get_temp_dir()` support

App Engine apps run in a security sandbox in which only the `/tmp` directory is writable and stored in the instance's RAM. For this reason, App Engine's version of [`tempnam()`](http://php.net/manual/en/function.tempnam.php) returns an in-memory temp file that can be written to a permanent storage solution such as [Cloud Storage buckets](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage).

Here is an example on how to write to the in-memory temp file using `file_put_contents()` and `fwrite()`.
    
    
    <?php
    $dir = sys_get_temp_dir();
    $tmp = tempnam($dir, "foo");
    file_put_contents($tmp, "hello");
    $f = fopen($tmp, "a");
    fwrite($f, " world");
    fclose($f);
    echo file_get_contents($tmp);
    

The expected output from the example would then be:
    
    
    hello world
    

**Note:** When an instance is deleted, any temporary files created by `tempnam()` are also removed.

## Managing Dependencies with Composer

For more information, see the [Specifying Dependencies page](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/specifying-dependencies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
