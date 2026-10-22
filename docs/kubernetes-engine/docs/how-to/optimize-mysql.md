---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-mysql/
title: Optimize MySQL workload performance on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:32:02.553348+00:00
---

# Optimize MySQL workload performance on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Optimize MySQL workload performance on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to improve the performance of your MySQL workloads on Google Kubernetes Engine (GKE) by generating optimized application-level and node-level configurations. For more details, see [Optimize for workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-optimization).

The optimizations for MySQL were determined for a MySQL 8 instance being used as a single-node online transaction processing database ("Read/Write OLTP") with SSL, with performance measured using Sysbench 1.1.0. Consider how the MySQL workload is used on your cluster compared to this use case. If your use case differs, then the recommended optimizations might need to be adjusted for your context.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the GKE Recommender API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,gkerecommender.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

Use GKE version 1.31.1-gke.12000 or later.

## Optimize for MySQL workloads

We recommend using a dedicated node pool for your MySQL workload. By default, a new node pool is created when you complete the following steps.

To optimize the performance of a MySQL workload, do the following:

  1. Create the manifests with optimizations for the MySQL workload:

     1. Generate manifests with recommended optimizations by running the following command:
            
            gcloud container workload profiles manifests create \
               --workload=mysql-8-oltp
               --cluster-version=CLUSTER_VERSION
               --options=machineType=MACHINE_TYPE \
               --output-path=/tmp/manifests.yaml
            

Replace the following:

        * `CLUSTER_VERSION`: the GKE version. Recommendation is GKE version 1.31.1-gke.12000 or later.
        * `MACHINE_TYPE`: the wanted machine type.

The `--output-path=/tmp/manifests.yaml` flag is optional. If it is not specified, then the manifests are printed to the terminal, but are not saved to a file.

This command generates a single YAML file containing two Kubernetes resources:

        * A ConfigMap specifying a MySQL config named `default-auth.cnf`.
        * A [ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) object. This specifies machines for MySQL to run on, which is optional. For details about how machine types are specified, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)
     2. Review the recommendations and modify the manifests so that they include your preferred optimizations. To assess the recommendations, you can do the following:

        * Review the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/server-configuration.html) to assess the recommended configuration for your context.
        * Consider how the MySQL workload is used on your cluster compared to the following use case. If your use case differs, then the recommended optimizations might need to be adjusted for your context.

The optimizations for MySQL were determined for a MySQL 8 instance being used as a single-node online transaction processing database ("Read/Write OLTP") with SSL, with performance measured using Sysbench 1.1.0.

     3. Edit the manifest file if you want to modify the configuration or add to the configuration.

     4. Apply the manifests to the cluster by using the following command:
            
            kubectl create -f /tmp/manifests.yaml
            

  2. Deploy a Pod referencing the optimizations. For example:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: mysql
         spec:
           containers:
             - name: mysql
               image: mysql:8
               **volumeMounts :
                 - name: gke-optimized-workload-config
                   subPath: default-auth.cnf
                   mountPath: /etc/mysql/conf.d/gke-optimized.cnf
                   readOnly: true
           volumes:
             - name: gke-optimized-workload-config
               configMap:
                 name: mysql-config
           nodeSelector:
             cloud.google.com/compute-class: optimized-gke-mysql-8-oltp-abc123**
         

Modify the ComputeClass name to match the generated one. Then, apply your Pod manifest to the cluster:
         
         kubectl apply -f pod.yaml
         

  3. Confirm MySQL is using the optimized configuration. To do so, you can run the following command to ensure MySQL is using the optimized configuration:
         
         kubectl exec mysql -- mysql -e "SELECT DISTINCT VARIABLE_PATH FROM performance_schema.variables_info WHERE VARIABLE_PATH != '';"
         

You should see an output similar to the following:
         
         VARIABLE_PATH
         /etc/mysql/conf.d/gke-optimized.cnf
         /etc/my.cnf
         

You can also use the `mysql` command to query the individual directives that are set in the optimized configuration, such as `max_connections`.




When you deploy the workload, the cluster creates a new node pool that adheres to the optimized configuration, and assigns your Pods to those node pools.

Pods that already exist are not modified. Only Pods that reference the optimized configurations are optimized. If you have previously deployed MySQL workloads in your cluster, then you need to redeploy these workloads to run them with the optimized configurations.

## What's next

  * Learn more about [workload optimization on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-optimization).
  * Learn more about how to [Deploy a stateful MySQL cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/mysql).
  * Learn more [about GKE ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes).
  * To optimize for Redis workloads, see [Optimize Redis workload performance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-redis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
