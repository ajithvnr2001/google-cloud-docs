---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3
title: Google Cloud OS Config v1alpha API - Class CVSSv3 (2.0.0-alpha07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:53.912569+00:00
---

# Google Cloud OS Config v1alpha API - Class CVSSv3 (2.0.0-alpha07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Config v1alpha API - Class CVSSv3 (2.0.0-alpha07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)
  * [ 2.0.0-alpha06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/2.0.0-alpha06/Google.Cloud.OsConfig.V1Alpha.CVSSv3)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/1.0.0-alpha04/Google.Cloud.OsConfig.V1Alpha.CVSSv3)


    
    
    public sealed class CVSSv3 : IMessage<CVSSv3>, IEquatable<CVSSv3>, IDeepCloneable<CVSSv3>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud OS Config v1alpha API class CVSSv3.

Common Vulnerability Scoring System version 3. For details, see <https://www.first.org/cvss/specification-document>

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CVSSv3

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OsConfig.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha)

## Assembly

Google.Cloud.OsConfig.V1Alpha.dll

## Constructors 

### CVSSv3()
    
    
    public CVSSv3()

### CVSSv3(CVSSv3)
    
    
    public CVSSv3(CVSSv3 other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)`  
  
  
## Properties 

### AttackComplexity
    
    
    public CVSSv3.Types.AttackComplexity AttackComplexity { get; set; }

This metric describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[AttackComplexity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.AttackComplexity)` |   
  
### AttackVector
    
    
    public CVSSv3.Types.AttackVector AttackVector { get; set; }

This metric reflects the context by which vulnerability exploitation is possible.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[AttackVector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.AttackVector)` |   
  
### AvailabilityImpact
    
    
    public CVSSv3.Types.Impact AvailabilityImpact { get; set; }

This metric measures the impact to the availability of the impacted component resulting from a successfully exploited vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[Impact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.Impact)` |   
  
### BaseScore
    
    
    public float BaseScore { get; set; }

The base score is a function of the base metric scores. <https://www.first.org/cvss/specification-document#Base-Metrics>

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### ConfidentialityImpact
    
    
    public CVSSv3.Types.Impact ConfidentialityImpact { get; set; }

This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[Impact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.Impact)` |   
  
### ExploitabilityScore
    
    
    public float ExploitabilityScore { get; set; }

The Exploitability sub-score equation is derived from the Base Exploitability metrics. <https://www.first.org/cvss/specification-document#2-1-Exploitability-Metrics>

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### ImpactScore
    
    
    public float ImpactScore { get; set; }

The Impact sub-score equation is derived from the Base Impact metrics.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### IntegrityImpact
    
    
    public CVSSv3.Types.Impact IntegrityImpact { get; set; }

This metric measures the impact to integrity of a successfully exploited vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[Impact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.Impact)` |   
  
### PrivilegesRequired
    
    
    public CVSSv3.Types.PrivilegesRequired PrivilegesRequired { get; set; }

This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[PrivilegesRequired](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.PrivilegesRequired)` |   
  
### Scope
    
    
    public CVSSv3.Types.Scope Scope { get; set; }

The Scope metric captures whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[Scope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.Scope)` |   
  
### UserInteraction
    
    
    public CVSSv3.Types.UserInteraction UserInteraction { get; set; }

This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component.

**Property Value**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types)[UserInteraction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.CVSSv3.Types.UserInteraction)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
