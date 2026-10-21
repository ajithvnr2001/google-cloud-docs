---
url: https://docs.cloud.google.com/iap/docs/force-login/
title: Use IAP as an authentication proxy \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:52.184595+00:00
---

# Use IAP as an authentication proxy  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/force-login/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Use IAP as an authentication proxy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Identity-Aware Proxy (IAP) as an authentication proxy.

When you configure an IAP policy to allow all users access to an application, IAP does not check user authentication credentials. If you want to use IAP as an authentication proxy, and have users authenticate when accessing a resource, you must set the IAP mode to `Force_Login`.

## Configure IAP as an authentication proxy

To configure IAP as an authentication proxy, complete the following steps:

  1. Follow the IAP [How-to guides ](https://docs.cloud.google.com/iap/docs/how-to) documentation to enable IAP on a resource.

  2. Go to the IAP page.   
[Go to Identity-Aware Proxy](https://console.cloud.google.com/security/iap/)

  3. Select a resource, and then click **Add Member**.

  4. Add the **IAP-secured Web App User** role to `allUsers` to make the resource publicly accessible.

  5. To have IAP authenticate users, ensure that your request to the application is in the following format:

`YOUR_APP_URL?gcp-iap-mode=FORCE_LOGIN`

This enforces authentication to all incoming requests and redirects the request to `YOUR_APP_URL` after successful authentication.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
