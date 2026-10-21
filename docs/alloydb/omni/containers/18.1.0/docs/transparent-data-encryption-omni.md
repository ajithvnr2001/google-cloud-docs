---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/transparent-data-encryption-omni/
title: Transparent Data Encryption (TDE) for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:23:49.775404+00:00
---

# Transparent Data Encryption (TDE) for AlloyDB Omni  |  AlloyDB Omni using containers: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/transparent-data-encryption-omni/

This page documents AlloyDB Omni version **18.1.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)



Send feedback 

#  Transparent Data Encryption (TDE) for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/transparent-data-encryption-omni)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/transparent-data-encryption-omni)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/transparent-data-encryption-omni)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/transparent-data-encryption-omni)

Transparent Data Encryption (TDE) lets you secure all data at rest in your AlloyDB Omni clusters without modifying your application code. By enabling this feature, you ensure that tables, indexes, and write-ahead logs (WAL) are automatically encrypted before being written to disk. This helps you meet compliance requirements and protect sensitive information. 

The encryption is transparent because SQL queries, DDL, and DML operations function normally without requiring application changes. Data is automatically encrypted before being written to disk and decrypted when read into memory.

**Note:** Though major version upgrades aren't supported, minor version upgrades are supported for TDE-enabled clusters.

## Key hierarchy

AlloyDB Omni implements a two-tier key hierarchy that maintains a strict separation of duties between the database and the user-managed security infrastructure.

  * Data Encryption Keys (DEKs): generated and owned by AlloyDB Omni. These keys encrypt the actual data files, WAL, and temporary files. AlloyDB Omni stores DEKs on disk but wraps them with your KEK. 
  * Key Encryption Key (KEK): the main key that you manage in an external Key Management Service (KMS). AlloyDB Omni uses your KEK to encrypt the DEKs. AlloyDB Omni accesses this key only at startup to unwrap the DEKs. Your KEK is never stored persistently on the database disk. 
    * The KEK's location and access parameters are provided through environment variables and the `--tde-kek-url` initialization flag. 



## How TDE works with AlloyDB Omni

When TDE is enabled, AlloyDB Omni secures your data using a layered encryption model that integrates with an external KMS.

  * Initialization and key retrieval: during the cluster's startup or initialization phase, the AlloyDB Omni engine establishes a secure connection to your KMS. It authenticates using a JSON Web Token (JWT) and retrieves the KEK.
  * Unwrapping the DEKs: AlloyDB Omni uses your KEK to unwrap the DEKs, which are stored on the local storage in a wrapped state. Then, these DEKs are loaded into memory.
  * Transparent data operations: 
    * Writing to disk: as the database writes data blocks, WAL records, or temporary files to the physical disk, it automatically encrypts the data using AES-256 algorithms before it writes to the physical disk.
    * Reading from disk: when the database needs to read data into memory, it automatically decrypts the blocks using the DEKs that are held in memory.
  * Security boundaries: your KEK is never stored on the local database disk, ensuring that even if physical storage media is compromised, the data remains unreadable without authorized access to the external vault.



## Encryption scope and specifications

AlloyDB Omni uses industry-standard AES-256 algorithms to secure your data. 

  * **Data files (tables and indexes):** AES-256-XTS.
  * **Write-ahead logs (WAL):** AES-256-CTR.
  * **Temporary files:** AES-256-XTS or AES-256-CTR depending on the type of temporary data.
  * **Key wrapping:** AES-256-KWP.



## Backup and high availability

When TDE is enabled, backups created using `pgBackRest` inherit the encryption configuration of the source cluster. This ensures that your backup data remains protected with the same level of security as your primary database.

Backups can only be restored to clusters where the same KEK is available. 

For HA setups, the recovery environment must be initialized with the same vault environment variables. The vault environment variables must be available on all participating hosts.

## Supported KMS and authentication

AlloyDB Omni supports [HashiCorp Vault](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) as the external KMS provider. AlloyDB Omni only supports KV-V2 secrets engine, and the only supported authentication method is JWT.

## PostgreSQL tool compatibility

TDE-enabled clusters support all built-in PostgreSQL tools, except `initdb`, transparently through environment variables. If you are using `initdb`, then ensure that you pass the KEK URL explicitly. For more information, see [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/create-tde-cluster). 

## Limitations

  * You cannot enable TDE on existing clusters.
  * Once enabled, you cannot disable TDE.
  * Major version upgrades are not supported for TDE-enabled clusters.
  * You cannot restore encrypted backups to unencrypted servers or unencrypted backups to encrypted servers.
  * DEK rotation is not supported.
  * KEK rotation is supported as long as the KEK URL path remains the same.
  * You cannot `CREATE DATABASE` using the `FILE_COPY` strategy.
  * On TDE-enabled clusters, Barman backups only support `rsync` mode. The `postgres` backup method isn't supported.



## What's next

  * Learn how to [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/create-tde-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
