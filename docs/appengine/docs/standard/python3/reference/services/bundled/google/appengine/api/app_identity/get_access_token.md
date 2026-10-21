---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/get_access_token/
title: google.appengine.api.app_identity.get_access_token \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:34:58.831623+00:00
---

# google.appengine.api.app_identity.get_access_token  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/get_access_token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.app_identity.get_access_token Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity.py#L440-L462) The OAuth 2.0 access token to act on behalf of the application.

#### View aliases

**Main aliases** `google.appengine.api.app_identity.app_identity.get_access_token`
    
    
    google.appengine.api.app_identity.get_access_token(
        scopes, service_account_id=None
    )
    

Each application has an associated Google account. This function returns an OAuth 2.0 access token that corresponds to the running app. Access tokens are safe to cache and reuse until their expiry time as returned. | 

## Args  
  
---  
  
`scopes` |  The requested API scope string, or a list of strings.   
  
## Returns  
  
---  
A `Pair`, `Access` token string and the expiration time in seconds since the epoch.   
  
## Raises  
  
---  
  
`InvalidScope` |  If the scopes are unspecified or invalid.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
