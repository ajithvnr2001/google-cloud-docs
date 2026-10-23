---
url: https://docs.cloud.google.com/storage/docs/object-enrichments/manage-object-enrichments/
title: Manage object enrichments \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:25.429954+00:00
---

# Manage object enrichments  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/object-enrichments/manage-object-enrichments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Manage object enrichments Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you [configure object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments), Cloud Storage evaluates eligible objects asynchronously and attaches enrichment metadata directly to your stored objects.

This page explains how to inspect basic context metadata, retrieve [extended data](https://docs.cloud.google.com/storage/docs/object-contexts#extended-data) payloads, discard enrichments from objects, and monitor processing progress in Cloud Monitoring.

## Get the required roles

To get the permissions that you need to view, retrieve, and discard object enrichments, ask your administrator to grant you the following IAM roles on your bucket or project: 

  * View basic object enrichments metadata: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) 
  * Retrieve object enrichments extended data: [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) 
  * Discard object enrichments during object rewrite: [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view, retrieve, and discard object enrichments. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view, retrieve, and discard object enrichments:

  * View basic object enrichments context metadata: `storage.objects.get`
  * Retrieve object enrichments extended data: `storage.objects.viewFullContext`
  * Discard object enrichments during object rewrite: 
    * `storage.objects.get`
    * `storage.objects.create`
    * `storage.objects.delete`
    * `storage.objects.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View object enrichments

Cloud Storage attaches enrichment metadata directly to your objects as Google-managed [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) under the `contexts.custom` property. Each model uses a reserved key prefixed with `google:annotation:` (for example, `google:annotation:label-detector-v1` or `google:annotation:face-detector-v1`).

Cloud Storage organizes enrichment data into two tiers:

  * **Context metadata** : Contains the context key, model execution status (`value`), timestamps, and the protobuf type URL. Standard object `describe` and `get` operations return this metadata.
  * **Extended data** ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): Contains the full structured JSON enrichment payload (up to 128 KiB). This payload includes details such as bounding polygon coordinates, classification confidence scores, facial expressions, and safety ratings.



### View basic context metadata

To check which models have processed an object and view basic context metadata, use the Google Cloud console or the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object that you want to inspect.

In the **Objects** table, the **Custom contexts** column displays a chip for each model that has processed an object (**Content Safety** , **Face Detector** , **Label Detector** , **Object Detector** , or **PDF Classification**).

  3. To inspect an individual object, click the object's name.

  4. On the **Object details** page, go to the **Custom contexts** field. If the field has multiple chips, click expand_more to expand the row.

  5. Hold the pointer over or click a model chip to view its basic context metadata:

     * **Context key** : The reserved model key, such as `google:annotation:label-detector-v1`.
     * **Context value** : The model execution status (`SUCCESS` or `FAILURE`).
     * **Creation time** and **Last modified time** : The timestamps for when Cloud Storage created and last updated the enrichment.
     * **View configuration hub** : Opens the **Object enrichments** page. When you view a chip from the bucket's **Objects** table, you can also click **Filter contexts** to filter objects in the bucket by that context.



### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.se/) to send an [`Objects: get` request](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) with the `projection=full` query parameter to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?projection=full"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object. For example, `image.jpg`.

The response returns the `contexts.custom` structure:
    
    {
      "kind": "storage#object",
      "id": "my-bucket/image.jpg/1700000000000000",
      "name": "image.jpg",
      "bucket": "my-bucket",
      "contexts": {
        "custom": {
          "google:annotation:label-detector-v1": {
            "value": "SUCCESS",
            "createTime": "2026-09-29T17:20:00.000Z",
            "updateTime": "2026-09-29T17:20:00.000Z",
            "extendedDataTypeUrl": "type.googleapis.com/google.protobuf.Struct"
          }
        }
      }
    }
    

The `value` field indicates the model execution status for the object, such as `SUCCESS` or `FAILURE`.




### Retrieve extended data

To retrieve the full structured enrichment data (such as bounding boxes, bounding polygons, labels, or detected faces), call the [`viewFullContext` method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) by using the JSON API.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.se/) to send a [`viewFullContext` request](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext) to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api), specifying the context key of the model that you want to inspect:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME/viewFullContext?contextKey=CONTEXT_KEY"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object. For example, `image.jpg`.
     * `CONTEXT_KEY` is the model context key. For example, `google:annotation:label-detector-v1`.

The response contains the `extendedData` structure with the full enrichment payload:
    
    {
      "kind": "storage#objectFullContext",
      "type": "CUSTOM",
      "key": "google:annotation:label-detector-v1",
      "value": "SUCCESS",
      "createTime": "2026-09-29T17:20:00.000Z",
      "updateTime": "2026-09-29T17:20:00.000Z",
      "extendedData": {
        "@type": "type.googleapis.com/google.protobuf.Struct",
        "modelName": "label-detector",
        "modelVersion": "v1",
        "labelAnnotationGroup": {
          "labelAnnotations": [
            {
              "description": "Night",
              "knowledgeGraphId": "/m/01d74z",
              "score": 0.92,
              "topicality": 0.19
            }
          ]
        }
      }
    }
    




For detailed JSON schemas and fields for each model, see [Supported models and schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models).

## Discard object enrichments

If you must comply with data retention policies or no longer need enrichment metadata, you can discard it from your objects.

Because Google manages context keys starting with the `google:` prefix, you can't modify or delete them by using standard metadata update methods. Instead, you discard them during an object rewrite, copy, or compose operation by specifying the `dropContextGroups=custom` parameter, which discards all object contexts on the object.

To discard object contexts (including object enrichments) when rewriting an object by using the [JSON API](https://docs.cloud.google.com/storage/docs/json_api), do the following:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` rewrite Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) request and the `dropContextGroups=custom` query parameter:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Length: 0" \
           "https://storage.googleapis.com/storage/v1/b/SOURCE_BUCKET/o/SOURCE_OBJECT/rewriteTo/b/DESTINATION_BUCKET/o/DESTINATION_OBJECT?dropContextGroups=custom"

