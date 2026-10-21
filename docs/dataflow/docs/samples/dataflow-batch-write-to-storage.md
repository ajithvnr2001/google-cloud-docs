---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-batch-write-to-storage/
title: Output text to Cloud Storage \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:12.014325+00:00
---

# Output text to Cloud Storage  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-batch-write-to-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Output text to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Use the TextIO connector to write text files to a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write from Dataflow to Cloud Storage](https://docs.cloud.google.com/dataflow/docs/guides/write-to-cloud-storage)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
