---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/troubleshoot-kubernetes-operator/
title: Troubleshoot the AlloyDB Omni Kubernetes operator \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:10:03.525941+00:00
---

# Troubleshoot the AlloyDB Omni Kubernetes operator  |  AlloyDB Omni using the container orchestrator: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/troubleshoot-kubernetes-operator/

This page documents AlloyDB Omni version **17.7.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/overview)



Send feedback 

#  Troubleshoot the AlloyDB Omni Kubernetes operator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/troubleshoot-kubernetes-operator)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/troubleshoot-kubernetes-operator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/troubleshoot-kubernetes-operator)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/troubleshoot-kubernetes-operator)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/troubleshoot-kubernetes-operator)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/troubleshoot-kubernetes-operator)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/troubleshoot-kubernetes-operator)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/troubleshoot-kubernetes-operator)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/troubleshoot-kubernetes-operator)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/troubleshoot-kubernetes-operator)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/troubleshoot-kubernetes-operator)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/troubleshoot-kubernetes-operator)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/troubleshoot-kubernetes-operator)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/troubleshoot-kubernetes-operator)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/troubleshoot-kubernetes-operator)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/troubleshoot-kubernetes-operator)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/troubleshoot-kubernetes-operator)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/troubleshoot-kubernetes-operator)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/troubleshoot-kubernetes-operator)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/troubleshoot-kubernetes-operator)

This page shows you how to resolve issues with the AlloyDB Omni Kubernetes operator. 

## Collect debugging information

These sections describe how to collect logs and configurations for debugging.

### Fetch logs from operator pods

To fetch logs from the operator pods, run the following commands:
    
    
    kubectl logs deployments/fleet-controller-manager -c fleet-manager -n alloydb-omni-system > alloydb-omni-system-fleet-controller-manager.out
    kubectl logs deployments/local-controller-manager -c local-manager -n alloydb-omni-system > alloydb-omni-system-local-controller-manager.out
    

### Fetch database pod logs

To fetch database pod logs, run the following commands:
    
    
    DB_POD=$(kubectl get pod -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -n DB_CLUSTER_NAMESPACE -o jsonpath='{.items[0].metadata.name}')
    kubectl logs -c database ${DB_POD} -n DB_CLUSTER_NAMESPACE > ${DB_POD}.log
    kubectl logs -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -c database -n DB_CLUSTER_NAMESPACE > dbcluster_DB_CLUSTER_NAME.out
    

The following logs are examples of successful database health checks:
    
    
    I0813 11:01:49.210051      27 gateway.go:184] "DatabaseHealthCheck: request handled successfully" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:01:59.196796      27 gateway.go:166] "DatabaseHealthCheck: handling request" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:01:59.196853      27 database.go:702] "dbdaemon/isRestoreInProgress: starting" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:01:59.209824      27 gateway.go:184] "DatabaseHealthCheck: request handled successfully" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:02:09.197013      27 gateway.go:166] "DatabaseHealthCheck: handling request" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:02:09.197093      27 database.go:702] "dbdaemon/isRestoreInProgress: starting" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:02:09.210010      27 gateway.go:184] "DatabaseHealthCheck: request handled successfully" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:02:19.197368      27 gateway.go:166] "DatabaseHealthCheck: handling request" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:02:19.197425      27 database.go:702] "dbdaemon/isRestoreInProgress: starting" log_name="agent" project_ns="default" dbcluster="adb"
    I0813 11:02:19.210416      27 gateway.go:184] "DatabaseHealthCheck: request handled successfully" log_name="agent" project_ns="default" dbcluster="adb"
    

### Fetch the postgresql.log

To fetch the `postgresql.log`, run the following command:
    
    
    DB_POD=$(kubectl get pod -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -n DB_CLUSTER_NAMESPACE -o jsonpath='{.items[0].metadata.name}')
    kubectl exec -c database -n DB_CLUSTER_NAMESPACE -it ${DB_POD} -- cat /obs/diagnostic/postgresql.log > dbcluster_DB_CLUSTER_NAME_postgresql.log
    

### Fetch the DBInstance YAML file

To fetch the DBInstance YAML file, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml > dbcluster_DB_CLUSTER_NAME.yaml
    

### Fetch configurations and logs for HA scenarios

