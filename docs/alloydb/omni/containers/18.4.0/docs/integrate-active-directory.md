---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/integrate-active-directory/
title: Integrate Active Directory user support with AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:51:27.053401+00:00
---

# Integrate Active Directory user support with AlloyDB Omni  |  AlloyDB Omni using containers: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/integrate-active-directory/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/overview)



Send feedback 

#  Integrate Active Directory user support with AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/integrate-active-directory)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/integrate-active-directory)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/integrate-active-directory)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/integrate-active-directory)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/integrate-active-directory)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/integrate-active-directory)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/integrate-active-directory)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/integrate-active-directory)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/integrate-active-directory)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/integrate-active-directory)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/integrate-active-directory)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/integrate-active-directory)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/integrate-active-directory)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/integrate-active-directory)

This page describes how to integrate AlloyDB Omni with your existing [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) implementation so that you can use your existing usernames and passwords to access your AlloyDB Omni database. Active Directory integration provides Kerberos as the default authentication mechanism to communicate with AlloyDB Omni. For more information, see [Active Directory overview](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/active-directory-overview). 

Active Directory configuration in AlloyDB Omni is optional and is disabled by default. Only environments using Active Directory Server for authentication can use this configuration mechanism.

## Before you begin

Before you integrate Active Directory, make sure that you meet the following requirements:

  * Make sure that the Active Directory is set up.
  * Obtain the `REALM` of the Active Directory server.
  * Obtain the Key Distribution Center (KDC) hostname of the Active Directory server. The hostname is stored in the Docker images.
  * Obtain the admin server hostname of the Active Directory server. This hostname is stored in the Docker images.
  * Make sure that you have access to the Active Directory server so that you can generate a `.keytab` file.
  * Choose an Active Directory user to use for testing and signin.
  * Get a `.keytab` file from the existing Active Directory server.



### Obtain a .keytab file from the existing Active Directory server

To get a keytab from the Active Directory Server, follow these steps:

  1. Sign in as the administrator to the powershell terminal of the Active Directory server.
  2. Create a user called `postgres` by running the following command, or by using the Active Directory user interface.
    
    New-ADUser -Name "postgres" `
                   -SamAccountName "postgres" `
                   -UserPrincipalName "postgres@REALM" `
                   -Description "Service Account for AlloyDB Omni PostgreSQL Kerberos Authentication" `
                   -AccountPassword (Read-Host -AsSecureString "Set a strong password for the postgres service account") `
                   -Enabled $true `
                   -PasswordNeverExpires $true
      

  3. Generate a service principal keytab that maps to this Active Directory server.
    
    ktpass /princ postgres/ALLOYDB_HOST_NAME@REALM /Pass ChangeMe123 /mapuser postgres /crypto ALL /ptype KRB5_NT_PRINCIPAL /mapOp set /out C:\Users\Public\postgres.keytab
      

Where `<HOST>` is the fully qualified domain name of the server where you plan to deploy AlloyDB Omni—for example, `alloydb-server.ad.example.com`. You must configure the same host in the `krb5.conf` file in your domain realm mapping.

  4. Copy the keytab file to your linux machine.

**Important:** The keytab file is highly sensitive. It contains the secret key for your service. Transfer the keytab to your Linux machine using a secure method—like SCP or WinSCP—and make sure that its file permissions on the Linux server are highly restrictive—for example, that they are readable only by the PostgreSQL user.

## Enable Active Directory authentication

To enable Active Directory authentication in AlloyDB Omni, follow these steps, which include configuring the [Generic Security Service Application Program Interface](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface) (GSSAPI), which is an application programming interface that enables programs to access security services.

  1. Add the following entries to the `/var/lib/postgresql/data/pg_hba.conf` file, before the  
`host all all all scram-sha-256` entry.

     1. Run the following Docker command to add `gss` inside the container:
            
            docker exec CONTAINER_NAME sed -i 's;^host all all all scram-sha-256$;hostgssenc all all 0.0.0.0/0 gss map=gssmap\n&;' /var/lib/postgresql/data/pg_hba.conf
            

     2. Run the following Docker command to verify that the `pg_hba.conf` file is inside the container:
            
            docker exec CONTAINER_NAME cat /var/lib/postgresql/data/pg_hba.conf
            

     3. Verify that the following entry is in the file:
            
            hostgssenc all all 0.0.0.0/0 gss map=gssmap
            

