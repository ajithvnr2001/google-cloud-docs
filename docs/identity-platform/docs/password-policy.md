---
url: https://docs.cloud.google.com/identity-platform/docs/password-policy/
title: Enable, disable, and use password policies \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:22.498488+00:00
---

# Enable, disable, and use password policies  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/password-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable, disable, and use password policies

This document shows you how to set password policies to improve password strength for new and existing users.

If you want to set a password policy from the Firebase console, see [Set a password policy](https://firebase.google.com/docs/auth/android/password-auth#policy).

## Overview

With password policies, you can improve account security by enforcing password complexity requirements. Password policies support the following password requirements:

  * Lowercase character required
  * Uppercase character required
  * Numeric character required
  * Non-alphanumeric character required
  * Minimum password length (ranges from 6 to 30 characters; defaults to 6)
  * Maximum password length (maximum length of 4096 characters)



The following characters satisfy the non-alphanumeric character requirement if configured:

`^ $ * . [ ] { } ( ) ? " ! @ # % & / \ , > < ' : ; | _ ~ ``

## Enforcement modes

You can enable password policy enforcement in two modes:

  * Require: Attempts to sign up fail until the user updates to a password that complies with your policy.
  * Notify: Users are allowed to sign up with a non-compliant password. Any missing criteria needed to satisfy the policy are returned. Criteria returned include:

    * `MISSING_LOWERCASE_CHARACTER`
    * `MISSING_UPPERCASE_CHARACTER`
    * `MISSING_NUMERIC_CHARACTER`
    * `MISSING_NON_ALPHANUMERIC_CHARACTER`
    * `MINIMUM_PASSWORD_LENGTH`
    * `MAXIMUM_PASSWORD_LENGTH`
**Note:** Password criteria parameters are not available in the client SDK. For information about validating passwords using the client SDK, see Enforcing on the client side.

You can send this information to the user to inform them to update their password. The following example shows a response containing missing password criteria:
    
    {
      "kind": "identitytoolkit#VerifyPasswordResponse",
      "localId": "CJL1i2",
      "email": "cloudysanfrancisco@gmail.com",
      "displayName": "",
      "idToken": "ID_TOKEN",
      "registered": true,
      "userNotifications": [
        {
          "notificationCode": "MISSING_NUMERIC_CHARACTER",
          "notificationMessage": "Password must contain a numeric character"
        },
        {
          "notificationCode": "MISSING_NON_ALPHANUMERIC_CHARACTER",
          "notificationMessage": "Password must contain a non-alphanumeric character"
        }
      ]
    }
    




New users are required to choose a password that complies with your policy. If you have active users, we recommend not enabling force upgrade on sign in unless you intend to immediately enforce the password policy. Instead, use notify mode, which allows users to sign in with their current passwords and sends notifications that detail the requirements their password lacks.

When you enable enforcement, set `forceUpgradeOnSignin` to `true` to enable enforcement in require mode. Set it to `false` to enable enforcement in notify mode.

## Enable enforcement

To enforce a password policy, follow these steps:

  1. If you haven't already done so, configure [email and password sign-in](https://docs.cloud.google.com/identity-platform/docs/quickstart-email-password).
  2. To enforce a password policy at the project level, follow these steps:

###  Firebase console 

     1. In the Firebase console, go to the **Authentication Settings** page.

[Go to Authentication Settings](https://console.firebase.google.com/project/_/authentication/settings)

     2. Select the **Password policy** tab.

     3. Configure your selected password strength requirements.

     4. Choose your enforcement mode (**Require** or **Notify**) and whether to force password upgrades on sign-in.

     5. Click **Save**.

###  REST 

     1. In the Google Cloud console, print an access token for your project ID using the [`gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token):
            
            gcloud auth print-access-token --project=PROJECT_ID
            

     2. Enable a password policy using the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig):
            
            curl -X PATCH -d "{'passwordPolicyConfig':{'enforcementState':'ENFORCE','forceUpgradeOnSignin':true,'constraints':{'requireUppercase':true,'requireLowercase':true,'requireNonAlphanumeric':true,'requireNumeric':true,'minLength':MIN_PASSWORD_LENGTH,'maxLength':MAX_PASSWORD_LENGTH}}}" \
                -H 'Authorization: Bearer ACCESS_TOKEN' \
                -H 'Content-Type: application/json' \
                -H 'X-Goog-User-Project: PROJECT_ID' \
                "https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/config?updateMask=passwordPolicyConfig"
            

