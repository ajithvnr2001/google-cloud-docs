---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-redis/
title: Optimize Redis workload performance on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:15.187590+00:00
---

# Optimize Redis workload performance on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Optimize Redis workload performance on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to improve the performance of your Redis workloads on Google Kubernetes Engine (GKE) by generating optimized application-level and node-level configurations. For more details, see [Optimize for workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-optimization).

The optimizations for Redis were determined for a Redis 7 instance being used as a single-node look-aside cache with a read-write ratio of 4:1 (4 reads to 1 write), with performance measured using Memtier 2.2.1. Consider how the Redis workload is used on your cluster compared to this use case. If your use case differs, then the recommended optimizations might need to be adjusted for your context.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the GKE Recommender API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkerecommender.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

Use GKE version 1.31.1-gke.12000 or later.

## Optimize for Redis workloads

We recommend using a dedicated node pool for your Redis workload. By default, a new node pool is created when you complete the following steps.

To optimize the performance of a Redis workload, do the following:

  1. Create the manifests with optimizations for the Redis workload by doing the following:

     1. Generate manifests with recommended optimizations by running the following command:
            
            gcloud container workload profiles manifests create \
               --workload=redis-7-caching \
               --cluster-version=CLUSTER_VERSION \
               --options=machineType=MACHINE_TYPE \
               --output-path=/tmp/manifests.yaml
            

Replace the following:

        * `CLUSTER_VERSION`: the GKE version. Recommendation is GKE version 1.31.1-gke.12000 or later.
        * `MACHINE_TYPE`: the wanted machine type.

The `--output-path=/tmp/manifests.yaml` flag is optional. If it is not specified, then the manifests are printed to the terminal, but are not saved to a file.

This command generates a single YAML file containing two Kubernetes resources:

        * A ConfigMap specifying a Redis config named `redis.conf`.
        * A [ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) object. This specifies machines for Redis to run on, which is optional. For details about how machine types are specified, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)

The following is a sample of the generated manifest:
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: redis.conf
    data:
      redis.conf: |
        io-threads 2
        io-threads-do-reads yes
        save ""
    ---
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      generateName: optimized-gke-redis-7-caching-
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorities:
      - machineType: c4-standard-4
      whenUnsatisfiable: DoNotScaleUp
    

     2. Review the recommendations and modify the manifests so that they include your preferred optimizations. To assess the recommendations, you can do the following:

        * Review the [Redis documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/config/) to assess the recommended configuration for your context.
        * Consider how the Redis workload is used on your cluster compared to the following use case. If your use case differs, then the recommended optimizations might need to be adjusted for your context.

The optimizations for Redis were determined for a Redis 7 instance being used as a single-node look-aside cache with a read-write ratio of 4:1 (4 reads to 1 write), with performance measured using Memtier 2.2.1.

     3. Edit the manifest file if you want to modify the configuration or add to the configuration.

     4. Apply the manifests to the cluster by using the following command:
            
            kubectl create -f /tmp/manifests.yaml
            

  2. Deploy a Pod referencing the optimizations. For example:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: redis
         spec:
           containers:
             - name: redis
               image: redis:7
               **args :
                 - /etc/gke/optimization/redis.conf
               volumeMounts:
                 - name: gke-optimized-workload-config
                   subPath: redis.conf
                   mountPath: /etc/gke/optimization/redis.conf
                   readOnly: true
           volumes:
             - name: gke-optimized-workload-config
               configMap:
                 name: redis.conf
           nodeSelector:
             cloud.google.com/compute-class: optimized-gke-redis-7-caching-abc123**
         

Then, apply your Pod manifest to the cluster:
         
         kubectl apply -f pod.yaml
         

  3. Confirm Redis is using the optimized configuration. To do so, you can run the following command to ensure Redis is using the optimized configuration:
         
         kubectl exec redis -- redis-cli INFO server | grep config_file
         

You should see an output similar to the following:
         
         config_file:/etc/gke/optimization/redis.conf
         

You can also use the `redis-cli` command to query the individual directives that are set in the optimized configuration, such as `io-threads`.




When you deploy the workload, the cluster creates a new node pool that adheres to the optimized configuration, and assigns your Pods to those node pools.

Pods that already exist are not modified. Only Pods that reference the optimized configurations are optimized. If you have previously deployed Redis workloads in your cluster, then you need to redeploy these workloads to run them with the optimized configurations.

## What's next

  * Learn more about [workload optimization on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-optimization).
  * Learn more about how to [Deploy a Redis cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/upgrading-stateful-workload)
  * Learn more [about GKE ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes).
  * To optimize for MySQL workloads, see [Optimize MySQL workload performance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-mysql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
