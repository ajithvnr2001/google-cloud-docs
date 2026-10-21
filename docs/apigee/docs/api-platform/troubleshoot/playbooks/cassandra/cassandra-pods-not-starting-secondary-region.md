---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-pods-not-starting-secondary-region/
title: Cassandra pods not starting in the secondary region \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:22.006880+00:00
---

# Cassandra pods not starting in the secondary region  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-pods-not-starting-secondary-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Cassandra pods not starting in the secondary region Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/404-support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

Cassandra pods fail to start in one of the regions in a multi-region Apigee hybrid setup. When applying the `overrides.yaml` file, the Cassandra pods do not start successfully. 

## Error messages

  1. You will observe the following error message in the Cassandra pod logs: 
         
         Exception (java.lang.RuntimeException) encountered during startup:
         A node with address 10.52.18.40 already exists, cancelling join.
         use cassandra.replace_addrees if you want to replace this node.

  2. You may observe the following warning in the Cassandra pod status:

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ts-cassandra-pods-not-starting-warning.png)



## Possible causes

This issue is typically observed in the following scenario: 

  1. The Apigee runtime cluster is deleted in one of the regions.
  2. An attempt to reinstall the Apigee runtime cluster is made in the region with Cassandra seed host configuration in the `overrides.yaml` file as described in [Multi-region deployment on GKE and GKE on-prem](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region).
  3. Deleting the Apigee runtime cluster does not remove the references in the Cassandra cluster. Thus, the stale references of the Cassandra pods in the deleted cluster will be retained. Because of this, when you try to reinstall the Apigee runtime cluster in the secondary region, the Cassandra pods complain that certain IP addresses already exist. That is because the IP addresses may be assigned from the same subnet which was used earlier.

**Note:** In this playbook, the term _primary region_ refers to the healthy Apigee runtime cluster and the term _secondary region_ refers to the Apigee runtime cluster which is deleted and reinstallation is attempted with Cassandra seed configuration referring to the primary region. Cause | Description  
---|---  
Stale references to deleted secondary region pods in Cassandra cluster | Deleting the Apigee runtime cluster in the secondary region does not remove the references to IP addresses of Cassandra pods in the secondary region.  
  
### Cause: Stale references to deleted secondary region pods in Cassandra cluster

### Diagnosis

  1. The error message in the in the Cassandra pod logs `A node with address 10.52.18.40 already exists` indicates that there exists a stale reference to one of the secondary region Cassandra pods with the IP address `10.52.18.40`. Validate this by running the `nodetool status` command in the primary region. 

**Sample Output:**

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ts-cassandra-pods-not-starting-sample-output.png)

The above example shows that the IP address `10.52.18.40` associated with Cassandra pods of the secondary region is still listed in the output.

  2. If the output contains the stale references to Cassandra pods in the secondary region, then it indicates that the secondary region has been deleted, but the IP addresses of the Cassandra pods in the secondary region are not removed. 



### Resolution

Perform the following steps to remove the stale references of Cassandra pods of the deleted cluster: 

  1. Log into the container and connect to the Cassandra command-line interface by following the steps at [Create the client container](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-the-client-container).
  2. After you have logged into the container and connected to the Cassandra `cqlsh` interface, run the following SQL query to list the current `keyspace` definitions: 
         
         select * from system_schema.keyspaces;

**Sample output showing current keyspaces:**

