---
url: https://docs.cloud.google.com/build/docs/running-builds/submit-build-via-cli-api/
title: Submit a build using CLI and API \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:05.638143+00:00
---

# Submit a build using CLI and API  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/running-builds/submit-build-via-cli-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Submit a build using CLI and API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to start a build in Cloud Build manually using the Google Cloud CLI and the Cloud Build API.

## Before you begin

  * To build using the Cloud Build build config, [create a build config file](https://docs.cloud.google.com/build/docs/building/build-containers#yaml).
  * Have your application source code and `Dockerfile` ready.
  * Have a Docker repository for storing images in Artifact Registry, or [create a repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).



### Required IAM permissions

To ensure that has the necessary permissions to submit builds, ask your administrator to grant the following IAM roles to on your service account: 

  * [Store build logs in the default logs bucket](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-default-bucket): [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`) 
  * [Store build logs in the user-created logs bucket](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-bucket): [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`) 
  * [Use private pools](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool): [Cloud Build WorkerPool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolUser) (`roles/cloudbuild.workerPoolUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Running builds

You can specify the source of your build using the [Build source](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#source) field. The Build source field is one of the following: [`storage_source`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#storagesource), `repo_source`, [`git_source`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#gitsource) and `connected_repository`.

### Submit builds with `storage_source`

###  gcloud 

**Using a Dockerfile** :

Your `Dockerfile` contains all information needed to build a Docker image using Cloud Build.

To build using a `Dockerfile`, run the following command from the directory containing your source code and the `Dockerfile`:
    
    
    gcloud builds submit --tag LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME
    

Where:

  * LOCATION: the regional or multi-regional location of your Docker repository in Artifact Registry.
  * PROJECT_ID: your Google Cloud project ID.
  * REPOSITORY: the name of your Artifact Registry repository.
  * IMAGE_NAME: the name of the container image to be built.



The full name of the image to be built is `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME`. Images pushed to Artifact Registry use the [Artifact Registry naming convention](https://docs.cloud.google.com/artifact-registry/docs/docker/names).

The `gcloud builds submit` command:

  * compresses your application code, `Dockerfile`, and any other assets in the current directory as indicated by `.`;
  * initiates a build in the location `LOCATION` using the uploaded files as input;
  * [tags the image using the provided name](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#tag-repo);
  * pushes the built image to Artifact Registry.



As the build progresses, its output is displayed in your shell or terminal window. When the build is complete, you should see an output similar to the following:
    
    
        DONE
        ---------------------------------------------------------------------------------
        ID                                    CREATE_TIME                DURATION STATUS
        $BUILD_ID                             2023-10-28T15:21:18+00:00  12S      SUCCESS
    

where `$BUILD_ID` is your build's unique identifier.

**Using the Cloud Build build config file** :

To submit a build using the build config, run the following command:
    
    
        gcloud builds submit --config BUILD_CONFIG SOURCE
    

Where:

  * BUILD_CONFIG is the path to the build config file.
  * SOURCE is the path or URL source code.



When you run `gcloud builds submit` for the first time in a Google Cloud project, Cloud Build creates a Cloud Storage bucket named `[YOUR_PROJECT_NAME]_cloudbuild` in that project. Cloud Build uses this bucket to store any source code that you might use for your builds. Cloud Build does not automatically delete contents in this bucket. To delete objects you're no longer using for builds, you can either [set up lifecycle configuration on the bucket](https://docs.cloud.google.com/storage/docs/lifecycle-configurations#deletion-example) or manually [delete the objects](https://docs.cloud.google.com/storage/docs/deleting-objects).

The following command demonstrates how to submit a `cloudbuild.yaml` build request using source code stored in a Cloud Storage bucket.
    
    
        gcloud builds submit --config cloudbuild.yaml \
            gs://BUCKET/SOURCE.tar.gz
    

Where:

  * BUCKET is the name of your bucket in Cloud Storage containing your source code to build.
  * SOURCE is the name of your compressed source code file.



You can use `.` to specify that the source code is in the current working directory:
    
    
        gcloud builds submit --config=cloudbuild.yaml .
    

###  API 

**To submit the build request using`curl`**:

  1. Create a file named `request.json` with the following contents:
         
         {
             "source": {
                 "storageSource": {
                     "bucket": "BUCKET",
                     "object": "SOURCE.tar.gz"
                 }
             },
             "steps": [{
                 "name": "gcr.io/cloud-builders/docker",
                 "args": [
                     "build",
                     "-t",
                     "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME",
                     "."
                 ]
             }],
             "images": [
                 "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME"
             ]
         }
         

Where:

     * BUCKET is the name of your [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets) containing your source code to build.
     * SOURCE is the name of your compressed source code file.
     * IMAGE_NAME is the name of the image to be built.
     * LOCATION: the regional or multi-regional location of your Docker repository in Artifact Registry.
     * PROJECT_ID: your Google Cloud project ID.
     * REPOSITORY: the name of your Docker repository in Artifact Registry.
**Note:** At build time, Cloud Build automatically replaces `$PROJECT_ID` with your project ID.

In this build request, Cloud Build calls the `docker` build step with the arguments `build -t LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY .`.

The full name of the image to be built is `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY`.

Images pushed to Artifact Registry use the [Artifact Registry naming convention](https://docs.cloud.google.com/artifact-registry/docs/docker/names).

  2. Run the following command, where `PROJECT_ID` is your Google Cloud project ID and `REGION` is one of the [supported regions](https://docs.cloud.google.com/build/docs/locations):
         
         curl -X POST -T request.json -H "Authorization: Bearer $(gcloud config config-helper \
             --format='value(credential.access_token)')" \
             https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/builds
         

In this command, `curl` sends `request.json` in a POST call to the `builds` endpoint for the [projects.builds.create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/create) API method.

The command displays details about your build in your shell or terminal window. The output is a JSON response and appears similar to the following:
         
         {
                 "name": "operations/build/$PROJECT-ID/NmZhZW...",
                 "metadata": {
                     "@type": "type.googleapis.com/google.devtools.cloudbuild.v1.BuildOperationMetadata",
                     "build": {
                         "id": $BUILD-ID,
                         "status": "QUEUED",
                         "source": {
                             "storageSource": {
                                 "bucket": "BUCKET",
                                 "object": "SOURCE.tar.gz"
                             }
                         },
                         "createTime": "2017-05-12T18:58:07.341526Z",
                         "steps": [
                         {
                             "name": "gcr.io/cloud-builders/docker",
                             "args": [
                                 "build",
                                 "-t",
                                 "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME",
                                 "."
                             ]
                         }
                         ],
                         "timeout": "600s",
                         "images": [
                             "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME"
                         ],
                         "projectId": $PROJECT-ID,
                         "logsBucket": "gs://...",
                         "sourceProvenance": {
                             "resolvedStorageSource": {
                                 "bucket": "BUCKET",
                                 "object": "SOURCE.tar.gz"
                                 "generation": "..."
                             }
                         },
                         "logUrl": "https://console.cloud.google.com/cloud-build/builds/...?project=$PROJECT_ID"
                     }
                 }
             }
         

The JSON response is modeled using the [`Operation`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/operations#Operation) resource in the Cloud Build API. The `metadata` field is modeled using the [`Build`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build) resource. The `QUEUED` status indicates that the build is awaiting execution.




### Submit builds with `connected_repository`

###  gcloud 

To run a build request with build source from a 2nd-gen repository resource, run the following command:
    
    
    gcloud builds submit REPOSITORY --revision=REVISION --config=BUILD_CONFIG LOCATION
    

Where:

  * LOCATION is the regional or multi-regional location of your Docker repository in Artifact Registry.
  * REPOSITORY is the name of the Cloud Build 2nd-gen repository, formatted as `projects/*/locations/*/connections/*/repositories/*`.
  * REVISION is the revision to fetch from the Git repository such as a branch, a tag, a commit SHA, or any Git ref.
  * BUILD_CONFIG is the path to the build config file.



As the build progresses, its output is displayed in your shell or terminal window. When the build is complete, you should see an output similar to the following:
    
    
        DONE
        ---------------------------------------------------------------------------------
        ID                                    CREATE_TIME                DURATION STATUS
        $BUILD_ID                             2023-10-28T15:21:18+00:00  12S      SUCCESS
    

where `$BUILD_ID` is your build's unique identifier.

**gcloudignore** : When including source code for the build, the previous command uploads all of the files in the specified directory to Google Cloud to build. If you want to exclude certain files in the directory, then you can include a file named `.gcloudignore` in the top-level upload directory; the files that it specifies will be ignored. If `.gcloudignore` isn't present in the top-level upload directory, but a `.gitignore` file is, the gcloud CLI generates a Git-compatible `.gcloudignore` file that respects your `.gitignore`-ed files. For more information, see the [`gcloudignore` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore).

If you don't have source code to pass in to your build, use the `--no-source` flag where BUILD_CONFIG is the path to the build config file:
    
    
        gcloud builds submit --config CONFIG_FILE_PATH SOURCE_DIRECTORY
    

###  API 

**To submit the build request using`curl`**:

  1. Create a file named `request.json` with the following contents:
         
         {
             "source": {
                 "connectedRepository": {
                     "repository": "REPOSITORY",
                     "revision": "REVISION"
                 }
             },
             "steps": [{
                 "name": "gcr.io/cloud-builders/docker",
                 "args": [
                     "build",
                     "-t",
                     "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME",
                     "."
                 ]
             }],
             "images": [
                 "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME"
             ]
         }
         

Where:

     * REPOSITORY is the name of the Cloud Build 2nd-gen repository, formatted as `projects/*/locations/*/connections/*repositories/*`.
     * REVISION is the revision to fetch from the Git repository such as a branch, a tag, a commit SHA, or any Git ref.
     * IMAGE_NAME is the name of the image to be built.
     * LOCATION: the regional or multi-regional location of your Docker repository in Artifact Registry.
     * PROJECT_ID: your Google Cloud project ID.
**Note:** At build time, Cloud Build automatically replaces `$PROJECT_ID` with your project ID.

In this build request, Cloud Build calls the `docker` build step with the arguments `build -t LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME .`.

The full name of the image to be built is `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME`. Images pushed to Artifact Registry use the [Artifact Registry naming convention](https://docs.cloud.google.com/artifact-registry/docs/docker/names).

  2. Run the following command where `PROJECT_ID` is your Google Cloud project ID and REGION is one of the [supported regions](https://docs.cloud.google.com/build/docs/locations):
         
         curl -X POST -T request.json -H "Authorization: Bearer $(gcloud config config-helper \
             --format='value(credential.access_token)')" \
             https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/builds
         

In this command, `curl` sends `request.json` in a POST call to the `builds` endpoint for the [projects.builds.create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/create) API method.

The command displays details about your build in your shell or terminal window. The output is a JSON response and appears similar to the following:
         
         {
                 "name": "operations/build/$PROJECT-ID/NmZhZW...",
                 "metadata": {
                     "@type": "type.googleapis.com/google.devtools.cloudbuild.v1.BuildOperationMetadata",
                     "build": {
                         "id": $BUILD-ID,
                         "status": "QUEUED",
                         "source": {
                             "connectedRepository": {
                                 "repository": "REPOSITORY",
                                 "revision": "REVISION"
                             }
                         },
                         "createTime": "2017-05-12T18:58:07.341526Z",
                         "steps": [
                         {
                             "name": "gcr.io/cloud-builders/docker",
                             "args": [
                                 "build",
                                 "-t",
                                 "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME",
                                 "."
                             ]
                         }
                         ],
                         "timeout": "600s",
                         "images": [
                             "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME"
                         ],
                         "projectId": PROJECT_ID,
                         "logsBucket": "gs://...",
                         "sourceProvenance": {
                             "resolvedConnectedRepository": {
                                 "repository": "REPOSITORY",
                                 "revision": "REVISION.tar.gz"
                                 "generation": "..."
                             }
                         },
                         "logUrl": "https://console.cloud.google.com/cloud-build/builds/...?project=PROJECT_ID"
                     }
                 }
             }
         

The JSON response is modeled using the [`Operation`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/operations#Operation) resource in the Cloud Build API. The `metadata` field is modeled using the [`Build`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build) resource. The `QUEUED` status indicates that the build is awaiting execution.




## What's next

  * Learn how to [create manual triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manual-triggers).
  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
