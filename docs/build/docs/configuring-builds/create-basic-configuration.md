---
url: https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration/
title: Create a build configuration file \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:27.929305+00:00
---

# Create a build configuration file  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Create a build configuration file Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a build configuration file that you can use to start a build on Cloud Build.

A build config file defines the fields that are needed for Cloud Build to perform your tasks. You'll need a build config file if you're starting builds using the [`gcloud` command-line tool](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [build triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds). You can write the build config file using the YAML or the JSON syntax.

## Before you begin

Read [Build Configuration Overview](https://docs.cloud.google.com/build/docs/build-config) to learn about the fields you can include in a build config file.

## Creating a build config

The following steps explain how to create a basic build config file. Each of the fields in the build config file defines a part of the task you want to perform. The only required field in the build config file is the `name` field for a step. All other fields are optional.

**Note:** The example config file mentioned on this page does not include all available fields. To learn about all fields you can include in a build config file, see [Build Configuration Overview](https://docs.cloud.google.com/build/docs/build-config).

###  YAML 

  1. **Create the build config file**. In your project root directory, create a file named `cloudbuild.yaml`. This is your Cloud Build config file.

  2. **Add the steps field**. The `steps` section in the build config file contains the build steps that you want Cloud Build to perform.
         
         steps:
         

  3. **Add the first step**. Under `steps:`, add a `name` field and point it to a container image to execute your task. Cloud Build and its developer community provides several container images with common tools and languages installed. You can use any of these images (also called **Cloud Builders**) or any publicly available image in a build step. For information on different types of container images you can use in a build step, see [Cloud Builders](https://docs.cloud.google.com/build/docs/cloud-builders).

The following snippet shows a build step with a `docker` builder `gcr.io/cloud-builders/docker`, which is a container image running Docker.
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
         

  4. **Add step arguments**. The `args` field of a step takes a list of arguments and passes them to the builder referenced by the `name` field. If the builder in the `name` field has an entrypoint, `args` in the list are used to access that entrypoint. If the builder in the `name` field does not have an entrypoint, the first element in `args` is used as the entrypoint.

In the following example:

     * `build` is the entrypoint to the Docker cloud builder.
     * `-t` is the Docker tag.
     * `us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/my-image` is the name of the image to be built in Artifact Registry. The build step uses the [default substitution](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions) for project ID, therefore this value is automatically substituted at build time.
     * `.` is the location of the source code, which indicates the source code is in the current working directory.
           
           steps:
           - name: 'gcr.io/cloud-builders/docker'
             args: ['build', '-t', 'us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/my-image', '.']
           

  5. **Add more steps**. You can add any number of build steps to your build config file by including additional `name` fields and pointing them to [cloud builders](https://cloud.google.com/build/docs/cloud-builders).

The following snippet includes two more steps to the build config file:

     * a docker build step to invoke the `docker push` command to push the image build in the previous step to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).
     * a build step for the Google Cloud SDK command with the `gcloud` entrypoint specified, which creates a Compute Engine instance from the container image in Artifact Registry. The `env` field is included to specify the Compute Engine zone and region.
           
           - name: 'gcr.io/cloud-builders/docker'
              args: ['push', 'us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/my-image']
            - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
              entrypoint: 'gcloud'
              args: ['compute', 'instances', 'create-with-container', 'my-vm-name', '--container-image', 'us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/my-image']
              env:
              - 'CLOUDSDK_COMPUTE_REGION=us-central1'
              - 'CLOUDSDK_COMPUTE_ZONE=us-central1-a'
           

  6. **Include additional build configuration fields**. You can configure the build further by including fields such as `machineType`, `tags`, or `timeout`. For the complete list of fields you can include in the build config file see [Build Configuration Overview](https://docs.cloud.google.com/build/docs/build-config).

In the following example, the `gcr.io/google.com/cloudsdktool/cloud-sdk` build step times out after 240 seconds.
         
         - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
             entrypoint: 'gcloud'
             timeout: 240s
             args: ['compute', 'instances', 'create-with-container', 'my-vm-name', '--container-image', 'us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/my-image']
             env:
             - 'CLOUDSDK_COMPUTE_REGION=us-central1'
             - 'CLOUDSDK_COMPUTE_ZONE=us-central1-a'
         

See the following snippet for the complete example of a basic build config file:
         
         steps:
           # Docker Build
           - name: 'gcr.io/cloud-builders/docker'
             args: ['build', '-t', 
                    'us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage', 
                    '.']
         
           # Docker Push
           - name: 'gcr.io/cloud-builders/docker'
             args: ['push', 
                    'us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage']
         
           # Entrypoint, timeout and environment variables
           - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
             entrypoint: 'gcloud'
             timeout: 240s
             args: ['compute', 'instances', 
                    'create-with-container', 'my-vm-name',
                    '--container-image', 
                    'us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage']
             env:
               - 'CLOUDSDK_COMPUTE_REGION=us-central1'
               - 'CLOUDSDK_COMPUTE_ZONE=us-central1-a'

In the example, container images are stored in Artifact Registry. If your build produces any non-container artifacts, you can store them in Cloud Storage using the `artifacts` field. For instructions on doing this, see [Storing Images and Artifacts](https://docs.cloud.google.com/build/docs/configuring-builds/store-images-artifacts).




###  JSON 

  1. **Create the build config file**. In your project root directory, create a file named `cloudbuild.json`. This is your Cloud Build config file.

  2. **Add the steps field**. The `steps` section in the build config file contains the build steps that you want Cloud Build to perform.
         
         {
            "steps":
         }
         

  3. **Add the first step**. Under `steps:`, add a `name` field and point it to a container image to execute your task. Cloud Build and its developer community provides several container images with common tools and languages installed. You can use any of these images (also called **Cloud Builders**) or any publicly available image in a build step. For information on different types of container images you can use in a build step, see [Cloud Builders](https://docs.cloud.google.com/build/docs/cloud-builders).

The following snippet shows a build step with a `docker` builder `gcr.io/cloud-builders/docker`, which is a container image running Docker.
         
         {
            "steps": [
               {
                  "name": "gcr.io/cloud-builders/docker"
               }
            ]
         }
         

  4. **Add step arguments**. The `args` field of a step takes a list of arguments and passes them to the builder referenced by the `name` field. If the builder in the `name` field has an entrypoint, `args` in the list are used to access that entrypoint. If the builder in the `name` field does not have an entrypoint, the first element in `args` is used as the entrypoint.

In the following example:

     * `build` is the entrypoint to the Docker cloud builder.
     * `-t` is the Docker tag.
     * `us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/my-image` is the name of the image to be built in Artifact Registry. The build step uses the [default substitution](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions) for project ID, therefore this value is automatically substituted at build time.
     * `.` is the location of the source code, which indicates the source code is in the current working directory.
           
           {
              "steps": [
                 {
                    "name": "gcr.io/cloud-builders/docker",
                    "args": [
                       "build",
                       "-t",
                       "us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage",
                       "."
                    ]
                 }
              ]
           }
           

  5. **Add more steps**. You can add any number of build steps to your build config file by including additional `name` fields and pointing them to [cloud builders](https://cloud.google.com/build/docs/cloud-builders).

The following snippet includes two more steps to the build config file:

     * a docker build step to invoke the `docker push` command to push the image build in the previous step to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).
     * a build step for the Google Cloud SDK command with the `gcloud` entrypoint specified, which creates a Compute Engine instance from the container image in Artifact Registry. The `env` field is included to specify the Compute Engine zone and region.
           
           {
                    "name": "gcr.io/cloud-builders/docker",
                    "args": [
                       "push",
                       "us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage"
                    ]
                 },
                 {
                    "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
                    "entrypoint": "gcloud",
                    "args": [
                       "compute",
                       "instances",
                       "create-with-container",
                       "my-vm-name",
                       "--container-image",
                       "us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage"
                    ],
                    "env": [
                       "CLOUDSDK_COMPUTE_REGION=us-central1",
                       "CLOUDSDK_COMPUTE_ZONE=us-central1-a"
                    ]
                 }
           

  6. **Include additional build configuration fields**. You can configure the build further by including fields such as `machineType`, `tags`, or `timeout`. For the complete list of fields you can include in the build config file see [Build Configuration Overview](https://docs.cloud.google.com/build/docs/build-config).

In the following example, the `gcr.io/google.com/cloudsdktool/cloud-sdk` build step times out after 240 seconds.
         
         {
                  "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
                  "entrypoint": "gcloud",
                  "timeout": "240s",
                  "args": [
                     "compute",
                     "instances",
                     "create-with-container",
                     "my-vm-name",
                     "--container-image",
                     "us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage"
                  ],
                  "env": [
                     "CLOUDSDK_COMPUTE_REGION=us-central1",
                     "CLOUDSDK_COMPUTE_ZONE=us-central1-a"
                  ]
               }
         

See the following snippet for the complete example of a basic build config file:
         
         {
            "steps": [
               {
                  "name": "gcr.io/cloud-builders/docker",
                  "args": [
                     "build",
                     "-t",
                     "us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage",
                     "."
                  ]
               },
               {
                  "name": "gcr.io/cloud-builders/docker",
                  "args": [
                     "push",
                     "us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage"
                  ]
               },
               {
                  "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
                  "entrypoint": "gcloud",
                  "timeout": "240s",
                  "args": [
                     "compute",
                     "instances",
                     "create-with-container",
                     "my-vm-name",
                     "--container-image",
                     "us-central1-docker.pkg.dev/${PROJECT_ID}/my-docker-repo/myimage"
                  ],
                  "env": [
                     "CLOUDSDK_COMPUTE_REGION=us-central1",
                     "CLOUDSDK_COMPUTE_ZONE=us-central1-a"
                  ]
               }
            ]
         }
         

In the example, container images are stored in Artifact Registry. If your build produces any non-container artifacts, you can store them in Cloud Storage using the `artifacts` field. For instructions on doing this, see [Storing Images and Artifacts](https://docs.cloud.google.com/build/docs/configuring-builds/store-images-artifacts).




## What's next

  * Learn how to run your builds [manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) and using [triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds) using the build config file.
  * Learn how to write build configs for [including dependencies, and building, testing, and deploying artifacts](https://docs.cloud.google.com/build/docs/configuring-builds/build-test-deploy-artifacts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
