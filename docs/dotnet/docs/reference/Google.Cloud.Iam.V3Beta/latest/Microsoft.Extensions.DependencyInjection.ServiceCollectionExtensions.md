---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Identity and Access Management (IAM) v3beta API - Class ServiceCollectionExtensions (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:11.427540+00:00
---

# Identity and Access Management (IAM) v3beta API - Class ServiceCollectionExtensions (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3beta API - Class ServiceCollectionExtensions (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Identity and Access Management (IAM) v3beta API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.Iam.V3Beta.dll

## Methods 

### AddAccessPoliciesClient(IServiceCollection, Action<AccessPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddAccessPoliciesClient(this IServiceCollection services, Action<AccessPoliciesClientBuilder> action = null)

Adds a singleton [AccessPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[AccessPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAccessPoliciesClient(IServiceCollection, Action<IServiceProvider, AccessPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddAccessPoliciesClient(this IServiceCollection services, Action<IServiceProvider, AccessPoliciesClientBuilder> action)

Adds a singleton [AccessPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[AccessPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPolicyBindingsClient(IServiceCollection, Action<PolicyBindingsClientBuilder>)
    
    
    public static IServiceCollection AddPolicyBindingsClient(this IServiceCollection services, Action<PolicyBindingsClientBuilder> action = null)

Adds a singleton [PolicyBindingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBindingsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PolicyBindingsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBindingsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPolicyBindingsClient(IServiceCollection, Action<IServiceProvider, PolicyBindingsClientBuilder>)
    
    
    public static IServiceCollection AddPolicyBindingsClient(this IServiceCollection services, Action<IServiceProvider, PolicyBindingsClientBuilder> action)

Adds a singleton [PolicyBindingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBindingsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PolicyBindingsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PolicyBindingsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPrincipalAccessBoundaryPoliciesClient(IServiceCollection, Action<PrincipalAccessBoundaryPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddPrincipalAccessBoundaryPoliciesClient(this IServiceCollection services, Action<PrincipalAccessBoundaryPoliciesClientBuilder> action = null)

Adds a singleton [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PrincipalAccessBoundaryPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPrincipalAccessBoundaryPoliciesClient(IServiceCollection, Action<IServiceProvider, PrincipalAccessBoundaryPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddPrincipalAccessBoundaryPoliciesClient(this IServiceCollection services, Action<IServiceProvider, PrincipalAccessBoundaryPoliciesClientBuilder> action)

Adds a singleton [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PrincipalAccessBoundaryPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
