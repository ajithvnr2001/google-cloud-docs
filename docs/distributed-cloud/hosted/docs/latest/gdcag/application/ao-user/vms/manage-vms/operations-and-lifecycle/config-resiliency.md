---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/config-resiliency/
title: VM resiliency \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:36:43.654896+00:00
---

# VM resiliency  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/config-resiliency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  VM resiliency Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an overview of virtual machine (VM) resiliency and optional checks that application operators can enable for deeper insights from within a VM in Google Distributed Cloud (GDC) air-gapped.

This document is for developers within the application operator group who operate VMs. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

VMs in GDC provide HA to improve service continuity in the event of underlying infrastructure or guest failures. You can also configure the system to emit optional health signals that offer deeper insight into VM status.

## VM availability checks

The system provides the following VM availability checks:

Check Name | Description | Mitigation Action Support | Signal Availability  
---|---|---|---  
Guest Health Check | Verifies guest OS health. A prerequisite for other in-guest checks. | Yes | In-Guest Check  
Storage Check | Verifies the VM's underlying storage health. | Yes | In-Guest Check  
Egress Check | Verifies connectivity to a well-known internal endpoint. | No | In-Guest Check and Outside  
Ingress Check | Verifies VM accessibility using its configured ingress (VirtualMachineExternalAccess). | No | In-Guest Check  
  
The mitigation actions can restart the VM and reschedule to another node on frequent failures.

**Note:** These checks can be configured to run using an in-guest agent, which provides more precise health assessments. If the `guest-agent` is not installed or the `guest-health-check` is disabled, the system relies on infrastructure-level metrics, since metrics collected by the guest agent are not available.

### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) that you have the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

### Enable in-guest checks

By default, the in-guest check is disabled if the `guestHealthCheck` is not present.

To enable or disable the in-guest check for a VM, you must update the `GuestEnvironment` in the spec of the VM. This setting collects metrics from inside the VM, provided the guest agent is installed. If the `guestHealthCheck` is not present, the in-guest checks are disabled by default.

  1. Open your VM's configuration file.
  2. Navigate to the `spec:` section.
  3. Add or modify the `guestEnvironment:` and `guestHealthCheck:` fields to enable the check.
  4. Set the `enable` field to true.



Here is an example of the configuration in a YAML file:
    
    
    spec:
      compute:
        virtualMachineType: n2-standard-2-gdc
      guestEnvironment:
        guestHealthCheck:
          enable: true
    

### Verify the checks

After configuring your VM, you can verify the status of the availability checks by inspecting the virtual machine's `Condition` in its `Status`.
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n NAMESPACE_NAME \
      get gvm -o yaml
    

The output shows the status of the various checks. For example, if the `guestHealthCheck` is enabled, the `gvm` status conditions are populated with the `VMGuestHealth` signal.

### Disable VM high availability

By default, VM high availability is enabled if the annotation is not present. You can explicitly disable HA for a specific VM by adding an annotation. Add the annotation to disable VM HA:

  1. Open your VM's configuration file.
  2. Add the `highavailability.virtualmachine.gdc.goog/enable: false` annotation to the VM's metadata to disable high availability.



Here is an example of the annotation in a YAML file:
    
    
    metadata:
      annotations:
        highavailability.virtualmachine.gdc.goog/enable: false
    

## Node failure mitigation

Automated mitigation actions address VM failures and maintain HA. When the underlying infrastructure can no longer support a running VM, the system attempts to fence the unhealthy node and reschedule the VM to a healthy node. The following scenarios can trigger this node level mitigation:

  * **Node partition from API server** : The bare metal node that hosts the VM is partitioned from the Management API server due to a condition like the following:

    * Loss of network connectivity between the API nserver and the node.
    * The `kubelet` agent on the node is down.
    * The node observes a power failure.
  * **User cluster VM partition** : A user cluster worker VM is partitioned from its cluster's Management API server.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
