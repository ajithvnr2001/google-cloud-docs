---
url: https://docs.cloud.google.com/identity-platform/docs/recaptcha-byok/
title: Bring your own reCAPTCHA keys \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:45:01.162768+00:00
---

# Bring your own reCAPTCHA keys  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/recaptcha-byok/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bring your own reCAPTCHA keys

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use your own reCAPTCHA key with [Identity Platform integration with the reCAPTCHA Enterprise API](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise).

When the Identity Platform integration with the reCAPTCHA Enterprise API is enabled, Identity Platform provisions reCAPTCHA keys on your behalf by default. However, you can choose to bring your own reCAPTCHA key to use with reCAPTCHA. Uploading your own reCAPTCHA key disables the provisioning by Identity Platform.

## Enable the ability to bring your own key

To enable this capability and upload your reCAPTCHA key, call the endpoint with the following `curl` command:
    
    
    curl -i -X PATCH -H 'Content-Type: application/json' -H
    "x-goog-user-project: PROJECT_ID" -H 'Authorization: Bearer OAUTH_TOKEN' -d
    '
    {
      "recaptchaConfig": {
        "recaptchaKeys": [{"key": "projects/PROJECT_NUMBER/keys/KEY_VALUE",
        "type": "PLATFORM_TYPE"}],
      },
    }'
    https://identitytoolkit.googleapis.com/v2/projects/PROJECT_ID/config?updateMask=recaptchaConfig.recaptchaKeys
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `OAUTH_TOKEN`: the credential used for administrator requests
  * `PROJECT_NUMBER`: the project number
  * `KEY_VALUE`: the string that represents the reCAPTCHA key you want to upload
  * `PLATFORM_TYPE`: the platform of the application using the reCAPTCHA key. Valid values are `WEB`, `ANDROID`, and `IOS`.



## Disable the ability to bring your own key

To continue provisioning reCAPTCHA keys through Identity Platform, call the endpoint with `curl` and pass an empty list for `recaptchaConfig.recaptchaKeys`. For example:
    
    
    curl -i -X PATCH -H 'Content-Type: application/json' -H "x-goog-user-project:
    PROJECT_ID" -H 'Authorization: Bearer OAUTH_TOKEN' -d '
    {
      "recaptchaConfig": {
        "recaptchaKeys": [],
      },
    }'
    https://identitytoolkit.googleapis.com/v2/projects/PROJECT_ID/config?updateMask=recaptchaConfig.recaptchaKeys
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `OAUTH_TOKEN`: the credential used for administrator requests



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
