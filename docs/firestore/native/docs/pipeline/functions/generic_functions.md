---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/generic_functions/
title: Generic Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:55.858531+00:00
---

# Generic Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/generic_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Generic Functions Reference

## **Generic Functions**

Name  | Description   
---|---  
`CURRENT_DOCUMENT` | Returns the document currently being processed in the pipeline.   
`CONCAT` | Concatenates two or more values of same type.   
`LENGTH` | Calculates the length of a `String`, `Bytes`, `Array`, `Vector`, or `Map`.   
`REVERSE` | Reverses a `String`, `Bytes`, or `Array`.   
  
### CURRENT_DOCUMENT

**Syntax:**
    
    
    current_document() -> MAP
    

**Description:**

Evaluates to a map that holds all fields defined in the current scope. This is useful when merging or aggregating multiple documents together or when wanting to dynamically inspect the field names in the document.

For example, to get a list of documents grouped by a field:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/restaurants")
      .aggregate({
        groups: [ field("location.state").as("state") ],
        accumulators: [ arrayAgg(currentDocument().as("restaurants")) ]
       })
      .execute();
    

### CONCAT

**Syntax:**
    
    
    concat[T <: STRING | BYTES | ARRAY](values:T ...) -> T
    

**Description:**

Concatenates two or more values of same type.

**Examples:**

values | `concat(values)`  
---|---  
"abc", "def" | "abcdef"  
[1, 2], [3, 4] | [1, 2, 3, 4]  
b"abc", b"def" | b"abcdef"  
"abc", [1,2,3], "ghi" | error  
[1,2,3] | error  
"abc", null | null  
  
##### Node.js
    
    
    concat(constant("Author ID: "), field("authorId"));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L55-L55)

### Web
    
    
    concat(constant("Author ID: "), field("authorId"));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L1383-L1383)

##### Swift
    
    
    let displayString = Constant("Author ID: ").concat([Field("authorId")])
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/f3036609c93935c1dac413010ec37306c33104fe/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L36-L36)

##### Kotlin  
Android
    
    
    val displayString = constant("Author ID: ").concat(field("authorId"))
    
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1346-L1347)

##### Java  
Android
    
    
    Expression displayString = constant("Author ID: ").concat(field("authorId"));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1344-L1344)

##### Python
    
    
    Constant.of("Author ID: ").concat(Field.of("authorId"))
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L32-L32)

### LENGTH

**Syntax:**
    
    
    length[T <: STRING | BYTES | ARRAY | VECTOR | MAP](value: T) -> INT64
    

**Description:**

Calculates the length of a `String`, `Bytes`, `Array`, `Vector`, or `Map` value.

**Examples:**

value | `length(value)`  
---|---  
"hello" | 5  
[1, 2, 3, 4] | 4  
b"abcde" | 5  
null | null  
1 | error  
  
### REVERSE

**Syntax:**
    
    
    reverse[T <: STRING | BYTES | ARRAY](value: T) -> T
    

**Description:**

Reverses a `String`, `Bytes`, or `Array` value.

**Examples:**

value | `reverse(value)`  
---|---  
"hello" | "olleh"  
[1, 2, 3] | [3, 2, 1]  
b"abc" | b"cba"  
23 | error  
null | null  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
