---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents/
title: About media documents and data stores \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:27.978569+00:00
---

# About media documents and data stores  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  About media documents and data stores Stay organized with collections  Save and categorize content based on your preferences. 

Builder for media. 

This page provides information about documents and data stores for media. If you're using media recommendations or media search, review the schema requirements for your documents and data stores on this page before uploading your data.

## Overview

A document is any item that you upload into an Agent Search data store. For media, a document typically contains metadata information about media content, such as videos, news articles, music files, or podcasts. The `Document` object in the API captures this metadata information.

Your data store contains a collection of documents that you have uploaded. When you create a data store, you specify that it will contain media documents. Data stores for media can only be attached to media apps, not to other app types such as custom search and recommendations. Data stores are represented in the API by the `DataStore` resource.

The quality of the data that you upload has a direct effect on the quality of the results that media apps provide. In general, the more accurate and specific information you can provide, the higher quality your results.

The data that you upload to the data store must be formatted in a specific JSON schema. The data arranged in that schema must be in a BigQuery table, a file or set of files in Cloud Storage, or in a JSON object that can be uploaded directly using the Google Cloud console.

## Google predefined schema versus custom schema

You have two options for your media data schema:

  * **The Google predefined schema.** If you haven't already designed a schema for your media data, the Google predefined schema is a good choice.

  * **Your own schema.** If you have your data already formatted in a schema, you can use your own schema. For more information, see Custom schema below.




With either option, you can add fields to the schema after the initial data import. However, with the Google predefined schema, for the initial import, your data field names and types must exactly match those in the Document fields tables.

## Key properties

Properties are used to train the models for search and recommendations. Property fields represent all fields in your schema.

_Key properties_ are a special fixed set of properties in the Google schema. The key properties identify important information that is used to understand semantic meanings of the data.

If you use a custom schema, make sure to map your fields to as many of the key properties as possible. You do the mapping in the Google Cloud console after importing the data; see [Create a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media).

## Google predefined JSON Schema for `Document`

When using media, documents can use the Google predefined JSON schema for media.

Documents are uploaded with either a JSON or Struct data representation. Make sure the document JSON or Struct conforms to the following JSON schema. The JSON schema uses [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/release-notes.html) for validation. For more about JSON Schema, also see the [JSON Schema specification documentation](https://json-schema.org/specification.html) at json-schema.org.
    
    
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
        },
        "description": {
          "type": "string",
        },
        "media_type": {
          "type": "string",
        },
        "language_code": {
          "type": "string",
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "uri": {
          "type": "string",
        },
        "images": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "uri": {
                "type": "string",
              },
              "name": {
                "type": "string",
              }
            },
          }
        },
        "in_languages": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "country_of_origin": {
          "type": "string",
        },
        "transcript": {
          "type": "string",
        },
        "content_index": {
          "type": "integer",
        },
        "persons": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
              },
              "role": {
                "type": "string",
              },
              "custom_role": {
                "type": "string",
              },
              "rank": {
                "type": "integer",
              },
              "uri": {
                "type": "string",
              }
            },
            "required": ["name", "role"],
          }
        },
        "organizations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
              },
              "role": {
                "type": "string",
              },
              "custom_role": {
                "type": "string",
              },
              "rank": {
                "type": "integer",
              },
              "uri": {
                "type": "string",
              }
            },
            "required": ["name", "role"],
          }
        },
        "hash_tags": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "filter_tags": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "duration": {
          "type": "string",
        },
        "content_rating": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "aggregate_ratings": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "rating_source": {
                "type": "string",
              },
              "rating_score": {
                "type": "number",
              },
              "rating_count": {
                "type": "integer",
              }
            },
            "required": ["rating_source"],
          }
        },
        "available_time": {
          "type": "datetime",
        },
        "expire_time": {
          "type": "datetime",
        },
        "live_event_start_time": {
          "type": "datetime",
        },
        "live_event_end_time": {
          "type": "datetime",
        },
        "production_year": {
          "type": "integer",
        }
      },
      "required": ["title", "categories", "uri", "available_time"],
    }

