---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions
title: REST Resource: projects.locations.collections.engines.sessions \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:48.255084+00:00
---

# REST Resource: projects.locations.collections.engines.sessions  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.engines.sessions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Session
    * JSON representation
  * Methods



## Resource: Session

External session proto definition.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.sessions#Session.State)),
      "userPseudoId": string,
      "turns": [
        {
          object ([Turn](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.sessions#Session.Turn))
        }
      ],
      "labels": [
        string
      ],
      "startTime": string,
      "endTime": string,
      "isPinned": boolean,
      "pendingAsyncAssistOperationId": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/engines/{engine}/sessions/*`  
`displayName` |  `string` Optional. The display name of the session.This field is used to identify the session in the UI. By default, the display name is the first turn query text in the session.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.sessions#Session.State)`)` The state of the session.  
`userPseudoId` |  `string` A unique identifier for tracking users.  
`turns[]` |  `object (`[Turn](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.sessions#Session.Turn)`)` Turns.  
`labels[]` |  `string` Optional. The labels for the session. Can be set as filter in ListSessionsRequest.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the session started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the session finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`isPinned` |  `boolean` Optional. Whether the session is pinned, pinned session will be displayed on the top of the session list.  
`pendingAsyncAssistOperationId` |  `string` Output only. Full resource name of an in-progress AsyncAssist operation for this session, e.g. `projects/*/locations/*/collections/*/engines/*/sessions/*/operations/*`. Set when the operation starts and cleared when it finishes.  
  
## Methods  
  
---  
  
### `[addContextFile](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/addContextFile)`

|  Uploads a context file to use as source for the assist calls within the session.  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/create)`

|  Creates a Session.  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/delete)`

|  Deletes a Session.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/get)`

|  Gets a Session.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/list)`

|  Lists all Sessions by their parent `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`.  
  
### `[patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/patch)`

|  Updates a Session.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
