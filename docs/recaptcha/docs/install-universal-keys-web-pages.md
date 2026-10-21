---
url: https://docs.cloud.google.com/recaptcha/docs/install-universal-keys-web-pages/
title: Install Universal keys on web pages \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:25.889191+00:00
---

# Install Universal keys on web pages  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/install-universal-keys-web-pages/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Install Universal keys on web pages Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can install and integrate a Universal key with your web pages.

## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  2. [Create a Universal key](https://docs.cloud.google.com/recaptcha/docs/policy-engine#create-key) and [configure domains](https://docs.cloud.google.com/recaptcha/docs/policy-engine#configure-domains).




## Install Universal keys on your website

To install your Universal key and help protect your web pages, choose either the Google Cloud Fraud Defense AutoExecute configuration or the standard JavaScript installation:

### AutoExecute configuration

Fraud Defense AutoExecute can help simplify your frontend JavaScript integration through intercepting network requests on your web pages, eliminating the need to manually call `grecaptcha.enterprise.execute()` for each frontend action.

**Important:** Consider the following when using AutoExecute:

  * AutoExecute only intercepts asynchronous network requests initiated with the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) or [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), including requests from frameworks like AJAX that use these APIs.
  * AutoExecute is not supported for resources that load automatically at page load time. Instead, apply AutoExecute to network requests triggered by user actions on the page, such as a login button.
  * To prevent Fraud Defense challenges from causing network timeouts, apply timeouts directly to the requests. Use `AbortSignal.timeout(n)` for the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and the `XMLHttpRequest.timeout` property for [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest).



### Add the script tag to your web pages

To load reCAPTCHA on your web page, add the JavaScript API with your Universal key within the `<head></head>` element of your web page:
    
    
    <head>
      <script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID"></script>
      ...
    </head>
    

Fraud Defense uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following:

`<script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID&hl=fr"></script>`

To learn about the supported languages, see [language codes for Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/language).

### Configure protected endpoints

The Fraud Defense script automatically integrates with network actions defined in the policy configuration of your Universal key. This section defines a mapping of URL paths (`path`) to action names (`action`).

