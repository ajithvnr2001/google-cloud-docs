---
url: https://docs.cloud.google.com/bigtable/docs/hbase-dataflow-java/
title: Bigtable HBase Beam connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:31.168368+00:00
---

# Bigtable HBase Beam connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-dataflow-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bigtable HBase Beam connector

To help you use Bigtable in a [Dataflow](https://docs.cloud.google.com/dataflow) pipeline, two open source Bigtable Beam I/O connectors are available.

If you are migrating from HBase to Bigtable or your application calls the HBase API, use the Bigtable HBase Beam connector (`CloudBigtableIO`) discussed on this page.

In all other cases, you should use the Bigtable Beam connector (`BigtableIO`) in conjunction with the Cloud Bigtable client for Java, which works with the Cloud Bigtable APIs. To get started using that connector, see [Bigtable Beam connector](https://docs.cloud.google.com/bigtable/docs/beam-connector).

For more information on the Apache Beam programming model, see the [Beam documentation](https://beam.apache.org/get-started/beam-overview/).

## Get started with HBase

The Bigtable HBase Beam connector is written in Java and is built on the Bigtable HBase client for Java. It's compatible with the Dataflow SDK 2.x for Java, which is based on [Apache Beam](https://beam.apache.org/). The connector's source code is on GitHub in the repository [googleapis/java-bigtable-hbase](https://github.com/googleapis/java-bigtable-hbase).

This page provides an overview of how to use `Read` and `Write` transforms.

## Set up authentication

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/bigtable/docs/authentication#on-gcp). 

## Add the connector to a Maven project

To add the Bigtable HBase Beam connector to a Maven project, add the Maven artifact to your `pom.xml` file as a dependency:
    
    
    <dependency>
      <groupId>com.google.cloud.bigtable</groupId>
      <artifactId>bigtable-hbase-beam</artifactId>
      <version>2.12.0</version>
    </dependency>

## Specify the Bigtable configuration

Create an options interface to allow inputs for running your pipeline:
    
    
    public interface BigtableOptions extends DataflowPipelineOptions {
    
      @Description("The Bigtable project ID, this can be different than your Dataflow project")
      @Default.String("bigtable-project")
      String getBigtableProjectId();
    
      void setBigtableProjectId(String bigtableProjectId);
    
      @Description("The Bigtable instance ID")
      @Default.String("bigtable-instance")
      String getBigtableInstanceId();
    
      void setBigtableInstanceId(String bigtableInstanceId);
    
      @Description("The Bigtable table ID in the instance.")
      @Default.String("mobile-time-series")
      String getBigtableTableId();
    
      void setBigtableTableId(String bigtableTableId);
    }

When you read from or write to Bigtable, you must provide a `CloudBigtableConfiguration` configuration object. This object specifies the project ID and instance ID for your table, as well as the name of the table itself:
    
    
    CloudBigtableTableConfiguration bigtableTableConfig =
        new CloudBigtableTableConfiguration.Builder()
            .withProjectId(options.getBigtableProjectId())
            .withInstanceId(options.getBigtableInstanceId())
            .withTableId(options.getBigtableTableId())
            .build();

For reading, provide a `CloudBigtableScanConfiguration` configuration object, which lets you specify an Apache HBase [`Scan`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html) object that limits and filters the results of a read. See Reading from Bigtable for details.

## Read from Bigtable

To read from a Bigtable table, you apply a `Read` transform to the result of a `CloudBigtableIO.read` operation. The `Read` transform returns a `PCollection` of HBase [`Result`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Result.html) objects, where each element in the `PCollection` represents a single row in the table.
    
    
    p.apply(Read.from(CloudBigtableIO.read(config)))
        .apply(
            ParDo.of(
                new DoFn<Result, Void>() {
                  @ProcessElement
                  public void processElement(@Element Result row, OutputReceiver<Void> out) {
                    System.out.println(Bytes.toString(row.getRow()));
                  }
                }));

By default, a `CloudBigtableIO.read` operation returns all of the rows in your table. You can use an HBase [`Scan`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html) object to limit the read to a range of row keys within your table, or to apply filters to the results of the read. To use a `Scan` object, include it in your `CloudBigtableScanConfiguration`.

For example, you can add a `Scan` that returns only the first key-value pair from each row in your table, which is useful when counting the number of rows in the table:
    
    
    import com.google.cloud.bigtable.beam.CloudBigtableIO;
    import com.google.cloud.bigtable.beam.CloudBigtableScanConfiguration;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.Read;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.hadoop.hbase.client.Result;
    import org.apache.hadoop.hbase.client.Scan;
    import org.apache.hadoop.hbase.filter.FirstKeyOnlyFilter;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class HelloWorldRead {
      public static void main(String[] args) {
        BigtableOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(BigtableOptions.class);
        Pipeline p = Pipeline.create(options);
    
        Scan scan = new Scan();
        scan.setCacheBlocks(false);
        scan.setFilter(new FirstKeyOnlyFilter());
    
        CloudBigtableScanConfiguration config =
            new CloudBigtableScanConfiguration.Builder()
                .withProjectId(options.getBigtableProjectId())
                .withInstanceId(options.getBigtableInstanceId())
                .withTableId(options.getBigtableTableId())
                .withScan(scan)
                .build();
    
        p.apply(Read.from(CloudBigtableIO.read(config)))
            .apply(
                ParDo.of(
                    new DoFn<Result, Void>() {
                      @ProcessElement
                      public void processElement(@Element Result row, OutputReceiver<Void> out) {
                        System.out.println(Bytes.toString(row.getRow()));
                      }
                    }));
    
        p.run().waitUntilFinish();
      }
    
      public interface BigtableOptions extends DataflowPipelineOptions {
        @Description("The Bigtable project ID, this can be different than your Dataflow project")
        @Default.String("bigtable-project")
        String getBigtableProjectId();
    
        void setBigtableProjectId(String bigtableProjectId);
    
        @Description("The Bigtable instance ID")
        @Default.String("bigtable-instance")
        String getBigtableInstanceId();
    
        void setBigtableInstanceId(String bigtableInstanceId);
    
        @Description("The Bigtable table ID in the instance.")
        @Default.String("mobile-time-series")
        String getBigtableTableId();
    
        void setBigtableTableId(String bigtableTableId);
      }
    }

## Write to Bigtable

To write to a Bigtable table, you `apply` a `CloudBigtableIO.writeToTable` operation. You'll need to perform this operation on a `PCollection` of HBase [`Mutation`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Mutation.html) objects, which can include [`Put`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Put.html) and [`Delete`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Delete.html) objects.

**Note:** [`Append`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Append.html) and [`Increment`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Increment.html) operations are not suitable for retriable batch programming models, including Hadoop and Dataflow, and are therefore not supported inputs to `CloudBigtableIO.writeToTable`. Dataflow bundles, or a group of inputs, can fail even though some of the inputs have been processed. In those cases, the entire bundle will be retried, and previously completed `Append` and `Increment` operations would be performed a second time, resulting in incorrect data.

The Bigtable table must already exist and must have the appropriate column families defined. The Dataflow connector does not create tables and column families on the fly. You can [use the `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/managing-tables) to create a table and set up column families, or you can do this programmatically.

Before you write to Bigtable, you must create your Dataflow pipeline so that puts and deletes can be serialized over the network:
    
    
    BigtableOptions options =
        PipelineOptionsFactory.fromArgs(args).withValidation().as(BigtableOptions.class);
    Pipeline p = Pipeline.create(options);

In general, you'll need to perform a transform, such as a `ParDo`, to format your output data into a collection of HBase `Put` or `Delete` objects. The following example shows a `DoFn` transform that takes the current value and uses it as the row key for a `Put`. You can then write the `Put` objects to Bigtable.
    
    
    p.apply(Create.of("phone#4c410523#20190501", "phone#4c410523#20190502"))
        .apply(
            ParDo.of(
                new DoFn<String, Mutation>() {
                  @ProcessElement
                  public void processElement(@Element String rowkey, OutputReceiver<Mutation> out) {
                    long timestamp = System.currentTimeMillis();
                    Put row = new Put(Bytes.toBytes(rowkey));
    
                    row.addColumn(
                        Bytes.toBytes("stats_summary"),
                        Bytes.toBytes("os_build"),
                        timestamp,
                        Bytes.toBytes("android"));
                    out.output(row);
                  }
                }))
        .apply(CloudBigtableIO.writeToTable(bigtableTableConfig));

To enable [batch write flow control](https://docs.cloud.google.com/bigtable/docs/writes#flow-control), set `BIGTABLE_ENABLE_BULK_MUTATION_FLOW_CONTROL` to `true`. This feature automatically rate-limits traffic for batch write requests and lets Bigtable autoscaling add or remove nodes automatically to handle your Dataflow job.
    
    
    CloudBigtableTableConfiguration bigtableTableConfig =
        new CloudBigtableTableConfiguration.Builder()
            .withProjectId(options.getBigtableProjectId())
            .withInstanceId(options.getBigtableInstanceId())
            .withTableId(options.getBigtableTableId())
            .withConfiguration(BigtableOptionsFactory.BIGTABLE_ENABLE_BULK_MUTATION_FLOW_CONTROL,
                "true")
            .build();
    return bigtableTableConfig;

Here is the full writing example, including the variation that enables batch write flow control.
    
    
    import com.google.cloud.bigtable.beam.CloudBigtableIO;
    import com.google.cloud.bigtable.beam.CloudBigtableTableConfiguration;
    import com.google.cloud.bigtable.hbase.BigtableOptionsFactory;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.hadoop.hbase.client.Mutation;
    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class HelloWorldWrite {
    
      public static void main(String[] args) {
        BigtableOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(BigtableOptions.class);
        Pipeline p = Pipeline.create(options);
    
        CloudBigtableTableConfiguration bigtableTableConfig =
            new CloudBigtableTableConfiguration.Builder()
                .withProjectId(options.getBigtableProjectId())
                .withInstanceId(options.getBigtableInstanceId())
                .withTableId(options.getBigtableTableId())
                .build();
    
        p.apply(Create.of("phone#4c410523#20190501", "phone#4c410523#20190502"))
            .apply(
                ParDo.of(
                    new DoFn<String, Mutation>() {
                      @ProcessElement
                      public void processElement(@Element String rowkey, OutputReceiver<Mutation> out) {
                        long timestamp = System.currentTimeMillis();
                        Put row = new Put(Bytes.toBytes(rowkey));
    
                        row.addColumn(
                            Bytes.toBytes("stats_summary"),
                            Bytes.toBytes("os_build"),
                            timestamp,
                            Bytes.toBytes("android"));
                        out.output(row);
                      }
                    }))
            .apply(CloudBigtableIO.writeToTable(bigtableTableConfig));
    
        p.run().waitUntilFinish();
      }
    
      public interface BigtableOptions extends DataflowPipelineOptions {
    
        @Description("The Bigtable project ID, this can be different than your Dataflow project")
        @Default.String("bigtable-project")
        String getBigtableProjectId();
    
        void setBigtableProjectId(String bigtableProjectId);
    
        @Description("The Bigtable instance ID")
        @Default.String("bigtable-instance")
        String getBigtableInstanceId();
    
        void setBigtableInstanceId(String bigtableInstanceId);
    
        @Description("The Bigtable table ID in the instance.")
        @Default.String("mobile-time-series")
        String getBigtableTableId();
    
        void setBigtableTableId(String bigtableTableId);
      }
    
      public static CloudBigtableTableConfiguration batchWriteFlowControlExample(
          BigtableOptions options) {
        CloudBigtableTableConfiguration bigtableTableConfig =
            new CloudBigtableTableConfiguration.Builder()
                .withProjectId(options.getBigtableProjectId())
                .withInstanceId(options.getBigtableInstanceId())
                .withTableId(options.getBigtableTableId())
                .withConfiguration(BigtableOptionsFactory.BIGTABLE_ENABLE_BULK_MUTATION_FLOW_CONTROL,
                    "true")
                .build();
        return bigtableTableConfig;
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
