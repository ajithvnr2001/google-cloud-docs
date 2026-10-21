---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts.documents
title: REST Resource: projects.alerts.documents \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:39.447135+00:00
---

# REST Resource: projects.alerts.documents  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts.documents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  REST Resource: projects.alerts.documents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AlertDocument
    * JSON representation
  * AlertDocumentTranslation
    * JSON representation
  * Methods



## Resource: AlertDocument

A document that is associated with an alert.

JSON representation  
---  
      
    
    {
      "name": string,
      "content": string,
      "author": string,
      "createTime": string,
      "languageCode": string,
      "title": string,
      "aiSummary": string,
      "translation": {
        object ([AlertDocumentTranslation](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts.documents#AlertDocumentTranslation))
      },
      "source": string,
      "sourceUri": string,
      "ingestTime": string,
      "collectionTime": string,
      "sourceUpdateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Server generated name for the alert document. format is projects/{project}/alerts/{alert}/documents/{document}  
`content` |  `string` Output only. The content of the document.  
`author` |  `string` Output only. The author of the document.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the document was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`languageCode` |  `string` Output only. The language code of the document.  
`title` |  `string` Output only. The title of the document, if available.  
`aiSummary` |  `string` Output only. AI summary of the finding.  
`translation` |  `object (`[AlertDocumentTranslation](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts.documents#AlertDocumentTranslation)`)` Output only. The translation of the document, if available.  
`source` |  `string` Output only. Source of the intel item, e.g. DarkMarket.  
`sourceUri` |  `string` Output only. URI of the intel item from the source.  
`ingestTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when GTI received the intel.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`collectionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the origin source collected the intel.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sourceUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the intel was last updated by the source.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## AlertDocumentTranslation

The translation of an alert document.

JSON representation  
---  
      
    
    {
      "translatedTitle": string,
      "translatedContent": string
    }  
  
Fields  
---  
`translatedTitle` |  `string` Output only. The translated title of the document.  
`translatedContent` |  `string` Output only. The translated content of the document.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts.documents/get)`

|  Gets a specific document associated with an alert.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
