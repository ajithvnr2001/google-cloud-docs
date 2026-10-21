---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-kafka-read-multi-topic/
title: Read from multiple Kafka topics to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:12.722937+00:00
---

# Read from multiple Kafka topics to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-kafka-read-multi-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Read from multiple Kafka topics to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to create a Dataflow pipeline that reads from multiple Kafka topics and performs different business logic based on the topic name.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Read from Apache Kafka to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka)



## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.kafka.KafkaIO;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.transforms.Filter;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.apache.kafka.common.serialization.LongDeserializer;
    import org.apache.kafka.common.serialization.StringDeserializer;
    import org.joda.time.Duration;
    import org.joda.time.Instant;
    
    public class KafkaReadTopics {
    
      public static Pipeline createPipeline(Options options) {
        String topic1 = options.getTopic1();
        String topic2 = options.getTopic2();
    
        // Build the pipeline.
        var pipeline = Pipeline.create(options);
        var allTopics = pipeline
            .apply(KafkaIO.<Long, String>read()
                .withTopics(List.of(topic1, topic2))
                .withBootstrapServers(options.getBootstrapServer())
                .withKeyDeserializer(LongDeserializer.class)
                .withValueDeserializer(StringDeserializer.class)
                .withMaxReadTime(Duration.standardSeconds(10))
                .withStartReadTime(Instant.EPOCH)
            );
    
        // Create separate pipeline branches for each topic.
        // The first branch filters on topic1.
        allTopics
            .apply(Filter.by(record -> record.getTopic().equals(topic1)))
            .apply(MapElements
                .into(TypeDescriptors.strings())
                .via(record -> record.getKV().getValue()))
            .apply(TextIO.write()
                .to(topic1)
                .withSuffix(".txt")
                .withNumShards(1)
            );
    
        // The second branch filters on topic2.
        allTopics
            .apply(Filter.by(record -> record.getTopic().equals(topic2)))
            .apply(MapElements
                .into(TypeDescriptors.strings())
                .via(record -> record.getKV().getValue()))
            .apply(TextIO.write()
                .to(topic2)
                .withSuffix(".txt")
                .withNumShards(1)
            );
        return pipeline;
      }
    }

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    import apache_beam as beam
    
    from apache_beam.io.kafka import ReadFromKafka
    from apache_beam.io.textio import WriteToText
    from apache_beam.options.pipeline_options import PipelineOptions
    
    
    def read_from_kafka() -> None:
        # Parse the pipeline options passed into the application. Example:
        #   --bootstrap_server=$BOOTSTRAP_SERVER --output=$STORAGE_BUCKET --streaming
        # For more information, see
        # https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        class MyOptions(PipelineOptions):
            @staticmethod
            def _add_argparse_args(parser: argparse.ArgumentParser) -> None:
                parser.add_argument('--bootstrap_server')
                parser.add_argument('--output')
    
        options = MyOptions()
        with beam.Pipeline(options=options) as pipeline:
            # Read from two Kafka topics.
            all_topics = pipeline | ReadFromKafka(consumer_config={
                    "bootstrap.servers": options.bootstrap_server
                },
                topics=["topic1", "topic2"],
                with_metadata=True,
                max_num_records=10,
                start_read_time=0
            )
    
            # Filter messages from one topic into one branch of the pipeline.
            (all_topics
                | beam.Filter(lambda message: message.topic == 'topic1')
                | beam.Map(lambda message: message.value.decode('utf-8'))
                | "Write topic1" >> WriteToText(
                    file_path_prefix=options.output + '/topic1/output',
                    file_name_suffix='.txt',
                    num_shards=1))
    
            # Filter messages from the other topic.
            (all_topics
                | beam.Filter(lambda message: message.topic == 'topic2')
                | beam.Map(lambda message: message.value.decode('utf-8'))
                | "Write topic2" >> WriteToText(
                    file_path_prefix=options.output + '/topic2/output',
                    file_name_suffix='.txt',
                    num_shards=1))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
