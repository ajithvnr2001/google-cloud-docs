---
url: https://docs.cloud.google.com/appengine/docs/standard/services/users/loginurls/
title: Login URLs \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:00.158898+00:00
---

# Login URLs  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/users/loginurls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Login URLs Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The Users API provides functions for constructing URLs that allow the user to sign in or sign out, then be redirected back to your application.

[`users.create_login_url()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users/CreateLoginURL) and [`users.create_logout_url()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users/CreateLogoutURL) each take a destination URL for the application, and return a URL for signing in or signing out that redirects back to the given URL afterward.

The development web server simulates Google Accounts using its own sign-in and sign-out facilities. When you sign in to your application on the development web server, the server prompts you for an email address to use for the session. See [The Development Web Server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server) for more information.

**Tip:** An easy way to restrict access to a part of your application to signed in users is to use the `login: required` element for the URL handler. See the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_login) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
