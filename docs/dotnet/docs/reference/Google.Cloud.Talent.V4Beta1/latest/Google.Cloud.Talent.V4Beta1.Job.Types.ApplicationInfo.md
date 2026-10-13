---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo
title: Google Cloud Talent Solution v4beta1 API - Class Job.Types.ApplicationInfo (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:55.004858+00:00
---

# Google Cloud Talent Solution v4beta1 API - Class Job.Types.ApplicationInfo (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Talent Solution v4beta1 API - Class Job.Types.ApplicationInfo (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/3.0.0-beta06/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/2.0.0-beta07/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo)


    
    
    public sealed class Job.Types.ApplicationInfo : IMessage<Job.Types.ApplicationInfo>, IEquatable<Job.Types.ApplicationInfo>, IDeepCloneable<Job.Types.ApplicationInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Talent Solution v4beta1 API class Job.Types.ApplicationInfo.

Application related details of a job posting.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Job.Types.ApplicationInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types)[ApplicationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types)[ApplicationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types)[ApplicationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Talent.V4Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1)

## Assembly

Google.Cloud.Talent.V4Beta1.dll

## Constructors 

### ApplicationInfo()
    
    
    public ApplicationInfo()

### ApplicationInfo(ApplicationInfo)
    
    
    public ApplicationInfo(Job.Types.ApplicationInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types)[ApplicationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Job.Types.ApplicationInfo)`  
  
  
## Properties 

### Emails
    
    
    public RepeatedField<string> Emails { get; }

Use this field to specify email address(es) to which resumes or applications can be sent.

The maximum number of allowed characters for each entry is 255.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Instruction
    
    
    public string Instruction { get; set; }

Use this field to provide instructions, such as "Mail your application to ...", that a candidate can follow to apply for the job.

This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags.

The maximum number of allowed characters is 3,000.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Uris
    
    
    public RepeatedField<string> Uris { get; }

Use this URI field to direct an applicant to a website, for example to link to an online application form.

The maximum number of allowed characters for each entry is 2,000.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
