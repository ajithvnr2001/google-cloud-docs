---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/use-connection-pooler-kubernetes/
title: Use the PgBouncer connection pooler \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:56:57.641624+00:00
---

# Use the PgBouncer connection pooler  |  AlloyDB Omni for Kubernetes: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/use-connection-pooler-kubernetes/

This page documents AlloyDB Omni version **15.13.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/overview)



Send feedback 

#  Use the PgBouncer connection pooler Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/use-connection-pooler-kubernetes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/use-connection-pooler-kubernetes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/use-connection-pooler-kubernetes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/use-connection-pooler-kubernetes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/use-connection-pooler-kubernetes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/use-connection-pooler-kubernetes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/use-connection-pooler-kubernetes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/use-connection-pooler-kubernetes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/use-connection-pooler-kubernetes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/use-connection-pooler-kubernetes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/use-connection-pooler-kubernetes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/use-connection-pooler-kubernetes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/use-connection-pooler-kubernetes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/use-connection-pooler-kubernetes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/use-connection-pooler-kubernetes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/use-connection-pooler-kubernetes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/use-connection-pooler-kubernetes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/use-connection-pooler-kubernetes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/use-connection-pooler-kubernetes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/use-connection-pooler-kubernetes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/use-connection-pooler-kubernetes)



The information on this page applies only to AlloyDB Omni for Kubernetes. It does not apply to AlloyDB Omni for containers.

This page describes how to enable and use the PgBouncer connection pooler for AlloyDB Omni using the AlloyDB Omni Kubernetes operator.

