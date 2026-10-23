---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication/
title: Step 5: Set up service account authentication \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:01.966527+00:00
---

# Step 5: Set up service account authentication  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 5: Set up service account authentication Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-sa-authentication.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-sa-authentication.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-sa-authentication.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-sa-authentication.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-sa-authentication.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-sa-authentication.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-sa-authentication.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-sa-authentication.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-sa-authentication.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-sa-authentication.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-sa-authentication.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-sa-authentication.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-sa-authentication.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-sa-authentication.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-sa-authentication.html)



## Overview

This step explains how to set up the authentication methods for the Google Cloud service accounts you created in the previous step. 

Select the instructions for the authentication method you want to use. See [Service account authentication methods in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-authentication-methods) for an overview of the different authentication methods. 

**Note:** In the following instructions, if you are using: 

  * **Workload Identity Federation for GKE** : select the tab **WIF for GKE**.
  * **Workload Identity Federation** : select the tab **WIF on other platforms**.



### Kubernetes Secrets

### Service accounts

You will need to create Kubernetes secrets for the following service accounts:

### Production

  * `apigee-cassandra`
  * `apigee-guardrails`
  * `apigee-logger`
  * `apigee-mart`
  * `apigee-metrics`
  * `apigee-mint-task-scheduler` (if you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid))
  * `apigee-runtime`
  * `apigee-synchronizer`
  * `apigee-watcher`



### Non-prod

  * `apigee-non-prod`



You will supply each of these secrets during the [Create the overrides file](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides) step. 

This procedure uses the following optional environment variables:

  * `$APIGEE_HELM_CHARTS_HOME`
  * `$APIGEE_NAMESPACE`
  * `$PROJECT_ID`



If you did not define these variables, substitute the appropriate value for each variable in the code samples.

### Create Kubernetes secrets

Create the Kubernetes secrets to store the service account keys.

The `kubectl create secret` command in the following code samples has the structure:
    
    
    kubectl create secret generic SECRET_NAME \
      --from-file="client_secret.json=PATH_TO_SERVICE_ACCOUNT_KEY" \
      -n $APIGEE_NAMESPACE

**Note:** The following commands assume you downloaded the service account key files to the `$APIGEE_HELM_CHARTS_HOME/service-accounts/` directory in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts). If you downloaded the keys to a different directory, edit the commands to use the correct directory. 

### Production
    
    
    kubectl create secret generic apigee-logger-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-logger.json" \
      -n $APIGEE_NAMESPACE
    kubectl create secret generic apigee-guardrails-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-guardrails.json" \
      -n $APIGEE_NAMESPACE
    kubectl create secret generic apigee-metrics-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-metrics.json" \
      -n $APIGEE_NAMESPACE
    kubectl create secret generic apigee-watcher-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-watcher.json" \
      -n $APIGEE_NAMESPACE
    kubectl create secret generic apigee-mart-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-mart.json" \
      -n $APIGEE_NAMESPACE
    kubectl create secret generic apigee-synchronizer-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-synchronizer.json" \
      -n $APIGEE_NAMESPACE
    kubectl create secret generic apigee-runtime-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-runtime.json" \
      -n $APIGEE_NAMESPACE

If you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid), you also need to create a Kubernetes secret for the `apigee-mint-task-scheduler` service account:
    
    
    kubectl create secret generic apigee-mint-task-scheduler-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-mint-task-scheduler.json" \
      -n $APIGEE_NAMESPACE

### Non-prod
    
    
    kubectl create secret generic apigee-non-prod-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-non-prod.json" \
      -n $APIGEE_NAMESPACE

**Optional:** You can delete the service account JSON files after you create the Kubernetes secrets. 

For more information about using Kubernetes secrets with Apigee hybrid, see [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-k8s-secrets).

### JSON files

No additional steps are needed to set up authentication with JSON files. Proceed to [Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates). 

### Vault

### Set up to store service account secrets in Vault

###  Install CSI driver and Vault provider 

If you haven't already installed the CSI driver on your cluster using Helm, follow the instructions in [Secrets Store CSI Driver: Installation](https://secrets-store-csi-driver.sigs.k8s.io/getting-started/installation.html). For more information, see [Installing the Vault CSI provider](https://developer.hashicorp.com/vault/docs/platform/k8s/csi/installation) in the Vault documentation. 

See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#csi-driver) for the minimum CSI Driver versions supported by Apigee hybrid.

###  Create Vault secrets, policies, and roles 

Use the Vault UI or APIs to create secrets and grant permissions for the Kubernetes service accounts used by Apigee hybrid to read those secrets. 

  1. Create the organization and environment-specific secrets in the following format: Secret Key| Secret Data  
---|---  
           
         secret/data/apigee/orgsakeys

| 
         
         {
             "cassandraBackup": "***",
             "cassandraRestore": "***",
             "connectAgent": "***",
             "guardrails": "***",
             "logger": "***",
             "mart": "***",
             "metrics": "***",
             "mint": "***",
             "watcher": "***"
         }

**Note:** `mint` is only required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid).   
           
         secret/data/apigee/envsakeys-ENV_NAME

| 
         
         {
             "runtime": "***",
             "synchronizer": "***"
         }  
  
Replace the `"***"` in each pair with the contents of the .json file for the Google service account corresponding to the apigee component. `apigee-cassandra-backup` and `apigee-cassandra-restore` both use the `apigee-cassandra` service account. For example: 
         
         {
             "cassandraBackup": "{
                 "type": "service_account",
                 "project_id": "myhybridorg",
                 "private_key_id": "PRIVATE_KEY_ID",
                 "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY_TEXT\n-----END PRIVATE KEY-----\n",
                 "client_email": "apigee-cassandra@myhybridorg.iam.gserviceaccount.com",
                 "client_id": "123456789012345678901",
                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                 "token_uri": "https://oauth2.googleapis.com/token",
                 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                 "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/apigee-cassandra%40myhybridorg.iam.gserviceaccount.com",
                 "universe_domain": "googleapis.com"
             }",
             "cassandraRestore":...
         ...
         }

  2. Grant access to the organization secret. Create a text file named orgsakeys-auth-policy.txt with the following contents: 
         
         path "secret/data/apigee/orgsakeys" {
             capabilities = ["read"]
         }

  3. Within Vault, create a policy which grants access to the organization secret: 
         
         vault policy write apigee-orgsakeys-auth orgsakeys-auth-policy.txt

  4. For each environment, create a text file named `envsakeys-ENV_NAME-auth-policy.txt` with the following contents: 
         
         path "secret/data/apigee/envsakeys-ENV_NAME" {
             capabilities = ["read"]
         }

Repeat this step for each environment. 

  5. Within Vault, create a policy which grants access to the environment secret: 
         
         vault policy write apigee-envsakeys-ENV_NAME-auth envsakeys-ENV_NAME-auth-policy.txt

