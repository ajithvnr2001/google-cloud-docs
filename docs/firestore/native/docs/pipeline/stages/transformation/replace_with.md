---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/replace_with/
title: Replace With (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:21.180577+00:00
---

# Replace With (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/replace_with/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Replace With (Transformation Stage)

## Description

Replaces fields in the existing document with the fields in a given expression.

The expression can either be a literal map or an expression that evaluates to a map. If a given expression does not evaluate to a map, this stage returns an error.

There are 3 supported modes:

  * `full_replace`: Replaces the entire document with the result of the given expression, omitting fields that don't appear in it.
  * `merge_overwrite_existing`: Merges the expression with the existing document, overwriting field values in the document with values in the expression
  * `merge_keep_existing`: Merges the expression with the existing document, only adding field values when one does not exist in the document.



## Examples

Create a cities collection with the following documents:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francisco", population: 800000, location: {country: "USA", state: "California"}});
    await db.collection("cities").doc("TO").set({name: "Toronto", population:  3000000, province: "ON", location: {country: "Canada", province: "Ontario"}});
    await db.collection("cities").doc("NY").set({name: "New York", location: {country: "USA", state: "New York"}});
    await db.collection("cities").cov("AT").set({name: "Atlantis", population: null});
    

#### Using the full_replace mode to get a mutated version of the document

Extract the nested location field, discarding all other data:

##### Node.js
    
    
      const names = await db.pipeline()
        .collection("/cities")
        .replace_with(Field.of("location"), "full_replace")
        .execute();
        

##### Java
    
    
    Pipeline.Snapshot names =
        firestore.pipeline().collection("cities").replaceWith(field("location")).execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L450-L451)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("cities").
    	ReplaceWith(firestore.FieldOf("location")).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_general.go#L980-L983)

Which produces the following documents:
    
    
    { country: "USA", state: "California" },
    { country: "Canada", province: "Ontario" },
    { country: "USA", state: "New York" },
    { }
    

#### Using the merge_overwrite_existing mode to set fields

Set the population field of all documents to 0, overwriting existing values:

##### Node.js
    
    
      const censoredResults = await db.pipeline()
        .collection("/cities")
        .replace_with(map("population", 0), "merge_overwrite_existing")
        .execute();
        

Which produces the following documents:
    
    
    {name: "San Francisco", population: 0, location: {country: "USA", state: "California"}},
    {name: "Toronto", population: 0, province: "ON", location: {country: "Canada", province: "Ontario"}},
    {name: "New York", population: 0, location: {country: "USA", state: "New York"}},
    {name: "Atlantis", population: 0}
    

#### Using the merge_keep_existing mode to add a default value

Setting a default value for location when it doesn't appear in a document:

##### Node.js
    
    
      const defaultedResults = await db.pipeline()
        .collection("/cities")
        .replace_with(map("location", "unknown"), "merge_keep_existing")
        .execute();
        

Which produces the following documents:
    
    
    { name: "San Francisco", population: 800000, location: { country: "USA", state: "California" } },
    { name: "Toronto", province: "ON", population: 3000000, location: { country: "Canada", province: "Ontario" } },
    { name: "New York", location: { country: "USA", state: "New York" } },
    { name: "Atlantis", population: null, location: "unknown" }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
