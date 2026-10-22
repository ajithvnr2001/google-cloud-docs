---
url: https://docs.cloud.google.com/identity-platform/docs/admin/sms-regions/
title: Use SMS regions to protect your app from SMS abuse \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:25.210271+00:00
---

# Use SMS regions to protect your app from SMS abuse  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/admin/sms-regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use SMS regions to protect your app from SMS abuse

This guide shows you how to use SMS regions to restrict Identity Platform SMS verification usage and view usage metrics.

## Overview of SMS regions

SMS regions is an Identity Platform feature you can use to protect your apps from SMS abuse.

SMS abuse typically happens when a malicious actor causes a service to send SMS through a carrier that they have a revenue sharing agreement with. SMS abuse can lead to higher costs and damage your product's reputation with customers.

Because Identity Platform allows SMS phone authorizations, SMS abuse can occur.

The SMS regions feature lets you set which regions can receive SMS phone authorizations.

The feature provides the following:

  * A Firebase console interface for you to set up your SMS region policy.
  * An API for you to set up your SMS region policy.
  * Metrics that can inform your decision to use an SMS region policy.

**Important:** For projects with multi-tenancy enabled, you must configure the SMS region policy for each tenant individually. Project-level policies don't apply to tenants.

## Set a region policy

This section describes an Identity Platform region policy. You can set up the following types of policies, and only one can be active:

  * **Allowlist-only:** only the regions that you specify in an allowlist can receive phone authorization requests.
  * **Denylist-only:** all regions can receive phone authorization requests except the ones you specify in a denylist.



After you change the configuration, the system immediately starts to enforce the policy. It blocks phone authorization requests from the regions that are disallowed by the policy based on the region code of the phone number.

**Important:** To protect your project from SMS abuse, we strongly recommend configuring an explicit SMS region policy that limits traffic to your specific operating regions. For additional protection against SMS abuse from bots and automated attacks, consider enabling [reCAPTCHA SMS defense](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp). 

### Allowlist-only policy

To set up an allowlist-only policy, follow these steps:

### Firebase console

  1. In the Firebase console, go to the **Firebase Auth Settings** page.

[Go to Firebase Auth settings](https://console.firebase.google.com/project/_/authentication/settings)

     1. Select **SMS region policy** in the navigation pane.

     2. Select **Allow**.

     3. Click **Select regions**.

  2. Add only regions where you plan to send SMS messages. Regions not on the list are blocked.

  3. Click **Save**.

You can configure either an allowlist or a denylist but not both. Doing so overwrites any previous configuration.




### Identity Toolkit API

  1. In the Google Cloud console, to print an access token for your project, run the following command:
         
         gcloud auth print-access-token --project=PROJECT_ID
         

  2. Update your project configuration to include your new policy using the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig):
         
         curl -X PATCH -d "{'sms_region_config':{'allowlist_only':{'allowed_regions':['REGION_LIST']}}}" \
         -H 'Authorization: Bearer ACCESS_TOKEN' \
         -H 'Content-Type: application/json' \
         'https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/config?updateMask=sms_region_config'</span>
         




Replace the following:

  * `ACCESS_TOKEN`: the access token you generated earlier.
  * `REGION_LIST`: one or more regions, for example, `IN` or `US`. To limit abuse, we recommend that you only allow the regions where you plan to send SMS messages.
  * `PROJECT_ID`: your project ID.



You must provide an [update mask](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig#query-parameters) to prevent other fields from being changed.

### Denylist-only policy

To set up a denylist-only policy, follow these steps:

### Firebase Console

  1. In the Firebase console, go to the **Firebase Auth Settings** page and select **SMS region policy** in the navigation pane.

[Go to Firebase Auth settings](https://console.firebase.google.com/project/_/authentication/settings)

     1. Select **Deny**.

     2. Click **Select regions**.

  2. Add any regions that you want to block sending SMS messages to. Regions not on the list will be allowed. For stronger abuse protection, we recommend using an allowlist-only policy and disabling all regions in which you don't plan to send SMS messages.

  3. Click **Save**.

You can configure either an allowlist or a denylist but not both. Doing so overwrites any previous configuration.




### Identity Toolkit API

  1. In the Google Cloud console, to print an access token for your project, run the following command:
         
         gcloud auth print-access-token --project=PROJECT_ID
         

  2. Update your project configuration to include your new policy using the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig):
         
         curl -X PATCH -d "{'sms_region_config':{'allow_by_default':{'disallowed_regions':['REGION_LIST']}}}" \
         -H 'Authorization: Bearer ACCESS_TOKEN' \
         -H 'Content-Type: application/json' \
         'https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/config?updateMask=sms_region_config'</span>
         




Replace the following:

  * `ACCESS_TOKEN`: the access token you generated earlier.
  * `REGION_LIST`: one or more regions, for example, `IN` or `US`.
  * `PROJECT_ID`: your project ID.



You must provide an [update mask](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig#query-parameters) to prevent other fields from being changed.

## Access regional SMS use metrics

This section describes how to view SMS use metrics.

To view the metrics, do the following:

  1. In the Google Cloud console, Go to the **Metrics explorer** page in Cloud Monitoring:

[Go to Cloud Monitoring](https://console.cloud.google.com/monitoring/metrics-explorer).

  2. Select the following fields:

     * identitytoolkit.googleapis.com/usage/sent_sms_count,
     * identitytoolkit.googleapis.com/usage/blocked_sms_count, and
     * firebaseauth.googleapis.com/phone_auth/phone_verification_count.

Note that the metrics have a field region_code. You use this code to view the regions that receive SMS authorizations.

  3. Compute the verification success rate as `verification_success_rate = phone_verification_count/sent_sms_count`, in a particular region. Typically, verification success rates above 75% are considered acceptable.




A low `verification_success_rate` can indicate abuse, especially in a region in which you wouldn't expect to have users. Typically, verification success rates below 75% are considered low.

If you suspect SMS abuse, you can set a region policy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
