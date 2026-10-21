---
url: https://docs.cloud.google.com/code/docs/shell/develop-service/
title: Develop a Cloud Run service locally in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:49.074691+00:00
---

# Develop a Cloud Run service locally in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/develop-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Develop a Cloud Run service locally in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Before you [deploy a service to Cloud Run](https://docs.cloud.google.com/code/docs/shell/deploy-service), you can develop it locally using a Cloud Run emulator.

## Configuring your service for development

If you don't have a `.vscode/launch.json` file defined, the **Run/Debug on Cloud Run Emulator** dialog lets you configure your launch and then saves your settings to `.vscode/launch.json`. If you have a `.vscode/launch.json` file configured, you can edit the file directly.

To run your service locally, specify your configuration:

  1. Open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Run on Cloud Run Emulator** command.
  2. In the Run/Debug on Cloud Run Emulator dialog, set the specifications for your configuration:

     * Only locally-installed build tools are available for Cloud Run Emulator
     * Choose **Docker** or **Buildpacks** as your builder and then specify the source
     * (Optional) To specify any environment variables to pass to the running containers, expand **Advanced Build Settings** and then click to specify key-value pairs. Name  | Description  | Example   
---|---|---  
PORT  | The port for the HTTP server to listen on.  | 8080   
K_SERVICE  | The name of the Cloud Run service being run.  | hello-world   
K_REVISION  | The name of the Cloud Run revision being run.  | hello-world.1   
K_CONFIGURATION  | The name of the Cloud Run configuration that created the revision.  | hello-world   
     * (Optional) To specify Cloud SQL connections, expand **Advanced Service Settings** , click **Connections** , and then specify one Cloud SQL connection per line.
     * (Optional) Check the **Make the service accessible from other devices on the local network** option.
     * (Optional) If you only want to rebuild and run your service manually, instead of automatically when you make a change, clear the **Automatically re-build and re-run on changes** option.



## Running your service locally

  1. After you define your preferred settings, run your service by clicking **Run**.

  2. Monitor the status of your deployment in the **output window**.

After deployment is complete, you can view your running service by opening the URL displayed in the output window.

  3. To view verbose logs, switch to the detailed Cloud Run view in the output window.

![Output pane with hello-world-5 - Detailed selected from output channel dropdown](https://docs.cloud.google.com/static/code/docs/vscode/images/cloud-run-detailed-logs.png)

  4. After your session completes, right-click to use the following commands:

     * **View Logs:** Open the application logs of a specific deployment with the Cloud Code logs explorer.
     * **Open URL:** Open the application service URL of a specific service in a web browser.
  5. If you've turned off watch mode in your launch configuration and you want to make changes to your application and rebuild and redeploy the application, click the Cloud Code status bar and then click **Turn on watch mode**. 

  6. To stop your deployment, you can click the **Stop** button in the action bar for your current deployment.

![Action bar for Cloud Run deployment](https://docs.cloud.google.com/static/code/docs/vscode/images/action-bar.png)




## Storing secrets

If your code includes potentially sensitive data like API keys, passwords, and certificates, storing them as secrets can help secure them. The Cloud Code Secret Manager integration lets you securely store these secrets and fetch them programmatically. For a detailed look at how you can create and manage secrets with Cloud Code, see the [Secret Manager guide](https://docs.cloud.google.com/code/docs/shell/secret-manager). 

## Customizing an existing launch.json configuration

The Cloud Code plugin updates the `launch.json` configuration file automatically when you choose a run action. To further customize how your service is run, you can specify the following fields in your `.vscode/launch.json` file:

  * **watch** : Watches for changes in the workspace and reruns the service. True by default.

The following sample shows watch set to `true`:
        
        "watch": true,
        

  * **build** : Specify the builder ([Docker](https://skaffold.dev/docs/pipeline-stages/builders/docker/), jibMaven, jibGradle, or [buildpacks](https://skaffold.dev/docs/pipeline-stages/builders/buildpacks/)) to build your images with.

The following sample shows a Docker builder:
        
        "build": {
          "docker": {
            "path": "Dockerfile"
          }
        },
        

The following sample shows a buildpack builder:
        
        "build": {
          "buildpacks": {
            "path": "src/requirements.txt",
            "builder": "gcr.io/buildpacks/builder:v1"
          }
        },
        

  * **image** : Specify the name of the image to use.

The following sample shows how to specify an image name:
        
        "image": "hello-world",
        

  * **service** : Specify the Cloud Run service to use.

The following sample shows how to specify a service name, port, and resource limits:
        
        "service": {
          "name": "hello-world",
          "containerPort": 8080,
          "resources": {
            "limits": {
              "memory": "256Mi"
            }
          }
        },
        

  * **debug** : Specify debug settings such as remote path mapping to map a local path to a path on the remote container.

The following sample shows a debug section that indicates the source files' location:
        
        "debug": {
          "sourceFileMap": {
            "${workspaceFolder}": "/app"
          }
        }
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
