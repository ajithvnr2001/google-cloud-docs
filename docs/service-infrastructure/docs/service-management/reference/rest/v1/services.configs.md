---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs
title: REST Resource: services.configs \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:27.773205+00:00
---

# REST Resource: services.configs  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.configs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Service
    * JSON representation
  * Api
    * JSON representation
  * Method
    * JSON representation
  * Option
    * JSON representation
  * Syntax
  * SourceContext
    * JSON representation
  * Mixin
    * JSON representation
  * Type
    * JSON representation
  * Field
    * JSON representation
  * Kind
  * Cardinality
  * Enum
    * JSON representation
  * EnumValue
    * JSON representation
  * Documentation
    * JSON representation
  * Page
    * JSON representation
  * DocumentationRule
    * JSON representation
  * Backend
    * JSON representation
  * BackendRule
    * JSON representation
  * PathTranslation
  * Http
    * JSON representation
  * HttpRule
    * JSON representation
  * CustomHttpPattern
    * JSON representation
  * Quota
    * JSON representation
  * QuotaLimit
    * JSON representation
  * MetricRule
    * JSON representation
  * Authentication
    * JSON representation
  * AuthenticationRule
    * JSON representation
  * OAuthRequirements
    * JSON representation
  * AuthRequirement
    * JSON representation
  * AuthProvider
    * JSON representation
  * JwtLocation
    * JSON representation
  * Context
    * JSON representation
  * ContextRule
    * JSON representation
  * Usage
    * JSON representation
  * UsageRule
    * JSON representation
  * CustomError
    * JSON representation
  * CustomErrorRule
    * JSON representation
  * Endpoint
    * JSON representation
  * Control
    * JSON representation
  * LogDescriptor
    * JSON representation
  * LabelDescriptor
    * JSON representation
  * ValueType
  * MetricDescriptor
    * JSON representation
  * MetricKind
  * ValueType
  * MetricDescriptorMetadata
    * JSON representation
  * LaunchStage
  * MonitoredResourceDescriptor
    * JSON representation
  * Billing
    * JSON representation
  * BillingDestination
    * JSON representation
  * Logging
    * JSON representation
  * LoggingDestination
    * JSON representation
  * Monitoring
    * JSON representation
  * MonitoringDestination
    * JSON representation
  * SystemParameters
    * JSON representation
  * SystemParameterRule
    * JSON representation
  * SystemParameter
    * JSON representation
  * SourceInfo
    * JSON representation
  * Methods



## Resource: Service

`Service` is the root object of Google API service configuration (service config). It describes the basic information about a logical service, such as the service name and the user-facing title, and delegates other aspects to sub-sections. Each sub-section is either a proto message or a repeated proto message that configures a specific aspect, such as auth. For more information, see each proto message definition.

