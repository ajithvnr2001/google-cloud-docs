---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/config/appref/
title: App Engine app.yaml reference \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:37.914255+00:00
---

# App Engine app.yaml reference  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/config/appref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  App Engine app.yaml reference Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

Go Java Node.js PHP Python Ruby

You configure your App Engine app's settings in the `app.yaml` configuration file. Your config file must specify at least a `runtime` entry.

Each [service](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine) in your app has its own `app.yaml` file, which acts as a descriptor for its deployment. You must first create the `app.yaml` file for the `default` service before you can create and deploy `app.yaml` files for additional services within your app. To learn more about structuring multiple services in your app, see [Structuring Web Services in App Engine](https://docs.cloud.google.com/appengine/docs/standard/configuration-files).

## Syntax

The syntax of `app.yaml` is the [YAML format](http://www.yaml.org/).

The YAML format supports comments. A line that begins with a pound (`#`) character is ignored:
    
    
    # This is a comment.
    

URL and file path patterns use [POSIX extended regular expression syntax](https://wikipedia.org/wiki/Regular_expression), excluding collating elements and collation classes. Back-references to grouped matches (e.g. `\1`) are supported, as are these Perl extensions: `\w \W \s \S \d \D`.

## Example

The following is an example of an `app.yaml` file:
    
    
    runtime: python314
    
    instance_class: F2
    
    env_variables:
      BUCKET_NAME: "example-gcs-bucket"
    
    handlers:
    # Matches requests to /images/... to files in static/images/...
    - url: /images
      static_dir: static/images
    
    - url: /.*
      secure: always
      redirect_http_response_code: 301
      script: auto

The following table provides YAML examples of available fields in an `app.yaml` file:

### Runtime and app elements

Element | Description  
---|---  
`app_engine_apis` |  Optional. Set this field to `true` to enable access to all the [bundled services](https://docs.cloud.google.com/appengine/docs/standard/services/overview) for second-generation runtimes. If you set this field to `true` or `false`, then deployments succeed only when the `app_engine_bundled_services` setting is unspecified. We recommend using `app_engine_bundled_services` to specify the bundled services your app requires. This approach provides fine-grained control and improves security by minimizing exposure to unneeded services. Additionally, it ensures your app receives critical updates for the services it actually uses, making it maintainable.  
`app_engine_bundled_services` |  Optional. Configure this field to enable [access to specific bundled services](https://docs.cloud.google.com/appengine/docs/standard/services/overview) for second-generation runtimes. You can't use this setting if you set the `app_engine_apis` field to `true`. Specify any of the following supported bundled services with this setting:

  * App identity: `app_identity_service`
  * Blobstore: `blobstore`
  * Capabilities: `capability_service`
  * Datastore: `datastore_v3`
  * Images: `images`
  * Namespaces: `namespaces`
  * Search: `search`
  * Deferred: `deferred`
  * Mail: `mail`
  * Memcache: `memcache`
  * Modules: `modules`
  * Task queues: `taskqueue`
  * URL fetch: `urlfetch`
  * User: `user`

**Example:**
    
    
    app_engine_bundled_services:
    - user
    - memcache

This example allows your application to use only Datastore and Memcache bundled services.  
`build_env_variables` |  Optional. If you are using a runtime that supports [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview), you can define build environment variables in your `app.yaml` file. To learn more, see [ Using build environment variables](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#build-env-vars).  
`default_expiration` |  Optional. Sets a global default cache period for all static file handlers for an application. You can also configure a cache duration for specific static file handlers. The value is a string of numbers and units, separated by spaces, where units can be d for days, h for hours, m for minutes, and s for seconds. For example, `"4d 5h"` sets cache expiration to 4 days and 5 hours after the file is first requested. If omitted, the production server sets the expiration to 10 minutes.  **Python example:**
    
    
    runtime: python314
    
    default_expiration: "4d 5h"
    
    handlers:
    # ...

For more information, see [Cache expiration](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#static_cache_expiration).   
`entrypoint` |  Optional. Overrides the default startup behavior by executing the `entrypoint` command when your app starts. For your app to receive HTTP requests, the `entrypoint` element should contain a command which starts a web server that listens on port 8080.  If you do not specify `entrypoint` for the Python runtime, App Engine [ configures and starts](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#application_startup) the Gunicorn webserver. For more information, see [ Application startup](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#application_startup).  
`env_variables` |  Optional. You can define environment variables in your `app.yaml` file to make them available to your app. Ensure that the key in Environment variable(s) matches the expression '[a-zA-Z_][a-zA-Z0-9_]*' (start with alphabet or "_" followed by any alphanumeric or "_").  Environment variables that are prefixed with `GAE` are reserved for system use and not allowed in the `app.yaml` file.  For Python, these variables are available in the `os.environ` dictionary:
    
    
    env_variables:
              DJANGO_SETTINGS_MODULE: "myapp.settings"

Also see the list of [ runtime environment variables](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#environment_variables) that cannot be overwritten.  
`error_handlers` |  Optional. Used to configure custom error pages that are returned for different error types.  This element can contain the following elements:

`error_code`
     Optional. The `error_code` can be one of the following: 

`over_quota`
    Indicates the app has [ exceeded a resource quota](https://docs.cloud.google.com/appengine/docs/quotas)
`timeout`
     Served if a deadline is reached before there is a response from your app. 
The error_code is optional; if it's not specified, the given file is the default error response for your app. 
`file`
     Each file entry indicates a static file that should be served in place of the generic error response. If you specify a `file` element without a corresponding `error_code` element, the static file will be the default error page for your app. **Warning:** Make sure that the path to the error response file does not overlap with static file handler paths.  The custom error data must be less than 10 kilobytes. 
**Example**
    
    
    error_handlers:
      - file: default_error.html
    
      - error_code: over_quota
        file: over_quota.html  
  
`handlers` |  Optional. A list of URL patterns and descriptions of how they should be handled. App Engine can handle URLs by executing application code, or by serving static files uploaded with the code, such as images, CSS, or JavaScript.  See the Handlers and sub-elements syntax.   
`inbound_services` |  Optional. Applications must enable those services before it can receive inbound requests. You can enable the service for an app by including an `inbound_services` section in the `app.yaml` file. 

`warmup`
     Enables warmup requests. See [ Configuring Warmup Requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests). 
**Example:**
    
    
    inbound_services:
    - warmup  
  
`instance_class` |  Optional. The [instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) for this service.  The following values are available depending on your service's [scaling](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine#instances): 

**Automatic scaling**
     `F1`, `F2`, `F4`, `F4_1G`
     _Default:_ `F1` Optionally use the  `automatic_scaling` element to change default settings for automatic scaling, such as minimum and maximum number of instances, latency, and concurrent connections.  **Note:** If `instance_class` is set to `F2` or higher, you can optimize your instances by setting  `max_concurrent_requests` to a value higher than the default value of 10. To determine the optimal value, gradually increase it and monitor the performance of your application. 
**Basic and manual scaling**
     `B1`, `B2`, `B4`, `B4_1G`, `B8`
     _Default:_ `B2` Basic and manual instance classes require you to specify either the  `basic_scaling` element or the  `manual_scaling` element.   
`runtime` |  Required. The name of the runtime environment that is used by your app. For example, to specify the runtime environment, use: 
    
    
    runtime: python314  
  
`service` |  Required if creating a [ service](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine). Optional for the `default` service. Each service and each version must have a name. A name can contain numbers, letters, and hyphens. The combined length of `VERSION-dot-SERVICE-dot-PROJECT_ID`, where `VERSION` is the name of your version, `SERVICE` is the name of your service, and `PROJECT_ID` is your project ID, cannot be longer than 63 characters and cannot start or end with a hyphen. Choose a unique name for each service and each version. Don't reuse names between services and versions.  Example: 
    
    
    service: service-name  
  
`service_account` |  Optional. The `service_account` element lets you specify a [version-specific service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts#set_a_version-specific_service_account) as the identity for the version. The specified service account is used when accessing other Google Cloud services and executing tasks.  Example: 
    
    
    service_account: [SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com  
  
`vpc_access` (Preview) |  Optional. Configure Direct VPC egress for your service, enabling the application to send requests to internal resources in your VPC network.  This configuration includes the following fields: 

`network_interface`
     Contains network interface settings to use for Direct VPC egress.

`network`
    The name of the VPC network to use for Direct VPC egress.
`subnet`
    The name of the VPC subnetwork to use for Direct VPC egress.
`tags`
    Optional. List of network tags to associate with your service's instances for use in firewall rules and routing policies.
`vpc_egress`
    Optional. Controls how outbound traffic is routed. This field supports the following configuration settings: 

`private-ranges-only`
    Default. Only traffic to internal IP addresses is routed through the VPC network. Internet traffic uses the default App Engine path. 
`all-traffic`
    All outbound requests are routed through the VPC network. 
For more details on how to configure Direct VPC egress, see [ Connect to a VPC network using Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc).  **Example**
    
    
    vpc_access:
      network_interface:
        network: direct-vpc-network
        subnet: direct-vpc-subnetwork
        tags:
        - my-tag1
        - my-tag2
      vpc_egress: all-traffic
          
  
`vpc_access_connector` |  Optional. Configures your application to use a Serverless VPC Access connector, enabling the application to send requests to internal resources in your VPC network. For more information, see [Connecting to a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc). 

`name`
    String literal. Specify the fully-qualified name of your Serverless VPC Access connector in quotes: 
    
    
    "projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME"

`egress_setting`
    Optional. Default is `private-ranges-only`. The `egress_setting` can be one of the following: 

`private-ranges-only`
    Default. Requests to internal IP addresses are sent through the Serverless VPC Access connector into the connected VPC network. Requests to external IP addresses are sent to the public internet. 
`all-traffic`
    All requests are sent through the Serverless VPC Access connector into the connected VPC network. 
**Example**
    
    
    vpc_access_connector:
      name: "projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME"
      egress_setting: all-traffic  
  
### Handlers element

The `handlers` element provides a list of URL patterns and descriptions of how they should be handled. App Engine can handle URLs by executing application code, or by serving static files uploaded with the code, such as images, CSS, or JavaScript.

Patterns are evaluated in the order they appear in the `app.yaml` file, from top to bottom. The first mapping whose pattern matches the URL is the one used to handle the request.

The following table lists the subelements of the `handlers` element that control the behavior for static files, static directories, scripts in runtimes other than Node.js, and other settings.

Element | Description  
---|---  
`auth_fail_action` |  To use this element, either enable the Users API by configuring the `user` setting in the `app_engine_bundled_services` list or set the `app_engine_apis` field to `true`. Optional. Describes the action taken when the `login` element is specified for a handler and the user is not logged in. Has two possible values: 

`redirect`
     Default. The user is redirected to the Google sign-in page, or `/_ah/login_required` if OpenID authentication is used. The user is redirected back to the application URL after signing in or creating an account. 
`unauthorized`
     The request is rejected with an `HTTP 401` status code and an error message. 
If an application needs different behavior, the application itself can implement the handling of user logins. For example, requiring a login for the `/profile/` directory or an administrator login for the `/admin/` directory. See [the Users API](https://docs.cloud.google.com/appengine/docs/standard/authenticating-users) for more information.  You can configure a handler to refuse access to protected URLs when the user is not signed in, instead of redirecting the user to the sign-in page, by adding `auth_fail_action: unauthorized` to the handler's configuration.   
`expiration` |  Optional. The length of time a static file served by this handler should be cached by web proxies and browsers. The value is a string of numbers and units, separated by spaces, where units can be `d` for days, `h` for hours, `m` for minutes, and `s` for seconds. For example, `"4d 5h"` sets cache expiration to 4 days and 5 hours after the file is first requested. If omitted, the application's `default_expiration` is used. See [Cache expiration](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#static_cache_expiration) for more details.   
`http_headers` |  Optional. You can set [HTTP headers](https://wikipedia.org/wiki/List_of_HTTP_header_fields) for responses of your static file or directory handlers. If you need to set HTTP headers in your `script` handlers, you should instead do that in your app's code. For information about which response headers influence caching, see [Caching static content](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#caching_static_content).  For more information about App Engine specific headers, see [ Request headers and responses](https://docs.cloud.google.com/appengine/docs/standard/reference/request-headers).  **Example**
    
    
    handlers:
    - url: /images
      static_dir: static/images
      http_headers:
        X-Foo-Header: foo
        X-Bar-Header: bar value
        vary: Accept-Encoding
      # ...

#### CORS Support

One important use of this feature is to support cross-origin resource sharing (CORS), such as accessing files hosted by another App Engine app.  For example, you could have a game app `mygame.uc.r.appspot.com` that accesses assets hosted by `myassets.uc.r.appspot.com`. However, if `mygame` attempts to make a JavaScript `XMLHttpRequest` to `myassets`, it will not succeed unless the handler for `myassets` returns an `Access-Control-Allow-Origin:` response header containing the value `http://mygame.uc.r.appspot.com`.  Here is how you would make your static file handler return that required response header value: 
    
    
    handlers:
    - url: /images
      static_dir: static/images
      http_headers:
        Access-Control-Allow-Origin: https://mygame.uc.r.appspot.com
      # ...

Tip: To allow everyone access to your assets, you can use the wildcard `'*'`, instead of `https://mygame.uc.r.appspot.com`.   
`login` |  To use this element, either enable the Users API by configuring the `user` setting in the `app_engine_bundled_services` list or set the `app_engine_apis` field to `true`. Optional. Determines whether the URL handler requires that the user is signed in. This element has three possible values:

`optional`
    Default. Does not require that the user is signed in.
`required`
     If the user has signed in, the handler proceeds normally. Otherwise, the action given in `auth_fail_action` is taken. 
`admin`
     As with `required`, performs `auth_fail_action` if the user is not signed in. In addition, if the user is not an administrator for the application, they are given an error message regardless of the `auth_fail_action` setting. If the user is an administrator, the handler proceeds. 
When a URL handler with a `login` setting other than `optional` matches a URL, the handler first checks whether the user has signed in to the application using its [ authentication option](https://docs.cloud.google.com/appengine/docs/standard/users#Authentication_options). If not, by default, the user is redirected to the sign-in page. You can also use `auth_fail_action` to configure the app to simply reject requests for a handler from users who are not properly authenticated, instead of redirecting the user to the sign-in page.  Note: the `admin` login restriction is also satisfied for internal requests for which App Engine sets appropriate `X-Appengine` special headers. For example, `cron` scheduled tasks satisfy the `admin` restriction, because App Engine sets an HTTP header `X-Appengine-Cron: true` on the respective requests. However, the requests would **not** satisfy the `required` login restriction, because cron scheduled tasks are not run as any user.   
`mime_type` |  Optional. If specified, all files served by this handler will be served using the specified MIME type. If not specified, the MIME type for a file will be derived from the file's filename extension. If the same file is uploaded with multiple extensions, the resulting extension can depend on the order in which the uploads occurred.  For more information about the possible MIME media types, see [the IANA MIME Media Types website](http://www.iana.org/assignments/media-types/).   
`redirect_http_response_code` |  Optional. `redirect_http_response_code` is used with the `secure` setting to set the HTTP response code returned when performing a redirect required by how the `secure` setting is configured. `redirect_http_response_code` element has the following possible values: 

`301`
    Moved Permanently response code.
`302`
     Found response code. 
`303`
     See Other response code. 
`307`
     Temporary Redirect response code. 
When a user's request is redirected, the HTTP status code will be set to the value of the `redirect_http_response_code` parameter. If the parameter is not present, 302 will be returned.   
`script` |  Optional. Specifies that requests to the specific handler should target your app. The only accepted value for the `script` element is `auto` because all traffic is served using the entrypoint command. In order to use static handlers, at least one of your handlers must contain the line `script: auto` or define an `entrypoint` element to deploy successfully.  
`secure` |  Optional. Any URL handler can use the `secure` setting, including static file handlers. The `secure` element has the following possible values: 

`optional`
     Both HTTP and HTTPS requests with URLs that match the handler succeed without redirects. The application can examine the request to determine which protocol was used, and respond accordingly. This is the default when `secure` is not provided for a handler. 
`never`
     Requests for a URL that match this handler that use HTTPS are automatically redirected to the HTTP equivalent URL. When a user's HTTPS request is redirected to be an HTTP request, the query parameters are removed from the request. This prevents a user from accidentally submitting query data over a non-secure connection that was intended for a secure connection. 
`always`
     Requests for a URL that match this handler that do not use HTTPS are automatically redirected to the HTTPS URL with the same path. Query parameters are preserved for the redirect. 
**Python example**
    
    
    handlers:
    - url: /youraccount/.*
      secure: always
      script: auto

To [ target a specific version of your app](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed) using the `REGION_ID.r.appspot.com` domain, you replace the periods that would usually separate the subdomain components of the URL with the string "`-dot-`", for example:  
`https://VERSION_ID-dot-default-dot-PROJECT_ID.REGION_ID.r.appspot.com` To use custom domains with HTTPS, you must first [ activate and configure SSL certificates for that domain](https://docs.cloud.google.com/appengine/docs/standard/securing-custom-domains-with-ssl).  Google Accounts sign-in and sign-out are always performed using a secure connection, unrelated to how the application's URLs are configured.   
`static_dir` |  Optional. The path to the directory containing the static files, from the application root directory. Everything after the end of the matched `url` pattern is appended to `static_dir` to form the full path to the requested file.  Each file in the static directory is served using the MIME type that corresponds with its filename extension unless overridden by the directory's `mime_type` setting. All of the files in the given directory are uploaded as static files, and none of them can be run as scripts.  **Example:**
    
    
    handlers:
    # All URLs beginning with /stylesheets are treated as paths to
    # static files in the stylesheets/ directory.
    - url: /stylesheets
      static_dir: stylesheets
      # ...  
  
`static_files` |  Optional. A static file pattern handler associates a URL pattern with paths to static files uploaded with the application. The URL pattern regular expression can define regular expression groupings to be used in the construction of the file path. You can use this instead of `static_dir` to map to specific files in a directory structure without mapping the entire directory.  **Example:**
    
    
    handlers:
    # All URLs ending in .gif .png or .jpg are treated as paths to
    # static files in the static/ directory. The URL pattern is a
    # regular expression, with a grouping that is inserted into the
    # path to the file.
    - url: /(.*\.(gif|png|jpg))$
      static_files: static/\1
      upload: static/.*\.(gif|png|jpg)$
      # ...

Static files cannot be the same as application code files.   
`upload` |  Optional. A regular expression that matches the file paths for all files that will be referenced by this handler. This is necessary because the handler cannot determine which files in your application directory correspond with the given `url` and `static_files` patterns. Static files are uploaded and handled separately from application files. The example above might use the following `upload` pattern: `archives/(.*)/items/(.*)`  
`url` |  Required element under `handlers`. The URL pattern, as a regular expression that can contain groupings. For example, `/profile/(.*)/(.*)` would match the URL `/profile/edit/manager` and use `edit` and `manager` as the first and second groupings.  The URL pattern has some differences in behavior when used with the following elements: 

`static_dir`
     Uses a URL prefix. The regular express pattern should not contain groupings when used with the `static_dir` element. All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path. 
`static_files`
     A static file pattern handler associates a URL pattern with paths to static files uploaded with the application. The URL pattern regular expression can define regular expression groupings to be used in the construction of the file path. You can use this instead of `static_dir` to map to specific files in a directory structure without mapping the entire directory.   
  
### Scaling elements

The elements in following table configure how your application scales. If no scaling type is specified, then automatic scaling is set by default.

To learn more about how App Engine apps scale, see [Scaling types](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#scaling_types).

Element | Description  
---|---  
`automatic_scaling` |  Optional. Applicable only for applications that use an [instance class](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#instance_class) of F1 or higher. Specify this element to change default settings for automatic scaling, such as setting minimum and maximum levels for number of instances, latency, and concurrent connections for a service.  This element can contain the following elements: 

`max_instances`
     Optional. Specify a value between 0 and 2147483647, where zero disables the setting. **Note:** For new projects you create after March 2025, App Engine sets the maximum instances default for standard environment deployments to 20\. This change doesn't impact existing apps. To override the default, specify a new value between `0` and `2147483647`, and deploy a new version or redeploy over an existing version. To disable the maximum instances default configuration setting, specify the maximum permitted value `2147483647`. This parameter specifies the maximum number of instances for App Engine to create for this module version. This is useful to limit the costs of a module. 
`min_instances`
     **Warning:** For this feature to function properly, you must make sure that [warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests) are enabled and that your application handles warmup requests. **Note:** This setting applies only if the version of the app defined by this `app.yaml` file is configured to receive traffic. To learn more about routing traffic to different versions of an app, see [ Splitting Traffic](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic).  Optional. The minimum number of instances for App Engine to create for this module version. These instances serve traffic when requests arrive, and continue to serve traffic even when additional instances are started up as required to handle traffic. Specify a value from 0 to 1000. You can set the parameter to the value 0 to allow scaling to 0 instances to lower costs when no requests are being served. Note that you are charged for the number of instances specified whether they are receiving traffic or not.
`max_idle_instances`
     Optional. The maximum number of idle instances that App Engine should maintain for this version. Specify a value from 1 to 1000. If not specified, the default value is `automatic`, which means App Engine will manage the number of idle instances. Keep the following in mind:

  * A high maximum reduces the number of idle instances more gradually when load levels return to normal after a spike. This helps your application maintain steady performance through fluctuations in request load, but also raises the number of idle instances (and consequent running costs) during such periods of heavy load. 
  * A low maximum keeps running costs lower, but can degrade performance in the face of volatile load levels. 

**Note:** When settling back to normal levels after a load spike, the number of idle instances can temporarily exceed your specified maximum. However, you will not be charged for more instances than the maximum number you've specified. 
`min_idle_instances`
     **Warning:** For this feature to function properly, you must make sure that [warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests) are enabled and that your application handles warmup requests. **Note:** This setting applies only if the version of the app defined by this `app.yaml` file is configured to receive traffic. To learn more about routing traffic to different versions of an app, see [ Splitting Traffic](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic).  Optional: The number of additional instances to be kept running and ready to serve traffic for this version.  App Engine calculates the number of instances necessary to serve your current application traffic based on scaling settings such as `target_cpu_utilization` and `target_throughput_utilization`. Setting `min_idle_instances` specifies the number of instances to run _in addition to_ this calculated number. For example, if App Engine calculates that 5 instances are necessary to serve traffic, and `min_idle_instances` is set to 2, App Engine will run 7 instances (5, calculated based on traffic, plus 2 additional per `min_idle_instances`).  Note that you are charged for the number of instances specified whether they are receiving traffic or not. Keep the following in mind: 

  * A low minimum helps keep your running costs down during idle periods, but means that fewer instances might be immediately available to respond to a sudden load spike. 
  * A high minimum allows you to prime the application for rapid spikes in request load. App Engine keeps the minimum number of instances running to serve incoming requests. You are charged for the number of instances specified, whether or not they are handling requests.  If you set a minimum number of idle instances, pending latency will have less effect on your application's performance. 


`target_cpu_utilization`
     Optional. Specify a value between 0.5 and 0.95. The default is `0.6`. This parameter specifies the CPU usage threshold at which new instances will be started to handle traffic, enabling you to balance between performance and cost, with lower values increasing performance and increasing cost, and higher values decreasing performance but also decreasing cost. For example, a value of 0.7 means that new instances will be started after CPU usage reaches 70 percent.
`target_throughput_utilization`
     Optional. Specify a value from 0.5 to 0.95. The default is `0.6`. Used with `max_concurrent_requests` to specify when a new instance is started due to concurrent requests. When the number of concurrent requests reaches a value equal to `max_concurrent_requests` times `target_throughput_utilization`, the scheduler tries to start a new instance.
`max_concurrent_requests`
     Optional. The number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance (Default: 10, Maximum: 1000).  Used with `target_throughput_utilization` to specify when a new instance is started due to concurrent requests. When the number of concurrent requests reaches a value equal to `max_concurrent_requests` times `target_throughput_utilization`, the scheduler tries to start a new instance.  We recommend you **do not set`max_concurrent_requests` to less than 10** unless you need single threading. A value of less than 10 is likely to result in more instances being created than you need for a threadsafe app, and that may lead to unnecessary cost.  If this setting is too high, you might experience increased API latency. Note that the scheduler might spawn a new instance before the actual maximum number of requests is reached. 
`max_pending_latency`
     The maximum amount of time that App Engine should allow a request to wait in the pending queue before starting additional instances to handle requests so that pending latency is reduced. When this threshold is reached, it is a signal to scale up, and results in an increase in the number of instances. If not specified, the default value is `automatic`. This means requests can remain in the pending queue for up to 10s, the maximum [ pending request time limit](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#quotas_and_limits), before new instance starts are triggered.  A low maximum means App Engine will start new instances sooner for pending requests, improving performance but raising running costs.  A high maximum means users might wait longer for their requests to be served (if there are pending requests and no idle instances to serve them), but your application will cost less to run. 
`min_pending_latency`
     An optional element you can set to specify the minimum amount of time that App Engine should allow a request to wait in the pending queue before starting a new instance to handle it. Specifying a value can lower running costs but increase the time users must wait for their requests to be served.  For free apps, the default value is `500ms`. For paid apps, the default value is `0`.  This element works together with the `max_pending_latency` element to determine when App Engine creates new instances. If pending requests are in the queue: 

  * Less than the `min_pending_latency` you specify, App Engine will not create new instances.
  * More than `max_pending_latency`, App Engine will try to create a new instance.
  * Between the time specified by `min_pending_latency` and `max_pending_latency`, App Engine will try to reuse an existing instance. If no instances are able to process the request before `max_pending_latency`, App Engine will create a new instance.


**Example**
    
    
    automatic_scaling:
      target_cpu_utilization: 0.65
      min_instances: 5
      max_instances: 100
      min_pending_latency: 30ms
      max_pending_latency: automatic
      max_concurrent_requests: 50  
  
`basic_scaling` |  Applications that use an [instance class](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#instance_class) of B1 or higher must specify either this element or `manual_scaling`.  This element enables basic scaling of instance classes B1 and higher, can contain the following elements: 

`max_instances`
     Required. The maximum number of instances for App Engine to create for this service version. This is useful to limit the costs of a service. 
`idle_timeout`
     Optional. The instance will be shut down this amount of time after receiving its last request. The default is 5 minutes (`5m`). 
**Example**
    
    
    basic_scaling:
      max_instances: 11
      idle_timeout: 10m  
  
`manual_scaling` |  Applications that use an [instance class](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#instance_class) of B1 or higher must specify either this element or `basic_scaling`.  This element enables manual scaling of instance classes B1 and higher, and can contain the following element: 

`instances`
     The number of instances to assign to the service at the start. 
**Example**
    
    
    manual_scaling:
      instances: 5  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
