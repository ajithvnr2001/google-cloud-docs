---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ao-example-site-monitoring/
title: Monitor system health and trigger failovers \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:57.155813+00:00
---

# Monitor system health and trigger failovers  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ao-example-site-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitor system health and trigger failovers Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to monitor the health of your primary site and execute an automated or manual failover of replicated block storage volumes to a secondary zone. This is essential for maintaining application availability during a regional outage.

## 1\. Monitor system health

Before initiating a failover, you must verify the health of the primary site and the state of your replication relationship. For automated scripts/utilities, use non-interactive credentials (e.g., dedicated service accounts mapped using `kubeconfig`) with least-privilege access to the management plane.

### Check primary API health

The first step is to determine if the management plane in the primary zone is responsive. When writing custom automation, execute a raw health check with a clear timeout and a consecutive failure threshold (e.g., requiring 3 consecutive failures to avoid false positives during transient network blips):
    
    
    kubectl --kubeconfig PRIMARY_ZONE_KUBECONFIG get --raw /healthz --request-timeout=5s
    

  * **Success** : A response of `ok` indicates the API server is healthy.
  * **Failure** : If the command times out or returns an error, the primary site may be unavailable.



### Inspect replication relationship

Retrieve the status of the `VolumeReplicationRelationship` (VRR) from the Global API to check for synchronization lag or errors. For programmatic verification, parse the structured JSON output rather than relying on string matching:
    
    
    kubectl --kubeconfig GLOBAL_MGMT_KUBECONFIG get volumereplicationrelationship \
      -n PROJECT_NAME VRR_NAME -o json
    

In the `replicaStatus` section, verify that the state is `Established` or `Idle`. A lag (`lastTransferTime`) exceeding your Recovery Point Objective (RPO) (e.g., 15 minutes) may also warrant a failover decision.

## 2\. Initiate volume failover

If the primary site is unreachable or the replication health is degraded, you must initiate a failover in the destination zone (e.g., Zone 2). This promotes the secondary disk to a writable state. 

### Create the VolumeFailover resource

Apply a `VolumeFailover` Cluster Resource (CR) to the organization's management plane in the destination zone. In automated workflows, generate this CR dynamically using the Kubernetes API client libraries to safely parameterize the `VolumeReplicationRelationship` name and references:
    
    
    # failover.yaml
    apiVersion: storage.gdc.goog/v1
    kind: VolumeFailover
    metadata:
      name: my-app-failover
      namespace: PROJECT_NAME
    spec:
      volumeReplicationRelationshipRef: VRR_NAME
    
    
    
    kubectl --kubeconfig DEST_ZONE_KUBECONFIG apply -f failover.yaml
    

## 3\. Verify the failover completion

The failover process is asynchronous. You must monitor the `VolumeFailover` resource until it reaches a terminal state. Automated operators should check this idempotently to prevent triggering duplicate failovers:
    
    
    kubectl --kubeconfig DEST_ZONE_KUBECONFIG get volumefailover \
      my-app-failover -n PROJECT_NAME -o jsonpath='{.status.state}'
    

  * **Success** : 
    * The `VolumeFailover` status transitions to `Completed`.
    * The `VolumeReplicationRelationship` will now show a state of `Broken Off`.



## 4\. Deploy application at the destination

Once the `VolumeFailover` has completed and the disk is promoted, you can create a new Virtual Machine (VM) on the destination zone and attach the promoted disk to resume service.

**Note:** Once a failover is completed, the original replication relationship is broken off. To resume protection, you must eventually delete the old VRR and create a new one to replicate data back to the primary site.

### Create a VM with the promoted disk

Use `kubectl` to deploy a VM in the destination zone, referencing the promoted secondary disk as the boot disk:
    
    
    # vm-at-dest.yaml
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachine
    metadata:
      name: recovery-vm
      namespace: PROJECT_NAME
    spec:
      compute:
        virtualMachineType: n3-standard-2-gdc
      disks:
      - virtualMachineDiskRef:
          name: SECONDARY_DISK_NAME
        boot: true
        autoDelete: false
    
    
    
    kubectl --kubeconfig DEST_ZONE_KUBECONFIG apply -f vm-at-dest.yaml
    

* * *

## 5\. Reference implementation for automated monitoring

Application Operators (AO) can implement the following logic as a bash script, in a programming language, or within their preferred orchestration tools using `kubectl` and `jq`:

Replace the following:

  * PRIMARY_ZONE_KUBECONFIG: The path to the kubeconfig file for the primary zone management API.
  * DEST_ZONE_KUBECONFIG: The path to the kubeconfig file for the destination zone management API.
  * PROJECT_NAME: The name of the project where the replication relationship resides.
  * VRR_NAME: The name of the volume replication relationship reference.
  * SECONDARY_DISK_NAME: The name of the secondary disk promoted to the recovery virtual machine.



### Step 1: Health check loop

Regularly poll the primary API server to check if the environment is responsive:
    
    
    # Loop to check API Health
    HEALTH_STATUS=$(kubectl --kubeconfig PRIMARY_ZONE_KUBECONFIG get --raw /healthz --request-timeout=5s)
    
    if [ "$HEALTH_STATUS" != "ok" ]; then
      echo "Primary site down. Triggering failover evaluation..."
      # Move to Step 2
    fi
    

### Step 2: Apply VolumeFailover

If the primary API is inaccessible or replication lag exceeds the RPO, trigger the failover on the destination cluster:
    
    
    # Apply the VolumeFailover Custom Resource
    cat <<EOF | kubectl --kubeconfig DEST_ZONE_KUBECONFIG apply -f -
    apiVersion: storage.gdc.goog/v1
    kind: VolumeFailover
    metadata:
      name: my-app-failover
      namespace: PROJECT_NAME
    spec:
      volumeReplicationRelationshipRef: VRR_NAME
    EOF
    

### Step 3: Monitor for completion and deploy recovery VM

Monitor the failover state until completion, then deploy the secondary virtual machine:
    
    
    # Wait for failover completion
    STATUS=$(kubectl --kubeconfig DEST_ZONE_KUBECONFIG get volumefailover my-app-failover -n PROJECT_NAME -o jsonpath='{.status.state}')
    
    
    if [ "$STATUS" == "Completed" ]; then
      echo "Failover successful. Deploying recovery VM..."
    
      cat <<EOF | kubectl --kubeconfig DEST_ZONE_KUBECONFIG apply -f -
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachine
    metadata:
      name: recovery-vm
      namespace: PROJECT_NAME
    spec:
      compute:
        virtualMachineType: n3-standard-2-gdc
      disks:
        - virtualMachineDiskRef:
            name: SECONDARY_DISK_NAME
          boot: true
          autoDelete: false
    EOF
    fi
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
