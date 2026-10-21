---
url: https://docs.cloud.google.com/code/docs/intellij/create-app-from-custom-sample/
title: Create a new application from a custom sample in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:36.576002+00:00
---

# Create a new application from a custom sample in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/create-app-from-custom-sample/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Create a new application from a custom sample in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use custom samples with Cloud Code, you need to have Git version 2.25.0 or later installed on your local machine.

Once you've [set up your sample repository](https://docs.cloud.google.com/code/docs/intellij/set-up-sample-repo) (or one has been set up for you), you can start creating applications with these samples.

Alternatively, you can import the [Cloud Code sample repository](https://github.com/GoogleCloudPlatform/cloud-code-custom-samples-example/) if you'd just like to try out the custom sample experience. To better understand how custom sample repositories are set up, it is recommended that you try forking the repository and modifying its structure and content before importing it. You can do this by creating new samples within the repository or modifying the source code to create your own versions of the Hello World or Kubernetes Custom Sample apps.

## Creating your app from an imported sample

To create a new application using one of the samples from your sample repository, follow these steps:

  1. Copy the Git URL of the sample repository that you'd like to use.

**Note:** Using a **HTTPS** Git URL is recommended. If you'd like to use a SSH URL instead, you'll need to make sure your local machine is set up correctly. Refer to your Git repository hosting service (such as [GitHub](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh), [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/), and [GitLab](https://docs.gitlab.com/ee/user/ssh/)) for detailed instructions on generating and configuring SSH keys.**Note:** If you're using a Git repository hosted live on your local machine, its URL should be of the form `/path/to/repo`, without a '.git' suffix.
  2. Navigate to the Custom Samples settings page with **File** > **Settings** > **Tools** > **Cloud Code** > **Custom Samples** or for Mac OS X, **IntelliJ IDEA** > **Preferences** > **Tools** > **Cloud Code** > **Custom Samples**.

![Custom application sample repositories page with table with columns, Repository URL and Branch](https://docs.cloud.google.com/static/code/docs/intellij/images/sample-repo-ui.png)

  3. Click **\+ Add** to open the Repository for Custom Application Samples dialog.

  4. Enter the Git URL you copied earlier in the Repo URL field and click **Next**.

The URL in this example is of the HTTPS GitHub format: `https://github.com/username/repo-name.git`.

![Git URL filled with HTTPS format URL: https://github.com/GoogleCloudPlatform/cloud-code-samples.git](https://docs.cloud.google.com/static/code/docs/intellij/images/custom-repo-url.png)

  5. Click **Add** to authorize your use of the repository in your IDE, if necessary, and to add the sample repository to your IDE.

  6. If your repository addition is successful, you'll see a ![Green checkmark in status column](https://docs.cloud.google.com/static/code/docs/intellij/images/intellij-green-checkmark-for-repo.png) green check mark in the Status column of your table of sample repositories. The branch field is automatically populated with the repository's default branch. To edit the branch, select the project and click the table's edit button.

If a warning icon is displayed in the Status column, hold your pointer over the icon to get more information about why your repository is not valid.

  7. To update your repository accordingly and check the repository's status in your IDE, click ![Reload Repositories button icon](https://docs.cloud.google.com/static/code/docs/intellij/images/intellij-reload-repositories-button.png)**Reload Repositories**

  8. Create a new project by navigating to **File** > **New** > **Project**.

  9. Select **Cloud Code: Custom**.

  10. To use the latest version of your samples in Cloud Code, click **Refresh**.

![Refresh button for custom samples](https://docs.cloud.google.com/static/code/docs/intellij/images/intellij-refresh-custom-samples.png)

  11. Choose a sample from the list of available custom samples and click **Next** to proceed.

![List of custom samples available when creating a new Cloud Code app](https://docs.cloud.google.com/static/code/docs/intellij/images/custom-sample-new-app.png)

  12. Pick a name and project location for your new app.

Once you click **Finish** , Cloud Code creates your app using your chosen sample and opens it for use.




## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
