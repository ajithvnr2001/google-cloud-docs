---
url: https://docs.cloud.google.com/php/docs/reference/gax/latest/Serializer/
title: Google API Core Client - Class Serializer (1.51.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:44.190659+00:00
---

# Google API Core Client - Class Serializer (1.51.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/gax/latest/Serializer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Core Client - Class Serializer (1.51.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.51.0 (latest)  1.46.0  1.43.0  1.42.5  1.40.0  1.38.2  1.36.1  1.35.1 

Reference documentation and code samples for the Google API Core Client class Serializer.

Collection of methods to help with serialization of protobuf objects

## Namespace

Google \ ApiCore

## Methods 

### __construct

Serializer constructor.

**Parameters**  
---  
**Name** | **Description**  
`fieldTransformers` |  `array`   
An array mapping field names to transformation functions  
`messageTypeTransformers` |  `array`   
An array mapping message names to transformation functions  
`decodeFieldTransformers` |  `array`   
An array mapping field names to transformation functions  
`decodeMessageTypeTransformers` |  `array`   
An array mapping message names to transformation functions  
`customEncoders` |  `mixed`   
  
  
### encodeMessage

Encode protobuf message as a PHP array

**Parameter**  
---  
**Name** | **Description**  
`message` |  `mixed`   
  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### decodeMessage

Decode PHP array into the specified protobuf message

**Parameters**  
---  
**Name** | **Description**  
`message` |  `mixed`   
  
`data` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`mixed` |   
  
### static::serializeToJson

**Parameter**  
---  
**Name** | **Description**  
`message` |  `[Google\Protobuf\Internal\Message](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.Message.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | Json representation of $message  
  
### static::serializeToPhpArray

**Parameter**  
---  
**Name** | **Description**  
`message` |  `[Google\Protobuf\Internal\Message](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.Message.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`array` | PHP array representation of $message  
  
### static::decodeMetadata

Decode metadata received from gRPC status object

**Parameters**  
---  
**Name** | **Description**  
`metadata` |  `array`   
  
`errors` |  `null|array`   
  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### static::decodeAnyMessages

Decode an array of Any messages into a printable PHP array.

**Parameter**  
---  
**Name** | **Description**  
`anyArray` |  `iterable`   
  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### static::getGetter

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | Getter function  
  
### static::getSetter

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | Setter function  
  
### static::toSnakeCase

Convert string from camelCase to snake_case

**Parameter**  
---  
**Name** | **Description**  
`key` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### static::toCamelCase

Convert string from snake_case to camelCase

**Parameter**  
---  
**Name** | **Description**  
`key` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### static::loadKnownMetadataTypes

## Constants 

### MAP_KEY_FIELD_NAME
    
    
    Value: 'key'

### MAP_VALUE_FIELD_NAME
    
    
    Value: 'value'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
