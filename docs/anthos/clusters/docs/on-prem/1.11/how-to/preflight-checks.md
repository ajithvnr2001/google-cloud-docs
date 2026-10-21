---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/preflight-checks/
title: Running preflight checks \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:40.318516+00:00
---

# Running preflight checks  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/preflight-checks/

**Version 1.11**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.11 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/overview)



Send feedback 

#  Running preflight checks Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.11 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/preflight-checks)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/preflight-checks)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page explains how to run preflight checks against your Google Distributed Cloud configuration file.

## Overview

During installation, you run `gkectl create-config` to generate an Google Distributed Cloud configuration file. The configuration file drives your installation: you provide information about your vSphere environment, your network and load balancer, and how you'd like your clusters to look. You're able to generate a configuration file before or after you've created an admin workstation. For certain checks to pass, they need to be run from the admin workstation.

After you've modified the file to meet the needs of your environment and your clusters, you use the file to create your clusters in your on-prem environment.

Before you create clusters, run [`gkectl check-config`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/reference/gkectl/check-config) to validate the configuration file with several preflight checks. If the command returns any `FAILURE` messages, fix the issues and validate the file again. If a certain feature validation returns any WARNING messages, you must fix the underlying issues before you can use that feature.

**Warning:** Some fields in the configuration file have been deprecated. If you run `gkectl check-config` against a file that has a deprecated field, the command might fail. For an example, see this [release note](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/release-notes#January_03_2020).

### Preflight check modes and skipping validations

`gkectl check-config` has a default mode and a fast mode:

  * In default mode, the command comprehensively validates each field. Also, the default mode creates temporary vSphere virtual machines (VMs) as part of its validations, which can take more time.

  * In fast mode, the command skips checks that create test VMs and runs only the fast checks. You enable fast mode by passing in the `--fast` flag.




You can skip specific validations by passing in other flags, which are described in `gkectl check-config --help`.

### Traffic between the admin workstation and the test VMs

In default mode, the preflight check creates test VMs for the cluster. Each test VM runs an HTTP server that listens on port 443 and on node ports that you specified in your configuration file.

Several IP addresses are assigned to the test VMs. If your configuration file indicates that your cluster nodes will get their IP addresses from a DHCP server, then the preflight check uses a DHCP server to assign IP addresses to the test VMs. If your configuration file indicates that your cluster nodes will be assigned static IP addresses, then the preflight check assigns static IP addresses that you specified in your [IP block files](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/ip-block-file) to the test VMs.

The preflight check, running on the admin workstation, sends HTTP requests to the test VMs using the various IP addresses that are assigned to the VMs. The requests are sent to port 443 and to the node ports that you specified in your configuration file.

### When should I run preflight checks?

It is a best practice to run preflight checks early and before attempting to create clusters. Running preflight checks early can help confirm that you've configured your vSphere environment and your network correctly.

If you are using Google Distributed Cloud version 1.2.0-gke.6, run `gkectl check-config` twice:

  1. Run `gkectl check-config --fast`.

  2. Run `gkectl prepare`.

  3. Run `gkectl check-config` again, without the `--fast` flag.




The reason for running twice is that `gkectl prepare` uploads the VM template for the cluster node OS image to your vSphere environment. That VM template must be in place before you run the full set of validations.

In Google Distributed Cloud version 1.2.1 and later, the `check-config` command itself uploads the VM template, so you can run the full set of validations before you run `gkectl prepare`:

  1. Run `gkectl check-config`, without the `--fast` flag.

  2. Run `gkectl prepare`.




The preflight checks validate the values you've provided to the file. You don't need to fill every field in the configuration file to run preflight checks against the file; rather, you can validate the file iteratively as you populate its fields. For example, if you only wanted to validate your vCenter configuration, you could fill only the `vcenter` fields and run checks against those.

Keep in mind that your Google Distributed Cloud configuration becomes immutable after you've created your clusters. Running preflight checks helps you discover and resolve issues in your configuration before creating your clusters.

### Preserving the test VM for debugging

Starting with Google Distributed Cloud version 1.2.1, the `gkectl check-config` command has a `--cleanup` flag.

When `gkectl check-config` performs a full set of validations, it creates a test VM and an associated SSH key. If you want to preserve the test VM and the SSH key for debugging purposes, set `--cleanup` to false.

The default value of `--cleanup` is true.

## List of preflight checks

The preflight checks validate each field in the configuration file. Here are the current checks:

Category | Description  
---|---  
Configuration file | Generally validates that each field and specification has the expected format and values. Skipped with `--skip-validation-config` flag. Skip `proxy` field validation with `--skip-validation-proxy` flag.  
Internet | Validates internet access to required domains. Validates proxy configuration based on where you are running gkectl. Skipped with the `--skip-validation-internet` flag.  
OS image | Validates that OS images exist. Skipped with the `--skip-validation-os-images` flag.  
Windows OS version | Validates Windows OS version. Validates that the Windows version is supported when creating admin workstations with the command line tool `gkeadm`. Note that while the `gkeadm` tool is available for Windows 10, Windows Server 2019, and Linux, there is no preflight check for Linux. This validation starts from release version 1.4.1.   
Cluster version | Validates that the admin cluster version, user cluster version, and `gkectl` version match for create and upgrade. Skipped with the `--skip-validation-cluster-version` flag.  
Cluster health | Validates that the admin or user cluster is healthy before upgrade:

  * **Admin cluster** : Check includes Kubernetes service, component status, DaemonSets, deployments, machines, and pods.
  * **User cluster** : Check includes Kubernetes service, cluster API endpoints, StatefulSets, deployments, machine deployments, machines, and pods.

Skipped with the `--skip-validation-cluster-health` flag.  
Ingress | Checks to see whether the user cluster has an Istio Gateway object before upgrade. See [Ingress migration](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/ingress-migration).  
Reserved IP | Validates that enough IP addresses are available for create and upgrade. Skipped with the `--skip-validation-reserved-ips` flag.  
Google Cloud |  | Project ID `[*].projectid` | Validates the project IDs provided to various fields in the configuration. If the project ID is missing, the validation is skipped.  
---|---  
Register service account`registerserviceaccountkeypath` | Validates that the service account hold the required IAM roles. Validates that the required APIs are enabled.  
Connect service account`agentserviceaccountkeypath` | Validates that the service account hold the required IAM roles. Validates that the required APIs are enabled.  
Google Cloud Observability service account`stackdriver.serviceaccountkeypath` | Validates that the service account hold the required IAM roles. Validates that the required APIs are enabled.  
Skipped with the `--skip-validation-gcp` flag.   
Access to `gcr.io/gke-on-prem-release` access | Validates access to Google Distributed Cloud's container image registry hosted in Container Registry. Skipped by the `--skip-validation-docker` flag.  
Docker registry |  `privateregistryconfig` If configured, valiates access to the Docker registry. Skipped with the `--skip-validation-docker` flag.  
vCenter | Checks that all `vcenter` fields are present, and also checks the following: |  Credentials `vcenter.credentials.[*]` | Validates authentication to vCenter Server using the provided user credentials.  
---|---  
vSphere version | Validates that vSphere is at version correct.  
Datacenter `vcenter.datacenter` | Validates that the vSphere datacenter exists.  
Datastore `vcenter.datastore` | Validates that the vSphere datastore exists.  
Data disk `vcenter.datadisk` | Validates that the vSphere virtual machine disk (VMDK) does not already exist in vSphere.  
Resource pool `vcenter.resourcepool` | Validates that the vSphere resource pool exists.  
Network `vcenter.network` | Validates that the vSphere network exists.  
vSphere CSI driver | Validates vSphere CSI driver prerequisites.  
  
Skipped with the `--skip-validation-infra` flag.  
  
Hosts for anti-affinity groups | Validates that the number of physical vCenter hosts is at least three if `antiAffinityGroups` is enabled. To disable `antiAffinityGroups` for a cluster, see [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field) and this [release note](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/release-notes#40c10ea4).  Skipped with the `--skip-validation-infra` flag.  
Load balancer | Validates load balancing configuration:

  * If load balancing mode is integrated (`lbmode: Integrated`), validates that all `bigip` fields are present in the `admincluster` and `usercluster` specifications.
  * If load balancing mode is manual (`lbmode: Manual`), validates that all `manuallbspec` fields are present in `admincluster` and `usercluster` specifications.

| Integrated load balancing  
---  
`bigip.credentials.[*]` | Validates your F5 BIG-IP credentials.  
`bigip.partition` | Validates that the partition provided exists.  
F5 BIG-IP user role | Validates that the F5 BIG-IP user provided holds either the Administrator or Resource Administrator role.  
`bigip.vips.[*]` | Validates VIPs provided. Skipped with the `--fast` or `--skip-validation-load-balancer` flags.  
Manual load balancing  
---  
Networking configuration | Validates VIPs, node IPs, etc. Skipped with the `--fast` or `--skip-validation-load-balancer` flags.  
`[*].manuallbspec.[*]` | Validates the provided node ports.  
Skipped with the `--skip-validation-load-balancer` flag.   
Networking | Validates that the provided CIDR ranges, VIPs, and static IPs (if configured) are available. Checks that IP addresses don't overlap. Skipped with the `--skip-validation-net-config` flag.  
DNS | Validates that the provided DNS server is available. Skipped with the `--skip-validation-dns` flag.  
NTP | Validates that the provided Network Time Protocol (NTP) server is available. Skipped with the `--skip-validation-tod` flag.  
VIPs | Pings the VIPs provided. This check is successful if the ping fails, indicating the expected VIP is not already taken. Skipped with the `--skip-validation-vips` flag.  
Node IPs | Pings the node IP addresses provided. This check is successful if the ping fails, indicating the expected node IP is not already taken. Skipped with the `--skip-validation-node-ips` flag.  
  
### Preflight check results

Preflight checks can return the following results:

SUCCESS
    The field and its value passed the check.
FAILURE
    The field and/or its value did not pass the check. If a check returns a `FAILURE` message, fix the issues and validate the file again.
SKIPPED
    

The check was skipped, likely because the check is not relevant to your configuration. For example, if you are using a DHCP server, checks for DNS and node IPs checks—relevant only to a static IP configuration—are skipped.

If you pass in a flag that skips a validation, the skipped check does not return a SKIPPED result; rather, the validation isn't run and doesn't appear in the command output at all.

UNKNOWN
    

The skip returned a non-zero code. You can consider UNKNOWN results to be failed checks. UNKNOWN usually indicates that the check failed to run some system package, such as failing to run nslookup or failing to run gcloud.

### Coming soon

The following preflight checks will be added in a future release:

  * NTP server



## Running preflight checks

You run preflight checks by running the following command:
    
    
    gkectl check-config --config [CONFIG]
    

where [CONFIG] is the path to your Google Distributed Cloud configuration file

### Running in fast mode

If you prefer, you can run preflight checks in "fast mode," which skips the validations that create temporary test VMs, such as the load balancing VIP and node IP validations. To do so, pass in `--fast`:
    
    
    gkectl check-config --config [CONFIG] --fast

### Skipping specific validations

You can pass in flags to granularly skip specific validations, such as DNS, proxy, and networking. Each skip flag is prefixed with `--skip-[VALIDATION]`.

To learn about the available skip flags, run the following command. Optionally, see [gkectl check-config reference](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/reference/gkectl/check-config):
    
    
    gkectl check-config --help

For example, to skip the load balancer validations:
    
    
    gkectl check-config --config my-config.yaml --skip-validation-load-balancer 

### Cancelling preflight checks

If you started running preflight checks and want to cancel, press CTRL + C twice. If a preflight check created a test VM, cancelling should also clean up the VM automatically.

#### Cleaning up a test VM

If a test VM is leftover after preflight checks are complete, you can delete the VM from vCenter. A test VM has a name like this:

`check-config-[dhcp|static]-[random number]`

To delete the VM:

  1. Right-click the VM, and click **Power** > **Power Off**

  2. After the VM has powered off, right-click the VM again, and click **Delete from Disk**.




## Example

Below is an example of the command's output. In this example, the configuration being validated uses integrated load balancing mode and static IPs without an external Docker registry:
    
    
    - Validation Category: Config Check
        - [SUCCESS] Config
    
    - Validation Category: Internet Access
        - [SUCCESS] Internet access to required domains
    
    - Validation Category: GCP
        - [SUCCESS] GCP Service
        - [SUCCESS] GCP Service Account
    
    - Validation Category: Docker Registry
        - [SUCCESS] gcr.io/gke-on-prem-release access
    
    - Validation Category: vCenter
        - [SUCCESS] Credentials
        - [SUCCESS] Version
        - [SUCCESS] Datacenter
        - [SUCCESS] Datastore
        - [SUCCESS] Data Disk
        - [SUCCESS] Resource Pool
        - [SUCCESS] Network
        - [SUCCESS] VSphere CSI Driver
    
    - Validation Category: F5 BIG-IP
        - [SUCCESS] Admin Cluster F5 (credentials, partition and user role)
        - [SUCCESS] User Cluster F5 (credentials, partition and user role)
    
    - Validation Category: Network Configuration
        - [SUCCESS] CIDR, VIP and static IP (availability and overlapping)
    
    - Validation Category: DNS
        - [SUCCESS] DNS (availability)
    
    - Validation Category: VIPs
        - [SUCCESS] ping (availability)
    
    - Validation Category: Node IPs
        - [SUCCESS] ping (availability)
    
    Now running slow validation checks. ...
    
    Reusing VM template "gke-on-prem-osimage-xxx" that already exists in vSphere.
    Creating test VMs with admin cluster configuration...  DONE
    Waiting to get IP addresses from test VMs...  DONE
    Waiting for test VMs to become ready...  DONE
    
    Reusing VM template "gke-on-prem-osimage-xxx" that already exists in vSphere.
    Creating test VMs with user cluster configuration...  DONE
    Waiting to get IP addresses from test VMs...  DONE
    Waiting for test VMs to become ready...  DONE
    
    - Validation Category: F5 BIG-IP
        - [SUCCESS] Admin Cluster VIP and NodeIP
        - [SUCCESS] Admin Cluster F5 Access
        - [SUCCESS] User Cluster VIP and NodeIP
        - [SUCCESS] User Cluster F5 Access
    
    - Validation Category: Internet Access
        - [SUCCESS] Internet access to required domains
    
    - Validation Category: vCenter on test VMs
        - [SUCCESS] Test VM: VCenter Access and Permission
    
    - Validation Category: DNS on test VMs
        - [SUCCESS] Test VM: DNS Availability
    
    - Validation Category: TOD on test VMs
        - [SUCCESS] Test VM: TOD Availability
    
    - Validation Category: Docker Registry
        - [SUCCESS] gcr.io/gke-on-prem-release access
    
    Deleting test VMs with admin cluster configuration...  DONE
    Deleting test VMs with user cluster configuration...  DONE
    

## Known issues

  * For version 1.3.0-gke.16:

You must run fast validation checks, `gkectl check-config --fast`, for your preflight checks if both of the following apply:

    1. You configured Google Distributed Cloud to use a proxy.

    2. You installed one of the following bundles:

       * The `/var/lib/gke/bundles/gke-onprem-vsphere-1.3.0-gke.16.tgz` bundle from the Downloads page.
       * The `/var/lib/gke/bundles/gke-onprem-vsphere-1.3.0-gke.16.tgz` bundle from the admin workstation.

You can run full set of validation only if you installed the full bundle. For example: `/var/lib/gke/bundles/gke-onprem-vsphere-1.3.0-gke.16-full.tgz`

  * For version 1.2.0-gke.6:

If you are using nested resource pools or the default resource pool, `gkectl check-config` fails when you attempt to do a full set of validations. However, you can do a smaller set of validations by passing the `--fast` flag.
        
        gkectl check-config --config [CONFIG] --fast




## What's next

  * [Installing using static IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/install-static-ips)
  * [Installing using a DHCP server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/install-dhcp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
