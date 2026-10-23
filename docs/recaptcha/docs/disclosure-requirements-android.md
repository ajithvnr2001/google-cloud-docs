---
url: https://docs.cloud.google.com/recaptcha/docs/disclosure-requirements-android/
title: Prepare for Google Play's data disclosure requirements \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:50.943979+00:00
---

# Prepare for Google Play's data disclosure requirements  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/disclosure-requirements-android/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Prepare for Google Play's data disclosure requirements Stay organized with collections  Save and categorize content based on your preferences. 

In May 2021, Google Play announced the new [Data safety section](https://android-developers.googleblog.com/2021/05/new-safety-section-in-google-play-will.html), which is a developer-provided disclosure for an app's data collection, sharing, and security practices. This document helps you complete the requirements for this data disclosure in regards to your usage of the reCAPTCHA Android SDK.

We aim to be as transparent as possible in supporting you. However, as the app developer, you are solely responsible for deciding how to respond to Google Play's [Data safety section form](https://support.google.com/googleplay/android-developer/answer/10787469) regarding your app's end-user data collection, sharing, and security practices.

## Data collected by Google Cloud Fraud Defense

Fraud Defense collects the following data automatically when it receives requests from the reCAPTCHA Android SDK:

Data | Description  
---|---  
IP address |  Collects IP addresses from the network requests coming from the reCAPTCHA Android SDK to help detect abuse.  
SDK version used by the app  | Collects version of the reCAPTCHA Android SDK that the app uses.  
Application package name | Collects package name of the application.  
User action string | Collects user actions from the app. For example, [`RecaptchaActionType.LOGIN`](https://developers.google.com/android/reference/com/google/android/gms/recaptcha/RecaptchaActionType#public-static-final-string-login).  
Device integrity response | Collects device integrity information from Google Play services.  
App interactions | Collects information about how a user interacts with the app. For example, the number of times they visit a page or sections they tap on.  
Installed apps | Collects information about some apps installed on a device, including malicious apps.  
Device ID | Collects identifiers that relate to an individual device, such as IMEI.  
  
For more information about the data collected by Fraud Defense, privacy policy, and terms, see the **Fraud Defense** section of **Service Terms** in [Service Specific Terms](https://cloud.google.com/terms/service-terms).

## Complete your data disclosure

  1. Determine which data type best describes the data collected by the reCAPTCHA Android SDK. To learn about the data types, see [Android's guide about data types](https://developer.android.com/guide/topics/data/collect-share).

  2. Fill out the Data safety form in Play Console. For instructions, see [Provide information for Google Play's Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469).




## What's next

  * [Integrate Fraud Defense with your Android apps](https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
