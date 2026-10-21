---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/firestore-bulk-delete/
title: Firestore Bulk Delete template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:20.211092+00:00
---

# Firestore Bulk Delete template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/firestore-bulk-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Firestore Bulk Delete template Stay organized with collections  Save and categorize content based on your preferences. 

The Firestore Bulk Delete template is a pipeline which reads in Entities from Firestore with a given GQL query and then deletes all matching Entities in the selected target project. The pipeline can optionally pass the JSON encoded Firestore Entities to your Javascript UDF, which you can use to filter out Entities by returning null values.

## Pipeline requirements

  * Firestore must be set up in the project prior to running the template.
  * If reading and deleting from separate Firestore instances, the Dataflow [Worker Service Account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) must have permission to read from one instance and delete from the other.
  * [Database writes](https://docs.cloud.google.com/datastore/docs/console/datastore-admin-console#enabling_datastore_writes) must be enabled on the Firestore instance.



## Template parameters

Parameter | Description  
---|---  
`firestoreReadGqlQuery` | GQL query which specifies which entities to match for deletion. Using a keys-only query may improve performance. For example: "SELECT __key__ FROM MyKind".  
`firestoreReadProjectId` | Project ID of the Firestore instance from which you want to read entities (using your GQL query) that are used for matching.  
`firestoreDeleteProjectId` | Project ID of the Firestore instance from which to delete matching entities. This can be the same as `firestoreReadProjectId` if you want to read and delete within the same Firestore instance.  
`firestoreReadNamespace` | (Optional) Namespace of requested Entities. Set as "" for default namespace.  
`firestoreHintNumWorkers` | (Optional) Hint for the expected number of workers in the Firestore ramp-up throttling step. Default is `500`.  
`javascriptTextTransformGcsPath` | (Optional) The Cloud Storage URI of the `.js` file that defines the JavaScript user-defined function (UDF) you want to use. For example, `gs://my-bucket/my-udfs/my_file.js`.   
`javascriptTextTransformFunctionName` | (Optional) The name of the JavaScript user-defined function (UDF) that you want to use. For example, if your JavaScript function code is `myTransform(inJson) { /*...do stuff...*/ }`, then the function name is `myTransform`. For sample JavaScript UDFs, see [UDF Examples](https://github.com/GoogleCloudPlatform/DataflowTemplates#udf-examples). If this function returns a value of undefined or null for a given Firestore entity, then that entity is not deleted.  
  
## User-defined function

Optionally, you can extend this template by writing a user-defined function (UDF). The template calls the UDF for each input element. Element payloads are serialized as JSON strings. For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

### Function specification

The UDF has the following specification:

  * **Input** : a Firestore entity, serialized as a JSON string.
  * **Output** : if you want to keep the entity and not delete it, return `null` or `undefined`. Otherwise, return the original entity for deletion.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Bulk Delete Entities in Firestore** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run classic templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 138.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow jobs run JOB_NAME \
        --gcs-location gs://dataflow-templates/VERSION/Firestore_to_Firestore_Delete \
        --region REGION_NAME \
        --parameters \
    firestoreReadGqlQuery="GQL_QUERY",\
    firestoreReadProjectId=FIRESTORE_READ_AND_DELETE_PROJECT_ID,\
    firestoreDeleteProjectId=FIRESTORE_READ_AND_DELETE_PROJECT_ID

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `GQL_QUERY`: the query you'll use to match entities for deletion
  * `FIRESTORE_READ_AND_DELETE_PROJECT_ID`: your Firestore instance project ID. This example both reads and deletes from the same Firestore instance.



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://dataflow-templates/VERSION/Firestore_to_Firestore_Delete
    {
       "jobName": "JOB_NAME",
       "parameters": {
           "firestoreReadGqlQuery": "GQL_QUERY",
           "firestoreReadProjectId": "FIRESTORE_READ_AND_DELETE_PROJECT_ID",
           "firestoreDeleteProjectId": "FIRESTORE_READ_AND_DELETE_PROJECT_ID"
       },
       "environment": { "zone": "us-central1-f" }
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
  * `GQL_QUERY`: the query you'll use to match entities for deletion
  * `FIRESTORE_READ_AND_DELETE_PROJECT_ID`: your Firestore instance project ID. This example both reads and deletes from the same Firestore instance.



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
    import com.google.cloud.teleport.templates.DatastoreToDatastoreDelete.DatastoreToDatastoreDeleteOptions;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.DatastoreDeleteEntityJson;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.DatastoreDeleteOptions;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.DatastoreReadOptions;
    import com.google.cloud.teleport.templates.common.DatastoreConverters.ReadJsonEntities;
    import com.google.cloud.teleport.templates.common.FirestoreNestedValueProvider;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.JavascriptTextTransformerOptions;
    import com.google.cloud.teleport.templates.common.JavascriptTextTransformer.TransformTextViaJavascript;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.ValueProvider;
    
    /**
     * Dataflow template which deletes pulled Datastore Entities.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Datastore_to_Datastore_Delete.md">README
     * Datastore</a> or <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v1/README_Firestore_to_Firestore_Delete.md">README
     * Firestore</a> for instructions on how to use or modify this template.
     */
    @Template(
        name = "Datastore_to_Datastore_Delete",
        category = TemplateCategory.LEGACY,
        displayName = "Bulk Delete Entities in Datastore [Deprecated]",
        description =
            "A pipeline which reads in Entities (via a GQL query) from Datastore, optionally passes in the JSON encoded "
                + "Entities to a JavaScript UDF, and then deletes all matching Entities in the selected target project.",
        optionsClass = DatastoreToDatastoreDeleteOptions.class,
        skipOptions = {
          "firestoreReadGqlQuery",
          "firestoreReadProjectId",
          "firestoreReadNamespace",
          "firestoreDeleteProjectId",
          "firestoreHintNumWorkers",
          "javascriptTextTransformReloadIntervalMinutes"
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/datastore-bulk-delete",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "Datastore must be set up in the project prior to running the template.",
          "If reading and deleting from separate Datastore instances, the Dataflow <a href=\"https://cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account\">Worker Service Account</a> must have permission to read from one instance and delete from the other."
        })
    @Template(
        name = "Firestore_to_Firestore_Delete",
        category = TemplateCategory.UTILITIES,
        displayName = "Bulk Delete Entities in Firestore (Datastore mode)",
        description =
            "A pipeline which reads in Entities (via a GQL query) from Firestore, optionally passes in the JSON encoded "
                + "Entities to a JavaScript UDF, and then deletes all matching Entities in the selected target project.",
        optionsClass = DatastoreToDatastoreDeleteOptions.class,
        optionsOrder = {
          DatastoreReadOptions.class,
          DatastoreDeleteOptions.class,
          JavascriptTextTransformerOptions.class
        },
        skipOptions = {
          "datastoreReadGqlQuery",
          "datastoreReadProjectId",
          "datastoreReadNamespace",
          "datastoreDeleteProjectId",
          "datastoreHintNumWorkers",
          "javascriptTextTransformReloadIntervalMinutes"
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/firestore-bulk-delete",
        contactInformation = "https://cloud.google.com/support",
        requirements = {
          "Firestore must be set up in the project prior to running the template.",
          "If reading and deleting from separate Firestore instances, the Dataflow <a href=\"https://cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account\">Worker Service Account</a> must have permission to read from one instance and delete from the other."
        })
    public class DatastoreToDatastoreDelete {
    
      public static <T> ValueProvider<T> selectProvidedInput(
          ValueProvider<T> datastoreInput, ValueProvider<T> firestoreInput) {
        return new FirestoreNestedValueProvider<T>(datastoreInput, firestoreInput);
      }
    
      /** Custom PipelineOptions. */
      public interface DatastoreToDatastoreDeleteOptions
          extends PipelineOptions,
              DatastoreReadOptions,
              JavascriptTextTransformerOptions,
              DatastoreDeleteOptions {}
    
      /**
       * Runs a pipeline which reads in Entities from datastore, passes in the JSON encoded Entities to
       * a Javascript UDF, and deletes all the Entities.
       *
       * <p>If the UDF returns value of undefined or null for a given Entity, then that Entity will not
       * be deleted.
       *
       * @param args arguments to the pipeline
       */
      public static void main(String[] args) {
        DatastoreToDatastoreDeleteOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(DatastoreToDatastoreDeleteOptions.class);
    
        Pipeline pipeline = Pipeline.create(options);
    
        pipeline
            .apply(
                ReadJsonEntities.newBuilder()
                    .setGqlQuery(
                        selectProvidedInput(
                            options.getDatastoreReadGqlQuery(), options.getFirestoreReadGqlQuery()))
                    .setProjectId(
                        selectProvidedInput(
                            options.getDatastoreReadProjectId(), options.getFirestoreReadProjectId()))
                    .setNamespace(
                        selectProvidedInput(
                            options.getDatastoreReadNamespace(), options.getFirestoreReadNamespace()))
                    .build())
            .apply(
                TransformTextViaJavascript.newBuilder()
                    .setFileSystemPath(options.getJavascriptTextTransformGcsPath())
                    .setFunctionName(options.getJavascriptTextTransformFunctionName())
                    .build())
            .apply(
                DatastoreDeleteEntityJson.newBuilder()
                    .setProjectId(
                        selectProvidedInput(
                            options.getDatastoreDeleteProjectId(),
                            options.getFirestoreDeleteProjectId()))
                    .setHintNumWorkers(
                        selectProvidedInput(
                            options.getDatastoreHintNumWorkers(), options.getFirestoreHintNumWorkers()))
                    .build());
    
        pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
