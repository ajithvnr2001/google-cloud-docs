---
url: https://docs.cloud.google.com/build/docs/building/build-go/
title: Build and test Go applications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:27.776643+00:00
---

# Build and test Go applications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/building/build-go/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build and test Go applications Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Cloud Build to build and test your Go applications, upload your artifacts to Artifact Registry, generate provenance information, and save your test logs in Cloud Storage.

## Before you begin

The instructions on this page assume that you are familiar with Go. In addition:

  * Enable the Cloud Build, Cloud Run, and Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,artifactregistry.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/building/build-go)

  * To run the `gcloud` commands on this page, install [Google Cloud CLI](https://docs.cloud.google.com/sdk).
  * Have your Go project ready.
  * Have a Go repository in Artifact Registry. If you don't have one, then [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  * If you want to store test logs in Cloud Storage, or if you want to use the gcloud CLI to start the build, [create a bucket in Cloud Storage](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * Ensure that you know the ID of the [runtime service account](https://docs.cloud.google.com/functions/docs/concepts/iam#runtime_service_accounts) for Cloud Run.



### Create a custom Cloud Build service account

Create a custom Cloud Build service account by running the following command in Google Cloud CLI:
    
    
      gcloud iam service-accounts create cloud-build-go \
          --description="Build and test Go applications" \
          --display-name="Cloud Build Go" \
          --project="PROJECT_ID"
    

Replace `PROJECT_ID` with your Google Cloud project ID. If the flag is omitted, then the current project is assumed.

You will use this service account to build and test your Go application.

### Configure IAM permissions

To configure your new service account with the permissions required to build and deploy Go applications, do the following:

  1. In the Google Cloud console, go to the _settings_ Cloud Build **Permissions** page: 

[Go to **Permissions**](https://console.cloud.google.com/cloud-build/settings)

  2. Go to the **Service account** menu and select your `cloud-build-go` service account.

  3. Set the status of the following roles to **Enabled** :

     * Cloud Run Admin (`roles/run.admin`): Lets Cloud Build deploy new services to Cloud Run. 
       * In the Assign Service Account User Role panel, select your [runtime service account](https://docs.cloud.google.com/functions/docs/concepts/iam#runtime_service_accounts) and then click **Grant Permission**. This configuration allows your custom Cloud Build service account to impersonate the runtime service account when interacting with the Cloud Run managed service. For more information, see [Configure Cloud Build service account impersonation for managed services](https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp).
     * Storage Admin (`roles/storage.admin`): Enables reading and writing from Cloud Storage.
     * Artifact Registry Writer (`roles/artifactregistry.writer`): Allows pulling images from and writing to Artifact Registry.
     * Logs Writer (`roles/logging.logWriter`): Allows log entries to be written to Cloud Logging.
     * Cloud Build Editor (`roles/cloudbuild.builds.editor`): Allows your service account to run builds.



## Configure Go builds

The public [`golang` image from Docker Hub](https://hub.docker.com/_/golang/tags) supports building using Go modules. Using this image as a build step in your Cloud Build config file lets you invoke `go` commands within the image. Arguments passed to this build step are passed to the `golang` tool directly, allowing you to run any `go` command in this image.

This section shows how to create an [example build config file](https://github.com/GoogleCloudPlatform/cloud-build-samples/blob/main/golang-sample/cloudbuild.yaml) for a Go app from the [cloud-build-samples](https://github.com/GoogleCloudPlatform/cloud-build-samples/tree/main) Git repository. The build config file has steps to build the app, add unit tests, and after the tests pass, to deploy the app.

To build the example Go application:

  1. **Configure unit tests** : If you've defined unit tests in your application, you can configure Cloud Build to run the tests by adding the following fields in a build step:

     * `name`: Set the value of this field to `golang` to use the golang image from Docker Hub for your task.
     * `entrypoint`: Set the value of this field to `/bin/bash`. This lets you run [multi-line bash commands](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash) directly from the build step.
     * `args`: The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field. In the following example, the `args` field takes the arguments for:

       * Running the test log formatter to download the test log output.
       * Printing the log output.
       * Saving test results in `sponge.log`.
       * Outputting the results in `sponge.log` to a JUNIT XML file. The name of the JUNIT XML file is constructed using [the short version of the commit ID associated with your build](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions). A subsequent build step will save the logs in this file to Cloud Storage.
             
             steps:
               # Run tests and save to file
               - name: golang:1.23
                 entrypoint: /bin/bash
                 args:
                   - -c
                   - |
                     go install github.com/jstemmer/go-junit-report/v2@latest
                     2>&1 go test -timeout 1m -v ./... | /go/bin/go-junit-report -set-exit-code -iocopy -out ${SHORT_SHA}_test_log.xml
             

  2. **Upload to Artifact Registry** : In your config file, use the `goModules` field to specify your application path and your Go repository in Artifact Registry:
         
         # Upload Go module to artifact registry
         artifacts:
           goModules:
             - repositoryName: 'repositoryName'
               repositoryLocation: 'location'
               repositoryProjectId: 'projectId'
               sourcePath: 'sourcePath'
               modulePath: 'appPath'
               moduleVersion: 'version'
         

Replace the following values:

     * repositoryName: the name of your Go repository in Artifact Registry.
     * location: the [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for your repository in Artifact Registry.
     * projectId: the ID of the Google Cloud project that contains your Artifact Registry repository.
     * sourcePath: the path to the `go.mod` file in the build's workspace.
     * appPath: the path to your packaged application.
     * version: the version number for your application, [formatted](https://go.dev/ref/mod#versions) in numbers and dots like `v1.0.1`.
  3. **Optional: Enable provenance generation**

Cloud Build can generate verifiable [Supply chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) build provenance metadata to help secure your continuous integration pipeline.

To enable provenance generation, add [`requestedVerifyOption: VERIFIED`](https://docs.cloud.google.com/build/docs/build-config-file-schema#options) to the `options` section in your config file.

Once your build completes, you can [view repository details](https://docs.cloud.google.com/artifact-registry/docs/repositories/list-repos) in Artifact Registry.

You can also [view build provenance metadata](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#view) and [validate provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#validate_provenance).

  4. **Save test logs to Cloud Storage** : You can configure Cloud Build to store any test logs in Cloud Storage by specifying an existing bucket location and path to the test logs.

The following build step stores the test logs that you saved in the JUNIT XML file to a Cloud Storage bucket:
         
         # Save test logs to Google Cloud Storage
         artifacts:
           objects:
             location: gs://$_BUCKET_NAME/
             paths:
               - ${SHORT_SHA}_test_log.xml
         

The following snippet shows the complete build config file for the preceding steps:
         
         steps:
             # Run tests and save to file
             - name: golang:1.23
               entrypoint: /bin/bash
               args:
                 - -c
                 - |
                   go install github.com/jstemmer/go-junit-report/v2@latest
                   2>&1 go test -timeout 1m -v ./... | /go/bin/go-junit-report -set-exit-code -iocopy -out ${SHORT_SHA}_test_log.xml
         
           # Store golang modules in Google Artifact Registry
           artifacts:
             goModules:
               - repositoryName: 'repositoryName'
                 repositoryLocation: 'location'
                 repositoryProjectId: 'projectId'
                 sourcePath: 'sourcePath'
                 modulePath: 'appPath'
                 moduleVersion: 'version'
         

  5. Start the build using the [gcloud CLI](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or create a [build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers):

###  gcloud 

Run the following command, using `--substitutions` to specify the [substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions) used in `cloudbuild.yaml`:
         
         gcloud builds submit --region=us-west2 --config=cloudbuild.yaml \
             --default-buckets-behavior=REGIONAL_USER_OWNED_BUCKET \
             --service-account=projects/PROJECT_ID/serviceAccounts/cloud-build-go@PROJECT_ID.iam.gserviceaccount.com \
             --substitutions=_AR_REPO_NAME="_AR_REPO_NAME",_BUCKET_NAME="_BUCKET_NAME",SHORT_SHA="SHORT_SHA"
         

Replace the following:

     * `_AR_REPO_NAME`: the name of your Artifact Registry repository.

     * `_BUCKET_NAME`: the name of your Cloud Storage bucket for test logs.

     * `SHORT_SHA`: a short generic text string, such as "manual". `SHORT_SHA` values are automatically populated for builds invoked by triggers, but aren't provided when submitting a build using the gcloud CLI.

###  Build triggers 

Follow the steps in [Create a build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers#build_trigger). In the **Substitution variables** field, you must also provide the name of your Artifact Registry repository and the name of your Cloud Storage bucket for test logs.




## What's next

  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
