---
url: https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.updateuserworkloadssecretrequest
title: Class protos.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:09.939519+00:00
---

# Class protos.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.updateuserworkloadssecretrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.2.0  4.0.1  3.6.0  3.2.0  2.4.0  2.3.2  2.1.2  1.0.0 

Represents an UpdateUserWorkloadsSecretRequest.

## Implements

[protos.google.cloud.orchestration.airflow.service.v1.IUpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.iupdateuserworkloadssecretrequest)

## Package

[@google-cloud/orchestration-airflow](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.orchestration.airflow.service.v1.IUpdateUserWorkloadsSecretRequest);

Constructs a new UpdateUserWorkloadsSecretRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.iupdateuserworkloadssecretrequest)`   
Properties to set  
  
## Properties 

### userWorkloadsSecret
    
    
    public userWorkloadsSecret?: (google.cloud.orchestration.airflow.service.v1.IUserWorkloadsSecret|null);

UpdateUserWorkloadsSecretRequest userWorkloadsSecret.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.orchestration.airflow.service.v1.IUpdateUserWorkloadsSecretRequest): google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest;

Creates a new UpdateUserWorkloadsSecretRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.iupdateuserworkloadssecretrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.updateuserworkloadssecretrequest)` | UpdateUserWorkloadsSecretRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest;

Decodes an UpdateUserWorkloadsSecretRequest message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.updateuserworkloadssecretrequest)` | UpdateUserWorkloadsSecretRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest;

Decodes an UpdateUserWorkloadsSecretRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.updateuserworkloadssecretrequest)` | UpdateUserWorkloadsSecretRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.orchestration.airflow.service.v1.IUpdateUserWorkloadsSecretRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateUserWorkloadsSecretRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.iupdateuserworkloadssecretrequest)`   
UpdateUserWorkloadsSecretRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.orchestration.airflow.service.v1.IUpdateUserWorkloadsSecretRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateUserWorkloadsSecretRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.iupdateuserworkloadssecretrequest)`   
UpdateUserWorkloadsSecretRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest;

Creates an UpdateUserWorkloadsSecretRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.updateuserworkloadssecretrequest)` | UpdateUserWorkloadsSecretRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateUserWorkloadsSecretRequest

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this UpdateUserWorkloadsSecretRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateUserWorkloadsSecretRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/orchestration-airflow/protos.google.cloud.orchestration.airflow.service.v1.updateuserworkloadssecretrequest)`   
UpdateUserWorkloadsSecretRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateUserWorkloadsSecretRequest message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
