---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetSpaceRequestOrBuilder
title: Interface GetSpaceRequestOrBuilder (0.66.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:30.442984+00:00
---

# Interface GetSpaceRequestOrBuilder (0.66.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetSpaceRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GetSpaceRequestOrBuilder (0.66.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.66.0 (latest)  0.62.0  0.61.0  0.60.0  0.58.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.47.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface GetSpaceRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getName()
    
    
    public abstract String getName()

Required. Resource name of the space.

Format: `spaces/{space}` or `spaces/{meetingCode}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

`{meetingCode}` is an alias for the space. It's a typeable, unique character string and is non-case sensitive. For example, `abc-mnop-xyz`. The maximum length is 128 characters.

A `meetingCode` shouldn't be stored long term as it can become dissociated from a meeting space and can be reused for different meeting spaces in the future. Generally, a `meetingCode` expires 365 days after last use. For more information, see [Learn about meeting codes in Google Meet](https://support.google.com/meet/answer/10710509).

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space).

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Resource name of the space.

Format: `spaces/{space}` or `spaces/{meetingCode}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

`{meetingCode}` is an alias for the space. It's a typeable, unique character string and is non-case sensitive. For example, `abc-mnop-xyz`. The maximum length is 128 characters.

A `meetingCode` shouldn't be stored long term as it can become dissociated from a meeting space and can be reused for different meeting spaces in the future. Generally, a `meetingCode` expires 365 days after last use. For more information, see [Learn about meeting codes in Google Meet](https://support.google.com/meet/answer/10710509).

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space).

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
