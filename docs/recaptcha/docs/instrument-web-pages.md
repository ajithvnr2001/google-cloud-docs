---
url: https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages/
title: Install score-based keys on websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:00.462116+00:00
---

# Install score-based keys on websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Install score-based keys on websites Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to install a score-based key with no challenge on your website. With a score-based key, you can include reCAPTCHA throughout your site without requiring users to solve CAPTCHA challenges.

When a score-based key is installed, reCAPTCHA sends an encrypted response, the reCAPTCHA response token (also known as token), when an end user triggers an interaction. After the token is generated, you need to create an assessment within two minutes to receive a score for each request. Based on the score, you can understand the level of risk that user interactions pose and configure an appropriate response (or responses). Also, the score-based key can collect bot activity telemetry for early warning against new attacks or targets.

To improve reCAPTCHA's risk model, we recommend that you include reCAPTCHA on every page of your site because it helps in understanding how real users and bots transition between different pages and actions.

## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  2. [Create a score-based key](https://docs.cloud.google.com/recaptcha/docs/create-key-website).

Alternatively, you can copy the ID of an existing score-based key by performing one of the following steps:

     * To copy the ID of an existing key from the **Google Cloud console** , do the following:

       1. Go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

       2. Select the **Keys** tab.
       3. In the reCAPTCHA keys list, find the key you want to copy, and then click  content_copy . 
     * To copy the ID of an existing key using the **REST API** , use the [projects.keys.list](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/list) method. 
     * To copy the ID of an existing key using the **gcloud CLI** , use the [gcloud recaptcha keys list](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/list) command. 



## Place the key on your website

reCAPTCHA works best when it has context about the interactions on your site. reCAPTCHA monitors both legitimate and abusive behavior to learn about the interactions on your site.

For best results, install score-based keys in the following places on your website:

  * Forms
  * Actions (user interactions)
  * In the background of all webpages



Score-based keys don't interrupt your users, so you can run reCAPTCHA with score-based keys whenever required without affecting conversion.

## Integrate the key with the frontend

We recommend adding reCAPTCHA verification on a user interaction that needs to be verified. For example, if you want to verify the submit action of a form, then you need to add reCAPTCHA verification on the submit action.

Depending on where you want to add reCAPTCHA verification, choose the appropriate option:

  * Add verification on a user interaction
  * Add reCAPTCHA on an HTML button



