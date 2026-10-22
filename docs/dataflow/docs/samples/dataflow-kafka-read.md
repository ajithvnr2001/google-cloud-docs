---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-kafka-read/
title: Read from Apache Kafka to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:38.399822+00:00
---

# Read from Apache Kafka to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-kafka-read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Read from Apache Kafka to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to create a Dataflow pipeline that reads from Apache Kafka

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Read from Apache Kafka to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka)



## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import java.io.UnsupportedEncodingException;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptors;
    
    public class KafkaRead {
    
      public static Pipeline createPipeline(Options options) {
    
        // Create configuration parameters for the Managed I/O transform.
        ImmutableMap<String, Object> config = ImmutableMap.<String, Object>builder()
            .put("bootstrap_servers", options.getBootstrapServer())
            .put("topic", options.getTopic())
            .put("format", "RAW")
            .put("max_read_time_seconds", 15)
            .put("auto_offset_reset_config", "earliest")
            .build();
    
        // Build the pipeline.
        var pipeline = Pipeline.create(options);
        pipeline
            // Read messages from Kafka.
            .apply(Managed.read(Managed.KAFKA).withConfig(config)).getSinglePCollection()
            // Get the payload of each message and convert to a string.
            .apply(MapElements
                .into(TypeDescriptors.strings())
                .via((row -> {
                  var bytes = row.getBytes("payload");
                  try {
                    return new String(bytes, "UTF-8");
                  } catch (UnsupportedEncodingException e) {
                    throw new RuntimeException(e);
                  }
                })))
            // Write the payload to a text file.
            .apply(TextIO
                .write()
                .to(options.getOutputPath())
                .withSuffix(".txt")
                .withNumShards(1));
        return pipeline;
      }
    }

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    import apache_beam as beam
    
    from apache_beam import window
    from apache_beam.io.textio import WriteToText
    from apache_beam.options.pipeline_options import PipelineOptions
    
    
    def read_from_kafka() -> None:
        # Parse the pipeline options passed into the application. Example:
        #     --topic=$KAFKA_TOPIC --bootstrap_server=$BOOTSTRAP_SERVER
        #     --output=$CLOUD_STORAGE_BUCKET --streaming
        # For more information, see
        # https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        class MyOptions(PipelineOptions):
            @staticmethod
            def _add_argparse_args(parser: argparse.ArgumentParser) -> None:
                parser.add_argument("--topic")
                parser.add_argument("--bootstrap_server")
                parser.add_argument("--output")
    
        options = MyOptions()
        with beam.Pipeline(options=options) as pipeline:
            (
                pipeline
                # Read messages from an Apache Kafka topic.
                | beam.managed.Read(
                    beam.managed.KAFKA,
                    config={
                      "bootstrap_servers": options.bootstrap_server,
                      "topic": options.topic,
                      "data_format": "RAW",
                      "auto_offset_reset_config": "earliest",
                      # The max_read_time_seconds parameter is intended for testing.
                      # Avoid using this parameter in production.
                      "max_read_time_seconds": 5
                    }
                )
                # Subdivide the output into fixed 5-second windows.
                | beam.WindowInto(window.FixedWindows(5))
                | WriteToText(
                    file_path_prefix=options.output, file_name_suffix=".txt", num_shards=1
                )
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
