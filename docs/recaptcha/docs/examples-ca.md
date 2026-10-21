---
url: https://docs.cloud.google.com/recaptcha/docs/examples-ca/
title: Examples of integration with Google Cloud Armor \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:15.043936+00:00
---

# Examples of integration with Google Cloud Armor  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/examples-ca/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Examples of integration with Google Cloud Armor Stay organized with collections  Save and categorize content based on your preferences. 

This document shows examples of how to implement the features of reCAPTCHA for WAF for Cloud Armor.

You can use one or more features of reCAPTCHA for WAF in a single application.

If you want to use more than one feature, then you must create a reCAPTCHA key for each of those features and use them in your application. For example, if you want to use reCAPTCHA action-tokens and reCAPTCHA challenge page, then you must create an action-token key and a challenge-page key, and use them in your application. 

## Example 1: Using reCAPTCHA session-tokens and reCAPTCHA challenge page

You can add a reCAPTCHA session-token on pages that a user might access so that the cookie gets refreshed periodically, for example, a login page. Configure a Cloud Armor security policy rule to redirect the request to a reCAPTCHA challenge page when the score is low.

The following illustration shows a workflow that uses reCAPTCHA session-token and reCAPTCHA challenge page features:

![](https://docs.cloud.google.com/static/recaptcha/images/sessiontoken-redirect.svg)

![](https://docs.cloud.google.com/static/recaptcha/images/sessiontoken-redirect.svg)

## Example 2: Using reCAPTCHA action-tokens and reCAPTCHA challenge page

You can add a reCAPTCHA action-token to protect a user action, such as checkout. Configure a Cloud Armor security policy rule to redirect the request to a reCAPTCHA challenge page in any of the following conditions:

  * The score is low.
  * The `action_name` attribute of the action-token does not match the user action that is protected.



The following illustration shows a workflow that uses reCAPTCHA action-token and reCAPTCHA challenge page features:

![](https://docs.cloud.google.com/static/recaptcha/images/actiontoken-redirect.svg)

![](https://docs.cloud.google.com/static/recaptcha/images/actiontoken-redirect.svg)

The following sample script shows how to use a reCAPTCHA action-token and redirect to a reCAPTCHA challenge page with the action-token attached as a header:
    
    
       <script src="https://www.google.com/recaptcha/enterprise.js?render=ACTION_TOKEN_SITE_KEY"></script>
        <script>
         function onSuccess(token) {
           const xhr = new XMLHttpRequest();
           xhr.open('GET','http://www.example.com/checkout', false);
           xhr.setRequestHeader("X-Recaptcha-Token", token);
           xhr.onreadystatechange = function() {
             // Make sure that the request is finished and response is ready with 200
             if (this.readyState == 4 && this.status == 200) {
               // Display the response, it could be a reCAPTCHA challenge
               // page based on your Cloud Armor security rule settings.
                document.open();
                document.write(xhr.responseText);
                document.close();
    
             }
           };
           xhr.send(null);
         }
    
         grecaptcha.enterprise.ready(function () {
           document.getElementById("execute-button").onclick = () => {
             grecaptcha.enterprise.execute('ACTION_TOKEN_SITE_KEY', {
             }).then(onSuccess, onError);
           };
         });
        </script>
    

## What's next

  * Learn how to [implement reCAPTCHA WAF features with Cloud Armor](https://codelabs.developers.google.com/codelabs/cloud-armor-recaptcha-bot-management).
  * Learn more about [features for integration with WAF service providers](https://docs.cloud.google.com/recaptcha/docs/features-ca).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
