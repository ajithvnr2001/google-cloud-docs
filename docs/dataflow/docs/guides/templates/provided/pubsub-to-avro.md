---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-avro/
title: Pub/Sub to Avro Files on Cloud Storage template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:17.114311+00:00
---

# Pub/Sub to Avro Files on Cloud Storage template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-avro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub to Avro Files on Cloud Storage template Stay organized with collections  Save and categorize content based on your preferences. 

The Pub/Sub to Avro files on Cloud Storage template is a streaming pipeline that reads data from a Pub/Sub topic and writes Avro files into the specified Cloud Storage bucket.

## Pipeline requirements

  * The input Pub/Sub topic must exist prior to pipeline execution.



## Template parameters

### Required parameters

  * **inputTopic** : The Pub/Sub topic to subscribe to for message consumption. The topic name must be in the format `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.
  * **outputDirectory** : The output directory where output Avro files are archived. Must contain `/` at the end. For example: `gs://example-bucket/example-directory/`.
  * **avroTempDirectory** : The directory for temporary Avro files. Must contain `/` at the end. For example: `gs://example-bucket/example-directory/`.



### Optional parameters

  * **outputFilenamePrefix** : The output filename prefix for the Avro files. Defaults to: output.
  * **outputFilenameSuffix** : The output filename suffix for the Avro files. Defaults to empty.
  * **outputShardTemplate** : The shard template defines the dynamic portion of each windowed file. By default, the pipeline uses a single shard for output to the file system within each window. Therefore, all data outputs into a single file per window. The `outputShardTemplate` defaults `to W-P-SS-of-NN`, where `W` is the window date range, `P` is the pane info, `S` is the shard number, and `N` is the number of shards. In case of a single file, the `SS-of-NN` portion of the `outputShardTemplate` is `00-of-01`.
  * **yearPattern** : Pattern for formatting the year. Must be one or more of `y` or `Y`. Case makes no difference in the year. Optionally, wrap the pattern with characters that aren't alphanumeric or the directory (`/`) character. Defaults to `YYYY`.
  * **monthPattern** : Pattern for formatting the month. Must be one or more of the `M` character. Optionally, wrap the pattern with characters that aren't alphanumeric or the directory (`/`) character. Defaults to `MM`.
  * **dayPattern** : Pattern for formatting the day. Must be one or more of `d` for day of month or `D` for day of year. Optionally, wrap the pattern with characters that aren't alphanumeric or the directory (`/`) character. Defaults to `dd`.
  * **hourPattern** : Pattern for formatting the hour. Must be one or more of the `H` character. Optionally, wrap the pattern with characters that aren't alphanumeric or the directory (`/`) character. Defaults to `HH`.
  * **minutePattern** : Pattern for formatting the minute. Must be one or more of the `m` character. Optionally, wrap the pattern with characters that aren't alphanumeric or the directory (`/`) character. Defaults to `mm`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub to Avro Files on Cloud Storage** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Cloud_PubSub_to_Avro \
        --region REGION_NAME \
        --staging-location STAGING_LOCATION \
        --parameters \
    inputTopic=projects/PROJECT_ID/topics/TOPIC_NAME,\
    outputDirectory=gs://BUCKET_NAME/output/,\
    outputFilenamePrefix=FILENAME_PREFIX,\
    outputFilenameSuffix=FILENAME_SUFFIX,\
    outputShardTemplate=SHARD_TEMPLATE,\
    avroTempDirectory=gs://BUCKET_NAME/temp/

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `TOPIC_NAME`: the Pub/Sub topic name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `FILENAME_PREFIX`: the preferred output filename prefix
  * `FILENAME_SUFFIX`: the preferred output filename suffix
  * `SHARD_TEMPLATE`: the preferred output shard template



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Cloud_PubSub_to_Avro
    {
       "jobName": "JOB_NAME",
       "environment": {
           "ipConfiguration": "WORKER_IP_UNSPECIFIED",
           "additionalExperiments": []
        },
       "parameters": {
           "inputTopic": "projects/PROJECT_ID/topics/TOPIC_NAME",
           "outputDirectory": "gs://BUCKET_NAME/output/",
           "avroTempDirectory": "gs://BUCKET_NAME/temp/",
           "outputFilenamePrefix": "FILENAME_PREFIX",
           "outputFilenameSuffix": "FILENAME_SUFFIX",
           "outputShardTemplate": "SHARD_TEMPLATE"
       }
    }

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `TOPIC_NAME`: the Pub/Sub topic name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `FILENAME_PREFIX`: the preferred output filename prefix
  * `FILENAME_SUFFIX`: the preferred output filename suffix
  * `SHARD_TEMPLATE`: the preferred output shard template



