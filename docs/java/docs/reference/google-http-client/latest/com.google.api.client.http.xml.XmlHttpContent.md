---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.XmlHttpContent
title: Class XmlHttpContent (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:02.781185+00:00
---

# Class XmlHttpContent (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.XmlHttpContent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class XmlHttpContent (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public class XmlHttpContent extends AbstractXmlHttpContent

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Serializes XML HTTP content based on the data key/value mapping object for an item.

Sample usage:

static void setContent(HttpRequest request, XmlNamespaceDictionary namespaceDictionary, String elementName, Object data) { request.setContent(new XmlHttpContent(namespaceDictionary, elementName, data)); }

Implementation is not thread-safe.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent) > [AbstractXmlHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.AbstractXmlHttpContent) > XmlHttpContent

## Inherited Members

[AbstractHttpContent.computeLength()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_computeLength__)

[AbstractHttpContent.computeLength(HttpContent)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_computeLength_com_google_api_client_http_HttpContent_)

[AbstractHttpContent.getCharset()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_getCharset__)

[AbstractHttpContent.getLength()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_getLength__)

[AbstractHttpContent.getMediaType()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_getMediaType__)

[AbstractHttpContent.getType()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_getType__)

[AbstractHttpContent.retrySupported()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_retrySupported__)

[AbstractXmlHttpContent.getNamespaceDictionary()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.AbstractXmlHttpContent#com_google_api_client_http_xml_AbstractXmlHttpContent_getNamespaceDictionary__)

[AbstractXmlHttpContent.setMediaType(HttpMediaType)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.AbstractXmlHttpContent#com_google_api_client_http_xml_AbstractXmlHttpContent_setMediaType_com_google_api_client_http_HttpMediaType_)

[AbstractXmlHttpContent.writeTo(OutputStream)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.AbstractXmlHttpContent#com_google_api_client_http_xml_AbstractXmlHttpContent_writeTo_java_io_OutputStream_)

[AbstractXmlHttpContent.writeTo(XmlSerializer)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.AbstractXmlHttpContent#com_google_api_client_http_xml_AbstractXmlHttpContent_writeTo_org_xmlpull_v1_XmlSerializer_)

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

## Constructors 

### XmlHttpContent(XmlNamespaceDictionary namespaceDictionary, String elementName, Object data)
    
    
    public XmlHttpContent(XmlNamespaceDictionary namespaceDictionary, String elementName, Object data)

XML namespace dictionary.

**Parameters**  
---  
**Name** | **Description**  
`namespaceDictionary` | `[XmlNamespaceDictionary](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.xml.XmlNamespaceDictionary)`  
XML namespace dictionary  
`elementName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
XML element local name, optionally prefixed by its namespace alias, for example `"atom:entry"`  
`data` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
Key/value pair data  
  
## Methods 

### getData()
    
    
    public final Object getData()

Returns the key/value pair data.

**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)` |   
  
### getElementName()
    
    
    public final String getElementName()

Returns the XML element local name, optionally prefixed by its namespace alias, for example `"atom:entry"`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### setMediaType(HttpMediaType mediaType)
    
    
    public XmlHttpContent setMediaType(HttpMediaType mediaType)

Sets the media type to use for the Content-Type header, or `null` if unspecified.

This will also overwrite any previously set parameter of the media type (for example ` "charset"`), and therefore might change other properties as well.

**Parameter**  
---  
**Name** | **Description**  
`mediaType` | `[HttpMediaType](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpMediaType)`  
  
**Returns**  
---  
**Type** | **Description**  
`[XmlHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.XmlHttpContent)` |   
**Overrides**

[AbstractXmlHttpContent.setMediaType(HttpMediaType mediaType)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.AbstractXmlHttpContent#com_google_api_client_http_xml_AbstractXmlHttpContent_setMediaType_com_google_api_client_http_HttpMediaType_)

### writeTo(XmlSerializer serializer)
    
    
    public final void writeTo(XmlSerializer serializer)

Writes the content to the given XML serializer.

**Parameter**  
---  
**Name** | **Description**  
`serializer` | `org.xmlpull.v1.XmlSerializer`  
  
**Overrides**

[AbstractXmlHttpContent.writeTo(XmlSerializer serializer)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.xml.AbstractXmlHttpContent#com_google_api_client_http_xml_AbstractXmlHttpContent_writeTo_org_xmlpull_v1_XmlSerializer_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
