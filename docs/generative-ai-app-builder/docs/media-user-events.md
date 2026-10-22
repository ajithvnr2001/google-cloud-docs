---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events/
title: About media user events \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:06.821636+00:00
---

# About media user events  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  About media user events Stay organized with collections  Save and categorize content based on your preferences. 

This page describes user events for media search and recommendations apps, including user event types, requirements, and examples for user event types. User events are required for media apps.

For general information about media search and recommendations, see [Introduction to media search and recommendations][about-media].

For help with recording user events, see [Record real-time user events][record-events]. To import past user events in bulk, see [Import historical user events][import-user-events].

**Note:** For information about user events for custom apps, see [About user events][about-user-events].

## User event types

You can record the following types of user events as end users browse or search your site:

User event name | User action  
---|---  
`view-item` | Views details of a document.  
`view-home-page` | Views home page.  
`search` | Searches the app.  
`media-play` | Clicks play on a media item.  
`media-complete` | Stops playing a media item, signifying the end of watching.  
  
For details about the user event object, see the [`UserEvent` API reference documentation][user-event].

## Event requirements for media search and recommendations

The types of user events that you need is determined by whether your app is a search app or a recommendations app, by the objective (click-through rate, conversion rate, or watch duration), and, for recommendations apps only, by the type of model that you've chosen. For more information about recommendation model types and optimization objectives, see [About media app recommendations types][rec-type-reqs].

To determine which user events you need to collect, refer to the following table.

