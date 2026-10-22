---
url: https://docs.cloud.google.com/recaptcha/docs/actions-mobile/
title: Action names \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:05.045507+00:00
---

# Action names  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/actions-mobile/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Action names Stay organized with collections  Save and categorize content based on your preferences. 

This document explains action names that are used to describe user-initiated events when integrating Google Cloud Fraud Defense on mobile applications.

You specify action names in the `action` parameter of `grecaptcha.enterprise.execute()` when integrating reCAPTCHA. We recommend using action names that are unique, meaningful, and not specific to users. Action names are not case-sensitive and they can only contain alphanumeric characters, slashes, and underscores. If you have a page with multiple applicable actions, you can concatenate multiple action strings together (for example, `cart_view_payment`).

Action names help you gain better visibility into how your users are using your site through Fraud Defense dashboards in the Google Cloud console.

The following table lists some recommended action names and examples of corresponding events. Using the recommended action names also allows Fraud Defense to associate user actions to page types, and improves the ability to monitor for different forms of attacks, such as attackers attempting to falsify or duplicate actions.

**Note:** Action names don't need to be confined to the following list, but we recommend applying these action names when appropriate.Action name | User initiated event  
---|---  
`registration` or `signup` | Register or sign up on the mobile application.  
`login` | Log in to the mobile application.  
`password_reset` | Request to reset the password.  
`get_price` | Fetch price for an item.  
`cart_add` | Add items to the cart.  
`cart_view` | View the contents of the cart.  
`payment_add` | Add or update payment information (e.g. card details or address).  
`checkout` | Check out from the mobile application.  
`transaction_confirmed` | Confirmation that a transaction was processed.  
`play_song` | Play a song from a list.  
  
## What's next

  * To learn about how action names are used for mobile applications, see the following: 
    * [Install reCAPTCHA keys on iOS](https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps)
    * [Install reCAPTCHA keys on Android](https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
