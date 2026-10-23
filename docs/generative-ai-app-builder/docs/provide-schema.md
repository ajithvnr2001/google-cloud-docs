---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema/
title: Provide or auto-detect a schema \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:52.141781+00:00
---

# Provide or auto-detect a schema  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Provide or auto-detect a schema Stay organized with collections  Save and categorize content based on your preferences. 

When you import structured data using the Google Cloud console, Agent Search auto-detects the schema. You can either use this auto-detected schema in your engine or use the API to provide a schema to indicate the structure of the data.

If you provide a schema and later update it with a new schema, the new schema must be backward compatible with the original. Otherwise, the schema update fails.

**Important:** If you don't provide a schema, the auto-detect feature can update your schema by incorporating any newly detected fields when you import new data. If any documents in your imported data contain new fields that are not backward compatible with your original schema, those documents fail to import.

For reference information about the schema, see [`dataStores.schemas`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas).

**Key Terms:** In the context of schema, the terms _field_ and _property_ are used interchangeably. 

To see an example of custom attributes by url pattern, run the "Custom attributes by URL pattern" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/custom_attributes_by_url_pattern.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/custom_attributes_by_url_pattern.ipynb)

## Approaches to providing the schema for your data store

There are various approaches to determining the schema for structured data.

  * **Auto-detect and edit.** Let Agent Search auto-detect and suggest an initial schema. Then, you refine the schema through the console interface. Google highly recommends that, after your fields are auto-detected, you map key properties to all the important fields.

This is the approach that you'll use when following the Google Cloud console instructions for structured data in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es) and [Create a custom recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).

  * **Provide the schema as a JSON object.** Provide the schema to Agent Search as a JSON object. You need to have prepared a correct JSON object. For an example of a JSON object, see Example schema as a JSON object. After creating the schema, you upload your data according to that schema.

