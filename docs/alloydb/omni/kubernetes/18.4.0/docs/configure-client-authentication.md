---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-client-authentication/
title: Configure client authentication \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:18:54.122863+00:00
---

# Configure client authentication  |  AlloyDB Omni using the container orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-client-authentication/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/overview)



Send feedback 

#  Configure client authentication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-client-authentication)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-client-authentication)

This document describes how to configure client authentication on your Kubernetes-based AlloyDB Omni database cluster using the `UserDefinedAuthentication` custom resource (`alloydbomni.dbadmin.goog/v1`). You can customize client authentication behavior—such as restricting client subnets, enforcing SSL/TLS, specifying custom authentication methods, or configuring user mapping—by defining custom `pg_hba.conf` and `pg_ident.conf` entries independently of Active Directory setup. 

This document assumes that you're familiar with [applying Kubernetes manifest files](https://kubernetes.io/docs/concepts/overview/working-with-objects/) and using the `kubectl` command-line tool. For more information, see [Command line tool (kubectl)](https://kubernetes.io/docs/reference/kubectl/).

## Before you begin

To configure client authentication, you must have the following:

  * An AlloyDB Omni cluster deployed in a Kubernetes environment.
  * Database users and roles configured in the cluster.
  * The `kubectl` CLI installed and configured.



## Apply the custom resource manifest

Apply the following user-defined authentication custom resource manifest:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: UserDefinedAuthentication
    metadata:
      name: USER_DEFINED_AUTHENTICATION_NAME
      namespace: DB_CLUSTER_NAMESPACE
    spec:
      dbclusterRef:
        name: DB_CLUSTER_NAME
      pgHbaEntries:
        PG_HBA_ENTRIES
      pgIdentEntries:
        PG_IDENT_ENTRIES
    

Replace the following:

  * `USER_DEFINED_AUTHENTICATION_NAME`: the name of the `UserDefinedAuthentication` custom resource—for example, `DB_CLUSTER_NAME-client-auth`.
  * `DB_CLUSTER_NAMESPACE`: the Kubernetes namespace for this custom resource. The namespace must match the namespace of the database cluster.
  * `DB_CLUSTER_NAME`: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/deploy-kubernetes#create).
  * `PG_HBA_ENTRIES`: `pg_hba.conf` entries as a string list. These entries overwrite the default entries in `pg_hba.conf`. For example, to restrict connections to a specific subnet, use `- "host all all 192.168.1.0/24 scram-sha-256"`. For more information, see [The pg_hba.conf File](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).  PostgreSQL evaluates entries sequentially from top to bottom and uses the first matching rule. 
  * `PG_IDENT_ENTRIES`: (Optional) `pg_ident.conf` entries as a string list. To implement username mapping, specify `map=` in the options field in the `pg_hba.conf` file. If you don't need username mapping, omit the `pgIdentEntries` field from the manifest. For more information, see [User Name Maps](https://www.postgresql.org/docs/current/auth-username-maps.html).



## Verify the client authentication rules

To check the status of the `UserDefinedAuthentication` resource, run the following command:
    
    
    kubectl get userdefinedauthentication -n DB_CLUSTER_NAMESPACE
    

Verify that the `STATE` column displays `Ready`.

To view resource details and conditions, run the following command:
    
    
    kubectl describe userdefinedauthentication USER_DEFINED_AUTHENTICATION_NAME -n DB_CLUSTER_NAMESPACE
    

## Update client authentication rules

To update client authentication rules or user mappings, update `spec.pgHbaEntries` or `spec.pgIdentEntries` in your manifest file and re-apply it:
    
    
    kubectl apply -f CLIENT_AUTH_MANIFEST.yaml
    

The AlloyDB Omni operator dynamically reloads the PostgreSQL configuration (`pg_ctl reload`) without database pod restart or downtime.

## Delete client authentication rules

To delete the custom authentication rules and revert to the default authentication rules, run the following command:
    
    
    kubectl delete userdefinedauthentication USER_DEFINED_AUTHENTICATION_NAME -n DB_CLUSTER_NAMESPACE
    

When you delete the `UserDefinedAuthentication` resource, the AlloyDB Omni operator dynamically reloads `pg_hba.conf` (`pg_ctl reload`) to restore the default authentication rules without requiring a database pod restart.

## What's next

  * [Manage users and roles](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/database-users/manage-users)
  * [Manage password policies](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/manage-password-policy)
  * [`UserDefinedAuthentication` CRD reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/reference/kubernetes-crds-1.8.0/userdefinedauthentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