To fetch configurations and logs specific to high availability (HA) scenarios, run the following commands:
    
    
    kubectl get replicationconfig.alloydbomni.internal.dbadmin.goog -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml > replicationconfig_DB_CLUSTER_NAME.yaml
    kubectl get deletestandbyjobs.alloydbomni.internal.dbadmin.goog -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml > deletestandbyjobs_DB_CLUSTER_NAME.yaml
    kubectl get createstandbyjobs.alloydbomni.internal.dbadmin.goog -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml > createstandbyjobs_DB_CLUSTER_NAME.yaml
    kubectl get failovers.alloydbomni.dbadmin.goog -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml > failovers_DB_CLUSTER_NAME.yaml
    

### Fetch pod and STS statuses

To fetch pod and StatefulSet (STS) statuses, run the following commands:
    
    
    DB_POD=$(kubectl get pod -n DB_CLUSTER_NAMESPACE -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -o jsonpath='{.items[0].metadata.name}')
    kubectl describe pod ${DB_POD} -n DB_CLUSTER_NAMESPACE > pod_${DB_POD}.out
    kubectl describe statefulset -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE > statefulset_DB_CLUSTER_NAME.out
    

## Identify errors

These sections describe how to identify errors.

### Look for error status and error codes

To identify the error code, check the DBCluster YAML file under the status. Refer to the error codes documentation for more information.

To fetch the DBCluster YAML file, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml > dbcluster_DB_CLUSTER_NAME.yaml
    

Look for `criticalIncidents`. This section contains the error code and a stack trace.

The following are examples of `criticalIncidents`:
    
    
    status:
        certificateReference:
          certificateKey: ca.crt
          secretRef:
            name: dbs-al-cert-dr-mce
            namespace: dr
        conditions:
        -   lastTransitionTime: "2024-10-07T22:46:03Z"
        ...
        criticalIncidents:
        -   code: DBSE0304
          createTime: "2024-10-03T11:50:54Z"
          message: 'Healthcheck: Health check invalid result.'
          resource:
            component: healthcheck
            location:
              group: alloydbomni.internal.dbadmin.goog
              kind: Instance
              name: bc0f-dr-mce
              namespace: dr
              version: v1
          stackTrace:
          -   component: healthcheck
            message: 'DBSE0304: Healthcheck: Health check invalid result. rpc error: code
              = Code(10304) desc = DBSE0304: Healthcheck: Health check invalid result.
              dbdaemon/healthCheck: invalid timestamp read back from the healthcheck table.
              Lag is 384837.296269 seconds, wanted 35 seconds'
    

You can also retrieve the status by extracting specific fields in JSON format:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o jsonpath='{.status.criticalIncidents}' | jq
    

The output is similar to the following:
    
    
    [
      {
        "code": "DBSE0085",
        "createTime": "2024-03-14T05:41:37Z",
        "message": "Platform: Pod is unschedulable.",
        "resource": {
          "component": "provisioning",
          "location": {
            "group": "alloydb.internal.dbadmin.goog",
            "kind": "Instance",
            "name": "b55f-testdbcluster",
            "namespace": "dbs-system",
            "version": "v1"
          }
        },
        "stackTrace": [
          {
            "component": "provisioning",
            "message": "DBSE0085: Platform: Pod is unschedulable. 0/16 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/16 nodes are available: 16 No preemption victims found for incoming pod..: Pod is unschedulable"
          }
        ]
      }
    ]
    

If the error message refers to the database pod, check the instances and pod resources in the same namespace:
    
    
    kubectl get instances.alloydbomni.internal.dbadmin.goog -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml > instance_DB_CLUSTER_NAME.yaml
    kubectl get pods -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -n DB_CLUSTER_NAMESPACE
    

## Resolve certificate issuance failures in cert-manager

