---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts
title: REST Resource: organizations.apiproducts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:17.878705+00:00
---

# REST Resource: organizations.apiproducts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.apiproducts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ApiProduct
    * JSON representation
  * OperationGroup
    * JSON representation
  * OperationConfig
    * JSON representation
  * Operation
    * JSON representation
  * Quota
    * JSON representation
  * GraphQLOperationGroup
    * JSON representation
  * GraphQLOperationConfig
    * JSON representation
  * GraphQLOperation
    * JSON representation
  * GrpcOperationGroup
    * JSON representation
  * GrpcOperationConfig
    * JSON representation
  * QuotaCounterScope
  * LlmOperationGroup
    * JSON representation
  * LlmOperationConfig
    * JSON representation
  * LlmOperation
    * JSON representation
  * LlmTokenQuota
    * JSON representation
  * PayloadOperationGroup
    * JSON representation
  * PayloadOperationConfig
    * JSON representation
  * PayloadOperation
    * JSON representation
  * Methods



## Resource: ApiProduct

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "approvalType": string,
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ],
      "description": string,
      "apiResources": [
        string
      ],
      "environments": [
        string
      ],
      "proxies": [
        string
      ],
      "quota": string,
      "quotaInterval": string,
      "quotaTimeUnit": string,
      "scopes": [
        string
      ],
      "createdAt": string,
      "lastModifiedAt": string,
      "operationGroup": {
        object ([OperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#OperationGroup))
      },
      "graphqlOperationGroup": {
        object ([GraphQLOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GraphQLOperationGroup))
      },
      "grpcOperationGroup": {
        object ([GrpcOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GrpcOperationGroup))
      },
      "quotaCounterScope": enum ([QuotaCounterScope](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#QuotaCounterScope)),
      "space": string,
      "llmOperationGroup": {
        object ([LlmOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmOperationGroup))
      },
      "llmQuota": string,
      "llmQuotaInterval": string,
      "llmQuotaTimeUnit": string,
      "payloadOperationGroup": {
        object ([PayloadOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#PayloadOperationGroup))
      }
    }  
  
Fields  
---  
`name` |  `string` Internal name of the API product. Characters you can use in the name are restricted to: `A-Z0-9._\-$ %`.**Note:** The internal name cannot be edited when updating the API product.  
`displayName` |  `string` Name displayed in the UI or developer portal to developers registering for API access.  
`approvalType` |  `string` Flag that specifies how API keys are approved to access the APIs defined by the API product.If set to `manual`, the consumer key is generated and returned in "pending" state. In this case, the API keys won't work until they have been explicitly approved.If set to `auto`, the consumer key is generated and returned in "approved" state and can be used immediately.**Note:** Typically, `auto` is used to provide access to free or trial API products that provide limited quota or capabilities.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` Array of attributes that may be used to extend the default API product profile with customer-specific metadata. You can specify a maximum of 18 attributes.Use this property to specify the access level of the API product as either `public`, `private`, or `internal`.Only products marked `public` are available to developers in the Apigee developer portal. For example, you can set a product to `internal` while it is in development and then change access to `public` when it is ready to release on the portal.API products marked as `private` do not appear on the portal, but can be accessed by external developers.  
`description` |  `string` Description of the API product. Include key information about the API product that is not captured by other fields.  
`apiResources[]` |  `string` Comma-separated list of API resources to be bundled in the API product.By default, the resource paths are mapped from the `proxy.pathsuffix` variable.The proxy path suffix is defined as the URI fragment following the ProxyEndpoint base path. For example, if the `apiResources` element is defined to be `/forecastrss` and the base path defined for the API proxy is `/weather`, then only requests to `/weather/forecastrss` are permitted by the API product.You can select a specific path, or you can select all subpaths with the following wildcard:

  * `/**`: Indicates that all sub-URIs are included.
  * `/*` : Indicates that only URIs one level down are included.

By default, / supports the same resources as /** as well as the base path defined by the API proxy.For example, if the base path of the API proxy is `/v1/weatherapikey`, then the API product supports requests to `/v1/weatherapikey` and to any sub-URIs, such as `/v1/weatherapikey/forecastrss`, `/v1/weatherapikey/region/CA`, and so on. For more information, see [Managing API products](https://cloud.google.com/apigee/docs/api-platform/publish/create-api-products).  
`environments[]` |  `string` Comma-separated list of environment names to which the API product is bound. Requests to environments that are not listed are rejected.By specifying one or more environments, you can bind the resources listed in the API product to a specific environment, preventing developers from accessing those resources through API proxies deployed in another environment.This setting is used, for example, to prevent resources associated with API proxies in `prod` from being accessed by API proxies deployed in `test`.  
`proxies[]` |  `string` Comma-separated list of API proxy names to which this API product is bound. By specifying API proxies, you can associate resources in the API product with specific API proxies, preventing developers from accessing those resources through other API proxies.Apigee rejects requests to API proxies that are not listed.**Note:** The API proxy names must already exist in the specified environment as they will be validated upon creation.  
`quota` |  `string` Number of request messages permitted per app by this API product for the specified `quotaInterval` and `quotaTimeUnit`.For example, a `quota` of 50, for a `quotaInterval` of 12 and a `quotaTimeUnit` of hours means 50 requests are allowed every 12 hours.  
`quotaInterval` |  `string` Time interval over which the number of request messages is calculated.  
`quotaTimeUnit` |  `string` Time unit defined for the `quotaInterval`. Valid values include `minute`, `hour`, `day`, or `month`.  
`scopes[]` |  `string` Comma-separated list of OAuth scopes that are validated at runtime. Apigee validates that the scopes in any access token presented match the scopes defined in the OAuth policy associated with the API product.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Response only. Creation time of this environment as milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Response only. Modified time of this environment as milliseconds since epoch.  
`operationGroup` |  `object (`[OperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#OperationGroup)`)` Configuration used to group Apigee proxies or remote services with resources, method types, and quotas. The resource refers to the resource URI (excluding the base path). With this grouping, the API product creator is able to fine-tune and give precise control over which REST methods have access to specific resources and how many calls can be made (using the `quota` setting).**Note:** The `apiResources` setting cannot be specified for both the API product and operation group; otherwise the call will fail.  
`graphqlOperationGroup` |  `object (`[GraphQLOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GraphQLOperationGroup)`)` Configuration used to group Apigee proxies or remote services with graphQL operation name, graphQL operation type and quotas. This grouping allows us to precisely set quota for a particular combination of graphQL name and operation type for a particular proxy request. If graphQL name is not set, this would imply quota will be applied on all graphQL requests matching the operation type.  
`grpcOperationGroup` |  `object (`[GrpcOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GrpcOperationGroup)`)` Optional. Configuration used to group Apigee proxies with gRPC services and method names. This grouping allows us to set quota for a particular proxy with the gRPC service name and method. If a method name is not set, this implies quota and authorization are applied to all gRPC methods implemented by that proxy for that particular gRPC service.  
`quotaCounterScope` |  `enum (`[QuotaCounterScope](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#QuotaCounterScope)`)` Scope of the quota decides how the quota counter gets applied and evaluate for quota violation. If the Scope is set as PROXY, then all the operations defined for the APIproduct that are associated with the same proxy will share the same quota counter set at the APIproduct level, making it a global counter at a proxy level. If the Scope is set as OPERATION, then each operations get the counter set at the API product dedicated, making it a local counter. Note that, the QuotaCounterScope applies only when an operation does not have dedicated quota set for itself.  
`space` |  `string` Optional. The resource ID of the parent Space. If not set, the parent resource will be the Organization.To learn how Spaces can be used to manage resources, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).  
`llmOperationGroup` |  `object (`[LlmOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmOperationGroup)`)` Optional. Configuration used to group Apigee proxies with resources, method types, LLM model and quotas. The resource refers to the resource URI (excluding the base path). With this grouping, the API product creator is able to fine-tune and give precise control over which REST methods have access to specific resources, specific LLM model and how many calls can be made (using the `quota` setting).**Note:** The `apiResources` setting cannot be specified for both the API product and llm operation group; otherwise the call will fail.  
`llmQuota` |  `string` Optional. Number of LLM tokens permitted per app by this API product for the specified `llmQuotaInterval` and `llmQuotaTimeUnit`.For example, an `llmQuota` of 50,000, for an `llmQuotaInterval` of 12 and an `llmQuotaTimeUnit` of hours means 50,000 llm tokens are allowed to be used every 12 hours.  
`llmQuotaInterval` |  `string` Optional. Time interval over which the number of tokens from LLM responses is calculated.  
`llmQuotaTimeUnit` |  `string` Optional. Time unit defined for the `llmQuotaInterval`. Valid values include `minute`, `hour`, `day`, or `month`.  
`payloadOperationGroup` |  `object (`[PayloadOperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#PayloadOperationGroup)`)` Optional. Configuration used to group Apigee proxies with payload-based operations and quotas. Unlike `operationGroup`, which matches on the URL path, this grouping matches on operation identifiers extracted from the request payload (for example, JSON-RPC method and tool names). This enables fine-grained authorization and quota enforcement for protocols such as MCP where multiple operations share a single endpoint.**Note:** The `proxies` and `apiResources` settings cannot be specified for both the API product and payload operation group; otherwise the call will fail.  
  
## OperationGroup

List of operation configuration details associated with Apigee API proxies or remote services. Remote services are non-Apigee proxies, such as Istio-Envoy.

JSON representation  
---  
      
    
    {
      "operationConfigs": [
        {
          object ([OperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#OperationConfig))
        }
      ],
      "operationConfigType": string
    }  
  
Fields  
---  
`operationConfigs[]` |  `object (`[OperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#OperationConfig)`)` Required. List of operation configurations for either Apigee API proxies or other remote services that are associated with this API product.  
`operationConfigType` |  `string` Flag that specifes whether the configuration is for Apigee API proxy or a remote service. Valid values include `proxy` or `remoteservice`. Defaults to `proxy`. Set to `proxy` when Apigee API proxies are associated with the API product. Set to `remoteservice` when non-Apigee proxies like Istio-Envoy are associated with the API product.  
  
## OperationConfig

Binds the resources in an API proxy or remote service with the allowed REST methods and associated quota enforcement.

JSON representation  
---  
      
    
    {
      "apiSource": string,
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Operation))
        }
      ],
      "quota": {
        object ([Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota))
      },
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ]
    }  
  
Fields  
---  
`apiSource` |  `string` Required. Name of the API proxy or remote service with which the resources, methods, and quota are associated.  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Operation)`)` List of resource/method pairs for the API proxy or remote service to which quota will applied.**Note** : Currently, you can specify only a single resource/method pair. The call will fail if more than one resource/method pair is provided.  
`quota` |  `object (`[Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota)`)` Quota parameters to be enforced for the resources, methods, and API source combination. If none are specified, quota enforcement will not be done.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` Custom attributes associated with the operation.  
  
## Operation

Represents the pairing of REST resource path and the actions (verbs) allowed on the resource path.

JSON representation  
---  
      
    
    {
      "resource": string,
      "methods": [
        string
      ]
    }  
  
Fields  
---  
`resource` |  `string` Required. REST resource path associated with the API proxy or remote service.  
`methods[]` |  `string` methods refers to the REST verbs as in <https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html>. When none specified, all verb types are allowed.  
  
## Quota

Quota contains the essential parameters needed that can be applied on the resources, methods, API source combination associated with this API product. While Quota is optional, setting it prevents requests from exceeding the provisioned parameters.

JSON representation  
---  
      
    
    {
      "limit": string,
      "interval": string,
      "timeUnit": string
    }  
  
Fields  
---  
`limit` |  `string` Required. Upper limit allowed for the time interval and time unit specified. Requests exceeding this limit will be rejected.  
`interval` |  `string` Required. Time interval over which the number of request messages is calculated.  
`timeUnit` |  `string` Time unit defined for the `interval`. Valid values include `minute`, `hour`, `day`, or `month`. If `limit` and `interval` are valid, the default value is `hour`; otherwise, the default is null.  
  
## GraphQLOperationGroup

List of graphQL operation configuration details associated with Apigee API proxies or remote services. Remote services are non-Apigee proxies, such as Istio-Envoy.

JSON representation  
---  
      
    
    {
      "operationConfigs": [
        {
          object ([GraphQLOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GraphQLOperationConfig))
        }
      ],
      "operationConfigType": string
    }  
  
Fields  
---  
`operationConfigs[]` |  `object (`[GraphQLOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GraphQLOperationConfig)`)` Required. List of operation configurations for either Apigee API proxies or other remote services that are associated with this API product.  
`operationConfigType` |  `string` Flag that specifies whether the configuration is for Apigee API proxy or a remote service. Valid values include `proxy` or `remoteservice`. Defaults to `proxy`. Set to `proxy` when Apigee API proxies are associated with the API product. Set to `remoteservice` when non-Apigee proxies like Istio-Envoy are associated with the API product.  
  
## GraphQLOperationConfig

Binds the resources in a proxy or remote service with the GraphQL operation and its associated quota enforcement.

JSON representation  
---  
      
    
    {
      "apiSource": string,
      "operations": [
        {
          object ([GraphQLOperation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GraphQLOperation))
        }
      ],
      "quota": {
        object ([Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota))
      },
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ]
    }  
  
Fields  
---  
`apiSource` |  `string` Required. Name of the API proxy endpoint or remote service with which the GraphQL operation and quota are associated.  
`operations[]` |  `object (`[GraphQLOperation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GraphQLOperation)`)` Required. List of GraphQL name/operation type pairs for the proxy or remote service to which quota will be applied. If only operation types are specified, the quota will be applied to all GraphQL requests irrespective of the GraphQL name.**Note** : Currently, you can specify only a single GraphQLOperation. Specifying more than one will cause the operation to fail.  
`quota` |  `object (`[Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota)`)` Quota parameters to be enforced for the resources, methods, and API source combination. If none are specified, quota enforcement will not be done.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` Custom attributes associated with the operation.  
  
## GraphQLOperation

Represents the pairing of GraphQL operation types and the GraphQL operation name.

JSON representation  
---  
      
    
    {
      "operationTypes": [
        string
      ],
      "operation": string
    }  
  
Fields  
---  
`operationTypes[]` |  `string` Required. GraphQL operation types. Valid values include `query` or `mutation`.**Note** : Apigee does not currently support `subscription` types.  
`operation` |  `string` GraphQL operation name. The name and operation type will be used to apply quotas. If no name is specified, the quota will be applied to all GraphQL operations irrespective of their operation names in the payload.  
  
## GrpcOperationGroup

List of gRPC operation configuration details associated with Apigee API proxies.

JSON representation  
---  
      
    
    {
      "operationConfigs": [
        {
          object ([GrpcOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GrpcOperationConfig))
        }
      ]
    }  
  
Fields  
---  
`operationConfigs[]` |  `object (`[GrpcOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#GrpcOperationConfig)`)` Required. List of operation configurations for either Apigee API proxies that are associated with this API product.  
  
## GrpcOperationConfig

Binds the resources in a proxy or remote service with the gRPC operation and its associated quota enforcement.

JSON representation  
---  
      
    
    {
      "apiSource": string,
      "methods": [
        string
      ],
      "quota": {
        object ([Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota))
      },
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ],
      "service": string
    }  
  
Fields  
---  
`apiSource` |  `string` Required. Name of the API proxy with which the gRPC operation and quota are associated.  
`methods[]` |  `string` List of unqualified gRPC method names for the proxy to which quota will be applied. If this field is empty, the Quota will apply to all operations on the gRPC service defined on the proxy.Example: Given a proxy that is configured to serve com.petstore.PetService, the methods com.petstore.PetService.ListPets and com.petstore.PetService.GetPet would be specified here as simply ["ListPets", "GetPet"].  
`quota` |  `object (`[Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota)`)` Quota parameters to be enforced for the methods and API source combination. If none are specified, quota enforcement will not be done.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` Custom attributes associated with the operation.  
`service` |  `string` Required. gRPC Service name associated to be associated with the API proxy, on which quota rules can be applied upon.  
  
## QuotaCounterScope

QuotaCounterScope lists the possible scopes for the application of quota counters.

Enums  
---  
`QUOTA_COUNTER_SCOPE_UNSPECIFIED` | When quota is not explicitly defined for each operation(REST/GraphQL), the limits set at product level will be used as a local counter for quota evaluation by all the operations, independent of proxy association.  
`PROXY` | When quota is not explicitly defined for each operation(REST/GraphQL), set at product level will be used as a global counter for quota evaluation by all the operations associated with a particular proxy.  
`OPERATION` | When quota is not explicitly defined for each operation(REST/GraphQL), the limits set at product level will be used as a local counter for quota evaluation by all the operations, independent of proxy association. This behavior mimics the same as QUOTA_COUNTER_SCOPE_UNSPECIFIED.  
`PRODUCT` | When quota is not explicitly defined for each operation(REST/GraphQL), the limits set at product level will be used as a global counter for quota evaluation by all the operations.  
  
## LlmOperationGroup

List of LLM operation configuration details associated with Apigee API proxies.

JSON representation  
---  
      
    
    {
      "operationConfigs": [
        {
          object ([LlmOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmOperationConfig))
        }
      ]
    }  
  
Fields  
---  
`operationConfigs[]` |  `object (`[LlmOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmOperationConfig)`)` Required. List of LLM operation configurations for either Apigee API proxies that are associated with this API product.  
  
## LlmOperationConfig

Binds the resources in an API proxy or remote service with the allowed REST methods and associated quota enforcement.

JSON representation  
---  
      
    
    {
      "apiSource": string,
      "llmOperations": [
        {
          object ([LlmOperation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmOperation))
        }
      ],
      "llmTokenQuota": {
        object ([LlmTokenQuota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmTokenQuota))
      },
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ]
    }  
  
Fields  
---  
`apiSource` |  `string` Required. Name of the API proxy or remote service with which the resources, methods, and quota are associated.  
`llmOperations[]` |  `object (`[LlmOperation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmOperation)`)` Required. List of resource/method/model for the API proxy to which quota will applied.**Note** : Currently, you can specify only a single resource/method/model mapping. The call will fail if more than one resource/method/model mappings are provided.  
`llmTokenQuota` |  `object (`[LlmTokenQuota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#LlmTokenQuota)`)` Required. LLM token Quota parameters to be enforced for the resources, methods, and API source & LLM model combination. If none are specified, quota enforcement will not be done.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` Optional. Custom attributes associated with the operation.  
  
## LlmOperation

Represents the pairing of REST resource path, model and the actions (verbs) allowed on the resource path.

JSON representation  
---  
      
    
    {
      "resource": string,
      "methods": [
        string
      ],
      "model": string
    }  
  
Fields  
---  
`resource` |  `string` Required. REST resource path associated with the API proxy or remote service.  
`methods[]` |  `string` Optional. methods refers to the REST verbs as in <https://httpwg.org/specs/rfc9110.html> For example: GET, POST, PUT, DELETE, etc. They need to be in uppercase. When none specified, all verb types are allowed.  
`model` |  `string` Required. LLM model name associated with the API proxy  
  
## LlmTokenQuota

LLM Token Quota contains the essential parameters needed that can be applied on the resources, methods, models, API source combination associated with this API product. While LLM Token Quota is optional, setting it prevents requests from exceeding the provisioned parameters.

JSON representation  
---  
      
    
    {
      "limit": string,
      "interval": string,
      "timeUnit": string
    }  
  
Fields  
---  
`limit` |  `string` Required. Upper limit of LLM tokens allowed for the time interval and time unit specified. Requests exceeding this limit will be rejected.  
`interval` |  `string` Required. Time interval over which the number of request messages is calculated.  
`timeUnit` |  `string` Optional. Time unit defined for the `interval`. Valid values include `minute`, `hour`, `day`, or `month`. If `limit` and `interval` are valid, the default value is `hour`; otherwise, the default is null.  
  
## PayloadOperationGroup

List of payload operation configuration details associated with Apigee API proxies. Payload operations enable governance of protocols where operations are embedded in the request body (such as JSON-RPC) rather than defined by the URL path.

JSON representation  
---  
      
    
    {
      "operationConfigs": [
        {
          object ([PayloadOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#PayloadOperationConfig))
        }
      ]
    }  
  
Fields  
---  
`operationConfigs[]` |  `object (`[PayloadOperationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#PayloadOperationConfig)`)` Required. List of payload operation configurations for Apigee API proxies that are associated with this API product.  
  
## PayloadOperationConfig

Binds the payload operations in an API proxy with the associated quota enforcement.

JSON representation  
---  
      
    
    {
      "apiSource": string,
      "operations": [
        {
          object ([PayloadOperation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#PayloadOperation))
        }
      ],
      "quota": {
        object ([Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota))
      },
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ]
    }  
  
Fields  
---  
`apiSource` |  `string` Required. Name of the API proxy with which the payload operations and quota are associated.  
`operations[]` |  `object (`[PayloadOperation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#PayloadOperation)`)` Required. List of payload operations for the API proxy to which quota will be applied.  
`quota` |  `object (`[Quota](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#Quota)`)` Optional. Quota parameters to be enforced for the operations and API source combination. If none are specified, quota enforcement will not be done unless a quota is defined at the API product level.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` Optional. Custom attributes associated with the operation.  
  
## PayloadOperation

Represents a single operation identifier extracted from the request payload.

JSON representation  
---  
      
    
    {
      "operation": string
    }  
  
Fields  
---  
`operation` |  `string` Required. The operation name extracted from the request payload at runtime by the ParsePayload policy. For example, for MCP protocol requests, this could be `"tools/list"` or `"tools/call/get_weather"`. Wildcards are not supported.  
  
## Methods  
  
---  
  
### `[attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/attributes)`

|  Updates or creates API product attributes.  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/create)`

|  Creates an API product in an organization.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/delete)`

|  Deletes an API product from an organization.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/get)`

|  Gets configuration details for an API product.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/list)`

|  Lists all API product names for an organization.  
  
### `[move](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/move)`

|  Moves an API product to a different space.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/update)`

|  Updates an existing API product.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
