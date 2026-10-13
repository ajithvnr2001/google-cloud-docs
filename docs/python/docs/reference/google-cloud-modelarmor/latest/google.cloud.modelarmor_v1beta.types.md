---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types
title: Package types (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:07.041592+00:00
---

# Package types (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 

API documentation for `modelarmor_v1beta.types` package.

## Classes 

### [AiPlatformFloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.AiPlatformFloorSetting)

message describing AiPlatformFloorSetting

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ByteDataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ByteDataItem)

Represents Byte Data item.

### [CreateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.CreateTemplateRequest)

Message for creating a Template

### [CsamFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.CsamFilterResult)

CSAM (Child Safety Abuse Material) Filter Result

### [DataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.DataItem)

Represents Data item

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.DeleteTemplateRequest)

Message for deleting a Template

### [DetectionConfidenceLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.DetectionConfidenceLevel)

Confidence levels for detectors. Higher value maps to a greater confidence level. To enforce stricter level a lower value should be used.

### [FilterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FilterConfig)

Filters configuration.

### [FilterExecutionState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FilterExecutionState)

Enum which reports whether a specific filter executed successfully or not.

### [FilterMatchState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FilterMatchState)

Option to specify filter match state.

### [FilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FilterResult)

Filter Result obtained after Sanitization operations.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FloorSetting)

Message describing FloorSetting resource

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.GetFloorSettingRequest)

Message for getting a Floor Setting

### [GetTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.GetTemplateRequest)

Message for getting a Template

### [InvocationResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.InvocationResult)

A field indicating the outcome of the invocation, irrespective of match status.

### [ListTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesRequest)

Message for requesting list of Templates

### [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse)

Message for response to listing Templates

### [MaliciousUriFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MaliciousUriFilterResult)

Malicious URI Filter Result.

### [MaliciousUriFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MaliciousUriFilterSettings)

Malicious URI filter settings.

### [McpServerFloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.McpServerFloorSetting)

Message describing MCP Server Floor Setting.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MessageItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MessageItem)

Message item to report information, warning or error messages.

### [MultiLanguageDetectionMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MultiLanguageDetectionMetadata)

Message for Enabling Multi Language Detection.

### [PiAndJailbreakFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterResult)

Prompt injection and Jailbreak Filter Result.

### [PiAndJailbreakFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterSettings)

Prompt injection and Jailbreak Filter settings.

### [RaiFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterResult)

Responsible AI Result.

### [RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterSettings)

Responsible AI Filter settings.

### [RaiFilterType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterType)

Options for responsible AI Filter Types.

### [RangeInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RangeInfo)

Half-open range interval [start, end)

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SanitizationResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizationResult)

Sanitization result after applying all the filters on input content.

### [SanitizeModelResponseRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizeModelResponseRequest)

Sanitize Model Response request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SanitizeModelResponseResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizeModelResponseResponse)

Sanitized Model Response Response.

### [SanitizeUserPromptRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizeUserPromptRequest)

Sanitize User Prompt request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SanitizeUserPromptResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizeUserPromptResponse)

Sanitized User Prompt Response.

### [SdpAdvancedConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpAdvancedConfig)

Sensitive Data Protection Advanced configuration.

### [SdpBasicConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpBasicConfig)

Sensitive Data Protection basic configuration.

### [SdpDeidentifyResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpDeidentifyResult)

Sensitive Data Protection Deidentification Result.

### [SdpFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpFilterResult)

Sensitive Data Protection filter result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SdpFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpFilterSettings)

Sensitive Data Protection settings.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SdpFinding](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpFinding)

Finding corresponding to Sensitive Data Protection filter.

### [SdpFindingLikelihood](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpFindingLikelihood)

For more information about each Sensitive Data Protection likelihood level, see <https://cloud.google.com/sensitive-data-protection/docs/likelihood>.

### [SdpInspectResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpInspectResult)

Sensitive Data Protection Inspection Result.

### [StreamingMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.StreamingMode)

Streaming Mode for Sanitize* API.

### [Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.Template)

Message describing Template resource

### [UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.UpdateFloorSettingRequest)

Message for Updating a Floor Setting

### [UpdateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.UpdateTemplateRequest)

Message for updating a Template

### [VirusDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.VirusDetail)

Details of an identified virus

### [VirusScanFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.VirusScanFilterResult)

Virus scan results.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
