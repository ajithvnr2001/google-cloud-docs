---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-Space/
title: Google Meet V2 API - Class Google::Apps::Meet::V2::Space (v0.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:11.171375+00:00
---

# Google Meet V2 API - Class Google::Apps::Meet::V2::Space (v0.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-Space/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Meet V2 API - Class Google::Apps::Meet::V2::Space (v0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.2  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Google Meet V2 API class Google::Apps::Meet::V2::Space.

Virtual place where conferences are held. Only one active conference can be held in one space at any given time.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #active_conference
    
    
    def active_conference() -> ::Google::Apps::Meet::V2::ActiveConference

**Returns**

  * ([::Google::Apps::Meet::V2::ActiveConference](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-ActiveConference)) — Active conference, if it exists. 



### #active_conference=
    
    
    def active_conference=(value) -> ::Google::Apps::Meet::V2::ActiveConference

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::ActiveConference](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-ActiveConference)) — Active conference, if it exists. 



**Returns**

  * ([::Google::Apps::Meet::V2::ActiveConference](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-ActiveConference)) — Active conference, if it exists. 



### #config
    
    
    def config() -> ::Google::Apps::Meet::V2::SpaceConfig

**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig)) — Configuration pertaining to the meeting space. 



### #config=
    
    
    def config=(value) -> ::Google::Apps::Meet::V2::SpaceConfig

**Parameter**

  * **value** ([::Google::Apps::Meet::V2::SpaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig)) — Configuration pertaining to the meeting space. 



**Returns**

  * ([::Google::Apps::Meet::V2::SpaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-SpaceConfig)) — Configuration pertaining to the meeting space. 



### #gateway_sip_access
    
    
    def gateway_sip_access() -> ::Array<::Google::Apps::Meet::V2::Space::GatewaySipAccess>

**Returns**

  * (::Array<[::Google::Apps::Meet::V2::Space::GatewaySipAccess](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-Space-GatewaySipAccess)>) — Output only. The SIP-based access methods that can be used to join the conference. Can be empty. 



### #meeting_code
    
    
    def meeting_code() -> ::String

**Returns**

  * (::String) — Output only. Type friendly unique string used to join the meeting.

Format: `[a-z]+-[a-z]+-[a-z]+`. For example, `abc-mnop-xyz`.

The maximum length is 128 characters.

Can only be used as an alias of the space name to get the space. 




### #meeting_uri
    
    
    def meeting_uri() -> ::String

**Returns**

  * (::String) — Output only. URI used to join meetings consisting of `https://meet.google.com/` followed by the `meeting_code`. For example, `https://meet.google.com/abc-mnop-xyz`. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Immutable. Resource name of the space.

Format: `spaces/{space}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space). 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. Resource name of the space.

Format: `spaces/{space}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space). 




**Returns**

  * (::String) — Immutable. Resource name of the space.

Format: `spaces/{space}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space). 




### #phone_access
    
    
    def phone_access() -> ::Array<::Google::Apps::Meet::V2::Space::PhoneAccess>

**Returns**

  * (::Array<[::Google::Apps::Meet::V2::Space::PhoneAccess](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2/latest/Google-Apps-Meet-V2-Space-PhoneAccess)>) — Output only. All regional phone access methods for this meeting space. Can be empty. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
