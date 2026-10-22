---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/integrate-active-directory-kubernetes-operator/
title: Integrate Active Directory user support on Kubernetes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:58.925325+00:00
---

# Integrate Active Directory user support on Kubernetes  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/integrate-active-directory-kubernetes-operator/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Integrate Active Directory user support on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/integrate-active-directory-kubernetes-operator)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/integrate-active-directory-kubernetes-operator)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/integrate-active-directory-kubernetes-operator)

This document describes how to enable [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) integration on your Kubernetes-based AlloyDB Omni database cluster so that you can allow your existing Active Directory-based users to access your AlloyDB Omni database. Active Directory integration provides authorization using GSSAPI for users authenticated using the Kerberos mechanism to access AlloyDB Omni. 

For more information, see [Active Directory overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/active-directory-overview).

Active Directory integration is only available in AlloyDB Omni version 16.3.0 and higher.  You can also use the `UserDefinedAuthentication` custom resource independently to configure custom client authentication rules, such as IP subnet restrictions, SSL enforcement, and custom authentication methods. For more information, see [Configure client authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-client-authentication). 

This document assumes that you're familiar with [applying Kubernetes manifest files](https://kubernetes.io/docs/concepts/overview/working-with-objects/) and using the kubectl command-line tool. For more information, see [Command line tool (kubectl)](https://kubernetes.io/docs/reference/kubectl/).

## Before you begin

To enable Active Directory integration, you must have the following:

  * An AlloyDB Omni cluster deployed in a Kubernetes environment
  * An Active Directory server keytab



### Migrate from AlloyDB Omni Kubernetes operator 1.4.0 to 1.5.0

If you're using Active Directory Integration in AlloyDB Omni operator version 1.4.0 or earlier, you must migrate to AlloyDB Omni operator version 1.5.0.

To migrate to AlloyDB Omni operator version 1.5.0, follow these steps:

  1. [Upgrade the AlloyDB Omni operator to version 1.5.0](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-operator-version).
  2. Create a user defined authentication resource. 
     1. Create a new UserDefinedAuthentication resource manifest.
     2. Populate `spec.dbclusterRef` with the target DBCluster name.
     3. Populate `spec.keytabSecretRef` with the name of the keytab secret.
     4. Copy the existing `pg_hba.conf` rules that are relevant to the Active Directory and Kerberos authentication into the `spec.pgHbaEntries` field.
     5. Copy the existing `pg_ident.conf rules` (if any) into the `spec.pgIdentEntries` field.
     6. Apply this new manifest, for example, `kubectl apply -f user-auth-crd.yaml`.
  3. Remove the Preview Configuration & Redeploy Cluster. 
     1. In the DBCluster resource definition, remove all annotations that you previously used to configure Active Directory integration, for example, host based authentication (HBA) rules, ident rules, and keytab file annotation.
     2. Delete the `pg_hba` and `pg_ident` config maps that you created.
     3. Re-apply the updated DBCluster manifest.



## Configure Active Directory support

  1. Create and apply a secret with the keytab:
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: KEYTAB_SECRET_NAME
           namespace: DB_CLUSTER_NAMESPACE
         type: Opaque
         data:
           krb5.keytab: |
            KEYTAB_FILE_CONTENT
         

The following is an example command that generates a keytab on the Active Directory server:
         
         ktpass /princ postgres/DBCLUSTER_HOST@REALM /Pass PASSWORD /mapuser postgres /crypto ALL /ptype KRB5_NT_Principal /out OUTPUT_PATH
         

`ALLOYDB_HOST` is the host which points to the DBCluster or the DBCluster IP Address.

**Note:** To obtain the base64-encoded keytab, use a command like the following: `cat postgres.keytab | base64`.
  2. Apply the following user defined authentication custom resource manifest:
         
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
         

Replace the following:

     * `USER_DEFINED_AUTHENTICATION_NAME`: the name of the UserDefinedConfiguration, for example, `DB_CLUSTER_NAME-ad-auth`.
     * `DB_CLUSTER_NAMESPACE`: the Kubernetes namespace for this backup plan. The namespace must match the namespace of the database cluster.
     * `DB_CLUSTER_NAME`: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create).
     * `KEYTAB_SECRET_NAME`: the name of the keytab that you created.
     * `PG_HBA_ENTRIES`: `pg_hba.conf` entries as a string list. These entries overwrite the default entries in `pg_hba.conf`. If you add an invalid configuration, users can't sign in.

In the preceding example, you added entries for GSS-based authentication followed by password-based authentication. This means that the user is signed in using the GSS API. If this signin approach fails, then password-based authentication is used as a fallback.

For more information, see [The pg_hba.conf File](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).

     * `PG_IDENT_ENTRIES`: `pg_ident.conf` entries as a string list. To implement username mapping, specify `map=` in the options field in the `pg_hba.conf` file. For more information, see [Ident Maps](https://www.postgresql.org/docs/8.0/auth-methods.html#:%7E:text=19.2.4.3.%20Ident%20Maps).

See the following example:
           
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
              pgIdentEntries:
                - usermap  active_directory_user postgres_user
           




## Create database roles as an Active Directory user

  1. Create a role in your database that matches the Active Directory user. To create a role for your Active Directory user, [connect to the cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/run-connect) and run the following commands:
         
         username=# CREATE ROLE "USERNAME@REALM" WITH LOGIN;
         

  2. Sign in to the database using the Active Directory user. You must have `kinit` enabled in the client where you are connecting. In this example, the `postgres-client` pod has `kinit` and `psql` installed and is configured to connect to the AlloyDB Omni cluster using the `psql` client.
         
         kubectl exec -it postgres-client -n DB_CLUSTER_NAMESPACE -- bash
         root:/# kinit USERNAME
         Password for USERNAME@REALM:
         
         root:/# psql -h HOSTNAME -d DB_NAME -U USERNAME@REALM
         psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
         GSSAPI-encrypted connection
         Type "help" for help.
         

  3. Run SQL queries.
         
         username=# select * from TABLE_NAME;
         




## Disable Active Directory authentication

To disable Active Directory authentication, run the following Helm command:
    
    
    helm upgrade alloydbomni-operator PATH_TO_CHART -n alloydb-omni-system --set userDefinedAuthentication.enabled=false
    

The command returns the following output:
    
    
    Release "alloydbomni-operator" has been upgraded. Happy Helming!
    NAME: alloydbomni-operator
    LAST DEPLOYED: CURRENT_TIMESTAMP
    NAMESPACE: alloydb-omni-system
    STATUS: deployed
    REVISION: 2
    TEST SUITE: None
    

**Note:** When you enable Active Directory authentication, the authentication modifies the `pg_hba.conf` file, which remains in that modified state until restart. When this happens, trigger a restart of the pods to reset `pg_hba.conf`. You must trigger a restart because when you disable User Defined Authentication, the entries in `pg_hba.conf` aren't reset to the default ones until the pod restarts.

## What's next

  * [Configure client authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-client-authentication)
  * [Integrate Active Directory group support on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/integrate-ad-group-support-kubernetes-operator)
  * [Troubleshoot Active Directory integration in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/troubleshoot-active-directory-integration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