Repeat this step for each environment. 

  6. Create a script called `generate-encoded-sas.sh` with the following contents: 
         
         # generate-encoded-sas.sh
         
         ORG=$APIGEE_ORG            # Apigee organization name
         ENVS=$APIGEE_ENV_LIST      # comma separated env names, for example: dev,prod
         
         ORG_SHORT_NAME=$(echo $ORG | head -c 15)
         ENCODE=$(echo -n $ORG | shasum -a 256 | head -c 7)
         ORG_ENCODE=$(echo "$ORG_SHORT_NAME-$ENCODE")
         NAMES=apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-${ORG_ENCODE},apigee-cassandra-schema-val-${ORG_ENCODE},apigee-cassandra-user-setup-${ORG_ENCODE},apigee-mart-${ORG_ENCODE},apigee-mint-task-scheduler-${ORG_ENCODE},apigee-connect-agent-${ORG_ENCODE},apigee-watcher-${ORG_ENCODE},apigee-metrics-apigee-telemetry,apigee-open-telemetry-collector-apigee-telemetry,apigee-logger-apigee-telemetry,apigee-operator-guardrails-sa
         
         for ENV in ${ENVS//,/ }
         do
             ENV_SHORT_NAME=$(echo $ENV | head -c 15)
             ENCODE=$(echo -n $ORG:$ENV | shasum -a 256 | head -c 7)
             ENV_ENCODE=$(echo "$ORG_SHORT_NAME-$ENV_SHORT_NAME-$ENCODE")
             NAMES+=,apigee-synchronizer-${ENV_ENCODE},apigee-runtime-${ENV_ENCODE}
         done
         
         echo $NAMES
         

**Note:** Remove `apigee-mint-task-scheduler-${ORG_ENCODE}` if not using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid). 
  7. Run the script to generate the service account name list to bind the policy to: 
         
         ./generate-encoded-sas.sh

**Tip:** You may need to change the permissions of the script file to make it executable, for example: 
         
         chmod +x ./generate-encoded-sas.sh

Your output should be a list of Kubernetes service account names separated by commas, similar to the following example: 
         
         ./generate-encoded-sas.sh
         apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,
         apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-myhybrido
         rg-5b044c1,apigee-cassandra-schema-val-myhybridorg-5b044c1,apigee-c
         assandra-user-setup-myhybridorg-5b044c1,apigee-mart-myhybridorg-5b0
         44c1,apigee-mint-task-scheduler-myhybridorg-5b044c1,apigee-connect-
         agent-myhybridorg-5b044c1,apigee-watcher-myhybridorg-5b044c1,apigee
         -metrics-apigee-telemetry,apigee-open-telemetry-collector-apigee-te
         lemetry,apigee-logger-apigee-telemetry,apigee-operator-guardrails-s
         a,apigee-synchronizer-myhybridorg-dev-ee52aca,apigee-runtime-myhybr
         idorg-dev-ee52aca,apigee-synchronizer-myhybridorg-prod-2d0221c,apig
         ee-runtime-myhybridorg-prod-2d0221c

  8. Copy the output text into and separate it into lists, one list for the **org** service account names and a separate list for the **env** service account name for each environment. The **org** service accounts are first in the output list up to `apigee-logger-apigee-telemetry`. 

**The list of**org** service names from the previous example:**
         
         apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,
         apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-myhybrido
         rg-5b044c1,apigee-cassandra-schema-val-myhybridorg-5b044c1,apigee-c
         assandra-user-setup-myhybridorg-5b044c1,apigee-mart-myhybridorg-5b0
         44c1,apigee-mint-task-scheduler-myhybridorg-5b044c1,apigee-connect-
         agent-myhybridorg-5b044c1,apigee-watcher-myhybridorg-5b044c1,apigee
         -metrics-apigee-telemetry,apigee-open-telemetry-collector-apigee-te
         lemetry,apigee-logger-apigee-telemetry,apigee-operator-guardrails-s
         a

The **env** service account names have the pattern `apigee-synchronizer-ORG_NAME-ENV_NAME-HASH_TEXT` and `apigee-runtime-ORG_NAME-ENV_NAME-HASH_TEXT`. Separate them into separated lists for each environment. For example, the output from the previous example can be separated into the following two lists: 

`dev` environment: 
         
         apigee-synchronizer-myhybridorg-dev-ee52aca,apigee-runtime-myhybrid
         org-dev-ee52aca

`prod` environment: 
         
         apigee-synchronizer-myhybridorg-prod-2d0221c,apigee-runtime-myhybri
         dorg-prod-2d0221c

  9. Using the policy, create a Vault role which binds the organization specific Apigee service accounts: 
         
         vault write auth/kubernetes/role/apigee-orgsakeys \
             bound_service_account_names=LIST_OF_ORG_SA_NAMES \
             bound_service_account_namespaces=apigee \
             policies=apigee-orgsakeys-auth \
             ttl=1m
         

  10. For each environment, create a Vault role for its service account keys: 
         
         vault write auth/kubernetes/role/apigee-envsakeys-ENV_NAME \
             bound_service_account_names=LIST_OF_ENV_NAME_SA_NAMES \
             bound_service_account_namespaces=apigee \
             policies=apigee-envsakeys-ENV_NAME-auth \ 
             ttl=1m
         

Repeat this step for every environment. 




### Create `SecretProviderClass` objects

The `SecretProviderClass` resource tells the CSI driver what provider to communicate with when requesting secrets. The service account keys must be configured via this object. The following table shows the file names (`objectNames`) expected by Apigee Hybrid: 

Service account| Expected secret file names  
---|---  
Cassandra backup | `cassandraBackup`  
Cassandra restore | `cassandraRestore`  
Guardrails | `guardrails`  
Connect agent | `connectAgent`  
Logger | `logger`  
MART | `mart`  
Metrics | `metrics`  
Monetization  
(if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) | `mint`  
Runtime | `runtime`  
Synchronizer | `synchronizer`  
Watcher | `watcher`  
  
  1. Use the following `SecretProviderClass` template to configure this resource for the organization-specific secrets: 
         
         apiVersion: secrets-store.csi.x-k8s.io/v1
         kind: SecretProviderClass
         metadata:
             name: apigee-orgsakeys-spc
         spec:
             provider: vault
             parameters:
                 roleName: apigee-orgsakeys
                 vaultAddress: VAULT_ADDRESS
                 # "objectName" is an alias used within the SecretProviderClass to reference
                 # that specific secret. This will also be the filename containing the secret.
                 # Apigee Hybrid expects these exact values so they must not be changed.
                 # "secretPath" is the path in Vault where the secret should be retrieved.
                 # "secretKey" is the key within the Vault secret response to extract a value from.
                 objects: |
                     - objectName: "cassandraBackup"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "cassandraRestore"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "guardrails"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "connectAgent"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "logger"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "mart"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "metrics"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "mint"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "watcher"
                         secretPath: ""
                         secretKey: ""
         

