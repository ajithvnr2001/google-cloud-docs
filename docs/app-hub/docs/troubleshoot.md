---
url: https://docs.cloud.google.com/app-hub/docs/troubleshoot/
title: Troubleshoot App Hub issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:16.078618+00:00
---

# Troubleshoot App Hub issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Troubleshoot App Hub issues Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to resolve issues with App Hub.

## You can't attach a service project to a host project

This issue can occur due to the following reasons:

  * If the service project has existing attachments to a host project. To resolve this issue, follow these steps:

    1. [Remove or detach](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project#remove-service-projects) the service project from the existing host project.
    2. [Attach the service project to the new host project](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project#attach-service-projects).
  * If the App Hub API is disabled on the host project. Even if the App Hub API has been disabled, any prior service project attachments to the host project will exist. To resolve this issue, follow these steps:

    1. [Remove or detach](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project#remove-service-projects) the service projects from the host project.
    2. [Enable the App Hub API](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling) on the host project.
    3. [Disable the App Hub API](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling) on the service projects.
    4. [Attach the service project to the host project](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project#attach-service-projects).
  * If the appropriate Identity and Access Management (IAM) permissions haven't been granted to the host and service projects. To resolve this issue, [grant the App Hub Admin role to your principal in the host and service projects](https://docs.cloud.google.com/app-hub/docs/roles-permissions).




## Related information

  * [Get support](https://docs.cloud.google.com/app-hub/docs/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
