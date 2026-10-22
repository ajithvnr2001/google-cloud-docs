---
url: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences/
title: Migrate from Java 8 to the latest Java runtime \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:47.278052+00:00
---

# Migrate from Java 8 to the latest Java runtime  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate from Java 8 to the latest Java runtime Stay organized with collections  Save and categorize content based on your preferences. 

This page covers instructions for migrating from the [first-generation to the second-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) Java runtimes. To upgrade your second-generation app to use the latest supported version of Java, see [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime).

Java 8 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated). You won't be able to deploy Java 8 applications, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing Java 8 applications will continue to run and receive traffic. We recommend that you migrate to the [latest supported version of Java](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java).

Migrating to the [second-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) Java runtimes, allow you to use up-to-date language features and build apps that are more portable, with idiomatic code.

## Understanding your migration options

To reduce runtime migration effort and complexity, the App Engine standard environment lets you access many of legacy bundled services and APIs, such as Memcache, in the second-generation Java runtimes. Your Java app can call the bundled services APIs through the App Engine API JAR, and access most of the same capabilities as on the Java 8 runtime.

**Note:** Not all the App Engine bundled services available for Java 8 have a corresponding service in the second-generation Java runtimes. For the full list of legacy bundled services APIs available for the second-generation Java runtimes, see the [legacy bundled services API references documentation](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled).

