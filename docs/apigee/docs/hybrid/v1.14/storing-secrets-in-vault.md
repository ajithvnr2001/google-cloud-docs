---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-secrets-in-vault/
title: Storing data in an external secret manager \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:48:17.716598+00:00
---

# Storing data in an external secret manager  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-secrets-in-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Storing data in an external secret manager Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-secrets-in-vault.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-secrets-in-vault.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/storing-secrets-in-vault.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-secrets-in-vault.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/storing-secrets-in-vault.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/storing-secrets-in-vault.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/storing-secrets-in-vault.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/storing-secrets-in-vault.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/storing-secrets-in-vault.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/storing-secrets-in-vault.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/storing-secrets-in-vault.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/storing-secrets-in-vault.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/storing-secrets-in-vault.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/storing-secrets-in-vault.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/storing-secrets-in-vault.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/storing-secrets-in-vault.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/storing-secrets-in-vault.html)



##  Storing data in an external secret manager 

This guide tells you how to store and manage the following types of information in the external secret storage service, [Hashicorp Vault](https://www.vaultproject.io/), instead of in your overrides.yaml file. 

  * **AX Hash Salt**
  * **Redis password**
  * **Encryption keys**



To store other kinds of information in Vault, see:

  * [Storing Cassandra secrets in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-cassandra-secrets-in-vault)
  * [Storing service account keys in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-sa-keys-in-vault)



##  Prerequisites 

  * A **Kubernetes secrets store CSI driver**. You can install it by following instructions in [Secrets Store CSI Driver: Installation](https://secrets-store-csi-driver.sigs.k8s.io/getting-started/installation.html). For supported versions, see [Apigee hybrid supported platforms and versions: Secret Store CSI driver](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#csi-driver). 
  * The **Vault CSI provider**. You can install it by following instructions in [Installing the Vault CSI provider](https://developer.hashicorp.com/vault/docs/platform/k8s/csi/installation). For supported versions, see [Apigee hybrid supported platforms and versions: Vault](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#vault). 



## Procedure

  1. Create the Vault secrets, policies, and roles. 
     1. Use the Vault UI or APIs to create secrets and grant permissions for the Apigee Kubernetes service accounts to read those secrets as described here. The secrets need to consist of a key and one or more values as shown in the following table: **Secret Key** | **Secret Data**  
---|---  
`secret/data/apigee/axhashsalt` | 
            
            {
              "ax-hash-salt": "AX_HASH_SALT_VALUE"
            }  
  
`secret/data/apigee/redis` | 
            
            {
              "redis-password": "REDIS_PASSWORD_VALUE"
            }  
  
`secret/data/apigee/orgencryptionkeys` | 
            
            {
              "kmsEncryptionKey": "KMS_ENCRYPTION_KEY_VALUE"
              "kvmEncryptionKey": "KVM_ENCRYPTION_KEY_VALUE"
              "contractEncryptionKey": "CONTRACT_ENCRYPTION_KEY_VALUE"
            }

**Important:** The `contractEncryptionKey` value must be a base64 encoded string with a length of 16, 24, or 32 characters. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-secrets-in-vault) for more information.   
`secret/data/apigee/envencryptionkeys` | 
            
            {
              "cacheEncryptionKey": "CACHE_ENCRYPTION_KEY_VALUE"
              "kvmEncryptionKey": "KVM_ENCRYPTION_KEY_VALUE"
              "envKvmEncryptionKey": "ENV_KVM_ENCRYPTION_KEY_VALUE"
              "kmsEncryptionKey": "KMS_ENCRYPTION_KEY_VALUE"
            }  
  
     2. Within Vault, create policies which grant access to the secrets: 
            
            cat axhashsalt-auth-policy.txt
            path "secret/data/apigee/axhashsalt" {
              capabilities = ["read"]
            }
            cat redis-auth-policy.txt
            path "secret/data/apigee/redis" {
              capabilities = ["read"]
            }
            cat orgencryptionkeys-auth-policy.txt
            path "secret/data/apigee/orgencryptionkeys" {
              capabilities = ["read"]
            }
            cat envencryptionkeys-auth-policy.txt
            path "secret/data/apigee/envencryptionkeys" {
              capabilities = ["read"]
            }
            
            vault policy write apigee-axhashsalt-auth axhashsalt-auth-policy.txt
            vault policy write apigee-redis-auth redis-auth-policy.txt
            vault policy write apigee-orgencryptionkeys-auth orgencryptionkeys-auth-policy.txt
            vault policy write apigee-envencryptionkeys-auth envencryptionkeys-auth-policy.txt
            

     3. Create a script called `generate-encoded-sas.sh` with the following contents: 
            
            # generate-encoded-sas.sh
            
            ORG=$APIGEE_ORG            # Apigee organization name
            ENVS=$APIGEE_ENV_LIST      # comma separated env names, for example: dev,prod
            
            ORG_SHORT_NAME=$(echo $ORG | head -c 15)
            ENCODE=$(echo -n $ORG | shasum -a 256 | head -c 7)
            ORG_ENCODE=$(echo "$ORG_SHORT_NAME-$ENCODE")
            NAMES="apigee-manager,apigee-redis-default,apigee-redis-envoy-default,apigee-mart-${ORG_ENCODE},apigee-mint-task-scheduler-${ORG_ENCODE}"
            
            for ENV in ${ENVS//,/ }
            do
              ENV_SHORT_NAME=$(echo $ENV | head -c 15)
              ENCODE=$(echo -n $ORG:$ENV | shasum -a 256 | head -c 7)
              ENV_ENCODE=$(echo "$ORG_SHORT_NAME-$ENV_SHORT_NAME-$ENCODE")
              NAMES+=,apigee-runtime-${ENV_ENCODE},apigee-synchronizer-${ENV_ENCODE}
            done
            
            echo $NAMES
            

     4. Run the script to generate the service account name list to bind the policies to: 
            
            chmod +x ./generate-encoded-sas.sh
            ./generate-encoded-sas.sh
            

The output should list the encoded service account names.

     5. Using the policies, create Vault roles which bind the required Apigee service accounts. 
            
            vault write auth/kubernetes/role/apigee-axhashsalt \
            	bound_service_account_names=BOUND_SA_NAMES \
            	bound_service_account_namespaces=APIGEE_NAMESPACE \
            	policies=apigee-axhashsalt-auth \
            	ttl=1m
            
            vault write auth/kubernetes/role/apigee-redis \
            	bound_service_account_names=BOUND_SA_NAMES \
            	bound_service_account_namespaces=APIGEE_NAMESPACE \
            	policies=apigee-redis-auth \
            	ttl=1m
            
            vault write auth/kubernetes/role/apigee-orgencryptionkeys \
            	bound_service_account_names=BOUND_SA_NAMES \
            	bound_service_account_namespaces=APIGEE_NAMESPACE \
            	policies=apigee-orgencryptionkeys-auth \
            	ttl=1m
            
            vault write auth/kubernetes/role/apigee-envencryptionkeys \
            	bound_service_account_names=BOUND_SA_NAMES \
            	bound_service_account_namespaces=APIGEE_NAMESPACE \
            	policies=apigee-envencryptionkeys-auth \
            	ttl=1m
            
            

  2. Create `SecretProviderClass` objects. 
     1. Add the following secrets via the `SecretProviderClass` resources. These resources tell the CSI driver what provider to communicate with when requesting secrets. The following table shows the file names (`objectNames`) expected by Apigee hybrid: **Secret** | **Expected secret file names**  
---|---  
AX Hash Salt | 
        * `ax-hash-salt`  
Redis | 
        * `redis-password`  
Org Encryption Keys | 
        * `kmsEncryptionKey`
        * `kvmEncryptionKey`
        * `contractEncryptionKey`  
Env Encryption Keys | 
        * `kmsEncryptionKey`
        * `kvmEncryptionKey`
        * `envKvmEncryptionKey`
        * `cacheEncryptionKey`  
     2. Use the following `SecretProviderClass` templates to configure these resources: 
            
            # axhashsalt-spc.yaml
            
            apiVersion: secrets-store.csi.x-k8s.io/v1
            kind: SecretProviderClass
            metadata:
              name: apigee-axhashsalt-spc
            spec:
              provider: vault
              parameters:
                roleName: apigee-axhashsalt
                vaultAddress: VAULT_ADDRESS
                # "objectName" is an alias used within the SecretProviderClass to reference
                # that specific secret. This will also be the filename containing the secret.
                # Apigee Hybrid expects these exact values so they must not be changed.
                # "secretPath" is the path in Vault where the secret should be retrieved.
                # "secretKey" is the key within the Vault secret response to extract a value from.
                objects: |
                  - objectName: "ax-hash-salt"
                    secretPath: ""
                    secretKey: ""
            
            
            # redis-spc.yaml
            
            apiVersion: secrets-store.csi.x-k8s.io/v1
            kind: SecretProviderClass
            metadata:
              name: apigee-redis-spc
            spec:
              provider: vault
              parameters:
                roleName: apigee-redis
                vaultAddress: VAULT_ADDRESS
                # "objectName" is an alias used within the SecretProviderClass to reference
                # that specific secret. This will also be the filename containing the secret.
                # Apigee Hybrid expects these exact values so they must not be changed.
                # "secretPath" is the path in Vault where the secret should be retrieved.
                # "secretKey" is the key within the Vault secret response to extract a value from.
                objects: |
                  - objectName: "redis-password"
                    secretPath: ""
                    secretKey: ""
            
            
            # orgencryptionkeys-spc.yaml
            
            apiVersion: secrets-store.csi.x-k8s.io/v1
            kind: SecretProviderClass
            metadata:
              name: apigee-orgencryptionkeys-spc
            spec:
              provider: vault
              parameters:
                roleName: apigee-orgencryptionkeys
                vaultAddress: VAULT_ADDRESS
                # "objectName" is an alias used within the SecretProviderClass to reference
                # that specific secret. This will also be the filename containing the secret.
                # Apigee Hybrid expects these exact values so they must not be changed.
                # "secretPath" is the path in Vault where the secret should be retrieved.
                # "secretKey" is the key within the Vault secret response to extract a value from.
                objects: |
                  - objectName: "kmsEncryptionKey"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "kvmEncryptionKey"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "contractEncryptionKey"
                    secretPath: ""
                    secretKey: ""
            
            
            # envencryptionkeys-spc.yaml
            
            apiVersion: secrets-store.csi.x-k8s.io/v1
            kind: SecretProviderClass
            metadata:
              name: apigee-envencryptionkeys-spc
            spec:
              provider: vault
              parameters:
                roleName: apigee-envencryptionkeys
                vaultAddress: VAULT_ADDRESS
                # "objectName" is an alias used within the SecretProviderClass to reference
                # that specific secret. This will also be the filename containing the secret.
                # Apigee Hybrid expects these exact values so they must not be changed.
                # "secretPath" is the path in Vault where the secret should be retrieved.
                # "secretKey" is the key within the Vault secret response to extract a value from.
                objects: |
                  - objectName: "cacheEncryptionKey"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "kvmEncryptionKey"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "envKvmEncryptionKey"
                    secretPath: ""
                    secretKey: ""
                  - objectName: "kmsEncryptionKey"
                    secretPath: ""
                    secretKey: ""
            

VAULT_ADDRESS is the endpoint where your Vault server is running. If Vault is running in the same cluster and namespace as Apigee, the format will generally be `http://vault.APIGEE_NAMESPACE.svc.cluster.local:VAULT_SERVICE_PORT`. 

     3. Apply the above `SecretProviderClasses` to the `APIGEE_NAMESPACE` namespace: 
            
            kubectl -n APIGEE_NAMESPACE apply -f axhashsalt-spc.yaml
            kubectl -n APIGEE_NAMESPACE apply -f redis-spc.yaml
            kubectl -n APIGEE_NAMESPACE apply -f orgencryptionkeys-spc.yaml
            kubectl -n APIGEE_NAMESPACE apply -f envencryptionkeys-spc.yaml
            

  3. Enable the external secret for the AX Hash Salt. 
     1. Within your `overrides.yaml` file, add the following configuration to enable external secret usage for the AX Hash Salt: 
            
            axHashSaltSecretProviderClass: apigee-axhashsalt-spc

     2. Apply the change by upgrading the `org` Helm chart: 
            
            helm upgrade org apigee-org/ \
              --namespace APIGEE_NAMESPACE \
              -f overrides.yaml

  4. Enable the external secret for the Redis password. 
     1. Within your `overrides.yaml` file, add the following configuration to enable external secret usage for the Redis password: 
            
            redis:
              auth:
                secretProviderClass: apigee-redis-spc

     2. Then apply the changes by upgrading the `operator` and `redis` charts in the following order: 
            
            helm upgrade operator apigee-operator/ \
              --namespace APIGEE_NAMESPACE \
              -f overrides.yaml
            helm upgrade redis apigee-redis/ \
              --namespace APIGEE_NAMESPACE \
              -f overrides.yaml
            

  5. Enable the external secret for the encryption keys 
     1. Within your `overrides.yaml` file, add the following configuration to enable external secret usage for the org-level encryption keys: 
            
            encryptionKeySecretProviderClass: apigee-orgencryptionkeys-spc

     2. Apply change by upgrading the `org` Helm chart: 
            
            helm upgrade org apigee-org/ \
              --namespace APIGEE_NAMESPACE \
              -f overrides.yaml

     3. Within your `overrides.yaml` file for each environment, add the following configuration for the env-specific encryption keys: 
            
            envs:
            - name: ENV_NAME
              encryptionKeySecretProviderClass: apigee-envencryptionkeys-spc

     4. Apply the change by upgrading the `env` Helm chart once for each environment: 
            
            helm upgrade ENV_NAME apigee-env/ \
              --namespace APIGEE_NAMESPACE \
              --set env=ENV_NAME \
              -f overrides.yaml
            


**Note:** After completing this procedure all secrets, including Cassandra backup service account secrets and Google service account keys, may still be present in the Kubernetes secrets. You can delete these secrets from Kubernetes once they have been securely stored in Vault. 

## Rollback

### AX Hash Salt

  1. Within your `overrides.yaml` file, remove the configuration which enabled external secret usage for the AX Hash Salt: 
         
         # Comment out or delete the following line:
         # axHashSaltSecretProviderClass: apigee-axhashsalt-spc

  2. Apply the change by upgrading the `org` Helm chart: 
         
         helm upgrade org apigee-org/ \
           --namespace APIGEE_NAMESPACE \
           -f overrides.yaml




### Redis password

  1. Within your `overrides.yaml` file, remove the configuration which enabled external secret usage for the Redis password: 
         
         redis:
           auth:
           # Comment out or delete the following line:
           # secretProviderClass: apigee-redis-spc

  2. Then apply the changes by upgrading the `redis` and `operator` charts in the following order: 
         
         helm upgrade redis apigee-redis/ \
           --namespace APIGEE_NAMESPACE \
           -f overrides.yaml
         helm upgrade operator apigee-operator/ \
           --namespace APIGEE_NAMESPACE \
           -f overrides.yaml
         




### Encryption keys

  1. Within your `overrides.yaml` file, remove the configuration which enabled external secret usage for the env encryption keys: 
         
         envs:
           - name: ENV_NAME
           # Comment out or delete the following line:
           # encryptionKeySecretProviderClass: apigee-envencryptionkeys-spc

  2. Apply the change by upgrading the `env` Helm chart once for each environment: 
         
         helm upgrade ENV_NAME apigee-env/ \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f overrides.yaml
         

  3. Within your `overrides.yaml` file, remove the configuration which enabled external secret usage for the org encryption keys: 
         
         # Comment out or delete the following line:
         # encryptionKeySecretProviderClass: apigee-orgencryptionkeys-spc
         

  4. And then Upgrade the `org` Helm chart: 
         
         helm upgrade org apigee-org/ \
           --namespace APIGEE_NAMESPACE \
           -f overrides.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