## Sample JSON `Document` object

The following example shows an example of a JSON `Document` object.
    
    
    {
      "title": "Test document title",
      "description": "Test document description",
      "media_type": "sports-game",
      "in_languages": [
        "en-US"
      ],
      "language_code": "en-US",
      "categories": [
        "sports > clip",
        "sports > highlight"
      ],
      "uri": "http://www.example.com",
      "images": [
        {
          "uri": "http://example.com/img1",
          "name": "image_1"
        }
      ],
      "country_of_origin": "US",
      "content_index": 0,
      "transcript": "Test document transcript",
      "persons": [
        {
          "name": "sports person",
          "role": "player",
          "rank": 0,
          "uri": "http://example.com/person"
        },
      ],
      "organizations": [
        {
          "name": "sports team",
          "role": "team",
          "rank": 0,
          "uri": "http://example.com/team"
        },
      ],
      "hash_tags": [
        "tag1"
      ],
      "filter_tags": [
        "filter_tag"
      ],
      "duration": "100s",
      "production_year": 1900,
      "content_rating": [
        "PG-13"
      ],
      "aggregate_ratings": [
        {
          "rating_source": "imdb",
          "rating_score": 4.5,
          "rating_count": 1250
        }
      ],
      "available_time": "2022-08-26T23:00:17Z"
    }

## Document fields

This section lists the field values you provide when you create documents for your data store. The values should correspond to the values used in your internal document database, and should accurately reflect the item represented.

### `Document` object fields

The following fields are top-level fields for the `Document` object. Also refer to these fields on the [`Document` reference page](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents).

Field name | Notes  
---|---  
`name` |  The full, unique resource name of the document. Required for all `Document` methods except for `create` and `import`. During import, the name is automatically generated and does not need to be manually provided.   
`id` |  The document ID used by your internal database. The ID field must be unique across your entire data store. The same value is used when you record a user event, and is also returned by the `recommend` and `search` methods.   
`schemaId` |  Required. The identifier of the schema located in the same data store. Should be set as "default_schema", which is automatically created when the default data store is created.   
`parentDocumentId` |  The ID of the parent document. For top-level (root) documents, `parent_document_id` can be empty or can point to itself. For child documents, `parent_document_id` should point to a valid root document.   
  
### Property fields

The following fields are defined using the predefined JSON Schema format for media.

