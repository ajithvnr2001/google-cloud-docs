---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/deploying-web-service/
title: Deploy your web service \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:23.359567+00:00
---

# Deploy your web service  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/deploying-web-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Deploy your web service Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Java web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-java-service).

This section of the guide shows how to use the gcloud CLI to deploy your Java web service on App Engine. To learn more about the Java runtime environment, see [Java Runtime Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime).

## Before you begin

  1. [Create a Google Cloud project with an App Engine app](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/creating-project).
  2. [Write a Java web server ready to deploy on App Engine](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/writing-web-service).
  3. [Install Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which provides the `gcloud` command-line tool. Ensure `gcloud` is configured to use the Google Cloud project you want to deploy to.



## Key points

  * Use `gcloud app deploy` and `gcloud app browse` to deploy and view your service.



## Deploy your service

In your `my-java-service` folder, where your Maven POM or Gradle build file is located, run the following command in your terminal:
    
    
    gcloud app deploy
    

Your source files are then uploaded to Cloud Storage. Cloud Build builds your app and deploys it to App Engine.

**Note:** Files listed in your [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file will not be uploaded.

### Deploy multiple services

You can add multiple services in your project by creating an `app.yaml` file for each service. Include the `service` attribute in each `app.yaml` file to specify the name of the service. To learn more about structuring your app using multiple services, see [Structuring Web Services in App Engine](https://docs.cloud.google.com/appengine/docs/standard/configuration-files#directory_structure).

To deploy multiple services, follow [these instructions](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#deploying_multiple_services)

Each deployed service will have its own assigned URL.

## View your service

To quickly launch your browser and access your web service at `https://PROJECT_ID.REGION_ID.r.appspot.com`, use the following command:
    
    
    gcloud app browse
    

## Services and versions

You've just created and deployed a service on App Engine. You can specify the name of your service in the `app.yaml` file. If the name is omitted, it is treated as `default`. The first service you deploy must be the default service.

You can update your service at any time by running the `gcloud app deploy` command again. Each time you deploy, a new version is created and traffic is automatically routed to the latest version.

To confirm that your service has been created and a version has been deployed:

  1. View your App Engine services in the Google Cloud console:

[View services](https://console.cloud.google.com/appengine/services)

You should see one service listed, named `default`. The default service is publicly accessible at the following URL:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

  2. View your versions:

[View versions](https://console.cloud.google.com/appengine/versions)

You should see one timestamped version listed, corresponding to your deployment.




To learn how to send requests to specific services and versions, see [How Requests are Routed](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).

## Next steps

Congratulations! You built an application that can store and classify uploaded images. Learn how to add other features to your application by exploring the following pages:

  * See more Java code samples for the App Engine standard environment on the [Google Cloud GitHub repository.](https://github.com/GoogleCloudPlatform/java-docs-samples/). These samples can be used for both Java.
  * Learn more about writing application logs and interpreting system logs in [Reading and writing application logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).
  * For a deeper dive into how App Engine works, see the [Java runtime environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime).



[ Previous arrow_back  Write your web service  ](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/building-app/writing-web-service)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