This is the approach that you can use when creating a data store through the API using a curl command (or program). For example, see [Import once from BigQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#bq-import-once). Also see the following instructions, Provide your own schema.

  * **Media: Provide your data in the Google-defined schema.** If you create a data store for media, you can choose to use the Google predefined schema. Choosing this option assumes that you have structured your JSON object in the format given in [About media documents and data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#json-schema). By default, auto-detect appends to the schema any new fields that it finds during data ingestion.

This is the approach that you use when following the instructions in [Create a media app and a data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media). It is also the approach in the tutorials, [Get started with media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations) and [Get started with media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-search), where the sample data is provided in the Google predefined schema.

  * **Media: Auto-detect and edit, making sure to include the required media properties.** For media data, you can use auto-detect to suggest the schema and edit to refine it. In your JSON object, you must include fields that can be mapped to the media key properties: `title`, `uri`, `category`, `media_duration`, and `media_available_time`.

This is the approach that you'll use when importing media data through the Google Cloud console if the media data is not in the Google-defined schema.

  * **Media: Provide your own schema as a JSON object.** Provide the schema to Agent Search as a JSON object. You need to have prepared a correct JSON object. The schema must include fields that can be mapped to the media key properties: `title`, `uri`, `category`, `media_duration`, and `media_available_time`.

For an example of a JSON object, see Example schema as a JSON object. After creating the schema, you upload the your media data according to that schema.

For this approach, you use the API through a curl command (or program). See the following instructions, Provide your own schema.




## About auto-detect and edit

When you begin importing data, Agent Search samples the first few documents that are imported. Based on these documents, it proposes a schema for the data, which you can then review or edit.

If fields that you want to map to key properties aren't present in the sampled documents, then you can manually add these fields when you review the schema.

**Tip:** Make sure that the documents at the beginning of your dataset are good quality—that all the key fields are represented. That way, you don't have to add or edit fields later.

If Agent Search encounters additional fields later in the data import, it still imports these fields and adds them to the schema. If you want to edit the schema after all the data has been imported, see [Update your schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas#discoveryengine_v1_generated_SchemaService_UpdateSchema_sync-console).

## Example schema as a JSON object

You can define your own schema using the [JSON Schema](https://json-schema.org/) format, which is an open source, declarative language to define, annotate, and validate JSON documents. For example, this is a valid JSON schema annotation:
    
    
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object",
      "dynamic": "true",
      "datetime_detection": true,
      "geolocation_detection": true,
      "properties": {
        "title": {
          "type": "string",
          "keyPropertyMapping": "title",
          "retrievable": true,
          "completable": true
        },
        "description": {
          "type": "string",
          "keyPropertyMapping": "description"
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "string",
            "keyPropertyMapping": "category"
          }
        },
        "uri": {
          "type": "string",
          "keyPropertyMapping": "uri"
        },
        "brand": {
          "type": "string",
          "indexable": true,
          "dynamicFacetable": true
        },
        "location": {
          "type": "geolocation",
          "indexable": true,
          "retrievable": true
        },
        "creationDate": {
          "type": "datetime",
          "indexable": true,
          "retrievable": true
        },
        "isCurrent": {
          "type": "boolean",
          "indexable": true,
          "retrievable": true
        },
        "runtime": {
          "type": "string",
          "keyPropertyMapping": "media_duration"
        },
        "releaseDate": {
          "type": "string",
          "keyPropertyMapping": "media_available_time"
        }
      }
    }

If you are defining a media schema, you must include fields that can be mapped to the media key properties. These key properties are shown in this example.

Here are some of the fields in this schema example:

  * **`dynamic`**. If `dynamic` is set to the string value `"true"`, then any new properties found in the imported data is added to the schema. If `dynamic` is set to `"false"`, new properties found in imported data are ignored; the properties are not added to the schema nor are the values are imported.

For example, a schema has two properties: `title` and `description`, and you upload a data that contains properties for `title`, `description`, and `rating`. If `dynamic` is `"true"`, then the ratings property and data are imported. If `dynamic` is `"false"`, then `rating` properties are not imported, although `title` and `description` are.

The default is `"true"`.

  * **`datetime_detection`**. If `datetime_detection` is set to the boolean `true`, then, when data in datetime format are imported, the schema type is set to `datetime`. The supported formats are [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

For example:

    * `2024-08-05 08:30:00 UTC`

    * `2024-08-05T08:30:00Z`

    * `2024-08-05T01:30:00-07:00`

    * `2024-08-05`

    * `2024-08-05T08:30:00+00:00`

If `datatime_detection` is set to the boolean `false`, then, when data in datetime format are imported, the schema type is set to `string`.

The default is `true`.

  * **`geolocation_detection`**. If `geolocation_detection` is set to the boolean `true`, then, when data in geolocation format are imported, the schema type is set to `geolocation`. Data is detected as geolocation if it is an object containing a latitude number and a longitude number or an object containing an address string.

For example:

    * `"myLocation": {"latitude":37.42, "longitude":-122.08}`

    * `"myLocation": {"address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043"}`

If `geolocation_detection` is set to the boolean `false`, then, when data in geolocation format are imported, the schema type is set to `object`.

The default is `true`.

  * **`keyPropertyMapping`**. A field that maps predefined keywords to critical fields in your documents, helping to clarify their semantic meaning. Values include `title`, `description`, `uri`, `category`, `update_time`, and `create_time`. Your field name doesn't need to match the `keyPropertyValues` value. For example, for a field that you named `my_title`, you can include a `keyPropertyValues` field with a value of `title`.

For search data stores, fields marked with `keyPropertyMapping` are by default indexable and searchable, but not retrievable, completable, or dynamicFacetable. This means that you don't need to include the `indexable` or `searchable` fields with a `keyPropertyValues` field to get the expected default behavior.

Key properties can improve the quality of search and recommendations results and search autocomplete accuracy. If you use auto-schema detection, it doesn't automatically map key properties and you must [manually add the mapping](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas#update-schema).

Mapping a document field to `update_time` (or `create_time` as a fallback) is required for the `document_age` custom ranking signal. For more information about `document_age`, see [Standard signal](https://docs.cloud.google.com/generative-ai-app-builder/docs/custom-ranking#signals).

  * **`type`**. The type of the field. This is a string value that is `datetime`, `geolocation` or one of the primitive types (`integer`, `boolean`, `object`, `array`, `number`, or `string`).




The following property fields apply only for search apps:

  * **`retrievable`**. Indicates whether this field can be returned in a search response. This can be set for fields of type `number`, `string`, `boolean`, `integer`, `datetime`, and `geolocation`. A maximum of 50 fields can be set as retrievable. User-defined fields and `keyPropertyValues` fields are not retrievable by default. To make a field retrievable, include `"retrievable": true` with the field.

  * **`indexable`**. Indicates whether this field can be filtered, faceted, boosted, or sorted in the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/search) method. This can be set for fields of type `number`, `string`, `boolean`, `integer`, `datetime`, and `geolocation`. A maximum of 50 fields can be set as indexable. User-defined fields are not indexable by default, except for fields containing the `keyPropertyMapping` field. To make a field indexable, include `"indexable": true` with the field.

  * **`dynamicFacetable`**. Indicates that the field can be used as a dynamic facet. This can be set for fields of type `number`, `string`, `boolean`, and `integer`. To make a field dynamically facetable, it must also be indexable: include `"dynamicFacetable": true` and `"indexable": true` with the field.

  * **`searchable`**. Indicates whether this field can be reverse indexed to match unstructured text queries. This can only be set for fields of type `string`. A maximum of 50 fields can be set as searchable. User-defined fields are not searchable by default, except for fields containing the `keyPropertyMapping` field. To make a field searchable, include `"searchable": true` with the field.

  * **`completable`**. Indicates whether this field can be returned as an autocomplete suggestion. This can only be set for fields of type `string`. To make a field completable, include `"completable": true` with the field.




Additionally, the following field applies only for recommendations apps:

  * **`recommendationsFilterable`**. Indicates that the field can be used in a recommendations filter expression. For general information about filtering recommendations, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations).
        
        ...
            "genres": {
            "type": "string",
            "recommendationsFilterable": true,
            ...
          },


**Note:** For auto-detected schemas, newly detected fields are automatically indexable, searchable, and retrievable, as long as they follow the type requirements and stay within the maximum limits.

To see an example of unstructured documents with metadata, run the "Unstructured documents with metadata" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/ingesting_unstructured_documents_with_metadata.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/ingesting_unstructured_documents_with_metadata.ipynb)

## Provide your own schema as a JSON object

To provide your own schema, you create a data store that contains an empty schema and then you update the schema, supplying your schema as a JSON object. Follow these steps:

  1. Prepare the schema as a JSON object, using the Example schema as a JSON object as a guide.

  2. Create a data store.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
         -d '{
           "displayName": "DATA_STORE_DISPLAY_NAME",
           "industryVertical": "INDUSTRY_VERTICAL"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DATA_STORE_DISPLAY_NAME`: the display name of the Agent Search data store that you want to create.
     * `INDUSTRY_VERTICAL`: `GENERIC` or `MEDIA`
  3. Use the [schemas.patch](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas/patch) API method to provide your new JSON schema as a JSON object.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/schemas/default_schema" \
         -d '{
           "structSchema": JSON_SCHEMA_OBJECT
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `JSON_SCHEMA_OBJECT`: your new JSON schema as a JSON object. For example:
           
           {
             "$schema": "https://json-schema.org/draft/2020-12/schema",
             "type": "object",
             "properties": {
               "title": {
                 "type": "string",
                 "keyPropertyMapping": "title"
               },
               "categories": {
                 "type": "array",
                 "items": {
                   "type": "string",
                   "keyPropertyMapping": "category"
                 }
               },
               "uri": {
                 "type": "string",
                 "keyPropertyMapping": "uri"
               }
             }
           }

#### Example command and result
           
           curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema" -d '{
           "structSchema": {
           "$schema": "https://json-schema.org/draft/2020-12/schema",
           "type": "object",
           "properties": {
           "title": {
           "type": "string",
           "keyPropertyMapping": "title"
           },
           "categories": {
           "type": "array",
           "items": {
           "type": "string",
           "keyPropertyMapping": "category"
           }
           },
           "uri": {
           "type": "string",
           "keyPropertyMapping": "uri"
           }
           }
           }
           }'
           
           
           * * *
           
           
           {
           "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema/operations/update-schema-10569824819404198922",
           "metadata": {
           "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.UpdateSchemaMetadata"
           }
           }
           

  4. Optional: Review the schema by following the procedure [View a schema definition](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition).




## What's next

  * [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es)
  * [Create a recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app)
  * [Create a media app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media)
  * [Get the schema definition for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition)
  * [Update a schema for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
