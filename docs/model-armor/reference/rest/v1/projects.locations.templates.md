---
url: https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
title: REST Resource: projects.locations.templates \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:46:30.021577+00:00
---

# REST Resource: projects.locations.templates  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  REST Resource: projects.locations.templates Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Template
    * JSON representation
  * FilterConfig
    * JSON representation
  * RaiFilterSettings
    * JSON representation
  * RaiFilter
    * JSON representation
  * RaiFilterType
  * DetectionConfidenceLevel
  * SdpFilterSettings
    * JSON representation
  * SdpBasicConfig
    * JSON representation
  * SdpBasicConfigEnforcement
  * SdpAdvancedConfig
    * JSON representation
  * PiAndJailbreakFilterSettings
    * JSON representation
  * PiAndJailbreakFilterEnforcement
  * MaliciousUriFilterSettings
    * JSON representation
  * MaliciousUriFilterEnforcement
  * TemplateMetadata
    * JSON representation
  * EnforcementType
  * MultiLanguageDetection
    * JSON representation
  * FilterVersionSelector
    * JSON representation
  * FilterVersionAlias
  * Modality
  * Methods



## Resource: Template

Message describing Template resource

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "filterConfig": {
        object ([FilterConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterConfig))
      },
      "templateMetadata": {
        object ([TemplateMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#TemplateMetadata))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. name of resource  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`filterConfig` |  `object (`[FilterConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterConfig)`)` Required. filter configuration for this template  
`templateMetadata` |  `object (`[TemplateMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#TemplateMetadata)`)` Optional. metadata for this template  
  
## FilterConfig

Filters configuration.

JSON representation  
---  
      
    
    {
      "raiSettings": {
        object ([RaiFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilterSettings))
      },
      "sdpSettings": {
        object ([SdpFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpFilterSettings))
      },
      "piAndJailbreakFilterSettings": {
        object ([PiAndJailbreakFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#PiAndJailbreakFilterSettings))
      },
      "maliciousUriFilterSettings": {
        object ([MaliciousUriFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#MaliciousUriFilterSettings))
      }
    }  
  
Fields  
---  
`raiSettings` |  `object (`[RaiFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilterSettings)`)` Optional. Responsible AI settings.  
`sdpSettings` |  `object (`[SdpFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpFilterSettings)`)` Optional. Sensitive Data Protection settings.  
`piAndJailbreakFilterSettings` |  `object (`[PiAndJailbreakFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#PiAndJailbreakFilterSettings)`)` Optional. Prompt injection and Jailbreak filter settings.  
`maliciousUriFilterSettings` |  `object (`[MaliciousUriFilterSettings](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#MaliciousUriFilterSettings)`)` Optional. Malicious URI filter settings.  
  
## RaiFilterSettings

Responsible AI Filter settings.

JSON representation  
---  
      
    
    {
      "raiFilters": [
        {
          object ([RaiFilter](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilter))
        }
      ]
    }  
  
Fields  
---  
`raiFilters[]` |  `object (`[RaiFilter](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilter)`)` Required. List of Responsible AI filters enabled for template.  
  
## RaiFilter

Responsible AI filter.

JSON representation  
---  
      
    
    {
      "filterType": enum ([RaiFilterType](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilterType)),
      "confidenceLevel": enum ([DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel))
    }  
  
Fields  
---  
`filterType` |  `enum (`[RaiFilterType](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilterType)`)` Required. Type of responsible AI filter.  
`confidenceLevel` |  `enum (`[DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel)`)` Optional. Confidence level for this RAI filter. During data sanitization, if data is classified under this filter with a confidence level equal to or greater than the specified level, a positive match is reported. If the confidence level is unspecified (i.e., 0), the system will use a reasonable default level based on the `filterType`.  
  
## RaiFilterType

Options for responsible AI Filter Types.

Enums  
---  
`RAI_FILTER_TYPE_UNSPECIFIED` | Unspecified filter type.  
`SEXUALLY_EXPLICIT` | Sexually Explicit.  
`HATE_SPEECH` | Hate Speech.  
`HARASSMENT` | Harassment.  
`DANGEROUS` | Danger  
  
## DetectionConfidenceLevel

Confidence levels for detectors. Higher value maps to a greater confidence level. To enforce stricter level a lower value should be used.

Enums  
---  
`DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED` | Same as LOW_AND_ABOVE.  
`LOW_AND_ABOVE` | Highest chance of a false positive.  
`MEDIUM_AND_ABOVE` | Some chance of false positives.  
`HIGH` | Low chance of false positives.  
  
## SdpFilterSettings

Sensitive Data Protection settings.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "basicConfig": {
        object ([SdpBasicConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpBasicConfig))
      },
      "advancedConfig": {
        object ([SdpAdvancedConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpAdvancedConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Either of Sensitive Data Protection basic or advanced configuration. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`basicConfig` |  `object (`[SdpBasicConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpBasicConfig)`)` Optional. Basic Sensitive Data Protection configuration inspects the content for sensitive data using a fixed set of six info-types. Sensitive Data Protection templates cannot be used with basic configuration. Only Sensitive Data Protection inspection operation is supported with basic configuration.  
`advancedConfig` |  `object (`[SdpAdvancedConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpAdvancedConfig)`)` Optional. Advanced Sensitive Data Protection configuration which enables use of Sensitive Data Protection templates. Supports both Sensitive Data Protection inspection and de-identification operations.  
End of mutually exclusive fields.  
  
## SdpBasicConfig

Sensitive Data Protection basic configuration.

JSON representation  
---  
      
    
    {
      "filterEnforcement": enum ([SdpBasicConfigEnforcement](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpBasicConfigEnforcement))
    }  
  
Fields  
---  
`filterEnforcement` |  `enum (`[SdpBasicConfigEnforcement](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#SdpBasicConfigEnforcement)`)` Optional. Tells whether the Sensitive Data Protection basic config is enabled or disabled.  
  
## SdpBasicConfigEnforcement

Option to specify the state of Sensitive Data Protection basic config (ENABLED/DISABLED).

Enums  
---  
`SDP_BASIC_CONFIG_ENFORCEMENT_UNSPECIFIED` | Same as Disabled  
`ENABLED` | Enabled  
`DISABLED` | Disabled  
  
## SdpAdvancedConfig

Sensitive Data Protection Advanced configuration.

JSON representation  
---  
      
    
    {
      "inspectTemplate": string,
      "deidentifyTemplate": string
    }  
  
Fields  
---  
`inspectTemplate` |  `string` Optional. Sensitive Data Protection inspect template resource nameIf only inspect template is provided (de-identify template not provided), then Sensitive Data Protection InspectContent action is performed during Sanitization. All Sensitive Data Protection findings identified during inspection will be returned as SdpFinding in SdpInsepctionResult.e.g. `projects/{project}/locations/{location}/inspectTemplates/{inspectTemplate}`  
`deidentifyTemplate` |  `string` Optional. Optional Sensitive Data Protection Deidentify template resource name.If provided then DeidentifyContent action is performed during Sanitization using this template and inspect template. The De-identified data will be returned in SdpDeidentifyResult. Note that all info-types present in the deidentify template must be present in inspect template.e.g. `projects/{project}/locations/{location}/deidentifyTemplates/{deidentifyTemplate}`  
  
## PiAndJailbreakFilterSettings

Prompt injection and Jailbreak Filter settings.

JSON representation  
---  
      
    
    {
      "filterEnforcement": enum ([PiAndJailbreakFilterEnforcement](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#PiAndJailbreakFilterEnforcement)),
      "confidenceLevel": enum ([DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel))
    }  
  
Fields  
---  
`filterEnforcement` |  `enum (`[PiAndJailbreakFilterEnforcement](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#PiAndJailbreakFilterEnforcement)`)` Optional. Tells whether Prompt injection and Jailbreak filter is enabled or disabled.  
`confidenceLevel` |  `enum (`[DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel)`)` Optional. Confidence level for this filter. Confidence level is used to determine the threshold for the filter. If detection confidence is equal to or greater than the specified level, a positive match is reported. Confidence level will only be used if the filter is enabled.  
  
## PiAndJailbreakFilterEnforcement

Option to specify the state of Prompt Injection and Jailbreak filter (ENABLED/DISABLED).

Enums  
---  
`PI_AND_JAILBREAK_FILTER_ENFORCEMENT_UNSPECIFIED` | Same as Disabled  
`ENABLED` | Enabled  
`DISABLED` | Disabled  
  
## MaliciousUriFilterSettings

Malicious URI filter settings.

JSON representation  
---  
      
    
    {
      "filterEnforcement": enum ([MaliciousUriFilterEnforcement](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#MaliciousUriFilterEnforcement))
    }  
  
Fields  
---  
`filterEnforcement` |  `enum (`[MaliciousUriFilterEnforcement](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#MaliciousUriFilterEnforcement)`)` Optional. Tells whether the Malicious URI filter is enabled or disabled.  
  
## MaliciousUriFilterEnforcement

Option to specify the state of Malicious URI filter (ENABLED/DISABLED).

Enums  
---  
`MALICIOUS_URI_FILTER_ENFORCEMENT_UNSPECIFIED` | Same as Disabled  
`ENABLED` | Enabled  
`DISABLED` | Disabled  
  
## TemplateMetadata

Message describing TemplateMetadata

JSON representation  
---  
      
    
    {
      "ignorePartialInvocationFailures": boolean,
      "customPromptSafetyErrorCode": integer,
      "customPromptSafetyErrorMessage": string,
      "customLlmResponseSafetyErrorCode": integer,
      "customLlmResponseSafetyErrorMessage": string,
      "logTemplateOperations": boolean,
      "logSanitizeOperations": boolean,
      "enforcementType": enum ([EnforcementType](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#EnforcementType)),
      "multiLanguageDetection": {
        object ([MultiLanguageDetection](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#MultiLanguageDetection))
      },
      "modalities": [
        enum ([Modality](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#Modality))
      ],
      "filterVersionSelector": {
        object ([FilterVersionSelector](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterVersionSelector))
      },
      "dataResidencyCompliant": boolean
    }  
  
Fields  
---  
`ignorePartialInvocationFailures` |  `boolean` Optional. If true, partial detector failures should be ignored.  
`customPromptSafetyErrorCode` |  `integer` Optional. Indicates the custom error code set by the user to be returned to the end user by the service extension if the prompt trips Model Armor filters.  
`customPromptSafetyErrorMessage` |  `string` Optional. Indicates the custom error message set by the user to be returned to the end user if the prompt trips Model Armor filters.  
`customLlmResponseSafetyErrorCode` |  `integer` Optional. Indicates the custom error code set by the user to be returned to the end user if the LLM response trips Model Armor filters.  
`customLlmResponseSafetyErrorMessage` |  `string` Optional. Indicates the custom error message set by the user to be returned to the end user if the LLM response trips Model Armor filters.  
`logTemplateOperations` |  `boolean` Optional. If true, log template crud operations.  
`logSanitizeOperations` |  `boolean` Optional. If true, log sanitize operations.  
`enforcementType` |  `enum (`[EnforcementType](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#EnforcementType)`)` Optional. Enforcement type for Model Armor filters.  
`multiLanguageDetection` |  `object (`[MultiLanguageDetection](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#MultiLanguageDetection)`)` Optional. Metadata for multi language detection.  
`modalities[]` |  `enum (`[Modality](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#Modality)`)` Optional. Specifies the modalities to scan. If empty, only text modality will be scanned.  
`filterVersionSelector` |  `object (`[FilterVersionSelector](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterVersionSelector)`)` Optional. Specifies the configuration for the Filter version to be used. If this field is populated, it takes precedence over any values set in the deprecated `filterVersion` fields within `RaiFilterSettings`, `PiAndJailbreakFilterSettings`.  
`dataResidencyCompliant` |  `boolean` Optional. Indicates whether the template is subject to data residency compliance. If true (default for new templates), the template is subject to data residency compliance. If false, the template bypasses data residency compliance checks.  
  
## EnforcementType

Enforcement type for Model Armor filters.

Enums  
---  
`ENFORCEMENT_TYPE_UNSPECIFIED` | Default value. Same as INSPECT_AND_BLOCK.  
`INSPECT_ONLY` | Model Armor filters will run in inspect only mode. No action will be taken on the request.  
`INSPECT_AND_BLOCK` | Model Armor filters will run in inspect and block mode. Requests that trip Model Armor filters will be blocked.  
  
## MultiLanguageDetection

Metadata to enable multi language detection via template.

JSON representation  
---  
      
    
    {
      "enableMultiLanguageDetection": boolean
    }  
  
Fields  
---  
`enableMultiLanguageDetection` |  `boolean` Required. If true, multi language detection will be enabled.  
  
## FilterVersionSelector

Represents the configuration for selecting a Filter Version. Allows customers to choose to use either a specific version or a predefined alias.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "version": string,
      "alias": enum ([FilterVersionAlias](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterVersionAlias))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Specifies whether to use a specific version or an alias. The 'oneof' ensures that only one of these fields can be set. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`version` |  `string` Allows customers to pin to a specific, immutable Filter Version. This provides stability, as this will not change after a version upgrade. Expected format is a case-sensitive string, e.g., "v1", "v2". Requests providing an invalid or non-existent version string will be rejected with an `INVALID_ARGUMENT` error.  
`alias` |  `enum (`[FilterVersionAlias](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterVersionAlias)`)` Allows customers to use a predefined alias that dynamically points to a specific version based on internal upgrades. This offers flexibility and reduces the need for template updates.  
End of mutually exclusive fields.  
  
## FilterVersionAlias

Enum for Filter Version Aliases. These aliases provide a way to always point to a specific track without needing to update the version in templates.

Enums  
---  
`FILTER_VERSION_ALIAS_UNSPECIFIED` | The default value. If used, it will resolve to the `STABLE` alias.  
`FILTER_VERSION_ALIAS_STABLE` | The `STABLE` alias points to the most recent stable model version. Using this alias means no code changes are required when a new model becomes the stable version.  
`FILTER_VERSION_ALIAS_LATEST` | The `LATEST` alias points to the newest model version available. This version is subject to frequent revisions and offers SLO guarantees but does not assure stability, providing the most current security protections.  
`FILTER_VERSION_ALIAS_LEGACY` | The `LEGACY` alias could be used for sanitization operations for a transition period. New templates cannot be created with this version.  
`FILTER_VERSION_ALIAS_RETIRED` | The `RETIRED` alias could be used for versions that are no longer available to be used. While new templates cannot be created with this alias, any existing template or request using `RETIRED` version will fall back to the current `STABLE` version for sanitization operations.  
  
## Modality

This enum is used in the TemplateMetadata message to indicate the modality supported for sanitize API calls.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unspecified modality. If specified, all modalities will be sanitized.  
`MODALITY_TEXT` | Represents text modality. If specified, it will sanitize text fields, and text extracted from rich text files (like PDFs, DOCs) and plain text files (like TXT).  
`MODALITY_IMAGE` | Represents image modality. If specified, it will sanitize image files. The visual content and the text content in the image will be sanitized depending on the filter configuration.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/create)`

|  Creates a new Template in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/delete)`

|  Deletes a single Template.  
  
### `[get](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/get)`

|  Gets details of a single Template.  
  
### `[list](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/list)`

|  Lists Templates in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/patch)`

|  Updates the parameters of a single Template.  
  
### `[sanitizeModelResponse](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse)`

|  Sanitizes Model Response.  
  
### `[sanitizeUserPrompt](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeUserPrompt)`

|  Sanitizes User Prompt.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-07 UTC."],[],[]] 