The AlloyDB Omni operator uses cert-manager to provision Transport Layer Security (TLS) certificates for the operator and database clusters. In `cert-manager` version 1.21.2 and earlier, a known race condition ([cert-manager issue #6331](https://github.com/cert-manager/cert-manager/issues/6331)) might cause certificate issuance to fail and enter a one-hour retry backoff.

### Symptoms

When this issue occurs, you might observe the following symptoms:

  * A `DBCluster` resource stays in the `DBClusterWaitingForCertificate` phase, and database cluster creation or upgrade times out.
  * A Helm installation of the AlloyDB Omni operator fails because a `Certificate` resource, such as `local-serving-cert` in the `alloydb-omni-system` namespace, isn't ready.
  * The status conditions of a `Certificate` resource include the `CSR not signed by referenced private key` message with the `Failed` or `ErrorKeyMatch` reason.



To find the `Certificate` resources that this issue affects, run the following command:
    
    
    kubectl get certificates.cert-manager.io --all-namespaces \
        -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.status.conditions[*].message}{"\n"}{end}' \
        | grep "CSR not signed by referenced private key"
    

The output lists the namespace, the name, and the status condition messages of each affected `Certificate` resource. If you view an affected `Certificate` resource in YAML format, its `status` field is similar to the following:
    
    
    status:
      conditions:
      - message: 'The certificate request has failed to complete and will be retried: Error generating certificate template: CSR not signed by referenced private key'
        reason: Failed
        status: "False"
        type: Issuing
      failedIssuanceAttempts: 1
    

### Workaround

To prevent controller update conflicts and reduce the retry delay for failed certificate requests from one hour to 15 seconds, upgrade `cert-manager` with the `ServerSideApply` feature gate and reduced backoff durations:
    
    
    helm upgrade cert-manager oci://quay.io/jetstack/charts/cert-manager \
        --version CERT_MANAGER_VERSION \
        --namespace cert-manager \
        --reuse-values \
        --set featureGates="ServerSideApply=true" \
        --set "extraArgs={--certificate-request-minimum-backoff-duration=15s,--certificate-request-maximum-backoff-duration=5m}"
    

Replace `CERT_MANAGER_VERSION` with the version of cert-manager that's installed in your Kubernetes cluster—for example, `v1.21.2`. To find the installed version, run the `helm list --namespace cert-manager` command. For example, `v1.12.2`.

**Note:** Passing the `--set` flags for the `featureGates` and `extraArgs` keys. replaces their existing values on the Helm release, even when you include the `--reuse-values` flag. If your `cert-manager` release already configures other feature gates or extra arguments, include them in the comma-separated lists. For GKE Autopilot clusters, also include the `--set global.leaderElection.namespace=cert-manager` flag.

After the cert-manager controller restarts, verify that all certificates show `True` in the `READY` column:
    
    
    kubectl get certificates.cert-manager.io --all-namespaces
    

If an installation of the AlloyDB Omni operator failed because of this issue, run the installation again.

## Debug memory issues

These sections describe how to debug memory issues.

### Run and take a heapdump

Only turn on this feature for troubleshooting purposes. Remember to turn it off afterward.

To take a heapdump, complete the following steps:

  1. Modify the operator deployment under the `alloydb-omni-system` namespace with name `fleet-controller-manager` and `local-controller-manager`.
  2. Add the following argument to the pod `--pprof-address=:8642` or to any other available port.
  3. Wait for the controller pod to restart.
  4. Port-forward the preceding port. For example:
         
         kubectl port-forward FLEET_CONTROLLER_MANAGER_POD_NAME -n alloydb-omni-system 8642:8642
         

  5. In another terminal, run `go tool pprof http://localhost:8642/debug/pprof/heap`. Change the port to match the preceding port if you don't use `8642`.

  6. Connect to the address and run troubleshooting commands. For example: `top`.

  7. After finishing troubleshooting, undo step 1 by removing the argument and waiting for the pod to restart.




### Determine the number of resources the operator is watching

To understand the resources that in use, run the following commands:
    
    
    kubectl get backuprepositories -A  | wc -l
    kubectl get failovers -A  | wc -l
    kubectl get instancebackupplans -A  | wc -l
    kubectl get instancebackups -A  | wc -l
    kubectl get instancerestores -A  | wc -l
    kubectl get instances -A  | wc -l
    kubectl get instanceswitchovers -A  | wc -l
    kubectl get lrojobs -A  | wc -l
    kubectl get replicationconfigs -A  | wc -l
    kubectl get sidecars -A  | wc -l
    kubectl get deployments -A  | wc -l
    kubectl get statefulsets -A  | wc -l
    kubectl get certificates.cert-manager.io -A  | wc -l
    kubectl get issuers.cert-manager.io -A  | wc -l
    kubectl get configmaps -A  | wc -l
    kubectl get persistentvolumeclaims -A  | wc -l
    kubectl get persistentvolumes -A  | wc -l
    kubectl get pods -A  | wc -l
    kubectl get secrets -A  | wc -l
    kubectl get services -A  | wc -l
    kubectl get storageclasses.storage.k8s.io -A  | wc -l
    

For example, if the number of secrets is high, it can lead to an Out Of Memory (OOM) error.
    
    
    kubectl get secrets -A | wc -l
    

## Advanced HA debugging

This section references resources that are internal implementations. These are subject to change at any point in time and have no backward compatibility commitments. Only apply manual fixes to issues on non-production databases. These steps may make the database unrecoverable.

The AlloyDB Omni HA setup has three phases:

  1. Set up the primary to receive a connection from the standby.
  2. Initialize the standby and connect it to the primary.
  3. Set the primary settings to make the connection synchronous.



Step 2 is generally the slowest. Depending on the size of the database, it might take several hours.

Each instance replicating instance should have a `replicationconfig` attached to it. For example:
    
    
    kubectl get replicationconfigs.alloydbomni.internal.dbadmin.goog -n DB_CLUSTER_NAMESPACE
    

Example output:
    
    
    NAME                 PARENT     TYPE       ROLE         READY   HEALTHY   SYNC_U   SYNC_D   SLOT_LOG   SLOT_REPLAY
    cd58-adb--58ea-adb   cd58-adb   Physical   Upstream     True    True      true
    ds-58ea-adb          58ea-adb   Physical   Downstream   True    True               true
    

The spec of the Replication Config indicates the intended settings, while the status reflects the actual state as read from the database. If there is a mismatch between the spec and the status, the controller is still attempting to apply the change, or there is some error that is preventing the change from being applied. This would be reflected in the status fields.

### Standby jobs

There should be two sets of internal jobs which track the workflow of a standby:

  * `createstandbyjobs.alloydbomni.internal.dbadmin.goog`
  * `deletestandbyjobs.alloydbomni.internal.dbadmin.goog`



If the setup appears to be stuck, view the jobs relating to the database cluster (DBC). The job might have error messages which explain which state the setup is in. Jobs are automatically cleaned up some time after they have completed, so you may not see any jobs if none are in progress.
    
    
    kubectl get createstandbyjobs.alloydbomni.internal.dbadmin.goog -n DB_CLUSTER_NAMESPACE
    

The output is similar to the following:
    
    
    apiVersion: alloydbomni.dbadmin.gdc.goog/v1
      kind: CreateStandbyJob
      metadata:
        creationTimestamp: "2024-11-05T03:34:26Z"
        finalizers:
        -   createstandbyjob.dbadmin.goog/finalizer
        generation: 1804
        labels:
          dbs.internal.dbadmin.goog/dbc: foo-ha-alloydb1-clone1
        name: foo-ha-alloydb1-clone1--ac00-foo-ha-alloydb1-clone1--6036-foo-ha-alloydb1-clone1-1730777666
        namespace: db
        resourceVersion: "11819071"
        uid: 1f24cedf-b326-422f-9405-c96c8720cd90
      spec:
        attempt: 3
        cleanup: false
        currentStep: SetupSynchronous
        currentStepTime: "2024-11-05T03:45:31Z"
        metadata:
          dbc: foo-ha-alloydb1-clone1
          primaryInstance: ac00-foo-ha-alloydb1-clone1
          retryError: 'etcdserver: leader changed'
          standbyInstance: 6036-foo-ha-alloydb1-clone1
        requeueTime: "2024-11-05T18:33:03Z"
        startTime: "2024-11-05T03:36:56Z"
    

### Primary verification

The first thing to verify is that the primary is set up correctly. There should be a Replication Profile for each standby. If `isSynchronous` is true on the spec and status, then setup should be complete. If `isSynchronous` is false on the spec and status, then it has not yet reached step 3. View the standby jobs to see if there are any running jobs, and if they have any error messages.
    
    
      replication:
        profiles:
        -   isActive: true
          isSynchronous: true
          name: ha:4c82-dbcluster-sample::d85d-dbcluster-sample
          password:
            name: ha-rep-pw-dbcluster-sample
            namespace: default
          passwordResourceVersion: "896080"
          role: Upstream
          type: Physical
          username: alloydbreplica
    

Verify that the `disableHealthcheck` annotation is false. It is meant to be disabled only during a failover or switchover.
    
    
    apiVersion: alloydbomni.internal.dbadmin.goog/v1
    kind: Instance
    metadata:
      annotations:
        dbs.internal.dbadmin.goog/consecutiveHealthcheckFailures: "0"
        dbs.internal.dbadmin.goog/disableHealthcheck: "false"
        dr-secondary: "false"
        forceReconcile: "1730414498"
    

### Queries

To verify that the resources on the DB pod are set up properly, sign in to the database as the administrator user `alloydbadmin`. Then issue the following queries:

#### Replication slot
    
    
    \x on
    select * from pg_replication_slots;
    
    
    
    -[ RECORD 1 ]-------+---------------------------------------------
    slot_name           | d85d_dbcluster_sample
    plugin              |
    slot_type           | physical
    datoid              |
    database            |
    temporary           | f
    active              | t
    active_pid          | 250
    xmin                | 16318
    catalog_xmin        |
    restart_lsn         | 0/CA657F0
    confirmed_flush_lsn |
    wal_status          | reserved
    safe_wal_size       |
    two_phase           | f
    

A good state is the presence of a replication slot bearing the same name as the standby instance. The absence of a replication slot indicates that the first setup step has not completed successfully.

If `active` is not `t` (true), then that means the standby is not connecting for some reason (networking, standby not finishing setup, etc.) and debugging will likely need to continue on the standby side.

#### Replication stats
    
    
    \x on
    select * from pg_stat_replication;
    
    
    
    -[ RECORD 1 ]----+----------------------------------------------------------------
    pid              | 250
    usesysid         | 16385
    usename          | alloydbreplica
    application_name | d85d_dbcluster_sample
    client_addr      | 10.54.79.196
    client_hostname  | gke-samwise-default-pool-afaf152d-8197.us-central1-a.c.foo
    client_port      | 24914
    backend_start    | 2024-10-30 21:44:26.408261+00
    backend_xmin     |
    state            | streaming
    sent_lsn         | 0/CA64DA8
    write_lsn        | 0/CA64DA8
    flush_lsn        | 0/CA64DA8
    replay_lsn       | 0/CA64DA8
    write_lag        |
    flush_lag        |
    replay_lag       |
    sync_priority    | 2
    sync_state       | sync
    reply_time       | 2024-11-04 22:08:04.370838+00
    

If this doesn't exist, then that means there is no active connection. The `sync_state` should be `sync`. If it is not `sync`, that means the final step of setup did not complete. Looking at the logs / jobs should provide more details.

### Standby verification

The standby should have a replication profile that matches the same profile to the primary:
    
    
      replication:
        profiles:
        -   host: 10.54.79.210
          isActive: true
          isSynchronous: true
          name: ha:4c82-dbcluster-sample::d85d-dbcluster-sample
          passwordResourceVersion: "896080"
          port: 5432
          role: Downstream
          type: Physical
          username: alloydbreplica
    

If there is no connection from the standby to the primary, there are two common possibilities:

  1. The standby is still setting up.
  2. The standby is getting an error while setting up or trying to connect.



To check if option 1 is happening, get the database pod logs and look for log statements named `dbdaemon/setupPhysicalReplicationDownstream`. The following are examples of successful setup logs:
    
    
    I1104 22:42:42.604871     103 replication.go:107] "dbdaemon/setupPhysicalReplicationDownstream: begin setup" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    2024-11-04 22:42:42,605 INFO waiting for postgres to stop
    2024-11-04 22:42:43,566 INFO stopped: postgres (exit status 0)
    I1104 22:42:43.567590     103 replication.go:131] "dbdaemon/setupPhysicalReplicationDownstream: about to call pg_basebackup" log_name="agent" project_ns="default" dbcluster="dbcluster-sample" cmd=["-h","10.54.79.210","-D","/mnt/disks/pgsql/pg_basebackup_data","-U","alloydbreplica","-v","-P","-p","5432","-w","-c","fast"]
    I1104 22:42:44.206403     103 replication.go:139] "dbdaemon/setupPhysicalReplicationDownstream: pg_basebackup finished" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    I1104 22:42:44.206440     103 replication.go:141] "dbdaemon/setupPhysicalReplicationDownstream: replacing data directory with pg_basebackup data directory" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    I1104 22:42:44.244749     103 replication.go:148] "dbdaemon/setupPhysicalReplicationDownstream: replaced data directory with pg_basebackup data directory" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    I1104 22:42:44.244783     103 replication.go:150] "dbdaemon/setupPhysicalReplicationDownstream: Creating config files" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    I1104 22:42:44.251565     103 replication.go:155] "dbdaemon/setupPhysicalReplicationDownstream: removing postgresql config file for log archiving" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    I1104 22:42:44.251621     103 replication.go:160] "dbdaemon/setupPhysicalReplicationDownstream: removing postgresql auto config file" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    I1104 22:42:44.251689     103 replication.go:165] "dbdaemon/setupPhysicalReplicationDownstream: Successfully wrote to config file" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    2024-11-04 22:42:44,256 INFO spawned: 'postgres' with pid 271
    2024-11-04 22:42:45,469 INFO success: postgres entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
    I1104 22:42:45.469838     103 replication.go:174] "dbdaemon/setupPhysicalReplicationDownstream: backup replication configuration after changing replication config" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    I1104 22:42:45.476732     103 replication.go:179] "dbdaemon/setupPhysicalReplicationDownstream: finished standby setup" log_name="agent" project_ns="default" dbcluster="dbcluster-sample"
    

