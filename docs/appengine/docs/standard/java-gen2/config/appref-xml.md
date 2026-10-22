---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml/
title: appengine-web.xml reference \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:31.777882+00:00
---

# appengine-web.xml reference  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  appengine-web.xml reference Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

**Note:** If you use legacy bundled services and want to upgrade to Java 25, you can choose to continue using `javax.servlet.*` APIs only if your apps run on Java Enterprise Edition 8 (EE 8). You must update your `appengine-web.xml` file if you choose to remain on EE 8. To learn more about your configuration options, see [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime).

You should use the `appengine-web.xml` file for configuring your app only if you are migrating an existing app from the App Engine Java 8 runtime to the latest supported Java version and you want to [use the legacy bundled services](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access). If you are using an `appengine-web.xml` in your project, the `app.yaml` is automatically generated for you at deployment.

App Engine Java applications use a configuration file, named `appengine-web.xml`, to specify information about your app and to identify which files in the app's `WAR` file are static files (like images) and which are resource files used by the application.

## Syntax

An App Engine Java app must have a file named `appengine-web.xml` in its WAR, in the directory `WEB-INF/`. This is an XML file whose root element is `<appengine-web-app>`.

You can find the Document Type Definition and schema specifications for the `appengine-web.xml` in the SDK's `docs/` directory.

