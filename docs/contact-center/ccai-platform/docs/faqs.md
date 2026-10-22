---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/faqs/
title: FAQs \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:06.766370+00:00
---

# FAQs  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/faqs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  FAQs Stay organized with collections  Save and categorize content based on your preferences. 

The following are some frequently asked questions pertaining to the configuration and use of CCAI Platform.

## Authentication FAQs

The following are frequently asked questions pertaining to authentication.

### Does the SDK make the call to authenticate or does it come from Contact Center AI Platform (CCAI Platform) service?

CCAI Platform provides `company_id` and `company_secret` to the host app server. These are found in the administrator portal under **Settings > developer**.

When the end-user signs into the host app, CCAI Platform asks to the host app to sign the payload. The host app signs the payload using the `company_secret` and generates a signed JWT that is used by CCAI Platform to authenticate the end-user. `POST /auth/end_user`

CCAI Platform verifies signed JWT and issues the auth token for the end-user. If the end-user of an identifier doesn't exist in CCAI Platform DB, create it. If the device of `device_token` doesn't exist, create it.

### How do we generate a push token for CCAI Platform if the user isn't logged in?

Push tokens aren't required for user authentication.

### Can CCAI Platform consume my company's generated tokens for authentication rather than using the service callback to authenticate?

Yes, you can use your own authentication system and you're encouraged to do so. The end-user identification should be in the payload. How this works is the end user authenticates and this is recognized on your server. Then your server sends this info to CCAI Platform. If your server doesn't know who the end user is, we'll think it's anonymous and show it as such—for example, "Web user" instead of the customer's actual name.

### Is it possible to run initialize chat client as a standalone activity?

It isn't possible to run initialize chat client as a standalone activity.

## iOS or Android integration FAQ

The following are frequently asked questions pertaining to the CCAI Platform mobile SDK.

### How do I set up on iOS without using cocoapods?

You'll need to install the file `ManualInstallationGuide.md` to set up the iOS without using cocoapods. You can find this in the iOS SDK.

TBD: Where in the iOS SDK? What about for Android?

## Web SDK integration FAQ

The following are frequently asked questions pertaining to the web SDK.

### Is there a way to move the CCAI Platform chat bubble icon so that it isn't being covered up by other elements of my webpage?

If implemented, the web SDK styling might have a lower z-index than your other elements that are covering it, or they may have the same z index but coded after these other items, making it hide behind it.

## API FAQs

The following are frequently asked questions pertaining to the CCAI Platform APIs.

### How long will my company's data be available using the API?

APIs can be accessed historically with no time limit.

### What is the interval in which I can access current information?

Our APIs can be accessed in real-time as the data is compiled at the time it's called.

### What is the recommended interval to poll data?

Since the APIs are GETs, best practice is to poll every 7 mins or 15 minutes.

### What is the rate limit?

Up to **10** calls per second.

## Data FAQs

The following are frequently asked questions pertaining to the use of CCAI Platform generated data.

### Is the SLA of the call or chat available or does that need to be calculated based on the metrics in the response?

SLA isn't in the response. It is something that will need to be identified and calculated.

### Can we report on the number of times, or the duration of time, that a specific agent puts a caller on hold?

In the `participants` object of the response there is an entry for `end_user` (the consumer) with a `hold_duration` value. That is the total hold duration the end-user experienced while on the call.

### Can we distinguish between warm and cold transfers?

Not at this time.

### Why is the call duration at the top of the response different from the call duration reported for the `end_user` under `participants`?

The current `call_duration` is represented as the difference of the call `connected_at` value and `finished_at` value. It isn't a value that represents the actual handle duration. Handle Duration can be obtained from the `handle_durations` object of the response. The sum of `call_duration` in each of those response objects plus the `acw_duration` would represent the total handle time of the call.

## General FAQ

The following are general frequently asked questions.

### What is the limit to the size or time length of a video?

CRMs like Zendesk have a video size limitation that caps at 20MB. If the video is larger than this, the end user is alerted that their file is too big.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
