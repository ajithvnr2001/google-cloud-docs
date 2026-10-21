---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sessions.events/list/
title: Method: events.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:03:44.003199+00:00
---

# Method: events.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sessions.events/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: events.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.reasoningEngines.sessions.events.list

Lists `[events](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Event)` in a given session.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/events`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the session to list events from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}/sessions/{session}`

### Query parameters

| `pageSize` `integer` Optional. The maximum number of events to return. The service may return fewer than this value. If unspecified, at most 100 events will be returned. These events are ordered by timestamp in ascending order. | `pageToken` `string` Optional. The `[nextPageToken](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sessions.events/list#body.ListEventsResponse.FIELDS.next_page_token)` value returned from a previous list `[SessionService.ListEvents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sessions.events/list#google.cloud.aiplatform.v1.SessionService.ListEvents)` call. | `filter` `string` Optional. The standard list filter. Supported fields: * `timestamp` range (i.e. `timestamp>="2025-01-31T11:30:00-04:00"` where the timestamp is in RFC 3339 format)More detail in [AIP-160](https://google.aip.dev/160). | `orderBy` `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * `timestamp`Example: `timestamp desc`.

### Request body

The request body must be empty.

### Response body

Response message for `[SessionService.ListEvents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sessions.events/list#google.cloud.aiplatform.v1.SessionService.ListEvents)`. If successful, the response body contains data with the following structure: | Fields  
  
`sessionEvents[]` `object (`[SessionEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/SessionEvent)`)` A list of events matching the request. Ordered by timestamp in ascending order. | `nextPageToken` `string` A token, which can be sent as `[ListEventsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sessions.events/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "sessionEvents": [
        {
          object ([SessionEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/SessionEvent))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
