---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-avatar/
title: Custom and default agent avatars \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:29.487780+00:00
---

# Custom and default agent avatars  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-avatar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Custom and default agent avatars Stay organized with collections  Save and categorize content based on your preferences. 

CCAI Platform mobile and web SDKs allow for an image to be displayed when interacting with agents using chat or voice calls. The avatar can be set by an administrator or each user can set their own avatar.

Avatar are images that are uploaded but need to be of a certain specification.

  * Images must be PNG or JPG, 512px square or larger.



## Agent avatar visibility

The visibility of the agent avatar is specific to the SDK being used:

  * For mobile SDK, avatar are displayed:

    * During chat sessions.

    * On call sessions.

    * Rating screen.

  * For web SDK, avatar are displayed:

    * During chat sessions.



## Administrator configuration

Administrators can set a default image for all avatars in the environment and choose if that image is locked and can't be changed.

### Adding a default avatar

A default avatar can be configured. To configure a default:

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. Navigate to the Default Avatar section.

  3. Click **Choose Image**.

  4. Select an image file, 

  5. Adjust image and click **Crop**.

  6. If you would like to lock the default avatar and overwrite any custom images that users have uploaded, click **Overwrite all other uploaded Avatars with default.** "

  7. Click **Save avatar setting** to save your changes.




## Agent - custom avatar upload

Based on administrator configured settings, the option for a user to upload their own avatar may or may be available.

  1. From the CCAI Platform portal, click the avatar in the upper-right.

  2. Click **My Profile**.

  3. Click the **Choose file** button.

  4. Adjust the image as needed in the edit screen.

  5. Click **Crop** to save the image selection.

  6. Click Upload Image to save.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
