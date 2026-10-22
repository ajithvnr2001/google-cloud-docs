---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-cloud-spanner/
title: Cloud Storage Avro to Spanner template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:16.434716+00:00
---

# Cloud Storage Avro to Spanner template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-cloud-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Cloud Storage Avro to Spanner template Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage Avro files to Spanner template is a batch pipeline that reads Avro files exported from Spanner stored in Cloud Storage and imports them to a Spanner database. 

## Pipeline requirements

  * The target Spanner database must exist and must be empty.
  * You must have read permissions for the Cloud Storage bucket and write permissions for the target Spanner database.
  * The input Cloud Storage path must exist, and it must include a [`spanner-export.json`](https://docs.cloud.google.com/spanner/docs/import-non-spanner#create-export-json) file that contains a JSON description of files to import.
  * If the source Avro file doesn't contain a primary key, you must create an empty Spanner table with a primary key before you run the template. This step isn't required if the Avro file defines the primary key. 

**Warning:** If the target Spanner database is not empty, new data might overwrite pre-existing data, or the import might fail.

## Template parameters

### Required parameters

  * **instanceId** : The instance ID of the Spanner database.
  * **databaseId** : The database ID of the Spanner database.
  * **inputDir** : The Cloud Storage path where the Avro files are imported from.



### Optional parameters

  * **spannerHost** : The Cloud Spanner endpoint to call in the template. Only used for testing. For example, `https://batch-spanner.googleapis.com`. Defaults to: <https://batch-spanner.googleapis.com>.
  * **waitForIndexes** : If `true`, the pipeline waits for indexes to be created. If `false`, the job might complete while indexes are still being created in the background. The default value is `false`.
  * **waitForForeignKeys** : If `true`, the pipeline waits for foreign keys to be created. If `false`, the job might complete while foreign keys are still being created in the background. The default value is `false`.
  * **waitForChangeStreams** : If `true`, the pipeline waits for change streams to be created. If `false`, the job might complete while change streams are still being created in the background. The default value is `true`.
  * **waitForSequences** : By default, the import pipeline is blocked on sequence creation. If `false`, the import pipeline might complete with sequences still being created in the background.
  * **earlyIndexCreateFlag** : Specifies whether early index creation is enabled. If the template runs a large number of DDL statements, it's more efficient to create indexes before loading data. Therefore, the default behavior is to create the indexes first when the number of DDL statements exceeds a threshold. To disable this feature, set `earlyIndexCreateFlag` to `false`. The default value is `true`.
  * **spannerProjectId** : The ID of the Google Cloud project that contains the Spanner database. If not set, the default Google Cloud project is used.
  * **ddlCreationTimeoutInMinutes** : The timeout in minutes for DDL statements performed by the template. The default value is 30 minutes.
  * **spannerPriority** : The request priority for Spanner calls. Possible values are `HIGH`, `MEDIUM`, and `LOW`. The default value is `MEDIUM`.
  * **earlyIndexCreateThreshold** : The threshold for the number of indexes and foreign keys that determines whether to create indexes before data loading. If the total number of indexes and foreign keys is larger than this threshold, they will be created before data import for better performance. The default value is 40.
  * **runIndexDdlInParallel** : If `true`, the pipeline executes index creation DDL statements in parallel. The default value is `false`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 

For the job to show up in the Spanner [Instances](https://console.cloud.google.com/spanner/instances) page of the Google Cloud console, the job name must match the following format:
         
         cloud-spanner-import-SPANNER_INSTANCE_ID-SPANNER_DATABASE_NAME

Replace the following:

     * `SPANNER_INSTANCE_ID`: your Spanner instance's ID
     * `SPANNER_DATABASE_NAME`: your Spanner database's name
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Avro Files on Cloud Storage to Cloud Spanner** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/GCS_Avro_to_Cloud_Spanner \
        --region REGION_NAME \
        --staging-location GCS_STAGING_LOCATION \
        --parameters \
    instanceId=INSTANCE_ID,\
    databaseId=DATABASE_ID,\
    inputDir=GCS_DIRECTORY

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `INSTANCE_ID`: the ID of the Spanner instance that contains the database
  * `DATABASE_ID`: the ID of the Spanner database to import to
  * `GCS_DIRECTORY`: the Cloud Storage path where the Avro files are imported from, for example, `gs://mybucket/somefolder`



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/GCS_Avro_to_Cloud_Spanner
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "instanceId": "INSTANCE_ID",
           "databaseId": "DATABASE_ID",
           "inputDir": "gs://GCS_DIRECTORY"
       },
       "environment": {
           "machineType": "n1-standard-2"
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
  * `INSTANCE_ID`: the ID of the Spanner instance that contains the database
  * `DATABASE_ID`: the ID of the Spanner database to import to
  * `GCS_DIRECTORY`: the Cloud Storage path where the Avro files are imported from, for example, `gs://mybucket/somefolder`



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
    package com.google.cloud.teleport.spanner;
    
    import com.google.cloud.spanner.[Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html).[RpcPriority](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.RpcPriority.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateCreationParameter;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.metadata.TemplateParameter.TemplateEnumOption;
    import com.google.cloud.teleport.spanner.ImportPipeline.[Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html);
    import com.google.cloud.teleport.spanner.spannerio.SpannerConfig;
    import org.apache.beam.runners.dataflow.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).Default;
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).Description;
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).PipelineOptions;
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).PipelineOptionsFactory;
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).ValueProvider;
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).ValueProvider.NestedValueProvider;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    
    /**
     * Avro to Cloud Spanner Import pipeline.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_GCS_Avro_to_Cloud_Spanner.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "GCS_Avro_to_Cloud_Spanner",
        category = TemplateCategory.BATCH,
        displayName = "Avro Files on Cloud Storage to Cloud Spanner",
        description =
            "The Cloud Storage Avro files to Cloud Spanner template is a batch pipeline that reads Avro files exported from "
                + "Cloud Spanner stored in Cloud Storage and imports them to a Cloud Spanner database.",
        optionsClass = [Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html).class,
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/avro-to-cloud-spanner",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "The target Cloud Spanner database must exist and must be empty.",
          "You must have read permissions for the Cloud Storage bucket and write permissions for the target Cloud Spanner database.",
          "The input Cloud Storage path must exist, and it must include a <a href=\"https://cloud.google.com/spanner/docs/import-non-spanner#create-export-json\">spanner-export.json</a> file that contains a JSON description of files to import."
        })
    public class ImportPipeline {
    
      /** Options for {@link ImportPipeline}. */
      public interface Options extends PipelineOptions {
    
        @TemplateParameter.Text(
            order = 1,
            groupName = "Target",
            regexes = {"^[a-z0-9\\-]+$"},
            description = "Cloud Spanner instance ID",
            helpText = "The instance ID of the Spanner database.")
        ValueProvider<String> getInstanceId();
    
        void setInstanceId(ValueProvider<String> value);
    
        @TemplateParameter.Text(
            order = 2,
            groupName = "Target",
            regexes = {"^[a-z_0-9\\-]+$"},
            description = "Cloud Spanner database ID",
            helpText = "The database ID of the Spanner database.")
        ValueProvider<String> getDatabaseId();
    
        void setDatabaseId(ValueProvider<String> value);
    
        @TemplateParameter.GcsReadFolder(
            order = 3,
            groupName = "Source",
            description = "Cloud storage input directory",
            helpText = "The Cloud Storage path where the Avro files are imported from.")
        ValueProvider<String> getInputDir();
    
        void setInputDir(ValueProvider<String> value);
    
        @TemplateParameter.Text(
            order = 4,
            groupName = "Target",
            optional = true,
            description = "Cloud Spanner Endpoint to call",
            helpText = "The Cloud Spanner endpoint to call in the template. Only used for testing.",
            example = "https://batch-spanner.googleapis.com")
        @Default.String("https://batch-spanner.googleapis.com")
        ValueProvider<String> getSpannerHost();
    
        void setSpannerHost(ValueProvider<String> value);
    
        @TemplateParameter.Boolean(
            order = 5,
            optional = true,
            description = "Wait for Indexes",
            helpText =
                "If `true`, the pipeline waits for indexes to be created. If `false`, the job might complete while indexes are still being created in the background. The default value is `false`.")
        @Default.Boolean(false)
        ValueProvider<Boolean> getWaitForIndexes();
    
        void setWaitForIndexes(ValueProvider<Boolean> value);
    
        @TemplateParameter.Boolean(
            order = 6,
            optional = true,
            description = "Wait for Foreign Keys",
            helpText =
                "If `true`, the pipeline waits for foreign keys to be created. If `false`, the job might complete while foreign keys are still being created in the background. The default value is `false`.")
        @Default.Boolean(false)
        ValueProvider<Boolean> getWaitForForeignKeys();
    
        void setWaitForForeignKeys(ValueProvider<Boolean> value);
    
        @TemplateParameter.Boolean(
            order = 7,
            optional = true,
            description = "Wait for Change Streams",
            helpText =
                "If `true`, the pipeline waits for change streams to be created. If `false`, the job might complete while change streams are still being created in the background. The default value is `true`.")
        @Default.Boolean(true)
        ValueProvider<Boolean> getWaitForChangeStreams();
    
        void setWaitForChangeStreams(ValueProvider<Boolean> value);
    
        @TemplateParameter.Boolean(
            order = 7,
            optional = true,
            description = "Wait for Sequences",
            helpText =
                "By default, the import pipeline is blocked on sequence creation. If `false`, the import pipeline might"
                    + " complete with sequences still being created in the background.")
        @Default.Boolean(true)
        ValueProvider<Boolean> getWaitForSequences();
    
        void setWaitForSequences(ValueProvider<Boolean> value);
    
        @TemplateParameter.Boolean(
            order = 8,
            optional = true,
            description = "Create Indexes early",
            helpText =
                "Specifies whether early index creation is enabled. If the template runs a large number of DDL statements, it's more efficient to create indexes before loading data. Therefore, the default behavior is to create the indexes first when the number of DDL statements exceeds a threshold. To disable this feature, set `earlyIndexCreateFlag` to `false`. The default value is `true`.")
        @Default.Boolean(true)
        ValueProvider<Boolean> getEarlyIndexCreateFlag();
    
        void setEarlyIndexCreateFlag(ValueProvider<Boolean> value);
    
        @TemplateCreationParameter(value = "false")
        @Description("If true, wait for job finish")
        @Default.Boolean(true)
        boolean getWaitUntilFinish();
    
        @TemplateParameter.ProjectId(
            order = 9,
            groupName = "Target",
            optional = true,
            description = "Cloud Spanner Project Id",
            helpText =
                "The ID of the Google Cloud project that contains the Spanner database. If not set, the default Google Cloud project is used.")
        ValueProvider<String> getSpannerProjectId();
    
        void setSpannerProjectId(ValueProvider<String> value);
    
        void setWaitUntilFinish(boolean value);
    
        @TemplateParameter.Integer(
            order = 10,
            optional = true,
            description = "DDL Creation timeout in minutes",
            helpText =
                "The timeout in minutes for DDL statements performed by the template. The default value is 30 minutes.")
        @Default.Integer(30)
        ValueProvider<Integer> getDdlCreationTimeoutInMinutes();
    
        void setDdlCreationTimeoutInMinutes(ValueProvider<Integer> value);
    
        @TemplateParameter.Enum(
            order = 11,
            groupName = "Target",
            enumOptions = {
              @TemplateEnumOption("LOW"),
              @TemplateEnumOption("MEDIUM"),
              @TemplateEnumOption("HIGH")
            },
            optional = true,
            description = "Priority for Spanner RPC invocations",
            helpText =
                "The request priority for Spanner calls. Possible values are `HIGH`, `MEDIUM`, and `LOW`. The default value is `MEDIUM`.")
        ValueProvider<RpcPriority> getSpannerPriority();
    
        void setSpannerPriority(ValueProvider<RpcPriority> value);
    
        @TemplateParameter.Integer(
            order = 12,
            optional = true,
            description = "Early Index Create Threshold",
            helpText =
                "The threshold for the number of indexes and foreign keys that determines whether to create indexes before data loading. If the total number of indexes and foreign keys is larger than this threshold, they will be created before data import for better performance. The default value is 40.")
        @Default.Integer(40)
        ValueProvider<Integer> getEarlyIndexCreateThreshold();
    
        void setEarlyIndexCreateThreshold(ValueProvider<Integer> value);
    
        @TemplateParameter.Boolean(
            order = 13,
            optional = true,
            description = "Run Index DDL in parallel",
            helpText =
                "If `true`, the pipeline executes index creation DDL statements in parallel. The default value is `false`.")
        @Default.Boolean(false)
        ValueProvider<Boolean> getRunIndexDdlInParallel();
    
        void setRunIndexDdlInParallel(ValueProvider<Boolean> value);
      }
    
      public static void main(String[] args) {
    
        [Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html) options = PipelineOptionsFactory.fromArgs(args).withValidation().as([Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html).class);
    
        Pipeline p = Pipeline.create(options);
    
        SpannerConfig spannerConfig =
            SpannerConfig.create()
                // Temporary fix explicitly setting SpannerConfig.projectId to the default project
                // if spannerProjectId is not provided as a parameter. Required as of Beam 2.38,
                // which no longer accepts null label values on metrics, and SpannerIO#setup() has
                // a bug resulting in the label value being set to the original parameter value,
                // with no fallback to the default project.
                // TODO: remove NestedValueProvider when this is fixed in Beam.
                .withProjectId(
                    NestedValueProvider.of(
                        [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getSpannerProjectId(),
                        (SerializableFunction<String, String>)
                            input -> input != null ? input : [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).[getDefaultProjectId](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.ConnectionOptions.html#com_google_cloud_spanner_connection_ConnectionOptions_getDefaultProjectId_com_google_auth_Credentials_)()))
                .withHost([options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getSpannerHost())
                .withInstanceId([options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getInstanceId())
                .withDatabaseId([options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getDatabaseId())
                .withRpcPriority([options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getSpannerPriority());
    
        p.apply(
            new ImportTransform(
                spannerConfig,
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getInputDir(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getWaitForIndexes(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getWaitForForeignKeys(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getWaitForChangeStreams(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getWaitForSequences(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getEarlyIndexCreateFlag(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getDdlCreationTimeoutInMinutes(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getEarlyIndexCreateThreshold(),
                [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getRunIndexDdlInParallel()));
    
        PipelineResult result = p.run();
    
        if ([options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getWaitUntilFinish()
            &&
            /* Only if template location is null, there is a dataflow job to wait for. Else it's
             * template generation which doesn't start a dataflow job.
             */
            options.as(DataflowPipelineOptions.class).getTemplateLocation() == null) {
          result.waitUntilFinish();
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
