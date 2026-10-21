---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-workload-identity/
title: Step 11 (Optional): Configure Workload Identity \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:03:16.846118+00:00
---

# Step 11 (Optional): Configure Workload Identity  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 11 (Optional): Configure Workload Identity Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-workload-identity.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-workload-identity.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-workload-identity.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-workload-identity.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-workload-identity.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-workload-identity.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-workload-identity.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-workload-identity.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-workload-identity.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-workload-identity.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-workload-identity.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-workload-identity.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-workload-identity.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-workload-identity.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-workload-identity.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-workload-identity.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-workload-identity.html)



Apigee hybrid v.1.13 supports Workload Identity on GKE and Workload Identity Federation on AKS and EKS. The procedures in this guide only cover configuring Workload Identity on **GKE**. For **AKS** and **EKS** , follow the procedures in [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-workload-identity-federation)

##  Configure Workload Identity on GKE 

### Google Cloud service accounts and Kubernetes service accounts

A Google Cloud service account is a special kind of account that can be used to make authorized API calls by authenticating as the service account itself. Google Cloud service accounts can be given roles and permissions similar to an individual user. When an application authenticates as a service account, it has access to all resources that the service account has permission to access. If you want to learn more about Google Cloud service accounts, see [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview). 

You created Google Cloud service accounts for your Apigee hybrid installation in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts). Apigee uses these service accounts to authenticate the hybrid components. 

Kubernetes service accounts are similar to Google Cloud service accounts. A Kubernetes service account provides an identity for processes that run in a Pod, and allows it to authenticate to the API server similarly to a user. If you want to learn more about Kubernetes service accounts, see [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/). 

If you have `gcp.workloadIdentity.enabled` set to `true` in your overrides file, when Helm charts for each hybrid component will create the Kubernetes service accounts for the components when you install or upgrade them like you did in [Step 10: Install Apigee hybrid using Helm](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-helm-charts). 

When you configure Workload Identity on GKE, you associate the Google Cloud service accounts with the Kubernetes service accounts in the Kubernetes cluster. That way, the Kubernetes service accounts can impersonate the Google Cloud service accounts and use their assigned roles and permissions to authenticate with the hybrid components. 

Follow these instructions to configure Workload Identity for your project. 

**Note:** Workload Identity is only available for hybrid installations on GKE.

### Prepare to configure Workload Identity

  1. Verify that Workload Identity is enabled in your overrides file. It should be enabled at the overrides file in the following properties. 
     * `namespace` is required. For example: 
           
           instanceID: "hybrid-instance-1"
           namespace: "apigee"
           

     * If you are using a single service account (Non-prod) for all components, specify it with: `gcp.workloadIdentity.gsa`. For example: 
           
           gcp:
               workloadIdentity:
                 enabled: true
                 gsa: "apigee-non-prod@my-hybrid-project.iam.gserviceaccount.com"
             

     * If you are using a separate service account for each component (Prod installations), specify the service account with the component's `gsa` property. For example: 
           
           logger:
               gsa: "apigee-logger@my-hybrid-project.iam.gserviceaccount.com"
             

See: [`gcp.workloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref#gcp-workloadidentity-enabled).

  2. Check that the current `gcloud` configuration is set to your Google Cloud project ID with the following command: 
         
         gcloud config get project

If needed, set the current `gcloud` configuration:
    
    gcloud config set project $PROJECT_ID

  3. Verify that Workload Identity is enabled for your GKE Cluster. When you created the cluster in [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-cluster#gke), step 6 was to Enable Workload Identity. You can confirm if Workload Identity is enabled by running the following command: 

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

  * `apigee-datastore`
  * `apigee-telemetry`
  * `apigee-org`
  * `apigee-env`



When you run the `helm upgrade` with the `--dry-run` flag for the `apigee-datastore`, `apigee-env`, `apigee-org`, and `apigee-telemetry` charts, the output will include the commands you will need to configure Workload Identity with the correct GSA and KSA names. 

For example:
    
    
    helm upgrade datastore apigee-datastore/ \
      --namespace APIGEE_NAMESPACE \
      -f overrides.yaml \
      --dry-run=server
    
    
    NAME: datastore
    ...
    For Cassandra backup GKE Workload Identity, please make sure to add the below membership to the IAM policy binding using the respective kubernetes SA (KSA).
    gcloud iam service-accounts add-iam-policy-binding _my-service-account_ @_my-project_.iam.gserviceaccount.com \
          --role roles/iam.workloadIdentityUser \
          --member "serviceAccount:_my-project_.svc.id.goog[apigee/apigee-cassandra-default]" \
          --project _my-project_
    
    kubectl annotate serviceaccount apigee-cassandra-default \
          iam.gke.io/gcp-service-account=_my-service-account_ @_my-project_.iam.gserviceaccount.com \
          --namespace apigee
    

  1. Get the command to set up Workload Identity for `apigee-datastore` and run the command under `NOTES:` in the output. 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace APIGEE_NAMESPACE \
           -f overrides.yaml \
           --dry-run=server

  2. Get the commands to set up Workload Identity for `apigee-telemetry` and run the command under `NOTES:` in the output. 
         
         helm upgrade telemetry apigee-telemetry/ \
           --namespace APIGEE_NAMESPACE \
           -f overrides.yaml \
           --dry-run=server

  3. Get the commands to set up Workload Identity for `apigee-org` and run the command under `NOTES:` in the output. 
         
         helm upgrade $ORG_NAME apigee-org/ \
           --namespace APIGEE_NAMESPACE \
           -f overrides.yaml \
           --dry-run=server

  4. Get the commands to set up Workload Identity for `apigee-env` and run the command under `NOTES:` in the output. 
         
         helm upgrade $ENV_NAME apigee-env/ \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f overrides.yaml \
           --dry-run=server

Repeat this step for each environment in your installation.

  5. (Optional) You can see the status of your Kubernetes service accounts in the **Kubernetes: Workloads Overview** page in the Google Cloud console. 

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

**Note:** You may see an error status for the `apigee-cassandra-backup` and `apigee-cassandra-restore` service accounts. This is because you are not currently running backup or restore, and these processes have not been fully configured yet. For more information on Cassandra backup and restore, see [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-backup-overview).



## Next steps

In the next step, you will configure the Apigee ingress gateway and deploy a proxy to test your installation.

## Next step

[(NEXT) Step 1: Expose Apigee ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-expose-apigee-ingress) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
