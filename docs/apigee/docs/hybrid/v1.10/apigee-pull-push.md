---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-pull-push/
title: apigee-pull-push \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:37:35.433814+00:00
---

# apigee-pull-push  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-pull-push/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  apigee-pull-push Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/apigee-pull-push.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/apigee-pull-push.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/apigee-pull-push.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/apigee-pull-push.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/apigee-pull-push.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/apigee-pull-push.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-pull-push.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/apigee-pull-push.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/apigee-pull-push.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/apigee-pull-push.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/apigee-pull-push.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/apigee-pull-push.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/apigee-pull-push.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/apigee-pull-push.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/apigee-pull-push.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/apigee-pull-push.html)



`apigee-pull-push.sh` is a utility that pulls all the images for the current Google Cloud project from the [Google Cloud Container Registry](https://cloud.google.com/container-registry/) and pushes them to your specified repository.

**Note:** You can set the current project with `gcloud config set project` or `gcloud init`.

##  Requirements 

  * Access to the [Google Cloud Container Registry](https://cloud.google.com/container-registry/)
  * `gcloud`. 

To install or upgrade `gcloud`, see [Installing Google Cloud SDK](https://docs.cloud.google.com/sdk/docs/install)




## Usage

### Syntax

`**apigee-pull-push [REPO] [--list] [--help]**`

###  _Optional:_ Check the current project in your `gcloud` context 

This step is optional, because `apigee-pull-push.sh` will confirm the project and allow you to proceed or abort. 

`apigee-pull-push.sh` pulls the images for the current project in your `gcloud` context. Check the project with the following command: 
    
    
    gcloud config list core/project --format='value(core.project)'

You can set the current project with the following command: 
    
    
    gcloud config set project PROJECT_ID

Where PROJECT_ID is the ID of the Google Cloud project for your Apigee hybrid installation. 

###  Push the Apigee hybrid image to a repository you name 
    
    
    apigee-pull-push.sh REPO

Where REPO is the URL of the repository, for example `https://gcr.io/apigee-release`. 

###  Push the Apigee image to the default repository 
    
    
    apigee-pull-push.sh 

This command pushes the image to `us.gcr.io/PROJECT_ID`, for example `us.gcr.io/my-project`. 

###  List the images in your repository 

Use the `--list` or `-l` option to list all the images in your repository. 
    
    
    apigee-pull-push.sh --list

Example output: 
    
    
    apigee:
            gcr.io/apigee-release/hybrid/apigee-mart-server:1.3.6
            gcr.io/apigee-release/hybrid/apigee-synchronizer:1.3.6
            gcr.io/apigee-release/hybrid/apigee-runtime:1.3.6
            gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra-client:1.3.6
            gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra:1.3.6
            gcr.io/apigee-release/hybrid/apigee-cassandra-backup-utility:1.3.6
            gcr.io/apigee-release/hybrid/apigee-udca:1.3.6
            gcr.io/apigee-release/hybrid/apigee-connect-agent:1.8.0
            gcr.io/apigee-release/hybrid/apigee-watcher:1.8.0
            gcr.io/apigee-release/hybrid/apigee-operators:1.8.0
            gcr.io/apigee-release/hybrid/apigee-installer:1.8.0
            gcr.io/apigee-release/hybrid/apigee-redis:1.8.0
            gcr.io/apigee-release/hybrid/apigee-diagnostics-collector:1.8.0
            gcr.io/apigee-release/hybrid/apigee-diagnostics-runner:1.8.0
    third party:
            gcr.io/apigee-release/hybrid/apigee-stackdriver-logging-agent:1.10.1
            gcr.io/apigee-release/hybrid/apigee-prom-prometheus:v2.48.0
            gcr.io/apigee-release/hybrid/apigee-stackdriver-prometheus-sidecar:0.9.0
            gcr.io/apigee-release/hybrid/apigee-kube-rbac-proxy:v0.15.0
            gcr.io/apigee-release/hybrid/apigee-envoy:v1.27.0
            gcr.io/apigee-release/hybrid/apigee-prometheus-adapter:v0.11.2
            gcr.io/apigee-release/hybrid/apigee-asm-ingress:1.18.7-asm.26-distroless
            gcr.io/apigee-release/hybrid/apigee-asm-istiod:1.18.7-asm.26-distroless
            gcr.io/apigee-release/hybrid/apigee-fluent-bit:2.2.0
    

###  Get help for `apigee-pull-push.sh`
    
    
    apigee-pull-push.sh --help

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
