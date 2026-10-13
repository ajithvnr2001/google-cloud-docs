---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages
title: REST Resource: projects.locations.datasets.hl7V2Stores.messages \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:50.047711+00:00
---

# REST Resource: projects.locations.datasets.hl7V2Stores.messages  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  REST Resource: projects.locations.datasets.hl7V2Stores.messages Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Message

A complete HL7v2 message. See [Introduction to HL7 Standards](https://www.hl7.org/implement/standards/index.cfm?ref=common) for details on the standard.

JSON representation  
---  
      
    
    {
      "name": string,
      "data": string,
      "createTime": string,
      "sendFacility": string,
      "sendTime": string,
      "messageType": string,
      "patientIds": [
        {
          object([PatientId](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#PatientId))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "parsedData": {
        object([ParsedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#ParsedData))
      },
      "schematizedData": {
        object([SchematizedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#SchematizedData))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name of the Message, of the form `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/hl7V2Stores/{hl7V2StoreId}/messages/{message_id}`.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw message bytes.A base64-encoded string.  
`createTime` |  `string(`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The datetime when the message was created. Set by the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sendFacility` |  `string` Output only. The hospital that this message came from. MSH-4.  
`sendTime` |  `string(`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The datetime the sending application sent this message. MSH-7.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`messageType` |  `string` Output only. The message type for this message. MSH-9.1.  
`patientIds[]` |  `object(`[PatientId](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#PatientId)`)` Output only. All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message.  
`labels` |  `map (key: string, value: string)` User-supplied key-value pairs used to organize HL7v2 stores.Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}No more than 64 labels can be associated with a given store.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`parsedData` |  `object(`[ParsedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#ParsedData)`)` Output only. The parsed version of the raw message data.  
`schematizedData` |  `object(`[SchematizedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#SchematizedData)`)` Output only. The parsed version of the raw message data schematized according to this store's schemas and type definitions.  
  
## PatientId

A patient identifier and associated type.

JSON representation  
---  
      
    
    {
      "value": string,
      "type": string
    }  
  
Fields  
---  
`value` |  `string` The patient's unique identifier.  
`type` |  `string` ID type. For example, MRN or NHS.  
  
## ParsedData

The content of a HL7v2 message in a structured format.

JSON representation  
---  
      
    
    {
      "segments": [
        {
          object([Segment](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#Segment))
        }
      ]
    }  
  
Fields  
---  
`segments[]` |  `object(`[Segment](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#Segment)`)`  
  
## Segment

A segment in a structured format.

JSON representation  
---  
      
    
    {
      "segmentId": string,
      "setId": string,
      "fields": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`segmentId` |  `string` A string that indicates the type of segment. For example, EVN or PID.  
`setId` |  `string` Set ID for segments that can be in a set. This can be empty if it's missing or isn't applicable.  
`fields` |  `map (key: string, value: string)` A mapping from the positional location to the value. The key string uses zero-based indexes separated by dots to identify Fields, components and sub-components. A bracket notation is also used to identify different instances of a repeated field. Regex for key: (\d+)([\d+])?(.\d+)?(.\d+)?Examples of (key, value) pairs:

  * (0.1, "hemoglobin") denotes that the first component of Field 0 has the value "hemoglobin".
  * (1.1.2, "CBC") denotes that the second sub-component of the first component of Field 1 has the value "CBC".
  * (1[0].1, "HbA1c") denotes that the first component of the first Instance of Field 1, which is repeated, has the value "HbA1c".

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## SchematizedData

The content of an HL7v2 message in a structured format as specified by a schema.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "data": string,
      "error": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`data` |  `string` JSON output of the parser.  
`error` |  `string` The error output of the parser.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create)`

|  Parses and stores an HL7v2 message.  
  
### `[delete](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/delete)`

|  Deletes an HL7v2 message.  
  
### `[get](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/get)`

|  Gets an HL7v2 message.  
  
### `[ingest](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/ingest)`

|  Parses and stores an HL7v2 message.  
  
### `[list](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/list)`

|  Lists all the messages in the given HL7v2 store with support for filtering.  
  
### `[patch](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/patch)`

|  Update the message.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
