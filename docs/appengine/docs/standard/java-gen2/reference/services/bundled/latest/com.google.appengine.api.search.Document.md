---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document
title: Class Document (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:59.518855+00:00
---

# Class Document (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Document (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class Document implements Serializable

Represents a user generated document. The following example shows how to create a document consisting of a set of fields, some with plain text and some in HTML; it also adds facets to the document.
    
    
        Document document = Document.newBuilder().setId("document id")
           .setLocale(Locale.UK)
           .addField(Field.newBuilder()
               .setName("subject")
               .setText("going for dinner"))
           .addField(Field.newBuilder()
               .setName("body")
               .setHTML("I found a restaurant."))
           .addField(Field.newBuilder()
               .setName("signature")
               .setText("ten post jest przeznaczony dla odbiorcy")
               .setLocale(new Locale("pl")))
           .addFacet(Facet.withAtom("tag", "food"))
           .addFacet(Facet.withNumber("priority", 5.0))
           .build();
     

The following example shows how to access the fields within a document:
    
    
        Document document = ...
    
        for (Field field : document.getFields()) {
          switch (field.getType()) {
            case TEXT -> use(field.getText());
            case HTML -> use(field.getHtml());
            case ATOM -> use(field.getAtom());
            case DATE -> use(field.getDate());
          }
        }
     

And this example shows how to access the facets within a document:
    
    
        Document document = ...
    
        for (Facet facet : document.getFacets()) {
          switch (facet.getType()) {
            case ATOM -> use(facet.getAtom());
            case NUMBER -> use(facet.getNumber());
          }
        }
     

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Document

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### newBuilder()
    
    
    public static Document.Builder newBuilder()

Creates a new document builder. You must use this method to obtain a new builder. The returned builder must be used to specify all properties of the document. To obtain the document call the Builder#build() method on the returned builder.

**Returns**  
---  
**Type** | **Description**  
`[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)` | a builder which constructs a document object  
  
## Constructors 

### Document(Document.Builder builder)
    
    
    protected Document(Document.Builder builder)

Constructs a document with the given builder.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[Document.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)`  
the builder capable of building a document  
  
## Methods 

### equals(Object object)
    
    
    public boolean equals(Object object)

**Parameter**  
---  
**Name** | **Description**  
`object` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getFacetCount(String name)
    
    
    public int getFacetCount(String name)

Returns the number of times a facet with the given name is present in this document.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the facet to be counted  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of times a facet with the given name is present  
  
### getFacetNames()
    
    
    public Set<String> getFacetNames()

Returns an unmodifiable [Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html) of the facet names in the document

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getFacets()
    
    
    public Iterable<Facet> getFacets()

Returns an iterable of [Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet) in the document

**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet)>` |   
  
### getFacets(String name)
    
    
    public Iterable<Facet> getFacets(String name)

Returns an iterable of all facets with the given name.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the facet whose values are to be returned  
**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet)>` | an unmodifiable [Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html) of [Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet) with the given name or `null`  
  
### getFieldCount(String name)
    
    
    public int getFieldCount(String name)

Returns the number of times a field with the given name is present in this document.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the field to be counted  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of times a field with the given name is present  
  
### getFieldNames()
    
    
    public Set<String> getFieldNames()

Returns an unmodifiable [Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html) of the field names in the document

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getFields()
    
    
    public Iterable<Field> getFields()

Returns an iterable of [Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field) in the document

**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field)>` |   
  
### getFields(String name)
    
    
    public Iterable<Field> getFields(String name)

Returns an iterable of all fields with the given name.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the field whose values are to be returned  
**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field)>` | an unmodifiable [Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html) of [Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field) with the given name or `null`  
  
### getId()
    
    
    public String getId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the id of the document  
  
### getLocale()
    
    
    public Locale getLocale()

**Returns**  
---  
**Type** | **Description**  
`[Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)` | the [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) the document is written in. Can be null  
  
### getOnlyFacet(String name)
    
    
    public Facet getOnlyFacet(String name)

Returns the single facet with the given name.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the facet to return  
**Returns**  
---  
**Type** | **Description**  
`[Facet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Facet)` | the single facet with name  
  
### getOnlyField(String name)
    
    
    public Field getOnlyField(String name)

Returns the single field with the given name.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the field to return  
**Returns**  
---  
**Type** | **Description**  
`[Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field)` | the single field with name  
  
### getRank()
    
    
    public int getRank()

Returns the rank of this document. A document's rank is used to determine the default order in which documents are returned by search, if no sorting or scoring is specified.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the rank of this document  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