Many applications, especially web applications, open and close database connections frequently, which can put a significant load on the database instance. [PgBouncer](https://www.pgbouncer.org/) helps reduce instance load by managing connections more efficiently. By reusing connections, PgBouncer minimizes the number of connections to the database instance, freeing up resources on the instance.

## Create a PgBouncer service

The AlloyDB Omni Kubernetes operator lets you create a dedicated PgBouncer service for your database. You can then access the database through the PgBouncer service to benefit from connection pooling.

There is a dedicated custom resource definition (CRD) for configuring your PgBouncer service as needed.

To create a PgBouncer service for your database, follow these steps:

  1. Create a `PgBouncer` custom resource in your Kubernetes cluster as follows:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: PgBouncer
         metadata:
           name: PGBOUNCER_NAME
         spec:
           dbclusterRef: DB_CLUSTER_NAME
           allowSuperUserAccess: true
           podSpec:
             resources:
               memory: 1Gi
               cpu: 1
             image: "gcr.io/alloydb-omni/operator/g-pgbouncer:1.4.0"
           parameters:
             pool_mode: POOL_MODE
             ignore_startup_parameters: IGNORE_STARTUP_PARAMETERS
             default_pool_size: "DEFAULT_POOL_SIZE"
             max_client_conn: "MAXIMUM_CLIENT_CONNECTIONS"
             max_db_connections: "MAXIMUM_DATABASE_CONNECTIONS"
           serviceOptions:
             type: "ClusterIP"

Replace the following:

     * `PGBOUNCER_NAME`: the name of your PgBouncer custom resource.
     * `DB_CLUSTER_NAME`: the name of your AlloyDB Omni database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes#create).
     * `POOL_MODE`: specifies when a database connection can be reused by other clients. Set the parameter to one of the following: 
       * `session`: database connection is released back to the pool after client disconnects. Used by default.
       * `transaction`: database connection is released back to pool after transaction finishes.
       * `statement`: database connection is released back to pool after query finishes. Transactions spanning multiple statements are disallowed in this mode.
     * `IGNORE_STARTUP_PARAMETERS`: specifies parameters that PgBouncer does not allow so that they are ignored during startup—for example, `extra_float_digits`. For more information, see [PgBouncer configuration](https://www.pgbouncer.org/config.html#generic-settings).
     * `DEFAULT_POOL_SIZE`: the number of database connections to allow per user-database pair—for example, `8`.
     * `MAXIMUM_CLIENT_CONNECTIONS`: the maximum number of client connections—for example, `800`.
     * `MAXIMUM_DATABASE_CONNECTIONS`: the maximum number of database connections—for example, `160`.
  2. Apply the manifest:
         
         kubectl apply -f PATH_TO_MANIFEST -n NAMESPACE

Replace PATH_TO_MANIFEST with the path to your manifest file—for example, `/fleet/config/pgbouncer.yaml`.

  3. To verify that the PgBouncer object you created is ready, execute the following query:
         
         kubectl get pgbouncers.alloydbomni.dbadmin.goog PGBOUNCER_NAME  -n NAMESPACE -w
         

Replace `NAMESPACE` with the name of the Kubernetes namespace for your PgBouncer object.

The output is similar to the following:
         
         NAMESPACE   NAME          ENDPOINT        STATE
         dbv2        mypgbouncer
         dbv2        mypgbouncer
         dbv2        mypgbouncer
         dbv2        mypgbouncer                   WaitingForDeploymentReady
         dbv2        mypgbouncer                   Acquiring IP
         dbv2        mypgbouncer   10.138.15.231   Ready
         




## Connect to the connection pooler endpoint

You can connect to the PgBouncer connection pooler from inside or outside a Kubernetes cluster.

### Connect from within a Kubernetes cluster

To connect to the connection pooler endpoint using the `psql` client, follow these steps:

  1. Create a Pod as follows:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: postgres
         spec:
           containers:
           - image: "docker.io/library/postgres:latest"
             command:
              - "sleep"
              - "604800"
             name: db-client
         

  2. Apply the manifest:
         
         kubectl apply -f PATH_TO_MANIFEST -n NAMESPACE
         

  3. Connect to the containerized application:
         
         kubectl exec -it postgres -n NAMESPACE -- bash
         

  4. Verify the SSL connection to the PgBouncer endpoint using the `psql` client:
         
         export PGSSLMODE="require"; psql -h HOST -d postgres -U postgres -p PORT
         

Replace the following:

     * `HOST`: the connection pooler endpoint that you obtain using `kubectl get pgbouncers.alloydbomni.dbadmin.goog -n NAMESPACE` command. If PgBouncer isn't exposed as a service, use its IP address.
     * `PORT`: the port PgBouncer listens on.

The terminal window displays `psql` login text that ends with a `postgres=#` prompt.




### Connect from outside a Kubernetes cluster

To access the PgBouncer connection pooler from outside a Kubernetes cluster, set the `type` field in the `serviceOptions` attribute to `LoadBalancer`, which creates a `loadbalancer` service.

  1. Create a `PgBouncer` custom resource in your Kubernetes cluster as follows:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: PgBouncer
         metadata:
         name: PGBOUNCER_NAME
         spec:
         dbclusterRef: DB_CLUSTER_NAME
         allowSuperUserAccess: true
         replicaCount: 2
         parameters:
           pool_mode: POOL_MODE
           ignore_startup_parameters: IGNORE_STARTUP_PARAMETERS
           default_pool_size: "DEFAULT_POOL_SIZE"
           max_client_conn: "MAXIMUM_CLIENT_CONNECTIONS"
           max_db_connections: "MAXIMUM_DATABASE_CONNECTIONS"
         podSpec:
           resources:
             memory: 1Gi
             cpu: 1
           image: "gcr.io/alloydb-omni/operator/g-pgbouncer:1.4.0"
         **serviceOptions :**
           **type : "LoadBalancer"**

  2. Apply the manifest:
         
         kubectl apply -f PATH_TO_MANIFEST

  3. To verify that the PgBouncer object you created is ready, execute the following query:
         
         kubectl get pgbouncers.alloydbomni.dbadmin.goog PGBOUNCER_NAME  -n NAMESPACE -w

The output is similar to the following:
         
         NAME          ENDPOINT       STATE
         mypgbouncer   10.138.15.207   Ready
         




## Configure PgBouncer settings

Use the following parameters to configure PGBouncer settings:

Parameter | Description | Default value  
---|---|---  
`pool_mode` | Specifies when a database connection can be reused by other clients.  
Allowed values are as follows:  


  * `session`: database connection is released back to the pool after client disconnects.
  * `transaction`: database connection is released back to pool after transaction finishes.
  * `statement`: database connection is released back to pool after query finishes.  
Transactions spanning multiple statements are disallowed in this mode.

| `session`  
`ignore_startup_parameters` | Specifies parameters that PgBouncer does not allow so that they are ignored during startup. |   
`default_pool_size` | The number of database connections to allow per user-database pair. | `20`  
`max_client_conn` | The maximum number of client connections. | `100`  
`max_db_connections` | The maximum number of database connections. | `0`  
  
## Customize PgBouncer deployment

AlloyDB Omni uses custom resources to manage its components. To customize the PgBouncer deployment within your AlloyDB Omni on Kubernetes, you modify the `PgBouncer` custom resource as follows:

  1. List the `PgBouncer` custom resources:
         
         kubectl get pgbouncers -n NAMESPACE

Replace NAMESPACE with the namespace where you deployed AlloyDB Omni.

  2. To modify the resource, open the declaration file for the `PgBouncer` resource in your default editor:
         
         kubectl edit pgbouncers PGBOUNCER_NAME -n NAMESPACE

  3. In the declaration file, find the `podSpec` section that contains the configuration and modify any of the following fields as needed:

     * `resources`: the `cpu` and `memory` defined for your container:
           
           apiVersion: alloydbomni.dbadmin.goog/v1
           kind: PgBouncer
           metadata:
             name: PGBOUNCER_NAME
           spec:
             dbclusterRef: DB_CLUSTER_NAME
             replicaCount: 2
             parameters:
               pool_mode: POOL_MODE
               ignore_startup_parameters: IGNORE_STARTUP_PARAMETERS
               default_pool_size: "DEFAULT_POOL_SIZE"
               max_client_conn: "MAXIMUM_CLIENT_CONNECTIONS"
               max_db_connections: "MAXIMUM_DATABASE_CONNECTIONS"
             **podSpec :**
               **resources :**
                 **memory : 1Gi**
                 **cpu : 1**
           ...
           

     * `image`: the path to the PgBouncer image tag:
           
           ...
             **podSpec :**
               resources:
                 memory: 1Gi
                 cpu: 1
               **image : IMAGE**
           ...
           

     * `schedulingconfig`: include the `nodeaffinity` section to control where the PgBouncer Pods are scheduled:
           
           ...
             **podSpec :**
               resources:
                 memory: 1Gi
                 cpu: 1
               image: IMAGE
               **schedulingconfig :**
                 **nodeaffinity :**
                   **NODE_AFFINITY_TYPE :**
                     **nodeSelectorTerms :**
                     **- matchExpressions:**
                       **- key: LABEL_KEY**
                         **operator : OPERATOR_VALUE**
                         **values :**
                         **- pgbouncer**
           ...
           

Replace the following:

       * `NODE_AFFINITY_TYPE`: set the parameter to one of the following: 
         * `requiredDuringSchedulingIgnoredDuringExecution`: Kubernetes schedules the Pod based exactly on the defined rules.
         * `preferredDuringSchedulingIgnoredDuringExecution`: the Kubernetes scheduler tries to find a node that meets the defined rule for scheduling. However, if there is no such node, Kubernetes schedules to a different node in the cluster.
       * `LABEL_KEY`: the node's label for the key that serves as a location indicator and facilitates even Pod distribution across the cluster—for example, `nodetype`.
       * `OPERATOR_VALUE`: represents a key's relationship to a set of values. Set the parameter to one of the following: 
         * `In`: the values array must be non-empty.
         * `NotIn`: the values array must be non-empty.
         * `Exists`: the values array must be empty.
         * `DoesNotExist`: the values array must be empty.
         * `Gt`: the values array must have a single element, which is interpreted as an integer.
         * `Lt`: the values array must have a single element, which is interpreted as an integer.
  4. After making the changes, save the declaration file. The AlloyDB Omni Kubernetes operator automatically applies the changes to your PgBouncer deployment.




## Delete the PgBouncer resource

To delete a PgBouncer custom resource, run the following command:
    
    
    kubectl delete pgbouncers.alloydbomni.dbadmin.goog PGBOUNCER_NAME -n NAMESPACE

The output is similar to the following:
    
    
    pgbouncer.alloydbomni.dbadmin.goog "mypgbouncer" deleted
    

## View PgBouncer logs

You can view and analyze logs of any PgBouncer replica instance in your AlloyDB Omni deployment on Kubernetes as follows:

  1. Get a list of all PgBouncer Pods in your namespace:
         
         kubectl get pods -n NAMESPACE

The output is similar to the following:
         
         NAME                                          READY   STATUS    RESTARTS   AGE
         al-092d-dbcluster-sample-0                    3/3     Running   0          3d1h
         mypgbouncer-pgb-deployment-659869f95c-4kbgv   1/1     Running   0          27m
         

  2. View logs for a particular Pod:
         
         kubectl logs -f POD_NAME -n NAMESPACE

**Note:** To continuously stream logs in realtime, use the `-f` option.

The output is similar to the following:
         
         2025-01-21 06:57:39.549 UTC [7] LOG kernel file descriptor limit: 1048576 (hard: 1048576); max_client_conn: 800, max expected fd use: 812
         2025-01-21 06:57:39.550 UTC [7] LOG listening on 0.0.0.0:6432
         2025-01-21 06:57:39.550 UTC [7] LOG listening on [::]:6432
         2025-01-21 06:57:39.550 UTC [7] LOG listening on unix:/tmp/.s.PGSQL.6432
         2025-01-21 06:57:39.550 UTC [7] LOG process up: PgBouncer 1.23.0, libevent 2.1.12-stable (epoll), adns: evdns2, tls: OpenSSL 3.0.13 30 Jan 2024
         2025-01-21 06:58:17.012 UTC [7] LOG C-0x55f2b1b322a0: (nodb)/(nouser)@10.138.15.215:48682 registered new auto-database: alloydbadmin
         2025-01-21 06:58:17.012 UTC [7] LOG S-0x55f2b1b4ecb0: alloydbadmin/alloydbpgbouncer@10.138.0.48:5432 new connection to server (from 10.12.1.113:53156)
         2025-01-21 06:58:17.042 UTC [7] LOG S-0x55f2b1b4ecb0: alloydbadmin/alloydbpgbouncer@10.138.0.48:5432 SSL established: TLSv1.3/TLS_AES_256_GCM_SHA384/ECDH=prime256v1
         2025-01-21 06:58:17.052 UTC [7] LOG C-0x55f2b1b322a0: pgbouncer/statsuser@10.138.15.215:48682 login attempt: db=pgbouncer user=statsuser tls=TLSv1.3/TLS_AES_256_GCM_SHA384 replication=no
         2025-01-21 06:58:19.526 UTC [7] LOG C-0x55f2b1b322a0: pgbouncer/statsuser@10.138.15.215:48682 closing because: client close request (age=2s)
         2025-01-21 06:58:20.344 UTC [7] LOG C-0x55f2b1b322a0: pgbouncer/statsuser@10.138.15.215:46796 login attempt: db=pgbouncer user=statsuser tls=TLSv1.3/TLS_AES_256_GCM_SHA384 replication=no
         




## Monitor PgBouncer performance and activity

You can view PgBouncer connection pool metrics using only a dedicated `statsuser` to access PgBouncer internal stats database. The `statsuser` is used for authentication when connecting to the PgBouncer database.

  1. Connect to your AlloyDB Omni as a superuser or a user with the `CREATE ROLE` privilege using the `psql` client:
         
         export PGPASSWORD="ChangeMe123"; export PGSSLMODE="require"; psql -h HOST -d postgres -U postgres -p PORT
         

The output is similar to the following:
         
         psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 15.7)
         SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
         Type "help" for help.
         

  2. Create the `statsuser` in your AlloyDB Omni:
         
         postgres=# CREATE USER "statsuser" WITH PASSWORD 'tester';
         

The output is similar to the following:
         
         CREATE ROLE
         postgres=#
         

  3. Connect to the PgBouncer database as the `statsuser`:
         
         export PGPASSWORD="ChangeMe123"; export PGSSLMODE="require"; psql -h HOST -d pgbouncer -U statsuser -p PORT
         

The output is similar to the following:
         
         psql (16.6 (Ubuntu 16.6-0ubuntu0.24.04.1), server 1.23.0/bouncer)
         WARNING: psql major version 16, server major version 1.23.
         Some psql features might not work.
         SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
         Type "help" for help.
         

  4. Run the [`SHOW STATS`](https://www.pgbouncer.org/usage.html#admin-console) command to view PgBouncer performance and identify potential issues:
         
         pgbouncer=# SHOW STATS;
         

The output is similar to the following:
         
         database   | total_server_assignment_count | total_xact_count | total_query_count | total_received | total_sent | total_xact_time | total_query_time | total_wait_time | avg_server_assignment_count | avg_xact_count | avg_query_count | avg_recv | avg_sent | avg_xact_time | avg_query_time | avg_wait_time
            -------------+-------------------------------+------------------+-------------------+----------------+------------+-----------------+------------------+-----------------+-----------------------------+----------------+-----------------+----------+----------+---------------+----------------+---------------
            alloydbadmin |                             1 |                0 |                 0 |              0 |        330 |               0 |                0 |           41730 |                           0 |              0 |               0 |        0 |        2 |             0 |              0 |         41730
            pgbouncer    |                             0 |                5 |                 5 |              0 |          0 |               0 |                0 |               0 |                           0 |              0 |               0 |        0 |        0 |             0 |              0 |             0
            (2 rows)
         




## Configure network access to your AlloyDB Omni instance

To ensure the security of your AlloyDB Omni deployment on Kubernetes, you can limit network access to the PgBouncer connection pooler by defining specific IP address ranges using CIDR (Classless Inter-Domain Routing) notation.

CIDR notation combines an IP address with a prefix length, for example, the CIDR block `192.168.1.0/24` specifies `192.168.1.0` for the address and `24` for the prefix length. The prefix length specifies the number of bits in the IP address that are used for the network portion and defines the subnet mask.

In your deployment's declaration file, locate the `serviceOptions` section and add or modify the `loadBalancerSourceRanges` setting:
    
    
      serviceOptions:
        type: "LoadBalancer"
        loadBalancerSourceRanges:
        - "CIDR_BLOCK"
    

Replace `CIDR_BLOCK` with a CIDR string that specifies the IP address ranges allowed for incoming connections to the `LoadBalancer` service. The `loadBalancerSourceRanges` setting filters incoming network traffic and controls which clients can access your database instance.

**Note:** Specify the narrowest possible IP ranges that allow your database instance to function correctly, enabling it to receive connections, execute queries, and perform other required database operations.

To verify that your `loadBalancerSourceRanges` configuration is applied correctly, use the following command to check the external IP address assigned to your `LoadBalancer` service:
    
    
    kubectl get svc -n NAMESPACE -w
    

Replace `NAMESPACE` with the namespace where your AlloyDB Omni deployment is located.

The output is similar to the following:
    
    
    NAME                     TYPE           CLUSTER_IP      EXTERNAL_IP   PORT(S)         AGE
    al-mypgbouncer-pgb-svc   LoadBalancer   34.118.230.149  10.138.0.26   6432:31367/TCP  3m39s
    

**Note:** The port is hardcoded to `6432` for the PgBouncer connection pooler. The `loadBalancerSourceRanges` attribute lets you pick an IP address only from the address range that you specify in `CIDR_BLOCK`.

Once the `LoadBalancer` is ready, the `EXTERNAL_IP` column is populated with the external IP address assigned to the `LoadBalancer` service. Connections to this external IP are filtered based on the `loadBalancerSourceRanges` setting.

After verifying the external IP, test connections from applications within your allowed CIDR ranges to ensure they can connect.

## Disable the PgBouncer connection pooler

If you need to deactivate or rollback the PgBouncer connection pooler, follow these steps:

  1. Check the status of the connection pooler:
         
         kubectl get deployment fleet-controller-manager --namespace alloydb-omni-system  -o json | jq '.spec.template.spec.containers[0].args'

This command shows the deployment manifest of the primary controller for managing the AlloyDB Omni fleet. Find the `--enable-pgbouncer` option in the `args` section of the `containers` array:
         
         ...
          spec:
           containers:
           - name: fleet-controller-manager
             image:...
             args:
             --health-probe-bind-address=:8081",
             --metrics-bind-address=127.0.0.1:8080",
             --leader-elect",
             --image-registry=gcr.io",
             --data-plane-image-repository=alloydb-omni-staging",
             --control-plane-agents-image-repository=aedi-gbox",
             --control-plane-agents-tag=jan19v3",
             --additional-db-versions-for-test-only=latest",
             --enable-multiple-backup-solutions=true",
             **--enable-pgbouncer=true**
         

  2. Edit the configuration of the controller deployment to disable the connection pooler:
         
         kubectl edit deployment fleet-controller-manager --namespace alloydb-omni-system

  3. In the deployment manifest, change the value of the `--enable-pgbouncer` option from `true` to `false`:
         
         ...
         **--enable-pgbouncer=false**
         

  4. Save the file and exit the editor. `kubectl` automatically applies the change.




## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
