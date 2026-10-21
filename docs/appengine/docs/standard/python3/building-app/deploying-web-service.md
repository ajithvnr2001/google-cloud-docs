---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service/
title: Deploy your web service \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:25.289628+00:00
---

# Deploy your web service  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service/

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

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python3/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

Use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/app) to deploy your web service to App Engine.

Though this initial version of the web service doesn't have Firestore in Datastore mode (Datastore) or Firebase authentication, you can deploy it to App Engine at this stage to test and ensure that it works as expected.

## Before you begin

If you have completed all the previous steps in this guide, skip this section. Otherwise, complete one of the following:

  * Start from [Build a Python 3 App](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app) and complete all the steps leading up to this one.

  * If you already have a [Google Cloud project](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project), you can continue by downloading a copy of the web service:

    1. Download the sample application repository using [Git](https://git-scm.com/):
           
           git clone https://github.com/GoogleCloudPlatform/python-docs-samples
           

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and then extract it.

    2. Navigate to the directory that contains a copy of the files from the previous step:
           
           cd python-docs-samples/appengine/standard_python3/building-an-app/building-an-app-1
           




## Deploy your service

To deploy your web service, you run the [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command from the root directory of your project, where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

Each time that you deploy your web service, a new [version](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine) of that app is created in App Engine. During deployment, a container image is created using the [Cloud Build](https://docs.cloud.google.com/container-builder/docs) service, and then a copy is uploaded to Google Cloud Storage before it is run in App Engine.

For more information about deploying to App Engine, see [Testing and Deploying Your App](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app).

**Note:** Files listed in your [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file are not uploaded to App Engine during deployment.

## Viewing your service

To quickly launch your browser and access your web service at `https://PROJECT_ID.REGION_ID.r.appspot.com`, enter the following command:
    
    
    gcloud app browse
    

**Tip:** If you would like to change the URL of your web service to something other than the default `https://PROJECT_ID.REGION_ID.r.appspot.com` URL, you can [add a custom domain](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains).

## Managing services and versions

You've just deployed a version of the web service to App Engine. Each time that you deploy a version of your code, that version is created in a service. The initial deployment to App Engine must be created in the `default` service, but for subsequent deployments, you can [specify the name of your service in your `app.yaml` file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#service).

You can update a service at any time by running the `gcloud app deploy` command and deploying new versions to that service. Each time that you update a service, traffic is automatically routed to the version last deployed. However, you can include [`gcloud` flags](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) to change the deploy command behavior.

Use the Google Cloud console to manage and view the services and versions that you deploy to App Engine:

  * Use the Google Cloud console to view your App Engine services:

[Go to the services page](https://console.cloud.google.com/appengine/services)

  * Use the Google Cloud console to view your versions:

[Go to the versions page](https://console.cloud.google.com/appengine/versions)




For more information about the multi-service design pattern, see [An Overview of App Engine](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine). To learn how to send requests to specific services and versions, see [Splitting Traffic](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic).

## Next steps

Now that you have a Python service running on App Engine, you're ready to learn how to handle data with Datastore.

[ Previous arrow_back  Write your web service  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service)

[ Next Handle data  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/storing-and-retrieving-data)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
