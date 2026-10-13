---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest
title: Service Health v1 API - Class GetOrganizationImpactRequest (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:55.751381+00:00
---

# Service Health v1 API - Class GetOrganizationImpactRequest (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Health v1 API - Class GetOrganizationImpactRequest (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.3.0/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.2.0/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.1.0/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.0.0/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest)


    
    
    public sealed class GetOrganizationImpactRequest : IMessage<GetOrganizationImpactRequest>, IEquatable<GetOrganizationImpactRequest>, IDeepCloneable<GetOrganizationImpactRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Health v1 API class GetOrganizationImpactRequest.

Gets information about an event that affects a project under an organization.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetOrganizationImpactRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetOrganizationImpactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetOrganizationImpactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetOrganizationImpactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceHealth.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1)

## Assembly

Google.Cloud.ServiceHealth.V1.dll

## Constructors 

### GetOrganizationImpactRequest()
    
    
    public GetOrganizationImpactRequest()

### GetOrganizationImpactRequest(GetOrganizationImpactRequest)
    
    
    public GetOrganizationImpactRequest(GetOrganizationImpactRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetOrganizationImpactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the resource using the form `organizations/{organization_id}/locations/global/organizationImpacts/{organization_impact_id}`.

`organization_id` \- ID (number) of the organization that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).<br> `organization_impact_id` \- ID of the [OrganizationImpact resource](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrganizationImpactName
    
    
    public OrganizationImpactName OrganizationImpactName { get; set; }

[OrganizationImpactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.OrganizationImpactName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.GetOrganizationImpactRequest#Google_Cloud_ServiceHealth_V1_GetOrganizationImpactRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationImpactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.OrganizationImpactName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
