---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-elasticsearch/
title: BigQuery to Elasticsearch template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:06.986675+00:00
---

# BigQuery to Elasticsearch template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-elasticsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  BigQuery to Elasticsearch template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The BigQuery to Elasticsearch template is a batch pipeline that ingests data from a BigQuery table into Elasticsearch as documents. The template can either read the entire table or read specific records using a supplied query. 

## Pipeline requirements

  * The source BigQuery table must exist.
  * A Elasticsearch host on a Google Cloud instance or on Elastic Cloud with Elasticsearch version 7.0 or later. Must be accessible from the Dataflow worker machines.



## Template parameters

### Required parameters

  * **connectionUrl** : The Elasticsearch URL in the format `https://hostname:[port]`. If using Elastic Cloud, specify the CloudID. For example, `https://elasticsearch-host:9200`.
  * **apiKey** : The Base64-encoded API key to use for authentication.
  * **index** : The Elasticsearch index that the requests are issued to. For example, `my-index`.



### Optional parameters

  * **inputTableSpec** : The BigQuery table to read from. If you specify `inputTableSpec`, the template reads the data directly from BigQuery storage by using the BigQuery Storage Read API (<https://cloud.google.com/bigquery/docs/reference/storage>). For information about limitations in the Storage Read API, see <https://cloud.google.com/bigquery/docs/reference/storage#limitations>. You must specify either `inputTableSpec` or `query`. If you set both parameters, the template uses the `query` parameter. For example, `<BIGQUERY_PROJECT>:<DATASET_NAME>.<INPUT_TABLE>`.
  * **outputDeadletterTable** : The BigQuery table for messages that failed to reach the output table. If a table doesn't exist, it is created during pipeline execution. If not specified, `<outputTableSpec>_error_records` is used. For example, `<PROJECT_ID>:<DATASET_NAME>.<DEADLETTER_TABLE>`.
  * **query** : The SQL query to use to read data from BigQuery. If the BigQuery dataset is in a different project than the Dataflow job, specify the full dataset name in the SQL query, for example: <PROJECT_ID>.<DATASET_NAME>.<TABLE_NAME>. By default, the `query` parameter uses GoogleSQL (<https://cloud.google.com/bigquery/docs/introduction-sql>), unless `useLegacySql` is `true`. You must specify either `inputTableSpec` or `query`. If you set both parameters, the template uses the `query` parameter. For example, `select * from sampledb.sample_table`.
  * **useLegacySql** : Set to `true` to use legacy SQL. This parameter only applies when using the `query` parameter. Defaults to `false`.
  * **queryLocation** : Needed when reading from an authorized view without underlying table's permission. For example, `US`.
  * **queryTempDataset** : With this option, you can set an existing dataset to create the temporary table to store the results of the query. For example, `temp_dataset`.
  * **KMSEncryptionKey** : If reading from BigQuery using query source, use this Cloud KMS key to encrypt any temporary tables created. For example, `projects/your-project/locations/global/keyRings/your-keyring/cryptoKeys/your-key`.
  * **elasticsearchUsername** : The Elasticsearch username to authenticate with. If specified, the value of `apiKey` is ignored.
  * **elasticsearchPassword** : The Elasticsearch password to authenticate with. If specified, the value of `apiKey` is ignored.
  * **batchSize** : The batch size in number of documents. Defaults to `1000`.
  * **batchSizeBytes** : The batch size in number of bytes. Defaults to `5242880` (5mb).
  * **maxRetryAttempts** : The maximum number of retry attempts. Must be greater than zero. Defaults to `5`.
  * **maxRetryDuration** : The maximum retry duration in milliseconds. Must be greater than zero. Defaults to `60000` (1 minute).
  * **propertyAsIndex** : The property in the document being indexed whose value specifies `_index` metadata to include with the document in bulk requests. Takes precedence over an `_index` UDF. Defaults to `none`.
  * **javaScriptIndexFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for a function that specifies `_index` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptIndexFnName** : The name of the UDF JavaScript function that specifies `_index` metadata to include with the document in bulk requests. Defaults to `none`.
  * **propertyAsId** : A property in the document being indexed whose value specifies `_id` metadata to include with the document in bulk requests. Takes precedence over an `_id` UDF. Defaults to `none`.
  * **javaScriptIdFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for the function that specifies `_id` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptIdFnName** : The name of the UDF JavaScript function that specifies the `_id` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptTypeFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for a function that specifies `_type` metadata to include with documents in bulk requests. Defaults to `none`.
  * **javaScriptTypeFnName** : The name of the UDF JavaScript function that specifies the `_type` metadata to include with the document in bulk requests. Defaults to `none`.
  * **javaScriptIsDeleteFnGcsPath** : The Cloud Storage path to the JavaScript UDF source for the function that determines whether to delete the document instead of inserting or updating it. The function returns a string value of `true` or `false`. Defaults to `none`.
  * **javaScriptIsDeleteFnName** : The name of the UDF JavaScript function that determines whether to delete the document instead of inserting or updating it. The function returns a string value of `true` or `false`. Defaults to `none`.
  * **usePartialUpdate** : Whether to use partial updates (update rather than create or index, allowing partial documents) with Elasticsearch requests. Defaults to `false`.
  * **bulkInsertMethod** : Whether to use `INDEX` (index, allows upserts) or `CREATE` (create, errors on duplicate _id) with Elasticsearch bulk requests. Defaults to `CREATE`.
  * **trustSelfSignedCerts** : Whether to trust self-signed certificate or not. An Elasticsearch instance installed might have a self-signed certificate, Enable this to true to by-pass the validation on SSL certificate. (Defaults to: `false`).
  * **disableCertificateValidation** : If `true`, trust the self-signed SSL certificate. An Elasticsearch instance might have a self-signed certificate. To bypass validation for the certificate, set this parameter to `true`. Defaults to `false`.
  * **apiKeyKMSEncryptionKey** : The Cloud KMS key to decrypt the API key. This parameter is required if the `apiKeySource` is set to `KMS`. If this parameter is provided, pass in an encrypted `apiKey` string. Encrypt parameters using the KMS API encrypt endpoint. For the key, use the format `projects/<PROJECT_ID>/locations/<KEY_REGION>/keyRings/<KEY_RING>/cryptoKeys/<KMS_KEY_NAME>`. See: <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt> For example, `projects/your-project-id/locations/global/keyRings/your-keyring/cryptoKeys/your-key-name`.
  * **apiKeySecretId** : The Secret Manager secret ID for the apiKey. If the `apiKeySource` is set to `SECRET_MANAGER`, provide this parameter. Use the format `projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<SECRET_VERSION>. For example, `projects/your-project-id/secrets/your-secret/versions/your-secret-version`.
  * **apiKeySource** : The source of the API key. Allowed values are `PLAINTEXT`, `KMS` orand `SECRET_MANAGER`. This parameter is required when you use Secret Manager or KMS. If `apiKeySource` is set to `KMS`, `apiKeyKMSEncryptionKey` and encrypted apiKey must be provided. If `apiKeySource` is set to `SECRET_MANAGER`, `apiKeySecretId` must be provided. If `apiKeySource` is set to `PLAINTEXT`, `apiKey` must be provided. Defaults to: PLAINTEXT.
  * **socketTimeout** : If set, overwrites the default max retry timeout and default socket timeout (30000ms) in the Elastic RestClient.
  * **javascriptTextTransformGcsPath** : The Cloud Storage URI of the .js file that defines the JavaScript user-defined function (UDF) to use. For example, `gs://my-bucket/my-udfs/my_file.js`.
  * **javascriptTextTransformFunctionName** : The name of the JavaScript user-defined function (UDF) to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see UDF Examples (<https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples>).



## User-defined functions

This template supports user-defined functions (UDFs) at several points in the pipeline, described below. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Index function

Returns the index to which the document belongs.

Template parameters:

  * `javaScriptIndexFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptIndexFnName`: the name of the JavaScript function. 



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : the value of the document's `_index` metadata field.



### Document ID function

Returns the document ID.

Template parameters:

  * `javaScriptIdFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptIdFnName`: the name of the JavaScript function.



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : the value of the document's `_id` metadata field.



### Document deletion function

Specifies whether to delete a document. To use this function, set the bulk insert mode to `INDEX` and provide a document ID function.

Template parameters:

  * `javaScriptIsDeleteFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptIsDeleteFnName`: the name of the JavaScript function.



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : return the string `"true"` to delete the document, or `"false"` to upsert the document.



### Mapping type function

Returns the document's mapping type.

**Caution:** Mapping types were removed in Elasticsearch 8.0. 

Template parameters:

  * `javaScriptTypeFnGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javaScriptTypeFnName`: the name of the JavaScript function. 



Function specification:

  * **Input** : the Elasticsearch document, serialized as a JSON string.
  * **Output** : the value of the document's `_type` metadata field.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **BigQuery to Elasticsearch** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/BigQuery_to_Elasticsearch \
        --parameters \
    inputTableSpec=INPUT_TABLE_SPEC,\
    connectionUrl=CONNECTION_URL,\
    apiKey=APIKEY,\
    index=INDEX

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `INPUT_TABLE_SPEC`: your BigQuery table name.
  * `CONNECTION_URL`: your Elasticsearch URL.
  * `APIKEY`: your base64 encoded API key for authentication.
  * `INDEX`: your Elasticsearch index.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "inputTableSpec": "INPUT_TABLE_SPEC",
              "connectionUrl": "CONNECTION_URL",
              "apiKey": "APIKEY",
              "index": "INDEX"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/BigQuery_to_Elasticsearch",
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
  * `INPUT_TABLE_SPEC`: your BigQuery table name.
  * `CONNECTION_URL`: your Elasticsearch URL.
  * `APIKEY`: your base64 encoded API key for authentication.
  * `INDEX`: your Elasticsearch index.



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
    package com.google.cloud.teleport.v2.elasticsearch.templates;
    
    import com.google.cloud.teleport.metadata.MultiTemplate;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.elasticsearch.options.BigQueryToElasticsearchOptions;
    import com.google.cloud.teleport.v2.elasticsearch.transforms.WriteToElasticsearch;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters.ReadBigQueryTableRows;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters.TableRowToJsonFn;
    import com.google.cloud.teleport.v2.transforms.JavascriptTextTransformer.TransformTextViaJavascript;
    import com.google.cloud.teleport.v2.transforms.PythonExternalTextTransformer;
    import com.google.common.base.Strings;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollection;
    
    /**
     * The {@link BigQueryToElasticsearch} pipeline exports data from a BigQuery table to Elasticsearch.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-elasticsearch/README_BigQuery_to_Elasticsearch.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @MultiTemplate({
      @Template(
          name = "BigQuery_to_Elasticsearch",
          category = TemplateCategory.BATCH,
          displayName = "BigQuery to Elasticsearch",
          description =
              "The BigQuery to Elasticsearch template is a batch pipeline that ingests data from a BigQuery table into Elasticsearch as documents. "
                  + "The template can either read the entire table or read specific records using a supplied query.",
          optionsClass = BigQueryToElasticsearchOptions.class,
          skipOptions = {
            "javascriptTextTransformReloadIntervalMinutes",
            "pythonExternalTextTransformGcsPath",
            "pythonExternalTextTransformFunctionName"
          },
          flexContainerName = "googlecloud-to-elasticsearch",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-elasticsearch",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The source BigQuery table must exist.",
            "A Elasticsearch host on a Google Cloud instance or on Elastic Cloud with Elasticsearch version 7.0 or above and should be accessible from the Dataflow worker machines.",
          }),
      @Template(
          name = "BigQuery_to_Elasticsearch_Xlang",
          category = TemplateCategory.BATCH,
          displayName = "BigQuery to Elasticsearch with Python UDFs",
          type = Template.TemplateType.XLANG,
          description =
              "The BigQuery to Elasticsearch template is a batch pipeline that ingests data from a BigQuery table into Elasticsearch as documents. "
                  + "The template can either read the entire table or read specific records using a supplied query.",
          optionsClass = BigQueryToElasticsearchOptions.class,
          skipOptions = {
            "javascriptTextTransformReloadIntervalMinutes",
            "javascriptTextTransformGcsPath",
            "javascriptTextTransformFunctionName"
          },
          flexContainerName = "googlecloud-to-elasticsearch-xlang",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-elasticsearch",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The source BigQuery table must exist.",
            "A Elasticsearch host on a Google Cloud instance or on Elastic Cloud with Elasticsearch version 7.0 or above and should be accessible from the Dataflow worker machines.",
          })
    })
    public class BigQueryToElasticsearch {
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        BigQueryToElasticsearchOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(BigQueryToElasticsearchOptions.class);
    
        run(options);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      private static PipelineResult run(BigQueryToElasticsearchOptions options) {
    
        // Create the pipeline.
        Pipeline pipeline = Pipeline.create(options);
        /*
         * Steps: 1) Read records from BigQuery via BigQueryIO.
         *        2) Create json string from Table Row.
         *        3) Write records to Elasticsearch.
         */
    
        boolean useJavascriptUdf = !Strings.isNullOrEmpty(options.getJavascriptTextTransformGcsPath());
        boolean usePythonUdf = !Strings.isNullOrEmpty(options.getPythonExternalTextTransformGcsPath());
        if (useJavascriptUdf && usePythonUdf) {
          throw new IllegalArgumentException(
              "Either javascript or Python gcs path must be provided, but not both.");
        }
    
        /*
         * Step #1: Read from BigQuery. If a query is provided then it is used to get the TableRows.
         */
        PCollection<String> readJsonDocuments =
            pipeline
                .apply(
                    "ReadFromBigQuery",
                    ReadBigQueryTableRows.newBuilder()
                        .setOptions(options.as(BigQueryToElasticsearchOptions.class))
                        .build())
    
                /*
                 * Step #2: Convert table rows to JSON documents.
                 */
                .apply("TableRowsToJsonDocument", ParDo.of(new TableRowToJsonFn()));
    
        /*
         * Step #3: Apply UDF functions (if specified)
         */
        PCollection<String> udfOut;
        if (usePythonUdf) {
          udfOut =
              readJsonDocuments
                  .apply(
                      "MapToRecord",
                      PythonExternalTextTransformer.FailsafeRowPythonExternalUdf
                          .stringMappingFunction())
                  .setRowSchema(PythonExternalTextTransformer.FailsafeRowPythonExternalUdf.ROW_SCHEMA)
                  .apply(
                      "InvokeUDF",
                      PythonExternalTextTransformer.FailsafePythonExternalUdf.newBuilder()
                          .setFileSystemPath(options.getPythonExternalTextTransformGcsPath())
                          .setFunctionName(options.getPythonExternalTextTransformFunctionName())
                          .build())
                  .apply(
                      "MapToStringElements",
                      ParDo.of(new PythonExternalTextTransformer.RowToStringElementFn()));
        } else {
          udfOut =
              readJsonDocuments.apply(
                  TransformTextViaJavascript.newBuilder()
                      .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                      .setFunctionName(options.getJavascriptTextTransformFunctionName())
                      .build());
        }
    
        /*
         * Step #4: Write converted records to Elasticsearch
         */
        udfOut.apply(
            "WriteToElasticsearch",
            WriteToElasticsearch.newBuilder()
                .setUserAgent("dataflow-bigquery-to-elasticsearch-template/v2")
                .setOptions(options.as(BigQueryToElasticsearchOptions.class))
                .build());
    
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
