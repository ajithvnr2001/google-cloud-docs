---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/summary_class/
title: Package Classes (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:51.999838+00:00
---

# Package Classes (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 

Summary of entries of Classes for google-cloud-modelarmor.

## Classes 

### [ModelArmorAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient)

Service describing handlers for resources

### [ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient)

Service describing handlers for resources

### [ListTemplatesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesAsyncPager)

A pager for iterating through `list_templates` requests.

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesResponse) object, and provides an `__aiter__` method to iterate through its `templates` field.

If there are more pages, the `__aiter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTemplatesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesPager)

A pager for iterating through `list_templates` requests.

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesResponse) object, and provides an `__iter__` method to iterate through its `templates` field.

If there are more pages, the `__iter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AiPlatformFloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.AiPlatformFloorSetting)

message describing AiPlatformFloorSetting

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ByteDataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ByteDataItem)

Represents Byte Data item.

### [ByteItemType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ByteDataItem.ByteItemType)

Option to specify the type of byte data.

### [CreateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.CreateTemplateRequest)

Message for creating a Template

### [CsamFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.CsamFilterResult)

CSAM (Child Safety Abuse Material) Filter Result

### [DataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DataItem)

Represents Data item

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DeleteTemplateRequest)

Message for deleting a Template

### [DetectionConfidenceLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DetectionConfidenceLevel)

Confidence levels for detectors. Higher value maps to a greater confidence level. To enforce stricter level a lower value should be used.

### [FilterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterConfig)

Filters configuration.

### [FilterExecutionState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterExecutionState)

Enum which reports whether a specific filter executed successfully or not.

### [FilterMatchState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterMatchState)

Option to specify filter match state.

### [FilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterResult)

Filter Result obtained after Sanitization operations.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting)

Message describing FloorSetting resource

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FloorSettingMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.FloorSettingMetadata)

message describing FloorSetting Metadata

### [MultiLanguageDetection](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.FloorSettingMetadata.MultiLanguageDetection)

Metadata to enable multi language detection via floor setting.

### [IntegratedService](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.IntegratedService)

Integrated service for which the floor setting is applicable.

### [GetFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetFloorSettingRequest)

Message for getting a Floor Setting

### [GetTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetTemplateRequest)

Message for getting a Template

### [InvocationResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.InvocationResult)

A field indicating the outcome of the invocation, irrespective of match status.

### [ListTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesRequest)

Message for requesting list of Templates

### [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesResponse)

Message for response to listing Templates

### [MaliciousUriFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MaliciousUriFilterResult)

Malicious URI Filter Result.

### [MaliciousUriMatchedItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MaliciousUriFilterResult.MaliciousUriMatchedItem)

Information regarding malicious URI and its location within the input content.

### [MaliciousUriFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MaliciousUriFilterSettings)

Malicious URI filter settings.

### [MaliciousUriFilterEnforcement](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MaliciousUriFilterSettings.MaliciousUriFilterEnforcement)

Option to specify the state of Malicious URI filter (ENABLED/DISABLED).

### [MessageItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MessageItem)

Message item to report information, warning or error messages.

### [MessageType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MessageItem.MessageType)

Option to specify the type of message.

### [Modality](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Modality)

This enum is used in the TemplateMetadata message to indicate the modality supported for sanitize API calls.

### [MultiLanguageDetectionMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MultiLanguageDetectionMetadata)

Message for Enabling Multi Language Detection.

### [PiAndJailbreakFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.PiAndJailbreakFilterResult)

Prompt injection and Jailbreak Filter Result.

### [PiAndJailbreakFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.PiAndJailbreakFilterSettings)

Prompt injection and Jailbreak Filter settings.

### [PiAndJailbreakFilterEnforcement](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement)

Option to specify the state of Prompt Injection and Jailbreak filter (ENABLED/DISABLED).

### [RaiFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterResult)

Responsible AI Result.

### [RaiFilterTypeResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterResult.RaiFilterTypeResult)

Detailed Filter result for each of the responsible AI Filter Types.

### [RaiFilterTypeResultsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterResult.RaiFilterTypeResultsEntry)

The abstract base class for a message.

### [RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings)

