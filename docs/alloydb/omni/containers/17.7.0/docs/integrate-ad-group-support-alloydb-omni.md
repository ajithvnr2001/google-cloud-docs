---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/integrate-ad-group-support-alloydb-omni/
title: Integrate Active Directory group support with AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:47:03.953101+00:00
---

# Integrate Active Directory group support with AlloyDB Omni  |  AlloyDB Omni using containers: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/integrate-ad-group-support-alloydb-omni/

This page documents AlloyDB Omni version **17.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/overview)



Send feedback 

#  Integrate Active Directory group support with AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/integrate-ad-group-support-alloydb-omni)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/integrate-ad-group-support-alloydb-omni)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/integrate-ad-group-support-alloydb-omni)



This page describes how to set up and manage Active Directory group-based authentication and authorization in AlloyDB Omni. Active Directory group-based support automates the management of PostgreSQL role memberships based on a user's group memberships in your Active Directory, which streamlines user management and makes sure that permissions are in sync.

For more information, see [Active Directory overview](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/active-directory-overview).

## Active Directory integration workflow

Active Directory integration is implemented using a PostgreSQL extension (`google_pg_auth`) as shown in the following workflow:

  1. User sign-in: a user authenticates to AlloyDB Omni using their standard Active Directory credentials using GSSAPI.
  2. Automatic role creation: if a corresponding PostgreSQL role for the user doesn't exist, the system automatically creates one—for example, `CREATE ROLE "user@REALM" WITH LOGIN;`.
  3. LDAP group check: the system securely connects to your Active Directory using the LDAP to retrieve the user's current group memberships.
  4. Membership sync: the system compares the user's Active Directory groups against the mappings that you configured. 
     * If the user is in a mapped Active Directory group but isn't in the corresponding PostgreSQL group, the user is granted membership.
     * If the user isn't in a mapped Active Directory group but is in the corresponding PostgreSQL group, the user's membership is revoked.
  5. Sign-in complete: the user's connection is finalized, and they are signed into the database. The user's permissions are determined by the PostgreSQL roles to which they belong, which are in sync with their Active Directory group status.



This synchronization happens automatically at each user sign-in, which makes sure that PostgreSQL access rights reflect the current state of your Active Directory.

## Before you begin

Before you integrate Active Directory group support with AlloyDB Omni, make sure that you meet the following requirements.

  * GSSAPI Authentication: GSSAPI-based authentication must be configured and operational for your AlloyDB Omni instance. For more information, see [Integrate Active Directory with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/integrate-active-directory).
  * PostgreSQL group roles: you must manually create the PostgreSQL group roles that you intend to map to Active Directory groups, as shown in The following example:
        
        CREATE ROLE 'postgres_developers';
        CREATE ROLE 'postgres_read_only';
        

  * Permissions: you must manually assign the database permissions—for example, `SELECT` and `INSERT`—to these PostgreSQL group roles. The integration only manages membership, but it doesn't manage the privileges of the groups themselves, as shown in the following example:
        
        GRANT SELECT ON ALL TABLES IN SCHEMA sales TO postgres_read_only;
        GRANT USAGE ON SCHEMA finance TO postgres_developers;
        GRANT USAGE ON SCHEMA sales TO postgres_read_only;
        GRANT SELECT, INSERT ON finance.transactions TO postgres_developers;
        




## Configure Active Directory group support

To configure Active Directory group support in AlloyDB Omni, you enable the `google_pg_auth` extension, provide your Active Directory details in the `postgresql.conf` file, and handle credentials securely.

  1. Provide the LDAP password.

