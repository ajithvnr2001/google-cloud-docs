---
url: https://docs.cloud.google.com/appengine/migration-center/standard/java/migrate-java-logging/
title: Migrate logging to second-generation Java runtimes \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:17.684160+00:00
---

# Migrate logging to second-generation Java runtimes  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/java/migrate-java-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate logging to second-generation Java runtimes Stay organized with collections  Save and categorize content based on your preferences. 

Some aspects of logging in the [second-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) runtimes (Java 11+) are different from the first-generation runtime (Java 8). Unlike the first-generation runtime, in the second-generation runtimes, app logs are not grouped under request logs within the Logs Explorer. Additionally, in the second-generation runtimes, App Engine writes each app log associated with a request as a separate log entry in Cloud Logging.

This guide describes how you can implement the same logging methods you used in your first-generation runtime apps, and achieve nearly the same filtering and logging correlation results when migrating your app to Java 11+.

## Key differences

The following table covers differences in logging between first- and second-generation runtimes:

| **First-generation runtime (Java 8)** | **Second-generation runtimes (Java 11+)**  
---|---|---  
Request and app logs (also called application logs) |  App Engine embeds all app logs within the request log. |  App Engine doesn't embed app logs within the request log.   
`stdout` and `stderr` | App Engine embeds logs written to `stdout` and `stderr` within the request log. | App Engine doesn't embed logs written to `stdout` and `stderr`.   
App Engine platform logs | App Engine doesn't emit internal platform logs. | App Engine emits internal platform logs during startup or shutdown of an instance with the log name `/var/log/google_init.log`.   
Cloud Logging API quota |  Each request corresponds to one [Cloud Logging write](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).  |  Each app log entry associated with a request corresponds to one Cloud Logging write. The Cloud Logging API usage increases in the second-generation runtimes.   
  
### Request logs and app logs

The logging behavior in first-generation and second-generation runtimes differ in the following ways:

  * In the **first-generation** runtime, App Engine embeds app logs in the `protoPayload.line` field of the request logs. You can view app logs by expanding a request in the Logs Explorer.

The following image shows correlated request and app logs in the first-generation runtime:

