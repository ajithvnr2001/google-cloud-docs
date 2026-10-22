---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-reference/
title: Apigee Operator for Kubernetes resource reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:34.603235+00:00
---

# Apigee Operator for Kubernetes resource reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Operator for Kubernetes resource reference Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page is a reference for each Kubernetes resource that is supported by the Apigee Operator for Kubernetes. Unless specifically noted as Optional, all fields are required.

## APIProduct

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | `apim.googleapis.com/v1`  
`kind` Type: `string` | `APIProduct`  
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: APIProductSpec | `spec` defines the desired state of the APIProductSet.   
  
### APIProductSpec

**Field** | **Description**  
---|---  
`name` Type: `string` | The name of the API Product.   
`approvalType` Type: `string` | Flag that specifies how API keys are approved to access the APIs defined by the API product. If set to `manual`, the consumer key is generated and returned as `pending`. In this case, the API keys won't work until they are explicitly approved. If set to `auto`, the consumer key is generated and returned as `approved` and can be used immediately.   
`description` Type: `string` | Description of the API product.   
`displayName` Type: `string` | Name displayed in the UI or developer portal to developers registering for API access.   
`analytics` Type: Analytics  | Defines whether analytics should be collected for operations associated with this product.   
`enforcementRefs` Type: `Array` | Array of EnforcementRef resources to apply to the API product.   
`attributes` Type: `Array` | Array of attributes that may be used to extend the default API product profile with customer-specific metadata.   
  
### EnforcementRef