You must provide the password for the `ldap_bind_dn` service account to the AlloyDB Omni container using the `AD_LDAP_PASSWORD` environment variable, as shown in the following example:
         
         docker run -d --name CONTAINER_NAME \
                   -e POSTGRES_PASSWORD=NEW_PASSWORD \
                   -e AD_LDAP_PASSWORD=AD_LDAP_PASSWORD \
                   -vDATA_DIR:/var/lib/postgresql/data \
                   -p HOST_PORT:5432 \
                   --restart=always \
                   google/alloydbomni:IMAGE_TAG
         

  2. Enable the `google_pg_auth` extension.

     1. In your `postgresql.conf` file, add or modify the following parameters to enable the extension and configure the LDAP connection. The `postgresql.conf` file is located in the data directory that you mounted when you started the AlloyDB Omni image.
            
            # ---------------------------------------------------------------------------
            # ALLOYDB ACTIVE DIRECTORY INTEGRATION SETTINGS
            # ---------------------------------------------------------------------------
            
            google_pg_auth.enable_auth = on
            google_pg_auth.ldap_uri = "AD_LDAP_SERVER_HOST"
            google_pg_auth.ldap_base_dn = AD_LDAP_BASE_DN
            google_pg_auth.ldap_bind_dn = AD_LDAP_BIND_DN
            google_pg_auth.auth_cache_ttl_sec = 3600
            google_pg_auth.allow_unmapped_ad_users: ALLOW_UNMAPPED_AD_USERS
            google_pg_auth.ldap_search_attribute: LDAP_SEARCH_ATTRIBUTE
            

Make the following replacements:

        * `AD_LDAP_SERVER_HOST`: the URI for your Active Directory LDAP server—for example, `ldap://ad-controller.example.com`.
        * `AD_LDAP_BASE_DN`: the Base Distinguished Name (DN) for performing LDAP searches (semicolon-separated for multiple bases) —for example, `DC=example,DC=com;DC=corp,DC=com`.
        * `AD_LDAP_BIND_DN`: the Distinguished Name (DN) of the Active Directory user account that AlloyDB Omni uses to connect and perform LDAP searches—for example, `setupadmin@ad-example.com`.
        * `auth_cache_ttl_sec` is the elapsed time until the data is cached by AlloyDB Omni per user before AlloyDB Omni attempts to contact the LDAP server again. The value of `auth_cache_ttl_sec` can range from a minimum of 60 seconds to a maximum of 86400 seconds (24 hours).
        * `ALLOW_UNMAPPED_AD_USERS`: (Optional) If set to `true`, users that are not a member of any mapped Active Directory group will also be allowed to login. The default is `false`.
        * `LDAP_SEARCH_ATTRIBUTE`: (Optional) LDAP attribute to search for. The default value is `userPrincipalName`.
     2. Add `google_pg_auth` to the `shared_preload_libraries` parameter in `postgresql.conf`.

     3. Add the following line to your `postgresql.conf` file:
            
            shared_preload_libraries='google_pg_auth,google_columnar_engine,google_job_scheduler,google_storage'
            

     4. Restart the database.
            
            docker restart CONTAINER_NAME
            

  3. Configure the LDAPS certificate.

To ensure a secure connection to your Active Directory server over LDAPS, you need a CA certificate.

Place your LDAPS certificate file at the following predefined location in the AlloyDB Omni image: `/etc/ldap/ldap.crt`.




## Manage group mappings

You can create and manage mappings between Active Directory groups and PostgreSQL roles using SQL functions.

### Sign into the cluster and load the extension
    
    
    docker exec -it CONTAINER_NAME psql -h localhost -U postgres
    postgres=# CREATE EXTENSION google_pg_auth;
    CREATE EXTENSION
    

### Create a group mapping

To map an Active Directory group to a PostgreSQL group role that you already created, use the `map_ad_group()` function:
    
    
    SELECT google_pg_auth.map_ad_group(ad_group_name TEXT, ad_group_sid TEXT, pg_role_name TEXT);
    

For example, to map the `ad-developers` Active Directory group to the `pg-developers` PostgreSQL role, use the following command:
    
    
    SELECT google_pg_auth.map_ad_group('ad-developers', 'S-1-5-21-.....', 'postgres_read_only');
    

