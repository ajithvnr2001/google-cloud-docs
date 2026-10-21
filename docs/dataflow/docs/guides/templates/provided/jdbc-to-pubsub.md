---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/jdbc-to-pubsub/
title: Java Database Connectivity (JDBC) to Pub/Sub template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:11.913414+00:00
---

# Java Database Connectivity (JDBC) to Pub/Sub template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/jdbc-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Java Database Connectivity (JDBC) to Pub/Sub template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Java Database Connectivity (JDBC) to Pub/Sub template is a batch pipeline that ingests data from JDBC source and writes the resulting records to a pre-existing Pub/Sub topic as a JSON string. 

## Pipeline requirements

  * The JDBC source must exist prior to running the pipeline. 
  * The Pub/Sub output topic must exist prior to running the pipeline.



## Template parameters

### Required parameters

  * **driverClassName** : The JDBC driver class name. For example, `com.mysql.jdbc.Driver`.
  * **connectionUrl** : The JDBC connection URL string. You can pass in this value as a string that's encrypted with a Cloud KMS key and then Base64-encoded. For example: 'echo -n "jdbc:mysql://some-host:3306/sampledb" | gcloud kms encrypt --location=
  * **driverJars** : Comma-separated Cloud Storage paths for JDBC drivers. For example, `gs://your-bucket/driver_jar1.jar,gs://your-bucket/driver_jar2.jar`.
  * **query** : The query to run on the source to extract the data. For example, `select * from sampledb.sample_table`.
  * **outputTopic** : The Pub/Sub topic to publish to. For example, `projects/<PROJECT_ID>/topics/<TOPIC_NAME>`.



