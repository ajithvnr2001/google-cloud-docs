---
url: https://docs.cloud.google.com/appengine/docs/flexible/php/runtime/
title: The PHP runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:00.360538+00:00
---

# The PHP runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/php/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The PHP runtime Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Some [PHP runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#php) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/php/runtime#newversions) to use the latest version of PHP. 

The PHP runtime is the software stack responsible for installing your application code and dependencies, and then running that application in the flexible environment.

## PHP versions

PHP 8.5 uses [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview). For the full list of supported PHP versions, and their corresponding Ubuntu version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#php).

To use a supported PHP version, you must:

  * Install `gcloud CLI` version **420.0.0 or later**. You can update your CLI tooling by running the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command. To view your installed version, you can run the [`gcloud version`](https://docs.cloud.google.com/sdk/gcloud/reference/version) command.

  * Include the `runtime_config` and `operating_system` settings in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) file to specify an operating system.

  * Declare the document root for your application in the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) file:
        
        runtime: php
          env: flex
        
          runtime_config:
              operating_system: "ubuntu24"
              document_root: "web"
        

Although you can specify the project root (`.`) directory as the document root, we recommend that you use a subdirectory for the `document_root` setting.

The source code is located in the `/workspace` directory instead of the root directory (`/`). If you override any configuration, the `NGINX` or `supervisor` processes reference your configuration file in this directory. To update corresponding references, you must:

    * Update any `include` statements in your NGINX configuration to be relative to `/workspace` instead of `/etc/nginx`.

    * Some files such as `gzip_params` are not included. To reference these files, include your own or copy from [GitHub](https://github.com/GoogleCloudPlatform/php-docker/blob/master/php-base/gzip_params). Files such as `mime.types` and `fastcgi_params` are available in `/etc/nginx` directory.

    * Some NGINX modules such as `nginx-plus-module-ndk` are not installed. Set the `$docroot` value or add the value manually in your `NGINX` configuration file.

  * Optionally, you can specify a runtime version by:

    * Including the `runtime_version` setting in your `app.yaml`. By default, the latest PHP version is used if the `runtime_version` setting is not specified.

      * To specify PHP 8.5 on Ubuntu 24:
            
            runtime: php
            env: flex
            
            runtime_config:
                operating_system: "ubuntu24"
                runtime_version: "8.5"
                document_root: .
            

      * To specify the latest supported PHP version on Ubuntu 24:
            
            runtime: php
              env: flex
            
              runtime_config:
                  operating_system: "ubuntu24"
                  document_root: .
            

    * Including a PHP version in the `composer.json` file.
          
          {
              "require": {
                  "php": "8.5.*"
              }
          }
          

When you specify a PHP version using MAJOR, MINOR, and PATCH, replace PATCH with `*`. Use the format `MAJOR.MINOR.*`. The PHP runtime is regularly updated to the latest release version and only supports one release version at a time, so specifying a release version can cause an error. 

See the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml) reference for more information.




### Previous runtime versions

