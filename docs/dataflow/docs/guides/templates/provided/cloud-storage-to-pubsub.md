---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-pubsub/
title: Cloud Storage Text to Pub/Sub (Batch) template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:11.106158+00:00
---

# Cloud Storage Text to Pub/Sub (Batch) template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage Text to Pub/Sub (Batch) template Stay organized with collections  Save and categorize content based on your preferences. 

This template creates a batch pipeline that reads records from text files stored in Cloud Storage and publishes them to a Pub/Sub topic. The template can be used to publish records in a newline-delimited file containing JSON records or CSV file to a Pub/Sub topic for real-time processing. You can use this template to replay data to Pub/Sub. 

This template does not set any timestamp on the individual records. The event time is equal to the publishing time during execution. If your pipeline relies on an accurate event time for processing, you must not use this pipeline.

## Pipeline requirements

  * The files to read need to be in newline-delimited JSON or CSV format. Records spanning multiple lines in the source files might cause issues downstream because each line within the files will be published as a message to Pub/Sub.
  * The Pub/Sub topic must exist before running the pipeline.



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

  4. From the **Dataflow template** drop-down menu, select the **Text Files on Cloud Storage to Pub/Sub** (Batch) template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/GCS_Text_to_Cloud_PubSub \
        --region REGION_NAME \
        --parameters \
    inputFilePattern=gs://BUCKET_NAME/files/*.json,\
    outputTopic=projects/PROJECT_ID/topics/TOPIC_NAME

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `TOPIC_NAME`: your Pub/Sub topic name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/GCS_Text_to_Cloud_PubSub
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "inputFilePattern": "gs://BUCKET_NAME/files/*.json",
           "outputTopic": "projects/PROJECT_ID/topics/TOPIC_NAME"
       },
       "environment": { "zone": "us-central1-f" }
    }

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `TOPIC_NAME`: your Pub/Sub topic name
  * `BUCKET_NAME`: the name of your Cloud Storage bucket



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
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.templates.TextToPubsub.Options;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.options.ValueProvider;
    
    /**
     * The {@code TextToPubsub} pipeline publishes records to Cloud Pub/Sub from a set of files. The
     * pipeline reads each file row-by-row and publishes each record as a string message. At the moment,
     * publishing messages with attributes is unsupported.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_GCS_Text_to_Cloud_PubSub.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "GCS_Text_to_Cloud_PubSub",
        category = TemplateCategory.BATCH,
        displayName = "Cloud Storage Text File to Pub/Sub (Batch)",
        description = {
          "This template creates a batch pipeline that reads records from text files stored in Cloud Storage and publishes them to a Pub/Sub topic. "
              + "The template can be used to publish records in a newline-delimited file containing JSON records or CSV file to a Pub/Sub topic for real-time processing. "
              + "You can use this template to replay data to Pub/Sub.\n",
          "This template does not set any timestamp on the individual records. The event time is equal to the publishing time during execution. "
              + "If your pipeline relies on an accurate event time for processing, you must not use this pipeline."
        },
        optionsClass = Options.class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-pubsub",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The files to read need to be in newline-delimited JSON or CSV format. Records spanning multiple lines in the source files might cause issues downstream because each line within the files will be published as a message to Pub/Sub.",
          "The Pub/Sub topic must exist before running the pipeline."
        })
    public class TextToPubsub {
    
      /** The custom options supported by the pipeline. Inherits standard configuration options. */
      public interface Options extends PipelineOptions {
        @TemplateParameter.GcsReadFile(
            order = 1,
            groupName = "Source",
            description = "Cloud Storage Input File(s)",
            helpText = "The input file pattern to read from.",
            example = "gs://bucket-name/files/*.json")
        @Required
        ValueProvider<String> getInputFilePattern();
    
        void setInputFilePattern(ValueProvider<String> value);
    
        @TemplateParameter.PubsubTopic(
            order = 2,
            groupName = "Target",
            description = "Output Pub/Sub topic",
            helpText =
                "The Pub/Sub input topic to write to. The name must be in the format `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.",
            example = "projects/your-project-id/topics/your-topic-name")
        @Required
        ValueProvider<String> getOutputTopic();
    
        void setOutputTopic(ValueProvider<String> value);
      }
    
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
            .apply("Read Text Data", TextIO.read().from(options.getInputFilePattern()))
            .apply("Write to PubSub", PubsubIO.writeStrings().to(options.getOutputTopic()));
    
        return pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
