---
url: https://docs.cloud.google.com/code/docs/shell/deploy-service/
title: Deploy a service in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:43.062269+00:00
---

# Deploy a service in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/deploy-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Deploy a service in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to deploy a service to Cloud Run using Cloud Code for Cloud Shell.

## Deploying a service to Cloud Run

To deploy your service to Cloud Run:

  1. Open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Deploy to Cloud Run** command.

  2. In the **Deploy to Cloud Run** pane, set your Google Cloud project.

  3. Select a preexisting service or create a new one.

  4. If you're creating a new service, choose your platform preferences under **Deployment Platform** , either **Cloud Run (fully managed)** or **Knative serving**. For help choosing the best option for your development needs, see the [Choosing your platform guide](https://docs.cloud.google.com/run/docs/choosing-a-platform).

  5. If you selected **Cloud Run (fully managed)** , choose a region to deploy to.

  6. (Optional) To specify additional settings like service account, environment variables, and SQL connections, expand the **Advanced revision settings** section.

The following environment variables are automatically added to the running containers:

Name  | Description  | Example   
---|---|---  
PORT  | The port your HTTP server should listen on.  | 8080   
K_SERVICE  | The name of the Cloud Run service being run.  | hello-world   
K_REVISION  | The name of the Cloud Run revision being run.  | hello-world.1   
K_CONFIGURATION  | The name of the Cloud Run configuration that created the revision.  | hello-world   
  7. Under Build environment, specify whether to build locally or using Cloud Build.

  8. Specify your builder (Docker or Buildpack) and its settings.

  9. After you define your preferred settings, click **Deploy**.

Cloud Code for Cloud Shell builds your image, pushes it to the registry, and deploys your service to Cloud Run. Your service is now live!

  10. View your running service by following the URL displayed in the **webview**.

You can also view details of your running service by clicking the **Show Detailed Logs** button and looking through your verbose logs in the output window.

![URL of the running service displayed in Deploy to Cloud Run UI and Show detailed logs button underneath](https://docs.cloud.google.com/static/code/docs/vscode/images/cccr-deploy-url.png)

  11. After your session completes, right-click to use the following commands:

     * **View Logs:** Open the application logs of a specific deployment with the Cloud Code Logs Explorer
     * **Open URL:** Open the application service URL of a specific service in a web browser
  12. If you've turned off watch mode in your launch configuration and you want to make changes to your application and rebuild and redeploy the application, click the Cloud Code status bar and then click **Turn on watch mode**. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
