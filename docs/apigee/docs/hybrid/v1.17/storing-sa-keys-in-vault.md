---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-vault/
title: Storing service account keys in Hashicorp Vault \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:33.785820+00:00
---

# Storing service account keys in Hashicorp Vault  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Storing service account keys in Hashicorp Vault Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-vault.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-vault.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/storing-sa-keys-in-vault.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-sa-keys-in-vault.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/storing-sa-keys-in-vault.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/storing-sa-keys-in-vault.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/storing-sa-keys-in-vault.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/storing-sa-keys-in-vault.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/storing-sa-keys-in-vault.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/storing-sa-keys-in-vault.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/storing-sa-keys-in-vault.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/storing-sa-keys-in-vault.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/storing-sa-keys-in-vault.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/storing-sa-keys-in-vault.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/storing-sa-keys-in-vault.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/storing-sa-keys-in-vault.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/storing-sa-keys-in-vault.html)



##  Storing service account secrets in Hashicorp Vault 

This feature allows you to store Google service account certs for Apigee Hybrid in [Hashicorp Vault](https://www.vaultproject.io/), an external secret manager. External secret managers allow you to manage how data is stored in Kubernetes, including managing data residency and fine grained access controls.

If you are not using [Workload Identity on GKE clusters](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-gke) or [Workload Identity Federation on EKS and AKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation), your Apigee hybrid components need to authenticate Google service accounts to be able to perform their tasks. There are three methods for storing and referring to Google service account keys in Apigee hybrid:

  * Service account JSON key files (`.json` files) stored on a hard drive. Refer to these in your overrides with the `serviceAccountPath` configuration property. For example: 
        
        logger:
          serviceAccountPath: service-accounts/myhybridorg-apigee-logger.json
        

  * Service account JSON key files (`.json` files) stored on a hard drive. Refer to these in your overrides with the `serviceAccountPath` configuration property. See [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about). 
  * Service account certs stored in a Kubernetes secret. Refer to these in your overrides with the `serviceAccountRef` configuration property. See [Storing service account keys in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-k8s-secrets). 
  * Service account certs stored in Hashicorp Vault, explained in this guide. Refer to these in your overrides with the `serviceAccountSecretProviderClass` configuration property. 



## Set up to store service account secrets in Vault

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

**Note:** `mint` is only required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later).   
           
         secret/data/apigee/envsakeys-ENV_NAME

| 
         
         {
           "runtime": "***",
           "synchronizer": "***"
         }  
  
