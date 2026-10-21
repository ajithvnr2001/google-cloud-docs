---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/vmware/
title: Installing Knative serving on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:25.425605+00:00
---

# Installing Knative serving on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/vmware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Installing Knative serving on VMware Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to install Knative serving in your GKE clusters outside Google Cloud. Knative serving now uses Cloud Service Mesh and GKE Enterprise fleets. [Learn what's new and changed with Knative serving fleet installations](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install). Warning: Performing the steps on this page will perform a new installation of Knative serving on VMware and irreversibly overwrite your previous non-fleet installation. Do not proceed with the following steps in your [clusters for which you previously enabled Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup).   
  
For previous "free-trial" installations of Knative serving, you must first [upgrade Knative serving on VMware to use GKE Enterprise fleets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/upgrade-vmware). 

Use the steps on this page to configure a new installation or to update an existing [fleet installation](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install) of Knative serving.

## Before you begin

You must ensure that you meet the [installation prerequisites](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/prerequisites).

## Configure your `CloudRun` custom resource

You need to manually create and configure the `CloudRun` custom resource to configure your installation.

To manually create a `CloudRun` custom resource for GKE clusters outside Google Cloud: 

  1. You must create or have an existing service account that has been granted the required [Monitoring Metric Writer role](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) (`monitoring.metricWriter`).

     * To create a new service account and then download the key, see [Using service accounts](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/service-accounts).

     * If you have an existing service account with the necessary permissions, locate the key that you downloaded when you created that service account.

  2. [Ensure Cloud Monitoring is enabled in Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/application-logging-monitoring).

  3. Create the `knative-serving` namespace:
         
         kubectl create namespace knative-serving
         

  4. Create a secret in the `knative-serving` namespace that holds the service account with `monitoring.metricWriter` permissions:
         
         kubectl create secret -n knative-serving generic SECRET_NAME --from-file=PATH_TO_KEY_FILE/SECRET_KEY
         

Replace:

     * SECRET_NAME with the name that you choose for the secret.
     * SECRET_KEY with the name of the file that includes your credentials. Example: `key.json`
     * PATH_TO_KEY_FILE with the path to the directory of the SECRET_KEY.

See the [`kubectl create secret`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-secret-generic-em-) reference to learn more, including optional flags.

  5. Create a YAML file with the following attributes, for example `cloudrunanthos.yaml`:
         
         apiVersion: operator.run.cloud.google.com/v1alpha1
         kind: CloudRun
         metadata:
           name: cloud-run
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
         
         gcloud container fleet cloudrun apply --kubeconfig=KUBECONFIG --context=CONTEXT --config=CONFIG_FILE
         

Replace the following:

     * KUBECONFIG with the absolute path to your kubectl config file.
     * CONTEXT with the name of the context in your kubectl config file to use for connecting. 
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
