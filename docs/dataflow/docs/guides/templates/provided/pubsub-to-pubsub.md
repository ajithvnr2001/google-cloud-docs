---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-pubsub/
title: Pub/Sub to Pub/Sub template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:48.836786+00:00
---

# Pub/Sub to Pub/Sub template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub to Pub/Sub template Stay organized with collections  Save and categorize content based on your preferences. 

The Pub/Sub to Pub/Sub template is a streaming pipeline that reads messages from a Pub/Sub subscription and writes the messages to another Pub/Sub topic. The pipeline also accepts an optional message attribute key and a value that can be used to filter the messages that should be written to the Pub/Sub topic. You can use this template to copy messages from a Pub/Sub subscription to another Pub/Sub topic with an optional message filter.

## Pipeline requirements

  * The source Pub/Sub subscription must exist prior to execution.
  * The source Pub/Sub subscription must be a [pull subscription](https://cloud.google.com/pubsub/docs/pull).
  * The destination Pub/Sub topic must exist prior to execution.



## Template parameters

### Required parameters

  * **inputSubscription** : The Pub/Sub subscription to read the input from. For example, `projects/your-project-id/subscriptions/your-subscription-name`.
  * **outputTopic** : The Pub/Sub topic to write the output to. For example, `projects/your-project-id/topics/your-topic-name`.



### Optional parameters

  * **filterKey** : The attribute key to use to filter events. No filters are applied if `filterKey` is not specified.
  * **filterValue** : The attribute value to use to filter events when a `filterKey` is provided. By default, a null `filterValue` is used.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub to Pub/Sub** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Optional: To switch from exactly-once processing to [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), select **At Least Once**.
  7. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Cloud_PubSub_to_Cloud_PubSub \
        --region REGION_NAME \
        --staging-location STAGING_LOCATION \
        --parameters \
    inputSubscription=projects/PROJECT_ID/subscriptions/SUBSCRIPTION_NAME,\
    outputTopic=projects/PROJECT_ID/topics/TOPIC_NAME,\
    filterKey=FILTER_KEY,\
    filterValue=FILTER_VALUE

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `STAGING_LOCATION`: the location for staging local files (for example, `gs://your-bucket/staging`)
  * `SUBSCRIPTION_NAME`: the Pub/Sub subscription name
  * `TOPIC_NAME`: the Pub/Sub topic name
  * `FILTER_KEY`: the attribute key by which events are filtered. No filters are applied if no key is specified.
  * `FILTER_VALUE`: filter attribute value to use if an event filter key is provided. Accepts a valid Java Regex string as an event filter value. In case a regex is provided, the complete expression should match in order for the message to be filtered. Partial matches (such as substring) are not filtered. A null event filter value is used by default.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Cloud_PubSub_to_Cloud_PubSub
    {
       "jobName": "JOB_NAME",
       "environment": {
           "ipConfiguration": "WORKER_IP_UNSPECIFIED",
           "additionalExperiments": []
        },
       "parameters": {
           "inputSubscription": "projects/PROJECT_ID/subscriptions/SUBSCRIPTION_NAME",
           "outputTopic": "projects/PROJECT_ID/topics/TOPIC_NAME",
           "filterKey": "FILTER_KEY",
           "filterValue": "FILTER_VALUE"
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
  * `SUBSCRIPTION_NAME`: the Pub/Sub subscription name
  * `TOPIC_NAME`: the Pub/Sub topic name
  * `FILTER_KEY`: the attribute key by which events are filtered. No filters are applied if no key is specified.
  * `FILTER_VALUE`: filter attribute value to use if an event filter key is provided. Accepts a valid Java Regex string as an event filter value. In case a regex is provided, the complete expression should match in order for the message to be filtered. Partial matches (such as substring) are not filtered. A null event filter value is used by default.



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
    
    import static com.google.common.base.Preconditions.checkNotNull;
    import static org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.base.Preconditions.checkArgument;
    
    import com.google.auto.value.AutoValue;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.templates.PubsubToPubsub.Options;
    import java.util.regex.Pattern;
    import java.util.regex.PatternSyntaxException;
    import javax.annotation.Nullable;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.metrics.Counter;
    import org.apache.beam.sdk.metrics.Metrics;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.options.Validation;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * A template that copies messages from one Pubsub subscription to another Pubsub topic. Allows
     * filtering specific messages.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Cloud_PubSub_to_Cloud_PubSub.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Cloud_PubSub_to_Cloud_PubSub",
        category = TemplateCategory.STREAMING,
        displayName = "Pub/Sub to Pub/Sub",
        description =
            "The Pub/Sub to Pub/Sub template is a streaming pipeline that reads messages from a Pub/Sub subscription and "
                + "writes the messages to another Pub/Sub topic. The pipeline also accepts an optional message attribute key and a value that can be used to filter the messages that should be written to the Pub/Sub topic. You can use this template to copy messages from a Pub/Sub subscription to another Pub/Sub topic with an optional message filter.",
        optionsClass = Options.class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-pubsub",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The source Pub/Sub subscription must exist prior to execution.",
          "The source Pub/Sub subscription must be a <a href=\"https://cloud.google.com/pubsub/docs/pull\">pull subscription</a>.",
          "The destination Pub/Sub topic must exist prior to execution."
        },
        streaming = true,
        supportsAtLeastOnce = true,
        supportsExactlyOnce = true)
    public class PubsubToPubsub {
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main(String[] args) {
    
        // Parse the user options passed from the command-line
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
    
        /*
         Steps:
    
         <p>1) Read PubSubMessage with attributes from input PubSub subscription.
    
         <p>2) Apply any filters if an attribute=value pair is provided.
    
         <p>3) Write each PubSubMessage to output PubSub topic.
        */
        pipeline
            .apply(
                "Read PubSub Events",
                PubsubIO.readMessagesWithAttributes().fromSubscription(options.getInputSubscription()))
            .apply(
                "Filter Events If Enabled",
                ParDo.of(
                    ExtractAndFilterEventsFn.newBuilder()
                        .withFilterKey(options.getFilterKey())
                        .withFilterValue(options.getFilterValue())
                        .build()))
            .apply("Write PubSub Events", PubsubIO.writeMessages().to(options.getOutputTopic()));
    
        // Execute the pipeline and return the result.
        return pipeline.run();
      }
    
      /**
       * Options supported by {@link PubsubToPubsub}.
       *
       * <p>Inherits standard configuration options.
       */
      public interface Options extends PipelineOptions, StreamingOptions {
        @TemplateParameter.PubsubSubscription(
            order = 1,
            groupName = "Source",
            description = "Pub/Sub input subscription",
            helpText = "The Pub/Sub subscription to read the input from.",
            example = "projects/your-project-id/subscriptions/your-subscription-name")
        @Validation.Required
        ValueProvider<String> getInputSubscription();
    
        void setInputSubscription(ValueProvider<String> inputSubscription);
    
        @TemplateParameter.PubsubTopic(
            order = 2,
            groupName = "Target",
            description = "Output Pub/Sub topic",
            helpText = "The Pub/Sub topic to write the output to.",
            example = "projects/your-project-id/topics/your-topic-name")
        @Validation.Required
        ValueProvider<String> getOutputTopic();
    
        void setOutputTopic(ValueProvider<String> outputTopic);
    
        @TemplateParameter.Text(
            order = 3,
            optional = true,
            description = "Event filter key",
            helpText =
                "The attribute key to use to filter events. No filters are applied if `filterKey` is not specified.")
        ValueProvider<String> getFilterKey();
    
        void setFilterKey(ValueProvider<String> filterKey);
    
        @TemplateParameter.Text(
            order = 4,
            optional = true,
            description = "Event filter value",
            helpText =
                "The attribute value to use to filter events when a `filterKey` is provided. By default, a null `filterValue` is used.")
        ValueProvider<String> getFilterValue();
    
        void setFilterValue(ValueProvider<String> filterValue);
      }
    
      /**
       * DoFn that will determine if events are to be filtered. If filtering is enabled, it will only
       * publish events that pass the filter else, it will publish all input events.
       */
      @AutoValue
      public abstract static class ExtractAndFilterEventsFn extends DoFn<PubsubMessage, PubsubMessage> {
    
        private static final Logger LOG = LoggerFactory.getLogger(ExtractAndFilterEventsFn.class);
    
        // Counter tracking the number of incoming Pub/Sub messages.
        private static final Counter INPUT_COUNTER =
            Metrics.counter(ExtractAndFilterEventsFn.class, "inbound-messages");
    
        // Counter tracking the number of output Pub/Sub messages after the user provided filter
        // is applied.
        private static final Counter OUTPUT_COUNTER =
            Metrics.counter(ExtractAndFilterEventsFn.class, "filtered-outbound-messages");
    
        private Boolean doFilter;
        private String inputFilterKey;
        private Pattern inputFilterValueRegex;
        private Boolean isNullFilterValue;
    
        public static Builder newBuilder() {
          return new AutoValue_PubsubToPubsub_ExtractAndFilterEventsFn.Builder();
        }
    
        @Nullable
        abstract ValueProvider<String> filterKey();
    
        @Nullable
        abstract ValueProvider<String> filterValue();
    
        @Setup
        public void setup() {
    
          if (this.doFilter != null) {
            return; // Filter has been evaluated already
          }
    
          inputFilterKey = (filterKey() == null ? null : filterKey().get());
    
          if (inputFilterKey == null) {
    
            // Disable input message filtering.
            this.doFilter = false;
    
          } else {
    
            this.doFilter = true; // Enable filtering.
    
            String inputFilterValue = (filterValue() == null ? null : filterValue().get());
    
            if (inputFilterValue == null) {
    
              LOG.warn(
                  "User provided a NULL for filterValue. Only messages with a value of NULL for the"
                      + " filterKey: {} will be filtered forward",
                  inputFilterKey);
    
              // For backward compatibility, we are allowing filtering by null filterValue.
              this.isNullFilterValue = true;
              this.inputFilterValueRegex = null;
            } else {
    
              this.isNullFilterValue = false;
              try {
                inputFilterValueRegex = getFilterPattern(inputFilterValue);
              } catch (PatternSyntaxException e) {
                LOG.error("Invalid regex pattern for supplied filterValue: {}", inputFilterValue);
                throw new RuntimeException(e);
              }
            }
    
            LOG.info(
                "Enabling event filter [key: " + inputFilterKey + "][value: " + inputFilterValue + "]");
          }
        }
    
        @ProcessElement
        public void processElement(ProcessContext context) {
    
          INPUT_COUNTER.inc();
          if (!this.doFilter) {
    
            // Filter is not enabled
            writeOutput(context, context.element());
          } else {
    
            PubsubMessage message = context.element();
            String extractedValue = message.getAttribute(this.inputFilterKey);
    
            if (this.isNullFilterValue) {
    
              if (extractedValue == null) {
                // If we are filtering for null and the extracted value is null, we forward
                // the message.
                writeOutput(context, message);
              }
    
            } else {
    
              if (extractedValue != null
                  && this.inputFilterValueRegex.matcher(extractedValue).matches()) {
                // If the extracted value is not null and it matches the filter,
                // we forward the message.
                writeOutput(context, message);
              }
            }
          }
        }
    
        /**
         * Write a {@link PubsubMessage} and increment the output counter.
         *
         * @param context {@link ProcessContext} to write {@link PubsubMessage} to.
         * @param message {@link PubsubMessage} output.
         */
        private void writeOutput(ProcessContext context, PubsubMessage message) {
          OUTPUT_COUNTER.inc();
          context.output(message);
        }
    
        /**
         * Return a {@link Pattern} based on a user provided regex string.
         *
         * @param regex Regex string to compile.
         * @return {@link Pattern}
         * @throws PatternSyntaxException If the string is an invalid regex.
         */
        private Pattern getFilterPattern(String regex) throws PatternSyntaxException {
          checkNotNull(regex, "Filter regex cannot be null.");
          return Pattern.compile(regex);
        }
    
        /** Builder class for {@link ExtractAndFilterEventsFn}. */
        @AutoValue.Builder
        abstract static class Builder {
    
          abstract Builder setFilterKey(ValueProvider<String> filterKey);
    
          abstract Builder setFilterValue(ValueProvider<String> filterValue);
    
          abstract ExtractAndFilterEventsFn build();
    
          /**
           * Method to set the filterKey used for filtering messages.
           *
           * @param filterKey Lookup key for the {@link PubsubMessage} attribute map.
           * @return {@link Builder}
           */
          public Builder withFilterKey(ValueProvider<String> filterKey) {
            checkArgument(filterKey != null, "withFilterKey(filterKey) called with null input.");
            return setFilterKey(filterKey);
          }
    
          /**
           * Method to set the filterValue used for filtering messages.
           *
           * @param filterValue Lookup value for the {@link PubsubMessage} attribute map.
           * @return {@link Builder}
           */
          public Builder withFilterValue(ValueProvider<String> filterValue) {
            checkArgument(filterValue != null, "withFilterValue(filterValue) called with null input.");
            return setFilterValue(filterValue);
          }
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
