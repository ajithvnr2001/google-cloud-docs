---
url: https://docs.cloud.google.com/application-integration/docs/integration-versions/
title: Integration versions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:54.486559+00:00
---

# Integration versions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/integration-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration versions

Integrations are design time entities that are often developed in collaboration with multiple authors. Although an integration can only be actively edited by one author at a time, teams can collaborate on an integration and track changes in state through its _versions_. 

A version of an integration can be in any of the following states: 

  * `DRAFT`: The state of an integration version actively being edited by an author. When an integration is in `DRAFT`, edit capabilities are only available to the current author. The integration is locked for editing by others for 15 minutes from the last update. Locks are released after 15 minutes from the last update.
  * `SNAPSHOT`: When a new author takes over editing a version, the existing version is converted to `SNAPSHOT` and a new `DRAFT` is created.
  * `ACTIVE`: The state of a published version.
  * `DELETED`: The state of a version that has been deleted by an author, or remains untouched for a specified period of time.



Only a `DRAFT` version of the integration is editable and only an `ACTIVE` version of the integration can be run from the integration editor or fired by a configured trigger. For information about editing integrations and edit locks, see [Edit and view integrations](https://docs.cloud.google.com/application-integration/docs/view-integration-details). 

## Viewing Version History

To view the version history of an integration, use the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select an existing integration. This opens the integration in the _integration editor_. 
  4. Click the **Version** drop-down in the designer toolbar. The drop-down lists all available versions of the integration, along with a color indicating the version status: 
     * **Green** : The version is currently active.
     * **Yellow** : The version is currently being edited.
     * **Gray** : The version is inactive.
  5. Click on a version, and the integration editor displays the requested version in its last modified state.



## Create a new version

To create a new version of an existing integration: 

  1. Click the **Version** drop-down in the integration editor toolbar. 
  2. Select **Create New Version**.
  3. (Optional) Add a label to the new version to help other editors identify the version.
  4. Click **OK**.



## Delete a version

To delete a version of an integration that is no longer in use, perform the following steps: 

**Caution** : Deleting all versions of an integration will result in deleting the entire integration. 

  1. Click the **Version** drop-down, and select the version to delete. 

The integration editor displays the requested version in its last modified state. 

  2. In the toolbar, click  more_vert  (Actions menu) and select **Delete the current version**.
  3. In the confirmation dialog, click **OK**. 



## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
