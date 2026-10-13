---
url: https://docs.cloud.google.com/run/docs/deploying-source-code/
title: Deploy services from source code \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:41.038754+00:00
---

# Deploy services from source code  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/deploying-source-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deploy services from source code Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy a new service or service revision to Cloud Run directly from source code using a single gcloud CLI command, `gcloud run deploy` with the [`--source`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--source) flag. For an example walkthrough of deploying a Hello World service, see [Deploy from source quickstarts](https://docs.cloud.google.com/run/docs/quickstarts#build-and-deploy-a-web-service). **Note:** The deploy command defaults to source deployment if you don't supply `--image` or `--source` flags. There are two different ways to use this feature:

  * Deploy from source with build (default): This option uses [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) and Cloud Build to automatically build container images from your source code without having to install Docker on your machine or set up buildpacks or Cloud Build. By default, Cloud Run uses the [default machine type provided by Cloud Build](https://docs.cloud.google.com/build/pricing). Running `gcloud run deploy --source` also eliminates the need to run the [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command.
  * Deploy prebuilt source (Preview): This option deploys artifacts directly to Cloud Run, bypassing the Cloud Build step. This allows for rapid deployment times. 



Note that source deployments use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to store built containers. If your project doesn't already have an Artifact Registry repository with the name `cloud-run-source-deploy` in the region you are deploying to, this feature automatically creates an Artifact Registry repository with the name `cloud-run-source-deploy`.

If a Dockerfile is present in the source code directory, the uploaded source code is built using that Dockerfile. If no Dockerfile is present in the source code directory, Google Cloud's buildpacks automatically detects the language you are using and fetches the dependencies of the code to make a production-ready container image, using a secure base image managed by Google.

By default, security fixes are only applied when the Cloud Run service is deployed. When you enable automatic security updates for a service, that service receives patches automatically with zero downtime. Learn more about [configuring security updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates). 

## Before you begin

  * Make sure you have set up a new project for Cloud Run as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page. 
  * If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).

  * Enable the Cloud Run Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

After the Cloud Run Admin API is enabled, the Compute Engine default service account is automatically created.




### Required roles

To deploy from source, you or your administrator must grant the deployer account the following IAM roles.

#### Click to view required roles for the deployer account

