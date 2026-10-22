---
url: https://docs.cloud.google.com/identity-platform/docs/sign-in-user-phone/
title: Signing in users with a phone number on Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:27.624962+00:00
---

# Signing in users with a phone number on Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/sign-in-user-phone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with a phone number on Identity Platform

This document shows you how to use Identity Platform to sign in users with a phone number.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable Identity Platform. See the [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email) to learn how. 



## Enable phone sign-in for Identity Platform

  1. Go to the **Identity Providers** page.

[ Go to Identity Providers](https://console.cloud.google.com/customer-identity/providers)

  2. On the **Identity Providers** page, click **Add a provider**.

  3. In the **Select a provider** list, select phone **Phone**.

  4. Click the **Enabled** toggle to on.

  5. To save the provider settings, click **Save**.




## Configure phone sign-in for your app platform

If you are using Identity Platform for Apple, Android, or web platforms, you must also configure your app from the Firebase console.

  * For Apple platforms:

    * Enable phone number sign-in for your Firebase project.
    * Enable app verification with silent push notifications.

For instructions, see [Authenticate with Firebase on Apple platforms using a phone number](https://firebase.google.com/docs/auth/ios/phone-auth).

  * For Android platforms:

    * Enable phone number sign-in for your Firebase project.
    * Enable app verification with the Play Integrity API.

For instructions, see [Authenticate with Firebase on Android using a phone number](https://firebase.google.com/docs/auth/ios/phone-auth).

  * For web platforms:

    * Enable phone number sign-in for your Firebase project.
    * Set up the reCAPTCHA verifier.

For instructions, see [Authenticate with Firebase with a phone number using JavaScript](https://firebase.google.com/docs/auth/web/phone-auth).


**Caution:** SMS authentication flows are common targets for attacks like SMS pumping and toll fraud, which can lead to unexpected charges. To protect your project, we strongly recommend configuring an explicit SMS region policy that restricts traffic to your specific operating regions. For additional defense against bots and automated attacks, consider enabling [reCAPTCHA SMS defense](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp) and configuring an [SMS region policy](https://docs.cloud.google.com/identity-platform/docs/admin/sms-regions). 

## What's Next

  * Learn how to [register test phone numbers](https://docs.cloud.google.com/identity-platform/docs/test-phone-numbers) for development purposes.
  * Learn how to [use SMS regions to restrict Identity Platform SMS verification usage](https://cloud.google.com/identity-platform/docs/admin/sms-regions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
