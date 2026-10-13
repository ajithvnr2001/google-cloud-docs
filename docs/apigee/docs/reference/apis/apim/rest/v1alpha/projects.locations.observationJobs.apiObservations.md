---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations
title: REST Resource: projects.locations.observationJobs.apiObservations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:55.248827+00:00
---

# REST Resource: projects.locations.observationJobs.apiObservations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: projects.locations.observationJobs.apiObservations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ApiObservation
    * JSON representation
  * Style
  * Methods



## Resource: ApiObservation

Message describing ApiObservation object

JSON representation  
---  
      
    
    {
      "name": string,
      "style": enum ([Style](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations#Style)),
      "serverIps": [
        string
      ],
      "hostname": string,
      "sourceLocations": [
        string
      ],
      "tags": [
        string
      ],
      "apiOperationCount": string,
      "createTime": string,
      "updateTime": string,
      "lastEventDetectedTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of resource  
`style` |  `enum (`[Style](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations#Style)`)` Style of ApiObservation  
`serverIps[]` |  `string` The IP address (IPv4 or IPv6) of the origin server that the request was sent to. This field can include port information. Examples: `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.  
`hostname` |  `string` The hostname of requests processed for this Observation.  
`sourceLocations[]` |  `string` Location of the Observation Source, for example "us-central1" or "europe-west1."  
`tags[]` |  `string` User-defined tags to organize and sort  
`apiOperationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of observed API Operations.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Create time stampA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Update time stampA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`lastEventDetectedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last event detected time stampA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## Style

ApiObservation protocol style For MVP, only support REST and unknown protocol

Enums  
---  
`STYLE_UNSPECIFIED` | Unknown style  
`REST` | Style is Rest API  
`GRPC` | Style is Grpc API  
`GRAPHQL` | Style is GraphQL API  
  
## Methods  
  
---  
  
### `[batchEditTags](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags)`

|  BatchEditTagsApiObservations adds or removes Tags for ApiObservations.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/get)`

|  GetApiObservation retrieves a single ApiObservation by name.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/list)`

|  ListApiObservations gets all ApiObservations for a given project and location and ObservationJob.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
