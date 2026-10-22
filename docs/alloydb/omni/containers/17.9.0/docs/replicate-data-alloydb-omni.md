---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/replicate-data-alloydb-omni/
title: Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:56.870141+00:00
---

# Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni  |  AlloyDB Omni using containers: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/replicate-data-alloydb-omni/

This page documents AlloyDB Omni version **17.9.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/overview)



Send feedback 

#  Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/replicate-data-alloydb-omni)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/replicate-data-alloydb-omni)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/replicate-data-alloydb-omni)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/replicate-data-alloydb-omni)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/replicate-data-alloydb-omni)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/replicate-data-alloydb-omni)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/replicate-data-alloydb-omni)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/replicate-data-alloydb-omni)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-alloydb-omni)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/replicate-data-alloydb-omni)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/replicate-data-alloydb-omni)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/replicate-data-alloydb-omni)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/replicate-data-alloydb-omni)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/replicate-data-alloydb-omni)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/replicate-data-alloydb-omni)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/replicate-data-alloydb-omni)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/replicate-data-alloydb-omni)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/replicate-data-alloydb-omni)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/replicate-data-alloydb-omni)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/replicate-data-alloydb-omni)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/replicate-data-alloydb-omni)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/replicate-data-alloydb-omni)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/replicate-data-alloydb-omni)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/replicate-data-alloydb-omni)

This page provides steps to replicate data between AlloyDB for PostgreSQL and AlloyDB Omni using the `pglogical` extension. 

For an overview of `pglogical` in AlloyDB Omni, its benefits, and limitations, see [About the pglogical extension](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/about-pglogical).

The information on this page applies only to AlloyDB Omni using containers. It does not apply to AlloyDB Omni using the container orchestrator.

## Key components of `pglogical`

Key components of the `pglogical` extension are as follows:

  * **Node** : reference given for the database within a PostgreSQL cluster. The `pglogical` extension is installed into, and works against any number of databases within the cluster, and each acts as a distinct pglogical node. Each node can be either a provider also known as replication source or subscriber also known as replication target, or both concurrently. Only one node is allowed per database.
  * **Replication set** : defined in the provider database as a logical grouping of tables and sequences to be migrated, and the SQL statements such as `INSERT, UPDATE, DELETE, TRUNCATE` that need to replicated. You can assign tables to more than one replication set. By default, three pre-configured replication sets such as `default`, `default_insert_only`, and `ddl_sql` are provided, and you can add any number of additional replication sets to meet your needs.
  * **Subscription** : provides details of the changes that are replicated from provider databases and changes that are replicated from provider databases, in the subscriber database. The subscription specifies the provider database through a connection string, and optionally, which replication sets from that provider should be copied. Additional, you can also specify whether to use `apply delay` when you create the subscription.



In this deployment, the AlloyDB for PostgreSQL service is the provider and the on-premises AlloyDB Omni is the subscriber. Note that the opposite configuration is also possible.

## Supported authentication methods

You must consider networking and security between the replication nodes before implementing the `pglogical` extension on AlloyDB Omni. The two main [authentication methods](https://www.postgresql.org/docs/17/auth-methods.html) used with the `pglogical` extension are password and trust authentication methods.

The recommended authentication method is trust authentication because in the password authentication method, passwords are stored in plain text format in database tables owned by `pglogical`. These passwords are visible in plain text to anyone with database permissions to query these tables, in non-binary backups, and in the PostgreSQL log files.

If you are using the trust authentication method, you must make specific entries in the host-based authentication file, `pg_hba.conf` for maximum security. You can restrict the access by specifying the target databases, permitting only the replication option or specific databases, the replication user, and only from the subscriber's specific IP address.

**Important:** The trust authentication method is not available for the AlloyDB for PostgreSQL service. For those connections, use the password authentication method.

## Before you begin

You can install `pglogical` as an extension within a given database. 

Before implementing the `pglogical` extension on AlloyDB Omni, ensure that you meet the following system requirements:

  * An AlloyDB for PostgreSQL cluster, and read/write access to the primary instance as an AlloyDB for PostgreSQL Admin. For instructions on how to provision an AlloyDB for PostgreSQL cluster, see [Create and connect to an AlloyDB for PostgreSQL database](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).
  * An AlloyDB Omni server, installed and configured. For instructions on how to install AlloyDB Omni, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install).
  * The IP addresses for both the AlloyDB for PostgreSQL primary instance and the AlloyDB Omni host server.
  * An established and secured network between AlloyDB for PostgreSQL and the AlloyDB Omni host server. TCP connectivity on the standard PostgreSQL port of 5432 is required.



