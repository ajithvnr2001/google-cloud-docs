---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder
title: Class Document.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:37.286113+00:00
---

# Class Document.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Document.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class Document.Builder

A builder of documents. This is not thread-safe.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Document.Builder

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

## Constructors 

### Builder()
    
    
    protected Builder()

Constructs a builder for a document.

## Methods 

### addFacet(Facet facet)
    
    
    public Document.Builder addFacet(Facet facet)

Adds a [Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet) to this builder.

**Parameter**  
---  
**Name** | **Description**  
`facet` | `[Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet)`  
the facet to add  
**Returns**  
---  
**Type** | **Description**  
`[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)` | this builder  
  
### addField(Field field)
    
    
    public Document.Builder addField(Field field)

Adds the field to the builder. Allows multiple fields with the same name, except that documents may only have one date and one number field for a name.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field)`  
the field to add  
**Returns**  
---  
**Type** | **Description**  
`[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)` | this builder  
  
### addField(Field.Builder builder)
    
    
    public Document.Builder addField(Field.Builder builder)

Adds the field builder to the document builder. Allows multiple fields with the same name.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)`  
the builder of the field to add  
**Returns**  
---  
**Type** | **Description**  
`[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)` | this document builder  
  
### build()
    
    
    public Document build()

Builds a valid document. The builder must have set a valid document id, and have a non-empty set of valid fields.

**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)` | the document built by this builder  
  
### setId(String documentId)
    
    
    public Document.Builder setId(String documentId)

Set the document id to a unique valid value. A valid document id must be a printable ASCII string of between 1 and DocumentChecker#MAXIMUM_DOCUMENT_ID_LENGTH characters, and also not start with '!' which is reserved. If no document id is provided, then the search service will provide one when the document is indexed.

**Parameter**  
---  
**Name** | **Description**  
`documentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the unique id for the document to be built  
**Returns**  
---  
**Type** | **Description**  
`[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)` | this builder  
  
### setLocale(Locale locale)
    
    
    public Document.Builder setLocale(Locale locale)

Sets the [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) the document is written in.

**Parameter**  
---  
**Name** | **Description**  
`locale` | `[Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)`  
the [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) the document is written in  
**Returns**  
---  
**Type** | **Description**  
`[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)` | this document builder  
  
### setRank(int rank)
    
    
    public Document.Builder setRank(int rank)

Sets the rank of this document, which determines the order of documents returned by search, if no sorting or scoring is given. If it is not specified, then the number of seconds since 2011/1/1 will be used.

**Parameter**  
---  
**Name** | **Description**  
`rank` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the rank of this document  
**Returns**  
---  
**Type** | **Description**  
`[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)` | this builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
