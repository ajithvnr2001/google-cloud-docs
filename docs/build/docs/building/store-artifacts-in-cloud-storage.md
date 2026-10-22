---
url: https://docs.cloud.google.com/build/docs/building/store-artifacts-in-cloud-storage/
title: Storing build artifacts in Cloud Storage \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:28.392250+00:00
---

# Storing build artifacts in Cloud Storage  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/building/store-artifacts-in-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Storing build artifacts in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can store build artifacts in Cloud Storage.

We recommend using Artifact Registry for storing build artifacts. Artifact Registry is a Google Cloud product that you can integrate with Cloud Build to securely store and manage your artifacts in private or public repositories. Storing artifacts in Artifact Registry enables you to:

  * Manage container metadata and scan for container vulnerabilities with [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs).
  * Enforce deployment policies with [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs).
  * [Use image streaming in Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming), which is particularly beneficial for large container images.



For instructions on configuring Cloud Build to store packages and images from your builds in Artifact Registry, see [Store artifacts in Artifact Registry](https://docs.cloud.google.com/build/docs/building/store-artifacts-in-artifact-registry). 

## Storing artifacts in Cloud Storage

**To store non-container artifacts in Cloud Storage** , add an `artifacts` field in your build config file with the location of the bucket to store the artifact and the path to one or more artifacts:

###  YAML 
    
    
    artifacts:
      objects:
        location: [STORAGE_LOCATION]
        paths: [[ARTIFACT_PATH],[ARTIFACT_PATH], ...]
    

Where,

  * `[STORAGE_LOCATION]`: A Cloud Storage bucket or a folder within the bucket where Cloud Build must store the artifact, such as `gs://mybucket` or `gs://mybucket/myproject/builds`. To find the names of existing buckets, see [list buckets](https://docs.cloud.google.com/storage/docs/listing-buckets) or [create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * `[ARTIFACT_PATH]`: Path to one or more artifacts. `[ARTIFACT_PATH]` is relative to your working directory. This can be either `/workspace`, which is Cloud Build's default working directory or the working directory you set using the [`dir`](https://docs.cloud.google.com/build/docs/build-config-file-schema#build_steps) field.



###  JSON 
    
    
    {
        "artifacts": {
            "objects": {
                "location": [
                    "[STORAGE_LOCATION]"
                ],
                "paths": [
                [
                    "[ARTIFACT_PATH]"
                ],
                [
                    "[ARTIFACT_PATH]"
                ],
                "..."
                ]
            }
        }
    }
    

Where,

  * `[STORAGE_LOCATION]`: A Cloud Storage bucket or a folder within the bucket where Cloud Build must store the artifact, such as `gs://mybucket` or `gs://mybucket/myproject/builds`. To find the names of existing buckets, see [list buckets](https://docs.cloud.google.com/storage/docs/listing-buckets) or [create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * `[ARTIFACT_PATH]`: Path to one or more artifacts. `[ARTIFACT_PATH]` is relative to your working directory. This can be either `/workspace`, which is Cloud Build's default working directory or the working directory you set using the [`dir`](https://docs.cloud.google.com/build/docs/build-config-file-schema#build_steps) field.



Note the following caveats when storing artifacts in Cloud Storage:

  * You can specify only one bucket to upload the artifacts and you must be the owner of the bucket. You can specify a valid directory path in the bucket.

  * You can upload any number of artifacts, but you can specify only up to one hundred artifact paths.

  * If you upload an artifact to a bucket that already has an artifact with the same name, the new artifact will replace the existing artifact. You can enable [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) for your bucket if you don't want the newer artifact to replace an existing artifact with the same name.




After the build completes successfully, you can find the upload results in the JSON manifest file located at `[STORAGE_LOCATION]/artifacts-$BUILD_ID.json`.

The JSON manifest file has the following fields:

  * `location`: this specifies the location in Cloud Storage where an artifact is stored and is of the form `gs://[STORAGE_LOCATION]/[FILE_NAME]#[GENERATION_NUMBER]`. You can use the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) to uniquely identify a version of the data in Cloud Storage bucket.
  * `file_hash`: this specifies the hash type and the value. The hash type is always 2, which specifies that MD5 hash was performed.



## Artifacts examples

The following examples show how you can use the `Artifacts` field in a build config file. In all of these examples replace `[VALUES_IN_BRACKETS]` with the appropriate values.

### Uploading files and folders

The build config file below uploads `helloworld.class` to the`gs://[STORAGE_LOCATION]/`:

###  YAML 
    
    
    steps:
    - name: 'gcr.io/cloud-builders/javac'
      args: ['HelloWorld.java']
    artifacts:
      objects:
        location: 'gs://[STORAGE_LOCATION]/'
        paths: ['HelloWorld.class']
    

###  JSON 
    
    
    {
        "steps": [
        {
            "name": "gcr.io/cloud-builders/javac",
            "args": [
                "HelloWorld.java"
            ]
        }
        ],
        "artifacts": {
            "objects": {
                "location": "gs://[STORAGE_LOCATION]/",
                "paths": [
                    "HelloWorld.class"
                ]
            }
        }
    }
    

To upload more than one artifact, specify the path to each artifact separated by a comma. The following example uploads `HelloWorld.java`, `HelloWorld.class`, and `cloudbuild.yaml` to `gs://[STORAGE_LOCATION]/`:

###  YAML 
    
    
    steps:
    - name: 'gcr.io/cloud-builders/javac'
      args: ['HelloWorld.java']
    artifacts:
      objects:
        location: 'gs://[STORAGE_LOCATION]/'
        paths: ['HelloWorld.java', 'HelloWorld.class', 'cloudbuild.yaml']
    

###  JSON 
    
    
    {
        "steps": [
        {
            "name": "gcr.io/cloud-builders/javac",
            "args": [
                "HelloWorld.java"
            ]
        }
        ],
        "artifacts": {
            "objects": {
                "location": "gs://[STORAGE_LOCATION]/",
                "paths": [
                    "HelloWorld.java",
                    "HelloWorld.class",
                    "cloudbuild.yaml"
                ]
            }
        }
    }
    

You can also upload the artifacts to a valid directory path in the bucket. The following example uploads `HelloWorld.java` and `HelloWorld.class` to `gs://[BUCKET_NAME]/[FOLDER_NAME]`:

###  YAML 
    
    
    steps:
    - name: 'gcr.io/cloud-builders/javac'
      args: ['HelloWorld.java']
    artifacts:
      objects:
        location: 'gs://[BUCKET_NAME]/[FOLDER_NAME]'
        paths: ['HelloWorld.java', 'HelloWorld.class']
    

###  JSON 
    
    
    {
        "steps": [
        {
            "name": "gcr.io/cloud-builders/javac",
            "args": [
                "HelloWorld.java"
            ]
        }
        ],
        "artifacts": {
            "objects": {
                "location": "gs://[BUCKET_NAME]/[FOLDER_NAME]",
                "paths": [
                    "HelloWorld.java",
                    "HelloWorld.class"
                ]
            }
        }
    }
    

### Using wildcard characters to upload more than one artifact

When uploading multiple artifacts, you can use [wildcard characters](https://docs.cloud.google.com/storage/docs/wildcards) in `paths` to specify multiple files.

The following example takes as an argument a file named `classes`, which contains the names of the `.java` files to compile. It then uploads any `.class` file to the specified Cloud Storage bucket:

###  YAML
    
    
    steps:
    - name: 'gcr.io/cloud-builders/javac'
      args: ['@classes']
    artifacts:
      objects:
        location: 'gs://[STORAGE_LOCATION]/'
        paths: ['*.class']
    

###  JSON 
    
    
    {
        "steps": [
        {
            "name": "gcr.io/cloud-builders/javac",
            "args": [
                "@classes"
            ]
        }
        ],
        "artifacts": {
            "objects": {
                "location": "gs://[STORAGE_LOCATION]/",
                "paths": [
                    "*.class"
                ]
            }
        }
    }
    

### Using substitution variables in the bucket location

You can use [substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) to specify a folder within the Cloud Storage bucket. If the folder you've specified doesn't exist, Cloud Build will create it for you.

The example below uploads the artifacts to a Cloud Storage path that includes the name of your Google Cloud project from which the build was run (such as gs://mybucket/myproject/):

###  YAML 
    
    
    steps:
    - name: 'gcr.io/cloud-builders/javac'
      args: ['@classes']
    artifacts:
      objects:
        location: 'gs://[BUCKET_NAME]/$PROJECT_ID'
        paths: ['helloworld.class']
    

###  JSON 
    
    
    {
        "steps": [
        {
            "name": "gcr.io/cloud-builders/javac",
            "args": [
                "@classes"
            ]
        }
        ],
        "artifacts": {
            "objects": {
                "location": "gs://[BUCKET_NAME]/$PROJECT_ID",
                "paths": [
                    "helloworld.class"
                ]
            }
        }
    }
    

## What's next

  * Learn how to [build `Go` projects](https://docs.cloud.google.com/build/docs/building/build-go).
  * Learn how to start a build [manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) and [using triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
