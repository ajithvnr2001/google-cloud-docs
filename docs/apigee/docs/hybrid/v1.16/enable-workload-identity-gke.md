---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke/
title: Enabling Workload Identity Federation for GKE \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:56.996444+00:00
---

# Enabling Workload Identity Federation for GKE  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enabling Workload Identity Federation for GKE Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-gke.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/enable-workload-identity-gke.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enable-workload-identity-gke.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-workload-identity-gke.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enable-workload-identity-gke.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity-gke.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enable-workload-identity-gke.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enable-workload-identity-gke.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/enable-workload-identity-gke.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/enable-workload-identity-gke.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/enable-workload-identity-gke.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/enable-workload-identity-gke.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/enable-workload-identity-gke.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/enable-workload-identity-gke.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/enable-workload-identity-gke.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/enable-workload-identity-gke.html)



This topic explains how to enable Workload Identity Federation for GKE for Apigee hybrid. 

If you are using Apigee hybrid **AKS** or **EKS** follow the instructions in [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation). 

## Overview

Workload Identity Federation for GKE is a way for applications running within GKE (Google Kubernetes Engine) to access Google Cloud services. For overviews of Workload Identity Federation for GKE, see:

  * [About Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)
  * [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)



A Google Cloud IAM service account is an identity that an application can use to make requests to Google APIs. These service accounts are referred to as GSA (Google Service Accounts) in the document. For more information about GSAs, see [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

Separately, Kubernetes also has the concept of service accounts. A service account provides an identity for processes that run in a Pod. Kubernetes service accounts are Kubernetes resources, while Google service accounts are specific to Google Cloud. For information on Kubernetes service accounts, see [ Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the Kubernetes documentation.

Apigee creates and uses a Kubernetes service account for each type of component when you first install the Helm charts for those components. Enabling Workload Identity Federation for GKE allows the hybrid components to interact with the Kubernetes service accounts.

**Note:** Although granting Identity and Access Management (IAM) roles directly to a Kubernetes ServiceAccount principal (`principal://`) is the recommended best practice for [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), Apigee hybrid requires IAM service account impersonation because the hybrid Helm charts (`*.gsa` properties in `overrides.yaml`) and control plane synchronization APIs require IAM service account email addresses.

### Environment variables used in these procedures

These procedures use the following environment variables. Either set these in your command shell or replace them in the code samples with the actual values: 

  * **`PROJECT_ID`** : The ID of your Google Cloud project.
  * **`ORG_NAME`** : The name of your Apigee organization.
  * **`ENV_NAME`** : Then name of the Apigee environment.
  * **`NAMESPACE`** : Your Apigee namespace (usually `apigee`).
  * **`CLUSTER_LOCATION`** : The region or zone of your Kubernetes cluster, for example: `us-west1`.
  * **`CLUSTER_NAME`** : The name of your cluster.



Verify the environment variables:
    
    
    echo $PROJECT_ID
    echo $ORG_NAME
    echo $ENV_NAME
    echo $NAMESPACE
    echo $CLUSTER_LOCATION
    echo $CLUSTER_NAME
    

Initialize any of the variables you need:
    
    
    export PROJECT_ID=MY_PROJECT_ID
    export ORG_NAME=MY_ORG_NAME
    export ENV_NAME=MY_ENV_NAME
    export NAMESPACE=APIGEE_NAMESPACE
    export CLUSTER_LOCATION=MY_CLUSTER_LOCATION
    export CLUSTER_NAME=MY_CLUSTER_NAME
    

## Workload Identity Federation for GKE and service account key files

When running Apigee hybrid on GKE, the standard practice is to create and download private keys (`.json` files) for each of the service accounts. When using Workload Identity Federation for GKE, you do not need to download service account private keys and add them to GKE clusters.

If you have downloaded service account key files as part of your Apigee hybrid installation, you can delete them after enabling Workload Identity Federation for GKE. In most installations, they reside in the directory for each component's chart.

## Enable Workload Identity Federation for GKE for Apigee hybrid

Follow these instructions to configure your project to use Workload Identity Federation for GKE. 

**Note:** Workload Identity Federation for GKE is only available for hybrid installations on GKE.

### Prepare to configure Workload Identity Federation for GKE

  1. Verify that Workload Identity Federation for GKE is enabled in your overrides file. It should be enabled at the overrides file and you should have values for the in the following configuration properties: 
     * For all installations: [`gcp.workloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-workloadidentityenabled) should be `true`. For example: 
           
           gcp:
             workloadIdentity:
               enabled: true

     * For production installations: 
       * [`connectAgent.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-gsa)
       * [`envs.gsa.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-gsa-runtime)
       * [`envs.gsa.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-gsa-synchronizer)
       * [`guardrails.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-gsa)
       * [`logger.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-gsa)
       * [`mart.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-gsa)
       * [`metrics.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-gsa)
       * [`mintTaskscheduler.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-gsa)  
(If using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) on [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
       * [`watcher.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-gsa)
     * For non-production installations, supply the address of the non-prod GSA (with all needed IAM roles) in the [`gcp.workloadIdentity.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-workloadidentity-gsa) property.
  2. Check that the current `gcloud` configuration is set to your Google Cloud project ID with the following command: 
         
         gcloud config get project

If needed, set the current `gcloud` configuration:
    
    gcloud config set project $PROJECT_ID

  3. Verify that Workload Identity Federation for GKE is enabled for your GKE Cluster. When you created the cluster in [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster#gke), step 6 was to Enable Workload Identity Federation for GKE. Confirm Workload Identity Federation for GKE is enabled with the following command: 

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

If you see `null` instead in your results, run the following command to enable Workload Identity Federation for GKE for your cluster: 

### Regional clusters
         
         gcloud container clusters update $CLUSTER_NAME \
           --workload-pool=$PROJECT_ID.svc.id.goog \
           --project $PROJECT_ID \
           --region $CLUSTER_LOCATION

### Zonal clusters
         
         gcloud container clusters update $CLUSTER_NAME \
           --workload-pool=$PROJECT_ID.svc.id.goog \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID

  4. Enable Workload Identity Federation for GKE for each node pool with the following commands. This operation can take up to 30 minutes for each node:

### Regional clusters
         
         gcloud container node-pools update NODE_POOL_NAME \
           --cluster=$CLUSTER_NAME \
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

  5. Verify that Workload Identity Federation for GKE is enabled on your node pools with the following commands: 

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
           




### Configure your installation to use Workload Identity Federation for GKE

Use the following procedure to enable Workload Identity Federation for GKE for the following Hybrid components:

  * `apigee-datastore`
  * `apigee-telemetry`
  * `apigee-org`
  * `apigee-env`



When you run the `helm upgrade` with the `--dry-run` or `--dry-run=server` flags for the `apigee-datastore`, `apigee-env`, `apigee-org`, and `apigee-telemetry` charts, the output will include the commands you will need to configure Workload Identity Federation for GKE with the correct GSA and KSA names. 

For example:
    
    
    helm upgrade datastore apigee-datastore/ \
      --namespace $NAMESPACE \
      -f OVERRIDES_FILE \
      --dry-run=server

Will output something like:
    
    
    NAME: datastore
    ...
    For Cassandra backup, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
    gcloud iam service-accounts add-iam-policy-binding **apigee-cassandra** @PROJECT_ID.iam.gserviceaccount.com \
          --role roles/iam.workloadIdentityUser \
          --member "serviceAccount:PROJECT_ID.svc.id.goog[APIGEE_NAMESPACE/**apigee-cassandra-default**]" \
          --project PROJECT_ID
    
    kubectl annotate serviceaccount **apigee-cassandra-default** \
          iam.gke.io/gcp-service-account=apigee-cassandra@PROJECT_ID.iam.gserviceaccount.com \
          --namespace APIGEE_NAMESPACE
    

Where: 

  * `**apigee-cassandra**` is the name of the Google service account (GSA) for Cassandra. See [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about).
  * `PROJECT_ID` is replaced with your Google Cloud project ID.
  * `APIGEE_NAMESPACE` is replaced with your Apigee namespace, `apigee` by default.
  * `**apigee-cassandra-default**` is the name of the Kubernetes service account for the Cassandra pods created by the `apigee-datastore` chart.


  1. Get the command to set up Workload Identity Federation for GKE for `apigee-datastore` and run the commands under `NOTES:` in the output. 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace $NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server

  2. Get the commands to set up Workload Identity Federation for GKE for `apigee-telemetry` and run the commands under `NOTES:` in the output. 
         
         helm upgrade telemetry apigee-telemetry/ \
           --namespace $NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run

  3. Get the commands to set up Workload Identity Federation for GKE for `apigee-org` and run the commands under `NOTES:` in the output. 
         
         helm upgrade $ORG_NAME apigee-org/ \
           --namespace $NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run

  4. Get the commands to set up Workload Identity Federation for GKE for `apigee-env` and run the commands under `NOTES:` in the output. 
         
         helm upgrade $ENV_NAME apigee-env/ \
           --namespace $NAMESPACE \
           --set env=$ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run

Repeat this step for each environment in your installation.




### Verify Workload Identity Federation for GKE

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

**Note:** You may see an error status for the `apigee-cassandra-backup` and `apigee-cassandra-restore` service accounts. This is because you are not currently running backup or restore, and these processes have not been fully configured yet. For more information on Cassandra backup and restore, see [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview).



### Set up guardrails with Workload Identity Federation for GKE

**Note:** Guardrails are intended for fresh installs of Apigee hybrid.

You can use guardrails during initial installation of the `apigee-operator` chart to check if the correct APIs are enabled for your project. To configure your installation with Workload Identity Federation for GKE to use guardrails during installation, you need to manually set up the binding before running the `helm upgrade` command.

  1. Get the email address of the guardrails GSA with the following command: 
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

GSA email addresses typically have the format of:
         
         GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
         
         DISPLAY NAME       EMAIL                                                DISABLED
         apigee-guardrails  apigee-guardrails@myproject.iam.gserviceaccount.com  False

Use this email address for the `GSA_EMAIL` variable in the next two steps.

  2. Make sure the `guardrails` stanza is in your overrides.yaml file: 
         
         guardrails:
           gsa: GSA_EMAIL
         

  3. The KSA for guardrails is named `apigee-operator-guardrails-sa`. Create the binding for the guardrails GSA with the following command: 
         
         gcloud iam service-accounts add-iam-policy-binding GSA_EMAIL \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:PROJECT_ID.svc.id.goog[APIGEE_NAMESPACE/apigee-operator-guardrails-sa]" \
           --project PROJECT_ID




When you run the `helm upgrade` command for the `apigee-operator` chart, the chart will create a guardrails pod to test if the required APIs are enabled for your project. If any required APIs are not enabled, the pod will fail and the installation will stop. You can inspect the guardrails pod logs to see which APIs are required but not enabled. For details, see [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/guardrails). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
