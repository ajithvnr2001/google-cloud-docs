---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/manage-user-events/
title: Manage user events \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:58:50.218056+00:00
---

# Manage user events  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/manage-user-events/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Manage user events Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view user event information and purge user events.

To record user events as they happen, see [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events). To import user event data from past events, see [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).

## View aggregated user event information

You can see information about recorded user events for your app in the Google Cloud console on the **Events** tab of your app's **Data** page.

This page shows information such as number of events ingested, number of unjoined events, percentage change in number of events over a period, and average count of event type per document. In addition, you can see metrics for each event type over time. Metrics appear about 24 hours after you first upload events.

To see your user event information:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to see user event information for.

  3. On the **Data** page, go to the **Events** tab. User event information is displayed on this tab.




## Purge user events

If you have user events that were not recorded correctly and need to remove them, you can do so using the [`userEvents.purge`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents/purge) API method. Although you [record](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events) and [import](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events) at a location level, you must purge user events at the data-store level.

Specify the events you want to remove by using a user event filter. You can use the user event filter to specify the events that you want to purge. You can filter with the `eventTime`, `eventType`, `visitorID`, and `userID` fields.

This example filters for a time range, which must use the [Zulu Time date format](https://www.ietf.org/rfc/rfc3339.txt).
    
    
    curl -X POST \
      -H "Authorization: Bearer "$(gcloud auth application-default print-access-token)"" \
      -H "Content-Type: application/json; charset=utf-8" \
      --data '{
        "filter":"eventTime > \"2023-12-21T18:25:43.511Z\" eventTime < \"2023-12-21T18:30:43.511Z\"",
      }' \
      "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/dataStores/DATA_STORE_ID/userEvents:purge"

You should receive a response object similar to the following, where `purge-user-events-54321` is the operation ID:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/operations/purge-user-events-54321"
    }

This example requests the operation status:
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/dataStores/DATA_STORE_ID/operations/OPERATION_ID"

Operation status example: 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.PurgeUserEventsResponse"
        "purgedEventsCount": "1"
      }
    }

## Use the user event filter

You can filter user events to be deleted.

The filter is a string that contains one or more of the following restrictions:

  * `eventTime`: Provides a timestamp to bound the events to be deleted. This filter can be specified once or twice, with a greater-than (`>`) or less-than (`<`) symbol. The bounded time must be a single contiguous block.

  * `eventType`: Restrict the events to be deleted to a single event type.

  * `visitorID`: Restrict the events to be deleted to a single visitor ID.

  * `userID`: Restrict the events to be deleted to a single user ID.




Only user events that satisfy all of the restrictions are deleted.

For example, to delete all user events of type `add-to-cart` that were logged on or after February 1, 2023, you would provide the following filter string:
    
    
    eventTime > "2023-02-01T00:00:00Z" eventType = add-to-cart

## What's next

  * [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events)
  * [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
