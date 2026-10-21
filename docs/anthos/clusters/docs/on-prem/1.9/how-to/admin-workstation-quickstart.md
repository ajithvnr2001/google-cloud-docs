---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-workstation-quickstart/
title: Create an admin workstation (quickstart) \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:52.809194+00:00
---

# Create an admin workstation (quickstart)  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-workstation-quickstart/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  Create an admin workstation (quickstart) Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/admin-workstation-quickstart)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/admin-workstation-quickstart)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create an admin workstation for Google Distributed Cloud that you can use to create clusters.

The instructions here are part of a quickstart. For full instructions on how to create an admin workstation, see [Creating an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/create-admin-workstation).

## Before you begin

[Create a Google Cloud project (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/cloud-project-quickstart).

[Create a service account (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/service-account-quickstart).

Know your [vCenter server address](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/vcenter-server-address) and your [CA cert path](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/vcenter-ca-cert-path).

## Generate templates for your configuration files

The steps in this document use the `gkeadm` command-line tool, which is available for 64-bit Linux, Windows 10, Windows Server 2019, and macOS 10.15 and higher.

[Download `gkeadm`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/downloads) to your current directory.

Generate templates:
    
    
    ./gkeadm create config
    

The preceding command created these files in your current directory:

  * `credential.yaml`
  * `admin-ws-config.yaml`



## Fill in `credential.yaml`

In `credential.yaml`, fill in your vCenter username and password. For example:
    
    
    kind: CredentialFile
    items:
    - name: vCenter
      username: "my-account-name"
      password: "AadmpqGPqq!a"
    

## Fill in `admin-ws-config.yaml`

The following fields are filled in for you:
    
    
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
    

Fill in the following required fields. For information on how to fill in the fields, see [Admin workstation configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-workstation-configuration-file).
    
    
    gcp:
       componentAccessServiceAccountKeyPath: "Fill in"
    vCenter:
      credentials:
        address: "Fill in"
      datacenter: "Fill in"
      datastore: "Fill in"
      cluster: "Fill in"
      network: "Fill in"
      resourcePool: "Fill in"
      caCertPath: "Fill in"
    
    network:
      hostConfig:
        ipAllocationMode: Fill in. Set to "static".
        ip: "Fill in"
        gateway: "Fill in"
        netmask: "Fill in"
        dns: "Fill in"
    

If necessary, fill in the [`proxyURL` field](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-workstation-configuration-file#proxyurl-field).
    
    
    adminWorkstation:
      proxyURL: "Fill in"
    

## Create your admin workstation

Create your admin workstation, and automatically create service accounts:
    
    
    ./gkeadm create admin-workstation --auto-create-service-accounts
    

The output gives detailed information about the creation of your admin workstation:
    
    
    ...
    Getting ... service account...
    
    Creating other service accounts and JSON key files...
        - connect-register-sa-2007081316
        - log-mon-sa-2007081316
    ********************************************************************
    Admin workstation is ready to use.
    
    Admin workstation information saved to /usr/local/google/home/me/my-admin-workstation
    This file is required for future upgrades
    SSH into the admin workstation with the following command:
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.5.1
    ********************************************************************
    

In the preceding output, you can see that `gkeadm` created two service accounts for you: a connect register service account and a logging monitoring service account. Those service accounts have the same parent Google Cloud project as your component access service account. Also, `gkeadm` grants roles to those service accounts on that same parent project.

## Getting an SSH connection to your admin workstation

Near the end of the preceding output there is a command you can use to get an SSH connection to your admin workstation. Enter that command now. For example:
    
    
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.5.1
    

List the files on your admin workstation:
    
    
    ls -1
    

In the output, you can see two cluster configuration files, your CA certificate file, and the JSON key files for your service accounts. For example:
    
    
    admin-cluster.yaml
    connect-agent-sa-2007081316.json
    connect-register-sa-2007081316.json
    log-mon-sa-2007081316.json
    user-cluster.yaml
    vcenter-ca-cert.pem
    component-access-key.json
    

## View the active account

Your component access service account is the active account on your admin workstation. To verify this:
    
    
    gcloud config list
    

## What's next

[Seesaw load balancer (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/seesaw-load-balance-quickstart)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