**Field** | **Description**  
---|---  
`name` Type: `string` | The name of the target resource.   
`kind` Type: `string` | `APIMExtensionPolicy`  
`group` Type: `string` | The [APIGroup](https://kubernetes.io/docs/reference/using-api/#api-groups) for Apigee APIM Operator, which is `apim.googleapis.com`.   
`namespace` Type: `string` | (Optional) The namespace of the referent. When unspecified, the local namespace is inferred.  
  
### Attribute

**Field** | **Description**  
---|---  
`name` Type: `string` | The key of the attribute.   
`value` Type: `string` | The value of the attribute.   
  
## APIOperationSet

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | `apim.googleapis.com/v1`  
`kind` Type: `string` | `APIOperationSet`  
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: APIOperationSetSpec | Defines the desired state of the APIOperationSet.   
  
### APIOperationSetSpec

**Field** | **Description**  
---|---  
`quota` Type: Quota | Quota definition.   
`restOperations` Type: `Array` | Array of RESTOperation definitions.   
`apiProductRefs` Type: `Array` | Array of APIProductRef resources, or references to API Products where the RESTOperations should apply.   
  
### Quota

**Field** | **Description**  
---|---  
`limit` Type: `integer` | Number of request messages permitted per app by the API product for the specified `interval` and `timeUnit`.   
`interval` Type: `integer` | Time interval over which the number of request messages is calculated.   
`timeUnit` Type: `string` | Time unit defined for the interval. Valid values include `minute`, `hour`, `day`, or `month`.   
  
### RESTOperation

**Field** | **Description**  
---|---  
`name` Type: `string` | The name of the of the REST operation.   
`path` Type: `string` | In combination with `methods`, `path` is the HTTP path to match for a quota and/or for an API product.   
`methods` Type: `array` | In combination with `path`, `methods` is the list (as `strings`) of applicable http methods to match for a quota and/or for an API product.   
  
### APIProductRef

**Field** | **Description**  
---|---  
`name` Type: `string` | The name of the target resource.   
`kind` Type: `string` | `APIProduct`  
`group` Type: `string` | The [APIGroup](https://kubernetes.io/docs/reference/using-api/#api-groups) for Apigee APIM Operator, which is `apim.googleapis.com`.   
`namespace` Type: `string` | (Optional) The namespace of the referent. When unspecified, the local namespace is inferred.  
  
## APIMExtensionPolicy

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | `apim.googleapis.com/v1`  
`kind` Type: `string` | APIMExtensionPolicy   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: APIMExtensionPolicySpec | Defines the desired state of APIMExtensionPolicy.   
  
### APIMExtensionPolicySpec

**Field** | **Description**  
---|---  
`apigeeEnv` | (Optional) Apigee environment. If not provided, a new environment is created and attached to all available instances. If provided, this environment must be attached to all available instances while using an external global load balancer.   
`failOpen` Type: ``boolean`` | Specifies whether or not to _fail open_ when the Apigee runtime is unreachable. If set to `true`, calls to the Apigee runtime will be treated as successful even if the runtime is unreachable.   
`timeout` Type: `string` | Specifies the timeout period before calls to the Apigee runtime fail, in seconds or milliseconds. For example, `10s`.   
`targetRef` Type: ExtensionServerRef | Identifies the Google Kubernetes Engine Gateway where the extension should be installed.   
`location` Type: `string` | Identifies the Google Cloud location where APIMExtensionPolicy is enforced.   
`supportedEvents` Type: `List` of events  | Specifies the list of extension processor events sent to Apigee. These include the following: 

  * `"REQUEST_HEADERS"`
  * `"RESPONSE_HEADERS"`
  * `"REQUEST_BODY"` (Preview)
  * `"RESPONSE_BODY"` (Preview)
  * `"REQUEST_TRAILERS"`
  * `"RESPONSE_TRAILERS"`

  
  
### ExtensionServerRef

**Field** | **Description**  
---|---  
`name` Type: `string` | The name of the target resource.   
`kind` Type: `string` | Specifies the `kind` of the target resource, for example, `Gateway` or `Service`.   
`group` Type: `string` | The [APIGroup](https://kubernetes.io/docs/reference/using-api/#api-groups) for Apigee APIM Operator, which is `apim.googleapis.com`.   
`namespace` Type: `string` | (Optional) The namespace of the referent. When unspecified, the local namespace is inferred.  
  
## ApigeeGatewayPolicy

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | ApigeeGatewayPolicy   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: ApigeeGatewayPolicySpec | Defines the desired state of ApigeeGatewayPolicy.   
  
### ApigeeGatewayPolicySpec

**Field** | **Description**  
---|---  
`ref`Type: ExtensionServerRef | Refers to the APIM template created to govern the policies applied to the GKE Gateway.   
`targetRef` Type: ExtensionServerRef | Refers to the APIM extension policy that should apply this specific Gateway policy. Indirectly refers to the GKE Gateway.   
`serviceAccount` | (Optional) Specifies the service account used to generate Google auth tokens in an Apigee ProApigee proxy.   
  
### ApimTemplate

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | ApimTemplate   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: ApimTemplateSpec | Defines the desired state of ApimTemplate.   
  
### ApimTemplateSpec

**Field** | **Description**  
---|---  
`templates` Type: `list` | A list of ApimTemplateFlow resources that specify the policies that are to be executed in the request flow.   
`apimTemplateRule` Type: ExtensionServerRef | Specifies the APIM template rule that should be used to validate the applied policies.   
  
### ApimTemplateFlow

**Field** | **Description**  
---|---  
`policies` Type: `list` ConditionalParameterReference |  A list of ConditionalParameterReference resources that specify the ordered list of policies to be executed as part of the request flow.   
`condition` Type: `string` | Specifies the conditions for executing this resource.   
  
### ConditionalParameterReference

**Field** | **Description**  
---|---  
`condition` `Type: `string`` | Specifies the conditions for executing this resource.   
  
## ApimTemplateRule

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | ApimTemplateRule   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: ApimTemplateRuleSpec | Defines the desired state of ApimTemplateRule.   
  
### ApimTemplateRuleSpec

**Field** | **Description**  
---|---  
`requiredList` | The list of policies (as `strings`) that _must_ be present in the ApimTemplate.   
`denyList` | The list of policies (as `strings`) that _should not_ be present in the ApimTemplate.   
`allowList` | The list of policies (as `strings`) that _may_ be present in the ApimTemplate but are not required.   
`override` Type: `boolean` | Overrides updates to the APIM template rule in the event that APIM templates using the rule exist. Valid values are `true` or `false`.   
  
## AssignMessage (Google token injection)

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | AssignMessage   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: AssignMessageBean | Defines the desired state of the AssignMessage policy.   
  
### AssignMessageBean

**Field** | **Description**  
---|---  
`setActions` Type: `array` | Array of `SetActionsBean` objects. Replaces values of existing properties on the request or response, as specified by the `AssignTo` element. If the headers or parameters are already present in the original message, `setActions` overwrites the values. Otherwise, `setActions` adds new headers or parameters as specified.   
`AssignTo` Type: AssignToBean | Specifies which message the AssignMessage policy operates on. Options include the request, the response, or a new custom message.   
  
### SetActionsBean

**Field** | **Description**  
---|---  
`Authentication` Type: AuthenticationBean | Generates Google OAuth 2.0 or OpenID Connect tokens to make authenticated calls to Google services or custom services running on certain Google Cloud products, such as Cloud Run functions and Cloud Run.   
  
### AuthenticationBean

**Field** | **Description**  
---|---  
`GoogleAccessToken` Type: GoogleAccessTokenBean | Generates [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) tokens to make authenticated calls to Google services.   
`GoogleIDToken` Type: GoogleIDTokenBean | Configuration to generate an OpenID Connect Token to authenticate the target request.   
`headerName` Type: `string` | By default, when an Authentication configuration is present, Apigee generates a bearer token and injects it into the Authorization header of the message sent to the target system. The `headerName` element allows you to specify the name of a _different_ header to hold the bearer token.   
  
### GoogleAccessTokenBean

**Field** | **Description**  
---|---  
`scopes` Type: `array` | Array of `strings` that specifies a valid Google API scope. For more information, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/googlescopes).   
`LifetimeInSeconds` Type: `integer` | Specifies the lifetime duration of the access token in seconds.   
  
### GoogleIDTokenBean

**Field** | **Description**  
---|---  
`Audience` Type: AudienceBean | The audience for the generated authentication token, such as the API or service account granted access by the token.   
`IncludeEmail` Type: `boolean` | If set to `true`, the generated authentication token will contain the service account `email` and `email_verified` claims.   
  
### AudienceBean

**Field** | **Description**  
---|---  
`useTargetHost` Type: `string` | If the value of `Audience` is empty or the `ref` variable does not resolve to a valid value, and `useTargetUrl` is `true`, then the URL of the target (excluding any query parameters) is used as the audience.   
`useTargetUrl` Type: `boolean` | By default, `useTargetUrl` is `false`.   
  
### AssignToBean

**Field** | **Description**  
---|---  
`createNew` Type: `boolean` | Determines whether the policy creates a new message when assigning values. If set to `true`, the policy creates a new message.   
`type` Type: `string` | Specifies the type of the new message, when `CreateNew` is set to `true` true. Valid values are **request** or **response**.   
  
## Javascript

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | JavaScript   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: JavascriptBean | Defines the desired state of the JavaScript policy.   
  
### JavascriptBean

**Field** | **Description**  
---|---  
`mode` Type: `array` | Array of `strings` that specifies `ProxyRequest` or `ProxyResponse`. Determines whether the policy is attached to the request flow or response flow.   
`source` Type: `string` | Inline JavaScript code.   
`timeLimit` Type: `integer` | Specifies the timeout for JavaScript code execution.   
  
## KVM

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | KVM   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: KeyValueMapOperationsBean | Defines the desired state of the KVM policy.   
  
### KeyValueMapOperationsBean

**Field** | **Description**  
---|---  
`MapName` Type: `MapName` | Enables the policy to identify which KVM to use dynamically, at runtime. For more information, see [MapName element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#mapname).  
`expiryTimeInSecs` Type: `integer` | Specifies the duration in seconds after which Apigee refreshes its cached value from the specified KVM. For more information, see [ExpiryTimeInSecs element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#expirytimeinsecs).  
`initialEntries` Type: `list` | Seed values for KVMs, which are populated in the KVM when it is initialized. For more information, see [InitialEntries element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#InitialEntriesElement).  
`delete` Type: `list` of `Delete` | Deletes the specified key/value pair from the KVM. For more information, see [Delete element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#DeleteElement).  
`get` Type: `list` of `Get` | Retrieves the value of a key from the KVM. For more information, see [Get element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#GetElement).  
  
## OASValidation

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | OASValidation  
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: OASValidationBean | Defines the desired state of the OASValidation policy.   
`status` Type: ApimResourceStatus | Shows the OASValidation policy status.   
  
### OASValidationBean

**Field** | **Description**  
---|---  
`openApiSpec` Type: `string` | Specifies the OpenAPI spec in `yaml` to be validated. Because this is a multiline `yaml` fragment, use the "|" delimiter.  
`source` Type: `string` | One of `message`, `request`, or `response`. When set to `request`, it will evaluate inbound requests from client apps; when set to `response`, it will evaluate responses from target servers. When set to `message`, it will automatically evaluate request or response depending on whether the policy is attached to the request or response flow.  
`options` Type: `OASValidationOptions` | See OASValidationOptions/td>  
  
### OASValidationOptions

**Field** | **Description**  
---|---  
`validateMessageBody` Type: `boolean` | Specifies whether the policy should validate the message body against the operation's request body schema in the OpenAPI Specification. Set to `true` to validate the message body contents. Set to `false` to validate only that the message body exists.  
`allowUnspecifiedParameters` Type: `StrictOptions` | See StrictOptions  
  
### StrictOptions

**Field** | **Description**  
---|---  
`header` Type: `boolean` | To allow header parameters to be specified in the request that are not defined in the OpenAPI Specification, set this parameter to `true`. Otherwise, set this parameter to `false` to cause policy execution to fail.  
`query` Type: `boolean` | To allow query parameters to be specified in the request that are not defined in the OpenAPI Specification, set this parameter to `true`. Otherwise, set this parameter to `false` to cause policy execution to fail.  
`cookie` Type: `boolean` | To allow cookie parameters to be specified in the request that are not defined in the OpenAPI Specification, set this parameter to `true`. Otherwise, set this parameter to `false` to cause policy execution to fail.  
  
## ApimResourceStatus

**Field** | **Description**  
---|---  
`currentState` Type: `enum` | Shows the current state of the resource: 

  * `RUNNING` = resource is in running state.
  * `CREATING` = resource is being created
  * `CREATED` = resource has been created
  * `UPDATING` = resource is being updated
  * `DELETING` = resource is being deleted
  * `CREATE_UPDATE_FAILED` = create or update operation failed
  * `DELETE_FAILED` = delete operation failed

  
`errorMessage` Type: `string` | Error message related to one of the failure states of `currentState` field.  
`operationResult` Type: `string` | A response string from one of the long running operations related to resource creation, update, or deletion.  
  
## ServiceCallout

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | ServiceCallout  
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: ServiceCalloutBean | Defines the desired state of the ServiceCallout policy.   
`status` Type: ApimResourceStatus | Shows the ServiceCallout policy status.   
  
### ServiceCalloutBean

**Field** | **Description**  
---|---  
`httpTargetConnection` Type: `HttpTargetConnection` | Provides transport details such as URL, TLS/SSL, and HTTP properties.  
`request` Type: CalloutRequest | Specifies the variable containing the request message that gets sent from the API proxy to the other service.  
`Response` Type: `string` | Specifies the variable containing the response message that gets returned to the API proxy from the external service.  
  
### HttpTargetConnection

**Field** | **Description**  
---|---  
`url` Type: `string` | The URL of the target service.  
`properties` Type: `Map` of `<string, string>``` | HTTP transport properties to the backend service. For more information, see [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).  
`timeout` Type: `int` | The timeout in milliseconds for the service callout. For more information, see [timeout](https://cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy#timeout).  
  
### CalloutRequest

**Field** | **Description**  
---|---  
`url` Type: `string` | The URL of the target service.  
`properties` Type: `Map` of `<string, string>``` | HTTP transport properties to the backend service. For more information, see [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).  
  
## SpikeArrest

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | SpikeArrest   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: SpikeArrestBean | Defines the desired state of the SpikeArrest policy.   
  
### SpikeArrestBean

**Field** | **Description**  
---|---  
`mode` Type: `array` | Array of `strings` that specifies `ProxyRequest` or `ProxyResponse`. Determines whether the policy is attached to the request flow or response flow.   
`peakMessageRate` Type: peakMessageRate | Specifies the message [rate](https://cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate) for SpikeArrest.   
`useEffectiveCount` Type: ``boolean`` | If set to `true`true, SpikeArrest is distributed in a region, with request counts synchronized across Apigee message processors (MPs) in a region. If set to `false`, SpikeArrest uses a [token bucket](https://wikipedia.org/wiki/Token_bucket) algorithm locally. For more information, see [ UseEffectiveCount](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount).  
  
### peakMessageRate

**Field** | **Description**  
---|---  
`ref` Type: `string` | Variable referencing the `rate` value.   
`value` Type: `string` | Actual `rate` value if a reference is not available.   
  
## GenerateJWT

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | GenerateJWT   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: GenerateJWTBean | Defines the desired state of the GenerateJWT policy.   
`status` Type: ApimResourceStatus | Shows the GenerateJWT policy status.   
  
### GenerateJWTBean

**Field** | **Description**  
---|---  
`subject` Type: PropertyBean | Identifies the principal that is the subject of the JWT. For more information, see [Subject element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#subject).  
`issuer` Type: PropertyBean | Identifies the principal that issued the JWT. For more information, see [Issuer element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#issuer).  
`audience` Type: VarArrayBean | Identifies the recipients that the JWT is intended for. For more information, see [Audience element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#audience).  
`id` Type: PropertyBean | Specifies a unique identifier for the JWT. For more information, see [Id element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#id).  
`expiresIn` Type: PropertyBean | Specifies the expiration time for the JWT. For more information, see [ExpiresIn element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#expiresin).  
`notBefore` Type: PropertyBean | Identifies the time before which the JWT must not be accepted for processing. For more information, see [NotBefore element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#notbefore).  
`additionalClaims` Type: AdditionalClaimsBean | Specifies additional claims to include in the JWT. For more information, see [AdditionalClaims element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#additionalclaimsclaim).  
`compress` Type: `boolean` | Specifies whether to compress the JWT payload. For more information, see [Compress element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#compress).  
  
### PropertyBean

**Field** | **Description**  
---|---  
`value` Type: `string` | The literal value of the property.  
`ref` Type: `string` | A reference to a variable containing the value of the property.  
  
### VarArrayBean

**Field** | **Description**  
---|---  
`values` Type: `array` of `string` | An array of literal string values.  
`ref` Type: `string` | A reference to a variable containing the array of values.  
  
### AdditionalClaimsBean

**Field** | **Description**  
---|---  
`claims` Type: `map` of `string` to `string` | A map of claim names to claim values.  
`ref` Type: `string` | A reference to a variable containing the claims map.  
  
## OAuthV2

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | OAuthV2   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: OAuthV2Bean | Defines the desired state of the OAuthV2 policy.   
`status` Type: ApimResourceStatus | Shows the OAuthV2 policy status.   
  
### OAuthV2Bean

**Field** | **Description**  
---|---  
`operation` Type: `enum` | The OAuthV2 operation to perform. Valid values are: 

  * `GenerateAuthorizationCode`
  * `GenerateAccessToken`
  * `GenerateAccessTokenImplicitGrant`
  * `GenerateJWTAccessTokenImplicitGrant`
  * `GenerateJWTAccessToken`
  * `RefreshAccessToken`
  * `RefreshJWTAccessToken`
  * `VerifyAccessToken`
  * `VerifyJWTAccessToken`
  * `ValidateToken`
  * `InvalidateToken`

For more information, see [Operation element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#operationelement).   
`configRef` Type: `string` | (Optional) Reference to an `OAuthV2Config` custom resource name containing reusable OAuthV2 settings.  
`scope` Type: `string` | The scope of the access token. For more information, see [Scope element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#scopeelement).  
`generateResponse` Type: GenerateResponse | Configures the response generation. For more information, see [GenerateResponse element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#generateresponseelement).  
`generateErrorResponse` Type: GenerateErrorResponse | Configures the error response generation. For more information, see [GenerateErrorResponse element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#generateerrorresponseelement).  
`expiresIn` Type: PropertyExpiryBean | The expiration time of the access token. For more information, see [ExpiresIn element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#expiresinelement).  
`refreshTokenExpiresIn` Type: PropertyExpiryBean | The expiration time of the refresh token. For more information, see [RefreshTokenExpiresIn element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#refreshtokenexpiresinelement).  
`supportedGrantTypes` Type: `array` of `string` | A list of supported grant types. For more information, see [SupportedGrantTypes element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#supportedgranttypesgranttypeelement).  
`redirectURI` Type: `string` | The redirect URI used in the authorization code grant type. For more information, see [RedirectUri element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#redirecturielement).  
`responseType` Type: `string` | The response type for the authorization code grant type. For more information, see [ResponseType element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#responsetypeelement).  
`clientID` Type: `string` | The client ID. For more information, see [ClientId element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#clientidelement).  
`state` Type: `string` | The state parameter for the authorization code grant type. For more information, see [State element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#stateelement).  
`appEndUser` Type: `string` | The end user ID. For more information, see [AppEndUser element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#appenduserelement).  
`code` Type: `string` | The authorization code. For more information, see [Code element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#codeelement).  
`userName` Type: `string` | The username for the password grant type. For more information, see [UserName element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#usernameelement).  
`password` Type: `string` | The password for the password grant type. For more information, see [Password element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#passwordelement).  
`grantType` Type: `string` | The grant type. For more information, see [GrantType element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#granttype).  
`refreshToken` Type: `string` | The refresh token. For more information, see [RefreshToken element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#refreshtokenelement).  
`accessToken` Type: `string` | The access token. For more information, see [AccessToken element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#accesstokenelement).  
`cacheExpiryInSeconds` Type: PropertyExpiryBean | The cache expiry time in seconds. For more information, see [Cache Expiry Settings](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#cache_expiry).  
`verifyAccessTokenPrefix` Type: `string` | (Optional) Prefix to use when verifying an access token.  
`externalAuthorization` Type: `boolean` | Indicates whether to use an external authorization service. For more information, see [ExternalAuthorization element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#externalauthorization-element).  
`reuseRefreshToken` Type: `boolean` | Specifies whether to reuse refresh tokens. For more information, see [ReuseRefreshToken element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#reuserefreshtoken).  
`rfcCompliance` Type: `boolean` | Enforces RFC compliance. For more information, see [RFCCompliantRequestResponse element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#RFCCompliantRequestResponseElement).  
`enforceStrictCallbackURIEnforced` Type: `boolean` | (Optional) Enforces strict callback URI matching.  
`customAttributes` Type: `array` of CustomAttribute | Custom attributes to add to the token. For more information, see [Attributes element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#attributesattribute).  
`externalAccessToken` Type: `string` | An external access token. For more information, see [ExternalAccessToken element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#externalaccesstoken-element).  
`externalRefreshToken` Type: `string` | An external refresh token. For more information, see [ExternalRefreshToken element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#externalrefreshtoken-element).  
`storeToken` Type: `string` | Specifies whether to store the token. For more information, see [StoreToken element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#storetokenelement).  
`tokens` Type: `array` of `Token` | A list of tokens to invalidate. For more information, see [Tokens element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#tokenstokenelement).  
`algorithm` Type: `string` | The algorithm used to sign the JWT. For more information, see [Algorithm element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#algorithm).  
`secretKey` Type: SecretKey | The secret key used to sign the JWT. For more information, see [SecretKey element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#secretkeyvalue).  
`privateKey` Type: PrivateKey | The private key used to sign the JWT. For more information, see [PrivateKey element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#privatekeyvalue).  
`publicKey` Type: PublicKey | The public key used to verify the JWT. For more information, see [PublicKey element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#publickeyvalue).  
  
### GenerateResponse

**Field** | **Description**  
---|---  
`enabled` Type: `boolean` | If set to `true` or if the enabled attribute is omitted, the policy generates and returns a response.  
`format` Type: `enum` | One of `XML`, `FORM_PARAM`.  
  
### GenerateErrorResponse

**Field** | **Description**  
---|---  
`enabled` Type: `boolean` | If set to `true` or if the enabled attribute is omitted, the policy generates and returns a response.  
`format` Type: `enum` | One of `XML`, `FORM_PARAM`.  
`realm` Type: PropertyBean | The realm to return in the `WWW-Authenticate` header.  
  
### PropertyExpiryBean

**Field** | **Description**  
---|---  
`value` Type: `long` | The literal value of the expiration.  
`ref` Type: `string` | A reference to a variable containing the expiration value.  
  
### CustomAttribute

**Field** | **Description**  
---|---  
`name` Type: `string` | The name of the custom attribute.  
`ref` Type: `string` | A reference to a variable containing the attribute value.  
`value` Type: `string` | The literal value of the attribute.  
  
### SecretKey

**Field** | **Description**  
---|---  
`value` Type: PropertyBean | Specifies the secret key used to sign the JWT. For more information, see [SecretKey element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#secretkeyvalue).  
  
### PrivateKey

**Field** | **Description**  
---|---  
`value` Type: PropertyBean | Specifies the private key used to sign the JWT. For more information, see [PrivateKey element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#privatekeyvalue).  
  
### PublicKey

**Field** | **Description**  
---|---  
`value` Type: PropertyBean | Specifies the public key used to verify the JWT. For more information, see [PublicKey element](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#publickeyvalue).  
  
## ResponseCache Policy

**Field** | **Description**  
---|---  
`apiVersion` Type: `string` | apim.googleapis.com/v1   
`kind` Type: `string` | ResponseCache   
`metadata` Type: [Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#objectmeta-v1-meta) | Refer to the Kubernetes API documentation for the fields available in `metadata`.   
`spec` Type: APIExtensionPolicySpec | Defines the desired state of ResponseCache.   
  
### ResponseCacheBean

**Field** | **Description**  
---|---  
`mode` Type: `boolean` | Specifies `ProxyRequest` or `ProxyResponse`. Determines whether the policy is attached to the request flow or response flow.   
`cacheExpiry` Type: cacheExpiry | Provides the cacheExpiry object.   
`cacheKey` Type: cacheKey | Provides the cacheKey object.   
`cacheLookupTimeOut` type: `integer` | Specifies the cache look up timeout period.   
`cacheResourceRef` type: `string` | Specifies the cache resource identifier using a variable reference.   
`excludeErrorResponse` type: `boolean` | This policy can cache HTTP responses with **any** status code. That means both success and error responses can be cached, including `2xx` and `3xx` status codes.   
`skipCacheLookupCondition` type: `string` | Defines an expression that, if it evaluates to `true` at runtime, specifies that cache lookup should be skipped and the cache should be refreshed   
`skipCachePopulationCondition` type: `string` | Defines an expression that, if it evaluates to `true` at runtime, specifies that cache lookup should be skipped and the cache should be refreshed at runtime, specifies that a write to the cache should be skipped.   
`useAcceptHeader` type: `boolean` | Set to `true` to append values from response `Accept` headers to the response cache entry's cache key.   
`useResponseCacheHeaders` type: `boolean` | Set to `true` to have HTTP response headers considered when setting the "time to live" (TTL) of the response in the cache.   
  
### cacheExpiry

**Field** | **Description**  
---|---  
`expiryDate` Type: `object` | Specifies the date on which a cache entry should expire.   
`timeOfDay` Type: `object` | Specifies the time of day at which a cache entry should expire.   
`timeoutInSeconds` Type: `object` | Specifies the number of seconds after which a cache entry should expire.   
  
### cacheKey

**Field** | **Description**  
---|---  
`cacheKeyPrefix` Type: `string` | Specifies a value to use as a cache key prefix.   
`fragments` Type: `object` | Specifies a value to be included in the cache key to create a namespace for matching requests to cached responses.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
