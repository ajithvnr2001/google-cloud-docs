---
url: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters
title: REST Resource: accessPolicies.servicePerimeters \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:19.894379+00:00
---

# REST Resource: accessPolicies.servicePerimeters  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  REST Resource: accessPolicies.servicePerimeters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServicePerimeter
    * JSON representation
  * PerimeterType
  * ServicePerimeterConfig
    * JSON representation
  * VpcAccessibleServices
    * JSON representation
  * ServicePattern
    * JSON representation
  * Modifier
    * JSON representation
  * AddRequestHeader
    * JSON representation
  * ServicePatternsEnforcementScope
  * IngressPolicy
    * JSON representation
  * IngressFrom
    * JSON representation
  * IngressSource
    * JSON representation
  * PrivateServiceConnectEndpoint
    * JSON representation
  * IdentityType
  * IngressTo
    * JSON representation
  * ApiOperation
    * JSON representation
  * EgressPolicy
    * JSON representation
  * EgressFrom
    * JSON representation
  * EgressSource
    * JSON representation
  * SourceRestriction
  * EgressTo
    * JSON representation
  * Methods



## Resource: ServicePerimeter

`ServicePerimeter` describes a set of Google Cloud resources which can freely import and export data amongst themselves, but not export outside of the `ServicePerimeter`. If a request with a source within this `ServicePerimeter` has a target outside of the `ServicePerimeter`, the request will be blocked. Otherwise the request is allowed. There are two types of Service Perimeter - Regular and Bridge. Regular Service Perimeters cannot overlap, a single Google Cloud project or VPC network can only belong to a single regular Service Perimeter. Service Perimeter Bridges can contain only Google Cloud projects as members, a single Google Cloud project may belong to multiple Service Perimeter Bridges.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
      "perimeterType": enum ([PerimeterType](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PerimeterType)),
      "status": {
        object ([ServicePerimeterConfig](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeterConfig))
      },
      "spec": {
        object ([ServicePerimeterConfig](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeterConfig))
      },
      "useExplicitDryRunSpec": boolean,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for the `ServicePerimeter`. Format: `accessPolicies/{access_policy}/servicePerimeters/{servicePerimeter}`.The `servicePerimeter` component must begin with a letter, followed by alphanumeric characters or `_`.After you create a `ServicePerimeter`, you cannot change its `name`.  
`title` |  `string` Human readable title. Must be unique within the Policy.  
`description` |  `string` Description of the `ServicePerimeter` and its use. Does not affect behavior.  
`perimeterType` |  `enum (`[PerimeterType](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PerimeterType)`)` Perimeter type indicator. A single project or VPC network is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty.  
`status` |  `object (`[ServicePerimeterConfig](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeterConfig)`)` Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries.  
`spec` |  `object (`[ServicePerimeterConfig](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeterConfig)`)` Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "useExplicitDryRunSpec" flag is set.  
`useExplicitDryRunSpec` |  `boolean` Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values.  
`etag` |  `string` Optional. An opaque identifier for the current version of the `ServicePerimeter`. This identifier does not follow any specific format. If an etag is not provided, the operation will be performed as if a valid etag is provided.  
  
## PerimeterType

Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter.

In addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by the regular perimeter that resource is in.

Perimeter Bridges are typically useful when building more complex toplogies with many independent perimeters that need to share some data with a common perimeter, but should not be able to share data among themselves.

Enums  
---  
`PERIMETER_TYPE_REGULAR` | Regular Perimeter. When no value is specified, the perimeter uses this type.  
`PERIMETER_TYPE_BRIDGE` | Perimeter Bridge.  
  
## ServicePerimeterConfig

`ServicePerimeterConfig` specifies a set of Google Cloud resources that describe specific Service Perimeter configuration.

