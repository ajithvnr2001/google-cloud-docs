---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke/
title: Configure GKE for ML Diagnostics \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:20.218209+00:00
---

# Configure GKE for ML Diagnostics  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure GKE for ML Diagnostics

If you are using Google Kubernetes Engine (GKE) for your ML workload, you can use the ML Diagnostics platform in two ways:

  1. **Automatic workload monitoring and system metrics collection** : For automatic workload monitoring and system metrics collection, you do not need to instrument your code or perform any extra configuration. Workload monitoring and system metrics collection is enabled by default, and you are not required to perform the steps in this guide. Workload monitoring supports the `jobset` and `job` GKE job types, and is compatible with GKE versions 1.36.0-gke.4681000 and later.
  2. **ML Diagnostics SDK and on-demand profiling** : If you want to use the ML Diagnostics SDK and do on-demand profiling, use this guide to configure your GKE cluster and install the required GKE artifacts.



The configuration of your workload depends on whether you use [on-demand profiling](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/cli) or [programmatic profiling](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/sdk).

  * **On-demand profiling** : Requires you to install `connection-operator`.
  * **Programmatic profiling** : Requires you to install `injection-webhook`, label the workload and use the [ML Diagnostics SDK](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/sdk).



If you are using a version of GKE that is later than `1.35.0-gke.3065000`, you can set up GKE cluster for ML Diagnostics with a single gcloud CLI command, through the Google Cloud console, or by using Terraform. For more information, see Set up with gcloud CLI, Google Cloud console, or Terraform.

For GKE versions prior to `1.35.0-gke.3065000`, you need to manually configure the GKE cluster to install the `cert-manager`, `injection-webhook`, and `connection-operator` artifacts. For more information, see Manual installation.

## Set up with gcloud CLI, Google Cloud console, or Terraform

For GKE versions later than `1.35.0-gke.3065000`, use one of the following methods to deploy the required ML Diagnostics components (both connection-operator and injection-webhook) into your GKE cluster.

###  gcloud 

For new GKE clusters:
    
    
    gcloud beta container clusters create CLUSTER_NAME --enable-managed-mldiagnostics
    

For existing GKE clusters:
    
    
    gcloud beta container clusters update CLUSTER_NAME --enable-managed-mldiagnostics
    

To disable ML Diagnostics, use the following:
    
    
    gcloud beta container clusters update CLUSTER_NAME --no-enable-managed-mldiagnostics
    

For more information on gcloud CLI commands to set up a GKE cluster for ML Diagnostics, refer to the `enable-managed-mldiagnostics` flag in the following API reference pages:

  * [`container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/update)
  * [`container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create)



###  Console 

  * For new GKE clusters, go to **Feature Manager > Managed Machine Learning Diagnostics**.

