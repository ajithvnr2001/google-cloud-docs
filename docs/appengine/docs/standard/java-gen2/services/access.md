---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access/
title: Access legacy bundled services for Java 11+ \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:45.442770+00:00
---

# Access legacy bundled services for Java 11+  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Access legacy bundled services for Java 11+ Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to install and use the bundled services with the latest supported [Java version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java) for the App Engine standard environment. Your app can access the bundled services through the **App Engine API JAR**.

## Before you begin

  * Refer to the [list of legacy bundled services APIs](https://docs.cloud.google.com/appengine/docs/standard/services/overview) you can call in the latest supported Java version.

  * This page requires that your app is running a [supported](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/\(/appengine/docs/standard/lifecycle/support-schedule#java\)) Java version. To migrate your app from the first-generation to the second-generation runtime, see [Migrate from Java 8 to the latest Java runtime](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences) and the migration considerations section.

  * If you use legacy bundled services and want to upgrade to Java 25, see [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime) to learn more about your configuration options.




## Install the App Engine API JAR

To use legacy bundled services in your latest supported Java app, you must use an [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml) file to configure your app (instead of an `app.yaml` file).

The following example demonstrates how to add configuration settings in your `appengine-web.xml` for different Java versions. To use the latest supported version on the default configuration, you must update your application servlets and dependencies to include the `Jakarta` namespace. To learn more about your configuration options, see [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime).

Add the following settings in your `appengine-web.xml` file depending on the Java version This example allows your application to use only Datastore and Memcache bundled services:

###  Java 25 (EE 11) 
    
    
      <?xml version="1.0" encoding="utf-8"?>
      <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
          <runtime>java25</runtime>
          <system-properties>
            <property name="appengine.use.EE11" value="true"/>
          </system-properties>
          <app-engine-bundled-services>
            <api>datastore_v3</api>
            <api>memcache</api>
            <!-- LIST YOUR SERVICES -->
          </app-engine-bundled-services>
      </appengine-web-app>
    

###  Java 21 (EE 10) 
    
    
      <?xml version="1.0" encoding="utf-8"?>
      <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
          <runtime>java21</runtime>
          <system-properties>
            <property name="appengine.use.EE10" value="true"/>
          </system-properties>
          <app-engine-bundled-services>
            <api>datastore_v3</api>
            <api>memcache</api>
            <!-- LIST YOUR SERVICES -->
          </app-engine-bundled-services>
      </appengine-web-app>
    

###  Java 17 (EE 8) 
    
    
      <?xml version="1.0" encoding="utf-8"?>
      <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
          <runtime>java17</runtime>
          <system-properties>
            <property name="appengine.use.EE8" value="true"/>
          </system-properties>
          <app-engine-bundled-services>
            <api>datastore_v3</api>
            <api>memcache</api>
            <!-- LIST YOUR SERVICES -->
          </app-engine-bundled-services>
      </appengine-web-app>
    

To specify the legacy bundled services as a dependency, add the following lines in your `pom.xml` file:
    
    
     <dependency>
        <groupId>com.google.appengine</groupId>
        <artifactId>appengine-api-1.0-sdk</artifactId>
        <version>2.0.31</version> <!-- or later-->
      </dependency>
    

If your app uses a `web.xml` file, configure the `<app-engine-bundled-service>` element. For `app_engine_bundled_services` configuration settings, see the [`web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/webxml#app_engine_bundled_services) file reference.
    
    
    <app-engine-bundled-services>
      <api>memcache</api>
      <api>datastore_v3</api>
      <api>modules</api>
      <api>search</api>
      <api><!-- LIST YOUR SERVICES --></api>
    </app-engine-bundled-services>
    

To deploy your Java 25 app, run the [`mvn appengine:deploy`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/maven-reference) command, or the [`gcloud app deploy ~/my_app/WEB-INF/appengine-web.xml`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command on a compiled and staged web application.

## Default entrypoint for Java 25

Java 25 applications benefit from extra user configuration when starting the JVM for web applications.

The default entrypoint used to boot the JVM is generated by App Engine buildpacks. Essentially, it is equivalent to define this entrypoint in the `appengine-web.xml` file. For example:
    
    
    java --add-opens java.base/java.lang=ALL-UNNAMED  --add-opens java.base/java.nio.charset=ALL-UNNAMED -showversion -Xms32M -Xmx204M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:+PrintCommandLineFlags -Dclasspath.runtimebase=/base/java_runtime -Djava.class.path=/base/java_runtime/runtime-main.jar -Djava.library.path=/base/java_runtime: com/google/apphosting/runtime/JavaRuntimeMainWithDefaults --fixed_application_path=/workspace /base/java_runtime

We don't recommend changing this default entrypoint as the memory settings are calculated based on the instance type (F1, F2, F4) and memory available.

By default, we use `--add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.nio.charset=ALL-UNNAMED` to open some necessary JDK APIs.

## Entry Point Features

The entry point for the [second-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) Java versions can be customized with user-defined environment variables added in the `appengine-web.xml` configuration file.

The following table indicates the environment variables that can be used to enable/disable/configure features, and the default values if they are not set:

Env Var | Description | Type | Default  
---|---|---|---  
`CPROF_ENABLE` | Stackdriver Profiler | boolean | `false`  
`GAE_MEMORY_MB` | Available memory | size | Set by App Engine or `/proc/meminfo`-400M  
`HEAP_SIZE_RATIO` | Memory for the heap | percent | 80  
`HEAP_SIZE_MB` | Available heap | size | `${HEAP_SIZE_RATIO}`% of `${GAE_MEMORY_MB}`  
`JAVA_HEAP_OPTS` | JVM heap args | JVM args | `-Xms${HEAP_SIZE_MB}M -Xmx${HEAP_SIZE_MB}M`  
`JAVA_GC_OPTS` | JVM GC args | JVM args | `-XX:+UseG1GC` plus configuration  
`JAVA_USER_OPTS` | JVM other args | JVM args |   
`JAVA_OPTS` | JVM args | JVM args | See below  
  
If not explicitly set, `JAVA_OPTS` is defaulted to:
    
    
       JAVA_OPTS:=-showversion \
                  $JAVA_HEAP_OPTS \
                  $JAVA_GC_OPTS \
                  $JAVA_USER_OPTS
    

When `CPROF_ENABLE` is true, the default entrypoint adds the `PROFILER_AGENT` as:

`-agentpath:/opt/cprof/profiler_java_agent.so=--logtostderr`

For example, if your application code needs more `-add-opens` flags, you can use the `JAVA_USER_OPTS` environment variable defined in the `appengine-web.xml` file:
    
    
        <env-variables>
           <env-var name="JAVA_USER_OPTS" value="--add-opens java.base/java.util=ALL-UNNAMED" />
         </env-variables>
    

## Migration considerations

You should be aware of the following considerations if you are migrating to a second-generation Java runtime and your app uses legacy bundled services:

  * To test the legacy bundled services capabilities in your second-generation Java app, you can use the [local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server).
  * Unlike the Java 8 runtime, the second-generation Java runtimes include JVM as part of the instance memory. If you see memory-related errors in the logs, consider increasing the instance class size in your [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#syntax) file.
  * If your application is trying to call an API which is not enabled for the second-generation Java runtimes, it will receive a `com.google.apphosting.api.ApiProxy$FeatureNotEnabledException` error.
  * All applications are assumed to be thread safe in the second-generation Java runtimes. You must remove the `threadsafe` element in your `app.yaml` or `appengine-web.xml` file when [Migrate from Java 8 to the latest Java runtime](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences#key-differences).



## Example (Datastore)

For an example of how to use Firestore in Datastore mode (Datastore), see the legacy bundled services for Java 11 [code sample in GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/main/appengine-java11-bundled-services/datastore).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
