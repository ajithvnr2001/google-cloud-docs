---
url: https://docs.cloud.google.com/appengine/docs/flexible/nodejs/create-app/
title: Quickstart: Create a Node.js app in the App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:33.879715+00:00
---

# Quickstart: Create a Node.js app in the App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/nodejs/create-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Node.js app in the App Engine flexible environment

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Node.js web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service).

This quickstart demonstrates how to create and deploy an app that displays a short message. You can use the sample application in this quickstart for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#nodejs) version of Node.js, by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime#newversions) file.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles: 

  * [App Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`) on the project
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`) on the project
  * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the project
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account
  * Ask your administrator to grant the following roles for the App Engine default service account: 
    * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the project
    * [Cloud Build Service Account ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`) on the project
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Additional prerequisites

  1. Initialize your App Engine app with your project and choose its region:
         
         gcloud app create --project=[YOUR_PROJECT_ID]
         

When prompted, select the [region](https://docs.cloud.google.com/appengine/docs/flexible/locations) where you want to locate your App Engine application.

**Caution** : You cannot change an app's region once it has been set.
  2. Install the following on your local machine:

     * [Download and install Git](https://git-scm.com/). 
     * [Prepare your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup). 




### App Engine locations

App Engine is _regional_ , which means the infrastructure that runs your apps is located in a specific region, and Google manages it so that it is available redundantly across [all of the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).

Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your apps are run. You can generally select the region nearest to your app's users, but you should consider [the locations where App Engine is available](https://cloud.google.com/about/locations/#region) as well as the [locations](https://cloud.google.com/about/locations/#region) of the other Google Cloud products and services that your app uses. Using services across multiple locations can affect your app's latency as well as its [pricing](https://cloud.google.com/appengine/pricing).

You cannot change an app's region after you set it.

**Note:** Two locations, which are called `europe-west` and `us-central` in App Engine commands and in the Google Cloud console, are called `europe-west1` and `us-central1`, respectively, elsewhere in Google documentation.

If you already created an App Engine application, you can view its region by doing one of the following:

  * Run the `gcloud app describe` command.

  * Open the [App Engine Dashboard in the Google Cloud console](https://console.cloud.google.com/appengine). The region appears near the top of the page.




OK

This quickstart demonstrates a simple Node.js application written with the [Express.js](http://expressjs.com/) framework.

**Important:** For the best experience on Windows, upgrade to the latest version of Node.js package manager (`npm`) by running `npm install -g npm`. The latest `npm` installs dependencies in a flat directory structure, so installations are unlikely to conflict with the Windows maximum path length of 255 characters. If you prefer to keep using an older version of `npm`, you can reduce the length of paths by moving your project to the root of your drive, for example, `C:\`.

## Download the Hello World app

We've created a Hello World app for App Engine so you can quickly get a feel for deploying an app to the Google Cloud. 

  1. Clone the Hello World sample app repository to your local machine.
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples
         

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the sample code.
         
         cd nodejs-docs-samples/appengine/hello-world/flexible/
         




## Run Hello World on your local machine

  1. Install dependencies for this project.
         
         npm install
         

Or if you are using Yarn.
         
         yarn install
         

  2. Run the start script.
         
         npm start
         

Or if you are using Yarn.
         
         yarn start
         

  3. View your app in your web browser.

     * If you are using Cloud Shell, in the toolbar, click **Web Preview**![](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg) and select **Preview on port 8080** instead.

     * If you are not using Cloud Shell, enter the following address:

<http://localhost:8080>




The **Hello World** message from the sample app displays on the page. In your terminal window, press **Ctrl+C** to exit the web server.

## Deploy and run Hello World on App Engine

To deploy your app to the App Engine flexible environment: 

  1. Deploy the Hello World app by running the following command from the `hello-world/flexible/` directory: 
         
         gcloud app deploy

Learn about the  optional flags. 

### Common `gcloud` command flags

     * Include the `--version` flag to specify an ID that uniquely identifies that version of your app, otherwise one is generated for you. Example: `--version [YOUR_VERSION_ID]`
     * Include the `--project` flag to specify an alternate Google Cloud project ID to what you initialized as the default in the `gcloud` tool. Example: `--project [YOUR_PROJECT_ID]`

Example:
    
    gcloud app deploy --version pre-prod-5 --project my-sample-app

To learn more about deploying your app from the command line, see [ Testing and Deploying Your App](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app) . For a list of all the command flags, see the `[gcloud app deploy](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy)` reference.

OK

**Note:** During deployment `npm install` is used by default to install dependencies unless a `yarn.lock` file exists and isn't listed in the `app.yaml` file's `skip_files` section, in which case `yarn install --production` is used instead. To cause the build to fall back to `npm install` delete the `yarn.lock` file or add `yarn.lock` to the `skip_files` section of your `app.yaml` file. 
  2. Launch your browser to view the app at `https://PROJECT_ID.REGION_ID.r.appspot.com`
         
         gcloud app browse

where `PROJECT_ID` represents your Google Cloud project ID. 



This time, the page that displays the Hello World message is delivered by a web server running on an App Engine instance.

**Congratulations!** You've deployed your first App Engine app to the App Engine flexible environment!

If you encountered any errors deploying your application, check the [troubleshooting tips](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app#troubleshooting). 

See the following sections for information about cleaning up as well as links to possible next steps that you can take. 

## Clean up

To avoid incurring charges, you can delete your Google Cloud project to stop billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

#### Learn the whole platform

Now that you know what it's like to develop and deploy App Engine apps, you can explore the rest of Google Cloud. You already have the Google Cloud CLI installed which gives you the tools to interact with products like Cloud SQL, Cloud Storage, Firestore, and more.

#### Learn about the App Engine flexible environment

Here are some topics to help continue your learning about App Engine:

  * [An overview of App Engine](https://docs.cloud.google.com/appengine/docs/flexible/an-overview-of-app-engine)
  * [Request routing](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed)
  * [Request handling](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-handled)
  * [Managing instances](https://docs.cloud.google.com/appengine/docs/flexible/how-instances-are-managed)



## Hello World code review

Hello World is the simplest possible App Engine app, as it contains only one service, has only one version, and all of the code is located within the app's root directory. This section describes each of the app files in detail.

#### `app.js`

The `app.js` file contains the JavaScript code to start a server and respond to requests.

The following code responds to requests from web clients by displaying the 'Hello World' message, via a server that runs on port `8080`.
    
    
    const express = require('express');
    
    const app = express();
    
    app.get('/', (req, res) => {
      res.status(200).send('Hello, world!').end();
    });
    
    // Start the server
    const PORT = parseInt(process.env.PORT) || 8080;
    app.listen(PORT, () => {
      console.log(`App listening on port ${PORT}`);
      console.log('Press Ctrl+C to quit.');
    });

#### `app.yaml`

The [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/configuring-your-app-with-app-yaml) file describes the following configuration for your app:

  * Sets `env: flex`, indicating your app uses the [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).
  * Specifies the runtime used by the app. 
        
        runtime: nodejs
        env: flex
        runtime_config:
          operating_system: ubuntu24
        # This sample incurs costs to run on the App Engine flexible environment.
        # The settings below are to reduce costs during testing and are not appropriate
        # for production use. For more information, see:
        # https://cloud.google.com/appengine/docs/flexible/nodejs/configuring-your-app-with-app-yaml
        manual_scaling:
          instances: 1
        resources:
          cpu: 1
          memory_gb: 0.5
          disk_size_gb: 10
        

    * For more information on how the Node.js runtime works, see [The Node.js runtime](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime).

    * For more details about how to design your app to take advantage of versions and services, see [An overview of App Engine](https://docs.cloud.google.com/appengine/docs/flexible/an-overview-of-app-engine).

    * For more details about the configuration settings for App Engine, see [Configuring your app with app.yaml](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/configuring-your-app-with-app-yaml).

#### `package.json`

[`package.json`](https://docs.npmjs.com/files/package.json) is used to specify app dependencies, node version, and app startup.
    
    {
      "name": "appengine-hello-world",
      "description": "Simple Hello World Node.js sample for Google App Engine Flexible Environment.",
      "version": "0.0.2",
      "private": true,
      "license": "Apache-2.0",
      "author": "Google Inc.",
      "repository": {
        "type": "git",
        "url": "https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "scripts": {
        "start": "node app.js",
        "test": "c8 mocha -p -j 2 --exit test/*.test.js"
      },
      "dependencies": {
        "express": "^5.0.0"
      },
      "devDependencies": {
        "c8": "^12.0.0",
        "mocha": "^10.0.0",
        "supertest": "^7.0.0"
      }
    }
    

In the preceding example, the `package.json` file specifies that the app uses Node.js version 18 and later, and depends on [express](http://expressjs.com). For more details about how to install and run your app, see the [Node.js runtime documentation](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
