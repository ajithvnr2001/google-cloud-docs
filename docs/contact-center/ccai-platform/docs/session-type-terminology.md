---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-type-terminology/
title: Session type terminology \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:38.535223+00:00
---

# Session type terminology  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-type-terminology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Session type terminology Stay organized with collections  Save and categorize content based on your preferences. 

Session type names are passed to the CRM record, used in the API response, displayed in the session metadata file, and appear in Reporting.

## Unified session types

The new session type variable, **Session Type V2** , is now available. This update introduces a range of new fields, variables, and columns that will provide you with access to valuable additional information such as the ability to distinguish between Inbound SMS, Outbound SMS, and Outbound SMS via API.

You can continue to use your existing scripts and automations while working with your internal teams to plan for the necessary modifications. However, to take advantage of the new fields and variables, you will need to update your scripts, code, automation triggers, and any third-party integrations. The legacy components will no longer be updated with new functionality and will be deprecated on **October 6, 2023**.

**Note:** Salesforce users must first install the latest version of the package (Version 1.31).Area | New field, variable, column names | Legacy field, variable, common names  
---|---|---  
API endpoints (/manager/api/v1/calls and /manager/api/v1/chats) | `session_type_v2` | `call_type` and `chat_type` will remain  
Session metadata | `session_type_v2` |   
{SESSION_TYPE} variable in CRM Record Title in Operation Management | {SESSION_TYPE_V2} | {SESSION_TYPE} will remain  
CRM tags (Zendesk, Kustomer, Freshdesk) | The new values will be pushed alongside the old values to the same standard tags field |   
CCAIP Session Object (Salesforce) *In order to use the new session type, it is necessary to update to Salesforce Version 1.31 | Session Type v2 | "Session Type" will be renamed to "Session Type v1","Channel" will remain  
Reports | Session Type v2 | "Type" will be renamed to "Type v1"  
CCAIP Portal | UI in the Portal will contain the new values only | UI in the Portal will contain the new values only  
  
## Naming of session types across release versions

Channel | Legacy Session Types (before release version 1.66) | Session Types V1 (between release version 1.66 and 2.42 in the legacy field) | Session Types V2  
---|---|---|---  
Call | IVR Call | Voice Inbound (IVR) | Voice Inbound (IVR)  
Call | Incoming Call (Web) | Voice Callback (Web) | Voice Callback (Web)  
Call | Scheduled Call (Web) | Voice Scheduled (Web) | Voice Scheduled (Web)  
Call | Incoming Call (App) | Voice Inbound (App) | Voice Inbound (Mobile)  
Call | Scheduled Call (App) | Voice Scheduled (App) | Voice Scheduled (Mobile)  
Call | IVR Call (App) | Voice Inbound (IVR via App) | Voice Inbound (IVR via Mobile)  
Call | Outbound Call, Direct Call | Voice Outbound | Voice Outbound  
Call | Incoming Call (Api) | Voice Inbound (API) | Voice Inbound (API)  
Call | Outbound Call (Api) | Voice Outbound (API) | Voice Outbound (API)  
Chat | Web, Web Chat aka In-App | Messaging Inbound (Web Chat) | Messaging Inbound (Web Chat)  
Chat | In-App, App Chat aka In-App | Messaging Inbound (Mobile Chat) | Messaging Inbound (Mobile Chat)  
Chat | SMS Chat, SMS aka SMS Chat | Messaging (SMS) | Messaging Inbound (SMS)  
Chat | SMS Chat, SMS aka SMS Chat | Messaging (SMS) | Messaging Outbound (SMS)  
Chat | SMS Chat, SMS via API | Messaging (SMS) | Messaging Outbound (SMS via API)  
Chat | WhatsApp | Messaging (WhatsApp) | Messaging (WhatsApp)  
Campaign | Acqueon campaign | Voice Campaign (Acqueon) | Voice Campaign (Acqueon)  
Campaign | Campaign Call, CCAIP Campaign | Voice Campaign (CCAIP) | Voice Campaign (CCAIP)  
  
Examples of where to find:

**API** : `call_type` and `chat_type` fields in `/manager/api/{VERSION]}/calls` and `/manager/api/{VERSION}/chats` respectively.

**Reporting** : You can select these session types when you select call or chat types.

**Session metadata file** : `call_type` and `chat_type` fields.

**CRM Record Title** : If the {CALL_TYPE} variable is used in "Case Title" configuration located in Operation Management.

**CRM Custom Field values** : 'Session Type' field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