## Adjust parameters on the AlloyDB for PostgreSQL provider

The `pglogical` extension requires a minimal set of parameter adjustments on the AlloyDB for PostgreSQL provider cluster. You must set the `wal_level` parameter to `logical`, and append `pglogical` to the `shared_preload_libraries` parameter in the `postgresql.conf` file.
    
    
       cp postgresql.conf postgresql.bak
       sed -r -i "s|(\#)?wal_level\s*=.*|wal_level=logical|" postgresql.conf
       sed -r -i "s|(\#)?(shared_preload_libraries\s*=\s*)'(.*)'.*$|\2'\3,pglogical'|" postgresql.conf
       sed -r -i "s|',|'|" postgresql.conf

In the AlloyDB for PostgreSQL service, you can adjust parameters by setting the appropriate cluster flags. 

You must adjust parameters for the following AlloyDB for PostgreSQL flags:

  * `alloydb.enable_pglogical = on`
  * `alloydb.logical_decoding = on`



For information about how to set database flags in AlloyDB for PostgreSQL, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

For the other required provider-node database parameters, you must set the AlloyDB for PostgreSQL default values as follows:

  * `max_worker_processes`: one per provider database and at least one per subscriber node. At least 10 is the standard for this parameter.
  * `max_replication_slots`: one per node on provider nodes.
  * `max_wal_senders`: one per node on provider nodes.
  * `track_commit_timestamp`: set to `on` if the last or first update wins conflict resolution is required.
  * `listen_addresses`: must include the AlloyDB Omni IP address or mention through a covering CIDR block.



You can check these parameters using any query tool, such as `psql`.

## Adjust parameters on the AlloyDB Omni subscriber cluster

The `pglogical`extension requires a minimal set of parameter adjustments on the AlloyDB Omni subscriber too. You must append `pglogical` to the `shared_preload_libraries` parameter in the `DATA_DIR/postgresql.conf` file. If any database within the cluster acts as a provider database, then make the parameter changes required for provider databases.

Replace DATA_DIR with the file system path to your data directory—for example, `/home/$USER/alloydb-data`.

  1. Adjust the parameters:
         
         sudo sed -r -i "s|(shared_preload_libraries\s*=\s*)'(.*)'.*$|\1'\2,pglogical'|" DATA_DIR/postgresql.conf

  2. Verify that the parameter is set properly:
         
         grep -iE 'shared_preload_libraries' DATA_DIR/postgresql.conf

  3. Restart AlloyDB Omni for the parameter change to take effect:

###  Docker 
         
         docker container restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 
         
         podman container restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

  4. Set the AlloyDB Omni default values for other provider database parameters:

     * `max_worker_processes`: One per provider database and one per subscriber node.
     * `track_commit_timestamp`: Set to `on` if the last or first update wins conflict resolution is required.
  5. Confirm all parameter values are set correctly:

###  Docker 
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres -c "
          SELECT name, setting
            FROM pg_catalog.pg_settings
           WHERE name IN ('listen_addresses',
                          'wal_level',
                          'shared_preload_libraries',
                          'max_worker_processes',
                          'max_replication_slots',
                          'max_wal_senders',
                          'track_commit_timestamp')
               ORDER BY name;"

###  Podman 
         
         podman exec CONTAINER_NAME psql -h localhost -U postgres -c "
          SELECT name, setting
            FROM pg_catalog.pg_settings
           WHERE name IN ('listen_addresses',
                          'wal_level',
                          'shared_preload_libraries',
                          'max_worker_processes',
                          'max_replication_slots',
                          'max_wal_senders',
                          'track_commit_timestamp')
               ORDER BY name;"




## Host-based authentication adjustments to the AlloyDB Omni subscriber cluster

The `pglogical` makes local TCP connections to the AlloyDB Omni subscriber database. Therefore, you must add the subscriber's host server's IP address to the AlloyDB Omni `DATA_DIR/pg_hba.conf` file.

  1. Add a trust authentication entry for the local server, specific to a new `pglogical_replication` user, to the `DATA_DIR/pg_hba.conf` file:
         
         echo -e "# pglogical entries:
         host all pglogical_replication samehost trust
         " | column -t | sudo tee -a DATA_DIR/pg_hba.conf

**Note:** Specify and limit connections to the exact database names instead of `all`.
  2. Verify that the entry is correct:
         
         tail -2 DATA_DIR/pg_hba.conf

  3. Restart AlloyDB Omni for the authentication change to take effect:

