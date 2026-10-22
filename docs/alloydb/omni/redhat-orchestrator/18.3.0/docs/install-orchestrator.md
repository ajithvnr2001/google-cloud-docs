---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-orchestrator/
title: Install the AlloyDB Omni RPM orchestrator \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:55.210248+00:00
---

# Install the AlloyDB Omni RPM orchestrator  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-orchestrator/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Install the AlloyDB Omni RPM orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-orchestrator)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-orchestrator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-orchestrator)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-orchestrator)

AlloyDB Omni using the RPM orchestrator provides an automation platform to install, set up, and manage AlloyDB Omni database clusters on a set of virtual machines (VMs) or bare metal servers. AlloyDB Omni using the RPM orchestrator provides a CLI and Ansible interface which is run on a dedicated control node from which you manage one or more clusters remotely. 

Depending on your automation needs, you can choose between two orchestrator interfaces:

  * AlloyDB Omni orchestrator CLI `alloydbctl`: recommended for environments using shell scripts for automation.
  * AlloyDB Omni orchestrator Ansible collection: recommended for environments that use [Ansible](https://docs.ansible.com)-based automation.



## Limitations

The following limitations apply to this release:

  * This release only supports AlloyDB Omni PostgreSQL 18.
  * This release only supports RHEL version 9-compatible software packages.
  * This release only supports Intel x86 64-bit based platform.
  * Major version upgrades are unsupported in this release.
  * This release does not include instructions to set up Disaster Recovery.
  * This release does not include instructions to set up read pool instances.
  * The AlloyDB Omni monitor does not support SSL connections. You must deploy your monitoring dashboard servers on the same private network as the AlloyDB Omni nodes.



## Before you begin

Before starting the deployment, ensure you meet the following requirements:

### Obtain AlloyDB Omni packages

AlloyDB Omni using the RPM orchestrator software packages are in [Preview](https://cloud.google.com/products#product-launch-stages). You must sign up using the [AlloyDB Omni using RPM orchestrator Preview signup form](https://docs.google.com/forms/d/e/1FAIpQLSdBfJeIDN_cG7IgCCOs8zlyJeXhueTaGZV4lUjSzgteQ2k9LA/viewform) to receive the RPM files.

If you manage software packages through a private Yum repository, then follow the instructions from your repository management to include dependent RPM files in the repository. For more information, see [Software package dependencies](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/package-dependencies).

### Set up a software repository

AlloyDB Omni RPMs are maintained in a global Yum repository. Alternatively, if your organization manages software through a private Yum repository, you must include the RPM packages provided after the signup into your repository according to your management tools. You need your private repository URL during the deployment process.

### Provision machines

Provision a set of VMs running RHEL 9, including:

  * Controller: 1 node that orchestrates the deployment and has passwordless SSH access to all other nodes.
  * Database: 1 or 3 nodes that run the AlloyDB Omni core and monitoring services.
  * Load balancer: 2 optional nodes that run HAProxy and optional connection poolers like PgBouncer.



## Configure network and firewall

Configure your firewall to allow the following TCP ports based on your architecture:

Port | Protocol | Node | Service | Traffic | Notes  
---|---|---|---|---|---  
5432 | TCP | Load balancer | HAProxy | Incoming | On the load balancer node if applicable  
6432 | TCP | Load balancer | PgBouncer | Incoming | Connection pooler if applicable  
9187 | TCP | Database | AlloyDB monitor | Incoming | Monitor if applicable; does not support TLS  
5432 | TCP | Database | AlloyDB | Incoming | 3-node resilient architecture  
6432 | TCP | Database | PgBouncer | Incoming | Connection pooler if applicable on 3-node resilient architecture  
2380 | TCP | etcd | etcd | Incoming | For etcd peer-peer protocol  
- | VRRP | Load balancer | Keepalived | Incoming | Keepalived leader election  
- | VRRP | Database | Keepalived | Incoming | Keepalived leader election on 3-node resilient architecture  
6703 | TCP | Cluster Manager | Cluster Manager | Incoming | Cluster Manager gRPC port  
6702 | TCP | All nodes | Node Manager | Incoming | Node Manager gRPC port  
6700 | TCP | All nodes | Node Manager | Incoming | Node Manager Init gRPC port  
8086 | HTTP | All nodes | Node Manager | Incoming | Node Manager HTTP Port to check primary or standby  
2379 | TCP | etcd | etcd | Incoming | For Cluster Manager to work with etcd  
443 | HTTPS | Database | Cloud Storage | Outgoing | For sending backup data  
  
## Host SELinux mode

AlloyDB Omni supports SELinux in both permissive and enforcing modes.

To enable or disable SELinux, verify that the `/etc/selinux/config` file is updated on all nodes. Prior to bootstrapping the cluster, ensure that SELinux settings are consistent on all database nodes and load balancer nodes. To verify the current settings, use the `getenforce` command.

For more information, see [SELinux policy specifications](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/create-cluster#selinux-policy-specifications).

## Install the orchestrator

###  Ansible 

Use this method if you plan to use Ansible playbooks to manage your clusters.

  1. On your control node, install Ansible and the required Python libraries:
         
         # Install EPEL for RHEL 9
         sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm -y
         # Install Ansible and dependencies
         sudo dnf install ansible
         sudo dnf install python3-grpcio python3-protobuf python3-googleapis-common-protos
         

  2. Download the Ansible collection tar file and its signature, verify the package, and install it:
         
         # Download the collection and its signature
         wget ALLOYDBOMNI_SERVER/google-alloydbomni_orchestrator-0.1.0-1.tar.gz
         wget ALLOYDBOMNI_SERVER/google-alloydbomni_orchestrator-0.1.0-1.tar.gz.asc
         
         # Import the Google Linux signing key
         curl -sS https://dl.google.com/linux/linux_signing_key.pub | gpg --import
         
         # Verify the collection tarball
         gpg --verify google-alloydbomni_orchestrator-0.1.0-1.tar.gz.asc \
         google-alloydbomni_orchestrator-0.1.0-1.tar.gz
         
         # Install the collection
         ansible-galaxy collection install google-alloydbomni_orchestrator-0.1.0-1.tar.gz
         
         # Verify the installation
         ansible-galaxy collection list | grep alloydbomni_orchestrator
         

Replace `ALLOYDBOMNI_SERVER` with the URL of the server where the AlloyDB Omni software packages, including the Ansible collection tar file, are hosted. This source is provided to you after you sign up for the AlloyDB Omni using the RPM orchestrator [Preview](https://cloud.google.com/products#product-launch-stages).




###  alloydbctl 

Use this method if you prefer a command-line utility for managing resources.

  1. Create a Yum configuration file on the control node at `/etc/yum.repos.d/alloydbomni_orchestrator.repo`:
         
         [alloydbomni_orchestrator]
         name=Google AlloyDB Omni orchestrator packages
         baseurl=ALLOYDB_OMNI_ORCHESTRATOR_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         

Replace the following:

     * `ALLOYDB_OMNI_ORCHESTRATOR_REPOSITORY_URL` the URL of the repository containing the AlloyDB Omni orchestrator RPMs.
     * `REPO_GPG_KEY`: the location of Google's public key for GNU Privacy Guard (GPG) verification, for example, `https://dl.google.com/linux/linux_signing_key.pub`. This can also be set as a path if the key is downloaded to a file, for example, `file:///tmp/linux_signing_key.pub`.
  2. Install the package and add the binary to your system's `PATH`:
         
         sudo dnf install alloydbomni_orchestrator
         export PATH=$PATH:/usr/local/bin
         

**Note:** The `yq` package is a dependency for the `alloydbomni_orchestrator`. You can configure `yq` using the EPEL release repository. If a private repository hosts the `yq` package, setting up the EPEL release becomes optional.
  3. Verify the installation by running:
         
         alloydbctl --help
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
