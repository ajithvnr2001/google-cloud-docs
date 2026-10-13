---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.CreateJobRequest
title: Dataflow v1beta3 API - Class CreateJobRequest (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:14.589125+00:00
---

# Dataflow v1beta3 API - Class CreateJobRequest (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.CreateJobRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataflow v1beta3 API - Class CreateJobRequest (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta03 
    
    
    public sealed class CreateJobRequest : IMessage<CreateJobRequest>, IEquatable<CreateJobRequest>, IDeepCloneable<CreateJobRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataflow v1beta3 API class CreateJobRequest.

Request to create a Cloud Dataflow job.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateJobRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.CreateJobRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.CreateJobRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.CreateJobRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3)

## Assembly

Google.Cloud.Dataflow.V1Beta3.dll

## Constructors 

### CreateJobRequest()
    
    
    public CreateJobRequest()

### CreateJobRequest(CreateJobRequest)
    
    
    public CreateJobRequest(CreateJobRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.CreateJobRequest)`  
  
  
## Properties 

### Job
    
    
    public Job Job { get; set; }

The job to create.

**Property Value**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.Job)` |   
  
### Location
    
    
    public string Location { get; set; }

The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectId
    
    
    public string ProjectId { get; set; }

The ID of the Cloud Platform project that the job belongs to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReplaceJobId
    
    
    public string ReplaceJobId { get; set; }

Deprecated. This field is now in the Job message.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### View
    
    
    public JobView View { get; set; }

The level of information requested in response.

**Property Value**  
---  
**Type** | **Description**  
`[JobView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobView)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
