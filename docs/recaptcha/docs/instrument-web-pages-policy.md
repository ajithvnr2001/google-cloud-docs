---
url: https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-policy/
title: Install policy-based challenge keys on websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:54.074997+00:00
---

# Install policy-based challenge keys on websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-policy/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Install policy-based challenge keys on websites Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to install a policy-based challenge key on your website. With a policy-based challenge key, reCAPTCHA can deterministically trigger CAPTCHA challenges based on a score threshold and challenge difficulty.

## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

reCAPTCHA requires billing to be linked and enabled on the project to use policy-based challenge keys. You can enable billing by using either a credit card or an existing Google Cloud project billing ID. If you need help with billing, contact [Cloud Billing support](https://cloud.google.com/support/billing).

  3. [Create a policy-based challenge key](https://docs.cloud.google.com/recaptcha/docs/create-key-website).

Alternatively, you can copy the ID of an existing policy-based challenge key by performing one of the following steps:

     * To copy the ID of an existing key from the **Google Cloud console** , do the following:

       1. Go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

       2. Select the **Keys** tab.
       3. In the reCAPTCHA keys list, find the key you want to copy, and then click  content_copy . 
     * To copy the ID of an existing key using the **REST API** , use the [projects.keys.list](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/list) method. 
     * To copy the ID of an existing key using the **gcloud CLI** , use the [gcloud recaptcha keys list](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/list) command. 



## Configure the policy-based challenge key

For your policy-based challenge key, you must specify the challenge difficulty that determines the complexity and frequency of CAPTCHA challenges, and define a custom score threshold for specific actions that overrides the default threshold.

  1. In the Google Cloud console, go to the **reCAPTCHA** page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha)

  2. Check that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, and then select your project.

  3. Select the **Keys** tab.

The **Keys** tab has two views: **Table** and **Cards**. If your project has many reCAPTCHA keys, only the **Table** view is available.

  4. In the **reCAPTCHA keys** section, identify the policy-based challenge key that you want to configure, and click the key.

  5. On the **Key details** page, click the **Overview** tab.

  6. In the **Configuration** section, click **Configure** for **Challenge settings**.

  7. On the **Configure challenge settings** page, select the challenge difficulty.

  8. To trigger CAPTCHA challenges, use the slider to specify the default threshold value.

The default threshold of `0.0` does not trigger any challenge. A threshold of `1.0` triggers a challenge for every request.

  9. To configure a custom score threshold for individual actions, which overrides the default threshold value, do the following:

     1. Enter an [action name](https://docs.cloud.google.com/recaptcha/docs/actions-website).

**Note:** You cannot use more than 100 action names.
     2. To specify a custom score threshold, use the **Set action threshold** slider.

     3. Click **Done**.

  10. Click **Save**.




## Add reCAPTCHA on an HTML button

  1. To load reCAPTCHA on your web page, add the JavaScript API with your policy-based challenge key within the `<head></head>` element of your web page.
         
         <head>
             <script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID"></script>
             ....
             </head>
           

reCAPTCHA uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following: `<script src="https://www.google.com/recaptcha/enterprise.js?hl=fr"></script>`. To learn about the supported languages, see [language codes for reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/language).

  2. To add reCAPTCHA on an HTML button, do the following:

     1. Define a callback function to handle the token.
            
            <script>
               function onSubmit(token) {
                 document.getElementById("demo-form").submit();
               } // Use `requestSubmit()` for extra features like browser input validation.
            </script>

For more information, see [requestSubmit() method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/requestSubmit).

     2. Add attributes to your HTML button.
            
            <button class="g-recaptcha"
            data-sitekey="KEY_ID"
            data-callback="onSubmit"
            data-action="submit">Submit</button>

If you want to specify a location for the badge, then use the `data-badge=LOCATION` attribute on the element that has `class=g-recaptcha`. By default, the location is set to `bottomright`. The other possible values are `inline` and `bottomleft`.

     3. When this button is used to submit a form on your site, the `g-recaptcha-response` POST parameter contains the response token.

**Note:** If you set the `g-recaptcha` button as `disabled`, the button is enabled when reCAPTCHA is loaded.
  3. After the token is generated, send the reCAPTCHA token to your backend and create an assessment within two minutes.

**Important:** The `action` that you specify is returned as part of the assessment. You must verify that the `action` in the JSON response of the assessment matches the expected action that you specify when creating an assessment. For example, a `login` action should be returned on your **login** page. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.



## What's next

  * To assess the reCAPTCHA response token, [create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
