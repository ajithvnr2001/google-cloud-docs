---
url: https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app/
title: Test and deploy your application \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:33.101197+00:00
---

# Test and deploy your application  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Test and deploy your application Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

Go Java Node.js PHP Python Ruby .NET Custom

Learn how to run your application locally, deploy it, and test on App Engine.

## Run locally

To test your application before deploying, run your application in your local environment with the development tools that you usually use. For example, you can usually run a Flask application with the Flask development server using:
    
    
    python main.py
    

Start Django applications using:
    
    
    python manage.py runserver
    

To simulate a production App Engine environment, you can run the full Web Server Gateway Interface (WSGI) server locally. Use the same command specified as `entrypoint` in your `app.yaml` file, for example:
    
    
    gunicorn -b :$PORT main:app
    

## Deploy your application

Deploy your application to App Engine by using the [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command. 

The [Cloud Build](https://docs.cloud.google.com/build/docs) service automatically builds your deployment into a container image and deploys the image to the App Engine flexible environment. The container includes any local modifications that you've made to the runtime image.

To programmatically deploy your apps, use the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/deploying-overview).

### Before you begin

Before you can deploy your application:

  * The [Owner](https://docs.cloud.google.com/appengine/docs/flexible/access-control#owner) of the Google Cloud project must [set up your Google Cloud project for App Engine](https://docs.cloud.google.com/appengine/docs/standard/managing-projects-apps-billing#create).

  * Ensure that your user account includes the [required privileges](https://docs.cloud.google.com/appengine/docs/flexible/access-control#basic_roles).




### Ensure successful deployment

If you enable [updated health checks](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#updated_health_checks), deployments are rolled back if your application does not reach healthy status. When you deploy your first application to the flexible environment, there might be a delay as your virtual machine (VM) and other infrastructure are set up. After the initial setup, the health checks make sure that your instance is healthy and ready to receive traffic. If your application does not reach ready status in a specified amount of time, indicated by the `initial_delay_sec` field in the `liveness_check` section of your `app.yaml` file, then your deployment fails and is rolled back.

Your application might need more time to become ready. For example, you might initialize your application by downloading large files or preloading caches. If you are using [updated health checks](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#updated_health_checks), you can increase the amount of time by modifying the `app_start_timeout_sec` configuration setting in the `readiness_check` section of in your `app.yaml` file.

If your deployment fails, make sure the Cloud Build API is [enabled in your project](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis). App Engine enables this API automatically the first time you deploy an app, but if someone has since disabled the API, deployments fail.

### Deploy a service

You deploy your application to App Engine by deploying versions of your application's services and each of their configuration files.

To deploy your application's service, run the following command from the directory where the `app.yaml` file of your service is located:
    
    
    gcloud app deploy
    

By default, the `gcloud app deploy` command deploys only the `app.yaml` file in your current directory. Whenever you run this command, App Engine generates a unique ID for the version that you deploy, deploys the version to the Google Cloud project you configured the gcloud CLI to use and routes all traffic to the new version. The new version becomes the default version.

**Note:** It is a good practice to check the App Engine [**Versions**](https://console.cloud.google.com/appengine/versions) page in the Google Cloud console or run `gcloud app versions list` after running the `gcloud app deploy` command to verify the version that is receiving traffic.

You can change the default behavior of the deploy command by targeting specific files, specifying versions, or including additional parameters:

  * You can deploy the other [configuration files](https://docs.cloud.google.com/appengine/docs/flexible/configuration-files) of your service by targeting and deploying each file separately, for example:
        
        gcloud app deploy cron.yaml
        gcloud app deploy dispatch.yaml
        gcloud app deploy index.yaml
        

  * To specify a custom version ID, use the `--version` flag.

  * To prevent traffic from being automatically routed to the new version, use the `--no-promote` flag.

  * To deploy to a specific Google Cloud project, use the `--project` flag.




For example, to deploy the service defined by the `app.yaml` file to a specific Google Cloud project, assign the service a custom version ID and prevent traffic from being routed to the new version:
    
    
    gcloud app deploy --project PROJECT_ID --version VERSION_ID --no-promote

For more information, see the [`gcloud app deploy` reference](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy).

You can [set properties](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) for the gcloud CLI and create and manage [SDK configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations) so you don't need to specify flags such as `--project` every time you deploy.

When you deploy a new version with the same name as an existing version, App Engine immediately migrates traffic to the new version. There is a latency spike when App Engine loads requests to the new version. The new version overwrites the previous one, and you won't be able to migrate the traffic to the previous version. When you deploy a new version with the same name as the previous version, App Engine deploys the new container image to your existing virtual machines for a faster deployment, and updates your application's container on the existing virtual machines.

### Deploy multiple services

You use the same deployment command for deploying or updating the multiple services that make up your application.

Before you begin:

  * You must initially deploy a version of your application to the `default` service before you can create and deploy subsequent services.

  * The ID of each of your services must be specified in their corresponding [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml) configuration files. To specify the service ID, include the [`service`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#service) element definition in each configuration file. By default, excluding this element definition from your configuration file deploys the version to the `default` service.




To deploy multiple services, you must separately deploy each service's `app.yaml` file, for example:
    
    
    gcloud app deploy service1/app.yaml
    gcloud app deploy service2/app.yaml
    

You can specify multiple files with a single deploy command:
    
    
    gcloud app deploy service1/app.yaml service2/app.yaml
    

### Ignore files

You can use a [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file to specify files and directories not to upload to Google Cloud when you deploy your services. This is useful for ignoring build artifacts and other files that don't need to be uploaded with your deployment.

**Note:** You cannot specify the `skip_files` field in your `app.yaml` file if you have a `.gcloudignore` file.

Learn more about the syntax of the `.gcloudignore` file in the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore#SYNTAX).

### Manually build a container for deployment

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

To build your container images outside of Google Cloud:

  1. Upload your images to an Artifact Registry repository. For more information, see [Push and pull images](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling#pushing).
  2. Deploy to App Engine with the `gcloud app deploy` command.



For example, if you build your container images locally with Docker, you can push those images to the [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling#pushing) and specify the URL of your image in the `--image-url` flag of the command:
    
    
    gcloud app deploy --image-url LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE

Replace:

  * LOCATION with the location of the repository where the image is stored.

  * PROJECT-ID with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  * REPOSITORY with the name of the repository where the image is stored.

  * IMAGE with the name of your container image.




### Use automated continuous deployment pipelines

You can use Cloud Build to automate deployments in continuous deployment pipelines. For more information, see [Deploying to App Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine) and [Create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) in the Cloud Build documentation.

## Docker base images

If you'd like to build a custom runtime application, see [Create a Docker file](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#docker).

## View your application

After you deploy your application to App Engine, you can run the following command to launch your browser and view it at `https://PROJECT_ID.REGION_ID.r.appspot.com`:
    
    
    gcloud app browse
    

## Test on App Engine

Before configuring a new version to receive traffic, you can test it on App Engine. For example, to test a new version of your `default` service:

  1. Deploy your new version and include the `--no-promote` flag: 
         
         gcloud app deploy --no-promote

  2. Access your new version by navigating to the following URL:

`https://VERSION_ID-dot-default-dot-PROJECT_ID.REGION_ID.r.appspot.com`

**Note:** You can find the version ID in the [Google Cloud console](https://console.cloud.google.com/appengine/versions), or specify one when you deploy with the `version` parameter.

Now you can test your new version in the App Engine runtime environment. You can debug your application by viewing its logs in the Google Cloud console [Logs Explorer](https://console.cloud.google.com/logs). For more information, see [Writing Application Logs](https://docs.cloud.google.com/appengine/docs/flexible/writing-application-logs).

Requests sent to `https://PROJECT_ID.REGION_ID.r.appspot.com` will still be routed to the version previously configured to receive traffic.

  3. When you want to send traffic to the new version, use the Google Cloud console to migrate traffic:

[Manage versions](https://console.cloud.google.com/appengine/versions)

Select the version you just deployed and click **Migrate traffic**.




You can use the same process to test new versions of other services by replacing `default` in the URL with your service's name:

`https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com`

For more information about targeting specific services and versions, see [How requests are routed](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed).

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



To use environment variables with buildpacks, specify the [`build_env_variables`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#build_environment_variables) field in your `app.yaml` file.

[Learn more](https://docs.cloud.google.com/docs/buildpacks/builders) about buildpacks.

## Use Cloud Trace

Cloud Trace is useful for understanding how requests propagate through your application. You can inspect detailed latency information for a single request or view aggregate latency for your entire application.

You can [view trace details](https://docs.cloud.google.com/trace/docs/finding-traces). In the [Trace explorer](https://console.cloud.google.com/traces/list), you can filter by your specific App Engine service and version.

## Troubleshoot

The following are common error messages that you might encounter when deploying apps:

`PERMISSION_DENIED: Operation not allowed`
`The "appengine.applications.create" permission is required.`
    If the Google Cloud project does not include the [required App Engine application](https://docs.cloud.google.com/appengine/docs/flexible/managing-projects-apps-billing#create), the `gcloud app deploy` command can fail when it tries to run the `gcloud app create` command. Only accounts with Owner role have the necessary permissions to create App Engine applications.
`502 Bad Gateway`
    The Google Cloud project can fail to start if the `app.yaml` is misconfigured. [Check the app logs](https://docs.cloud.google.com/appengine/docs/flexible/writing-application-logs#viewing_logs) for more detailed error messages.
`[13] An internal error occurred while creating a Cloud Storage bucket.`
    

App Engine creates a [default Cloud Storage multi-regional bucket](https://docs.cloud.google.com/appengine/docs/flexible/locations#cloud-storage-location) on your behalf on the same region where it creates your application. It requires this bucket to store the contents of your application. The error returns when this bucket cannot be created, such as in the following scenarios:

  * The [App Engine flexible environment service agent](https://docs.cloud.google.com/appengine/docs/flexible/service-agent) is not present in your project or it doesn't have the `App Engine flexible environment Service Agent` role. You can add the agent's service account back into your project by granting it the correct IAM permissions. See [Restore a deleted service agent](https://docs.cloud.google.com/appengine/docs/flexible/service-agent#restoring_a_deleted_service_agent).

  * The [default App Engine service account](https://docs.cloud.google.com/appengine/docs/flexible/default-service-account) is not present in your project. If the App Engine service account was removed before 30 days had elapsed since its deletion, you can [restore it](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting).

  * Your project is under an organization enforcing the [`constraints/gcp.resourceLocations` policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) and the organization is not allowing the creation of resources on the same [region](https://docs.cloud.google.com/appengine/docs/flexible/locations) where your App Engine was created. You must [override the enforced `constraints/gcp.resourceLocations` policy for your project](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints) and allow the [multi-region locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations#setting_the_organization_policy) on the same region where your App Engine app is created.




For example, if your App Engine app is created in the `europe-west` region, even though the region maps to the [`europe-west1` locations](https://docs.cloud.google.com/appengine/docs/flexible/locations), you must modify the constraint to allow resources in the `in:eu-locations`, which includes all the `EU` regions. This is required because the App Engine-created buckets are multi-regional. If your App Engine app is created in the `US` region, you must allow `in:us-locations`, and if your app is created in the `ASIA` regions, you must allow `in:asia-locations`.

`[13] An internal error occurred.`
    

This error can occur if you are deploying your service with a network configuration that uses a Shared VPC setup. Try the following:

  1. Ensure that your `app.yaml` configuration is valid.
  2. Ensure that your App Engine flexible environment fulfills all the requirements for a Shared VPC setup. See [Using the App Engine flexible environment on a Shared VPC network](https://docs.cloud.google.com/appengine/docs/flexible/using-shared-vpc).
  3. Be sure that you have [configured service accounts](https://docs.cloud.google.com/appengine/docs/flexible/using-shared-vpc#setting_up_permissions) present in your project. If not, you must [restore the accounts](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting). The subnet region in the Shared VPC host project must match the [location](https://docs.cloud.google.com/appengine/docs/flexible/locations) where your App Engine environment was created.


    

If the issue persists, redeploy your service by using the Google Cloud SDK. Be sure to add the [`--verbosity=debug` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity). Contact [Google Cloud Support](https://cloud.google.com/support-hub) and provide the command's output.

`IP space of {USER_SUBNETWORK_NAME} is exhausted and needs to be expanded.`
    

If the deployment fails with this error message, the network configured for the App Engine service doesn't have addresses left to allocate for the new instances of the service. To resolve the issue, [expand the VPC ranges](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet) on the subnet that is configured for your App Engine flexible environment service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
