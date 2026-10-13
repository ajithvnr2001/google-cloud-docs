---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-ActionResponse-ResponseType/
title: Google Chat V1 API - Module Google::Apps::Chat::V1::ActionResponse::ResponseType (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:28.146813+00:00
---

# Google Chat V1 API - Module Google::Apps::Chat::V1::ActionResponse::ResponseType (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-ActionResponse-ResponseType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Module Google::Apps::Chat::V1::ActionResponse::ResponseType (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API module Google::Apps::Chat::V1::ActionResponse::ResponseType.

The type of Chat app response.

## Constants 

### TYPE_UNSPECIFIED

**value:** 0  
Default type that's handled as `NEW_MESSAGE`.

### NEW_MESSAGE

**value:** 1  
Post as a new message in the topic.

### UPDATE_MESSAGE

**value:** 2  
Update the Chat app's message. This is only permitted on a `CARD_CLICKED` event where the message sender type is `BOT`.

### UPDATE_USER_MESSAGE_CARDS

**value:** 6  
Update the cards on a user's message. This is only permitted as a response to a `MESSAGE` event with a matched url, or a `CARD_CLICKED` event where the message sender type is `HUMAN`. Text is ignored.

### REQUEST_CONFIG

**value:** 3  
Privately ask the user for additional authentication or configuration.

### DIALOG

**value:** 4  
Presents a [dialog](https://developers.google.com/workspace/chat/dialogs).

### UPDATE_WIDGET

**value:** 7  
Widget text autocomplete options query.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
