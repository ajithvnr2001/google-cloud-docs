---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/jms-to-pubsub/
title: JMS to Pub/Sub template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:16.228775+00:00
---

# JMS to Pub/Sub template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/jms-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  JMS to Pub/Sub template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The JMS to Pub/Sub template is a streaming pipeline that reads messages from Active MQ JMS Server (Queue/Topic) and writes them to Pub/Sub. 

## Pipeline Requirements

  * The Pub/Sub output topic name must exist.
  * The JMS host IP must exist and have the proper network configuration for Dataflow worker VMs to reach the JMS host.
  * The JMS topic/queue that data is extracted from must have a name.



## Template parameters

### Required parameters

  * **inputName** : The name of the JMS topic or queue that data is read from. For example, `queue`.
  * **inputType** : The JMS destination type to read data from. Can be a queue or a topic. For example, `queue`.
  * **outputTopic** : The name of the Pub/Sub topic to publish data to. For example, `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.
  * **username** : The username to use for authentication on the JMS server. For example, `sampleusername`.
  * **password** : The password associated with the provided username. For example, `samplepassword`.



### Optional parameters

  * **jmsServer** : The JMS (ActiveMQ) Server IP. For example, `tcp://10.0.0.1:61616`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select JMS to Pub/Sub template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=YOUR_PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/JMS_to_Cloud_PubSub \
        --parameters \
    jmsServer=JMS_SERVER,\
    inputName=INPUT_NAME,\
    inputType=INPUT_TYPE,\
    outputTopic=OUTPUT_TOPIC,\
    username=USERNAME,\
    password=PASSWORD
      

You must replace the following values in this example:

  * Replace YOUR_PROJECT_ID with your project ID.
  * Replace  with Dataflow region name. For example: `us-central1`.
  * Replace JOB_NAME with a job name of your choice. The job name must match the regular expression `[a-z]([-a-z0-9]{0,38}[a-z0-9])?` to be valid.
  * Replace JMS_SERVER with the JMS server addresses. For example: `tcp://10.0.0.0:61616`
  * Replace INPUT_NAME with the name of the JMS server input topic/queue. For example: `testtopic`.
  * Replace INPUT_TYPE with the JMS server Destination Type(queue/topic). For example: `topic`
  * Replace OUTPUT_TOPIC with the name of Pub/Sub output topic. For example: `projects/myproject/topics/testoutput`.
  * Replace USERNAME with the username for the JMS server. For example: `testuser`.
  * Replace PASSWORD with the password that corresponds to the username used with the JMS server.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "jmsServer": "JMS_SERVER",
              "inputName": "INPUT_NAME",
              "inputType": "INPUT_TYPE",
              "outputTopic": "OUTPUT_TOPIC",
              "username": "USERNAME",
              "password": "PASSWORD"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/JMS_to_Cloud_PubSub",
       }
    }
      