[Go to GKE Managed Machine Learning Diagnostics](https://console.cloud.google.com/kubernetes/features)

  * For existing GKE clusters, go to **Clusters** , select the name of your cluster, go to **Edit** , and edit **Managed Machine Learning Diagnostics** under **Features**.




###  Terraform 

If you use Terraform to provision your GKE infrastructure, you can use the `terraform-provider-google-beta` provider (version `v7.28.0` or later), or the `terraform-google-modules/kubernetes-engine/google` module (version `v45.0.0` or later).

### Using the Google Cloud Terraform provider

To enable Managed ML Diagnostics on a new cluster using the `google_container_cluster` resource, add the `managed_machine_learning_diagnostics_config` block with `enabled = true` using the `google-beta` provider (version `v7.28.0` or later):
    
    
    terraform {
      required_providers {
        google-beta = {
          source  = "hashicorp/google-beta"
          version = ">= 7.28.0"
        }
      }
    }
    
    resource "google_container_cluster" "primary" {
      provider = google-beta
      name     = "CLUSTER_NAME"
      location = "LOCATION"
    
      # ... other cluster configuration ...
    
      managed_machine_learning_diagnostics_config {
        enabled = true
      }
    }
    

To disable Managed ML Diagnostics on a cluster using the Terraform resource, set `enabled = false` in the `managed_machine_learning_diagnostics_config` block:
    
    
    resource "google_container_cluster" "primary" {
      provider = google-beta
      name     = "CLUSTER_NAME"
      location = "LOCATION"
    
      # ... other cluster configuration ...
    
      managed_machine_learning_diagnostics_config {
        enabled = false
      }
    }
    

### Using the GKE Terraform module

To enable Managed ML Diagnostics on a cluster using the [`terraform-google-modules/kubernetes-engine/google`](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine) module (such as the `beta-public-cluster` submodule), set `enable_managed_machine_learning_diagnostics = true`:
    
    
    module "gke" {
      source  = "terraform-google-modules/kubernetes-engine/google//modules/beta-public-cluster"
      version = ">= 45.0"
    
      project_id = "PROJECT_ID"
      name       = "CLUSTER_NAME"
      region     = "LOCATION"
    
      # ... other cluster configuration ...
    
      enable_managed_machine_learning_diagnostics = true
    }
    

To disable Managed ML Diagnostics on a cluster using the Terraform module, set `enable_managed_machine_learning_diagnostics = false`:
    
    
    module "gke" {
      source  = "terraform-google-modules/kubernetes-engine/google//modules/beta-public-cluster"
      version = ">= 45.0"
    
      # ... other cluster configuration ...
    
      enable_managed_machine_learning_diagnostics = false
    }
    

After updating your configuration, apply the changes:
    
    
    terraform apply
    

Replace the following:

  * `PROJECT_ID`: the name of the project.
  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the region or zone.



To learn more about using Terraform with GKE, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## Manual installation

For GKE versions prior to `1.35.0-gke.3065000`, you need to manually configure the GKE cluster to install the following:

  * `cert-manager`: A prerequisite for the `injection-webhook`.
  * `injection-webhook`: Provides the SDK with the required metadata. It supports common ML Kubernetes workloads, like `JobSet`,`RayJob`, and `LeaderWorkerSet`.
  * `connection-operator`: For on-demand profiling on GKE. Deploying `connection-operator` along with `injection-webhook` into the GKE cluster will initialize profiling requests to target pods with profiling servers running when you trigger on-demand capture.



For more information on setting up for Google Kubernetes Engine, see [Configure Google Kubernetes Engine cluster](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics#configure-gke-cluster).

### Cert-manager

`cert-manager` acts as the certificate controller for your cluster, ensuring that your applications are secure and that your certificates never unintentionally expire.

Use Helm to install the following:
    
    
    helm repo add jetstack https://charts.jetstack.io
    helm repo update
    
    helm install \
      cert-manager jetstack/cert-manager \
      --namespace cert-manager \
      --create-namespace \
      --version v1.13.0 \
      --set installCRDs=true \
      --set global.leaderElection.namespace=cert-manager \
      --timeout 10m
    

### Injection-webhook

`injection-webhook` passes metadata into the SDK. Use `helm upgrade --install` to install for the first time or upgrade an existing installation.
    
    
    helm upgrade --install mldiagnostics-injection-webhook \
      --namespace=gke-mldiagnostics \
      --create-namespace \
      --version 0.25.0 \
      oci://us-docker.pkg.dev/ai-on-gke/mldiagnostics-webhook-and-operator-helm/mldiagnostics-injection-webhook
    

### Connection-operator

`connection-operator` enables on-demand profiling on GKE. Use the following table to find the correct `mldiagnostics-connection-operator` version:

JAX Version | Helm Chart Version  
---|---  
0.8.x | 0.24.0  
0.9.x+ | 0.24.0+  
  
Use Helm to install the required version.

For JAX 0.8.x:
    
    
    helm upgrade --install mldiagnostics-connection-operator \
      --namespace=gke-mldiagnostics \
      --create-namespace \
      --version 0.24.0 \
      oci://us-docker.pkg.dev/ai-on-gke/mldiagnostics-webhook-and-operator-helm/mldiagnostics-connection-operator \
      --set 'mldiagnosticsConnectionOperator.controller.args={--metrics-bind-address=:8443,--health-probe-bind-address=:8081,--sidecar-timeout=65m,--disable-hostname-override}'
    

For JAX 0.9.x+:
    
    
    helm upgrade --install mldiagnostics-connection-operator \
      --namespace=gke-mldiagnostics \
      --create-namespace \
      --version 0.24.0 \
      oci://us-docker.pkg.dev/ai-on-gke/mldiagnostics-webhook-and-operator-helm/mldiagnostics-connection-operator
    

## Label workload

For **programmatic profiling** , you need to trigger the `injection-webhook` to inject metadata into pods. Label either the workload or its namespace with `managed-mldiagnostics-gke=true` before deploying the workload:

  * **Label a workload**. Label a `Jobset`, `LWS`, or `RayJob` workload, which will enable the webhook for that specific workload. The following is an example for a `JobSet` workload:
        
        apiVersion: jobset.x-k8s.io/v1alpha2
        kind: JobSet
        metadata:
          name: single-host-tpu-v3-jobset2
          namespace: default
          labels:
            managed-mldiagnostics-gke: "true"
        

  * **Label a namespace.** This will enable the webhook for all `Jobset`, `LWS`, and `RayJob` workloads within that namespace.
        
        kubectl create namespace ai-workloads
        kubectl label namespace ai-workloads managed-mldiagnostics-gke=true
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
