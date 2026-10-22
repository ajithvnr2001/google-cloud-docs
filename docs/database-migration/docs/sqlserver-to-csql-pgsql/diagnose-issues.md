---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/diagnose-issues/
title: Diagnose issues for SQL Server to Cloud SQL for PostgreSQL migrations \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:48.798372+00:00
---

# Diagnose issues for SQL Server to Cloud SQL for PostgreSQL migrations  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Diagnose issues for SQL Server to Cloud SQL for PostgreSQL migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page lists known errors and recommended troubleshooting steps for:

  * Errors encountered during the migration job

  * Issues encountered when establishing network connectivity




## Migration job errors

The migration job process might incur errors during runtime.

  * Some errors, such as a bad password on the source database, are recoverable. The migration job resumes automatically after these errors are fixed.
  * Some errors are unrecoverable, such as errors in data replication. You must restart the migration job after these errors are fixed.



When an error occurs, the migration job status changes to `Failed`, and the substatus reflects the last status before failure. To troubleshoot an error, navigate to the failed migration job to view the error, and follow the steps outlined in the error message. To view more details about the error, navigate to Cloud Monitoring by using the link on the migration job. The logs are filtered to the specific migration job.

In the following table, you can find some examples of issues and how they can be solved:

Symptom | Possible causes | Things to try  
---|---|---  
Error message: `Length of LOB data ({size in bytes}) to be replicated exceeds configured maximum {size in bytes}.` | After CDC is enabled on your source database, SQL Server limits the maximum size of writes for columns of the `LOB` (Large Object) type. You attempted to write an object that is larger than the configured maximum.  | Adjust your limit limit by modifying the [ `max text repl size` parameter with the `sp_configure` stored procedure](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-text-repl-size-server-configuration-option).   
Error message: `Database Migration Service can't set up a tunnel to be connected to the bastion host`.  | Database Migration Service couldn't access the bastion host or the bastion host is not accepting connections. | Verify your forward SSH tunnel settings in the [ source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-source-connection-profile#fwd-ssh-connectivity) and the [ SSH tunnel server configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-source#forward-ssh-tunnel), and try again.  
Error message: `Database Migration Service can't connect to the database` or `Database Migration Service private connectivity error, cannot connect to the database`.  | Database Migration Service couldn't establish connectivity to the source SQL Server database.  | Verify that you can access the source database from your project. Check the settings related to your [ source connectivity configuration method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-source).   
Error message: `We're missing the necessary permissions to read from the source`.  | The dedicated migration account that Database Migration Service uses to connect to your source database is missing required permissions. | Verify the permissions. For more information, see [ Configure your source SQL Server database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-source-database).  
Error message: `Unable to connect to the destination database`.  | There was a problem connecting to the destination database. | Verify the settings in the destination PostgreSQL connection profile. For private connectivity, see the  Connection timeout, connection refused section.  
Error message: `database {database_name} does not exist`.  | Database Migration Service expects the destination database name and the username to match. | Ensure that the username indicated in the destination connection profile and the destination database name match. Either recreate the destination database, or create a different username that matches the destination database. For more information, see [ Configure your destination Cloud SQL for PostgreSQL database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database).   
Error message: `The following tables don't exist in the destination database: `{table_names}` ` | The listed tables that you are trying to migrate don't exist in the destination database. | Ensure you [ pull the schema snapshot, convert, and apply it to the destination database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/work-with-conversion-workspaces). Alternatively, [ modify the migration job settings](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-migration-jobs#edit-non-draft-job) and exclude the faulty table from the migration.  
Error message: `password authentication failed for user {username}`.  | The username or the password for the destination database are misconfigured. | Ensure that the destination Cloud SQL for PostgreSQL connection profile is configured correctly with the right username and password.  
Warning: `The following tables have foreign keys: {table_names}`.  | The tables listed exist in the destination database, but have foreign keys. | Database Migration Service doesn't replicate data in a transactional manner, so tables might be migrated out of order. If foreign keys are present, and a child table that uses a foreign key is migrated before its parent, you might encounter replication errors. To avoid such data integrity issues, skip foreign keys by using the `REPLICATION` option for the migration user. For more information, see [ Configure your destination Cloud SQL for PostgreSQL database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database)..  
Running a connectivity test returns the `[DATABASE] unable to connect to the destination database: EOF` error message.  | If you use Terraform to configure private connectivity for a non-PSC enabled destination instance, there might be issues with the `enable_proxy_protocol` setting. | Make sure that `enable_proxy_protocol` is set to `false` in the [ service attachment Terraform configuration file](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-dst-connection-private-ip#non-psc). Proxy protocol is supported only for HTTP servers such as NGINX and Apache. When using `gcloud` to create the Private Service Connect setup, the proxy protocol is disabled by default.  
**For private IP connectivity with non-PSC-enabled destinations** : Running a connectivity test fails or times out.  | Possibly caused caused by misconfigured routing within the Private Service Connect setup.  | This problem requires more advanced troubleshooting. For more information, see the  Connection timeout, connection refused section.  
  
## Connectivity issues

### Connection timeout, connection refused

Running the connectivity test fails or times out. This is most likely caused by misconfigured routing within the Private Service Connect setup. There can be several reasons for this problem.

**Possible cause:** There's a missing firewall rule that allows the Private Service Connect NAT CIDR range to access the Private Service Connect subnet where the bastion is located, specifically the bastion VM `nic0` interface.

**Things to try:** Make sure your organization policy doesn't restrict internal firewall rules, such as the `psc_sp_in_fw` firewall rule defined in the example Terraform script for [ configuring destination private IP connectivity for non-PSC enabled Cloud SQL instances](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-dst-connection-private-ip#non-psc).

**Possible cause:** The proxy is down. There is no listener on the supplied port, and therefore the connection hangs.

**Things to try:** You can try to establish an SSH connection to the bastion VM, and search for the proxy using the following command:

  * `netstat -tunalp | grep PORT`



Analyze the responses to the command:

  * If you get an empty response, the proxy is down. Try running the following commands:

`sudo su; cd /` and check if the Dante server is installed by running `sudo dpkg -s dante-server`:

    * If the proxy is installed, you get the following message:

`Status: install ok installed`

    * If the proxy isn't installed, the probable issue is a missing router. Add a router and check if you can download the proxy by running `apt-get install dante-server`.

To learn how to add a router, check how the `psc_sp_ex_router` and `psc_sp_ex_router_nat` resources are added in the `main.tf` file in [ Configuring destination private IP connectivity for non-PSC enabled Cloud SQL instances](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-dst-connection-private-ip#non-psc). 
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

    * If the commands fail to open a connection, try looking at the proxy logs to locate the root cause. The root cause can vary depending on the Cloud SQL instance setup.

    * If the connection is opened using telnet but hangs in the native client, the probable issue is the bastion IP address routing. On your VM, type `ip route` in the terminal. See if you can locate a routing rule that routes connections to the Cloud SQL instance private IP address using the secondary `nic` (`nic1`, the `DB_SUBNETWORK_GATEWAY` IP address).




**Possible cause:** The service attachment doesn't accept the endpoint connection coming from Database Migration Service. The service attachment holds a list of projects which are accepted, and the Database Migration Service project isn't included in the list.

**Things to try:** To resolve the issue, try either of the following:

  * In the Google Cloud console, go to **Private Service Connect**.

[ Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

On the **Published services** tab, accept the connection from Database Migration Service for your service attachment (if it's pending).

  * Add the requesting project to the allowlisted projects on the service attachment (if it's rejected).

    * For more information about adding an allowlisted project in Terraform, see [ Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_service_attachment#consumer_reject_lists).

    * For more information about adding an allowlisted project in `gcloud`, see [ gcloud reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/service-attachments/create#--consumer-accept-list).

If this doesn't solve the issue, recreate the connection profile.

  * [ Delete the connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-connection-profiles#delete_a_connection_profile) associated with the Private Service Connect connectivity, and recreate it.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
