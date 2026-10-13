---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductInputsServiceGrpc.AsyncService
title: Interface CssProductInputsServiceGrpc.AsyncService (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:53.917442+00:00
---

# Interface CssProductInputsServiceGrpc.AsyncService (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductInputsServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CssProductInputsServiceGrpc.AsyncService (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface CssProductInputsServiceGrpc.AsyncService

Service to use CssProductInput resource. This service helps to insert/update/delete CSS Products.

## Methods 

### deleteCssProductInput(DeleteCssProductInputRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteCssProductInput(DeleteCssProductInputRequest request, StreamObserver<Empty> responseObserver)

Deletes a CSS Product input from your CSS Center account. After a delete it may take several minutes until the input is no longer available.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCssProductInputRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.DeleteCssProductInputRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### insertCssProductInput(InsertCssProductInputRequest request, StreamObserver<CssProductInput> responseObserver)
    
    
    public default void insertCssProductInput(InsertCssProductInputRequest request, StreamObserver<CssProductInput> responseObserver)

Uploads a CssProductInput to your CSS Center account. If an input with the same contentLanguage, identity, feedLabel and feedId already exists, this method replaces that entry. After inserting, updating, or deleting a CSS Product input, it may take several minutes before the processed CSS Product can be retrieved.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertCssProductInputRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.InsertCssProductInputRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CssProductInput](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductInput)>`  
  
  
### updateCssProductInput(UpdateCssProductInputRequest request, StreamObserver<CssProductInput> responseObserver)
    
    
    public default void updateCssProductInput(UpdateCssProductInputRequest request, StreamObserver<CssProductInput> responseObserver)

Updates the existing Css Product input in your CSS Center account. After inserting, updating, or deleting a CSS Product input, it may take several minutes before the processed Css Product can be retrieved.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCssProductInputRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.UpdateCssProductInputRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CssProductInput](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductInput)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
