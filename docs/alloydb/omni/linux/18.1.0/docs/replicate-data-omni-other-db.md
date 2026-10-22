---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/replicate-data-omni-other-db/
title: Replicate data between AlloyDB Omni and other databases \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:20.708423+00:00
---

# Replicate data between AlloyDB Omni and other databases  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/replicate-data-omni-other-db/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Replicate data between AlloyDB Omni and other databases Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/replicate-data-omni-other-db)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/replicate-data-omni-other-db)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/replicate-data-omni-other-db)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/replicate-data-omni-other-db)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/replicate-data-omni-other-db)

This page provides steps to replicate data between AlloyDB Omni and other databases using the `pglogical` extension. The information on this page applies only to AlloyDB Omni using RPM.

For more information, see [About the `pglogical` extension](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/about-pglogical) and [`pglogical` terminology and fundamental components](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/replicate-data-alloydb-omni#terminology).

## Supported authentication methods

The two main [authentication methods](https://www.postgresql.org/docs/18/auth-methods.html) used with the `pglogical` extension are password and trust authentication methods.

The recommended authentication method is trust authentication method. For more information, see [Supported authentication methods](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/replicate-data-alloydb-omni#authentication).

**Note:** The trust authentication method is not available for cloud provider's managed-service database, such as Amazon Aurora as the non-AlloyDB source. For those connections, use the password authentication method.

## Before you begin

You can install `pglogical` as an extension within a given database. 

Before implementing the `pglogical` extension on AlloyDB Omni, ensure that you meet the following system requirements:

  * Access to your non-AlloyDB PostgreSQL cluster as a `superuser`.
  * The `pglogical` extension is installed in your non-AlloyDB PostgreSQL cluster. For release and distribution-specific installation instructions, see the [pglogical](https://github.com/2ndQuadrant/pglogical).
  * An AlloyDB Omni server installed and configured. For instructions on how to install AlloyDB Omni, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install).
  * The IP addresses for both the non-AlloyDB PostgreSQL cluster and the AlloyDB Omni host server.
  * An established and secured network between the non-AlloyDB PostgreSQL cluster and the AlloyDB Omni host server. TCP connectivity on the standard PostgreSQL port of 5432 is required.



## Adjust parameters on the non-AlloyDB provider

  1. Set the `wal_level` parameter to `logical`, and append `pglogical` to the `shared_preload_libraries` parameter in the `postgresql.conf` file. The `pglogical` extension requires a minimal set of parameter adjustments on the non-AlloyDB provider cluster. 
         
         cp postgresql.conf postgresql.bak
         sed -r -i "s|(\#)?wal_level\s*=.*|wal_level=logical|" postgresql.conf
         sed -r -i "s|(\#)?(shared_preload_libraries\s*=\s*)'(.*)'.*$|\2'\3,pglogical'|" postgresql.conf
         sed -r -i "s|',|'|" postgresql.conf

  2. Verify that the parameters are properly set:
         
         grep -iE 'wal_level|shared_preload_libraries' postgresql.conf

  3. Restart your non-AlloyDB cluster for the parameter changes to take effect.

Other parameters might be already set to sufficient values or might require adjusting depending on your non-AlloyDB distribution and version.

Check the following parameters:

     * `max_worker_processes`: one per provider database and at least one per subscriber node. At least 10 is the standard for this parameter.
     * `max_replication_slots`: one per node on provider nodes.
     * `max_wal_senders`: one per node on provider nodes.
     * `track_commit_timestamp`: set to `on` if the last or first update wins conflict resolution is required.
     * `listen_addresses`: must include the AlloyDB Omni IP address or mention through a covering CIDR block.
  4. (Optional) If your non-AlloyDB provider is Amazon RDS or Aurora, then the pglogical extension must be enabled and the required parameters adjusted through `cluster parameter group` adjustments.

     1. In an existing or new cluster parameter group, set the following parameters:

        * `rds.logical_replication` to `1`
        * `max_replication_slots` to `50`
        * `max_wal_senders` to `50`
        * `max_worker_processes` to `64`
        * `shared_preload_libraries` to `pg_stat_statements, pglogical`
     2. Restart your Amazon RDS or Aurora cluster for the cluster parameter group adjustments to take effect.

  5. Confirm that all parameter values are relevant:
         
         SELECT name, setting
         FROM pg_catalog.pg_settings
          WHERE name IN ('listen_addresses',
                         'wal_level',
                         'shared_preload_libraries',
                         'max_worker_processes',
                         'max_replication_slots',
                         'max_wal_senders',
                         'track_commit_timestamp')
          ORDER BY name;
         




## Host-based authentication adjustments to the non-AlloyDB Omni provider cluster

The `pglogical` makes local TCP connections to the provider database. Therefore, you must add the host server's IP address to the AlloyDB Omni `DATA_DIR/pg_hba.conf` file where `DATA_DIR` is the file system path to your data directory—for example, `/home/$USER/alloydb-data`.

  1. Add a trust authentication entry for the local server, specific to a new `pglogical_replication` user, to the `DATA_DIR/pg_hba.conf` file.

**Important:** If you prefer to use _password authentication_ , remove the `trust` values and replace them with `scram-sha-256`.

Additionally, subscriber nodes must be able to authenticate against the provider nodes. Add either each subscriber node's IP address or the appropriate [CIDR block](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) IP range to the `DATA_DIR/pg_hba.conf` file:
         
         echo -e "# pglogical entries:
         host all pglogical_replication samehost trust
         host all pglogical_replication SERVER_IP_ADDRESS/32 trust
         " | column -t | sudo tee -a DATA_DIR/pg_hba.conf

Replace `SERVER_IP_ADDRESS` with the IP address of the primary AlloyDB Omni instance to replicate from.

**Note:** Specify and limit connections to the exact database names instead of `all`. Also, restrict the CIRD block IP ranges by specifying the subscriber node IP addresses, such as `/32` instead of IP ranges.
  2. Verify that the entries are correct:
         
         tail -3 DATA_DIR/pg_hba.conf

  3. Restart your non-AlloyDB cluster for the parameter changes to take effect.


**Note:** Cloud managed services PostgreSQL databases such as Amazon RDS or Aurora usually don't permit manual adjustments or customization to the `DATA_DIR/pg_hba.conf` file. In some cases, either no adjustments are required, or firewall and routing adjustments are required.

## Adjust parameters to the AlloyDB Omni subscriber cluster

The `pglogical` requires a minimal set of parameter adjustments on the AlloyDB Omni subscriber cluster too. You must append `pglogical` to the `shared_preload_libraries` parameter in the `DATA_DIR/postgresql.conf` file. If any database within the cluster acts as a provider database, then make the parameter changes required for provider databases.

  1. Adjust the parameters:
         
         sudo sed -r -i "s|(shared_preload_libraries\s*=\s*)'(.*)'.*$|\1'\2,pglogical'|" DATA_DIR/postgresql.conf

  2. Verify that the parameter is set properly:
         
         grep -iE 'shared_preload_libraries' DATA_DIR/postgresql.conf

  3. Restart AlloyDB Omni for the parameter change to take effect:
         
         sudo systemctl restart alloydbomni18

  4. Set the AlloyDB Omni default values for other provider database parameters:

     * `max_worker_processes`: One per provider database and one per subscriber node.
     * `track_commit_timestamp`: Set to `on` if the last/first update wins conflict resolution is required.
  5. Confirm that all parameter values are relevant:
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -c "
         SELECT name, setting
         FROM pg_catalog.pg_settings
         WHERE name IN ('listen_addresses',
                         'wal_level',
                         'shared_preload_libraries',
                         'max_worker_processes',
                         'max_replication_slots',
                         'max_wal_senders',
                         'track_commit_timestamp')
             ORDER BY name;
         "




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
         
         docker container restart CONTAINER_NAME




## Create a `pglogical` user in both provider and subscriber clusters

You must create a new user in both the provider and subscriber cluster. `pglogical` requires the user to have both the `superuser` and `replication` attributes.

  1. In the AlloyDB for PostgreSQL provider cluster, create the user role:
         
         CREATE USER pglogical_replication LOGIN PASSWORD 'secret';
         ALTER USER pglogical_replication WITH replication;
         ALTER USER pglogical_replication WITH superuser;
         

  2. (Optional) If your non-AlloyDB provider is Amazon RDS or Aurora, then you must grant the following role:
         
         GRANT rds_superuser TO replication_user;
         

**Note:** If your non-AlloyDB database is from some other cloud-managed service, then a service-specific, custom grant might be required.



## Add `pglogical` and nodes to the non-AlloyDB provider database

  1. Grant required privileges.

You must install the `pglogical` extension in each database and grant the `usage` permission to the pglogical database user.

For example, if your database is `my_test_db`, run the following command:
         
         CREATE EXTENSION IF NOT EXISTS pglogical;
         GRANT usage ON SCHEMA pglogical TO pglogical_replication;
         

  2. Create a `pglogical` node for the provider databases. The `node_name` is arbitrary and the `dsn` string must be a valid TCP connection back to the same database.

**Important:** If you're using a cloud-managed service database, then the password authentication is mandatory. You can choose to use password authentication in your self-managed PostgreSQL deployment. In such cases, include the password in your `dsn`` string. If you're using a self-managed installation, then you can either use the password or trust authentication.

For example, for the `my_test_db` database, run the following command:
         
         SELECT pglogical.create_node(node_name := 'provider', dsn := 'host=SERVER_IP_ADDRESS port=5432 dbname=my_test_db user=pglogical_replication password=secret');
         

**Note:** If your non-AlloyDB provider is Amazon RDS or Aurora, then use the provided AWS endpoint instead of the host IP address in the `dsn` parameter. If your non-AlloyDB database is from some other cloud-managed service, then a service-specific, endpoint or IP address is required.



## Create a table and add it to the default replication set

Create a table and add it to the default replication set on the non-AlloyDB provider database.

  1. Create a test table called `test_table_1` in the provider database:
         
         CREATE TABLE test_table_1 (col1 INT PRIMARY KEY);
         INSERT INTO test_table_1 VALUES (1),(2),(3);
         

  2. Manually add the test table to the default replication set. You can either create custom pglogical replication sets, or you can use the default replication sets. Several default replication sets such as `default`, `default_insert_only`, and `ddl_sql`were created when you created the extension. You can add tables and sequences to the replication sets individually, or all at once for a specified schema.
         
         -- Add the specified table to the default replication set:
         SELECT pglogical.replication_set_add_table(set_name := 'default', relation := 'test_table_1', synchronize_data := TRUE);
         
         -- Check which tables have been added to all replication sets:
         SELECT * FROM pglogical.replication_set_table;
         

  3. (Optional) Add all tables in a specified schema, such as `public`:
         
         -- Add all "public" schema tables to the default replication set:
         SELECT pglogical.replication_set_add_all_tables('default', ARRAY['public']);
         
         -- Check which tables have been added to all replication sets:
         SELECT * FROM pglogical.replication_set_table;
         
         -- Add all "public" schema sequences to the default replication:
         SELECT pglogical.replication_set_add_all_sequences('default', ARRAY['public']);
         
         -- Check which sequences have been added to all replication sets:
         SELECT * FROM pglogical.replication_set_seq;
         

  4. Remove the table from the `default` replication set. If there are any tables in the schema that don't have a primary key or a replica identity, then only `INSERT` statements can be replicated. If you have added those tables to the `default` replication set automatically through the `replication_set_add_all_tables` function, then you need to manually remove them from that replication set and add them to the `default_insert_only` set.
         
         -- Remove the table from the **default** replication set:
         SELECT pglogical.replication_set_remove_table(set_name := 'default', relation := 'test_table_2');
         
         -- Manually add to the **default_insert_only** replication set:
         SELECT pglogical.replication_set_add_table(set_name := 'default_insert_only', relation := 'test_table_2');
         

Optionally, if you want to add the newly created tables to the replication set automatically, add the `pglogical_assign_repset` trigger as suggested in the [`pglogical` source](https://github.com/2ndQuadrant/pglogical#automatic-assignment-of-replication-sets-for-new-tables).




## Copy the database to the AlloyDB Omni subscriber cluster

  1. Create a schema-only backup of the source database using the `pg_dump` utility.

  2. Run the `pg_dump`command from your AlloyDB Omni subscriber server using the IP address or endpoint of your non-AlloyDB server.

**Note:** We recommend that you run the `pg_dump` command from your AlloyDB Omni host server if you can install the PostgreSQL client. You can also run the command from another server, if necessary.
         
         pg_dump -h SERVER_IP_ADDRESS -U postgres --create --schema-only my_test_db > my_test_db.schema-only.sql

**Note:** If your non-AlloyDB provider is Amazon RDS or Aurora, then use the provided AWS endpoint instead of the host IP address in the `dsn` parameter. If your non-AlloyDB database is from some other cloud-managed service, then you must use a service-specific, endpoint, or IP address.
  3. Import the backup into the subscriber database on the subscriber AlloyDB Omni server:
         
         sudo -u postgres /usr/lib/postgresql/18/bin/psql -h localhost -U postgres < my_test_db.schema-only.sql

This creates the database and the schema without any of the row data. Row data is replicated by the `pglogical` extension. Manually copy or recreate any other users or roles that are required.




## Create a node and subscription on the AlloyDB Omni subscriber database

  1. Create a node on the AlloyDB Omni subscriber database. Add the password to your `dsn` if you choose to use password authentication.
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -d my_test_db -c "
         SELECT pglogical.create_node(node_name := 'subscriber', dsn := 'host=localhost port=5432 dbname=my_test_db user=pglogical_replication');"

  2. Create a subscription in the subscriber database, pointing back to provider database in the AlloyDB Omni provider server.

**Note:** For cloud-managed service PostgreSQL databases, trust authentication is not available. You must include the password argument in the `dsn` parameter.**Caution:** Verify that the connection details in the `dsn` parameter are accurate.
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -d my_test_db -c "
         SELECT pglogical.create_subscription(subscription_name := 'test_sub_1', provider_dsn := 'host=PROVIDER_IP_ADDRESS port=5432 dbname=my_test_db user=pglogical_replication password=secret');"

**Note:** If your non-AlloyDB provider is Amazon RDS or Aurora, then use the provided AWS endpoint instead of the host IP address in the `dsn`parameter. If your non-AlloyDB database is from some other cloud-managed service, then a service-specific, endpoint or IP address is required.
  3. Within a few seconds or minutes, the initial data should have replicated from the provider to the subscriber:
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -d my_test_db -c "SELECT * FROM test_table_1 ORDER BY 1;"

Additional rows that are added to the provider database are also replicated in real time within seconds.




## Additional `pglogical` deployment considerations

The `pglogical` extension has many advanced features that are not covered in this document. Many of these features are applicable to your implementation. You can consider the following advanced features:

  * Conflict resolution
  * Multimaster and bi-directional replication
  * Inclusion of sequences
  * Switchover and failover procedures



## What's next

  * [Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/replicate-data-alloydb-omni)
  * [Switchover and failover with `pglogical` replication](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/switchover-failover)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
