---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource
title: Cloud Functions v2 API - Class RepoSource (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:12.620932+00:00
---

# Cloud Functions v2 API - Class RepoSource (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2 API - Class RepoSource (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.7.0/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.6.0/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.5.0/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.4.0/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.3.0/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.2.0/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.1.0/Google.Cloud.Functions.V2.RepoSource)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.0.0/Google.Cloud.Functions.V2.RepoSource)


    
    
    public sealed class RepoSource : IMessage<RepoSource>, IEquatable<RepoSource>, IDeepCloneable<RepoSource>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v2 API class RepoSource.

Location of the source in a Google Cloud Source Repository.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RepoSource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RepoSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RepoSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RepoSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2)

## Assembly

Google.Cloud.Functions.V2.dll

## Constructors 

### RepoSource()
    
    
    public RepoSource()

### RepoSource(RepoSource)
    
    
    public RepoSource(RepoSource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RepoSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource)`  
  
  
## Properties 

### BranchName
    
    
    public string BranchName { get; set; }

Regex matching branches to build.

The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CommitSha
    
    
    public string CommitSha { get; set; }

Explicit commit SHA to build.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Dir
    
    
    public string Dir { get; set; }

Directory, relative to the source root, in which to run the build.

This must be a relative path. If a step's `dir` is specified and is an absolute path, this value is ignored for that step's execution. eg. helloworld (no leading slash allowed)

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasBranchName
    
    
    public bool HasBranchName { get; }

Gets whether the "branch_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCommitSha
    
    
    public bool HasCommitSha { get; }

Gets whether the "commit_sha" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTagName
    
    
    public bool HasTagName { get; }

Gets whether the "tag_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InvertRegex
    
    
    public bool InvertRegex { get; set; }

Only trigger a build if the revision regex does NOT match the revision regex.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ProjectId
    
    
    public string ProjectId { get; set; }

ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RepoName
    
    
    public string RepoName { get; set; }

Name of the Cloud Source Repository.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RevisionCase
    
    
    public RepoSource.RevisionOneofCase RevisionCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RepoSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource)[RevisionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.RepoSource.RevisionOneofCase)` |   
  
### TagName
    
    
    public string TagName { get; set; }

Regex matching tags to build.

The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