**Tip:** Specify `protected_endpoints` only for sensitive paths. For each path, specify a meaningful name for the user interaction in the `action` parameter. Avoid protecting every endpoint, because triggering Fraud Defense on every backend request can negatively impact performance. For more guidance, see [Actions](https://docs.cloud.google.com/recaptcha/docs/actions-website).

If the Fraud Defense script detects an asynchronous network request to a mapped path, it intercepts the request, triggers a risk evaluation, and potentially displays a CAPTCHA challenge to the user before the original request continues. The generated response token is automatically attached to the `X-Recaptcha-Token` header in the request.

### gcloud

To inspect the current policy configuration for your Universal key, use the [`gcloud alpha recaptcha policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/policies/describe) command:
    
    
    gcloud alpha recaptcha policies describe --key=KEY_ID
    

To update the policy configuration with your protected endpoints, create a YAML file (for example, `POLICY.yaml`) defining your protected paths and actions:
    
    
    client_settings:
      allowedDomains:
        - example.com
      protected_endpoint_group:
        protected_endpoints:
          - path: "/login_api"
            action: login
          - path: "/register_api"
            action: register
          - path: "/cart_api/add/*"
            action: add_to_cart
    

Update your key configuration with the YAML file using the [`gcloud alpha recaptcha policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/policies/update) command:
    
    
    gcloud alpha recaptcha policies update \
        --key=KEY_ID \
        --policy=POLICY.yaml
    

**Note:** The `gcloud alpha recaptcha policies update` command updates the entire policy. Any existing `protected_endpoint_group` or `challenge_rule_groups` must be included in your `POLICY.yaml` file to avoid deleting them.

### REST API

To update the policy configuration to define protected endpoints using the REST API, use the [`projects.keys.updatePolicy`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/updatePolicy) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * KEY_ID: the ID of your Universal key



HTTP method and URL: 
    
    
    PATCH https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy?updateMask=clientSettings.protectedEndpointGroup

Request JSON body: 
    
    
    {
    "clientSettings": {
      "protectedEndpointGroup": {
        "protectedEndpoints": [
          {
            "path": "/login_api",
            "action": "login"
          },
          {
            "path": "/register_api",
            "action": "register"
          },
          {
            "path": "/cart_api/add/*",
            "action": "add_to_cart"
          }
        ]
      }
    }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy?updateMask=clientSettings.protectedEndpointGroup"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys/KEY_ID/policy?updateMask=clientSettings.protectedEndpointGroup" | Select-Object -Expand Content

If successful, the request returns the updated policy configuration. 

The `path` parameter supports glob patterns with the following rules:

  * Must start with `/` and cannot be empty.
  * Cannot be a standalone `/*` or `/**`, as it can negatively impact performance to trigger Fraud Defense on every single request to your backend.
  * Wildcards `*` (matching a single path segment) and `**` (matching multiple path segments) must occupy the entirety of a path segment (for example, `/api/*/login` or `/api/*` are valid; `/api/login*` is invalid).
  * The `**` wildcard must only occupy the last path segment (for example, `/api/**` is valid; `/api/**/login` is invalid).

**Note:** `AutoExecute` matches requests based on the **URL path only** and does not check the destination domain. This has the following practical implications:

  * **Third-party requests:** If third-party tools running on your page (such as analytics or partner scripts) send requests to paths that match your protected endpoints (for example, `https://analytics.example.net/login` matching `/login`), `AutoExecute` will also intercept them. This can cause extra network latency, skewed metrics, or unexpected CAPTCHA challenges. To avoid conflicts, ensure your protected paths are distinctive (for example, `/auth/v1/login`), or use the **Standard installation** if path collisions occur.
  * **Cross-domain APIs:** If your backend API is hosted on a different domain than your website (for example, `examplecdn.net` versus `www.example.com`), `AutoExecute` works automatically without extra domain configuration.



If matching against specific destination domains is important for your integration, [file a feature request](https://docs.cloud.google.com/support/docs/issue-trackers).

In your backend, get the response token from the `X-Recaptcha-Token` request header and [create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website) within two minutes.

**Important:** Your backend must specify `assessment.event.expected_action` (or `expectedAction` in JSON) in the [`CreateAssessmentRequest`](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website), and it must match the action configured in the `ProtectedEndpoint`. For example, if you configure the protected endpoint action to be `login`, your backend must set `expected_action` to `login` when creating an assessment for that request. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.

### Standard installation

We recommend that you add Fraud Defense verification on a user interaction that needs to be verified. For example, if you want to verify the submit action of a form, then you need to add Fraud Defense verification on the submit action.

Depending on where you want to add Fraud Defense verification, choose the appropriate option:

  * Add verification on a user interaction
  * Add Fraud Defense on an HTML button



### Add verification on a user interaction

  1. To load reCAPTCHA on your web page, add the JavaScript API with your Universal key within the `<head></head>` element of your web page:
         
         <head>
           <script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID"></script>
           ...
         </head>
         

Fraud Defense uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following:

`<script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID&hl=fr"></script>`

To learn about the supported languages, see [language codes for Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/language).

If you want to specify a location for the badge, use `badge=LOCATION` as a query parameter in the script tag. For example, `https://www.google.com/recaptcha/enterprise.js?render=KEY_ID&badge=bottomleft`. By default, the location is set to `bottomright`. Other possible values are `inline` and `bottomleft`.

  2. To add Fraud Defense verification on a user interaction, do the following:

     1. To help ensure that `grecaptcha.enterprise.execute()` runs after the Fraud Defense library loads, use `grecaptcha.enterprise.ready()`.
     2. Call `grecaptcha.enterprise.execute()` on each interaction that you want to protect with your Universal key. Specify a meaningful name for a user interaction in the `action` parameter. For more guidance, see [Actions](https://docs.cloud.google.com/recaptcha/docs/actions-website).

**Tip:** Add the `execute` call to sensitive actions such as `LOGIN`, `SIGNUP`, `PASSWORD_RESET`, or `PURCHASE`.

The following example shows how to call `grecaptcha.enterprise.execute()` on a login action:
            
            <script>
              // Use `requestSubmit()` for extra features like browser input
              // validation.
              function onClick(e) {
                e.preventDefault();
                grecaptcha.enterprise.ready(async () => {
                  const token = await grecaptcha.enterprise.execute(
                    'KEY_ID',
                    {action: 'LOGIN'}
                  );
                  // IMPORTANT: The 'token' that results from execute is an
                  // encrypted response sent by Fraud Defense to
                  // the end user's browser.
                  // This token must be validated by creating an assessment.
                  // See https://cloud.google.com/recaptcha/docs/create-assessment
                });
              }
            </script>
            

s

  3. After the token is generated, send the reCAPTCHA token to your backend and create an assessment within two minutes.

**Important:** Your backend must specify `assessment.event.expected_action` (or `expectedAction` in JSON) in the [`CreateAssessmentRequest`](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website), and it must match the action configured in the `execute()` call. For example, if you configure the frontend action to be `LOGIN`, your backend must set `expected_action` to `LOGIN` when creating an assessment for that request. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.



### Add Fraud Defense on an HTML button

  1. To load reCAPTCHA on your web page, add the JavaScript API with your Universal key within the `<head></head>` element of your web page:
         
         <head>
           <script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID"></script>
           ...
         </head>
         

Fraud Defense uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following:

`<script src="https://www.google.com/recaptcha/enterprise.js?render=KEY_ID&hl=fr"></script>`

To learn about the supported languages, see [language codes for Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/language).

  2. To add Fraud Defense on an HTML button, do the following:

     1. Define a callback function to handle the token.
    
    <script>
      function onSubmit(token) {
        document.getElementById("demo-form").submit();
      }
      // Use `requestSubmit()` for extra features like browser input
      // validation.
    </script>
    

For more information, see the [requestSubmit() method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/requestSubmit).

     1. Add attributes to your HTML button.
    
    <button class="g-recaptcha"
        data-sitekey="KEY_ID"
        data-callback="onSubmit"
        data-action="submit">Submit</button>
    

If you want to specify a location for the badge, use the `data-badge="LOCATION"` attribute on the element that has `class="g-recaptcha"`. By default, the location is set to `bottomright`. Other possible values are `inline` and `bottomleft`.

     1. When this button is used to submit a form on your site, the `g-recaptcha-response` POST parameter contains the response token.
**Note:** If you set the `g-recaptcha` button as `disabled`, the button is enabled when Fraud Defense is loaded.
  3. After the token is generated, send the reCAPTCHA token to your backend and create an assessment within two minutes.

**Important:** Your backend must specify `assessment.event.expected_action` (or `expectedAction` in JSON) in the [`CreateAssessmentRequest`](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website), and it must match the action configured on the button. For example, if you configure the button action to be `submit`, your backend must set `expected_action` to `submit` when creating an assessment for that request. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.



## What's next

  * To trigger CAPTCHA challenges based on custom rules, [configure challenge policies](https://docs.cloud.google.com/recaptcha/docs/challenge-policies).

  * To assess the reCAPTCHA response token, [create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
