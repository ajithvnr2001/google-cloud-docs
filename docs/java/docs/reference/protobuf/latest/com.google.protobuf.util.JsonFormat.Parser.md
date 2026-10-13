---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser
title: Class JsonFormat.Parser (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:26.170377+00:00
---

# Class JsonFormat.Parser (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class JsonFormat.Parser (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class JsonFormat.Parser

A Parser parses JSON to protobuf message.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > JsonFormat.Parser

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### ignoringUnknownFields()
    
    
    public JsonFormat.Parser ignoringUnknownFields()

Creates a new [Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser) configured to not throw an exception when an unknown field is encountered. The new Parser clones all other configurations from this Parser.

**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser)` |   
  
### merge(Reader json, Message.Builder builder)
    
    
    public void merge(Reader json, Message.Builder builder)

Parses from JSON into a protobuf message.

**Parameters**  
---  
**Name** | **Description**  
`json` | `[Reader](https://docs.oracle.com/javase/8/docs/api/java/io/Reader.html)`  
  
`builder` | `[Message.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.Builder)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the input is not valid JSON format or there are unknown fields in the input.  
  
### merge(String json, Message.Builder builder)
    
    
    public void merge(String json, Message.Builder builder)

Parses from JSON into a protobuf message.

**Parameters**  
---  
**Name** | **Description**  
`json` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`builder` | `[Message.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.Builder)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException)` | if the input is not valid JSON format or there are unknown fields in the input.  
  
### usingTypeRegistry(TypeRegistry registry)
    
    
    public JsonFormat.Parser usingTypeRegistry(TypeRegistry registry)

Creates a new [Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser) using the given registry. The new Parser clones all other configurations from this Parser.

**Parameter**  
---  
**Name** | **Description**  
`registry` | `[TypeRegistry](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TypeRegistry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser)` |   
  
### usingTypeRegistry(JsonFormat.TypeRegistry oldRegistry)
    
    
    public JsonFormat.Parser usingTypeRegistry(JsonFormat.TypeRegistry oldRegistry)

Creates a new [Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser) using the given registry. The new Parser clones all other configurations from this Parser.

**Parameter**  
---  
**Name** | **Description**  
`oldRegistry` | `[JsonFormat.TypeRegistry](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.TypeRegistry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
