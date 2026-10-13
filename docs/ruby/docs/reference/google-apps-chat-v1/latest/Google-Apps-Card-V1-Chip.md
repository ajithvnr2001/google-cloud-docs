---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Chip/
title: Google Chat V1 API - Class Google::Apps::Card::V1::Chip (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:16.937582+00:00
---

# Google Chat V1 API - Class Google::Apps::Card::V1::Chip (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Chip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Class Google::Apps::Card::V1::Chip (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API class Google::Apps::Card::V1::Chip.

A text, icon, or text and icon chip that users can click.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alt_text
    
    
    def alt_text() -> ::String

**Returns**

  * (::String) — The alternative text that's used for accessibility.

Set descriptive text that lets users know what the chip does. For example, if a chip opens a hyperlink, write: "Opens a new browser tab and navigates to the Google Chat developer documentation at https://developers.google.com/workspace/chat". 




### #alt_text=
    
    
    def alt_text=(value) -> ::String

**Parameter**

  * **value** (::String) — The alternative text that's used for accessibility.

Set descriptive text that lets users know what the chip does. For example, if a chip opens a hyperlink, write: "Opens a new browser tab and navigates to the Google Chat developer documentation at https://developers.google.com/workspace/chat". 




**Returns**

  * (::String) — The alternative text that's used for accessibility.

Set descriptive text that lets users know what the chip does. For example, if a chip opens a hyperlink, write: "Opens a new browser tab and navigates to the Google Chat developer documentation at https://developers.google.com/workspace/chat". 




### #disabled
    
    
    def disabled() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the chip is in an inactive state and ignores user actions. Defaults to `false`. 



### #disabled=
    
    
    def disabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the chip is in an inactive state and ignores user actions. Defaults to `false`. 



**Returns**

  * (::Boolean) — Whether the chip is in an inactive state and ignores user actions. Defaults to `false`. 



### #enabled
    
    
    def enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the chip is in an active state and responds to user actions. Defaults to `true`. Deprecated. Use `disabled` instead. 



### #enabled=
    
    
    def enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the chip is in an active state and responds to user actions. Defaults to `true`. Deprecated. Use `disabled` instead. 



**Returns**

  * (::Boolean) — Whether the chip is in an active state and responds to user actions. Defaults to `true`. Deprecated. Use `disabled` instead. 



### #icon
    
    
    def icon() -> ::Google::Apps::Card::V1::Icon

**Returns**

  * ([::Google::Apps::Card::V1::Icon](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Icon)) — The icon image. If both `icon` and `text` are set, then the icon appears before the text. 



### #icon=
    
    
    def icon=(value) -> ::Google::Apps::Card::V1::Icon

**Parameter**

  * **value** ([::Google::Apps::Card::V1::Icon](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Icon)) — The icon image. If both `icon` and `text` are set, then the icon appears before the text. 



**Returns**

  * ([::Google::Apps::Card::V1::Icon](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Icon)) — The icon image. If both `icon` and `text` are set, then the icon appears before the text. 



### #label
    
    
    def label() -> ::String

**Returns**

  * (::String) — The text displayed inside the chip. 



### #label=
    
    
    def label=(value) -> ::String

**Parameter**

  * **value** (::String) — The text displayed inside the chip. 



**Returns**

  * (::String) — The text displayed inside the chip. 



### #on_click
    
    
    def on_click() -> ::Google::Apps::Card::V1::OnClick

**Returns**

  * ([::Google::Apps::Card::V1::OnClick](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-OnClick)) — Optional. The action to perform when a user clicks the chip, such as opening a hyperlink or running a custom function. 



### #on_click=
    
    
    def on_click=(value) -> ::Google::Apps::Card::V1::OnClick

**Parameter**

  * **value** ([::Google::Apps::Card::V1::OnClick](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-OnClick)) — Optional. The action to perform when a user clicks the chip, such as opening a hyperlink or running a custom function. 



**Returns**

  * ([::Google::Apps::Card::V1::OnClick](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-OnClick)) — Optional. The action to perform when a user clicks the chip, such as opening a hyperlink or running a custom function. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
