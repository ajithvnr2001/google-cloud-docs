---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/troubleshoot-active-directory-integration/
title: Troubleshoot Active Directory integration in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 16.14.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:55:20.465530+00:00
---

# Troubleshoot Active Directory integration in AlloyDB Omni  |  AlloyDB Omni using containers: 16.14.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/troubleshoot-active-directory-integration/

This page documents AlloyDB Omni version **16.14.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/overview)



Send feedback 

#  Troubleshoot Active Directory integration in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.14.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/troubleshoot-active-directory-integration)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/troubleshoot-active-directory-integration)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/troubleshoot-active-directory-integration)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/troubleshoot-active-directory-integration)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/troubleshoot-active-directory-integration)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/troubleshoot-active-directory-integration)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/troubleshoot-active-directory-integration)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/troubleshoot-active-directory-integration)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/troubleshoot-active-directory-integration)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/troubleshoot-active-directory-integration)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/troubleshoot-active-directory-integration)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/troubleshoot-active-directory-integration)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/troubleshoot-active-directory-integration)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/troubleshoot-active-directory-integration)

This document describes errors you might encounter when you integrate Active Directory in AlloyDB Omni. Examples of errors and recommended fixes are also provided. 

## Active Directory integration with AlloyDB Omni fails

When Active Directory isn't working, follow these steps to resolve the issue:

  1. Verify the keytab file. Make sure that you can connect to the Active Directory server using the keytab that you obtained:
         
         kinit -kt PATH_TO_KEYTAB_FILE postgres/DBCLUSTER_HOST@REALM
         

  2. Verify the host.

Make sure that the host you used when you generated the keytab file is the same host in the psql command, as shown in the following example:
         
         KTPass /princ postgres/DBCLUSTER_HOST@REALM /Pass PASSWORD /mapuser postgres /crypto ALL /ptype KRB5_NT_Principal /out OUTPUT_PATH
         
         psql -h DBCLUSTER_HOST -d DB_NAME -U USERNAME@REALM
         

Make sure that `DBCLUSTER_HOST` is the same in both commands.

  3. Verify the `krb5.conf` file.

Verify the contents of the `krb5.conf` file on the client. Make sure that the `krb5.conf` file contents are correct for your configuration.
         
         cat /etc/krb5.conf
         

The following is the expected output:
         
         [libdefaults]
           default_realm = REALM
         [realms]
           REALM = {
               kdc = KDC_HOST
               admin_server = ADMIN_SERVER
           }
         [domain_realm]
           HOST_DOMAIN_1 = REALM
           HOST_DOMAIN_2 = REALM
         

  4. Verify the HBA entries and status.

     1. Run the following commands and send the logs to the [AlloyDB Omni product team](https://docs.google.com/forms/d/e/1FAIpQLSfLhBlJbtPJuvXcAS7WSF4J_CcCfO7tSWdCLqztAg1PhLX_vw/viewform).
            
            psql -h DBCLUSTER_HOST -U postgres -d postgres
            

`psql` prompts you for the `postgres` user's password:
            
            Password for user postgres:
            

`psql` returns the following output:
            
            psql (17.5 (Ubuntu 17.5-0ubuntu0.25.04.1), server 16.3)
            SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off, ALPN: none)
            Type "help" for help.
            

     2. Run the following command in the `psql` prompt:
            
            postgres=# table pg_hba_file_rules ;
            

Output similar to the following example is returned. 
            
            rule_number |            file_name             | line_number |  type   | database |     user_name      |  address  |                 netmask                 | auth_method |         options          |                        error
            -------------+--------------------------------------+-------------+---------+----------+--------------------+-----------+-----------------------------------------+-------------+--------------------------+-----------------------------------------------------
                  1 | /var/lib/postgresql/data/pg_hba.conf |           1 | host    | {all}    | {alloydbadmin}     | 127.0.0.1 | 255.255.255.255                         | trust       |                          |
                    | /var/lib/postgresql/data/pg_hba.conf |           2 | hostssl | {all}    | {alloydbadmin}     | ::1       | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | trust       |                          | hostssl record cannot match because SSL is disabled
                    | /var/lib/postgresql/data/pg_hba.conf |           3 | hostssl | {all}    | {alloydbpgbouncer} | 0.0.0.0   | 0.0.0.0                                 | cert        | {clientcert=verify-full} | hostssl record cannot match because SSL is disabled
                    | /var/lib/postgresql/data/pg_hba.conf |           4 | hostssl | {all}    | {alloydbpgbouncer} | ::1       | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | cert        | {clientcert=verify-full} | hostssl record cannot match because SSL is disabled
                    | /var/lib/postgresql/data/pg_hba.conf |           5 | hostssl | {all}    | {alloydbadmin}     | all       |                                         | reject      |                          | hostssl record cannot match because SSL is disabled
                    | /var/lib/postgresql/data/pg_hba.conf |           6 |         |          |                    |           |                                         |             |                          | invalid CIDR mask in address "0.0.0.0/1000"
                  2 | /var/lib/postgresql/data/pg_hba.conf |           7 | local   | {all}    | {all}              |           |                                         | trust       |                          |
            

  5. Review error messages in the `error` column, which can help you identify configuration issues.

  6. Print the debug level `krb5` logs.
         
         export KRB5_TRACE=/dev/stderr
         kinit AD_USER@REALM
         psql -h DBCLUSTER_HOST -d DB_NAME -U USERNAME@REALM
         

**Note:** For more information about this issue, open the `postgres.log` file.



## psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: FATAL: role "user2" does not exist

**Description**

This error occurs when a system user, who is trying to connect, doesn't have a PostgreSQL user created, or doesn't have a role mapped.

**Recommended fix**

Create a role in PostgreSQL with the required username, or add an entry for this user to the `pg_ident.conf` file.
    
    
    psql (16.3)
    Type "help" for help.
    
    postgres=# CREATE ROLE user2 WITH LOGIN;
    CREATE ROLE
    

## Server restart fails with error: "could not load /var/lib/postgresql/data/pg_hba.conf"

**Description**

The server restart failed because the `pg_hba.conf` contains invalid entries.

**Recommended fix**

Check the `pg_hba.conf` file for invalid entries.

## FATAL: LDAP group synchronization failed

**Description**

LDAP synchronization fails when the user tries to sign in.

**Recommended fix**

  1. Sign in as the `postgres` user and run the following:
         
         CREATE EXTENSION google_pg_auth;
         

  2. Check the `postgresql.log` file for information about why the LDAP sign-in failed.
         
         cat /obs/diagnostic/postgresql.log | grep google_pg_auth
         




## What's next

  * [Integrate Active Directory with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/integrate-active-directory)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
