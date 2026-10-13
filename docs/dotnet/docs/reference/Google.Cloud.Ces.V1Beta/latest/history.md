---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/history/
title: Version history \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:41.908486+00:00
---

# Version history  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Version history Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 

## Version 1.0.0-beta09, released 2026-07-13

### New features

  * Update public libraries for CES v1beta
  * Add WhatsApp, Instagram, and CCaaS Chat deployment channels
  * Add evaluation run caching settings
  * Add evaluation type (GOLDEN, SCENARIO) to evaluation service
  * Add context messages for external supervision guardrails
  * Add timeout configuration for toolsets



### Documentation improvements

  * A comment for field `disable_barge_in` in message `.google.cloud.ces.v1beta.BargeInConfig` is changed
  * A comment for enum value `PENDING` in enum `State` is changed
  * A comment for enum value `DONE` in enum `State` is changed
  * A comment for enum value `EXPIRED` in enum `State` is changed



## Version 1.0.0-beta08, released 2026-07-06

### Bug fixes

  * Add routing annotations to BidiRunSession in v1 and v1beta



## Version 1.0.0-beta07, released 2026-06-22

### Bug fixes

  * An existing field `root_agent` is removed from message `.google.cloud.ces.v1.AgentTool`



## Version 1.0.0-beta06, released 2026-06-15

### New features

  * Update cloud ml ces v1beta client libraries



### Documentation improvements

  * Update comments for `audio_recording_config` and `bigquery_export_settings` in `LoggingSettings`.
  * Update comments for various `InputType` enum values.
  * Update comments for `root_span`, `turns`, and `max_turns` in `Evaluation`.



## Version 1.0.0-beta05, released 2026-05-04

### New features

  * Add ability to specify mocked tool responses in ExecuteTool
  * Add ExportEvaluation RPC
  * Add support for app level fallback config
  * Add evaluation run and result information to ImportEvaluationsResponse



## Version 1.0.0-beta04, released 2026-04-06

### New features

  * Update public libraries for CES v1beta
  * Add support for generating app resources with LLM
  * Deprecate `root_agent` in message `.google.cloud.ces.v1beta.AgentTool` in favor of new `agent` field.
  * [Memorystore for Redis Cluster] Add support for Flexible CA feature
  * Update public libraries for CES v1beta
  * Add support for generating app resources with LLM
  * Deprecate `root_agent` in message `.google.cloud.ces.v1beta.AgentTool` in favor of new `agent` field.



### Documentation improvements

  * A comment for field `root_agent` in message `.google.cloud.ces.v1beta.AgentTool` is changed
  * A comment for field `root_agent` in message `.google.cloud.ces.v1beta.AgentTool` is changed



## Version 1.0.0-beta03, released 2026-03-23

### New features

  * Update public libraries for CES v1beta



### Documentation improvements

  * A comment for field `fallback_action` in message `.google.cloud.ces.v1beta.LanguageSettings` is changed
  * A comment for enum value `ERROR_HANDLING_STRATEGY_UNSPECIFIED` in enum `ErrorHandlingStrategy` is changed
  * A comment for enum value `FALLBACK_RESPONSE` in enum `ErrorHandlingStrategy` is changed
  * A comment for field `project` in message `.google.cloud.ces.v1beta.BigQueryExportSettings` is changed
  * A comment for field `dataset` in message `.google.cloud.ces.v1beta.BigQueryExportSettings` is changed
  * A comment for message `RunEvaluationOperationMetadata` is changed
  * A comment for method `RunSession` in service `SessionService` is changed



## Version 1.0.0-beta02, released 2026-03-09

### New features

  * Update public libraries for CES v1beta



### Bug fixes

  * An existing google.api.http annotation `http_uri` is changed for method `UploadEvaluationAudio` in service `EvaluationService`
  * An existing method_signature `app,audio_content` is removed from method `UploadEvaluationAudio` in service `EvaluationService`
  * An existing field `app` is renamed to `name` in message `.google.cloud.ces.v1beta.UploadEvaluationAudioRequest`
  * An existing field `audio_transcript` is renamed to `transcript` in message `.google.cloud.ces.v1beta.UploadEvaluationAudioResponse`
  * An existing field `audio_duration` is renamed to `duration` in message `.google.cloud.ces.v1beta.UploadEvaluationAudioResponse`
  * An existing field `variables` is moved in to oneof in message `.google.cloud.ces.v1beta.ExecuteToolRequest`



### Documentation improvements

  * A comment for field `cert` in message `.google.cloud.ces.v1beta.TlsConfig` is changed
  * A comment for field `entry_agent` in message `.google.cloud.ces.v1beta.SessionConfig` is changed
  * A comment for field `name` in message `.google.cloud.ces.v1beta.Tool` is changed



## Version 1.0.0-beta01, released 2026-03-02

### New features

  * Initial generation for Google.Cloud.Ces.V1Beta



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
