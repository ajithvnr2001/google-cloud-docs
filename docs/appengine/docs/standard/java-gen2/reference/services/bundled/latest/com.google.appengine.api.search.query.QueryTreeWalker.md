---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeWalker
title: Class QueryTreeWalker<T> (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:06:51.683406+00:00
---

# Class QueryTreeWalker<T> (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeWalker

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class QueryTreeWalker<T> (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class QueryTreeWalker<T>

The walking of the query tree. This class takes care of visiting a tree resulting from parsing a query. As it traverses the tree it calls appropriate methods of the visitor, set at the construction time. The class uses a depth-first search, visiting all children of a node, before visiting the node. The visit is done by calling an appropriate method of the visitor. Typical code should match the following pattern:
    
    
     class MyVisitor implements QueryTreeVisitor {
       ...
     }
     class MyContext extends QueryTreeContext<MyContext> {
       ...
       @Override
       protected MyContext newChildContext() {
         return new MyContext();
       }
     }
    
     MyContext context = new MyContext();
     QueryTreeWalker<MyContext> walker = new QueryTreeWalker<MyContext>(new MyVisitor());
     Tree root = parser.query(queryStr);
     walker.walk(root, context);
     // retrieve whatever information you need from context
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QueryTreeWalker<T>

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
  
## Static Methods 

### simplify(Tree tree)
    
    
    public static Tree simplify(Tree tree)

**Parameter**  
---  
**Name** | **Description**  
`tree` | `org.antlr.runtime.tree.Tree`  
  
**Returns**  
---  
**Type** | **Description**  
`org.antlr.runtime.tree.Tree` |   
  
## Constructors 

### QueryTreeWalker(QueryTreeVisitor<T> visitor)
    
    
    public QueryTreeWalker(QueryTreeVisitor<T> visitor)

Creates a new query walker that calls the given `visitor`.

**Parameter**  
---  
**Name** | **Description**  
`visitor` | `[QueryTreeVisitor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeVisitor)<T>`  
the visitor to be called by this walker  
  
## Methods 

### postBooleanExpression(T context)
    
    
    protected void postBooleanExpression(T context)

**Parameter**  
---  
**Name** | **Description**  
`context` | `T`  
  
  
### walk(Tree tree, T context)
    
    
    public void walk(Tree tree, T context)

**Parameters**  
---  
**Name** | **Description**  
`tree` | `org.antlr.runtime.tree.Tree`  
the tree to be walked  
`context` | `T`  
the context in which the tree is walked  
**Exceptions**  
---  
**Type** | **Description**  
`[QueryTreeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeException)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
