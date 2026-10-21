---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-elasticsearch/
title: Cloud Storage to Elasticsearch template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:11.517979+00:00
---

# Cloud Storage to Elasticsearch template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-elasticsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage to Elasticsearch template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud Storage to Elasticsearch template is a batch pipeline that reads data from CSV files stored in a Cloud Storage bucket and writes the data into Elasticsearch as JSON documents. 

## Pipeline requirements

  * The Cloud Storage bucket must exist.
  * A Elasticsearch host on a Google Cloud instance or on Elasticsearch Cloud that is accessible from Dataflow must exist.
  * A BigQuery table for error output must exist.



### CSV schema

If the CSV files contain headers, set the `containsHeaders` template parameter to `true`.

Otherwise, create a JSON schema file that describes the data. Specify the Cloud Storage URI of the schema file in the `jsonSchemaPath` template parameter. The following example shows a JSON schema:

`[{"name":"id", "type":"text"}, {"name":"age", "type":"integer"}] `

Alternatively, you can provide a user-defined function (UDF) that parses the CSV text and outputs Elasticsearch documents.

## Template parameters

### Required parameters

  * **deadletterTable** : The BigQuery dead-letter table to send failed inserts to. For example, `your-project:your-dataset.your-table-name`.
  * **inputFileSpec** : The Cloud Storage file pattern to search for CSV files. For example, `gs://mybucket/test-*.csv`.
  * **connectionUrl** : The Elasticsearch URL in the format `https://hostname:[port]`. If using Elastic Cloud, specify the CloudID. For example, `https://elasticsearch-host:9200`.
  * **apiKey** : The Base64-encoded API key to use for authentication.
  * **index** : The Elasticsearch index that the requests are issued to. For example, `my-index`.



### Optional parameters

  * **inputFormat** : The input file format. Defaults to `CSV`.
  * **containsHeaders** : Input CSV files contain a header record (true/false). Only required if reading CSV files. Defaults to: false.
  * **delimiter** : The column delimiter of the input text files. Default: `,` For example, `,`.
  * **csvFormat** : CSV format specification to use for parsing records. Default is: `Default`. See <https://commons.apache.org/proper/commons-csv/apidocs/org/apache/commons/csv/CSVFormat.html> for more details. Must match format names exactly found at: <https://commons.apache.org/proper/commons-csv/apidocs/org/apache/commons/csv/CSVFormat.Predefined.html>.
  * **jsonSchemaPath** : The path to the JSON schema. Defaults to `null`. For example, `gs://path/to/schema`.
  * **largeNumFiles** : Set to true if number of files is in the tens of thousands. Defaults to `false`.
  * **csvFileEncoding** : The CSV file character encoding format. Allowed values are `US-ASCII`, `ISO-8859-1`, `UTF-8`, and `UTF-16`. Defaults to: UTF-8.
  * **logDetailedCsvConversionErrors** : Set to `true` to enable detailed error logging when CSV parsing fails. Note that this may expose sensitive data in the logs (e.g., if the CSV file contains passwords). Default: `false`.
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

### Text transform function

Transforms the CSV data into an Elasticsearch document.

Template parameters:

  * `javascriptTextTransformGcsPath`: the Cloud Storage URI of the JavaScript file.
  * `javascriptTextTransformFunctionName`: the name of the JavaScript function.



