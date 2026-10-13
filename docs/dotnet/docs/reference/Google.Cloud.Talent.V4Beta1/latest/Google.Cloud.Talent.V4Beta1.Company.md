---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company
title: Google Cloud Talent Solution v4beta1 API - Class Company (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:01.217168+00:00
---

# Google Cloud Talent Solution v4beta1 API - Class Company (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Talent Solution v4beta1 API - Class Company (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/3.0.0-beta06/Google.Cloud.Talent.V4Beta1.Company)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/2.0.0-beta07/Google.Cloud.Talent.V4Beta1.Company)


    
    
    public sealed class Company : IMessage<Company>, IEquatable<Company>, IDeepCloneable<Company>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Talent Solution v4beta1 API class Company.

A Company resource represents a company in the service. A company is the entity that owns job postings, that is, the hiring entity responsible for employing applicants for the job position.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Company

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Talent.V4Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1)

## Assembly

Google.Cloud.Talent.V4Beta1.dll

## Constructors 

### Company()
    
    
    public Company()

### Company(Company)
    
    
    public Company(Company other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company)`  
  
  
## Properties 

### CareerSiteUri
    
    
    public string CareerSiteUri { get; set; }

The URI to employer's career site or careers page on the employer's web site, for example, "<https://careers.google.com>".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CompanyName
    
    
    public CompanyName CompanyName { get; set; }

[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompanyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company#Google_Cloud_Talent_V4Beta1_Company_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CompanyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompanyName)` |   
  
### DerivedInfo
    
    
    public Company.Types.DerivedInfo DerivedInfo { get; set; }

Output only. Derived details about the company.

**Property Value**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company.Types)[DerivedInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company.Types.DerivedInfo)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. The display name of the company, for example, "Google LLC".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EeoText
    
    
    public string EeoText { get; set; }

Equal Employment Opportunity legal disclaimer text to be associated with all jobs, and typically to be displayed in all roles.

The maximum number of allowed characters is 500.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExternalId
    
    
    public string ExternalId { get; set; }

Required. Client side company identifier, used to uniquely identify the company.

The maximum number of allowed characters is 255.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HeadquartersAddress
    
    
    public string HeadquartersAddress { get; set; }

The street address of the company's main headquarters, which may be different from the job location. The service attempts to geolocate the provided address, and populates a more specific location wherever possible in [DerivedInfo.headquarters_location][google.cloud.talent.v4beta1.Company.DerivedInfo.headquarters_location].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HiringAgency
    
    
    public bool HiringAgency { get; set; }

Set to true if it is the hiring agency that post jobs for other employers.

Defaults to false if not provided.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ImageUri
    
    
    public string ImageUri { get; set; }

A URI that hosts the employer's company logo.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KeywordSearchableJobCustomAttributes
    
    
    [Obsolete]
    public RepeatedField<string> KeywordSearchableJobCustomAttributes { get; }

This field is deprecated. Please set the searchability of the custom attribute in the [Job.custom_attributes][google.cloud.talent.v4beta1.Job.custom_attributes] going forward.

A list of keys of filterable [Job.custom_attributes][google.cloud.talent.v4beta1.Job.custom_attributes], whose corresponding `string_values` are used in keyword searches. Jobs with `string_values` under these specified field keys are returned if any of the values match the search keyword. Custom field values with parenthesis, brackets and special symbols are not searchable as-is, and those keyword queries must be surrounded by quotes.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required during company update.

The resource name for a company. This is generated by the service when a company is created.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".

If tenant id is unspecified, the default tenant is used. For example, "projects/foo/companies/bar".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Size
    
    
    public CompanySize Size { get; set; }

The employer's company size.

**Property Value**  
---  
**Type** | **Description**  
`[CompanySize](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.CompanySize)` |   
  
### Suspended
    
    
    public bool Suspended { get; set; }

Output only. Indicates whether a company is flagged to be suspended from public availability by the service when job content appears suspicious, abusive, or spammy.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### WebsiteUri
    
    
    public string WebsiteUri { get; set; }

The URI representing the company's primary web site or home page, for example, "<https://www.google.com>".

The maximum number of allowed characters is 255.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
