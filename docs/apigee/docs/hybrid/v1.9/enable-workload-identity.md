---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enable-workload-identity/
title: Enabling Workload Identity with Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:37:08.031465+00:00
---

# Enabling Workload Identity with Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enable-workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enabling Workload Identity with Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/enable-workload-identity.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enable-workload-identity.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-workload-identity.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enable-workload-identity.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enable-workload-identity.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enable-workload-identity.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/enable-workload-identity.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/enable-workload-identity.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/enable-workload-identity.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/enable-workload-identity.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/enable-workload-identity.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/enable-workload-identity.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/enable-workload-identity.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/enable-workload-identity.html)



This topic explains how to enable Workload Identity for Apigee hybrid. 

**Note:** Apigee hybrid v.1.9 only supports Workload Identity federation on GKE.

## Overview

Workload Identity is a way for applications running within GKE (Google Kubernetes Engine) to access Google Cloud services. For overviews of Workload Identity, see:

  * [ Introducing Workload Identity: Better authentication for your GKE applications](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications)
  * [Using Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)



A Google Cloud IAM service account is an identity that an application can use to make requests to Google APIs. These service accounts are referred to as GSA (Google Service Accounts) in the document. For more information about GSAs, see [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

Separately, Kubernetes also has the concept of service accounts. A service account provides an identity for processes that run in a Pod. Kubernetes service accounts are Kubernetes resources, while Google service accounts are specific to Google Cloud. For information on Kubernetes service accounts, see [ Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the Kubernetes documentation.

With Apigee hybrid 1.4 and later, Apigee creates and uses a Kubernetes service account for each type of component. Enabling Workload Identity allows the hybrid components to interact with the Kubernetes service accounts.

### Google service accounts in Apigee hybrid without Workload Identity

Without using Workload Identity, you must link the Google service accounts to each component in your overrides.yaml file with either a reference to a cert file or a Kubernetes secret. For example: 

  * Cert files: 
        
        watcher:
          serviceAccountPath: ./apigee-org/my-hybrid-project-apigee-watcher.json

See: 

[cassandra.backup.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#cassandra-backup-serviceaccountpath)  
[cassandra.restore.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#cassandra-restore-serviceaccountpath)  
[connectAgent.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#connectagent-serviceaccountpath)  
[diagnostic.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#diagnostic-serviceaccountpath)  
[envs[].serviceAccountPaths.runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#envs-serviceaccountpaths-runtime)  
[envs[].serviceAccountPaths.synchronizer](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#envs-serviceaccountpaths-synchronizer)  
[envs[].serviceAccountPaths.udca](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#envs-serviceaccountpaths-udca) |  [logger.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#logger-serviceaccountpath)  
[mart.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#mart-serviceaccountpath)  
[metrics.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#metrics-serviceaccountpath)  
[synchronizer.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#synchronizer-serviceaccountpath)  
[udca.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#udca-serviceaccountpath)  
[watcher.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-propwatcher-ref#-serviceaccountpath)  
---|---  
  * Kubernetes secret: 
        
        watcher:
          serviceAccountRef: my-watcher-k8s-secret

See: 

[cassandra.backup.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#cassandra-backup-serviceaccountref)  
[cassandra.restore.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#cassandra-restore-serviceaccountref)  
[connectAgent.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#connectagent-serviceaccountref)  
[diagnostic.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#diagnostic-serviceaccountref)  
[envs[].serviceAccountRefs.runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#envs-serviceaccountrefs-runtime)  
[envs[].serviceAccountRefs.synchronizer](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#envs-serviceaccountrefs-synchronizer)  
[envs[].serviceAccountRefs.udca](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#envs-serviceaccountrefs-udca) |  [logger.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#logger-serviceaccountref)  
[mart.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#mart-serviceaccountref)  
[metrics.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#metrics-serviceaccountref)  
[synchronizer.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#synchronizer-serviceaccountref)  
[udca.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#udca-serviceaccountref)  
[watcher.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-propwatcher-ref#-serviceaccountref)  
---|---  



### Environment variables used in these procedures

These procedures make use of the following environment variables. Either set these in your command shell or replace them in the code samples with the actual values: 

  * **`APIGEECTL_HOME`** : The directory where you have installed `apigeectl`.
  * **`CLUSTER_LOCATION`** : The region or zone of your cluster, for example: `us-west1`.
  * **`ENV_NAME`** : Then name of the Apigee environment.
  * **`NAMESPACE`** : The Kubernetes namespace you are using for Apigee hybrid. Usually `apigee`.
  * **`HYBRID_FILES`** : Your hybrid files directory, for example `hybrid-base-directory/hybrid-files`.
  * **`ORG_NAME`** : The name of your Apigee organization.
  * **`PROJECT_ID`** : The ID of your Google Cloud project.



Verify the environment variables:
    
    
    echo $PROJECT_ID
    echo $ORG_NAME
    echo $ENV_NAME
    echo $NAMESPACE
    echo $CLUSTER_LOCATION
    echo $APIGEECTL_HOME
    echo $HYBRID_FILES
    

Initialize any of the variables you need:
    
    
    export PROJECT_ID=my-project-id
    export ORG_NAME=$PROJECT_ID
    export ENV_NAME=my-environment-name
    export NAMESPACE=apigee
    export CLUSTER_LOCATION=my-cluster-location
    export APIGEECTL_HOME=hybrid-base-directory/apigeectl
    export HYBRID_FILES=hybrid-base-directory/hybrid-files
    

## Workload Identity and service account key files

When running Apigee hybrid on GKE, the standard practice is to create and download private keys (`.json` files) for each of the service accounts. When using Workload Identity, you do not need to download service account private keys and add them to GKE clusters.

If you have downloaded service account key files as part of your Apigee hybrid installation, you can delete them after enabling Workload Identity. In most installations, they reside in the `hybrid-base-directory/hybrid-files/service-accounts/` directory.

## Enable Workload Identity for Apigee hybrid

To begin, follow the instructions in Prepare to enable Workload Identity to update node pools and initialize variables prior to enabling Workload Identity.

Then, follow _one of_ these sections, depending on the steps you're performing: 

  * Enable Workload Identity for a fresh install. Follow these instructions for a new Apigee hybrid installation or if you have not already installed ASM on your hybrid installation.
  * Upgrade an installation to use Workload Identity. Follow these instructions to enable Workload Identity on your existing Apigee hybrid installation. 



### Prepare to enable Workload Identity

Before starting the install process, follow the steps in this section.

  1. Set the project to the project you're modifying: 
         
         gcloud config set project $PROJECT_ID

  2. Get the `gcloud` credentials of the cluster on which you are enabling Workload Identity with the following command: 
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
           --region **${CLUSTER_LOCATION}** \
           --project **${PROJECT_ID}**

**Note:** If you created a zonal cluster instead of a regional cluster, get the credentials with the following command: 
         
         gcloud container clusters get-credentials **${CLUSTER_NAME}** \
           --zone **${CLUSTER_LOCATION}** \
           --project **${PROJECT_ID}**

  3. Verify that Workload Identity is enabled for the GKE cluster running Apigee with the following command: 
         
         gcloud container clusters describe $CLUSTER_NAME --region $CLUSTER_LOCATION --project $PROJECT_ID

**Note:** For zonal clusters use: 
         
         gcloud container clusters describe $CLUSTER_NAME --zone $CLUSTER_LOCATION --project $PROJECT_ID

The output should include something like the following: 
         
         …
           …
           status: RUNNING
           subnetwork: default
           workloadIdentityConfig:
             workloadPool: my-project-id.svc.id.goog

If needed, enable workload identity on the cluster. This operation can take up to 30 minutes:
         
         gcloud container clusters update **$CLUSTER_NAME** \
           --workload-pool=**$PROJECT_ID**.svc.id.goog \
           --project **$PROJECT_ID** \
           --region **$CLUSTER_LOCATION**

**Note:** If you created a zonal cluster instead of a regional cluster, use the `--zone` argument instead of `--region` as in the following command: 
         
         gcloud container clusters update **$CLUSTER_NAME** \
           --workload-pool=**$PROJECT_ID**.svc.id.goog \
           --zone **$CLUSTER_LOCATION** \
           --project **$PROJECT_ID**

For more information, see [Enable Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable). 

  4. Ensure Workload Identity is enabled on each node pool. 
     1. List your node pools with the following command: 
            
            gcloud container node-pools list \
              --cluster $CLUSTER_NAME \
              --region $CLUSTER_LOCATION \
              --project $PROJECT_ID

Your output should look something like:
            
            NAME            MACHINE_TYPE   DISK_SIZE_GB  NODE_VERSION
              apigee-runtime  e2-standard-4  100           1.23.12-gke.100
              apigee-data     e2-standard-4  100           1.23.12-gke.100

     2. Ensure Workload Identity is enabled per node pool using the following command for each node pool: 
            
            gcloud container node-pools update NODE_POOL_NAME \
              --cluster=$CLUSTER_NAME \
              --region $CLUSTER_LOCATION \
              --project $PROJECT_ID \
              --workload-metadata=GKE_METADATA

Where NODE_POOL_NAME is the name of each node pool.




### Verify or create Google service accounts

Google service accounts are created for many Apigee hybrid components during installation. Use this procedure to verify the Google service accounts and create any that are needed. 

  1. Check the names of the Google service accounts for your project with the following command: 
         
         gcloud iam service-accounts list --project $PROJECT_ID

Your output should look something like:

###  Prod 

For non-production environments:
         
         DISPLAY NAME         EMAIL                                                      DISABLED
         apigee-cassandra     apigee-cassandra@my_project_id.iam.gserviceaccount.com     False
         apigee-logger        apigee-logger@my_project_id.iam.gserviceaccount.com        False
         apigee-mart          apigee-mart@my_project_id.iam.gserviceaccount.com          False
         apigee-metrics       apigee-metrics@my_project_id.iam.gserviceaccount.com       False
         apigee-runtime       apigee-runtime@my_project_id.iam.gserviceaccount.com       False
         apigee-synchronizer  apigee-synchronizer@my_project_id.iam.gserviceaccount.com  False
         apigee-udca          apigee-udca@my_project_id.iam.gserviceaccount.com          False
         apigee-watcher       apigee-watcher@my_project_id.iam.gserviceaccount.com       False
         

###  Non-prod 

For non-production environments:
         
         DISPLAY NAME         EMAIL                                                      DISABLED
         apigee-non-prod      apigee-non-prod@my_project_id.iam.gserviceaccount.com      False
         

**Tip:** If you have custom names for your service accounts that do not correspond easily with the names of the Apigee components, you can determine the role of each service account by checking the roles assigned to it and comparing the roles with the roles recommended in [**About service accounts**](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-about#recommended-sas). 

Use the following command to check the roles assigned to a service account:
         
         gcloud projects get-iam-policy ${PROJECT_ID}  \
         --flatten="bindings[].members" \
         --format='table(bindings.role)' \
         --filter="SERVICE_ACCOUNT_NAME"

If you need to create the Google service accounts for your project, there are two methods you can use:

     * Use the [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/create-service-account) tool included with apigee in the `apigeectl/tools/` directory. This tool can create all the service accounts with a single command or let you create them individually. `create-service-account` generates key files for each service account and downloads them. Using Workload Identity, you will not need these key files. If you are concerned about the security of these key files, you may want to delete them. Alternatively you can use `gcloud` to create the service accounts and assign the appropriate roles to them.
     * Use the `gcloud iam service-accounts create` command to create the service accounts one at a time and the `gcloud projects add-iam-policy-binding` command to assign the appropriate roles to each service account. This method requires you to create each service account individually, but lets you avoid downloading the key files. 

### `create-service-account`

Use the following command to create a Google service account per component: 

###  Prod 

For non-production environments:
    
    $APIGEECTL_HOME/tools/create-service-account --env prod --dir $APIGEECTL_HOME/../service-accounts

This command will create the following service accounts:

     * `apigee-cassandra`
     * `apigee-logger`
     * `apigee-mart`
     * `apigee-metrics`
     * `apigee-runtime`
     * `apigee-synchronizer`
     * `apigee-udca`
     * `apigee-watcher`

###  Non-prod 

For non-production environments:
    
    $APIGEECTL_HOME/tools/create-service-account --env non-prod --dir $APIGEECTL_HOME/../service-accounts

This command will create a single service accounts, `apigee-non-prod`, with all the roles assigned needed to manage all Apigee components.

### `gcloud`

Create the following service accounts and assign roles to them. 

**Tip:** If you want to use custom names, change the red service account name in the code sample to the name you want to use.
     1. **Service account:**`apigee-cassandra`, **role:**`roles/storage.objectAdmin`

Create the account:
            
            gcloud iam service-accounts create apigee-cassandra \
              --display-name="apigee-cassandra" \
              --project $PROJECT_ID
                        

Assign the role:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
              --member="serviceAccount:apigee-cassandra@$PROJECT_ID.iam.gserviceaccount.com" \
              --role="roles/storage.objectAdmin"
                        

     2. **Service account:**`apigee-logger`, **role:**`roles/logging.logWriter`

Create the account:
            
            gcloud iam service-accounts create apigee-logger \
              --display-name="apigee-logger" \
              --project $PROJECT_ID
                        

Assign the role:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
              --member="serviceAccount:apigee-logger@$PROJECT_ID.iam.gserviceaccount.com" \
              --role="roles/logging.logWriter"
                        

     3. **Service account:**`apigee-mart`, **role:**`roles/apigeeconnect.Agent`

Create the account:
            
            gcloud iam service-accounts create apigee-mart \
              --display-name="apigee-mart" \
              --project $PROJECT_ID
                        

Assign the role:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
              --member="serviceAccount:apigee-mart@$PROJECT_ID.iam.gserviceaccount.com" \
              --role="roles/apigeeconnect.Agent"
                        

     4. **Service account:**`apigee-metrics`, **role:**`roles/monitoring.metricWriter`

Create the account:
            
            gcloud iam service-accounts create apigee-metrics \
              --display-name="apigee-metrics" \
              --project $PROJECT_ID
                        

Assign the role:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
              --member="serviceAccount:apigee-metrics@$PROJECT_ID.iam.gserviceaccount.com" \
              --role="roles/monitoring.metricWriter"
                        

     5. **Service account:**`apigee-runtime`, **role:**_No role assigned._

Create the account:
            
            gcloud iam service-accounts create apigee-runtime \
              --display-name="apigee-runtime" \
              --project $PROJECT_ID
                        

     6. **Service account:**`apigee-synchronizer`, **role:**`roles/apigee.synchronizerManager`

Create the account:
            
            gcloud iam service-accounts create apigee-synchronizer \
              --display-name="apigee-synchronizer" \
              --project $PROJECT_ID
                        

Assign the role:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
              --member="serviceAccount:apigee-synchronizer@$PROJECT_ID.iam.gserviceaccount.com" \
              --role="roles/apigee.synchronizerManager"
                        

     7. **Service account:**`apigee-udca`, **role:**`roles/apigee.analyticsAgent`

Create the account:
            
            gcloud iam service-accounts create apigee-udca \
              --display-name="apigee-udca" \
              --project $PROJECT_ID
                        

Assign the role:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
              --member="serviceAccount:apigee-udca@$PROJECT_ID.iam.gserviceaccount.com" \
              --role="roles/apigee.analyticsAgent"
                        

     8. **Service account:**`apigee-watcher`, **role:**`roles/apigee.runtimeAgent`

Create the account:
            
            gcloud iam service-accounts create apigee-watcher \
              --display-name="apigee-watcher" \
              --project $PROJECT_ID
                        

Assign the role:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
              --member="serviceAccount:apigee-watcher@$PROJECT_ID.iam.gserviceaccount.com" \
              --role="roles/apigee.runtimeAgent"
                        




###  Set `workloadIdentityEnabled: true` and create service accounts 

`apigeectl` creates Kubernetes service accounts for each Apigee hybrid component when you set `workloadIdentityEnabled: true` in your overrides file and apply the changes. 

  1. Add the bolded line below to your `overrides.yaml` file under the `gcp` stanza. This enables Workload Identity for your installation and triggers `apigeectl` to create the Kubernetes service accounts when you apply the configuration: 
         
         gcp:
           projectID: "my-project-id"
           name: "my-project-id"
           region: "analytics-region"
           **workloadIdentityEnabled: true**

  2. Add the bolded lines below to your `overrides.yaml` file under the `cassandra` stanza. This triggers the creation of the `apigee-cassandra-backup` Kubernetes service account: 
         
         cassandra:
           ...
           **backup:
             enabled: true**

  3. Apply the changes with `apigeectl` with the `--restore` flag: 
         
         $APIGEECTL_HOME/apigeectl apply -f overrides/overrides.yaml --restore

**Note:** The `--restore` flag triggers creation of the `apigee-cassandra-restore` Kubernetes service account.
  4. Verify the service accounts with the following command: 
         
         kubectl get sa -n $NAMESPACE

Your output should look something like the following. The Kubernetes service accounts in **bold** are the ones you will need to annotate with your Google service accounts: 
         
         NAME                                                         SECRETS   AGE
         **apigee-cassandra-backup**                                      1         11m
         **apigee-cassandra-restore**                                     1         11m
         **apigee-cassandra-schema-setup- my-project-id-123abcd-sa**       1         11m
         **apigee-cassandra-schema-val- my-project-id-123abcd**            1         11m
         **apigee-cassandra-user-setup- my-project-id-123abcd-sa**         1         11m
         **apigee-connect-agent- my-project-id-123abcd-sa**                1         11m
         **apigee-datastore-default-sa**                                  1         11m
         apigee-ingressgateway                                        1         11m
         apigee-ingressgateway-my-project-id-123abcd                  1         11m
         apigee-ingressgateway-manager                                1         11m
         apigee-init                                                  1         11m
         **apigee-mart- my-project-id-123abcd-sa**                         1         11m
         **apigee-metrics-sa**                                            1         11m
         apigee-mint-task-scheduler-my-project-id-123abcd-sa          1         11m
         apigee-redis-default-sa                                      1         11m
         apigee-redis-envoy-default-sa                                1         11m
         **apigee-runtime- my-project-id-env-name-234bcde-sa**             1         11m
         **apigee-synchronizer- my-project-id-env-name-234bcde**-sa        1         11m
         **apigee-udca- my-project-id-123abcd-sa**                         1         11m
         **apigee-udca- my-project-id-env-name-234bcde-**sa                1         11m
         **apigee-watcher- my-project-id-123abcd-sa**                      1         11m
         default                                                      1         11m
             




### Annotate the Kubernetes service accounts with the Google service accounts

For each Apigee component annotate the corresponding Kubernetes service accounts with the Google service account for the component. 

#### Org-level components

You will have only one instance of each Kubernetes service account for your Apigee org.

Component | Kubernetes Service Account | Google Service Account  
---|---|---  
**Cassandra** | `apigee-cassandra-backup` | `apigee-cassandra`  
`apigee-cassandra-restore ` | `apigee-cassandra`  
`apigee-cassandra-schema-setup-my-project-id-num-id1-sa` | `apigee-cassandra`  
`apigee-cassandra-schema-val-my-project-id-num-id1` | `apigee-cassandra`  
`apigee-cassandra-user-setup-my-project-id-num-id1-sa` | `apigee-cassandra`  
`apigee-datastore-default-sa` | `apigee-cassandra`  
**Apigee Connect** | `apigee-connect-agent-my-project-id-num-id1-sa` | `apigee-mart`  
**MART** | `apigee-mart-my-project-id-num-id1-sa` | `apigee-mart`  
**Metrics** | `apigee-metrics-sa` | `apigee-metrics`  
**UDCA (org-level)** | `apigee-udca-my-project-id-num-id1-sa` | `apigee-udca` | **Watcher** | `apigee-watcher-my-project-id-num-id1-sa` | `apigee-watcher`  
  
#### Env-level components

You will have one instance of each Kubernetes service account for each Apigee environment.

Component | Kubernetes Service Account | Google Service Account  
---|---|---  
**Apigee Runtime** | `apigee-runtime-my-project-id-env-name-num-id2-sa` | `apigee-runtime`  
**Synchronizer** | `apigee-synchronizer-my-project-id-env-name-num-id2-sa` | `apigee-synchronizer`  
**UDCA (env-level)** | `apigee-udca-my-project-id-env-name-num-id2-sa` | `apigee-udca`  
**IMPORTANT:** If your service account names do not match the default names created by `create-service-account`, in the following commands replace the red service account name with the correct service account name for the component. For example, if your Cassandra service account is named `my-cassandra-accnt-1`, then replace `apigee-cassandra` with that name in the command.

In the following commands use the Kubernetes service account names returned by the `kubectl get sa -n $NAMESPACE` command, for example: `apigee-cassandra-schema-val-hybrid-example-project-123abcd`. 

In this procedure, for each Kubernetes service account, you will: 

  * Bind the Kubernetes service account and the principal Google service account to the `roles/iam.workloadIdentityUser` IAM role. 
  * Annotate the Kubernetes service account with the Google service account. 


  1. Bind the roles and annotate the service accounts. 

####  Org-level components 

Annotate Kubernetes service accounts for the org-level components. You will need to do this once for each component in your Apigee organization. 

     * **Cassandra**

The Cassandra component has six associated Kubernetes service accounts:

       * `apigee-cassandra-backup`
       * `apigee-cassandra-restore`
       * `apigee-cassandra-schema-setup`
       * `apigee-cassandra-schema-val` _(`val` = validation)_
       * `apigee-cassandra-user-setup`
       * `apigee-datastore-default`

###  Prod 

**`apigee-cassandra-backup`**

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-cassandra"
              KSA_NAME="apigee-cassandra-backup"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-restore`**

       1. Redefine the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-cassandra-restore"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-schema-setup-service-account-name`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-schema-setup-service-account-name"

Bind the IAM role:
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       2. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-schema-val-service-account-name`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-schema-val-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-user-setup-service-account-name`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-user-setup-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-datastore-default-sa`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-datastore-default-sa"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

**`apigee-cassandra-backup`**

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-non-prod"
              KSA_NAME="apigee-connect-agent-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-restore`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-restore"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-schema-setup-service-account-name`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-schema-setup-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-schema-val-service-account-name`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-schema-val-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-cassandra-user-setup-service-account-name`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-user-setup-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

**`apigee-datastore-default-sa`**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-datastore-default-sa"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

     * **Apigee Connect**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-mart"
              KSA_NAME="apigee-connect-agent-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-connect-agent-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

     * **MART**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-mart"
              KSA_NAME="apigee-mart-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-mart-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

     * **Apigee metrics**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-metrics"
              KSA_NAME="apigee-metrics-sa"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-metrics-sa"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

     * **UDCA (org-level)**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-udca"
              KSA_NAME="apigee-udca-org-level-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME`environment variables: 
              
              KSA_NAME="apigee-udca-org-level-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                  --role roles/iam.workloadIdentityUser \
                  --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                  $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                  --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

     * **Apigee Watcher**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-watcher"
              KSA_NAME="apigee-watcher-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-watcher-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

For each environment:

     * **Runtime**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-runtime"
              KSA_NAME="apigee-runtime-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-runtime-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

     * **Synchronizer**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-synchronizer"
              KSA_NAME="apigee-synchronizer-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-synchronizer-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

     * **UDCA (env-level)**

###  Prod 

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-udca"
              KSA_NAME="apigee-udca-env-level-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

###  Non-prod 

       1. Define the `KSA_NAME` environment variable: 
              
              KSA_NAME="apigee-udca-env-level-service-account-name"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com

  2. Validate if the steps worked: 
         
         gcloud config set project $PROJECT_ID
         

Select a kubernetes service account to test, for example: `apigee-cassandra-backup`. 
         
         KSA_NAME="kubernetes-service-account-name"
         
         
         kubectl run --rm -it --image google/cloud-sdk:slim \
           --namespace $NAMESPACE workload-identity-test\
           -- gcloud auth list

If you don't see a command prompt, try pressing `Enter`.

If the steps were correctly run, you should see a response like the following:
         
         Credentialed Accounts
         ACTIVE  ACCOUNT
         *       GSA@PROJECT_ID.iam.gserviceaccount.com

  3. If upgrading from a previous install, clean up secrets that contained service account private keys: 
         
         kubectl delete secrets -n $NAMESPACE $(k get secrets -n $NAMESPACE | grep svc-account | awk '{print $1}')
         

  4. Check logs: 
         
         kubectl logs -n $NAMESPACE -l app=apigee=synchronizer,env=$ENV_NAME,org=$ORG_NAME apigee-synchronizer
         




##  Upgrade an install to use Workload Identity 

Follow these instructions to add Workload Identity to an existing hybrid installation. 

Here is a sample showing Google Service Accounts (GSA) created for Apigee: 
    
    
    gcloud iam service-accounts list --filter "apigee"
    
    
    DISPLAY NAME       EMAIL                                                  DISABLED
    apigee-cassandra   apigee-cassandra@PROJECT_ID.iam.gserviceaccount.com    False
    apigee-connect     apigee-connect@PROJECT_ID.iam.gserviceaccount.com      False
    apigee-runtime     apigee-runtime@PROJECT_ID.iam.gserviceaccount.com      False
    apigee-metrics     apigee-metrics@PROJECT_ID.iam.gserviceaccount.com      False
    apigee-mart        apigee-mart@PROJECT_ID.iam.gserviceaccount.com         False
    apigee-watcher     apigee-watcher@PROJECT_ID.iam.gserviceaccount.com      False
    apigee-sync        apigee-sync@PROJECT_ID.iam.gserviceaccount.com         False
    apigee-udca        apigee-udca@$PROJECT_ID.iam.gserviceaccount.com        False
    

Here is a sample Kubernetes service accounts (KSA) created for Apigee: 
    
    
    kubectl get sa -n $NAMESPACE
    
    
    
    apigee-cassandra-schema-setup-ORG_NAME-cb84b88-sa             1         xxd
    apigee-cassandra-user-setup-ORG_NAME-cb84b88-sa               1         xxd
    apigee-connect-agent-ORG_NAME-cb84b88-sa                      1         xxd
    apigee-init                                                   1         xxd
    apigee-mart-ORG_NAME-cb84b88-sa                               1         xxd
    apigee-metrics-apigee-telemetry                               1         xxd
    apigee-runtime-ORG_NAME-ENV_NAME-1d0dc5e-sa                   1         xxd
    apigee-synchronizer-ORG_NAME-ENV_NAME-1d0dc5e-sa              1         xxd
    apigee-udca-ORG_NAME-ENV_NAME-1d0dc5e-sa                      1         xxd
    apigee-watcher-ORG_NAME-cb84b88                               1         xxd

**Where:** ORG_NAME and ENV_NAME may be a shortened version of the organization and environment names.

  1. Add the Workload Identity role to each service account: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com
         

For example, if you were setting the permissions for Apigee Synchronizer, you would run:
         
         export KSA_NAME=$(kubectl get sa -n apigee -l app=apigee-synchronizer,env=$ENV_NAME,org=$ORG_NAME --output=jsonpath={.items..metadata.name})
         
         
         gcloud iam service-accounts add-iam-policy-binding --role roles/iam.workloadIdentityUser --member "serviceAccount:$PROJECT_ID.svc.id.goog[apigee/$KSA_NAME]" apigee-sync@$PROJECT_ID.iam.gserviceaccount.com
         

  2. Annotate each KSA with the GSA details: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE \
           $KSA_NAME \
           iam.gke.io/gcp-service-account=GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com
         

For example, if you were setting the permissions for Apigee Synchronizer, you would run:
         
         export KSA_NAME=$(kubectl get sa -n apigee -l app=apigee-synchronizer,env=$ENV_NAME,org=$ORG_NAME --output=jsonpath={.items..metadata.name})
         
         
         kubectl annotate serviceaccount --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=apigee-sync@$PROJECT_ID.iam.gserviceaccount.com
         

  3. Validate if the steps worked: 
         
         gcloud config set project $PROJECT_ID
         
         
         kubectl run --rm -it --image google/cloud-sdk:slim \
           --namespace $NAMESPACE workload-identity-test\
           -- gcloud auth list

If you don't see a command prompt, try pressing `Enter`.

If the steps were correctly run, you should see a response like the following:
         
         Credentialed Accounts
         ACTIVE  ACCOUNT
         *       GSA@PROJECT_ID.iam.gserviceaccount.com

  4. If upgrading from a previous install, clean up secrets that contained service account private keys: 
         
         kubectl delete secrets -n $NAMESPACE $(k get secrets -n $NAMESPACE | grep svc-account | awk '{print $1}')
         

  5. Check logs: 
         
         kubectl logs -n $NAMESPACE -l app=apigee=synchronizer,env=$ENV_NAME,org=$ORG_NAME apigee-synchronizer
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
