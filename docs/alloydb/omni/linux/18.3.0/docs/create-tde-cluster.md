---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/create-tde-cluster/
title: Create a TDE-enabled cluster \u00a0|\u00a0 AlloyDB Omni using RPM: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T06:00:06.935394+00:00
---

# Create a TDE-enabled cluster  |  AlloyDB Omni using RPM: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/create-tde-cluster/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)



Send feedback 

#  Create a TDE-enabled cluster Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/create-tde-cluster)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/create-tde-cluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/create-tde-cluster)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/create-tde-cluster)



You can secure your data at rest and protect sensitive information by enabling transparent data encryption (TDE) in AlloyDB Omni. This document describes how to create a TDE-enabled cluster by providing required vault environment variables and the `--tde-kek-url` flag in the `POSTGRES_INITDB_ARGS` environment variable during database initialization.

## Before you begin

  * Read [Plan your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/plan-installation-linux).
  * When you plan your AlloyDB Omni deployment with TDE enabled, be sure to account for additional CPU usage based on your anticipated workload and data volume. Encryption and decryption are compute-intensive operations.


  * [Configure HashiCorp Vault's KV-V2 secrets engine](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) to ensure that the Key Encryption Key (KEK) path and [JSON Web Token (JWT)](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication) are available.
  * Verify that AlloyDB Omni has permission to read the JSON Web Token (JWT) file, which is the authentication token.



## Create the cluster

To create a TDE-enabled cluster, you must pass the necessary Key Management Service (KMS) configuration and authentication credentials during the initialization of the database. The only supported authentication type is `jwt`.

  1. [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/deploy-vm) to prepare your environment and install the AlloyDB Omni RPM package.

**Note:** Don't initialize the database yet.
  2. Initialize the database.

**Note:** AlloyDB Omni also supports File Based KMS. However, we recommend this for testing purposes only, and not for production workloads.

### HashiCorp Vault KMS

Use this approach for production workloads.

     1. Run the following command to initialize the database with TDE enabled:
            
            sudo PGPASSWORD=POSTGRES_PASSWORD \
            PGDATA=DATA_DIR \
            VAULT_AUTH_TYPE=jwt \
            VAULT_AUTH_MOUNT=JWT_AUTH_ENGINE_MOUNT \
            VAULT_JWT_PATH=JWT_FILE_PATH \
            VAULT_ROLE=VAULT_ROLE \
            VAULT_CERT_PATH=VAULT_CERT_PATH \
            POSTGRES_INITDB_ARGS="--tde-kek-url=KEK_URL" \
            /usr/lib/postgresql/18/bin/alloydbomniproduct_major_version_numeric-setup initdb

Replace the following:

        * `POSTGRES_PASSWORD`: the password for the database user.
        * `DATA_DIR`: the local directory to mount as the data volume for AlloyDB Omni—for example, `/local/data`.
        * `JWT_AUTH_ENGINE_MOUNT`: the path where the HashiCorp Vault authentication engine is mounted—for example, `/auth/jwt`.
        * `JWT_FILE_PATH`: the path where vault JWT is stored on your nodes—for example, `tde-tls/jwt-token`.
        * (Optional) `VAULT_ROLE`: the client role defined in your vault setup that lets HashiCorp Vault verify the JWT token authenticity.
        * `VAULT_CERT_PATH`: the path where the certificates for the vault connection are located on your nodes—for example, `/tde-tls`. If not set, the certificates in the default trust store are used.
        * `KEK_URL`: the fully qualified URL to the KEK in HashiCorp Vault. Use `vault` as the protocol to specify HashiCorp Vault as the KMS provider—for example, `vault://127.0.0.1:8200/v1/secrets/data/alloydb_kek`.
     2. To create an override file for `alloydbomni18.service` in `/etc/systemd/system/alloydbomni18.service.d/override.conf`, add the following to the `override.conf` file:
            
            [Service]
            Environment="VAULT_AUTH_TYPE=VAULT_AUTH_TYPE"
            Environment="VAULT_AUTH_MOUNT=JWT_AUTH_ENGINE_MOUNT"
            Environment="VAULT_JWT_PATH=JWT_FILE_PATH"
            Environment="VAULT_ROLE=VAULT_ROLE"
            Environment="VAULT_CERT_PATH=VAULT_CERT_PATH"

Replace the following:

        * `VAULT_AUTH_TYPE`: the type of authentication to use for the vault connection. Only `jwt` is supported.
        * `JWT_AUTH_ENGINE_MOUNT`: the path where the HashiCorp Vault authentication engine is mounted—for example, `/auth/jwt`.
        * `JWT_FILE_PATH`: the path where vault JWT is stored on your nodes—for example, `tde-tls/jwt-token`.
        * (Optional) `VAULT_ROLE`: the client role defined in your vault setup that lets HashiCorp Vault verify the JWT token authenticity.
        * `VAULT_CERT_PATH`: the path where the certificates for the vault connection are located on your nodes—for example, `/tde-tls`. If not set, the certificates in the default trust store are used.
     3. To apply the changes, reload the systemd daemon.
            
            sudo systemctl daemon-reload

### File-based KMS

Use this approach for testing purposes only.

To test TDE locally using a file-based key, you must first generate a 32 byte KEK on your machine.

     1. Create the directory, generate the key, and set the appropriate permissions.
            
            KEK_DIR=KEK_DIR
            mkdir -p $KEK_DIR
            sudo chown 999:999 $KEK_DIR
            openssl rand -base64 32 | sudo tee $KEK_DIR/key
            sudo chmod 0755 $KEK_DIR/key

     2. Initialize the database by passing the local file URI as your KEK URL.
            
            sudo PGPASSWORD=POSTGRES_PASSWORD \
            PGDATA=DATA_DIR \
            POSTGRES_INITDB_ARGS="--tde-kek-url=file:///$KEK_DIR/key" \
            /usr/lib/postgresql/18/bin/alloydbomniproduct_major_version_numeric-setup initdb

Replace the following:

        * `POSTGRES_PASSWORD`: the password for the database user.
        * `DATA_DIR`: the local directory to mount as the data volume for AlloyDB Omni—for example, `/local/data`.
        * `KEK_DIR`: the directory where the local file-based KEK is stored—for example, `/tmp/alloydb/kms`.

  3. After the database is initialized, follow the instructions in [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/deploy-vm) to prepare the database, set up the host, and start the `systemd` service.

  4. To enable TDE for columnar engine cache data spilled to SSD storage, connect to your database instance and run the following query:
         
         ALTER SYSTEM SET google_columnar_engine.enable_tde_for_storage_cache = 'on';
         

  5. Restart your database server for the changes to take effect.




## TDE metrics references

You can view all TDE metrics in AlloyDB Omni's monitoring agent. The following table describes each metric.

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

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
