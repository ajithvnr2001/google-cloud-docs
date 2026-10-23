---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/tutorials/cloud-build-integration/
title: Integrate the Connect gateway with Cloud Build \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:55.344717+00:00
---

# Integrate the Connect gateway with Cloud Build  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/tutorials/cloud-build-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Integrate the Connect gateway with Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

This is a basic tutorial on how to integrate [Cloud Build](https://docs.cloud.google.com/build/docs/overview) with the Connect gateway, letting you create a CI/CD pipeline for GKE clusters running across many different environments.

This tutorial assumes that you are familiar with the previous sections in [the Connect gateway guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway), and are also familiar with Cloud Build. These instructions leverage the [`cloud-sdk` builder image](https://github.com/GoogleCloudPlatform/cloud-sdk-docker) which requires some minor scripting (as you'll see below).

## Before you begin

  * Ensure that you have the following command line tools installed:

    * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which includes `gcloud`, the command-line tool for interacting with Google Cloud.
    * [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl), the command-line tool for interacting with Kubernetes.

If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  * Ensure that you have [initialized](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project.

  * Ensure the Connect gateway and other required APIs are enabled for your project, as described in the [setup guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup#enable_the_gateway_apis).




## 1\. Grant IAM roles to the Cloud Build service account

By default, Cloud Build uses a Google Cloud service account to run all required work, with an address in the format `MY_PROJECT_NUMBER-compute@cloudbuild.gserviceaccount.com`. You can find this service account email address for your project under **Cloud Build** \- **Permissions** in the [Google Cloud console](https://console.cloud.google.com/cloud-build/settings).

![Screenshot of Cloud Build settings page](https://docs.cloud.google.com/static/anthos/images/buildsettings.png)

Follow the instructions in [Grant IAM permissions](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup#grant_iam_roles_to_users) in the gateway setup guide to grant this account the required roles in your project.

## 2\. Specify RBAC policies for the Cloud Build service account

Follow the instructions in [Configure RBAC policies](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup#configure_role-based_access_control_rbac_policies) in the gateway setup guide to give the Cloud Build service account appropriate permissions on all the clusters you want to use.

We strongly recommend using [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) to deploy and maintain RBAC policies on multiple clusters.

## 3\. Create a Cloud Build pipeline

The Cloud Build workflow needs a `cloudbuild.yaml` file to configure the pipeline. The following is a simple example that deploys a static manifest to two different clusters (one GKE cluster on Google Cloud, and one on VMware). You can find out more about how to configure a Cloud Build pipeline in the [Cloud Build documentation](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).
    
    
    steps:
    - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
      entrypoint: bash
      id: Deploy to cluster on Google Cloud
      args:
      - '-c'
      - |
        set -x && \
        export KUBECONFIG="$(pwd)/gateway-kubeconfig" && \
        gcloud container fleet memberships get-credentials my-gke-cluster && \
        kubectl --kubeconfig gateway-kubeconfig apply -f myapp.yaml
    - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
      entrypoint: bash
      id: Deploy to cluster on VMware
      args:
      - '-c'
      - |
        set -x && \
        export KUBECONFIG="$(pwd)/gateway-kubeconfig" && \
        gcloud container fleet memberships get-credentials my-vmware-cluster && \
        kubectl --kubeconfig gateway-kubeconfig apply -f myapp.yaml
    

You can put any desired workflow in `myapp.yaml` to configure clusters. Here is an example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-nginx
    spec:
      selector:
        matchLabels:
          app: nginx
      replicas: 3
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.14.2
            ports:
            - containerPort: 80
    

Once you push your configuration to your Git repository, the Cloud Build workflow deploys the required application to the specified clusters. You can also set up Cloud Build to detect changes in the linked Git repository to trigger automated application update or installation.

## Advanced usage

Since it uses standard Cloud Build concepts, you can adapt and customize our example further to suit your particular CI/CD needs. In particular, if you want to build an image from scratch and deploy it in your pipeline, you can use the `gke-deploy` builder's [prepare mode](https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/gke-deploy/doc/gke-deploy_prepare.md). For example, the following Cloud Build configuration:

  1. Builds a docker image from the Dockerfile in the root of the Git repo and tags it with the Git SHA.
  2. Pushes the tagged image to the project’s [Container Registry](https://docs.cloud.google.com/container-registry/docs/overview).
  3. Prepares the Kubernetes manifests in the `manifest` directory by setting the correct image tag(s), placing the output manifests in `output/expanded`.
  4. Deploys to an GKE cluster on premises using the Connect gateway.


    
    
    steps:
    - name: 'gcr.io/cloud-builders/docker'
      id: "Build Container"
      args: ['build', '--tag=gcr.io/$PROJECT_ID/demo-app:$SHORT_SHA', '.']
    - name: 'gcr.io/cloud-builders/docker'
      id: "Push to GCR"
      args: ['push', 'gcr.io/$PROJECT_ID/demo-app:$SHORT_SHA']
    - name: "gcr.io/cloud-builders/gke-deploy"
      id: "Prepare Manifests"
      args:
      - prepare
      - --filename=manifests/
      - --image=gcr.io/$PROJECT_ID/demo-app:$SHORT_SHA
    - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
      entrypoint: bash
      id: "Deploy to cluster on VMware
      args:
      - '-c'
      - |
        set -x && \
        export KUBECONFIG="$(pwd)/gateway-kubeconfig" && \
        gcloud container fleet memberships get-credentials my-vmware-cluster && \
        kubectl --kubeconfig=gateway-kubeconfig apply -f output/expanded
    

Note that in this example we had to create an [image pull secret](http://docs.heptio.com/content/private-registries/pr-gcr.html) to authorize the on-premises GKE cluster to pull images from Container Registry.

For more ideas for Cloud Build usage, see the [Cloud Build documentation](https://docs.cloud.google.com/build/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
