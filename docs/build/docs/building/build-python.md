---
url: https://docs.cloud.google.com/build/docs/building/build-python/
title: Build and test Python applications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:03.855342+00:00
---

# Build and test Python applications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/building/build-python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build and test Python applications Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Cloud Build to build and test your Python applications, upload your artifacts to Artifact Registry, generate provenance information, and save your test logs in Cloud Storage.

Cloud Build enables you to use any publicly available container image to execute your tasks. The public [`python` image from Docker Hub](https://hub.docker.com/_/python/) comes preinstalled with `python` and `pip` tools. You can configure Cloud Build use these tools to install dependencies, build, and run unit tests using these tools.

## Before you begin

The instructions on this page assume that you are familiar with Python. In addition:

  * Enable the Cloud Build, Artifact Registry, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,artifactregistry.googleapis.com,storage.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/building/build-python)

  * To run the `gcloud` commands on this page, install [Google Cloud CLI](https://docs.cloud.google.com/sdk).
  * Have your Python project handy.
  * Have a Python repository in Artifact Registry. If you don't have one, then [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  * If you want to store test logs in Cloud Storage, [create a bucket in Cloud Storage](https://docs.cloud.google.com/storage/docs/creating-buckets).



### Required IAM permissions

  * To store test logs in Logging, grant the [Storage Object Creator (`roles/storage.objectCreator`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) role for the Cloud Storage bucket to your build service account.

  * To store built images in Artifact Registry, grant the [Artifact Registry Writer (`roles/artifactregistry.writer`) role](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the your build service account.




For instructions on granting these roles see [Granting a role using the IAM page](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page).

## Configuring Python builds

This section walks through an example build config file for a Python app. It has build steps to manage installation requirements, add unit tests, and after the tests pass, to build and deploy the app.

  1. In your project root directory, create [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config) named `cloudbuild.yaml`.

  2. **Install requirements** : The `python` image from Docker Hub comes preinstalled with `pip`. To install dependencies from `pip`, add a build step with the following fields:

     * `name`: Set the value of this field to `python` or `python:<tag>` to use the python image from Docker Hub for this task. To see a list of available tags for other Python images, see the [Docker Hub reference for the python image](https://hub.docker.com/_/python/tags).
     * `entrypoint`: Setting this field overrides the default entrypoint of the image referenced in `name`. Set the value of this field to `pip` to invoke `pip` as the entrypoint of the build step and run `pip` commands.
     * `args`: The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field. Pass the arguments to run the `pip install` command in this field. `--user` flag in the `pip install` command ensures that the subsequent build steps can access the modules installed in this build step.

The following build step adds arguments to install requirements:
    
    steps:
        - name: 'python'
          entrypoint: 'python'
          args: ['-m', 'pip', 'install', '--upgrade', 'pip']
        - name: python
          entrypoint: python
          args: ['-m', 'pip', 'install', 'build', 'pytest', 'Flask', '--user']
    

  3. **Add unit tests** : If you've defined unit tests in your application using a testing framework such as `pytest`, you can configure Cloud Build to run the tests by adding the following fields in a build step:

     * `name`: Set the value of this field to `python` to use the python image from Docker Hub for your task.
     * `entrypoint`: Set the value of this field to `python` to run `python` commands.
     * `args`: Add the arguments for running the `python pytest` command.

The following build step saves the `pytest` log output to a JUNIT XML file. The name of this file is constructed using `$SHORT_SHA`, [the short version of the commit ID associated with your build](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions). A subsequent build step will save the logs in this file to Cloud Storage.
    
    - name: 'python'
          entrypoint: 'python'
          args: ['-m', 'pytest', '--junitxml=${SHORT_SHA}_test_log.xml']
    

  4. **Build** : In your build config file, define the builder and the `args` to build your application:

     * `name`: Set the value of this field to `python` to use the python image from Docker Hub for your task.
     * `entrypoint`: Set the value of this field to `python` to run `python` commands.
     * `args`: Add the arguments for executing your build.

The following build step starts the build:
    
    - name: 'python'
          entrypoint: 'python'
          args: ['-m', 'build']
    

  5. **Upload to Artifact Registry** :

In your config file, add the `pythonPackages` field and specify your Python repository in Artifact Registry:
         
         artifacts:
                pythonPackages:
                - repository: 'https://LOCATION-python.pkg.dev/PROJECT-ID/REPOSITORY'
                   paths: ['dist/*']
         

Replace the following values:

     * PROJECT-ID is the ID of the Google Cloud project that contains your Artifact Registry repository.
     * REPOSITORY is the ID of the repository.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  6. **Optional: Enable provenance generation**

Cloud Build can generate verifiable [Supply chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) build provenance metadata to help secure your continuous integration pipeline.

To enable provenance generation, add [`requestedVerifyOption: VERIFIED`](https://docs.cloud.google.com/build/docs/build-config-file-schema#options) to the `options` section in your config file.

  7. **Save test logs to Cloud Storage** : You can configure Cloud Build to store any test logs in Cloud Storage by specifying an existing bucket location and path to the test logs. The following build step stores the test logs that you saved in the JUNIT XML file to a Cloud Storage bucket:
         
         artifacts:
             objects:
                location: 'gs://${_BUCKET_NAME}/'
                paths:
                   - '${SHORT_SHA}_test_log.xml'
         

  8. **Start your build** : [manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [using build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

Once your build completes, you can [view repository details](https://docs.cloud.google.com/artifact-registry/docs/repositories/list-repos) in Artifact Registry.

You can also [view build provenance metadata](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#view) and [validate provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#validate_provenance).




## What's next

  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [safeguard builds](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds).
  * Learn how to [build and containerize Python applications](https://docs.cloud.google.com/build/docs/building/build-containerize-python).
  * Learn how to [use private dependencies](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build#python).
  * Learn how to [perform blue/green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