To retrieve the SID for a particular group in Active Directory, use the following command on your Active Directory server:
    
    
    C:\Users\Admin> Get-ADGroup -Identity ad-developers | select SID
    
                 SID
    -----------------------------------------------
    S-1-5-21-3168537779-1985441202-1799118680-1612
    

**Note:** The Active Directory group must be a security group and not a distribution group. For more information, see [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups).

### Remove a group mapping

To remove an existing mapping, use the `unmap_ad_group()` function. This function stops synchronization for that group, but it doesn't remove users from the PostgreSQL group if they are already members.
    
    
    SELECT google_pg_auth.unmap_ad_group(ad_group_sid TEXT, pg_role_name TEXT);
    

See the following example:
    
    
    SELECT google_pg_auth.unmap_ad_group('quinn@google.com', 'postgres_read_only');
    

## Connect to the AlloyDB Omni database

Sign into the AlloyDB Omni database using the Active Directory user. You must enable `kinit` in the client where you are connecting.

In the following example, the `postgres-client` pod has `kinit` and `psql` installed and is configured to connect to the AlloyDB Omni cluster using the `psql` client.
    
    
    root@postgres-client:/# kinit AD_USER_NAME
    Password for user1REALM:
    
    root@postgres-client:/# psql -h ALLOYDB_SERVER_HOST_NAME -U AD_USER_NAME@REALM -d postgres
    psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
    GSSAPI-encrypted connection
    Type "help" for help.
    
    user1=#
    

Your access in the AlloyDB Omni database is automatically determined based on the following:

  * Your current membership in Active Directory groups.
  * The mappings defined by the administrator between those Active Directory groups and PostgreSQL roles.
  * The permissions granted by the administrator to those PostgreSQL roles.



If this is your first time connecting, your PostgreSQL user role (`your_ad_user@YOURDOMAIN.COM`) is created automatically.

Each time you sign in, the system checks your current Active Directory group memberships and updates your corresponding PostgreSQL role memberships to match. You don't need to take any specific action in order for this synchronization to occur.

### Database connection example

For example, assume that a user Quinn is part of an Active Directory group named `ad_developers`. The administrator mapped `ad_developers` to a postgres role named `pg_read_only`. This role has read access to a table named `sales`. When the user signs in, they can access the table.
    
    
    root@postgres-client:/# kinit quinn@REALM
    Password for quinn@YOUR.REALM:
    
    root@postgres-client:/# psql -h ALLOYDB_SERVER_HOST_NAME -U quinn@REALM -d postgres
    psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
    GSSAPI-encrypted connection
    Type "help" for help.
    
    postgres=# select * from sales;
    // Query will be run successfully
    

In the following example, Quinn is removed from the `ad_developers` group in Active Directory:
    
    
    root@postgres-client:/# kinit quinn@REALM
    Password for quinn@YOUR.REALM:
    
    root@postgres-client:/# psql -h ALLOYDB_SERVER_HOST_NAME -U quinn@REALM -d postgres
    psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
    GSSAPI-encrypted connection
    Type "help" for help.
    
    postgres=# select * from sales;
    // Query will fail
    

## Limitations

  * Manual group and permission management: this feature only automates user membership in existing PostgreSQL groups. The creation of those groups and the granting of their permissions remains a manual administrative task.
  * Synchronization latency: membership is only synchronized when a user signs in. Any changes made to a user's group membership in Active Directory are only reflected in AlloyDB Omni at the user's next sign-in session.
  * Performance: the LDAP lookup adds a small amount of latency to the initial user sign-in process. Caching helps mitigate this latency for subsequent sign-ins within the configured time to live duration (`auth_cache_ttl_sec`).
  * Error handling: if the LDAP server is unreachable, or if other errors occur during the synchronization process, AlloyDB Omni logs the error. However, the user's sign-in will still succeed since GSSAPI authentication was successful. Only the group membership sync for that session will fail.



## What's next

  * [Integrate Active Directory user support with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/integrate-active-directory).
  * [Troubleshoot Active Directory integration in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/troubleshoot-active-directory-integration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