**Note:** Remove the `objectName: "mint"` lines if not using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid). 

VAULT_ADDRESS is the endpoint where your Vault server is running. If Vault is running in the same cluster as Apigee, the format will generally be `http://vault.$APIGEE_NAMESPACE.svc.cluster.local:VAULT_SERVICE_PORT`. 

Save the template to a file named `spc-org.yaml`. 

  2. Apply the org-specific `SecretProviderClass` to your apigee namespace: 
         
         kubectl -n $APIGEE_NAMESPACE apply -f spc-org.yaml

  3. For each environment, use the following `SecretProviderClass` template to configure this resource for the environment-specific secrets. Repeat this step for every environment: 
         
         apiVersion: secrets-store.csi.x-k8s.io/v1
         kind: SecretProviderClass
         metadata:
             name: apigee-envsakeys-ENV_NAME-spc
         spec:
             provider: vault
             parameters:
                 roleName: apigee-envsakeys-ENV_NAME
                 vaultAddress: VAULT_ADDRESS
                 # "objectName" is an alias used within the SecretProviderClass to reference
                 # that specific secret. This will also be the filename containing the secret.
                 # Apigee Hybrid expects these exact values so they must not be changed.
                 # "secretPath" is the path in Vault where the secret should be retrieved.
                 # "secretKey" is the key within the Vault secret response to extract a value from.
                 objects: |
                     - objectName: "runtime"
                         secretPath: ""
                         secretKey: ""
                     - objectName: "synchronizer"
                         secretPath: ""
                         secretKey: ""
         

VAULT_ADDRESS is the endpoint where your Vault server is running. If Vault is running in the same cluster and namespace as Apigee, the format will generally be `http://vault.$APIGEE_NAMESPACE.svc.cluster.local:VAULT_SERVICE_PORT`. 

Save the template to a file named `spc-env-ENV_NAME.yaml`.

  4. For each environment, apply the environment-specific `SecretProviderClass` to your apigee namespace: 
         
         kubectl -n $APIGEE_NAMESPACE apply -f spc-env-ENV_NAME.yaml

Repeat this step for every environment. 

  5. **Optional:** You can delete the service account JSON files after you create the `SecretProviderClass` objects. 



### WIF for GKE

### Prepare to configure Workload Identity Federation for GKE

  1. Verify that Workload Identity Federation for GKE is enabled in your overrides file. It should be enabled at the overrides file in the following properties. 
     * `namespace` is required. For example: 
           
           instanceID: "hybrid-instance-1"
           namespace: "apigee"
           

     * If you are using a single service account (Non-prod) for all components, specify it with: `gcp.workloadIdentity.gsa`. For example: 
           
           gcp:
               workloadIdentity:
                 enabled: true
                 gsa: "apigee-non-prod@my-hybrid-project.iam.gserviceaccount.com"
             

     * If you are using a separate service account for each component (Production installations), specify the service account with the component's `gsa` property. For example: 
           
           logger:
               gsa: "apigee-logger@my-hybrid-project.iam.gserviceaccount.com"
             