If there is a connection error, check the db pod logs as well as the log file on the database at `/obs/diagnostic/postgresql.log` and see what the error is when trying to connect. One common error is there is no networking connectivity between the standby and the primary.

### Manual fixes

The easiest way to fix HA issues is to disable and then re-enable HA by setting `numberOfStandbys` to 0 and then resetting it to the number you want. If standbys are stuck being disabled, then follow these steps to manually reset the HA setup to be empty:

  1. Manually delete the standby instances.
  2. Connect to the primary database. Query the current replication slots and delete any replication slots of standbys you want to delete:
         
         select pg_drop_replication_slot('REPLICATION_SLOT_NAME');
         

  3. Delete any replication profiles from the primary instance that you want to delete.




If an instance has not reconciled recently, you can edit the `forceReconcile` annotation value. Set that to any numerical value, which is the timestamp of the last time that annotation was updated. The only purpose of that annotation is to provide a field we can update to force a new reconciliation.
    
    
    apiVersion: alloydbomni.internal.dbadmin.goog/v1
    kind: Instance
    metadata:
      annotations:
        dbs.internal.dbadmin.goog/consecutiveHealthcheckFailures: "0"
        dbs.internal.dbadmin.goog/disableHealthcheck: "false"
        dr-secondary: "false"
        forceReconcile: "1730414498"
    

