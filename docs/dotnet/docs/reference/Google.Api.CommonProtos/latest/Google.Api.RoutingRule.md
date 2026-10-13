---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule
title: Class RoutingRule (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:01.008162+00:00
---

# Class RoutingRule (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class RoutingRule (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.RoutingRule)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.RoutingRule)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.RoutingRule)


    
    
    public sealed class RoutingRule : IMessage<RoutingRule>, IEquatable<RoutingRule>, IDeepCloneable<RoutingRule>, IBufferMessage, IMessage

Specifies the routing information that should be sent along with the request in the form of routing header. **NOTE:** All service configuration rules follow the "last one wins" order.

The examples below will apply to an RPC which has the following request type:

Message Definition:
    
    
    message Request {
      // The name of the Table
      // Values can be of the following formats:
      // - `projects/<project>/tables/<table>`
      // - `projects/<project>/instances/<instance>/tables/<table>`
      // - `region/<region>/zones/<zone>/tables/<table>`
      string table_name = 1;
    
      // This value specifies routing for replication.
      // It can be in the following formats:
      // - `profiles/<profile_id>`
      // - a legacy `profile_id` that can be any string
      string app_profile_id = 2;
    }
    

Example message:
    
    
    {
      table_name: projects/proj_foo/instances/instance_bar/table/table_baz,
      app_profile_id: profiles/prof_qux
    }
    

The routing header consists of one or multiple key-value pairs. Every key and value must be percent-encoded, and joined together in the format of `key1=value1&key2=value2`. The examples below skip the percent-encoding for readability.

Example 1

Extracting a field from the request to put into the routing header unchanged, with the key equal to the field name.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `app_profile_id`.
      routing_parameters {
        field: "app_profile_id"
      }
    };
    

result:
    
    
    x-goog-request-params: app_profile_id=profiles/prof_qux
    

Example 2

Extracting a field from the request to put into the routing header unchanged, with the key different from the field name.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `app_profile_id`, but name it `routing_id` in the header.
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
    };
    

result:
    
    
    x-goog-request-params: routing_id=profiles/prof_qux
    

Example 3

Extracting a field from the request to put into the routing header, while matching a path template syntax on the field's value.

NB: it is more useful to send nothing than to send garbage for the purpose of dynamic routing, since garbage pollutes cache. Thus the matching.

Sub-example 3a

The field matches the template.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `table_name`, if it's well-formed (with project-based
      // syntax).
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=projects/*/instances/*/**}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    table_name=projects/proj_foo/instances/instance_bar/table/table_baz
    

Sub-example 3b

The field does not match the template.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `table_name`, if it's well-formed (with region-based
      // syntax).
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=regions/*/zones/*/**}"
      }
    };
    

result:
    
    
    <no routing header will be sent>
    

Sub-example 3c

Multiple alternative conflictingly named path templates are specified. The one that matches is used to construct the header.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `table_name`, if it's well-formed, whether
      // using the region- or projects-based syntax.
    
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=regions/*/zones/*/**}"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=projects/*/instances/*/**}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    table_name=projects/proj_foo/instances/instance_bar/table/table_baz
    

Example 4

Extracting a single routing header key-value pair by matching a template syntax on (a part of) a single request field.

annotation:
    
    
    option (google.api.routing) = {
      // Take just the project id from the `table_name` field.
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
    };
    

result:
    
    
    x-goog-request-params: routing_id=projects/proj_foo
    

Example 5

Extracting a single routing header key-value pair by matching several conflictingly named path templates on (parts of) a single request field. The last template to match "wins" the conflict.

annotation:
    
    
    option (google.api.routing) = {
      // If the `table_name` does not have instances information,
      // take just the project id for routing.
      // Otherwise take project + instance.
    
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*/instances/*}/**"
      }
    };
    

result:
    
    
    x-goog-request-params:
    routing_id=projects/proj_foo/instances/instance_bar
    

Example 6

Extracting multiple routing header key-value pairs by matching several non-conflicting path templates on (parts of) a single request field.

Sub-example 6a

Make the templates strict, so that if the `table_name` does not have an instance information, nothing is sent.

annotation:
    
    
    option (google.api.routing) = {
      // The routing code needs two keys instead of one composite
      // but works only for the tables with the "project-instance" name
      // syntax.
    
      routing_parameters {
        field: "table_name"
        path_template: "{project_id=projects/*}/instances/*/**"
      }
      routing_parameters {
        field: "table_name"
        path_template: "projects/*/{instance_id=instances/*}/**"
      }
    };
    

