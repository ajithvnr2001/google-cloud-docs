---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-jdbc/
title: Pub/Sub to Java Database Connectivity (JDBC) template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:18.448322+00:00
---

# Pub/Sub to Java Database Connectivity (JDBC) template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-jdbc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Pub/Sub to Java Database Connectivity (JDBC) template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Pub/Sub to Java Database Connectivity (JDBC) template is a streaming pipeline that ingests data from a pre-existing Pub/Sub subscription as JSON strings, and writes the resulting records to JDBC.

## Pipeline requirements

  * The Pub/Sub subscription must exist prior to running the pipeline. 
  * The JDBC source must exist prior to running the pipeline. 
  * The Pub/Sub output dead-letter topic must exist prior to running the pipeline.



## Template parameters

Parameter | Description  
---|---  
`driverClassName` | The JDBC driver class name. For example, `com.mysql.jdbc.Driver`.  
`connectionUrl` | The JDBC connection URL string. For example, `jdbc:mysql://some-host:3306/sampledb`. You can pass in this value as a string that's encrypted with a Cloud KMS key and then Base64-encoded. Remove whitespace characters from the Base64-encoded string.  
`driverJars` | Comma separated Cloud Storage paths for JDBC drivers. For example, `gs://your-bucket/driver_jar1.jar,gs://your-bucket/driver_jar2.jar`.   
`username` | Optional: The username to be used for the JDBC connection. You can pass in this value encrypted by a Cloud KMS key as a Base64-encoded string.  
`password` | Optional: The password to be used for the JDBC connection. You can pass in this value encrypted by a Cloud KMS key as a Base64-encoded string.  
`connectionProperties` | Optional: Properties string to use for the JDBC connection. Format of the string must be `[propertyName=property;]*`. For example, `unicode=true;characterEncoding=UTF-8`.  
`statement` | Statement to run against the database. The statement must specify the column names of the table in any order. Only the values of the specified column names are read from the JSON and added to the statement. For example, `INSERT INTO tableName (column1, column2) VALUES (?,?)`  
`inputSubscription` | The Pub/Sub input subscription to read from, in the format of `projects/<project>/subscriptions/<subscription>`.  
`outputDeadletterTopic` | The Pub/Sub topic to forward undeliverable messages. For example, `projects/<project-id>/topics/<topic-name>`.  
`KMSEncryptionKey` | Optional: Cloud KMS Encryption Key to decrypt the username, password, and connection string. If Cloud KMS key is passed in, the username, password, and connection string must all be passed in encrypted.  
`extraFilesToStage` | Comma separated Cloud Storage paths or Secret Manager secrets for files to stage in the worker. These files will be saved under the `/extra_files` directory in each worker. For example, `gs://<my-bucket>/file.txt,projects/<project-id>/secrets/<secret-id>/versions/<version-id>`.  
  
## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Pub/Sub to JDBC** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location gs://dataflow-templates/VERSION/flex/Pubsub_to_Jdbc \
        --region REGION_NAME \
        --parameters \
    driverClassName=DRIVER_CLASS_NAME,\
    connectionUrl=JDBC_CONNECTION_URL,\
    driverJars=DRIVER_PATHS,\
    username=CONNECTION_USERNAME,\
    password=CONNECTION_PASSWORD,\
    connectionProperties=CONNECTION_PROPERTIES,\
    statement=SQL_STATEMENT,\
    inputSubscription=INPUT_SUBSCRIPTION,\
    outputDeadletterTopic=OUTPUT_DEADLETTER_TOPIC,\
    KMSEncryptionKey=KMS_ENCRYPTION_KEY

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `DRIVER_CLASS_NAME`: the driver class name
  * `JDBC_CONNECTION_URL`: the JDBC connection URL
  * `DRIVER_PATHS`: the comma-separated Cloud Storage path(s) of the JDBC driver(s)
  * `CONNECTION_USERNAME`: the JDBC connection username
  * `CONNECTION_PASSWORD`: the JDBC connection password
  * `CONNECTION_PROPERTIES`: the JDBC connection properties, if necessary
  * `SQL_STATEMENT`: the SQL statement to be executed against the database
  * `INPUT_SUBSCRIPTION`: the Pub/Sub input subscription to read from
  * `OUTPUT_DEADLETTER_TOPIC`: the Pub/Sub to forward undeliverable messages
  * `KMS_ENCRYPTION_KEY`: the Cloud KMS Encryption Key



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "driverClassName": "DRIVER_CLASS_NAME",
           "connectionUrl": "JDBC_CONNECTION_URL",
           "driverJars": "DRIVER_PATHS",
           "username": "CONNECTION_USERNAME",
           "password": "CONNECTION_PASSWORD",
           "connectionProperties": "CONNECTION_PROPERTIES",
           "statement": "SQL_STATEMENT",
           "inputSubscription": "INPUT_SUBSCRIPTION",
           "outputDeadletterTopic": "OUTPUT_DEADLETTER_TOPIC",
           "KMSEncryptionKey":"KMS_ENCRYPTION_KEY"
       },
       "environment": { "zone": "us-central1-f" },
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
  * `DRIVER_CLASS_NAME`: the driver class name
  * `JDBC_CONNECTION_URL`: the JDBC connection URL
  * `DRIVER_PATHS`: the comma-separated Cloud Storage path(s) of the JDBC driver(s)
  * `CONNECTION_USERNAME`: the JDBC connection username
  * `CONNECTION_PASSWORD`: the JDBC connection password
  * `CONNECTION_PROPERTIES`: the JDBC connection properties, if necessary
  * `SQL_STATEMENT`: the SQL statement to be executed against the database
  * `INPUT_SUBSCRIPTION`: the Pub/Sub input subscription to read from
  * `OUTPUT_DEADLETTER_TOPIC`: the Pub/Sub to forward undeliverable messages
  * `KMS_ENCRYPTION_KEY`: the Cloud KMS Encryption Key



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2021 Google LLC
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
    
    import static com.google.cloud.teleport.v2.utils.KMSUtils.maybeDecrypt;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.io.DynamicJdbcIO;
    import com.google.cloud.teleport.v2.options.PubsubToJdbcOptions;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters;
    import com.google.cloud.teleport.v2.utils.JsonStringToQueryMapper;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.base.Splitter;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.jdbc.JdbcIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    import org.apache.beam.sdk.values.PCollection;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link PubsubToJdbc} streaming pipeline reads data from Google Cloud PubSub and publishes to
     * JDBC.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-googlecloud/README_Pubsub_to_Jdbc.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Pubsub_to_Jdbc",
        category = TemplateCategory.STREAMING,
        displayName = "Pub/Sub to JDBC",
        description =
            "The Pub/Sub to Java Database Connectivity (JDBC) template is a streaming pipeline that ingests data from a "
                + "pre-existing Cloud Pub/Sub subscription as JSON strings, and writes the resulting records to JDBC.",
        optionsClass = PubsubToJdbcOptions.class,
        flexContainerName = "jdbc-and-googlecloud",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-jdbc",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The Cloud Pub/Sub subscription must exist prior to running the pipeline.",
          "The JDBC source must exist prior to running the pipeline.",
          "The Cloud Pub/Sub output deadletter topic must exist prior to running the pipeline.",
        },
        streaming = true,
        supportsAtLeastOnce = true)
    public class PubsubToJdbc {
    
      /* Logger for class.*/
      private static final Logger LOG = LoggerFactory.getLogger(PubsubToJdbc.class);
    
      /** String/String Coder for FailsafeElement. */
      public static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        PubsubToJdbcOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubsubToJdbcOptions.class);
    
        run(options);
      }
    
      /**
       * Runs a pipeline which reads message from Pub/Sub and writes to JDBC.
       *
       * @param options The execution options.
       * @return The pipeline result.
       */
      public static PipelineResult run(PubsubToJdbcOptions options) {
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        LOG.info("Starting Pubsub-to-Jdbc Pipeline.");
    
        /*
         * Steps:
         *  1) Read data from a Pub/Sub subscription
         *  2) Write to Jdbc Table
         *  3) Write errors to deadletter topic
         */
        PCollection<String> pubsubData =
            pipeline.apply(
                "readFromPubSubSubscription",
                PubsubIO.readStrings().fromSubscription(options.getInputSubscription()));
    
        JdbcIO.DataSourceConfiguration dataSourceConfiguration =
            JdbcIO.DataSourceConfiguration.create(
                    ValueProvider.StaticValueProvider.of(options.getDriverClassName()),
                    maybeDecrypt(options.getConnectionUrl(), options.getKMSEncryptionKey()))
                .withDriverJars(options.getDriverJars());
        if (options.getUsername() != null) {
          dataSourceConfiguration =
              dataSourceConfiguration.withUsername(
                  maybeDecrypt(options.getUsername(), options.getKMSEncryptionKey()).get());
        }
        if (options.getPassword() != null) {
          dataSourceConfiguration =
              dataSourceConfiguration.withPassword(
                  maybeDecrypt(options.getPassword(), options.getKMSEncryptionKey()).get());
        }
        if (options.getConnectionProperties() != null) {
          dataSourceConfiguration =
              dataSourceConfiguration.withConnectionProperties(options.getConnectionProperties());
        }
    
        PCollection<FailsafeElement<String, String>> errors =
            pubsubData
                .apply(
                    "writeToJdbc",
                    DynamicJdbcIO.<String>write()
                        .withDataSourceConfiguration(dataSourceConfiguration)
                        .withStatement(options.getStatement())
                        .withPreparedStatementSetter(
                            new JsonStringToQueryMapper(getKeyOrder(options.getStatement()))))
                .setCoder(FAILSAFE_ELEMENT_CODER);
    
        errors.apply(
            "WriteFailedRecords",
            ErrorConverters.WriteStringMessageErrorsToPubSub.newBuilder()
                .setErrorRecordsTopic(options.getOutputDeadletterTopic())
                .build());
    
        return pipeline.run();
      }
    
      private static List<String> getKeyOrder(String statement) {
        int startIndex = statement.indexOf("(");
        int endIndex = statement.indexOf(")");
        String data = statement.substring(startIndex + 1, endIndex);
        return Splitter.on(',').trimResults().splitToList(data);
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
