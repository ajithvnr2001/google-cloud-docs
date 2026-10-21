---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/integrate-ad-group-support-kubernetes-operator/
title: Integrate Active Directory group support on Kubernetes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:52.873839+00:00
---

# Integrate Active Directory group support on Kubernetes  |  AlloyDB Omni for Kubernetes: 16.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/integrate-ad-group-support-kubernetes-operator/

This page documents AlloyDB Omni version **16.8.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/overview)



Send feedback 

#  Integrate Active Directory group support on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.8.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/integrate-ad-group-support-kubernetes-operator)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/integrate-ad-group-support-kubernetes-operator)



**Preview —[AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to set up and manage Active Directory group-based authentication and authorization in AlloyDB Omni deployed on Kubernetes. Active Directory group-based support automates the management of PostgreSQL role memberships based on a user's group memberships in your Active Directory, which streamlines user management and makes sure that permissions are in sync. For more information, see [Active Directory overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/active-directory-overview).

This document assumes that you're familiar with [applying Kubernetes manifest files](https://kubernetes.io/docs/concepts/overview/working-with-objects/) and using the kubectl command-line tool. For more information, see [Command line tool (kubectl)](https://kubernetes.io/docs/reference/kubectl/).

## Active Directory integration workflow

Active Directory integration is implemented using a PostgreSQL extension (`google_pg_auth`) in the following workflow:

  1. User sign-in: a user authenticates to AlloyDB Omni using their standard Active Directory credentials using the Generic Security Services Application Programming Interface (GSSAPI).
  2. Automatic role creation: if a corresponding PostgreSQL role for the user doesn't exist, then the system automatically creates one—for example, `CREATE ROLE "user@REALM" WITH LOGIN;`.
  3. LDAP group check: the system securely connects to your Active Directory using LDAP to retrieve the user's current group memberships.
  4. Membership sync: the system compares the user's Active Directory groups to the mappings you configured.

     * If the user is in a mapped Active Directory group but isn't in the corresponding PostgreSQL group, the user is granted membership.
     * If the user isn't in a mapped Active Directory group but is in the corresponding PostgreSQL group, the user's membership is revoked.
  5. Sign-in complete: the user's connection is finalized, and they are signed into the database. The user's permissions are determined by the PostgreSQL roles that they belong to, which are in sync with their Active Directory group status.

This synchronization happens automatically at each user sign-in, which makes sure that PostgreSQL access rights reflect the current state of your Active Directory.




## Before you begin

Before you integrate Active Directory group support with AlloyDB Omni, make sure that you meet the following requirements.

  * GSSAPI Authentication: you must have GSSAPI-based authentication configured and operational for your AlloyDB Omni instance. For more information, see [Integrate Active Directory with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/integrate-active-directory-kubernetes-operator).
  * PostgreSQL group roles: you must manually create the PostgreSQL group roles that you intend to map to Active Directory groups, as shown in The following example:
        
        CREATE ROLE "postgres_developers";
        CREATE ROLE "postgres_read_only";
        

  * Permissions: you must manually assign the database permissions—for example, `SELECT` and `INSERT`—to these PostgreSQL group roles. The integration only manages membership, but it doesn't manage the privileges of the groups themselves, as shown in the following example:
        
        GRANT SELECT ON ALL TABLES IN SCHEMA sales TO postgres_read_only;
        GRANT USAGE ON SCHEMA finance TO postgres_developers;
        GRANT USAGE ON SCHEMA sales TO postgres_read_only;
        GRANT SELECT, INSERT ON finance.transactions TO postgres_developers;
        




## Configure Active Directory group support

To configure Active Directory group support, you must apply a `UserDefinedAuthentication` Custom Resource on your existing database cluster.

  1. Configure AlloyDB Omni using the LDAP server credentials. Apply the following user-defined authentication custom resource manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: UserDefinedAuthentication
         metadata:
          name: USER_DEFINED_AUTHENTICATION_NAME
          namespace: DB_CLUSTER_NAMESPACE
         spec:
          dbclusterRef: 
         name: DB_CLUSTER_NAME
          keytabSecretRef: 
         name: KEYTAB_SECRET_NAME
          pgHbaEntries:
            PG_HBA_ENTRIES
          pgIdentEntries:
            PG_IDENT_ENTRIES
         ldapConfiguration:
            enableGroupMapping: true
            ldapURI: LDAP_URI
            ldapBaseDN: LDAP_BASE_DN
            ldapBindDN: LDAP_BIND_DN
            cacheTTLSeconds: CACHE_TTL_SECONDS
            ldap_connection_timeout_ms: LDAP_CONNECTION_TIMEOUT
            ldapBindPasswordSecretRef:
              name: LDAP_PASSWORD_SECRET_REF
            ldapsCertificateSecretRef:
              name: LDAPS_CERT_SECRET_REF
         

Make the following replacements:

     * `USER_DEFINED_AUTHENTICATION_NAME`: the name of the UserDefinedConfiguration—for example, `DB_CLUSTER_NAME-ad-auth`.
     * `DB_CLUSTER_NAMESPACE`: the Kubernetes namespace for this backup plan. The namespace must match the namespace of the database cluster.
     * `DB_CLUSTER_NAME`: the name of your database cluster, which you assigned when you created it.
     * `LDAP_URI`: LDAP server URI—for exampole—`ldaps://ad.example.com:636`.
     * `LDAP_BASE_DN`: Base DN for LDAP searches. (e.g. DC=ad,DC=alloydb,DC=COM)
     * `LDAP_BIND_DN`: Distinguished Name (DN) for the LDAP bind user.
     * `LDAP_PASSWORD_SECRET_REF`: reference to the Kubernetes secret with the password LDAP password. The key of this secret must be `password`.
     * `LDAPS_CERT_SECRET_REF`: (Optional) Reference to the Kubernetes secret with the LDAPS certificate. The key of this secret must be `ldap.crt`.
     * `CACHE_TTL_SECONDS`: (Optional) Maximum time to wait before triggering an LDAP group membership sync in seconds. The default is 3600 seconds.
     * `LDAP_CONNECTION_TIMEOUT`: (Optional) LDAP connection timeout in milliseconds. The default is 5000 ms.

See the following example:
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: ldaps-secret
    type: Opaque
    data:
      ldap.crt: LDAPS_CERTIFICATE_CONTENT_BASE64_ENCODED
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: ldap-password-dbcluster-sample
    type: Opaque
    data:
      password: LDAPS_PASSWORD_CONTENT_BASE64_ENCODED
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: POSTGRES_PASSWORD
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: 16.8.0
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-keytab-dbcluster-sample
    type: Opaque
    data:
      krb5.keytab: |
    DUMMY_KEYTAB    
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: UserDefinedAuthentication
    metadata:
      name: dbcluster-sample-ad-auth
    spec:
      dbclusterRef: 
        name: dbcluster-sample
      keytabSecretRef: 
        name: db-keytab-dbcluster-sample
      pgHbaEntries:
        - hostgssenc all           all      0.0.0.0/0     gss
        - hostgssenc all           all      ::1/128       gss
        - hostssl all all 0.0.0.0/0 scram-sha-256
        - hostssl all all ::/0 scram-sha-256
      ldapConfiguration:
        enableGroupMapping: true
        ldapURI: ldaps://ad.alloydb.com:636
        ldapBaseDN: DC=ad,DC=alloydb,DC=COM
        ldapBindDN: read-only-admin@ad.alloydb.com
        cacheTTLSeconds: 60
        ldapBindPasswordSecretRef:
          name: ldap-password-dbcluster-sample
        ldapsCertificateSecretRef:
          name: ldaps-secret
    




## Manage group mappings

You can create and manage mappings between Active Directory groups and PostgreSQL roles using SQL functions.

### Sign into the cluster and load the extension

  * [Connect to AlloyDB Omni running on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/run-connect#connect-kubernetes).
        
        export DBPOD=`kubectl get pod --selector=alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -n DB_CLUSTER_NAMESPACE -o jsonpath='{.items[0].metadata.name}'`
        
        kubectl exec -ti $DBPOD -n DB_CLUSTER_NAMESPACE -c database -- psql -h localhost -U postgres
        postgres=# CREATE EXTENSION google_pg_auth;
        CREATE EXTENSION
        




### Create a group mapping

To map an Active Directory group to a PostgreSQL group role that you already created, use the `map_ad_group()` function.
    
    
    SELECT google_pg_auth.map_ad_group(ad_group_name TEXT, ad_group_sid TEXT, pg_role_name TEXT);
    

In the following example, the `ad-developers` Active Directory group is mapped to the `pg-developers` PostgreSQL role:
    
    
    SELECT google_pg_auth.map_ad_group('ad-developers', 'S-1-5-21-.....', 'postgres_read_only');
    

To retrieve the SID for a particular group in Active Directory, use the following command on your Active Directory server:
    
    
    C:\Users\Admin> Get-ADGroup -Identity ad-developers | select SID
                
                 SID
    -----------------------------------------------
    S-1-5-21-3168537779-1985441202-1799118680-1612
    

**Note:** The Active Directory group must be a security group and not a distribution group. For more information, see [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups).

### Remove a group mapping

To remove an existing mapping, use the `unmap_ad_group()` function, which stops synchronization for that group. The `unmap_ad_group()` function doesn't remove users from the PostgreSQL group if they are already members.
    
    
    SELECT google_pg_auth.unmap_ad_group(ad_group_sid TEXT, pg_role_name TEXT);
    

See the following example:
    
    
    SELECT google_pg_auth.unmap_ad_group('S-1-5-21-.....', ''postgres_read_only'');
    

### Create a user mapping

To map an individual Active Directory user to a PostgreSQL role that you already created, use the `map_ad_user()` function.
    
    
    SELECT google_pg_auth.map_ad_user(ad_username TEXT, pg_role_name TEXT);
    

For example, to map the `quinn@google.com` Active Directory user to the `pg-developers` PostgreSQL role, do the following:
    
    
    SELECT google_pg_auth.map_ad_user('quinn@google.com', ''postgres_read_only'');
    

### Remove a user mapping

To remove an existing mapping, use the `unmap_ad_user()` function.
    
    
    SELECT google_pg_auth.unmap_ad_user(ad_username TEXT, pg_role_name TEXT);
    

For example, to unmap the `quinn@google.com` Active Directory user from the `pg-developers` PostgreSQL role, do the following:
    
    
    SELECT google_pg_auth.unmap_ad_user('quinn@google.com', ''postgres_read_only'');
    

## Connect to the AlloyDB Omni database

Sign into the AlloyDB Omni database using the Active Directory user. You must have `kinit` enabled in the client where you are connecting.

In the following example, the `postgres-client` pod has `kinit` and `psql` installed and is configured to connect to the AlloyDB Omni cluster using the `psql` client.
    
    
    root@postgres-client:/# kinit AD_USER_NAME
    Password for user1REALM:
    
    root@postgres-client:/# psql -h ALLOYDB_SERVER_HOST_NAME -U AD_USER_NAME -d postgres
    psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
    GSSAPI-encrypted connection
    Type "help" for help.
    
    user1=# 
    

Your access in the AlloyDB Omni database is determined automatically based on the following:

  * Your current membership in Active Directory groups.
  * The mappings defined by the administrator between those Active Directory groups and the PostgreSQL roles.
  * The permissions granted by the administrator to those PostgreSQL roles.



If this is your first time connecting, your PostgreSQL user role (`your_ad_user@YOURDOMAIN.COM`) is created automatically.

Each time you sign in, the system checks your current Active Directory group memberships and updates your corresponding PostgreSQL role memberships to match. You don't need to take any specific action for this synchronization to occur.

### Database connection example

In the following example, a user Quinn is part of an Active Directory group named `ad_developers`. The administrator mapped `ad_developers` to a postgres role named `postgres_read_only`. This role has read access to a table named `sales`. When the user signs in, they can access the table.
    
    
    root@postgres-client:/# kinit quinnREALM
    Password for quinn@YOUR.REALM:
    
    root@postgres-client:/# psql -h ALLOYDB_SERVER_HOST_NAME -U quinnREALM -d postgres
    psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
    GSSAPI-encrypted connection
    Type "help" for help.
    
    postgres=# select * from sales;
    // Query will be run successfully
    

In the following example, Quinn is removed from the `ad_developers` group in Active Directory.
    
    
    root@postgres-client:/# kinit quinnREALM
    Password for quinn@YOUR.REALM:
    
    root@postgres-client:/# psql -h ALLOYDB_SERVER_HOST_NAME -U quinnREALM -d postgres
    psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
    GSSAPI-encrypted connection
    Type "help" for help.
    
    postgres=# select * from sales;
    // Query will fail
    

## Limitations

  * Manual group and permission management: this feature only automates user membership in existing PostgreSQL groups. The creation of those groups and the granting of their permissions is a manual administrative task.
  * Synchronization latency: membership is only synchronized when a user signs in. Any changes made to a user's group membership in Active Directory are only reflected in AlloyDB Omni at the user's next sign-in session.
  * Performance: the LDAP lookup adds a small amount of latency to the initial user sign-in process. Caching helps mitigate this latency for subsequent sign-ins within the configured time to live (`auth_cache_ttl_sec`).
  * Error handling: if the LDAP server is unreachable or if other errors occur during the synchronization process, AlloyDB Omni logs the error. However, the user's sign-in will still succeed since GSSAPI authentication was successful. Only the group membership sync for that session will fail.



## What's next

  * [Integrate Active Directory user support on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/integrate-active-directory-kubernetes-operator).
  * [Troubleshoot Active Directory integration in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/troubleshoot-active-directory-integration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
