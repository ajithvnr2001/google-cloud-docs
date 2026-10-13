---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/reliabilityRisks/
title: REST Resource: reliabilityRisks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:58.697519+00:00
---

# REST Resource: reliabilityRisks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/reliabilityRisks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: reliabilityRisks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ReliabilityRisk
    * JSON representation
      * JSON representation
  * Methods



## Resource: ReliabilityRisk

Represents a ReliabilityRisk resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "name": string,
      "id": string,
      "description": string,
      "creationTimestamp": string,
      "details": {
        "globalDnsInsight": {
          "projectDefaultIsGlobalDns": boolean,
          "queryObservationWindow": string,
          "totalQueryCount": string,
          "riskyQueryCount": string
        },
        "lastUpdateTimestamp": string,
        "duration": string,
        "type": enum,
        "severity": enum
      },
      "recommendation": {
        "content": string,
        "referenceUrl": string
      },
      "selfLink": string,
      "selfLinkWithId": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#reliabilityRisk` for reliability risks.  
`name` |  `string` Name of the resource. The name must be 1-63 characters long and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`description` |  `string` An optional textual description of the resource; provided when the resource is created.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`details` |  `object` Output only. Details of the reliability risk resource  
`details.globalDnsInsight` |  `object` Insight details for global DNS risk.  
`details.globalDnsInsight.projectDefaultIsGlobalDns` |  `boolean` Indicates whether the project's default DNS setting is global DNS.  
`details.globalDnsInsight.queryObservationWindow` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The observation window for the query counts.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`details.globalDnsInsight.totalQueryCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of queries in the observation window.  
`details.globalDnsInsight.riskyQueryCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of queries that are risky. This is always less than or equal to totalQueryCount.  
`details.lastUpdateTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last time the risk was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`details.duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration of the risk since it was detected.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`details.type` |  `enum` The type of risk.  
`details.severity` |  `enum` The severity of the risk.  
`recommendation` |  `object` The recommendation to mitigate the risk.  
`recommendation.content` |  `string` Mitigation guide for the risk.  
`recommendation.referenceUrl` |  `string` URL referencing a more detailed mitigation guide.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reliabilityRisks/get)`

|  Returns the specified ReliabilityRisk resource.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reliabilityRisks/list)`

|  Retrieves the list of reliabilityRisks available in the specified project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
