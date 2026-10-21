---
url: https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox/
title: Install checkbox keys (checkbox challenge) on websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:15.310930+00:00
---

# Install checkbox keys (checkbox challenge) on websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Install checkbox keys (checkbox challenge) on websites Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to install a checkbox key with the **I'm not a robot** checkbox challenge on your website. Depending on how you have configured the challenge security option when creating the checkbox key, reCAPTCHA might require the end user to solve a CAPTCHA challenge before generating a valid token.

## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  2. [Create a checkbox key](https://docs.cloud.google.com/recaptcha/docs/create-key-website).

Alternatively, you can copy the ID of an existing checkbox key by performing one of the following steps:

     * To copy the ID of an existing key from the **Google Cloud console** , do the following:

       1. Go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

       2. Select the **Keys** tab.
       3. In the reCAPTCHA keys list, find the key you want to copy, and then click  content_copy . 
     * To copy the ID of an existing key using the **REST API** , use the [projects.keys.list](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/list) method. 
     * To copy the ID of an existing key using the **gcloud CLI** , use the [gcloud recaptcha keys list](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/list) command. 



## Render the reCAPTCHA widget on the frontend

To display the reCAPTCHA widget on your web page, use one of the following methods:

#### Automatically render the widget

With this method, you can render the widget on any object (such as a `div` or a `span`) with the `g-recaptcha` class.

On your web page, include the necessary [JavaScript resource](https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys#resource_js) and an HTML element with the [`g-recaptcha`](https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys#attributes_parameters) class.

In the element with the `g-recaptcha` class, also include the `data-sitekey` attribute and set it equal to your checkbox key.

To specify an action, include the `data-action` attribute and set it to an action name. For more guidance, see [Actions](https://docs.cloud.google.com/recaptcha/docs/actions-website).

**Important:** The action that you specify is returned as part of the assessment. You must verify that the action in the JSON response of the assessment matches the expected action that you specify when creating an assessment. For example, a login action should be returned on your login page. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.

The script must be loaded using the HTTPS protocol and can be included from any point on the page without restriction.

reCAPTCHA uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following: `<script src="https://www.google.com/recaptcha/enterprise.js?hl=fr"></script>`. To learn about the supported languages, see [language codes for reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/language).

The following example is a snippet of sample code:
    
    
        <html>
          <head>
            <title>reCAPTCHA demo: Simple page</title>
            <script src="https://www.google.com/recaptcha/enterprise.js"></script>
          </head>
          <body>
            <form action="?" method="POST">
              <div class="g-recaptcha" data-sitekey="KEY_ID" data-action="LOGIN"></div>
              <br/>
              <input type="submit" value="Submit">
            </form>
          </body>
        </html>
    

#### Explicitly render the widget

With this method, you can render the widget through an existing JavaScript script using the `grecaptcha.enterprise.render()` method. Use this method to avoid race conditions or if you want to show the widget based on the existing JavaScript logic.

To avoid race conditions when rendering the widget explicitly, order your scripts with the callback function first and then the reCAPTCHA API.

To render the widget explicitly, follow these steps:

  1. To defer rendering of the widget, do the following:

     1. Specify your `onload` callback function before the reCAPTCHA API and other dependencies are loaded.
            
            <script type="text/javascript">
             var onloadCallback = function() {
                alert("grecaptcha is ready!");
             };
             </script>
            

     2. After your callback function is executed, call the `grecaptcha.enterprise.render()` method with the following parameters from the [JavaScript API](https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys#javascript_api).

        * **container** : The HTML element to render the reCAPTCHA widget. Specify either the ID of the container (string) or the DOM element itself.

        * **parameters** : An object containing parameters as key-value pairs, for example, {"sitekey": "KEY_ID", "theme": "light"}.

        * **action** : Specify the action name associated with the protected element.

**Important:** The action that you specify is returned as part of the assessment. You must verify that the action in the JSON response of the assessment matches the expected action that you specify when creating an assessment. For example, a login action should be returned on your login page. If there is a mismatch, it indicates that an attacker is attempting to falsify actions.
    
    grecaptcha.enterprise.render('html_element', {
       'sitekey' : 'KEY_ID',
       'action': 'LOGIN',
     });
    

  2. To render the widget, insert the [JavaScript resource](https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys#resource_js). Set `onload` to the name of your onload callback function, and include `render=explicit`.

reCAPTCHA uses the browser's language by default. If you want to specify a different language, use the `hl=LANG` attribute in your script. For example, to use French, specify the following: `<script src="https://www.google.com/recaptcha/enterprise.js?hl=fr"></script>`. To learn about the supported languages, see [language codes for reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/language).
         
         <script src="https://www.google.com/recaptcha/enterprise.js?onload=onload_Callback_function&render=explicit">
          </script>
         




**Example 1**

The following code sample shows explicit rendering after an `onload` callback:
    
    
    <html>
       <head>
        <title>reCAPTCHA demo: Explicit render after an onload callback</title>
         <script type="text/javascript">
          var onloadCallback = function() {
            grecaptcha.enterprise.render('html_element', {
              'sitekey' : 'KEY_ID',
              'action': 'LOGIN',
            });
          };
        </script>
      </head>
      <body>
        <form action="?" method="POST">
          <div id="html_element"></div>
          <br>
          <input type="submit" value="Submit">
        </form>
          <script src="https://www.google.com/recaptcha/enterprise.js?onload=onloadCallback&render=explicit">
        </script>
      </body>
    </html>
    

**Example 2**

The following code sample shows explicit rendering of multiple widgets:
    
    
    <html>
      <head>
        <title>reCAPTCHA demo: Explicit render for multiple widgets</title>
            <script type="text/javascript">
          var verifyCallback = function(response) {
            alert(response);
          };
          var widgetId1;
          var widgetId2;
          var onloadCallback = function() {
            // Renders the HTML element with id 'example1' as a reCAPTCHA widget.
            // The id of the reCAPTCHA widget is assigned to 'widgetId1'.
            widgetId1 = grecaptcha.enterprise.render('example1', {
              'sitekey' : 'KEY_ID',
              'action': 'action1',
              'theme' : 'light'
            });
            widgetId2 = grecaptcha.enterprise.render(document.getElementById('example2'), {
              'sitekey' : 'KEY_ID',
              'action': 'action2',
            });
            grecaptcha.enterprise.render('example3', {
              'sitekey' : 'KEY_ID',
              'action': 'action3',
              'callback' : verifyCallback,
              'theme' : 'dark'
            });
          };
        </script>
      </head>
      <body>
        <!-- The g-recaptcha-response string displays in an alert message upon submit. -->
        <form action="javascript:alert(grecaptcha.enterprise.getResponse(widgetId1));">
          <div id="example1"></div>
          <br>
          <input type="submit" value="getResponse">
        </form>
        <br>
        <!-- Resets reCAPTCHA widgetId2 upon submit. -->
        <form action="javascript:grecaptcha.enterprise.reset(widgetId2);">
          <div id="example2"></div>
          <br>
          <input type="submit" value="reset">
        </form>
        <br>
        <!-- POSTs back to the page's URL upon submit with a g-recaptcha-response POST parameter. -->
        <form action="?" method="POST">
          <div id="example3"></div>
          <br>
          <input type="submit" value="Submit">
        </form>
         <script src="https://www.google.com/recaptcha/enterprise.js?onload=onloadCallback&render=explicit">
        </script>
      </body>
    </html>
    

## What's next

  * To assess the reCAPTCHA response token, [create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