For more information about JSON properties, see the Understanding JSON Schema documentation for [properties](https://json-schema.org/understanding-json-schema/reference/object.html) at json-schema.org.

The following table defines flat fields

Field name | Notes  
---|---  
`title` |  String - required  Document title from your database. A UTF-8 encoded string. Limited to 1000 characters.   
`categories` |  String - required Document categories. This property is repeated for supporting one document belonging to several parallel categories. Use the full category path for higher quality results.  To represent the full path of a category, use the `>` symbol to separate hierarchies. If `>` is part of the category name, replace it with another character(s).  For example:  ` "categories": [ "sports > highlight" ] ` A document can contain at most 250 categories. Each category is a UTF-8 encoded string with a length limit of 5000 characters.   
`uri` |  String - required  URI of the document. Length limit of 5000 characters.   
`description` |  String - highly recommended  Description of the document. Length limit of 5000 characters.   
`media_type` |  String - this field is required for movies and shows  Top-level category.  Supported types: `movie`, `show`, `concert`, `event`, `live-event`, `broadcast`, `tv-series`, `episode`, `video-game`, `clip`, `vlog`, `audio`, `audio-book`, `music`, `album`, `articles`, `news`, `radio`, `podcast`, `book`, and `sports-game`.  The values `movie` and `show` have special significance. They cause documents to be enriched in a way that improves ranking and helps users making title searches to find alternate content they might be interested in.   
`language_code` |  String - optional  Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  For document search this field is in use. It defaults to `en-US` if unset. For example, `"language_code": "en-US"`.  For media, such as movies, that have metadata in multiple languages, treat each language version as a separate document; each version has its own title, description, categories, and other property fields in the corresponding language. To distinguish between different language versions, use the `language_code` property. This property also lets you filter search results on the serving side, so that only media content in the relevant language is returned for a query.   
`duration` |  String - required for media recommendations apps where the business objective is click-through rate (CVR) or watch duration per session.  Duration of the media content. Duration should be encoded as a string. Encoding should be the same as the `google::protobuf::Duration` JSON string encoding. For example: "5s", "1m"   
`available_time` |  Datetime - required The time that the content is available to the end-users. This field identifies the freshness of a content for end-users. The timestamp should conform to RFC 3339 standard.  For example:  ` "2022-08-26T23:00:17Z" ` To filter on availability, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations#restrictions) and [Filter for available documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search#availability).   
`expire_time` |  Datetime - optional The time that the content will expire for the end-users. This field identifies the freshness of a content for end-users. The timestamp should conform to RFC 3339 standard.  For example:  ` "2032-12-31T23:00:17Z" ` To exclude expired documents from results, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations) and [Filter media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search#availability).   
`live_event_start_time` |  Datetime - optional The time that the live event begins. The timestamp should conform to RFC 3339 standard.  For example:  ` "2020-12-31T23:00:17Z" `  
`live_event_end_time` |  Datetime - optional The time that the live event is finished. The timestamp should conform to RFC 3339 standard.  For example:  ` "2024-01-28T23:00:17Z" `  
`in_languages` |  String - optional - repeated  Language of the media contents. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  For example: `"in_languages": [ "en-US"]`  
`country_of_origin` |  String - optional  Media document country of origin. Length limit of 128 characters.  For example: `"country_of_origin": "US"`  
`transcript` |  String - optional  Transcript of the media document.   
`content_index` |  Integer - optional  Content index of the media document. Content index field can be used to order the documents relative to others. For example, episode number can be used as the content index.  Content index should be a non-negative integer.  For example: `"content_index": 0`  
`filter_tags` |  String - optional - repeated  Filter tags for the document. At most 250 values are allowed per document with a length limit of 1000 characters. Otherwise, an INVALID_ARGUMENT error is returned.  These tags can be used to filter search results and recommendations results. To filter recommendations results, pass the tags as part of the `RecommendRequest.filter`. The tags are only used to filter returned results; the values of the tags don't affect the results that are returned by the search and recommendations models.  For example: `"filter_tags": [ "grade_level", "season"]`  
`hash_tags` |  String - optional - repeated  Hashtags for the document. At most 100 values are allowed per document, with a length limit of 5000 characters.  For example: `"hash_tags": [ "soccer", "world cup"]`  
`production_year` |  Integer - optional  The year the media was produced.   
`content_rating` |  String - optional - repeated  The content rating, used for content advisory systems and content filtering based on the audience. At most 100 values are allowed per document with a length limit of 128 characters.  This tag can be used to filter recommendations results by passing the tag as part of the `RecommendRequest.filter`.  For example: `content_rating: ["PG-13"]`  
  
The following table defines hierarchical fields.

Field name | Notes  
---|---  
`images` |  Object - optional - repeated  Root key property for encapsulating image-related properties.   
`images.uri` |  String - optional URI of the image. Length limit of 5,000 characters.   
`images.name` |  String - optional  Name of the image. Length limit of 128 characters.   
`persons` |  Object - optional - repeated  Root key property for encapsulating the person-related properties.  For example: `"persons":[{"name":"sports person","role":"player","rank":0,"uri":"http://example.com/person"}]`  
`persons.name` |  String - required Name of the person.   
`persons.role` |  String - required  The role of the person in the media item.  Supported values: director, actor, player, team, league, editor, author, character, contributor, creator, editor, funder, producer, provider, publisher, sponsor, translator, music-by, channel, custom-role  If none of the supported values are applied to `role`, set `role` to `custom-role` and provide the value in the `custom_role` field.   
`persons.custom_role` |  String - optional  `custom_role` is set if and only if the `role` is set to be a `custom-role`. Must be a UTF-8 encoded string with a length limit of 128 characters. Must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`.   
`persons.rank` |  Integer - optional  Used for role ranking. For example, for first actor, `role = "actor", rank = 1`  
`persons.uri` |  String - optional  URI of the person.   
`organizations` |  Object - optional - repeated  Root key property for encapsulating the `organization`-related properties.  For example: `"organizations ":[{"name":"sports team","role":"team","rank":0,"uri":"http://example.com/team"}]`  
`organizations.name` |  String - required  Name of the organization.   
`organizations.role` |  String - required  The role of the organization in the media item.  Supported values: director, actor, player, team, league, editor, author, character, contributor, creator, editor, funder, producer, provider, publisher, sponsor, translator, music-by, channel, custom-role  If none of the supported values are applied to `role`, set `role` to `custom-role` and provide the value in the `custom_role` field.   
`organizations.custom_role` |  String - optional  `custom_role` is set if and only if the `role` is set to be a `custom-role`. Must be a UTF-8 encoded string with a length limit of 128 characters. Must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`.   
`organizations.rank` |  String - optional  Used for role ranking. For example, for first publisher: `role = "publisher", rank = 1`  
`organizations.uri` |  String - optional  URI of the organization.   
`aggregate_ratings` |  Object - optional - repeated  Root key property for encapsulating the `aggregate_rating` related properties.   
`aggregate_ratings.rating_source` |  String - required  The source for rating. For example, `imdb` or `rotten_tomatoes`. Must be a UTF-8 encoded string with a length limit of 128 characters. Must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`.   
`aggregate_ratings.rating_score` |  Double - required  The aggregated rating. The rating should be normalized to the [1, 5] range.   
`aggregate_ratings.rating_count` |  Integer - optional  The number of individual reviews. Should be a non-negative value.   
  
## Document levels

Document levels determine the hierarchy in your data store. Typically, you should have a single-level data store or a two-level data store. Only two layers are supported.

For example, you can have a single-level data store where each document is an individual item. Alternatively, you might choose a two-level data store that contains both groups of items and individual items.

### Document level types

There are two document level types:

  * **Parent.** Parent documents are what Agent Search

returns in recommendations and searches. Parents can be individual documents or groups of similar documents. This level type is recommended.

  * **Child.** Child documents are versions of a group's parent document. Children can only be individual documents. For example, if the parent document is "Example TV Show", children could be "Episode 1" and "Episode 2". This level type can be difficult to configure and maintain, and is not recommended.




## About data store hierarchy

When planning your data store hierarchy, decide if your data store should contain only parents or parents and children. The key point to remember is that recommendations and searches only return parent documents.

For example, a parent-only data store might work well for audiobooks, where a recommendations panel returns a selection of individual audiobooks. On the other hand, if you uploaded TV show episodes as parent documents to a parent-only data store, several out-of-order episodes could be recommended in the same panel.

A TV show data store could work with both parents and children, where each parent document represents a TV show with child documents that represent the episodes of that TV show. This two-level data store allows the recommendations panel to show a range of similar TV shows. The end-user can click a particular show to select an episode to watch.

Because parent-child hierarchies can be difficult to configure and maintain, parent-only data stores are recommended.

For example, a TV show data store can work well as a parent-only data store where each parent document represents a TV show that can be recommended, and individual episodes are not included (and therefore not recommended).

If you determine that your data store needs to have both parents and children, that is, groups and singular items, but you only have singular items now, you need to create parents for the groups. The minimum information that you need to provide for a parent is `id`, `title`, and `categories`. For more information, see the section Document fields.

## BigQuery schema for media

If you plan to import your documents from BigQuery, use the predefined BigQuery schema to create a BigQuery table with the correct format and load it with your documents data before you [import your documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).
    
    
    [
      {
        "name": "id",
        "mode": "REQUIRED",
        "type": "STRING",
        "fields": []
      },
      {
        "name": "schemaId",
        "mode": "REQUIRED",
        "type": "STRING",
        "fields": []
      },
      {
        "name": "parentDocumentId",
        "mode": "NULLABLE",
        "type": "STRING",
        "fields": []
      },
      {
        "name": "jsonData",
        "mode": "NULLABLE",
        "type": "STRING",
        "fields": []
      }
    ]

## Custom schema

If you have your data already formatted in a schema, you might decide not to use the Google predefined schema described above. Instead, you can use your own schema and map fields from your schema to media key properties. To map your schema when you [create the data media store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media), use the Google Cloud console.

If you use your own schema, you must have fields in your schema that can be mapped to the following five key properties for media:

Required key property name | Notes  
---|---  
`title` |  String - required  Document title from your database. A UTF-8 encoded string. Limited to 1000 characters.   
`uri` |  String - required  URI of the document. Length limit of 5000 characters.   
`categories` |  String - required Document categories. This property is repeated for supporting one document belonging to several parallel categories. Use the full category path for higher quality results.  To represent the full path of a category, use the `>` symbol to separate hierarchies. If `>` is part of the category name, replace it with another character(s).  For example:  ` "categories": [ "sports > highlight" ] ` A document can contain at most 250 categories. Each category is a UTF-8 encoded string with a length limit of 5000 characters.   
`media_available_time` |  Datetime - required The time that the content is available to the end-users. This field identifies the freshness of a content for end-users. The timestamp should conform to RFC 3339 standard.  For example:  ` "2022-08-26T23:00:17Z" ` To filter on availability, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations#restrictions) and [Filter for available documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search#availability).   
`media_duration` |  String - required for media recommendations apps where the business objective is click-through rate (CVR) or watch duration per session.  Duration of the media content. Duration should be encoded as a string. Encoding should be the same as the `google::protobuf::Duration` JSON string encoding. For example: "5s", "1m"  This field is important for media recommendations apps where the business objective is to maximize the conversion rate (CVR) or the watch duration per visitor.   
  
Additionally, there are key properties that are not required, but for quality results, map as many of these as you can to your schema.

These key properties are as follows:

Key property name | Notes  
---|---  
`description` |  String - highly recommended  Description of the document. Length limit of 5000 characters.   
`image` |  Object - optional - repeated  Root key property for encapsulating image-related properties.   
`image_name` |  String - optional  Name of the image. Length limit of 128 characters.   
`image_uri` |  String - optional URI of the image. Length limit of 5,000 characters.   
`language_code` |  String - optional  Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  For document recommendations, this field is ignored and the text language is detected automatically. The document can include text in different languages, but duplicating documents to provide text in multiple languages can result in degraded performance.  For document search this field is in use. It defaults to `en-US` if unset. For example, `"language_code": "en-US"` For media, such as movies, that have metadata in multiple languages, treat each language version as a separate document; each version has its own title, description, categories, and other property fields in the corresponding language. To distinguish between different language versions, use the `language_code` property. This property also lets you filter search results on the serving side, so that only media content in the relevant language is returned for a query.   
`media_aggregated_rating` |  Object - optional - repeated  Root key property for encapsulating the `aggregate_rating` related properties.   
`media_aggregated_rating_count` |  Integer - optional  The number of individual reviews. Should be a non-negative value.   
`media_aggregated_rating_score` |  Double - required  The aggregated rating. The rating should be normalized to the [1, 5] range.   
`media_aggregated_rating_source` |  String - required  The source for rating. For example, `imdb` or `rotten_tomatoes`. Must be a UTF-8 encoded string with a length limit of 128 characters. Must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`.   
`media_content_index` |  Integer - optional  Content index of the media document. Content index field can be used to order the documents relative to others. For example, episode number can be used as the content index.  Content index should be a non-negative integer.  For example: `"content_index": 0`  
`media_content_rating` |  String - optional - repeated  The content rating, used for content advisory systems and content filtering based on the audience. At most 100 values are allowed per document with a length limit of 128 characters.  This tag can be used to filter recommendations results by passing the tag as part of the `RecommendRequest.filter`.  For example: `content_rating: ["PG-13"]`  
`media_country_of_origin` |  String - optional  Media document country of origin. Length limit of 128 characters.  For example: `"country_of_origin": "US"`  
`media_expire_time` |  Datetime - optional The time that the content will expire for the end-users. This field identifies the freshness of a content for end-users. The timestamp should conform to RFC 3339 standard.  For example:  ` "2032-12-31T23:00:17Z" ` To exclude expired documents from results, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations) and [Filter media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search#availability).   
`live_event_start_time` |  Datetime - optional The time that the live event begins. The timestamp should conform to RFC 3339 standard.  For example:  ` "2020-12-31T23:00:17Z" `  
`live_event_end_time` |  Datetime - optional The time that the live event is finished. The timestamp should conform to RFC 3339 standard.  For example:  ` "2024-01-28T23:00:17Z" `  
`media_filter_tag` |  String - optional - repeated  Filter tags for the document. At most 250 values are allowed per document with a length limit of 1000 characters. Otherwise, an INVALID_ARGUMENT error is returned.  This tag can be used to filter recommendations results by passing the tag as part of the `RecommendRequest.filter`.  For example: `"filter_tags": [ "filter_tag"]`  
`media_hash_tag` |  String - optional - repeated  Hashtags for the document. At most 100 values are allowed per document, with a length limit of 5000 characters.  For example: `"hash_tags": [ "soccer", "world cup"]`  
`media_in_language` |  String - optional - repeated  Language of the media contents. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  For example: `"in_languages": [ "en-US"]`  
`media_organization` |  Object - optional - repeated  Root key property for encapsulating the `organization`-related properties.  For example: `"organizations ":[{"name":"sports team","role":"team","rank":0,"uri":"http://example.com/team"}]`  
`media_organization_custom_role` |  String - optional  `custom_role` is set if and only if the `role` is set to be a `custom-role`. Must be a UTF-8 encoded string with a length limit of 128 characters. Must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`.   
`media_organization_name` |  String - required  Name of the organization.   
`media_organization_rank` |  String - optional  Used for role ranking. For example, for first publisher: `role = "publisher", rank = 1`.   
`media_organization_role` |  String - required  The role of the organization in the media item.  Supported values: director, actor, player, team, league, editor, author, character, contributor, creator, editor, funder, producer, provider, publisher, sponsor, translator, music-by, channel, custom-role  If none of the supported values are applied to `role`, set `role` to `custom-role` and provide the value in the `custom_role` field.   
`media_organization_uri` |  String - optional  URI of the organization.   
`media_person` |  Object - optional - repeated  Root key property for encapsulating the person-related properties.  For example: `"persons":[{"name":"sports person","role":"player","rank":0,"uri":"http://example.com/person"}]`  
`media_person_custom_role` |  String - optional  `custom_role` is set if and only if the `role` is set to be a `custom-role`. Must be a UTF-8 encoded string with a length limit of 128 characters. Must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`.   
`media_person_name` |  String - required Name of the person.   
`media_person_rank` |  Integer - optional  Used for role ranking. For example, for first actor, `role = "actor", rank = 1`  
`media_person_role` |  String - required  The role of the person in the media item.  Supported values: director, actor, player, team, league, editor, author, character, contributor, creator, editor, funder, producer, provider, publisher, sponsor, translator, music-by, channel, custom-role  If none of the supported values are applied to `role`, set `role` to `custom-role` and provide the value in the `custom_role` field.   
`media_person_uri` |  String - optional  URI of the person.   
`media_production_year` |  Integer - optional  The year the media was produced.   
`media_transcript` |  String - optional  Transcript of the media document.   
`media_type` |  String - this field is required for movies and shows  Top-level category.  Supported types: `movie`, `show`, `concert`, `event`, `live-event`, `broadcast`, `tv-series`, `episode`, `video-game`, `clip`, `vlog`, `audio`, `audio-book`, `music`, `album`, `articles`, `news`, `radio`, `podcast`, `book`, and `sports-game`.  The values `movie` and `show` have special significance. They cause documents to be enriched in a way that improves ranking and helps users making title searches to find alternate content they might be interested in.   
  
If you are using your own schema instead of the Google predefined schema, see [Provide or auto-detect a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema) for information about formatting and importing your own schema.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
