---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesnapshot
title: Class Pipelines.PipelineSnapshot (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:35.858458+00:00
---

# Class Pipelines.PipelineSnapshot (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesnapshot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Pipelines.PipelineSnapshot (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

Represents the results of a Firestore pipeline execution.

A `PipelineSnapshot` contains zero or more `PipelineResult` objects representing the documents returned by a pipeline query. It provides methods to iterate over the documents and access metadata about the query results.

## Implements

firestore.Pipelines.PipelineSnapshot

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Example
    
    
    typescript
    const snapshot: PipelineSnapshot = await firestore
      .pipeline()
      .collection('myCollection')
      .where(field('value').greaterThan(10))
      .execute();
    
    snapshot.results.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });
    

## Constructors 

### (constructor)(pipeline, results, executionTime, explainStats)
    
    
    constructor(pipeline: Pipeline, results: PipelineResult[], executionTime?: Timestamp, explainStats?: ExplainStats);

Constructs a new instance of the `PipelineSnapshot` class

**Parameters**  
---  
**Name** | **Description**  
`pipeline` |  `[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)`   
  
`results` |  `[PipelineResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelineresult)[]`   
  
`executionTime` |  `[Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)`   
  
`explainStats` |  `ExplainStats`   
  
  
## Properties 

### executionTime
    
    
    get executionTime(): Timestamp;

The time at which the pipeline producing this result is executed.

{Timestamp}

### explainStats
    
    
    get explainStats(): ExplainStats | undefined;

Return stats from query explain.

If `explainOptions.mode` was set to `execute` or left unset, then this returns `undefined`.

### pipeline
    
    
    get pipeline(): Pipeline;

The Pipeline on which you called `execute()` in order to get this `PipelineSnapshot`.

### results
    
    
    get results(): PipelineResult[];

An array of all the results in the `PipelineSnapshot`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
