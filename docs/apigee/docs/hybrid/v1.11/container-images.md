---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/container-images/
title: Use a private image repository with apigeectl \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:52:22.914196+00:00
---

# Use a private image repository with apigeectl  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Use a private image repository with apigeectl Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

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



**Note:** These procedures include instructions for using `apigeectl`. If you are using Helm charts to manage Apigee hybrid, see [Use a private image repository with Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/container-images-helm).

This document explains how to configure Apigee hybrid to use images from a private container image repository. 

##  Overview 

All Apigee hybrid runtime images are hosted in the [ Google Cloud Container Registry](https://docs.cloud.google.com/container-registry) (GCR). If for any reason you wish to employ a private image container repository, you can download the images from GCR, push them to your private repository, and override the default image locations in your `overrides.yaml` file.

##  Configuration steps 

Follow these steps to use a private image container repository for the Apigee hybrid images. To perform these steps and successfully use the images in your private repository, you must be familiar with the [Apigee hybrid installation procedure](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-before-begin). In a typical scenario, you would plan to configure the private repository as part of a fresh hybrid installation. 

  1. Push the Apigee hybrid images from GCR to your private repository. We recommend that you use the [apigee-push-pull](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/apigee-pull-push) utility to accomplish this step. 

If you prefer to do this step manually, you need to have [Docker](https://docs.docker.com/get-started/) installed and use the `docker pull` command as follows. Be sure to append the correct tag to each image name. For example, the tag for `apigee-synchronizer` is `1.11.2`, as shown below.

     1. Get an up to date list of all images in your current project with the `--list` option of the [`apigee-pull-push.sh` utility](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/apigee-pull-push) in the `apigeectl/tools/` directory: 
            
            apigee-pull-push.sh --list

Your output should look something like:
    
    apigee:
            gcr.io/apigee-release/hybrid/apigee-mart-server:1.11.2
            gcr.io/apigee-release/hybrid/apigee-synchronizer:1.11.2
            gcr.io/apigee-release/hybrid/apigee-runtime:1.11.2
            gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra-client:1.11.2
            gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra:1.11.2
            gcr.io/apigee-release/hybrid/apigee-cassandra-backup-utility:1.11.2
            gcr.io/apigee-release/hybrid/apigee-udca:1.11.2
            gcr.io/apigee-release/hybrid/apigee-connect-agent:1.11.2
            gcr.io/apigee-release/hybrid/apigee-watcher:1.11.2
            gcr.io/apigee-release/hybrid/apigee-operators:1.11.2
            gcr.io/apigee-release/hybrid/apigee-installer:1.11.2
            gcr.io/apigee-release/hybrid/apigee-redis:1.11.2
            gcr.io/apigee-release/hybrid/apigee-diagnostics-collector:1.11.2
            gcr.io/apigee-release/hybrid/apigee-diagnostics-runner:1.11.2
            gcr.io/apigee-release/hybrid/apigee-mint-task-scheduler:1.11.2
    third party:
            gcr.io/apigee-release/hybrid/apigee-stackdriver-logging-agent:1.10.5
            gcr.io/apigee-release/hybrid/apigee-prom-prometheus:v2.52.0
            gcr.io/apigee-release/hybrid/apigee-stackdriver-prometheus-sidecar:0.9.0
            gcr.io/apigee-release/hybrid/apigee-kube-rbac-proxy:v0.18.0
            gcr.io/apigee-release/hybrid/apigee-envoy:v1.27.0
            gcr.io/apigee-release/hybrid/apigee-prometheus-adapter:v0.12.0
            gcr.io/apigee-release/hybrid/apigee-asm-ingress:1.18.7-asm.26-distroless
            gcr.io/apigee-release/hybrid/apigee-asm-istiod:1.18.7-asm.26-distroless
            gcr.io/apigee-release/hybrid/apigee-fluent-bit:3.0.3
    

  2. Pull the images needed for the `apigee-system` and `apigee` namespaces with the `docker pull` command. For example: 
         
         docker pull gcr.io/apigee-release/hybrid/apigee-installer:1.11.2

The following list shows the images needed for each namespace:

### `apigee-system` namespace

     * `apigee-installer`
     * `apigee-kube-rbac-proxy`
     * `apigee-operators`

### Your `apigee` namespace

     * `apigee-asm-ingress`
     * `apigee-asm-istiod`
     * `apigee-cassandra-backup-utility`
     * `apigee-connect-agent`
     * `apigee-diagnostics-collector`
     * `apigee-diagnostics-runner`
     * `apigee-envoy`
     * `apigee-fluent-bit`
     * `apigee-hybrid-cassandra-client`
     * `apigee-hybrid-cassandra`
     * `apigee-mart-server`
     * `apigee-prom-prometheus`
     * `apigee-prometheus-adapter`
     * `apigee-redis`
     * `apigee-runtime`
     * `apigee-stackdriver-logging-agent`
     * `apigee-stackdriver-prometheus-sidecar`
     * `apigee-synchronizer`
     * `apigee-udca`
     * `apigee-watcher`
  3. After you pull and tag the images, push them to your private repository. See [docker push](https://docs.docker.com/engine/reference/commandline/push/). 


* Create a Kubernetes Secret in the `apigee` and `apigee-system` namespaces. 

If these namespaces do not exist in your cluster, you must create them before performing this step.

For steps to create the Secret, see [Create a Secret by providing credentials on the command line](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-secret-by-providing-credentials-on-the-command-line). For example, to create a secret in the `apigee-system` namespace:
    
    
    kubectl create secret docker-registry SECRET_NAME -n apigee-system \
      --docker-server=YOUR_REGISTRY_SERVER \
      --docker-username=YOUR_DOCKER_USERNAME \
      --docker-email=YOUR_DOCKER_EMAIL \
      --docker-password="YOUR_DOCKER_PASSWORD)"

To create a Secret in the `apigee` namespace: 
    
    
    kubectl create secret docker-registry SECRET_NAME -n apigee \
      --docker-server=YOUR_REGISTRY_SERVER \
      --docker-username=YOUR_DOCKER_USERNAME \
      --docker-email=YOUR_DOCKER_EMAIL \
      --docker-password="YOUR_DOCKER_PASSWORD)"

* Add the Secret to your `overrides.yaml` file. Creation of the overrides file is described in the hybrid installation steps. See [Configure the cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-configure-cluster) for details. 
    
    
    imagePullSecrets:
      - name: SECRET_NAME

* Update your `overrides.yaml` file with image URLs for the images stored in your private repository. Each component that is stored in the repository has an `image:url` element. Use this element to specify the URL of each component image. For example: 
    
    
    mart:
      serviceAccountPath: /installdir/hybrid-files/service-accounts/hybrid-apigee-non-prod.json
      **image:
        url: my-docker.pkg.dev/hybrid-1/registry-name/apigee-mart-server**

Follow this pattern to update each top-level hybrid component in your `overrides.yaml` file with its private repository image URL. A complete example overrides file is provided with your hybrid installation in `**$APIGEECTL_HOME** /examples/private-overrides.yaml` directory.

**Note:** You only need to update the `url` property. You can accept the default values for the `tag` and `pullPolicy` properties. For a complete list of components and their configuration properties, see also [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref). 

You can now complete a new hybrid installation using the private images, or update your existing installation. See the [Apigee hybrid installation steps](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-before-begin) for more information. 

##  Installing cert-manager from a private repository 

To install `cert-manager` from your private repository, see [Installing with Helm](https://cert-manager.io/docs/installation/helm/). It is important that you install the same version of `cert-manager` as specified in the [Apigee hybrid installation](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-cert-manager) instructions to ensure compatibility. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
