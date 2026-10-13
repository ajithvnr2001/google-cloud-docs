---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId
title: Google.Cloud.DevTools.Common - Class CloudWorkspaceId (3.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:04.232857+00:00
---

# Google.Cloud.DevTools.Common - Class CloudWorkspaceId (3.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.DevTools.Common - Class CloudWorkspaceId (3.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/3.2.0/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId)
  * [ 3.1.1 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/3.1.1/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/3.0.0/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/2.1.0/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId)


    
    
    public sealed class CloudWorkspaceId : IMessage<CloudWorkspaceId>, IMessage, IEquatable<CloudWorkspaceId>, IDeepCloneable<CloudWorkspaceId>

Reference documentation and code samples for the Google.Cloud.DevTools.Common class CloudWorkspaceId.

A CloudWorkspaceId is a unique identifier for a cloud workspace. A cloud workspace is a place associated with a repo where modified files can be stored before they are committed.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudWorkspaceId

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudWorkspaceId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudWorkspaceId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudWorkspaceId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DevTools.Source.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1)

## Assembly

Google.Cloud.DevTools.Common.dll

## Constructors 

### CloudWorkspaceId()
    
    
    public CloudWorkspaceId()

### CloudWorkspaceId(CloudWorkspaceId)
    
    
    public CloudWorkspaceId(CloudWorkspaceId other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudWorkspaceId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.CloudWorkspaceId)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

The unique name of the workspace within the repo. This is the name chosen by the client in the Source API's CreateWorkspace method.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RepoId
    
    
    public RepoId RepoId { get; set; }

The ID of the repo containing the workspace.

**Property Value**  
---  
**Type** | **Description**  
`[RepoId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.Common/latest/Google.Cloud.DevTools.Source.V1.RepoId)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