## Collect database engine and audit logs

The database engine logs and audit logs are available as files inside the database pod (requiring root access):

  * `obs/diagnostic/postgresql.log`
  * `obs/diagnostic/postgresql.audit`


    
    
    DB_POD=$(kubectl get pod -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -n DB_CLUSTER_NAMESPACE -o jsonpath='{.items[0].metadata.name}')
    kubectl exec -c database -n DB_CLUSTER_NAMESPACE ${DB_POD} -it -- /bin/bash
    

When connected to the database container:
    
    
    ls -l /obs/diagnostic/
    

Example output:
    
    
    drwx--S--- 2 postgres postgres    4096 Aug 13 10:22 archive
    -rw------- 1 postgres postgres  256050 Aug 13 13:25 postgresql.internal
    -rw------- 1 postgres postgres 1594799 Aug 13 13:25 postgresql.log
    

## Collect database and database pod metrics

The AlloyDB Omni operator provides a set of basic metrics for the AlloyDB Omni engine and the pod hosting it. The metrics are available as Prometheus endpoints available at port 9187. To access the endpoints you need to identify the pod name for the database pod using the DBCluster label and start port forwarding as follows:
    
    
    DB_POD=$(kubectl get pod -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o jsonpath='{.items[0].metadata.name}')
    kubectl port-forward -n DB_CLUSTER_NAMESPACE ${DB_POD} 9187:9187
    

### Access database pod metrics

In another terminal:
    
    
    curl http://localhost:9187/metrics | grep HELP
    

For more information about monitoring, see [Monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manage#kubernetes).

You can also configure Prometheus to scrape the metrics in your Kubernetes cluster. Refer to the [Prometheus Kubernetes service discovery config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config) for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
