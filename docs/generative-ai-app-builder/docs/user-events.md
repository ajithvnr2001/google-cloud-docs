---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events/
title: About user events for custom apps \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:21.514519+00:00
---

# About user events for custom apps  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  About user events for custom apps Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Media apps require different user events. For information, see [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events).

This page describes user events for custom search and recommendations apps, including user event types, requirements, and examples for user event types.

Although users events are not required for custom apps, they are highly recommended.

Google recommends to upload events at least daily to maintain good data quality. During historical event imports make sure that data distribution skews toward the most recent timestamp. The number of events on the last timestamp day should be equal to or more than the average daily event count.

For help with recording user events, see [Record real-time user events][record-events]. To import past user events in bulk, see [Import historical user events][import-user-events].

## User event types

You can record the following types of user events as end users browse or search your site:

User event name | User action  
---|---  
`view-item-list` | Views a panel or ordered list of documents.  
`view-item` | Views details of a document.  
`view-home-page` | Views home page.  
`search` | Searches the app.  
  
For details about the user event object, see the [`UserEvent` API reference documentation][user-event].

## User event type examples and schemas

This section provides the data formats for each event type supported by custom apps. Examples for JavaScript Pixel are provided. For BigQuery, the full table schema for each type is provided.

For all user events types, `userId` is optional.

Note that: 

  * The `tagIds` field is needed only if you are running an A/B experiment.

  * The `attributionToken` field is optional; it is used to measure performance. `search` and `view-item` events that are generated from recommendations clicks should have an attribution token in order to link the events back to the recommendations that generated them. 




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
      }]
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
      eventType: "view-item",
      userPseudoId: "visitor0",
      "engine": "APP_ID",
      eventTime: "2020-01-01T03:33:33.000001Z",
      userInfo: {
        userId: "abc@example.com",
        userAgent: "Mozilla/5.0",
      },
      pageInfo: {
        pageViewId: "currentPageUri",
        uri: "http://example",
        referrerUri: "https://google",
      },
      attributionToken: "abcd",
      documents: [
        {
          id: "abcd",
        },
      ],
      tagIds: ["Treatment_B"],
      attributes: {
        example_text_attribute: {
          text: ["text_1", "text_2"],
        },
        example_number_attribute: {
          numbers: [3.14, 42, 1.2345],
        },
      },
      panels: [
             {
               panelId: "HOME_RFY_1",
               documents: [
                 {
                   id: "123"
                 },
                 {
                   id: "456"
                 }
               ],
               panelPosition: 1,
               totalPanels: 2
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

At least one of `searchQuery` or `pageCategory` field is required:

  * Provide `searchQuery` for search events where the user entered a text query.

  * Provide `pageCategory` when the user navigated to items of interest by browsing, that is, by clicking categories instead of by entering a text query.




The `attributionToken` is returned with the search query or browse results.

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
      "pageInfo": {
        "pageCategory": "CATEGORY_1 > CATEGORY_2",
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

## About user information

`userPseudoId` represents the unique user identifier and is required when you record a user event.

The user information ([`UserInfo`][user-info]) included when you record a user event contains the `userPseudoId` value and, if available, the `userId` value. `userId` is optional and can be used as a unique, persistent identifier for a user across devices whenever a user logs in to your site. When you record the `userId` for a user, your search and recommendation apps can generate more personalized results for one user across multiple devices, such as both a mobile device and a web browser.

**Note:** Use a secure form of a unique identifier to keep users anonymous to Agent Search and protect your users' privacy. You are responsible for redacting PII (personally identifiable information), such as email or home addresses, from your data.

## About the timestamp

When you record a user event, be sure to include an accurate timestamp of when the event occurred. Accurate timestamps make sure that your events are stored in the correct order. Timestamps are recorded automatically for events collected using the JavaScript Pixel. When you import events, you must provide the timestamp in the [`eventTime`][event-time] field in the format specified by [RFC 3339](https://tools.ietf.org/html/rfc3339).

## What's next

  * Learn how to [record user events][record-events].



[rec-type-reqs]: /generative-ai-app-builder/docs/about-media-recommendations-types [record-events]: /generative-ai-app-builder/docs/record-user-events [event-time]: /generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.event_time [user-event]: /generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents [user-info]: /generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#userinfo

[import-user-events]: /generative-ai-app-builder/docs/import-user-events [record-events]: /generative-ai-app-builder/docs/record-user-events

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
