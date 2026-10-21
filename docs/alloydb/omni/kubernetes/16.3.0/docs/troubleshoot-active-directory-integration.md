---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/troubleshoot-active-directory-integration/
title: Troubleshoot Active Directory integration in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:43.175729+00:00
---

# Troubleshoot Active Directory integration in AlloyDB Omni  |  AlloyDB Omni for Kubernetes: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/troubleshoot-active-directory-integration/

This page documents AlloyDB Omni version **16.3.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)



Send feedback 

#  Troubleshoot Active Directory integration in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/troubleshoot-active-directory-integration)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/troubleshoot-active-directory-integration)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/troubleshoot-active-directory-integration)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/troubleshoot-active-directory-integration)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/troubleshoot-active-directory-integration)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/troubleshoot-active-directory-integration)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/troubleshoot-active-directory-integration)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/troubleshoot-active-directory-integration)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/troubleshoot-active-directory-integration)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/troubleshoot-active-directory-integration)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/troubleshoot-active-directory-integration)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/troubleshoot-active-directory-integration)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/troubleshoot-active-directory-integration)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/troubleshoot-active-directory-integration)



**Preview —[AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes errors you might encounter when you integrate Active Directory in AlloyDB Omni. Examples of errors and recommended fixes are also provided.

## Active Directory isn't working

**Description**

Active Directory isn't working in AlloyDB Omni, which is caused by incorrect `pg_hba.conf` entries. If the entries that you added to the `pg_hba.conf` file aren't valid, AlloyDB for PostgreSQL ignores those entries. As a result, the specified authentication mechanism won't work.

**Recommended fix**

To view the error message, including information about how to resolve the issue, sign into `psql` and run the following command:
    
    
    docker exec -it alloydb_docs psql -h localhost -U postgres
    psql (16.3)
    Type "help" for help.
    postgres=# table pg_hba_file_rules ;
     rule_number |              file_name               | line_number |  type   | database |     user_name      |  address  |                 netmask                 | auth_method |         options          |                        error
    -------------+--------------------------------------+-------------+---------+----------+--------------------+-----------+-----------------------------------------+-------------+--------------------------+-----------------------------------------------------
               1 | /var/lib/postgresql/data/pg_hba.conf |           1 | host    | {all}    | {alloydbadmin}     | 127.0.0.1 | 255.255.255.255                         | trust       |                          |
                 | /var/lib/postgresql/data/pg_hba.conf |           2 | hostssl | {all}    | {alloydbadmin}     | ::1       | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | trust       |                          | hostssl record cannot match because SSL is disabled
                 | /var/lib/postgresql/data/pg_hba.conf |           3 | hostssl | {all}    | {alloydbpgbouncer} | 0.0.0.0   | 0.0.0.0                                 | cert        | {clientcert=verify-full} | hostssl record cannot match because SSL is disabled
                 | /var/lib/postgresql/data/pg_hba.conf |           4 | hostssl | {all}    | {alloydbpgbouncer} | ::1       | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | cert        | {clientcert=verify-full} | hostssl record cannot match because SSL is disabled
                 | /var/lib/postgresql/data/pg_hba.conf |           5 | hostssl | {all}    | {alloydbadmin}     | all       |                                         | reject      |                          | hostssl record cannot match because SSL is disabled
                 | /var/lib/postgresql/data/pg_hba.conf |           6 |         |          |                    |           |                                         |             |                          | invalid CIDR mask in address "0.0.0.0/1000"
               2 | /var/lib/postgresql/data/pg_hba.conf |           7 | local   | {all}    | {all}              |           |                                         | trust       |                          |
    

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
    

## Server restart fails with error: "could not load /var/lib/postgresql/data/pg_hba.conf""

**Description**

The server restart failed because the `pg_hba.conf` contains invalid entries.

**Recommended fix**

Check the `pg_hba.conf` file for invalid entries.

## What's next

  * [Integrate Active Directory with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/integrate-active-directory)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
