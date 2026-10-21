---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings/
title: Security settings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:54.216477+00:00
---

# Security settings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Security settings Stay organized with collections  Save and categorize content based on your preferences. 

Security settings configure data redaction and data retention. For example, these settings control how data is redacted in [Cloud logging](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging) and the [Conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history).

Security settings are set at the project level. If you have [access](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control#df-console) to an agent in a project, you can view project-level security settings. To update project-level security settings, you must have the [`dialogflow.securitySettings.update` permission](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin). Dialogflow can take up to one hour to implement security settings updates.

**Note:** For more information about other redaction options, see [parameter redaction](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#redact).

The following table summarizes the settings. For more information about the settings, see the [SecuritySettings RPC reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings).

Security Setting | Description  
---|---  
`redaction_strategy` | `[RedactionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.RedactionStrategy)`: Defines how we do redaction.  
`redaction_scope` | `[RedactionScope](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.RedactionScope)`: Defines the data for which Dialogflow applies redaction. Dialogflow does not redact data that it does not have access to – for example, Cloud logging.  
`inspect_template` | `string`[Sensitive Data Protection](https://cloud.google.com/dlp/docs): The inspect template name. Use this template to define inspect base settings.The `The DLP Inspect Templates Reader` role is needed on the Dialogflow service identity service account for your agent's project.If empty, we use the default Sensitive Data Protection inspect config.The template name will have one of the following formats: `projects//locations//inspectTemplates/` OR `organizations//locations//inspectTemplates/`Note: `inspect_template` must be located in the same region as the `SecuritySettings`.  
`deidentify_template` | `string`[Sensitive Data Protection](https://cloud.google.com/dlp/docs): The deidentify template name. Use this template to define deidentification configuration for the content.The `DLP Deidentify Templates Reader` role is needed on the Dialogflow service identity service account for your agent's project.If empty, Dialogflow replaces sensitive info with `[redacted]` text.The template name will have one of the following formats: `projects//locations//deidentifyTemplates/` OR `organizations//locations//deidentifyTemplates/`Note: `deidentify_template` must be located in the same region as the `SecuritySettings`.  
`purge_data_types[]` | `[PurgeDataType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.PurgeDataType)`: A list of types of data to be removed when retention settings triggers purge.  
`audio_export_settings` | `[AudioExportSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.AudioExportSettings)`: Controls audio export settings for post-conversation analytics when ingesting audio to conversations using `[]` or `[Participants.StreamingAnalyzeContent][]`.If `[retention_strategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.FIELDS.google.cloud.dialogflow.cx.v3.SecuritySettings.RetentionStrategy.google.cloud.dialogflow.cx.v3.SecuritySettings.retention_strategy)` is set to `REMOVE_AFTER_CONVERSATION` or `[audio_export_settings.gcs_bucket][]` is empty, audio export is disabled. If audio export is enabled, audio is recorded and saved to `[audio_export_settings.gcs_bucket][]`, subject to retention policy of `[audio_export_settings.gcs_bucket][]`.This setting won't affect audio input for implicit sessions using `[Sessions.DetectIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions.DetectIntent)` or `[Sessions.StreamingDetectIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions.StreamingDetectIntent)`.  
`insights_export_settings` | `[InsightsExportSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.InsightsExportSettings)`: Controls conversation exporting settings to Insights after conversation is completed.If `[retention_strategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.FIELDS.google.cloud.dialogflow.cx.v3.SecuritySettings.RetentionStrategy.google.cloud.dialogflow.cx.v3.SecuritySettings.retention_strategy)` is set to `REMOVE_AFTER_CONVERSATION`, Insights export is disabled no matter what you configure here.  
`data_retention` | The union field that specifies how data is retained. Even if data is purged because of a retention policy, it might remain in backup storage for a few days without allowing direct access. `data_retention` can be only one of the following:— `retention_window_days` (`int32`): Retains data for the specified number of days. You must set a value lower than Dialogflow's default 365-day TTL (30 days for Agent Assist traffic); higher values are ignored and the default is used. Setting a value higher than the default is ignored. A missing value or a setting of `0` also uses the default TTL. When data retention configuration is changed, it only applies to data created after the change; the TTL of existing data created before the change remains intact.— `[retention_strategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.RetentionStrategy)`: Specifies the retention behavior defined by `[SecuritySettings.RetentionStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings.RetentionStrategy)`.  
  
You can configure multiple security settings in each [location](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region). Each agent specifies the security settings to apply, and you can apply each setting to multiple agents in the same project and location. For more information about data application levels, see [data application levels](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level).

If you don't specify security settings in an agent, Dialogflow doesn't apply redaction.

## Create a security settings resource

To create a security settings resource in a particular location:

###  Console 

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your Google Cloud project.
  3. Select your agent.
  4. Click **Agent Settings**.
  5. Click the **Security** tab.
  6. Click **Manage security settings**. The CCAI console opens in a new tab.
  7. Click **Create security settings** in the CCAI console.
  8. Enter security settings configuration.
  9. Click **Create**.



###  API 

For information about the `create` method, see the `SecuritySettings` type. Go to the SecuritySettings API reference

**Select a protocol and version for the SecuritySettings reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [SecuritySettings resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings) |  [SecuritySettings resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.securitySettings)  
RPC |  [SecuritySettings interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SecuritySettings) |  [SecuritySettings interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.SecuritySettings)  
C++ |  [SecuritySettingssClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SecuritySettingsServiceClient.html) |  Not available   
C# |  [SecuritySettingssClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsClient) |  Not available   
Go |  [SecuritySettingssClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient) |  Not available   
Java |  [SecuritySettingssClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SecuritySettingsServiceClient) |  [SecuritySettingssClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SecuritySettingsServiceClient)  
Node.js |  [SecuritySettingssClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SecuritySettingsServiceClient.html) |  [SecuritySettingssClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SecuritySettingsServiceClient.html)  
PHP |  Not available  |  Not available   
Python |  [SecuritySettingssClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.security_settings_service.SecuritySettingsServiceClient) |  [SecuritySettingssClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.security_settings_service.SecuritySettingsServiceClient)  
Ruby |  Not available  |  Not available   
  
Close

## Specify a security setting in agent

To specify a security setting in agent:

###  Console 

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your Google Cloud project.
  3. Select your agent.
  4. Click **Agent Settings**.
  5. Click the **Security** tab.
  6. Select settings in the **Security settings** drop-down menu.
  7. Click **Save**.



###  API 

For information about the `patch` and `update` methods, see the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

**Caution:** If the Sensitive Data Protection inspect template is not defined, a default template is used. The default template only has some of the [infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes) enabled and might be unreliable for identifying and removing types according to end-user requirements. Always [create](https://console.cloud.google.com/security/dlp/create/template) a Sensitive Data Protection template whenever possible.

[ Previous arrow_back  Customer-managed encryption keys (CMEK)  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek)

[ Next Using VPC Service Controls  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/vpc-service-controls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