**Warning:** PHP **version 7.3 and earlier** have reached end of support. App Engine blocks you from deploying your applications using runtimes that have reached end of support. We recommend that you migrate your app to use a [supported version](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#php) of PHP or use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes).

To use PHP **version 7.3 and earlier** , you must:

  * Declare the document root for your application. You can do this in your `app.yaml` file:
        
        runtime: php
        env: flex
        api_version: 1
        
        runtime_config:
          document_root: .
        

Although you can specify the project root (`.`) directory as the document root, we recommend that you use a subdirectory for the `document_root` setting.

  * Specify a PHP version in the `composer.json` file to prevent your application from automatically upgrading when a new version of PHP becomes available.
        
        {
            "require": {
                "php": "7.3.*"
            }
        }
        

When you specify a PHP version using MAJOR, MINOR, and PATCH, replace PATCH with `*`. Use the format `MAJOR.MINOR.*`. The PHP runtime is regularly updated to the latest release version and only supports one release version at a time, so specifying a release version can cause an error. 




### Support for other PHP runtimes

If you need to use a PHP version that isn't [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#php), you can create a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build) and select a valid base image with the PHP version you need.

For Google-supplied base images or [Docker PHP base images](https://hub.docker.com/_/php), see [Building custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base).

## Customize NGINX

To define a custom configuration file, include the `nginx-app.conf` file in the root directory of your project.

By default, the framework front controller uses the `index.php` file. You might need to change this to something different for your project. For instance, the Symfony framework uses `app.php` instead of `index.php`. You can change the filename in the `runtime_config` section of your `app.yaml` file:
    
    
    runtime: php
    env: flex
    
    runtime_config:
      operating_system: "ubuntu24"
      document_root: .
      front_controller_file: app.php
    

For version 7.3 and earlier, the `nginx-app.conf` configuration file is included in the server section of the main `NGINX` configuration file. For example, the default configuration `php-app.conf` file, contains the following:
    
    
    location / {
    # try to serve files directly, fallback to the front controller
    try_files $uri /$front_controller_file$is_args$args;
    }
    

To define a custom configuration file, create the `nginx-app.conf` file in the root directory of your project. The runtime overrides the default file with the file you provide.

By default, the framework front controller uses the `index.php` file. You might need to change this to something different for your project. For instance, the Symfony framework uses `app.php` instead of `index.php`. You can change the filename in the `runtime_config` section of your `app.yaml` file:
    
    
    runtime: php
    env: flex
    
    runtime_config:
      document_root: .
      front_controller_file: app.php
    

## OPcache

Enable OPcache in your `php.ini` file. See [the official doc](http://php.net/manual/en/opcache.configuration.php) for how to configure OPcache.

To disable OPcache, create or edit the file `php.ini` with the following line:
    
    
    opcache.enable=0
    

## Dependencies

The runtime looks for a [`composer.json`](https://getcomposer.org/doc/01-basic-usage.md#composer-json-project-setup) file in your application's source directory and uses [`composer`](https://getcomposer.org) to install any dependencies before starting your application. For more information on declaring and managing packages, see [Using PHP Libraries](https://docs.cloud.google.com/appengine/docs/flexible/php/specifying-dependencies).

### Using PHP extensions

The following PHP extensions are pre-installed and enabled on the system:

###  Supported PHP versions 

  * [BCMath](https://www.php.net/manual/en/book.bc.php)
  * [Bzip2](http://php.net/manual/en/book.bzip2.php)
  * [Calendar](https://www.php.net/manual/en/book.calendar.php)
  * [ctype](https://docs.cloud.google.com/appengine/docs/flexible/php/runtime/)
  * [cURL](http://php.net/manual/en/book.curl.php)
  * [DBA](https://www.php.net/manual/en/book.dba.php)
  * [DOM](https://www.php.net/manual/en/book.dom.php)
  * [Enchant](https://www.php.net/manual/en/book.enchant.php)
  * [EXIF](https://www.php.net/manual/en/book.exif.php)
  * [Fileinfo](https://www.php.net/manual/en/book.fileinfo.php)
  * [Filter](https://www.php.net/manual/en/book.filter.php)
  * [FTP](https://www.php.net/manual/en/book.ftp.php)
  * [GD](https://www.php.net/manual/en/book.image.php)
  * [Gettext](https://www.php.net/manual/en/book.gettext.php)
  * [GMP](http://php.net/manual/en/book.gmp.php)
  * [iconv](https://www.php.net/manual/en/book.iconv.php)
  * [Intl](https://www.php.net/manual/en/book.intl.php)
  * [LDAP](https://www.php.net/manual/en/book.ldap.php)
  * [libxml](https://www.php.net/manual/en/book.libxml.php)
  * [mbstring](http://php.net/manual/en/book.mbstring.php)
  * [MySQLi](http://php.net/manual/en/book.mysqli.php)
  * [MySQLND](https://www.php.net/manual/en/book.mysqlnd.php)
  * [OpenSSL](http://php.net/manual/en/book.openssl.php)
  * [pcntl](http://php.net/manual/en/book.pcntl.php)
  * [PDO](https://www.php.net/manual/en/intro.pdo.php)
  * [PDO_MYSQL](https://www.php.net/manual/en/ref.pdo-mysql.php)
  * [PDO_PGSQL](https://www.php.net/manual/en/ref.pdo-pgsql.php)
  * [PDO_SQLITE](https://www.php.net/manual/en/ref.pdo-sqlite.php)
  * [PGSQL](https://www.php.net/manual/en/pgsql.installation.php)
  * [Phar](https://www.php.net/manual/en/book.phar.php)
  * [POSIX](https://www.php.net/manual/en/book.posix.php)
  * [Session](https://www.php.net/manual/en/refs.basic.session.php)
  * [Shmop](https://www.php.net/manual/en/book.shmop.php)
  * [SimpleXML](https://www.php.net/manual/en/book.simplexml.php)
  * [SOAP](https://www.php.net/manual/en/book.soap.php)
  * [Sockets](http://php.net/manual/en/book.sockets.php)
  * [SQLite3](https://www.php.net/manual/en/book.sqlite3.php)
  * [Tidy](https://www.php.net/manual/en/book.tidy.php)
  * [Tokenizer](https://www.php.net/manual/en/book.tokenizer.php)
  * [XML](https://www.php.net/manual/en/xml.installation.php)
  * [XMLReader](https://www.php.net/manual/en/book.xmlreader.php)
  * [XMLWriter](https://www.php.net/manual/en/book.xmlwriter.php)
  * [XSL](https://www.php.net/manual/en/book.xsl.php)
  * [zend_test](https://www.zend.com/resources/php-extensions/running-php-extension-tests)
  * [Zip](http://php.net/manual/en/book.zip.php) (**Ubuntu 22 only**)
  * [Zlib](http://php.net/manual/en/book.zlib.php)



You can enable the following extensions using the `php.ini` file:

  * [gRPC](http://www.grpc.io/docs/tutorials/basic/php.html)
  * [ImageMagick](http://php.net/manual/en/book.imagick.php)
  * [Mailparse](https://www.php.net/manual/en/book.mailparse.php)
  * [Memcached](http://php.net/manual/en/book.memcached.php)
  * [mongodb](http://php.net/manual/en/book.mongodb.php)
  * [OpenCensus](https://pecl.php.net/package/opencensus)
  * [OpenTelemetry](https://pecl.php.net/package/opentelemetry) (PHP version 8.1 and later)
  * [OPcache](http://php.net/manual/en/book.opcache.php)
  * [protobuf](https://pecl.php.net/package/protobuf)
  * [Redis](https://pecl.php.net/package/redis)



###  v7.3 and earlier 

  * [APCu](http://php.net/manual/en/book.apcu.php)
  * [Bzip2](http://php.net/manual/en/book.bzip2.php)
  * [cURL](http://php.net/manual/en/book.curl.php)
  * [FPM](http://php.net/manual/en/book.fpm.php)
  * [GMP](http://php.net/manual/en/book.gmp.php)
  * [mbstring](http://php.net/manual/en/book.mbstring.php)
  * [mcrypt](http://php.net/manual/en/book.mcrypt.php)
  * [libsodium](https://pecl.php.net/package/libsodium)
  * [Memcached](http://php.net/manual/en/book.memcached.php)
  * [MySQL (PDO)](http://php.net/manual/en/book.pdo.php) (uses mysqlnd)
  * [MySQLi](http://php.net/manual/en/book.mysqli.php) (uses mysqlnd)
  * [OPcache](http://php.net/manual/en/book.opcache.php)
  * [OpenSSL](http://php.net/manual/en/book.openssl.php)
  * [pcntl](http://php.net/manual/en/book.pcntl.php)
  * [PostgreSQL](http://php.net/manual/en/book.pgsql.php)
  * [PostgreSQL (PDO)](http://php.net/manual/en/ref.pdo-pgsql.php)
  * [Readline](http://php.net/manual/en/book.readline.php)
  * [recode](http://php.net/manual/en/book.recode.php)
  * [sem](http://php.net/manual/en/book.sem.php)
  * [Sockets](http://php.net/manual/en/book.sockets.php)
  * [Zip](http://php.net/manual/en/book.zip.php)
  * [Zlib](http://php.net/manual/en/book.zlib.php)



The following PHP extensions are disabled by default. You can enable the following extensions in the using the `php.ini` file:

  * [amqp](https://pecl.php.net/package/amqp)
  * [APM](https://pecl.php.net/package/apm) (7.0+)
  * [BCMath](http://php.net/manual/en/book.bc.php)
  * [Bitset](https://pecl.php.net/package/bitset)
  * [Calendar](http://php.net/manual/en/book.calendar.php)
  * [Cassandra](http://datastax.github.io/php-driver/)
  * [couchbase](https://pecl.php.net/package/couchbase) (7.0+)
  * [ds](http://php.net/manual/en/book.ds.php) (7.0+)
  * [eio](http://php.net/manual/en/book.eio.php)
  * [ev](http://php.net/manual/en/book.ev.php)
  * [event](http://php.net/manual/en/book.event.php)
  * [Exif](http://php.net/manual/en/book.exif.php)
  * [FTP](http://php.net/manual/en/book.ftp.php)
  * [GD](http://php.net/manual/en/book.image.php) (with PNG, JPEG and FreeType support)
  * [gettext](http://php.net/manual/en/book.gettext.php)
  * [gRPC](http://www.grpc.io/docs/tutorials/basic/php.html)
  * [hprose](https://pecl.php.net/package/hprose)
  * [igbinary](https://pecl.php.net/package/igbinary)
  * [intl](http://php.net/manual/en/book.intl.php)
  * [ImageMagick](http://php.net/manual/en/book.imagick.php)
  * [jsond](https://pecl.php.net/package/jsond)
  * [krb5](https://pecl.php.net/package/krb5)
  * [lua](http://php.net/manual/en/book.lua.php) (7.0+)
  * [LZF](http://php.net/manual/en/book.lzf.php)
  * [memprof](https://pecl.php.net/package/memprof)
  * [mongodb](http://php.net/manual/en/book.mongodb.php)
  * [MySQL](http://php.net/manual/en/book.mysql.php) (5.6)
  * [oauth](http://php.net/manual/en/book.oauth.php)
  * [OpenCensus](https://pecl.php.net/package/opencensus)
  * [PCNTL](http://php.net/manual/en/book.pcntl.php)
  * [Phalcon](https://docs.phalcon.io/5.0/en/installation) (5.6, 7.0)
  * [pq](https://mdref.m6w6.name/pq)
  * [protobuf](https://pecl.php.net/package/protobuf)
  * [rdkafka](https://pecl.php.net/package/rdkafka)
  * [Redis](https://pecl.php.net/package/redis)
  * [SeasLog](https://pecl.php.net/package/seaslog)
  * [Shmop](http://php.net/manual/en/book.shmop.php)
  * [SOAP](http://php.net/manual/en/book.soap.php)
  * [SQLite3](http://php.net/manual/en/book.sqlite3.php)
  * [SQLite (PDO)](http://php.net/manual/en/ref.pdo-sqlite.php)
  * [stomp](http://php.net/manual/en/book.stomp.php)
  * [swoole](https://pecl.php.net/package/swoole)
  * [sync](http://php.net/manual/en/book.sync.php)
  * [tcpwrap](http://php.net/manual/en/book.tcpwrap.php)
  * [timezonedb](https://pecl.php.net/package/timezonedb)
  * [v8js](http://php.net/manual/en/book.v8js.php) (7.0+)
  * [vips](https://pecl.php.net/package/vips) (7.0+)
  * [XMLRPC](http://php.net/manual/en/book.xmlrpc.php)
  * [XSL](http://php.net/manual/en/book.xsl.php)
  * [yaconf](https://pecl.php.net/package/yaconf) (7.0+)
  * [yaf](http://php.net/manual/en/book.yaf.php)
  * [yaml](http://php.net/manual/en/book.yaml.php)



To enable an extension, add a `php.ini` file in the root of your application with the `extension` directive:
    
    
    ; Enable the Redis extension
    extension=redis.so
    
    ; Enable the OpenTelemetry extension (must be in an opentelemetry section)
    [opentelemetry]
    extension=opentelemetry.so
    

Alternatively, you can also enable an extension by adding a `require` to your `composer.json`:
    
    
    {
        "require": {
            "ext-redis": "*"
        }
    }
    

These packages allow the installation of most popular PHP extensions. If your application requires additional operating-system level dependencies, you must [extend the PHP runtime](https://docs.cloud.google.com/appengine/docs/flexible/php/runtime#extending_the_runtime) or use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) to install the appropriate packages.

#### HTTPS and forwarding proxies

App Engine terminates the HTTPS connection at the load balancer and forwards the request to your application. The NGINX server is configured to set the HTTPS environment variable (`$_SERVER["HTTPS"]`) to `on` when the request is made via HTTPS.

Some applications also need to ascertain the user's IP address. This is available in the standard `X-Forwarded-For` header.

## Disabled functions

The following functions are disabled with the `disable_functions` directive in `php.ini`:

  * `exec`
  * `passthru`
  * `proc_open`
  * `proc_close`
  * `shell_exec`
  * `show_source`
  * `symlink`
  * `system`



If you need any of the above functions, add a `php.ini` file in the root of your application and change the `disable_functions` directive. Alternatively, set `whitelist_functions` in the `runtime_config` section in `app.yaml` to a comma-delimited list of functions to allow.

For PHP version 7.3 and earlier, the [suhosin Security extension](https://suhosin.org) is installed and configured by default to run in simulation mode. Simulation mode logs the use of potentially dangerous functions, which will show in the [Cloud Logging UI](https://console.cloud.google.com/logs/query). Turning the simulation mode off will make your application exit when a potentially dangerous function is used. To enable this additional security feature, add a `php.ini` in your project root with the following option:
    
    
    ; Prevent the use of potentially dangerous functions rather than logging them
    suhosin.simulation = Off
    

## Patched functions

The function [`parse_str`](http://php.net/manual/en/function.parse-str.php) is patched and the second parameter is mandatory. If you call `parse_str` with only one parameter, it will throw a warning and the function will not be called.

## Available configurations

You can include the following configurations in the `runtime_config` section:

Name| Description| Default value  
---|---|---  
`document_root` |  Specifies `DOCUMENT_ROOT` for nginx and PHP. You must use a relative path from the project root directory.  | Required field  
`composer_flags` | You can override some of the composer flags with this key.  | `--no-dev --prefer-dist`  
`enable_stackdriver_integration` |  Supported only for **version 7.3 and earlier**. When set to true, the runtime will automatically enable Google Cloud Observability integration. This configuration requires `google/cloud` package v0.33 or higher.  | false  
`skip_lockdown_document_root` |  Supported only for **version 7.3 and earlier**. By default, the runtime will set a strict read-only permission on all the files and directories under the `document_root` directory. When set to `true`, the runtime will skip changing the permission.  | false  
`whitelist_functions` |  Supported only for **version 7.3 and earlier**. A comma-separated list of function names to allowlist. | An empty string  
`front_controller_file` | Default PHP file name for the directory access. | `index.php`  
`nginx_conf_http_include` |  Filename of a partial nginx config, which will be included in the `http` section in the main nginx config file.  | `nginx-http.conf`  
`nginx_conf_include` |  Filename of a partial nginx config which will be included in the `server` section in the main nginx config file.  | `nginx-app.conf`  
`nginx_conf_override` |  Filename of a user supplied nginx configuration file, which will be used as the nginx main configuration file. | `nginx.conf`  
`php_fpm_conf_override` |  Filename of a user supplied php-fpm configuration file, which will be included at the bottom of the `[app]` section so that it will override the existing configurations.  | `php-fpm.conf`  
`php_ini_override` | Filename of a user supplied PHP configuration file. | `php.ini`  
`supervisord_conf_addition` |  Filename of a user supplied supervisord config file, which will be included in the main supervisord config file.  | `additional-supervisord.conf`  
`supervisord_conf_override` |  Filename of a user supplied supervisord config file, which will override the main supervisord config file.  | `supervisord.conf`  
  
You can control whether Nginx serves static files for matching URIs by setting the `NGINX_SERVES_STATIC_FILES` environment variable in the `build_env_variables` section of your `app.yaml` file:
    
    
    runtime: php
    env: flex
    
    runtime_config:
      document_root: "web"
      operating_system: "ubuntu24"
    
    build_env_variables:
      NGINX_SERVES_STATIC_FILES: true
    

## Configuring supervisord in the PHP runtime

The App Engine flexible environment uses [supervisord](http://supervisord.org/) to manage processes. By default, `supervisord` runs `nginx` and `php-fpm` to run PHP web applications; however, some applications need to run external processes. Also such applications sometimes even do not need `nginx` nor `php-fpm`.

If you want to add a process managed by `supervisord`, add a file named `additional-supervisord.conf` to the project root directory. The following is an example configuration file content for this case:
    
    
    [program:quote-updater]
    command = php %(ENV_APP_DIR)s/worker.php
    stdout_logfile = /dev/stdout
    stdout_logfile_maxbytes=0
    stderr_logfile = /dev/stderr
    stderr_logfile_maxbytes=0
    user = www-data
    autostart = true
    autorestart = true
    priority = 5
    stopwaitsecs = 20
    

If you want to replace `nginx` and `php-fpm` with your process, add a file named `supervisord.conf` to the project root directory. The following is an example configuration file content for this case:
    
    
    [supervisord]
    nodaemon = true
    logfile = /dev/null
    logfile_maxbytes = 0
    pidfile = /var/run/supervisord.pid
    
    [program:react-server]
    command = php %(ENV_APP_DIR)s/index.php
    stdout_logfile = /dev/stdout
    stdout_logfile_maxbytes=0
    stderr_logfile = /dev/stderr
    stderr_logfile_maxbytes=0
    user = www-data
    autostart = true
    autorestart = true
    priority = 5
    stopwaitsecs = 20
    

## Extending the runtime

The App Engine flexible environment PHP runtime can be used to create a custom runtime. See [Customizing the PHP Runtime](https://docs.cloud.google.com/appengine/docs/flexible/php/customizing-the-php-runtime) for more information.

## Environment variables

The following environment variables are set by the runtime environment:

Environment variable | Description  
---|---  
`GAE_INSTANCE` | The name of the current instance.  
`GAE_MEMORY_MB` | The amount of memory available to the application process.  
`GAE_SERVICE` | The service name specified in your application's `app.yaml` file, or if no service name is specified, it is set to `default`.  
`GAE_VERSION` | The version label of the current application.  
`GOOGLE_CLOUD_PROJECT` | The Project ID associated with your application, which is visible in the Google Cloud console  
`PORT` | The port that will receive HTTP requests.  
  
You can set additional environment variables with [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#defining_environment_variables).

## Metadata server

Each instance of your application can use the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to query information about the instance, including its host name, external IP address, instance ID, custom metadata, and service account information. App Engine doesn't allow you to set custom metadata for each instance, but you can set [project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide) and read it from your App Engine and Compute Engine instances.

This example function uses the metadata server to get the external IP address of an instance:
    
    
    function get_external_ip_using_google_cloud()
    {
        $metadata = new Google\Cloud\Core\Compute\Metadata();
        $externalIp = $metadata->get(
            'instance/network-interfaces/0/access-configs/0/external-ip');
    
        return $externalIp;
    }
    
    function get_external_ip_using_curl()
    {
        $url = 'http://metadata.google.internal/computeMetadata/v1/' .
            'instance/network-interfaces/0/access-configs/0/external-ip';
    
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Metadata-Flavor: Google'));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        return curl_exec($ch);
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
