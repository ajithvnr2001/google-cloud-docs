---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.DocumentChecker
title: Class DocumentChecker (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:26.564877+00:00
---

# Class DocumentChecker (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.DocumentChecker

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DocumentChecker (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class DocumentChecker

Checks values of a [com.google.appengine.api.search.Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DocumentChecker

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

### checkDocumentId(String documentId)
    
    
    public static String checkDocumentId(String documentId)

Checks whether a document id is valid. A document id is a non-null ASCII visible printable string of

# MAXIMUM_DOCUMENT_ID_LENGTH characters which does not start

with '!' which is reserved for system documents.

**Parameter**  
---  
**Name** | **Description**  
`documentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the document id to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked document id  
  
### checkFacetSet(DocumentPb.Document document)
    
    
    public static void checkFacetSet(DocumentPb.Document document)

Checks validity of facets in document.

**Parameter**  
---  
**Name** | **Description**  
`document` | `com.google.apphosting.api.search.DocumentPb.Document`  
  
  
### checkFieldSet(DocumentPb.Document document)
    
    
    public static void checkFieldSet(DocumentPb.Document document)

Checks whether a document's field set is valid. A field set is valid if it does not contain any number, date, or vector fields with the same name.

**Parameter**  
---  
**Name** | **Description**  
`document` | `com.google.apphosting.api.search.DocumentPb.Document`  
the document to check  
  
### checkValid(DocumentPb.Document pb)
    
    
    public static DocumentPb.Document checkValid(DocumentPb.Document pb)

Checks whether a DocumentPb.Document has a valid set of fields.

**Parameter**  
---  
**Name** | **Description**  
`pb` | `com.google.apphosting.api.search.DocumentPb.Document`  
the DocumentPb.Document protocol buffer to check  
**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.api.search.DocumentPb.Document` | the checked document  
  
### getNumberOfSecondsSince()
    
    
    public static int getNumberOfSecondsSince()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of seconds since 2011/1/1  
  
## Constructors 

### DocumentChecker()
    
    
    public DocumentChecker()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