In the following output, `Primary-DC1` refers to the primary region and `Secondary-DC2` refers to the secondary region.
         
         bash-4.4# cqlsh 10.50.112.194 -u admin_user -p ADMIN.PASSWORD --ssl
         Connected to apigeecluster at 10.50.112.194:9042.
         [cqlsh 5.0.1 | Cassandra 3.11.6 | CQL spec 3.4.4 | Native protocol v4]
         Use HELP for help.
         
         admin_user@cqlsh> Select * from system_schema.keyspaces;
         
         keyspace_name                        | durable_writes | replication
         -------------------------------------+----------------+--------------------------------------------------------------------------------------------------
         system_auth                          |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         kvm_tsg1_apigee_hybrid_prod_hybrid   |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         kms_tsg1_apigee_hybrid_prod_hybrid   |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         system_schema                        |           True |                                           {'class': 'org.apache.cassandra.locator.LocalStrategy'}
         system_distributed                   |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         system                               |           True |                                           {'class': 'org.apache.cassandra.locator.LocalStrategy'}
         perses                               |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         cache_tsg1_apigee_hybrid_prod_hybrid |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         rtc_tsg1_apigee_hybrid_prod_hybrid   |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         quota_tsg1_apigee_hybrid_prod_hybrid |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         system_traces                        |           True | {'Primary-DC1': '3', 'Secondary-DC2': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'}
         (11 rows)

As you can see, the `keyspaces` are referring to both `Primary-DC1` and `Secondary-DC2`, even though the Apigee runtime cluster was deleted in the secondary region.

The stale references to `Secondary-DC2` have to be deleted from each of the `keyspace` definitions.

  3. Before deleting the stale references in the `keyspace` definitions, use the following command to delete the entire Apigee hybrid installation _except ASM (Istio) and`cert-manager` from the `Secondary-DC2`_. For more information, refer to [ Uninstall the hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/latest/uninstall). 
         
         helm uninstall -n APIGEE_NAMESPACE ENV_GROUP_RELEASE_NAME ENV_RELEASE_NAME $ORG_NAME ingress-manager telemetry redis datastore

Also, uninstall `apigee-operator`:
         
         helm uninstall -n APIGEE_NAMESPACE operator

  4. Remove the stale references to `Secondary-DC2` from each of the `keyspaces` by altering the `keyspace` definition. 
         
         ALTER KEYSPACE system_auth WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE kvm_ORG_NAME_apigee_hybrid_prod_hybrid WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE kms_ORG_NAME_apigee_hybrid_prod_hybrid WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE system_distributed WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE perses WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE cache_ORG_NAME_apigee_hybrid_ENV_NAME_hybrid WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE rtc_ORG_NAME_apigee_hybrid_ENV_NAME_hybrid WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE quota_ORG_NAME_apigee_hybrid_ENV_NAME_hybrid WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};
         ALTER KEYSPACE system_traces WITH replication = {'Primary-DC1': '3', 'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy'};

  5. Verify that the stale references to the `Secondary-DC2` region have been removed from all the `keyspaces` by running the following command: 
         
         select * from system_schema.keyspaces;

  6. Log in to a Cassandra pod of the `Primary-DC1` and remove the references to UUIDs of all the Cassandra pods of `Secondary-DC2`. The UUIDs can be obtained from the `nodetool status` command as described earlier in Diagnosis. 
         
         kubectl exec -it -n apigee apigee-cassandra-default-0 -- bash
         nodetool -u admin_user -pw ADMIN.PASSWORD removenode UUID_OF_CASSANDRA_POD_IN_SECONDARY_DC2
         

  7. Verify that no Cassandra pods of `Secondary-DC2` are present by running the `nodetool status` command again. 
  8. Install the Apigee runtime cluster in the secondary region (`Secondary-DC2`) by following the steps in [ Multi-region deployment on GKE and GKE on-prem](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region). 



## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID
  2. The name of the Apigee hybrid organization
  3. The `overrides.yaml` files from both the primary and secondary regions, masking any sensitive information
  4. Kubernetes pod status in all namespaces of both the primary and secondary regions: 
         
         kubectl get pods -A > kubectl-pod-status`date +%Y.%m.%d_%H.%M.%S`.txt
         

  5. A kubernetes `cluster-info` dump from both the primary and secondary regions: 
         
         # generate kubernetes cluster-info dump
         kubectl cluster-info dump -A --output-directory=/tmp/kubectl-cluster-info-dump
         
         # zip kubernetes cluster-info dump
         zip -r kubectl-cluster-info-dump`date +%Y.%m.%d_%H.%M.%S`.zip /tmp/kubectl-cluster-info-dump/*
         

  6. The output of the below `nodetool` commands from the primary region. 
         
         export u=`kubectl -n apigee get secrets apigee-datastore-default-creds -o jsonpath='{.data.jmx\.user}' | base64 -d`
         export pw=`kubectl -n apigee get secrets apigee-datastore-default-creds -o jsonpath='{.data.jmx\.password}' | base64 -d`
         
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw info 2>&1 | tee /tmp/k_nodetool_info_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw describecluster 2>&1 | tee /tmp/k_nodetool_describecluster_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw failuredetector 2>&1 | tee /tmp/k_nodetool_failuredetector_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw status 2>&1 | tee /tmp/k_nodetool_status_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw gossipinfo 2>&1 | tee /tmp/k_nodetool_gossipinfo_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw netstats 2>&1 | tee /tmp/k_nodetool_netstats_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw proxyhistograms 2>&1 | tee /tmp/k_nodetool_proxyhistograms_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw tpstats 2>&1 | tee /tmp/k_nodetool_tpstats_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw gcstats 2>&1 | tee /tmp/k_nodetool_gcstats_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw version 2>&1 | tee /tmp/k_nodetool_version_$(date +%Y.%m.%d_%H.%M.%S).txt
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u $u -pw $pw ring 2>&1 | tee /tmp/k_nodetool_ring_$(date +%Y.%m.%d_%H.%M.%S).txt
               




## References

  * Apigee hybrid [ Multi-region deployment on GKE and GKE on-prem](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region)
  * [Kubernetes Documentation](https://kubernetes.io/docs/home/)
  * [ Cassandra `nodetool status` command](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/tools/toolsStatus.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
