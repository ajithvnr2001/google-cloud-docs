---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-create-a-metadata-bucket-version/
title: Create a metadata bucket version \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:06.181622+00:00
---

# Create a metadata bucket version  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-create-a-metadata-bucket-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a metadata bucket version

This guide describes how to create a new metadata bucket version for an existing bucket in Manufacturing Data Engine (MDE).

Metadata bucket versions lets you evolve the bucket schema. Types and parsers always reference a specific bucket version, so when you create a new version, it doesn't affect the existing data processing pipelines. You must upgrade your types and parsers or create new types and parsers to use the new bucket version. You can create a metadata bucket version using the configuration API or MDE web interface.

## Before you begin

This guide requires you have already created a [metadata bucket](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-create-a-metadata-bucket) for the MDE.

## Versioning restrictions

When creating new versions of a bucket, consider the following limitations:

**New versions may:**

  * Add new optional fields.
  * Mark a required field optional.



**New versions may not:**

  * Remove fields.
  * Change data type of existing fields.
  * Mark an an optional attribute required.



## Create a new metadata bucket version

You can create a metadata bucket version using the terminal or the console.

### REST

Execute the following REST API request:

`POST /metadata/v1/buckets/BUCKET_NAME/versions`
    
    
    {
      "schema": "BUCKET_SCHEMA",
      "provider": "local"
    }
    

Replace the following:

  * `BUCKET_NAME`: Name of the bucket to be created.
  * `BUCKET_TYPE`: Type of the bucket to be created. Must be one of `TAG`, `RECORD`, or `LOOKUP`. The `natural_key` of a metadata instance in a `TAG` bucket must be a tag name. The `natural_key` of a metadata instance in a `RECORD` bucket can be any key. The `natural_key` of a metadata instance in a `LOOKUP` bucket can be any key, but records can't reference instances in a lookup bucket, and the instances are not written to any data sink. Lookup buckets only serve as source of reference data that can be retrieved by a parser using the Whistle function `lookupByKey` and used to enrich records.
  * `BUCKET_SCHEMA`: JSON schema of the bucket. The schema constrains the instances that may be created in the bucket.
  * `INSTANCE_OVERWRITE_MODE`: Either `TRUE` or `FALSE`. Determines whether new instances are created by merging the provided instance with the latest instance for a given natural key or if new instances are created as provided.



### Console

  1. To create a **new metadata bucket version** click **Create New Version** from the **METADATA** section of the **Cloud Management MC** web interface:

![Types section - list of Types](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-metadata-create-new-version-menu.png)

  2. A configuration panel is displayed with a form to update the parameters of the new **metadata bucket version** :

![Types section - list of Types](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-metadata-new-bucket-version.png)

Only **backward compatible** changes are allowed for new versions. New, breaking, and changes requires creating a new bucket. In the panel you can update the following:

     * **Instance update mode** : Change the instance ingestion behavior of the bucket.
     * **Metadata schema** : Add new attributes to the existing schema of the bucket.
  3. After the changes are implemented, click **CREATE** to save the new version of the metadata bucket. 

  4. An error message is displayed if the change is unsuccessful. A success message is shown if the change is successful. The new version number is sequential and is automatically assigned to the bucket.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
