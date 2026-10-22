---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-actions-in-session/
title: SmartActions \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:34.003971+00:00
---

# SmartActions  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-actions-in-session/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  SmartActions Stay organized with collections  Save and categorize content based on your preferences. 

Consumers calling or initiating a chat can share photos, videos, and screenshots with agents to get on the same page fast. By prompting the consumer to send the requested media, there's no more need for walking them through each step just to send the media, and the media is captured, then immediately available to the agent.

## Using SmartActions with Mobile SDK calls

  1. **Actions menu** : Click to bring up smart action options

  2. **Get Verification** : Asks the consumer to verify using fingerprint or PIN code they use to unlock their mobile device. This can be used as a security measure to verify ownership of the product or device in question.

  3. **Request Photos** : Prompts caller to take or select up to 4 photos. They will need to grant camera or photo access for your app.

_Example use case_ : Product arrived broken, the consumer can send photos of the damaged item.

  4. **Request Screenshots** : Prompts caller to take a screenshot of the current page in the app.

**Process Note** : Since this prompts the consumer to take and send a screenshot of the current page, guide them to the part of the app that you would want to view a screenshot of before initiating the screenshot request.

_Example use case_ : Consumer receiving an error on a certain page

  5. **Request Videos** : Prompts caller to select an existing video or to take a new video.

_Example use case_ : Consumer sends a video showing their current product setup that would be hard to describe.

  6. **Get Text Input** : Prompts consumers to type in information using their mobile device keyboard.

_Example use case:_ Consumer can correctly send their tracking #, email, or a correct spelling of their last name.

  7. **Redact** : When enabled, agents can initiate call redaction to pause recording a call. See Call Redaction.

_Example use case:_ Consumer is sharing sensitive information such as credit card details or social security information.

**Note:** If using call redaction, click the red bar when call recording should resume.




## SmartActions for Mobile SDK chat

  1. **Actions menu** : Click to bring up smart action options

  2. **Get Verification** : Asks the consumer to verify using fingerprint or PIN code they use to unlock their mobile device. This can be used as a security measure to verify ownership of the product or device in question.

  3. **Request Photos** : Prompts caller to take or select up to 4 photos. They will need to grant camera or photo access for your app.

_Example use case_ : Product arrived broken, the consumer can send photos of the damaged item.

  4. **Request Screenshots** : Prompts caller to take a screenshot of the current page in the app.

**Process Note** : Since this prompts the caller to take and send a screenshot of the current page, guide them to the part of the app that you would want to view a screenshot of before initiating the screenshot request.

_Example use case_ : Consumer receiving an error on a certain page

  5. **Request Videos** : Prompts caller to select an existing video or to take a new video.

_Example use case_ : Consumer sends a video showing their current product setup that would be hard to describe.




## Using SmartActions for Web SDK Chats

While the same flow of prompting the consumer to take an action like send a photo or video is not available for Web SDK chat, consumers can still add image attachments.

While chatting, direct the chat participant to click the paperclip icon and they will be prompted to select and attach a file. Accepted file types are .png, .jpg, and mp4.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