For more information, see [The pg_hba.conf File](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).

  2. Copy the key tab file to the data directory inside the AlloyDB Omni image.
         
         docker cp PATH TO KEYTAB FILE CONTAINER_NAME:/var/lib/postgresql/data/alloydb.keytab
         docker exec CONTAINER_NAME chmod 600 /var/lib/postgresql/data/alloydb.keytab
         docker exec CONTAINER_NAME chown postgres:postgres /var/lib/postgresql/data/alloydb.keytab
         

**Note:** The keytab file must be owned by the PostgreSQL user and must have 600 permissions.

The keytab file is generated by Kerberos for the PostgreSQL server. To learn more about authentication, see [GSSAPI Authentication](https://www.postgresql.org/docs/current/gssapi-auth.html).

  3. Add an entry for the keytab file to the `/var/lib/postgresql/data/DATA_DIR/postgresql.conf` file.

     1. Run the following Docker command to add the entry inside the container:
            
            docker exec CONTAINER_NAME sed -i '$akrb_server_keyfile='"'"'/var/lib/postgresql/data/alloydb.keytab'"'" /var/lib/postgresql/data/postgresql.conf
            

     2. Run the following Docker command verify the `postgresql.conf` file inside the container:
            
            docker exec CONTAINER_NAME tail  /var/lib/postgresql/data/postgresql.conf
            

     3. Ensure that the following entry is in the file:
            
            krb_server_keyfile=/var/lib/postgresql/data/alloydb.keytab
            

For more information, see [krb_server_keyfile](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-KRB-SERVER-KEYFILE).

  4. Optional: Add entries to the `/var/lib/postgresql/data/DATA_DIR/pg_ident.conf` file.

When you use an external authentication system like GSSAPI, the name of the operating system user that initiated the connection might not be the same as the database user (role) that you want to use.

In this case, specify the system user-to-PostgreSQL user mapping in the `/var/lib/postgresql/data/DATA_DIR/pg_ident.conf` file:
         
         docker exec -it CONTAINER_NAME bash
         $ echo -e "
         gssmap              /^(.*)@EXAMPLE\.COM$     \1
         gssmap              /^(.*)@example\.com$     \1
         " | column -t | tee -a /var/lib/postgresql/data/pg_ident.conf
         

To implement username mapping, specify `map=gssmap` in the options field in the `pg_hba.conf` file.

For more information about ident-based authentication, see [Ident Maps](https://www.postgresql.org/docs/8.0/auth-methods.html#:%7E:text=19.2.4.3.%20Ident%20Maps).

  5. Reload the PostgreSQL configurations using the following command:
         
         docker exec -it CONTAINER_NAME psql -h localhost -U postgres
         psql (16.3)
         Type "help" for help.
         postgres=# select pg_reload_conf();
         




## Test Active Directory authentication

To verify that Active Directory authentication is working, follow these steps:

  1. Sign into Active Directory using `kinit`.
  2. Run the following `psql` command from the machine where you usually run `kinit`:
         
         root@4f6414ad02ef:/# kinit AD_USER_NAME
         Password for user1@YOUR.REALM:
         
         root@4f6414ad02ef:/# psql --h ALLOYDB_SERVER_HOST_NAME -U AD_USER_NAME
         psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
         GSSAPI-encrypted connection
         Type "help" for help.
         
         user1=#
         

**Note:** To ensure that Active Directory authentication is working, make sure that the user in Active Directory has a role in AlloyDB Omni, or ensure that the user has a valid mapping in the `pg_ident.conf` file.



## Disable Active Directory authentication

To disable Active Directory authentication in AlloyDB Omni, follow these steps, which disable the GSSAPI:

  1. Remove entries in the `pg_hba.conf` file that point to the `gss` authentication method:
         
         docker exec CONTAINER_NAME sed -i '/hostgssenc all all 0.0.0.0\/0 gss map=gssmap/d' /var/lib/postgresql/data/pg_hba.conf
         

  2. Reload the PostgreSQL configurations using the following command:
         
         docker exec -it CONTAINER_NAME psql -h localhost -U postgres
         psql (16.3)
         Type "help" for help.
         postgres=# select pg_reload_conf();
         




## What's next

  * [Integrate Active Directory group support with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/integrate-ad-group-support-alloydb-omni).
  * [Troubleshoot Active Directory in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/troubleshoot-active-directory-integration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
