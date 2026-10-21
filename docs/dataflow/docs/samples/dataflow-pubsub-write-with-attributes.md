---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-pubsub-write-with-attributes/
title: Write messages with custom attributes to Pub/Sub \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:13.913756+00:00
---

# Write messages with custom attributes to Pub/Sub  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-pubsub-write-with-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Write messages with custom attributes to Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

Use Dataflow to write messages with custom attributes to Pub/Sub

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write from Dataflow to Pub/Sub](https://docs.cloud.google.com/dataflow/docs/guides/write-to-pubsub)



## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.nio.charset.StandardCharsets;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.coders.DefaultCoder;
    import org.apache.beam.sdk.extensions.avro.coders.AvroCoder;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptor;
    
    
    
    public class PubSubWriteWithAttributes {
      public interface Options extends PipelineOptions {
        @Description("The Pub/Sub topic to write to. Format: projects/<PROJECT>/topics/<TOPIC>")
        String getTopic();
    
        void setTopic(String value);
      }
    
      // A custom datatype for the source data.
      @DefaultCoder(AvroCoder.class)
      static class ExampleData {
        public String name;
        public String product;
        public Long timestamp; // Epoch time in milliseconds
    
        public ExampleData() {}
    
        public ExampleData(String name, String product, Long timestamp) {
          this.name = name;
          this.product = product;
          this.timestamp = timestamp;
        }
      }
    
      // Write messages to a Pub/Sub topic.
      public static void main(String[] args) {
        // Example source data.
        final List<ExampleData> messages = Arrays.asList(
            new ExampleData("Robert", "TV", 1613141590000L),
            new ExampleData("Maria", "Phone", 1612718280000L),
            new ExampleData("Juan", "Laptop", 1611618000000L),
            new ExampleData("Rebeca", "Videogame", 1610000000000L)
        );
    
        // Parse the pipeline options passed into the application. Example:
        //   --runner=DirectRunner --topic=projects/MY_PROJECT/topics/MY_TOPIC"
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        var options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        var pipeline = Pipeline.create(options);
        pipeline
            // Create some data to write to Pub/Sub.
            .apply(Create.of(messages))
            // Convert the data to Pub/Sub messages.
            .apply(MapElements
                .into(TypeDescriptor.of(PubsubMessage.class))
                .via((message -> {
                  byte[] payload = message.product.getBytes(StandardCharsets.UTF_8);
                  // Create attributes for each message.
                  HashMap<String, String> attributes = new HashMap<String, String>();
                  attributes.put("buyer", message.name);
                  attributes.put("timestamp", Long.toString(message.timestamp));
                  return new PubsubMessage(payload, attributes);
                })))
            // Write the messages to Pub/Sub.
            .apply(PubsubIO.writeMessages().to(options.getTopic()));
        pipeline.run().waitUntilFinish();
      }
    }

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    from typing import Any, Dict, List
    
    import apache_beam as beam
    from apache_beam.io import PubsubMessage
    from apache_beam.io import WriteToPubSub
    from apache_beam.options.pipeline_options import PipelineOptions
    
    from typing_extensions import Self
    
    
    def item_to_message(item: Dict[str, Any]) -> PubsubMessage:
        # Re-import needed types. When using the Dataflow runner, this
        # function executes on a worker, where the global namespace is not
        # available. For more information, see:
        # https://cloud.google.com/dataflow/docs/guides/common-errors#name-error
        from apache_beam.io import PubsubMessage
    
        attributes = {"buyer": item["name"], "timestamp": str(item["ts"])}
        data = bytes(item["product"], "utf-8")
    
        return PubsubMessage(data=data, attributes=attributes)
    
    
    def write_to_pubsub(argv: List[str] = None) -> None:
        # Parse the pipeline options passed into the application. Example:
        #     --topic=$TOPIC_PATH --streaming
        # For more information, see
        # https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        class MyOptions(PipelineOptions):
            @classmethod
            # Define a custom pipeline option to specify the Pub/Sub topic.
            def _add_argparse_args(cls: Self, parser: argparse.ArgumentParser) -> None:
                parser.add_argument("--topic", required=True)
    
        example_data = [
            {"name": "Robert", "product": "TV", "ts": 1613141590000},
            {"name": "Maria", "product": "Phone", "ts": 1612718280000},
            {"name": "Juan", "product": "Laptop", "ts": 1611618000000},
            {"name": "Rebeca", "product": "Video game", "ts": 1610000000000},
        ]
        options = MyOptions()
    
        with beam.Pipeline(options=options) as pipeline:
            (
                pipeline
                | "Create elements" >> beam.Create(example_data)
                | "Convert to Pub/Sub messages" >> beam.Map(item_to_message)
                | WriteToPubSub(topic=options.topic, with_attributes=True)
            )
    
        print("Pipeline ran successfully.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
