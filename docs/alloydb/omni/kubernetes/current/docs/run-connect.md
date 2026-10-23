---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/run-connect/
title: Run and connect to AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:33.290294+00:00
---

# Run and connect to AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/run-connect/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Run and connect to AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/run-connect)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/run-connect)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/run-connect)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/run-connect)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/run-connect)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/run-connect)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/run-connect)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/run-connect)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/run-connect)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/run-connect)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/run-connect)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/run-connect)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/run-connect)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/run-connect)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/run-connect)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/run-connect)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/run-connect)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/run-connect)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/run-connect)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/run-connect)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/run-connect)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/run-connect)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/run-connect)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/run-connect)



This page describes how to run and connect to AlloyDB Omni after you [deploy it to your Kubernetes cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes).

The Kubernetes-specific instructions on this page assume basic familiarity with operating Kubernetes.

## Run AlloyDB Omni

The procedures you use to run AlloyDB Omni depend on whether you're running AlloyDB Omni on a Kubernetes cluster.

### Start AlloyDB Omni

Start a stopped database cluster by setting `isStopped` to `false` in its manifest definition.

You can perform this on the command line using `kubectl`:
    
    
      kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME \
      -p '{"spec":{"primarySpec":{"isStopped":false}}}' --type=merge  -n DB_CLUSTER_NAMESPACE

Replace the following:

  * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.
  * `DB_CLUSTER_NAMESPACE` (Optional): the namespace you where created this database cluster—for example, `my-db-cluster-namespace`.



### Check the status of AlloyDB Omni
    
    
      kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME  -n DB_CLUSTER_NAMESPACE

Replace the following:

  * `DB_CLUSTER_NAME`: the [name of your database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create).
  * `DB_CLUSTER_NAMESPACE` (Optional): the namespace where you created your [database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create).



### Stop AlloyDB Omni

To stop a database cluster, set `isStopped` to `true` in its manifest definition.

You can perform this on the command line using `kubectl`:
    
    
      kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -p '{"spec":{"primarySpec":{"isStopped":true}}}' --type=merge -n DB_CLUSTER_NAMESPACE

Replace the following:
    
    
    *   `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.
    *   `DB_CLUSTER_NAMESPACE` (Optional): the namespace where you created this database cluster—for example, `my-db-cluster-namespace`.
    

## Connect to AlloyDB Omni running on Kubernetes

The AlloyDB Omni Kubernetes operator allows connections to the database cluster from within the same Kubernetes cluster, optionally using certificates for authentication.

### Connect using the preinstalled `psql`

You can make a test connection using a `psql` client already installed on the pod running the database.

To do this, run the following commands:
    
    
    export DBPOD=`kubectl get pod --selector=alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -n DB_CLUSTER_NAMESPACE -o jsonpath='{.items[0].metadata.name}'`
    kubectl exec -ti $DBPOD -n DB_CLUSTER_NAMESPACE -c database -- psql -h localhost -U postgres

Replace `DB_CLUSTER_NAME` with the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create).

You can skip setting the `DB_CLUSTER_NAMESPACE`, if you created the database cluster in the default namespace.

After you enter the command, the database server prompts you for a password. Enter the password whose base64-encoded version you supplied as a Kubernetes secret when [creating the database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create). For example, if you created the database cluster with a secret of `Q2hhbmdlTWUxMjM=`, then the login password to use here is `ChangeMe123`.

The AlloyDB Omni operator connects you to the server as the `postgres` user role and displays a `postgres=#` command prompt. You can now [run `psql` commands](https://www.postgresql.org/docs/current/app-psql.html) and SQL queries.

To exit `psql`, run the `\q` command.

### Connect from a separate pod in the same cluster

The pod running the AlloyDB Omni database cluster allows connections from within the same Kubernetes cluster, by default. As a best practice, we recommend securing all connections to the database cluster using TLS.

