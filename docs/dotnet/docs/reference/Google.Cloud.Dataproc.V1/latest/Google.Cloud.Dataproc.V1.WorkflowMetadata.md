---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata
title: Google Cloud Dataproc v1 API - Class WorkflowMetadata (5.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:11.886808+00:00
---

# Google Cloud Dataproc v1 API - Class WorkflowMetadata (5.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dataproc v1 API - Class WorkflowMetadata (5.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.28.0 (latest)  5.27.0  5.26.0  5.25.0  5.24.0  5.23.0  5.22.0  5.21.0  5.20.0  5.19.0  5.18.0  5.17.0  5.16.0  5.15.0  5.14.0  5.13.0  5.12.0  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.0.0  3.4.0  3.3.0  3.2.0  3.1.0 
    
    
    public sealed class WorkflowMetadata : IMessage<WorkflowMetadata>, IEquatable<WorkflowMetadata>, IDeepCloneable<WorkflowMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dataproc v1 API class WorkflowMetadata.

A Dataproc workflow template resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WorkflowMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[WorkflowMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WorkflowMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[WorkflowMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataproc.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1)

## Assembly

Google.Cloud.Dataproc.V1.dll

## Constructors 

### WorkflowMetadata()
    
    
    public WorkflowMetadata()

### WorkflowMetadata(WorkflowMetadata)
    
    
    public WorkflowMetadata(WorkflowMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[WorkflowMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata)`  
  
  
## Properties 

### ClusterName
    
    
    public string ClusterName { get; set; }

Output only. The name of the target cluster.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ClusterUuid
    
    
    public string ClusterUuid { get; set; }

Output only. The UUID of target cluster.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateCluster
    
    
    public ClusterOperation CreateCluster { get; set; }

Output only. The create cluster operation metadata.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.ClusterOperation)` |   
  
### DagEndTime
    
    
    public Timestamp DagEndTime { get; set; }

Output only. DAG end time, only set for workflows with [dag_timeout][google.cloud.dataproc.v1.WorkflowMetadata.dag_timeout] when DAG ends.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DagStartTime
    
    
    public Timestamp DagStartTime { get; set; }

Output only. DAG start time, only set for workflows with [dag_timeout][google.cloud.dataproc.v1.WorkflowMetadata.dag_timeout] when DAG begins.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DagTimeout
    
    
    public Duration DagTimeout { get; set; }

Output only. The timeout duration for the DAG of jobs, expressed in seconds (see [JSON representation of duration](https://developers.google.com/protocol-buffers/docs/proto3#json)).

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### DeleteCluster
    
    
    public ClusterOperation DeleteCluster { get; set; }

Output only. The delete cluster operation metadata.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.ClusterOperation)` |   
  
### EndTime
    
    
    public Timestamp EndTime { get; set; }

Output only. Workflow end time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Graph
    
    
    public WorkflowGraph Graph { get; set; }

Output only. The workflow graph.

**Property Value**  
---  
**Type** | **Description**  
`[WorkflowGraph](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowGraph)` |   
  
### Parameters
    
    
    public MapField<string, string> Parameters { get; }

Map from parameter names to values that were used for those parameters.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Output only. Workflow start time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### State
    
    
    public WorkflowMetadata.Types.State State { get; set; }

Output only. The workflow state.

**Property Value**  
---  
**Type** | **Description**  
`[WorkflowMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.WorkflowMetadata.Types.State)` |   
  
### Template
    
    
    public string Template { get; set; }

Output only. The resource name of the workflow template as described in <https://cloud.google.com/apis/design/resource_names>.

  * For `projects.regions.workflowTemplates`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`

  * For `projects.locations.workflowTemplates`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`




**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Version
    
    
    public int Version { get; set; }

Output only. The version of template at the time of workflow instantiation.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
