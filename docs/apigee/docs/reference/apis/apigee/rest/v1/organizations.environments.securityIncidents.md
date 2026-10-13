---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents
title: REST Resource: organizations.environments.securityIncidents \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:30.250570+00:00
---

# REST Resource: organizations.environments.securityIncidents  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.environments.securityIncidents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SecurityIncident
    * JSON representation
  * RiskLevel
  * Observability
  * Methods



## Resource: SecurityIncident

Represents an SecurityIncident resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "firstDetectedTime": string,
      "lastDetectedTime": string,
      "detectionTypes": [
        string
      ],
      "trafficCount": string,
      "riskLevel": enum ([RiskLevel](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents#RiskLevel)),
      "observability": enum ([Observability](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents#Observability)),
      "lastObservabilityChangeTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Name of the security incident resource. Format: organizations/{org}/environments/{environment}/securityIncidents/{incident} Example: organizations/apigee-org/environments/dev/securityIncidents/1234-5678-9101-1111  
`displayName` |  `string` Optional. Display name of the security incident.  
`firstDetectedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when events associated with the incident were first detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastDetectedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when events associated with the incident were last detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`detectionTypes[]` |  `string` Output only. Detection types which are part of the incident. Examples: Flooder, OAuth Abuser, Static Content Scraper, Anomaly Detection.  
`trafficCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total traffic detected as part of the incident.  
`riskLevel` |  `enum (`[RiskLevel](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents#RiskLevel)`)` Output only. Risk level of the incident.  
`observability` |  `enum (`[Observability](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents#Observability)`)` Optional. Indicates if the user archived this incident.  
`lastObservabilityChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the incident observability was last changed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RiskLevel

RiskLevel indicates the severity of the incident.

Enums  
---  
`RISK_LEVEL_UNSPECIFIED` | Risk Level Unspecified.  
`LOW` | Risk level of the incident is low.  
`MODERATE` | Risk level of the incident is moderate.  
`SEVERE` | Risk level of the incident is severe.  
  
## Observability

The current observability of the incident.

Enums  
---  
`OBSERVABILITY_UNSPECIFIED` | The incident observability is unspecified.  
`ACTIVE` | The incident is currently active. Can change to this status from archived.  
`ARCHIVED` | The incident is currently archived and was archived by the customer.  
  
## Methods  
  
---  
  
### `[batchUpdate](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/batchUpdate)`

|  BatchUpdateSecurityIncident updates multiple existing security incidents.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/get)`

|  GetSecurityIncident gets the specified security incident.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/list)`

|  ListSecurityIncidents lists all the security incident associated with the environment.  
  
### `[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/patch)`

|  UpdateSecurityIncidents updates an existing security incident.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