To get the permissions that you need to build and deploy from source, ask your administrator to grant you the following IAM roles:

  * [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on your project
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your project
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Cloud Run service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Supported languages

In addition to sources with a Dockerfile, deploying from source supports the following languages using [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview):

Runtime | Source deployment | Configuration  
---|---|---  
Go | [Deploy a Go service](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-go-service) | [Configure Go buildpacks](https://docs.cloud.google.com/docs/buildpacks/go)  
Node.js | [Deploy a Node.js service](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service) | [Configure Node.js buildpacks](https://docs.cloud.google.com/docs/buildpacks/nodejs)  
Python | [Deploy a Python service](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service) | [Configure Python buildpacks](https://docs.cloud.google.com/docs/buildpacks/python)  
Java   
(includes Kotlin, Groovy, Scala) | [Deploy a Java service](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-java-service) | [Configure Java buildpacks](https://docs.cloud.google.com/docs/buildpacks/java)  
.NET | [Deploy a .NET service](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-dotnet-service) | [Configure .NET buildpacks](https://docs.cloud.google.com/docs/buildpacks/build-application)  
Ruby | [Deploy a Ruby service](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-ruby-service) | [Configure Ruby buildpacks](https://docs.cloud.google.com/docs/buildpacks/ruby)  
PHP | [Deploy a PHP service](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-php-service) | [Configure PHP buildpacks](https://docs.cloud.google.com/docs/buildpacks/php)  
OS only | Deploy a Go service | [Configure OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly)  
  
Read more details about [supported language versions](https://docs.cloud.google.com/run/docs/runtime-support).

## Deploy from source with build

This section describes how to use [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) and Cloud Build to automatically build container images from your source code without having to install Docker on your machine or set up buildpacks or Cloud Build.

### Limitations

  * Deploy from source uses Artifact Registry and Cloud Build, so this feature is only available in [regions supported by Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/repo-locations#location-r) and [Cloud Build](https://docs.cloud.google.com/build/docs/locations).
  * Deploying from source is a convenience feature, and does not allow full customization of the build. For more control, build the container image using Cloud Build, for example, using `gcloud builds submit`, and then [deploy the container image](https://docs.cloud.google.com/run/docs/deploying) using, for example, `gcloud run deploy --image`. 
  * Deploying from source with Google Cloud's buildpacks sets the Last Modified Date of source files to Jan 1, 1980. This is the default behavior of buildpacks and is designed to support [reproducible builds](https://reproducible-builds.org/). Depending on your language framework, this can affect browser-side caching of static files. If your application is affected by this, Google recommends disabling `etag` and `Last-Modified` HTTP headers in your application.
  * Deploying from source with Google Cloud's buildpacks always uses `gcr.io/buildpacks/builder:latest`. If your preferred language or OS configuration is not available in `latest`, [use a specific builder](https://docs.cloud.google.com/docs/buildpacks/use-a-specific-builder) to create an application image using your preferred builder.
  * You can deploy your service from source using Kotlin and other JVM languages such as [Java](https://docs.cloud.google.com/docs/buildpacks/java). The language you use must conform to the following rules:

    * You can build the application using Maven or Gradle.
    * The build file contains all the plugins required to produce classes.



### Before you deploy with build

Before you deploy from source with build:

  * Follow the steps in Before you begin.

  * Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)




#### Required roles

To deploy from source with build, you or your administrator must grant the Cloud Build service account the following IAM roles.

#### Click to view required roles for the Cloud Build service account

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior. For Cloud Build to build your sources, ask your administrator to grant [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) to the Compute Engine default service account on your project:
    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
          --role=roles/run.builder
      

Replace `PROJECT_NUMBER` with your Google Cloud project number, and `PROJECT_ID` with your Google Cloud project ID. For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role to the Compute Engine default service account takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Deploy with build

To deploy from source code, click the tab for instructions on using the tool of your choice.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Change to your source directory. The source directory uses a Dockerfile if present, although it's not required.

  3. Build and deploy your service:
         
         gcloud run deploy SERVICE --source .

Replace `SERVICE` with the name you want for your service.

  4. Respond to any prompts to install required APIs by responding `y` when prompted. You only need to do this once for a project. Respond to other prompts by supplying the platform and region, if you haven't set defaults for these as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.

  5. Wait for the build and deploy to complete. When finished, Cloud Run displays a success message.




After deployment, this service revision serves 100% of traffic.

###  Compose 

You can store your [Compose specification](https://compose-spec.io) in a `YAML` file and then deploy it from source code as a Cloud Run service using a single gcloud command.

  1. Change to your source directory. The source directory uses a Dockerfile if present, although it's not required.

  2. In your project directory, create a `compose.yaml` file with your service definitions.
         
         services:
           web:
             build: .
             ports:
               - "8080:8080"

You can also specify more configuration options such as environment variables, secrets, and volume mounts.




**Deploy the services**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

## Deploy prebuilt source

**Preview — Deploy without build**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can deploy prebuilt source artifacts directly to Cloud Run, bypassing the Cloud Build step. The way this works is that instead of building a container image from source, you can upload a pre-packaged archive of your application directly to a Cloud Storage bucket. Cloud Run then takes this archive and runs it directly on a base image. This approach lets you develop and iterate fast locally and results in dramatically faster deployment times. 

### Limitations

Deploying prebuilt source only supports the following:

  * Cloud Run services.
  * [Supported runtimes](https://docs.cloud.google.com/run/docs/runtime-support) (no Dockerfile support).
  * Source archive (.tar.gz) <= 250 MiB.
  * Binary (for example, go binary) or script (for example, python script) must be compatible with x86 architecture.
  * The source has to be self-contained, with all the dependencies packaged. The runtime base image only contains the minimum operating system and a few language libraries.



### Before you deploy prebuilt source

To use the "deploy without build" feature:

  * Make sure you have followed the steps in Before you begin.
  * Enable the Cloud Run and Cloud Storage APIs:
        
        gcloud services enable run.googleapis.com \
          storage.googleapis.com
        

  * You must install the application dependencies locally before deploying, as they won't be installed (no build).




### Deploy without build

This section describes how to deploy your prebuilt source directly to Cloud Run.

###  gcloud 

To deploy prebuilt source from a local directory, use the `--no-build` flag to tell the `deploy` command to bypass the Cloud Build step:
    
    
    gcloud beta run deploy SERVICE_NAME \
      --source APPLICATION_PATH \
      --no-build \
      --base-image=BASE_IMAGE \
      --command=COMMAND \
      --args=ARG
    

Replace the following:

  * `SERVICE_NAME`: the name of your Cloud Run service.
  * `APPLICATION_PATH`: the location of your application on the local file system.
  * `BASE_IMAGE`: the [runtime base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) you want to use for your application. For example, `us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs24`. You could also use the short alias `nodejs24`.

You can also deploy a pre-compiled binary without configuring additional language-specific runtime components using the OS only base image, such as `osonly24`. For more information, see [OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly) in the buildpacks documentation. 

  * `COMMAND`: the command that the container starts up with. Optional. If you don't specify a command, the base image will infer the container starting command at runtime.

  * `ARG`: an argument you send to the container command. If you use multiple arguments, specify each on its own line. Optional. If you don't specify arguments, the base image will infer any arguments at runtime.




###  YAML 

You can store your service specification in a YAML file and then deploy it using the gcloud CLI or the Google Cloud console `service.yaml` editor.

  1. Create a storage bucket to hold your application:
         
         gcloud storage buckets create gs://BUCKET_NAME --location=BUCKET_LOCATION
         

Replace the following:

     * `BUCKET_NAME`: the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * `BUCKET_LOCATION`: the [location](https://docs.cloud.google.com/storage/docs/locations) of your bucket. For example, `US`.
  2. Create an archive with your application source using either zip or tar, for example:
         
         tar -cvzf ARCHIVE_NAME APPLICATION_PATH
         

Replace the following:

     * `ARCHIVE_NAME`: the name of the archive to create. For example, `app.tar.gz`.
     * `APPLICATION_PATH`: the location of your application on the local file system. For example, `~/my-application`. To archive the current working directory, set this value to `*`.
  3. Upload your application archive to Cloud Storage:
         
         gcloud storage cp ARCHIVE_NAME gs://BUCKET_NAME
         

Replace the following:

     * `ARCHIVE_NAME`: the local path to the archive you created previously. For example, `app.tar.gz`.
     * `BUCKET_NAME`: the name of the bucket you created previously. For example, `my-bucket`.
  4. Create a new `service.yaml` file with the following content:
         
         apiVersion: serving.knative.dev/v2
         kind: Service
         metadata:
          name: SERVICE_NAME
         spec:
          template:
            metadata:
              annotations:
                run.googleapis.com/sources: '{"": "gs://BUCKET_NAME/ARCHIVE_NAME"}'
                run.googleapis.com/base-images: '{"": "BASE_IMAGE"}'
            spec:
              containers:
              - image: scratch
                command:
                - COMMAND
                args:
                - ARG1
                - ARG-N
              runtimeClassName: run.googleapis.com/linux-base-image-update
         

Replace the following:

     * `SERVICE_NAME`: the name of your Cloud Run service. Service names must be 49 characters or less and must be unique per region and project.
     * `BUCKET_NAME`: the name of the bucket you created previously. For example, `my-bucket`.
     * `ARCHIVE_NAME`: the local path to the archive you created previously. For example, [`app.tar.gz`](http://app.tar.gz).
     * `BASE_IMAGE`: the runtime base image you want to use for your application. For example, `us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs24`.

You can also deploy a pre-compiled binary without configuring additional language-specific runtime components using the OS only base image, such as `osonly24`. For more information, see [OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly) in the buildpacks documentation. 

     * `COMMAND`: the command that the container is to start up with. Optional. If you don't specify a command, the base image will infer the container starting command at runtime.

     * `ARG1`: the argument you are sending to the container command. If you use multiple arguments, specify each on its own line, for example, as shown, `ARG-N`. Optional. If you don't specify arguments, the base image will infer any arguments at runtime.

  5. Deploy the new service:
         
         gcloud run services replace service.yaml
         




###  REST API 

To deploy using the REST API:
    
    
    curl -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -X POST \
    -d '{"template": {"containers": [{"command": ["COMMAND"], "args": ["ARG1"], "image": "scratch", "baseImageUri": "BASE_IMAGE", "sourceCode": {"cloudStorageSource": {"bucket": "'GCS_BUCKET_NAME", "object":"ARCHIVE_NAME"}}}]}}' \
    https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services?serviceId=SERVICE_NAME
    

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to deploy services](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * COMMAND: the command that the container is to start up with. Optional. If you don't specify a command, the base image will infer the container starting command at runtime.
  * ARG1: the argument you are sending to the container command. If you use multiple arguments, specify each on its own line, for example, as shown, `ARG-N`. Optional. If you don't specify arguments, the base image will infer any arguments at runtime.
  * BASE_IMAGE: the runtime base image you want to use for your application. For example, `us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs24`.

You can also deploy a pre-compiled binary without configuring additional language-specific runtime components using the OS only base image, such as `osonly24`. For more information, see [OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly) in the buildpacks documentation. 

  * BUCKET_NAME: the name of the bucket you created previously. For example, `my-bucket`.

  * ARCHIVE_NAME: the local path to the archive you created previously. For example, [`app.tar.gz`](http://app.tar.gz).

  * PROJECT-ID: the Google Cloud project ID.

  * REGION: the Google Cloud region of the service.

  * SERVICE_NAME: the name of your Cloud Run service. Service names must be 49 characters or less and must be unique per region and project.




###  Terraform 

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_storage_bucket_object" "source_tar" {
      provider = google-beta
      name   = "ARCHIVE_NAME"
      bucket = "BUCKET_NAME"
      source = "ARCHIVE_PATH"
    }
    
    resource "google_cloud_run_v2_service" "default" {
      provider = google-beta
      name     = "SERVICE_NAME"
      location = "REGION"
      deletion_protection = false
    
      template {
        containers {
          image = "scratch"
          base_image_uri = "BASE_IMAGE"
          command = ["COMMAND"]
          args = ["ARG1"]
          source_code {
            cloud_storage_source {
              bucket = "BUCKET_NAME"
              object = google_storage_bucket_object.source_tar.name
              generation = google_storage_bucket_object.source_tar.generation
            }
          }
        }
      }
    }
    

Replace the following:

  * `ARCHIVE_NAME`: the name of the file as it will appear in your Cloud Storage bucket. For example, `source-code.tar.gz`.
  * `BUCKET_NAME`: the name of the bucket where you want to upload the source archive. For example, `my-source-bucket`.
  * `ARCHIVE_PATH`: the local path to the archive you created previously. For example, `./app.tar.gz`. This archive must be in GZIP format (`.tar.gz`).
  * `SERVICE_NAME`: the name of the Cloud Run service
  * `REGION`: the Google Cloud region for both the bucket and the service. For example, europe-west1. Both resources must be in the same region to avoid extraction timeouts.
  * `BASE_IMAGE`: the runtime base image you want to use for your application. For example, `us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs24`.
  * `COMMAND`: the command that the container is to start up with. Optional. If you don't specify a command, the base image will infer the container starting command at runtime.
  * `ARG1`: the argument you are sending to the container command. Optional. If you don't specify arguments, the base image will infer any arguments at runtime.



### MCP

You can use an AI agent to deploy your service with or without a storage bucket using the official Cloud Run MCP server.

For best results, tell your agent to prefer MCP tools over gcloud CLI before you start using this MCP server.

  1. To set up the Cloud Run remote MCP server, follow the instructions in the [Use the Cloud Run remote MCP server](https://docs.cloud.google.com/run/docs/use-cloud-run-mcp) guide.

     * **With a storage bucket**

To create a storage bucket and deploy a service, instruct your agent with the following prompt: `Create storage bucket "my-bucket" for my source code and deploy service "my-app" to Cloud Run from source in this current directory.`

The agent uses the [`deploy_service_from_archive`](https://docs.cloud.google.com/run/docs/reference/mcp/tools_list/deploy_service_from_archive) tool to pass the source code directly to Cloud Run from a self-contained source code archive for faster deployment.

You can also instruct your agent to reuse an existing Cloud Storage bucket for the source code.

     * **Without a storage bucket**

For code snippets of 50 MiB or less with no external dependencies, instruct your agent to deploy without a storage bucket using the following prompt: `Deploy service "my-app" to Cloud Run from source in this current directory.`

The agent uses the [`deploy_service_from_file_contents`](https://docs.cloud.google.com/run/docs/reference/mcp/tools_list/deploy_service_from_file_contents) tool to pass the source code directly from local source files to Cloud Run.




**Use the`/deploy` prompt**

You can use the `/deploy` prompt to quickly deploy a service using the Cloud Run MCP server. You might need to navigate your chatbot menu to find the necessary tool or prompt.

To deploy the current working directory to Cloud Run, run the following `/deploy` prompt:
    
    
    /deploy SERVICE_NAME \
        --project PROJECT_ID \
        --region REGION \
    

Replace the following:

  * `SERVICE_NAME`: the name of the Cloud Run service
  * `PROJECT_ID`: the Google Cloud project ID
  * `REGION`: the name of the region



### Examples of deploying prebuilt source

This section shows examples of how to deploy from source without using build.

###  Node.js 

Create a Node.js service:

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
         cd helloworld
         

  2. Create a `package.json` file with the following contents:
         
         {
           "name": "helloworld",
           "description": "Simple hello world sample in Node",
           "version": "1.0.0",
           "private": true,
           "main": "index.js",
           "type": "module",
           "scripts": {
             "start": "node index.js"
           },
           "engines": {
             "node": ">=16.0.0"
           },
           "author": "Google LLC",
           "license": "Apache-2.0",
           "dependencies": {
             "express": "^5.2.1"
           }
         }
         

  3. In the same directory, create a `index.js` file, and copy the following lines into it:
         
         import express from 'express';
         const app = express();
         
         app.get('/', (req, res) => {
           const name = process.env.NAME || 'World';
           res.send(`Hello ${name}!`);
         });
         
         const port = parseInt(process.env.PORT) || 8080;
         app.listen(port, () => {
           console.log(`helloworld: listening on port ${port}`);
         });

This code creates a basic web server that listens on the port defined by the [`PORT` environment variable](https://docs.cloud.google.com/run/docs/reference/container-contract#port).

  4. In your `helloworld` directory, run the following command to install the service dependencies locally:
         
         npm install

  5. In your `helloworld` directory, deploy the service using the `--no-build` flag, which tells the `deploy` command to skip the Cloud Build step:
         
         gcloud beta run deploy helloworld \
          --source . \
          --region=REGION \
          --no-build \
          --base-image=nodejs24 \
          

Replace the following:

     * `REGION`: the region where your service is deployed.



###  Python 

Create a Python service:

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
         cd helloworld
         

  2. Create a file named `main.py` and paste the following code into it:
         
         import os
         
         from flask import Flask
         
         app = Flask(__name__)
         
         
         @app.route("/")
         def hello_world():
             """Example Hello World route."""
             name = os.environ.get("NAME", "World")
             return f"Hello {name}!"
         
         
         if __name__ == "__main__":
             app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

This code responds to requests with our "Hello World" greeting. HTTP handling is done by a Gunicorn web server in the container. When directly invoked for local use, this code creates a basic web server that listens on the port defined by the [`PORT` environment variable](https://docs.cloud.google.com/run/docs/reference/container-contract#port).

  3. Create a file named `requirements.txt` and paste the following code into it:
         
         Flask==3.1.3; python_version >= '3.9'
         gunicorn==23.0.0
         Werkzeug==3.1.8; python_version >= '3.9'
         

This code adds packages needed by the sample.

  4. Vendor the dependencies:
         
         pip3 install -r requirements.txt --target=./vendor
         

  5. Deploy the service using the gcloud CLI. The `--no-build` flag tells the `deploy` command to bypass the Cloud Build step:
         
         gcloud beta run deploy helloworld \
           --source . \
           --region=REGION \
           --no-build \
           --base-image=python314 \
         




Replace `REGION` with the region where your service is deployed.

###  Go 

Create and deploy a Go service using the OS only runtime:

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
         cd helloworld
         

  2. Initialize a `go.mod` file from the project directory to declare the [go module](https://blog.golang.org/using-go-modules):
         
         go mod init github.com/GoogleCloudPlatform/golang-samples/run/helloworld
         

  3. Create a new file named `main.go` and paste the following code into it:
         
         // Sample run-helloworld is a minimal Cloud Run service.
         package main
         
         import (
         	"fmt"
         	"log"
         	"net/http"
         	"os"
         )
         
         func main() {
         	log.Print("starting server...")
         	http.HandleFunc("/", handler)
         
         	// Determine port for HTTP service.
         	port := os.Getenv("PORT")
         	if port == "" {
         		port = "8080"
         		log.Printf("defaulting to port %s", port)
         	}
         
         	// Start HTTP server.
         	log.Printf("listening on port %s", port)
         	if err := http.ListenAndServe(":"+port, nil); err != nil {
         		log.Fatal(err)
         	}
         }
         
         func handler(w http.ResponseWriter, r *http.Request) {
         	name := os.Getenv("NAME")
         	if name == "" {
         		name = "World"
         	}
         	fmt.Fprintf(w, "Hello %s!\n", name)
         }
         

  4. Build the binary targeting a Linux OS, such as `linux/amd64`, by running the following command:
         
         GOOS="linux" GOARCH=amd64 go build main.go
         

  5. Deploy the service using the gcloud CLI. The `--no-build` flag tells the `deploy` command to bypass the Cloud Build step:
         
         gcloud beta run deploy helloworld \
           --source . \
           --region=REGION \
           --no-build \
           --base-image=osonly24 \
           --command=./main
         




Replace `REGION` with the region where your service is deployed.

### Troubleshooting

This section gives some tips on troubleshooting deploy from source without using build.

#### Local development

Deploying from source without using build works similarly to mounting your code or executable to the base image.

For example:

  1. Make a copy of all the contents:
         
         cp -R python/hello-world/ workspace

  2. Run the base image as root user with the source mounted. You can optionally include `-p 8080:8080` if you need to curl from a host machine.
         
         docker run -it -v "LOCAL_PATH" -u 0 us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python314 /bin/bash`

Replace LOCAL_PATH with the location of your local source files.

  3. Run the server:
         
         python main.py




#### Execution log

The execution log is useful for debugging deployment failure. In the [Google Cloud console](https://console.cloud.google.com/run), go to **Observability > Logs**.

#### Permission denied on Cloud Storage access

If your Cloud Run service is encountering "Permission denied" errors when trying to access Cloud Storage objects, you must grant the `roles/storage.objectViewer` role to your Cloud Run service account:
    
    
    gcloud projects add-iam-policy-binding PROJECT \
      --member="SERVICE_ACCOUNT" \
      --role="roles/storage.objectViewer"
    

Replace the following:

  * PROJECT: your Google Cloud project ID.
  * SERVICE_ACCOUNT: your Cloud Run service account. For example, `service-123@serverless-robot-staging.iam.gserviceaccount.com`. 



## Automating building from source

As a best practice for avoiding unversioned changes in local source, Google recommends that you automatically deploy when changes are pushed to your Git repository. To make this easier, you can connect and configure continuous deployment to your Cloud Run service. By connecting your GitHub repositories to Cloud Run, you can configure builds and deploy your repositories without writing Dockerfiles or build files.

To configure automated builds, set up automation as described in the [continuous builds page](https://docs.cloud.google.com/run/docs/continuous-deployment-with-cloud-build#setup-cd), making sure you choose the option for building source with buildpacks. 

## Disabling the deployment health check

By default, Cloud Run checks that your deployment is healthy by starting an instance and waiting for its startup probe to pass. If the health check fails, the revision will be marked as unhealthy and the traffic won't be routed to it.

If it is not needed or to increase deployment speed, the deployment health check can be disabled:

###  gcloud 

To disable the deployment health check, use the `--no-deploy-health-check` flag:
    
    
    gcloud run deploy --image IMAGE_URL --no-deploy-health-check

Replace the following:

  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .



Use `--deploy-health-check` to re-enable the deployment health check if it was previous disabled.

### YAML

To disable the deployment health check, add the `run.googleapis.com/health-check-disabled` annotation with value `'true'` to `spec.template.metadata.annotations`.
    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      name: SERVICE
    spec:
      template:
        metadata:
          annotations:
            run.googleapis.com/health-check-disabled: 'true'
    

### Terraform

To disable the deployment health check, set the `health_check_disabled` argument to `true` in the `template` block.
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      ...
      template {
        health_check_disabled = true
        ...
      }
    }
    

## What's next

After you deploy a Cloud Run service, you can do the following:

  * [Gradual rollouts, rollback revisions, traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)
  * [View service logs](https://docs.cloud.google.com/run/docs/logging)
  * [Monitor service performances](https://docs.cloud.google.com/run/docs/monitoring)
  * [Set memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits)
  * [Set environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables)
  * [Change service concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency)
  * [Manage the service](https://docs.cloud.google.com/run/docs/managing/services)
  * [Manage service revisions](https://docs.cloud.google.com/run/docs/managing/revisions)



Learn about the source deploy configurations:

  * [Automatic base image updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates)
  * [Build environment variables](https://docs.cloud.google.com/run/docs/configuring/services/build-environment-variables)
  * [Build service account](https://docs.cloud.google.com/run/docs/configuring/services/build-service-account)
  * [Build worker pools](https://docs.cloud.google.com/run/docs/configuring/services/build-worker-pools)



You can automate the builds and deployments of your Cloud Run services using Cloud Build triggers:

  * [Set up continuous deployment](https://docs.cloud.google.com/run/docs/continuous-deployment)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
