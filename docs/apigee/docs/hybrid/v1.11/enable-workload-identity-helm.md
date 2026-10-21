---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity-helm/
title: Enabling Workload Identity with Helm charts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:46:36.941210+00:00
---

# Enabling Workload Identity with Helm charts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity-helm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enabling Workload Identity with Helm charts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-helm.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-helm.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/enable-workload-identity-helm.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enable-workload-identity-helm.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-workload-identity-helm.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enable-workload-identity-helm.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity-helm.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enable-workload-identity-helm.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enable-workload-identity-helm.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/enable-workload-identity-helm.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/enable-workload-identity-helm.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/enable-workload-identity-helm.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/enable-workload-identity-helm.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/enable-workload-identity-helm.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/enable-workload-identity-helm.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/enable-workload-identity-helm.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/enable-workload-identity-helm.html)



This topic explains how to enable Workload Identity for Apigee hybrid using Helm Charts. 

If you are using `apigeectl` to install and manage Apigee hybrid, see [Enabling Workload Identity with `apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity). 

**Note:** Apigee hybrid v.1.11 only supports Workload Identity federation on GKE.

## Overview

Workload Identity is a way for applications running within GKE (Google Kubernetes Engine) to access Google Cloud services. For overviews of Workload Identity, see:

  * [ Introducing Workload Identity: Better authentication for your GKE applications](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications)
  * [Using Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)



A Google Cloud IAM service account is an identity that an application can use to make requests to Google APIs. These service accounts are referred to as GSA (Google Service Accounts) in the document. For more information about GSAs, see [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

Separately, Kubernetes also has the concept of service accounts. A service account provides an identity for processes that run in a Pod. Kubernetes service accounts are Kubernetes resources, while Google service accounts are specific to Google Cloud. For information on Kubernetes service accounts, see [ Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the Kubernetes documentation.

Apigee creates and uses a Kubernetes service account for each type of component when you first install the Helm charts for those components. Enabling Workload Identity allows the hybrid components to interact with the Kubernetes service accounts.

### Environment variables used in these procedures

These procedures use the following environment variables. Either set these in your command shell or replace them in the code samples with the actual values: 

  * **`CLUSTER_LOCATION`** : The region or zone of your Kubernetes cluster, for example: `us-west1`.
  * **`CLUSTER_NAME`** : The name of your cluster.
  * **`ENV_NAME`** : Then name of the Apigee environment.
  * **`ORG_NAME`** : The name of your Apigee organization.
  * **`PROJECT_ID`** : The ID of your Google Cloud project.
  * **`NAMESPACE`** : Your Apigee namespace (usually "apigee").



Verify the environment variables:
    
    
    echo $PROJECT_ID
    echo $ORG_NAME
    echo $ENV_NAME
    echo $NAMESPACE
    echo $CLUSTER_LOCATION
    echo $CLUSTER_NAME
    CLUSTER_NAME

Initialize any of the variables you need:
    
    
    export PROJECT_ID=my-project-id
    export ORG_NAME=$PROJECT_ID
    export ENV_NAME=my-environment-name
    export NAMESPACE=apigee
    export CLUSTER_LOCATION=my-cluster-location
    export CLUSTER_NAME=hybrid-base-directory/apigeectl
    

## Workload Identity and service account key files

When running Apigee hybrid on GKE, the standard practice is to create and download private keys (`.json` files) for each of the service accounts. When using Workload Identity, you do not need to download service account private keys and add them to GKE clusters.

If you have downloaded service account key files as part of your Apigee hybrid installation, you can delete them after enabling Workload Identity. In most installations, they reside in the directory for each component's char.

## Enable Workload Identity for Apigee hybrid

Follow these instructions to configure Workload Identity for your project. 

**Note:** Workload Identity is only available for hybrid installations on GKE.

### Migrated installation and Workload Identity

If you migrated your cluster from `apigeectl` management with the [Apigee hybrid Helm migration tool](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-migration), the overrides syntax for Workload Identity will have changed. You will need to check the following properties in your overrides file: 

  * `namespace` is required. For example: 
        
        instanceID: "hybrid-instance-1"
        namespace: "apigee"
        

  * The [`gcp.workloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#gcp-workloadidentity-enabled) property replaces the [`gcp.workloadIdentityEnabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#gcp-workloadidentityenabled) property. For example: 
        
        gcp:
          workloadIdentity:
            enabled: true

  * For production installations, each component has a `gsa` property. The value for these properties is the email address for the Google IAM service account for the corresponding component. For example: 
        
        watcher
          gsa: apigee-watcher@my-hybrid-project.iam.gserviceaccount.com
        

  * For non-production installations, you can supply a single GSA in the [`gcp.workloadIdentity.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#gcp-workloadidentity-gsa) property. 
        
        gcp
          workloadIdentity
            gsa: apigee-watcher@my-hybrid-project.iam.gserviceaccount.com
        

  * With Helm charts for Apigee hybrid, mix prod and non-prod GSAs for Workload Identity. You can specify a single for the [`gcp.workloadIdentity.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#gcp-workloadidentity-gsa) property _and_ specify individual GSAs for specific components. The values you provide for the individual components will override the value you provide for `gcp.workloadIdentity.gsa` for that component only.



### Prepare to configure Workload Identity

  1. Verify that Workload Identity is enabled in your overrides file. It should be enabled at the overrides file and you should have values for the in the following configuration properties: 
     * For all installations: [`gcp.workloadIdentityEnabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#gcp-workloadidentityenabled) should be `true`. For example: 
           
           gcp:
             workloadIdentity:
               enabled: true

     * For production installations: 
       * [`connectAgent.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#connectagent-gsa)
       * [`envs.gsa.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#envs-gsa-runtime)
       * [`envs.gsa.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#envs-gsa-synchronizer)
       * [`envs.gsa.udca`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#envs-gsa-udca)
       * [`logger.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#logger-gsa)
       * [`mart.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#mart-gsa)
       * [`metrics.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#metrics-gsa)
       * [`udca.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#udca-gsa)
       * [`watcher.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#watcher-gsa)
     * For non-production installations, supply the address of the non-prod GSA (with all needed IAM roles) in the [`gcp.workloadIdentity.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref#gcp-workloadidentity-gsa) property.
  2. Check that the current `gcloud` configuration is set to your Google Cloud project ID with the following command: 
         
         gcloud config get project

If needed, set the current `gcloud` configuration:
    
    gcloud config set project $PROJECT_ID

  3. Verify that Workload Identity is enabled for your GKE Cluster. When you created the cluster in [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-cluster#gke), step 6 was to Enable Workload Identity. You can confirm if Workload Identity is enabled by running the following command: 

### Regional clusters
         
         gcloud container clusters describe $CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten 'workloadIdentityConfig'

### Zonal clusters
         
         gcloud container clusters describe $CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten 'workloadIdentityConfig'

Your output should look like the following: 
         
         ---
         workloadPool: PROJECT_ID.svc.id.goog

If you see `null` instead in your results, run the following command to enable Workload Identity for your cluster: 

### Regional clusters
         
         gcloud container clusters update $CLUSTER_NAME \
           --workload-pool=$PROJECT_ID.svc.id.goog \
           --project $PROJECT_ID \
           --region $CLUSTER_LOCATION

### Zonal clusters
         
         gcloud container clusters update  $CLUSTER_NAME \
           --workload-pool=$PROJECT_ID.svc.id.goog \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID

  4. Enable Workload Identity for each node pool with the following commands. This operation can take up to 30 minutes for each node:

### Regional clusters
         
         gcloud container node-pools update NODE_POOL_NAME \
           -cluster=$CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --workload-metadata=GKE_METADATA

### Zonal clusters
         
         gcloud container node-pools update NODE_POOL_NAME \
           --cluster=$CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --workload-metadata=GKE_METADATA

Where NODE_POOL_NAME is the name of each node pool. In most Apigee hybrid installations, the two default node pools are named `apigee-data` and `apigee-runtime`.

  5. Verify that Workload Identity is enabled on your node pools with the following commands: 

### Regional clusters
         
         gcloud container node-pools describe apigee-data \
           --cluster $CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"
         
         gcloud container node-pools describe apigee-runtime \
           --cluster $CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"

### Zonal clusters
         
         gcloud container node-pools describe apigee-data \
           --cluster $CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"
         
         gcloud container node-pools describe apigee-runtime \
           --cluster $CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"

Your output should look something like:
         
         ---
         diskSizeGb: 100
         diskType: pd-standard
         ...
         **workloadMetadataConfig:
         mode: GKE_METADATA**
           




### Configure Workload Identity

Use the following procedure to enable Workload Identity for the following Hybrid components:

  * `apigee-telemetry`
  * `apigee-org`
  * `apigee-env`



When you run the `helm upgrade` with the `--dry-run` flag for the `apigee-datastore`, `apigee-env`, `apigee-org`, and `apigee-telemetry` charts, the output will include the commands you will need to configure Workload Identity with the correct GSA and KSA names. 

For example:
    
    
    helm upgrade datastore apigee-datastore/ \
      --namespace $NAMESPACE \
      -f overrides.yaml \
      --dry-run
    
    
    NAME: datastore
    ...
    For C* backup GKE Workload Identity, please make sure to add the below membership to the IAM policy binding using the respective kubernetes SA (KSA).
    gcloud iam service-accounts add-iam-policy-binding  \
          --role roles/iam.workloadIdentityUser \
          --member "serviceAccount:_my-project_.svc.id.goog[apigee/apigee-cassandra-backup-sa]" \
          --project :_my-project_
    

  1. Get the command to set up Workload Identity for `apigee-datastore` and run the command under `NOTES:` in the output. 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace $NAMESPACE \
           -f overrides.yaml \
           --dry-run

  2. Get the commands to set up Workload Identity for `apigee-telemetry` and run the command under `NOTES:` in the output. 
         
         helm upgrade telemetry apigee-telemetry/ \
           --namespace $NAMESPACE \
           -f overrides.yaml \
           --dry-run

  3. Get the commands to set up Workload Identity for `apigee-org` and run the command under `NOTES:` in the output. 
         
         helm upgrade $ORG_NAME apigee-org/ \
           --namespace $NAMESPACE \
           -f overrides.yaml \
           --dry-run

  4. Get the commands to set up Workload Identity for `apigee-env` and run the command under `NOTES:` in the output. 
         
         helm upgrade $ENV_NAME apigee-env/ \
           --namespace $NAMESPACE \
           --set env=ENV_NAME \
           -f overrides.yaml \
           --dry-run

Repeat this step for each environment in your installation.




### Verify Workload Identity

  1. Validate if the steps worked: 
         
         gcloud config set project $PROJECT_ID
         
         
         kubectl run --rm -it --image google/cloud-sdk:slim \
           --namespace $NAMESPACE workload-identity-test\
           -- gcloud auth list

If you don't see a command prompt, try pressing `Enter`.

If the steps were correctly run, you should see a response like the following:
         
         Credentialed Accounts
         ACTIVE  ACCOUNT
         *       GSA@PROJECT_ID.iam.gserviceaccount.com

  2. If upgrading from a previous install, clean up secrets that contained service account private keys: 
         
         kubectl delete secrets -n $NAMESPACE $(k get secrets -n $NAMESPACE | grep svc-account | awk '{print $1}')
         

  3. Check logs: 
         
         kubectl logs -n $NAMESPACE -l app=apigee=synchronizer,env=$ENV_NAME,org=$ORG_NAME apigee-synchronizer
         

  4. (Optional) You can see the status of your Kubernetes service accounts in the **Kubernetes: Workloads Overview** page in the Google Cloud console. 

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

**Note:** You may see an error status for the `apigee-cassandra-backup` and `apigee-cassandra-restore` service accounts. This is because you are not currently running backup or restore, and these processes have not been fully configured yet. For more information on Cassandra backup and restore, see [feedbackCassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-backup-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
