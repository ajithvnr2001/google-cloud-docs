---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Google Cloud Dialogflow v2 API - Class ServiceCollectionExtensions (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:52.755315+00:00
---

# Google Cloud Dialogflow v2 API - Class ServiceCollectionExtensions (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class ServiceCollectionExtensions (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Methods 

### AddAgentsClient(IServiceCollection, Action<AgentsClientBuilder>)
    
    
    public static IServiceCollection AddAgentsClient(this IServiceCollection services, Action<AgentsClientBuilder> action = null)

Adds a singleton [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[AgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAgentsClient(IServiceCollection, Action<IServiceProvider, AgentsClientBuilder>)
    
    
    public static IServiceCollection AddAgentsClient(this IServiceCollection services, Action<IServiceProvider, AgentsClientBuilder> action)

Adds a singleton [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[AgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAnswerRecordsClient(IServiceCollection, Action<AnswerRecordsClientBuilder>)
    
    
    public static IServiceCollection AddAnswerRecordsClient(this IServiceCollection services, Action<AnswerRecordsClientBuilder> action = null)

Adds a singleton [AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecordsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[AnswerRecordsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecordsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAnswerRecordsClient(IServiceCollection, Action<IServiceProvider, AnswerRecordsClientBuilder>)
    
    
    public static IServiceCollection AddAnswerRecordsClient(this IServiceCollection services, Action<IServiceProvider, AnswerRecordsClientBuilder> action)

Adds a singleton [AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecordsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[AnswerRecordsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecordsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCompanionAgentsClient(IServiceCollection, Action<CompanionAgentsClientBuilder>)
    
    
    public static IServiceCollection AddCompanionAgentsClient(this IServiceCollection services, Action<CompanionAgentsClientBuilder> action = null)

Adds a singleton [CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[CompanionAgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCompanionAgentsClient(IServiceCollection, Action<IServiceProvider, CompanionAgentsClientBuilder>)
    
    
    public static IServiceCollection AddCompanionAgentsClient(this IServiceCollection services, Action<IServiceProvider, CompanionAgentsClientBuilder> action)

Adds a singleton [CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[CompanionAgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddContextsClient(IServiceCollection, Action<ContextsClientBuilder>)
    
    
    public static IServiceCollection AddContextsClient(this IServiceCollection services, Action<ContextsClientBuilder> action = null)

Adds a singleton [ContextsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ContextsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ContextsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ContextsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddContextsClient(IServiceCollection, Action<IServiceProvider, ContextsClientBuilder>)
    
    
    public static IServiceCollection AddContextsClient(this IServiceCollection services, Action<IServiceProvider, ContextsClientBuilder> action)

Adds a singleton [ContextsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ContextsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ContextsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ContextsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationDatasetsClient(IServiceCollection, Action<ConversationDatasetsClientBuilder>)
    
    
    public static IServiceCollection AddConversationDatasetsClient(this IServiceCollection services, Action<ConversationDatasetsClientBuilder> action = null)

Adds a singleton [ConversationDatasetsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationDatasetsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ConversationDatasetsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationDatasetsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationDatasetsClient(IServiceCollection, Action<IServiceProvider, ConversationDatasetsClientBuilder>)
    
    
    public static IServiceCollection AddConversationDatasetsClient(this IServiceCollection services, Action<IServiceProvider, ConversationDatasetsClientBuilder> action)

Adds a singleton [ConversationDatasetsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationDatasetsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ConversationDatasetsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationDatasetsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationModelsClient(IServiceCollection, Action<ConversationModelsClientBuilder>)
    
    
    public static IServiceCollection AddConversationModelsClient(this IServiceCollection services, Action<ConversationModelsClientBuilder> action = null)

Adds a singleton [ConversationModelsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationModelsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ConversationModelsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationModelsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationModelsClient(IServiceCollection, Action<IServiceProvider, ConversationModelsClientBuilder>)
    
    
    public static IServiceCollection AddConversationModelsClient(this IServiceCollection services, Action<IServiceProvider, ConversationModelsClientBuilder> action)

Adds a singleton [ConversationModelsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationModelsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ConversationModelsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationModelsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationProfilesClient(IServiceCollection, Action<ConversationProfilesClientBuilder>)
    
    
    public static IServiceCollection AddConversationProfilesClient(this IServiceCollection services, Action<ConversationProfilesClientBuilder> action = null)

Adds a singleton [ConversationProfilesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationProfilesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ConversationProfilesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationProfilesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationProfilesClient(IServiceCollection, Action<IServiceProvider, ConversationProfilesClientBuilder>)
    
    
    public static IServiceCollection AddConversationProfilesClient(this IServiceCollection services, Action<IServiceProvider, ConversationProfilesClientBuilder> action)

Adds a singleton [ConversationProfilesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationProfilesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ConversationProfilesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationProfilesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationsClient(IServiceCollection, Action<ConversationsClientBuilder>)
    
    
    public static IServiceCollection AddConversationsClient(this IServiceCollection services, Action<ConversationsClientBuilder> action = null)

Adds a singleton [ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ConversationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConversationsClient(IServiceCollection, Action<IServiceProvider, ConversationsClientBuilder>)
    
    
    public static IServiceCollection AddConversationsClient(this IServiceCollection services, Action<IServiceProvider, ConversationsClientBuilder> action)

Adds a singleton [ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ConversationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDocumentsClient(IServiceCollection, Action<DocumentsClientBuilder>)
    
    
    public static IServiceCollection AddDocumentsClient(this IServiceCollection services, Action<DocumentsClientBuilder> action = null)

Adds a singleton [DocumentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DocumentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DocumentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DocumentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDocumentsClient(IServiceCollection, Action<IServiceProvider, DocumentsClientBuilder>)
    
    
    public static IServiceCollection AddDocumentsClient(this IServiceCollection services, Action<IServiceProvider, DocumentsClientBuilder> action)

Adds a singleton [DocumentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DocumentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DocumentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DocumentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEncryptionSpecServiceClient(IServiceCollection, Action<EncryptionSpecServiceClientBuilder>)
    
    
    public static IServiceCollection AddEncryptionSpecServiceClient(this IServiceCollection services, Action<EncryptionSpecServiceClientBuilder> action = null)

Adds a singleton [EncryptionSpecServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EncryptionSpecServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[EncryptionSpecServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EncryptionSpecServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEncryptionSpecServiceClient(IServiceCollection, Action<IServiceProvider, EncryptionSpecServiceClientBuilder>)
    
    
    public static IServiceCollection AddEncryptionSpecServiceClient(this IServiceCollection services, Action<IServiceProvider, EncryptionSpecServiceClientBuilder> action)

Adds a singleton [EncryptionSpecServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EncryptionSpecServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[EncryptionSpecServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EncryptionSpecServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEntityTypesClient(IServiceCollection, Action<EntityTypesClientBuilder>)
    
    
    public static IServiceCollection AddEntityTypesClient(this IServiceCollection services, Action<EntityTypesClientBuilder> action = null)

Adds a singleton [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EntityTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[EntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EntityTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEntityTypesClient(IServiceCollection, Action<IServiceProvider, EntityTypesClientBuilder>)
    
    
    public static IServiceCollection AddEntityTypesClient(this IServiceCollection services, Action<IServiceProvider, EntityTypesClientBuilder> action)

Adds a singleton [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EntityTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[EntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EntityTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEnvironmentsClient(IServiceCollection, Action<EnvironmentsClientBuilder>)
    
    
    public static IServiceCollection AddEnvironmentsClient(this IServiceCollection services, Action<EnvironmentsClientBuilder> action = null)

Adds a singleton [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EnvironmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[EnvironmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EnvironmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEnvironmentsClient(IServiceCollection, Action<IServiceProvider, EnvironmentsClientBuilder>)
    
    
    public static IServiceCollection AddEnvironmentsClient(this IServiceCollection services, Action<IServiceProvider, EnvironmentsClientBuilder> action)

Adds a singleton [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EnvironmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[EnvironmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EnvironmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFulfillmentsClient(IServiceCollection, Action<FulfillmentsClientBuilder>)
    
    
    public static IServiceCollection AddFulfillmentsClient(this IServiceCollection services, Action<FulfillmentsClientBuilder> action = null)

Adds a singleton [FulfillmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.FulfillmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FulfillmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.FulfillmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFulfillmentsClient(IServiceCollection, Action<IServiceProvider, FulfillmentsClientBuilder>)
    
    
    public static IServiceCollection AddFulfillmentsClient(this IServiceCollection services, Action<IServiceProvider, FulfillmentsClientBuilder> action)

Adds a singleton [FulfillmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.FulfillmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FulfillmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.FulfillmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGeneratorEvaluationsClient(IServiceCollection, Action<GeneratorEvaluationsClientBuilder>)
    
    
    public static IServiceCollection AddGeneratorEvaluationsClient(this IServiceCollection services, Action<GeneratorEvaluationsClientBuilder> action = null)

Adds a singleton [GeneratorEvaluationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorEvaluationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GeneratorEvaluationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorEvaluationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGeneratorEvaluationsClient(IServiceCollection, Action<IServiceProvider, GeneratorEvaluationsClientBuilder>)
    
    
    public static IServiceCollection AddGeneratorEvaluationsClient(this IServiceCollection services, Action<IServiceProvider, GeneratorEvaluationsClientBuilder> action)

Adds a singleton [GeneratorEvaluationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorEvaluationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GeneratorEvaluationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorEvaluationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGeneratorsClient(IServiceCollection, Action<GeneratorsClientBuilder>)
    
    
    public static IServiceCollection AddGeneratorsClient(this IServiceCollection services, Action<GeneratorsClientBuilder> action = null)

Adds a singleton [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GeneratorsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGeneratorsClient(IServiceCollection, Action<IServiceProvider, GeneratorsClientBuilder>)
    
    
    public static IServiceCollection AddGeneratorsClient(this IServiceCollection services, Action<IServiceProvider, GeneratorsClientBuilder> action)

Adds a singleton [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GeneratorsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIntentsClient(IServiceCollection, Action<IntentsClientBuilder>)
    
    
    public static IServiceCollection AddIntentsClient(this IServiceCollection services, Action<IntentsClientBuilder> action = null)

Adds a singleton [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.IntentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[IntentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.IntentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIntentsClient(IServiceCollection, Action<IServiceProvider, IntentsClientBuilder>)
    
    
    public static IServiceCollection AddIntentsClient(this IServiceCollection services, Action<IServiceProvider, IntentsClientBuilder> action)

Adds a singleton [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.IntentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[IntentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.IntentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddKnowledgeBasesClient(IServiceCollection, Action<KnowledgeBasesClientBuilder>)
    
    
    public static IServiceCollection AddKnowledgeBasesClient(this IServiceCollection services, Action<KnowledgeBasesClientBuilder> action = null)

Adds a singleton [KnowledgeBasesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBasesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[KnowledgeBasesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBasesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddKnowledgeBasesClient(IServiceCollection, Action<IServiceProvider, KnowledgeBasesClientBuilder>)
    
    
    public static IServiceCollection AddKnowledgeBasesClient(this IServiceCollection services, Action<IServiceProvider, KnowledgeBasesClientBuilder> action)

Adds a singleton [KnowledgeBasesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBasesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[KnowledgeBasesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBasesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddParticipantsClient(IServiceCollection, Action<ParticipantsClientBuilder>)
    
    
    public static IServiceCollection AddParticipantsClient(this IServiceCollection services, Action<ParticipantsClientBuilder> action = null)

Adds a singleton [ParticipantsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ParticipantsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ParticipantsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ParticipantsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddParticipantsClient(IServiceCollection, Action<IServiceProvider, ParticipantsClientBuilder>)
    
    
    public static IServiceCollection AddParticipantsClient(this IServiceCollection services, Action<IServiceProvider, ParticipantsClientBuilder> action)

Adds a singleton [ParticipantsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ParticipantsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ParticipantsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ParticipantsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionEntityTypesClient(IServiceCollection, Action<SessionEntityTypesClientBuilder>)
    
    
    public static IServiceCollection AddSessionEntityTypesClient(this IServiceCollection services, Action<SessionEntityTypesClientBuilder> action = null)

Adds a singleton [SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionEntityTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SessionEntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionEntityTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionEntityTypesClient(IServiceCollection, Action<IServiceProvider, SessionEntityTypesClientBuilder>)
    
    
    public static IServiceCollection AddSessionEntityTypesClient(this IServiceCollection services, Action<IServiceProvider, SessionEntityTypesClientBuilder> action)

Adds a singleton [SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionEntityTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SessionEntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionEntityTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionsClient(IServiceCollection, Action<SessionsClientBuilder>)
    
    
    public static IServiceCollection AddSessionsClient(this IServiceCollection services, Action<SessionsClientBuilder> action = null)

Adds a singleton [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SessionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionsClient(IServiceCollection, Action<IServiceProvider, SessionsClientBuilder>)
    
    
    public static IServiceCollection AddSessionsClient(this IServiceCollection services, Action<IServiceProvider, SessionsClientBuilder> action)

Adds a singleton [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SessionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSipTrunksClient(IServiceCollection, Action<SipTrunksClientBuilder>)
    
    
    public static IServiceCollection AddSipTrunksClient(this IServiceCollection services, Action<SipTrunksClientBuilder> action = null)

Adds a singleton [SipTrunksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SipTrunksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SipTrunksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SipTrunksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSipTrunksClient(IServiceCollection, Action<IServiceProvider, SipTrunksClientBuilder>)
    
    
    public static IServiceCollection AddSipTrunksClient(this IServiceCollection services, Action<IServiceProvider, SipTrunksClientBuilder> action)

Adds a singleton [SipTrunksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SipTrunksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SipTrunksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SipTrunksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddToolsClient(IServiceCollection, Action<ToolsClientBuilder>)
    
    
    public static IServiceCollection AddToolsClient(this IServiceCollection services, Action<ToolsClientBuilder> action = null)

Adds a singleton [ToolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ToolsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ToolsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ToolsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddToolsClient(IServiceCollection, Action<IServiceProvider, ToolsClientBuilder>)
    
    
    public static IServiceCollection AddToolsClient(this IServiceCollection services, Action<IServiceProvider, ToolsClientBuilder> action)

Adds a singleton [ToolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ToolsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ToolsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ToolsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVersionsClient(IServiceCollection, Action<VersionsClientBuilder>)
    
    
    public static IServiceCollection AddVersionsClient(this IServiceCollection services, Action<VersionsClientBuilder> action = null)

Adds a singleton [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.VersionsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VersionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.VersionsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVersionsClient(IServiceCollection, Action<IServiceProvider, VersionsClientBuilder>)
    
    
    public static IServiceCollection AddVersionsClient(this IServiceCollection services, Action<IServiceProvider, VersionsClientBuilder> action)

Adds a singleton [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.VersionsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VersionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.VersionsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