See: [`gcp.workloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-workloadidentity-enabled).

  2. Check that the current `gcloud` configuration is set to your Google Cloud project ID with the following command: 
         
         gcloud config get project

If needed, set the current `gcloud` configuration:
    
    gcloud config set project $PROJECT_ID

  3. Verify that Workload Identity Federation for GKE is enabled for your GKE Cluster. When you created the cluster in [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster#gke), step 6 was to Enable Workload Identity Federation for GKE. Confirm it is enabled with the following command: 

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
           workloadPool: $PROJECT_ID.svc.id.goog

If you see `null` instead in your results, run the following command to enable Workload Identity Federation for GKE for your cluster: 

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
             

**Tip:** You can limit the output to the `workloadMetadataConfig` field by piping the output through `grep` with the `-A 1` flag to include the following line: 
         
         gcloud container node-pools describe apigee-data \
           --cluster $CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:" | grep "workloadMetadataConfig" -A 1
         




### Set up guardrails with Workload Identity Federation for GKE

During initial installation, the `apigee-operator` chart creates a guardrails pod to check if the correct APIs are enabled for your project. You must configure the service account binding for Workload Identity Federation for GKE to use guardrails during installation before installing the chart.

  1. Get the email address of the guardrails GSA with the following command: 
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

GSA email addresses typically have the format of:
         
         GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
         
         DISPLAY NAME       EMAIL                                                DISABLED
         apigee-guardrails  apigee-guardrails@myproject.iam.gserviceaccount.com  False

Use this email address for the `GSA_EMAIL` variable in the next step.

  2. The Kubernetes service account (KSA) for guardrails is named `apigee-operator-guardrails-sa`. Create the binding for the guardrails GSA with the following command: 
         
         gcloud iam service-accounts add-iam-policy-binding GSA_EMAIL \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:PROJECT_ID.svc.id.goog[$APIGEE_NAMESPACE/apigee-operator-guardrails-sa]" \
           --project PROJECT_ID




For more information, see [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/guardrails). 

### WIF on other platforms

Using Workload Identity Federation on platforms other than GKE, you can use the following methods to configure SA authentication:

  * Kubernetes secrets
  * Service account JSON files
  * Vault



In the following instructions, choose the tab for the authentication method you are using.

This procedure uses the following two environment variables defined in [Step 2: Download the Apigee Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts). These variables are optional. If you did not define them, substitute the appropriate directory path for each variable in the code samples. 

  * `$APIGEE_HELM_CHARTS_HOME`: The directory where you downloaded the Apigee Helm charts, defined in [Step 2: Download the Apigee Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts). 
  * `$PROJECT_ID`: Your Google Cloud project ID, defined in [Part 1: Project and Org setup--Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-enableapi). 



For installations on **AKS** , Make sure you have enabled the [OpenID Connect (OIDC) issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer). You must enable this feature so that Workload Identity Federation can access the OpenID Connect metadata and the JSON Web Key Set (JWKS) for the cluster. 

**Note:** If the cluster gets deleted for any reason, the IAM provider will need to be recreated.

###  Configure your cluster to use Workload Identity Federation. 

  1. Check that the current `gcloud` configuration is set to your Google Cloud project ID with the following command: 
         
         gcloud config get project

If needed, set the current `gcloud` configuration:
    
    gcloud config set project $PROJECT_ID

  2. Enable the Security Token Service API: 

Check that the Security Token Service API is enabled with the following command: 
         
         gcloud services list --enabled --project $PROJECT_ID | grep sts.googleapis.com

If the API is not enabled: 

### Console

Enable the Security Token Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sts.googleapis.com&redirect=https%3A//console.cloud.google.com)

### Command line

Enable the API with the following command: 
         
         gcloud services enable sts.googleapis.com --project $PROJECT_ID

  3. Create the workload identity pool and provider. 

#### Required roles

To get the permissions that you need to configure Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project: 

     * [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure identity federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

To create a workload identity pool and provider, do the following: 

     1. Determine the issuer URL of your AKS cluster: 

### AKS
            
            az aks show -n CLUSTER_NAME -g RESOURCE_GROUP --query "oidcIssuerProfile.issuerUrl" -otsv

Replace the following: 

        * `CLUSTER_NAME`: The name of the cluster.
        * `RESOURCE_GROUP`: The resource group of the cluster.

The command outputs the issuer URL. You will need the issuer URL in one of the following steps. 

If the command doesn't return an issuer URL, verify that you've enabled the [OIDC issuer](https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer) feature. 

### EKS
    
    aws eks describe-cluster --name CLUSTER_NAME --query "cluster.identity.oidc.issuer" --output text
    

Replace `CLUSTER_NAME` with the name of the cluster. 

The command outputs the issuer URL. You need the issuer URL in one of the following steps. 

### Other Kubernetes

Connect to your Kubernetes cluster and use `kubectl` to determine your cluster's issuer URL:
    
    kubectl get --raw /.well-known/openid-configuration | jq -r .issuer
    

You need the issuer URL in one of the following steps. 

     2. **Optional:** If your OIDC issuer is not publicly accessible, download the cluster's JSON Web Key Set (JWKS): **Note:** This step requires kubectl access to your cluster. **Tip:** When using the JWKS file, you will need to upload a new JWKS file whenever you rotate the signing keys for the cluster. 
            
            kubectl get --raw /openid/v1/jwks > cluster-jwks.json

To check if your OIDC provider is publicly available, you should be able to access your provider URL with a CURL command and receive a 200 response. 

     3. Create a new workload identity pool: 
            
            gcloud iam workload-identity-pools create POOL_ID \
                --location="global" \
                --description="DESCRIPTION" \
                --display-name="DISPLAY_NAME"
            

Replace the following: 

        * `POOL_ID`: The unique ID for the pool.
        * `DISPLAY_NAME`: (Optional) The name of the pool.
        * `DESCRIPTION`: (Optional) A description of the pool that you choose. This description appears when you grant access to pool identities.

For example:
    
    gcloud iam workload-identity-pools create my-wi-pool --display-name="My workload pool" --description="My workload pool description"

     4. Add the cluster as a workload identity pool provider. Choose the command to create the provider depending on whether your OIDC issuer is **publicly accessible** or **not publicly accessible** : 

### Publicly accessible

If your OIDC issuer is publicly accessible, create the provider with the following command: 
            
            gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
                --location="global" \
                --workload-identity-pool="POOL_ID" \
                --issuer-uri="ISSUER" \
                --attribute-mapping="google.subject=assertion.sub"

### Not publicly accessible

If your OIDC issuer is not publicly accessible, create the provider with the following command: 
            
            gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
                --location="global" \
                --workload-identity-pool="POOL_ID" \
                --issuer-uri="ISSUER" \
                --jwks-file="cluster-jwks.json" \
                --attribute-mapping="google.subject=assertion.sub"

**Note:** If you rotate your keys, you must [upload the new JWKS](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage-oidc-keys) with each key rotation. 

The command doesn't validate the cluster's JWKS. If the JWKS is malformed or expired, subsequent authentication attempts might fail with an error message `Error connecting to the given credential's issuer`.

Replace the following: 

        * `WORKLOAD_PROVIDER_ID`: A unique workload identity pool provider ID of your choice. 
        * `POOL_ID`: The workload identity pool ID that you created earlier. 
        * `ISSUER`: Use the issuer URL you determined earlier for the issuer URI . 

`attribute-mapping="google.subject=assertion.sub"` maps the Kubernetes subject to the IAM subject. 




###  Create the credential configuration files 

To deploy a Kubernetes workload that can access Google Cloud resources, you first need to create a credential configuration file for each IAM service account: 

  1. List the **IAM service accounts** (_also called "Google service accounts"_) with the following command: 
         
         gcloud iam service-accounts list --project $PROJECT_ID

**Note:** You most likely have already created the IAM service accounts (also called "Google service accounts") during initial installation of Apigee hybrid with the [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/create-service-account) tool. See [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about#recommended-sas) for a list of IAM service accounts needed by Apigee hybrid. See [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts) for the installation guide procedure to create the IAM service accounts. 

You will need to create the credential configuration files for the following IAM service accounts: 

###  Production 

For production environments:
         
         DISPLAY NAME         EMAIL                                                      DISABLED
         apigee-cassandra     apigee-cassandra@my_project_id.iam.gserviceaccount.com     False
         apigee-guardrails    apigee-guardrails@my_project_id.iam.gserviceaccount.com    False
         apigee-mart          apigee-mart@my_project_id.iam.gserviceaccount.com          False
         apigee-metrics       apigee-metrics@my_project_id.iam.gserviceaccount.com       False
         apigee-runtime       apigee-runtime@my_project_id.iam.gserviceaccount.com       False
         apigee-synchronizer  apigee-synchronizer@my_project_id.iam.gserviceaccount.com  False
         apigee-watcher       apigee-watcher@my_project_id.iam.gserviceaccount.com       False
         

If you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid), you will also need to create the credential configuration file for the `apigee-mint-task-scheduler` service account.
         
         DISPLAY NAME                 EMAIL                                                              DISABLED
         ...
         apigee-mint-task-scheduler   apigee-mint-task-scheduler@my_project_id.iam.gserviceaccount.com   False
         ...

### Non-prod

For non-production environments:
         
         DISPLAY NAME         EMAIL                                                      DISABLED
         apigee-non-prod      apigee-non-prod@my_project_id.iam.gserviceaccount.com      False
         

**Tip:** If you have custom names for your service accounts that do not correspond easily with the names of the Apigee components, you can determine the role of each service account by checking the roles assigned to it and comparing the roles with the roles recommended in [**About service accounts**](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about#recommended-sas). 

Use the following command to check the roles assigned to a service account:
         
         gcloud projects get-iam-policy $PROJECT_ID  \
             --flatten="bindings[].members" \
             --format='table(bindings.role)' \
             --filter="SERVICE_ACCOUNT_NAME"

Note which custom service account corresponds to each IAM SA listed in the previous list.

  2. Create a credential configuration file for each IAM service account in the previous list. 

###  WIF: secrets 

This approach uses credential configurations stored in Kubernetes secrets. When you build your overrides file in [Step 7: Create the overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides), you supply the name of the secret for each service account with the `serviceAccountRef` or `envs.serviceAccountRefs` property. 

### Create the credential configuration files

### Production

You will need to create the credential configuration files for the following service accounts:

     * `apigee-cassandra`
     * `apigee-guardrails`
     * `apigee-mart`
     * `apigee-metrics`
     * `apigee-mint-task-scheduler` if you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid).
     * `apigee-runtime`
     * `apigee-synchronizer`
     1. Create a directory for the credential configuration files. The directory can have any name. For this procedure, the directory is named `credential-configurations`: 
            
            mkdir $APIGEE_HELM_CHARTS_HOME/credential-configurations

     2. Create the credential configuration file for **`apigee-cassandra`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-cassandra@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-cassandra-credential-configuration.json
            

Where: 

        * `PROJECT_NUMBER`: The project number of the project containing the workload identity pool. This must be the project number instead of the project ID. 
        * `POOL_ID`: The ID of the workload identity pool 
        * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider 
**Important:** `credential-source-type` must be set to `text`. 
     3. Create the credential configuration file for **`apigee-guardrails`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-guardrails@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-guardrails-credential-configuration.json
            

     4. Create the credential configuration file for **`apigee-mart`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-mart@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-mart-credential-configuration.json
            

     5. Create the credential configuration file for **`apigee-metrics`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-metrics@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-metrics-credential-configuration.json
            

     6. Create the credential configuration file for **`apigee-runtime`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-runtime@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-runtime-credential-configuration.json
            

     7. Create the credential configuration file for **`apigee-synchronizer`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-synchronizer@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-synchronizer-credential-configuration.json
            

     8. Create the credential configuration file for **`apigee-watcher`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-watcher@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-watcher-credential-configuration.json
            

     9. If you are using Monetization for Apigee hybrid, you will also need to create the credential configuration file for **`apigee-mint-task-scheduler`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-mint-task-scheduler@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-mint-task-scheduler-credential-configuration.json
            

**Note:** Do not create a credential configuration file for the `apigee-logger` service account. 

### Non-prod

     1. Create a directory for the credential configuration file. The directory can have any name. For this procedure, the directory is named `credential-configurations`: 
            
            mkdir $APIGEE_HELM_CHARTS_HOME/credential-configurations

     2. Create the credential configuration file in the for the `apigee-non-prod` service account in the `credential-configurations` directory with the following command: 
            
            gcloud iam workload-identity-pools create-cred-config \
            projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-non-prod-credential-configuration.json
            

Where: 

        * `PROJECT_NUMBER`: The project number of the project containing the workload identity pool. This must be the project number instead of the project ID. 
        * `POOL_ID`: The ID of the workload identity pool 
        * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider 
**Important:** `credential-source-type` must be set to `text`. 

### Create the Kubernetes secrets

Create the Kubernetes secrets to store the credential configuration files for each service account. 

The `kubectl create secret` command in the following code samples has the structure:
    
    kubectl create secret generic SECRET_NAME \
            --from-file="client_secret.json=PATH_TO_CREDENTIAL_CONFIGURATION_FILE" \
            -n $APIGEE_NAMESPACE

### Production

     1. Create the secret file for **`apigee-cassandra`** : 
            
            kubectl create secret generic apigee-cassandra-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-cassandra.json" \
              -n $APIGEE_NAMESPACE
            

     2. Create the secret file for **`apigee-guardrails`** : 
            
            kubectl create secret generic apigee-guardrails-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-guardrails.json" \
              -n $APIGEE_NAMESPACE
            

     3. Create the secret file for **`apigee-mart`** : 
            
            kubectl create secret generic apigee-mart-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-mart.json" \
              -n $APIGEE_NAMESPACE
            

     4. Create the secret file for **`apigee-metrics`** : 
            
            kubectl create secret generic apigee-metrics-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-metrics.json" \
              -n $APIGEE_NAMESPACE
            

     5. Create the secret file for **`apigee-runtime`** : 
            
            kubectl create secret generic apigee-runtime-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-runtime.json" \
              -n $APIGEE_NAMESPACE

     6. Create the secret file for **`apigee-synchronizer`** : 
            
            kubectl create secret generic apigee-synchronizer-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-synchronizer.json" \
              -n $APIGEE_NAMESPACE
            

     7. Create the secret file for **`apigee-watcher`** : 
            
            kubectl create secret generic apigee-watcher-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-watcher.json" \
              -n $APIGEE_NAMESPACE
            

     8. If you are using Monetization for Apigee hybrid, create the secret file for **`apigee-mint-task-scheduler`** : 
            
            kubectl create secret generic apigee-mint-task-scheduler-svc-account \
              --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-mint-task-scheduler.json" \
              -n $APIGEE_NAMESPACE
            

Create the secret file for **`apigee-non-prod`** : 

### Non-prod
    
    kubectl create secret generic apigee-non-prod-svc-account \
            --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/credential-configurations/$PROJECT_ID-apigee-non-prod.json" \
            -n $APIGEE_NAMESPACE

### WIF: files

This approach uses the credential configuration files in place of the Google service account key files. When you build your overrides file in [Step 7: Create the overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides), you supply the path to the credential configuration file for each `serviceAccountPath` or `envs.serviceAccountPaths` property. 

### Production

You will need to create the credential configuration files in the corresponding chart directories:

Service account | Apigee Helm chart directory  
---|---  
`apigee-cassandra` | `apigee-datastore/`  
`apigee-guardrails` | `apigee-operator/`  
`apigee-mart` | `apigee-org/`  
`apigee-metrics` | `apigee-telemetry/`  
`apigee-mint-task-scheduler`  
(If using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) | `apigee-org/`  
`apigee-runtime` | `apigee-env/`  
`apigee-synchronizer` | `apigee-env/`  
`apigee-watcher` | `apigee-org/`  
  
Create the credential configuration files with the following commands:

     * **`apigee-cassandra`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-cassandra@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-datastore/apigee-cassandra-credential-configuration.json
           

Where: 

       * `PROJECT_NUMBER`: The project number of the project containing the workload identity pool. This must be the project number instead of the project ID. 
       * `POOL_ID`: The ID of the workload identity pool 
       * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider 
**Important:** `credential-source-type` must be set to `text`. 
     * **`apigee-guardrails`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-guardrails@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-operator/apigee-guardrails-credential-configuration.json
           

     * **`apigee-mart`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-mart@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-org/apigee-mart-credential-configuration.json
           

     * **`apigee-metrics`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-metrics@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-telemetry/apigee-metrics-credential-configuration.json
           

     * **`apigee-runtime`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-runtime@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-env/apigee-runtime-credential-configuration.json
           

     * **`apigee-synchronizer`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-synchronizer@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-env/apigee-synchronizer-credential-configuration.json
           

     * **`apigee-watcher`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-watcher@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-org/apigee-watcher-credential-configuration.json
           

     * If you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid), you will also need to create the credential configuration file for **`apigee-mint-task-scheduler`** : 
           
           gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
             --service-account=apigee-mint-task-scheduler@$PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/service-account/token \
             --credential-source-type=text \
             --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-org/apigee-mint-task-scheduler-credential-configuration.json
           