JSON representation  
---  
      
    
    {
      "resources": [
        string
      ],
      "accessLevels": [
        string
      ],
      "restrictedServices": [
        string
      ],
      "vpcAccessibleServices": {
        object ([VpcAccessibleServices](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#VpcAccessibleServices))
      },
      "ingressPolicies": [
        {
          object ([IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy))
        }
      ],
      "egressPolicies": [
        {
          object ([EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy))
        }
      ]
    }  
  
Fields  
---  
`resources[]` |  `string` A list of Google Cloud resources that are inside of the service perimeter. Currently only projects and VPCs are allowed. Project format: `projects/{projectNumber}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`.  
`accessLevels[]` |  `string` A list of `AccessLevel` resource names that allow resources within the `ServicePerimeter` to be accessed from the internet. `AccessLevels` listed must be in the same policy as this `ServicePerimeter`. Referencing a nonexistent `AccessLevel` is a syntax error. If no `AccessLevel` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `"accessPolicies/MY_POLICY/accessLevels/MY_LEVEL"`. For Service Perimeter Bridge, must be empty.  
`restrictedServices[]` |  `string` Google Cloud services that are subject to the Service Perimeter restrictions. For example, if `storage.googleapis.com` is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions.  
`vpcAccessibleServices` |  `object (`[VpcAccessibleServices](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#VpcAccessibleServices)`)` Configuration for APIs allowed within Perimeter.  
`ingressPolicies[]` |  `object (`[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)`)` List of `[IngressPolicies](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` to apply to the perimeter. A perimeter may have multiple `[IngressPolicies](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)`, each of which is evaluated separately. Access is granted if any `[Ingress Policy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` grants it. Must be empty for a perimeter bridge.  
`egressPolicies[]` |  `object (`[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)`)` List of `[EgressPolicies](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` to apply to the perimeter. A perimeter may have multiple `[EgressPolicies](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)`, each of which is evaluated separately. Access is granted if any `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` grants it. Must be empty for a perimeter bridge.  
  
## VpcAccessibleServices

Specifies how APIs are allowed to communicate within the Service Perimeter.

JSON representation  
---  
      
    
    {
      "enableRestriction": boolean,
      "allowedServices": [
        string
      ],
      "allowedServicePatterns": [
        {
          object ([ServicePattern](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePattern))
        }
      ],
      "servicePatternsEnforcementScopes": [
        enum ([ServicePatternsEnforcementScope](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePatternsEnforcementScope))
      ]
    }  
  
Fields  
---  
`enableRestriction` |  `boolean` Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'.  
`allowedServices[]` |  `string` The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True. You can specify a list of individual services, as well as include the 'RESTRICTED-SERVICES' value, which automatically includes all of the services protected by the perimeter.  
`allowedServicePatterns[]` |  `object (`[ServicePattern](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePattern)`)` Specifies which Google services are allowed to be accessed from VPC networks in the service perimeter.  
`servicePatternsEnforcementScopes[]` |  `enum (`[ServicePatternsEnforcementScope](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePatternsEnforcementScope)`)` Defines the enforcement scopes of service patterns.  
  
## ServicePattern

Service patterns used to allow access.

JSON representation  
---  
      
    
    {
      "modifiers": [
        {
          object ([Modifier](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#Modifier))
        }
      ],
    
      // Union field kind can be only one of the following:
      "service": string,
      "pattern": string
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`modifiers[]` |  `object (`[Modifier](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#Modifier)`)` Modifiers to apply to the requests that match the URL pattern.  
Union field `kind`. The service or pattern to allow. `kind` can be only one of the following:  
`service` |  `string` Supported service to allow.  
`pattern` |  `string` URL pattern to allow.Only patterns of ".googleapis.com/*", "www.googleapis.com//*" and "*.appspot.com/* forms are supported, where  should be an alphanumeric name.  
  
## Modifier

Modifier to apply to the API requests.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "addRequestHeader": {
        object ([AddRequestHeader](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#AddRequestHeader))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. Modifier to apply to the API requests. `kind` can be only one of the following:  
`addRequestHeader` |  `object (`[AddRequestHeader](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#AddRequestHeader)`)` Adds an additional HTTP request header.  
  
## AddRequestHeader

Adds a request header to the API.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` HTTP header key.  
`value` |  `string` HTTP header value.  
  
## ServicePatternsEnforcementScope

Defines the enforcement scope of service patterns.

Enums  
---  
`SERVICE_PATTERNS_ENFORCEMENT_SCOPE_UNSPECIFIED` | Default value. This cannot be used.  
`GOOGLE_APIS_VIA_PRIVATE_PATH` | Enables VPC Accessible Services enforcement for all APIs (including unsupported APIs) for Private Google Access configured with Private VIP and Private Service Connect Endpoint for Global Google APIs that uses 'all-apis' bundle.  
  
## IngressPolicy

Policy for ingress into `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`.

`[IngressPolicies](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` match requests based on `ingressFrom` and `ingressTo` stanzas. For an ingress policy to match, both the `ingressFrom` and `ingressTo` stanzas must be matched. If an `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` matches a request, the request is allowed through the perimeter boundary from outside the perimeter.

For example, access from the internet can be allowed either based on an `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` or, for traffic hosted on Google Cloud, the project of the source network. For access from private networks, using the project of the hosting network is required.

Individual ingress policies can be limited by restricting which services and/or actions they match using the `ingressTo` field.

JSON representation  
---  
      
    
    {
      "ingressFrom": {
        object ([IngressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressFrom))
      },
      "ingressTo": {
        object ([IngressTo](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressTo))
      },
      "title": string
    }  
  
Fields  
---  
`ingressFrom` |  `object (`[IngressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressFrom)`)` Defines the conditions on the source of a request causing this `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` to apply.  
`ingressTo` |  `object (`[IngressTo](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressTo)`)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)` and request destination that cause this `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the ingress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
## IngressFrom

Defines the conditions under which an `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` matches a request. Conditions are based on information about the source of the request. The request must satisfy what is defined in `sources` AND identity related fields in order to match.

JSON representation  
---  
      
    
    {
      "sources": [
        {
          object ([IngressSource](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressSource))
        }
      ],
      "identities": [
        string
      ],
      "identityType": enum ([IdentityType](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IdentityType))
    }  
  
Fields  
---  
`sources[]` |  `object (`[IngressSource](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressSource)`)` Sources that this `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` authorizes access from.  
`identities[]` |  `string` A list of identities that are allowed access through [IngressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identityType` |  `enum (`[IdentityType](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IdentityType)`)` Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
  
## IngressSource

The source that `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` authorizes access from.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "accessLevel": string,
      "resource": string,
      "pscEndpoint": {
        object ([PrivateServiceConnectEndpoint](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PrivateServiceConnectEndpoint))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Allowed ingress source. It can be one of `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` or Google Cloud resource or a `[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PrivateServiceConnectEndpoint)`. `source` can be only one of the following:  
`accessLevel` |  `string` An `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` resource name that allow resources within the `[ServicePerimeters](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` to be accessed from the internet. `[AccessLevels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` listed must be in the same policy as this `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`. Referencing a nonexistent `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` will cause an error. If no `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `accessLevel`, then all `[IngressSources](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressSource)` will be allowed.  
`resource` |  `string` A Google Cloud resource that is allowed to ingress the perimeter. Requests from these resources will be allowed to access perimeter data. Currently only projects and VPCs are allowed. Project format: `projects/{projectNumber}` VPC network format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`. The project may be in any Google Cloud organization, not just the organization that the perimeter is defined in. `*` is not allowed, the case of allowing all Google Cloud resources only is not supported.  
`pscEndpoint` |  `object (`[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PrivateServiceConnectEndpoint)`)` A `[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PrivateServiceConnectEndpoint)` that is allowed to access the perimeter. The Private Service Connect endpoint may be in any organization, not just the organization that the perimeter is defined in.  
  
## PrivateServiceConnectEndpoint

Specifies the Private Service Connect endpoint that an API call refers to.

JSON representation  
---  
      
    
    {
      "forwardingRule": string
    }  
  
Fields  
---  
`forwardingRule` |  `string` The full resource name of the global forwarding rule that identifies a Private Service Connect endpoint. Forwarding rule format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/forwardingRules/{FORWARDING_RULE_ID}`.  
  
## IdentityType

Specifies the types of identities that are allowed access in either `[IngressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressFrom)` or `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressFrom)` rules.

Enums  
---  
`IDENTITY_TYPE_UNSPECIFIED` | No blanket identity group specified.  
`ANY_IDENTITY` | Authorize access from all identities outside the perimeter.  
`ANY_USER_ACCOUNT` | Authorize access from all human users outside the perimeter.  
`ANY_SERVICE_ACCOUNT` | Authorize access from all service accounts outside the perimeter.  
  
## IngressTo

Defines the conditions under which an `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` matches a request. Conditions are based on information about the `[ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)` intended to be performed on the target resource of the request. The request must satisfy what is defined in `operations` AND `resources` in order to match.

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation))
        }
      ],
      "resources": [
        string
      ],
      "roles": [
        string
      ]
    }  
  
Fields  
---  
`operations[]` |  `object (`[ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)`)` A list of `[ApiOperations](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)` allowed to be performed by the sources specified in corresponding `[IngressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressFrom)` in this `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`.  
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, protected by this `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` that are allowed to be accessed by sources defined in the corresponding `[IngressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressFrom)`. If a single `*` is specified, then access to all resources inside the perimeter are allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[IngressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressFrom)` are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`.  
  
## ApiOperation

Identification for an API Operation.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "methodSelectors": [
        {
          object ([MethodSelector](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/MethodSelector))
        }
      ]
    }  
  
Fields  
---  
`serviceName` |  `string` The name of the API whose methods or permissions the `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` or `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` want to allow. A single `[ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)` with `serviceName` field set to `*` will allow all methods AND permissions for all services.  
`methodSelectors[]` |  `object (`[MethodSelector](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/MethodSelector)`)` API methods or permissions to allow. Method or permission must belong to the service specified by `serviceName` field. A single `[MethodSelector](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/MethodSelector)` entry with `*` specified for the `method` field will allow all methods AND permissions for the service specified in `serviceName`.  
  
## EgressPolicy

Policy for egress from perimeter.

`[EgressPolicies](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` match requests based on `egressFrom` and `egressTo` stanzas. For an `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` to match, both `egressFrom` and `egressTo` stanzas must be matched. If an `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` matches a request, the request is allowed to span the `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` boundary. For example, an `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` can be used to allow VMs on networks within the `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` to access a defined set of projects outside the perimeter in certain contexts (e.g. to read data from a Cloud Storage bucket or query against a BigQuery dataset).

`[EgressPolicies](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` are concerned with the _resources_ that a request relates as well as the API services and API actions being used. They do not related to the direction of data movement. More detailed documentation for this concept can be found in the descriptions of `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressFrom)` and `[EgressTo](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressTo)`.

JSON representation  
---  
      
    
    {
      "egressFrom": {
        object ([EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressFrom))
      },
      "egressTo": {
        object ([EgressTo](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressTo))
      },
      "title": string
    }  
  
Fields  
---  
`egressFrom` |  `object (`[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressFrom)`)` Defines conditions on the source of a request causing this `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` to apply.  
`egressTo` |  `object (`[EgressTo](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressTo)`)` Defines the conditions on the `[ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)` and destination resources that cause this `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` to apply.  
`title` |  `string` Optional. Human-readable title for the egress rule. The title must be unique within the perimeter and can not exceed 100 characters. Within the access policy, the combined length of all rule titles must not exceed 240,000 characters.  
  
## EgressFrom

Defines the conditions under which an `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` matches a request. Conditions based on information about the source of the request. Note that if the destination of the request is also protected by a `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`, then that `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` must have an `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` which allows access in order for this request to succeed.

JSON representation  
---  
      
    
    {
      "identities": [
        string
      ],
      "identityType": enum ([IdentityType](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IdentityType)),
      "sources": [
        {
          object ([EgressSource](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressSource))
        }
      ],
      "sourceRestriction": enum ([SourceRestriction](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#SourceRestriction))
    }  
  
Fields  
---  
`identities[]` |  `string` A list of identities that are allowed access through [EgressPolicy]. Identities can be an individual user, service account, Google group, third-party identity, or agent identity. For the list of supported identity types, see <https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities>.  
`identityType` |  `enum (`[IdentityType](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IdentityType)`)` Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.  
`sources[]` |  `object (`[EgressSource](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressSource)`)` Sources that this `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#EgressPolicy)` authorizes access from. If this field is not empty, then `sourceRestriction` must be set to `SOURCE_RESTRICTION_ENABLED`.  
`sourceRestriction` |  `enum (`[SourceRestriction](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#SourceRestriction)`)` Whether to enforce traffic restrictions based on `sources` field. If the `sources` fields is non-empty, then this field must be set to `SOURCE_RESTRICTION_ENABLED`.  
  
## EgressSource

The source that `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#EgressPolicy)` authorizes access from inside the `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#ServicePerimeter)` to somewhere outside the `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#ServicePerimeter)` boundaries.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "accessLevel": string,
      "resource": string,
      "pscEndpoint": {
        object ([PrivateServiceConnectEndpoint](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PrivateServiceConnectEndpoint))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Allowed egress source. `source` can be only one of the following:  
`accessLevel` |  `string` An `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` resource name that allows protected resources inside the `[ServicePerimeters](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#ServicePerimeter)` to access outside the `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#ServicePerimeter)` boundaries. `[AccessLevels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` listed must be in the same policy as this `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#ServicePerimeter)`. Referencing a nonexistent `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` will cause an error. If an `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` name is not specified, only resources within the perimeter can be accessed through Google Cloud calls with request origins within the perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is specified for `accessLevel`, then all `[EgressSources](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#EgressSource)` will be allowed.  
`resource` |  `string` A Google Cloud resource from the service perimeter that you want to allow to access data outside the perimeter. This field supports only projects. The project format is `projects/{projectNumber}`. You can't use `*` in this field to allow all Google Cloud resources.  
`pscEndpoint` |  `object (`[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PrivateServiceConnectEndpoint)`)` A `[PrivateServiceConnectEndpoint](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#PrivateServiceConnectEndpoint)` that is allowed to access data outside the perimeter. The Private Service Connect endpoint may be in any organization, not just the organization that the perimeter is defined in.  
  
## SourceRestriction

Whether to enable the enforcement of traffic based on on the `sources` field. Only applies to `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#EgressFrom)`.

Enums  
---  
`SOURCE_RESTRICTION_UNSPECIFIED` | Enforcement preference unspecified, will not enforce traffic restrictions based on `sources` in `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#EgressFrom)`.  
`SOURCE_RESTRICTION_ENABLED` | Enforcement preference enabled, traffic restrictions will be enforced based on `sources` in `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#EgressFrom)`.  
`SOURCE_RESTRICTION_DISABLED` | Enforcement preference disabled, will not enforce traffic restrictions based on `sources` in `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters#EgressFrom)`.  
  
## EgressTo

Defines the conditions under which an `[EgressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressPolicy)` matches a request. Conditions are based on information about the `[ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)` intended to be performed on the `resources` specified. Note that if the destination of the request is also protected by a `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`, then that `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` must have an `[IngressPolicy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#IngressPolicy)` which allows access in order for this request to succeed. The request must match `operations` AND `resources` fields in order to be allowed egress out of the perimeter.

JSON representation  
---  
      
    
    {
      "resources": [
        string
      ],
      "operations": [
        {
          object ([ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation))
        }
      ],
      "externalResources": [
        string
      ],
      "roles": [
        string
      ]
    }  
  
Fields  
---  
`resources[]` |  `string` A list of resources, currently only projects in the form `projects/<projectnumber>`, that are allowed to be accessed by sources defined in the corresponding `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressFrom)`. A request matches if it contains a resource in this list. If `*` is specified for `resources`, then this `[EgressTo](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressTo)` rule will authorize access to all resources outside the perimeter.  
`operations[]` |  `object (`[ApiOperation](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)`)` A list of `[ApiOperations](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ApiOperation)` allowed to be performed by the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressFrom)`. A request matches if it uses an operation/service in this list.  
`externalResources[]` |  `string` A list of external resources that are allowed to be accessed. Only AWS and Azure resources are supported. For Amazon S3, the supported formats are s3://BUCKET_NAME, s3a://BUCKET_NAME, and s3n://BUCKET_NAME. For Azure Storage, the supported format is <azure://myaccount.blob.core.windows.net/CONTAINER_NAME>. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed.  
`roles[]` |  `string` IAM roles that represent the set of operations that the sources specified in the corresponding `[EgressFrom](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#EgressFrom)`. are allowed to perform in this `[ServicePerimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`.  
  
## Methods  
  
---  
  
### `[commit](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/commit)`

|  Commits the dry-run specification for all the `[service perimeters](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` in an `[access policy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)`.  
  
### `[create](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/create)`

|  Creates a `[service perimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`.  
  
### `[delete](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/delete)`

|  Deletes a `[service perimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` based on the resource name.  
  
### `[get](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/get)`

|  Gets a `[service perimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` based on the resource name.  
  
### `[list](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/list)`

|  Lists all `[service perimeters](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` for an access policy.  
  
### `[patch](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/patch)`

|  Updates a `[service perimeter](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`.  
  
### `[replaceAll](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/replaceAll)`

|  Replace all existing `[service perimeters](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` in an `[access policy](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)` with the `[service perimeters](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` provided.  
  
### `[testIamPermissions](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/testIamPermissions)`

|  Returns the IAM permissions that the caller has on the specified Access Context Manager resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