result:
    
    
    x-goog-request-params:
    project_id=projects/proj_foo&instance_id=instances/instance_bar
    

Sub-example 6b

Make the templates loose, so that if the `table_name` does not have an instance information, just the project id part is sent.

annotation:
    
    
    option (google.api.routing) = {
      // The routing code wants two keys instead of one composite
      // but will work with just the `project_id` for tables without
      // an instance in the `table_name`.
    
      routing_parameters {
        field: "table_name"
        path_template: "{project_id=projects/*}/**"
      }
      routing_parameters {
        field: "table_name"
        path_template: "projects/*/{instance_id=instances/*}/**"
      }
    };
    

result (is the same as 6a for our example message because it has the instance information):
    
    
    x-goog-request-params:
    project_id=projects/proj_foo&instance_id=instances/instance_bar
    

Example 7

Extracting multiple routing header key-value pairs by matching several path templates on multiple request fields.

NB: note that here there is no way to specify sending nothing if one of the fields does not match its template. E.g. if the `table_name` is in the wrong format, the `project_id` will not be sent, but the `routing_id` will be. The backend routing code has to be aware of that and be prepared to not receive a full complement of keys if it expects multiple.

annotation:
    
    
    option (google.api.routing) = {
      // The routing needs both `project_id` and `routing_id`
      // (from the `app_profile_id` field) for routing.
    
      routing_parameters {
        field: "table_name"
        path_template: "{project_id=projects/*}/**"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    project_id=projects/proj_foo&routing_id=profiles/prof_qux
    

Example 8

Extracting a single routing header key-value pair by matching several conflictingly named path templates on several request fields. The last template to match "wins" the conflict.

annotation:
    
    
    option (google.api.routing) = {
      // The `routing_id` can be a project id or a region id depending on
      // the table name format, but only if the `app_profile_id` is not set.
      // If `app_profile_id` is set it should be used instead.
    
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
      routing_parameters {
         field: "table_name"
         path_template: "{routing_id=regions/*}/**"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
    };
    

result:
    
    
    x-goog-request-params: routing_id=profiles/prof_qux
    

Example 9

Bringing it all together.

annotation:
    
    
    option (google.api.routing) = {
      // For routing both `table_location` and a `routing_id` are needed.
      //
      // table_location can be either an instance id or a region+zone id.
      //
      // For `routing_id`, take the value of `app_profile_id`
      // - If it's in the format `profiles/<profile_id>`, send
      // just the `<profile_id>` part.
      // - If it's any other literal, send it as is.
      // If the `app_profile_id` is empty, and the `table_name` starts with
      // the project_id, send that instead.
    
      routing_parameters {
        field: "table_name"
        path_template: "projects/*/{table_location=instances/*}/tables/*"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{table_location=regions/*/zones/*}/tables/*"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "profiles/{routing_id=*}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    table_location=instances/instance_bar&routing_id=prof_qux
    

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RoutingRule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### RoutingRule()
    
    
    public RoutingRule()

### RoutingRule(RoutingRule)
    
    
    public RoutingRule(RoutingRule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule)`  
  
  
## Fields 

### RoutingParametersFieldNumber
    
    
    public const int RoutingParametersFieldNumber = 2

Field number for the "routing_parameters" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### Parser
    
    
    public static MessageParser<RoutingRule> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule)` |   
  
### RoutingParameters
    
    
    public RepeatedField<RoutingParameter> RoutingParameters { get; }

A collection of Routing Parameter specifications. **NOTE:** If multiple Routing Parameters describe the same key (via the `path_template` field or via the `field` field when `path_template` is not provided), "last one wins" rule determines which Parameter gets used. See the examples for more details.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public RoutingRule Clone()

**Returns**  
---  
**Type** | **Description**  
`[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule)` |   
  
### Equals(RoutingRule)
    
    
    public bool Equals(RoutingRule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Equals(object)
    
    
    public override bool Equals(object other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[object](https://learn.microsoft.com/dotnet/api/system.object)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
**Overrides**

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### MergeFrom(RoutingRule)
    
    
    public void MergeFrom(RoutingRule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule)`  
  
  
### MergeFrom(CodedInputStream)
    
    
    public void MergeFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedInputStream.html)`  
  
  
### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

### WriteTo(CodedOutputStream)
    
    
    public void WriteTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedOutputStream.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
