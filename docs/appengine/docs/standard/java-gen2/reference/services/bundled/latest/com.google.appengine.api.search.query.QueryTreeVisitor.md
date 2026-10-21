---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeVisitor
title: Interface QueryTreeVisitor<T> (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:09:47.459325+00:00
---

# Interface QueryTreeVisitor<T> (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.query.QueryTreeVisitor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface QueryTreeVisitor<T> (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface QueryTreeVisitor<T>

Defines an interface of the visitor invoked by the walker.

## Type Parameter  
  
---  
**Name** | **Description**  
`T` |   
  
## Methods 

### visitConjunction(Tree node, T context)
    
    
    public abstract void visitConjunction(Tree node, T context)

Visits a node that represents a conjunction (logical and) of conditions.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitContains(Tree node, T context)
    
    
    public abstract void visitContains(Tree node, T context)

Visits a node that represents that a field must contain a value.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitDisjunction(Tree node, T context)
    
    
    public abstract void visitDisjunction(Tree node, T context)

Visits a node that represents a disjunction (logical or) of conditions.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitEqual(Tree node, T context)
    
    
    public abstract void visitEqual(Tree node, T context)

Visits a node that represents that a field value must be greater than or equal to some specified value.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitFunction(Tree node, T context)
    
    
    public abstract void visitFunction(Tree node, T context)

Visits a node that represents a function computed on some arguments.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitFuzzy(Tree node, T context)
    
    
    public abstract void visitFuzzy(Tree node, T context)

Visits a node that represents a text field that is subject to query rewrite.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitGlobal(Tree node, T context)
    
    
    public abstract void visitGlobal(Tree node, T context)

Visits a node that represents a global field.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitGreaterOrEqual(Tree node, T context)
    
    
    public abstract void visitGreaterOrEqual(Tree node, T context)

Visits a node that represents an inequality between a field and value.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitGreaterThan(Tree node, T context)
    
    
    public abstract void visitGreaterThan(Tree node, T context)

Visits a node that represents that a field value must be greater than some specified value.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitLessOrEqual(Tree node, T context)
    
    
    public abstract void visitLessOrEqual(Tree node, T context)

Visits a node that represents that a field value must be less than or equal to some specified value.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitLessThan(Tree node, T context)
    
    
    public abstract void visitLessThan(Tree node, T context)

Visits a node that represents that a field value must be less than some specified value.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitLiteral(Tree node, T context)
    
    
    public abstract void visitLiteral(Tree node, T context)

Visits a node that represents a text field that must not be altered.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitNegation(Tree node, T context)
    
    
    public abstract void visitNegation(Tree node, T context)

Visits a node that represents a negation of conditions.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitOther(Tree node, T context)
    
    
    public abstract void visitOther(Tree node, T context)

Catch-all method for future type of query nodes.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitSequence(Tree node, T context)
    
    
    public abstract void visitSequence(Tree node, T context)

Visits a node that represents a sequence of expressions.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
### visitValue(Tree node, T context)
    
    
    public abstract void visitValue(Tree node, T context)

Visits a node that represents a constant value.

**Parameters**  
---  
**Name** | **Description**  
`node` | `org.antlr.runtime.tree.Tree`  
  
`context` | `T`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