Example:
    
    
    type: google.api.Service
    name: calendar.googleapis.com
    title: Google Calendar API
    apis:
    - name: google.calendar.v3.Calendar
    
    visibility:
      rules:
      - selector: "google.calendar.v3.*"
        restriction: PREVIEW
    backend:
      rules:
      - selector: "google.calendar.v3.*"
        address: calendar.example.com
    
    authentication:
      providers:
      - id: google_calendar_auth
        jwksUri: https://www.googleapis.com/oauth2/v1/certs
        issuer: https://securetoken.google.com
      rules:
      - selector: "*"
        requirements:
          providerId: google_calendar_auth
    

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "producerProjectId": string,
      "id": string,
      "apis": [
        {
          object ([Api](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api))
        }
      ],
      "types": [
        {
          object ([Type](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Type))
        }
      ],
      "enums": [
        {
          object ([Enum](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Enum))
        }
      ],
      "documentation": {
        object ([Documentation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Documentation))
      },
      "backend": {
        object ([Backend](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Backend))
      },
      "http": {
        object ([Http](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Http))
      },
      "quota": {
        object ([Quota](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Quota))
      },
      "authentication": {
        object ([Authentication](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Authentication))
      },
      "context": {
        object ([Context](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Context))
      },
      "usage": {
        object ([Usage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Usage))
      },
      "customError": {
        object ([CustomError](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#CustomError))
      },
      "endpoints": [
        {
          object ([Endpoint](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Endpoint))
        }
      ],
      "control": {
        object ([Control](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Control))
      },
      "logs": [
        {
          object ([LogDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LogDescriptor))
        }
      ],
      "metrics": [
        {
          object ([MetricDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricDescriptor))
        }
      ],
      "monitoredResources": [
        {
          object ([MonitoredResourceDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MonitoredResourceDescriptor))
        }
      ],
      "billing": {
        object ([Billing](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Billing))
      },
      "logging": {
        object ([Logging](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Logging))
      },
      "monitoring": {
        object ([Monitoring](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Monitoring))
      },
      "systemParameters": {
        object ([SystemParameters](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SystemParameters))
      },
      "sourceInfo": {
        object ([SourceInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SourceInfo))
      },
      "systemTypes": [
        {
          object ([Type](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Type))
        }
      ],
      "configVersion": integer
    }  
  
Fields  
---  
`name` |  `string` The service name, which is a DNS-like logical identifier for the service, such as `calendar.googleapis.com`. The service name typically goes through DNS verification to make sure the owner of the service also owns the DNS name.  
`title` |  `string` The product title for this service, it is the name displayed in Google Cloud Console.  
`producerProjectId` |  `string` The Google project that owns this service.  
`id` |  `string` A unique ID for a specific instance of this message, typically assigned by the client for tracking purpose. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If empty, the server may choose to generate one instead.  
`apis[]` |  `object (`[Api](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)`)` A list of API interfaces exported by this service. Only the `name` field of the `[google.protobuf.Api](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)` needs to be provided by the configuration author, as the remaining fields will be derived from the IDL during the normalization process. It is an error to specify an API interface here which cannot be resolved against the associated IDL files.  
`types[]` |  `object (`[Type](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Type)`)` A list of all proto message types included in this API service. Types referenced directly or indirectly by the `apis` are automatically included. Messages which are not referenced but shall be included, such as types used by the `google.protobuf.Any` type, should be listed here by name by the configuration author. Example:
    
    
    types:
    - name: google.protobuf.Int32
      
  
`enums[]` |  `object (`[Enum](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Enum)`)` A list of all enum types included in this API service. Enums referenced directly or indirectly by the `apis` are automatically included. Enums which are not referenced but shall be included should be listed here by name by the configuration author. Example:
    
    
    enums:
    - name: google.someapi.v1.SomeEnum
      
  
`documentation` |  `object (`[Documentation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Documentation)`)` Additional API documentation.  
`backend` |  `object (`[Backend](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Backend)`)` API backend configuration.  
`http` |  `object (`[Http](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Http)`)` HTTP configuration.  
`quota` |  `object (`[Quota](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Quota)`)` Quota configuration.  
`authentication` |  `object (`[Authentication](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Authentication)`)` Auth configuration.  
`context` |  `object (`[Context](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Context)`)` Context configuration.  
`usage` |  `object (`[Usage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Usage)`)` Configuration controlling usage of this service.  
`customError` |  `object (`[CustomError](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#CustomError)`)` Custom error configuration.  
`endpoints[]` |  `object (`[Endpoint](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Endpoint)`)` Configuration for network endpoints. If this is empty, then an endpoint with the same name as the service is automatically generated to service all defined APIs.  
`control` |  `object (`[Control](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Control)`)` Configuration for the service control plane.  
`logs[]` |  `object (`[LogDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LogDescriptor)`)` Defines the logs used by this service.  
`metrics[]` |  `object (`[MetricDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricDescriptor)`)` Defines the metrics used by this service.  
`monitoredResources[]` |  `object (`[MonitoredResourceDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MonitoredResourceDescriptor)`)` Defines the monitored resources used by this service. This is required by the `[Service.monitoring](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.monitoring)` and `[Service.logging](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.logging)` configurations.  
`billing` |  `object (`[Billing](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Billing)`)` Billing configuration.  
`logging` |  `object (`[Logging](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Logging)`)` Logging configuration.  
`monitoring` |  `object (`[Monitoring](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Monitoring)`)` Monitoring configuration.  
`systemParameters` |  `object (`[SystemParameters](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SystemParameters)`)` System parameter configuration.  
`sourceInfo` |  `object (`[SourceInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SourceInfo)`)` Output only. The source information for this configuration if available.  
`systemTypes[]` |  `object (`[Type](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Type)`)` A list of all proto message types included in this API service. It serves similar purpose as `[google.api.Service.types](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.types)`, except that these types are not needed by user-defined APIs. Therefore, they will not show up in the generated discovery doc. This field should only be used to define system APIs in ESF.  
`configVersion` |  `integer` Obsolete. Do not use.This field has no semantic meaning. The service config compiler always sets this field to `3`.  
  
## Api

Api is a light-weight descriptor for an API Interface.

Interfaces are also described as "protocol buffer services" in some contexts, such as by the "service" keyword in a .proto file, but they are different from API Services, which represent a concrete implementation of an interface as opposed to simply a description of methods and bindings. They are also sometimes simply referred to as "APIs" in other contexts, such as the name of this message itself. See <https://cloud.google.com/apis/design/glossary> for detailed terminology.

JSON representation  
---  
      
    
    {
      "name": string,
      "methods": [
        {
          object ([Method](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Method))
        }
      ],
      "options": [
        {
          object ([Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option))
        }
      ],
      "version": string,
      "sourceContext": {
        object ([SourceContext](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.SourceContext))
      },
      "mixins": [
        {
          object ([Mixin](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Mixin))
        }
      ],
      "syntax": enum ([Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax))
    }  
  
Fields  
---  
`name` |  `string` The fully qualified name of this interface, including package name followed by the interface's simple name.  
`methods[]` |  `object (`[Method](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Method)`)` The methods of this interface, in unspecified order.  
`options[]` |  `object (`[Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option)`)` Any metadata attached to the interface.  
`version` |  `string` A version string for this interface. If specified, must have the form `major-version.minor-version`, as in `1.10`. If the minor version is omitted, it defaults to zero. If the entire version field is empty, the major version is derived from the package name, as outlined below. If the field is not empty, the version in the package name will be verified to be consistent with what is provided here.The versioning schema uses [semantic versioning](http://semver.org) where the major version number indicates a breaking change and the minor version an additive, non-breaking change. Both version numbers are signals to users what to expect from different versions, and should be carefully chosen based on the product plan.The major version is also reflected in the package name of the interface, which must end in `v<major-version>`, as in `google.feature.v1`. For major versions 0 and 1, the suffix can be omitted. Zero major versions must only be used for experimental, non-GA interfaces.  
`sourceContext` |  `object (`[SourceContext](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.SourceContext)`)` Source context for the protocol buffer service represented by this message.  
`mixins[]` |  `object (`[Mixin](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Mixin)`)` Included interfaces. See `[Mixin](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Mixin)`.  
`syntax` |  `enum (`[Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax)`)` The source syntax of the service.  
  
## Method

method represents a method of an API interface.

JSON representation  
---  
      
    
    {
      "name": string,
      "requestTypeUrl": string,
      "requestStreaming": boolean,
      "responseTypeUrl": string,
      "responseStreaming": boolean,
      "options": [
        {
          object ([Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option))
        }
      ],
      "syntax": enum ([Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax))
    }  
  
Fields  
---  
`name` |  `string` The simple name of this method.  
`requestTypeUrl` |  `string` A URL of the input message type.  
`requestStreaming` |  `boolean` If true, the request is streamed.  
`responseTypeUrl` |  `string` The URL of the output message type.  
`responseStreaming` |  `boolean` If true, the response is streamed.  
`options[]` |  `object (`[Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option)`)` Any metadata attached to the method.  
`syntax` |  `enum (`[Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax)`)` The source syntax of this method.  
  
## Option

A protocol buffer option, which can be attached to a message, field, enumeration, etc.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": {
        "@type": string,
        field1: ...,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` The option's name. For protobuf built-in options (options defined in descriptor.proto), this is the short name. For example, `"mapEntry"`. For custom options, it should be the fully-qualified name. For example, `"google.api.http"`.  
`value` |  `object` The option's value packed in an Any message. If the value is a primitive, the corresponding wrapper type defined in google/protobuf/wrappers.proto should be used. If the value is an enum, it should be stored as an int32 value using the google.protobuf.Int32Value type.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Syntax

The syntax in which a protocol buffer element is defined.

Enums  
---  
`SYNTAX_PROTO2` | Syntax `proto2`.  
`SYNTAX_PROTO3` | Syntax `proto3`.  
  
## SourceContext

`SourceContext` represents information about the source of a protobuf element, like the file in which it is defined.

JSON representation  
---  
      
    
    {
      "fileName": string
    }  
  
Fields  
---  
`fileName` |  `string` The path-qualified name of the .proto file that contained the associated protobuf element. For example: `"google/protobuf/sourceContext.proto"`.  
  
## Mixin

Declares an API Interface to be included in this interface. The including interface must redeclare all the methods from the included interface, but documentation and options are inherited as follows:

  * If after comment and whitespace stripping, the documentation string of the redeclared method is empty, it will be inherited from the original method.

  * Each annotation belonging to the service config (http, visibility) which is not set in the redeclared method will be inherited.

  * If an http annotation is inherited, the path pattern will be modified as follows. Any version prefix will be replaced by the version of the including interface plus the `[root](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Mixin)` path if specified.




Example of a simple mixin:
    
    
    package google.acl.v1;
    service AccessControl {
      // Get the underlying ACL object.
      rpc GetAcl(GetAclRequest) returns (Acl) {
        option (google.api.http).get = "/v1/{resource=**}:getAcl";
      }
    }
    
    package google.storage.v2;
    service Storage {
      //       rpc GetAcl(GetAclRequest) returns (Acl);
    
      // Get a data record.
      rpc GetData(GetDataRequest) returns (Data) {
        option (google.api.http).get = "/v2/{resource=**}";
      }
    }
    

Example of a mixin configuration:
    
    
    apis:
    - name: google.storage.v2.Storage
      mixins:
      - name: google.acl.v1.AccessControl
    

The mixin construct implies that all methods in `AccessControl` are also declared with same name and request/response types in `Storage`. A documentation generator or annotation processor will see the effective `Storage.GetAcl` method after inheriting documentation and annotations as follows:
    
    
    service Storage {
      // Get the underlying ACL object.
      rpc GetAcl(GetAclRequest) returns (Acl) {
        option (google.api.http).get = "/v2/{resource=**}:getAcl";
      }
      ...
    }
    

Note how the version in the path pattern changed from `v1` to `v2`.

If the `root` field in the mixin is specified, it should be a relative path under which inherited HTTP paths are placed. Example:
    
    
    apis:
    - name: google.storage.v2.Storage
      mixins:
      - name: google.acl.v1.AccessControl
        root: acls
    

This implies the following inherited HTTP annotation:
    
    
    service Storage {
      // Get the underlying ACL object.
      rpc GetAcl(GetAclRequest) returns (Acl) {
        option (google.api.http).get = "/v2/acls/{resource=**}:getAcl";
      }
      ...
    }
    

JSON representation  
---  
      
    
    {
      "name": string,
      "root": string
    }  
  
Fields  
---  
`name` |  `string` The fully qualified name of the interface which is included.  
`root` |  `string` If non-empty specifies a path under which inherited HTTP paths are rooted.  
  
## Type

A protocol buffer message type.

JSON representation  
---  
      
    
    {
      "name": string,
      "fields": [
        {
          object ([Field](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Field))
        }
      ],
      "oneofs": [
        string
      ],
      "options": [
        {
          object ([Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option))
        }
      ],
      "sourceContext": {
        object ([SourceContext](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.SourceContext))
      },
      "syntax": enum ([Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax))
    }  
  
Fields  
---  
`name` |  `string` The fully qualified message name.  
`fields[]` |  `object (`[Field](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Field)`)` The list of fields.  
`oneofs[]` |  `string` The list of types appearing in `oneof` definitions in this type.  
`options[]` |  `object (`[Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option)`)` The protocol buffer options.  
`sourceContext` |  `object (`[SourceContext](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.SourceContext)`)` The source context.  
`syntax` |  `enum (`[Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax)`)` The source syntax.  
  
## Field

A single field of a message type.

JSON representation  
---  
      
    
    {
      "kind": enum ([Kind](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Field)),
      "cardinality": enum ([Cardinality](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Field)),
      "number": integer,
      "name": string,
      "typeUrl": string,
      "oneofIndex": integer,
      "packed": boolean,
      "options": [
        {
          object ([Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option))
        }
      ],
      "jsonName": string,
      "defaultValue": string
    }  
  
Fields  
---  
`kind` |  `enum (`[Kind](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Field)`)` The field type.  
`cardinality` |  `enum (`[Cardinality](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Field)`)` The field cardinality.  
`number` |  `integer` The field number.  
`name` |  `string` The field name.  
`typeUrl` |  `string` The field type URL, without the scheme, for message or enumeration types. Example: `"type.googleapis.com/google.protobuf.Timestamp"`.  
`oneofIndex` |  `integer` The index of the field type in `type.oneofs`, for message or enumeration types. The first type has index 1; zero means the type is not in the list.  
`packed` |  `boolean` Whether to use alternative packed wire representation.  
`options[]` |  `object (`[Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option)`)` The protocol buffer options.  
`jsonName` |  `string` The field JSON name.  
`defaultValue` |  `string` The string value of the default value of this field. Proto2 syntax only.  
  
## Kind

Basic field types.

Enums  
---  
`TYPE_UNKNOWN` | Field type unknown.  
`TYPE_DOUBLE` | Field type double.  
`TYPE_FLOAT` | Field type float.  
`TYPE_INT64` | Field type int64.  
`TYPE_UINT64` | Field type uint64.  
`TYPE_INT32` | Field type int32.  
`TYPE_FIXED64` | Field type fixed64.  
`TYPE_FIXED32` | Field type fixed32.  
`TYPE_BOOL` | Field type bool.  
`TYPE_STRING` | Field type string.  
`TYPE_GROUP` | Field type group. Proto2 syntax only, and deprecated.  
`TYPE_MESSAGE` | Field type message.  
`TYPE_BYTES` | Field type bytes.  
`TYPE_UINT32` | Field type uint32.  
`TYPE_ENUM` | Field type enum.  
`TYPE_SFIXED32` | Field type sfixed32.  
`TYPE_SFIXED64` | Field type sfixed64.  
`TYPE_SINT32` | Field type sint32.  
`TYPE_SINT64` | Field type sint64.  
  
## Cardinality

Whether a field is optional, required, or repeated.

Enums  
---  
`CARDINALITY_UNKNOWN` | For fields with unknown cardinality.  
`CARDINALITY_OPTIONAL` | For optional fields.  
`CARDINALITY_REQUIRED` | For required fields. Proto2 syntax only.  
`CARDINALITY_REPEATED` | For repeated fields.  
  
## Enum

Enum type definition.

JSON representation  
---  
      
    
    {
      "name": string,
      "enumvalue": [
        {
          object ([EnumValue](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.EnumValue))
        }
      ],
      "options": [
        {
          object ([Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option))
        }
      ],
      "sourceContext": {
        object ([SourceContext](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.SourceContext))
      },
      "syntax": enum ([Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax))
    }  
  
Fields  
---  
`name` |  `string` Enum type name.  
`enumvalue[]` |  `object (`[EnumValue](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.EnumValue)`)` Enum value definitions.  
`options[]` |  `object (`[Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option)`)` Protocol buffer options.  
`sourceContext` |  `object (`[SourceContext](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.SourceContext)`)` The source context.  
`syntax` |  `enum (`[Syntax](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Syntax)`)` The source syntax.  
  
## EnumValue

Enum value definition.

JSON representation  
---  
      
    
    {
      "name": string,
      "number": integer,
      "options": [
        {
          object ([Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Enum value name.  
`number` |  `integer` Enum value number.  
`options[]` |  `object (`[Option](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Option)`)` Protocol buffer options.  
  
## Documentation

`Documentation` provides the information for describing a service.

Example:
    
    
    documentation:
      summary: >
        The Google Calendar API gives access
        to most calendar features.
      pages:
      - name: Overview
        content: (== include google/foo/overview.md ==)
      - name: Tutorial
        content: (== include google/foo/tutorial.md ==)
        subpages;
        - name: Java
          content: (== include google/foo/tutorial_java.md ==)
      rules:
      - selector: google.calendar.Calendar.Get
        description: >
          ...
      - selector: google.calendar.Calendar.Put
        description: >
          ...
    

Documentation is provided in markdown syntax. In addition to standard markdown features, definition lists, tables and fenced code blocks are supported. Section headers can be provided and are interpreted relative to the section nesting of the context where a documentation fragment is embedded.

Documentation from the IDL is merged with documentation defined via the config at normalization time, where documentation provided by config rules overrides IDL provided.

A number of constructs specific to the API platform are supported in documentation text.

In order to reference a proto element, the following notation can be used:
    
    
    [fully.qualified.proto.name][]

To override the display text used for the link, this can be used:
    
    
    [display text][fully.qualified.proto.name]

Text can be excluded from doc using the following notation:
    
    
    (-- internal comment --)

A few directives are available in documentation. Note that directives must appear on a single line to be properly identified. The `include` directive includes a markdown file from an external source:
    
    
    (== include path/to/file ==)

The `resource_for` directive marks a message to be the resource of a collection in REST view. If it is not specified, tools attempt to infer the resource from the operations in a collection:
    
    
    (== resource_for v1.shelves.books ==)

The directive `suppress_warning` does not directly affect documentation and is documented together with service config validation.

JSON representation  
---  
      
    
    {
      "summary": string,
      "pages": [
        {
          object ([Page](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Page))
        }
      ],
      "rules": [
        {
          object ([DocumentationRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule))
        }
      ],
      "documentationRootUrl": string,
      "serviceRootUrl": string,
      "overview": string
    }  
  
Fields  
---  
`summary` |  `string` A short description of what the service does. The summary must be plain text. It becomes the overview of the service displayed in Google Cloud Console. NOTE: This field is equivalent to the standard field `description`.  
`pages[]` |  `object (`[Page](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Page)`)` The top level pages for the documentation set.  
`rules[]` |  `object (`[DocumentationRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule)`)` A list of documentation rules that apply to individual API elements.**NOTE:** All service configuration rules follow "last one wins" order.  
`documentationRootUrl` |  `string` The URL to the root of documentation.  
`serviceRootUrl` |  `string` Specifies the service root url if the default one (the service name from the yaml file) is not suitable. This can be seen in any fully specified service urls as well as sections that show a base that other urls are relative to.  
`overview` |  `string` Declares a single overview page. For example:
    
    
    documentation:
      summary: ...
      overview: (== include overview.md ==)
    

This is a shortcut for the following declaration (using pages style):
    
    
    documentation:
      summary: ...
      pages:
      - name: Overview
        content: (== include overview.md ==)
    

Note: you cannot specify both `overview` field and `pages` field.  
  
## Page

Represents a documentation page. A page can contain subpages to represent nested documentation set structure.

JSON representation  
---  
      
    
    {
      "name": string,
      "content": string,
      "subpages": [
        {
          object ([Page](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Page))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The name of the page. It will be used as an identity of the page to generate URI of the page, text of the link to this page in navigation, etc. The full page name (start from the root page name to this page concatenated with `.`) can be used as reference to the page in your documentation. For example:
    
    
    pages:
    - name: Tutorial
      content: (== include tutorial.md ==)
      subpages:
      - name: Java
        content: (== include tutorial_java.md ==)
    

You can reference `Java` page using Markdown reference link syntax: `[Java][Tutorial.Java]`.  
`content` |  `string` The Markdown content of the page. You can use  `(== include {path} ==)` to include content from a Markdown file. The content can be used to produce the documentation page such as HTML format page.  
`subpages[]` |  `object (`[Page](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Page)`)` Subpages of this page. The order of subpages specified here will be honored in the generated docset.  
  
## DocumentationRule

A documentation rule provides information about individual API elements.

JSON representation  
---  
      
    
    {
      "selector": string,
      "description": string,
      "deprecationDescription": string
    }  
  
Fields  
---  
`selector` |  `string` The selector is a comma-separated list of patterns for any element such as a method, a field, an enum value. Each pattern is a qualified name of the element which may end in "*", indicating a wildcard. Wildcards are only allowed at the end and for a whole component of the qualified name, i.e. "foo.*" is ok, but not "foo.b*" or "foo.*.bar". A wildcard will match one or more components. To specify a default for all applicable elements, the whole pattern "*" is used.  
`description` |  `string` description of the selected proto element (e.g. a message, a method, a 'service' definition, or a field). Defaults to leading & trailing comments taken from the proto source definition of the proto element.  
`deprecationDescription` |  `string` Deprecation description of the selected element(s). It can be provided if an element is marked as `deprecated`.  
  
## Backend

`Backend` defines the backend configuration for a service.

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([BackendRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#BackendRule))
        }
      ]
    }  
  
Fields  
---  
`rules[]` |  `object (`[BackendRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#BackendRule)`)` A list of API backend rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
  
## BackendRule

A backend rule provides configuration for an individual API element.

JSON representation  
---  
      
    
    {
      "selector": string,
      "address": string,
      "deadline": number,
      "operationDeadline": number,
      "pathTranslation": enum ([PathTranslation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#PathTranslation)),
      "protocol": string,
    
      // Union field authentication can be only one of the following:
      "jwtAudience": string,
      "disableAuth": boolean
      // End of list of possible types for union field authentication.
    }  
  
Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`address` |  `string` The address of the API backend.The scheme is used to determine the backend protocol and security. The following schemes are accepted:SCHEME PROTOCOL SECURITY http:// HTTP None https:// HTTP TLS grpc:// gRPC None grpcs:// gRPC TLSIt is recommended to explicitly include a scheme. Leaving out the scheme may cause constrasting behaviors across platforms.If the port is unspecified, the default is: - 80 for schemes without TLS - 443 for schemes with TLSFor HTTP backends, use `[protocol](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#BackendRule.FIELDS.protocol)` to specify the protocol version.  
`deadline` |  `number` The number of seconds to wait for a response from a request. The default varies based on the request protocol and deployment environment.  
`operationDeadline` |  `number` The number of seconds to wait for the completion of a long running operation. The default is no deadline.  
`pathTranslation` |  `enum (`[PathTranslation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#PathTranslation)`)`  
`protocol` |  `string` The protocol used for sending a request to the backend. The supported values are "http/1.1" and "h2".The default value is inferred from the scheme in the `[address](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#BackendRule.FIELDS.address)` field:SCHEME PROTOCOL http:// http/1.1 https:// http/1.1 grpc:// h2 grpcs:// h2For secure HTTP backends (https://) that support HTTP/2, set this field to "h2" for improved performance.Configuring this field to non-default values is only supported for secure HTTP backends. This field will be ignored for all other backends.See <https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids> for more details on the supported values.  
Union field `authentication`. Authentication settings used by the backend.These are typically used to provide service management functionality to a backend served on a publicly-routable URL. The `authentication` details should match the authentication behavior used by the backend.For example, specifying `jwt_audience` implies that the backend expects authentication via a JWT.When authentication is unspecified, the resulting behavior is the same as `disable_auth` set to `true`.Refer to <https://developers.google.com/identity/protocols/OpenIDConnect> for JWT ID token. `authentication` can be only one of the following:  
`jwtAudience` |  `string` The JWT audience is used when generating a JWT ID token for the backend. This ID token will be added in the HTTP "authorization" header, and sent to the backend.  
`disableAuth` |  `boolean` When disableAuth is true, a JWT ID token won't be generated and the original "Authorization" HTTP header will be preserved. If the header is used to carry the original token and is expected by the backend, this field must be set to true to preserve the header.  
  
## PathTranslation

Path Translation specifies how to combine the backend address with the request path in order to produce the appropriate forwarding URL for the request.

Path Translation is applicable only to HTTP-based backends. Backends which do not accept requests over HTTP/HTTPS should leave `pathTranslation` unspecified.

Enums  
---  
`PATH_TRANSLATION_UNSPECIFIED` |   
`CONSTANT_ADDRESS` | Use the backend address as-is, with no modification to the path. If the URL pattern contains variables, the variable names and values will be appended to the query string. If a query string parameter and a URL pattern variable have the same name, this may result in duplicate keys in the query string.Given the following operation config:
    
    
    method path:        /api/company/{cid}/user/{uid}
    Backend address:    https://example.cloudfunctions.net/getUser
    

Requests to the following request paths will call the backend at the translated path:
    
    
    Request path: /api/company/widgetworks/user/johndoe
    Translated:
    https://example.cloudfunctions.net/getUser?cid=widgetworks&uid=johndoe
    
    Request path: /api/company/widgetworks/user/johndoe?timezone=EST
    Translated:
    https://example.cloudfunctions.net/getUser?timezone=EST&cid=widgetworks&uid=johndoe
      
  
`APPEND_PATH_TO_ADDRESS` | The request path will be appended to the backend address.Given the following operation config:
    
    
    method path:        /api/company/{cid}/user/{uid}
    Backend address:    https://example.appspot.com
    

Requests to the following request paths will call the backend at the translated path:
    
    
    Request path: /api/company/widgetworks/user/johndoe
    Translated:
    https://example.appspot.com/api/company/widgetworks/user/johndoe
    
    Request path: /api/company/widgetworks/user/johndoe?timezone=EST
    Translated:
    https://example.appspot.com/api/company/widgetworks/user/johndoe?timezone=EST
      
  
## Http

Defines the HTTP configuration for an API service. It contains a list of `[HttpRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule)`, each specifying the mapping of an RPC method to one or more HTTP REST API methods.

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([HttpRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule))
        }
      ],
      "fullyDecodeReservedExpansion": boolean
    }  
  
Fields  
---  
`rules[]` |  `object (`[HttpRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule)`)` A list of HTTP configuration rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
`fullyDecodeReservedExpansion` |  `boolean` When set to true, URL path parameters will be fully URI-decoded except in cases of single segment matches in reserved expansion, where "%2F" will be left encoded.The default behavior is to not decode RFC 6570 reserved characters in multi segment matches.  
  
## HttpRule

#### gRPC Transcoding

gRPC Transcoding is a feature for mapping between a gRPC method and one or more HTTP REST endpoints. It allows developers to build a single API service that supports both gRPC APIs and REST APIs. Many systems, including [Google APIs](https://github.com/googleapis/googleapis), [Cloud Endpoints](https://cloud.google.com/endpoints), [gRPC Gateway](https://github.com/grpc-ecosystem/grpc-gateway), and [Envoy](https://github.com/envoyproxy/envoy) proxy support this feature and use it for large scale production services.

`HttpRule` defines the schema of the gRPC/REST mapping. The mapping specifies how different portions of the gRPC request message are mapped to the URL path, URL query parameters, and HTTP request body. It also controls how the gRPC response message is mapped to the HTTP response body. `HttpRule` is typically specified as an `google.api.http` annotation on the gRPC method.

Each mapping specifies a URL path template and an HTTP method. The path template may refer to one or more fields in the gRPC request message, as long as each field is a non-repeated field with a primitive (non-message) type. The path template controls how fields of the request message are mapped to the URL path.

Example:
    
    
    service Messaging {
      rpc GetMessage(GetMessageRequest) returns (Message) {
        option (google.api.http) = {
            get: "/v1/{name=messages/*}"
        };
      }
    }
    message GetMessageRequest {
      string name = 1; // Mapped to URL path.
    }
    message Message {
      string text = 1; // The resource content.
    }
    

This enables an HTTP REST to gRPC mapping as below:

HTTP  | gRPC  
---|---  
`GET /v1/messages/123456` | `GetMessage(name: "messages/123456")`  
  
Any fields in the request message which are not bound by the path template automatically become HTTP query parameters if there is no HTTP request body. For example:
    
    
    service Messaging {
      rpc GetMessage(GetMessageRequest) returns (Message) {
        option (google.api.http) = {
            get:"/v1/messages/{message_id}"
        };
      }
    }
    message GetMessageRequest {
      message SubMessage {
        string subfield = 1;
      }
      string message_id = 1; // Mapped to URL path.
      int64 revision = 2;    // Mapped to URL query parameter `revision`.
      SubMessage sub = 3;    // Mapped to URL query parameter `sub.subfield`.
    }
    

This enables a HTTP JSON to RPC mapping as below:

HTTP  | gRPC  
---|---  
`GET /v1/messages/123456?revision=2&sub.subfield=foo`  
  
`GetMessage(message_id: "123456" revision: 2 sub: SubMessage(subfield: "foo"))`

Note that fields which are mapped to URL query parameters must have a primitive type or a repeated primitive type or a non-repeated message type. In the case of a repeated type, the parameter can be repeated in the URL as `...?param=A&param=B`. In the case of a message type, each field of the message is mapped to a separate parameter, such as `...?foo.a=A&foo.b=B&foo.c=C`.

For HTTP methods that allow a request body, the `body` field specifies the mapping. Consider a REST update method on the message resource collection:
    
    
    service Messaging {
      rpc UpdateMessage(UpdateMessageRequest) returns (Message) {
        option (google.api.http) = {
          patch: "/v1/messages/{message_id}"
          body: "message"
        };
      }
    }
    message UpdateMessageRequest {
      string message_id = 1; // mapped to the URL
      Message message = 2;   // mapped to the body
    }
    

The following HTTP JSON to RPC mapping is enabled, where the representation of the JSON in the request body is determined by protos JSON encoding:

HTTP  | gRPC  
---|---  
`PATCH /v1/messages/123456 { "text": "Hi!" }` | `UpdateMessage(message_id: "123456" message { text: "Hi!" })`  
  
The special name `*` can be used in the body mapping to define that every field not bound by the path template should be mapped to the request body. This enables the following alternative definition of the update method:
    
    
    service Messaging {
      rpc UpdateMessage(Message) returns (Message) {
        option (google.api.http) = {
          patch: "/v1/messages/{message_id}"
          body: "*"
        };
      }
    }
    message Message {
      string message_id = 1;
      string text = 2;
    }
    

The following HTTP JSON to RPC mapping is enabled:

HTTP  | gRPC  
---|---  
`PATCH /v1/messages/123456 { "text": "Hi!" }` | `UpdateMessage(message_id: "123456" text: "Hi!")`  
  
Note that when using `*` in the body mapping, it is not possible to have HTTP parameters, as all fields not bound by the path end in the body. This makes this option more rarely used in practice when defining REST APIs. The common usage of `*` is in custom methods which don't use the URL at all for transferring data.

It is possible to define multiple HTTP methods for one RPC by using the `additionalBindings` option. Example:
    
    
    service Messaging {
      rpc GetMessage(GetMessageRequest) returns (Message) {
        option (google.api.http) = {
          get: "/v1/messages/{message_id}"
          additionalBindings {
            get: "/v1/users/{userId}/messages/{message_id}"
          }
        };
      }
    }
    message GetMessageRequest {
      string message_id = 1;
      string userId = 2;
    }
    

This enables the following two alternative HTTP JSON to RPC mappings:

HTTP  | gRPC  
---|---  
`GET /v1/messages/123456` | `GetMessage(message_id: "123456")`  
`GET /v1/users/me/messages/123456` | `GetMessage(userId: "me" message_id: "123456")`  
  
##### Rules for HTTP mapping

  1. Leaf request fields (recursive expansion nested messages in the request message) are classified into three categories:


  * Fields referred by the path template. They are passed via the URL path.
  * Fields referred by the `[HttpRule.body](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule.FIELDS.body)`. They are passed via the HTTP request body.
  * All other fields are passed via the URL query parameters, and the parameter name is the field path in the request message. A repeated field can be represented as multiple query parameters under the same name.


  1. If `[HttpRule.body](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule.FIELDS.body)` is "*", there is no URL query parameter, all fields are passed via URL path and HTTP request body.
  2. If `[HttpRule.body](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule.FIELDS.body)` is omitted, there is no HTTP request body, all fields are passed via URL path and URL query parameters.



###### Path template syntax
    
    
    Template = "/" Segments [ Verb ] ;
    Segments = Segment { "/" Segment } ;
    Segment  = "*" | "**" | LITERAL | Variable ;
    Variable = "{" FieldPath [ "=" Segments ] "}" ;
    FieldPath = IDENT { "." IDENT } ;
    Verb     = ":" LITERAL ;
    

The syntax `*` matches a single URL path segment. The syntax `**` matches zero or more URL path segments, which must be the last part of the URL path except the `Verb`.

The syntax `Variable` matches part of the URL path as specified by its template. A variable template must not contain other variables. If a variable matches a single path segment, its template may be omitted, e.g. `{var}` is equivalent to `{var=*}`.

The syntax `LITERAL` matches literal text in the URL path. If the `LITERAL` contains any reserved character, such characters should be percent-encoded before the matching.

If a variable contains exactly one path segment, such as `"{var}"` or `"{var=*}"`, when such a variable is expanded into a URL path on the client side, all characters except `[-_.~0-9a-zA-Z]` are percent-encoded. The server side does the reverse decoding. Such variables show up in the [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) as `{var}`.

If a variable contains multiple path segments, such as `"{var=foo/*}"` or `"{var=**}"`, when such a variable is expanded into a URL path on the client side, all characters except `[-_.~/0-9a-zA-Z]` are percent-encoded. The server side does the reverse decoding, except "%2F" and "%2f" are left unchanged. Such variables show up in the [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) as `{+var}`.

##### Using gRPC API Service Configuration

gRPC API Service Configuration (service config) is a configuration language for configuring a gRPC service to become a user-facing product. The service config is simply the YAML representation of the `google.api.Service` proto message.

As an alternative to annotating your proto file, you can configure gRPC transcoding in your service config YAML files. You do this by specifying a `HttpRule` that maps the gRPC method to a REST endpoint, achieving the same effect as the proto annotation. This can be particularly useful if you have a proto that is reused in multiple services. Note that any transcoding specified in the service config will override any matching transcoding configuration in the proto.

Example:
    
    
    http:
      rules:
        # Selects a gRPC method and applies HttpRule to it.
        - selector: example.v1.Messaging.GetMessage
          get: /v1/messages/{message_id}/{sub.subfield}
    

##### Special notes

When gRPC Transcoding is used to map a gRPC to JSON REST endpoints, the proto to JSON conversion must follow the [proto3 specification](https://developers.google.com/protocol-buffers/docs/proto3#json).

While the single segment variable follows the semantics of [RFC 6570](https://tools.ietf.org/html/rfc6570) Section 3.2.2 Simple String Expansion, the multi segment variable **does not** follow RFC 6570 Section 3.2.3 reserved Expansion. The reason is that the reserved Expansion does not expand special characters like `?` and `#`, which would lead to invalid URLs. As the result, gRPC Transcoding uses a custom encoding for multi segment variables.

The path variables **must not** refer to any repeated or mapped field, because client libraries are not capable of handling such variable expansion.

The path variables **must not** capture the leading "/" character. The reason is that the most common use case "{var}" does not capture the leading "/" character. For consistency, all path variables must share the same behavior.

Repeated message fields must not be mapped to URL query parameters, because no client library can support such complicated mapping.

If an API needs to use a JSON array for request or response body, it can map the request or response body to a repeated field. However, some gRPC Transcoding implementations may not support this feature.

JSON representation  
---  
      
    
    {
      "selector": string,
      "body": string,
      "responseBody": string,
      "additionalBindings": [
        {
          object ([HttpRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule))
        }
      ],
    
      // Union field pattern can be only one of the following:
      "get": string,
      "put": string,
      "post": string,
      "delete": string,
      "patch": string,
      "custom": {
        object ([CustomHttpPattern](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#CustomHttpPattern))
      }
      // End of list of possible types for union field pattern.
    }  
  
Fields  
---  
`selector` |  `string` Selects a method to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`body` |  `string` The name of the request field whose value is mapped to the HTTP request body, or `*` for mapping all request fields not captured by the path pattern to the HTTP body, or omitted for not having any HTTP request body.NOTE: the referred field must be present at the top-level of the request message type.  
`responseBody` |  `string` Optional. The name of the response field whose value is mapped to the HTTP response body. When omitted, the entire response message will be used as the HTTP response body.NOTE: The referred field must be present at the top-level of the response message type.  
`additionalBindings[]` |  `object (`[HttpRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#HttpRule)`)` Additional HTTP bindings for the selector. Nested bindings must not contain an `additionalBindings` field themselves (that is, the nesting may only be one level deep).  
Union field `pattern`. Determines the URL pattern is matched by this rules. This pattern can be used with any of the {get|put|post|delete|patch} methods. A custom method can be defined using the 'custom' field. `pattern` can be only one of the following:  
`get` |  `string` Maps to HTTP GET. Used for listing and getting information about resources.  
`put` |  `string` Maps to HTTP PUT. Used for replacing a resource.  
`post` |  `string` Maps to HTTP POST. Used for creating a resource or performing an action.  
`delete` |  `string` Maps to HTTP DELETE. Used for deleting a resource.  
`patch` |  `string` Maps to HTTP PATCH. Used for updating a resource.  
`custom` |  `object (`[CustomHttpPattern](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#CustomHttpPattern)`)` The custom pattern is used for specifying an HTTP method that is not included in the `pattern` field, such as HEAD, or "*" to leave the HTTP method unspecified for this rule. The wild-card rule is useful for services that provide content to Web (HTML) clients.  
  
## CustomHttpPattern

A custom pattern is used for defining custom HTTP verb.

JSON representation  
---  
      
    
    {
      "kind": string,
      "path": string
    }  
  
Fields  
---  
`kind` |  `string` The name of this custom HTTP verb.  
`path` |  `string` The path matched by this custom verb.  
  
## Quota

Quota configuration helps to achieve fairness and budgeting in service usage.

The metric based quota configuration works this way: - The service configuration defines a set of metrics. - For API calls, the quota.metric_rules maps methods to metrics with corresponding costs. - The quota.limits defines limits on the metrics, which will be used for quota checks at runtime.

An example quota configuration in yaml format:

quota: limits:
    
    
     - name: apiWriteQpsPerProject
       metric: library.googleapis.com/write_calls
       unit: "1/min/{project}"  # rate limit for consumer projects
       values:
         STANDARD: 10000
    
    
     # The metric rules bind all methods to the read_calls metric,
     # except for the UpdateBook and DeleteBook methods. These two methods
     # are mapped to the write_calls metric, with the UpdateBook method
     # consuming at twice rate as the DeleteBook method.
     metricRules:
     - selector: "*"
       metricCosts:
         library.googleapis.com/read_calls: 1
     - selector: google.example.library.v1.LibraryService.UpdateBook
       metricCosts:
         library.googleapis.com/write_calls: 2
     - selector: google.example.library.v1.LibraryService.DeleteBook
       metricCosts:
         library.googleapis.com/write_calls: 1
    

Corresponding Metric definition:
    
    
     metrics:
     - name: library.googleapis.com/read_calls
       displayName: Read requests
       metricKind: DELTA
       valueType: INT64
    
     - name: library.googleapis.com/write_calls
       displayName: Write requests
       metricKind: DELTA
       valueType: INT64
    

JSON representation  
---  
      
    
    {
      "limits": [
        {
          object ([QuotaLimit](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#QuotaLimit))
        }
      ],
      "metricRules": [
        {
          object ([MetricRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricRule))
        }
      ]
    }  
  
Fields  
---  
`limits[]` |  `object (`[QuotaLimit](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#QuotaLimit)`)` List of `QuotaLimit` definitions for the service.  
`metricRules[]` |  `object (`[MetricRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricRule)`)` List of `MetricRule` definitions, each one mapping a selected method to one or more metrics.  
  
## QuotaLimit

`QuotaLimit` defines a specific limit that applies over a specified duration for a limit type. There can be at most one limit for a duration and limit type combination defined within a `QuotaGroup`.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "defaultLimit": string,
      "maxLimit": string,
      "freeTier": string,
      "duration": string,
      "metric": string,
      "unit": string,
      "values": {
        string: string,
        ...
      },
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` name of the quota limit.The name must be provided, and it must be unique within the service. The name can only include alphanumeric characters as well as '-'.The maximum length of the limit name is 64 characters.  
`description` |  `string` Optional. User-visible, extended description for this quota limit. Should be used only when more context is needed to understand this limit than provided by the limit's display name (see: `displayName`).  
`defaultLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Default number of tokens that can be consumed during the specified duration. This is the number of tokens assigned when a client application developer activates the service for his/her project.Specifying a value of 0 will block all requests. This can be used if you are provisioning quota to selected consumers and blocking others. Similarly, a value of -1 will indicate an unlimited quota. No other negative values are allowed.Used by group-based quotas only.  
`maxLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Maximum number of tokens that can be consumed during the specified duration. Client application developers can override the default limit up to this maximum. If specified, this value cannot be set to a value less than the default limit. If not specified, it is set to the default limit.To allow clients to apply overrides with no upper bound, set this to -1, indicating unlimited maximum quota.Used by group-based quotas only.  
`freeTier` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Free tier value displayed in the Developers Console for this limit. The free tier is the number of tokens that will be subtracted from the billed amount when billing is enabled. This field can only be set on a limit with duration "1d", in a billable group; it is invalid on any other limit. If this field is not set, it defaults to 0, indicating that there is no free tier for this service.Used by group-based quotas only.  
`duration` |  `string` Duration of this limit in textual notation. Must be "100s" or "1d".Used by group-based quotas only.  
`metric` |  `string` The name of the metric this quota limit applies to. The quota limits with the same metric will be checked together during runtime. The metric must be defined within the service config.  
`unit` |  `string` Specify the unit of the quota limit. It uses the same syntax as [Metric.unit][]. The supported unit kinds are determined by the quota backend system.Here are some examples: * "1/min/{project}" for quota per minute per project.Note: the order of unit components is insignificant. The "1" at the beginning is required to follow the metric unit syntax.  
`values` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` Tiered limit values. You must specify this as a key:value pair, with an integer value that is the maximum number of requests allowed for the specified unit. Currently only STANDARD is supported.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` User-visible display name for this limit. Optional. If not set, the UI will provide a default display name based on the quota configuration. This field can be used to override the default display name generated from the configuration.  
  
## MetricRule

Bind API methods to metrics. Binding a method to a metric causes that metric's configured quota behaviors to apply to the method call.

JSON representation  
---  
      
    
    {
      "selector": string,
      "metricCosts": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`metricCosts` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` Metrics to update when the selected methods are called, and the associated cost applied to each metric.The key of the map is the metric name, and the values are the amount increased for the metric against which the quota limits are defined. The value must not be negative.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Authentication

`Authentication` defines the authentication configuration for API methods provided by an API service.

Example:
    
    
    name: calendar.googleapis.com
    authentication:
      providers:
      - id: google_calendar_auth
        jwksUri: https://www.googleapis.com/oauth2/v1/certs
        issuer: https://securetoken.google.com
      rules:
      - selector: "*"
        requirements:
          providerId: google_calendar_auth
      - selector: google.calendar.Delegate
        oauth:
          canonicalScopes: https://www.googleapis.com/auth/calendar.read
    

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([AuthenticationRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#AuthenticationRule))
        }
      ],
      "providers": [
        {
          object ([AuthProvider](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#AuthProvider))
        }
      ]
    }  
  
Fields  
---  
`rules[]` |  `object (`[AuthenticationRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#AuthenticationRule)`)` A list of authentication rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
`providers[]` |  `object (`[AuthProvider](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#AuthProvider)`)` Defines a set of authentication providers that a service supports.  
  
## AuthenticationRule

Authentication rules for the service.

By default, if a method has any authentication requirements, every request must include a valid credential matching one of the requirements. It's an error to include more than one kind of credential in a single request.

If a method doesn't have any auth requirements, request credentials will be ignored.

JSON representation  
---  
      
    
    {
      "selector": string,
      "oauth": {
        object ([OAuthRequirements](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#OAuthRequirements))
      },
      "allowWithoutCredential": boolean,
      "requirements": [
        {
          object ([AuthRequirement](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#AuthRequirement))
        }
      ]
    }  
  
Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`oauth` |  `object (`[OAuthRequirements](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#OAuthRequirements)`)` The requirements for OAuth credentials.  
`allowWithoutCredential` |  `boolean` If true, the service accepts API keys without any other credential. This flag only applies to HTTP and gRPC requests.  
`requirements[]` |  `object (`[AuthRequirement](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#AuthRequirement)`)` Requirements for additional authentication providers.  
  
## OAuthRequirements

OAuth scopes are a way to define data and permissions on data. For example, there are scopes defined for "Read-only access to Google Calendar" and "Access to Cloud Platform". Users can consent to a scope for an application, giving it permission to access that data on their behalf.

OAuth scope specifications should be fairly coarse grained; a user will need to see and understand the text description of what your scope means.

In most cases: use one or at most two OAuth scopes for an entire family of products. If your product has multiple APIs, you should probably be sharing the OAuth scope across all of those APIs.

When you need finer grained OAuth consent screens: talk with your product management about how developers will use them in practice.

Please note that even though each of the canonical scopes is enough for a request to be accepted and passed to the backend, a request can still fail due to the backend requiring additional scopes or permissions.

JSON representation  
---  
      
    
    {
      "canonicalScopes": string
    }  
  
Fields  
---  
`canonicalScopes` |  `string` The list of publicly documented OAuth scopes that are allowed access. An OAuth token containing any of these scopes will be accepted.Example:
    
    
     canonicalScopes: https://www.googleapis.com/auth/calendar,
                       https://www.googleapis.com/auth/calendar.read
      
  
## AuthRequirement

User-defined authentication requirements, including support for [JSON Web token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

JSON representation  
---  
      
    
    {
      "providerId": string,
      "audiences": string
    }  
  
Fields  
---  
`providerId` |  `string` `[id](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#AuthProvider.FIELDS.id)` from authentication provider.Example:
    
    
    providerId: bookstore_auth
      
  
`audiences` |  `string` NOTE: This will be deprecated soon, once AuthProvider.audiences is implemented and accepted in all the runtime components.The list of JWT [audiences](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.3). that are allowed to access. A JWT containing any of these audiences will be accepted. When this setting is absent, only JWTs with audience "https://`[Service_name](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.name)`/`[API_name](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)`" will be accepted. For example, if no audiences are in the setting, LibraryService API will only accept JWTs with the following audience "https://library-example.googleapis.com/google.example.library.v1.LibraryService".Example:
    
    
    audiences: bookstore_android.apps.googleusercontent.com,
               bookstore_web.apps.googleusercontent.com
      
  
## AuthProvider

Configuration for an authentication provider, including support for [JSON Web token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

JSON representation  
---  
      
    
    {
      "id": string,
      "issuer": string,
      "jwksUri": string,
      "audiences": string,
      "authorizationUrl": string,
      "jwtLocations": [
        {
          object ([JwtLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#JwtLocation))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` The unique identifier of the auth provider. It will be referred to by `AuthRequirement.provider_id`.Example: "bookstore_auth".  
`issuer` |  `string` Identifies the principal that issued the JWT. See <https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.1> Usually a URL or an email address.Example: <https://securetoken.google.com> Example: [1234567-compute@developer.gserviceaccount.com](mailto:1234567-compute@developer.gserviceaccount.com)  
`jwksUri` |  `string` URL of the provider's public key set to validate signature of the JWT. See [OpenID Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata). Optional if the key set document: - can be retrieved from [OpenID Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) of the issuer. - can be inferred from the email domain of the issuer (e.g. a Google service account).Example: <https://www.googleapis.com/oauth2/v1/certs>  
`audiences` |  `string` The list of JWT [audiences](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.3). that are allowed to access. A JWT containing any of these audiences will be accepted. When this setting is absent, JWTs with audiences: - "https://[service.name]/`[google.protobuf.Api.name](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)`" - "https://[service.name]/" will be accepted. For example, if no audiences are in the setting, LibraryService API will accept JWTs with the following audiences: - <https://library-example.googleapis.com/google.example.library.v1.LibraryService> \- <https://library-example.googleapis.com/>Example:
    
    
    audiences: bookstore_android.apps.googleusercontent.com,
               bookstore_web.apps.googleusercontent.com
      
  
`authorizationUrl` |  `string` Redirect URL if JWT token is required but not present or is expired. Implement authorizationUrl of securityDefinitions in OpenAPI spec.  
`jwtLocations[]` |  `object (`[JwtLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#JwtLocation)`)` Defines the locations to extract the JWT. For now it is only used by the Cloud Endpoints to store the OpenAPI extension [x-google-jwt-locations](https://cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-jwt-locations)JWT locations can be one of HTTP headers, URL query parameters or cookies. The rule is that the first match wins.If not specified, default to use following 3 locations: 1) Authorization: Bearer 2) x-goog-iap-jwt-assertion 3) access_token query parameterDefault locations can be specified as followings: jwtLocations: - header: Authorization valuePrefix: "Bearer " - header: x-goog-iap-jwt-assertion - query: access_token  
  
## JwtLocation

Specifies a location to extract JWT from an API request.

JSON representation  
---  
      
    
    {
      "valuePrefix": string,
    
      // Union field in can be only one of the following:
      "header": string,
      "query": string,
      "cookie": string
      // End of list of possible types for union field in.
    }  
  
Fields  
---  
`valuePrefix` |  `string` The value prefix. The value format is "valuePrefix{token}" Only applies to "in" header type. Must be empty for "in" query type. If not empty, the header value has to match (case sensitive) this prefix. If not matched, JWT will not be extracted. If matched, JWT will be extracted after the prefix is removed.For example, for "Authorization: Bearer {JWT}", valuePrefix="Bearer " with a space at the end.  
Union field `in`.`in` can be only one of the following:  
`header` |  `string` Specifies HTTP header name to extract JWT token.  
`query` |  `string` Specifies URL query parameter name to extract JWT token.  
`cookie` |  `string` Specifies cookie name to extract JWT token.  
  
## Context

`Context` defines which contexts an API requests.

Example:
    
    
    context:
      rules:
      - selector: "*"
        requested:
        - google.rpc.context.ProjectContext
        - google.rpc.context.OriginContext
    

The above specifies that all methods in the API request `google.rpc.context.ProjectContext` and `google.rpc.context.OriginContext`.

Available context types are defined in package `google.rpc.context`.

This also provides mechanism to allowlist any protobuf message extension that can be sent in grpc metadata using “x-goog-ext--bin” and “x-goog-ext--jspb” format. For example, list any service specific protobuf types that can appear in grpc metadata as follows in your yaml file:

Example:
    
    
    context:
      rules:
       - selector: "google.example.library.v1.LibraryService.CreateBook"
         allowedRequestExtensions:
         - google.foo.v1.NewExtension
         allowedResponseExtensions:
         - google.foo.v1.NewExtension
    

You can also specify extension ID instead of fully qualified extension name here.

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([ContextRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#ContextRule))
        }
      ]
    }  
  
Fields  
---  
`rules[]` |  `object (`[ContextRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#ContextRule)`)` A list of RPC context rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
  
## ContextRule

A context rule provides information about the context for an individual API element.

JSON representation  
---  
      
    
    {
      "selector": string,
      "requested": [
        string
      ],
      "provided": [
        string
      ],
      "allowedRequestExtensions": [
        string
      ],
      "allowedResponseExtensions": [
        string
      ]
    }  
  
Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`requested[]` |  `string` A list of full type names of requested contexts.  
`provided[]` |  `string` A list of full type names of provided contexts.  
`allowedRequestExtensions[]` |  `string` A list of full type names or extension IDs of extensions allowed in grpc side channel from client to backend.  
`allowedResponseExtensions[]` |  `string` A list of full type names or extension IDs of extensions allowed in grpc side channel from backend to client.  
  
## Usage

Configuration controlling usage of a service.

JSON representation  
---  
      
    
    {
      "requirements": [
        string
      ],
      "rules": [
        {
          object ([UsageRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#UsageRule))
        }
      ],
      "producerNotificationChannel": string
    }  
  
Fields  
---  
`requirements[]` |  `string` Requirements that must be satisfied before a consumer project can use the service. Each requirement is of the form <service.name>/; for example 'serviceusage.googleapis.com/billing-enabled'.For Google APIs, a Terms of Service requirement must be included here. Google Cloud APIs must include "serviceusage.googleapis.com/tos/cloud". Other Google APIs should include "serviceusage.googleapis.com/tos/universal". Additional ToS can be included based on the business needs.  
`rules[]` |  `object (`[UsageRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#UsageRule)`)` A list of usage rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
`producerNotificationChannel` |  `string` The full resource name of a channel used for sending notifications to the service producer.Google Service Management currently only supports [Google Cloud Pub/Sub](https://cloud.google.com/pubsub) as a notification channel. To use Google Cloud Pub/Sub as the channel, this must be the name of a Cloud Pub/Sub topic that uses the Cloud Pub/Sub topic name format documented in <https://cloud.google.com/pubsub/docs/overview>.  
  
## UsageRule

Usage configuration rules for the service.

NOTE: Under development.

Use this rule to configure unregistered calls for the service. Unregistered calls are calls that do not contain consumer project identity. (Example: calls that do not contain an API key). By default, API methods do not allow unregistered calls, and each method call must be identified by a consumer project identity. Use this rule to allow/disallow unregistered calls.

Example of an API that wants to allow unregistered calls for entire service.
    
    
    usage:
      rules:
      - selector: "*"
        allowUnregisteredCalls: true
    

Example of a method that wants to allow unregistered calls.
    
    
    usage:
      rules:
      - selector: "google.example.library.v1.LibraryService.CreateBook"
        allowUnregisteredCalls: true
    

JSON representation  
---  
      
    
    {
      "selector": string,
      "allowUnregisteredCalls": boolean,
      "skipServiceControl": boolean
    }  
  
Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies. Use '*' to indicate all methods in all APIs.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`allowUnregisteredCalls` |  `boolean` If true, the selected method allows unregistered calls, e.g. calls that don't identify any user or application.  
`skipServiceControl` |  `boolean` If true, the selected method should skip service control and the control plane features, such as quota and billing, will not be available. This flag is used by Google Cloud Endpoints to bypass checks for internal methods, such as service health check methods.  
  
## CustomError

Customize service error responses. For example, list any service specific protobuf types that can appear in error detail lists of error responses.

Example:
    
    
    customError:
      types:
      - google.foo.v1.CustomError
      - google.foo.v1.AnotherError
    

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([CustomErrorRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#CustomErrorRule))
        }
      ],
      "types": [
        string
      ]
    }  
  
Fields  
---  
`rules[]` |  `object (`[CustomErrorRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#CustomErrorRule)`)` The list of custom error rules that apply to individual API messages.**NOTE:** All service configuration rules follow "last one wins" order.  
`types[]` |  `string` The list of custom error detail types, e.g. 'google.foo.v1.CustomError'.  
  
## CustomErrorRule

A custom error rule.

JSON representation  
---  
      
    
    {
      "selector": string,
      "isErrorType": boolean
    }  
  
Fields  
---  
`selector` |  `string` Selects messages to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`isErrorType` |  `boolean` Mark this message as possible payload in error response. Otherwise, objects of this type will be filtered when they appear in error payload.  
  
## Endpoint

`Endpoint` describes a network address of a service that serves a set of APIs. It is commonly known as a service endpoint. A service may expose any number of service endpoints, and all service endpoints share the same service definition, such as quota limits and monitoring metrics.

Example:
    
    
    type: google.api.Service
    name: library-example.googleapis.com
    endpoints:
      # Declares network address `https://library-example.googleapis.com`
      # for service `library-example.googleapis.com`. The `https` scheme
      # is implicit for all service endpoints. Other schemes may be
      # supported in the future.
    - name: library-example.googleapis.com
      allowCors: false
    - name: content-staging-library-example.googleapis.com
      # Allows HTTP OPTIONS calls to be passed to the API frontend, for it
      # to decide whether the subsequent cross-origin request is allowed
      # to proceed.
      allowCors: true
    

JSON representation  
---  
      
    
    {
      "name": string,
      "target": string,
      "allowCors": boolean
    }  
  
Fields  
---  
`name` |  `string` The canonical name of this endpoint.  
`target` |  `string` The specification of an Internet routable address of API frontend that will handle requests to this [API Endpoint](https://cloud.google.com/apis/design/glossary). It should be either a valid IPv4 address or a fully-qualified domain name. For example, "8.8.8.8" or "myservice.appspot.com".  
`allowCors` |  `boolean` Allowing [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), aka cross-domain traffic, would allow the backends served from this endpoint to receive and respond to HTTP OPTIONS requests. The response will be used by the browser to determine whether the subsequent cross-origin request is allowed to proceed.  
  
## Control

Selects and configures the service controller used by the service.

Example:
    
    
    control:
                environment: servicecontrol.googleapis.com

JSON representation  
---  
      
    
    {
      "environment": string
    }  
  
Fields  
---  
`environment` |  `string` The service controller environment to use. If empty, no control plane feature (like quota and billing) will be enabled. The recommended value for most services is servicecontrol.googleapis.com  
  
## LogDescriptor

A description of a log type. Example in YAML format:
    
    
    - name: library.googleapis.com/activity_history
      description: The history of borrowing and returning library items.
      displayName: Activity
      labels:
      - key: /customerId
        description: Identifier of a library customer
    

JSON representation  
---  
      
    
    {
      "name": string,
      "labels": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LabelDescriptor))
        }
      ],
      "description": string,
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` The name of the log. It must be less than 512 characters long and can include the following characters: upper- and lower-case alphanumeric characters [A-Za-z0-9], and punctuation characters including slash, underscore, hyphen, period [/_-.].  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LabelDescriptor)`)` The set of labels that are available to describe a specific log entry. Runtime requests that contain labels not specified here are considered invalid.  
`description` |  `string` A human-readable description of this log. This information appears in the documentation and can contain details.  
`displayName` |  `string` The human-readable name for this log. This information appears on the user interface and should be concise.  
  
## LabelDescriptor

A description of a label.

JSON representation  
---  
      
    
    {
      "key": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#ValueType)),
      "description": string
    }  
  
Fields  
---  
`key` |  `string` The label key.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#ValueType)`)` The type of data that can be assigned to the label.  
`description` |  `string` A human-readable description for the label.  
  
## ValueType

Value types that can be used as label values.

Enums  
---  
`STRING` | A variable-length string. This is the default.  
`BOOL` | Boolean; true or false.  
`INT64` | A 64-bit signed integer.  
  
## MetricDescriptor

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "labels": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LabelDescriptor))
        }
      ],
      "metricKind": enum ([MetricKind](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricKind)),
      "valueType": enum ([ValueType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#ValueType_1)),
      "unit": string,
      "description": string,
      "displayName": string,
      "metadata": {
        object ([MetricDescriptorMetadata](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricDescriptorMetadata))
      },
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LaunchStage)),
      "monitoredResourceTypes": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the metric descriptor.  
`type` |  `string` The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
    
    
    "custom.googleapis.com/invoice/paid/amount"
    "external.googleapis.com/prometheus/up"
    "appengine.googleapis.com/http/server/response_latencies"
      
  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LabelDescriptor)`)` The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.  
`metricKind` |  `enum (`[MetricKind](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricKind)`)` Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metricKind` and `valueType` might not be supported.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#ValueType_1)`)` Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metricKind` and `valueType` might not be supported.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `valueType` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)
  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)
  * `m` milli (10^-3)
  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)
  * `Ki` kibi (2^10)
  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar** The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).
  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:
    
    
    Expression = Component { "." Component } { "/" Component } ;
    
    Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ]
              | Annotation
              | "1"
              ;
    
    Annotation = "{" NAME "}" ;
    

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.
  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").

  
`description` |  `string` A detailed description of the metric, which can be used in documentation.  
`displayName` |  `string` A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.  
`metadata` |  `object (`[MetricDescriptorMetadata](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricDescriptorMetadata)`)` Optional. Metadata which can be used to guide usage of the metric.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LaunchStage)`)` Optional. The launch stage of the metric definition.  
`monitoredResourceTypes[]` |  `string` Read-only. If present, then a [time series][google.monitoring.v3.TimeSeries], which is identified partially by a metric type and a `[MonitoredResourceDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MonitoredResourceDescriptor)`, that is associated with this metric type can only be associated with one of the monitored resource types listed here.  
  
## MetricKind

The kind of measurement. It describes how the data is reported. For information on setting the start time and end time based on the MetricKind, see [TimeInterval][google.monitoring.v3.TimeInterval].

Enums  
---  
`METRIC_KIND_UNSPECIFIED` | Do not use this default value.  
`GAUGE` | An instantaneous measurement of a value.  
`DELTA` | The change in a value during a time interval.  
`CUMULATIVE` | A value accumulated over a time interval. Cumulative measurements in a time series should have the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
  
## ValueType

The value type of a metric.

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Do not use this default value.  
`BOOL` | The value is a boolean. This value type can be used only if the metric kind is `GAUGE`.  
`INT64` | The value is a signed 64-bit integer.  
`DOUBLE` | The value is a double precision floating point number.  
`STRING` | The value is a text string. This value type can be used only if the metric kind is `GAUGE`.  
`DISTRIBUTION` | The value is a [`Distribution`][google.api.Distribution].  
`MONEY` | The value is money.  
  
## MetricDescriptorMetadata

Additional annotations that can be used to guide the usage of a metric.

JSON representation  
---  
      
    
    {
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LaunchStage)),
      "samplePeriod": string,
      "ingestDelay": string
    }  
  
Fields  
---  
`launchStage  
**(deprecated)**` |  `enum (`[LaunchStage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LaunchStage)`)` This item is deprecated!Deprecated. Must use the `[MetricDescriptor.launch_stage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MetricDescriptor.FIELDS.launch_stage)` instead.  
`samplePeriod` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.A duration in seconds with up to nine fractional digits, terminated by '`s`'. Example: `"3.5s"`.  
`ingestDelay` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.A duration in seconds with up to nine fractional digits, terminated by '`s`'. Example: `"3.5s"`.  
  
## LaunchStage

The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages).

Enums  
---  
`LAUNCH_STAGE_UNSPECIFIED` | Do not use this default value.  
`UNIMPLEMENTED` | The feature is not yet implemented. Users can not use it.  
`PRELAUNCH` | Prelaunch features are hidden from users and are only visible internally.  
`EARLY_ACCESS` | Early Access features are limited to a closed group of testers. To use these features, you must sign up in advance and sign a Trusted Tester agreement (which includes confidentiality provisions). These features may be unstable, changed in backward-incompatible ways, and are not guaranteed to be released.  
`ALPHA` | Alpha is a limited availability test for releases before they are cleared for widespread use. By Alpha, all significant design issues are resolved and we are in the process of verifying functionality. Alpha customers need to apply for access, agree to applicable terms, and have their projects allowlisted. Alpha releases don't have to be feature complete, no SLAs are provided, and there are no technical support obligations, but they will be far enough along that customers can actually use them in test environments or for limited-use tests -- just like they would in normal production cases.  
`BETA` | Beta is the point at which we are ready to open a release for any customer to use. There are no SLA or technical support obligations in a Beta release. Products will be complete from a feature perspective, but may have some open outstanding issues. Beta releases are suitable for limited production use cases.  
`GA` | GA features are open to all developers and are considered stable and fully qualified for production use.  
`DEPRECATED` | Deprecated features are scheduled to be shut down and removed. For more information, see the "Deprecation Policy" section of our [Terms of Service](https://cloud.google.com/terms/) and the [Google Cloud Platform Subject to the Deprecation Policy](https://cloud.google.com/terms/deprecation) documentation.  
  
## MonitoredResourceDescriptor

An object that describes the schema of a `MonitoredResource` object using a type name and a set of labels. For example, the monitored resource descriptor for Google Compute Engine VM instances has a type of `"gce_instance"` and specifies the use of the labels `"instance_id"` and `"zone"` to identify particular VM instances.

Different APIs can support different monitored resource types. APIs generally provide a `list` method that returns the monitored resource descriptors used by the API.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "displayName": string,
      "description": string,
      "labels": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LabelDescriptor))
        }
      ],
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LaunchStage))
    }  
  
Fields  
---  
`name` |  `string` Optional. The resource name of the monitored resource descriptor: `"projects/{projectId}/monitoredResourceDescriptors/{type}"` where {type} is the value of the `type` field in this object and {projectId} is a project ID that provides API-specific context for accessing the type. APIs that do not use project information can use the resource name format `"monitoredResourceDescriptors/{type}"`.  
`type` |  `string` Required. The monitored resource type. For example, the type `"cloudsql_database"` represents databases in Google Cloud SQL. For a list of types, see [Monitoring resource types](https://cloud.google.com/monitoring/api/resources) and [Logging resource types](https://cloud.google.com/logging/docs/api/v2/resource-list).  
`displayName` |  `string` Optional. A concise name for the monitored resource type that might be displayed in user interfaces. It should be a Title Cased Noun Phrase, without any article or other determiners. For example, `"Google Cloud SQL Database"`.  
`description` |  `string` Optional. A detailed description of the monitored resource type that might be used in documentation.  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LabelDescriptor)`)` Required. A set of labels used to describe instances of this monitored resource type. For example, an individual Google Cloud SQL database is identified by values for the labels `"database_id"` and `"zone"`.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LaunchStage)`)` Optional. The launch stage of the monitored resource definition.  
  
## Billing

Billing related configuration of the service.

The following example shows how to configure monitored resources and metrics for billing, `consumerDestinations` is the only supported destination and the monitored resources need at least one label key `cloud.googleapis.com/location` to indicate the location of the billing usage, using different monitored resources between monitoring and billing is recommended so they can be evolved independently:
    
    
    monitoredResources:
    - type: library.googleapis.com/billing_branch
      labels:
      - key: cloud.googleapis.com/location
        description: |
          Predefined label to support billing location restriction.
      - key: city
        description: |
          Custom label to define the city where the library branch is located
          in.
      - key: name
        description: Custom label to define the name of the library branch.
    metrics:
    - name: library.googleapis.com/book/borrowed_count
      metricKind: DELTA
      valueType: INT64
      unit: "1"
    billing:
      consumerDestinations:
      - monitoredResource: library.googleapis.com/billing_branch
        metrics:
        - library.googleapis.com/book/borrowed_count
    

JSON representation  
---  
      
    
    {
      "consumerDestinations": [
        {
          object ([BillingDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#BillingDestination))
        }
      ]
    }  
  
Fields  
---  
`consumerDestinations[]` |  `object (`[BillingDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#BillingDestination)`)` Billing configurations for sending metrics to the consumer project. There can be multiple consumer destinations per service, each one must have a different monitored resource type. A metric can be used in at most one consumer destination.  
  
## BillingDestination

Configuration of a specific billing destination (Currently only support bill against consumer project).

JSON representation  
---  
      
    
    {
      "monitoredResource": string,
      "metrics": [
        string
      ]
    }  
  
Fields  
---  
`monitoredResource` |  `string` The monitored resource type. The type must be defined in `[Service.monitored_resources](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.monitored_resources)` section.  
`metrics[]` |  `string` Names of the metrics to report to this billing destination. Each name must be defined in `[Service.metrics](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.metrics)` section.  
  
## Logging

Logging configuration of the service.

The following example shows how to configure logs to be sent to the producer and consumer projects. In the example, the `activity_history` log is sent to both the producer and consumer projects, whereas the `purchase_history` log is only sent to the producer project.
    
    
    monitoredResources:
    - type: library.googleapis.com/branch
      labels:
      - key: /city
        description: The city where the library branch is located in.
      - key: /name
        description: The name of the branch.
    logs:
    - name: activity_history
      labels:
      - key: /customerId
    - name: purchase_history
    logging:
      producerDestinations:
      - monitoredResource: library.googleapis.com/branch
        logs:
        - activity_history
        - purchase_history
      consumerDestinations:
      - monitoredResource: library.googleapis.com/branch
        logs:
        - activity_history
    

JSON representation  
---  
      
    
    {
      "producerDestinations": [
        {
          object ([LoggingDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LoggingDestination))
        }
      ],
      "consumerDestinations": [
        {
          object ([LoggingDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LoggingDestination))
        }
      ]
    }  
  
Fields  
---  
`producerDestinations[]` |  `object (`[LoggingDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LoggingDestination)`)` Logging configurations for sending logs to the producer project. There can be multiple producer destinations, each one must have a different monitored resource type. A log can be used in at most one producer destination.  
`consumerDestinations[]` |  `object (`[LoggingDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#LoggingDestination)`)` Logging configurations for sending logs to the consumer project. There can be multiple consumer destinations, each one must have a different monitored resource type. A log can be used in at most one consumer destination.  
  
## LoggingDestination

Configuration of a specific logging destination (the producer project or the consumer project).

JSON representation  
---  
      
    
    {
      "monitoredResource": string,
      "logs": [
        string
      ]
    }  
  
Fields  
---  
`monitoredResource` |  `string` The monitored resource type. The type must be defined in the `[Service.monitored_resources](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.monitored_resources)` section.  
`logs[]` |  `string` Names of the logs to be sent to this destination. Each name must be defined in the `[Service.logs](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.logs)` section. If the log name is not a domain scoped name, it will be automatically prefixed with the service name followed by "/".  
  
## Monitoring

Monitoring configuration of the service.

The example below shows how to configure monitored resources and metrics for monitoring. In the example, a monitored resource and two metrics are defined. The `library.googleapis.com/book/returned_count` metric is sent to both producer and consumer projects, whereas the `library.googleapis.com/book/num_overdue` metric is only sent to the consumer project.
    
    
    monitoredResources:
    - type: library.googleapis.com/Branch
      displayName: "Library Branch"
      description: "A branch of a library."
      launchStage: GA
      labels:
      - key: resourceContainer
        description: "The Cloud container (ie. project id) for the Branch."
      - key: location
        description: "The location of the library branch."
      - key: branch_id
        description: "The id of the branch."
    metrics:
    - name: library.googleapis.com/book/returned_count
      displayName: "Books Returned"
      description: "The count of books that have been returned."
      launchStage: GA
      metricKind: DELTA
      valueType: INT64
      unit: "1"
      labels:
      - key: customerId
        description: "The id of the customer."
    - name: library.googleapis.com/book/num_overdue
      displayName: "Books Overdue"
      description: "The current number of overdue books."
      launchStage: GA
      metricKind: GAUGE
      valueType: INT64
      unit: "1"
      labels:
      - key: customerId
        description: "The id of the customer."
    monitoring:
      producerDestinations:
      - monitoredResource: library.googleapis.com/Branch
        metrics:
        - library.googleapis.com/book/returned_count
      consumerDestinations:
      - monitoredResource: library.googleapis.com/Branch
        metrics:
        - library.googleapis.com/book/returned_count
        - library.googleapis.com/book/num_overdue
    

JSON representation  
---  
      
    
    {
      "producerDestinations": [
        {
          object ([MonitoringDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MonitoringDestination))
        }
      ],
      "consumerDestinations": [
        {
          object ([MonitoringDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MonitoringDestination))
        }
      ]
    }  
  
Fields  
---  
`producerDestinations[]` |  `object (`[MonitoringDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MonitoringDestination)`)` Monitoring configurations for sending metrics to the producer project. There can be multiple producer destinations. A monitored resource type may appear in multiple monitoring destinations if different aggregations are needed for different sets of metrics associated with that monitored resource type. A monitored resource and metric pair may only be used once in the Monitoring configuration.  
`consumerDestinations[]` |  `object (`[MonitoringDestination](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#MonitoringDestination)`)` Monitoring configurations for sending metrics to the consumer project. There can be multiple consumer destinations. A monitored resource type may appear in multiple monitoring destinations if different aggregations are needed for different sets of metrics associated with that monitored resource type. A monitored resource and metric pair may only be used once in the Monitoring configuration.  
  
## MonitoringDestination

Configuration of a specific monitoring destination (the producer project or the consumer project).

JSON representation  
---  
      
    
    {
      "monitoredResource": string,
      "metrics": [
        string
      ]
    }  
  
Fields  
---  
`monitoredResource` |  `string` The monitored resource type. The type must be defined in `[Service.monitored_resources](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.monitored_resources)` section.  
`metrics[]` |  `string` Types of the metrics to report to this monitoring destination. Each type must be defined in `[Service.metrics](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service.FIELDS.metrics)` section.  
  
## SystemParameters

###### System parameter configuration

A system parameter is a special kind of parameter defined by the API system, not by an individual API. It is typically mapped to an HTTP header and/or a URL query parameter. This configuration specifies which methods change the names of the system parameters.

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([SystemParameterRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SystemParameterRule))
        }
      ]
    }  
  
Fields  
---  
`rules[]` |  `object (`[SystemParameterRule](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SystemParameterRule)`)` Define system parameters.The parameters defined here will override the default parameters implemented by the system. If this field is missing from the service config, default system parameters will be used. Default system parameters and names is implementation-dependent.Example: define api key for all methods
    
    
    systemParameters
      rules:
        - selector: "*"
          parameters:
            - name: api_key
              urlQueryParameter: api_key
    

Example: define 2 api key names for a specific method.
    
    
    systemParameters
      rules:
        - selector: "/ListShelves"
          parameters:
            - name: api_key
              httpHeader: Api-Key1
            - name: api_key
              httpHeader: Api-Key2
    

**NOTE:** All service configuration rules follow "last one wins" order.  
  
## SystemParameterRule

Define a system parameter rule mapping system parameter definitions to methods.

JSON representation  
---  
      
    
    {
      "selector": string,
      "parameters": [
        {
          object ([SystemParameter](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SystemParameter))
        }
      ]
    }  
  
Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies. Use '*' to indicate all methods in all APIs.Refer to `[selector](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#DocumentationRule.FIELDS.selector)` for syntax details.  
`parameters[]` |  `object (`[SystemParameter](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#SystemParameter)`)` Define parameters. Multiple names may be defined for a parameter. For a given method call, only one of them should be used. If multiple names are used the behavior is implementation-dependent. If none of the specified names are present the behavior is parameter-dependent.  
  
## SystemParameter

Define a parameter's name and location. The parameter may be passed as either an HTTP header or a URL query parameter, and if both are passed the behavior is implementation-dependent.

JSON representation  
---  
      
    
    {
      "name": string,
      "httpHeader": string,
      "urlQueryParameter": string
    }  
  
Fields  
---  
`name` |  `string` Define the name of the parameter, such as "api_key" . It is case sensitive.  
`httpHeader` |  `string` Define the HTTP header name to use for the parameter. It is case insensitive.  
`urlQueryParameter` |  `string` Define the URL query parameter name to use for the parameter. It is case sensitive.  
  
## SourceInfo

Source information used to create a Service Config

JSON representation  
---  
      
    
    {
      "sourceFiles": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`sourceFiles[]` |  `object` All files used during config generation.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/create)`

|  Creates a new service configuration (version) for a managed service.  
  
### `[get](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/get)`

|  Gets a service configuration (version) for a managed service.  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/list)`

|  Lists the history of the service configuration for a managed service, from the newest to the oldest.  
  
### `[submit](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit)`

|  Creates a new service configuration (version) for a managed service based on user-supplied configuration source files (for example: OpenAPI Specification).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-11 UTC."],[],[]] 