Function specification:

  * **Input** : a single line from an input CSV file.
  * **Output** : a stringified JSON document to insert into Elasticsearch.



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

  4. From the **Dataflow template** drop-down menu, select the **Cloud Storage to Elasticsearch** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID\
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/GCS_to_Elasticsearch \
        --parameters \
    inputFileSpec=INPUT_FILE_SPEC,\
    connectionUrl=CONNECTION_URL,\
    apiKey=APIKEY,\
    index=INDEX,\
    deadletterTable=DEADLETTER_TABLE,\

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `INPUT_FILE_SPEC`: your Cloud Storage file pattern.
  * `CONNECTION_URL`: your Elasticsearch URL.
  * `APIKEY`: your base64 encoded API key for authentication.
  * `INDEX`: your Elasticsearch index.
  * `DEADLETTER_TABLE`: your BigQuery table.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launch_parameter": {
          "jobName": "JOB_NAME",
          "parameters": {
              "inputFileSpec": "INPUT_FILE_SPEC",
              "connectionUrl": "CONNECTION_URL",
              "apiKey": "APIKEY",
              "index": "INDEX",
              "deadletterTable": "DEADLETTER_TABLE"
          },
          "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/GCS_to_Elasticsearch",
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
  * `INPUT_FILE_SPEC`: your Cloud Storage file pattern.
  * `CONNECTION_URL`: your Elasticsearch URL.
  * `APIKEY`: your base64 encoded API key for authentication.
  * `INDEX`: your Elasticsearch index.
  * `DEADLETTER_TABLE`: your BigQuery table.



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
    
    import static org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.base.Preconditions.checkArgument;
    
    import com.google.cloud.teleport.metadata.MultiTemplate;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.elasticsearch.options.GCSToElasticsearchOptions;
    import com.google.cloud.teleport.v2.elasticsearch.transforms.WriteToElasticsearch;
    import com.google.cloud.teleport.v2.transforms.CsvConverters;
    import com.google.cloud.teleport.v2.transforms.ErrorConverters.WriteStringMessageErrors;
    import com.google.cloud.teleport.v2.utils.SchemaUtils;
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.common.base.Strings;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.CoderRegistry;
    import org.apache.beam.sdk.coders.NullableCoder;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.WithTimestamps;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.joda.time.Instant;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * The {@link GCSToElasticsearch} pipeline exports data from one or more CSV files in Cloud Storage
     * to Elasticsearch.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-elasticsearch/README_GCS_to_Elasticsearch.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @MultiTemplate({
      @Template(
          name = "GCS_to_Elasticsearch",
          category = TemplateCategory.BATCH,
          displayName = "Cloud Storage to Elasticsearch",
          description = {
            "The Cloud Storage to Elasticsearch template is a batch pipeline that reads data from CSV files stored in a Cloud Storage bucket and writes the data into Elasticsearch as JSON documents.",
            "If the CSV files contain headers, set the <code>containsHeaders</code> template parameter to <code>true</code>.\n"
                + "Otherwise, create a JSON schema file that describes the data. Specify the Cloud Storage URI of the schema file in the jsonSchemaPath template parameter. "
                + "The following example shows a JSON schema:\n"
                + "<code>[{\"name\":\"id\", \"type\":\"text\"}, {\"name\":\"age\", \"type\":\"integer\"}]</code>\n"
                + "Alternatively, you can provide a Javascript user-defined function (UDF) that parses the CSV text and outputs Elasticsearch documents."
          },
          optionsClass = GCSToElasticsearchOptions.class,
          skipOptions = {
            "javascriptTextTransformReloadIntervalMinutes",
            "pythonExternalTextTransformGcsPath",
            "pythonExternalTextTransformFunctionName"
          },
          flexContainerName = "googlecloud-to-elasticsearch",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-elasticsearch",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The Cloud Storage bucket must exist.",
            "A Elasticsearch host on a Google Cloud instance or on Elasticsearch Cloud that is accessible from Dataflow must exist.",
            "A BigQuery table for error output must exist."
          }),
      @Template(
          name = "GCS_to_Elasticsearch_Xlang",
          category = TemplateCategory.BATCH,
          displayName = "Cloud Storage to Elasticsearch with Python UDFs",
          type = Template.TemplateType.XLANG,
          description = {
            "The Cloud Storage to Elasticsearch template is a batch pipeline that reads data from CSV files stored in a Cloud Storage bucket and writes the data into Elasticsearch as JSON documents.",
            "If the CSV files contain headers, set the <code>containsHeaders</code> template parameter to <code>true</code>.\n"
                + "Otherwise, create a JSON schema file that describes the data. Specify the Cloud Storage URI of the schema file in the jsonSchemaPath template parameter. "
                + "The following example shows a JSON schema:\n"
                + "<code>[{\"name\":\"id\", \"type\":\"text\"}, {\"name\":\"age\", \"type\":\"integer\"}]</code>\n"
                + "Alternatively, you can provide a Python user-defined function (UDF) that parses the CSV text and outputs Elasticsearch documents."
          },
          optionsClass = GCSToElasticsearchOptions.class,
          skipOptions = {
            "javascriptTextTransformGcsPath",
            "javascriptTextTransformFunctionName",
            "javascriptTextTransformReloadIntervalMinutes"
          },
          flexContainerName = "googlecloud-to-elasticsearch-xlang",
          documentation =
              "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-elasticsearch",
          contactInformation = "https://cloud.google.com/support",
          preview = true,
          requirements = {
            "The Cloud Storage bucket must exist.",
            "A Elasticsearch host on a Google Cloud instance or on Elasticsearch Cloud that is accessible from Dataflow must exist.",
            "A BigQuery table for error output must exist."
          })
    })
    public class GCSToElasticsearch {
    
      /** The tag for the headers of the CSV if required. */
      static final TupleTag<String> CSV_HEADERS = new TupleTag<String>() {};
    
      /** The tag for the lines of the CSV. */
      static final TupleTag<String> CSV_LINES = new TupleTag<String>() {};
    
      /** The tag for the dead-letter output of the UDF. */
      static final TupleTag<FailsafeElement<String, String>> PROCESSING_DEADLETTER_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /** The tag for the main output for the UDF. */
      static final TupleTag<FailsafeElement<String, String>> PROCESSING_OUT =
          new TupleTag<FailsafeElement<String, String>>() {};
    
      /* Logger for class. */
      private static final Logger LOG = LoggerFactory.getLogger(GCSToElasticsearch.class);
    
      /** String/String Coder for FailsafeElement. */
      private static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(
              NullableCoder.of(StringUtf8Coder.of()), NullableCoder.of(StringUtf8Coder.of()));
    
      /**
       * Main entry point for pipeline execution.
       *
       * @param args Command line arguments to the pipeline.
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        GCSToElasticsearchOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(GCSToElasticsearchOptions.class);
    
        run(options);
      }
    
      /**
       * Runs the pipeline to completion with the specified options.
       *
       * @param options The execution options.
       * @return The pipeline result.
       */
      private static PipelineResult run(GCSToElasticsearchOptions options) {
        // Create the pipeline
        Pipeline pipeline = Pipeline.create(options);
    
        // Register the coder for pipeline
        CoderRegistry coderRegistry = pipeline.getCoderRegistry();
        coderRegistry.registerCoderForType(
            FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor(), FAILSAFE_ELEMENT_CODER);
    
        // Throw error if containsHeaders is true and a schema or Udf is also set.
        if (options.getContainsHeaders()) {
          checkArgument(
              options.getJavascriptTextTransformGcsPath() == null
                  && options.getJsonSchemaPath() == null
                  && options.getPythonExternalTextTransformGcsPath() == null,
              "Cannot parse file containing headers with UDF or Json schema.");
        }
    
        // Throw error if only one retry configuration parameter is set.
        checkArgument(
            (options.getMaxRetryAttempts() == null && options.getMaxRetryDuration() == null)
                || (options.getMaxRetryAttempts() != null && options.getMaxRetryDuration() != null),
            "To specify retry configuration both max attempts and max duration must be set.");
    
        // Throw error if both Javascript UDF and Python UDF are set. We can only apply one or the
        // other.
        boolean useJavascriptUdf = !Strings.isNullOrEmpty(options.getJavascriptTextTransformGcsPath());
        boolean usePythonUdf = !Strings.isNullOrEmpty(options.getPythonExternalTextTransformGcsPath());
        if (useJavascriptUdf && usePythonUdf) {
          throw new IllegalArgumentException(
              "Either javascript or Python gcs path must be provided, but not both.");
        }
    
        /*
         * Steps: 1) Read records from CSV(s) via {@link CsvConverters.ReadCsv}.
         *        2) Convert lines to JSON strings via {@link CsvConverters.LineToFailsafeJson}.
         *        3a) Write JSON strings as documents to Elasticsearch via {@link ElasticsearchIO}.
         *        3b) Write elements that failed processing to {@link org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO}.
         */
        PCollectionTuple readCsvLines =
            pipeline
                /*
                 * Step 1: Read CSV file(s) from Cloud Storage using {@link CsvConverters.ReadCsv}.
                 */
                .apply(
                "ReadCsv",
                CsvConverters.ReadCsv.newBuilder()
                    .setCsvFormat(options.getCsvFormat())
                    .setDelimiter(options.getDelimiter())
                    .setHasHeaders(options.getContainsHeaders())
                    .setInputFileSpec(options.getInputFileSpec())
                    .setHeaderTag(CSV_HEADERS)
                    .setLineTag(CSV_LINES)
                    .setFileEncoding(options.getCsvFileEncoding())
                    .build());
        /*
         * Step 2: Convert lines to Elasticsearch document.
         */
        CsvConverters.LineToFailsafeJson.Builder lineToFailsafeJsonBuilder =
            CsvConverters.LineToFailsafeJson.newBuilder()
                .setDelimiter(options.getDelimiter())
                .setJsonSchemaPath(options.getJsonSchemaPath())
                .setHeaderTag(CSV_HEADERS)
                .setLineTag(CSV_LINES)
                .setUdfOutputTag(PROCESSING_OUT)
                .setUdfDeadletterTag(PROCESSING_DEADLETTER_OUT);
        if (options.getPythonExternalTextTransformGcsPath() != null) {
          lineToFailsafeJsonBuilder
              .setPythonUdfFileSystemPath(options.getPythonExternalTextTransformGcsPath())
              .setPythonUdfFunctionName(options.getPythonExternalTextTransformFunctionName());
        } else {
          lineToFailsafeJsonBuilder
              .setJavascriptUdfFileSystemPath(options.getJavascriptTextTransformGcsPath())
              .setJavascriptUdfFunctionName(options.getJavascriptTextTransformFunctionName());
        }
        PCollectionTuple convertedCsvLines =
            readCsvLines.apply("ConvertLine", lineToFailsafeJsonBuilder.build());
        /*
         * Step 3a: Write elements that were successfully processed to Elasticsearch using {@link WriteToElasticsearch}.
         */
        convertedCsvLines
            .get(PROCESSING_OUT)
            .apply(
                "GetJsonDocuments",
                MapElements.into(TypeDescriptors.strings()).via(FailsafeElement::getPayload))
            .apply(
                "WriteToElasticsearch",
                WriteToElasticsearch.newBuilder()
                    .setUserAgent("dataflow-gcs-to-elasticsearch-template/v2")
                    .setOptions(options.as(GCSToElasticsearchOptions.class))
                    .build());
    
        /*
         * Step 3b: Write elements that failed processing to deadletter table via {@link BigQueryIO}.
         */
        convertedCsvLines
            .get(PROCESSING_DEADLETTER_OUT)
            .apply(
                "AddTimestamps",
                WithTimestamps.of((FailsafeElement<String, String> failures) -> new Instant()))
            .apply(
                "WriteFailedElementsToBigQuery",
                WriteStringMessageErrors.newBuilder()
                    .setErrorRecordsTable(options.getDeadletterTable())
                    .setErrorRecordsTableSchema(SchemaUtils.DEADLETTER_SCHEMA)
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
