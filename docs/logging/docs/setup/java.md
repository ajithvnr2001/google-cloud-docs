---
url: https://docs.cloud.google.com/logging/docs/setup/java/
title: Setting Up Cloud Logging for Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:34.614097+00:00
---

# Setting Up Cloud Logging for Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/setup/java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Setting Up Cloud Logging for Java Stay organized with collections  Save and categorize content based on your preferences. 

You can write logs to Cloud Logging from Java applications by using the [Logback appender](https://docs.cloud.google.com/logging/docs/setup/java#logback_appender) or a [java.util.logging handler](https://docs.cloud.google.com/logging/docs/setup/java#jul_handler), or by using the Cloud Logging library for Java directly.

The Cloud Logging agent does not have to be installed to use the Cloud Logging library for Java. 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)




## Logback appender for Cloud Logging

Using the [Logback](https://logback.qos.ch/) appender, you can use Cloud Logging with the [SLF4J](https://www.slf4j.org/) logging facade.

### Installing the dependency

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-logging-logback</artifactId>
      <version>0.131.11-alpha</version>
    </dependency>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation 'com.google.cloud:google-cloud-logging-logback:0.131.11-alpha'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-logging-logback" % "0.131.11-alpha"

### Logback configuration

Logback can be [configured](https://logback.qos.ch/manual/configuration.html) programmatically or using a script expressed in XML or Groovy.

You can customize the minimum severity threshold, log name, or provide additional enhancers. This is a sample Logback configuration in XML format:
    
    
    <configuration>
      <appender name="CLOUD" class="com.google.cloud.logging.logback.LoggingAppender">
        <!-- Optional : filter logs at or above a level -->
        <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
          <level>INFO</level>
        </filter>
        <log>application.log</log> <!-- Optional : default java.log -->
        <resourceType>gae_app</resourceType> <!-- Optional : default: auto-detected, fallback: global -->
        <enhancer>com.example.logging.logback.enhancers.ExampleEnhancer</enhancer> <!-- Optional -->
        <flushLevel>WARN</flushLevel> <!-- Optional : default ERROR -->
      </appender>
    
      <root level="info">
        <appender-ref ref="CLOUD" />
      </root>
    </configuration>

### Example

Once you have configured Logback to use the Cloud Logging Logback appender, you can now redirect logs using the SLF4J logging API. Provide Google Cloud [configuration](https://docs.cloud.google.com/logging/docs/setup/java#run-local) if you plan to run the example locally or outside of Google Cloud. This snippet shows how to log using SLF4J facade within your application:
    
    
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    public class Quickstart {
      private static final Logger logger = LoggerFactory.getLogger(Quickstart.class);
    
      public static void main(String[] args) {
        logger.info("Logging INFO with Logback");
        logger.error("Logging ERROR with Logback");
      }
    }

## The java.util.logging handler

You can also use the Cloud Logging API using a default Java Logging API [handler](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler). 

### Installing the dependency

If you are using [Maven](https://maven.apache.org/) with a BOM, add the following to your `pom.xml` file:
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.55.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-logging</artifactId>
      </dependency>
    
      <!-- ...
    </dependencies>

If you are using [Maven](https://maven.apache.org/) without a BOM, add this to your dependencies:
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-logging</artifactId>
      <version>3.21.3</version>
    </dependency>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.74.0')
    
    implementation 'com.google.cloud:google-cloud-logging'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-logging" % "3.24.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### java.util.logging configuration

Logging handlers can be added programmatically or by using a configuration file. The path to the configuration file must be provided to your application as a system property:
    
    
      -Djava.util.logging.config.file=/path/to/logging.properties
    

Here is an example of a configuration file: 
    
    
    # To use this configuration, add to system properties : -Djava.util.logging.config.file="/path/to/file"
    #
    .level = INFO
    
    # it is recommended that io.grpc and sun.net logging level is kept at INFO level,
    # as both these packages are used by Cloud internals and can result in verbose / initialization problems.
    io.grpc.netty.level=INFO
    sun.net.level=INFO
    
    com.example.logging.jul.Quickstart.handlers=com.google.cloud.logging.LoggingHandler
    # default : java.log
    com.google.cloud.logging.LoggingHandler.log=custom_log
    
    # default : INFO
    com.google.cloud.logging.LoggingHandler.level=FINE
    
    # default : ERROR
    com.google.cloud.logging.LoggingHandler.flushLevel=ERROR
    
    # default : auto-detected, fallback "global"
    com.google.cloud.logging.LoggingHandler.resourceType=container
    
    # custom formatter
    com.google.cloud.logging.LoggingHandler.formatter=java.util.logging.SimpleFormatter
    java.util.logging.SimpleFormatter.format=%3$s: %5$s%6$s
    
    #optional enhancers (to add additional fields, labels)
    com.google.cloud.logging.LoggingHandler.enhancers=com.example.logging.jul.enhancers.ExampleEnhancer

### Example

Provide Google Cloud [configuration](https://docs.cloud.google.com/logging/docs/setup/java#run-local) if you plan to run the example locally or outside of Google Cloud. This snippet shows you how to log using `java.util.logging`: 
    
    
    import java.util.logging.Logger;
    
    public class Quickstart {
      private static final Logger logger = Logger.getLogger(Quickstart.class.getName());
    
      public static void main(String[] args) {
        logger.info("Logging INFO with java.util.logging");
        logger.severe("Logging ERROR with java.util.logging");
      }
    }

## Common Configuration

The following sections cover configuration that is common to the `java.util.logging` handler and the Logback appender for Cloud Logging.

### Defaults

The Logback appender and `java.util.logging` handler use the following defaults to instantiate a Cloud Logging client:

  * Log name : `java.log`

  * Minimum threshold to log : `INFO`

  * Flush severity : `ERROR`




The Cloud Logging library for Java batches messages by size and time since last write. Batches with logging requests at or above the flush severity are immediately written out.

**Note:** If using the Cloud Logging library for Java API directly, there is no default log name or minimum threshold.

### Monitored resource detection

All logs sent via the Cloud Logging libraries require a [monitored resource type](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types) to identify your application.

The Logback appender and the `java.util.logging` handler provide automatic resource type detection of your App Engine, Compute Engine, and Google Kubernetes Engine applications.

A `global` monitored resource is used as the default in other environments.

You can override the monitored resource type to a [valid type](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types) in the Logback appender Configuration or the `java.util.logging` Handler Configuration.

**Note:** If using the Cloud Logging API directly, you must provide a valid monitored resource type when logging using the API.

### Additional fields and labels

Using the Logback appender and the `java.util.logging` handler, you can add or update fields on a [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry) object using an instance of [LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer).

The enhancers must be configured as shown in the Logback appender configuration or the `java.util.logging` handler configuration:
    
    
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer.html);
    
    // Add / update additional fields to the log entry
    public class ExampleEnhancer implements [LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer.html) {
    
      @Override
      public void enhanceLogEntry([LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html).Builder logEntry) {
        // add additional labels
        logEntry.[addLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.Builder.html#com_google_cloud_logging_LogEntry_Builder_addLabel_java_lang_String_java_lang_String_)("test-label-1", "test-value-1");
      }
    }

Use of custom labels might not be supported for your configuration. For example, Dataflow logs don't include these labels.

For more information on installation, see the [documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/overview) for the Cloud Logging library for Java. You can also report issues using the [issue tracker](https://github.com/googleapis/java-logging-logback/issues).

## Write logs with the Cloud Logging client library

For information on using the Cloud Logging client library for Java directly, see [Cloud Logging Client Libraries](https://docs.cloud.google.com/logging/docs/reference/libraries).

## Run on Google Cloud

For an application to write logs by using the Cloud Logging library for Java, the service account for the underlying resource must have the [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) [IAM](https://docs.cloud.google.com/iam/docs/understanding-roles) role. Most Google Cloud environments automatically configure the default service account to have this role.

### App Engine

Cloud Logging is automatically enabled for App Engine, and your app's [default service account](https://docs.cloud.google.com/appengine/docs/standard/java11/service-account) has the IAM permissions by default to write log entries.

App Engine standard environment, by [default](https://docs.cloud.google.com/appengine/docs/standard/java/logs), uses the [`java.util.logging.Logger`](https://docs.oracle.com/en/java/javase/11/docs/api/java.logging/java/util/logging/Logger.html) API; this writes to Cloud Logging directly and is easy to configure.

For further details, see App Engine documentation on [Reading and Writing Application Logs](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/writing-application-logs).

#### App Engine flexible environment

On [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible/java), `java.util.logging` uses the [`ConsoleHandler`](https://docs.oracle.com/javase/8/docs/api/java/util/logging/ConsoleHandler.html) by default, and sends logs to `stdout` and `stderr`.

The [Jetty](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime) Runtime is bundled with the Cloud Logging library for Java.

The `java.util.logging` handler can be used to log directly to Cloud Logging by providing the `logging.properties` in your `app.yaml` as shown here:
    
    
        env_variables:
          JETTY_ARGS: -Djava.util.logging.config.file=WEB-INF/logging.properties
    

Trace ID logging is available on Jetty runtimes if you are using the `java.util.logging` handler or the Logback appender.

When running on App Engine flexible environment, a [TraceLoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.TraceLoggingEnhancer) instance adds a thread-safe trace ID to every log entry using the label `trace_id`. 

### Google Kubernetes Engine (GKE)

[GKE](https://docs.cloud.google.com/kubernetes-engine/docs) automatically grants the default service account the [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) IAM role. If you use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) with this default service account to let workloads access specific Google Cloud APIs, then no additional configuration is required. However, if you use Workload Identity Federation for GKE with a custom IAM service account, then ensure that the custom service account has the role of Logs Writer (`roles/logging.logWriter`).

If needed, you can also use the following command to add the `logging.write` access scope when creating the cluster:
    
    
    gcloud container clusters create example-cluster-name \
        --scopes https://www.googleapis.com/auth/logging.write
    

### Compute Engine

**Note:** To use the Cloud Logging library for Java on a **Compute Engine** VM instance, you do not need to install the Cloud Logging agent.

When using [Compute Engine](https://docs.cloud.google.com/compute/docs) VM instances, add the `cloud-platform` access scope to each instance. When creating a new instance through the Google Cloud console, you can do this in the **Identity and API access** section of the **Create Instance** panel. Use the Compute Engine default service account or another service account of your choice, and select **Allow full access to all Cloud APIs** in the **Identity and API access** section. Whichever service account you select, ensure that it has been granted the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) in the **IAM & Admin** section of the Google Cloud console.

## Run locally and elsewhere

To use the Cloud Logging library for Java outside of Google Cloud, including running the library on your own workstation, on your data center's computers, or on the VM instances of another cloud provider, you must set up Application Default Credentials (ADC) in your local environment to authenticate to the Cloud Logging library for Java.

For more information, see [Set up ADC for on-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).

## View the logs

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

In the Logs Explorer, you must specify one or more resources, but the resource selection might not be obvious. Here are some tips to help you get started:

  * If you are deploying your application to App Engine or using the App Engine-specific libraries, set your resource to **GAE Application**.

  * If you are deploying your application on Compute Engine, set the resource to **GCE VM Instance**.

  * If you are deploying your application on Google Kubernetes Engine, your cluster's logging configuration determines the resource type of the log entries. For a detailed discussion on the Legacy Google Cloud Observability and the Google Cloud Observability Kubernetes Monitoring solutions, and how those options affect the resource type, see [Migrating to Google Cloud Observability Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration#stackdriver-options).

  * If your application is using the Cloud Logging API directly, the resource is dependent on the API and your configuration. For example, in your application, you can specify a resource or use a default resource.

  * If you don't see any logs in the Logs Explorer, to see all log entries, switch to the advanced query mode and use an empty query.

    1. To switch to the advanced query mode, click **menu** (▾) at the top of the Logs Explorer and then select **Convert to advanced filter**.
    2. Clear the content that appears in the filter box.
    3. Click **Submit Filter**.

You can examine the individual entries to identify your resources.




For additional information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
