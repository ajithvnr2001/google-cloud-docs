---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientExtensions
title: Class ClientExtensions (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:42.878839+00:00
---

# Class ClientExtensions (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class ClientExtensions (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientExtensions)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.ClientExtensions)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.ClientExtensions)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.ClientExtensions)


    
    
    public static class ClientExtensions

Holder for extension identifiers generated from the top level of google/api/client.proto

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ClientExtensions

## Inherited Members

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Fields 

### ApiVersion
    
    
    public static readonly Extension<ServiceOptions, string> ApiVersion

The API version of this service, which should be sent by version-aware clients to the service. This allows services to abide by the schema and behavior of the service at the time this API version was deployed. The format of the API version must be treated as opaque by clients. Services may use a format with an apparent structure, but clients must not rely on this to determine components within an API version, or attempt to construct other valid API versions. Note that this is for upcoming functionality and may not be implemented for all services.

Example:

service Foo { option (google.api.api_version) = "v1_20230821_preview"; }

**Field Value**  
---  
**Type** | **Description**  
`[Extension](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Extension-2.html)[ServiceOptions](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.ServiceOptions.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultHost
    
    
    public static readonly Extension<ServiceOptions, string> DefaultHost

The hostname for this service. This should be specified with no prefix or protocol.

Example:

service Foo { option (google.api.default_host) = "foo.googleapi.com"; ... }

**Field Value**  
---  
**Type** | **Description**  
`[Extension](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Extension-2.html)[ServiceOptions](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.ServiceOptions.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MethodSignature
    
    
    public static readonly RepeatedExtension<MethodOptions, string> MethodSignature

A definition of a client library method signature.

In client libraries, each proto RPC corresponds to one or more methods which the end user is able to call, and calls the underlying RPC. Normally, this method receives a single argument (a struct or instance corresponding to the RPC request object). Defining this field will add one or more overloads providing flattened or simpler method signatures in some languages.

The fields on the method signature are provided as a comma-separated string.

For example, the proto RPC and annotation:

rpc CreateSubscription(CreateSubscriptionRequest) returns (Subscription) { option (google.api.method_signature) = "name,topic"; }

Would add the following Java overload (in addition to the method accepting the request object):

public final Subscription createSubscription(String name, String topic)

The following backwards-compatibility guidelines apply:

  * Adding this annotation to an unannotated method is backwards compatible.
  * Adding this annotation to a method which already has existing method signature annotations is backwards compatible if and only if the new method signature annotation is last in the sequence.
  * Modifying or removing an existing method signature annotation is a breaking change.
  * Re-ordering existing method signature annotations is a breaking change.



**Field Value**  
---  
**Type** | **Description**  
`[RepeatedExtension](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.RepeatedExtension-2.html)[MethodOptions](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MethodOptions.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OauthScopes
    
    
    public static readonly Extension<ServiceOptions, string> OauthScopes

OAuth scopes needed for the client.

Example:

service Foo { option (google.api.oauth_scopes) = \ "<https://www.googleapis.com/auth/cloud-platform>"; ... }

If there is more than one scope, use a comma-separated string:

Example:

service Foo { option (google.api.oauth_scopes) = \ "<https://www.googleapis.com/auth/cloud-platform>," "<https://www.googleapis.com/auth/monitoring>"; ... }

**Field Value**  
---  
**Type** | **Description**  
`[Extension](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Extension-2.html)[ServiceOptions](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.ServiceOptions.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
