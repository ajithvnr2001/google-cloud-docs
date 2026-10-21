---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/troubleshoot-cloud-nat/
title: Troubleshoot Cloud NAT \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:54.611802+00:00
---

# Troubleshoot Cloud NAT  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/troubleshoot-cloud-nat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Troubleshoot Cloud NAT Stay organized with collections  Save and categorize content based on your preferences. 

This guide helps you diagnose why your workloads (Pods or VMs) cannot access external networks using Cloud NAT. As a developer, you primarily interact with the `CloudNatGateway` resource. The status of this resource is your primary source of truth for debugging.

## Before you begin

To troubleshoot a Cloud NAT configuration, you must have the following:

  * The necessary identity and access roles. Ask your Project IAM Admin to grant you one or both of the following roles: 
    * **Cloud NAT Viewer (`cloud-nat-viewer`)**: This role offers read-only access to Cloud NAT resources. This role gets you started on diagnosing the problem.
    * **Cloud NAT Developer (`cloud-nat-developer`)**: This role provides the necessary permissions for application operators to Create, Read, Update, and Delete (CRUD) Cloud NAT objects within their assigned projects. This role lets you perform many of the fixes described on this page.
    * Additional roles may be needed for some specific diagnostic measures and fixes.



## Initial diagnostics

Before diving into error codes, ensure that the basic resources are present and reachable.

**Command:**
    
    
    kubectl get cloudnatgateway GATEWAY_NAME -n PROJECT_NAMESPACE -o yaml
    

Replace the following:

  * `GATEWAY_NAME`: The name of the `CloudNatGateway` resource.
  * `PROJECT_NAMESPACE`: The namespace of your project.



**Check the Status Conditions:** A healthy gateway must have **all** the following conditions set to `True`:

  * `Ready`: Global health status.
  * `SubnetsReady`: The IP pool configuration is valid.
  * `PerimeterConfigurationReady`: The upstream network infrastructure is configured.
  * `EgressRoutesReady`: The routing policies for your pods are active.



If any of these are `False`, check the `reason` and `message` fields in the status output and refer to the tables in the following sections.

## Error code reference and remediation

The error codes returned by `kubectl get cloudnatgateway` fall into three main categories.

### Subnet errors (`SubnetsReady` is False)

This condition indicates issues with the IP address pool assigned to the gateway.

Error Code | What It Means | Remediation Steps  
---|---|---  
`CloudNATSelectorFieldOverlapsCode` | **Configuration Conflict.** The `workloadSelector` of this gateway matches the same workloads as another gateway in your project. Traffic cannot be deterministically routed. | 

  1. List all Cloud NAT gateways in your project: `kubectl get cloudnatgateway`
  2. Compare the `workloadSelector` of this gateway with others.
  3. Modify the labels so that no single Pod/VM is selected by more than one gateway.

  
`CloudNATSubnetRefsFieldInvalidCode` | **Invalid Subnet.** The subnet specified in `subnetRefs` is unusable. Common reasons:

  * Subnet does not exist.
  * Subnet is not in `Ready` state.
  * Subnet is not of type `Leaf`.

| 

  1. Verify the subnet exists: `kubectl get subnet <SUBNET_NAME>`
  2. Check the subnet status is `Ready`.
  3. Ensure the subnet `type` is `Leaf` (Cloud NAT cannot use Root or Loopback subnets).

  
`CloudNATSubnetAlreadyInUseCode` | **Subnet Conflict.** The subnet you requested is already "owned" by another Cloud NAT gateway. A subnet can only be attached to one gateway at a time. | 

  1. Choose a different subnet for this gateway.
  2. Or, remove the subnet from the other gateway first.

  
`UNETAPIServerErrorCode` | **System Error.** The controller cannot talk to the API server to validate subnets. | **Action:** This is likely a temporary platform issue. If it persists, contact your Platform Administrator.  
  
### Perimeter configuration errors (`PerimeterConfigurationReady` is False)

This condition reflects the status of the perimeter gateways.

Error Code | What It Means | Remediation Steps  
---|---|---  
`NET-E0305` | **Configuration Conflict.** (Same as above). Overlapping selectors prevent the system from calculating the correct routing group. | 

  1. List all Cloud NAT gateways in your project: `kubectl get cloudnatgateway`
  2. Compare the `workloadSelector` of this gateway with others.
  3. Modify the labels so that no single Pod/VM is selected by more than one gateway.

  
