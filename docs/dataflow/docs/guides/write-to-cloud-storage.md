---
url: https://docs.cloud.google.com/dataflow/docs/guides/write-to-cloud-storage/
title: Write from Dataflow to Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:42.194536+00:00
---

# Write from Dataflow to Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/write-to-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write from Dataflow to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to write text data from Dataflow to Cloud Storage by using the Apache Beam `TextIO` [I/O connector](https://beam.apache.org/documentation/io/connectors/).

**Note:** Depending on your scenario, consider using one of the [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates). Several of these templates output to Cloud Storage.

## Include the Google Cloud library dependency

To use the `TextIO` connector with Cloud Storage, include the following dependency. This library provides a schema handler for `"gs://"` filenames.

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

To speed up your Dataflow job's write requests to Cloud Storage, you can enable the Apache Beam I/O connector on Dataflow to use gRPC. 

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

Parallelism is determined primarily by the number of shards. By default, the runner automatically sets this value. For most pipelines, using the default behavior is recommended. In this document, see Best practices.

## Performance

The following table shows performance metrics for writing to Cloud Storage. The workloads were run on one `e2-standard2` worker, using the Apache Beam SDK 2.49.0 for Java. They did not use the Portable Runner.

100 M records | 1 kB | 1 column | Throughput (bytes) | Throughput (elements)  
---|---|---  
[Write](https://github.com/apache/beam/blob/master/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/storage/FileBasedIOLT.java#L162) | 130 MBps | 130,000 elements per second  
  
These metrics are based on simple batch pipelines. They are intended to compare performance between I/O connectors, and are not necessarily representative of real-world pipelines. Dataflow pipeline performance is complex, and is a function of VM type, the data being processed, the performance of external sources and sinks, and user code. Metrics are based on running the Java SDK, and aren't representative of the performance characteristics of other language SDKs. For more information, see [Beam IO Performance](https://beam.apache.org/performance/).

## Best practices

  * In general, avoid setting a specific number of shards. This allows the runner to select an appropriate value for your scale. To enable autosharding, call `.withAutoSharding()`, not `.withNumShards(0)`. If you tune the number of shards, we recommend writing between 100MB and 1GB per shard. However, the optimum value might depend on the workload.

  * Cloud Storage can scale to a very large number of requests per second. However, if your pipeline has large spikes in write volume, consider writing to multiple buckets, to avoid temporarily overloading any single Cloud Storage bucket.

  * In general, writing to Cloud Storage is more efficient when each write is larger (1 kb or greater). Writing small records to a large number of files can result in worse performance per byte.

  * When generating file names, consider using non-sequential file names, in order to distribute load. For more information, see [Use a naming convention that distributes load evenly across key ranges](https://docs.cloud.google.com/storage/docs/request-rate#naming-convention).

  * When naming files, don't use the at sign ('@') followed by a number or an asterisk ('*'). For more information, see ["@*" and "@N" are reserved sharding specs](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#reserved-sharding-spec).




## Example: Write text files to Cloud Storage

The following example creates a batch pipeline that writes text files using GZIP compression:

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.util.Arrays;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.Compression;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Create;
    
    public class BatchWriteStorage {
      public interface Options extends PipelineOptions {
        @Description("The Cloud Storage bucket to write to")
        String getBucketName();
    
        void setBucketName(String value);
      }
    
      // Write text data to Cloud Storage
      public static void main(String[] args) {
        final List<String> wordsList = Arrays.asList("1", "2", "3", "4");
    
        var options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        var pipeline = Pipeline.create(options);
        pipeline
            .apply(Create
                .of(wordsList))
            .apply(TextIO
                .write()
                .to(options.getBucketName())
                .withSuffix(".txt")
                .withCompression(Compression.GZIP)
            );
        pipeline.run().waitUntilFinish();
      }
    }

If the input `PCollection` is unbounded, you must define a window or a trigger on the collection, and then specify windowed writes by calling [`TextIO.Write.withWindowedWrites`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/TextIO.Write.html#withWindowedWrites--). 

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    from typing import List
    
    import apache_beam as beam
    from apache_beam.io.textio import WriteToText
    from apache_beam.options.pipeline_options import PipelineOptions
    
    from typing_extensions import Self
    
    
    def write_to_cloud_storage(argv: List[str] = None) -> None:
        # Parse the pipeline options passed into the application.
        class MyOptions(PipelineOptions):
            @classmethod
            # Define a custom pipeline option that specfies the Cloud Storage bucket.
            def _add_argparse_args(cls: Self, parser: argparse.ArgumentParser) -> None:
                parser.add_argument("--output", required=True)
    
        wordsList = ["1", "2", "3", "4"]
        options = MyOptions()
    
        with beam.Pipeline(options=options.view_as(PipelineOptions)) as pipeline:
            (
                pipeline
                | "Create elements" >> beam.Create(wordsList)
                | "Write Files" >> WriteToText(options.output, file_name_suffix=".txt")
            )
    
    

For the output path, specify a Cloud Storage path that includes the bucket name and a filename prefix. For example, if you specify `gs://my_bucket/output/file`, the `TextIO` connector writes to the Cloud Storage bucket named `my_bucket`, and the output files have the prefix `output/file*`.

By default, the `TextIO` connector shards the output files, using a naming convention like this: `<file-prefix>-00000-of-00001`. Optionally, you can specify a filename suffix and a compression scheme, as shown in the example.

To ensure idempotent writes, Dataflow writes to a temporary file and then copies the completed temporary file to the final file. To control where these temporary files are stored, use the [`withTempDirectory`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/TextIO.TypedWrite.html#withTempDirectory-org.apache.beam.sdk.io.fs.ResourceId-) method.

## What's next

  * Read the [`TextIO`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/TextIO.html) API documentation.
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
