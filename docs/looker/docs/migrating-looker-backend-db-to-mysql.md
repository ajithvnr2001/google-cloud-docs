---
url: https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql/
title: Migrating the Looker backend database to MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:47:34.985467+00:00
---

# Migrating the Looker backend database to MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Migrating the Looker backend database to MySQL Stay organized with collections  Save and categorize content based on your preferences. 

By default, Looker uses a HyperSQL in-memory database to store its configuration, users, and other data. On a busy instance, this database can grow to be gigabytes in size, which can lead to performance issues, Java memory pressure, and long startup times.

On a customer-hosted instance, we recommend that you replace the HyperSQL database with a full MySQL database backend when the internal HyperSQL database exceeds 600 MB in size. To check the size of the HyperSQL database, view the size of the `looker.script` file:
    
    
    cd looker
    cd .db
    ls -lah
    

If the `looker.script` file exceeds 600 MB in size, follow the following procedures to migrate to an external MySQL database.

**Note:** This procedure assumes a deployment in AWS EC2. For local deployments, systems should be sized comparably to the equivalent AWS instances. If you're updating Looker and migrating to MySQL, we recommend that you complete the Looker update before performing the migration to MySQL.

## Provision a MySQL instance and user

You can provision a MySQL 8.4.X (recommended) or MySQL 8.0.X instance to use as the backend. MySQL versions prior to 8.0 are not supported.

Looker 26.6 and later supports MySQL 8.4.X for the Looker backend database. For customer-hosted instances that use MySQL 8.0.X for the Looker backend database, it is recommended that you update to MySQL 8.4.X as soon as you update your Looker instance to version 26.6 or later. 

In AWS RDS, an instance of class `db.m5.large` is probably sufficient as a backend for a single Looker instance. Even though the database's actual usage will likely be in the 5-10 GB range, it's a good idea to provision 100-150 GB of SSD storage because the provisioned IOPS is based on the amount of storage requested.

### MySQL 8.4.X

Looker supports using MySQL 8.4.X as the internal database starting with Looker 26.6. For MySQL 8.4.X, you can use either of the following MySQL authentication plugins, as described in the following sections:

  * `caching_sha2_password`
  * `mysql_native_password`

**Note:** If you're upgrading your Looker backend from MySQL 8.0.X to MySQL 8.4.X, you can keep the database user that you created for MySQL 8.0.X. However, with MySQL 8.0.X, Looker requires that database users authenticate with `mysql_native_password`. So, if you want to keep the database user from MySQL 8.0.X, follow the instructions to provision MySQL 8.4.X with `mysql_native_password` so that your existing user can still authenticate. Otherwise, if you want to create a new user when you provision MySQL 8.4.X, you can provision the MySQL instance and create a new user with either the `caching_sha2_password` or the `mysql_native_password` authentication plugin.

#### Using `caching_sha2_password`