You must replace the following values in this example:

  * Replace YOUR_PROJECT_ID with your project ID.
  * Replace  with Dataflow region name. For example: `us-central1`.
  * Replace JOB_NAME with a job name of your choice. The job name must match the regular expression `[a-z]([-a-z0-9]{0,38}[a-z0-9])?` to be valid.
  * Replace JMS_SERVER with the JMS server addresses. For example: `tcp://10.0.0.0:61616`
  * Replace INPUT_NAME with the name of the JMS server input topic/queue. For example: `testtopic`.
  * Replace INPUT_TYPE with the JMS server Destination Type(queue/topic). For example: `topic`
  * Replace OUTPUT_TOPIC with the name of Pub/Sub output topic. For example: `projects/myproject/topics/testoutput`.
  * Replace USERNAME with the username for the JMS server. For example: `testuser`.
  * Replace PASSWORD with the password that corresponds to the username used with the JMS server.



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2023 Google LLC
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
    package com.google.cloud.teleport.v2.templates;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import javax.jms.ConnectionFactory;
    import org.apache.activemq.ActiveMQConnectionFactory;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.jms.JmsIO;
    import org.apache.beam.sdk.io.jms.JmsRecord;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.SimpleFunction;
    import org.apache.beam.sdk.values.PCollection;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * Dataflow template which reads data from Jms Queue/Topic and writes it to Cloud PubSub.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/jms-to-pubsub/README_Jms_to_PubSub.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Jms_to_PubSub",
        category = TemplateCategory.STREAMING,
        displayName = "JMS to Pubsub",
        description =
            "The JMS to Pub/Sub template is a streaming pipeline that reads messages from ActiveMQ JMS Server (Queue/Topic) and writes them to Pub/Sub.",
        optionsClass = com.google.cloud.teleport.v2.templates.JmsToPubsub.JmsToPubsubOptions.class,
        flexContainerName = "googlecloud-and-jms",
        contactInformation = "https://cloud.google.com/support",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/jms-to-pubsub",
        preview = true,
        requirements = {
          "The Pub/Sub output topic name must exist.",
          "The JMS host IP must exist and have the proper network configuration for Dataflow worker VMs to reach the JMS host.",
          "The JMS topic/queue that data is extracted from must have a name."
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public class JmsToPubsub {
    
      /**
       * Runs a pipeline which reads data from JMS queue/topic and writes it to Cloud PubSub.
       *
       * @param args arguments to the pipeline
       */
      private static final Logger LOG = LoggerFactory.getLogger(JmsToPubsub.class);
    
      public static void main(String[] args) {
        JmsToPubsubOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(JmsToPubsubOptions.class);
        run(options);
      }
    
      public static void validate(JmsToPubsubOptions options) {
        if (options != null) {
          if ((options.getUsername() != null
                  && (!options.getUsername().isEmpty() || !options.getUsername().isBlank()))
              && (options.getPassword() == null
                  || options.getPassword().isBlank()
                  || options.getPassword().isEmpty())) {
            throw new IllegalArgumentException(
                "While username is provided, password is required for authentication");
          }
        }
      }
    
      public static PipelineResult run(JmsToPubsubOptions options) {
        validate(options);
        Pipeline pipeline = Pipeline.create(options);
        String connectionURI = options.getJmsServer();
        ConnectionFactory myConnectionFactory;
        PCollection<JmsRecord> input;
    
        if (!options.getUsername().isEmpty() || !options.getUsername().isBlank()) {
          myConnectionFactory =
              new ActiveMQConnectionFactory(
                  options.getUsername(), options.getPassword(), connectionURI);
        } else {
          myConnectionFactory = new ActiveMQConnectionFactory(connectionURI);
        }
        LOG.info("Given Input Type " + options.getInputType());
        if (options.getInputType().equalsIgnoreCase("queue")) {
          input =
              pipeline.apply(
                  "Read From JMS Queue",
                  JmsIO.read()
                      .withConnectionFactory(myConnectionFactory)
                      .withQueue(options.getInputName()));
        } else {
          input =
              pipeline.apply(
                  "Read From JMS Topic",
                  JmsIO.read()
                      .withConnectionFactory(myConnectionFactory)
                      .withTopic(options.getInputName()));
        }
    
        input
            .apply(
                MapElements.via(
                    new SimpleFunction<JmsRecord, String>() {
                      public String apply(JmsRecord input) {
                        return input.getPayload();
                      }
                    }))
            .apply("WriteToPubSubTopic", PubsubIO.writeStrings().to(options.getOutputTopic()));
        return pipeline.run();
      }
    
      /**
       * The {@link JmsToPubsubOptions} interface provides the custom execution options passed by the
       * executor at the command-line.
       */
      public interface JmsToPubsubOptions extends PipelineOptions {
        @TemplateParameter.Text(
            order = 1,
            groupName = "Source",
            optional = true,
            regexes = {"[,\\/:a-zA-Z0-9._-]+"},
            description = "JMS Host IP",
            helpText = "The JMS (ActiveMQ) Server IP.",
            example = "tcp://10.0.0.1:61616")
        @Validation.Required
        String getJmsServer();
    
        void setJmsServer(String jmsServer);
    
        @TemplateParameter.Text(
            order = 2,
            groupName = "Source",
            optional = false,
            regexes = {"[a-zA-Z0-9._-]+"},
            description = "JMS Queue/Topic Name to read the input from",
            helpText = "The name of the JMS topic or queue that data is read from.",
            example = "queue")
        @Validation.Required
        String getInputName();
    
        void setInputName(String inputName);
    
        @TemplateParameter.Text(
            order = 3,
            optional = false,
            regexes = {"[a-zA-Z0-9._-]+"},
            description = "JMS Destination Type to read the input from",
            helpText = "The JMS destination type to read data from. Can be a queue or a topic.",
            example = "queue")
        @Validation.Required
        String getInputType();
    
        void setInputType(String inputType);
    
        @TemplateParameter.PubsubTopic(
            order = 4,
            groupName = "Target",
            description = "Output Pub/Sub topic",
            helpText = "The name of the Pub/Sub topic to publish data to.",
            example = "projects/<PROJECT_ID>/topics/<TOPIC_NAME>")
        @Validation.Required
        String getOutputTopic();
    
        void setOutputTopic(String outputTopic);
    
        @TemplateParameter.Text(
            order = 5,
            description = "JMS Username",
            helpText = "The username to use for authentication on the JMS server.",
            example = "sampleusername")
        String getUsername();
    
        void setUsername(String username);
    
        @TemplateParameter.Password(
            order = 6,
            description = "JMS Password",
            helpText = "The password associated with the provided username.",
            example = "samplepassword")
        String getPassword();
    
        void setPassword(String password);
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