###  Docker 
         
         docker container restart CONTAINER_NAME

###  Podman 
         
         podman container restart CONTAINER_NAME




## Create a `pglogical` user in provider and subscriber clusters

You must create a new user in both the provider and subscriber cluster. `pglogical` requires the user to have both the `superuser` and `replication` permissions.

  1. In the AlloyDB for PostgreSQL provider cluster, create the user and grant the `alloydbsuperuser` role:
         
         CREATE USER pglogical_replication LOGIN PASSWORD 'secret';
         ALTER USER pglogical_replication WITH replication;
         GRANT alloydbsuperuser TO pglogical_replication;
         

  2. In the AlloyDB Omni subscriber cluster, create the user and grant the `replication` and `superuser` attributes:
         
         CREATE USER pglogical_replication LOGIN PASSWORD 'secret';
         ALTER USER pglogical_replication WITH replication;
         ALTER USER pglogical_replication WITH superuser;
         




## Add `pglogical` and nodes to the AlloyDB for PostgreSQL provider database

  1. Grant required privileges.

You must install the `pglogical` extension in each database and grant the `usage` permission to the pglogical database user. In AlloyDB for PostgreSQL, you must grant privileges on the `pglogical` schema.

For example, if your database is `my_test_db`, run the following command against the AlloyDB for PostgreSQL provider database:
         
         \c my_test_db;
          CREATE EXTENSION IF NOT EXISTS pglogical;
          GRANT usage ON SCHEMA pglogical TO pglogical_replication;
         -- For Google Cloud AlloyDB we also need to manually grant privileges:
          GRANT ALL PRIVILEGES ON ALL tables IN SCHEMA pglogical TO pglogical_replication;
         

  2. Create a `pglogical` node for the provider databases. The `node_name` is arbitrary and the `dsn` string must be a valid TCP connection back to the same database. For AlloyDB for PostgreSQL, the host part of the `dsn` is the IP address provided for the primary instance.

For AlloyDB for PostgreSQL, trust authentication is not permitted, and the password argument must be included in the `dsn`. parameter.

