---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-to-gcs/
title: Pub/Sub to Cloud Storage using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:59.877458+00:00
---

# Pub/Sub to Cloud Storage using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-to-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Pub/Sub to Cloud Storage using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Stream Pub/Sub messages to Cloud Storage using Dataflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Stream messages from Pub/Sub by using Dataflow](https://docs.cloud.google.com/pubsub/docs/stream-messages-dataflow)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.io.IOException;
    import org.apache.beam.examples.common.WriteOneFilePerWindow;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.transforms.windowing.FixedWindows;
    import org.apache.beam.sdk.transforms.windowing.Window;
    import org.joda.time.Duration;
    
    public class PubSubToGcs {
      /*
       * Define your own configuration options. Add your own arguments to be processed
       * by the command-line parser, and specify default values for them.
       */
      public interface PubSubToGcsOptions extends StreamingOptions {
        @Description("The Cloud Pub/Sub topic to read from.")
        @Required
        String getInputTopic();
    
        void setInputTopic(String value);
    
        @Description("Output file's window size in number of minutes.")
        @Default.Integer(1)
        Integer getWindowSize();
    
        void setWindowSize(Integer value);
    
        @Description("Path of the output file including its filename prefix.")
        @Required
        String getOutput();
    
        void setOutput(String value);
      }
    
      public static void main(String[] args) throws IOException {
        // The maximum number of shards when writing output.
        int numShards = 1;
    
        PubSubToGcsOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubSubToGcsOptions.class);
    
        options.setStreaming(true);
    
        Pipeline pipeline = Pipeline.create(options);
    
        pipeline
            // 1) Read string messages from a Pub/Sub topic.
            .apply("Read PubSub Messages", PubsubIO.readStrings().fromTopic(options.getInputTopic()))
            // 2) Group the messages into fixed-sized minute intervals.
            .apply(Window.into(FixedWindows.of(Duration.standardMinutes(options.getWindowSize()))))
            // 3) Write one file to GCS for every window of messages.
            .apply("Write Files to GCS", new WriteOneFilePerWindow(options.getOutput(), numShards));
    
        // Execute the pipeline and wait until it finishes running.
        pipeline.run().waitUntilFinish();
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    from datetime import datetime
    import logging
    import random
    
    from apache_beam import (
        DoFn,
        GroupByKey,
        io,
        ParDo,
        Pipeline,
        PTransform,
        WindowInto,
        WithKeys,
    )
    from apache_beam.options.pipeline_options import PipelineOptions
    from apache_beam.transforms.window import FixedWindows
    
    
    class GroupMessagesByFixedWindows(PTransform):
        """A composite transform that groups Pub/Sub messages based on publish time
        and outputs a list of tuples, each containing a message and its publish time.
        """
    
        def __init__(self, window_size, num_shards=5):
            # Set window size to 60 seconds.
            self.window_size = int(window_size * 60)
            self.num_shards = num_shards
    
        def expand(self, pcoll):
            return (
                pcoll
                # Bind window info to each element using element timestamp (or publish time).
                | "Window into fixed intervals"
                >> WindowInto(FixedWindows(self.window_size))
                | "Add timestamp to windowed elements" >> ParDo(AddTimestamp())
                # Assign a random key to each windowed element based on the number of shards.
                | "Add key" >> WithKeys(lambda _: random.randint(0, self.num_shards - 1))
                # Group windowed elements by key. All the elements in the same window must fit
                # memory for this. If not, you need to use `beam.util.BatchElements`.
                | "Group by key" >> GroupByKey()
            )
    
    
    class AddTimestamp(DoFn):
        def process(self, element, publish_time=DoFn.TimestampParam):
            """Processes each windowed element by extracting the message body and its
            publish time into a tuple.
            """
            yield (
                element.decode("utf-8"),
                datetime.utcfromtimestamp(float(publish_time)).strftime(
                    "%Y-%m-%d %H:%M:%S.%f"
                ),
            )
    
    
    class WriteToGCS(DoFn):
        def __init__(self, output_path):
            self.output_path = output_path
    
        def process(self, key_value, window=DoFn.WindowParam):
            """Write messages in a batch to Google Cloud Storage."""
    
            ts_format = "%H:%M"
            window_start = window.start.to_utc_datetime().strftime(ts_format)
            window_end = window.end.to_utc_datetime().strftime(ts_format)
            shard_id, batch = key_value
            filename = "-".join([self.output_path, window_start, window_end, str(shard_id)])
    
            with io.gcsio.GcsIO().open(filename=filename, mode="w") as f:
                for message_body, publish_time in batch:
                    f.write(f"{message_body},{publish_time}\n".encode())
    
    
    def run(input_topic, output_path, window_size=1.0, num_shards=5, pipeline_args=None):
        # Set `save_main_session` to True so DoFns can access globally imported modules.
        pipeline_options = PipelineOptions(
            pipeline_args, streaming=True, save_main_session=True
        )
    
        with Pipeline(options=pipeline_options) as pipeline:
            (
                pipeline
                # Because `timestamp_attribute` is unspecified in `ReadFromPubSub`, Beam
                # binds the publish time returned by the Pub/Sub server for each message
                # to the element's timestamp parameter, accessible via `DoFn.TimestampParam`.
                # https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html#apache_beam.io.gcp.pubsub.ReadFromPubSub
                | "Read from Pub/Sub" >> io.ReadFromPubSub(topic=input_topic)
                | "Window into" >> GroupMessagesByFixedWindows(window_size, num_shards)
                | "Write to GCS" >> ParDo(WriteToGCS(output_path))
            )
    
    
    if __name__ == "__main__":
        logging.getLogger().setLevel(logging.INFO)
    
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--input_topic",
            help="The Cloud Pub/Sub topic to read from."
            '"projects/<PROJECT_ID>/topics/<TOPIC_ID>".',
        )
        parser.add_argument(
            "--window_size",
            type=float,
            default=1.0,
            help="Output file's window size in minutes.",
        )
        parser.add_argument(
            "--output_path",
            help="Path of the output GCS file including the prefix.",
        )
        parser.add_argument(
            "--num_shards",
            type=int,
            default=5,
            help="Number of shards to use when writing windowed elements to GCS.",
        )
        known_args, pipeline_args = parser.parse_known_args()
    
        run(
            known_args.input_topic,
            known_args.output_path,
            known_args.window_size,
            known_args.num_shards,
            pipeline_args,
        )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
