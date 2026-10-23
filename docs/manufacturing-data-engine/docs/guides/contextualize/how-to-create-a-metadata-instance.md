---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/contextualize/how-to-create-a-metadata-instance/
title: Create metadata instances \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:02.501214+00:00
---

# Create metadata instances  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/contextualize/how-to-create-a-metadata-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create metadata instances

This guide describes how to create cloud metadata instances in _Metadata buckets_. Manufacturing Data Engine (MDE) provides two ways of creating metadata instances:

  1. Over the Metadata API or web interface (all buckets).
  2. Dynamically from parsers (record and tag buckets only).



## Before you begin

To complete this guide, you need the have already [created a metadata bucket](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-create-a-metadata-bucket).

## Metadata instances creation over the metadata API or Console

You can create metadata instances over the Metadata API or the MDE UI. You can use the API to load metadata instances into MDE from external sources and to populate lookup buckets with reference data.

Create a cloud metadata instance with the following instructions for REST API calls or the console:

### REST

`POST metadata/v1/buckets/BUCKET_NAME/BUCKET_VERSION/instances`
    
    
    {
        "naturalKey": "NATURAL_KEY",
        "instance": METADATA_INSTANCE_OBJECT
    }
    

Replace the following:

  * `BUCKET_NAME` with the name of the bucket in which to create a metadata instance.
  * `BUCKET_VERSION` with the version of the metadata bucket in which to create a metadata instance.
  * `NATURAL_KEY` with the natural key of the metadata instance. It must be `tagName` if `BUCKET_NAME` corresponds to a tag bucket. If `BUCKET_NAME` corresponds to a record bucket and the natural key is omitted, the natural key is automatically set to the hash of the value.
  * `METADATA_INSTANCE_OBJECT` with the metadata instance object. The metadata instance object must conform to the schema defined for the `BUCKET_NAME` and `BUCKET_VERSION`.



### Console

Open the **'CLOUD TAGS'** section of the top menu of the UI to create a **Metadata Instance**. The default view provides a list of the available **Tags** in the MDE instance:

![Metadata Section – list](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-tags-list.png)

The UI only supports editing Tag Metadata Buckets. Other Bucket types instances can only be created using the API. To create a **Tag Metadata Instance** :

  1. Click the **'ACTIONS'** icon in the selected **Tag** from the list.
  2. Select **'View / Edit'**.

![Tag Section – Edit Tag](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-tags-edit-tag.png)

  3. In the **'Edit Tag'** side menu, locate the **'Tag Metadata'** section to edit or add a new **Metadata Instance**.

  4. Click the **Badge** of the Bucket you want to implement. The attributes of the bucket appear underneath.

![Tag Section – Edit Tag Metadata](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-tags-edit-tag-tag-metadata.png)

  5. Modify the existing attributes or add new ones as needed. Those attributes are editable and can be modified.

  6. Add the selected values in each box of the form.

  7. After the instance is complete click the **'SAVE'**.

  8. The instance is then validated against the Bucket schema(s). If the validation is successful, the instance is stored and a success message is displayed. This instance becomes the current valid instance qualifying the new **Records** received for this Tag.




## Metadata instances creation dynamically from parsers

Metadata instances can be created dynamically from parsers when you use the `lookup by value` method of resolving metadata instance references. When you use the `lookup by value` method, and the latest metadata instance value for the provided natural key does not exist, MDE automatically creates a new metadata instance for the natural key from the instance object defined the in the proto record. See the documentation on [how to resolve metadata instance_id by instance value](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-link-records-to-metadata-instances#resolving_a_metadata_instance_id_by_instance_value) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