**Note:** Do not create a credential configuration file for the `apigee-logger` service account. 

### Non-prod

You will need to create the credential configuration file and copy it into the corresponding chart directories:

Service account | Apigee Helm chart  
---|---  
`apigee-non-prod` | `apigee-datastore/`  
`apigee-telemetry/`  
`apigee-org/`  
`apigee-env/`  
     1. Create the credential configuration file in the `apigee-datastore` chart directory with the following command: 
            
            gcloud iam workload-identity-pools create-cred-config \
            projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
            --service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com \
            --credential-source-file=/var/run/service-account/token \
            --credential-source-type=text \
            --output-file=$APIGEE_HELM_CHARTS_HOME/apigee-datastore/apigee-non-prod-credential-configuration.json
            

Where: 

        * `PROJECT_NUMBER`: The project number of the project containing the workload identity pool. This must be the project number instead of the project ID. 
        * `POOL_ID`: The ID of the workload identity pool 
        * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider 
**Important:** `credential-source-type` must be set to `text`. 
     2. Copy the credential configuration file to the `apigee-env`, `apigee-org/`, and `apigee-telemetry/` chart directory. 
            
            cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/apigee-non-prod-credential-configuration.json \
              $APIGEE_HELM_CHARTS_HOME/apigee-env/apigee-non-prod-credential-configuration.json
            
            cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/apigee-non-prod-credential-configuration.json \
              $APIGEE_HELM_CHARTS_HOME/apigee-org/apigee-non-prod-credential-configuration.json
            
            cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/apigee-non-prod-credential-configuration.json \
              $APIGEE_HELM_CHARTS_HOME/apigee-telemetry/apigee-non-prod-credential-configuration.json

