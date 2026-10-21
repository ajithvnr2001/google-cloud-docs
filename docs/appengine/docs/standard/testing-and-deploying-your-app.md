---
url: https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app/
title: Test and deploy your application \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:08:47.426925+00:00
---

# Test and deploy your application  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Test and deploy your application Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

Go Java Node.js PHP Python Ruby

Learn how to run your application locally, deploy it, and test on App Engine.

## Run locally

To test your application before deploying, run your application in your local environment with the development tools that you usually use. We recommend that you use standard Python tools, such as `virtualenv` to create isolated environments and `pytest` to run unit tests and integration tests, rather than depending on `dev_appserver`, the local development server provided with the Google Cloud SDK.

For example, you can usually run a Flask application with the Flask development server using:
    
    
    python main.py

Start Django applications using:
    
    
    python manage.py runserver

To simulate a production App Engine environment, run the full Web Server Gateway Interface (WSGI) server locally. Use the same command specified as entrypoint in your `app.yaml` file, for example:
    
    
    gunicorn -b :$PORT main:app

## Before deploying your application

Before deploying your application:

  * The [Owner](https://docs.cloud.google.com/appengine/docs/standard/access-control#owner) of the Google Cloud project must [set up your Google Cloud project for App Engine](https://docs.cloud.google.com/appengine/docs/flexible/managing-projects-apps-billing#create).
  * Ensure that your user account includes the [required privileges](https://docs.cloud.google.com/appengine/docs/standard/access-control#basic_roles).



## Deploy your application

Deploy your application to App Engine using the [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command. During deployment, the [Cloud Build](https://docs.cloud.google.com/build/docs) service builds a container image of your application to run in the standard environment. Each build is run in the same region as your Google Cloud project. For more information, see Manage build images.

To programmatically deploy your apps, use the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/deploying-overview). 

### Deploy a service

You deploy your application to App Engine by deploying versions of your application's services and each of their configuration files.

To deploy a version of your application's service, run the following command from the directory where the `app.yaml` file of your service is located:
    
    
    gcloud app deploy

Specifying no files with the command deploys only the `app.yaml` file in your current directory. By default, the `deploy` command generates a unique ID for the version that you deploy, deploys the version to the Google Cloud project you configured the Google Cloud CLI to use, and routes all traffic to the new version.

You can change the default behavior of the command by targeting specific files or including additional parameters:

  * To deploy the other configuration files of your service, you must target and deploy each file separately. For example: 
        
        gcloud app deploy cron.yaml
        gcloud app deploy dispatch.yaml
        gcloud app deploy index.yaml

  * To specify a custom version ID, use the `--version` flag.
  * To prevent traffic from being automatically routed to the new version, use the `--no-promote` flag.
  * To deploy to a specific Google Cloud project, use the `--project` flag.



For example, to deploy the service defined by the `app.yaml` file to a specific Google Cloud project, assign it a custom version ID, and prevent traffic from being routed to the new version:
    
    
    gcloud app deploy --project PROJECT_ID --version VERSION_ID --no-promote

For more information about this command, see the `gcloud app deploy` [reference](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy).

**Note:** You can [set properties](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) for the Google Cloud CLI and create and manage [SDK configurations](https://docs.cloud.google.com/sdk/docs/configurations) so you don't need to specify flags such as `--project` every time you deploy.

When you deploy a new version with the same name as an existing version, App Engine immediately migrates traffic to the new version. There is a latency spike when App Engine loads requests to the new version. The new version overwrites the previous one, and you won't be able to migrate the traffic to the previous version. All instances of the previous version are immediately shut down. For more information, see [Migrating traffic](https://docs.cloud.google.com/appengine/docs/standard/migrating-traffic#migrating_traffic_gradually).

### Deploy multiple services

You use the same deployment command for deploying or updating the multiple services that make up your application.

Before you begin:

  * You must initially deploy a version of your application to the `default` service before you can create and deploy subsequent services.
  * The ID of each of your services must be specified in their corresponding `app.yaml` configuration files. To specify the service ID, include the `service` element definition in each configuration file. By default, excluding this element definition from your configuration file deploys the version to the `default` service.



To deploy multiple services, separately deploy each service's `app.yaml` file. You can specify multiple files with a single `gcloud app deploy` command:
    
    
    gcloud app deploy service1/app.yaml service2/app.yaml

### View build logs

Cloud Build streams build and deploy logs that are viewable in the Cloud Build [Build history](https://console.cloud.google.com/cloud-build/builds) section of the Google Cloud console. To view builds in the app's region, use the **Region** menu to filter by the region.

### Manage build images

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

Each time you deploy a new version:

  1. App Engine creates a container image using the [Cloud Build](https://docs.cloud.google.com/build/docs) service.

  2. Cloud Build builds the container image in the app's region, and runs in the App Engine standard environment.

  3. App Engine stores built container images in [Artifact Registry](https://console.cloud.google.com/artifacts/). You can download these images to keep or run elsewhere.




After deployment is complete, App Engine no longer needs the container images. The container images aren't automatically deleted. To avoid reaching your storage quota, you can safely delete any images you don't need. However, if you might need the images in the future or want to keep a copy of the images, you need to export a copy prior to deletion. For more information about managing images in Artifact Registry, see [Manage images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images).

### Ignore files

You can use a `.gcloudignore` file to specify files and directories that won't be uploaded to App Engine when you deploy your services. This is useful for ignoring build artifacts and other files that don't need to be uploaded with your deployment.

**Note:** You cannot specify the `skip_files` field in your `app.yaml` file if you have a `.gcloudignore` file.

### View your application

After you deploy your application to App Engine, you can run the following command to launch your browser and view it at `https://PROJECT_ID.REGION_ID.r.appspot.com`:
    
    
    gcloud app browse

## Test on App Engine before shifting traffic

Before configuring a new version to receive traffic, you can test it on App Engine. For example, to test a new version of your `default` service:

  1. Deploy your new version, but prevent traffic from being automatically routed to the new version: 
         
         gcloud app deploy --no-promote

  2. Access your new version by navigating to the following URL:

`https://VERSION_ID-dot-default-dot-PROJECT_ID.REGION_ID.r.appspot.com`

**Note:** You can find the version ID in the [Google Cloud console](https://console.cloud.google.com/appengine/versions) or specify one when you deploy with the `--version flag`. The Google Cloud CLI also outputs the version ID when you deploy.

Now you can test your new version in the App Engine runtime environment. You can debug your application by viewing its logs. For more information, see [Writing Application Logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).

App Engine routes requests sent to `https://PROJECT_ID.REGION_ID.r.appspot.com` to the version previously configured to receive traffic.

  3. When you want to send traffic to the new version, use the Google Cloud console to migrate traffic:

[Manage versions](https://console.cloud.google.com/appengine/versions)

Select the version you just deployed and click **Migrate traffic**.




You can use the same process to test new versions of other services by replacing `default` in the URL with your service's name:

`https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com`

For more information about targeting specific services and versions, see [How requests are routed](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).

## Use build environment variables

You can set build environment variables for runtimes that support [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview).

Build environment variables are key-value pairs that you can specify to configure the buildpack you use to deploy your app. For example, you might want to specify compiler options.

Before you begin:

  * Keys must start with an uppercase ASCII letter, and can include uppercase ASCII letters, digits, and underscores.
  * You should avoid creating any variables with a `GOOGLE_*` key prefix.
  * The following keys are reserved for Google's use: 
    * `GOOGLE_RUNTIME`
    * `GOOGLE_RUNTIME_VERSION`
    * `GOOGLE_ENTRYPOINT`
    * `GOOGLE_DEVMODE`
  * You can use any key that is supported by [buildpacks](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs).



To use environment variables with buildpacks, specify the [`build_env_variables`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#build_environment_variables) field in your `app.yaml` file.

[Learn more](https://docs.cloud.google.com/docs/buildpacks/builders) about buildpacks.

## Use the local development server

The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) includes a local development server named `dev_appserver` that you can run locally to simulate your application running in production App Engine. This development server partially simulates the environment in which your application runs, allowing you to test apps written for any of the standard environment runtimes. 

### Run the local development server

**Important:** Before running the local development server, follow the [setup instructions](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server#set-up).

After you create the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/config/appref) configuration file for your app, you can start the local development server with the `dev_appserver.py` command to run your app locally.

  1. To obtain access credentials for your user account, run:
         
         gcloud auth login
         

  2. Allow your local application to temporarily use your user credentials for API access:
         
         gcloud auth application-default login
         

  3. To start the local development server:

In the directory that contains your `app.yaml` configuration file, run the `dev_appserver.py` command and specify your project ID and path to your `app.yaml` file:
         
         python3 CLOUD_SDK_ROOT/bin/dev_appserver.py --application=PROJECT_ID app.yaml

To change the port, include the `--port` option:
         
         python3 CLOUD_SDK_ROOT/bin/dev_appserver.py --application=PROJECT_ID app.yaml --port=9999

To test a Python 3 app, run `dev_appserver.py` with a Python 3 interpreter, you must specify the Python 3 binary in the `--runtime_python_path` flag, for example:
         
         python3 CLOUD_SDK_ROOT/bin/dev_appserver.py --runtime_python_path=/usr/bin/python3 --application=PROJECT_ID app.yaml --port=9999

To learn more about the `dev_appserver.py` command options, see [Local development server options](https://docs.cloud.google.com/appengine/docs/standard/tools/local-devserver-command).

  4. As the local development server starts, it sets up a development environment that pre-installs the dependencies found in your `requirements.txt` file.

  5. The local development server is now running and listening for requests. Visit <http://localhost:8080/> in your web browser to see the app in action.

If you specified a custom port with the `--port` option, remember to open your browser to that port.

  6. To stop the local server from the command line, press `Control-C` on your keyboard.




### Detect application runtime environment

To determine whether your code is running in production or in the local development server, you can check the `GAE_ENV` environment variable:
    
    
    if os.getenv('GAE_ENV', '').startswith('standard'):
      # Production in the standard environment
    else:
      # Local execution.

### Use the local development server with Google Cloud services

You can integrate `dev_appserver` with other Google Cloud components.

#### Cloud client libraries

Many Google Cloud client libraries depend on the presence of the `GOOGLE_CLOUD_PROJECT` environment variable, which should be your Google Cloud project ID. You can find its value by running the `gcloud config list project` command or looking at your project page in the [Google Cloud console](https://console.cloud.google.com/).

To ensure that this environment variable is set correctly during local development, initialize `dev_appserver` using the `--application=PROJECT_ID` parameter as shown in the example above.

#### Cloud emulators

You can test your application with emulators for [Cloud Datastore](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator), [Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/emulator) and [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs/emulator).

### Auto-reload `requirements.txt` and `app.yaml` changes

The local development server automatically installs dependencies found in your `requirements.txt` file. `dev_appserver` also allows you to test functionality that is configured via `app.yaml`. For example, you can test your app's ability to [serve static files](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files). When `dev_appserver` is running, any changes to `requirements.txt` and `app.yaml` automatically restarts your app to reflect these changes. This may result in a temporary delay as dependencies are downloaded and installed.

### Instance management and routing in the development server

#### Discover instance addresses

The local development server creates all manual scaling instances at startup. Instances for automatic and basic scaling services are managed dynamically. The server assigns a port to each service, and clients can depend on the server to load-balance and select an instance automatically. The port assignments for addressing each service appear in the server's log message stream.

Here are the ports for an app that defines three services:
    
    
    INFO Starting module "default" running at: http://localhost:8084
    INFO Starting module "service1" running at: http://localhost:8082
    INFO Starting module "service2" running at: http://localhost:8083

When you use a service's address, for example `http://localhost:8082/`, the server creates or selects an instance of the service and sends the request to that instance.

The server assigns unique ports to each instance of a service. You can use the admin server to discover these ports. There is a unique port for the admin server, which appears in the message log:
    
    
    INFO Starting admin server at: http://localhost:8000

This address takes you to the admin server console. Click on **Instances** to see the dynamic state of your app's instances

A separate entry appears for each manual and basic instance. The instance numbers are links with unique port addresses for each instance. Click on the link to send a request directly to that instance.

#### Dispatch files

If your app includes a `dispatch.yaml` file, the log messages stream includes a dispatcher port:
    
    
    INFO Starting dispatcher running at: http://localhost:8080

Requests to this port are routed according to the rules in the dispatch file. The server does **not** support `dispatch.yaml` file rules that include hostnames, for example, `url: "customer1.myapp.com/*"`. Rules with relative path patterns (`url: "*/fun"`), **do** work, so you can use URLs like `http://localhost/fun/mobile` to reach instances. The server reports an error in the log stream if you try to start an application with a `dispatch.yaml` file that contains host-based rules.

## Use Cloud Trace

Cloud Trace is useful for understanding how requests propagate through your application. You can inspect detailed latency information for a single request or view aggregate latency for your entire application.

To view trace details in Cloud Trace, you can follow [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces). In the [Trace explorer](https://console.cloud.google.com/traces/list), you can use the filters to filter by your specific App Engine service and version.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
