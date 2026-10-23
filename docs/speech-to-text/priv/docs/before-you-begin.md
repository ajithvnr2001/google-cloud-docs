---
url: https://docs.cloud.google.com/speech-to-text/priv/docs/before-you-begin/
title: Quickstart: Before you begin \u00a0|\u00a0 Cloud Speech-to-Text private documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:36.076369+00:00
---

# Quickstart: Before you begin  |  Cloud Speech-to-Text private documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/priv/docs/before-you-begin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text)
  * [ Cloud Speech-to-Text On-Prem ](https://docs.cloud.google.com/speech-to-text/priv)
  * [ Documentation ](https://docs.cloud.google.com/speech-to-text/priv/docs)



Send feedback 

#  Quickstart: Before you begin Stay organized with collections  Save and categorize content based on your preferences. 

**Private feature**  
This product is a private feature. The documentation is publicly available but you must [contact Google](https://cloud.google.com/contact) for full access. 

This quickstart walks you through the series of actions that must be completed before you can [deploy the Speech-to-Text On-Prem API](https://docs.cloud.google.com/speech-to-text/priv/docs/deploy). For more information on the configurable API parameters that are exposed during installation and setup, see the [API configurations](https://docs.cloud.google.com/text-to-speech/priv/docs/configurations) page.

  1. Purchase a plan.
  2. Assign the required Identity Access Management (IAM) roles to a service account.
  3. Install the required tools.
  4. Create a Kubernetes cluster.
  5. Preconfigure the API from the command line (Optional- for CLI installation only).
  6. Install Istio for gRPC load balancing (Optional).



## Set up billing

On the Google Cloud Platform [solutions page](https://console.cloud.google.com/marketplace/details/speech-onprem/speech-to-text-on-prem), click **PURCHASE PLAN**. This should be done by a Billing Account Administrator. You can verify it by navigating from Google Cloud Platform Console left hand side navigation bar: **Billing - > Account Management**, then check the right hand side Role/Principal. This is only required once.

![](https://docs.cloud.google.com/static/speech-to-text/priv/docs/images/billing.png)

## Required IAM roles

  1. Locate the Google Cloud Platform project drop-down menu in your [dashboard](https://console.cloud.google.com/):

![](https://docs.cloud.google.com/static/speech-to-text/priv/docs/images/project.png)

  2. In the window that pops up, you can either choose an existing Google Cloud Platform project or create a new one. After you have selected the project you want to associate with Speech-to-Text On-Prem, navigate to the hamburger icon in the top left corner and select **IAM & Admin** \--> **IAM** to see the list of the service accounts associated with that project.

  3. Assign the following roles to service accounts belonging to the Google Cloud Platform project that you will use during installation. They can be assigned to a single service account or multiple separate accounts, but all accounts must belong to the same project. To edit service account permissions, click on the pencil icon to the right of the service account's name. You can also create new service accounts by clicking the **+ADD** button at the top of the IAM page in your Google Cloud Platform console.

Required IAM roles:

     * Project Viewer
     * Billing Account Administrator (Required to purchase a plan, not required for deployment)
     * Kubernetes Engine Admin (If deploying to GKE)
     * Kubernetes Engine Cluster Admin (If deploying to Anthos)



## Required tools

  1. Install the [Google Cloud CLI](https://cloud.google.com/sdk/gcloud).
  2. Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).



## Create a Kubernetes cluster

Make sure that you are running either a [GKE](https://cloud.google.com/kubernetes-engine/) or [Anthos](https://cloud.google.com/anthos/gke) cluster. Kubernetes clusters are [available](https://console.cloud.google.com/kubernetes/list) on Google Cloud Platform. If you have pre-existing clusters, you can choose one from the list that appears by checking the box at the far left of the cluster's name:

![](https://docs.cloud.google.com/static/speech-to-text/priv/docs/images/clusters.png)

If you don't have any pre-existing clusters you are prompted to create one. Make sure that the cluster's parameters match the recommendations in the list below (the default parameters are not sufficient). Record the cluster's **Name** and **Location** , as well as the name of the Google Cloud Platform project the cluster is deployed to.

Basic recommendations for cluster setup:

  * Release Channel: Regular.
  * Node pool size should be equal or larger than the $REPLICAS.
  * Node Machine Type: e2-standard-4 (4 vCPU, 16 GB Memory) or higher.
  * Enable autoscaling
  * Enable Istio if you need gRpc load balancing (Optional).
  * Enable Kubernetes Engine Monitoring if you want to export metrics to Stackdriver (Optional).



## Install Istio for gRPC load balancing (Optional)

In order to scale Speech-to-Text On-Prem, we rely on a L7 load balancer that is compatible with gRPC. While there are several options available, we provide an [Istio](https://istio.io/latest/docs/concepts/traffic-management/) sample configuration here. Be aware, **the default Kubernetes service L3 load balancing strategy is not sufficient**. You can follow either the [Google Cloud official guide](https://cloud.google.com/istio/docs/istio-on-gke/installing) or the [Istio official page](https://istio.io/) to install Istio. If you also want to export the metrics, follow [steps 1 and 2 (in the Configure your Kubernetes cluster section, below)](https://docs.cloud.google.com/speech-to-text/priv/docs/before-you-begin#configure_your_kubernetes_cluster) and then run the command below:
    
    
        kubectl get deployment/istio-pilot -n istio-system \
        && kubectl set env deployment/istio-pilot -n istio-system PILOT_HTTP10=1 \
        || kubectl set env deployment/istiod -n istio-system PILOT_HTTP10=1
    

The `PILOT_HTTP10=1` flag allows HTTP 1.0 requests to be made by our application. This is crucial for allowing the application to authenticate with Stackdriver (using the [Google Cloud Platform metadata server](https://cloud.google.com/compute/docs/storing-retrieving-metadata)) in order to publish telemetry.

## Preconfigure the API from the command line (Optional)

If you plan to perform a CLI-based installation, follow the instructions in this section.

### Configure your environment

  1. [Install Docker](https://docs.docker.com/get-docker/).
  2. [Install the `mpdev` tool](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/mpdev-references.md).



### Configure your Kubernetes cluster

  1. Set your **PROJECT** and **NAMESPACE** environment variables. **PROJECT** is the project id of the Google Cloud Platform project your cluster is deployed to. **NAMESPACE** is the name of the new namespace you will create in Step 3, below. You can input any value for **NAMESPACE** , but "speech" is a safe default.
         
         export PROJECT=<my-project-id>
         export CLUSTER_NAME=<name of the cluster>
         export LOCATION=<location of the cluster>
         export NAMESPACE=<new name for NAMESPACE>
         

  2. Fetch your [cluster's credentials](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials):
         
         gcloud container clusters get-credentials $CLUSTER_NAME
         --project $PROJECT --zone $LOCATION
         

  3. Create the namespace the application will be deployed to and assign it to the **NAMESPACE** name you created in step 1, above:
         
         kubectl create namespace ${NAMESPACE:?}
         

  4. Install the [Application CRD](https://github.com/kubernetes-sigs/application), which is required in order to use Google Cloud Platform marketplace apps:
         
         kubectl apply -f "https://raw.githubusercontent.com/GoogleCloudPlatform/marketplace-k8s-app-tools/master/crd/app-crd.yaml"
         

  5. Create a reporting secret. This value is used by the application to report usage back to Google, and is used for future billing. On the [solution page](https://console.cloud.google.com/marketplace/kubernetes/config/speech-onprem/speech-to-text-on-prem), under "Deploy via command line" tab, follow only instructions 1 & 2 to generate & deploy the license reporting secret.


**Note:** Before running `kubectl apply`, make sure that you update `license.yaml`. Set the value of `metadata.name` to `reporting-secret`, and `metadata.namespace` to the value chosen for `$NAMESPACE`.

![](https://docs.cloud.google.com/static/speech-to-text/priv/docs/images/reporting.png)

## What's next

Learn how to [deploy](https://docs.cloud.google.com/speech-to-text/priv/docs/deploy) the Speech-to-Text On-Prem API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
