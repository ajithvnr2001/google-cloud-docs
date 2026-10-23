---
url: https://docs.cloud.google.com/storage/docs/object-contexts/
title: Object contexts \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:43.070973+00:00
---

# Object contexts  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/object-contexts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Object contexts Stay organized with collections  Save and categorize content based on your preferences. 

Object contexts let you associate custom key-value pairs with your Cloud Storage objects so you can categorize, track, and search your data.

For steps to attach and manage object contexts, see [Use object contexts](https://docs.cloud.google.com/storage/docs/use-object-contexts).

## How object contexts work

You can attach contexts when you create or update objects, or you can let Google Cloud services attach them automatically.

In the [`objects` resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource), all object contexts appear under the [`contexts.custom`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#contexts.custom) field. Within `contexts.custom`, there are two types of contexts:

  * **Custom contexts without extended data** : Contexts that consist of a key, a string value, and timestamps. You can use these contexts to organize, filter, and track objects across your storage buckets.

  * **Custom contexts with extended data** ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): Contexts that consist of a key, a string value, timestamps, and an optional structured JSON payload. Google Cloud services attach these contexts during automated analysis, such as machine learning labeling.




### Context components

Each context entry consists of the following components:

  * **Key** : A unique identifier for the context on the object (up to 256 bytes). Keys starting with `google:` (for example, `google:annotation:face-detector-v1`) are reserved for Google-generated contexts. You can't create or update contexts with the `google:` prefix. To remove contexts with the `google:` prefix, you must discard them by using the `dropContextGroups` parameter during a rewrite operation.

  * **Value** : A string value associated with the key (up to 256 bytes) to control workflows and filter object listings.

  * **Timestamps** : Output-only timestamps (`createTime` and `updateTime`) indicating when the context was created and last modified.

  * **Extended data** ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): An optional structured JSON payload (up to 128 KiB) containing detailed information, such as machine learning labels or automated annotations.




Standard [`get`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) and [`list`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) requests return context keys, values, and timestamps. If a context has extended data, standard requests include an `extendedDataTypeUrl` field (`type.googleapis.com/google.protobuf.Struct`). To retrieve the full extended data payload, use the [`viewFullContext` method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).

For example, an object with custom contexts, both with and without extended data, has the following JSON representation:
    
    
    {
      "contexts": {
        "custom": {
          "customer_id": {
            "value": "cust-78901",
            "createTime": "2026-01-01T00:00:00.000Z",
            "updateTime": "2026-01-01T00:00:00.000Z"
          },
          "payment_status": {
            "value": "unpaid",
            "createTime": "2026-01-01T00:00:00.000Z",
            "updateTime": "2026-01-01T00:00:00.000Z"
          },
          "google:annotation:face-detector-v1": {
            "value": "SUCCESS",
            "createTime": "2026-09-29T17:20:00.000Z",
            "updateTime": "2026-09-29T17:20:00.000Z",
            "extendedDataTypeUrl": "type.googleapis.com/google.protobuf.Struct"
          }
        }
      }
    }

In this example:

  * `customer_id` and `payment_status` are custom contexts without extended data.
  * `google:annotation:face-detector-v1` is a Google-generated custom context with extended data.



All contexts can be retrieved and used to filter object listings by their keys and values.

## Use cases for object contexts

Object contexts let you classify, track, and enrich your data. The following sections describe the scenarios for using object contexts to manage different types of information.

### Group and classify objects

Classify and organize objects across buckets and projects. Use contexts to tag data by attributes, such as dataset origin, ownership, or cost center.

  * Example 1: Assign the context `data_classification: PII` to objects containing personally identifiable information (PII) so that compliance policies can handle them.

  * Example 2: Group new training images during ingestion by assigning `batch_id: 2025_Q4_Model_Run` context to enable efficient model testing and retrieval.




### Track workflows

To optimize custom workflows and prevent redundant operations, embed workflow state information directly onto objects to track their journey through a processing pipeline.

  * Example 1: Use `processing_status: awaiting_review` to indicate objects pending external release approval.

  * Example 2: Use `processed_by: analytics_pipeline` to prevent your custom data processing service from re-scanning files that have already completed a stage.




### Enrich objects with application-specific context

Attach specific information about an application or business process to provide additional context and data lineage for each object.

  * Example 1: For a satellite image, record capture details, such as `capture_angle: 45deg_NW`, or track the file's history with `lineage: ingested_from_s3`.

  * Example 2: Embed details about a file's contents, such as `document_type: service_manual` and `vehicle_model: f250`.




## Benefits of object contexts

Object contexts extend the capabilities of your Cloud Storage objects. By associating custom key-value pairs directly with stored objects, you can achieve the following benefits:

  * **Data discovery** : Filter object listings to limit inputs for your workloads to only the objects of interest.

  * **Interoperability** : Support interoperability with object tags from other cloud providers and help simplify migrations, as object contexts accept string values without predefinition.

  * **Data persistence** : Preserve context data across the object's lifecycle. When you copy, rewrite, compose, move, or restore objects, contexts are automatically transferred. You can also selectively discard contexts during copy, rewrite, and compose operations using the `dropContextGroups` query parameter (for example, `dropContextGroups=custom`) if you want to prevent them from carrying over to the destination object.

  * **Context modification control** : Define who can add, change, or remove contexts using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) permissions to maintain an audit trail.

  * **Batch operations** : Manage object contexts in bulk across billions of objects using [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).

  * **Bulk analysis with BigQuery** : Query and analyze object contexts and extended data (such as labels, face detections, and bounding boxes) across your storage buckets using the [Object Contexts Catalog view (`object_contexts_catalog_view`)](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#object-contexts-catalog-schema) in Storage Insights datasets.




## Pricing

For pricing details, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

## What's next

  * Learn how to [use object contexts](https://docs.cloud.google.com/storage/docs/use-object-contexts).
  * Learn how to [analyze object contexts in BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-contexts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
