---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/diagnose-issues/
title: Diagnose issues in Oracle to AlloyDB for PostgreSQL migrations \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:35.468178+00:00
---

# Diagnose issues in Oracle to AlloyDB for PostgreSQL migrations  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Diagnose issues in Oracle to AlloyDB for PostgreSQL migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page lists known errors and recommended troubleshooting steps for:

  * Errors encountered during the migration job

  * Issues encountered when establishing network connectivity

  * Errors encountered when working with Oracle SCAN




## Migration job errors

The migration job process might incur errors during runtime.

  * Some errors, such as a bad password on the source database, are recoverable. The migration job resumes automatically after these errors are fixed.
  * Some errors are unrecoverable, such as errors in data replication. You must restart the migration job after these errors are fixed.



When an error occurs, the migration job status changes to `Failed`, and the substatus reflects the last status before failure. To troubleshoot an error, navigate to the failed migration job to view the error, and follow the steps outlined in the error message. To view more details about the error, navigate to Cloud Monitoring by using the link on the migration job. The logs are filtered to the specific migration job.

In the following table, you can find some examples of issues and how they can be solved:

Symptom | Possible causes | Things to try  
---|---|---  
Error message: `Database Migration Service can't set up a tunnel to be connected to the bastion host`.  | Database Migration Service couldn't access the bastion host or the bastion host is not accepting connections.  | Verify your forward SSH tunnel settings in the [ source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-source-connection-profile#fwd-ssh-connectivity) and the [ SSH tunnel server configuration](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source#forward-ssh-tunnel), and try again.   
Error message: `Database Migration Service can't connect to the database` or `Database Migration Service private connectivity error, cannot connect to the database`.  | Database Migration Service couldn't establish connectivity to the source Oracle database. |  Verify that you can access the source database from your project. Check the settings related to your [ source connectivity configuration method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source).  If there is a specific Oracle error code included, for example `ORA-12170: TNS:Connect timeout occurred`, see the [ Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/errmg/) for more information.   
Error message: `Archiving mode is not ARCHIVELOG`. | Your source database isn't running in the `ARCHIVELOG` mode. | Configure your source database to use the `ARCHIVELOG` mode. For more information, see [ Configure your source Oracle database](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-source-database).   
Error message: `Supplemental logging ("ALL COLUMN LOGGING") isn't turned on for the tables listed below`.  | Your source database doesn't have supplemental log data enabled. | Enable supplemental log data and set its mode to `ALL`. For more information, see [ Configure your source Oracle database](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-source-database).   
Error message: `No Archive Log Files were found in the source`. | Database Migration Service only reads closed archive logs, and no logs were found in the source database.  | 

  1. Run the following command in the source database to close the current log file: `ALTER SYSTEM SWITCH LOGFILE`. 
  2. Try to find the logs again.

If the database doesn't have any active write operations, you might need to perform at least one `INSERT` operation to trigger the log creation.   
Error message: `We're missing the necessary permissions to read from the source`.  | The migration user account in your source database doesn't have the required permissions.  |  Database Migration Service connects to your source as the user account you configure in the source connection profile. That account needs a specific set of permissions (for example `SELECT ANY TABLE`) to read data in your source database.  Make sure the migration user account has the necessary privileges. For more information, see [ Configure your source Oracle database](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-source-database).   
Error message: `Unable to connect to the destination database`. | There was a problem connecting to the destination database. | Verify that you can access the destination database from your project. Check the settings related to your [ destination connectivity configuration method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination).   
Error message: `The following tables don't exist in the destination database: {table_names}`. | The listed tables that you are trying to migrate don't exist in the destination database.  | Database Migration Service creates the necessary table and definitions when you convert your source schema.   
Error message: `password authentication failed for user {username}`. | The username or the password for the destination database are misconfigured. | Ensure that the destination PostgreSQL connection profile is configured correctly with the right username and password.   
Error message: `The following tables in the destination database don't have primary keys: {table_names}`.  | The tables listed in the error message exist in the destination database, but are missing primary keys.  |  Database Migration Service conversion workspaces automatically add primary keys for tables that don't have them when you convert schema.  If you use legacy conversion workspaces, you need to create the primary keys manually in your destination. For more information, see [ Legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/legacy-conversion-workspaces).   
Warning: `The following tables have foreign keys: {table_names}`. | The tables listed in the error message exist in the destination database, but have foreign keys.  |  Database Migration Service doesn't replicate data in a transactional manner, so tables might be migrated out of order. If foreign keys are present, and a child table that uses a foreign key is migrated before its parent, you might encounter replication errors.  To avoid such data integrity issues, skip foreign keys by using the `REPLICATION` option for the migration user. For more information, see [ Considerations for foreign keys and triggers](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/known-limitations#foreign-keys-triggers-considerations).   
Error message: `Unable to resume replication as log position is lost`. | This error might occur when the replication process is paused for a long time, leading to the loss of the log position.  | A migration job shouldn't be paused for longer than (or close to) the log retention period. If the log position is lost, you need to re-create the migration job.   
Error message: `ORA-00942: table or view does not exist`. | This error might occur as a result of caching on the Oracle server. | Recreate the database user to fix the caching issue.  
The migration job remains in the full dump phase and doesn't advance to the change data capture (CDC) phase.  | Database Migration Service is still performing full dump for some of the tables, or one or more of the tables can't finish full dump due to errors.  | 

  * Check the migration job errors and either fix errors that apply to tables or remove the associated tables from the job. 
  * Check the Database Migration Service logs for ongoing full dump activity and wait until it's finished. 

  
  
