---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/rich-messaging/
title: Configure rich messaging and file attachments \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:59.137526+00:00
---

# Configure rich messaging and file attachments  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/rich-messaging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure rich messaging and file attachments Stay organized with collections  Save and categorize content based on your preferences. 

You can configure CCAI Platform so that agents can use rich messaging, emoji, and file attachments in the chat adapter. Rich formatting and emoji are available in [chat shortcuts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-shortcuts) and in [Customize mobile and web SDK channel messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/customize-mobile-web-messages) without any special configuration. Rich formatting is not available for SMS chats.

## Configure rich messaging and file attachments for the chat adapter

To configure rich messaging and file attachments for the chat adapter, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Chat**.

  2. In the **Global Chat Settings** pane, for **Rich Messaging** , select the required options from the following:

     * **Allow agents to attach files**

     * **Allow agents to format messages (e.g. bold, italicize, create lists)**

     * **Allow agents to use emojis**.

  3. Click **Save Global Chat Settings**.




## File attachment limitations

This section describes file attachment limitations.

### Allowed file types

The following table shows the file types that agents can attach to messages in the chat adapter.

Image | Video | Audio | Document  
---|---|---|---  
JPEG, JPG, PNG, GIF, WebP | MP4, MOV, AVI, WMV, WebM | MP3, WAV, M4A, WEBA | PDF, DOC, XLS, PPT, CSV, TXT  
  
### File size limits

The following table shows size limits for files that agents can attach to messages in the chat adapter.

| Image | Video | Audio | Document  
---|---|---|---|---  
**Chat adapter** | 100 MB | 100 MB | 100 MB | 100 MB  
**Web SDK** | 20 MB | 20 MB | N/A | N/A  
**Mobile SDKs** | 2 MB | 20 MB | N/A | N/A  
  
For the mobile SDKs, if you attach an image or video file larger than the limit shown in this table, the file is compressed to within the limit. This could reduce the quality of the image or video.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