**Note:** Unlike a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys), a credential configuration file doesn't contain a private key and doesn't need to be kept confidential. Details about the credential configuration file are available at <https://google.aip.dev/auth/4117>. 

###  WIF: Vault 

This approach uses credential configurations stored in an external secret manager, Hashicorp Vault. When you build your overrides file in [Step 7: Create the overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides), you supply org-level and environment-level vault secrets with the `serviceAccountSecretProviderClass` or `envs.serviceAccountSecretProviderClass` properties. 

### Create the credential configuration files

### Production

You will need to create the credential configuration files for the following service accounts:

     * `apigee-cassandra`
     * `apigee-guardrails`
     * `apigee-mart`
     * `apigee-metrics`
     * `apigee-mint-task-scheduler` (If using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid))
     * `apigee-runtime`
     * `apigee-synchronizer`
     1. Create a directory for the credential configuration files. The directory can have any name. For this procedure, the directory is named `credential-configurations`: 
            
            mkdir $APIGEE_HELM_CHARTS_HOME/credential-configurations

     2. Create the credential configuration file for **`apigee-cassandra`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-cassandra@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-cassandra-credential-configuration.json
            

Where: 

        * `PROJECT_NUMBER`: The project number of the project containing the workload identity pool. This must be the project number instead of the project ID. 
        * `POOL_ID`: The ID of the workload identity pool 
        * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider 
**Important:** `credential-source-type` must be set to `text`. 
     3. Create the credential configuration file for **`apigee-guardrails`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-guardrails@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-guardrails-credential-configuration.json
            

     4. Create the credential configuration file for **`apigee-mart`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-mart@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-mart-credential-configuration.json
            

     5. Create the credential configuration file for **`apigee-metrics`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-metrics@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-metrics-credential-configuration.json
            

     6. Create the credential configuration file for **`apigee-runtime`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-runtime@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-runtime-credential-configuration.json
            

     7. Create the credential configuration file for **`apigee-synchronizer`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-synchronizer@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-synchronizer-credential-configuration.json
            

     8. Create the credential configuration file for **`apigee-watcher`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-watcher@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-watcher-credential-configuration.json
            

     9. If you are using Monetization for Apigee hybrid, you will also need to create the credential configuration file for **`apigee-mint-task-scheduler`** : 
            
            gcloud iam workload-identity-pools create-cred-config \
              projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-mint-task-scheduler@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-mint-task-scheduler-credential-configuration.json
            

**Note:** Do not create a credential configuration file for the `apigee-logger` service account. 

### Non-prod

     1. Create a directory for the credential configuration file. The directory can have any name. For this procedure, the directory is named `credential-configurations`: 
            
            mkdir $APIGEE_HELM_CHARTS_HOME/credential-configurations

     2. Create the credential configuration file in the for the `apigee-non-prod` service account in the `credential-configurations` directory with the following command: 
            
            gcloud iam workload-identity-pools create-cred-config \
            projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
              --service-account=apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com \
              --credential-source-file=/var/run/service-account/token \
              --credential-source-type=text \
              --output-file=$APIGEE_HELM_CHARTS_HOME/credential-configurations/apigee-non-prod-credential-configuration.json
            

Where: 

        * `PROJECT_NUMBER`: The project number of the project containing the workload identity pool. This must be the project number instead of the project ID. **Tip:** You can find the project number with the following command: 
              
              gcloud projects describe $PROJECT_ID --format="value(projectNumber)"

        * `POOL_ID`: The ID of the workload identity pool 
        * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider 
**Important:** `credential-source-type` must be set to `text`. 

###  Install CSI driver and Vault provider 

If you haven't already installed the CSI driver on your cluster using Helm, follow the instructions in [Secrets Store CSI Driver: Installation](https://secrets-store-csi-driver.sigs.k8s.io/getting-started/installation.html). For more information, see [Installing the Vault CSI provider](https://developer.hashicorp.com/vault/docs/platform/k8s/csi/installation) in the Vault documentation. 

See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#csi-driver) for the minimum CSI Driver versions supported by Apigee hybrid.

###  Create Vault secrets, policies, and roles 

Use the Vault UI or APIs to create secrets and grant permissions for the Kubernetes service accounts used by Apigee hybrid to read those secrets. 

     1. Create the organization and environment-specific secrets in the following format: Secret Key| Secret Data  
---|---  
              
            secret/data/apigee/orgsakeys

| 
            
            {
              "cassandraBackup": "***",
              "cassandraRestore": "***",
              "connectAgent": "***",
              "guardrails": "***",
              "mart": "***",
              "metrics": "***",
              "mint": "***",
              "watcher": "***"
            }

**Note:** `mint` is only required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid).   
              
            secret/data/apigee/envsakeys-ENV_NAME

| 
            
            {
              "runtime": "***",
              "synchronizer": "***"
                }  
  
### Production

Replace the `"***"` in each pair with the contents of the credential configuration file for the Google service account corresponding to the apigee component. `apigee-cassandra-backup` and `apigee-cassandra-restore` both use the `apigee-cassandra` service account. For example: 
            
            {
              "cassandraBackup": "{
                "universe_domain": "googleapis.com",
                "type": "external_account:,"
                "audience": "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider",
                "subject_token_type": "urn:ietf:params:oauth: token-type:jwt",
                "token_url": "https://sts.googleapis.com/v1/token",
                "service
                "impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/apigee-cassandra@my-project.iam.gserviceaccount.com:generateAccessToken",
                "credential_source": {
                  "file": "/var/run/service-account/token",
                  "format": {
                    "type": "text"
                  }
                }
              }",
              "cassandraRestore":...
            ...
            }