Responsible AI Filter settings.

### [RaiFilter](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.RaiFilter)

Responsible AI filter.

### [RaiFilterType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterType)

Options for responsible AI Filter Types.

### [RangeInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RangeInfo)

Half-open range interval [start, end)

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SanitizationResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizationResult)

Sanitization result after applying all the filters on input content.

### [FilterResultsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizationResult.FilterResultsEntry)

The abstract base class for a message.

### [SanitizationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizationResult.SanitizationMetadata)

Message describing Sanitization metadata.

### [SanitizeModelResponseRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseRequest)

Sanitize Model Response request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SanitizeModelResponseResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseResponse)

Sanitized Model Response Response.

### [SanitizeUserPromptRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptRequest)

Sanitize User Prompt request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SanitizeUserPromptResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptResponse)

Sanitized User Prompt Response.

### [SdpAdvancedConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpAdvancedConfig)

Sensitive Data Protection Advanced configuration.

### [SdpBasicConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpBasicConfig)

Sensitive Data Protection basic configuration.

### [SdpBasicConfigEnforcement](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpBasicConfig.SdpBasicConfigEnforcement)

Option to specify the state of Sensitive Data Protection basic config (ENABLED/DISABLED).

### [SdpContentLocation](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpContentLocation)

Precise location of the finding within a document, record, image, or metadata container.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SdpDeidentifyResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpDeidentifyResult)

Sensitive Data Protection Deidentification Result.

### [SdpFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFilterResult)

Sensitive Data Protection filter result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SdpFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFilterSettings)

Sensitive Data Protection settings.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SdpFinding](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFinding)

Finding corresponding to Sensitive Data Protection filter.

### [SdpFindingLocation](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFinding.SdpFindingLocation)

Location of this Sensitive Data Protection Finding within input content.

### [SdpFindingLikelihood](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFindingLikelihood)

For more information about each Sensitive Data Protection likelihood level, see <https://cloud.google.com/sensitive-data-protection/docs/likelihood>.

### [SdpImageFindingLocation](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpImageFindingLocation)

Location of the finding within an image.

### [SdpBoundingBox](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpImageFindingLocation.SdpBoundingBox)

Bounding box encompassing a finding within an image.

### [SdpInspectResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpInspectResult)

Sensitive Data Protection Inspection Result.

### [SdpRedactResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpRedactResult)

Sensitive Data Protection Redaction Result.

### [StreamingMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.StreamingMode)

Streaming Mode for Sanitize* API.

### [Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template)

Message describing Template resource

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.LabelsEntry)

The abstract base class for a message.

### [TemplateMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.TemplateMetadata)

Message describing TemplateMetadata

### [EnforcementType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.TemplateMetadata.EnforcementType)

Enforcement type for Model Armor filters.

### [MultiLanguageDetection](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.TemplateMetadata.MultiLanguageDetection)

Metadata to enable multi language detection via template.

### [UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateFloorSettingRequest)

Message for Updating a Floor Setting

### [UpdateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateTemplateRequest)

Message for updating a Template

### [VirusDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusDetail)

Details of an identified virus

### [ThreatType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusDetail.ThreatType)

Defines all the threat types of a virus

### [VirusScanFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusScanFilterResult)

Virus scan results.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ScannedContentType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusScanFilterResult.ScannedContentType)

Type of content scanned.

### [ModelArmorAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient)

Service describing handlers for resources

### [ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient)

Service describing handlers for resources

### [ListTemplatesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesAsyncPager)

A pager for iterating through `list_templates` requests.

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) object, and provides an `__aiter__` method to iterate through its `templates` field.

If there are more pages, the `__aiter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTemplatesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesPager)

A pager for iterating through `list_templates` requests.

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) object, and provides an `__iter__` method to iterate through its `templates` field.

If there are more pages, the `__iter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AiPlatformFloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.AiPlatformFloorSetting)

message describing AiPlatformFloorSetting

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ByteDataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ByteDataItem)

Represents Byte Data item.

### [ByteItemType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ByteDataItem.ByteItemType)

Option to specify the type of byte data.

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

### [FloorSettingMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FloorSetting.FloorSettingMetadata)

