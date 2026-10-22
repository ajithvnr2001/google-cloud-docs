---
url: https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup/
title: Set up client-side metrics \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:54.846099+00:00
---

# Set up client-side metrics  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up client-side metrics

Bigtable client-side metrics let you monitor application performance, track request latencies, and diagnose connectivity issues.

Client-side metrics are available for users of the following client libraries:

  * [Bigtable client library for C++](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest)
  * [Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview)
  * [Bigtable HBase client for Java](https://github.com/googleapis/java-bigtable-hbase)
  * [Bigtable client library for Go](https://pkg.go.dev/cloud.google.com/go/bigtable)
  * [Bigtable client library for Node.js](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest)



For conceptual background and metric definitions, see the [Client-side metrics overview](https://docs.cloud.google.com/bigtable/docs/client-side-metrics) and [Client-side metric descriptions](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions).

## Add or confirm service account permissions

**Note:** Metrics writer Identity and Access Management permissions are included in the [Bigtable predefined roles](https://docs.cloud.google.com/bigtable/docs/access-control#roles) by default. This step is only required if you're using a [custom role](https://docs.cloud.google.com/bigtable/docs/access-control#custom-roles).

To add IAM permissions to the service account, complete the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select the project where you created the Bigtable cluster.

  3. Search for the service account you want to add the permission to.

  4. Click **Edit principal.**

  5. Click Add another role.

  6. Search for "monitoring metric writer" and select the result.

  7. Click **Save**.




## Enable the Cloud Monitoring API

  1. In the Google Cloud console, go to the **APIs & Services** page.

[Go to APIs and services](https://console.cloud.google.com/projectselector/apis/dashboard?supportedpurview=project,folder,organizationId)

  2. Select the project where you created the Bigtable cluster.

  3. Click **Enable APIs and Service**.

  4. Search for `Monitoring`.

  5. In the search results, click **Cloud Monitoring API**.

  6. If **API enabled** is displayed, then the API is already enabled. If not, then click **Enable**.




## Set up your Bigtable client library

After you enable the Cloud Monitoring API, configure your Bigtable client library.

### C++

Follow these steps if you use the Bigtable client library for C++, which calls the Bigtable APIs.

### Install and configure the client library for C++

Integrate the library using common C++ build systems, such as CMake or Bazel. For more information, see [Building and Installing](https://github.com/googleapis/google-cloud-cpp/blob/v2.40.0/README.md#building-and-installing).

For the Bigtable client library to collect the client-side metrics, your project must include dependencies for [OpenTelemetry](https://opentelemetry.io/) and Cloud Monitoring. OpenTelemetry provides the framework for the client library to create, instrument, and record the metrics, while the Cloud Monitoring library provides the functionality to then export or publish these metrics to Cloud Monitoring.

### Enable client-side metrics in your application

Client-side metrics are enabled by default in the [Bigtable client library for C++](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest) as of version 2.40.0.

The metrics are collected automatically if both the OpenTelemetry and Cloud Monitoring dependencies are available in your project. There is no additional charge for these metrics.

### Optional: Opt out of client-side metrics

You can opt out of using client-side metrics by setting the `EnableMetricsOption` to `false` when you create your data connection.
    
    
    auto options = Options{}.set<EnableMetricsOption>(false);
    TableResource resource("my-project", "my-instance", "my-table");
    Table table(MakeDataConnection(std::move(options)), std::move(resource));
    

###  Go 

Follow these steps if you use the Bigtable client library for Go, which calls the Bigtable APIs.

### Install and configure the client library for Go

Update the Bigtable client library for Go to version 1.27.0 or later. Your `go.mod` should look similar to the following:
    
    
    require (
      cloud.google.com/go/bigtable v1.27.2-0.20240725222120-ce31365acc54
    

### Optional: Opt out of client-side metrics

Client-side metrics are enabled by default in the Go client library. To opt out, pass `NoopMetricsProvider` in the `ClientConfig`:
    
    
    client, err := bigtable.NewClientWithConfig(ctx, project, instance,
    bigtable.ClientConfig{MetricsProvider: bigtable.NoopMetricsProvider{},
    })
    

###  HBase 

Follow these steps if you use the Bigtable HBase client for Java, which calls the HBase API, to connect your application to Bigtable.

### Install and configure the HBase client library for Java

  1. Download and install the latest [Bigtable HBase client for Java](https://github.com/googleapis/java-bigtable-hbase). To enable client-side metrics, you must use version 2.6.4 or later.

  2. Create an empty Maven project.

  3. Determine the artifact dependency that's right for your use case. The `2.x` versions include an HBase async client that the `1.x` versions do not have.

     * `bigtable-hbase-1.x` or `bigtable-hbase-2.x`: Use for standalone applications where you are in control of your dependencies.
     * `bigtable-hbase-1.x-hadoop` or `bigtable-hbase-2.x-hadoop`: Use in Hadoop environments.
     * `bigtable-hbase-1.x-shaded` or `bigtable-hbase-2.x-shaded`: Use in environments other than Hadoop that require earlier versions of components such as protobufs or Guava.
  4. Update the pom.xml file:
         
         <dependencyManagement>
             <dependencies>
                 <dependency>
                       <groupId>com.google.cloud.bigtable</groupId>
                       <artifactId>BIGTABLE_HBASE_ARTIFACT</artifactId>
                       <version>VERSION_NUMBER</version>
                   </dependency>
             </dependencies>
         </dependencyManagement>
         

Provide the following: 

     * `BIGTABLE_HBASE_ARTIFACT`: the artifact dependency for your project, formatted like `bigtable-hbase-1.x` or `bigtable-hbase-2.x-hadoop`.
     * `VERSION_NUMBER`: the client library version that you are using, formatted like `2.6.4`



### Enable client-side metrics in your application

**Note:** Client-side metrics are enabled by default since version 2.14.1. The following steps are only required when you're using a version between 2.6.4 and 2.14.1.

#### Using `bigtable-hbase-1.x` or `bigtable-hbase-2.x`

When you create a connection using the HBase client library and either the `bigtable-hbase-1.x` or `bigtable-hbase-2.x` artifacts, your code to enable the built-in client-side metrics looks similar to the following:
    
    
      import com.google.cloud.bigtable.data.v2.[BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html);
    
      Configuration configuration = BigtableConfiguration.configure("my-project-id", "my-instance-id");
      Connection connection = new BigtableConnection(configuration);
    
      [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html).[enableBuiltinMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_enableBuiltinMetrics__)();
    

#### Using `-hadoop` or `-shaded` artifacts

When you create a connection using the HBase client library and one of the `-hadoop` or `-shaded` artifacts, your code to enable the built-in client-side metrics looks similar to the following:
    
    
      import com.google.bigtable.repackaged.com.google.cloud.bigtable.data.v2.BigtableDataSettings;
    
      Configuration configuration = BigtableConfiguration.configure("my-project-id", "my-instance-id");
      Connection connection = new BigtableConnection(configuration);
    
      BigtableDataSettings.enableBuiltinMetrics();
    

#### Optional: Opt out of client-side metrics

If you are using version 2.14.1 or later, client-side metrics are enabled by default. You can opt out.
    
    
    Configuration configuration = BigtableConfiguration.configure("my-project-id", "my-instance-id");
    configuration.setBoolean(BigtableOptionsFactory.BIGTABLE_ENABLE_CLIENT_SIDE_METRICS, false);
    Connection connection = new BigtableConnection(configuration);
    

###  Java 

Follow these steps if you use the Bigtable client library for Java, which calls the Bigtable APIs.

### Before you begin

Optional: If you use an [OpenCensus Stats](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable#enabling-cloud-bigtable-metrics-opencensus-stats) integration to get Bigtable metrics, revert the dependency and `StackdriverStatsExporter` changes in your application. To understand why, see [When to upgrade](https://docs.cloud.google.com/bigtable/docs/client-side-metrics#when-to-upgrade).

### Install and configure the client library for Java

  1. Download and install the latest [Bigtable client library for Java](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable). You must have version 2.16.0 or higher to use client-side metrics.
  2. Update the Java client library's pom.xml file to use the latest version. Your pom should look similar to the following:
         
         <dependencyManagement>
             <dependencies>
                 <dependency>
                       <groupId>com.google.cloud</groupId>
                       <artifactId>google-cloud-bigtable-bom</artifactId>
                       <version>2.38.0</version>
                       <scope>import</scope>
                       <type>pom</type>
                   </dependency>
             </dependencies>
         </dependencyManagement>
         
         <dependencies>
             <dependency>
                   <groupId>com.google.cloud</groupId>
                   <artifactId>google-cloud-bigtable</artifactId>
             </dependency>
         </dependencies>
         




### Enable client-side metrics in your application

**Note:** Client-side metrics are enabled by default since version 2.38.0. This step is only required when you're using a version between 2.16.0 and 2.38.0.

When you create a client using the client library, enable the built-in metrics. Your code should look similar to the following:
    
    
      BigtableDataSettings settings = BigtableDataSettings.newBuilder()
                  .setProjectId("our-project-2-12")
                  .setInstanceId("our-instance-85")
                  .setAppProfileId("our-appProfile-06")
                  .build();
    
      BigtableDataSettings.enableBuiltinMetrics();
    
      try (BigtableDataClient client = BigtableDataClient.create(settings)) {
              // Application logic
      }
    

### Set up a custom OpenTelemetry instance

If you are using version 2.38.0 or later, and you want to publish client-side metrics to Cloud Monitoring and custom sinks, you can set up a custom OpenTelemetry instance.
    
    
      SdkMeterProviderBuilder meterProviderBuilder = SdkMeterProvider.builder();
    
      // register client side metrics on your meter provider
      BuiltinMetricsView.registerBuiltinMetrics("my-project-id", meterProviderBuilder);
    
      // register other metric reader and views
      meterProviderBuilder.registerMetricReader().registerView();
    
      // create the OTEL instance
      OpenTelemetry openTelemetry = OpenTelemetrySdk.builder()
              .setMeterProvider(meterProviderBuilder.build())
              .build();
    
      // Override MetricsProvider in BigtableDataSettings
      BigtableDataSettings settings = BigtableDataSettings.newBuilder()
              .setProjectId("my-project-id")
              .setInstanceId("my-instance-id")
              .setMetricsProvider(CustomOpenTelemetryMetricsProvider.create(openTelemetry))
              .build();
    
      try (BigtableDataClient client = BigtableDataClient.create(settings)) {
            // Application logic
      }
    

### Optional: Opt out of client-side metrics

If you are using version 2.38.0 and later, you can opt out of using client-side metrics.
    
    
    BigtableDataSettings settings = BigtableDataSettings.newBuilder()
            .setProjectId("my-project")
            .setInstanceId("my-instance")
            .setMetricsProvider(NoopMetricsProvider.INSTANCE)
            .build();
    

###  Node.js 

Follow these steps if you use the Bigtable client library for Node.js, which calls the Bigtable APIs.

### Install and configure the client library for Node.js

  1. Download and install the latest [Bigtable client library for Node.js](https://github.com/googleapis/nodejs-bigtable).

You must have version 6.2.0 or later to use client-side metrics. Your `package.json` file should look similar to the following:
         
         {
           "dependencies": {
             "@google-cloud/bigtable": "^6.2.0"
           }
         }
         

  2. In your project, reinstall Node.js modules:
         
         rm -rf node_modules
         rm package-lock.json
         npm i
         




### Enable client-side metrics in your application

Client-side metrics are enabled by default in the [Bigtable client library for Node.js](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest) as of version 6.4.0.

### Optional: Opt out of client-side metrics

You can opt out of using client-side metrics.
    
    
    const bigtable = new Bigtable({metricsEnabled: false});
    

## View metrics in Metrics Explorer

  1. In the Google Cloud console, go to the **Metrics Explorer** page.

[Go to Metrics Explorer](https://console.cloud.google.com/projectselector/monitoring/metrics-explorer?supportedpurview=project,folder,organizationId)

  2. Select the project.

  3. Click **Select a metric**.

  4. Search for `bigtable.googleapis.com/client`.

  5. Select a metric, a `group by` method, and status, and pick an **Aggregator**. To explore more options, see [Select metrics when using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).




After you enable client-side metrics, let your application run for at least a minute before you check for any published metrics.

## View metrics in Bigtable monitoring

Charts for the following client-side metrics are displayed on the Bigtable monitoring page:

  * Client-side read latency
  * Client-side write latency
  * Client-side read attempt latency
  * Client-side write attempt latency



To view client-side metrics on the **Monitoring** page, follow these steps:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. In the left pane, click **Monitoring**. The Google Cloud console displays a series of charts for the instance.

  4. Scroll through the pane to view the client-side metrics.

  5. Optional: To view metrics at the table level, click **Tables**.

  6. Optional: To view metrics for individual app profiles, click **Application Profiles**.




For more information, see [Bigtable monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

## What's next

  * [Read an overview of client-side metrics.](https://docs.cloud.google.com/bigtable/docs/client-side-metrics)
  * [View complete descriptions of client-side metrics.](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
