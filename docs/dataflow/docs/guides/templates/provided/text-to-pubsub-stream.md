---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/text-to-pubsub-stream/
title: Text Files on Cloud Storage to Pub/Sub (Stream) template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:51.422854+00:00
---

# Text Files on Cloud Storage to Pub/Sub (Stream) template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/text-to-pubsub-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Text Files on Cloud Storage to Pub/Sub (Stream) template Stay organized with collections  Save and categorize content based on your preferences. 

This template creates a streaming pipeline that continuously polls for new text files uploaded to Cloud Storage, reads each file line by line, and publishes strings to a Pub/Sub topic. The template publishes records in a newline-delimited file containing JSON records or CSV file to a Pub/Sub topic for real-time processing. You can use this template to replay data to Pub/Sub. 

The pipeline runs indefinitely and needs to be terminated manually via a 'cancel' and not a 'drain', due to its use of the 'Watch' transform, which is a 'SplittableDoFn' that does not support draining. 

Currently, the polling interval is fixed and set to 10 seconds. This template does not set any timestamp on the individual records, so the event time is equal to the publishing time during execution. If your pipeline relies on an accurate event time for processing, you shouldn't use this pipeline. 

This template is impacted by [Beam Issue 18459](https://github.com/apache/beam/issues/18459) and will likely have memory issues on large buckets (observed on buckets with 5 million files). Here are some known workarounds: 

  1. Split the files into two or more buckets and use this template.
  2. Create a custom template, possibly forked from this one, that streams file names through Pub/Sub and processes those files.



## Pipeline requirements

  * Input files must be in newline-delimited JSON or CSV format. Records that span multiple lines in the source files can cause issues downstream, because each line within the files is published as a message to Pub/Sub.
  * The Pub/Sub topic must exist prior to execution.
  * The pipeline runs indefinitely and needs to be terminated manually.



## Template parameters

### Required parameters

  * **inputFilePattern** : The input file pattern to read from. For example, `gs://bucket-name/files/*.json`.
  * **outputTopic** : The Pub/Sub input topic to write to. The name must be in the format `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`. For example, `projects/your-project-id/topics/your-topic-name`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Text Files on Cloud Storage to Pub/Sub** (Stream) template.
  5. In the provided parameter fields, enter your parameter values.
  6. Optional: To switch from exactly-once processing to [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), select **At Least Once**.
  7. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Stream_GCS_Text_to_Cloud_PubSub \
        --region REGION_NAME\
        --staging-location STAGING_LOCATION\
        --parameters \
    inputFilePattern=gs://BUCKET_NAME/FILE_PATTERN,\
    outputTopic=projects/PROJECT_ID/topics/TOPIC_NAME

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `TOPIC_NAME`: your Pub/Sub topic name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `FILE_PATTERN`: the file pattern glob to read from in the Cloud Storage bucket (for example, `path/*.csv`)



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Stream_GCS_Text_to_Cloud_PubSub
    {
       "jobName": "JOB_NAME",
       "environment": {
           "ipConfiguration": "WORKER_IP_UNSPECIFIED",
           "additionalExperiments": []
        },
       "parameters": {
           "inputFilePattern": "gs://BUCKET_NAME/FILE_PATTERN",
           "outputTopic": "projects/PROJECT_ID/topics/TOPIC_NAME"
       }
    }

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `TOPIC_NAME`: your Pub/Sub topic name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `FILE_PATTERN`: the file pattern glob to read from in the Cloud Storage bucket (for example, `path/*.csv`)



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
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.templates.TextToPubsub.Options;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Watch;
    import org.joda.time.Duration;
    
    /**
     * The {@code TextToPubsubStream} is a streaming version of {@code TextToPubsub} pipeline that
     * publishes records to Cloud Pub/Sub from a set of files. The pipeline continuously polls for new
     * files, reads them row-by-row and publishes each record as a string message. The polling interval
     * is fixed and equals to 10 seconds. At the moment, publishing messages with attributes is
     * unsupported.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Stream_GCS_Text_to_Cloud_PubSub.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Stream_GCS_Text_to_Cloud_PubSub",
        category = TemplateCategory.STREAMING,
        displayName = "Text Files on Cloud Storage to Pub/Sub",
        description = {
          "This template creates a streaming pipeline that continuously polls for new text files uploaded to Cloud Storage, reads each file line by line, and publishes strings to a Pub/Sub topic. "
              + "The template publishes records in a newline-delimited file containing JSON records or CSV file to a Pub/Sub topic for real-time processing. "
              + "You can use this template to replay data to Pub/Sub.\n",
          "The pipeline runs indefinitely and needs to be terminated manually via a <a href=\"https://cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel\">cancel</a> and not a <a href=\"https://cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain\">drain</a>, due to its use of the <code>Watch</code> transform, which is a <code>SplittableDoFn</code> that does not support draining.\n",
          "Currently, the polling interval is fixed and set to 10 seconds. This template does not set any timestamp on the individual records, so the event time is equal to the publishing time during execution. "
              + "If your pipeline relies on an accurate event time for processing, you should not use this pipeline."
        },
        optionsClass = Options.class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/text-to-pubsub-stream",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "Input files must be in newline-delimited JSON or CSV format. Records that span multiple lines in the source files can cause issues downstream, because each line within the files is published as a message to Pub/Sub.",
          "The Pub/Sub topic must exist prior to execution.",
          "The pipeline runs indefinitely and needs to be terminated manually.",
        },
        streaming = true,
        supportsAtLeastOnce = true,
        supportsExactlyOnce = true)
    public class TextToPubsubStream {
      private static final Duration DEFAULT_POLL_INTERVAL = Duration.standardSeconds(10);
    
      /**
       * Main entry-point for the pipeline. Reads in the command-line arguments, parses them, and
       * executes the pipeline.
       *
       * @param args Arguments passed in from the command-line.
       */
      public static void main(String[] args) {
    
        // Parse the user options passed from the command-line
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
    
        run(options);
      }
    
      /**
       * Executes the pipeline with the provided execution parameters.
       *
       * @param options The execution parameters.
       */
      public static PipelineResult run(Options options) {
        // Create the pipeline.
        Pipeline pipeline = Pipeline.create(options);
    
        /*
         * Steps:
         *  1) Read from the text source.
         *  2) Write each text record to Pub/Sub
         */
        pipeline
            .apply(
                "Read Text Data",
                TextIO.read()
                    .from(options.getInputFilePattern())
                    .watchForNewFiles(DEFAULT_POLL_INTERVAL, Watch.Growth.never()))
            .apply("Write to PubSub", PubsubIO.writeStrings().to(options.getOutputTopic()));
    
        return pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