message describing FloorSetting Metadata

### [MultiLanguageDetection](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FloorSetting.FloorSettingMetadata.MultiLanguageDetection)

Metadata to enable multi language detection via floor setting.

### [IntegratedService](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.FloorSetting.IntegratedService)

Integrated service for which the floor setting is applicable.

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

### [MaliciousUriMatchedItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MaliciousUriFilterResult.MaliciousUriMatchedItem)

Information regarding malicious URI and its location within the input content.

### [MaliciousUriFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MaliciousUriFilterSettings)

Malicious URI filter settings.

### [MaliciousUriFilterEnforcement](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MaliciousUriFilterSettings.MaliciousUriFilterEnforcement)

Option to specify the state of Malicious URI filter (ENABLED/DISABLED).

### [McpServerFloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.McpServerFloorSetting)

Message describing MCP Server Floor Setting.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MessageItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MessageItem)

Message item to report information, warning or error messages.

### [MessageType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MessageItem.MessageType)

Option to specify the type of message.

### [MultiLanguageDetectionMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.MultiLanguageDetectionMetadata)

Message for Enabling Multi Language Detection.

### [PiAndJailbreakFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterResult)

Prompt injection and Jailbreak Filter Result.

### [PiAndJailbreakFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterSettings)

Prompt injection and Jailbreak Filter settings.

### [PiAndJailbreakFilterEnforcement](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement)

Option to specify the state of Prompt Injection and Jailbreak filter (ENABLED/DISABLED).

### [RaiFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterResult)

Responsible AI Result.

### [RaiFilterTypeResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterResult.RaiFilterTypeResult)

Detailed Filter result for each of the responsible AI Filter Types.

### [RaiFilterTypeResultsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterResult.RaiFilterTypeResultsEntry)

The abstract base class for a message.

### [RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterSettings)

Responsible AI Filter settings.

### [RaiFilter](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterSettings.RaiFilter)

Responsible AI filter.

### [RaiFilterType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RaiFilterType)

Options for responsible AI Filter Types.

### [RangeInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.RangeInfo)

Half-open range interval [start, end)

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SanitizationResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizationResult)

Sanitization result after applying all the filters on input content.

### [FilterResultsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizationResult.FilterResultsEntry)

The abstract base class for a message.

### [SanitizationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SanitizationResult.SanitizationMetadata)

Message describing Sanitization metadata.

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

### [SdpBasicConfigEnforcement](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpBasicConfig.SdpBasicConfigEnforcement)

Option to specify the state of Sensitive Data Protection basic config (ENABLED/DISABLED).

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

### [SdpFindingLocation](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpFinding.SdpFindingLocation)

Location of this Sensitive Data Protection Finding within input content.

### [SdpFindingLikelihood](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpFindingLikelihood)

For more information about each Sensitive Data Protection likelihood level, see <https://cloud.google.com/sensitive-data-protection/docs/likelihood>.

### [SdpInspectResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.SdpInspectResult)

Sensitive Data Protection Inspection Result.

### [StreamingMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.StreamingMode)

Streaming Mode for Sanitize* API.

### [Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.Template)

Message describing Template resource

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.Template.LabelsEntry)

The abstract base class for a message.

### [TemplateMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.Template.TemplateMetadata)

Message describing TemplateMetadata

### [EnforcementType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.Template.TemplateMetadata.EnforcementType)

Enforcement type for Model Armor filters.

### [MultiLanguageDetection](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.Template.TemplateMetadata.MultiLanguageDetection)

Metadata to enable multi language detection via template.

### [UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.UpdateFloorSettingRequest)

Message for Updating a Floor Setting

### [UpdateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.UpdateTemplateRequest)

Message for updating a Template

### [VirusDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.VirusDetail)

Details of an identified virus

### [ThreatType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.VirusDetail.ThreatType)

Defines all the threat types of a virus

### [VirusScanFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.VirusScanFilterResult)

Virus scan results.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ScannedContentType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.VirusScanFilterResult.ScannedContentType)

Type of content scanned.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.pagers)

API documentation for `modelarmor_v1.services.model_armor.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers)

API documentation for `modelarmor_v1beta.services.model_armor.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
