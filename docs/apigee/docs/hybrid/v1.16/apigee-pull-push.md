---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push/
title: apigee-pull-push \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:13:29.305744+00:00
---

# apigee-pull-push  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  apigee-pull-push Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

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




## File location

`apigee-pull-push.sh` can be found in `$APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/`

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

Where REPO is the URL of the repository, for example `/gcr.io/apigee-release`. 

**Note:** The repository must be a protocol-less URL (without `HTTP` or `HTTPS`). 

For example, use `./apigee-pull-push.sh us-central1-docker.pkg.dev/apigee-hybrid-support-amer-01/hybrid`, instead of `./apigee-pull-push.sh https://us-central1-docker.pkg.dev/apigee-hybrid-support-amer-01/hybrid`.

###  Push the Apigee image to the default repository 
    
    
    apigee-pull-push.sh 

This command pushes the image to `us.gcr.io/PROJECT_ID`, for example `us.gcr.io/my-project`. 

###  List the images in your repository 

Use the `--list` or `-l` option to list all the images in your repository. 
    
    
    apigee-pull-push.sh --list

Example output: 
    
    
    apigee:
            gcr.io/apigee-release/hybrid/apigee-mart-server:1.16.11
            gcr.io/apigee-release/hybrid/apigee-synchronizer:1.16.11
            gcr.io/apigee-release/hybrid/apigee-runtime:1.16.11
            gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra-client:1.16.11
            gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra:1.16.11
            gcr.io/apigee-release/hybrid/apigee-connect-agent:1.16.11
            gcr.io/apigee-release/hybrid/apigee-watcher:1.16.11
            gcr.io/apigee-release/hybrid/apigee-operators:1.16.11
            gcr.io/apigee-release/hybrid/apigee-redis:1.16.11
            gcr.io/apigee-release/hybrid/apigee-mint-task-scheduler:1.16.11
    third party:
            gcr.io/apigee-release/hybrid/apigee-stackdriver-logging-agent:1.16.11
            gcr.io/apigee-release/hybrid/apigee-prom-prometheus:1.16.11
            gcr.io/apigee-release/hybrid/apigee-stackdriver-prometheus-sidecar:1.16.11
            gcr.io/apigee-release/hybrid/apigee-kube-rbac-proxy:1.16.11
            gcr.io/apigee-release/hybrid/apigee-envoy:1.16.11
            gcr.io/apigee-release/hybrid/apigee-prometheus-adapter:1.16.11
            gcr.io/apigee-release/hybrid/apigee-asm-ingress:1.16.11
            gcr.io/apigee-release/hybrid/apigee-asm-istiod:1.16.11
            gcr.io/apigee-release/hybrid/apigee-fluent-bit:1.16.11
            gcr.io/apigee-release/hybrid/apigee-open-telemetry-collector:1.16.11
    

**Note:** You can see the original version tag as the label returned by the `docker history` or `docker inspect` commands. For example: 
    
    
    docker history gcr.io/apigee-release/hybrid/apigee-stackdriver-prometheus-sidecar:0.10.0
    IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
    cb2c96a7aeab   3 months ago   /bin/sh -c #(nop)  **LABEL original-label=0.10.2**  0B
    

###  Get help for `apigee-pull-push.sh`
    
    
    apigee-pull-push.sh --help

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
