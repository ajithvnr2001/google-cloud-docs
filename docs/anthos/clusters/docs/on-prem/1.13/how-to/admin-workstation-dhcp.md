---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-workstation-dhcp/
title: Creating an admin workstation \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:19.678558+00:00
---

# Creating an admin workstation  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-workstation-dhcp/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  Creating an admin workstation Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-admin-workstation)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-admin-workstation)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create an admin workstation, for Google Distributed Cloud, that you can use to create clusters.

The steps in this document use the `gkeadm` command-line tool, which is available for 64-bit Linux, Windows 10, Windows Server 2019, and macOS 10.15 and higher.

The instructions here are complete. For a shorter introduction to creating an admin workstation, see [Create an admin workstation (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-workstation-quickstart).

## Before you begin

[Know your vCenter server address.](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/vcenter-server-address)

[Know your CA cert path.](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/vcenter-ca-cert-path)

[Install the Google Cloud CLI.](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/cloud-sdk)

Create one or more Google Cloud projects as described in [Using multiple Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/multiple-gcp-projects).

## Planning your service accounts

When you use `gkeadm` to create an admin workstation, you have the option of letting `gkeadm` create some of your service accounts and keys for you. In that case, `gkeadm` also grants the appropriate Identity and Access Management roles to the service accounts.

As an alternative, you can create your service accounts and keys manually. In that case, you must manually grant IAM roles to your service accounts.

Creating service accounts manually gives you more flexibility than having `gkeadm` create them for you:

  * Automatically created service accounts all have the same parent Google Cloud project as your component access service account. When you create a service account manually, you can choose the parent Google Cloud project.

  * Automatically created service accounts are all granted IAM roles on the parent Google Cloud project of your component access service account. This is fine if that is the only Google Cloud project associated with your clusters. But if you want to associate your clusters with [multiple Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/multiple-gcp-projects), then you need the flexibility to grant roles to a service account on a Google Cloud project of your choice.




If you decide to create your own service accounts, follow the instructions in [Service accounts and keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts).

Regardless of whether you have `gkeadm` create service accounts for you automatically, there is one service account that you must create manually: your component access service account. For instructions on how to create your component access service account and grant it the appropriate IAM roles, see [Component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts#component_access_service_account).

## Generating templates for your configuration files

[Download `gkeadm`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/downloads) to your current directory.

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

**Note:** Admin workstations cannot contain special characters and cannot be renamed after creation.

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
    
      diskGB: 100
      dataDiskName: gke-on-prem-admin-workstation-data-disk,,,.vmdk
      dataDiskMB: 512
      network:
        ntpServer: ntp.ubuntu.com
    

### Fields that you must fill in

Fill in the following required fields. For information on how to fill in the fields, [Admin workstation configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-workstation-configuration-file).
    
    
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
    

If you want to create your admin workstation inside a vSphere VM folder, fill in the `vCenter.folder` field:
    
    
    vCenter:
      folder: "Fill in"
    

If your admin workstation will be behind a proxy server, fill in the `proxyURL` field:
    
    
    adminWorkstation:
      proxyURL: "Fill in"
    

If you want your admin workstation to get its IP address from a DHCP server, set `ipAllocationMode` to `"dhcp"`, and remove the `hostconfig` section:
    
    
    adminWorkstation:
      network:
        ipAllocationMode: "dhcp"
    

If you want to specify a static IP address for your admin workstation, set `ipAllocationMode` to `"static"`, and fill in the [`hostconfig`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-workstation-configuration-file#adminworkstationnetworkhostconfig) section:
    
    
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

## Logging in

The Google Account that is set as your [SDK `account` property](https://docs.cloud.google.com/sdk/docs/properties) is called your _SDK account_. The `gkeadm` command-line tool uses your SDK account to download the admin workstation OVA and enable services in your Google Cloud project.

If you choose to have `gkeadm` automatically create service accounts for you, then `gkeadm` also uses your SDK account to create service accounts and keys, and to grant roles to service accounts. So it is important that you set your SDK `account` property before you run `gkeadm` to create an admin workstation.

Log in with any Google Account. This sets your SDK `account` property:
    
    
    gcloud auth login
    

Verify that your SDK `account` property is set correctly:
    
    
    gcloud config list
    

The output shows the values of your SDK `account` property. For example:
    
    
    [core]
    account = my-name@google.com
    disable_usage_reporting = False
    Your active configuration is: [default]
    

## Grant roles to your SDK account

Your SDK account must have the following [IAM role](https://docs.cloud.google.com/iam/docs/overview) on the parent Google Cloud project of your component access service account. This is so that `gkeadm` can enable services on the Google Cloud project.

  * `serviceUsage.serviceUsageAdmin`



If you choose to have `gkeadm` automatically create service accounts for you, then your SDK account must also have the following roles on the parent project of your component access service account. This is so that `gkeadm` can create service accounts and keys.

  * `resourcemanager.projectIamAdmin`
  * `iam.serviceAccountCreator`
  * `iam.serviceAccountKeyAdmin`



To grant roles on a Google Cloud project, you must have certain permissions on the Google Cloud project. For details, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If you have the required permissions, you can grant the roles yourself. Otherwise, someone else in your organization must grant the roles for you.

To grant the required role to your SDK account:

### Linux and macOS
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/serviceusage.serviceUsageAdmin"
    

### Windows
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/serviceusage.serviceUsageAdmin"
    

Replace the following:

  * `PROJECT_ID`: the ID of the parent Google Cloud project of your component access service account

  * `ACCOUNT`: your SDK account




To grant additional roles in case you want `gkeadm` to automatically create service accounts"

### Linux and macOS
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/iam.serviceAccountKeyAdmin"
    

### Windows
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountKeyAdmin"
    

Replace the following:

  * `PROJECT_ID`: the ID of the parent project of your component access service account

  * `ACCOUNT`: your SDK account




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
    

In the output, you can see two cluster configuration files, your CA certificate file, and the JSON key file for your component access service account. If `gkeadm` created service accounts for you, you can also see the JSON key files for those service accounts. For example:
    
    
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
  * Logging-monitoring service account



If you created any of the following service accounts, you must manually copy the keys for those service accounts to the home directory of your admin workstation:

  * Usage metering service account
  * Audit logging service account
  * Binary authorization service account



## Restoring the admin workstation from a backup file

When you upgrade an admin workstation, then by default the `gkeadm` upgrade command also saves a backup file. Later, if you no longer have an admin workstation, or if you have lost some of the files that were on your upgraded admin workstation, you can use this backup file to create an admin workstation that is restored to what was in place immediately after the upgrade.

To create an admin workstation from a backup file, run this command:
    
    
    gkeadm create admin-workstation --restore-from-backup ADMIN_WORKSTATION_NAME-backup.tar.gz
    

Replace ADMIN_WORKSTATION_NAME with the name of the admin workstation.

## What's next

[Creating an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-admin-cluster)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
