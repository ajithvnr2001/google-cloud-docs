---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/run-connect/
title: Run and connect to AlloyDB Omni using RPM \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:41.882229+00:00
---

# Run and connect to AlloyDB Omni using RPM  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/run-connect/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Run and connect to AlloyDB Omni using RPM Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/run-connect)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/run-connect)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/run-connect)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/run-connect)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/run-connect)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/run-connect)



This page describes how to run and connect to AlloyDB Omni after you install it on your own machine.

## Before you begin

[Install AlloyDB Omni on your system](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/deploy-vm).

## Run AlloyDB Omni

Use the information in the following sections to start, check the status, and stop AlloyDB Omni.

### Optional: Update SELinux policies

If SELinux is enabled on your system and you modify certain Grand Unified Configuration (GUC) parameters in the `postgresql.conf` file, you must update your SELinux policies before starting the AlloyDB Omni service. Updating these policies prevents resource access denials that can make the database server unavailable or disrupt operations such as backups.

Running the `semanage` and `restorecon` commands requires the `policycoreutils-python-utils` package.

The following table lists the GUC parameters that require SELinux policy updates when you change them from their default values:

GUC parameter | Resource type | Impact if SELinux policy isn't updated | Resolution  
---|---|---|---  
[`port`](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-PORT) | Port | The database server fails to start and becomes unavailable. | Assign the `postgresql_port_t` label to the custom TCP port.  
[`external_pid_file`](https://www.postgresql.org/docs/18/runtime-config-file-locations.html#GUC-EXTERNAL-PID-FILE) | File | The database server remains available, but SELinux denies access to create the external PID file outside `/var/run/postgresql/`. | Assign the `postgresql_db_t` label to the custom PID file directory.  
[`unix_socket_directories`](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-UNIX-SOCKET-DIRECTORIES) | File | The database server fails to create the socket file and becomes unavailable. | Assign the `postgresql_db_t` label to the custom Unix socket directory.  
[`log_directory`](https://www.postgresql.org/docs/18/runtime-config-logging.html#GUC-LOG-DIRECTORY) | File | The database server fails to write logs and becomes unavailable. | Assign the `postgresql_db_t` label to the custom log directory.  
[`archive_command`](https://www.postgresql.org/docs/18/runtime-config-wal.html#GUC-ARCHIVE-COMMAND) | File | The database server remains available, but SELinux denies write access to the target directory, which can disrupt write-ahead log (WAL) archiving and backups. | Assign the `postgresql_db_t` label to the custom archive directory.  
  
#### Update the SELinux policy for a custom port

If you change the `port` parameter in the `postgresql.conf` file, run the following commands to allow AlloyDB Omni to bind to the custom TCP port:

  1. Add the `postgresql_port_t` label to the custom port:
         
         sudo /usr/sbin/semanage port -a -t postgresql_port_t -p tcp PORT_NUMBER

Replace `PORT_NUMBER` with the custom TCP port number—for example, `5433`.

  2. Confirm that the port policy is updated:
         
         sudo /usr/sbin/semanage port -l | grep postgresql_port_t




#### Update the SELinux policy for a custom directory

If you change the `external_pid_file`, `unix_socket_directories`, `log_directory`, or `archive_command` parameter in the `postgresql.conf` file to use a custom directory, run the following commands to apply the `postgresql_db_t` context to that directory:
    
    
    sudo /usr/sbin/semanage fcontext -a -t postgresql_db_t "DIRECTORY_PATH(/.*)?"
    sudo /sbin/restorecon -R -F DIRECTORY_PATH

Replace `DIRECTORY_PATH` with the full path to the custom PID file directory, Unix socket directory, log directory, or WAL archive directory.

### Start AlloyDB Omni
    
    
      sudo systemctl start alloydbomni18

### Optional: Enable automatic service restart

To enable automatic restart of the AlloyDB Omni service, do the following:

  1. Add the following configuration to the `/etc/systemd/system/alloydbomni18.service.d/override.conf` file.
         
         [Service]
             Restart=on-failure

  2. Reload the `systemd` manager configuration and restart the `alloydbomni18` service for the changes to take effect.
         
         sudo systemctl daemon-reload
         sudo systemctl restart alloydbomni18




### Check the status of AlloyDB Omni
    
    
       sudo systemctl status alloydbomni18

### Stop AlloyDB Omni
    
    
      sudo systemctl stop alloydbomni18

## Connect to AlloyDB Omni

The AlloyDB Omni RPM package also includes the psql client that lets you open an interactive SQL shell session with the database server.

You can also connect to AlloyDB Omni using the PostgreSQL-compatible software of your choice.

### Connect using bundled psql
    
    
      /usr/lib/postgresql/18/bin/psql -h localhost -U postgres

This command connects you to the server as the `postgres` user role, and displays a `postgres=#` command prompt. You can now [run psql commands](https://www.postgresql.org/docs/18/app-psql.html) and SQL queries.

To exit `psql`, run the `\q` command.

## Connect using your own applications

Any client application that works with PostgreSQL can also work with AlloyDB Omni, with no modification needed.

Use any PostgreSQL-compatible client or code library to connect to AlloyDB Omni.

After you connect to the database server, you can define, query, and modify your databases by sending DML and SQL queries through standard PostgreSQL communication protocols.

Because AlloyDB Omni runs within your own environment, you can control how you connect to AlloyDB Omni. You can allow or restrict network access to AlloyDB Omni according to the needs of your application, just as you would with an ordinary PostgreSQL server.

## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