Event | `search` | `view-home-page` | `view-item` | `media-play` | `media-complete`  
---|---|---|---|---|---  
**Search use case**  
| Required | Not  
required | Required | Required | Required  
**Recommended for You model type, by objective**  
**[CTR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#ctr)** | Not  
required | Required for homepage context  
  
Not required for general context | Either `view-item` or `media-play` is required | Strongly  
recommended  
  
Required if history demotion is turned on  
**[CVR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#cvr)** | Not  
required | Required for homepage context  
  
Not required for general context | Either `view-item` or `media-play` is required | Required  
**[Watch duration](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#watch-duration)** | Not  
required | Required for homepage context  
  
Not required for general context | Either `view-item` or `media-play` is required | Required  
**Others You May Like model type, by objective**  
**[CTR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#ctr)** | Not  
required | Not  
required | Either `view-item` or `media-play` is required | Strongly  
recommended  
  
Required if history demotion is turned on  
**[CVR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#cvr)** | Not  
required | Not  
required | Either `view-item` or `media-play` is required | Required  
**[Watch duration](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#watch-duration)** | Not  
required | Not  
required | Either `view-item` or `media-play` is required | Required  
**More Like This model type, by objective**  
**[CTR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#ctr)** | Not  
required | Not  
required | Either `view-item` or `media-play` is required | Required if history demotion is turned on  
**[CVR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#cvr)** | Not  
required | Not  
required | Either `view-item` or `media-play` is required | Required  
**[Watch duration](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#watch-duration)** | Not  
required | Not  
required | Either `view-item` or `media-play` is required | Required  
**Most Popular model type, by objective**  
**[CTR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#ctr)** | Not  
required | Not  
required | One of `view-item` or `media-play` is required | Not  
required  
**[CVR](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#cvr)** | Not  
required | Not  
required | Not  
required | Not  
required | Required  
  
## Requirements for media user events

Make sure your user events meet the following requirements so that your media apps can generate quality results.

Event type | Requirement | Impact  
---|---|---  
All events |  Don't include synthetic data or duplicate events.  |  Synthetic or duplicate events negatively impact result quality and can prevent you from deploying your app. Duplicate events can cause incorrect metrics values.   
Include at least 100 unique user pseudo IDs for each type of event ingested.  |  Include these IDs so that media recommendations apps have enough data to generate quality results.   
User pseudo IDs must be formatted exactly the same across event import or event recording and in media recommendations requests.  |  Using a consistent format for user pseudo IDs helps media recommendations apps correctly identify visitor patterns and provide better-quality results based on user behavior.   
The `DocumentInfo.name` field or the `DocumentInfo.id` field is required for all documents.  |  An event that includes a document without a `DocumentInfo.name` field or a `DocumentInfo.id` field can't be used by media recommendations apps.   
Documents included in the events should exist in your data store.  |  The unjoined events ratio should be kept as low as possible. A high ratio can negatively impact the quality of results.   
Some user events should have the same user pseudo ID.  |  To construct valid behavior sequence histories, media recommendations apps must be able to see multiple events with the same user pseudo ID.  For example, `visitor123` has viewed five items and clicked play on two. If these events provide the same consistently formatted user pseudo ID, a media recommendations app can consider that behavior sequence in its results.   
`view-item` |  Include exactly one document per event.  |  The event can't be used if no document exists. If multiple documents are included, the event is malformed and can't be used.   
`search` |  Include the [`attributionToken`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents). The `attributionToken` is returned by the [search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method along with the search or browse results.  |  The `attributionToken` enables Agent Search to accurately attribute the search event to a particular search response.   
`media-play` |  Include exactly one document per event.  |  If multiple documents are included, the event is malformed and can't be used.   
  
## User event tags for A/B tests

If you do A/B testing, make sure to add tag IDs to all the user events that you collect, adding one tag for each test group.

For example, add the tag `"tagIds": ["original"]` to the user events from your current model and add the tag `"tagIds": ["google"]` to the user events from Agent Search for media.

## User event type examples and schemas

This section provides the data formats for each event type supported by media recommendations. Examples for JavaScript Pixel are provided. For BigQuery, the full table schema for each type is provided.

For all user events types, `userId` is optional.

For more details about the user event object, see the [`UserEvent` API reference documentation][user-event].

### view-item

The following shows the `view-item` user event data format.

#### Search optimization requirements for view-item events

To let search automatically optimize the search experience based on overall user trends, upload the following data.

Events should be uploaded at least daily with a maximum delay of 24 hours.

Events metric | Events volume/frequency | Description  
---|---|---  
Volume of `view-item` events | 250k view items |  At least 250,000 view items are **required** to optimize the search experience based on events ingested.   
  
#### Minimum required view-item object

The following examples show only the required fields of the `view-item` user event format. 

The [`documents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo) object contains the document's ID ([`id`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource name ([`name`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)). 

  * When you ingest or record user events at a data-store level, you can provide the document's ID (`id`) or resource name (`name`). 
  * When you ingest or record events at a location level, you must supply the document's resource name (`name`) because it indicates a document's full path and refers to the data store where the document resides. You can provide the document's ID as an optional, additional information.



### JavaScript Pixel
    
    
    var user_event = {
      "eventType": "view-item",
      "userPseudoId": "USER_PSEUDO_ID",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "documents": [{
        "name": "DOCUMENT_NAME"
      }],
      "panels": [
         {
           "panelId": "HOME_RFY_1",
           "documents": [
             {
               "id": "123"
             },
             {
               "id": "456"
             }
           ],
           "panelPosition": 1,
           "totalPanels": 2
         }
      ]
    };
    

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      }
    ]

####  Complete view-item object example 

The following examples include both required and optional fields for the `view-item` user event. 

###  JavaScript Pixel 
    
    
    var user_event = {
      "eventType": "view-item",
      "userPseudoId": "visitor0",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "userInfo": {
        "userId": "abc@example.com",
        "userAgent": "Mozilla/5.0",
      },
      "pageInfo": {
        "pageViewId": "currentPageUri",
        "uri": "http://example",
        "referrerUri": "https://google",
      },
      "attributionToken": "abcd",
      "documents": [
        {
          "id": "abcd",
        },
      ],
      "tagIds": ["Treatment_B"],
      "attributes": {
        "example_text_attribute": {
          "text": ["text_1", "text_2"],
        },
        "example_number_attribute": {
          "numbers": [3.14, 42, 1.2345],
        },
      },
      "panels": [
             {
               "panelId": "HOME_RFY_1",
               "documents": [
                 {
                   "id": "123"
                 },
                 {
                   "id": "456"
                 }
               ],
               "panelPosition": 1,
               "totalPanels": 2
             }
          ]
    };

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      }
    ]

### view-home-page

The following shows the `view-home-page` user event format.

#### Minimum required view-home-page object

The following examples show only the required fields of the `view-home-page` user event format. 

The [`documents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo) object contains the document's ID ([`id`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource name ([`name`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)). 

  * When you ingest or record user events at a data-store level, you can provide the document's ID (`id`) or resource name (`name`). 
  * When you ingest or record events at a location level, you must supply the document's resource name (`name`) because it indicates a document's full path and refers to the data store where the document resides. You can provide the document's ID as an optional, additional information.



### JavaScript Pixel
    
    
    var user_event = {
      "eventType": "view-home-page",
      "userPseudoId": "USER_PSEUDO_ID",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "panels": [
         {
           "panelId": "HOME_RFY_1",
           "documents": [
             {
               "id": "123"
             },
             {
               "id": "456"
             }
           ],
           "panelPosition": 1,
           "totalPanels": 2
         }
      ]
    };
    

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "quantity",
            "type": "INT64",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      }
    ]

For information about the `panels` object, see About panels.

####  Complete view-home-page object example 

The following examples include both required and optional fields for the `view-home-page` user event. 

###  JavaScript Pixel 
    
    
    var user_event = {
      "eventType": "view-home-page",
      "userPseudoId": "visitor0",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "userInfo": {
        "userId": "abc@example.com",
        "userAgent": "Mozilla/5.0",
      },
      "pageInfo": {
        "pageViewId": "currentPageUri",
        "uri": "http://example",
        "referrerUri": "https://google",
      },
      "attributionToken": "abcd",
      "documents": [
        {
          "id": "abcd",
          "quantity": 2,
        },
      ],
      "tagIds": ["Treatment_B"],
      "attributes": {
        "example_text_attribute": {
          "text": ["text_1", "text_2"],
        },
        "example_number_attribute": {
          "numbers": [3.14, 42, 1.2345],
        },
      },
      "panels": [
             {
               "panelId": "HOME_RFY_1",
               "documents": [
                 {
                   "id": "123"
                 },
                 {
                   "id": "456"
                 }
               ],
               "panelPosition": 1,
               "totalPanels": 2
             }
          ]
    };

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "quantity",
            "type": "INT64",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      }
    ]

### search

The following shows the `search` user event format.

#### Search optimization requirements for search events

To let search automatically optimize the search experience based on overall user trends, upload the following data.

Events should be uploaded at least daily with a maximum delay of 24 hours.

Events metric | Events volume/frequency | Description  
---|---|---  
Volume of `search` events | 100k searches |  At least 100,000 searches are **required** to optimize the search experience based on events ingested.   
  
#### Minimum required search object

The following examples show only the required fields of the `search` user event format.

Provide `searchQuery` for search events where the user entered a text query. 

The `attributionToken` is returned with the search query results.

The [`documents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo) object contains the document's ID ([`id`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource name ([`name`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)). 

  * When you ingest or record user events at a data-store level, you can provide the document's ID (`id`) or resource name (`name`). 
  * When you ingest or record events at a location level, you must supply the document's resource name (`name`) because it indicates a document's full path and refers to the data store where the document resides. You can provide the document's ID as an optional, additional information.



### JavaScript Pixel
    
    
    var user_event = {
      "eventType": "search",
      "userPseudoId": "USER_PSEUDO_ID",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "searchInfo": {
        "searchQuery": "SEARCH_QUERY",
      }, 
      "attributionToken": "ATTRIBUTION_TOKEN",
      "documents": [
        {
          "name": "DOCUMENT_NAME_1",
        },
        {
          "name": "DOCUMENT_NAME_2",
        },
      ]
    };
    

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "searchInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "searchQuery",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageCategory",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      }
    ]

### media-play

The following shows the `media-play` user event format.

#### Minimum required media-play object

The following examples show only the required fields of the `media-play` user event format. 

The [`documents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo) object contains the document's ID ([`id`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource name ([`name`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)). 

  * When you ingest or record user events at a data-store level, you can provide the document's ID (`id`) or resource name (`name`). 
  * When you ingest or record events at a location level, you must supply the document's resource name (`name`) because it indicates a document's full path and refers to the data store where the document resides. You can provide the document's ID as an optional, additional information.



### JavaScript Pixel
    
    
    var user_event = {
      "eventType": "media-play",
      "userPseudoId": "USER_PSEUDO_ID",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "documents": [
        {
          "name": "DOCUMENT_NAME_1"
        }
      ]
    };
    

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      }
    ]

####  Complete media-play object example 

The following examples include both required and optional fields for the `media-play` user event. 

###  JavaScript Pixel 
    
    
    var user_event = {
      "eventType": "media-play",
      "userPseudoId": "visitor0",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "userInfo": {
        "userId": "abc@example.com",
        "userAgent": "Mozilla/5.0",
      },
      "pageInfo": {
        "pageViewId": "currentPageUri",
        "uri": "http://example",
        "referrerUri": "https://google",
      },
      "attributionToken": "abcd",
      "documents": [
        {
          "id": "abcd",
        },
      ],
      "tagIds": ["Treatment_B"],
      "attributes": {
        "example_text_attribute": {
          "text": ["text_1", "text_2"],
        },
        "example_number_attribute": {
          "numbers": [3.14, 42, 1.2345],
        },
      },
    };

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      }
    ]

### media-complete

The following shows the `media-complete` user event format.

#### Minimum required media-complete object

The following examples show only the required fields of the `media-complete` user event format. 

The [`documents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo) object contains the document's ID ([`id`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource name ([`name`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)). 

  * When you ingest or record user events at a data-store level, you can provide the document's ID (`id`) or resource name (`name`). 
  * When you ingest or record events at a location level, you must supply the document's resource name (`name`) because it indicates a document's full path and refers to the data store where the document resides. You can provide the document's ID as an optional, additional information.



### JavaScript Pixel
    
    
    var user_event = {
      "eventType": "media-complete",
      "userPseudoId": "USER_PSEUDO_ID",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "documents": [
        {
          "name": "DOCUMENT_NAME_1"
        }
      ],
      "mediaInfo": {
        "mediaProgressDuration": "65s",
        "mediaProgressPercentage": 0.2
      }
    };
    

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      },
      {
        "name": "mediaInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "mediaProgressDuration",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "mediaProgressPercentage",
            "type": "NUMERIC",
            "mode": "NULLABLE"
          }
        ]
      }
    ]

####  Complete media-complete object example 

The following examples include both required and optional fields for the `media-complete` user event. 

###  JavaScript Pixel 
    
    
    var user_event = {
      "eventType": "media-complete",
      "userPseudoId": "visitor0",
      "engine": "APP_ID",
      "eventTime": "2020-01-01T03:33:33.000001Z",
      "userInfo": {
        "userId": "abc@example.com",
        "userAgent": "Mozilla/5.0",
      },
      "pageInfo": {
        "pageViewId": "currentPageUri",
        "uri": "http://example",
        "referrerUri": "https://google",
      },
      "attributionToken": "abcd",
      "documents": [
        {
          "id": "abcd",
        },
      ],
      "tagIds": ["Treatment_B"],
      "attributes": {
        "example_text_attribute": {
          "text": ["text_1", "text_2"],
        },
        "example_number_attribute": {
          "numbers": [3.14, 42, 1.2345],
        },
      },
      "mediaInfo": {
        "mediaProgressDuration": "65s",
        "mediaProgressPercentage": 0.2,
      },
    };

###  BigQuery 

This is the complete JSON schema for this user event type. Specify this schema when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with BigQuery. `eventTime` is a string with a Timestamp format. 
    
    
    [
      {
        "name": "eventType",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userPseudoId",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "engine",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "eventTime",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "userInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "userId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "userAgent",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "pageInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "pageviewId",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "referrerUri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "attributionToken",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "documents",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "id",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "tagIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "example_text_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              }
            ]
          },
          {
            "name": "example_number_attribute",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "numbers",
                "type": "NUMERIC",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      },
      {
        "name": "mediaInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "mediaProgressDuration",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "mediaProgressPercentage",
            "type": "NUMERIC",
            "mode": "NULLABLE"
          }
        ]
      }
    ]

## Custom attributes

You can include additional custom attributes and features for user events. This can result in improved, more specific results for your users. To add custom attributes, use `attributes` when you record a user event.

If you provide custom attributes for ingested user events, it's important to also include them in the user events that you associate with recommendation and search requests. The formatting of custom attributes must be consistent between imported events and events provided with requests. This lets media apps use those custom attributes to improve quality.

You can provide custom text values by using the `text` field or custom numerical values by using the `numbers` field.

For example, the following shows the `attributes` section from a request to record a user event:
    
    
      attributes: {
        user_age: {text: ["teen", "young adult"]},
        user_location: {text: ["CA"]},
        user_zip: {numbers: [90210]}
      }

## About user information

`userPseudoId` represents the unique user identifier and is required when you record a user event.

The user information ([`UserInfo`][user-info]) included when you record a user event contains the `userPseudoId` value and, if available, the `userId` value. `userId` is optional and can be used as a unique, persistent identifier for a user across devices whenever a user logs in to your site. When you record the `userId` for a user, media search and recommendations apps can generate more personalized results for one user across multiple devices, such as both a mobile device and a web browser.

**Note:** Use a secure form of a unique identifier to keep users anonymous to Agent Search and protect your users' privacy. You are responsible for redacting PII (personally identifiable information), such as email or home addresses, from your data.

## About the timestamp

When you record a user event, be sure to include an accurate timestamp of when the event occurred. Accurate timestamps make sure that your events are stored in the correct order. Timestamps are recorded automatically for events collected using the JavaScript Pixel. When you import events, you must provide the timestamp in the [`eventTime`][event-time] field in the format specified by [RFC 3339](https://tools.ietf.org/html/rfc3339).

## About panels

On a homepage, you'll typically have one or more panels, such as a "trending now" panel and a "recommended for you" panel. On detail pages, you might also have panels, such as "others you may like".

### Panel information for user events

Panel information is needed for recommendation user events of type `view-home-page` and `view-item`. Panel information is required for home pages and detail pages that display content recommended by Google.

If you are conducting A/B testing for a panel, then you must record user events with panel information for all content in the test, regardless of source. For home pages and detail pages without Google-generated panel content, it is recommended, but not required, to provide panel information in the `view-home-page` and `view-item` events. These requirements are summarized in the following table:

Source of user event (`view-home-page` and `view-item`)  | `PanelInfo` required   
---|---  
Includes content recommended by Google  | Yes   
Includes content NOT recommended by Google and used in A/B testing  | Yes   
Includes content NOT recommended by Google and NOT used in A/B testing  | No   
  
Panel information (`PanelInfo`) is a set of fields that describes various elements of the panel:

  * The ID number for the panel

  * The display name

  * The position of the panel on the page (_e.g.,_ first panel (`1`) on the page, or the third panel (`3`) on the page)

  * The total number of panels on the page

  * The list of documents (`DocumentInfo`) presented in each panel




For detailed information about the `PanelInfo` objects, see [PanelInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#PanelInfo).

**Note:** The user event resource contains both a `panel` and a `panels` field. The field that you need to populate for view-home-page user events is the `panels` field, which takes an array of `PanelInfo` objects.

### Pre-loading panels versus lazy-loading panels

There are two common methods for displaying recommendations on web pages or mobile pages. The method that you use determines the number and content of the `view-home-page` user events that you record.

  * **Pre-loading:** With pre-loading all the recommendation items are generated the user arrives at the page. In this case, when the user loads the homepage, you record one `view-home-page` (or `view-item`) user event with all panels and documents.

  * **Lazy loading:** With lazy loading, panel content is not generated when the user arrives on the page, but instead content is dynamically loaded when the user scrolls down to panels or right to see more recommendations. In this case, when a user loads the homepage, your record an initial `view-home-page` (or `view-item`) user event and then continue to record more events when the user scrolls to generate more recommended content. In the subsequent events, you only need to include in the `panels` array the increment of documents being displayed.




### Example scenario

A media company's home page displays two panels of recommendations:

  * A trending-now panel that is powered by the [Most Popular](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#most-popular) model.

  * A personalized recommendation panel that is being A/B tested. Some users see a panel of suggestions powered by the [Recommended for You](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#recommended-for-you) model (group-A), and other users see recommendations from the company's proprietary model (group-B).




When a user assigned to group-B views this home page, the user event in JavaScript Pixel format looks like this:
    
    
    var user_event = {
      "eventType": "view-home-page",
      "userPseudoId": "4003345673.123451357",
      "eventTime": "2025-07-01T03:33:33.000001Z",
      "userInfo": {
        "userId": "jane.doe@example.com",
      },
      "tagIds": ["group-B"],
      "panels": [
        {
          "panelId": "panel-1",
          "displayId": "Trending Now",
          "documents": [
            {
              "id": "254722"
            },
            {
              "id": "2951"
            },
            ...
            {
              "id": "1201"
            }
          ],
          "panelPosition": 1,
          "totalPanels": 2
        },
        {
          "panelId": "panel-2",
          "displayId": "Recommended for You",
          "documents": [
            {
              "id": "79132"
            },
            {
              "id": "109487"
            },
            ...
            {
              "id": "164179"
            }
          ],
          "panelPosition": 2,
          "totalPanels": 2
        }
      ]
    };

## What's next

  * Learn how to [record user events][record-events].



[rec-type-reqs]: /generative-ai-app-builder/docs/about-media-recommendations-types [record-events]: /generative-ai-app-builder/docs/record-user-events [event-time]: /generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.event_time [user-event]: /generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents [user-info]: /generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#userinfo

[about-media]: /generative-ai-app-builder/docs/about-media [about-user-events]: /generative-ai-app-builder/docs/user-events [import-user-events]: /generative-ai-app-builder/docs/import-user-events [record-events]: /generative-ai-app-builder/docs/record-user-events

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
