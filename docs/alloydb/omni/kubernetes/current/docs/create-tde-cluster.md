---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/create-tde-cluster/
title: Create a TDE-enabled cluster \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:37:16.259457+00:00
---

# Create a TDE-enabled cluster  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/create-tde-cluster/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Create a TDE-enabled cluster Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/create-tde-cluster)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/create-tde-cluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/create-tde-cluster)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/create-tde-cluster)



The AlloyDB Omni Kubernetes operator automates the lifecycle of transparent data encryption (TDE) clusters using the `TdeConfig` custom resource. This resource stores Key Management Service (KMS) connection details for HashiCorp Vault or Thales CipherTrust Manager, enabling the operator to securely inject required credentials into database pods.

## Before you begin

### HashiCorp Vault KMS

  * [Configure HashiCorp Vault's KV-V2 secrets engine](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) to ensure that the Key Encryption Key (KEK) path and [JSON Web Token (JWT)](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication) are available.
  * Verify that AlloyDB Omni has permission to read the JSON Web Token (JWT) file, which is the authentication token.
  * Optional: To deploy a TDE-enabled cluster on OpenShift, grant the `hostmount-anyuid` Security Context Constraint (SCC) to the `DBCluster` service account running the database cluster.
        
        oc adm policy add-scc-to-user hostmount-anyuid -z DBCLUSTER_NAME-sa -n DBCLUSTER_NAMESPACE

Replace DBCLUSTER_NAME with the name of the `DBCluster` and DBCLUSTER_NAMESPACE with the namespace where you want to create the `DBCluster` resource.




### Thales CipherTrust KMS

  * Configure [Thales CipherTrust Manager](https://cpl.thalesgroup.com/encryption/ciphertrust-manager) to ensure that your secret Key Encryption Key (KEK) is created and exportable.
  * Verify that you have a CipherTrust Manager user account (`username` and `password`) with permission to authenticate and export the KEK secret.
  * Optional: To deploy a TDE-enabled cluster on OpenShift, grant the `hostmount-anyuid` Security Context Constraint (SCC) to the `DBCluster` service account running the database cluster.
        
        oc adm policy add-scc-to-user hostmount-anyuid -z DBCLUSTER_NAME-sa -n DBCLUSTER_NAMESPACE

Replace DBCLUSTER_NAME with the name of the `DBCluster` and DBCLUSTER_NAMESPACE with the namespace where you want to create the `DBCluster` resource.




## Configure KMS access

Create the Kubernetes `ConfigMap` and `Secret` resources that contain your KEK path and KMS authentication credentials. Make sure to create these resources in the same namespace where you plan to deploy your `DBCluster`.

### HashiCorp Vault KMS

Create a `ConfigMap` resource that contains your KEK URL and the host path to your JWT token:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: CONFIG_MAP_NAME
    data:
      kek_url: "KEK_URL"
      token_path: "JWT_TOKEN_PATH"

Replace the following:

  * `CONFIG_MAP_NAME`: name of the ConfigMap. The values defined in `kek_url` and `token_path` are used in the `TdeConfig` resource definition.
  * `KEK_URL`: the fully qualified URL to the KEK in HashiCorp Vault. Use `vault` as the protocol to specify HashiCorp Vault as the KMS provider—for example, `vault://vault.default.svc:8200/v1/secret/data/alloydb_kek`.
  * `JWT_TOKEN_PATH`: path to the JWT token on the node—for example, `/tmp/token`. The JWT token access path must be consistent across all nodes in the cluster.



### Thales CipherTrust KMS

Create a `ConfigMap` resource that contains your KEK URL and a `Secret` resource that contains your Thales CipherTrust Manager authentication credentials:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: CONFIG_MAP_NAME
    data:
      kek_url: "KEK_URL"
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: CREDENTIALS_SECRET_NAME
    type: Opaque
    stringData:
      username: "CIPHERTRUST_USERNAME"
      password: "CIPHERTRUST_PASSWORD"

Replace the following:

  * `CONFIG_MAP_NAME`: name of the ConfigMap. The value defined in `kek_url` is used in the `TdeConfig` resource definition.
  * `KEK_URL`: the fully qualified URL to the KEK in Thales CipherTrust Manager. Use `ciphertrust` as the protocol to specify Thales CipherTrust Manager as the KMS provider—for example, `ciphertrust://ciphertrust.default.svc:443/api/v1/vault/secrets/alloydb_kek`.
  * `CREDENTIALS_SECRET_NAME`: name of the Kubernetes Secret that stores your CipherTrust Manager credentials—for example, `ciphertrust-credentials`.
  * `CIPHERTRUST_USERNAME`: the username used to authenticate with Thales CipherTrust Manager.
  * `CIPHERTRUST_PASSWORD`: the password for the Thales CipherTrust Manager user.



## Create a TLS secret

To create a TLS secret to store the certificates for verifying your KMS server connection (HashiCorp Vault or Thales CipherTrust Manager), run the following commands:
    
    
    kubectl create secret tls TLS_SECRET_NAME \
        --cert=CLIENT_CERT_FILE \
        --key=CLIENT_KEY_FILE
    
    kubectl patch secret TLS_SECRET_NAME \
        -p '{"data":{"ca.crt":"'$(base64 -w 0 CA_CERT_FILE)'"}}' \
        --type=merge
    

Replace the following:

  * `TLS_SECRET_NAME`: a name for the TLS secret (for example, `vault-secret` or `ciphertrust-tls-secret`). You use this secret name when you create the `TdeConfig` custom resource.
  * `CLIENT_CERT_FILE`: the path to your client TLS certificate file (stored as `tls.crt` in the secret).
  * `CLIENT_KEY_FILE`: the path to your client TLS private key file (stored as `tls.key` in the secret).
  * `CA_CERT_FILE`: the path to the Certificate Authority (CA) certificate file used to verify the KMS server certificate (stored as `ca.crt` in the secret).



## Create the TdeConfig custom resource

Create a `TdeConfig` resource that defines how AlloyDB Omni communicates with your external KMS provider to retrieve the KEK. Make sure that you create the `TdeConfig` resource in the same namespace as the `DBCluster` resource.

Ensure that your KMS instance is reachable over the network from your database pods.

### HashiCorp Vault KMS

Ensure that the path to your JWT token on the host node is accessible to the `postgres` user. Create and apply a manifest for the `TdeConfig` resource:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: TdeConfig
    metadata:
      name: TDE_CONFIG_NAME
    spec:
      kekUrlRef:
        name: CONFIG_MAP_NAME
        key: kek_url
      kmsProvider:
        vault:
          authType: "jwt"
          authMount: "JWT_AUTH_MOUNT_PATH"
          jwt:
            pathRef:
              name: "CONFIG_MAP_NAME"
              key: "token_path"
            role: "VAULT_ROLE"
      tls:
        certSecret:
          name: "TLS_SECRET_NAME"

Replace the following:

  * `TDE_CONFIG_NAME`: name of the `TdeConfig` resource.
  * `CONFIG_MAP_NAME`: name of the ConfigMap created in the previous step.
  * `JWT_AUTH_MOUNT_PATH`: path where the authentication engine is mounted within HashiCorp Vault, as defined by your configuration—for example, `auth/kms`.
  * Optional: `VAULT_ROLE`: the client role defined in your Vault setup. The client role validates the JWT and reflects the specific access rights and identity the role is granted within HashiCorp Vault.
  * `TLS_SECRET_NAME`: name of the secret that contains the TLS certificates for the Vault connection—for example, `vault-secret`.



### Thales CipherTrust KMS

Create and apply a manifest for the `TdeConfig` resource using the `ciphertrust` provider:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: TdeConfig
    metadata:
      name: TDE_CONFIG_NAME
    spec:
      kekUrlRef:
        name: CONFIG_MAP_NAME
        key: kek_url
      kmsProvider:
        ciphertrust:
          authType: "password"
          credentialsSecretRef:
            name: "CREDENTIALS_SECRET_NAME"
      tls:
        certSecret:
          name: "TLS_SECRET_NAME"

Replace the following:

  * `TDE_CONFIG_NAME`: name of the `TdeConfig` resource.
  * `CONFIG_MAP_NAME`: name of the ConfigMap containing `kek_url`.
  * `CREDENTIALS_SECRET_NAME`: name of the Kubernetes Secret containing your CipherTrust Manager `username` and `password` keys—for example, `ciphertrust-credentials`.
  * `TLS_SECRET_NAME`: name of the secret that contains the TLS certificates for the CipherTrust Manager connection—for example, `ciphertrust-tls-secret`.



## Deploy the DBCluster

  1. Create and apply a manifest to create a `DBCluster` resource that references your `TdeConfig` resource. For more information about creating a database cluster, see [Create a database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create).
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: "DBCLUSTER_NAME"
         spec:
           databaseVersion: "18.4.0"
           primarySpec:
             features:
               transparentDataEncryption:
                 tdeConfigRef:
                   name: "TDE_CONFIG_NAME"
         
         [...]
         

Replace `TDE_CONFIG_NAME` with the name of your `TdeConfig` resource and `DBCLUSTER_NAME` with the name of the `DBCluster` you want to create.

  2. Optional: If you're deploying `DBCluster` in an OpenShift environment, you need to annotate the `DBCluster` resource with the `hostmount-anyuid` annotation.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog DBCLUSTER_NAME -n DBCLUSTER_NAMESPACE openshift.io/scc=anyuid
         

Replace `DBCLUSTER_NAME` with the name of your `DBCluster` resource and `DBCLUSTER_NAMESPACE` with the namespace where you want to create the `DBCluster` resource.




To enable TDE for columnar cache spilled to SSD, patch your DBCluster as follows:
    
    
    kubectl patch dbcluster DBCLUSTER_NAME \
      -n DBCLUSTER_NAMESPACE \
      -p '{"spec":{"primarySpec":{"parameters": {"google_columnar_engine.enable_tde_for_storage_cache": "on"}}}}' \
      --type=merge
    

## TDE metrics reference

You can view all TDE metrics in AlloyDB Omni's monitoring agent. The following table describes each metric.

Name | Description | Label | Unit | Type  
---|---|---|---|---  
`alloydb_omni_database_tde_data_blocks_decrypted_count_total` | Number of data blocks decrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_data_blocks_encrypted_count_total` | Number of data blocks encrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_data_decryption_time_us_total` | Total time spent in data block decryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_data_encryption_time_us_total` | Total time spent in data block encryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_enabled` | TDE enabled status. | Not applicable |  | gauge  
`alloydb_omni_database_tde_kek_info` | TDE KEK information. | 

  * `kek_version`: Version of the KEK in use for key wrapping.
  * `kek_url`: Fully qualified path to KEK in KMS.
  * `kek_creation_timestamp`: Creation time of the KEK version in use.

|  | gauge  
`alloydb_omni_database_tde_temp_blocks_decrypted_count_total` | Number of temporary blocks decrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_temp_blocks_encrypted_count_total` | Number of temporary blocks encrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_temp_decryption_time_us_total` | Total time spent in temporary block decryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_temp_encryption_time_us_total` | Total time spent in temporary block encryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_wal_blocks_decrypted_count_total` | Number of WAL blocks decrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_wal_blocks_encrypted_count_total` | Number of WAL blocks encrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_wal_decryption_time_us_total` | Total time spent in WAL block decryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_wal_encryption_time_us_total` | Total time spent in WAL block encryption. | Not applicable | microseconds | counter  
`tde_chill_cache_blocks_encrypted` | Number of chill cache blocks encrypted. | Not applicable |  | counter  
`tde_chill_cache_blocks_decrypted` | Number of chill cache blocks decrypted. | Not applicable |  | counter  
`tde_chill_cache_blocks_total_encryption_time_us` | Total time spent in chill cache block encryption. | Not applicable | microseconds | counter  
`tde_chill_cache_blocks_total_decryption_time_us` | Total time spent in chill cache block decryption. | Not applicable | microseconds | counter  
`tde_ce_cache_ssd_blocks_encrypted` | Number of columnar cache blocks spilled to SSD storage that were encrypted. | Not applicable |  | counter  
`tde_ce_cache_ssd_blocks_decrypted` | Number of columnar cache blocks spilled to SSD storage that were decrypted. | Not applicable |  | counter  
`tde_ce_cache_ssd_blocks_total_encryption_time_us` | Total time spent encrypting columnar cache blocks spilled to SSD storage. | Not applicable | microseconds | counter  
`tde_ce_cache_ssd_blocks_total_decryption_time_us` | Total time spent decrypting columnar cache blocks spilled to SSD storage. | Not applicable | microseconds | counter  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
