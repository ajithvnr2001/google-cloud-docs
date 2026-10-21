---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as/
title: Set a run-as service account \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:51.157006+00:00
---

# Set a run-as service account  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set a run-as service account

This page is part of [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes). Follow these steps for each integration that [needs a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-find-affected) and doesn't have one.

## Set the service account

  1. Choose or create the service account, and grant it the roles the integration's tasks need on the resources they touch. To work out what to grant, look at the roles your project's Application Integration service agent, `service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`, holds today, and give the new account just the part this integration uses.
  2. [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) on it to everyone who needs it, including any automation and trigger service accounts.
  3. Open the integration in the integration editor, and then click settings (**Integration settings**) in the editor toolbar. 

![The integration editor toolbar, with the Integration settings icon next to the Integration information icon, and the Publish button on the right](https://docs.cloud.google.com/static/application-integration/images/runas-sa-editor-toolbar.png)![The integration editor toolbar, with the Integration settings icon next to the Integration information icon, and the Publish button on the right](https://docs.cloud.google.com/static/application-integration/images/runas-sa-editor-toolbar.png)

  4. In the **Integration settings** pane, click the **Service account** list, and then select the service account. If it doesn't exist yet, click **New service account** to create it. 

![The Service account list open in the Integration settings pane, showing No service account and a list of service accounts in the project](https://docs.cloud.google.com/static/application-integration/images/runas-sa-select.png)![The Service account list open in the Integration settings pane, showing No service account and a list of service accounts in the project](https://docs.cloud.google.com/static/application-integration/images/runas-sa-select.png)

  5. Click **Save**. 

![The Integration settings pane with a service account selected in the Service account field, and the Save button](https://docs.cloud.google.com/static/application-integration/images/runas-sa-selected.png)![The Integration settings pane with a service account selected in the Service account field, and the Save button](https://docs.cloud.google.com/static/application-integration/images/runas-sa-selected.png)

  6. Click **Publish**. The new run-as service account takes effect for the runs that the published version handles. For more, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).



## Use one service account per integration

Google Cloud recommends using a dedicated, minimally scoped service account for each integration rather than one broadly privileged account shared across all of them, because it does the following:

  * Contains the effect of any one integration.
  * Shows up by name in your audit logs.



For more, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

## What's next

  * If publishing or a run fails after the change, see [Troubleshoot authorization errors](https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
