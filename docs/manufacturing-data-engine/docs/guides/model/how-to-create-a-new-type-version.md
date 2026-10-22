---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-create-a-new-type-version/
title: Create a type version \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:58.067189+00:00
---

# Create a type version  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-create-a-new-type-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a type version

This guide describes how to create a new type version for an existing type in Manufacturing Data Engine (MDE).

## Before you begin

Before you begin creating a new type version for an existing type, you need to read about [how to create a type](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-create-a-type).

## Versioning restrictions

When creating new versions of a type, consider the following limitations:

**New versions may:**

  * Add new optional fields to the data schema.
  * Mark a required field optional in the data schema.
  * Add new metadata bucket references.



**New versions may not:**

  * Remove fields from the data schema.
  * Change data type of existing fields in the data schema.
  * Mark an an optional attribute required in the data schema.
  * Remove metadata bucket references.



## Create a new type version

You can create a new type version that associates a new metadata bucket to an existing type that already has an existing metadata bucket association and applies typical storage specifications using the API or the Console.

### REST

Execute the following REST API request:

`POST /configuration/v1/types/TYPE_NAME/versions`
    
    
    {
      "metadataBuckets": [
        {
          "bucketName": "EXISTING_BUCKET_NAME",
          "version": "EXISTING_BUCKET_VERSION"
        },
        {
          "bucketName": "NEW_BUCKET_NAME",
          "version": "NEW_BUCKET_VERSION"
        }
      ],
      "storageSpecs": [
        {
          "sink": "BIG_QUERY",
          "disabled": "false",
          "materializeCloudMetadata": "true"
        },
        {
          "sink": "BIG_TABLE",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "GCS",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "PUBSUB_PROTO",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "PUBSUB_JSON",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        }
      ]
    }
    

Replace the following:

  * `TYPE_NAME`: Name of the type for which a new version is created.
  * `EXISTING_BUCKET_NAME`: Name of the existing bucket already associated to this type.
  * `EXISTING_BUCKET_VERSION`: Version of the existing bucket already associated to this type.
  * `NEW_BUCKET_NAME`: Name of the new bucket.
  * `NEW_BUCKET_VERSION`: The version of the new bucket.



### Console

  1. To create a new **Type Version** using the Console open the **Types** section tab.

![Types section - list of Types](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-types-list.png)

  2. All available types in the MDE instance are listed in this section. The list exposes the basic configuration of each type, including:



  * **Name** : Unique name of the type. All types must have different unique names.
  * **Storage** : Displays the current storage specifications associated to the type.
  * **Archetype** : Shows the name of the archetype defining the type. Each type is associated to a unique archetype. The archetype association can't be modified after the type is created.
  * **Version** : Version number of the type. A type can be versioned. The default view in this list only displays the latest version available for the type. It's possible to show earlier versions by un-checking the **Show Latest** check-box.
  * **Metadata** : Renders a color-coded badge for each metadata bucket associated to the type. Tag metadata buckets are differentiated from record metadata buckets using a specific icon inside the badge. 
    * **Transformations** : Displays a badge for each transformation type associated to the type.
  * **Enabled** : Displays a `true` value if the type is enabled and a `false` value if it is not. Users can enable or disable types at any time.
  * **Active** : When types are created take a certain time to provision. While types are being provisioned, their active status is `false`. When they are ready they show as `true`.


  1. To create a new **Type Version** in this web interface, click the **Actions** icon and click **Create New Version**. The following form will appear:

![Types section - list of types](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-types-create-new-verion.png)

  2. The **Create New Type Version** opens displaying a form to modify the settings of the selected **type** :

![Types section - list of types](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-types-create-new-type-version.png)




The top section of the form displays the name and archetype of the type. Those attributes can't me modified. Only changing the metadata specification or modifying the data schema will trigger a new type version. Modifying the rest of the type parameters will update the type but won't require a new version.

Both metadata specification and data schema can be modified by adding new elements. However all new type versions need to be backward compatible. It isn't possible to remove metadata buckets to create a new version of the type. It's possible to add new metadata buckets by opening the **Metadata Bucket** section.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
