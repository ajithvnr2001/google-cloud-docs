---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationRunsResponseOrBuilder
title: Interface ExportEvaluationRunsResponseOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:54.131235+00:00
---

# Interface ExportEvaluationRunsResponseOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationRunsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExportEvaluationRunsResponseOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ExportEvaluationRunsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEvaluationRunsCase()
    
    
    public abstract ExportEvaluationRunsResponse.EvaluationRunsCase getEvaluationRunsCase()

**Returns**  
---  
**Type** | **Description**  
`[ExportEvaluationRunsResponse.EvaluationRunsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationRunsResponse.EvaluationRunsCase)` |   
  
### getEvaluationRunsContent()
    
    
    public abstract ByteString getEvaluationRunsContent()

The content of the exported Evaluation Runs. This will be populated if gcs_uri was not specified in the request.

`bytes evaluation_runs_content = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The evaluationRunsContent.  
  
### getEvaluationRunsUri()
    
    
    public abstract String getEvaluationRunsUri()

The Google Cloud Storage URI folder where the exported Evaluation Runs were written. This will be populated if gcs_uri was specified in the request.

`string evaluation_runs_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The evaluationRunsUri.  
  
### getEvaluationRunsUriBytes()
    
    
    public abstract ByteString getEvaluationRunsUriBytes()

The Google Cloud Storage URI folder where the exported Evaluation Runs were written. This will be populated if gcs_uri was specified in the request.

`string evaluation_runs_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for evaluationRunsUri.  
  
### hasEvaluationRunsContent()
    
    
    public abstract boolean hasEvaluationRunsContent()

The content of the exported Evaluation Runs. This will be populated if gcs_uri was not specified in the request.

`bytes evaluation_runs_content = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the evaluationRunsContent field is set.  
  
### hasEvaluationRunsUri()
    
    
    public abstract boolean hasEvaluationRunsUri()

The Google Cloud Storage URI folder where the exported Evaluation Runs were written. This will be populated if gcs_uri was specified in the request.

`string evaluation_runs_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the evaluationRunsUri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
