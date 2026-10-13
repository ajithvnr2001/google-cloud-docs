---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Columns-Column-Widgets/
title: Google Chat V1 API - Class Google::Apps::Card::V1::Columns::Column::Widgets (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:08.979395+00:00
---

# Google Chat V1 API - Class Google::Apps::Card::V1::Columns::Column::Widgets (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Columns-Column-Widgets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Class Google::Apps::Card::V1::Columns::Column::Widgets (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API class Google::Apps::Card::V1::Columns::Column::Widgets.

The supported widgets that you can include in a column.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend)

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #button_list
    
    
    def button_list() -> ::Google::Apps::Card::V1::ButtonList

**Returns**

  * ([::Google::Apps::Card::V1::ButtonList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ButtonList)) — [ButtonList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ButtonList "Google::Apps::Card::V1::ButtonList \(class\)") widget.

Note: The following fields are mutually exclusive: `button_list`, `text_paragraph`, `image`, `decorated_text`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #button_list=
    
    
    def button_list=(value) -> ::Google::Apps::Card::V1::ButtonList

**Parameter**

  * **value** ([::Google::Apps::Card::V1::ButtonList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ButtonList)) — [ButtonList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ButtonList "Google::Apps::Card::V1::ButtonList \(class\)") widget.

Note: The following fields are mutually exclusive: `button_list`, `text_paragraph`, `image`, `decorated_text`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::ButtonList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ButtonList)) — [ButtonList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ButtonList "Google::Apps::Card::V1::ButtonList \(class\)") widget.

Note: The following fields are mutually exclusive: `button_list`, `text_paragraph`, `image`, `decorated_text`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #chip_list
    
    
    def chip_list() -> ::Google::Apps::Card::V1::ChipList

**Returns**

  * ([::Google::Apps::Card::V1::ChipList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ChipList)) — [ChipList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ChipList "Google::Apps::Card::V1::ChipList \(class\)") widget.

Note: The following fields are mutually exclusive: `chip_list`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #chip_list=
    
    
    def chip_list=(value) -> ::Google::Apps::Card::V1::ChipList

**Parameter**

  * **value** ([::Google::Apps::Card::V1::ChipList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ChipList)) — [ChipList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ChipList "Google::Apps::Card::V1::ChipList \(class\)") widget.

Note: The following fields are mutually exclusive: `chip_list`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::ChipList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ChipList)) — [ChipList](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-ChipList "Google::Apps::Card::V1::ChipList \(class\)") widget.

Note: The following fields are mutually exclusive: `chip_list`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #date_time_picker
    
    
    def date_time_picker() -> ::Google::Apps::Card::V1::DateTimePicker

**Returns**

  * ([::Google::Apps::Card::V1::DateTimePicker](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DateTimePicker)) — [DateTimePicker](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DateTimePicker "Google::Apps::Card::V1::DateTimePicker \(class\)") widget.

Note: The following fields are mutually exclusive: `date_time_picker`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #date_time_picker=
    
    
    def date_time_picker=(value) -> ::Google::Apps::Card::V1::DateTimePicker

**Parameter**

  * **value** ([::Google::Apps::Card::V1::DateTimePicker](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DateTimePicker)) — [DateTimePicker](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DateTimePicker "Google::Apps::Card::V1::DateTimePicker \(class\)") widget.

Note: The following fields are mutually exclusive: `date_time_picker`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::DateTimePicker](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DateTimePicker)) — [DateTimePicker](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DateTimePicker "Google::Apps::Card::V1::DateTimePicker \(class\)") widget.

Note: The following fields are mutually exclusive: `date_time_picker`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #decorated_text
    
    
    def decorated_text() -> ::Google::Apps::Card::V1::DecoratedText

**Returns**

  * ([::Google::Apps::Card::V1::DecoratedText](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DecoratedText)) — [DecoratedText](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DecoratedText "Google::Apps::Card::V1::DecoratedText \(class\)") widget.

Note: The following fields are mutually exclusive: `decorated_text`, `text_paragraph`, `image`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #decorated_text=
    
    
    def decorated_text=(value) -> ::Google::Apps::Card::V1::DecoratedText

