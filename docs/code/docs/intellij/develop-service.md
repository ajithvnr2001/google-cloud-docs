---
url: https://docs.cloud.google.com/code/docs/intellij/develop-service/
title: Develop a service locally in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:44.748219+00:00
---

# Develop a service locally in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/develop-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Develop a service locally in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Code, you can develop your Cloud Run services locally in a Cloud Run-like environment. Cloud Code watches for changes in your source and quickly updates the running service to reflect these changes.

## Defining your run configuration

Before you run your service, you must create your run configuration:

  1. Navigate to Run/Debug configurations selector in the Navigation bar and click **Edit Configurations**.
  2. Under Cloud Code: Cloud Run, choose **Cloud Run: Run Locally**.
  3. If you want Cloud Code to redeploy your application automatically after your changes are saved, under **Watch mode - rebuild and redeploy** , select **On file save**. New Cloud Run services have **On demand** selected by default. For more information about watch modes, see [Watch modes](https://docs.cloud.google.com/code/docs/intellij/watch-modes).
  4. Specify your builder option and its relevant settings.

Cloud Code supports Docker, Jib, and Buildpacks [artifact types](https://skaffold.dev/docs/builders/).

  5. Click **OK**.




### Optional: Customizing your configuration

When developing locally, you can specify additional settings like a service account, environment variables, and SQL connections (when using Cloud Run (fully managed)), using the Advanced revision settings section when you choose **Edit Configurations**.

#### Environment variables

The following environment variables are automatically added to the running containers:

Name  | Description  | Example   
---|---|---  
PORT  | The port your HTTP server should listen on.  | 8080   
K_SERVICE  | The name of the Cloud Run service being run.  | hello-world   
K_REVISION  | The name of the Cloud Run revision being run.  | hello-world.1   
K_CONFIGURATION  | The name of the Cloud Run configuration that created the revision.  | hello-world   
  
## Storing secrets

If your code includes potentially sensitive data like API keys, passwords, and certificates, it is recommended you store them as secrets. With Cloud Code, you can securely store these secrets in Secret Manager and programmatically fetch them when you need them. For a detailed look at how you can create and manage secrets with Cloud Code, refer to the [Secret Manager guide](https://docs.cloud.google.com/code/docs/intellij/secret-manager).

## Running your service

To run your service, follow these steps:

  1. Choose the **Cloud Run: Run Locally** run target from the Run/Debug configurations selector in the Navigation bar.
  2. Click ![run action icon](https://docs.cloud.google.com/static/code/docs/intellij/images/run-action-icon.png)**Cloud Run: Run Locally**.
  3. View the logs from your running service, streamed directly to the **output window**.
  4. Once deployment is complete, you can view your running service by following the URL displayed in your Event Log panel. In the example below, this URL is http://localhost:8080.

![Event log with successful deployment notification and URL to preview your service](https://docs.cloud.google.com/static/code/docs/intellij/images/local-cloud-run-app.png)




## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
