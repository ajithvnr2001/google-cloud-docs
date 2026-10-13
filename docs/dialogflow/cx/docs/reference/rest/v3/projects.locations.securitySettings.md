---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings
title: REST Resource: projects.locations.securitySettings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:26.675739+00:00
---

# REST Resource: projects.locations.securitySettings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.securitySettings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SecuritySettings
    * JSON representation
  * RedactionStrategy
  * RedactionScope
  * RetentionStrategy
  * PurgeDataType
  * AudioExportSettings
    * JSON representation
  * AudioFormat
  * InsightsExportSettings
    * JSON representation
  * Methods



## Resource: SecuritySettings

Represents the settings related to security issues, such as data redaction and data retention. It may take hours for updates on the settings to propagate to all the related components and take effect.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "redactionStrategy": enum ([RedactionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#RedactionStrategy)),
      "redactionScope": enum ([RedactionScope](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#RedactionScope)),
      "inspectTemplate": string,
      "deidentifyTemplate": string,
      "purgeDataTypes": [
        enum ([PurgeDataType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#PurgeDataType))
      ],
      "audioExportSettings": {
        object ([AudioExportSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#AudioExportSettings))
      },
      "insightsExportSettings": {
        object ([InsightsExportSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#InsightsExportSettings))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "retentionWindowDays": integer,
      "retentionStrategy": enum ([RetentionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#RetentionStrategy))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Resource name of the settings. Required for the `[SecuritySettingsService.UpdateSecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/patch#google.cloud.dialogflow.cx.v3.SecuritySettingsService.UpdateSecuritySettings)` method. `[SecuritySettingsService.CreateSecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/create#google.cloud.dialogflow.cx.v3.SecuritySettingsService.CreateSecuritySettings)` populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`.  
`displayName` |  `string` Required. The human-readable name of the security settings, unique within the location.  
`redactionStrategy` |  `enum (`[RedactionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#RedactionStrategy)`)` Strategy that defines how we do redaction.  
`redactionScope` |  `enum (`[RedactionScope](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#RedactionScope)`)` Defines the data for which Dialogflow applies redaction. Dialogflow does not redact data that it does not have access to – for example, Cloud logging.  
`inspectTemplate` |  `string` [DLP](https://cloud.google.com/dlp/docs) inspect template name. Use this template to define inspect base settings.The `DLP Inspect Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project.If empty, we use the default DLP inspect config.The template name will have one of the following formats: `projects/<ProjectID>/locations/<LocationID>/inspectTemplates/<TemplateID>` OR `organizations/<OrganizationID>/locations/<LocationID>/inspectTemplates/<TemplateID>`Note: `inspectTemplate` must be located in the same region as the `SecuritySettings`.  
`deidentifyTemplate` |  `string` [DLP](https://cloud.google.com/dlp/docs) deidentify template name. Use this template to define de-identification configuration for the content.The `DLP De-identify Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project.If empty, Dialogflow replaces sensitive info with `[redacted]` text.The template name will have one of the following formats: `projects/<ProjectID>/locations/<LocationID>/deidentifyTemplates/<TemplateID>` OR `organizations/<OrganizationID>/locations/<LocationID>/deidentifyTemplates/<TemplateID>`Note: `deidentifyTemplate` must be located in the same region as the `SecuritySettings`.  
`purgeDataTypes[]` |  `enum (`[PurgeDataType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#PurgeDataType)`)` List of types of data to remove when retention settings triggers purge.  
`audioExportSettings` |  `object (`[AudioExportSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#AudioExportSettings)`)` Controls audio export settings for post-conversation analytics when ingesting audio to conversations via [Participants.AnalyzeContent][] or [Participants.StreamingAnalyzeContent][].If `[retentionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings.FIELDS.retention_strategy)` is set to REMOVE_AFTER_CONVERSATION or [audioExportSettings.gcs_bucket][] is empty, audio export is disabled.If audio export is enabled, audio is recorded and saved to [audioExportSettings.gcs_bucket][], subject to retention policy of [audioExportSettings.gcs_bucket][].This setting won't effect audio input for implicit sessions via `[Sessions.DetectIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/detectIntent#google.cloud.dialogflow.cx.v3.Sessions.DetectIntent)` or `Sessions.StreamingDetectIntent`.  
`insightsExportSettings` |  `object (`[InsightsExportSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#InsightsExportSettings)`)` Controls conversation exporting settings to Insights after conversation is completed.If `[retentionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings.FIELDS.retention_strategy)` is set to REMOVE_AFTER_CONVERSATION, Insights export is disabled no matter what you configure here.  
Specifies how data is retained. Note that even if the data is purged due to retention policy, we may still hold it in backup storage for a few days without allowing direct readings. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`retentionWindowDays` |  `integer` Retains the data for the specified number of days. User must set a value lower than Dialogflow's default 365d TTL (30 days for Agent Assist traffic), higher value will be ignored and use default. Setting a value higher than that has no effect. A missing value or setting to 0 also means we use default TTL. When data retention configuration is changed, it only applies to the data created after the change; the TTL of existing data created before the change stays intact.  
`retentionStrategy` |  `enum (`[RetentionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#RetentionStrategy)`)` Specifies the retention behavior defined by `[SecuritySettings.RetentionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#RetentionStrategy)`.  
End of mutually exclusive fields.  
  
## RedactionStrategy

Defines how we redact data.

Enums  
---  
`REDACTION_STRATEGY_UNSPECIFIED` | Do not redact.  
`REDACT_WITH_SERVICE` | Call redaction service to clean up the data to be persisted.  
  
## RedactionScope

Defines what types of data to redact.

Enums  
---  
`REDACTION_SCOPE_UNSPECIFIED` | Don't redact any kind of data.  
`REDACT_DISK_STORAGE` | On data to be written to disk or similar devices that are capable of holding data even if power is disconnected. This includes data that are temporarily saved on disk.  
  
## RetentionStrategy

Defines how long we retain persisted data that contains sensitive info.

Enums  
---  
`RETENTION_STRATEGY_UNSPECIFIED` | Retains the persisted data with Dialogflow's internal default 365d TTLs.  
`REMOVE_AFTER_CONVERSATION` | Removes data when the conversation ends. If there is no [Conversation][] explicitly established, a default conversation ends when the corresponding Dialogflow session ends.  
  
## PurgeDataType

Type of data we purge after retention settings triggers purge.

Enums  
---  
`PURGE_DATA_TYPE_UNSPECIFIED` | Unspecified. Do not use.  
`DIALOGFLOW_HISTORY` | Dialogflow history. This does not include Cloud logging, which is owned by the user - not Dialogflow.  
  
## AudioExportSettings

Settings for exporting audio.

JSON representation  
---  
      
    
    {
      "gcsBucket": string,
      "audioExportPattern": string,
      "enableAudioRedaction": boolean,
      "audioFormat": enum ([AudioFormat](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#AudioFormat)),
      "storeTtsAudio": boolean
    }  
  
Fields  
---  
`gcsBucket` |  `string` Cloud Storage bucket to export audio record to. Setting this field would grant the Storage Object Creator role to the Dialogflow Service Agent. API caller that tries to modify this field should have the permission of storage.buckets.setIamPolicy.  
`audioExportPattern` |  `string` Filename pattern for exported audio. {conversation} and {timestamp} are placeholders that will be replaced with the conversation ID and epoch micros of the conversation. For example, "{conversation}/recording_{timestamp}.mulaw".  
`enableAudioRedaction` |  `boolean` Enable audio redaction if it is true. Note that this only redacts end-user audio data; Synthesised audio from the virtual agent is not redacted.  
`audioFormat` |  `enum (`[AudioFormat](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#AudioFormat)`)` File format for exported audio file. Currently only in telephony recordings.  
`storeTtsAudio` |  `boolean` Whether to store TTS audio. By default, TTS audio from the virtual agent is not exported.  
  
## AudioFormat

File format for exported audio file. Currently only in telephony recordings.

Enums  
---  
`AUDIO_FORMAT_UNSPECIFIED` | Unspecified. Do not use.  
`MULAW` | G.711 mu-law PCM with 8kHz sample rate.  
`MP3` | MP3 file format.  
`OGG` | OGG Vorbis.  
  
## InsightsExportSettings

Settings for exporting conversations to [Insights](https://cloud.google.com/contact-center/insights/docs).

JSON representation  
---  
      
    
    {
      "enableInsightsExport": boolean
    }  
  
Fields  
---  
`enableInsightsExport` |  `boolean` If enabled, we will automatically exports conversations to Insights and Insights runs its analyzers.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/create)`

|  Create security settings in the specified location.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/delete)`

|  Deletes the specified `[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)`.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/get)`

|  Retrieves the specified `[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)`.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/list)`

|  Returns the list of all security settings in the specified location.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/patch)`

|  Updates the specified `[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
