---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext
title: Class QueryTreeContext<T> (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:54:48.733898+00:00
---

# Class QueryTreeContext<T> (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class QueryTreeContext<T> (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class QueryTreeContext<T>

The base class for specific query tree context used by the walker. This class is used to maintain additional information gathered while walking the tree. On this level it is used to collect return type information.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QueryTreeContext<T>

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

## Type Parameter  
  
---  
**Name** | **Description**  
`T` |   
  
## Constructors 

### QueryTreeContext()
    
    
    protected QueryTreeContext()

## Methods 

### addChild()
    
    
    public T addChild()

**Returns**  
---  
**Type** | **Description**  
`T` | a child context for this context  
  
### addReturnType(QueryTreeContext.Type type)
    
    
    public void addReturnType(QueryTreeContext.Type type)

**Parameter**  
---  
**Name** | **Description**  
`type` | `[QueryTreeContext.Type](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.Type)`  
additional type to be added to current return types  
  
### children()
    
    
    public Iterable<T> children()

**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<T>` | iterable over all children contexts  
  
### getChild(int index)
    
    
    public T getChild(int index)

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the index of the child to get  
**Returns**  
---  
**Type** | **Description**  
`T` | the child context at the given index  
  
### getChildCount()
    
    
    public int getChildCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of children contexts  
  
### getCommonReturnTypes(T other)
    
    
    public Set<QueryTreeContext.Type> getCommonReturnTypes(T other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `T`  
the other context whose types are to be inspected  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Type](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.Type)>` | a set of types common to this and the other context  
  
### getReturnTypes()
    
    
    public Set<QueryTreeContext.Type> getReturnTypes()

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Type](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.Type)>` | the set of return types  
  
### getText()
    
    
    public String getText()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | sets the text associated with this context  
  
### inDisjunction()
    
    
    public boolean inDisjunction()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if this context's lowest ancester compounding operator (AND, OR) is a disjunction.  
  
### isCompatibleWith(QueryTreeContext.Type returnType)
    
    
    public boolean isCompatibleWith(QueryTreeContext.Type returnType)

**Parameter**  
---  
**Name** | **Description**  
`returnType` | `[QueryTreeContext.Type](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.Type)`  
the type to be checked against types of this context  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | whether or not it is compatible with at least one type  
  
### isField()
    
    
    public boolean isField()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | returns if this context represents a field of a document  
  
### isFunction()
    
    
    public boolean isFunction()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | if this context represents a function  
  
### isFuzzy()
    
    
    public boolean isFuzzy()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | whether or not the value associated with this context is rewritable  
  
### isLiteral()
    
    
    public boolean isLiteral()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | if this context represents a literal constant  
  
### isPhrase()
    
    
    public boolean isPhrase()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | whether or not this context represents a phrase (quoted text)  
  
### isStrict()
    
    
    public boolean isStrict()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | whether or not the value associated with this context must not be rewritten  
  
### newChildContext()
    
    
    protected abstract T newChildContext()

**Returns**  
---  
**Type** | **Description**  
`T` | a new child of type T  
  
### setInDisjunction(boolean inDisjunction)
    
    
    public void setInDisjunction(boolean inDisjunction)

**Parameter**  
---  
**Name** | **Description**  
`inDisjunction` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setKind(QueryTreeContext.Kind kind)
    
    
    public void setKind(QueryTreeContext.Kind kind)

**Parameter**  
---  
**Name** | **Description**  
`kind` | `[QueryTreeContext.Kind](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.Kind)`  
the kind of the  
  
### setReturnType(QueryTreeContext.Type type)
    
    
    public void setReturnType(QueryTreeContext.Type type)

**Parameter**  
---  
**Name** | **Description**  
`type` | `[QueryTreeContext.Type](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.Type)`  
the unique return type for this context  
  
### setReturnTypes(Set<QueryTreeContext.Type> type)
    
    
    public void setReturnTypes(Set<QueryTreeContext.Type> type)

**Parameter**  
---  
**Name** | **Description**  
`type` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Type](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.Type)>`  
a set of types to be set as the only return types  
  
### setRewriteMode(QueryTreeContext.RewriteMode mode)
    
    
    public void setRewriteMode(QueryTreeContext.RewriteMode mode)

**Parameter**  
---  
**Name** | **Description**  
`mode` | `[QueryTreeContext.RewriteMode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeContext.RewriteMode)`  
the rewrite mode for the value represented by this context  
  
### setText(String text)
    
    
    public void setText(String text)

**Parameter**  
---  
**Name** | **Description**  
`text` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
returns the text associated with this context  
  
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