You also have the option to use Google Cloud products that offer similar functionality as the legacy bundled services. These Google Cloud products provide idiomatic [Cloud Client Libraries for Java](https://github.com/googleapis/google-cloud-java). For the bundled services that are not available as separate products in Google Cloud, such as image processing, search, and messaging, you can use third-party providers or other workarounds.

To learn more about migrating to unbundled services, see [Migrating from bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).

There are some differences in how you perform the runtime migration, based on whether you choose to use legacy bundled services:

Migrating to the second-generation Java runtimes with bundled services  |  Migrating to the second-generation Java runtimes without bundled services   
---|---  
[Access bundled services using the App Engine APIs JAR](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access). | Optionally, use [ recommended Google Cloud products or third-party services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).   
Use [ `appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml) and [ `web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/webxml) for app configuration. In your `appengine-web.xml` and `web.xml` files, configure the `app-engine-bundled-services` field to enable [access to specific bundled services](https://docs.cloud.google.com/appengine/docs/standard/services/overview?tab=java). You might also need to configure additional YAML files depending on the features your app uses. |  Use [ `app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/configuring-your-app-with-app-yaml) for app configuration. You might also need to configure additional YAML files depending on the features your app uses.  
Apps are deployed via Jetty. Use WAR format to package your app.  | Apps are deployed using your own server. Use JAR format to package your app. To learn more about converting your existing WAR file to an executable JAR, see [Re-packaging a WAR file](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/war-packaging).   
  
## Overview of the migration process

The following lists some changes you might have to make to your existing App Engine Java 8 app and your [deployment process](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app) in order to use the second-generation Java runtimes:

  * [Download Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).
  * Migrate from the standalone App Engine Maven plugin to the [gcloud CLI-based Maven plugin](https://docs.cloud.google.com/appengine/docs/standard/java/tools/migrate-maven) or the [gcloud CLI-based Gradle plugin](https://docs.cloud.google.com/appengine/docs/standard/java/tools/migrate-gradle).
  * [Install the App Engine API JAR if you are using the legacy bundled services.](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access#installing)
  * Migrate your XML files to the equivalent `yaml` files.

**Note:** If you are planning to use the [App Engine legacy bundled services](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access) for the second-generation Java runtimes, you must maintain an [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml) file (rather than `app.yaml`) to configure your second-generation Java runtime apps.



## Key differences between the Java 8 and the second-generation Java runtimes

The following is a summary of the differences between the Java 8 and the second-generation Java runtimes on the App Engine standard environment:

| Java 8 runtime | Second-generation Java runtimes  
---|---|---  
Server deployment  | Server deployed for you using Jetty  | If your app does not use the legacy bundled services, you have to deploy a server yourself.1  
App Engine legacy bundled services  | Provided  | Provided   
Ability to use Cloud Client Libraries for Java  | Yes  | Yes   
Language extension and system library support  | Yes  | Yes   
External network access  | Yes  | Yes   
Files system access  | Read/write access to `/tmp` | Read/write access to `/tmp`  
Language runtime  | Modified for App Engine  | Unmodified, open-source runtime   
Isolation mechanism  | [gVisor-based](https://github.com/google/gvisor) container sandbox  | [gVisor-based](https://github.com/google/gvisor) container sandbox   
Testing with local development server  | Supported  | Supported   
Thread safety configuration  | Can be specified in the `appengine-web.xml` file.  | Can't be specified in the configuration files. All apps are presumed to be thread safe.3  
Logging  | Uses a `java.util.logging.` `ConsoleHandler`, which writes to `stderr` and flushes the stream after each record.  | Standard Cloud Logging 2  
DataNucleus plugin 2.x support  |  Supported  |  Not supported 4  
  
Notes:

  1. If your app is not using the legacy bundled services, the second-generation Java runtimes can execute any Java framework as long as you package a web server that is configured to respond to HTTP requests on the port specified by the `PORT` environment variable (recommended) or on port 8080. For example, the second-generation Java runtimes can run a Spring Boot Uber JAR as is. For more examples, see the Framework flexibility section.

If your app is using the legacy bundled services, App Engine deploys it using Jetty in the same way as in the Java 8 runtime.

  2. Logging in the second-generation Java runtimes follows the logging standard in [Cloud Logging](https://docs.cloud.google.com/logging). In the second-generation Java runtimes, app logs are no longer bundled with the request logs but are separated in different records. To learn more about reading and writing logs in the second-generation Java runtimes, see the [logging guide](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).

  3. To configure a non-threadsafe app in the second-generation Java runtime, similar to setting `<threadsafe>false</threadsafe>` in Java 8, set max concurrency to 1 in either your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#max_concurrent_requests) file, or [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#automatic_scaling_max_concurrent_requests) file if using the [legacy bundled services](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access#migration).

  4. Google doesn't support the DataNucleus library in the second-generation runtimes. Newer versions of DataNucleus are backwards incompatible with the versions used in Java 8. To access Datastore, we recommend that you use [Datastore mode client library](https://docs.cloud.google.com/datastore/docs/reference/libraries) or Java [Objectify (version 6 or later)](https://github.com/objectify/objectify/) solution. Objectify is an open source API for Datastore that provides a higher-level of abstraction.




### Memory usage differences

Second-generation runtimes see a higher baseline of memory usage compared to first-generation runtimes. This is due to multiple factors, such as different base image versions, and differences in how the two generations calculate memory usage.

Second-generation runtimes calculate instance memory usage as the sum of what an application process uses, and the number of application files dynamically cached in memory. To avoid memory-intensive applications from experiencing instance shutdowns due to exceeding memory limits, upgrade to a larger [instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) with more memory.

### CPU usage differences

Second-generation runtimes can see a higher baseline of CPU usage upon instance cold-start. Depending on an application's scaling configuration, this might have unintended side effects, such as, a higher instance count than anticipated if an application is configured to scale based on CPU utilization. To avoid this issue, review and test application scaling configurations to ensure the number of instances are acceptable.

### Request header differences

First-generation runtimes allow request headers with underscores (e.g. `X-Test-Foo_bar`) to be forwarded to the application. Second-generation runtimes introduces Nginx into the host architecture. As a result of this change, second-generation runtimes are configured to automatically remove headers with underscores (`_`). To prevent application issues, avoid using underscores in application request headers.

## Framework flexibility

The second-generation Java runtimes don't include any web-serving framework unless you are using the [legacy bundled services](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/services/access). This means that you can use a framework other than a servlet-based framework. If you are using the legacy bundled services, the second-generation Java runtimes provide the Jetty web-serving framework.

There are `hello world` samples using popular Java web frameworks on the [Google Cloud GitHub repository](https://github.com/GoogleCloudPlatform/java-docs-samples/):

  * [Spring Boot](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java11/springboot-helloworld)
  * [Vert.x](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java11/vertx-helloworld)
  * [SparkJava](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java11/sparkjava-helloworld)
  * [Ktor](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java11/kotlin-ktor)
  * [Micronaut](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java11/micronaut-helloworld)
  * [Quarkus](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/appengine-java11/quarkus-helloworld)



## Migrating XML to YAML file formats

gcloud CLI does not support the following file formats:

  * `cron.xml`
  * `datastore-index.xml`
  * `dispatch.xml`
  * `queue.xml`



The following examples demonstrate how to migrate your `xml` files to `yaml` files.

### Migrating your files automatically

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To migrate your `xml` files automatically:

  1. You must have [gcloud CLI version 226.0.0 or later](https://docs.cloud.google.com/appengine/docs/standard/setting-up-environment). To update to the latest version:
         
         gcloud components update
         

  2. For each file you'd like to migrate, specify one of the following subcommands (`cron-xml-to-yaml`, `datastore-indexes-xml-to-yaml`, `dispatch-xml-to-yaml`, `queue-xml-to-yaml`) and file name:
         
         gcloud beta app migrate-config queue-xml-to-yaml MY-QUEUE-XML-FILE.xml
         

  3. Manually double-check the converted file before deploying to production.

For a successful sample `xml` to `yaml` file conversion, see the Migrating your files manually tabs.




### Migrating your files manually

To manually migrate your `xml` files to `yaml` files:

### `cron.yaml`

Create a `cron.yaml` file with a `cron` object containing a list of objects, each with fields that correspond to each of the `<cron>` tag attributes in your `cron.xml` file, as shown below.

Converted `cron.yaml` file:
    
    
    cron:
    - url: '/recache'
      schedule: 'every 2 minutes'
      description: 'Repopulate the cache every 2 minutes'
    - url: '/weeklyreport'
      schedule: 'every monday 08:30'
      target: 'version-2'
      timezone: 'America/New_York'
      description: 'Mail out a weekly report'
    

Original `cron.xml` file:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <cronentries>
      <cron>
        <url>/recache</url>
        <description>Repopulate the cache every 2 minutes</description>
        <schedule>every 2 minutes</schedule>
      </cron>
      <cron>
        <url>/weeklyreport</url>
        <description>Mail out a weekly report</description>
        <schedule>every monday 08:30</schedule>
        <timezone>America/New_York</timezone>
        <target>version-2</target>
      </cron>
    </cronentries>
    

For more information, see the [`cron.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/scheduling-jobs-with-cron-yaml) documentation.

### `dispatch.yaml`

Create a `dispatch.yaml` file with a `dispatch` object containing a list of objects, each with fields that correspond to each of the `<dispatch>` tag attributes in your `dispatch.xml` file, as shown below.

Converted `dispatch.yaml` file:
    
    
    dispatch:
    - url: '*/favicon.ico'
      module: default
    - url: 'simple-sample.uc.r.appspot.com/'
      module: default
    - url: '*/mobile/*'
      module: mobile-frontend
    

Original `dispatch.xml` file
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <dispatch-entries>
      <dispatch>
          <url>*/favicon.ico</url>
          <module>default</module>
      </dispatch>
      <dispatch>
          <url>simple-sample.uc.r.appspot.com/</url>
          <module>default</module>
      </dispatch>
      <dispatch>
          <url>*/mobile/*</url>
          <module>mobile-frontend</module>
      </dispatch>
    </dispatch-entries>
    

For more information, see the [`dispatch.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/dispatch-yaml) documentation

### `index.yaml`

Create an `index.yaml` file with an `indexes` object containing a list of objects, each with fields that correspond to each of the `<datastore-index>` tag attributes in your `datastore-indexes.xml` file, as shown below.

Converted `index.yaml` file:
    
    
    indexes:
    - ancestor: false
      kind: Employee
      properties:
      - direction: asc
        name: lastName
      - direction: desc
        name: hireDate
    - ancestor: false
      kind: Project
      properties:
      - direction: asc
        name: dueDate
      - direction: desc
        name: cost
    

Original `datastore-index.xml` file:
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <datastore-indexes
     autoGenerate="true">
       <datastore-index kind="Employee" ancestor="false">
           <property name="lastName" direction="asc" />
           <property name="hireDate" direction="desc" />
       </datastore-index>
       <datastore-index kind="Project" ancestor="false">
           <property name="dueDate" direction="asc" />
           <property name="cost" direction="desc" />
       </datastore-index>
    </datastore-indexes>
    

For more information, see the [`index.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/configuring-datastore-indexes-with-index-yaml) documentation.

### `queue.yaml`

Create a `queue.yaml` file with a `queue` object containing a list of objects, each with fields that correspond to each of the `<queue>` tag attributes in your `queue.xml` file, as shown below.

Converted `queue.yaml` file:
    
    
    queue:
    - name: fooqueue
      mode: push
      rate: 1/s
      retry_parameters:
        task_retry_limit: 7
        task_age_limit: 2d
    - name: barqueue
      mode: push
      rate: 1/s
      retry_parameters:
        min_backoff_seconds: 10
        max_backoff_seconds: 200
        max_doublings: 0
    

Original `queue.xml` file:
    
    
    <queue-entries>
      <queue>
        <name>fooqueue</name>
        <rate>1/s</rate>
        <retry-parameters>
          <task-retry-limit>7</task-retry-limit>
          <task-age-limit>2d</task-age-limit>
        </retry-parameters>
      </queue>
      <queue>
        <name>barqueue</name>
        <rate>1/s</rate>
        <retry-parameters>
          <min-backoff-seconds>10</min-backoff-seconds>
          <max-backoff-seconds>200</max-backoff-seconds>
          <max-doublings>0</max-doublings>
        </retry-parameters>
      </queue>
    <queue-entries>
    

**Caution:** Queue creation for the task queue service can also be managed using Queue Management methods available through the Cloud Tasks API, but mixing the `queue.yaml` method with the Queue Management methods can produce unexpected results and is not recommended. For more information, see [Using Queue Management versus queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
