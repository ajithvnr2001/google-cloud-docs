---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/implement-user-events/
title: Implement user events \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:00.386890+00:00
---

# Implement user events  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/implement-user-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Implement user events Stay organized with collections  Save and categorize content based on your preferences. 

To configure your user events:

  1. Import [historical user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events).

  2. Record [live user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events).

  3. Tag user events [with entities](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/entities).

  4. Flag user events with [attribution tokens](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events#attribution-tokens).




## User information

The `visitorId` value represents the unique user identifier. It's required when you record a user event. ([`UserInfo`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#userinfo)) is included when you record a user event that has the `visitorId` value and, if available, the `userId` value. 

You can use the optional `userId` value as a unique, persistent identifier for a user across devices whenever a user signs in to your site. When you record the `userId` for a user, AI Commerce Search can generate more personalized results for one user across multiple devices, such as a mobile device and web browser.

**Note:** Use a secure form of a unique identifier to keep users anonymous to AI Commerce Search and protect your users' privacy. You are responsible for redacting PII (personally identifiable information), such as email or home addresses, from your data. 

## User event timestamp

When you record a user event, be sure to include an accurate timestamp of when the event occurred. Accurate timestamps ensure that events are stored in the correct order. Timestamps are recorded automatically for events collected using Tag Manager and the JavaScript Pixel. When you import events, you must provide the timestamp in the [`eventTime`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.event_time) field in the format specified by [RFC 3339](https://tools.ietf.org/html/rfc3339).

## Custom attributes for user events

You can include additional custom attributes and features for user events. This can result in improved, more specific recommendations for your users when you use recommendations. To add custom attributes, use [`attributes`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.attributes) when you record a user event.

If you provide custom attributes for ingested user events, it's important to also include them in the user events that you associate with prediction requests. The formatting of custom attributes must be consistent between imported events and events provided with prediction requests. This enables use of those custom attributes when training models and serving predictions, which helps improve recommendation quality.

You can provide custom text values by using the `text` field, or custom numerical values by using the `number` field.

For example, the following shows the `attributes` section from a request to record a user event:
    
    
    "attributes": {
      "user_age": {"text": ["teen", "young adult"]},
      "user_location": {"text": ["CA"]}
    }

## Monitor import health

Recording user events successfully is important for getting high-quality results. You should monitor the event recording error rates and take action if needed. For more information, see [Setting up alerts for data upload issues](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
