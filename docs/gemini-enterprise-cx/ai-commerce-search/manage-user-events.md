---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events/
title: Manage user events \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:03.675952+00:00
---

# Manage user events  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Manage user events Stay organized with collections  Save and categorize content based on your preferences. 

Book: /gemini-enterprise-cx/ai-commerce-search/_book.yaml

This page describes how to view and delete user events. For information about recording user events as they happen, see [Record real-time user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events). To import user event data from past events, see [Import historical user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events).

## Rejoin user events tutorial

This tutorial show how to rejoin user events by making a `POST` request to the [`userEvents:rejoin`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/rejoin) endpoint.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_rejoin_user_events_select_language&show=ide&environment_deployment=ide)

* * *

## Remove user events tutorial

This tutorial show how to purge user events.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_purge_user_events_select_language&show=ide&environment_deployment=ide)

* * *

## View aggregated user event information

View event integration metrics in the **Events** tab on the AI Commerce Search in Gemini Enterprise for Customer Experience console **Data** page. This page shows all events written or imported in last year. Metrics can take up to 24 hours to appear after successful data ingestion. 

[Go to the Data page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/)

![AI Commerce Search User Event Stats](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/user-events-stats.png)

## Rejoin user events

You can rejoin user events by making a `POST` request to the [`userEvents:rejoin`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/rejoin) endpoint.

The rejoin operation joins specified events with the latest version of the product catalog.

A user event is considered unjoined if the product it is associated with isn't present in the catalog at the time that the user event is ingested. Unjoined events lack detailed product information and are not as useful to training models and serving results.

In addition to addressing unjoined events, the rejoin operation can be used to correct events that have been joined with the wrong product catalog.

You must have the **Retail AI Admin** IAM role to call this method. A rejoin operation can take hours or days to complete. [Verify that you have the permissions required](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/iam).

### curl

Set `userEventRejoinScope` according to the types of events you're rejoining:

  * `USER_EVENT_REJOIN_SCOPE_UNSPECIFIED`: Default. Trigger rejoin for both joined and unjoined events.
  * `JOINED_EVENTS`: Trigger rejoin for only joined events.
  * `UNJOINED_EVENTS`: Trigger rejoin for only unjoined events.



The following example triggers a rejoin for only unjoined events:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
         'userEventRejoinScope': 'UNJOINED_EVENTS'
         }" \
        "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:rejoin"

You should receive a response object that looks something like this:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/OPERATION_ID"
    }

You can check the status of the rejoin. Replace OPERATION_ID with the ID of the operation ID returned by the rejoin method:
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/OPERATION_ID"

When the operation completes, the operation status returns as `done`:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.retail.v2.RejoinUserEventsResponse",
        "rejoinedUserEventsCount": "1"
      }
    }

### Java
    
    
    public static String rejoinUserEvents(UserEventRejoinScope scope)
        throws IOException, InterruptedException, ExecutionException {
      UserEventServiceClient userEventsClient = getUserEventServiceClient();
    
      RejoinUserEventsRequest request = RejoinUserEventsRequest.newBuilder()
          .setParent(DEFAULT_CATALOG_NAME)
          .setUserEventRejoinScope(scope)
          .build();
    
      String operationName = userEventsClient
          .rejoinUserEventsAsync(request).getName();
    
      userEventsClient.shutdownNow();
      userEventsClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return operationName;
    }

## Remove user events

Generally, you should leave user events in place after they have been recorded. Purging events is not recommended.

An event purge can take up to several days to complete. If you plan to reset user events entirely, consider creating a new project instead.

If you have user events that were not recorded properly and need to remove them, you can do so using the [`userEvents.purge`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/purge) method.

Specify the events you want to remove by using a filter string. This supports selectively deleting user events by filtering on the `eventTime`, `eventType`, `visitorID`, and `userID` fields.

Because you cannot undo the delete, test your filter string by conducting a dry run before deleting user events. The `force` field is set to `false` by default; this setting will return the number of events to be deleted without actually deleting them. When you are ready to actually delete the user events, set the `force` field to `true`.

You must have the **Retail AI Admin** IAM role to call this method. [Verify that you have the permissions required](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/iam).

### curl

This example filters for a time range, which must use the [Zulu Time date format](https://www.ietf.org/rfc/rfc3339.txt). The `force` field is set to `false`.
    
    
    curl -X POST \
      -H "Authorization: Bearer "$(gcloud auth application-default print-access-token)"" \
      -H "Content-Type: application/json; charset=utf-8" \
      --data '{
        "filter":"eventTime > \"2019-12-23T18:25:43.511Z\" eventTime < \"2019-12-23T18:30:43.511Z\"",
        "force":"false"
      }' \
      "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:purge"

You should receive a response object that looks something like this, where `purge-user-events-54321` is the operation ID:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/purge-user-events-54321"
    }

This example requests the operation status:
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/OPERATION_ID"

Operation status example: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.retail.v2.PurgeUserEventsResponse",
        "purgedEventsCount": "1"
      }
    }

Setting the `force` field to `true` forces the delete to occur.
    
    
    curl -X POST \
      -H "Authorization: Bearer "$(gcloud auth application-default print-access-token)"" \
      -H "Content-Type: application/json; charset=utf-8" \
      --data '{
        "filter":"eventTime > \"2019-12-23T18:25:43.511Z\" eventTime < \"2019-12-23T18:30:43.511Z\"",
        "force":"true"
      }' \
    "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:purge"

### Java
    
    
    public static String purgeUserEvents(
        String filter)
        throws IOException, InterruptedException, ExecutionException {
      UserEventServiceClient userEventsClient = getUserEventServiceClient();
    
      PurgeUserEventsRequest request = PurgeUserEventsRequest.newBuilder()
          .setParent(DEFAULT_CATALOG_NAME)
          .setFilter(filter)
          .setForce(true)
          .build();
    
      String operationName = userEventsClient
          .purgeUserEventsAsync(request).getName();
    
      userEventsClient.shutdownNow();
      userEventsClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return operationName;
    }

## Use the user event filter

You can filter user events to be deleted.

The filter is a string that contains one or more of the following restrictions:

  * **_eventTime_**

Provides a timestamp to bound the events to be deleted. This filter can be specified once or twice, with a greater-than (>) or less-than (<) symbol. The bounded time must be a single, contiguous block.

  * **_eventType_**

Restrict the events to be deleted to a single event type.

  * **_visitorID_**

Restrict the events to be deleted to a single visitor ID.

  * **_userID_**

Restrict the events to be deleted to a single user ID.




Only user events that satisfy all of the restrictions are deleted.

To delete all user events of type `add-to-cart` that were logged on or after February 1, 2019, you would provide the following filter string:
    
    
    eventTime > "2019-02-01T00:00:00Z" eventType = add-to-cart

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
