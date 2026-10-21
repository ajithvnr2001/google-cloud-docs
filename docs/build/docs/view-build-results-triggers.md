---
url: https://docs.cloud.google.com/build/docs/view-build-results-triggers/
title: View build results for build triggers \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:07.914442+00:00
---

# View build results for build triggers  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/view-build-results-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  View build results for build triggers Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view information about your Cloud Build builds using the [Cloud Build dashboard](https://console.cloud.google.com/cloud-build/dashboard) in Google Cloud console.

The Cloud Build dashboard provides a high-level overview of your most recent builds for each build trigger.

The dashboard is organized by cards, where each card is associated with a build trigger in your repository. If there are multiple triggers created in a single repository, there will be multiple cards. These cards are ordered alphabetically by the name of your repository followed by the name of the trigger. You can also pin any card to the top of the page by hovering over the right side of the card and clicking on the pin icon as indicated in the example below:

![Screenshot of an example card on the dashboard](https://docs.cloud.google.com/build/images/dashboard-card-example.png)

Cards are titled by the latest outcomes of the build, such as **Successful** or **Failed**. The name of the repository and the trigger name follow the result of the latest outcome. Under the title, the card summarizes results related to your most recent builds.

## View the dashboard

The Cloud Build dashboard is populated if you have build triggers set up. To learn more about how to set up build triggers, see [Creating and managing build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

To view the Cloud Build dashboard:

  1. Go to the Cloud Build dashboard page:

[Open the Cloud Build dashboard page](https://console.cloud.google.com/cloud-build)

  2. Select your project from the drop-down menu.




You will see the Cloud Build dashboard listing recent builds for your build triggers.

The Cloud Build dashboard displays the following information:

  * **Latest build** : The date and time of your most recent build.

  * **Duration** : The duration of your most recent build, in `HH:MM:SS` format.

  * **Source** : Links to your connected source repository. Your source repository can either be a [Cloud Source Repository](https://docs.cloud.google.com/source-repositories/docs/creating-an-empty-repository), a GitHub repository, a Bitbucket repository, or a GitLab repository.

  * **Commit** : Links to the commit that was used for your build.

  * **Failed Step** : The failed step that resulted in the build failure, if your most recent build has failed.

If your most recent build has failed, **Failed step** will link to the step that caused the failure in your build log.

  * **Build History** : A bar chart representing the build duration for your 20 most recent builds. You can hover over each bar in the bar chart to view information about each individual build.

  * **Average Duration** : The average runtime of your 20 most recent builds, not including builds that are still running.

If the average duration of your build time exceeds 10 minutes and the [machine type](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build.MachineType) you specified for your build is `E2_MEDIUM`, `E2_HIGHCPU_8` or `N1_HIGHCPU_8`, you will see the **IMPROVE SPEED** button. You can click on **IMPROVE SPEED** to view recommendations on how to improve the speed of your build. To learn more, see [Best practices for speeding up builds](https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds).

  * **Pass - Fail %** : The average pass/fail ratio of your 20 most recent builds.




## Filter cards

To filter cards on your dashboard, click the **Filter triggers** option at the top of the Cloud Build dashboard page:

![Screenshot of filtering triggers prompt](https://docs.cloud.google.com/build/images/dashboard-filter-triggers.png)

You can filter cards by:

  * **Trigger source** : the name of your source repository.
  * **Trigger name** : the name of your trigger.
  * **Trigger description** : the description of your trigger.



## What's next

  * Learn how to [store and view build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs).
  * Learn how to [configure notifications using the Slack notifier](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-slack).
  * Learn how to [configure notifications using the SMTP notifier](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