**Parameter**

  * **value** ([::Google::Apps::Card::V1::DecoratedText](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DecoratedText)) — [DecoratedText](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DecoratedText "Google::Apps::Card::V1::DecoratedText \(class\)") widget.

Note: The following fields are mutually exclusive: `decorated_text`, `text_paragraph`, `image`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::DecoratedText](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DecoratedText)) — [DecoratedText](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-DecoratedText "Google::Apps::Card::V1::DecoratedText \(class\)") widget.

Note: The following fields are mutually exclusive: `decorated_text`, `text_paragraph`, `image`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #image
    
    
    def image() -> ::Google::Apps::Card::V1::Image

**Returns**

  * ([::Google::Apps::Card::V1::Image](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Image)) — [Image](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Image "Google::Apps::Card::V1::Image \(class\)") widget.

Note: The following fields are mutually exclusive: `image`, `text_paragraph`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #image=
    
    
    def image=(value) -> ::Google::Apps::Card::V1::Image

**Parameter**

  * **value** ([::Google::Apps::Card::V1::Image](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Image)) — [Image](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Image "Google::Apps::Card::V1::Image \(class\)") widget.

Note: The following fields are mutually exclusive: `image`, `text_paragraph`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::Image](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Image)) — [Image](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Image "Google::Apps::Card::V1::Image \(class\)") widget.

Note: The following fields are mutually exclusive: `image`, `text_paragraph`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #selection_input
    
    
    def selection_input() -> ::Google::Apps::Card::V1::SelectionInput

**Returns**

  * ([::Google::Apps::Card::V1::SelectionInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput)) — [SelectionInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput "Google::Apps::Card::V1::SelectionInput \(class\)") widget.

Note: The following fields are mutually exclusive: `selection_input`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #selection_input=
    
    
    def selection_input=(value) -> ::Google::Apps::Card::V1::SelectionInput

**Parameter**

  * **value** ([::Google::Apps::Card::V1::SelectionInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput)) — [SelectionInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput "Google::Apps::Card::V1::SelectionInput \(class\)") widget.

Note: The following fields are mutually exclusive: `selection_input`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::SelectionInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput)) — [SelectionInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput "Google::Apps::Card::V1::SelectionInput \(class\)") widget.

Note: The following fields are mutually exclusive: `selection_input`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_input
    
    
    def text_input() -> ::Google::Apps::Card::V1::TextInput

**Returns**

  * ([::Google::Apps::Card::V1::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextInput)) — [TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextInput "Google::Apps::Card::V1::TextInput \(class\)") widget.

Note: The following fields are mutually exclusive: `text_input`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_input=
    
    
    def text_input=(value) -> ::Google::Apps::Card::V1::TextInput

**Parameter**

  * **value** ([::Google::Apps::Card::V1::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextInput)) — [TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextInput "Google::Apps::Card::V1::TextInput \(class\)") widget.

Note: The following fields are mutually exclusive: `text_input`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextInput)) — [TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextInput "Google::Apps::Card::V1::TextInput \(class\)") widget.

Note: The following fields are mutually exclusive: `text_input`, `text_paragraph`, `image`, `decorated_text`, `button_list`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_paragraph
    
    
    def text_paragraph() -> ::Google::Apps::Card::V1::TextParagraph

**Returns**

  * ([::Google::Apps::Card::V1::TextParagraph](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextParagraph)) — [TextParagraph](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextParagraph "Google::Apps::Card::V1::TextParagraph \(class\)") widget.

Note: The following fields are mutually exclusive: `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_paragraph=
    
    
    def text_paragraph=(value) -> ::Google::Apps::Card::V1::TextParagraph

**Parameter**

  * **value** ([::Google::Apps::Card::V1::TextParagraph](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextParagraph)) — [TextParagraph](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextParagraph "Google::Apps::Card::V1::TextParagraph \(class\)") widget.

Note: The following fields are mutually exclusive: `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::TextParagraph](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextParagraph)) — [TextParagraph](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextParagraph "Google::Apps::Card::V1::TextParagraph \(class\)") widget.

Note: The following fields are mutually exclusive: `text_paragraph`, `image`, `decorated_text`, `button_list`, `text_input`, `selection_input`, `date_time_picker`, `chip_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
