---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/migrate-tde-cluster/
title: Migrate data to and from a TDE-enabled cluster \u00a0|\u00a0 AlloyDB Omni using containers: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:26.064143+00:00
---

# Migrate data to and from a TDE-enabled cluster  |  AlloyDB Omni using containers: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/migrate-tde-cluster/

This page documents AlloyDB Omni version **18.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/overview)



Send feedback 

#  Migrate data to and from a TDE-enabled cluster Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/migrate-tde-cluster)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/migrate-tde-cluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/migrate-tde-cluster)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/migrate-tde-cluster)



This guide describes how to migrate data between [transparent data encryption-enabled](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/transparent-data-encryption-omni) (TDE) and non-encrypted clusters using `pg_dump` and `pg_restore`.

Both migration directions—TDE to non-encrypted and the other way around—are supported and use standard PostgreSQL logical backup tools.

Logical migration using `pg_dump` decodes the encrypted data on-the-fly at the source and dumps it as unencrypted SQL statements. When you restore the data, the destination cluster writes the data according to its own encryption settings. The destination cluster encrypts the data if TDE is enabled, and it writes as plain text if TDE is disabled.

Caution: The generated SQL file contains unencrypted data from your database. Verify that the SQL file is stored securely and delete it after the restore process is complete. 

## Before you begin

  * Verify that you installed AlloyDB Omni. For more information, see [Install AlloyDB Omni using containers](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/deploy-vm). 
  * If you're migrating to a TDE-enabled database server, verify that you set up your key management provider. For more information, see [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/create-tde-cluster).



## Migrate a TDE-enabled database to a TDE-disabled database

  1. Dump the database from the TDE-enabled database server to a file on the host.

###  Docker 
         
         docker exec -i TDE_CONTAINER_NAME pg_dump -U postgres -d DATABASE_NAME > /tmp/decrypted_dump.sql
         

###  Podman 
         
         podman exec -i TDE_CONTAINER_NAME pg_dump -U postgres -d DATABASE_NAME > /tmp/decrypted_dump.sql
         

  2. Start a TDE-disabled AlloyDB Omni server by following the instructions in [Install AlloyDB Omni using Docker](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/quickstart#install-using-docker). 

  3. Restore the dump file to the non-encrypted database server.

###  Docker 
         
         docker exec -i NON_TDE_CONTAINER_NAME psql -U postgres -c "CREATE DATABASE DATABASE_NAME"
         docker exec -i NON_TDE_CONTAINER_NAME psql -U postgres -d DATABASE_NAME < /tmp/decrypted_dump.sql
         

###  Podman 
         
         podman exec -i NON_TDE_CONTAINER_NAME psql -U postgres -c "CREATE DATABASE DATABASE_NAME"
         podman exec -i NON_TDE_CONTAINER_NAME psql -U postgres -d DATABASE_NAME < /tmp/decrypted_dump.sql
         




## Migrate a TDE-disabled database to a TDE-enabled database

  1. Use `pg_dump` to dump the database from the non-encrypted database server.

###  Docker 
         
         docker exec -i NON_TDE_CONTAINER_NAME pg_dump -U postgres -d DATABASE_NAME > /tmp/src_plaintext_dump.sql
         

###  Podman 
         
         podman exec -i NON_TDE_CONTAINER_NAME pg_dump -U postgres -d DATABASE_NAME > /tmp/src_plaintext_dump.sql
         

  2. Start a TDE-enabled AlloyDB Omni server following the instructions in [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/create-tde-cluster).

  3. Restore to the TDE-enabled database server. The data is transparently encrypted as it is written.

###  Docker 
         
         docker exec -i TDE_CONTAINER_NAME psql -U postgres -c "CREATE DATABASE DATABASE_NAME"
         docker exec -i TDE_CONTAINER_NAME psql -U postgres -d DATABASE_NAME < /tmp/src_plaintext_dump.sql
         

###  Podman 
         
         podman exec -i TDE_CONTAINER_NAME psql -U postgres -c "CREATE DATABASE DATABASE_NAME"
         podman exec -i TDE_CONTAINER_NAME psql -U postgres -d DATABASE_NAME < /tmp/src_plaintext_dump.sql
         




## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/run-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
