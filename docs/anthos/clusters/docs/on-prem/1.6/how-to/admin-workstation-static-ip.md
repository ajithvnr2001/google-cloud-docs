---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation-static-ip/
title: Creating an admin workstation \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:31.736798+00:00
---

# Creating an admin workstation  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation-static-ip/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Creating an admin workstation Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to create an admin workstation, for Google Distributed Cloud, that you can use to create clusters.

The steps in this document use the `gkeadm` command-line tool, which is available for 64-bit Linux, Windows 10, Windows Server 2019, and macOS 10.15 and higher.

The instructions here are complete. For a shorter introduction to creating an admin workstation, see [Create an admin workstation (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation-quickstart).

## Before you begin

[Know your vCenter server address.](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/vcenter-server-address)

[Know your CA cert path.](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/vcenter-ca-cert-path)

[Install Google Cloud CLI.](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/cloud-sdk)

Create one or more Google Cloud projects as described in [Using multiple Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/multiple-gcp-projects).

## Planning your service accounts

When you use `gkeadm` to create an admin workstation, you have the option of letting `gkeadm` create most of your service accounts and keys for you. In that case, `gkeadm` also grants the appropriate Identity and Access Management roles to the service accounts.

As an alternative, you can create your service accounts and keys manually. In that case, you must manually grant IAM roles to your service accounts.

Creating service accounts manually gives you more flexibility than having `gkeadm` create them for you:

  * Automatically created service accounts are all children of your [connect project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/multiple-gcp-projects#connect_project). When you create a service account manually, you can choose the parent Google Cloud project.

  * Automatically created service accounts are all granted IAM roles on your connect project. This is fine if your connect project is the only Google Cloud project associated with your clusters. But if you want to associate your clusters with [multiple Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/multiple-gcp-projects), then you need the flexibility to grant roles to a service account on a Google Cloud project of your choice.




If you decide to create your own service accounts, follow the instructions in [Service accounts and keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/service-accounts).

Regardless of whether you have `gkeadm` create service accounts for you automatically, there is one service account that you must create manually: your component access service account. For instructions on how to create your component access service account and grant it the appropriate IAM roles, see [Component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/service-accounts#component_access_service_account).

## Generating templates for your configuration files

[Download `gkeadm`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/downloads) to your current directory.

Generate templates:
    
    
    ./gkeadm create config
    

The preceding command created these files in your current directory:

  * `credential.yaml`
  * `admin-ws-config.yaml`



## Filling in `credential.yaml`

In `credential.yaml`, fill in your vCenter username and password. For example:
    
    
    kind: CredentialFile
    items:
    - name: vCenter
      username: "my-account-name"
      password: "AadmpqGPqq!a"
    

## Filling in `admin-ws-config.yaml`

Several fields in `admin-ws-config.yaml` are already filled in with default or generated values. You can keep the populated values or make changes as you prefer.

See the fields that are already filled in.
    
    
    vCenter:
      credentials:
        fileRef:
        path: credential.yaml
        entry: vCenter
    
    adminWorkstation:
      name: gke-admin-ws-...
      cpus: 4
      memoryMB: 8192
    
      diskGB: 50
      dataDiskName: gke-on-prem-admin-workstation-data-disk,,,.vmdk
      dataDiskMB: 512
      network:
        ntpServer: ntp.ubuntu.com
    

### Fields that you must fill in

Fill in the following required fields. For information on how to fill in the fields, [Admin workstation configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation-configuration-file).
    
    
    gcp:
       whitelistedServiceAccountKeyPath: "Fill in"
    vCenter:
      credentials:
        address: "Fill in"
      datacenter: "Fill in"
      datastore: "Fill in"
      cluster: "Fill in"
      network: "Fill in"
      resourcePool: "Fill in"
      caCertPath: "Fill in"
    

If your admin workstation will be behind a proxy server, fill in the `proxyURL` field:
    
    
    adminWorkstation:
      proxyURL: "Fill in"
    

If you want your admin workstation to get its IP address from a DHCP server, set `ipAllocationMode` to `"dhcp"`, and remove the `hostconfig` section:
    
    
    adminWorkstation:
      network:
        ipAllocationMode: "dhcp"
    

If you want to specify a static IP address for your admin workstation, set `ipAllocationMode` to `"static"`, and fill in the [`hostconfig`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation-configuration-file#adminworkstationnetworkhostconfig) section:
    
    
    adminWorkstation:
      network:
        ipAllocationMode: "static"
        hostconfig:
          ip: "Fill in"
          gateway: "Fill in"
          netmask: "Fill in"
          dns:
          - "Fill in"
    

**Note:** Check the vCenter network to make sure the static IP address that you enter is not already in use.

## Creating your admin workstation

Enter this command to create your admin workstation. If you want `gkeadm` to create service accounts for you, include the `--auto-create-service-accounts` flag. If you want to manually create your own service accounts, omit the flag.
    
    
    ./gkeadm create admin-workstation [--auto-create-service-accounts]
    

The output gives detailed information about the creation of your admin workstation:
    
    
    ...
    Getting ... service account...
    ...
    ********************************************************************
    Admin workstation is ready to use.
    
    Admin workstation information saved to /usr/local/google/home/me/my-admin-workstation
    This file is required for future upgrades
    SSH into the admin workstation with the following command:
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.5.1
    ********************************************************************
    

## Getting an SSH connection to your admin workstation

Near the end of the preceding output there is a command you can use to get an SSH connection to your admin workstation. Enter that command now. For example:
    
    
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.5.1
    

List the files on your admin workstation:
    
    
    ls -1
    

In the output, you can see two cluster configuration files, your CA certificate file, and the JSON key file for your component access service account. If `gkeadm` created service accounts for you, you can also see the JSON key files for those service accounts:
    
    
    admin-cluster.yaml
    user-cluster.yaml
    vcenter-ca-cert.pem
    component-access-key.json
    

Verify that `gkeadm` activated your component access service account on your admin workstation:
    
    
    gcloud config get-value account
    

## Copying JSON key file to your admin workstation

Before you create a cluster, the JSON key files for your service accounts must be on your admin workstation in the home directory.

The key for your component access service account is already on your admin workstation.

If you included the `--auto-create-service-accounts` flag when you ran `gkeadm create admin-workstation`, then then the keys for the following service accounts are already on your admin workstation in the home directory. Otherwise you must manually copy the keys to the home directory of your admin workstation:

  * Connect-register service account
  * Connect-agent service account
  * Logging-monitoring service account



If you created any of the following service accounts, you must manually copy the keys for those service accounts to the home directory of your admin workstation:

  * Usage metering service account
  * Audit logging service account
  * Binary authorization service account



## What's next

[Creating an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-admin-cluster)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
