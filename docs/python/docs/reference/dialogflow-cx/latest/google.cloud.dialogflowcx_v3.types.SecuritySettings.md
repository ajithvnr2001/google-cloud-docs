---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings
title: Class SecuritySettings (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:21.889346+00:00
---

# Class SecuritySettings (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SecuritySettings (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    SecuritySettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the settings related to security issues, such as data redaction and data retention. It may take hours for updates on the settings to propagate to all the related components and take effect.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: `projects/`.   
`display_name` |  `str`   
Required. The human-readable name of the security settings, unique within the location.   
`redaction_strategy` |  `[google.cloud.dialogflowcx_v3.types.SecuritySettings.RedactionStrategy](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings.RedactionStrategy)`   
Strategy that defines how we do redaction.   
`redaction_scope` |  `[google.cloud.dialogflowcx_v3.types.SecuritySettings.RedactionScope](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings.RedactionScope)`   
Defines the data for which Dialogflow applies redaction. Dialogflow does not redact data that it does not have access to – for example, Cloud logging.   
`inspect_template` |  `str`   
`DLP `__ inspect template name. Use this template to define inspect base settings. The `DLP Inspect Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project. If empty, we use the default DLP inspect config. The template name will have one of the following formats: `projects/` OR `organizations/` Note: `inspect_template` must be located in the same region as the `SecuritySettings`.   
`deidentify_template` |  `str`   
`DLP `__ deidentify template name. Use this template to define de-identification configuration for the content. The `DLP De-identify Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project. If empty, Dialogflow replaces sensitive info with `[redacted]` text. The template name will have one of the following formats: `projects/` OR `organizations/` Note: `deidentify_template` must be located in the same region as the `SecuritySettings`.   
`retention_window_days` |  `int`   
Retains the data for the specified number of days. User must set a value lower than Dialogflow's default 365d TTL (30 days for Agent Assist traffic), higher value will be ignored and use default. Setting a value higher than that has no effect. A missing value or setting to 0 also means we use default TTL. When data retention configuration is changed, it only applies to the data created after the change; the TTL of existing data created before the change stays intact. This field is a member of `oneof`_ `data_retention`.   
`retention_strategy` |  `[google.cloud.dialogflowcx_v3.types.SecuritySettings.RetentionStrategy](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings.RetentionStrategy)`   
Specifies the retention behavior defined by SecuritySettings.RetentionStrategy. This field is a member of `oneof`_ `data_retention`.   
`purge_data_types` |  `MutableSequence[[google.cloud.dialogflowcx_v3.types.SecuritySettings.PurgeDataType](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings.PurgeDataType)]`   
List of types of data to remove when retention settings triggers purge.   
`audio_export_settings` |  `[google.cloud.dialogflowcx_v3.types.SecuritySettings.AudioExportSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings.AudioExportSettings)`   
Controls audio export settings for post-conversation analytics when ingesting audio to conversations via [Participants.AnalyzeContent][] or [Participants.StreamingAnalyzeContent][]. If retention_strategy is set to REMOVE_AFTER_CONVERSATION or [audio_export_settings.gcs_bucket][] is empty, audio export is disabled. If audio export is enabled, audio is recorded and saved to [audio_export_settings.gcs_bucket][], subject to retention policy of [audio_export_settings.gcs_bucket][]. This setting won't effect audio input for implicit sessions via Sessions.DetectIntent or Sessions.StreamingDetectIntent.   
`insights_export_settings` |  `[google.cloud.dialogflowcx_v3.types.SecuritySettings.InsightsExportSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings.InsightsExportSettings)`   
Controls conversation exporting settings to Insights after conversation is completed. If retention_strategy is set to REMOVE_AFTER_CONVERSATION, Insights export is disabled no matter what you configure here.   
  
## Classes 

### AudioExportSettings
    
    
    AudioExportSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings for exporting audio.

### InsightsExportSettings
    
    
    InsightsExportSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings for exporting conversations to `Insights <https://cloud.google.com/contact-center/insights/docs>`__.

### PurgeDataType
    
    
    PurgeDataType(value)

Type of data we purge after retention settings triggers purge.

### RedactionScope
    
    
    RedactionScope(value)

Defines what types of data to redact.

### RedactionStrategy
    
    
    RedactionStrategy(value)

Defines how we redact data.

### RetentionStrategy
    
    
    RetentionStrategy(value)

Defines how long we retain persisted data that contains sensitive info.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