This template uses a fixed window, and data that arrives outside of the window might be discarded. To modify the template to change this behavior, see [Extend templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates#extend). 

## Template source code

### Java
    
    
    /*
     * Copyright (C) 2018 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License"); you may not
     * use this file except in compliance with the License. You may obtain a copy of
     * the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
     * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
     * License for the specific language governing permissions and limitations under
     * the License.
     */
    package com.google.cloud.teleport.templates;
    
    import com.google.cloud.teleport.avro.AvroPubsubMessageRecord;
    import com.google.cloud.teleport.io.WindowedFilenamePolicy;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateCreationParameter;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.options.WindowedFilenamePolicyOptions;
    import com.google.cloud.teleport.templates.PubsubToAvro.Options;
    import com.google.cloud.teleport.util.DurationUtils;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.extensions.avro.io.AvroIO;
    import org.apache.beam.sdk.io.FileBasedSink;
    import org.apache.beam.sdk.io.fs.ResourceId;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.options.ValueProvider.NestedValueProvider;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.transforms.windowing.FixedWindows;
    import org.apache.beam.sdk.transforms.windowing.Window;
    import org.apache.beam.sdk.values.PCollection;
    
    /**
     * This pipeline ingests incoming data from a Cloud Pub/Sub topic and outputs the raw data into
     * windowed Avro files at the specified output directory.
     *
     * <p>Files output will have the following schema:
     *
     * <pre>
     *   {
     *      "type": "record",
     *      "name": "AvroPubsubMessageRecord",
     *      "namespace": "com.google.cloud.teleport.avro",
     *      "fields": [
     *        {"name": "message", "type": {"type": "array", "items": "bytes"}},
     *        {"name": "attributes", "type": {"type": "map", "values": "string"}},
     *        {"name": "timestamp", "type": "long"}
     *      ]
     *   }
     * </pre>
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Cloud_PubSub_to_Avro.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_PubSub_to_Avro",
        category = TemplateCategory.STREAMING,
        displayName = "Pub/Sub to Avro Files on Cloud Storage",
        description =
            "The Pub/Sub to Avro files on Cloud Storage template is a streaming pipeline that reads data from a Pub/Sub "
                + "topic and writes Avro files into the specified Cloud Storage bucket.",
        optionsClass = Options.class,
        skipOptions = "inputSubscription",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-avro",
        contactInformation = "https://cloud.google.com/support",
        requirements = {"The input Pub/Sub topic must exist prior to pipeline execution."},
        streaming = true,
        supportsAtLeastOnce = true)
    public class PubsubToAvro {
    
      /**
       * Options supported by the pipeline.
       *
       * <p>Inherits standard configuration options.
       */
      public interface Options
          extends PipelineOptions, StreamingOptions, WindowedFilenamePolicyOptions {
        @TemplateParameter.PubsubSubscription(
            order = 1,
            groupName = "Source",
            description = "Pub/Sub input subscription",
            helpText = "The Pub/Sub subscription to read the input from.",
            example = "projects/<PROJECT_ID>/subscriptions/<SUBSCRIPTION_NAME>")
        ValueProvider<String> getInputSubscription();
    
        void setInputSubscription(ValueProvider<String> value);
    
        @TemplateParameter.PubsubTopic(
            order = 2,
            groupName = "Source",
            description = "Pub/Sub input topic",
            helpText =
                "The Pub/Sub topic to subscribe to for message consumption. The topic name must be in the format `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.")
        ValueProvider<String> getInputTopic();
    
        void setInputTopic(ValueProvider<String> value);
    
        @TemplateCreationParameter(value = "false")
        @Description(
            "This determines whether the template reads from " + "a pub/sub subscription or a topic")
        @Default.Boolean(false)
        Boolean getUseSubscription();
    
        void setUseSubscription(Boolean value);
    
        @TemplateParameter.GcsWriteFolder(
            order = 4,
            groupName = "Target",
            description = "Output file directory in Cloud Storage",
            helpText =
                "The output directory where output Avro files are archived. Must contain `/` at the end. For example: `gs://example-bucket/example-directory/`")
        @Required
        ValueProvider<String> getOutputDirectory();
    
        void setOutputDirectory(ValueProvider<String> value);
    
        @TemplateParameter.Text(
            order = 5,
            groupName = "Target",
            optional = true,
            description = "Output filename prefix of the files to write",
            helpText = "The output filename prefix for the Avro files.",
            regexes = "^[a-zA-Z\\-]+$")
        @Default.String("output")
        ValueProvider<String> getOutputFilenamePrefix();
    
        void setOutputFilenamePrefix(ValueProvider<String> value);
    
        @TemplateParameter.Text(
            order = 6,
            groupName = "Target",
            optional = true,
            description = "Output filename suffix of the files to write",
            helpText = "The output filename suffix for the Avro files.")
        @Default.String("")
        ValueProvider<String> getOutputFilenameSuffix();
    
        void setOutputFilenameSuffix(ValueProvider<String> value);
    
        @TemplateParameter.GcsWriteFolder(
            order = 7,
            description = "Temporary Avro write directory",
            helpText =
                "The directory for temporary Avro files. Must contain `/` at the end. For example: `gs://example-bucket/example-directory/`.")
        @Required
        ValueProvider<String> getAvroTempDirectory();
    
        void setAvroTempDirectory(ValueProvider<String> value);
      }
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
    
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        options.setStreaming(true);
    
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static PipelineResult run(Options options) {
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        PCollection<PubsubMessage> messages = null;
    
        /*
         * Steps:
         *   1) Read messages from PubSub
         *   2) Window the messages into minute intervals specified by the executor.
         *   3) Output the windowed data into Avro files, one per window by default.
         */
    
        if (options.getUseSubscription()) {
          messages =
              pipeline.apply(
                  "Read PubSub Events",
                  PubsubIO.readMessagesWithAttributes()
                      .fromSubscription(options.getInputSubscription()));
        } else {
          messages =
              pipeline.apply(
                  "Read PubSub Events",
                  PubsubIO.readMessagesWithAttributes().fromTopic(options.getInputTopic()));
        }
        messages
            .apply("Map to Archive", ParDo.of(new PubsubMessageToArchiveDoFn()))
            .apply(
                options.getWindowDuration() + " Window",
                Window.into(FixedWindows.of(DurationUtils.parseDuration(options.getWindowDuration()))))
    
            // Apply windowed file writes. Use a NestedValueProvider because the filename
            // policy requires a resourceId generated from the input value at runtime.
            .apply(
                "Write File(s)",
                AvroIO.write(AvroPubsubMessageRecord.class)
                    .to(
                        WindowedFilenamePolicy.writeWindowedFiles()
                            .withOutputDirectory(options.getOutputDirectory())
                            .withOutputFilenamePrefix(options.getOutputFilenamePrefix())
                            .withShardTemplate(options.getOutputShardTemplate())
                            .withSuffix(options.getOutputFilenameSuffix())
                            .withYearPattern(options.getYearPattern())
                            .withMonthPattern(options.getMonthPattern())
                            .withDayPattern(options.getDayPattern())
                            .withHourPattern(options.getHourPattern())
                            .withMinutePattern(options.getMinutePattern()))
                    .withTempDirectory(
                        NestedValueProvider.of(
                            options.getAvroTempDirectory(),
                            (SerializableFunction<String, ResourceId>)
                                input -> FileBasedSink.convertToFileResourceIfPossible(input)))
                    /*.withTempDirectory(FileSystems.matchNewResource(
                    options.getAvroTempDirectory(),
                    Boolean.TRUE))
                    */
                    .withWindowedWrites()
                    .withNumShards(options.getNumShards()));
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    
      /**
       * Converts an incoming {@link PubsubMessage} to the {@link AvroPubsubMessageRecord} class by
       * copying its fields and the timestamp of the message.
       */
      static class PubsubMessageToArchiveDoFn extends DoFn<PubsubMessage, AvroPubsubMessageRecord> {
        @ProcessElement
        public void processElement(ProcessContext context) {
          PubsubMessage message = context.element();
          context.output(
              new AvroPubsubMessageRecord(
                  message.getPayload(), message.getAttributeMap(), context.timestamp().getMillis()));
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
