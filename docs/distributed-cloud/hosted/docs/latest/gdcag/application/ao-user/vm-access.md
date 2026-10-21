---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vm-access/
title: VM access \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:01.601555+00:00
---

# VM access  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vm-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  VM access Stay organized with collections  Save and categorize content based on your preferences. 

This section describes how to open the ingress traffic virtual machine in Google Distributed Cloud air-gapped using an external load balancer.

## Expose a VM using load balancer service

Ingress traffic goes into the Linux VM in your GDC cluster through a service of type _LoadBalancer_ , which directs traffic of some specific ports to your VM.

To enable the ingress traffic of your Linux VM, add the label `ingress.virtualmachines.gpc.gke.io: true` in the YAML file that you use to create the VM. Then a `LoadBalancer` service for ingress traffic is created when the VM instance is created. The service is created in the same namespace as the VM with the name `VM_NAME-default-ingress`.

### Open VM port for ingress traffic

You must explicitly open a port on your VM to accept ingress traffic. For example:
    
    
    kubectl  patch svc VM_NAME-default-ingress -n NAMESPACE_NAME -p \
      '{"spec":{"ports":[{"protocol":"TCP","port":PORT, "name": "NAME"}]}}'
    

Replace the following placeholders:

  * VM_NAME with the name of the VM.
  * NAMESPACE_NAME with the namespace for the service.
  * PORT with the port you want to open on the VM.
  * NAME with the port name.



### Egress

A VM workload in a project can reach the external network, or be exposed to services in other Fleets.

#### Enable egress (by EgressNAT)

Enable an egress NAT gateway for persistent, deterministic routing for egress traffic using predefined IP addresses. This lets you create more specific firewall and routing rules.

### NetworkPolicy

You can set network policy for container workloads at the project level. A project might be across multiple default bare metal user clusters.

### Connect to a Linux VM using SSH

To connect to a Linux VM using SSH, use the load balancer service's IP address. SSH port 22 is open by default for the VM.

#### Get the load balancer service IP address

The following example output shows the load balancer service is ready to direct SSH traffic on TCP port 22 if the IP address is `10.200.0.102`:
    
    
    kubectl get services VM_NAME-default-ingress -n NAMESPACE_NAME
    
    TYPE          CLUSTER-IP   EXTERNAL-IP    PORT(S)        AGE
    LoadBalancer  10.106.6.18  10.200.0.102   22:32443/TCP   11s
    

#### Connect to the VM

To connect to your VM, use the IP address of the load balancer service and your SSH key. For example, you might connect from your bootstrap machine.
    
    
    ssh -i /path/to/KEY_NAME ubuntu@10.200.0.102
    

## Transfer files to or from a VM

To transfer files to Distributed Cloud VM instances, different options are available depending on your workstation OS and the target VM instance OS.

### Transfer files to Linux VMs

Establish an SSH connection to a VM and use that connection to transfer files to the VM.

### Transfer a file from a VM

You can also copy files and directories from a VM to your local workstation. Use the following command (TBD) to recursively copy a directory from your VM (the source) to your local workstation (the destination). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
