---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-topic-subscription-to-text/
title: Pub/Sub Topic or Subscription to Text Files on Cloud Storage template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:17.740313+00:00
---

# Pub/Sub Topic or Subscription to Text Files on Cloud Storage template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-topic-subscription-to-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub Topic or Subscription to Text Files on Cloud Storage template Stay organized with collections  Save and categorize content based on your preferences. 

The Pub/Sub Topic or Subscription to Cloud Storage Text template is a streaming pipeline that reads records from Pub/Sub and saves them as a series of Cloud Storage files in text format. The template can be used as a quick way to save data in Pub/Sub for future use. By default, the template generates a new file every 5 minutes.

## Pipeline requirements

  * The Pub/Sub topic or subscription must exist prior to execution.
  * The messages published to the topic must be in text format.
  * The messages published to the topic must not contain any newlines. Note that each Pub/Sub message is saved as a single line in the output file.



## Template parameters

### Required parameters

  * **outputDirectory** : The path and filename prefix to write write output files to. This value must end in a slash. For example, `gs://your-bucket/your-path/`.



### Optional parameters

  * **inputTopic** : The Pub/Sub topic to read the input from. If this parameter is provided don't use `inputSubscription`. For example, `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.
  * **inputSubscription** : The Pub/Sub subscription to read the input from. If this parameter is provided, don't use `inputTopic`. For example, `projects/<PROJECT_ID>/subscription/<SUBSCRIPTION_NAME>`.
  * **userTempLocation** : The user provided directory to output temporary files to. Must end with a slash.
  * **outputFilenamePrefix** : The prefix to place on each windowed file. For example, `output-`. Defaults to: output.
  * **outputFilenameSuffix** : The suffix to place on each windowed file, typically a file extension such as `.txt` or `.csv`. For example, `.txt`. Defaults to empty.
  * **outputShardTemplate** : The shard template defines the dynamic portion of each windowed file. By default, the pipeline uses a single shard for output to the file system within each window. This means that all data outputs into a single file per window. The `outputShardTemplate` defaults to `W-P-SS-of-NN` where `W` is the window date range, `P` is the pane info, `S` is the shard number, and `N` is the number of shards. In case of a single file, the `SS-of-NN` portion of the `outputShardTemplate` is `00-of-01`.
  * **numShards** : The maximum number of output shards produced when writing. A higher number of shards means higher throughput for writing to Cloud Storage, but potentially higher data aggregation cost across shards when processing output Cloud Storage files. Defaults to: 0.
  * **windowDuration** : The window duration is the interval in which data is written to the output directory. Configure the duration based on the pipeline's throughput. For example, a higher throughput might require smaller window sizes so that the data fits into memory. Defaults to `5m` (5 minutes), with a minimum of `1s` (1 second). Allowed formats are: `[int]s` (for seconds, example: `5s`), `[int]m` (for minutes, example: `12m`), `[int]h` (for hours, example: `2h`). For example, `5m`.
  * **yearPattern** : Pattern for formatting the year. Must be one or more of `y` or `Y`. Case makes no difference in the year. The pattern can be optionally wrapped by characters that aren't either alphanumeric or the directory (`/`) character. Defaults to `YYYY`.
  * **monthPattern** : Pattern for formatting the month. Must be one or more of the `M` character. The pattern can be optionally wrapped by characters that aren't alphanumeric or the directory (`/`) character. Defaults to `MM`.
  * **dayPattern** : Pattern for formatting the day. Must be one or more of `d` for day of month or `D` for day of year. Case makes no difference in the year. The pattern can be optionally wrapped by characters that aren't either alphanumeric or the directory (`/`) character. Defaults to `dd`.
  * **hourPattern** : Pattern for formatting the hour. Must be one or more of the `H` character. The pattern can be optionally wrapped by characters that aren't alphanumeric or the directory (`/`) character. Defaults to `HH`.
  * **minutePattern** : Pattern for formatting the minute. Must be one or more of the `m` character. The pattern can be optionally wrapped by characters that aren't alphanumeric or the directory (`/`) character. Defaults to `mm`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub Topic or Subscription to Text Files on Cloud Storage** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=YOUR_PROJECT_ID \
        --region REGION_NAME \
        --template-file-gcs-location gs://dataflow-templates/VERSION/flex/Cloud_PubSub_to_GCS_Text_Flex \
        --parameters \
    inputSubscription=projects/PROJECT_ID/subscriptions/SUBSCRIPTION_NAME,\
    outputDirectory=gs://BUCKET_NAME/output/,\
    outputFilenamePrefix=output-,\
    outputFilenameSuffix=.txt

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `SUBSCRIPTION_NAME`: your Pub/Sub subscription name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
      "launch_parameter": {
        "jobName": "JOB_NAME",
        "parameters": {
           "inputSubscription": "projects/PROJECT_ID/subscriptions/SUBSCRIPTION_NAME"
           "outputDirectory": "gs://BUCKET_NAME/output/",
           "outputFilenamePrefix": "output-",
           "outputFilenameSuffix": ".txt",
        },
        "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Cloud_PubSub_to_GCS_Text_Flex",
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
  * `SUBSCRIPTION_NAME`: your Pub/Sub subscription name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket



This template uses a fixed window, and data that arrives outside of the window might be discarded. To modify the template to change this behavior, see [Extend templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates#extend). 

## Template source code

### Java
    
    
    /*
     * Copyright (C) 2022 Google LLC
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
    package com.google.cloud.teleport.v2.templates.pubsubtotext;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.io.WindowedFilenamePolicy;
    import com.google.cloud.teleport.v2.options.WindowedFilenamePolicyOptions;
    import com.google.cloud.teleport.v2.templates.pubsubtotext.PubsubToText.Options;
    import com.google.cloud.teleport.v2.utils.DurationUtils;
    import com.google.common.base.Strings;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.FileBasedSink;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.transforms.windowing.FixedWindows;
    import org.apache.beam.sdk.transforms.windowing.Window;
    import org.apache.beam.sdk.values.PCollection;
    
    /**
     * This pipeline ingests incoming data from a Cloud Pub/Sub topic and outputs the raw data into
     * windowed files at the specified output directory.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-googlecloud/README_Cloud_PubSub_to_GCS_Text_Flex.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_PubSub_to_GCS_Text_Flex",
        category = TemplateCategory.STREAMING,
        displayName = "Pub/Sub Subscription or Topic to Text Files on Cloud Storage",
        description =
            "The Pub/Sub Topic or Subscription to Cloud Storage Text template is a streaming pipeline that reads records "
                + "from Pub/Sub and saves them as a series of Cloud Storage files in text format. The template can be used as a quick way to save data in Pub/Sub for future use. By default, the template generates a new file every 5 minutes.",
        optionsClass = Options.class,
        flexContainerName = "googlecloud-to-googlecloud",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-topic-subscription-to-text",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The Pub/Sub topic or subscription must exist prior to execution.",
          "The messages published to the topic must be in text format.",
          "The messages published to the topic must not contain any newlines. Note that each Pub/Sub message is saved as a single line in the output file."
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public class PubsubToText {
    
      /**
       * Options supported by the pipeline.
       *
       * <p>Inherits standard configuration options.
       */
      public interface Options
          extends PipelineOptions, StreamingOptions, WindowedFilenamePolicyOptions {
    
        @TemplateParameter.PubsubTopic(
            order = 1,
            groupName = "Source",
            optional = true,
            description = "Pub/Sub input topic",
            helpText =
                "The Pub/Sub topic to read the input from. If this parameter is provided "
                    + "don't use `inputSubscription`.",
            example = "projects/<PROJECT_ID>/topics/<TOPIC_NAME>")
        String getInputTopic();
    
        void setInputTopic(String value);
    
        @TemplateParameter.PubsubSubscription(
            order = 2,
            groupName = "Source",
            optional = true,
            description = "Pub/Sub input subscription",
            helpText =
                "The Pub/Sub subscription to read the input from. If this parameter is "
                    + "provided, don't use `inputTopic`.",
            example = "projects/<PROJECT_ID>/subscription/<SUBSCRIPTION_NAME>")
        String getInputSubscription();
    
        void setInputSubscription(String value);
    
        @TemplateParameter.GcsWriteFolder(
            order = 3,
            groupName = "Target",
            description = "Output file directory in Cloud Storage",
            helpText =
                "The path and filename prefix to write write output files to. "
                    + "This value must end in a slash.",
            example = "gs://your-bucket/your-path/")
        @Required
        String getOutputDirectory();
    
        void setOutputDirectory(String value);
    
        @TemplateParameter.GcsWriteFolder(
            order = 4,
            optional = true,
            description = "User provided temp location",
            helpText =
                "The user provided directory to output temporary files to. Must end with a slash.")
        String getUserTempLocation();
    
        void setUserTempLocation(String value);
    
        @TemplateParameter.Text(
            order = 5,
            groupName = "Target",
            optional = true,
            description = "Output filename prefix of the files to write",
            helpText = "The prefix to place on each windowed file.",
            example = "output-")
        @Default.String("output")
        @Required
        String getOutputFilenamePrefix();
    
        void setOutputFilenamePrefix(String value);
    
        @TemplateParameter.Text(
            order = 6,
            groupName = "Target",
            optional = true,
            description = "Output filename suffix of the files to write",
            helpText =
                "The suffix to place on each windowed file, typically a file extension such as `.txt` or `.csv`.",
            example = ".txt")
        @Default.String("")
        String getOutputFilenameSuffix();
    
        void setOutputFilenameSuffix(String value);
      }
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
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
        boolean useInputSubscription = !Strings.isNullOrEmpty(options.getInputSubscription());
        boolean useInputTopic = !Strings.isNullOrEmpty(options.getInputTopic());
        if (useInputSubscription == useInputTopic) {
          throw new IllegalArgumentException(
              "Either input topic or input subscription must be provided, but not both.");
        }
    
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        PCollection<String> messages = null;
    
        /*
         * Steps:
         *   1) Read string messages from PubSub
         *   2) Window the messages into minute intervals specified by the executor.
         *   3) Output the windowed files to GCS
         */
        if (useInputSubscription) {
          messages =
              pipeline.apply(
                  "Read PubSub Events",
                  PubsubIO.readStrings().fromSubscription(options.getInputSubscription()));
        } else {
          messages =
              pipeline.apply(
                  "Read PubSub Events", PubsubIO.readStrings().fromTopic(options.getInputTopic()));
        }
        messages
            .apply(
                options.getWindowDuration() + " Window",
                Window.into(FixedWindows.of(DurationUtils.parseDuration(options.getWindowDuration()))))
    
            // Apply windowed file writes
            .apply(
                "Write File(s)",
                TextIO.write()
                    .withWindowedWrites()
                    .withNumShards(options.getNumShards())
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
                        FileBasedSink.convertToFileResourceIfPossible(
                            maybeUseUserTempLocation(
                                options.getUserTempLocation(), options.getOutputDirectory()))));
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    
      /**
       * Utility method for using optional parameter userTempLocation as TempDirectory. This is useful
       * when output bucket is locked and temporary data cannot be deleted.
       *
       * @param userTempLocation user provided temp location
       * @param outputLocation user provided outputDirectory to be used as the default temp location
       * @return userTempLocation if available, otherwise outputLocation is returned.
       */
      private static String maybeUseUserTempLocation(String userTempLocation, String outputLocation) {
        return !Strings.isNullOrEmpty(userTempLocation) ? userTempLocation : outputLocation;
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
