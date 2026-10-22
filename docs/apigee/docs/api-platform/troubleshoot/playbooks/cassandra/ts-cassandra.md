---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra/
title: Cassandra troubleshooting guide \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:53.882621+00:00
---

# Cassandra troubleshooting guide  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Cassandra troubleshooting guide Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is applicable for Apigee hybrid users only. 

This topic discusses steps you can take to troubleshoot and fix problems with the [Cassandra](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/what-is-hybrid#cassandra-datastore) datastore. Cassandra is a persistent datastore that runs in the `cassandra` component of the [hybrid runtime architecture](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/what-is-hybrid#about-the-runtime-plane). See also [Runtime service configuration overview](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/service-config). 

## Cassandra pods are stuck in the Releasing state

### Symptom

After trying to do an update to the Cassandra pods the datastore is reporting that it is stuck in releasing state. 

### Error message

When you use `kubectl` to view the pod states, you will see one or more Cassandra pods are stuck in the releasing state: 
    
    
    Events:
    Type Reason Age From Message
    ---- ------ ---- ---- -------
    Normal Ack 57s (x7 over 24h) apigee-datastore release started

### Possible causes

A pod stuck in the releasing state can be caused by the following: 

Cause | Description  
---|---  
Storage capacity changes |  Steps were executed to change the storage capacity in the `override.yaml` file.   
Other Configuration changes |  Updates were made to the cassandra properties in the `override.yaml` file; however, the changes did not take effect.   
  
## Storage capacity changes

### Diagnosis

  1. Use `kubectl` to see the current state of `apigee` datastore pod: 
         
         kubectl get apigeeds -n apigee
         
         NAME STATE AGE
         default releasing 122d

  2. Check to see if there were any changes to the `override.yaml` file: 
     1. Using your version control system, compare the previous version of the `override.yaml` file with the current version: 
            
            diff OVERRIDES_BEFORE.yaml OVERRIDES_AFTER.yaml

     2. The output of a diff in the `override.yaml` may show the possible problem with the size of the storage capacity. For example: 
            
            # Overrides.yaml  before:
            cassandra:
               storage:
                  capacity: 500Gi
            
            # Overrides.yaml after:
            cassandra:
               storage:
                  capacity: 100Gi

If there was an operation to [ change the storage capacity](https://docs.cloud.google.com/apigee/docs/hybrid/latest/expand-persistent-volumes) where steps were skipped, and a new `override.yaml` was applied directly, this can cause the datastore to be in the releasing state. 

  3. Check the `statefulset` to make sure that there is one there for `apigee-cassandra-default`: 
         
         kubectl describe sts -n apigee

The output looks something like this:
         
         Name:               apigee-cassandra-default
         Namespace:          apigee
         CreationTimestamp:  Tue, 18 Jul 2023 00:40:57 +0000
         Selector:           app=apigee-cassandra,name=default
         Labels:             apigee.cloud.google.com.revision=v1-2cc098050836c6b4
                             apigee.cloud.google.com.version=v1
                             apigee.cloud.google.com/platform=apigee
                             app=apigee-cassandra
                             name=default
         Annotations:        <none>
         Replicas:           3 desired | 3 total
         Update Strategy:    RollingUpdate
           Partition:        0
         Pods Status:        3 Running / 0 Waiting / 0 Succeeded / 0 Failed
         Pod Template:
           Labels:       apigee.cloud.google.com/apigee_servicename=production
                         apigee.cloud.google.com/billing_type=subscription
                         apigee.cloud.google.com/platform=apigee
                         app=apigee-cassandra
                         name=default
                         revision=v1
                         runtime_type=hybrid
           Annotations:  apigee.cloud.google.com/pod-template-spec-hash: 2cc098050836c6b4
                         prometheus.io/path: /metrics
                         prometheus.io/port: 7070
                         prometheus.io/scheme: https
                         prometheus.io/scrape: true
           Containers:
            apigee-cassandra:
             Image:       gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra:1.10.1
             Ports:       7000/TCP, 7001/TCP, 7199/TCP, 9042/TCP, 8778/TCP
             Host Ports:  7000/TCP, 7001/TCP, 7199/TCP, 9042/TCP, 8778/TCP
             Requests:
               cpu:      500m
               memory:   1Gi
             Readiness:  exec [/bin/bash -c /opt/apigee/ready-probe.sh] delay=0s timeout=5s period=10s #success=1 #failure=2
             Environment:
               POD_NAME:                  (v1:metadata.name)
               POD_IP:                    (v1:status.podIP)
               MAX_HEAP_SIZE:            512M
               HEAP_NEWSIZE:             100M
               CASSANDRA_SEEDS:          apigee-cassandra-default-0.apigee-cassandra-default.apigee.svc.cluster.local
               CASSANDRA_CLUSTER_NAME:   apigeecluster
               CASSANDRA_DC:             dc-1
               CASSANDRA_RACK:           ra-1
               CASSANDRA_OPEN_JMX:       true
               CPS_ADMIN_USER:           <set to the key 'admin.user' in secret 'apigee-datastore-default-creds'>        Optional: false
               CPS_ADMIN_PASSWORD:       <set to the key 'admin.password' in secret 'apigee-datastore-default-creds'>    Optional: false
               APIGEE_JMX_USER:          <set to the key 'jmx.user' in secret 'apigee-datastore-default-creds'>          Optional: false
               APIGEE_JMX_PASSWORD:      <set to the key 'jmx.password' in secret 'apigee-datastore-default-creds'>      Optional: false
               CASS_PASSWORD:            <set to the key 'default.password' in secret 'apigee-datastore-default-creds'>  Optional: false
               APIGEE_JOLOKIA_USER:      <set to the key 'jolokia.user' in secret 'apigee-datastore-default-creds'>      Optional: false
               APIGEE_JOLOKIA_PASSWORD:  <set to the key 'jolokia.password' in secret 'apigee-datastore-default-creds'>  Optional: false
             Mounts:
               /opt/apigee/apigee-cassandra/conf from appsfs (rw)
               /opt/apigee/customer from cwc-volume (ro)
               /opt/apigee/data from cassandra-data (rw)
               /opt/apigee/ssl from tls-volume (ro)
               /var/secrets/google from apigee-cassandra-backup (rw)
               /var/secrets/keys from apigee-cassandra-backup-key-file (rw)
           Volumes:
            cwc-volume:
             Type:        Secret (a volume populated by a Secret)
             SecretName:  config-cassandra-default
             Optional:    false
            tls-volume:
             Type:        Secret (a volume populated by a Secret)
             SecretName:  apigee-cassandra-default-tls
             Optional:    false
            appsfs:
             Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
             Medium:
             SizeLimit:  <unset>
            apigee-cassandra-backup:
             Type:        Secret (a volume populated by a Secret)
             SecretName:  apigee-cassandra-backup-svc-account
             Optional:    true
            apigee-cassandra-backup-key-file:
             Type:        Secret (a volume populated by a Secret)
             SecretName:  apigee-cassandra-backup-key-file
             Optional:    true
         Volume Claims:
           Name:          cassandra-data
           StorageClass:
           Labels:        <none>
           Annotations:   <none>
           Capacity:      10Gi
           Access Modes:  [ReadWriteOnce]
         Events:
           Type    Reason            Age   From                    Message
           ----    ------            ----  ----                    -------
           Normal  SuccessfulCreate  47m   statefulset-controller  create Pod apigee-cassandra-default-2 in StatefulSet apigee-cassandra-default successful

  4. Check for errors in the apigee controller: 
         
         kubectl logs -f apigee-controller-manager-59cf595c77-wtwnr -n apigee-system -c manager | grep apigeedatastore
         

Results:
         
         "error creating
         apigee-cassandra object: failed to update resource
         apigee/apigee-cassandra-default: StatefulSet.apps \"apigee-cassandra-default\"
         is invalid: spec: Forbidden: updates to statefulset spec for fields other than
         'replicas', 'template', 'updateStrategy', 'persistentVolumeClaimRetentionPolicy'
         and 'minReadySeconds' are forbiddenerror creating apigee-cassandra object:
         failed to update resource apigee/apigee-cassandra-default: StatefulSet.apps
         \"apigee-cassandra-default\" is invalid: spec: Forbidden: updates to statefulset
         spec for fields other than 'replicas', 'template', 'updateStrategy',
         'persistentVolumeClaimRetentionPolicy' and 'minReadySeconds' are forbidden"




### Resolution

The state for Cassandra can be reset using the following steps to get it back to a running state: 

  1. Disable the `apigee-controller`: 
         
         kubectl -n apigee-system edit deployments and set --enable-controllers=true to --enable-controllers=false
         

  2. Return the datastore to a running state using the `PATCH` command: 
         
         curl -XPATCH \-H "Accept: application/json" -H "Content-Type: application/json-patch+json" --data '[{"op": "replace", "path": "/status/nestedState", "value": ""},{"op": "replace", "path": "/status/state", "value": "running"}]' 'http://127.0.0.1:8001/apis/apigee.cloud.google.com/v1alpha1/namespaces/apigee/apigeedatastores/default/status'
         

  3. Reapply the original `override.yaml` file using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
         
         helm upgrade datastore apigee-datastore/ \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f OVERRIDES_FILE \
         --dry-run=server

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Install the chart:
         
         helm upgrade datastore apigee-datastore/ \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f OVERRIDES_FILE

  4. Enable the `apigee-controller`: 
         
         kubectl -n apigee-system edit deployments and set --enable-controllers=false to --enable-controllers=true
         

  5. Wait for the datastore to come back up and validate using the following: 
         
         kubectl get apigeeds --namespace apigee
         

  6. Validate Apigee deployments and pods are in the running status, and `apigeeds` is no longer in the releasing state: 
         
         kubectl get ad -n apigee
         
         
         kubectl get pods -n apigee
         
         
         kubectl get apigeeds -n apigee
         
         
         NAME      STATE     AGE
         default   running   24d




## Other configuration changes

Updates made to the `cassandra` properties in the `override.yaml` and changes did not take effect. This could be a password change, or change to resources in the `override.yaml`. Or erroneously applying the wrong `override.yaml` to a cluster. 

### Diagnosis

See the steps in Diagnosis.

### Resolution

See the steps in Resolution.

## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  * `Overrides.yaml` for each cluster in the installation. 
  * A kubernetes cluster-info dump from the Apigee hybrid installation:

Generate kubernetes `cluster-info dump`:
        
        kubectl cluster-info dump -A --output-directory=/tmp/kubectl-cluster-info-dump
        

Compress using zip kubernetes `cluster-info dump`:
        
        zip -r kubectl-cluster-info-dump`date +%Y.%m.%d_%H.%M.%S`.zip /tmp/kubectl-cluster-info-dump/*
        




##  Cassandra pods are stuck in the Pending state 

###  Symptom 

When starting up, the Cassandra pods remain in the **Pending** state. 

###  Error message 

When you use `kubectl` to view the pod states, you see that one or more Cassandra pods are stuck in the `Pending` state. The `Pending` state indicates that Kubernetes is unable to schedule the pod on a node: the pod cannot be created. For example: 
    
    
    kubectl get pods -n NAMESPACE
    
    NAME                                     READY   STATUS      RESTARTS   AGE
    adah-resources-install-4762w             0/4     Completed   0          10m
    apigee-cassandra-default-0               0/1     Pending     0          10m
    ...

###  Possible causes 

A pod stuck in the Pending state can have multiple causes. For example: 

Cause | Description  
---|---  
Insufficient resources |  There is not enough CPU or memory available to create the pod.   
Volume not created |  The pod is waiting for the persistent volume to be created.   
Missing Amazon EBS CSI driver |  For EKS installations, the required Amazon EBS CSI driver is not installed.   
  
###  Diagnosis 

Use `kubectl` to describe the pod to determine the source of the error. For example:
    
    
    kubectl -n NAMESPACE describe pods POD_NAME

For example: 
    
    
    kubectl describe pods apigee-cassandra-default-0 -n apigee

The output may show one of these possible problems: 

  * If the problem is insufficient resources, you will see a Warning message that indicates insufficient CPU or memory.
  * If the error message indicates that the pod has unbound immediate PersistentVolumeClaims (PVC), it means the pod is not able to create its [ Persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/). 



###  Resolution 

####  Insufficient resources 

Modify the Cassandra node pool so that it has sufficient CPU and memory resources. See [ Resizing a node pool](https://cloud.google.com/kubernetes-engine/docs/how-to/node-pools#resizing_a_node_pool) for details. 

####  Persistent volume not created 

If you determine a persistent volume issue, describe the PersistentVolumeClaim (PVC) to determine why it is not being created:

  1. List the PVCs in the cluster: 
         
         kubectl -n NAMESPACE get pvc
         
         NAME                                        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
         cassandra-data-apigee-cassandra-default-0   Bound    pvc-b247faae-0a2b-11ea-867b-42010a80006e   10Gi       RWO            standard       15m
         ...

  2. Describe the PVC for the pod that is failing. For example, the following command describes the PVC bound to the pod `apigee-cassandra-default-0`: 
         
         kubectl apigee describe pvc cassandra-data-apigee-cassandra-default-0
         
         Events:
           Type     Reason              Age                From                         Message
           ----     ------              ----               ----                         -------
           Warning  ProvisioningFailed  3m (x143 over 5h)  persistentvolume-controller  storageclass.storage.k8s.io "apigee-sc" not found

Note that in this example, the StorageClass named `apigee-sc` does not exist. To resolve this problem, create the missing StorageClass in the cluster, as explained in [ Change the default StorageClass](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-config). 




See also [ Debugging Pods](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-pod-replication-controller#debugging-pods). 

#### Missing Amazon EBS CSI driver

If the hybrid instance is running on an EKS cluster, make sure the EKS cluster is using the Amazon EBS container storage interface (CSI) driver. See [ Amazon EBS CSI migration frequently asked questions](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi-migration-faq.html) for details.

##  Cassandra pods are stuck in the CrashLoopBackoff state 

###  Symptom 

When starting up, the Cassandra pods remain in the **CrashLoopBackoff** state. 

###  Error message 

When you use `kubectl` to view the pod states, you see that one or more Cassandra pods are in the `CrashLoopBackoff` state. This state indicates that Kubernetes is unable to create the pod. For example: 
    
    
    kubectl get pods -n NAMESPACE
    
    NAME                                     READY   STATUS            RESTARTS   AGE
    adah-resources-install-4762w             0/4     Completed         0          10m
    apigee-cassandra-default-0               0/1     CrashLoopBackoff  0          10m
    ...

###  Possible causes 

A pod stuck in the `CrashLoopBackoff` state can have multiple causes. For example: 

Cause | Description  
---|---  
Data center differs from previous data center |  This error indicates that the Cassandra pod has a persistent volume that has data from a previous cluster, and the new pods are not able to join the old cluster. This usually happens when stale persistent volumes persist from the previous Cassandra cluster on the same Kubernetes node. This problem can occur if you delete and recreate Cassandra in the cluster.   
Kubernetes upgrade |  A Kubernetes upgrade may affect the Cassandra cluster. This can happen when the Anthos worker nodes hosting the Cassandra pods are upgraded to a new OS version.   
  
###  Diagnosis 

Check the [Cassandra error log](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-logs) to determine the cause of the problem. 

  1. List the pods to get the ID of the Cassandra pod that is failing: 
         
         kubectl get pods -n NAMESPACE

  2. Check the failing pod's log: 
         
         kubectl logs POD_ID -n NAMESPACE




###  Resolution 

Look for the following clues in the pod's log: 

####  Data center differs from previous data center 

If you see this log message: 
    
    
    Cannot start node if snitch's data center (us-east1) differs from previous data center

  * Check if there are any stale or old PVC in the cluster and delete them.
  * If this is a fresh install, delete all the PVCs and re-try the setup. For example: 
        
        kubectl -n NAMESPACE get pvc
        kubectl -n NAMESPACE delete pvc cassandra-data-apigee-cassandra-default-0




####  Anthos upgrade changes security settings 

Check the Cassandra logs for this error message: 
    
    
    /opt/apigee/run.sh: line 68: ulimit: max locked memory:
      cannot modify limit: Operation not permitted

  * If the hybrid instance is multi-region, [decommission the impacted hybrid instance](https://docs.cloud.google.com/apigee/docs/hybrid/latest/decommission-region) and [re-expand into the impacted region](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region).
  * If the hybrid instance is a single region, perform a rolling restart on each Cassandra pod in the hybrid instance.



##  Create a client container for debugging 

This section explains how to create a client container from which you can access Cassandra debugging utilities such as [`cqlsh`: the CQL shell](https://cassandra.apache.org/doc/stable/cassandra/managing/tools/cqlsh.html). These utilities allow you to query Cassandra tables and can be useful for debugging purposes. 

###  Create the client container 

To create the client container, follow these steps: 

  1. The container must use the TLS certificate from the `apigee-cassandra-user-setup` pod. This is stored as a Kubernetes secret. Fetch the name of the secret that stores this certificate: 
         
         kubectl get secrets -n apigee --field-selector type=kubernetes.io/tls | grep apigee-cassandra-user-setup | awk '{print $1}'

This command returns the name of the secret. For example: `apigee-cassandra-user-setup-rg-hybrid-b7d3b9c-tls`. You will use this below in the `secretName` field in the YAML file. 

  2. Open a new file and paste the following pod spec into it: 
         
         apiVersion: v1
         kind: Pod
         metadata:
           labels:
           name: CASSANDRA_CLIENT_NAME   # For example: my-cassandra-client
           namespace: apigee
         spec:
           containers:
           - name: CASSANDRA_CLIENT_NAME
             image: "gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra-client:YOUR_APIGEE_HYBRID_VERSION" # For example, 1.10.5.
             imagePullPolicy: Always
             command:
             - sleep
             - "3600"
             env:
             - name: CASSANDRA_SEEDS
               value: apigee-cassandra-default.apigee.svc.cluster.local
             - name: APIGEE_DML_USER
               valueFrom:
                 secretKeyRef:
                   key: dml.user
                   name: apigee-datastore-default-creds
             - name: APIGEE_DML_PASSWORD
               valueFrom:
                 secretKeyRef:
                   key: dml.password
                   name: apigee-datastore-default-creds
             volumeMounts:
             - mountPath: /opt/apigee/ssl
               name: tls-volume
               readOnly: true
           volumes:
           - name: tls-volume
             secret:
               defaultMode: 420
               secretName: YOUR_SECRET_NAME    # For example: apigee-cassandra-user-setup-rg-hybrid-b7d3b9c-tls
           restartPolicy: Never

  3. Save the file with a `.yaml` extension. For example: `my-spec.yaml`.
  4. Apply the spec to your cluster: 
         
         kubectl apply -f YOUR_SPEC_FILE.yaml -n apigee

  5. Log in to the container: 
         
         kubectl exec -n apigee CASSANDRA_CLIENT_NAME -it -- bash

  6. Connect to the Cassandra `cqlsh` interface with the following command. Enter the command exactly as shown: 
         
         cqlsh ${CASSANDRA_SEEDS} -u ${APIGEE_DML_USER} -p ${APIGEE_DML_PASSWORD} --ssl




###  Deleting the client pod 

Use this command to delete the Cassandra client pod: 
    
    
    kubectl delete pods -n apigee cassandra-client

##  Misconfigured region expansion: all Cassandra nodes under one datacenter 

This situation occurs in a multi-region expansion on GKE and GKE on-prem (Anthos) platforms. Try to avoid trying to create all your Cassandra nodes in the same data center.

###  Symptom 

Cassandra nodes fail to create in the data center for the second region. 

###  Error Message 
    
    
    failed to rebuild from dc-1: java.lang.RuntimeException : Error while rebuilding node: Stream failed

###  Resolution 

Repair the misconfigured region expansion with the following steps: 

  1. Update the Cassandra `replicaCount` to `1` in the `overrides.yaml` file for the second data center. For example: 
         
         cassandra:
           . . .
           replicaCount: 1

Apply the setting using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
         
         helm upgrade datastore apigee-datastore \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f 2ND_DATACENTER_OVERRIDES_FILE \
         --dry-run=server

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Install the chart:
         
         helm upgrade datastore apigee-datastore \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f 2ND_DATACENTER_OVERRIDES_FILE

  2. Use `kubectl exec` to access the remaining Cassandra pod with the following command: 
         
         kubectl exec -it -n apigee apigee-cassandra-default-0 -- /bin/bash

  3. Decommission the remaining Cassandra pod with the following command: 
         
         nodetool -u CASSANDRA_DB_USER -pw CASSANDRA_DB_PASSWORD decommission

  4. Delete the Cassandra pods from the second data center using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
         
         helm uninstall datastore -n APIGEE_NAMESPACE

  5. Change your Kubernetes context to the cluster for your first data center: 
         
         kubectl config use-context FIRST_DATACENTER_CLUSTER

  6. Verify there are no Cassandra nodes in a down state in the first data center. 
         
         nodetool -u CASSANDRA_DB_USER -pw CASSANDRA_DB_PASSWORD status

  7. Verify the misconfigured Cassandra nodes (intended for the second data center) have been removed from the first data center. Make sure the IP addresses that are displayed in the nodetool status output are only the IP addresses for the Cassandra pods intended for your _first_ data center. For example, in the following output the IP address `10.100.0.39` should be for a pod in your first data center. 
         
         kubectl exec -it -n apigee apigee-cassandra-default-0 -- /bin/bash
         nodetool -u CASSANDRA_DB_USER -pw CASSANDRA_DB_PASSWORD status
         
           Datacenter: dc-1
           ================
           Status=U/D (Up/Down) | State=N/L/J/M (Normal/Leaving/Joining/Moving)
           --  Address      Load      Tokens  Owns (effective)  Host ID                               Rack
           UN  10.100.0.39  4.21 MiB  256     100.0%            a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d  ra-1

  8. Verify that the `overrides.yaml` file for the second data center contains the data center name setting under the cassandra section. For example: 
         
         cassandra:
           datacenter: DATA_CENTER_2
           rack: "RACK_NAME" # "ra-1" is the default value.
           . . .

  9. Update the `cassandra:replicaCount` setting in the `overrides.yaml` file for the second data center to the desired number. For example: 
         
         cassandra:
           datacenter: DATA_CENTER_2
           . . .
           **replicaCount: 3**

**Note:** The value of [`cassandra:replicaCount`](https://docs.cloud.google.com/apigee/docs/hybrid/latest/config-prop-ref#cassandra-replicacount) must be a multiple of 3. Use the same value for `replicaCount` that your specified for your first datacenter.
  10. Apply the `overrides.yaml` file for the second data center with the `datastore` argument. For example: 
         
         helm upgrade datastore apigee-datastore \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f 2ND_DATACENTER_OVERRIDES_FILE \
         --dry-run=server

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Install the chart:
         
         helm upgrade datastore apigee-datastore \
         --namespace APIGEE_NAMESPACE \
         --atomic \
         -f 2ND_DATACENTER_OVERRIDES_FILE

  11. Use `kubectl exec` to access one of the new Cassandra pods in the second data center and verify there are two data centers: 
         
         "nodetool -u CASSANDRA_DB_USER -pw CASSANDRA_DB_PASSWORD status"




## Workaround for Known Issue 388608440

This section explains how to check whether your installation is affected by the known issue [388608440](https://docs.cloud.google.com/apigee/docs/release/known-issues#388608440) and how to resolve it. 

### Diagnosis

To check whether you are affected by this known issue, run the following command:
    
    
    kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-cassandra -o name | \
      xargs -i -P0 kubectl -n APIGEE_NAMESPACE -c apigee-cassandra exec {} -- \
      bash -c 'echo "{}: Found $(nodetool -u cassandra -pw $CASS_PASSWORD listsnapshots | grep -c compaction_history) leftover snapshots"'
    

For example:
    
    
    kubectl -n apigee get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n apigee -c apigee-cassandra exec {} -- bash -c 'echo "{}: Found $(nodetool -u cassandra -pw $CASS_PASSWORD listsnapshots | grep -c compaction_history) leftover snapshots"'
    
    
    pod/apigee-cassandra-default-0: Found 0 leftover snapshots
    pod/apigee-cassandra-default-1: Found 0 leftover snapshots
    pod/apigee-cassandra-default-2: Found 0 leftover snapshots
        

If the number of leftover snapshots is more than 0 for any of your Cassandra pods, then your installation is affected by this issue. 

### Resolution

To resolve this issue, follow the steps below, selecting the type of backup you use and your Apigee Hybrid minor version: 

### Cloud Storage backup

  1. Ensure you use the correct configuration for Cloud Storage backup. Some common issues include, but are not limited to, the following: 
     * Wrong Google Service Account is used.
     * Wrong Cloud Storage bucket name specified in [cassandra.backup.dbStorageBucket](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/config-prop-ref#cassandra-backup-dbStorageBucket).
     * The Google API is not reachable through proxy (if [cassandra.backup.httpproxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/config-prop-ref#cassandra-backup-httpproxy) is used). 

If you find any issues with your setup, please fix them before proceeding.

  2. Manually delete leftover snapshots using the following command: 

### Apigee Hybrid 1.12
         
         kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n APIGEE_NAMESPACE -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot --all)"'

For example:
         
         kubectl -n apigee get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n apigee -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot --all)"'

### Apigee Hybrid 1.11
         
         kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n APIGEE_NAMESPACE -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot)"'

For example:
         
         kubectl -n apigee get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n apigee -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot)"'
         
         pod/apigee-cassandra-default-1: Requested clearing snapshot(s) for [all keyspaces] with [all snapshots]
         pod/apigee-cassandra-default-2: Requested clearing snapshot(s) for [all keyspaces] with [all snapshots]
         pod/apigee-cassandra-default-0: Requested clearing snapshot(s) for [all keyspaces] with [all snapshots]
                     

**Note:**
     * The `clearsnapshot` command only deletes snapshots without affecting the stored data. 
     * The process may take minutes if the number of leftover snapshots is large.
  3. Trigger a [manual backup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/schedule-cassandra-backup-gcs#manual-backup) job and validate that it completes successfully. 
  4. Validate that the backup archive created by the manual backup job is successfully uploaded to the [cassandra.backup.dbStorageBucket](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/config-prop-ref#cassandra-backup-dbStorageBucket) Cloud Storage bucket that you specified in your `overrides.yaml` file. 
  5. Validate that the number of leftover snapshots is 0 for all Cassandra pods using the command presented earlier in the Diagnosis section. 



### Remote Server backup

  1. Ensure the remote backup server is healthy and reachable from the Cassandra pods. Check the [troubleshooting](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/schedule-cassandra-backup-non-gcs#troubleshooting) section for steps to verify SSH connectivity. Some common issues include, but are not limited to, the following: 
     * Network firewall is blocking the connection.
     * The SSH key is not set up correctly.
     * The remote backup server is not reachable.
     * The remote backup server is out of free storage.

If you find any issues with the remote backup server, please fix them before proceeding. 

  2. Manually delete leftover snapshots using the following command: 

### Apigee Hybrid 1.12
         
         kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n APIGEE_NAMESPACE -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot --all)"'

For example:
         
         kubectl -n apigee get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n apigee -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot --all)"'

### Apigee Hybrid 1.11
         
         kubectl -n APIGEE_NAMESPACE get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n APIGEE_NAMESPACE -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot)"'

For example:
         
         kubectl -n apigee get pods -l app=apigee-cassandra -o name | xargs -i -P0 kubectl -n apigee -c apigee-cassandra exec {} -- bash -c 'echo "{}: $(nodetool -u cassandra -pw $CASS_PASSWORD clearsnapshot)"'
         
         pod/apigee-cassandra-default-1: Requested clearing snapshot(s) for [all keyspaces] with [all snapshots]
         pod/apigee-cassandra-default-2: Requested clearing snapshot(s) for [all keyspaces] with [all snapshots]
         pod/apigee-cassandra-default-0: Requested clearing snapshot(s) for [all keyspaces] with [all snapshots]
                     

**Note:**
     * The `clearsnapshot` command only deletes snapshots without affecting the stored data. 
     * The process may take minutes if the number of leftover snapshots is large.
  3. Trigger a [manual backup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/schedule-cassandra-backup-non-gcs#manual-backup) job and validate that it completes successfully. 
  4. Validate that the backup archive created by the manual backup job is successfully uploaded to the remote backup server. 
  5. Validate that the number of leftover snapshots is 0 for all Cassandra pods using the command presented earlier in the Diagnosis section. 



## Additional resources

See [ Introduction to Apigee X and Apigee hybrid playbooks](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/introduction).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
