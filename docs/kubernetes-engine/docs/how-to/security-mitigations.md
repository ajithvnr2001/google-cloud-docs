---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-mitigations/
title: Mitigate security incidents \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:09.920271+00:00
---

# Mitigate security incidents  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-mitigations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Mitigate security incidents Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes common mitigations and responses to potential security incidents on your Google Kubernetes Engine (GKE) clusters and containers.

This document is for Security specialists looking for guidance when responding to GKE security incidents. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

The suggestions in [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) can improve the security of your GKE workloads. Security incidents, however, can occur even when measures to protect your workloads are in place.

## Detect incidents

To detect potential incidents, we recommend you set up a process that collects and monitors your workload's logs. Then, set up alerts based on abnormal events detected from logs. Alerts notify your security team when something unusual is detected. Your security team can then review the potential incident.

You can customize alerts based on specific metrics or actions. For example, alerting on high CPU usage on your GKE nodes may indicate they are compromised for cryptomining.

Alerts should be generated where you aggregate your logs and metrics. For example, you can use GKE [Audit Logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging) in combination with [logs-based alerting](https://docs.cloud.google.com/logging/docs/logs-based-metrics) in Cloud Logging.

To learn more about security-relevant queries, see the [Audit Logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging#example_filters_for_your_admin_activity_log) documentation.

## Respond to a security incident

After you have been alerted to an incident, take action. Fix the vulnerability if you can. If you do not know the root cause of the vulnerability or do not have a fix ready, apply mitigations.

The mitigations you might take depend on the severity of the incident and your certainty that you have identified the issue.

This guide covers actions you can take after you detect an incident on a workload running on GKE. You could, in increasing order of severity:

  * **Snapshot the host VM's disk**. A snapshot lets you perform some forensics on the VM state at the time of the anomaly after the workload has been redeployed or deleted.
  * **Inspect the VM while the workload continues to run**. Connecting to the host VM or workload container can provide information about the attacker's actions. We recommend you reduce access before inspecting the live VM**.**

  * **Redeploy a container**. Redeploying ends currently running processes in the affected container and restarts them.

  * **Delete a workload**. Deleting the workload ends currently running processes in the affected container without a restart.




These mitigations are described in the following sections.

## Before you begin

The methods used in this topic use the following information:

  * The name of the Pods you think have been compromised, or `POD_NAME`.
  * The name of the host VM running the container or Pods, or `NODE_NAME`.



Also, before taking any of the actions, consider if there will be a negative reaction from the attacker if they are discovered. The attacker may decide to delete data or destroy workloads. If the risk is too high, consider more drastic mitigations such as deleting a workload before performing further investigation.

## Snapshot the VM's disk

Creating a snapshot of the VM's disk allows forensic investigation after the workload has been redeployed or deleted. Snapshots can be created while disks are attached to running instances.

**Note:** Snapshots only capture state written to disk. Snapshots do not capture contents of the VM's memory.

  1. To snapshot your persistent disk, first find the disks attached to your VM. Run the following command and look at the `source` field:
         
         gcloud compute instances describe NODE_NAME --zone COMPUTE_ZONE \
             --format="flattened([disks])"
         

  2. Look for the lines that contain `disks[NUMBER].source`. The output is similar to the following:
         
         disks[0].source: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/COMPUTE_ZONE/disks/DISK_NAME
         

The disk name is the portion of the source name after the final slash. For example disk name is `gke-cluster-pool-1-abcdeffff-zgt8`.

  3. To complete the snapshot, run the following command:
         
         gcloud compute disks snapshot DISK_NAME
         




For more information, see [Creating persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) in the Compute Engine documentation.

## Inspect the VM

**Caution:** In severe incidents, workloads on the same node or the same cluster may also be compromised. This is known as a container escape. Monitor all of your workloads for abnormal behavior and take appropriate actions.

Consider what access an attacker may have before taking action. If you suspect a container has been compromised and are concerned about informing the attacker, you can [connect to](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/) the container and inspect it without disrupting your workloads. Inspecting is useful for quick investigation before taking more disruptive actions. Inspecting is also the least disruptive approach to the workload, but it doesn't stop the incident.

Alternatively, to avoid logging into a machine with a privileged credential, you can analyze your workloads by setting up live forensics (such as [GRR Rapid Response](https://grr-doc.readthedocs.io/en/latest/)), on-node agents, or network filtering.

### Reduce access before inspecting the live VM

By [cordoning](https://kubernetes.io/docs/concepts/architecture/nodes/#manual-node-administration), [draining](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/), and limiting network access to the VM hosting a compromised container, you can _partially_ isolate the compromised container from the rest of your cluster. Limiting access to the VM reduces risk but does not prevent an attacker from moving laterally in your environment if they take advantage of a critical vulnerability.

#### Cordon the node and drain the other workloads from it

Cordoning and draining a node moves workloads colocated with the compromised container to other VMs in your cluster. Cordoning and draining reduces an attacker's ability to impact other workloads on the same node. It does not necessarily prevent them from inspecting a workload's persistent state (for example, by inspecting container image contents).

**Caution:** `kubectl cordon` marks a node as 'unschedulable', which has the side effect of the service controller removing the node from any LoadBalancer node target lists it was previously eligible for, effectively removing incoming load balancer traffic from the cordoned node(s). This issue applies to GKE versions 1.18 and earlier.

  1. Use `kubectl` to cordon the node and ensure that no other Pods are scheduled on it:
         
         kubectl cordon NODE_NAME
         

**Caution:** Draining evicts other workloads from the same node, which might cause downtime. Using `kubectl drain` will respect PodDisruptionBudgets, but it assumes Pods are configured to be automatically re-created on other nodes after eviction.

After cordoning the node, drain the node of other Pods.

  2. Label the Pod that you are quarantining:
         
         kubectl label pods POD_NAME quarantine=true
         

Replace `POD_NAME` with the name of the Pod that you want to quarantine.

  3. Drain the node of Pods that are not labeled with `quarantine`:
         
         kubectl drain NODE_NAME --pod-selector='!quarantine'
         




#### Restrict network access to the node

We recommended blocking both internal and external traffic from accessing the host VM. Next, allow inbound connections from a specific VM on your network or VPC to connect to the quarantined VM.

The first step is to abandon the VM from the [Managed Instance Group](https://docs.cloud.google.com/compute/docs/instance-groups) that owns it. Abandoning the VM prevents the node from being marked unhealthy and auto-repaired (re-created) before your investigation is complete.

To abandon the VM, run the following command:
    
    
    gcloud compute instance-groups managed abandon-instances INSTANCE_GROUP_NAME \
        --instances=NODE_NAME
    

### Firewall the VM

[Creating a firewall](https://docs.cloud.google.com/vpc/docs/using-firewalls) between the affected container and other workloads in the same network helps prevent an attacker from moving into other parts of your environment while you conduct further analysis. Since you already drained the VM of other containers, this only affects the quarantined container.

The following instructions on firewalling the VM prevents:

  * **New** outbound connections to other VMs in your cluster using an egress rule.
  * Inbound connections to the compromised VM using an ingress rule.

**Note:** Firewalls have several limitations. 

  1. Adding firewall rules doesn't close existing connections. Removing the VM's external IP address (described in the following section) breaks existing connections from the external internet, although not from inside your network.
  2. An attacker who compromises a privileged container or breaks out of an unprivileged container can access the VM's [metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata). We recommend using [Shielded GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) to remove the privileged bootstrap keys from the metadata server.



To firewall the VM off from your other instances, follow these steps for the node that hosts the Pod you want to quarantine:

  1. Tag the instance so you can apply a new firewall rule.

**Note:** Check that the tag does not conflict with other VMs before applying it.
         
         gcloud compute instances add-tags NODE_NAME \
             --zone COMPUTE_ZONE \
             --tags quarantine
         

  2. Create a firewall rule to deny all egress TCP traffic from instances with the `quarantine` tag:
         
         gcloud compute firewall-rules create quarantine-egress-deny \
             --network NETWORK_NAME \
             --action deny \
             --direction egress \
             --rules tcp \
             --destination-ranges 0.0.0.0/0 \
             --priority 0 \
             --target-tags quarantine
         

  3. Create a firewall rule to deny all ingress TCP traffic to instances with the `quarantine` tag. Give this ingress rule a `priority` of `1`, which lets you override it with another rule that allows SSH from a specified VM.
         
         gcloud compute firewall-rules create quarantine-ingress-deny \
             --network NETWORK_NAME \
             --action deny \
             --direction ingress \
             --rules tcp \
             --source-ranges 0.0.0.0/0 \
             --priority 1 \
             --target-tags quarantine
         




#### Remove the VM's external IP address

Removing the VM's external IP address breaks any existing network connections outside your VPC.

To remove the external address of a VM, perform the following steps:

  1. Find and delete the access config that associates the external IP with the VM. First find the access config by describing the VM:
         
         gcloud compute instances describe NODE_NAME \
             --zone COMPUTE_ZONE --format="flattened([networkInterfaces])"
         

Look for the lines that contain `name` and `natIP`. They look like the following:
         
         networkInterfaces[0].accessConfigs[0].name:              ACCESS_CONFIG_NAME
         networkInterfaces[0].accessConfigs[0].natIP:             EXTERNAL_IP_ADDRESS
         

  2. Find the value of `natIP` that matches the external IP you want to remove. Note the name of the access config.

  3. To remove the external IP, run the following command:
         
         gcloud compute instances delete-access-config NODE_NAME \
             --access-config-name "ACCESS_CONFIG_NAME"
         




### SSH to the host VM via an intermediate VM

After you remove the host VM's external IP, you cannot ssh from outside your VPC. You access it from another VM in the same network. For the rest of this section, we refer to this as the **intermediate VM**.

#### Prerequisites

  * An intermediate VM with access to the subnetwork of the host VM. If you do not already have one, [create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) for this purpose.
  * The internal IP address of the intermediate VM.
  * An SSH public key from the intermediate VM. To learn more, see [Managing SSH Keys](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys#locatesshkeys)



#### Connecting to the host VM

  1. Add the intermediate VM's public key to the host VM. For more information, see [Adding and Removing SSH keys](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys) in the Compute Engine documentation.
  2. Add a tag to the intermediate VM.

**Note:** Check that the tag does not conflict with other VMs in your network before applying it.
         
         gcloud compute instances add-tags INTERMEDIATE_NODE_NAME \
           --zone COMPUTE_ZONE \
           --tags intermediate
         

  3. Add an ingress allow rule to override the deny rule you added earlier. To add the rule, run the following command.
         
         gcloud compute firewall-rules create quarantine-ingress-allow \
             --network NETWORK_NAME \
             --action allow \
             --direction ingress \
             --rules tcp:22 \
             --source-tags intermediate \
             --priority 0 \
             --target-tags quarantine
         

This rule allows incoming traffic on port 22 (SSH) from VMs in your network with the `intermediate` tag. It overrides the deny rule with a `priority` of `0`.

  4. Connect to the quarantined VM with using its internal IP:
         
         ssh -i KEY_PATH USER@QUARANTINED_VM_INTERNAL_IP
         

Replace the following:

     * `KEY_PATH`: the path to your SSH private key.
     * `USER`: your Google Cloud account's email address.
     * `QUARANTINED_VM_INTERNAL_IP`: the internal IP address.



## Redeploy a container

By redeploying your container, you start a fresh copy of the container and delete the compromised container.

You redeploy a container by deleting the Pod that hosts it. If the Pod is managed by a higher-level Kubernetes construct (for example, a Deployment or DaemonSet), deleting the Pod schedules a new Pod. This Pod runs new containers.

Redeploying makes sense when:

  * You already know the cause of the vulnerability.
  * You think it takes an attacker significant effort or time to compromise your container again.
  * You think that the container might quickly get compromised again and you don't want to take it offline, so you plan to place it in a [sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) to limit the impact.

**Note:** **If you have a fix for the vulnerability, roll out the fix first, then migrate traffic to the replacement workload.** Redeploying a Pod does not fix security issues. An attacker might repeat the same exploit chain again. Attacks can continue until a fix has been deployed.

When redeploying the workload, if the possibility of another compromise is high, consider placing the workload in a sandbox environment such as [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods). Sandboxing limits access to the host node kernel if the attacker compromises the container again.

To redeploy a container in Kubernetes, delete the Pod that contains it:
    
    
    kubectl delete pods POD_NAME --grace-period=10
    

If the containers in the deleted Pod continue to run, you can delete the workload.

To redeploy the container within a sandbox, follow the instructions in [Harden workload isolation with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).

## Delete a workload

Deleting a workload, such as a Deployment or DaemonSet, causes all of its member Pods to be deleted. All containers inside those Pods stop running. Deleting a workload can make sense when:

  * You want to stop an attack in progress.
  * You are willing to take the workload offline.
  * Stopping the attack immediately is more important than application uptime or forensic analysis.

**Caution:** Deleting a workload takes the entire application offline.

To delete a workload, use `kubectl delete CONTROLLER_TYPE`. For example, to delete a Deployment, run the following command:
    
    
    kubectl delete deployments DEPLOYMENT
    

If deleting the workload doesn't delete all associated Pods or containers, you can manually delete the containers using `crictl`, the container runtime's CLI tool.

**Note:** If you manually delete a container before deleting the workload, Kubernetes redeploys the container.

Stop or remove containers with `crictl`.

To stop a container in `containerd`, run the following command:
    
    
    crictl stop CONTAINER
    

To remove a container in `containerd`, run the following command:
    
    
    crictl rm -f CONTAINER
    

## Delete the host VM

**Warning:** Deleting a VM stops any workloads co-located on the node. Cordon and drain the node first to limit disruption.

If you are unable to delete or remove the container, you can delete the virtual machine that hosts the affected container.

If the Pod is still visible, you can find the name of the host VM with the following command:
    
    
    kubectl get pods --all-namespaces \
      -o=custom-columns=POD_NAME:.metadata.name,INSTANCE_NAME:.spec.nodeName \
      --field-selector=metadata.name=POD_NAME
    

To delete the host VM, run the following `gcloud` command:
    
    
    gcloud compute instance-groups managed delete-instances INSTANCE_GROUP_NAME \
        --instances=NODE_NAME
    

Abandoning the instance from the Managed Instance Group reduces the size of the group by one VM. You can manually add one instance back to the group with the following command:
    
    
    gcloud compute instance-groups managed resize INSTANCE_GROUP_NAME \
        --size=SIZE
    

## What's next

  * [Performing forensics on containers](https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-performing-forensics-on-containers)
  * [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)
  * [Forensic analysis for GKE applications](https://docs.cloud.google.com/solutions/security-controls-and-forensic-analysis-for-GKE-apps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