To provide your own server TLS certificate, specify a certificate secret when configuring your database cluster. If you don't specify a certificate secret, then the AlloyDB Omni Kubernetes operator creates a TLS certificate secret for you, based on a certificate signed by a self-signed certificate authority. In either case, you can require your database client pod to require certificate validation on every connection, ensuring TLS security.

To establish secure database connections using TLS, perform the following actions:

  * In the manifest that defines the pod making the client connections, specify a TLS certificate secret. It can be one of the following:

    * A TLS certificate secret that you have already created in your Kubernetes cluster. For more information about working with TLS certificate secrets in Kubernetes, see [TLS Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets).

    * The default certificate secret that the AlloyDB Omni Kubernetes operator creates for you, named `DB_CLUSTER_NAME-ca-cert`, if you do not specify a TLS secret as part of your database cluster's manifest.

  * Whenever your client pod connects to the database cluster, it must define the following environment variables prior to establishing the connection:

    * Set `PGSSLMODE` to `"verify-ca"`.

    * Set `PGSSLROOTCERT` to the absolute path, on the client pod's file system, of the relevant `ca.crt` file.




The following example manifest shows how to configure a pod that installs the official PostgreSQL image, which includes the `psql` command-line client. The example presumes that you don't specify any TLS secret configuration in [the manifest that defines your database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create). Therefore, the AlloyDB Omni Kubernetes operator uses the default TLS secret, which is named `dbs-al-cert-DB_CLUSTER_NAME`.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: postgres
      namespace: DB_CLUSTER_NAMESPACE
    spec:
      containers:
      - image: "docker.io/library/postgres:latest"
        command:
          - "sleep"
          - "604800"
        imagePullPolicy: IfNotPresent
        name: db-client
        volumeMounts:
        - name: ca-cert
          mountPath: "/DB_CLUSTER_NAME-ca-cert"
          readOnly: true
      volumes:
      - name: ca-cert
        secret:
          secretName: dbs-al-cert-DB_CLUSTER_NAME
      restartPolicy: Always
    

Replace the following:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create).
  * `DB_CLUSTER_NAMESPACE` (Optional): the namespace where you created your database cluster.



You can now use the pod to securely connect to your database cluster using the following steps:

  1. Determine the internal IP address of your database cluster:
         
         kubectl get dbclusters.alloydbomni.dbadmin.goog -n DB_CLUSTER_NAMESPACE

The output resembles the following:
         
         NAME              PRIMARYENDPOINT   PRIMARYPHASE   DBCLUSTERPHASE
         DB_CLUSTER_NAME   IP_ADDRESS        Ready          DBClusterReady
         

Take note of `IP_ADDRESS`, and use it in the following step.

  2. Use `psql` to connect to your cluster from the client pod, setting the environment variables that enable and require TLS certificate verification:
         
         kubectl exec -it postgres -n DB_CLUSTER_NAMESPACE -- bash
         PGSSLMODE="verify-ca" PGSSLROOTCERT=/DB_CLUSTER_NAME-ca-cert/ca.crt psql -h IP_ADDRESS -p 5432 -U postgres -d postgres

Replace `IP_ADDRESS` with the internal IP address that you determined in the previous step.

  3. Optional. Customize the port on which the database accepts incoming connection requests. To override the default port `5432`, use the `port` attribute. Values must be between `1024` and `65535`.

**Note:** To use this feature, you must have AlloyDB Omni Kubernetes operator version 1.7.0 or later.

The following example shows the configuration for an AlloyDB Omni DBCluster resource when you customize the database port.
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: db-pw-dbcluster-sample
         type: Opaque
         data:
           dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: dbcluster-sample
         spec:
           databaseVersion: "18.4.0"
           primarySpec:
             **port : 6789**
             adminUser:
               passwordRef:
                 name: db-pw-dbcluster-sample
             resources:
               memory: 5Gi
               cpu: 1
               disks:
                - name: DataDisk
                  size: 10Gi
         




## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