### Optional parameters

  * **username** : The username to use for the JDBC connection. You can pass in this value as a string that's encrypted with a Cloud KMS key and then Base64-encoded. For example, `echo -n 'some_username' | glcloud kms encrypt --location=my_location --keyring=mykeyring --key=mykey --plaintext-file=- --ciphertext-file=- | base64`.
  * **password** : The password to use for the JDBC connection. You can pass in this value as a string that's encrypted with a Cloud KMS key and then Base64-encoded. For example, `echo -n 'some_password' | glcloud kms encrypt --location=my_location --keyring=mykeyring --key=mykey --plaintext-file=- --ciphertext-file=- | base64`.
  * **connectionProperties** : The properties string to use for the JDBC connection. The format of the string must be `[propertyName=property;]*`. For example, `unicode=true;characterEncoding=UTF-8`.
  * **KMSEncryptionKey** : The Cloud KMS Encryption Key to use to decrypt the username, password, and connection string. If a Cloud KMS key is passed in, the username, password, and connection string must all be passed in encrypted and base64 encoded. For example, `projects/your-project/locations/global/keyRings/your-keyring/cryptoKeys/your-key`.
  * **disabledAlgorithms** : Comma separated algorithms to disable. If this value is set to `none`, no algorithm is disabled. Use this parameter with caution, because the algorithms disabled by default might have vulnerabilities or performance issues. For example, `SSLv3, RC4`.
  * **extraFilesToStage** : Comma separated Cloud Storage paths or Secret Manager secrets for files to stage in the worker. These files are saved in the /extra_files directory in each worker. For example, `gs://<BUCKET_NAME>/file.txt,projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<VERSION_ID>`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **JDBC to Pub/Sub** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/flex/Jdbc_to_PubSub \
        --region REGION_NAME \
        --parameters \
    driverClassName=DRIVER_CLASS_NAME,\
    connectionURL=JDBC_CONNECTION_URL,\
    driverJars=DRIVER_PATHS,\
    username=CONNECTION_USERNAME,\
    password=CONNECTION_PASSWORD,\
    connectionProperties=CONNECTION_PROPERTIES,\
    query=SOURCE_SQL_QUERY,\
    outputTopic=OUTPUT_TOPIC,\
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
  * `SOURCE_SQL_QUERY`: the SQL query to be run on the source database
  * `OUTPUT_TOPIC`: the Pub/Sub to publish to
  * `KMS_ENCRYPTION_KEY`: the Cloud KMS Encryption Key



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
      "launchParameter": {
        "jobName": "JOB_NAME",
        "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Jdbc_to_PubSub"
        "parameters": {
          "driverClassName": "DRIVER_CLASS_NAME",
          "connectionURL": "JDBC_CONNECTION_URL",
          "driverJars": "DRIVER_PATHS",
          "username": "CONNECTION_USERNAME",
          "password": "CONNECTION_PASSWORD",
          "connectionProperties": "CONNECTION_PROPERTIES",
          "query": "SOURCE_SQL_QUERY",
          "outputTopic": "OUTPUT_TOPIC",
          "KMSEncryptionKey":"KMS_ENCRYPTION_KEY"
        },
        "environment": { "zone": "us-central1-f" }
      }
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
  * `SOURCE_SQL_QUERY`: the SQL query to be run on the source database
  * `OUTPUT_TOPIC`: the Pub/Sub to publish to
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
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.options.JdbcToPubsubOptions;
    import java.sql.Clob;
    import java.sql.ResultSet;
    import java.sql.ResultSetMetaData;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.jdbc.JdbcIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider.StaticValueProvider;
    import org.apache.beam.sdk.values.PCollection;
    import org.json.JSONObject;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link JdbcToPubsub} batch pipeline reads data from JDBC and publishes to Google Cloud
     * PubSub.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/jdbc-and-googlecloud/README_Jdbc_to_PubSub.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Jdbc_to_PubSub",
        category = TemplateCategory.BATCH,
        displayName = "JDBC to Pub/Sub",
        description =
            "The Java Database Connectivity (JDBC) to Pub/Sub template is a batch pipeline that ingests data from "
                + "JDBC source and writes the resulting records to a pre-existing Pub/Sub topic as a JSON string.",
        optionsClass = JdbcToPubsubOptions.class,
        flexContainerName = "jdbc-and-googlecloud",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/jdbc-to-pubsub",
        contactInformation = "https://cloud.google.com/support",
        preview = true,
        requirements = {
          "The JDBC source must exist prior to running the pipeline.",
          "The Cloud Pub/Sub output topic must exist prior to running the pipeline."
        })
    public class JdbcToPubsub {
    
      /* Logger for class.*/
      private static final Logger LOG = LoggerFactory.getLogger(JdbcToPubsub.class);
    
      /**
       * {@link JdbcIO.RowMapper} implementation to convert Jdbc ResultSet rows to UTF-8 encoded JSONs.
       */
      public static class ResultSetToJSONString implements JdbcIO.RowMapper<String> {
    
        @Override
        public String mapRow(ResultSet resultSet) throws Exception {
          ResultSetMetaData metaData = resultSet.getMetaData();
          JSONObject json = new JSONObject();
    
          for (int i = 1; i <= metaData.getColumnCount(); i++) {
            Object value = resultSet.getObject(i);
    
            // JSONObject.put() does not support null values. The exception is JSONObject.NULL
            if (value == null) {
              json.put(metaData.getColumnLabel(i), JSONObject.NULL);
              continue;
            }
    
            switch (metaData.getColumnTypeName(i).toLowerCase()) {
              case "clob":
                Clob clobObject = resultSet.getClob(i);
                if (clobObject.length() > Integer.MAX_VALUE) {
                  LOG.warn(
                      "The Clob value size {} in column {} exceeds 2GB and will be truncated.",
                      clobObject.length(),
                      metaData.getColumnLabel(i));
                }
                json.put(
                    metaData.getColumnLabel(i), clobObject.getSubString(1, (int) clobObject.length()));
                break;
              default:
                json.put(metaData.getColumnLabel(i), value);
            }
          }
          return json.toString();
        }
      }
    
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        JdbcToPubsubOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(JdbcToPubsubOptions.class);
    
        run(options);
      }
    
      /**
       * Runs a pipeline which reads message from JDBC and writes to Pub/Sub.
       *
       * @param options The execution options.
       * @return The pipeline result.
       */
      public static PipelineResult run(JdbcToPubsubOptions options) {
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        LOG.info("Starting Jdbc-To-PubSub Pipeline.");
    
        /*
         * Steps:
         *  1) Read data from a Jdbc Table
         *  2) Write to Pub/Sub topic
         */
        JdbcIO.DataSourceConfiguration dataSourceConfiguration =
            JdbcIO.DataSourceConfiguration.create(
                    StaticValueProvider.of(options.getDriverClassName()),
                    maybeDecrypt(options.getConnectionUrl(), options.getKMSEncryptionKey()))
                .withDriverJars(options.getDriverJars());
        if (options.getUsername() != null) {
          dataSourceConfiguration =
              dataSourceConfiguration.withUsername(
                  maybeDecrypt(options.getUsername(), options.getKMSEncryptionKey()));
        }
        if (options.getPassword() != null) {
          dataSourceConfiguration =
              dataSourceConfiguration.withPassword(
                  maybeDecrypt(options.getPassword(), options.getKMSEncryptionKey()));
        }
        if (options.getConnectionProperties() != null) {
          dataSourceConfiguration =
              dataSourceConfiguration.withConnectionProperties(options.getConnectionProperties());
        }
    
        PCollection<String> jdbcData =
            pipeline.apply(
                "readFromJdbc",
                JdbcIO.<String>read()
                    .withDataSourceConfiguration(dataSourceConfiguration)
                    .withQuery(options.getQuery())
                    .withCoder(StringUtf8Coder.of())
                    .withRowMapper(new ResultSetToJSONString()));
    
        jdbcData.apply("writeSuccessMessages", PubsubIO.writeStrings().to(options.getOutputTopic()));
    
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