In MySQL 8.4.X, the default authentication plugin is [`caching_sha2_password`](https://dev.mysql.com/doc/refman/8.4/en/caching-sha2-pluggable-authentication.html). Looker provides two ways to use the `caching_sha2_password` plugin:

  1. **When using an SSL connection for the internal database:** No RSA public key is needed. Looker securely connects to the database with the user credentials provided. Refer to the Create a database credentials file section on this page to set up an SSL connection to your database.
  2. **If not connecting with SSL enabled:** Looker by default uses the [`--get-server-public-key`](https://dev.mysql.com/doc/refman/8.4/en/connection-options.html#option_general_get-server-public-key) option to connect to the internal database when the `caching_sha2_password` plugin is used by the user account provided to Looker. Ensure that the network environment is secured if SSL is not enabled.

**Note:** Specifying a local file as an RSA public key for connection is not supported by Looker.

For either way of using the `caching_sha2_password` plugin, set up the user by issuing the following statement:
    
    
    CREATE USER 'DB_username' IDENTIFIED WITH caching_sha2_password BY 'password';
    

Replace the following:

  * DB_username: username
  * password: unique, secure password



#### Using `mysql_native_password`

Looker works with the [`mysql_native_password`](https://dev.mysql.com/doc/refman/8.4/en/native-pluggable-authentication.html) plugin to authenticate to MySQL databases through the JDBC driver. For MySQL 8.4.X to work with the `mysql_native_password` plugin, you must take the following additional steps:

  1. Configure the MySQL database to [enable the `mysql_native_password` plugin](https://dev.mysql.com/doc/refman/8.4/en/native-pluggable-authentication.html#native-pluggable-authentication-installation). This can be done in multiple ways, depending on how your MySQL database is deployed and what type of access you have to the configuration:

     1. Start the MySQL server with `--mysql-native-password=ON`.
     2. Set the property in the [`my.cnf`](https://dev.mysql.com/doc/refman/8.4/en/option-files.html) configuration file:
            
            [mysqld]
            mysql_native_password=ON
            

     3. If the MySQL instance is hosted on Google Cloud, AWS, or Azure, the `mysql_native_password` plugin should be enabled automatically. Refer to your provider documentation for detailed instructions.

  2. Create the user:
         
         CREATE USER 'DB_username' IDENTIFIED WITH mysql_native_password BY 'password';
         

Replace the following:

     * DB_username: username
     * password: unique, secure password



### MySQL 8.0.X

In MySQL 8.0.X, the default authentication plugin is `caching_sha2_password`. Looker uses the `mysql_native_password` plugin to attempt to authenticate to MySQL databases through the JDBC driver. For MySQL 8.0.X to work properly, you must take the following additional steps:

  1. Configure the MySQL database to use the `mysql_native_password` plugin. This can be done in multiple ways, and will depend on how your MySQL 8 database is deployed and what type of access you have to the configuration:

     * Start the process with the flag `--default-auth=mysql_native_password`

     * Set the property in the [`my.cnf`](https://dev.mysql.com/doc/refman/8.0/en/option-files.html) configuration file:
           
           [mysqld]
           default-authentication-plugin=mysql_native_password
           

     * If your database instance is hosted through AWS RDS, set the `default_authentication_plugin` parameter through an RDS Parameter Group that is applied to this database instance.

  2. Create the user:
         
         CREATE USER 'DB_username' IDENTIFIED WITH mysql_native_password BY 'password';
         

Replace the following:

     * DB_username: username
     * password: unique, secure password



## Tune MySQL

Adjust the following settings on your MySQL instance.

### Increase maximum packet size

MySQL's default `max_allowed_packet` size is too small for database migration and can cause the migration to fail with a [`PACKET_TOO_LARGE`](https://dev.mysql.com/doc/refman/8.4/en/packet-too-large.html) error. Set [`max_allowed_packet`](https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_max_allowed_packet) to the maximum allowed value of `1073741824`:
    
    
    max_allowed_packet = 1073741824
    

### Set temporary table algorithm

MySQL 8 handles internal temporary tables differently than previous versions. The default settings can cause problems running some of the queries needed for Looker to run, especially for Looker instances with many users and projects. The best practice is to set the following global server setting:
    
    
    internal_tmp_mem_storage_engine = MEMORY
    

### Configure character sets

Set the following default parameters to use UTF8mb4, which supports UTF8 character sets. See the article [In MySQL, never use "utf8". Use "utf8mb4".](https://medium.com/@adamhooper/in-mysql-never-use-utf8-use-utf8mb4-11761243e434) for information about why we recommend the use of UTF8mb4 — not UTF8 — with MySQL.
    
    
    character_set_client = utf8mb4
    character_set_results = utf8mb4
    character_set_connection = utf8mb4
    character_set_database = utf8mb4
    character_set_server = utf8mb4
    collation_connection = utf8mb4_general_ci
    collation_server = utf8mb4_general_ci
    

On Amazon RDS instances, you apply this setting by creating or modifying a parameter group and editing the appropriate settings. We recommend that you copy the current parameter group and make the changes on the copy, especially if you are sharing parameter groups across several RDS instances. After saving the parameter group, apply it to the RDS instance. A reboot may be required.

## Set your replica scheme

Looker relies on functionality that necessitates a `mixed` or `row` binlog. If you are hosting your own MySQL instance, set your `binlog_format` to `mixed` or `row` by issuing one of the following commands:
    
    
    SET GLOBAL binlog_format = 'MIXED';
    

or
    
    
    SET GLOBAL binlog_format = 'ROW';
    

## Create a database and grant user permission

Create a database on the database instance: 
    
    
    create database DB_name default character set DB_charset default collate DB_collation;
    

Then grant permissions to the user that you created when you provisioned the MySQL instance and user:
    
    
    grant all on DB_name.* to 'DB_username'@'%';
    grant all on looker_tmp.* to 'DB_username'@'%';
    

Replace the following:

  * DB_name: database name
  * DB_charset: the character set that matches the RDS instance param group settings (for true UTF8 support, we recommend `utf8mb4`)
  * DB_collation: the collation that matches the RDS instance param group settings (for true UTF8 support, we recommend `utf8mb4_general_ci`)
  * DB_username: username



The `looker_tmp` database on the last line doesn't have to actually exist, but the `grant` statement is needed for internal reporting.

## Create a database credentials file

Looker needs to know which MySQL database to talk to and which credentials to use. In the Looker directory, create a file named `looker-db.yml` with the following contents, replacing DB_hostname, DB_username, DB_password, and DB_name with values for your database:
    
    
    dialect: mysql_8
    host: DB_hostname
    username: DB_username
    password: DB_password
    database: DB_name
    port: 3306
    

If your MySQL database requires an SSL connection, add the following line to `looker-db.yml`:
    
    
    ssl: true
    

If you also want to enable verification of the SSL certificate, add the following line to `looker-db.yml`:
    
    
    verify_ssl: true
    

Optionally, you can also specify any other additional JDBC parameters that are supported by the [MariaDB JDBC Driver](https://mariadb.com/kb/en/about-mariadb-connector-j/) by adding `jdbc_additional_params`. For example, if you need to use a specific Trust Store file, you can add the following parameter to the MySQL JDBC connection string:
    
    
    jdbc_additional_params: trustStore=/path/to/my/truststore.jks&keyStore=/path/to/my/keystore.jks
    

For customer-hosted installations, you can optionally specify the maximum number of connections that Looker can establish with your database by adding `max_connections`. For example, to limit the number of concurrent connections to your database to 10, add the following:
    
    
    max_connections: 10
    

**Important:** Follow best-practice security considerations when saving credentials to a file. Ideally, set the `looker-db.yml` file permissions to 600, owned by the Linux "user" account under which the Looker application is executed. This file should never be checked into a Git repository.

Under Looker's encryption scheme, all sensitive data in the database is encrypted at rest. Even if someone were to gain access to plaintext database credentials and access the database, Looker encrypts or hashes sensitive data before storing. This applies to elements such as passwords, analytics database credentials, and query cache. However, if you don't want to store the cleartext password for this configuration in the `looker-db.yml` file on disk, you can configure the environment variable `LOOKER_DB` to contain a list of keys and values for each line in the `looker-db.yml` file. For example:
    
    
    export LOOKER_DB="dialect=mysql_8&host=localhost&username=root&password=&database=looker&port=3306"
    

**Important:** Limit use of your MySQL user account to the IP address used by your Looker server.

## Back up the `.db` directory

Back up the `.db` directory, which contains the files needed to build the in-memory HyperSQL database, in case you need to restore HyperSQL:
    
    
    cp -r .db .db-backup
    tar -zcvf db-backup.tar.gz ./.db-backup
    

## Migrate the database

Migrating the database to MySQL can take hours on a medium or large instance, especially if the HyperSQL database is 1 GB or more. We recommend that you temporarily upgrade the EC2 instance to an `m5.2xlarge` (with 32 GB RAM to allow the 26 GB heap specified in the steps) during the migration, which reduces the time required to ~10 minutes.

  1. On the Looker host:
         
         cd looker
         ./looker stop
         vi looker
         

  2. In the Looker startup script, make a new second line in the file:
         
         exit
         

  3. Stop the instance in the AWS console. Once it stops, change the EC2 instance size to `m5.2xlarge`. Then start the instance back up again.

  4. SSH to the host as the Looker user. First make sure Java isn't running; then run:
         
         cd looker
         java -Xms26000m -Xmx26000m -jar looker.jar migrate_internal_data  looker-db.yml
         

When running the `migrate_internal_data` step, `libcrypt` may not be found and a stack trace will appear, starting with this:
         
         NotImplementedError: getppid unsupported or native support failed to load
         ppid at org/jruby/RubyProcess.java:752
         ppid at org/jruby/RubyProcess.java:749
         

If this happens, set the `LD_LIBRARY_PATH` manually before executing the Java command:
         
         export LD_LIBRARY_PATH=$HOME/looker/.tmp/:$LD_LIBRARY_PATH
         

  5. Once that successfully completes, stop the instance from the AWS console.

  6. You can now restore the instance to its original size.

  7. Start the instance again.




## Start Looker

  1. Edit the Looker startup script and delete the `exit` line that you added earlier.

  2. Ensure that there are no arguments defined in `LOOKERARGS` in the startup script. Instead, any arguments should move to [the `lookerstart.cfg` file](https://docs.cloud.google.com/looker/docs/startup-options#making_startup_options_permanent) so that they won't be overwritten by new versions of the startup script. Save and exit the startup script.

  3. Edit `lookerstart.cfg`. It should look similar to the following:
         
         LOOKERARGS="-d looker-db.yml"
         

If there were any other arguments in the Looker startup script, add them to the `lookerstart.cfg` file.

  4. Archive the `.db` directory, if it is not archived already.
         
         mv .db .db-backup
         tar -zcvf db-backup.tar.gz ./.db-backup
         rm -rf ./.db-backup/
         

  5. Start Looker:
         
         ./looker start
         




## Verify that Looker is using the new database

If Looker is successfully using the backend MySQL, you should see network connections between the Looker instance and the new database instance. To check this, run the following command on the Looker instance:
    
    
    netstat -na | grep 3306
    

You should see some connections to the database instance. The following is a sample output, showing a DB instance at IP address `10.0.3.155`:
    
    
    looker@instance1:~$ netstat -na | grep 3306
    tcp6       0      0 10.0.5.131:56583        10.0.3.155:3306         ESTABLISHED
    tcp6       0      0 10.0.5.131:56506        10.0.3.155:3306         ESTABLISHED
    tcp6       0      0 10.0.5.131:56582        10.0.3.155:3306         ESTABLISHED
    tcp6       0      0 10.0.5.131:56508        10.0.3.155:3306         ESTABLISHED
    

## Backing up Looker

After you migrate to a MySQL backend, Looker's automated S3 backups will no longer function. We recommend at least nightly backups of the MySQL database along with nightly file system backups of the Looker working directory. The `looker/log/` directory may be excluded from the file system backups. See the [Creating backups](https://docs.cloud.google.com/looker/docs/creating-backups) documentation page for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
