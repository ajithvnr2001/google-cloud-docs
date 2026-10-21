---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/create-tde-cluster/
title: Create a TDE-enabled cluster \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:05:35.250814+00:00
---

# Create a TDE-enabled cluster  |  AlloyDB Omni using RPM: 18.1.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/create-tde-cluster/

This page documents AlloyDB Omni version **18.1.1** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/overview)



Send feedback 

#  Create a TDE-enabled cluster Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Select a documentation version: 18.1.1keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/create-tde-cluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/create-tde-cluster)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/create-tde-cluster)



## Before you begin

  * Read [Plan your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/plan-installation-linux).


  * [Configure HashiCorp Vault's KV-V2 secrets engine](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) to make sure that the Key Encryption Key (KEK) path and [JSON Web Token (JWT)](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication) are available.

  * Verify that AlloyDB Omni has permission to read the JWT token file.




## Create the cluster

To create a TDE-enabled cluster, you must pass the necessary Key Management Service (KMS) configuration and authentication credentials during the initialization of the database. The only supported authentication type is `jwt`.

  1. [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/18-next/docs/deploy-vm) to prepare your environment and install the AlloyDB Omni RPM package.

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
            /usr/lib/postgresql/18/bin/alloydbomni18-setup initdb

Replace the following:

        * `POSTGRES_PASSWORD`: the password for the database user.
        * `DATA_DIR`: the local directory to mount as the data volume for AlloyDB Omni—for example, `/local/data`.
        * `VAULT_AUTH_TYPE`: the type of authentication to use for the vault connection. Only `jwt` is supported.
        * `JWT_AUTH_ENGINE_MOUNT`: the path where the HashiCorp Vault authentication engine is mounted—for example, `/auth/jwt`.
        * `JWT_FILE_PATH`: the path where vault JWT is stored on your nodes—for example, `tde-tls/jwt-token`.
        * (Optional) `VAULT_ROLE`: the client role defined in your vault setup that lets HashiCorp Vault verify the JWT token authenticity.
        * `VAULT_CERT_PATH`: the path where the certificates for the vault connection are located in your container—for example, `/tde-tls`. If not set, the certificates in the default trust store are used.
        * `KEK_URL`: the fully qualified URL to the KEK in HashiCorp Vault. Use `vault` as the protocol to specify HashiCorp Vault as the KMS provider—for example, `vault://127.0.0.1:8200/v1/secrets/data/alloydb_kek`.
     2. To create an override file for `alloydbomni.service in /etc/systemd/system/alloydbomni18.service.d/override.conf`, add the following to the `override.conf` file:
            
            [Service]
            Environment="VAULT_AUTH_TYPE"
            Environment="VAULT_AUTH_MOUNT=JWT_AUTH_ENGINE_MOUNT"
            Environment="VAULT_JWT_PATH=JWT_FILE_PATH"
            Environment="VAULT_ROLE=VAULT_ROLE"
            Environment="VAULT_CERT_PATH=VAULT_CERT_PATH"

     3. To apply the changes, reload the systemd daemon.
            
            sudo systemctl daemon-reload

### File Based KMS

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
            /usr/lib/postgresql/18/bin/alloydbomni18-setup initdb

Replace the following:

        * `POSTGRES_PASSWORD`: the password for the database user.
        * `DATA_DIR`: the local directory to mount as the data volume for AlloyDB Omni—for example, `/local/data`.
        * `KEK_DIR`: the directory where the local file-based KEK is stored—for example, `/tmp/alloydb/kms`.

  3. After the database is initialized, follow the instructions in [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/18-next/docs/deploy-vm) to prepare the database, set up the host, and start the `systemd` service. 




## View TDE metrics

After the cluster is initialized, complete the following steps to verify that TDE is enabled and view related TDE metrics.

  1. Connect to your database using `psql` or your preferred client. For detailed instructions on connecting to your instances, see [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/run-connect).
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