For example, for the `my_test_db` database, run the following command:
         
         SELECT pglogical.create_node(node_name := 'provider', dsn := 'host=SERVER_IP_ADDRESS
         port=5432 dbname=my_test_db user=pglogical_replication password=secret');
         




## Create a table and add it to the default replication set

Create a table and add it to the default replication set on the AlloyDB for PostgreSQL provider database.

  1. Create a test table called `test_table_1` in the provider database:
         
         CREATE TABLE test_table_1 (col1 INT PRIMARY KEY);
         INSERT INTO test_table_1 VALUES (1),(2),(3);
         

  2. Grant `SELECT` on the individual tables or run the `GRANT SELECT ON ALL TABLES` command. Any tables that are to be part of a replication set must have query permission granted to the replication user, `pglogical_replication`.
         
         GRANT SELECT ON ALL TABLES IN SCHEMA public TO pglogical_replication;
         

  3. Manually add the test table to the default replication set. You can either create custom pglogical replication sets, or you can use the default replication sets. Several default replication sets such as `default`, `default_insert_only`, and `ddl_sql`were created when you created the extension. You can add tables and sequences to the replication sets individually, or all at once for a specified schema.
         
         -- Add the specified table to the default replication set:
         SELECT pglogical.replication_set_add_table(set_name := 'default', relation := 'test_table_1', synchronize_data := TRUE);
         
         -- Check which tables have been added to all replication sets:
         SELECT * FROM pglogical.replication_set_table;
         

  4. (Optional) Add all tables in a specified schema, such as `public`:
         
         -- Add all "public" schema tables to the default replication set:
         SELECT pglogical.replication_set_add_all_tables('default', ARRAY['public']);
         
         -- Check which tables have been added to all replication sets:
         SELECT * FROM pglogical.replication_set_table;
         
         -- Add all "public" schema sequences to the default replication:
         SELECT pglogical.replication_set_add_all_sequences('default', ARRAY['public']);
         
          -- Check which sequences have been added to all replication sets:
         SELECT * FROM pglogical.replication_set_seq;
         

  5. Remove the table from the `default` replication set. If there are any tables in the schema that do not have a primary key, then you can either set it up for INSERT only replication or set the columns that uniquely identify the row by using the `REPLICA IDENTITY` feature used with the `ALTER TABLE` command. If you have added those tables to the `default` replication set automatically using the `replication_set_add_all_tables` function, then you must manually remove them from that replication set and add them to the `default_insert_only` set.
         
         -- Remove the table from the **default** replication set:
         SELECT pglogical.replication_set_remove_table(set_name := 'default', relation := 'test_table_2');
         
         
         -- Manually add to the **default_insert_only** replication set:
         SELECT pglogical.replication_set_add_table(set_name := 'default_insert_only', relation := 'test_table_2');
         

Optionally, if you want to add the newly created tables to the replication set automatically, add the `pglogical_assign_repset` trigger as suggested in the [`pglogical` source](https://github.com/2ndQuadrant/pglogical#automatic-assignment-of-replication-sets-for-new-tables).




## Copy the database to the AlloyDB Omni subscriber cluster

  1. Create a schema-only backup of the source database using the `pg_dump` utility.

  2. Run the `pg_dump`command from your AlloyDB Omni subscriber server using the IP address of the AlloyDB for PostgreSQL primary instance.

**Note:** You must run the `pg_dump` command from outside of the AlloyDB Omni container. It is recommended that you run the `pg_dump` command from your AlloyDB Omni host server if you can install the PostgreSQL client. You can also run the command from another server, if necessary.
         
         pg_dump -h SERVER_IP_ADDRESS -U postgres --create --schema-only my_test_db > my_test_db.schema-only.sql

  3. Import the backup into the subscriber database on the subscriber AlloyDB Omni server:

###  Docker 
         
         docker exec -i CONTAINER_NAME psql -h localhost -U postgres < my_test_db.schema-only.sql

###  Podman 
         
         podman exec -i CONTAINER_NAME psql -h localhost -U postgres < my_test_db.schema-only.sql




Ignore errors such as `alloydbsuperuser not existing`. This role is specific to AlloyDB for PostgreSQL.

This creates the database and the schema, without any of the row data. Row data is replicated by the `pglogical` extension. Manually copy or recreate any other users or roles that are required.

## Create a node and subscription on the AlloyDB Omni subscriber database

  1. Create a node on the AlloyDB Omni subscriber database:

###  Docker 
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres -d my_test_db -c "
         SELECT pglogical.create_node(node_name := 'subscriber', dsn := 'host=localhost port=5432 dbname=my_test_db user=pglogical_replication');"

###  Podman 
         
         podman exec CONTAINER_NAME psql -h localhost -U postgres -d my_test_db -c "
         SELECT pglogical.create_node(node_name := 'subscriber', dsn := 'host=localhost port=5432 dbname=my_test_db user=pglogical_replication');"

  2. Create a subscription in the subscriber database, pointing back to the AlloyDB for PostgreSQL provider database's primary instance.

**Note:** For AlloyDB for PostgreSQL, trust authentication is not available. You must include the password argument in the `dsn` parameter.**Caution:** Ensure that the connection details in the **`dsn`** parameter are accurate.

###  Docker 
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres -d my_test_db -c "
         SELECT pglogical.create_subscription(subscription_name := 'test_sub_1', provider_dsn := 'host=SERVER_IP_ADDRESS port=5432 dbname=my_test_db user=pglogical_replication password=secret');"

###  Podman 
         
         podman exec CONTAINER_NAME psql -h localhost -U postgres -d my_test_db -c "
         SELECT pglogical.create_subscription(subscription_name := 'test_sub_1', provider_dsn := 'host=SERVER_IP_ADDRESS port=5432 dbname=my_test_db user=pglogical_replication password=secret');"

  3. Based on your table size and data to be replicated, the replication time might vary from seconds to minutes, after which the initial data should have replicated from the provider to the subscriber:

###  Docker 
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres -d my_test_db -c "
         SELECT * FROM test_table_1 ORDER BY 1;"

###  Podman 
         
         podman exec CONTAINER_NAME psql -h localhost -U postgres -d my_test_db -c "
         SELECT * FROM test_table_1 ORDER BY 1;"

Additional rows that are added to the provider database are also replicated within seconds.




## Additional `pglogical` deployment considerations

The `pglogical` extension has many advanced features that are not covered in this document. Many of these features are applicable to your implementation. You can consider the following advanced features:

  * Conflict resolution
  * Multimaster and bi-directional replication
  * Inclusion of sequences
  * Switchover and failover procedures



## What's next

  * [Replicate data between AlloyDB Omni and other databases](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/replicate-data-omni-other-db)
  * [Switchover and failover with `pglogical` replication](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/switchover-failover)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