You can see an example of each option in the source code of the [demo website](https://docs.cloud.google.com/recaptcha/docs/quickstart-app).

### Add verification on a user interaction

  1. To load reCAPTCHA on your web page, add the JavaScript API with your score-based key within the `<head></head>` element of your web page.
         
         <head>
             <script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID"></script>
             ....
             </head>
           

reCAPTCHA uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following: `<script src="https://www.google.com/recaptcha/enterprise.js?hl=fr"></script>`. To learn about the supported languages, see [language codes for reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/language).

If you want to specify a location for the badge, then use `badge=LOCATION` as a query parameter in the script tag. For example, `www.google.com/recaptcha/enterprise.js?render=KEY_ID&badge=bottomleft`. By default, the location is set to `bottomright`. The other possible values are `inline` and `bottomleft`.

  2. To add reCAPTCHA verification on a user interaction, do the following:

     1. To ensure that `grecaptcha.enterprise.execute()` runs after the reCAPTCHA library loads, use `grecaptcha.enterprise.ready()`.

     2. Call `grecaptcha.enterprise.execute()` on each interaction you want to protect with your score-based key. Specify a meaningful name for a user interaction in the `action` parameter. For more guidance, see [Actions](https://docs.cloud.google.com/recaptcha/docs/actions-website).

**Tip:** Add the `execute` call to interesting or sensitive actions like `Register`, `Password Reset`, `Purchase`, or `Play`.

The following example shows how to call `grecaptcha.enterprise.execute()` on a login action:
            
            <script>
            function onClick(e) {
              e.preventDefault();
              grecaptcha.enterprise.ready(async () => {
                const token = await grecaptcha.enterprise.execute('KEY_ID', {action: 'LOGIN'});
                // IMPORTANT: The 'token' that results from execute is an encrypted response sent by
                // reCAPTCHA to the end user's browser.
                // This token must be validated by creating an assessment.
                // See https://cloud.google.com/recaptcha/docs/create-assessment
              });
            }
            </script>

`grecaptcha.enterprise.execute()` generates a token as shown in the following example: 
            
            03AGdBq27tvcDrfiRuxQnyKs-SarXVzPODXLlpiwNsLqdm9BSQQRtxhkD-Wv6l2vBSnL_JQd80FZp3IeeF_TxNMrqhyQchk7hmg_ypDctt_F5RTr9zNO9TSDX3Fy0qHQTuaM9E3hrAkA1v1l7D-fCreg7uq8zoudfh1ZRmN49-2iAMAn4E8_ff-nmlLTNGVZmCSyeze-5xM24pM_JhhUVcCMIDKYtDUnr2imxg2ubIqMscCZGUtdXNUO_LRSzuwWDlLyAr3V2nVn29Z48PQa2QzbymEXzO9pCtoGQmY7kiZ8ILfD9DAJSSyUTMwJXVJptUeBmLM341fq_STYZBbPQJ0zYOEDvJoFsIwGMfuphkDet0nK56b0mkzaL8RCRy2oK31Mcx6n3PhGkCnQ6QIhiV5ZVmV1Hz9M3w99zYw6ekc3wPCNMZ6V6x1ApVpIk3reFfByRQ0C0_pRWwbKZHLXQ_oSTI1UI7kyH1VeXngsJAx2l7zcp0hQNipajC4YwL7Jb8X4cCD0NeiaY1YCrI5j87mK5axcMikq460I4niIFeDBlHGF-ndqu3CJstosAur-C_x827f-dPPjA9Vrw8MDb3 _x4KUb0vbA8xE9mJxPYGY0rPCR27vJ38Voa7DjEBGX9c_ -iufv5_wfj-yIfIAHy0iijnRLI0CVkWF2-iPdWv7LnkTwL3WKbF_MrEGZXmtyLX9dEZArfxmToeMuSdYkfikkgR2-k4Xzxlz15RbHJuWSAYqEyTTnpUXmOvDuTN92b0kYqbRelcLUI_Shm-8dq9e-L7K6YWQv32gV6NukZKY15dyrJaW10frBgTOGSTTpIyB7MNEL8S27WjWtOb-zWsgimIhoRNfS8BiJWkmK4gTj51m7Wur-qsDbHgV6gXlMvjJs_B7oXX-mKsKhY9ACtwukotBelGYQOvf1RDHjH3Yi1RDfELBY6AkwUK4tq8cACVGpCwa0gKUo-sbORTsGu_r7VTzYo1AaZD5HV4XUm8yoqszel6DmIfkJcI7PfzzvfUJuvMQ1itZSzpzuth3glbKBYsIjbKqG-q8cxtZ7u0l32j46ASo2zlCJWUjwP3W1P7MUenEoIZtjlyTB_tT6Fk8RxGgRv3oLP7NPFJGs9ZGOAl6tBHpZF8Y_FqEOCMKtBl2JYOE5h6_Es3buSdiMm7mtLr64pboGiEColF1vbVvYpyaaqGFPXBM6ekZSXEXLAI0_7rj_fCLgnB21KXfac95vZbM9vyJCASvDcWKwqajQwy5aGMNe9GtbMogYbZfz5UGWAIi24Vd8KSv3qKOOwvzbcw4H0HYdsBXA
            

  3. After the token is generated, send the reCAPTCHA token to your backend and create an assessment within two minutes.

For WAF integrations, if you are integrating an action-token key, you must attach the token to a predefined request header and you need not create an assessment. For details, see [Implement reCAPTCHA action-tokens](https://docs.cloud.google.com/recaptcha/docs/implement-tokens#action-token).

**Important:** The `action` that you specify during `execute()` is returned as part of the assessment. You must verify that the `action` in the JSON response of the assessment matches the expected action that you specify when creating an assessment. For example, a `login` action should be returned on your **login** page. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.



### Add reCAPTCHA on an HTML button

  1. To load reCAPTCHA on your web page, add the JavaScript API with your score-based key within the `<head></head>` element of your web page.
         
         <head>
             <script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID"></script>
             ....
             </head>
           

reCAPTCHA uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following: `<script src="https://www.google.com/recaptcha/enterprise.js?hl=fr"></script>`. To learn about the supported languages, see [language codes for reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/language).

  2. To add reCAPTCHA on a simple HTML button, do the following:

     1. Define a callback function to handle the token.
            
            <script>
               function onSubmit(token) {
                 document.getElementById("demo-form").submit();
               } // Use `requestSubmit()` for extra features like browser input validation.
            </script>

For more information, see [requestSubmit() method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/requestSubmit).

     2. Add attributes to your html button.
            
            <button class="g-recaptcha"
            data-sitekey="KEY_ID"
            data-callback="onSubmit"
            data-action="submit">Submit</button>

If you want to specify a location for the badge, then use the `data-badge=LOCATION` attribute on the element that has `class=g-recaptcha`. By default, the location is set to `bottomright`. The other possible values are `inline` and `bottomleft`.

     3. When this button is used to submit a form on your site, the `g-recaptcha-response` POST parameter contains the response token.

**Note:** If you set the `g-recaptcha` button as `disabled`, the button is enabled when reCAPTCHA is loaded.
  3. After the token is generated, send the reCAPTCHA token to your backend and create an assessment within two minutes.

For WAF integrations, if you are integrating an action-token key, you must attach the token to a predefined request header and you need not create an assessment. For details, see [Implement reCAPTCHA action-tokens](https://docs.cloud.google.com/recaptcha/docs/implement-tokens#action-token).

**Important:** The `action` that you specify during `execute()` is returned as part of the assessment. You must verify that the `action` in the JSON response of the assessment matches the expected action that you specify when creating an assessment. For example, a `login` action should be returned on your **login** page. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.



## What's next

  * To assess the reCAPTCHA response token, [create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
