---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.DotnetSettings
title: Google API Common Protos Client - Class DotnetSettings (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:24.655082+00:00
---

# Google API Common Protos Client - Class DotnetSettings (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.DotnetSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class DotnetSettings (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class DotnetSettings.

Settings for Dotnet client libraries.

Generated from protobuf message `google.api.DotnetSettings`

## Namespace

Google \ Api

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ common` |  `[CommonLanguageSettings](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.CommonLanguageSettings)`   
Some settings.  
`↳ renamed_services` |  `array|[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)`   
Map from original service names to renamed versions. This is used when the default generated types would cause a naming conflict. (Neither name is fully-qualified.) Example: Subscriber to SubscriberServiceApi.  
`↳ renamed_resources` |  `array|[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)`   
Map from full resource types to the effective short name for the resource. This is used when otherwise resource named from different services would cause naming collisions. Example entry: "datalabeling.googleapis.com/Dataset": "DataLabelingDataset"  
`↳ ignored_resources` |  `string[]`   
List of full resource types to ignore during generation. This is typically used for API-specific Location resources, which should be handled by the generator as if they were actually the common Location resources. Example entry: "documentai.googleapis.com/Location"  
`↳ forced_namespace_aliases` |  `string[]`   
Namespaces which must be aliased in snippets due to a known (but non-generator-predictable) naming collision  
`↳ handwritten_signatures` |  `string[]`   
Method signatures (in the form "service.method(signature)") which are provided separately, so shouldn't be generated. Snippets _calling_ these methods are still generated, however.  
  
### getCommon

Some settings.

**Returns**  
---  
**Type** | **Description**  
`[CommonLanguageSettings](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.CommonLanguageSettings)|null` |   
  
### hasCommon

### clearCommon

### setCommon

Some settings.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CommonLanguageSettings](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.CommonLanguageSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRenamedServices

Map from original service names to renamed versions.

This is used when the default generated types would cause a naming conflict. (Neither name is fully-qualified.) Example: Subscriber to SubscriberServiceApi.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)` |   
  
### setRenamedServices

Map from original service names to renamed versions.

This is used when the default generated types would cause a naming conflict. (Neither name is fully-qualified.) Example: Subscriber to SubscriberServiceApi.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRenamedResources

Map from full resource types to the effective short name for the resource. This is used when otherwise resource named from different services would cause naming collisions.

Example entry: "datalabeling.googleapis.com/Dataset": "DataLabelingDataset"

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)` |   
  
### setRenamedResources

Map from full resource types to the effective short name for the resource. This is used when otherwise resource named from different services would cause naming collisions.

Example entry: "datalabeling.googleapis.com/Dataset": "DataLabelingDataset"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIgnoredResources

List of full resource types to ignore during generation.

This is typically used for API-specific Location resources, which should be handled by the generator as if they were actually the common Location resources. Example entry: "documentai.googleapis.com/Location"

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setIgnoredResources

List of full resource types to ignore during generation.

This is typically used for API-specific Location resources, which should be handled by the generator as if they were actually the common Location resources. Example entry: "documentai.googleapis.com/Location"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getForcedNamespaceAliases

Namespaces which must be aliased in snippets due to a known (but non-generator-predictable) naming collision

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setForcedNamespaceAliases

Namespaces which must be aliased in snippets due to a known (but non-generator-predictable) naming collision

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getHandwrittenSignatures

Method signatures (in the form "service.method(signature)") which are provided separately, so shouldn't be generated.

Snippets _calling_ these methods are still generated, however.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setHandwrittenSignatures

Method signatures (in the form "service.method(signature)") which are provided separately, so shouldn't be generated.

Snippets _calling_ these methods are still generated, however.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
