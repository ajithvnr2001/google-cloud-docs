---
url: https://docs.cloud.google.com/dataflow/docs/guides/read-from-cloud-storage/
title: Read from Cloud Storage to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:13.329476+00:00
---

# Read from Cloud Storage to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/read-from-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Read from Cloud Storage to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Unstructured or semi-structured data stored in Cloud Storage—such as text, CSV, JSON, or Avro files—often needs to be ingested and transformed at scale for downstream analytics. Ingesting Cloud Storage data into Dataflow lets you run distributed, parallel pipelines to read and process high-volume file datasets reliably across batch and streaming workloads.

To build custom pipelines, you can use Apache Beam [I/O connectors](https://beam.apache.org/documentation/io/connectors/) such as `TextIO` or `AvroIO` to read files for processing. For common workflows, you can also use [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) to deploy prebuilt pipelines without writing custom code.

## Include the Google Cloud library dependency

To use the `TextIO` or `AvroIO` connector with Cloud Storage, include the following dependency. This library provides a schema handler for `"gs://"` filenames.

###  Java 
    
    
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-io-google-cloud-platform</artifactId>
      <version>${beam.version}</version>
    </dependency>
    

###  Python 
    
    
    apache-beam[gcp]==VERSION
    

###  Go 
    
    
    import _ "github.com/apache/beam/sdks/v2/go/pkg/beam/io/filesystem/gcs"
    

For more information, see [Install the Apache Beam SDK](https://docs.cloud.google.com/dataflow/docs/guides/installing-beam-sdk).

## Enable gRPC on Apache Beam I/O connector on Dataflow

You can [connect to Cloud Storage using gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api) through the Apache Beam I/O connector on Dataflow. [gRPC](https://grpc.io/) is a high performance open-source remote procedure call (RPC) framework developed by Google that you can use to interact with Cloud Storage.

To speed up your Dataflow job's read requests to Cloud Storage, you can enable the Apache Beam I/O connector on Dataflow to use gRPC. 

### Command line

  1. Ensure that you use the [ Apache Beam SDK](https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options) version [2.55.0](https://beam.apache.org/get-started/beam-overview/) or later.
  2. To run a Dataflow job, use `--additional-experiments=use_grpc_for_gcs` pipeline option. For information about the different pipeline options, see [Optional flags](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run#--additional-experiments).



### Apache Beam SDK

  1. Ensure that you use the [ Apache Beam SDK](https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options) version [2.55.0](https://beam.apache.org/get-started/beam-overview/) or later.
  2. To run a Dataflow job, use `--experiments=use_grpc_for_gcs` pipeline option. For information about the different pipeline options, see [Basic options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#basic_options).



You can configure Apache Beam I/O connector on Dataflow to generate gRPC related metrics in Cloud Monitoring. The gRPC related metrics can help you to do the following: 

  * Monitor and optimize the performance of gRPC requests to Cloud Storage.
  * Troubleshoot and debug issues.
  * Gain insights into your application's usage and behavior.

  
For information about how to configure Apache Beam I/O connector on Dataflow to generate gRPC related metrics, see [Use client-side metrics](https://docs.cloud.google.com/storage/docs/client-side-metrics). If gathering metrics isn't necessary for your use case, you can choose to opt-out of metrics collection. For instructions, see [Opt-out of client-side metrics](https://docs.cloud.google.com/storage/docs/client-side-metrics#opt_out_of_client-side_metrics). 

## Parallelism

The `TextIO` and `AvroIO` connectors support two levels of parallelism:

  * Individual files are keyed separately, so that multiple workers can read them.
  * If the files are uncompressed, the connector can read sub-ranges of each file separately, leading to a very high level of parallelism. This splitting is only possible if each line in the file is a meaningful record. For example, it's not available by default for JSON files.



## Performance

The following table shows performance metrics for reading from Cloud Storage. The workloads were run on one `e2-standard2` worker, using the Apache Beam SDK 2.49.0 for Java. They did not use the Portable Runner.

100 M records | 1 kB | 1 column | Throughput (bytes) | Throughput (elements)  
---|---|---  
[Read](https://github.com/apache/beam/blob/master/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/storage/FileBasedIOLT.java#L162) | 320 MBps | 320,000 elements per second  
  
These metrics are based on simple batch pipelines. They are intended to compare performance between I/O connectors, and are not necessarily representative of real-world pipelines. Dataflow pipeline performance is complex, and is a function of VM type, the data being processed, the performance of external sources and sinks, and user code. Metrics are based on running the Java SDK, and aren't representative of the performance characteristics of other language SDKs. For more information, see [Beam IO Performance](https://beam.apache.org/performance/).

## Best practices

  * Avoid using [`watchForNewFiles`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/TextIO.Read.html#watchForNewFiles-org.joda.time.Duration-org.apache.beam.sdk.transforms.Watch.Growth.TerminationCondition-) with Cloud Storage. This approach scales poorly for large production pipelines, because the connector must keep a list of seen files in memory. The list can't be flushed from memory, which reduces the working memory of workers over time. Consider using [Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications) instead. For more information, see [File processing patterns](https://beam.apache.org/documentation/patterns/file-processing/).

  * If both the filename and the file contents are useful data, use the [`FileIO`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/FileIO.html) class to read filenames. For example, a filename might contain metadata that is useful when processing the data in the file. For more information, see [Accessing filenames](https://beam.apache.org/documentation/patterns/file-processing/). The [`FileIO` documentation](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/FileIO.html) also shows an example of this pattern.




## Example

The following example shows how to read from Cloud Storage.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptors;
    
    public class ReadFromStorage {
      public static Pipeline createPipeline(Options options) {
        var pipeline = Pipeline.create(options);
        pipeline
            // Read from a text file.
            .apply(TextIO.read().from(
                "gs://" + options.getBucket() + "/*.txt"))
            .apply(
                MapElements.into(TypeDescriptors.strings())
                    .via(
                        (x -> {
                          System.out.println(x);
                          return x;
                        })));
        return pipeline;
      }
    }

## What's next

  * Read the [`TextIO`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/TextIO.html) API documentation.
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
