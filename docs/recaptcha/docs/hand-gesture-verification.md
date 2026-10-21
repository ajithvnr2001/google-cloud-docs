---
url: https://docs.cloud.google.com/recaptcha/docs/hand-gesture-verification/
title: Hand gesture verification \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:33.961237+00:00
---

# Hand gesture verification  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/hand-gesture-verification/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Hand gesture verification Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about data collection, camera permissions, and accessibility for hand gesture verification.

## Data collection and storage

When the hand gesture feature is enabled, Google Cloud Fraud Defense collects the following data:

  * Google analyzes one or more videos of a user's hand as they perform various actions or gestures. The video is processed to extract hand landmark data, which includes [21 hand-knuckle coordinates](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker).
  * The videos are never associated with a user's identity and are deleted after the verification process. Audio is never recorded.



### Additional data storage

  * Google does not retain any images or videos of a user's hand gestures beyond the verification process or use the data for any other purpose. Videos or images are automatically deleted after the challenge is complete.
  * The information Google collects is used and stored in accordance with the [Google Privacy Policy](https://policies.google.com/privacy).



## Permissions

Hand gesture challenges require permission to access a user's camera. After the user consents to perform hand gestures, Google receives camera permissions, and users can manage these permissions in their browser settings at any time. Google processes hand gesture videos for the sole purpose of security verification and does not transfer any related data or permissions to third parties.

## Accessibility

For users with accessibility needs who cannot use hand gestures to complete the challenge, Fraud Defense continues to provide visual and audio challenges, and develop more accessible and secure alternatives.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