![Correlated logs in Java 8](https://docs.cloud.google.com/static/appengine/docs/images/logging/java/Java8_logs_correlated.png)

  * In the **second-generation** runtimes, request logs don't contain app log entries because the `protoPayload.line` field is absent in the request log. Instead, App Engine logs each app log as a separate entry. The log name depends on your logging setup. `var/log/app` contains logs emitted using standard logging frameworks such as, `java.util.logging` or the Simple Logging Facade for Java (SLF4J). The `stderr` and `stdout` logs contain app logs that are logged using `System.err.print()` or `System.out.print()`.

The following image shows separate request and app logs in the second-generation runtimes:

![Separate logs in Java 11](https://docs.cloud.google.com/static/appengine/docs/images/logging/java/Java11_logs_separate.png)




### `stdout` and `stderr`

In the first-generation runtime, App Engine considers logs emitted to `stdout` and `stderr` as app logs, and automatically groups these app log entries under the associated request log.

In the second-generation runtimes, App Engine doesn't correlate logs emitted to `stdout` and `stderr` by default. To group app log entities with the request log using `stdout` and `stderr`, follow the instructions in [Write structured logs to `stdout` and `stderr`](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs#stdout_stderr).

We don't recommend logging to `stdout` and `stderr` since certain App Engine platform logs (JVM, Jetty, internal infrastructure logs) are also emitted to `stderr`. App logs and platform logs appear together with the `stderr` log name, which causes ambiguity. This is exaggerated in second-generation runtimes since App Engine has a higher volume of platform logs.

### App Engine platform logs

In the first-generation runtime, App Engine doesn't emit platform logs.

In the second generation runtimes, App Engine emits platform logs during instance startup or shutdown with the log name `/var/log/google_init.log`.

You can safely ignore the platform logs. To avoid seeing these logs, add a filter to the Logs Explorer with the query `logName="/var/log/google_init.log"`.

The following image displays platform logs in the second-generation runtimes:

![Platform logs](https://docs.cloud.google.com/static/appengine/docs/images/logging/java/platform_logs.png)

### Cloud Logging API quota

In the first-generation runtime, App Engine embeds all the app logs emitted during a request into a single request log, and sends the embedded request to Cloud Logging. Each request corresponds to one [Cloud Logging write](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).

In the second-generation runtimes, App Engine sends each app log to Cloud Logging in separate log entries, causing an increase in the total number of Cloud Logging writes per request.

Google Cloud determines billing based on the overall storage that Cloud Logging uses. Even if the overall storage required for logs don't increase significantly, the writes per minute increase, depending on how many app logs App Engine writes per request. If your app exceeds the Cloud Logging [write quota](https://docs.cloud.google.com/logging/quotas#api-limits), you can [request an increase](https://docs.cloud.google.com/logging/quotas#more-quota) in your usage quota.

For more information, see [pricing](https://cloud.google.com/stackdriver/pricing) for Cloud Logging.

## Overview of the migration process

Even if app logs aren't embedded within the request logs in the second-generation runtimes, it is possible to retain the log viewing experience like the first-generation apps.

You can choose one of the following options for setting up logging in the second-generation runtimes:

  * Use the `java.util.logging` (JUL) package: App Engine has built-in support for correlating request and app logs with a trace ID. If the trace ID is present in app logs, Logs Explorer renders app logs grouped within a request log.

  * Use the Simple Logging Facade for Java (SLF4J): You must modify your source code to add the trace ID depending on the following logging backend your app uses:

    * SLF4J with `java.util.logging` package
    * SLF4J with Logback appender



### Use the `java.util.logging` (JUL) package

If your apps using the first-generation runtime implement the `java.util.logging` package for all the logging requirements, migrating to second-generation runtimes require no code changes.

The following sample shows how you can use the `java.util.logging` package for logging in the second-generation runtimes:
    
    
        package com.example.appengine.my_app;
        import java.io.IOException;
        import javax.servlet.annotation.WebServlet;
        import javax.servlet.http.*;
        import java.util.logging.Logger;
    
        @WebServlet(name = "HelloAppEngine", value = "/")
        public class HelloAppEngine extends HttpServlet {
    
          // Use the java.util.logging.Logger to log messages
          private static final Logger logger = Logger.getLogger(HelloAppEngine.class.getName());
    
          @Override
          public void doGet(HttpServletRequest request, HttpServletResponse response)
              throws IOException {
            // Sample log messages
            logger.info("Info message");
            logger.warning("Warning message");
            logger.severe("Severe message");
    
            response.setContentType("text/plain");
            response.getWriter().println("Hello App Engine");
          }
        }
    

#### Group app logs with the request log

In the second-generation runtimes, the `protoPayload.line` field in the request log doesn't contain app logs. The Logs Explorer uses the `trace` field to group request logs and app logs. The `java.util.logging` package automatically adds the trace ID to all request and app logs. To view correlated logs in the Logs Explorer, see View correlated logs.

### Use the Simple Logging Facade for Java (SLF4J)

SLF4J is the most popular logging interface used in Java applications. Being a facade, the SLF4J interface is platform-independent of its logging backend, enabling you to choose any backend suitable for your apps.

The following image shows integration options for two SLF4J backends including the `java.util.logging` library and the Logback appender:

![SLF4J overview](https://docs.cloud.google.com/static/appengine/docs/images/logging/java/migrate_with_SLF4J.png)

#### SLF4J with `java.util.logging` package

SLF4J lets you integrate your app with Cloud Logging when you use SLF4J with `java.util.logging` as the logging backend. By default, App Engine adds a trace ID to all request and app logs. This mechanism enables the grouping of request and app logs in the Logs Explorer.

To implement SLF4J with `java.util.logging`, follow these steps:

  1. Add the `slf4j-jdk14.jar` dependency to your `pom.xml` file. The `slf4j-jdk14.jar` file provides the backend integration for the `java.util.logging` library:
         
         <!-- SLF4J interface -->
         <dependency>
           <groupId>org.slf4j</groupId>
           <artifactId>slf4j-api</artifactId>
           <version>2.0.4</version>
         </dependency>
         <!-- JUL implementation for SLF4J -->
         <dependency>
           <groupId>org.slf4j</groupId>
           <artifactId>slf4j-jdk14</artifactId>
           <version>2.0.9</version>
         </dependency>
         

  2. Create a `WEB-INF/logging.properties` file to add custom configurations:
         
         com.example.appengine.java8.HelloAppEngine.level = INFO
         

  3. Update your `appengine-web.xml` file to include the `<property>` value for `WEB-INF/logging.properties`:
         
         <system-properties>
           <property name="java.util.logging.config.file" value="WEB-INF/logging.properties"/>
         </system-properties>
         




The following image shows how SLF4J with `java.util.logging` automatically adds the trace ID to an app log:

![Group app logs by request with trace ID](https://docs.cloud.google.com/static/appengine/docs/images/logging/java/identify_requests.png)

To tune your Logs Explorer view to a request-centric view like the first-generation runtime, see View correlated logs.

#### Use SLF4J with Logback appender

If your first-generation runtime apps use the built-in implementation of SLF4J with [Logback](https://logback.qos.ch/), you must update your source code, and implement additional steps to group request and app logs.

To integrate your app with Cloud Logging, follow these steps:

  1. Add the `google-cloud-logging-logback` appender to your `pom.xml` file to install the logging appender for Logback:
         
         <!-- SLF4J interface -->
          <dependency>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-api</artifactId>
                <version>2.0.4</version>
          </dependency>
         
          <!-- Logback JARs -->
          <dependency>
                <groupId>ch.qos.logback</groupId>
                <artifactId>logback-classic</artifactId>
                <version>1.3.6</version>
          </dependency>
          <dependency>
                <groupId>ch.qos.logback</groupId>
                <artifactId>logback-core</artifactId>
                <version>1.3.5</version>
          </dependency>
         
          <!-- Google Cloud logging appender for Logback -->
          <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>google-cloud-logging-logback</artifactId>
          </dependency>
         

  2. Create a logging enhancer to add a trace ID to each `LogEntry` field. The following `TraceIdLoggingEnhancer` class uses the [ApiProxy API](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy) to retrieve the trace ID associated with a request:
         
         import com.google.appengine.api.utils.[SystemProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty.html);
           import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
           import com.google.cloud.logging.[LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer.html);
         
           import com.google.apphosting.api.[ApiProxy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.html);
           import com.google.apphosting.api.[ApiProxy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.html).Environment;
         
           // Add trace ID to the log entry
           public class TraceIdLoggingEnhancer implements [LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer.html) {
         
             @Override
             public void enhanceLogEntry([LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html).Builder logEntry) {
               final String PROJECT_ID = [SystemProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty.html).applicationId.get();
         
               Environment environment = [ApiProxy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.html).[getCurrentEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.html#com_google_apphosting_api_ApiProxy_getCurrentEnvironment__)();
         
               if (environment instanceof [ApiProxy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.html).[EnvironmentWithTrace](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.EnvironmentWithTrace.html)) {
                 [ApiProxy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.html).[EnvironmentWithTrace](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.EnvironmentWithTrace.html) environmentWithTrace = ([ApiProxy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.html).[EnvironmentWithTrace](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.EnvironmentWithTrace.html)) environment;
                 environmentWithTrace
                     .getTraceId()
                     .ifPresent(
                         id ->
                           logEntry.[setTrace](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.Builder.html#com_google_cloud_logging_LogEntry_Builder_setTrace_java_lang_Object_)(String.format("projects/%s/traces/%s", PROJECT_ID, id)));
               }
             }
           }
           // [END logging_enhancer]
         

  3. Add the Cloud Logging appender configuration in `logback.xml` file to configure the Logback. The Logback framework manages configuration through the `logback.xml` file in the `WEB-INF/classes`:
         
         <configuration>
           <appender name="CLOUD" class="com.google.cloud.logging.logback.LoggingAppender">
               <!-- This should be set to the new Logging Enhancer in the app code. -->
               <enhancer>com.example.appengine.my_app.enhancers.TraceIdLoggingEnhancer</enhancer>
               <resourceType>gae_app</resourceType>
           </appender>
           <root level="info">
               <appender-ref ref="CLOUD" />
           </root>
         </configuration>
         

The following image shows the final app directory structure:

![Directory structure](https://docs.cloud.google.com/static/appengine/docs/images/logging/java/directory_structure.png)




## View correlated logs

You can view correlated logs in the Logs Explorer using the trace ID field in each log entry. To view correlated logs in the Logs Explorer:

  1. In the navigation panel of the Google Cloud console, select **Logging** , and then select **Logs Explorer** :

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In **Resource Type** , select **GAE Application**.

  3. To view and correlate request logs, in **Log Name** , select **request_log**. Alternatively, to correlate by request logs, click **Correlate by** and select **request_log** :

![Correlating logs](https://docs.cloud.google.com/static/appengine/docs/images/logging/java/group_logs.png)

  4. In the **Query results** pane, to expand a log entry, click **Expand**. On expanding, each request log will show the associated app logs.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
