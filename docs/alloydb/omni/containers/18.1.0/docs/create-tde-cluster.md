---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/create-tde-cluster/
title: Create a TDE-enabled cluster \u00a0|\u00a0 AlloyDB Omni using containers: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:07.136785+00:00
---

# Create a TDE-enabled cluster  |  AlloyDB Omni using containers: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/create-tde-cluster/

This page documents AlloyDB Omni version **18.1.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)



Send feedback 

#  Create a TDE-enabled cluster Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/create-tde-cluster)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/create-tde-cluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/create-tde-cluster)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/create-tde-cluster)



To enable Transparent Data Encryption (TDE), you must provide the required vault environment variables and include the `--tde-kek-url` flag within the `POSTGRES_INITDB_ARGS`.

## Before you begin

  * [Configure HashiCorp Vault's KV-V2 secrets engine](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) to ensure that the Key Encryption Key (KEK) path and [JSON Web Token (JWT)](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication) is available.
  * Ensure that AlloyDB Omni has permission to read the JWT token file. 



## Create the cluster

To create a TDE-enabled cluster, you must pass the necessary Key Management Service (KMS) configuration and authentication credentials during the initialization of the database. The only supported authentication type is `jwt`.

Select the tab for your container runtime.

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
  * `VAULT_AUTH_TYPE`: the type of authentication to use for the vault connection. Only `jwt` is supported.
  * `JWT_AUTH_ENGINE_MOUNT`: path where the HashiCorp Vault authentication engine is mounted. For example, `/auth/jwt`.
  * `JWT_FILE_PATH`: path where vault JWT is stored on your nodes. For example, `tde-tls/jwt-token`.
  * (Optional) `VAULT_ROLE`: the client role defined in your vault setup that lets HashiCorp Vault verify the JWT token authenticity.
  * `VAULT_CERT_PATH_ON_DISK`: path to vault certs on host machine. For example, `/local/vault/config`.
  * `VAULT_CERT_PATH`: path where the certificates for the vault connection are located in your container. For example, `/tde-tls`. If not set, the certificates in the default trust store are used.
  * `KEK_URL`: The fully qualified URL to the KEK in HashiCorp Vault. Use `vault` as the protocol to specify HashiCorp Vault as the KMS provider—for example, `vault://127.0.0.1:8200/v1/secrets/data/alloydb_kek`.
  * `IMAGE_TAG`: Use `18.1.0` for the latest Debian image or `18.1.0-ubi` for the latest UBI image.



## View TDE metrics

After the cluster is initialized, complete the following steps to verify that TDE is enabled and view related TDE metrics.

  1. Connect to your database using `psql` or your preferred client. For detailed instructions on connecting to your instances, see [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/run-connect).
  2. Run the following command:
         
         select * FROM pgsnap.g$tde_stats;
         

If TDE is enabled successfully, the output shows TDE metrics such as whether TDE is enabled, the KEK URL, KEK version, and KEK creation timestamp.

The following table explains what each metric means.

Name | Description | Label | Unit | Type  
---|---|---|---|---  
`alloydb_omni_database_tde_data_blocks_decrypted_count_total` | Number of data blocks decrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_data_blocks_encrypted_count_total` | Number of data blocks encrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_data_decryption_time_us_total` | Total time spent in data block decryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_data_encryption_time_us_total` | Total time spent in data block encryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_enabled` | TDE enabled status. | Not applicable |  | gauge  
`alloydb_omni_database_tde_kek_info` | TDE KEK information. | 
     * `kek_version`: Version of the KEK  
in use for key wrapping.
     * `kek_url`: Fully qualified path  
to KEK in KMS
     * `kek_creation_timestamp`:   
Creation time of the KEK version in use.
|  | gauge  
`alloydb_omni_database_tde_temp_blocks_decrypted_count_total` | Number of temporary blocks decrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_temp_blocks_encrypted_count_total` | Number of temporary blocks encrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_temp_decryption_time_us_total` | Total time spent in temporary block decryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_temp_encryption_time_us_total` | Total time spent in temporary block encryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_wal_blocks_decrypted_count_total` | Number of WAL blocks decrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_wal_blocks_encrypted_count_total` | Number of WAL blocks encrypted. | Not applicable |  | counter  
`alloydb_omni_database_tde_wal_decryption_time_us_total` | Total time spent in WAL block decryption. | Not applicable | microseconds | counter  
`alloydb_omni_database_tde_wal_encryption_time_us_total` | Total time spent in WAL block encryption. | Not applicable | microseconds | counter  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
