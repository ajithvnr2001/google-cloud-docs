---
url: https://docs.cloud.google.com/build/docs/building/build-containerize-go/
title: Build, test, and containerize Go applications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:53.130217+00:00
---

# Build, test, and containerize Go applications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/building/build-containerize-go/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build, test, and containerize Go applications Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Cloud Build to build, test, containerize, and deploy Go applications, and how to save your test logs in Cloud Storage.

## Before you begin

The instructions on this page assume that you are familiar with Go. In addition:

  * Enable the Cloud Build, Cloud Run, and Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,artifactregistry.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/building/build-go)

  * To run the `gcloud` commands on this page, install [Google Cloud CLI](https://docs.cloud.google.com/sdk).
  * Have your Go project handy.
  * If you want to containerize your Go app using Cloud Build, you'll need a `Dockerfile` along with your source code.
  * If you want to store the built container in Artifact Registry, create a [Docker repository in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#create).
  * If you want to store test logs in Cloud Storage, [create a bucket in Cloud Storage](https://docs.cloud.google.com/storage/docs/creating-buckets).



### Required IAM permissions

  * To store test logs in Logging, grant the [Storage Object Creator (`roles/storage.objectCreator`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) role for the Cloud Storage bucket to your build service account.

  * To store built images in Artifact Registry, grant the [Artifact Registry Writer (`roles/artifactregistry.writer`) role](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to your build service account.




For instructions on granting these roles see [Granting a role using the IAM page](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page).

## Configuring Go builds

The public `golang` image from Docker Hub supports building using Go modules. Using this image as a build step in your Cloud Build config file lets you invoke `go` commands within the image. Arguments passed to this build step are passed to the `golang` tool directly, allowing you to run any `go` command in this image.

This section walks through an example build config file for a Go app. It has build steps to build the app, add unit tests, and after the tests pass, to containerize and deploy the app.

To build your Go application:

  1. In your project root directory, create a [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config) named `cloudbuild.yaml`.

  2. **Build and test** : If you've defined unit tests in your application, you can configure Cloud Build to run the tests by adding the following fields in a build step:

     * `name`: Set the value of this field to `golang` to use the golang image from Docker Hub for your task.
     * `entrypoint`: Set the value of this field to `/bin/bash`. This lets you run [multi-line bash commands](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash) directly from the build step.
     * `args`: The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field. In the following example, the `args` field takes the arguments for:

       * Running the test log formatter to download the test log output.
       * Printing the log output.
       * Saving test results in `sponge.log`.
       * Outputting the results in `sponge.log` to a JUNIT XML file. The name of the JUNIT XML file is constructed using [the short version of the commit ID associated with your build](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions). A subsequent build step will save the logs in this file to Cloud Storage.
    
    steps:
      # Run tests and save to file
      - name: golang:1.26-trixie
        entrypoint: /bin/bash
        args:
          - -c
          - |
            go install github.com/jstemmer/go-junit-report/v2@latest
            2>&1 go test -timeout 1m -v ./... | /go/bin/go-junit-report -set-exit-code -iocopy -out ${SHORT_SHA}_test_log.xml

  3. **Containerize the app** : After adding the build step to ensure that the tests have passed, you can build the application. Cloud Build provides a [pre-built Docker image](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/docker) that you can use to containerize your Go application. To containerize your app, add the following fields in a build step:

     * `name`: Set the value of this field to `gcr.io/cloud-builders/docker` to use the prebuilt docker image for your task.
     * `args`: Add the arguments for the `docker build` command as values for this field.

The following build step builds the image `myimage` and tags it with the short version of your commit ID. The build step uses [substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) for project ID, repository name, and short SHA values therefore these values are automatically substituted at build time. Note that you will need to create or have an existing [Docker repository in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#create) to store the image.
    
    # Docker Build
    - name: 'gcr.io/cloud-builders/docker'
      args: ['build', '-t',
             'us-central1-docker.pkg.dev/$PROJECT_ID/$_AR_REPO_NAME/myimage:$SHORT_SHA', '.']

  4. **Push the container to Artifact Registry** : You can store the built container in Artifact Registry, which is a Google Cloud service that you can use to store, manage, and secure build artifacts. To do this, you'll need to have an existing Docker repository in Artifact Registry. To configure Cloud Build to store the image in an Artifact Registry Docker repository, add a build step with the following fields:

     * `name`: Set the value of this field to `gcr.io/cloud-builders/docker` to use the official `docker` builder image for your task.
     * `args`: Add the arguments for the `docker push` command as values of this field. For the destination URL, enter the Artifact Registry Docker repository where you want to store the image.

The following build step pushes the image that you built in the previous step to Artifact Registry:
    
    # Docker push to Google Artifact Registry
    - name: 'gcr.io/cloud-builders/docker'
      args: ['push', 'us-central1-docker.pkg.dev/$PROJECT_ID/$_AR_REPO_NAME/myimage:$SHORT_SHA']

  5. **Deploy the container to Cloud Run** : To deploy the image on Cloud Run, add a build step with the following fields:

     * `name`: Set the value of this field to `google/cloud-sdk` to use the gcloud CLI image to invoke the `gcloud` command to deploy the image on Cloud Run.
     * `args`: Add the arguments for the `gcloud run deploy` command as the values of this field.

The following build step deploys the previously built image to Cloud Run:
    
    # Deploy to Cloud Run
    - name: 'gcr.io/cloud-builders/gcloud'
      args: ['run', 'deploy', 'helloworld-${SHORT_SHA}',
             '--image=us-central1-docker.pkg.dev/$PROJECT_ID/$_AR_REPO_NAME/myimage:$SHORT_SHA',
             '--region', 'us-central1', '--platform', 'managed']

  6. **Save test logs to Cloud Storage** : You can configure Cloud Build to store any test logs in Cloud Storage by specifying an existing bucket location and path to the test logs.

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
           - name: golang:1.26-trixie
             entrypoint: /bin/bash
             args:
               - -c
               - |
                 go install github.com/jstemmer/go-junit-report/v2@latest
                 2>&1 go test -timeout 1m -v ./... | /go/bin/go-junit-report -set-exit-code -iocopy -out ${SHORT_SHA}_test_log.xml
         
           # Docker Build
           - name: 'gcr.io/cloud-builders/docker'
             args: ['build', '-t',
                    'us-central1-docker.pkg.dev/$PROJECT_ID/$_AR_REPO_NAME/myimage:$SHORT_SHA', '.']
         
           # Docker push to Google Artifact Registry
           - name: 'gcr.io/cloud-builders/docker'
             args: ['push', 'us-central1-docker.pkg.dev/$PROJECT_ID/$_AR_REPO_NAME/myimage:$SHORT_SHA']
         
           # Deploy to Cloud Run
           - name: 'gcr.io/cloud-builders/gcloud'
             args: ['run', 'deploy', 'helloworld-${SHORT_SHA}',
                    '--image=us-central1-docker.pkg.dev/$PROJECT_ID/$_AR_REPO_NAME/myimage:$SHORT_SHA',
                    '--region', 'us-central1', '--platform', 'managed']
         
         # Save test logs to Google Cloud Storage
         artifacts:
           objects:
             location: gs://$_BUCKET_NAME/
             paths:
               - ${SHORT_SHA}_test_log.xml
         # Store images in Google Artifact Registry
         images:
           - us-central1-docker.pkg.dev/$PROJECT_ID/$_AR_REPO_NAME/myimage:$SHORT_SHA

  7. Start the build using the [gcloud CLI](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers). You must specify the Artifact Registry repository name when starting the build.

To specify the Artifact Registry repository when starting the build using the gcloud CLI:
         
         gcloud builds submit --region=us-west2 --config=cloudbuild.yaml \
             --substitutions=_AR_REPO_NAME="AR_REPO_NAME"
         

Replace `AR_REPO_NAME` with the name of your Artifact Registry repository.

To specify the Artifact Registry repository when building with build triggers, specify the name of your Artifact Registry repository in the **Substitution variables** field when [creating the build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers#build_trigger).




## What's next

  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).
  * Learn how to [build container images](https://docs.cloud.google.com/build/docs/building/build-containers).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
