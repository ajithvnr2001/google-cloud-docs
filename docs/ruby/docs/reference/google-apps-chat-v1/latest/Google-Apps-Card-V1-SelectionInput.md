---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput/
title: Google Chat V1 API - Class Google::Apps::Card::V1::SelectionInput (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:21.156076+00:00
---

# Google Chat V1 API - Class Google::Apps::Card::V1::SelectionInput (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Class Google::Apps::Card::V1::SelectionInput (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API class Google::Apps::Card::V1::SelectionInput.

A widget that creates one or more UI items that users can select. Supports form submission validation for `dropdown` and `multiselect` menus only. When `Action.all_widgets_are_required` is set to `true` or this widget is specified in `Action.required_widgets`, the submission action is blocked unless a value is selected. For example, a dropdown menu or checkboxes. You can use this widget to collect data that can be predicted or enumerated. For an example in Google Chat apps, see [Add selectable UI elements](https://docs.cloud.google.com/workspace/chat/design-interactive-card-dialog#add_selectable_ui_elements).

Chat apps can process the value of items that users select or input. For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data).

To collect undefined or abstract data from users, use the [TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-TextInput "Google::Apps::Card::V1::TextInput \(class\)") widget.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #external_data_source
    
    
    def external_data_source() -> ::Google::Apps::Card::V1::Action

**Returns**

  * ([::Google::Apps::Card::V1::Action](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Action)) — An external data source, such as a relational database.

Note: The following fields are mutually exclusive: `external_data_source`, `platform_data_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #external_data_source=
    
    
    def external_data_source=(value) -> ::Google::Apps::Card::V1::Action

**Parameter**

  * **value** ([::Google::Apps::Card::V1::Action](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Action)) — An external data source, such as a relational database.

Note: The following fields are mutually exclusive: `external_data_source`, `platform_data_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::Action](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Action)) — An external data source, such as a relational database.