Where:

     * `SOURCE_BUCKET` is the name of the bucket containing the source object. For example, `my-source-bucket`.
     * `SOURCE_OBJECT` is the URL-encoded name of the source object. For example, `image.jpg`.
     * `DESTINATION_BUCKET` is the name of the destination bucket (can match the source bucket). For example, `my-source-bucket`.
     * `DESTINATION_OBJECT` is the URL-encoded name of the destination object (can match the source object). For example, `image.jpg`.



To manage and discard contexts across billions of objects, see [Manage object contexts in bulk](https://docs.cloud.google.com/storage/docs/use-object-contexts#bulk-contexts).

## Monitor object enrichments metrics

You can track enrichment processing throughput, pending objects, and model execution counts by using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Cloud Storage exports the following metrics under the `storage.googleapis.com` namespace on the [`gcs_bucket` monitored resource](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket):

Metric type (prefixed with `storage.googleapis.com/`) | Kind and type | Description and labels  
---|---|---  
`auto_annotate/operations/pending_objects` | `GAUGE`, `INT64` | Total number of objects pending enrichment in the bucket. Sampled every 300 seconds.  
`auto_annotate/operations/processed_object_count` | `DELTA`, `INT64` | Total number of objects processed by object enrichments during the time window. Sampled every 300 seconds.  
`auto_annotate/operations/model_count` | `DELTA`, `INT64` | Total number of models executed in the bucket during the time window, grouped by `model_name`, `model_version`, and `status` (such as `SUCCESS` or `FAILURE`).  
`auto_annotate/operations/request_count` | `DELTA`, `INT64` | Total number of API calls made during the time window, grouped by `method` and `response_code`.  
`auto_annotate/storage/annotated_objects` | `GAUGE`, `INT64` | Daily snapshot of the total number of objects in the bucket that have enrichments generated for them, grouped by `type` and `data_locations`.  
`auto_annotate/storage/model_outputs` | `GAUGE`, `INT64` | Daily snapshot of the total number of model outputs stored in the bucket, grouped by `model_name`, `model_version`, `status`, `type`, and `data_locations`.  
  
For more information about querying metrics and setting up alerts, see [Cloud Monitoring metrics for Cloud Storage](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) and [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## What's next

  * [Configure object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments).
  * [Analyze object enrichments with SQL in BigQuery](https://docs.cloud.google.com/storage/docs/object-enrichments/analyze-bigquery).
  * [Review supported models and output schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models).
  * [Read the object enrichments overview](https://docs.cloud.google.com/storage/docs/object-enrichments/overview).
  * [Review the `featureConfigs` JSON API resource and methods](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs).
  * [Learn about object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).
  * [Manage objects in bulk with Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
