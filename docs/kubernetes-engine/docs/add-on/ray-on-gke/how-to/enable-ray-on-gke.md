---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke/
title: Enable the Ray operator on Google Kubernetes Engine (GKE) \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:42.592796+00:00
---

# Enable the Ray operator on Google Kubernetes Engine (GKE)  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Enable the Ray operator on Google Kubernetes Engine (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to enable the Ray operator for Google Kubernetes Engine (GKE), letting you use the KubeRay APIs to scale and manage Ray clusters. For more information on Ray and KubeRay, see [Ray on GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable the Ray operator for a cluster

You can enable the Ray operator on new or existing Autopilot or Standard GKE clusters using the Google Cloud CLI, the Google Cloud console, or Terraform.

###  Console 

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click add_box **Create** , and then in the Standard or Autopilot section, click **Configure**.

  3. In the navigation pane, click **Advanced settings** , and then do one of the following:

     * **Autopilot** : In the **AI and Machine Learning** section, select the **Enable Ray Operator** checkbox.
     * **Standard** : In the **Ray Operator** row, click _edit_ **Edit configuration** , select the **Enable Ray Operator** checkbox, and click **Save**.
  4. Click **Create**.




###  gcloud 

### Standard

Create a Standard cluster with the Ray Operator enabled.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --cluster-version=VERSION \
        --addons=RayOperator
    

### Autopilot

Create an Autopilot cluster with the Ray Operator enabled.
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --cluster-version=VERSION \
        --enable-ray-operator
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `VERSION`: the GKE version, which must be 1.30.0-gke.1747000 or later. You can also use the `--release-channel` option to select a release channel. The release channel must have a default version of 1.30.0-gke.1747000 or later.



You can enable the Ray operator on an existing cluster by using the [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) command with option `--update-addons=RayOperator=ENABLED`.

###  Terraform 

The following Terraform example creates and configures a Standard cluster:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-standard-regional-ray-operator"
      location = "us-west1"
    
      initial_node_count = 1
    
      release_channel {
        channel = "RAPID"
      }
    
      addons_config {
        ray_operator_config {
          enabled = true
          ray_cluster_logging_config {
            enabled = true
          }
          ray_cluster_monitoring_config {
            enabled = true
          }
        }
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## Versioning

The Ray Operator is available in the following GKE minor versions with a corresponding KubeRay version:

GKE Minor Version | KubeRay Version  
---|---  
1.35 | [v1.5](https://github.com/ray-project/kuberay/releases/tag/v1.5.1)  
1.34 | [v1.4](https://github.com/ray-project/kuberay/releases/tag/v1.4.2)  
1.33 | [v1.3](https://github.com/ray-project/kuberay/releases/tag/v1.3.2)  
1.32 | [v1.2](https://github.com/ray-project/kuberay/releases/tag/v1.2.1)  
1.31 | [v1.2](https://github.com/ray-project/kuberay/releases/tag/v1.2.1)  
1.30 | [v1.1](https://github.com/ray-project/kuberay/releases/tag/v1.1.1)  
1.29 | [v1.1](https://github.com/ray-project/kuberay/releases/tag/v1.1.1)  
  
## Verify the Ray operator is enabled

You can verify that the Ray operator is enabled on an Autopilot or Standard GKE cluster using the gcloud CLI or the Google Cloud console.

###  Console 

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster that you want to verify.

  3. In the **Features** section, confirm that the **Ray Operator** checkbox is selected.




###  gcloud 

Describe your cluster:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of the cluster.

The output is similar to the following
    
    
    # Several lines omitted
    addonsConfig:
      rayOperatorConfig:
        enabled: true
    

This output indicates that the Ray operator is enabled for the cluster.

## What's next

  * Learn about [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html).
  * Learn how to [collect and view logs and metrics for Ray clusters](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics).
  * Explore the [KubeRay documentation](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
