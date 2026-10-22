---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/google-cloud-to-neo4j/
title: Google Cloud to Neo4j template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:51.217015+00:00
---

# Google Cloud to Neo4j template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/google-cloud-to-neo4j/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Google Cloud to Neo4j template Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud to Neo4j template lets you import a dataset into a Neo4j database through a Dataflow job, sourcing data from CSV files hosted in Cloud Storage buckets. It also lets you manipulate and transform the data at various steps of the import. You can use the template for both first-time imports and incremental imports.

## Pipeline requirements

  * A running Neo4j instance
  * A Cloud Storage bucket
  * A dataset to import, in the form of CSV files
  * A job specification file to use



## Create a job specification file

The job specification file consists of a JSON object with the following sections:

  * `config`: global flags affecting how the import is performed.
  * `sources`: data source definitions (relational).
  * `targets`: data target definitions (graph: nodes/relationships).
  * `actions`: pre/post-load actions.



For more information, see [Create a job specification file](https://neo4j.com/docs/dataflow-google-cloud/current/job-specification/) in the Neo4j documentation.

## Template parameters

### Required parameters

  * **jobSpecUri** : The path to the job specification file, which contains the JSON description of data sources, Neo4j targets and actions.



### Optional parameters

  * **neo4jConnectionUri** : The path to the Neo4j connection JSON file.
  * **neo4jConnectionSecretId** : The secret ID for the Neo4j connection metadata. You can use this value as an alternative to the `neo4jConnectionUri`.
  * **optionsJson** : A JSON object that is also called runtime tokens For example, `{token1:value1,token2:value2}. Spec can refer to $token1 and $token2.`. Defaults to empty.
  * **readQuery** : SQL query override. Defaults to empty.
  * **inputFilePattern** : The text file path override For example, `gs://your-bucket/path/*.json`. Defaults to empty.
  * **disabledAlgorithms** : Comma separated algorithms to disable. If this value is set to `none`, no algorithm is disabled. Use this parameter with caution, because the algorithms disabled by default might have vulnerabilities or performance issues. For example, `SSLv3, RC4`.
  * **extraFilesToStage** : Comma separated Cloud Storage paths or Secret Manager secrets for files to stage in the worker. These files are saved in the /extra_files directory in each worker. For example, `gs://<BUCKET_NAME>/file.txt,projects/<PROJECT_ID>/secrets/<SECRET_ID>/versions/<VERSION_ID>`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Google Cloud to Neo4j** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Google_Cloud_to_Neo4j \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           jobSpecUri=JOB_SPEC_URI,\
           neo4jConnectionUri=NEO4J_CONNECTION_URI,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `JOB_SPEC_URI`: the path to the job specification file
  * `NEO4J_CONNECTION_URI`: the path to the Neo4j connection metadata



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "jobSpecUri": "JOB_SPEC_URI",
           "neo4jConnectionUri": "NEO4J_CONNECTION_URI",
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Google_Cloud_to_Neo4j",
         "environment": { "maxWorkers": "10" }
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
  * `JOB_SPEC_URI`: the path to the job specification file
  * `NEO4J_CONNECTION_URI`: the path to the Neo4j connection metadata



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
    package com.google.cloud.teleport.v2.neo4j.templates;
    
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.Template.AdditionalDocumentationBlock;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.common.UncaughtExceptionLogger;
    import com.google.cloud.teleport.v2.neo4j.model.InputValidator;
    import com.google.cloud.teleport.v2.neo4j.model.Json;
    import com.google.cloud.teleport.v2.neo4j.model.Json.ParsingResult;
    import com.google.cloud.teleport.v2.neo4j.model.connection.ConnectionParams;
    import com.google.cloud.teleport.v2.neo4j.model.helpers.JobSpecMapper;
    import com.google.cloud.teleport.v2.neo4j.model.helpers.OverlayTokenParser;
    import com.google.cloud.teleport.v2.neo4j.options.Neo4jFlexTemplateOptions;
    import com.google.cloud.teleport.v2.neo4j.utils.FileSystemUtils;
    import com.google.cloud.teleport.v2.utils.SecretManagerUtils;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.io.FileSystems;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.commons.lang3.StringUtils;
    import org.neo4j.importer.v1.pipeline.ImportPipeline;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * Dataflow template which reads Google Cloud data (Text, BigQuery) and writes it to Neo4j.
     *
     * <p>In case of BigQuery, the source data can be either a table or a SQL query.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/googlecloud-to-neo4j/README_Google_Cloud_to_Neo4j.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Google_Cloud_to_Neo4j",
        category = TemplateCategory.BATCH,
        displayName = "Google Cloud to Neo4j",
        description =
            "The Google Cloud to Neo4j template lets you import a dataset into a Neo4j database through a Dataflow job, "
                + "sourcing data from CSV files hosted in Google Cloud Storage buckets. It also lets you to manipulate and transform the data "
                + "at various steps of the import. You can use the template for both first-time imports and incremental imports.",
        optionsClass = Neo4jFlexTemplateOptions.class,
        flexContainerName = "googlecloud-to-neo4j",
        contactInformation = "https://support.neo4j.com/",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/google-cloud-to-neo4j",
        requirements = {
          "A running Neo4j instance",
          "A Google Cloud Storage bucket",
          "A dataset to import, in the form of CSV files",
          "A job specification file to use"
        },
        additionalDocumentation = {
          @AdditionalDocumentationBlock(
              name = "Create a job specification file",
              content = {
                "The job specification file consists of a JSON object with the following sections:\n"
                    + "- `config` - global flags affecting how the import is performed.\n"
                    + "- `sources` - data source definitions (relational).\n"
                    + "- `targets` - data target definitions (graph: nodes/relationships/custom queries).\n"
                    + "- `actions` - pre/post-load actions.\n"
                    + "For more information, see <a href=\"https://neo4j.com/docs/dataflow-google-cloud/job-specification/\" class=\"external\">Create a job specification file</a> in the Neo4j documentation."
              })
        },
        preview = true)
    public class GoogleCloudToNeo4j {
    
      private static final Logger LOG = LoggerFactory.getLogger(GoogleCloudToNeo4j.class);
    
      /**
       * Runs a pipeline which reads data from various sources and writes it to Neo4j.
       *
       * @param args arguments to the pipeline
       */
      public static void main(String[] args) {
        UncaughtExceptionLogger.register();
    
        Neo4jFlexTemplateOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(Neo4jFlexTemplateOptions.class);
        ValidationErrors.processValidations(
            "Errors found validating pipeline options: ",
            InputValidator.validateNeo4jPipelineOptions(options));
    
        if (StringUtils.isBlank(options.getDisabledAlgorithms())) {
          options.setDisabledAlgorithms(
              "SSLv3, RC4, DES, MD5withRSA, DH keySize < 1024, EC keySize < 224, 3DES_EDE_CBC, anon,"
                  + " NULL");
        }
        LOG.info("Job: {}", options.getJobSpecUri());
        FileSystems.setDefaultPipelineOptions(options);
        var overlayTokens = OverlayTokenParser.parse(options.getOptionsJson());
        var templateVersion = readTemplateVersion(options);
        var neo4jConnectionConfig = readConnectionConfiguration(options);
        var importSpecification = JobSpecMapper.parse(options.getJobSpecUri(), overlayTokens);
        var importPipeline =
            new Neo4jImportPipelineRunner(
                options,
                templateVersion,
                neo4jConnectionConfig,
                overlayTokens,
                ImportPipeline.of(importSpecification));
        importPipeline.run();
      }
    
      private static String readTemplateVersion(Neo4jFlexTemplateOptions options) {
        var labels = options.as(DataflowPipelineOptions.class).getLabels();
        String defaultVersion = "UNKNOWN";
        if (labels == null) {
          return defaultVersion;
        }
        return labels.getOrDefault("goog-dataflow-provided-template-version", defaultVersion);
      }
    
      private static ConnectionParams readConnectionConfiguration(
          Neo4jFlexTemplateOptions pipelineOptions) {
        String neo4jConnectionJson = readConnectionSettings(pipelineOptions);
        ParsingResult parsingResult = InputValidator.validateNeo4jConnection(neo4jConnectionJson);
        if (!parsingResult.isSuccessful()) {
          ValidationErrors.processValidations(
              "Errors found validating Neo4j connection: ",
              parsingResult.formatErrors("Could not validate connection JSON"));
        }
        return Json.map(parsingResult, ConnectionParams.class);
      }
    
      private static String readConnectionSettings(Neo4jFlexTemplateOptions options) {
        String secretId = options.getNeo4jConnectionSecretId();
        if (StringUtils.isNotEmpty(secretId)) {
          return SecretManagerUtils.getSecret(secretId);
        }
        String uri = options.getNeo4jConnectionUri();
        try {
          return FileSystemUtils.getPathContents(uri);
        } catch (Exception e) {
          throw new RuntimeException(
              String.format("Unable to read Neo4j configuration at URI %s: ", uri), e);
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
