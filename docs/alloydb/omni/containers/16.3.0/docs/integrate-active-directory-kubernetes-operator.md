---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/integrate-active-directory-kubernetes-operator/
title: Integrate Active Directory with AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni for containers: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:25:54.391989+00:00
---

# Integrate Active Directory with AlloyDB Omni on Kubernetes  |  AlloyDB Omni for containers: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/integrate-active-directory-kubernetes-operator/

This page documents AlloyDB Omni version **16.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)



Send feedback 

#  Integrate Active Directory with AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/integrate-active-directory-kubernetes-operator)



**Preview —[AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to enable [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) integration on your Kubernetes-based AlloyDB Omni database cluster so that you can allow your existing Active Directory-based users to access your AlloyDB Omni database. Active Directory integration provides authorization using GSSAPI for users authenticated using the Kerberos mechanism to access AlloyDB Omni.

**Note:** Active Directory integration is only available in AlloyDB Omni version 16.3.0 and higher.

Active Directory configuration in AlloyDB Omni is optional and is disabled by default. Only environments using Active Directory Server for authentication can use this configuration mechanism.

This document assumes that you're familiar with [applying Kubernetes manifest files](https://kubernetes.io/docs/concepts/overview/working-with-objects/) and using the kubectl command-line tool. For more information, see [Command line tool (kubectl)](https://kubernetes.io/docs/reference/kubectl/).

## Before you begin

To enable Active Directory integration, you must have the following:

  * An AlloyDB Omni cluster deployed in a Kubernetes environment
  * An Active Directory server keytab



## Enable Active Directory authentication

To enable Active Directory authentication, run the following [Helm](https://helm.sh/) command:
    
    
    helm upgrade alloydbomni-operator PATH_TO_CHART -n alloydb-omni-system --set userDefinedAuthentication.enabled=true
    

The command returns the following output:
    
    
    Release "alloydbomni-operator" has been upgraded. Happy Helming!
    NAME: alloydbomni-operator
    LAST DEPLOYED: CURRENT_TIMESTAMP
    NAMESPACE: alloydb-omni-system
    STATUS: deployed
    REVISION: 2
    TEST SUITE: None
    

## Check Active Directory authentication status

To determine the status of Active Directory authentication, follow these steps:

  1. Get the current deployment `args` for the fleet controller and ensure that `enable-user-defined-authentication` is set to `true`, run the following commands:
         
         kubectl get deployment -n alloydb-omni-system fleet-controller-manager -o json | jq '.spec.template.spec.containers[0].args'
         
         [
           "--health-probe-bind-address=:8081",
           "--metrics-bind-address=127.0.0.1:8080",
           "--leader-elect",
           "--image-registry=gcr.io",
           ...
           **"--enable-user-defined-authentication=true"**
         ]
         

  2. Get the current deployment args for the local controller and ensure that `enable-user-defined-authentication` is set to `true` by running the following commands:
         
         kubectl get deployment -n alloydb-omni-system local-controller-manager -o json | jq '.spec.template.spec.containers[0].args'
         
         [
           "--health-probe-bind-address=:8081",
           "--metrics-bind-address=127.0.0.1:8080",
           "--leader-elect",
           "--deployment-platform=generic-k8s",
           "--enable-backup-from-standby=true",
           **"--enable-user-defined-authentication=true"**
         ]
         




## Configure Active Directory support

  1. Create and apply a config map using `pg_hba.conf` file entries:
         
         kubectl apply -f - 
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: pg-hba-config
         data:
           pg_hba_entries: |
             # Active Directory-based users
             hostgssenc all all 0.0.0.0/0    gss
             hostgssenc all all ::1/128      gss
             # Database-based users
             hostssl    all all 0.0.0.0/0  scram-sha-256
             hostssl    all all ::/0       scram-sha-256
         EOF
         

Modify these entries based on your requirements. These entries overwrite the default entries in `pg_hba.conf`. If you add an invalid configuration, users can't sign in.

In the preceding example, you added entries for GSS-based authentication followed by password-based authentication. This means that the user will be signed in using the GSS API. If this signin approach fails, then password-based authentication will be used as a fallback.

For more information, see [The pg_hba.conf File](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).

  2. Create and apply a secret with the keytab:
         
         kubectl apply -f - 
          apiVersion: v1
          kind: Secret
          metadata:
            name: db-keytab-dbcluster-sample
          type: Opaque
          data:
            krb5.keytab: |
             BASE64_ENCODED_KEYTAB
          EOF
          

**Note:** To obtain the base64-encoded keytab, use this example command: `cat postgres.keytab |base64.`
  3. Optional: Create and apply a config map using `pg_ident.conf` entries.
         
         kubectl apply -f - EOF
           apiVersion: v1
           kind: ConfigMap
           metadata:
             name: pg-ident-config
           data:
             pg_ident_entries: |  
         MAP_NAME /^(._)@YOUR.REALM$/        \1 MAP_NAME /^(._)@your.realm$/        \1
           EOF
           

To implement username mapping, specify `map=MAP_NAME` in the options field in the `pg_hba.conf` file.

For more information, see [Ident Maps](https://www.postgresql.org/docs/8.0/auth-methods.html#:%7E:text=19.2.4.3.%20Ident%20Maps).

  4. To enable Active Directory integration, add annotations to the DBCluster spec.

**Note:** Active Directory integration is only available in AlloyDB Omni version 16.3.0 and higher.
         
         kubectl apply -f - DB_CLUSTER_NAME
         type: Opaque
         data:
           DB_CLUSTER_NAME: "ENCODED_PASSWORD"
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: DB_CLUSTER_NAME
           annotations:
             dbs.dbadmin.goog.com/pg-hba-config-map: pg-hba-config
             dbs.dbadmin.goog.com/pg-ident-config-map: pg-ident-config
             dbs.dbadmin.goog.com/keytab-ref: db-keytab-dbcluster-sample
         spec:
           databaseVersion: "DB_VERSION"
           primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-DB_CLUSTER_NAME
             resources:
               memory: MEMORY_SIZE
               cpu: CPU_COUNT
               disks:
               - name: DataDisk
                 size: DISK_SIZE
         EOF
         




## Create database roles as an Active Directory user

  1. Create a role in your database that matches the Active Directory user. To create a role for your Active Directory user, connect to the cluster and run the following commands:
         
         username=# CREATE ROLE "USERNAME@REALM" WITH LOGIN;
         

  2. Sign into the database using the Active Directory user. You must have `kinit` enabled in the client where you are connecting.
         
         kubectl exec -it postgres -n DB_CLUSTER_NAMESPACE -- bash
         root:/# kinit USERNAME
         Password for USERNAME@REALM:
         
         root:/# psql -h HOSTNAME -d DB_NAME -U USERNAME@REALM
         psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 16.3)
         GSSAPI-encrypted connection
         Type "help" for help.
         

  3. Run SQL queries.
         
         username=# select * from ;
         




## Disable Active Directory authentication

To disable Active Directory authentication, run the following Helm command:
    
    
    helm upgrade alloydbomni-operator PATH_TO_CHART -n alloydb-omni-system --set userDefinedAuthentication.enabled=false
    

You can check the Active Directory authentication status.

The command returns the following output:
    
    
    Release "alloydbomni-operator" has been upgraded. Happy Helming!
    NAME: alloydbomni-operator
    LAST DEPLOYED: CURRENT_TIMESTAMP
    NAMESPACE: alloydb-omni-system
    STATUS: deployed
    REVISION: 2
    TEST SUITE: None
    

**Note:** When you enable Active Directory authentication using annotations, the authentication modifies the `pg_hba.conf` file, which remains in that modified state until restart. When this happens, trigger a restart of the pods to reset `pg_hba.conf`. You must trigger a restart because when you disables User Defined Authentication, the entries in `pg_hba.conf` aren't reset to the default ones until the pod restarts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