## Connectivity issues

This section lists and describes troubleshooting steps for potential network connectivity issues.

### Unable to connect to the destination database: EOF

Running a connectivity test returns the `[DATABASE] unable to connect to the destination database: EOF` error message.

**Possible cause:** The service attachment is configured incorrectly.

**Things to try:** Make sure that `enable_proxy_protocol` is set to `false` in the [ service attachment Terraform configuration file](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-dst-connection-private-ip#non-psc). Proxy protocol is supported only for HTTP servers such as NGINX and Apache.

When using `gcloud` to create the Private Service Connect setup, the proxy protocol is disabled by default.

### Connection timeout, connection refused

Running the connectivity test fails or times out. This is most likely caused by misconfigured routing within the Private Service Connect setup. There can be several reasons for this problem.

**Possible cause:** There's a missing firewall rule that allows the Private Service Connect NAT CIDR range to access the Private Service Connect subnet where the bastion is located, specifically the bastion VM `nic0` interface.

**Things to try:** Make sure your organization policy doesn't restrict internal firewall rules, such as the `psc_sp_in_fw` firewall rule defined in the example Terraform script for [ configuring destination private IP connectivity for non-PSC enabled AlloyDB for PostgreSQL instances](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-dst-connection-private-ip#non-psc).

**Possible cause:** The proxy is down. There is no listener on the supplied port, and therefore the connection hangs.

**Things to try:** You can try to establish an SSH connection to the bastion VM, and search for the proxy using the following command:

  * `netstat -tunalp | grep PORT`



Analyze the responses to the command:

  * If you get an empty response, the proxy is down. Try running the following commands:

`sudo su; cd /` and check if the Dante server is installed by running `sudo dpkg -s dante-server`:

    * If the proxy is installed, you get the following message:

`Status: install ok installed`

    * If the proxy isn't installed, the probable issue is a missing router. Add a router and check if you can download the proxy by running `apt-get install dante-server`.

To learn how to add a router, check how the `psc_sp_ex_router` and `psc_sp_ex_router_nat` resources are added in the `main.tf` file in [ Configuring destination private IP connectivity for non-PSC enabled AlloyDB for PostgreSQL instances](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-dst-connection-private-ip#non-psc). 
  * If the proxy is running and listening on the supplied port, try opening a connection to it by doing the following:

    1. Install the PostgreSQL client:

`sudo apt-get install postgresql-client`.

    2. Connect to the PostgreSQL database:

`psql -h 127.0.0.1 -p PORT -U DBUSERNAME -W` (you will be prompted to enter the password).

Replace the following:

       * `PORT`: the database port number.
       * `DBUSERNAME`: the username used to connect to the PostgreSQL database.
    3. Install the telnet client:

`sudo apt-get install telnet`

    4. Connect to the telnet client:

`telnet 127.0.0.1 PORT`

Replace `PORT` with the database port number.

Depending on the results of the commands:

    * If the commands fail to open a connection, try looking at the proxy logs to locate the root cause. The root cause can vary depending on the AlloyDB for PostgreSQL instance setup.

    * If the connection is opened using telnet but hangs in the client, the probable issue is the bastion IP address routing. On your VM, type `ip route` in the terminal. See if you can locate a routing rule that routes connections to the AlloyDB for PostgreSQL instance private IP address using the secondary `nic` (`nic1`, the `DB_SUBNETWORK_GATEWAY` IP address).




**Possible cause:** The service attachment doesn't accept the endpoint connection coming from Database Migration Service. The service attachment holds a list of projects which are accepted, and the Database Migration Service project isn't included in the list.

**Things to try:** To resolve the issue, try either of the following:

  * In the Google Cloud console, go to **Private Service Connect**.

[ Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

On the **Published services** tab, accept the connection from Database Migration Service for your service attachment (if it's pending).

  * Add the requesting project to the allowlisted projects on the service attachment (if it's rejected).

    * For more information about adding an allowlisted project in Terraform, see [ Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_service_attachment#consumer_reject_lists).

    * For more information about adding an allowlisted project in `gcloud`, see [ Google Cloud CLI reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/service-attachments/create#--consumer-accept-list).

If this doesn't solve the issue, recreate the connection profile.

  * [ Delete the connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-connection-profiles#delete_a_connection_profile) associated with the Private Service Connect connectivity, and recreate it.




## Troubleshoot Oracle SCAN errors

This section describes potential issues you might have when migrating from Oracle Real Application Clusters (RAC) sources using the Single Client Access Name (SCAN) feature.

### Unable to establish connectivity to an Oracle SCAN database

Running the connectivity test fails or times out.

**Possible cause:** You might be trying to establish connectivity directly to your Oracle SCAN source database. Database Migration Service doesn't support direct connectivity to databases using the SCAN feature in Oracle RAC environments.

**Things to try:** To resolve the issue, try either of the following:

  * Connect directly to one of the nodes.

  * Use the [ Oracle Connection Manager](https://docs.oracle.com/en/database/oracle/oracle-database/19/netag/configuring-oracle-connection-manager.html#GUID-E599547C-2AE3-4383-93A4-DC45C707467D).

  * Create a private connectivity configuration using a reverse proxy solution such as HAProxy.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
