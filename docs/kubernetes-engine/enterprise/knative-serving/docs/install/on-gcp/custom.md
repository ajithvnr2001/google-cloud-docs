---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/custom/
title: Customizing your Google Cloud installation \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:07.314849+00:00
---

# Customizing your Google Cloud installation  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Customizing your Google Cloud installation Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to install Knative serving in your GKE clusters on Google Cloud. Knative serving now uses Cloud Service Mesh and GKE Enterprise fleets. [Learn what's new and changed with Knative serving fleet installations](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install). 

Use this page to customize a new installation or to configure an existing [fleet installation](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install) of Knative serving. For example, you can configure for private clusters or set Cloud Monitoring credentials.

The [default installation steps](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install) automatically deploy the following `CloudRun` custom resource which enables metrics on GKE Enterprise on Google Cloud clusters:
    
    
      apiVersion: operator.run.cloud.google.com/v1alpha1
      kind: CloudRun
      metadata:
        name: cloud-run
    

To learn about custom resources in general, see [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

## Before you begin

  * You must ensure that you meet the [installation prerequisites](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/prerequisites).

  * If Knative serving is installed in your cluster, you must ensure that the "_GKE add-on_ " does not exist before you perform these fleet component installation steps. If you have the "_add-on_ " installed, you must instead [follow the steps for upgrading to GKE Enterprise fleets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/upgrade). 

#### Check if the "_GKE add-on_ " is installed.

To check if your installation of Knative serving is the "_GKE add-on_ ", run the following command: 
        
        gcloud container clusters describe \
        CLUSTER_NAME \
        --region CLUSTER_LOCATION \
        --project PROJECT_ID --format='get(addonsConfig.cloudRunConfig)'

Replace: 

    * CLUSTER_NAME with the name of your cluster.
    * CLUSTER_LOCATION with the [location](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone) where your cluster is located.
    * PROJECT_ID with the ID of your Google Cloud project.

Results: 

    * **"_GKE add-on_ " not installed**: 
      * Nothing is returned to your terminal if the add-on was never installed.
      * `disabled=true` is returned if the add-on was previously uninstalled.
    * **"_GKE add-on_ " is installed**: If the add-on is installed in your cluster, the configuration details for the add-on are returned. Example: `loadBalancerType=LOAD_BALANCER_TYPE_EXTERNAL`

Example:
     The following example demonstrates that Knative serving was installed in the `my-addon-cluster` cluster through the "_GKE add-on_ ", which is configured to handle external traffic: 
    
    gcloud container clusters describe **my-addon-cluster** \
    --region **us-central1-c** --project **my-gcp-project** \
    --format='get(addonsConfig.cloudRunConfig)'

Response: 
    
    loadBalancerType=LOAD_BALANCER_TYPE_EXTERNAL




## Configure your `CloudRun` custom resource

You need to manually create and configure the `CloudRun` custom resource to configure your installation.

To manually create a `CloudRun` custom resource for GKE clusters on Google Cloud: 

  1. Create a YAML file and include the default configuration, for example `cloudrunanthos.yaml`:
         
         apiVersion: operator.run.cloud.google.com/v1alpha1
         kind: CloudRun
         metadata:
           name: cloud-run
         

  2. In `cloudrunanthos.yaml`, you customize the installation by configuring one or more of the following attributes under a `spec` section:

     * **Private clusters** : You must add the `clusterConfig` and `isPrivate` set of attributes to install Knative serving on a [private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) on Google Cloud.

The `clusterConfig` and `isPrivate` attributes:
           
           spec:
             clusterConfig:
               isPrivate: true
           

Note that this setting disables [Managed TLS](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls) because private clusters are not able to communicate with the certificate authority by default.

     * **Metrics** : Add the `metricscollector` set of attributes to configure Cloud Monitoring. By default, metrics are enable for GKE Enterprise on Google Cloud clusters.
           
           spec:
             metricscollector:
               stackdriver:
                 projectid: PROJECT_ID
                 gcpzone: CLUSTER_LOCATION
                 clustername: CLUSTER_NAME
                 secretname: SECRET_NAME
                 secretkey: SECRET_KEY
           

Replace the following:

       * PROJECT_ID with the ID of your Google Cloud project.
       * CLUSTER_LOCATION with the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which your cluster is located.
       * CLUSTER_NAME with the ID of your cluster or the fully qualified identifier for the cluster.
       * SECRET_NAME with the name of the Secret for the service account of the `knative-serving` namespace.
       * SECRET_KEY with the key of the Secret for the service account of the `knative-serving` namespace. For example: `key.json`

For details about service accounts, see:

         * [Creating service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)
         * [Creating service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys)

**Example**

In this example `CloudRun` custom resource, the configuration details for Cloud Monitoring are specified to use the `my-gcp-logging-secret` secret and `key.json` key:
    
    
     apiVersion: operator.run.cloud.google.com/v1alpha1
     kind: CloudRun
     metadata:
       name: cloud-run
     spec:
       metricscollector:
         stackdriver:
           projectid: **my-gcp-project-id**
           gcpzone: **us-central1-c**
           clustername: **my-anthos-cluster-name**
           secretname: **my-gcp-logging-secret**
           secretkey: **key.json**
     ```
    

## Enable and install Knative serving

Enable the Knative serving component in your GKE Enterprise fleet and then deploy your `CloudRun` custom resource:

  1. Enable Knative serving in your fleet:
         
         gcloud container fleet cloudrun enable --project=PROJECT_ID
         

Replace PROJECT_ID with the ID of your Google Cloud project.

For details and additional options, see the [gcloud container fleet cloudrun enable](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun/enable) reference.

  2. Optional: Verify that the Knative serving feature component is enabled:

### Console

View if the Knative serving component is **Enabled** in the Google Cloud console:

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features)

### Command line

View if the `appdevexperience` state is `ACTIVE`:
         
         gcloud container fleet features list  --project=PROJECT_ID
         

Replace PROJECT_ID with the ID of your Google Cloud project.

For details and additional options, see the [gcloud container fleet features list](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/features/list) reference.

Result:
         
         NAME               STATE
         appdevexperience   ACTIVE
         

  3. For each GKE Enterprise cluster where you want to install Knative serving, you must deploy your `CloudRun` custom resource:

### gcloud
         
         gcloud container fleet cloudrun apply --gke-cluster=CLUSTER_LOCATION/CLUSTER_NAME --config=CONFIG_FILE
         

Replace the following:

     * CLUSTER_LOCATION with the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which your cluster is located.
     * CLUSTER_NAME with the ID of your cluster or the fully qualified identifier for the cluster. 
     * CONFIG_FILE with the filename relative path to your `cloudRun` custom resource. Example `cloudrunanthos.yaml`. 

For details and additional options, see the [gcloud container fleet cloudrun apply](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun/apply) reference.

### kubectl
    
    kubectl apply --kubeconfig=KUBECONFIG --filename CONFIG_FILE
    

Replace the following:

     * KUBECONFIG with the absolute path to your kubectl config file.
     * CONFIG_FILE with the filename and relative path to your `cloudRun` custom resource. Example `cloudrunanthos.yaml`.

For details and additional options, see the [kubectl apply](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) reference.

  4. Verify that Knative serving has been enabled in your cluster: 
     1. Open the Google Cloud console: 

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. Click on the name of your cluster to open the details pane. 

     3. Run this command to check if you can see the Knative serving version details: `kubectl get all -n knative-serving -o 'go-template={{index .metadata.labels "serving.knative.dev/release"}}'`
     4. Verify that all Knative serving specific deployments are in running status under `knative-serving` and `appdevexperience` namespaces. 



## What's next

[Set up your installation of Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