### Non-prod

Replace the `"***"` in each pair with the contents of the credential configuration file for the `apigee-non-prod` service account. `apigee-cassandra-backup` and `apigee-cassandra-restore` both use the `apigee-cassandra` service account. For example: 
            
            {
              "cassandraBackup": "{
                "universe_domain": "googleapis.com",
                "type": "external_account:,"
                "audience": "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider",
                "subject_token_type": "urn:ietf:params:oauth: token-type:jwt",
                "token_url": "https://sts.googleapis.com/v1/token",
                "service
                "impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/apigee-non-prod@my-project.iam.gserviceaccount.com:generateAccessToken",
                "credential_source": {
                  "file": "/var/run/service-account/token",
                  "format": {
                    "type": "text"
                  }
                }
              }",
              "cassandraRestore":...
            ...
            }

     2. Grant access to the organization secret. Create a text file named orgsakeys-auth-policy.txt with the following contents: 
            
            path "secret/data/apigee/orgsakeys" {
              capabilities = ["read"]
            }

     3. Within Vault, create a policy which grants access to the organization secret: 
            
            vault policy write apigee-orgsakeys-auth orgsakeys-auth-policy.txt

     4. For each environment, create a text file named `envsakeys-ENV_NAME-auth-policy.txt` with the following contents: 
            
            path "secret/data/apigee/envsakeys-ENV_NAME" {
              capabilities = ["read"]
            }

Repeat this step for each environment. 

     5. Within Vault, create a policy which grants access to the environment secret: 
            
            vault policy write apigee-envsakeys-ENV_NAME-auth envsakeys-ENV_NAME-auth-policy.txt

Repeat this step for each environment. 

     6. Create a script called `generate-encoded-sas.sh` with the following contents: 
            
            # generate-encoded-sas.sh
            
            ORG=$APIGEE_ORG            # Apigee organization name
            ENVS=$APIGEE_ENV_LIST      # comma separated env names, for example: dev,prod
            
            ORG_SHORT_NAME=$(echo $ORG | head -c 15)
            ENCODE=$(echo -n $ORG | shasum -a 256 | head -c 7)
            ORG_ENCODE=$(echo "$ORG_SHORT_NAME-$ENCODE")
            NAMES=apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-${ORG_ENCODE},apigee-cassandra-schema-val-${ORG_ENCODE},apigee-cassandra-user-setup-${ORG_ENCODE},apigee-operator-guardrails-sa,apigee-mart-${ORG_ENCODE},apigee-mint-task-scheduler-${ORG_ENCODE},apigee-connect-agent-${ORG_ENCODE},apigee-watcher-${ORG_ENCODE},apigee-metrics-apigee-telemetry,apigee-open-telemetry-collector-apigee-telemetry,apigee-logger-apigee-telemetry
            
            for ENV in ${ENVS//,/ }
              do
                ENV_SHORT_NAME=$(echo $ENV | head -c 15)
                ENCODE=$(echo -n $ORG:$ENV | shasum -a 256 | head -c 7)
                ENV_ENCODE=$(echo "$ORG_SHORT_NAME-$ENV_SHORT_NAME-$ENCODE")
                NAMES+=,apigee-synchronizer-${ENV_ENCODE},apigee-runtime-${ENV_ENCODE}
              done
            
            echo $NAMES
            

**Note:** Remove `apigee-mint-task-scheduler-${ORG_ENCODE}` if not using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid). 
     7. Run the script to generate the service account name list to bind the policy to: 
            
            ./generate-encoded-sas.sh

**Tip:** You may need to change the permissions of the script file to make it executable, for example: 
            
            chmod +x ./generate-encoded-sas.sh

Your output should be a list of Kubernetes service account names separated by commas, similar to the following example: 
            
            ./generate-encoded-sas.sh
            apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,
            apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-myhybrido
            rg-5b044c1,apigee-cassandra-schema-val-myhybridorg-5b044c1,apigee-c
            assandra-user-setup-myhybridorg-5b044c1,apigee-operator-guardrails-
            sa,apigee-mart-myhybridorg-5b044c1,apigee-mint-task-scheduler-myhyb
            ridorg-5b044c1,apigee-connect-agent-myhybridorg-5b044c1,apigee-watc
            her-myhybridorg-5b044c1,apigee-metrics-apigee-telemetry,apigee-open
            -telemetry-collector-apigee-telemetry,apigee-logger-apigee-telemetr
            y,apigee-synchronizer-myhybridorg-dev-ee52aca,apigee-runtime-myhybr
            idorg-dev-ee52aca,apigee-synchronizer-myhybridorg-prod-2d0221c,apig
            ee-runtime-myhybridorg-prod-2d0221c

     8. Copy the output text into and separate it into lists, one list for the **org** service account names and a separate list for the **env** service account name for each environment. The **org** service accounts are first in the output list up to `apigee-logger-apigee-telemetry`. 

**The list of**org** service names from the previous example:**
            
            apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,
            apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-myhybrido
            rg-5b044c1,apigee-cassandra-schema-val-myhybridorg-5b044c1,apigee-c
            assandra-user-setup-myhybridorg-5b044c1,apigee-operator-guardrails-
            sa,apigee-mart-myhybridorg-5b044c1,apigee-mint-task-scheduler-myhyb
            ridorg-5b044c1,apigee-connect-agent-myhybridorg-5b044c1,apigee-watc
            her-myhybridorg-5b044c1,apigee-metrics-apigee-telemetry,apigee-open
            -telemetry-collector-apigee-telemetry,apigee-logger-apigee-telemetr
            y

The **env** service account names have the pattern `apigee-synchronizer-ORG_NAME-ENV_NAME-HASH_TEXT` and `apigee-runtime-ORG_NAME-ENV_NAME-HASH_TEXT`. Separate them into separated lists for each environment. For example, the output from the previous example can be separated into the following two lists: 

`dev` environment: 
            
            apigee-synchronizer-myhybridorg-dev-ee52aca,apigee-runtime-myhybrid
            org-dev-ee52aca

`prod` environment: 
            
            apigee-synchronizer-myhybridorg-prod-2d0221c,apigee-runtime-myhybri
            dorg-prod-2d0221c

     9. Using the policy, create a Vault role which binds the organization specific Apigee service accounts: 
            
            vault write auth/kubernetes/role/apigee-orgsakeys \
              bound_service_account_names=LIST_OF_ORG_SA_NAMES \
              bound_service_account_namespaces=apigee \
              policies=apigee-orgsakeys-auth \
              ttl=1m
                

     10. For each environment, create a Vault role for its service account keys: 
            
            vault write auth/kubernetes/role/apigee-envsakeys-ENV_NAME \
              bound_service_account_names=LIST_OF_ENV_NAME_SA_NAMES \
              bound_service_account_namespaces=apigee \
              policies=apigee-envsakeys-ENV_NAME-auth \ 
              ttl=1m
            

