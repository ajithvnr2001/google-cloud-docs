---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding
title: Web Security Scanner v1 API - Class Finding (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:05.271476+00:00
---

# Web Security Scanner v1 API - Class Finding (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Web Security Scanner v1 API - Class Finding (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.5.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.4.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.3.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.2.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.1.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/2.0.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/1.2.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/1.1.0/Google.Cloud.WebSecurityScanner.V1.Finding)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/1.0.0/Google.Cloud.WebSecurityScanner.V1.Finding)


    
    
    public sealed class Finding : IMessage<Finding>, IEquatable<Finding>, IDeepCloneable<Finding>, IBufferMessage, IMessage

Reference documentation and code samples for the Web Security Scanner v1 API class Finding.

A Finding resource represents a vulnerability instance identified during a ScanRun.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Finding

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.WebSecurityScanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1)

## Assembly

Google.Cloud.WebSecurityScanner.V1.dll

## Constructors 

### Finding()
    
    
    public Finding()

### Finding(Finding)
    
    
    public Finding(Finding other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding)`  
  
  
## Properties 

### Body
    
    
    public string Body { get; set; }

Output only. The body of the request that triggered the vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

Output only. The description of the vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FinalUrl
    
    
    public string FinalUrl { get; set; }

Output only. The URL where the browser lands when the vulnerability is detected.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FindingName
    
    
    public FindingName FindingName { get; set; }

[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.FindingName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding#Google_Cloud_WebSecurityScanner_V1_Finding_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.FindingName)` |   
  
### FindingType
    
    
    public string FindingType { get; set; }

Output only. The type of the Finding. Detailed and up-to-date information on findings can be found here: <https://cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Form
    
    
    public Form Form { get; set; }

Output only. An addon containing information reported for a vulnerability with an HTML form, if any.

**Property Value**  
---  
**Type** | **Description**  
`[Form](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Form)` |   
  
### FrameUrl
    
    
    public string FrameUrl { get; set; }

Output only. If the vulnerability was originated from nested IFrame, the immediate parent IFrame is reported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FuzzedUrl
    
    
    public string FuzzedUrl { get; set; }

Output only. The URL produced by the server-side fuzzer and used in the request that triggered the vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HttpMethod
    
    
    public string HttpMethod { get; set; }

Output only. The http method of the request that triggered the vulnerability, in uppercase.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name of the Finding. The name follows the format of 'projects/{projectId}/scanConfigs/{scanConfigId}/scanruns/{scanRunId}/findings/{findingId}'. The finding IDs are generated by the system.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OutdatedLibrary
    
    
    public OutdatedLibrary OutdatedLibrary { get; set; }

Output only. An addon containing information about outdated libraries.

**Property Value**  
---  
**Type** | **Description**  
`[OutdatedLibrary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.OutdatedLibrary)` |   
  
### ReproductionUrl
    
    
    public string ReproductionUrl { get; set; }

Output only. The URL containing human-readable payload that user can leverage to reproduce the vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Severity
    
    
    public Finding.Types.Severity Severity { get; set; }

Output only. The severity level of the reported vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding.Types)[Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Finding.Types.Severity)` |   
  
### TrackingId
    
    
    public string TrackingId { get; set; }

Output only. The tracking ID uniquely identifies a vulnerability instance across multiple ScanRuns.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ViolatingResource
    
    
    public ViolatingResource ViolatingResource { get; set; }

Output only. An addon containing detailed information regarding any resource causing the vulnerability such as JavaScript sources, image, audio files, etc.

**Property Value**  
---  
**Type** | **Description**  
`[ViolatingResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.ViolatingResource)` |   
  
### VulnerableHeaders
    
    
    public VulnerableHeaders VulnerableHeaders { get; set; }

Output only. An addon containing information about vulnerable or missing HTTP headers.

**Property Value**  
---  
**Type** | **Description**  
`[VulnerableHeaders](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.VulnerableHeaders)` |   
  
### VulnerableParameters
    
    
    public VulnerableParameters VulnerableParameters { get; set; }

Output only. An addon containing information about request parameters which were found to be vulnerable.

**Property Value**  
---  
**Type** | **Description**  
`[VulnerableParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.VulnerableParameters)` |   
  
### Xss
    
    
    public Xss Xss { get; set; }

Output only. An addon containing information reported for an XSS, if any.

**Property Value**  
---  
**Type** | **Description**  
`[Xss](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Xss)` |   
  
### Xxe
    
    
    public Xxe Xxe { get; set; }

Output only. An addon containing information reported for an XXE, if any.

**Property Value**  
---  
**Type** | **Description**  
`[Xxe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WebSecurityScanner.V1/latest/Google.Cloud.WebSecurityScanner.V1.Xxe)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
