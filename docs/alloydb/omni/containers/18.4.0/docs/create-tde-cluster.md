---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/create-tde-cluster/
title: Create a TDE-enabled cluster \u00a0|\u00a0 AlloyDB Omni using containers: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:18:38.944135+00:00
---

# Create a TDE-enabled cluster  |  AlloyDB Omni using containers: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/create-tde-cluster/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/overview)



Send feedback 

#  Create a TDE-enabled cluster Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/create-tde-cluster)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/create-tde-cluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/create-tde-cluster)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/create-tde-cluster)



You can secure your data at rest and protect sensitive information by enabling transparent data encryption (TDE) in AlloyDB Omni. This document describes how to create a TDE-enabled cluster by providing required Key Management Service (KMS) environment variables (for HashiCorp Vault or Thales CipherTrust Manager) and the `--tde-kek-url` flag in the `POSTGRES_INITDB_ARGS` environment variable during database initialization.

## Before you begin

### HashiCorp Vault KMS

  * [Configure HashiCorp Vault's KV-V2 secrets engine](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) to ensure that the Key Encryption Key (KEK) path and [JSON Web Token (JWT)](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication) are available.
  * Verify that AlloyDB Omni has permission to read the JSON Web Token (JWT) file, which is the authentication token.



### Thales CipherTrust KMS

  * Configure [Thales CipherTrust Manager](https://cpl.thalesgroup.com/encryption/ciphertrust-manager) to ensure that your secret Key Encryption Key (KEK) is created and exportable.
  * Verify that you have a CipherTrust Manager user account (`username` and `password`) with permission to authenticate and export the KEK secret.



## Create the cluster

To create a TDE-enabled cluster, you must pass the necessary Key Management Service (KMS) configuration and authentication credentials during the initialization of the database. Follow the instructions in either the HashiCorp Vault KMS section (using `jwt` authentication) or the Thales CipherTrust KMS section (using username and password authentication).

### HashiCorp Vault KMS

Select the tab for your container runtime to initialize AlloyDB Omni with HashiCorp Vault.

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v VAULT_CERT_PATH_ON_DISK:VAULT_CERT_PATH \
    -e VAULT_AUTH_TYPE=jwt \
    -e VAULT_AUTH_MOUNT=JWT_AUTH_ENGINE_MOUNT \
    -e VAULT_JWT_PATH=JWT_FILE_PATH \
    -e VAULT_ROLE=VAULT_ROLE \
    -e VAULT_CERT_PATH=VAULT_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v VAULT_CERT_PATH_ON_DISK:VAULT_CERT_PATH \
    -e VAULT_AUTH_TYPE=jwt \
    -e VAULT_AUTH_MOUNT=JWT_AUTH_ENGINE_MOUNT \
    -e VAULT_JWT_PATH=JWT_FILE_PATH \
    -e VAULT_ROLE=VAULT_ROLE \
    -e VAULT_CERT_PATH=VAULT_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v VAULT_CERT_PATH_ON_DISK:VAULT_CERT_PATH \
    -e VAULT_AUTH_TYPE=jwt \
    -e VAULT_AUTH_MOUNT=JWT_AUTH_ENGINE_MOUNT \
    -e VAULT_JWT_PATH=JWT_FILE_PATH \
    -e VAULT_ROLE=VAULT_ROLE \
    -e VAULT_CERT_PATH=VAULT_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v VAULT_CERT_PATH_ON_DISK:VAULT_CERT_PATH \
    -e VAULT_AUTH_TYPE=jwt \
    -e VAULT_AUTH_MOUNT=JWT_AUTH_ENGINE_MOUNT \
    -e VAULT_JWT_PATH=JWT_FILE_PATH \
    -e VAULT_ROLE=VAULT_ROLE \
    -e VAULT_CERT_PATH=VAULT_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

Replace the following:

  * `CONTAINER_NAME`: the name of the container to create. For example, `alloydb-tde`.
  * `DATA_DIR`: the local directory to mount as the data volume for AlloyDB Omni. For example, `/local/data`.
  * `JWT_AUTH_ENGINE_MOUNT`: path where the HashiCorp Vault authentication engine is mounted. For example, `/auth/jwt`.
  * `JWT_FILE_PATH`: path where the Vault JWT is stored on your nodes. For example, `/tde-tls/jwt-token`.
  * Optional: `VAULT_ROLE`: the client role defined in your Vault setup that lets HashiCorp Vault verify the JWT token authenticity.
  * `VAULT_CERT_PATH_ON_DISK`: path to Vault certificates on the host machine. For example, `/local/vault/config`.
  * `VAULT_CERT_PATH`: path where the certificates for the Vault connection are located in your container. For example, `/tde-tls`. If not set, the certificates in the default trust store are used.
  * `KEK_URL`: The fully qualified URL to the KEK in HashiCorp Vault. Use `vault` as the protocol to specify HashiCorp Vault as the KMS provider—for example, `vault://127.0.0.1:8200/v1/secret/data/alloydb_kek`.
  * `IMAGE_TAG`: Use `18.4.0` for the latest Debian image or `18.4.0-ubi` for the latest UBI image.



### Thales CipherTrust KMS

Select the tab for your container runtime to initialize AlloyDB Omni with Thales CipherTrust Manager.

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v CIPHERTRUST_CERT_PATH_ON_DISK:CIPHERTRUST_CERT_PATH \
    -e CIPHERTRUST_USER=CIPHERTRUST_USERNAME \
    -e CIPHERTRUST_PASSWORD=CIPHERTRUST_PASSWORD \
    -e CIPHERTRUST_CERT_PATH=CIPHERTRUST_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v CIPHERTRUST_CERT_PATH_ON_DISK:CIPHERTRUST_CERT_PATH \
    -e CIPHERTRUST_USER=CIPHERTRUST_USERNAME \
    -e CIPHERTRUST_PASSWORD=CIPHERTRUST_PASSWORD \
    -e CIPHERTRUST_CERT_PATH=CIPHERTRUST_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v CIPHERTRUST_CERT_PATH_ON_DISK:CIPHERTRUST_CERT_PATH \
    -e CIPHERTRUST_USER=CIPHERTRUST_USERNAME \
    -e CIPHERTRUST_PASSWORD=CIPHERTRUST_PASSWORD \
    -e CIPHERTRUST_CERT_PATH=CIPHERTRUST_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    --network host \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v CIPHERTRUST_CERT_PATH_ON_DISK:CIPHERTRUST_CERT_PATH \
    -e CIPHERTRUST_USER=CIPHERTRUST_USERNAME \
    -e CIPHERTRUST_PASSWORD=CIPHERTRUST_PASSWORD \
    -e CIPHERTRUST_CERT_PATH=CIPHERTRUST_CERT_PATH \
    -e POSTGRES_INITDB_ARGS=" \
    --tde-kek-url=KEK_URL" \
    google/alloydbomni:IMAGE_TAG

Replace the following:

  * `CONTAINER_NAME`: the name of the container to create. For example, `alloydb-tde`.
  * `DATA_DIR`: the local directory to mount as the data volume for AlloyDB Omni. For example, `/local/data`.
  * `CIPHERTRUST_USERNAME`: the username used to authenticate with Thales CipherTrust Manager.
  * `CIPHERTRUST_PASSWORD`: the password for the Thales CipherTrust Manager user.
  * `CIPHERTRUST_CERT_PATH_ON_DISK`: path to CipherTrust Manager TLS certificates on the host machine. For example, `/local/ciphertrust/certs`.
  * `CIPHERTRUST_CERT_PATH`: path where the certificates for the CipherTrust Manager connection (`ca.crt`, `tls.crt`, and `tls.key`) are located in your container. For example, `/tde-tls`. If not set, the certificates in the default trust store are used.
  * `KEK_URL`: The fully qualified URL to the KEK in Thales CipherTrust Manager. Use `ciphertrust` as the protocol to specify Thales CipherTrust Manager as the KMS provider—for example, `ciphertrust://10.0.0.1:443/api/v1/vault/secrets/alloydb_kek`.
  * `IMAGE_TAG`: Use `18.4.0` for the latest Debian image or `18.4.0-ubi` for the latest UBI image.



To enable TDE for columnar engine cache data spilled to SSD storage, connect to your database instance and run the following query:
    
    
    ALTER SYSTEM SET google_columnar_engine.enable_tde_for_storage_cache = 'on';
    

Restart your database server for the changes to take effect.

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
