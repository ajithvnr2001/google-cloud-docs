---
url: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Api
title: proto library Client - Class Api (v5.36.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:53.322450+00:00
---

# proto library Client - Class Api (v5.36.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Api

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  proto library Client - Class Api (v5.36.2) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the proto library Client class Api.

Api is a light-weight descriptor for an API Interface.

Interfaces are also described as "protocol buffer services" in some contexts, such as by the "service" keyword in a .proto file, but they are different from API Services, which represent a concrete implementation of an interface as opposed to simply a description of methods and bindings. They are also sometimes simply referred to as "APIs" in other contexts, such as the name of this message itself. See <https://cloud.google.com/apis/design/glossary> for detailed terminology. New usages of this message as an alternative to ServiceDescriptorProto are strongly discouraged. This message does not reliability preserve all information necessary to model the schema and preserve semantics. Instead make use of FileDescriptorSet which preserves the necessary information.

Generated from protobuf message `google.protobuf.Api`

## Namespace

Google \ Protobuf

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
The fully qualified name of this interface, including package name followed by the interface's simple name.  
`↳ methods` |  `array<[Method](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Method)>`   
The methods of this interface, in unspecified order.  
`↳ options` |  `array<[Option](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Option)>`   
Any metadata attached to the interface.  
`↳ version` |  `string`   
A version string for this interface. If specified, must have the form `major-version.minor-version`, as in `1.10`. If the minor version is omitted, it defaults to zero. If the entire version field is empty, the major version is derived from the package name, as outlined below. If the field is not empty, the version in the package name will be verified to be consistent with what is provided here. The versioning schema uses [semantic versioning](http://semver.org) where the major version number indicates a breaking change and the minor version an additive, non-breaking change. Both version numbers are signals to users what to expect from different versions, and should be carefully chosen based on the product plan. The major version is also reflected in the package name of the interface, which must end in `v<major-version>`, as in `google.feature.v1`. For major versions 0 and 1, the suffix can be omitted. Zero major versions must only be used for experimental, non-GA interfaces.  
`↳ source_context` |  `[SourceContext](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.SourceContext)`   
Source context for the protocol buffer service represented by this message.  
`↳ mixins` |  `array<[Mixin](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Mixin)>`   
Included interfaces. See Mixin.  
`↳ syntax` |  `int`   
The source syntax of the service.  
`↳ edition` |  `string`   
The source edition string, only valid when syntax is SYNTAX_EDITIONS.  
  
### getName

The fully qualified name of this interface, including package name followed by the interface's simple name.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The fully qualified name of this interface, including package name followed by the interface's simple name.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMethods

The methods of this interface, in unspecified order.

**Returns**  
---  
**Type** | **Description**  
`[RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField)<[Method](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Method)>` |   
  
### setMethods

The methods of this interface, in unspecified order.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Method](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Method)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOptions

Any metadata attached to the interface.

**Returns**  
---  
**Type** | **Description**  
`[RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField)<[Option](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Option)>` |   
  
### setOptions

Any metadata attached to the interface.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Option](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Option)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getVersion

A version string for this interface. If specified, must have the form `major-version.minor-version`, as in `1.10`. If the minor version is omitted, it defaults to zero. If the entire version field is empty, the major version is derived from the package name, as outlined below. If the field is not empty, the version in the package name will be verified to be consistent with what is provided here.

The versioning schema uses [semantic versioning](http://semver.org) where the major version number indicates a breaking change and the minor version an additive, non-breaking change. Both version numbers are signals to users what to expect from different versions, and should be carefully chosen based on the product plan. The major version is also reflected in the package name of the interface, which must end in `v<major-version>`, as in `google.feature.v1`. For major versions 0 and 1, the suffix can be omitted. Zero major versions must only be used for experimental, non-GA interfaces.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setVersion

A version string for this interface. If specified, must have the form `major-version.minor-version`, as in `1.10`. If the minor version is omitted, it defaults to zero. If the entire version field is empty, the major version is derived from the package name, as outlined below. If the field is not empty, the version in the package name will be verified to be consistent with what is provided here.

The versioning schema uses [semantic versioning](http://semver.org) where the major version number indicates a breaking change and the minor version an additive, non-breaking change. Both version numbers are signals to users what to expect from different versions, and should be carefully chosen based on the product plan. The major version is also reflected in the package name of the interface, which must end in `v<major-version>`, as in `google.feature.v1`. For major versions 0 and 1, the suffix can be omitted. Zero major versions must only be used for experimental, non-GA interfaces.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceContext

Source context for the protocol buffer service represented by this message.

**Returns**  
---  
**Type** | **Description**  
`[SourceContext](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.SourceContext)|null` |   
  
### hasSourceContext

### clearSourceContext

### setSourceContext

Source context for the protocol buffer service represented by this message.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[SourceContext](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.SourceContext)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMixins

Included interfaces. See Mixin.

**Returns**  
---  
**Type** | **Description**  
`[RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField)<[Mixin](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Mixin)>` |   
  
### setMixins

Included interfaces. See Mixin.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Mixin](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Mixin)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSyntax

The source syntax of the service.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Syntax](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Syntax). one of the values in {@see \Google\Protobuf\Syntax}  
  
### setSyntax

The source syntax of the service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Syntax](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Syntax). one of the values in [Syntax](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Syntax)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEdition

The source edition string, only valid when syntax is SYNTAX_EDITIONS.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEdition

The source edition string, only valid when syntax is SYNTAX_EDITIONS.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
