---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerGrpc.AsyncService
title: Interface ParameterManagerGrpc.AsyncService (0.43.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:55.777370+00:00
---

# Interface ParameterManagerGrpc.AsyncService (0.43.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ParameterManagerGrpc.AsyncService (0.43.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.43.0 (latest)  0.39.0  0.38.0  0.37.0  0.35.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.24.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.14.0  0.12.0  0.11.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ParameterManagerGrpc.AsyncService

Service describing handlers for resources

## Methods 

### createParameter(CreateParameterRequest request, StreamObserver<Parameter> responseObserver)
    
    
    public default void createParameter(CreateParameterRequest request, StreamObserver<Parameter> responseObserver)

Creates a new Parameter in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateParameterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.CreateParameterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter)>`  
  
  
### createParameterVersion(CreateParameterVersionRequest request, StreamObserver<ParameterVersion> responseObserver)
    
    
    public default void createParameterVersion(CreateParameterVersionRequest request, StreamObserver<ParameterVersion> responseObserver)

Creates a new ParameterVersion in a given project, location, and parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateParameterVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.CreateParameterVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion)>`  
  
  
### createTemplate(CreateTemplateRequest request, StreamObserver<Template> responseObserver)
    
    
    public default void createTemplate(CreateTemplateRequest request, StreamObserver<Template> responseObserver)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.CreateTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Template)>`  
  
  
### createTemplateVersion(CreateTemplateVersionRequest request, StreamObserver<TemplateVersion> responseObserver)
    
    
    public default void createTemplateVersion(CreateTemplateVersionRequest request, StreamObserver<TemplateVersion> responseObserver)

Creates a new TemplateVersion in a given project, location, and template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.CreateTemplateVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TemplateVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.TemplateVersion)>`  
  
  
### deleteParameter(DeleteParameterRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteParameter(DeleteParameterRequest request, StreamObserver<Empty> responseObserver)

Deletes a single Parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteParameterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.DeleteParameterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteParameterVersion(DeleteParameterVersionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteParameterVersion(DeleteParameterVersionRequest request, StreamObserver<Empty> responseObserver)

Deletes a single ParameterVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteParameterVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.DeleteParameterVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteTemplate(DeleteTemplateRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteTemplate(DeleteTemplateRequest request, StreamObserver<Empty> responseObserver)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.DeleteTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteTemplateVersion(DeleteTemplateVersionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteTemplateVersion(DeleteTemplateVersionRequest request, StreamObserver<Empty> responseObserver)

Deletes a single TemplateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.DeleteTemplateVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getParameter(GetParameterRequest request, StreamObserver<Parameter> responseObserver)
    
    
    public default void getParameter(GetParameterRequest request, StreamObserver<Parameter> responseObserver)

Gets details of a single Parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetParameterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.GetParameterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter)>`  
  
  
### getParameterVersion(GetParameterVersionRequest request, StreamObserver<ParameterVersion> responseObserver)
    
    
    public default void getParameterVersion(GetParameterVersionRequest request, StreamObserver<ParameterVersion> responseObserver)

Gets details of a single ParameterVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetParameterVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.GetParameterVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion)>`  
  
  
### getTemplate(GetTemplateRequest request, StreamObserver<Template> responseObserver)
    
    
    public default void getTemplate(GetTemplateRequest request, StreamObserver<Template> responseObserver)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.GetTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Template)>`  
  
  
### getTemplateVersion(GetTemplateVersionRequest request, StreamObserver<TemplateVersion> responseObserver)
    
    
    public default void getTemplateVersion(GetTemplateVersionRequest request, StreamObserver<TemplateVersion> responseObserver)

Gets details of a single TemplateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.GetTemplateVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TemplateVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.TemplateVersion)>`  
  
  
### listParameterVersions(ListParameterVersionsRequest request, StreamObserver<ListParameterVersionsResponse> responseObserver)
    
    
    public default void listParameterVersions(ListParameterVersionsRequest request, StreamObserver<ListParameterVersionsResponse> responseObserver)

Lists ParameterVersions in a given project, location, and parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListParameterVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListParameterVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsResponse)>`  
  
  
### listParameters(ListParametersRequest request, StreamObserver<ListParametersResponse> responseObserver)
    
    
    public default void listParameters(ListParametersRequest request, StreamObserver<ListParametersResponse> responseObserver)

Lists Parameters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParametersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParametersResponse)>`  
  
  
### listTemplateVersions(ListTemplateVersionsRequest request, StreamObserver<ListTemplateVersionsResponse> responseObserver)
    
    
    public default void listTemplateVersions(ListTemplateVersionsRequest request, StreamObserver<ListTemplateVersionsResponse> responseObserver)

Lists TemplateVersions in a given project, location, and template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplateVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListTemplateVersionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTemplateVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListTemplateVersionsResponse)>`  
  
  
### listTemplates(ListTemplatesRequest request, StreamObserver<ListTemplatesResponse> responseObserver)
    
    
    public default void listTemplates(ListTemplatesRequest request, StreamObserver<ListTemplatesResponse> responseObserver)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListTemplatesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListTemplatesResponse)>`  
  
  
### renderParameterVersion(RenderParameterVersionRequest request, StreamObserver<RenderParameterVersionResponse> responseObserver)
    
    
    public default void renderParameterVersion(RenderParameterVersionRequest request, StreamObserver<RenderParameterVersionResponse> responseObserver)

Gets rendered version of a ParameterVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RenderParameterVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RenderParameterVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse)>`  
  
  
### renderTemplateVersion(RenderTemplateVersionRequest request, StreamObserver<RenderTemplateVersionResponse> responseObserver)
    
    
    public default void renderTemplateVersion(RenderTemplateVersionRequest request, StreamObserver<RenderTemplateVersionResponse> responseObserver)

Gets rendered version of a TemplateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RenderTemplateVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderTemplateVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RenderTemplateVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderTemplateVersionResponse)>`  
  
  
### updateParameter(UpdateParameterRequest request, StreamObserver<Parameter> responseObserver)
    
    
    public default void updateParameter(UpdateParameterRequest request, StreamObserver<Parameter> responseObserver)

Updates a single Parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateParameterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.UpdateParameterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter)>`  
  
  
### updateParameterVersion(UpdateParameterVersionRequest request, StreamObserver<ParameterVersion> responseObserver)
    
    
    public default void updateParameterVersion(UpdateParameterVersionRequest request, StreamObserver<ParameterVersion> responseObserver)

Updates a single ParameterVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateParameterVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.UpdateParameterVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion)>`  
  
  
### updateTemplate(UpdateTemplateRequest request, StreamObserver<Template> responseObserver)
    
    
    public default void updateTemplate(UpdateTemplateRequest request, StreamObserver<Template> responseObserver)

Updates a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.UpdateTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Template)>`  
  
  
### updateTemplateVersion(UpdateTemplateVersionRequest request, StreamObserver<TemplateVersion> responseObserver)
    
    
    public default void updateTemplateVersion(UpdateTemplateVersionRequest request, StreamObserver<TemplateVersion> responseObserver)

Updates a single TemplateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.UpdateTemplateVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TemplateVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.TemplateVersion)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