Replace the `"***"` in each pair with the contents of the .json file for the google service account corresponding to the apigee component. `apigee-cassandra-backup` and `apigee-cassandra-restore` both use the `apigee-cassandra` service account. For example: 
         
         {
           "cassandraBackup": "{
             "type": "service_account",
             "project_id": "my-project",
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
         NAMES=apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-${ORG_ENCODE},apigee-cassandra-schema-val-${ORG_ENCODE},apigee-cassandra-user-setup-${ORG_ENCODE},apigee-mart-${ORG_ENCODE},apigee-mint-task-scheduler-${ORG_ENCODE},apigee-connect-agent-${ORG_ENCODE},apigee-operator-guardrails-sa,apigee-watcher-${ORG_ENCODE},apigee-metrics-apigee-telemetry,apigee-open-telemetry-collector-apigee-telemetry,apigee-logger-apigee-telemetry
         
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
         agent-myhybridorg-5b044c1,apigee-operator-guardrails-sa,apigee-watc
         her-myhybridorg-5b044c1,apigee-metrics-apigee-telemetry,apigee-open
         -telemetry,apigee-synchronizer-myhybridorg-dev-ee52aca,apigee-runti
         m-telemetry-collector-apigee-telemetry,apigee-logger-apigee-e-myhyb
         rridorg-dev-ee52aca,apigee-synchronizer-myhybridog-prod-2d0221c,api
         gee-runtime-myhybridorg-prod-2d0221c

  8. Copy the output text into and separate it into lists, one list for the **org** service account names and a separate list for the **env** service account name for each environment. The **org** service accounts are first in the output list up to `apigee-logger-apigee-telemetry`. 

**The list of**org** service names from the previous example:**
         
         apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,
         apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-myhybrido
         rg-5b044c1,apigee-cassandra-schema-val-myhybridorg-5b044c1,apigee-c
         assandra-user-setup-myhybridorg-5b044c1,apigee-mart-myhybridorg-5b0
         44c1,apigee-mint-task-scheduler-myhybridorg-5b044c1,apigee-connect-
         agent-myhybridorg-5b044c1,apigee-operator-guardrails-sa,apigee-watc
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
               - objectName: "connectAgent"
                 secretPath: ""
                 secretKey: ""
               - objectName: "guardrails"
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

VAULT_ADDRESS is the endpoint where your Vault server is running. If Vault is running in the same cluster as Apigee, the format will generally be `http://vault.APIGEE_NAMESPACE.svc.cluster.local:VAULT_SERVICE_PORT`. 

Save the template to a file named `spc-org.yaml`. 

  2. Apply the org-specific `SecretProviderClass` to your apigee namespace: 
         
         kubectl -n APIGEE_NAMESPACE apply -f spc-org.yaml

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
         

VAULT_ADDRESS is the endpoint where your Vault server is running. If Vault is running in the same cluster and namespace as Apigee, the format will generally be `http://vault.APIGEE_NAMESPACE.svc.cluster.local:VAULT_SERVICE_PORT`. 

Save the template to a file named `spc-env-ENV_NAME.yaml`.

  4. For each environment, apply the environment-specific `SecretProviderClass` to your apigee namespace: 
         
         kubectl -n APIGEE_NAMESPACE apply -f spc-env-ENV_NAME.yaml

Repeat this step for every environment. 




###  Enable external secrets for Google service accounts 

  1. Within your overrides file, add the [`serviceAccountSecretProviderClass`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#serviceaccountsecretproviderclass) and [`envs[].serviceAccountSecretProviderClass`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-serviceaccountsecretproviderclass) configuration properties to enable external secret usage for Google service accounts. You can remove or comment out the `serviceAccountPath` and `serviceAccountPaths` configuration properties: 
         
         serviceAccountSecretProviderClass: apigee-orgsakeys-spc
         
         envs:
           - name: ENV_NAME
             serviceAccountSecretProviderClass: apigee-envsakeys-ENV_NAME-spc

  2. Apply each Helm chart: 
         
         helm upgrade datastore apigee-datastore/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         
         
         helm upgrade telemetry apigee-telemetry/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         
         
         helm upgrade redis apigee-redis/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         
         
         helm upgrade ORG_NAME apigee-org/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         

  3. For each environment, apply the `apigee-env` chart: 
         
         helm upgrade ENV_NAME apigee-env/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --set env=ENV_NAME \
             --atomic \
             -f overrides.yaml
         




## Rolling back to using service account JSON files

If you need to roll back to using stored Google service account JSON files, use the following procedure:

  1. Update your overrides file: 
     1. Remove or comment out the `serviceAccountSecretProviderClass` and `envs:serviceAccountSecretProviderClass` lines. 
     2. Add the `serviceAccountPath` and `serviceAccountPaths` configuration properties with the paths to the appropriate service accounts. 

For example:
    
    _# serviceAccountSecretProviderClass: apigee-orgsakeys-spc - (commented out)_
    
    cassandra:
      backup:
        serviceAccountPath: service-accounts/myhybridorg-apigee-cassandra.json
      restore:
        serviceAccountPath: service-accounts/myhybridorg-apigee-cassandra.json
    
    connectAgent:
      serviceAccountPath: service-accounts/myhybridorg-apigee-mart.json
    
    envs:
      - name: test
      _# serviceAccountSecretProviderClass: apigee-envsakeys-spc - (commented out)_
        serviceAccountPaths:
          runtime: service-accounts/myhybridorg-apigee-runtime.json
          synchronizer: service-accounts/myhybridorg-apigee-synchronizer.json
    
    guardrails:
      serviceAccountPath: service-accounts/myhybridorg-apigee-guardrails.json
    
    logger:
      serviceAccountPath: service-accounts/myhybridorg-apigee-logger.json
    
    mart:
      serviceAccountPath: service-accounts/myhybridorg-apigee-mart.json
    
    metrics:
      serviceAccountPath: service-accounts/myhybridorg-apigee-metrics.json
    
    mint: # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
      serviceAccountPath: service-accounts/myhybridorg-apigee-mint-task-scheduler.json
    
    
    watcher:
      serviceAccountPath: service-accounts/myhybridorg-apigee-watcher.json
    

**Note:** If your hybrid installation uses kubernetes secrets instead of service account JSON files, use the `serviceAccountRef` configuration property instead of `serviceAccountPath`. 
  2. Apply each Helm chart: 
         
         helm upgrade datastore apigee-datastore/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         
         
         helm upgrade telemetry apigee-telemetry/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         
         
         helm upgrade redis apigee-redis/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         
         
         helm upgrade ORG_NAME apigee-org/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml
         

  3. For each environment, apply the `apigee-env` chart: 
         
         helm upgrade ENV_NAME apigee-env/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --set env=ENV_NAME \
             --atomic \
             -f overrides.yaml
         

Repeat this step for every environment. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
