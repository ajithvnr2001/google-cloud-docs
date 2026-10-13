---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader
title: Class PemReader (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:33.839059+00:00
---

# Class PemReader (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PemReader (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public final class PemReader

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
PEM file reader.

Supports reading any PEM stream that contains Base64 encoded content stored inside ` "-----BEGIN ...-----"` and `"-----END ...-----"` tags. Each call to [#readNextSection()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader#com_google_api_client_util_PemReader_readNextSection__) parses the next section in the PEM file. If you need a section of a certain title use [#readNextSection(String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader#com_google_api_client_util_PemReader_readNextSection_java_lang_String_), for example `readNextSection("PRIVATE KEY")`. To ensure that the stream is closed properly, call [#close()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader#com_google_api_client_util_PemReader_close__) in a finally block.

As a convenience, use [#readFirstSectionAndClose(Reader)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader#com_google_api_client_util_PemReader_readFirstSectionAndClose_java_io_Reader_) or [#readFirstSectionAndClose(Reader, String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader#com_google_api_client_util_PemReader_readFirstSectionAndClose_java_io_Reader_java_lang_String_) for the common case of only a single section in a PEM file (or only a single section of a given title).

Limitations:

  * Assumes the PEM file section content is not encrypted and cannot handle the case of any headers inside the BEGIN and END tag. 
  * It also ignores any attributes associated with any PEM file section. 



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PemReader

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

### readFirstSectionAndClose(Reader reader)
    
    
    public static PemReader.Section readFirstSectionAndClose(Reader reader)

Reads the first section in the PEM file, and then closes the reader.

**Parameter**  
---  
**Name** | **Description**  
`reader` | `[Reader](https://docs.oracle.com/javase/8/docs/api/java/io/Reader.html)`  
reader  
**Returns**  
---  
**Type** | **Description**  
`[PemReader.Section](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader.Section)` | first section found or `null` for none found  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### readFirstSectionAndClose(Reader reader, String titleToLookFor)
    
    
    public static PemReader.Section readFirstSectionAndClose(Reader reader, String titleToLookFor)

Reads the first section in the PEM file, optionally based on a title to look for, and then closes the reader.

**Parameters**  
---  
**Name** | **Description**  
`reader` | `[Reader](https://docs.oracle.com/javase/8/docs/api/java/io/Reader.html)`  
reader  
`titleToLookFor` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
title to look for or `null` for any title  
**Returns**  
---  
**Type** | **Description**  
`[PemReader.Section](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader.Section)` | first section found or `null` for none found  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
## Constructors 

### PemReader(Reader reader)
    
    
    public PemReader(Reader reader)

**Parameter**  
---  
**Name** | **Description**  
`reader` | `[Reader](https://docs.oracle.com/javase/8/docs/api/java/io/Reader.html)`  
reader  
  
## Methods 

### close()
    
    
    public void close()

Closes the reader.

To ensure that the stream is closed properly, call [#close()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader#com_google_api_client_util_PemReader_close__) in a finally block.

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### readNextSection()
    
    
    public PemReader.Section readNextSection()

Reads the next section in the PEM file or `null` for end of file.

**Returns**  
---  
**Type** | **Description**  
`[PemReader.Section](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader.Section)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### readNextSection(String titleToLookFor)
    
    
    public PemReader.Section readNextSection(String titleToLookFor)

Reads the next section in the PEM file, optionally based on a title to look for.

**Parameter**  
---  
**Name** | **Description**  
`titleToLookFor` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
title to look for or `null` for any title  
**Returns**  
---  
**Type** | **Description**  
`[PemReader.Section](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.PemReader.Section)` | next section or `null` for end of file  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
