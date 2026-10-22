---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra-restore/
title: Troubleshooting Cassandra restore \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:50.193455+00:00
---

# Troubleshooting Cassandra restore  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Troubleshooting Cassandra restore Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

During the Cassandra restoration in Apigee hybrid, you may encounter errors in the [ restore logs](https://docs.cloud.google.com/apigee/docs/hybrid/latest/view-cassandra-restore-logs). 

## Error message

You see one of the following in the logs:
    
    
    java.net.ConnectException: Connection timed out (Connection timed out)
    
    
    /tmp/tmp/schema.cql:662:OperationTimedOut: errors={'10.0.0.1': 'Client request timeout. See Session.execute[_async](timeout)'}, last_host=10.0.0.1
    
    
    /tmp/tmp/schema.cql:6409:AlreadyExists: Table 'kvm_myorg.kvm_map_keys_descriptor' already exists

## Possible causes

Cause | Description | Troubleshooting instructions applicable for  
---|---|---  
Connection timed out |  This error is a connectivity error between `apigee-cassandra-restore` pods and `apigee-cassandra-default-*` pods.  | Apigee hybrid  
Operation timed out |  This error occurs if restoration times out after more than 15 minutes.  | Apigee hybrid  
Already exists |  This error message is not related to the cause of the issue and is a result of a retry operation of a restoration job.  | Apigee hybrid  
  
## Cause: Connection timed out

The following error is a connectivity error between `apigee-cassandra-restore` pods and `apigee-cassandra-default-*` pods: 
    
    
    java.net.ConnectException: Connection timed out (Connection timed out)

### Diagnosis

  1. If your host network is not reachable from the pod network, ensure that `hostNetwork` is set to `false` under `cassandra` in `overrides.yaml` as shown in [ Restoring a region from a backup](https://docs.cloud.google.com/apigee/docs/hybrid/latest/restore-cassandra-single-region#restore-gcs). 
  2. To test the connectivity, log-in to the `apigee-mart` or `apigee-runtime` pod, which is in the same network as the `apigee-cassandra-restore` job. You can also use any other pod in the pod network. 
     1. Obtain the name of the `apigee-mart` pod: 
            
            kubectl -n apigee get po --selector=app=apigee-mart --no-headers -o custom-columns=":metadata.name"

     2. Execute a bash session inside the mart pod: 
            
            kubectl exec -it MART_POD_NAME -n apigee -- bash

Replace MART_POD_NAME with the name of the MART pod. For example, `apigee-mart-myorg--9a8228a-191-t0xh1-qz5fl`. 

     3. Run connectivity tests against [Cassandra ports](https://docs.cloud.google.com/apigee/docs/hybrid/latest/ports): 
            
            curl -v -m 5 telnet://apigee-cassandra-default-0.apigee-cassandra-default.apigee.svc.cluster.local:9042
            
            curl -v -m 5 telnet://apigee-cassandra-default-0.apigee-cassandra-default.apigee.svc.cluster.local:7001

If you get a `Connection timed out` error in the output, that means you have connectivity issues. But if you see a `Connected to` message, that indicates that the connection is successful, and you need to press `Ctrl + C` to close the connection and proceed. 




### Resolution

Ensure that the `HostNetwork` setting is set to `false` in the `overrides.yaml` file used for restore, and [ repeat the restoration process](https://docs.cloud.google.com/apigee/docs/hybrid/latest/restore-cassandra-single-region#restore-gcs). If the setting is already set to `false`, but you see connectivity errors, ensure that Cassandra pods are up and running with the following command: 
    
    
    kubectl get pods -n apigee -l app=apigee-cassandra

Your output should look something like the following example:
    
    
    NAME                         READY   STATUS    RESTARTS   AGE
    apigee-cassandra-default-0   1/1     Running   0          14m
    apigee-cassandra-default-1   1/1     Running   0          13m
    apigee-cassandra-default-2   1/1     Running   0          11m
    exampleuser@example hybrid-files %

## Cause: Operation timed out

The following error occurs if restoration times out after more than 15 minutes. The error indicates I/O issues such as storage and network not being able to transmit the uncompressed contents of the backup on time. 
    
    
    /tmp/tmp/schema.cql:662:OperationTimedOut: errors={'10.0.0.1': 'Client
    request timeout. See Session.execute[_async](timeout)'}, last_host=10.0.0.1

### Diagnosis

  1. Check the `apigee-cassandra-default-0` logs to note the timestamp of the beginning of the restoration: 
         
         kubectl logs apigee-cassandra-default-0 -n apigee | grep 'MigrationManager.java' | head -n 1

  2. Compare the timestamp with the latest log of table creation:
         
         kubectl logs apigee-cassandra-default-0 -n apigee | grep 'Create new table' | tail -n 1

The results from this comparison should show that the Cassandra pod was still in the process of creating tables after the timeout had been exceeded. 

  3. Test the storage bandwidth with the following commands:
         
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- bash -c 'dd if=/dev/zero of=/opt/apigee/data/test.img bs=200M count=1 ; rm /opt/apigee/data/test.img'
         
         kubectl -n apigee exec -it apigee-cassandra-default-1 -- bash -c 'dd if=/dev/zero of=/opt/apigee/data/test.img bs=200M count=1 ; rm /opt/apigee/data/test.img'
         
         kubectl -n apigee exec -it apigee-cassandra-default-2 -- bash -c 'dd if=/dev/zero of=/opt/apigee/data/test.img bs=200M count=1 ; rm /opt/apigee/data/test.img'

If the write speed is less than 100 M/s, this could indicate a lack of an [appropriate StorageClass](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-config) (SSD) used. 

  4. Test the networking bandwidth:

     1. Run `netcat` on the Cassandra pod to listen on the port: 
            
            kubectl -n apigee exec -it apigee-cassandra-default-0 -- bash -c 'nc -l -p 3456 > /dev/null'

     2. In a separate shell session, obtain the name of the `apigee-mart` pod: 
            
            kubectl -n apigee get po --selector=app=apigee-mart --no-headers -o custom-columns=":metadata.name"

     3. Execute a bash session inside the `apigee-mart` pod. You can also use any other pod in the pod network: 
            
            kubectl exec -it MART_POD_NAME -n apigee -- bash

Replace MART_POD_NAME with the name of the MART pod. For example, `apigee-mart-myorg--9a8228a-191-t0xh1-qz5fl`. 

     4. Run a network bandwidth test against the Cassandra pod that is still running the `netcat`: 
            
            dd if=/dev/zero bs=50M count=1 | nc apigee-cassandra-default-0.apigee-cassandra-default.apigee.svc.cluster.local 3456

You can repeat the process for other Cassandra pods. If the resulting speed is less than 10M/s, then the network bandwidth most likely is the cause of the issue. 




### Resolution

Once slow I/O speed is confirmed with the steps above, ensure that your cluster adheres to minimum [ network](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cluster-overview#cassandra-network-requirements) and [ storage](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-config) requirements. Test the bandwidth again afterwards. 

## Cause: Already exists

### Diagnosis

You see an error similar to the following: 
    
    
    /tmp/tmp/schema.cql:6409:AlreadyExists: Table 'kvm_myorg.kvm_map_keys_descriptor' already exists

### Resolution

This error message is not related to the cause of the issue and is a result of a retry operation of a restoration job. The actual error message should be displayed in the logs of the first pod that failed. 

[ Obtain the logs](https://docs.cloud.google.com/apigee/docs/hybrid/latest/view-cassandra-restore-logs) from the initial failure in order to diagnose the issue. 

If the problem still persists, go to Must gather diagnostic information. 

## Workaround for Known Issue 391861216

### Diagnosis

The highest numbered Cassandra pod is in a `CrashLoopBackoff` state after restore. This can occur due to known issue [391861216](https://docs.cloud.google.com/apigee/docs/release/known-issues#391861216). You see an error in the Cassandra pod log similar to the following: 
    
    
    Cannot change the number of tokens from 512 to 256

### Resolution

Perform the following steps to clear the underlying issue. This will allow Cassandra to start up normally while preserving the data. 

  1. Start the deletion of the PVC for the Cassandra pod stuck in the `CrashLoopBackoff` state. Set POD_NAME to the name of the pod in the `CrashLoopBackoff` state. Set APIGEE_NAMESPACE to the namespace of the cluster that Apigee is installed in. 
         
         kubectl delete pvc cassandra-data-POD_NAME -n APIGEE_NAMESPACE --wait=false

  2. Delete the pod in the `CrashLoopBackoff` state. 
         
         kubectl delete pod POD_NAME -n APIGEE_NAMESPACE

  3. Manually change the seed host for Cassandra to the highest numbered pod. For example, if you have three replicas, SEED_POD_NAME should be `apigee-cassandra-default-2`. This is needed only once and can be skipped for subsequent pods. 
         
         kubectl patch apigeeds/default -n APIGEE_NAMESPACE --type='merge' -p '{"spec": {"components": {"cassandra": {"properties": {"externalSeedHost":"SEED_POD_NAME.apigee-cassandra-default.APIGEE_NAMESPACE.svc.cluster.local"}}}}}'

  4. Remove the node with 512 tokens from the Cassandra ring. 
         
         kubectl exec -n APIGEE_NAMESPACE -t sts/apigee-cassandra-default -c apigee-cassandra -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD status' | awk '/^DN .*\?.* 512 / {print $6; exit}; /^DN .* [KMG]iB.* 512 / {print $7; exit}' | xargs -I {} kubectl exec -n APIGEE_NAMESPACE -t sts/apigee-cassandra-default -c apigee-cassandra -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD removenode {}'

  5. Wait for the Cassandra pod to recover, restart possibly more than once, and reach a `Ready` state of `2/2`. The next highest pod will then go into the `CrashLoopBackoff` state. 
         
         kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra -w

  6. Update POD_NAME and repeat the previous steps above for the remaining pods, one at a time, as they go into the `CrashLoopBackoff` state until all pods are in a `Ready` state of `2/2` and have a `Running` status. 

  7. Verify all pods have successfully joined the Cassandra ring. 
         
         kubectl exec -n APIGEE_NAMESPACE -t sts/apigee-cassandra-default -c apigee-cassandra -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD status'

All Cassandra nodes should have `UN` status and 256 tokens. 

  8. Revert the change to the seed host for Cassandra. 
         
         kubectl patch apigeeds/default -n APIGEE_NAMESPACE --type='merge' -p '{"spec": {"components": {"cassandra": {"properties": {"externalSeedHost":""}}}}}'

The Apigee Datastore controller will restart the Cassandra pods again as it reverts the seed host change. 




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. In addition to the usual data you might be asked to provide, collect the diagnostic data from all the Cassandra pods with the following command: 
         
         for p in $(kubectl -n apigee get pods -l app=apigee-cassandra --no-headers -o custom-columns=":metadata.name") ; do \
                 for com in info describecluster failuredetector version status ring info gossipinfo compactionstats tpstats netstats cfstats proxyhistograms gcstats ; do kubectl \
                 -n apigee exec ${p} -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD '"$com"' 2>&1 '\
                 | tee /tmp/k_cassandra_nodetool_${com}_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt | head -n 40 ; echo '...' ; done; done
               

  2. Compress it, and provide it in the support case:
         
         tar -cvzf /tmp/cassandra_data_$(date +%Y.%m.%d_%H.%M.%S).tar.gz /tmp/k_cassandra_nodetool*

  3. Collect and provide [ logs from the restore pod](https://docs.cloud.google.com/apigee/docs/hybrid/latest/view-cassandra-restore-logs). Note that logs are short-lived, so they should be collected right after the failure. 
  4. If you followed the diagnosis steps above, collect all the console outputs, copy them into a file, and attach the file to the support case. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
