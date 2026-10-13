---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64
title: Class Base64 (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:29.585719+00:00
---

# Class Base64 (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Base64 (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public class Base64

**Deprecated.** _use com.google.common.io.BaseEncoding#base64_

Proxy for handling Base64 encoding/decoding.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Base64

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

## Static Methods 

### decodeBase64(byte[] base64Data) (deprecated)
    
    
    public static byte[] decodeBase64(byte[] base64Data)

Decodes Base64 data into octets. Note that this method handles both URL-safe and non-URL-safe base 64 encoded inputs.

**Parameter**  
---  
**Name** | **Description**  
`base64Data` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
Byte array containing Base64 data or `null` for `null` result  
**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` | Array containing decoded data or `null` for `null` input  
  
### decodeBase64(String base64String) (deprecated)
    
    
    public static byte[] decodeBase64(String base64String)

Decodes a Base64 String into octets. Note that this method handles both URL-safe and non-URL-safe base 64 encoded strings.

For the compatibility with the old version that used Apache Commons Coded's decodeBase64, this method discards new line characters and trailing whitespaces.

**Parameter**  
---  
**Name** | **Description**  
`base64String` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
String containing Base64 data or `null` for `null` result  
**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` | Array containing decoded data or `null` for `null` input  
  
### encodeBase64(byte[] binaryData) (deprecated)
    
    
    public static byte[] encodeBase64(byte[] binaryData)

Encodes binary data using the base64 algorithm but does not chunk the output.

**Parameter**  
---  
**Name** | **Description**  
`binaryData` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
binary data to encode or `null` for `null` result  
**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` | byte[] containing Base64 characters in their UTF-8 representation or `null` for `null` input  
  
### encodeBase64String(byte[] binaryData) (deprecated)
    
    
    public static String encodeBase64String(byte[] binaryData)

Encodes binary data using the base64 algorithm but does not chunk the output.

**Parameter**  
---  
**Name** | **Description**  
`binaryData` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
binary data to encode or `null` for `null` result  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | String containing Base64 characters or `null` for `null` input  
  
### encodeBase64URLSafe(byte[] binaryData) (deprecated)
    
    
    public static byte[] encodeBase64URLSafe(byte[] binaryData)

Encodes binary data using a URL-safe variation of the base64 algorithm but does not chunk the output. The url-safe variation emits - and _ instead of + and / characters.

**Parameter**  
---  
**Name** | **Description**  
`binaryData` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
binary data to encode or `null` for `null` result  
**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` | byte[] containing Base64 characters in their UTF-8 representation or `null` for `null` input  
  
### encodeBase64URLSafeString(byte[] binaryData) (deprecated)
    
    
    public static String encodeBase64URLSafeString(byte[] binaryData)

Encodes binary data using a URL-safe variation of the base64 algorithm but does not chunk the output. The url-safe variation emits - and _ instead of + and / characters.

**Parameter**  
---  
**Name** | **Description**  
`binaryData` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
binary data to encode or `null` for `null` result  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | String containing Base64 characters or `null` for `null` input  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