`NET-E0301` | **Resource Exhaustion / Node Failure.** The system created the configuration, but couldn't assign your egress IPs to a healthy physical node. This usually means either the subnet is out of IPs or the gateway nodes are down. | 

  1. Check your [Subnet](/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview) usage. Is it full?
  2. If the Subnet has free IPs and is `Ready`, this indicates a platform-side infrastructure failure (e.g., no healthy gateway nodes available). **Action** : Contact Platform Administrator.

  
`NET-E0001` | **System Error.** Controller communication failure. | **Action:** Contact Platform Administrator.  
  
### Egress route errors (`EgressRoutesReady` is False)

This condition reflects the status of the routing policies inside the cluster.

Error Code | What It Means | Remediation Steps  
---|---|---  
`NET-E0305` | **Configuration Conflict.** (Same as above). | 

  1. List all Cloud NAT gateways in your project: `kubectl get cloudnatgateway`
  2. Compare the `workloadSelector` of this gateway with others.
  3. Modify the labels so that no single Pod/VM is selected by more than one gateway.

  
`NET-E0304` | **Programming Failure.** The system failed to program the routing rules (BPF) for your specific gateway IPs. | **Action:** This is an internal programming error or state inconsistency.

  1. Try making a trivial update to the Gateway (e.g., edit a label) to trigger a reconciliation.
  2. If it persists, contact the Platform Administrator.

  
  
## Other common issues

If the Gateway status is `Ready: True` but traffic is still failing, check these common misconfigurations:

### Missing project-level permission

Your project must be explicitly authorized to egress traffic.

  * **Check:** Does your Project resource have the label `networking.gdc.goog/enable-default-egress-allow-to-outside-the-org: "true"`?
  * **Fix:** Ask your Project Admin to apply this label.



### Missing VM annotation (Virtual Machines Only)

VMs bypass the standard Pod egress path and need explicit instruction to use Cloud NAT.

  * **Check:** Does the `VirtualMachineExternalAccess` (VMEA) object for your VM have the annotation `egress.networking.gke.io/use-cloud-nat: "true"`?
  * **Fix:** Add the annotation to the VMEA object.



### Standard cluster node egress

If you are running a Standard Cluster, the nodes themselves need permission to egress.

  * **Check:** Does the `Cluster` object have the label `cluster.gdc.goog/enable-node-egress-to-outside-the-org: "true"`?
  * **Fix:** Ask your Platform Admin to label the Cluster object.



### Default Egress NAT versus Cloud NAT collision

A common configuration error occurs when a workload is configured to use the legacy Default Egress NAT mechanism while simultaneously being selected by a Cloud NAT Gateway. This combination results in a collision where the data plane receives conflicting routing instructions, leading to packet loss or non-deterministic routing behavior.

#### Diagnose Pod collisions

For Pods, the Default Egress NAT is typically enabled by adding a specific label. A Pod cannot have this label while also being targeted by a Cloud NAT Gateway.

  1. **Identify the Target Pod:** Get the labels of the Pod experiencing connectivity issues.
         
         kubectl get pod <POD_NAME> -n <NAMESPACE> --show-labels
         

  2. **Check for Conflicting Labels:**

     * **Cloud NAT Selection:** Do the Pod's labels match the `workloadSelector` of any `CloudNatGateway` in the namespace?
     * **Default Egress Label:** Does the Pod have the label `egress.networking.gke.io/enabled: "true"`?

**Condition:** If **BOTH** are true, you have a collision.

  3. **Resolution:** Remove the legacy default egress label from the Pod (or its parent Deployment/StatefulSet) to allow Cloud NAT to take over exclusive control.




#### Diagnose VM collisions

For Virtual Machines, the mechanism is different. VMs with `VirtualMachineExternalAccess` (VMEA) objects are often configured for default access. To use Cloud NAT, they must explicitly opt-in by adding an annotation to disable the default path and enable the Cloud NAT path.

  1. **Identify the VMEA:** Find the `VirtualMachineExternalAccess` object associated with the VM.
         
         kubectl get vmea -n <NAMESPACE>
         

  2. **Check for Missing Annotation:**

     * **Cloud NAT Selection:** Do the VM's labels match a `CloudNatGateway`?
     * **Opt-in Annotation:** Check the VMEA for the annotation `egress.networking.gke.io/use-cloud-nat: "true"`.

**Condition:** If the VM matches a gateway but **LACKS** this annotation, traffic will collide with the default egress system.

  3. **Resolution:** Add the annotation to the VMEA object.
         
         kubectl annotate vmea <VMEA_NAME> -n <NAMESPACE> egress.networking.gke.io/use-cloud-nat="true"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