**Note:** The standard `appengine-web.xml` file defines the default service. You will need to specify additional configuration parameters for each non-default service, which were formerly known as modules. These are described in the [overview of App Engine](https://docs.cloud.google.com/appengine/docs/standard). You can also apply these configuration parameters to the default service.Element | Description  
---|---  
`<application>` |  Not required if you deploy your app using Google Cloud SDK-based tooling, such as the `gcloud app deploy` command, IntelliJ plugins, Maven or Gradle plugins. The Google Cloud SDK-based tooling ignore this element and get the project ID from the gcloud config project property. Note that although you can override the project ID using the Google Cloud CLI, this sets a machine-wide project ID, which may cause confusion if you are developing multiple projects. The `<application>` element contains the application's project ID. This is the project ID you register when you create your project in the [Google Cloud console](https://console.cloud.google.com/).   
`app_engine_apis` |  Optional. Set this field to `true` to enable access to all the [bundled services](https://docs.cloud.google.com/appengine/docs/standard/services/overview?tab=java) for second-generation runtimes. If you set this field to `true` or `false`, then deployments succeed only when the `app_engine_bundled_services` setting is unspecified. We recommend using `app_engine_bundled_services` to specify the bundled services your app requires. This approach provides fine-grained control and improves security by minimizing exposure to unneeded services. Additionally, it ensures your app receives critical updates for the services it actually uses, making it maintainable.  
`app_engine_bundled_services` |  Optional. Configure this field to enable [access to specific bundled services](https://docs.cloud.google.com/appengine/docs/standard/services/overview?tab=java) for second-generation runtimes. You can't use this setting if you configure the `app_engine_apis` field. Specify any of the following supported bundled services with this setting:

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
    
    
    <app-engine-bundled-services>
      <api>datastore_v3</api>
      <api>memcache</api>
    </app-engine-bundled-services>

This example allows your application to use only Datastore and Memcache bundled services.  
`<entrypoint>` |  Optional and only for second-generation runtimes. Overrides the default entrypoint which is the process command line that boots the Java application. By default, the generated entrypoint for a F4 instance class (memory settings are calculated from the instance class) is equivalent to the following configuration: 
    
    
      <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
      <entrypoint>
       java
       -showversion -Xms32M -Xmx819M -XX:+UseG1GC -XX:+ParallelRefProcEnabled
       -XX:+PrintCommandLineFlags
       --add-opens java.base/java.lang=ALL-UNNAMED
       --add-opens java.base/java.nio.charset=ALL-UNNAMED
       --add-opens java.logging/java.util.logging=ALL-UNNAMED
       --add-opens java.base/java.util.concurrent=ALL-UNNAMED
       -Dclasspath.runtimebase=/base/java_runtime
       -Djava.class.path=/base/java_runtime/runtime-main.jar
       -Djava.library.path=/base/java_runtime:
       com/google/apphosting/runtime/JavaRuntimeMainWithDefaults
       --fixed_application_path=/workspace
       /base/java_runtime
      </entrypoint>
    </appengine-web-app>

You can modify the configuration to add extra JVM process flags or define your own process to boot. Notice that the application is deployed in the `/workspace` directory, while the runtime JARs are located under `/base/java_runtime` directory.  [ Learn how to customize the entry point for the Java runtime using environment variables](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access#default-entrypoint).   
`<async-session-persistence>` |  Optional. It's possible to reduce request latency by configuring your application to asynchronously write HTTP session data to the Datastore: 
    
    
    <async-session-persistence enabled="true" />

With async session persistence turned on, App Engine will submit a Task Queue task to write session data to the Datastore before writing the data to memcache. By default the task will be submitted to the `default` queue. If you'd like to use a different queue, add the `queue-name` attribute: 
    
    
      <async-session-persistence enabled="true" queue-name="myqueue"/>

Session data is always written synchronously to memcache. If a request tries to read the session data when memcache is not available (or the session data has been flushed), it will fail over to Datastore, which might not yet have the most recent session data. This means that asynchronous session persistence can cause your application to see stale session data. However, for most applications the latency benefit far outweighs the risk.   
`<auto-id-policy>` |  Optional. If you are [ setting entity identifiers automatically](https://docs.cloud.google.com/appengine/docs/standard/services/datastore/entities?tab=java), you can change the method employed by setting the auto ID policy. The following are valid options: 

`default`
     Default. Uses scattered auto IDs that are large well-distributed integers that are small enough to be represented by 64-bit floats. 
`legacy`
     The legacy option will be deprecated in a future release and will eventually be removed. For more information, see the [blog post announcing this change](http://googlecloudplatform.blogspot.com/2013/05/update-on-datastore-auto-ids.html).   
`<automatic-scaling>` |  Optional. For a full explanation, see the automatic scaling section.   
`<basic-scaling>` |  Optional. For a full explanation, see the basic scaling section.   
`<env-variables>` |  Optional. The `appengine-web.xml` file can define environment variables that are set when the application is running. 
    
    
    <env-variables>
    <env-var name="DEFAULT_ENCODING" value="UTF-8" />
    </env-variables>

To avoid conflicts with your local environment, the development server does not set environment variables based on this file, and requires that the local environment have these variables already set to matching values. 
    
    
    export DEFAULT_ENCODING="UTF-8"
    dev_appserver war

When deployed to App Engine, the environment is created with these variables already set.  To determine how long a connection remains inactive without any data transmission before the client closes it, configure an idle timeout using the following syntax: 
    
    
    <env-variables>
    <env-var name="APPENGINE_API_CALLS_IDLE_TIMEOUT_MS" value="TIMEOUT_IN_MS" />
    </env-variables>

Replace `TIMEOUT_IN_MS` with the required timeout in milliseconds. To match a 60-second overall request/URL Fetch deadline, set it to `60000`. Alternatively, setting it slightly less than the server-side timeout (often 60 seconds) might be beneficial, for example, `59000`. The current default is `58000` milliseconds.  This idle timeout configuration isn't the same as the overall request deadline for scaling, or the URL Fetch API deadline that you configure using `appengine.api.urlfetch.defaultDeadline`.  
`<inbound-services>` |  Optional. Before an application can receive email, the application must be configured to enable the service. You enable the service for a Java app by including an `<inbound-services>` section in the `appengine-web.xml` file.  The following inbound service is available:

`mail`
     Allows your application to [receive mail](https://docs.cloud.google.com/appengine/docs/standard/services/mail/receiving-mail-with-mail-api?tab=java).   
`<instance-class>` |  Optional. The instance class size for this module.  The following [instance classes](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) are available when specifying different scaling options: 

`automatic_scaling`
     When using automatic scaling, the F1, F2, F4, and F4_1G instance classes are available. 
     _Default:_ F1 is assigned if you don't specify an instance class along with the  `automatic_scaling` element. 
`basic_scaling`
     When using basic scaling, the B1, B2, B4, B4_1G, and B8 instance classes are available. 
     _Default:_ B2 is assigned if you don't specify a instance class along with the  `basic_scaling` element. 
`manual_scaling`
     When using manual scaling, the B1, B2, B4, B4_1G, and B8 instance classes are available. 
     _Default:_ B2 is assigned if you don't specify a instance class along with the  `manual_scaling` element.  **Note:** If `instance-class` is set to `F2` or higher, you can optimize your instances by setting `max-concurrent-requests` to a value higher than 10, which is the default. To find the optimal value, gradually increase it and monitor the performance of your application.   
`<manual-scaling>` |  Optional. For a full explanation, see the manual scaling section.   
`<precompilation-enabled>` |  Optional. App Engine uses a "precompilation" process with the Java bytecode of an app to enhance the performance of the app in the Java runtime environment. Precompiled code functions identically to the original bytecode.  If for some reason you prefer that your app not use precompilation, you can turn it off by adding the following to your `appengine-web.xml` file: 
    
    
    <precompilation-enabled>false</precompilation-enabled>  
  
`<module>` |  **Note:** Modules are now named [Services](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine) and services are still declared in `appengine-web.xml` files as modules, for example: `<module>service_name</module>`.  Required if creating a service. Optional for the default service. Each service and each version must have a name. A name can contain numbers, letters, and hyphens. It cannot be longer than 63 characters, start or end with a hyphen, and contain the string `-dot`. Choose a unique name for each service and each version. Don't reuse names between services and versions.  Also see service.   
`<public-root>` |  Optional. The `<public-root>` is a directory in your application that contains the static files for your application. When a request for a static file is made, the `<public-root>` for your application is prepended to the request path. This gives the path of an application file containing the content that is being requested.  The default `<public-root>` is `/`.  For example, the following would map the URL path `/index.html` to the application path `/static/index.html`: 
    
    
    <public-root>/static</public-root>  
  
`<resource-files>` |  Optional. The files listed in the `<resource-files>` element are accessible by the application code using the file system. These files are stored on the application servers with the app as opposed to how static files are stored and served.  The `<resource-files>` element can contain the following elements: 

`<include>`
     An `<include>` element designates the files as resource files and available to your application code. These files are only available to your code on a read-only basis and not for traffic serving. Including and excluding files. 
`<exclude>`
     Files and directories matching `<exclude>` patterns won't be uploaded or available to your application code. However, these files and directories will still be accessible to your application when running on the local Development Server. For more information, see Including and excluding files.  **Example:**
    
    
    <resource-files>
      <include path="/**.xml" />
      <exclude path="/feeds/**.xml" />
    </resource-files>

This example demonstrates how to designate all `.xml` files as resource files except those in the `feeds/` directory and all of its subdirectories. 
App Engine resource files are read using `java.io.File` or `javax.servlet.ServletContext.getResource/getResourceAsStream`. They aren't accessible with `Class.getResourceAsStream()`.   
`<runtime>` |  To use the latest supported Java version, you must specify this entry with the value `java25`.  **Example:**
    
    
    <runtime>java25</runtime>  
  
`<service>` |  Services were formerly known as modules. Defining a service as: `<service>service_name</service >` is supported only by [gcloud app](https://docs.cloud.google.com/sdk/gcloud/reference/app) commands.  
`<service-account>` |  Optional. The `<service-account>` element lets you specify a [user-managed service account](https://docs.cloud.google.com/appengine/docs/standard/user-managed-service-accounts) as the identity for the version. The specified service account will be used when accessing other Google Cloud services and executing tasks.  **Example:**
    
    
    <service-account>[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com</service-account>  
  
`<sessions-enabled>` |  Optional. App Engine includes an implementation of sessions, using [the servlet session interface](https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpSession.html). The implementation stores session data in Datastore for persistence, and also uses memcache for speed. As with most other servlet containers, the session attributes that are set with `session.setAttribute()` during the request are persisted at the end of the request.  This feature is off by default. To turn it on, add the following to `appengine-web.xml`:  **Example:**
    
    
    <sessions-enabled>true</sessions-enabled>

The implementation creates Datastore entities of the kind `_ah_SESSION`, and memcache entries using keys with a prefix of `_ahs`. You can delete these entities using the Dataflow template.  **Note** : Because App Engine stores session data in Datastore and memcache, all values stored in the session must implement the `java.io.Serializable` interface.  See  `async-session-persistence` element for reducing the latency of the storage of session data.   
`<ssl-enabled>` |  Optional. By default, any user can access any URL using either HTTP or HTTPS. You can configure an app to require HTTPS for certain URLs in the deployment descriptor. See [Deployment Descriptor: Secure URLs](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/webxml#Secure_URLs).  If you want to disallow the use of HTTPS for the application, put the following in the `appengine-web.xml` file: 
    
    
    <ssl-enabled>false</ssl-enabled>

There is no way to disallow HTTPS for some URL paths and not others in the Java runtime environment.   
`<static-error-handlers>` |  Optional. When certain errors occur, App Engine serves a generic error page. You can configure your app to serve a custom static file instead of these generic error pages, so long as the custom error data is less than 10 kilobytes. You can set up different static files to be served for each supported error code by specifying the files in your app's `appengine-web.xml` file. To serve custom error pages, add a `<static-error-handlers>` section to your `appengine-web.xml`, as ins this example: 
    
    
    <static-error-handlers>
      <handler file="default_error.html" />
      <handler file="over_quota.html" error-code="over_quota" />
    </static-error-handlers>

**Warning** : Make sure that the path to the error response file does not overlap with static file handler paths.  Each `file` entry indicates a static file that should be served in place of the generic error response. The `error-code` indicates which error code should cause the associated file to be served. Supported error codes are as follows: 

`over_quota`
     Indicates that the app has [exceeded a resource quota](https://docs.cloud.google.com/appengine/docs/quotas). 
`timeout`
     Served if a deadline is reached before there is a response from your app. 
The `error-code` is optional; if it's not specified, the given file is the default error response for your app.  You can optionally specify a `mime-type` to use when serving the custom error. See [a complete list of MIME types](http://www.iana.org/assignments/media-types/).   
`<static-files>` |  Optional. The `<static-files>` element specifies patterns that match file paths to include and exclude from the list of static files, overriding or amending the default behavior. Static file are served from dedicated servers and caches that are separate from the application servers and are useful for serving static content such as images, CSS stylesheets or JavaScript files.  The `<static-files>` element can contain the following elements: 

`<include>`
     An `<include>` element overrides the default behavior of including all non-JSP files. The `<include>` element can specify HTTP headers to use when responding to request for the specified resources. For more information, see Including and excluding files.  You can override the default static cache expiration by specifying the `expiration` attribute on the include element. The value is a string of numbers and units, separated by spaces, where units can be `d` for days, `h` for hours, `m` for minutes, and `s` for seconds. For example, `"4d 5h"` sets cache expiration to 4 days and 5 hours after the file is first requested. For more information, see [Cache expiration](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#static_cache_expiration). 
`<exclude>`
     Files and directories matching `<exclude>` patterns won't be uploaded when you deploy your app to App Engine. However, these files and directories will still be accessible to your application when running on the local Development Server. For more information, see Including and excluding files. 
**Example**
    
    
    <static-files>
      <include path="/my_static-files" >
        <http-header name="Access-Control-Allow-Origin"
                     value="http://example.org" />
      </include>
    </static-files>  
  
`<system-properties>` |  Optional. The `appengine-web.xml` file can define system properties and environment variables that are set when the application is running. 
    
    
    <system-properties>
      <property name="myapp.maximum-message-length" value="140" />
      <property name="myapp.notify-every-n-signups" value="1000" />
      <property name="myapp.notify-url"
                value="http://www.example.com/signupnotify" />
    </system-properties>
    
    <env-variables>
      <env-var name="DEFAULT_ENCODING" value="UTF-8" />
    </env-variables>

Optional. You can configure an HTTP connector for improving CPU and memory utilization. If your application interacts with Datastore or Task Queues operations, [set up monitoring](https://docs.cloud.google.com/appengine/docs/standard/monitoring-and-alerting-latency#setting_up_monitoring_and_alerting) to monitor performance and behavior impacts after enabling this feature. 
    
    
      <system-properties>
        <property name="appengine.use.httpconnector" value="true"/>
      </system-properties>

Optional. You can configure the underlying Java 17 runtime to work on EE 8, Java 21 on EE 10, or Java 25 on EE 11 using the following system property. For more information regarding EE support, see [Upgrade Java on a compatible Enterprise Edition (EE) version](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime#upgrade-java). 
    
    
      <system-properties>
        <property name="appengine.use.EE11" value="true"/><!--only for Java 25-->
      </system-properties>

Starting in Java 21, you can configure your Java web server to use virtual threads. For example: 
    
    
      <system-properties>
        <property name="appengine.use.virtualthreads" value="true"/>
      </system-properties>

For more information regarding thread support, see [Jetty 12 – Virtual Threads Support](https://webtide.com/jetty-12-virtual-threads-support/).   
`<url-stream-handler>` |  Optional. Possible values, `native` or `urlfetch`. The default value is `native`, which means that standard Java network classes use the standard Java HTTP(S) transport. To use this setting, you must enable billing for your app, or you will get exceptions, which are documented in [Issue requests](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests).  If you set `url-stream-handler` to `urlfetch`, [`URL.openConnection`](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html#openConnection--) and related methods will use URL Fetch for `http` and `https` transport.
    
    
    <url-stream-handler>urlfetch</url-stream-handler>  
  
`<version>` |  The `<version>` element contains the version identifier for the latest version of the app's code. The version identifier can contain lowercase letters, digits, and hyphens. It cannot begin with the prefix "ah-" and the names "default" and "latest" are reserved and cannot be used.  Version names should begin with a letter, to distinguish them from numeric instances which are always specified by a number. This avoids the ambiguity with URLs like `123.my-module.uc.r.appspot.com`, which can be interpreted two ways: If version "123" exists, the target will be version "123" of the given module. If that version does not exist, the target will be instance number 123 of the default version of the module.   
`<warmup-requests-enabled>` |  Optional. Default: true. Warmup requests are enabled by default for Java applications.  With [warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests?tab=java) enabled, the App Engine infrastructure issues `GET` requests to `/_ah/warmup`, initializing `<load-on-startup>` servlets, `ServletContextListeners`, and custom warmup servlets, which allow you to initialize your application's code as it requires. You might need to implement your own handler for `/_ah/warmup` depending on which of these methods you choose.  To disable warmup requests, specify `false` for this element: 
    
    
    <warmup-requests-enabled>false</warmup-requests-enabled>  
  
`<vpc-access-connector>` |  Optional. Configures your application to use a Serverless VPC Access connector, enabling the application to send requests to internal resources in your VPC network. Specify the fully-qualified name of a connector in the `<name>` element: 
    
    
    <vpc-access-connector>
      <name>projects/[PROJECT_ID]/locations/[REGION]/connectors/[CONNECTOR_NAME]</name>
    </vpc-access-connector>

For more information, see [Connecting to internal resources in a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc).   
  
### Scaling elements

The following table lists the options for defining how you can specify that your application should scale.

For a comparison of the performance features of the scaling types, see [Scaling dynamic instances](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#scaling_dynamic_instances).

Element | Description  
---|---  
`<automatic-scaling>` |  Optional. Automatic scaling is assumed by default with a default instance class of `F1` unless specified otherwise.  The `automatic_scaling` element sets minimum and maximum levels for number of instances, latency, and concurrent connections for a module.  This element can contain the following elements: 

`<target-cpu-utilization>`
     Optional. Specify a value from 0.5 to 0.95. This parameter specifies the CPU usage threshold at which new instances will be started to handle traffic, enabling you to balance between performance and cost, with lower values increasing performance and increasing cost, and higher values decreasing performance but also decreasing cost. For example, a value of 0.7 means that new instances will be started after CPU usage reaches 70 percent.
`<target-throughput-utilization>`
     Optional. Specify a value from 0.5 to 0.95. Used with `max-concurrent-requests` to specify when a new instance is started due to concurrent requests. When the number of concurrent requests reaches a value equal to `max-concurrent-requests` times `target-throughput-utilization`, the scheduler starts a new instance.
`<max-instances>`
     Optional. The maximum number of instances for App Engine to create for this application version. This is useful to limit the costs of a module. Specify a value between 0 and 2147483647. 
`<min-instances>`
     Optional. The minimum number of instances for App Engine to create for this module version. These instances serve traffic when requests arrive, and continue to serve traffic even when additional instances are started up as required to handle traffic. Specify a value from 0 to 1000. You can set the parameter to the value 0 to allow scaling to 0 instances to lower costs when no requests are being served. Note that you are charged for the number of instances specified whether they are receiving traffic or not.
`<max-concurrent-requests>`
     Optional. The number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance (Default: 10, Maximum: 80).  You might experience increased API latency if this setting is too high. Note that the scheduler might spawn a new instance before the actual maximum number of requests is reached.  **Note:** If `instance-class` is set to `F2` or higher, you can optimize your instances by setting `max-concurrent-requests` to a value higher than 10, which is the default. To find the optimal value, gradually increase it and monitor the performance of your application. 
`<max-idle-instances>`
     The maximum number of idle instances that App Engine should maintain for this version. The default value is "automatic." Keep the following in mind: 

  * A high maximum reduces the number of idle instances more gradually when load levels return to normal after a spike. This helps your application maintain steady performance through fluctuations in request load, but also raises the number of idle instances (and consequent running costs) during such periods of heavy load. 
  * A low maximum keeps running costs lower, but can degrade performance in the face of volatile load levels. 

**Note:** When settling back to normal levels after a load spike, the number of idle instances can temporarily exceed your specified maximum. However, you won't be charged for more instances than the maximum number you've specified. 
`<max-pending-latency>`
     The maximum amount of time that App Engine should allow a request to wait in the pending queue before starting additional instances to handle requests so that pending latency is reduced. 

  * A low maximum means App Engine will start new instances sooner for pending requests, improving performance but raising running costs. 
  * A high maximum means users might wait longer for their requests to be served, if there are pending requests and no idle instances to serve them, but your application will cost less to run. 


`<min-idle-instances>`
     The number of instances to be kept running and ready to serve traffic.This setting only applies to the version that receives most of the traffic. Keep the following in mind: 

  * A low minimum helps keep your running costs down during idle periods, but means that fewer instances might be immediately available to respond to a sudden load spike. 
  * A high minimum lets you prime the application for rapid spikes in request load. App Engine keeps the minimum number of instances running to serve incoming requests. You are charged for instances, whether or not they are handling requests. For this feature to function properly, you must make sure that [ warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests?tab=java) are enabled and that your application handles warmup requests.  If you set a minimum number of idle instances, pending latency will have less effect on your application's performance. Because App Engine keeps idle instances in reserve, it is unlikely that requests will enter the pending queue except in exceptionally high load spikes. You will need to test your application and expected traffic volume to determine the ideal number of instances to keep in reserve. 


`<min-pending-latency>`
     The minimum amount of time in seconds that App Engine should allow a request to wait in the pending queue before starting a new instance to handle it. Specify a value from 0.01 to 15. 

  * A low minimum means requests must spend less time in the pending queue when all existing instances are active. This improves performance but increases the cost of running your application. 
  * A high minimum means requests will remain pending longer if all existing instances are active. This lowers running costs but increases the time users must wait for their requests to be served. 


**Example**
    
    
    <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
      <application>simple-app</application>
      <module>default</module>
      <version>uno</version>
      <instance-class>F2</instance-class>
      <automatic-scaling>
        <target-cpu-utilization>0.65</target-cpu-utilization>
        <min-instances>5</min-instances>
        <max-instances>100</max-instances>
        <max-concurrent-requests>50</max-concurrent-requests>
      </automatic-scaling>
    </appengine-web-app>  
  
`<basic-scaling>` |  Optional. The `<basic-scaling>` element sets the number of instances for a module.  This element can contain the following elements: 

`<idle-timeout>`
     Optional. The instance will be shut down this amount of time after receiving its last request. The default is 5 minutes. 
`<max-instances>`
     Required. The maximum number of instances for App Engine to create for this module version. This is useful to limit the costs of a module. 
**Example**
    
    
    <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
      <application>simple-app</application>
      <module>default</module>
      <version>uno</version>
      <instance-class>B8</instance-class>
      <basic-scaling>
        <max-instances>11</max-instances>
        <idle-timeout>10m</idle-timeout>
      </basic-scaling>
    </appengine-web-app>  
  
`<manual-scaling>` |  Optional. The `<manual-scaling>` element enables manual scaling for a module and sets the number of instances for a module.  This element can contain the following elements: 

`<instances>`
     The number of instances to assign to the module at the start. 
**Example**
    
    
    <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
      <application>simple-app</application>
      <module>default</module>
      <version>uno</version>
      <instance-class>B8</instance-class>
      <manual-scaling>
        <instances>5</instances>
      </manual-scaling>
    </appengine-web-app>  
  
### Staging elements

Much of the work done during a deployment occurs locally in a preparation step called _staging_ , where JAR files are assembled, JSPs are compiled, and so forth. You can optionally configure certain parts of the staging behavior using staging elements in the application configuration file. Most applications will deploy successfully without manually configuring staging behavior. If your app doesn't deploy, you may need to configure staging using the options shown in the following table.

Element | Description  
---|---  
`<staging>` |  Optional. Most applications don't need to change default behavior.  The staging element lets you specify a particular staging configuration if needed for deployment.  This element can contain the following elements: 

`<enable-jar-splitting>`
     Optional. Split large jar files (> 10 Megabytes) into smaller fragments. (Default: true). 
`<jar-splitting-excludes>`
     Specifies a comma-separated list of file suffixes. If `enable-jar-splitting` is enabled, all files that match the suffixes will be excluded from all JARs. 
`<disable_jar_jsps>`
     Don't jar classes generated from JSPs. (Default: false). 
`<enable-jar-classes>`
     Jar the contents of WEB-INF/classes. (Default: true). 
`<delete-jsps>`
     Delete the JSP source files after compilation. (Default: true). 
`<compile-encoding>`
     Input encoding of source files for compilation. (Default: utf-8). 
For example:
    
    
            <staging>
              <delete-jsps>false</delete-jsps>
            </staging>
              
  
### Staging option defaults

The defaults for staging options are different depending on whether you use Google Cloud SDK-based tooling, such as the gcloud CLI, or the Google Cloud SDK-based [Maven](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/using-maven) or [Gradle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/using-gradle) plugins.

Staging element | App Engine SDK-based defaults - | Google Cloud SDK-based defaults  
---|---|---  
`enable-jar-splitting` | `false` | `true`  
`jar-splitting-excludes` | N/A | N/A  
`disable-jar-jsps` | `false` | `false`  
`enable-jar-classes` | `false` | `true`. This can impact class loading order, so if your app depends on a certain order using the former `false` default, you can set this to `false`.  
`delete-jsps` | `false` | `true`  
`compile-encoding` | `utf-8` | `utf-8`  
  
### Include and exclude syntax

Path patterns are specified using zero or more `<include>` and `<exclude>` elements. In a pattern, `'*'` represents zero or more of any character in a file or directory name, and `**` represents zero or more directories in a path. Files and directories matching `<exclude>` patterns won't be uploaded when you deploy your app to App Engine. However, these files and directories will still be accessible to your application when running on the local Development Server.

An `<include>` element overrides the default behavior of including all files. An `<exclude>` element applies after all `<include>` patterns (as well as the default if no explicit `<include>` is provided).

The following example demonstrates how to designate all `png` files as static files (except those in the `data/` directory and all of its subdirectories):
    
    
    <static-files>
      <include path="/**.png" />
      <exclude path="/data/**.png" />
    </static-files>
    

You can also set HTTP headers to use when responding to requests to these static resources.
    
    
    <static-files>
      <include path="/my_static-files" >
        <http-header name="Access-Control-Allow-Origin"
                     value="http://example.org" />
      </include>
    </static-files>
    

**Note:** If the `path` string doesn't start with a slash, then the HTTP headers, if any, work on App Engine but do **not** work on the Development Server.

## MIME types for static files

By default, static files are served using a MIME type selected based on the filename extension. You can associate custom MIME types with filename extensions for static files using `mime-mapping` elements in `web.xml`.

## URLFetch timeout

You can set a deadline for each [URLFetch](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests#setting_a_request_timeout) request. By default, the deadline for a fetch is 5 seconds. You can change this default by including the following setting in your `appengine-web.xml` configuration file. Specify the timeout in seconds:
    
    
    <system-properties>
        <property name="appengine.api.urlfetch.defaultDeadline" value="10"/>
    </system-properties>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
