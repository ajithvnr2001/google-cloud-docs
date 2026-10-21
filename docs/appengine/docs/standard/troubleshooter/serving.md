---
url: https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/serving/
title: Troubleshoot serving issues in App Engine \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:58.664202+00:00
---

# Troubleshoot serving issues in App Engine  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/serving/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Troubleshoot serving issues in App Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes common app initialization and serving errors in App Engine and methods to troubleshoot them.

### Permission error when creating an app with the default service account

When you create an app after enabling the App Engine API for the first time, it might fail with the following errors:

###  gcloud CLI 
    
    
    An internal error occurred while calling service consumer manager for service account.
    Creating  App Engine application in projectPROJECT and REGION....failed. DEBUG: (gcloud.app.create) Error Response: [13] an internal error has occurred
    

###  Request logs 
    
    
    Service account creation is not allowed on this project.
    

###  Console 
    
    
    Error while initialising App Engine.
    

This error might occur due to the enforcement of the organization policy constraint [`constraints/iam.disableServiceAccountCreation`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_creation) when creating your app. This policy prevents the provisioning of the [ App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts) `PROJECT_ID@appspot.gserviceaccount.com`.

To resolve this issue, you must temporarily remove the organization policy constraint `constraints/iam.disableServiceAccountCreation` to allow for the creation and deployment of the App Engine default service account. The default service account is necessary for app creation and can't be skipped. This is also applicable when you use a per-version service account. The App Engine default service account can be deleted or replaced with a service account that you create after successful deployment.

If you are using a service account that you created, review the [Overview of role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) to understand how to enforce restricting permissions, such as providing a token creator role on the service account you create for the service agent.

### Security errors when using legacy bundled services for Python

If you use a legacy bundled services API when a Python 3 app is starting up, you might see the following error message:
    
    
    Attempted RPC call without active security ticket
    

This error might occur in scenarios such as, reading certain values from [Memcache](https://docs.cloud.google.com/appengine/docs/standard/services/memcache) when your app is starting to configure a database connection or set a global variable.

To resolve this issue, you could try moving such logic into a [warmup request](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