Note: The following fields are mutually exclusive: `external_data_source`, `platform_data_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #items
    
    
    def items() -> ::Array<::Google::Apps::Card::V1::SelectionInput::SelectionItem>

**Returns**

  * (::Array<[::Google::Apps::Card::V1::SelectionInput::SelectionItem](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-SelectionItem)>) — An array of selectable items. For example, an array of radio buttons or checkboxes. Supports up to 100 items. 



### #items=
    
    
    def items=(value) -> ::Array<::Google::Apps::Card::V1::SelectionInput::SelectionItem>

**Parameter**

  * **value** (::Array<[::Google::Apps::Card::V1::SelectionInput::SelectionItem](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-SelectionItem)>) — An array of selectable items. For example, an array of radio buttons or checkboxes. Supports up to 100 items. 



**Returns**

  * (::Array<[::Google::Apps::Card::V1::SelectionInput::SelectionItem](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-SelectionItem)>) — An array of selectable items. For example, an array of radio buttons or checkboxes. Supports up to 100 items. 



### #label
    
    
    def label() -> ::String

**Returns**

  * (::String) — The text that appears above the selection input field in the user interface.

Specify text that helps the user enter the information your app needs. For example, if users are selecting the urgency of a work ticket from a drop-down menu, the label might be "Urgency" or "Select urgency". 




### #label=
    
    
    def label=(value) -> ::String

**Parameter**

  * **value** (::String) — The text that appears above the selection input field in the user interface.

Specify text that helps the user enter the information your app needs. For example, if users are selecting the urgency of a work ticket from a drop-down menu, the label might be "Urgency" or "Select urgency". 




**Returns**

  * (::String) — The text that appears above the selection input field in the user interface.

Specify text that helps the user enter the information your app needs. For example, if users are selecting the urgency of a work ticket from a drop-down menu, the label might be "Urgency" or "Select urgency". 




### #multi_select_max_selected_items
    
    
    def multi_select_max_selected_items() -> ::Integer

**Returns**

  * (::Integer) — For multiselect menus, the maximum number of items that a user can select. Minimum value is 1 item. If unspecified, defaults to 3 items. 



### #multi_select_max_selected_items=
    
    
    def multi_select_max_selected_items=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — For multiselect menus, the maximum number of items that a user can select. Minimum value is 1 item. If unspecified, defaults to 3 items. 



**Returns**

  * (::Integer) — For multiselect menus, the maximum number of items that a user can select. Minimum value is 1 item. If unspecified, defaults to 3 items. 



### #multi_select_min_query_length
    
    
    def multi_select_min_query_length() -> ::Integer

**Returns**

  * (::Integer) — 

For multiselect menus, the number of text characters that a user inputs before the menu returns suggested selection items.

If unset, the multiselect menu uses the following default values:

    * If the menu uses a static array of `SelectionInput` items, defaults to 0 characters and immediately populates items from the array.
    * If the menu uses a dynamic data source (`multi_select_data_source`), defaults to 3 characters before querying the data source to return suggested items.



### #multi_select_min_query_length=
    
    
    def multi_select_min_query_length=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — 

For multiselect menus, the number of text characters that a user inputs before the menu returns suggested selection items.

If unset, the multiselect menu uses the following default values:

    * If the menu uses a static array of `SelectionInput` items, defaults to 0 characters and immediately populates items from the array.
    * If the menu uses a dynamic data source (`multi_select_data_source`), defaults to 3 characters before querying the data source to return suggested items.



**Returns**

  * (::Integer) — 

For multiselect menus, the number of text characters that a user inputs before the menu returns suggested selection items.

If unset, the multiselect menu uses the following default values:

    * If the menu uses a static array of `SelectionInput` items, defaults to 0 characters and immediately populates items from the array.
    * If the menu uses a dynamic data source (`multi_select_data_source`), defaults to 3 characters before querying the data source to return suggested items.



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name that identifies the selection input in a form input event.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data). 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name that identifies the selection input in a form input event.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data). 




**Returns**

  * (::String) — Required. The name that identifies the selection input in a form input event.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data). 




### #on_change_action
    
    
    def on_change_action() -> ::Google::Apps::Card::V1::Action

**Returns**

  * ([::Google::Apps::Card::V1::Action](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Action)) — If specified, the form is submitted when the selection changes. If not specified, you must specify a separate button that submits the form.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data). 




### #on_change_action=
    
    
    def on_change_action=(value) -> ::Google::Apps::Card::V1::Action

**Parameter**

  * **value** ([::Google::Apps::Card::V1::Action](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Action)) — If specified, the form is submitted when the selection changes. If not specified, you must specify a separate button that submits the form.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data). 




**Returns**

  * ([::Google::Apps::Card::V1::Action](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-Action)) — If specified, the form is submitted when the selection changes. If not specified, you must specify a separate button that submits the form.

For details about working with form inputs, see [Receive form data](https://developers.google.com/workspace/chat/read-form-data). 




### #platform_data_source
    
    
    def platform_data_source() -> ::Google::Apps::Card::V1::SelectionInput::PlatformDataSource

**Returns**

  * ([::Google::Apps::Card::V1::SelectionInput::PlatformDataSource](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-PlatformDataSource)) — A data source from Google Workspace.

Note: The following fields are mutually exclusive: `platform_data_source`, `external_data_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #platform_data_source=
    
    
    def platform_data_source=(value) -> ::Google::Apps::Card::V1::SelectionInput::PlatformDataSource

**Parameter**

  * **value** ([::Google::Apps::Card::V1::SelectionInput::PlatformDataSource](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-PlatformDataSource)) — A data source from Google Workspace.

Note: The following fields are mutually exclusive: `platform_data_source`, `external_data_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Apps::Card::V1::SelectionInput::PlatformDataSource](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-PlatformDataSource)) — A data source from Google Workspace.

Note: The following fields are mutually exclusive: `platform_data_source`, `external_data_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #type
    
    
    def type() -> ::Google::Apps::Card::V1::SelectionInput::SelectionType

**Returns**

  * ([::Google::Apps::Card::V1::SelectionInput::SelectionType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-SelectionType)) — The type of items that are displayed to users in a `SelectionInput` widget. Selection types support different types of interactions. For example, users can select one or more checkboxes, but they can only select one value from a dropdown menu. 



### #type=
    
    
    def type=(value) -> ::Google::Apps::Card::V1::SelectionInput::SelectionType

**Parameter**

  * **value** ([::Google::Apps::Card::V1::SelectionInput::SelectionType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-SelectionType)) — The type of items that are displayed to users in a `SelectionInput` widget. Selection types support different types of interactions. For example, users can select one or more checkboxes, but they can only select one value from a dropdown menu. 



**Returns**

  * ([::Google::Apps::Card::V1::SelectionInput::SelectionType](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Card-V1-SelectionInput-SelectionType)) — The type of items that are displayed to users in a `SelectionInput` widget. Selection types support different types of interactions. For example, users can select one or more checkboxes, but they can only select one value from a dropdown menu. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
