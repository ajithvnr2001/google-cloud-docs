---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig/
title: Google Meet V2 API - Class Google::Apps::Meet::V2::SpaceConfig (v0.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:13.102720+00:00
---

# Google Meet V2 API - Class Google::Apps::Meet::V2::SpaceConfig (v0.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Meet V2 API - Class Google::Apps::Meet::V2::SpaceConfig (v0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.2  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Google Meet V2 API class Google::Apps::Meet::V2::SpaceConfig.

The configuration pertaining to a meeting space.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access_type
    
    
    def access_type() -> ::Google::Apps::Meet::V2::SpaceConfig::AccessType

**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-AccessType)) — Access type of the meeting space that determines who can join without knocking. Default: The user's default access settings. Controlled by the user's admin for enterprise users or RESTRICTED. 



### #access_type=
    
    
    def access_type=(value) -> ::Google::Apps::Meet::V2::SpaceConfig::AccessType

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::SpaceConfig::AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-AccessType)) — Access type of the meeting space that determines who can join without knocking. Default: The user's default access settings. Controlled by the user's admin for enterprise users or RESTRICTED. 



**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-AccessType)) — Access type of the meeting space that determines who can join without knocking. Default: The user's default access settings. Controlled by the user's admin for enterprise users or RESTRICTED. 



### #artifact_config
    
    
    def artifact_config() -> ::Google::Apps::Meet::V2::SpaceConfig::ArtifactConfig

**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::ArtifactConfig](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-ArtifactConfig)) — Configuration pertaining to the auto-generated artifacts that the meeting supports. 



### #artifact_config=
    
    
    def artifact_config=(value) -> ::Google::Apps::Meet::V2::SpaceConfig::ArtifactConfig

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::SpaceConfig::ArtifactConfig](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-ArtifactConfig)) — Configuration pertaining to the auto-generated artifacts that the meeting supports. 



**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::ArtifactConfig](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-ArtifactConfig)) — Configuration pertaining to the auto-generated artifacts that the meeting supports. 



### #attendance_report_generation_type
    
    
    def attendance_report_generation_type() -> ::Google::Apps::Meet::V2::SpaceConfig::AttendanceReportGenerationType

**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::AttendanceReportGenerationType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-AttendanceReportGenerationType)) — Whether attendance report is enabled for the meeting space. 



### #attendance_report_generation_type=
    
    
    def attendance_report_generation_type=(value) -> ::Google::Apps::Meet::V2::SpaceConfig::AttendanceReportGenerationType

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::SpaceConfig::AttendanceReportGenerationType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-AttendanceReportGenerationType)) — Whether attendance report is enabled for the meeting space. 



**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::AttendanceReportGenerationType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-AttendanceReportGenerationType)) — Whether attendance report is enabled for the meeting space. 



### #entry_point_access
    
    
    def entry_point_access() -> ::Google::Apps::Meet::V2::SpaceConfig::EntryPointAccess

**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::EntryPointAccess](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-EntryPointAccess)) — Defines the entry points that can be used to join meetings hosted in this meeting space. Default: EntryPointAccess.ALL 



### #entry_point_access=
    
    
    def entry_point_access=(value) -> ::Google::Apps::Meet::V2::SpaceConfig::EntryPointAccess

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::SpaceConfig::EntryPointAccess](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-EntryPointAccess)) — Defines the entry points that can be used to join meetings hosted in this meeting space. Default: EntryPointAccess.ALL 



**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::EntryPointAccess](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-EntryPointAccess)) — Defines the entry points that can be used to join meetings hosted in this meeting space. Default: EntryPointAccess.ALL 



### #moderation
    
    
    def moderation() -> ::Google::Apps::Meet::V2::SpaceConfig::Moderation

**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::Moderation](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-Moderation)) — The pre-configured moderation mode for the Meeting. Default: Controlled by the user's policies. 



### #moderation=
    
    
    def moderation=(value) -> ::Google::Apps::Meet::V2::SpaceConfig::Moderation

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::SpaceConfig::Moderation](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-Moderation)) — The pre-configured moderation mode for the Meeting. Default: Controlled by the user's policies. 



**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::Moderation](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-Moderation)) — The pre-configured moderation mode for the Meeting. Default: Controlled by the user's policies. 



### #moderation_restrictions
    
    
    def moderation_restrictions() -> ::Google::Apps::Meet::V2::SpaceConfig::ModerationRestrictions

**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::ModerationRestrictions](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-ModerationRestrictions)) — When moderation.ON, these restrictions go into effect for the meeting. When moderation.OFF, will be reset to default ModerationRestrictions. 



### #moderation_restrictions=
    
    
    def moderation_restrictions=(value) -> ::Google::Apps::Meet::V2::SpaceConfig::ModerationRestrictions

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::SpaceConfig::ModerationRestrictions](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-ModerationRestrictions)) — When moderation.ON, these restrictions go into effect for the meeting. When moderation.OFF, will be reset to default ModerationRestrictions. 



**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig::ModerationRestrictions](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig-ModerationRestrictions)) — When moderation.ON, these restrictions go into effect for the meeting. When moderation.OFF, will be reset to default ModerationRestrictions. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
