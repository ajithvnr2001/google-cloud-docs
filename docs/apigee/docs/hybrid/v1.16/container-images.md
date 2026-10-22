---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/container-images/
title: Use a private image repository with Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:50.490035+00:00
---

# Use a private image repository with Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Use a private image repository with Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/container-images.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/container-images.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/container-images.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/container-images.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/container-images.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/container-images.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/container-images.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/container-images.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/container-images.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/container-images.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/container-images.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/container-images.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/container-images.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/container-images.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/container-images.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/container-images.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/container-images.html)



This document explains how to configure Apigee hybrid to use images from a private container image repository. 

##  Overview 

All Apigee hybrid runtime images are hosted in the [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) (AR). If for any reason you wish to employ a private image container repository, you can download the images from AR, push them to your private repository. Instead of overriding each component, you can add hub details on the overrides:

##  Configuration steps 

Set the value of the [`hub` configuration property](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#hub) with path to your private repository. 
    
    
    hub: PRIVATE_REPO

For example, if the following hub is provided, it will automatically resolve the image path: 
    
    
    hub: private-docker-host.example.com

as:
    
    
    ## an example of internal component vs 3rd party
    containers:
    - name: apigee-redis
      image: private-docker-host.example.com/apigee-redis:1.16.11
      imagePullPolicy: IfNotPresent
    
    containers:
    - name: apigee-ingressgateway
      image: private-docker-host.example.com/apigee-asm-ingress:1.22.6-asm.2-distroless
      imagePullPolicy: IfNotPresent

####  _Click to expand a list of Apigee images_
    
    
    apigee:
        gcr.io/apigee-release/hybrid/apigee-mart-server:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-synchronizer:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-runtime:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra-client:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-connect-agent:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-watcher:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-operators:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-redis:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-mint-task-scheduler:YOUR_HYBRID_VERSION_TAG
    third party:
        gcr.io/apigee-release/hybrid/apigee-stackdriver-logging-agent:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-prom-prometheus:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-stackdriver-prometheus-sidecar:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-kube-rbac-proxy:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-envoy:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-prometheus-adapter:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-asm-ingress:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-asm-istiod:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-fluent-bit:YOUR_HYBRID_VERSION_TAG
        gcr.io/apigee-release/hybrid/apigee-open-telemetry-collector:YOUR_HYBRID_VERSION_TAG

You can see the original version tag of third-party images as a label returned by the `docker history` or `docker inspect` commands. 

To display a list of the Apigee images hosted in the Google Cloud repository use the [`apigee-pull-push`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) command:
    
    
    ./apigee-operator/etc/tools/apigee-pull-push.sh --list

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