Repeat this step for every environment. 

### Create `SecretProviderClass` objects

The `SecretProviderClass` resource tells the CSI driver what provider to communicate with when requesting secrets. The service account keys must be configured via this object. The following table shows the file names (`objectNames`) expected by Apigee Hybrid: 

Service account| Expected secret file names  
---|---  
Cassandra backup | `cassandraBackup`  
Cassandra restore | `cassandraRestore`  
Connect agent | `connectAgent`  
Guardrails | `guardrails`  
MART | `mart`  
Metrics | `metrics`  
Monetization  
(if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) | `mint`  
Runtime | `runtime`  
Synchronizer | `synchronizer`  
Watcher | `watcher`  
     1. Use the following `SecretProviderClass` template to configure this resource for the organization-specific secrets: 
            
            apiVersion: secrets-store.csi.x-k8s.io/v1
            kind: SecretProviderClass
            metadata:
              name: apigee-orgsakeys-spc
            spec:
              provider: vault
              parameters:
                roleName: apigee-orgsakeys
                vaultAddress: VAULT_ADDRESS
                # "objectName" is an alias used within the SecretProviderClass to reference
                # that specific secret. This will also be the filename containing the secret.
                # Apigee Hybrid expects these exact values so they must not be changed.
                # "secretPath" is the path in Vault where the secret should be retrieved.
                # "secretKey" is the key within the Vault secret response to extract a value from.
                  objects: |
                  - objectName: "cassandraBackup"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "cassandraRestore"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "connectAgent"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "guardrails"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "mart"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "metrics"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "mint"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "watcher"
                    secretPath: ""
                    secretKey: ""
            

**Note:** Remove the `objectName: "mint"` lines if not using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid). 

VAULT_ADDRESS is the endpoint where your Vault server is running. If Vault is running in the same cluster as Apigee, the format will generally be `http://vault.$APIGEE_NAMESPACE.svc.cluster.local:VAULT_SERVICE_PORT`. 

Save the template to a file named `spc-org.yaml`. 

     2. Apply the org-specific `SecretProviderClass` to your apigee namespace: 
            
            kubectl -n $APIGEE_NAMESPACE apply -f spc-org.yaml

     3. For each environment, use the following `SecretProviderClass` template to configure this resource for the environment-specific secrets. Repeat this step for every environment: 
            
            apiVersion: secrets-store.csi.x-k8s.io/v1
            kind: SecretProviderClass
            metadata:
              name: apigee-envsakeys-ENV_NAME-spc
            spec:
              provider: vault
              parameters:
                roleName: apigee-envsakeys-ENV_NAME
                vaultAddress: VAULT_ADDRESS
                # "objectName" is an alias used within the SecretProviderClass to reference
                # that specific secret. This will also be the filename containing the secret.
                # Apigee Hybrid expects these exact values so they must not be changed.
                # "secretPath" is the path in Vault where the secret should be retrieved.
                # "secretKey" is the key within the Vault secret response to extract a value from.
                objects: |
                  - objectName: "runtime"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "synchronizer"
                    secretPath: ""
                    secretKey: ""
                

VAULT_ADDRESS is the endpoint where your Vault server is running. If Vault is running in the same cluster and namespace as Apigee, the format will generally be `http://vault.$APIGEE_NAMESPACE.svc.cluster.local:VAULT_SERVICE_PORT`. 

Save the template to a file named `spc-env-ENV_NAME.yaml`.

     4. For each environment, apply the environment-specific `SecretProviderClass` to your apigee namespace: 
            
            kubectl -n $APIGEE_NAMESPACE apply -f spc-env-ENV_NAME.yaml

Repeat this step for every environment. 




### Set up guardrails with Workload Identity Federation for GKE

During initial installation, the `apigee-operator` chart creates a guardrails pod to check if the correct APIs are enabled for your project. You must configure the service account binding for Workload Identity Federation for GKE to use guardrails during installation before installing the chart.

  1. Get the email address of the guardrails GSA with the following command: 
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

GSA email addresses typically have the format of:
         
         GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
         
         DISPLAY NAME       EMAIL                                                DISABLED
         apigee-guardrails  apigee-guardrails@myproject.iam.gserviceaccount.com  False

Use this email address for the `GSA_EMAIL` variable in the next steps.

The Kubernetes service account (KSA) for guardrails is named `apigee-operator-guardrails-sa`. Create the binding to grant the guardrails KSA access to impersonate the `apigee-guardrails` GSA with the following command: 

### Production

### Template
    
    gcloud iam service-accounts add-iam-policy-binding \
      GSA_EMAIL \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
        --role=roles/iam.workloadIdentityUser

### Example
    
    gcloud iam service-accounts add-iam-policy-binding \
      apigee-guardrails@my-project.iam.gserviceaccount.com \
        --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-operator-guardrails-sa" \
        --role=roles/iam.workloadIdentityUser

### Non-prod

### Template
    
    gcloud iam service-accounts add-iam-policy-binding \
      NON_PROD_GSA_EMAIL \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
        --role=roles/iam.workloadIdentityUser

### Example
    
    gcloud iam service-accounts add-iam-policy-binding \
      apigee-non-prod@my-project.iam.gserviceaccount.com \
        --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-operator-guardrails-sa" \
        --role=roles/iam.workloadIdentityUser

Where:

     * `GSA_EMAIL`: the email address of the Guardrails IAM service account.
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where you created the workload identity pool. **Note:** You must use the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in the member identifier. Using the project ID is not supported. You can find the project number with the following command: 
           
           gcloud projects describe PROJECT_ID --format="value(projectNumber)"

     * `POOL_ID`: the workload identity pool ID.
     * `MAPPED_SUBJECT`: the Kubernetes Service Account from the claim in your ID token. In most hybrid installations, this will have the format: `system:serviceaccount:$APIGEE_NAMESPACE:KSA_NAME`. 

For `apigee-operator-guardrails-sa`, this will be something similar to `system:serviceaccount:apigee:apigee-operator-guardrails-sa`. 

**Tip:** In the step [Add the cluster as a workload identity pool provider](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication#add-pool-provider) in **Step 5: Set up service account authentication** , the value of `google.subject` is mapped to the value of `sub` in the ID token. Therefore the value of `MAPPED_SUBJECT` will be the value in the ID token following `"sub": `. You can find the mapped subject for a Kubernetes service account by searching the ID token for `sub` followed by the name of the service account. 

For example: pipe the contents of the ID token through `grep -E 'sub.*_apigee-operator-guardrails-sa_ '`




For more information, see [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/guardrails). 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication) [(NEXT) Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