Replace the following:

        * `ACCESS_TOKEN`: the access token that you generated earlier
        * `PROJECT_ID`: your project ID
        * `MIN_PASSWORD_LENGTH`: the minimum required password length
        * `MAX_PASSWORD_LENGTH`: the maximum required password length

  3. To enforce a password policy at the tenant level, follow these steps:

**Note:** Tenant-level password policies are not supported in the Firebase console.

###  REST 

     1. In the Google Cloud console, print an access token for your project ID using the [`gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token):
            
            gcloud auth print-access-token --project=PROJECT_ID
            

     2. Enable a password policy for a tenant using the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/patch):
            
            curl -X PATCH -d "{'passwordPolicyConfig':{'enforcementState':'ENFORCE','forceUpgradeOnSignin':true,'constraints':{'requireUppercase':true,'requireLowercase':true,'requireNonAlphanumeric':true,'requireNumeric':true,'minLength':MIN_PASSWORD_LENGTH,'maxLength':MAX_PASSWORD_LENGTH}}}" \
                -H 'Authorization: Bearer ACCESS_TOKEN' \
                -H 'Content-Type: application/json' \
                -H 'X-Goog-User-Project: PROJECT_ID' \
                "https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/tenants/TENANT_ID?updateMask=passwordPolicyConfig"
            

Replace the following:

        * `ACCESS_TOKEN`: the access token that you generated earlier
        * `PROJECT_ID`: your project ID
        * `TENANT_ID`: the ID of the tenant where you want to enforce the password policy
        * `MIN_PASSWORD_LENGTH`: the minimum required password length
        * `MAX_PASSWORD_LENGTH`: the maximum required password length




## Disable enforcement

  1. To disable password policy enforcement at the project level, follow these steps:

###  Firebase console 

     1. In the Firebase console, go to the **Authentication Settings** page.

[Go to Authentication Settings](https://console.firebase.google.com/project/_/authentication/settings)

     2. Select the **Password policy** tab.

     3. Disable password policy enforcement.

     4. Click **Save**.

###  REST 

     1. In the Google Cloud console, print an access token for your project ID using the [`gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token):
            
            gcloud auth print-access-token --project=PROJECT_ID
            

     2. Disable password policy enforcement using the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig):
            
            curl -X PATCH -d "{'passwordPolicyConfig':{'enforcementState':'OFF'}}" \
                -H 'Authorization: Bearer ACCESS_TOKEN' \
                -H 'Content-Type: application/json' \
                -H 'X-Goog-User-Project: PROJECT_ID' \
                "https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/config?updateMask=passwordPolicyConfig"
            

Replace the following:

        * `ACCESS_TOKEN`: the access token that you generated earlier
        * `PROJECT_ID`: your project ID

  2. To disable password policy enforcement at the tenant level, follow these steps:

**Note:** Tenant-level password policies are not supported in the Firebase console.

###  REST 

     1. In the Google Cloud console, print an access token for your project ID using the [`gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token):
            
            gcloud auth print-access-token --project=PROJECT_ID
            

     2. Disable password policy enforcement for a tenant using the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants/patch):
            
            curl -X PATCH -d "{'passwordPolicyConfig':{'enforcementState':'OFF'}}" \
                -H 'Authorization: Bearer ACCESS_TOKEN' \
                -H 'Content-Type: application/json' \
                -H 'X-Goog-User-Project: PROJECT_ID' \
                "https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/tenants/TENANT_ID?updateMask=passwordPolicyConfig"
            

Replace the following:

        * `ACCESS_TOKEN`: the access token that you generated earlier
        * `PROJECT_ID`: your project ID
        * `TENANT_ID`: the ID of the tenant where you want to disable the password policy




## Enforcing on the client side

Passwords can be validated against the password policy for the project or a tenant on the client side before submission.
    
    
    import { getAuth, validatePassword } from 'firebase/auth';
    
    const auth = getAuth();
    auth.tenantId = TENANT-ID;
    
    const status = await validatePassword(auth, 'password').catch((error) => {
      // Password couldn't be validated.
    });
    const policy = status.passwordPolicy;
    
    // Use the status and policy to show what requirements are met and which are
    // missing.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
