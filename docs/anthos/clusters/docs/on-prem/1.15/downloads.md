---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/downloads/
title: Google Distributed Cloud downloads \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:30.903965+00:00
---

# Google Distributed Cloud downloads  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/downloads/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Google Distributed Cloud downloads Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/downloads)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/downloads)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to download the `gkeadm` command-line tool and other components that are part of Google Distributed Cloud.

Typically, `gkeadm` is the only component that you have to download manually. For example, you don't need to manually download `gkectl`, or the Google Distributed Cloud bundle file, because they are automatically copied to the admin workstation. Also, you don't have to manually download the Admin workstation Open Virtual Appliance (OVA), because `gkeadm` automatically copies the OVA to your vSphere environment.

## Before you begin

You must be logged in with a [Google Account](https://www.google.com/account/about/).

To see whether you are logged in, view your SDK `account` [property](https://docs.cloud.google.com/sdk/docs/properties):
    
    
    gcloud config get-value account
    

To sign in:
    
    
    gcloud auth login
    

## Download `gkeadm`

You use the `gkeadm` command-line tool to create an admin workstation. Then you get an SSH connection to your admin workstation, and from there, you create clusters.

The `gkeadm` command-line tool is available for 64-bit Linux.

`gkeadm` is also available for macOS 10.15 and higher, Windows 10, and Windows Server 2019. However, support for macOS and Windows is deprecated and will be removed in a future release.

### Linux
    
    
    gcloud storage cp gs://gke-on-prem-release/gkeadm/VERSION/linux/gkeadm ./
    chmod +x gkeadm
    

### Windows
    
    
    gcloud storage cp gs://gke-on-prem-release/gkeadm/VERSION/windows/gkeadm.exe ./
    

**Note:** Support for Windows is deprecated and will be removed in a future release.

### macOS Catalina
    
    
    gcloud storage cp gs://gke-on-prem-release/gkeadm/VERSION/darwin/gkeadm ./
    chmod +x gkeadm
    

**Note:** Support for macOS is deprecated and will be removed in a future release.

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. The latest available patch version is 1.15.10-gke.32. For a list of available versions, see [Version history](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history#supported-versions).

### Verify `gkeadm` using `openssl`

You can use `openssl` to verify the `gkeadm` binary against the public key.
    
    
    gcloud storage cp gs://gke-on-prem-release/gkeadm/VERSION/linux/gkeadm.1.sig /tmp/gkeadm.1.sig
    echo "-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----" > key.pem
    openssl dgst -verify key.pem -signature /tmp/gkeadm.1.sig ./gkeadm
    

The expected output of this command is `Verified OK`.

## Download the Google Distributed Cloud bundle

In certain cases, you might want to download a Google Distributed Cloud bundle to your admin workstation.

On your admin workstation, run this command:
    
    
    gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION.tgz /var/lib/gke/bundles/gke-onprem-vsphere-VERSION.tgz
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. The latest available patch version is 1.15.10-gke.32. For a list of available versions, see [Version history](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history#supported-versions).

### Verify the bundle
    
    
    gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION.tgz.1.sig /tmp/gke-onprem-vsphere-VERSION.tgz.1.sig
    echo "-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----" > key.pem
    openssl dgst -verify key.pem -signature /tmp/gke-onprem-vsphere-VERSION.tgz.1.sig /var/lib/gke/bundles/gke-onprem-vsphere-VERSION.tgz
    

## Download `gkectl`

Normally there is no reason for your to download the `gkectl` command-line tool. In the rare case that you want to download `gkectl`, you can find it here:
    
    
    gcloud storage cp gs://gke-on-prem-release/gkectl/VERSION/gkectl ./
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. The latest available patch version is 1.15.10-gke.32. For a list of available versions, see [Version history](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history#supported-versions).

### Verify `gkectl` using `openssl`

You can use `openssl` to verify the `gkectl` binary against the public key.
    
    
    gcloud storage cp gs://gke-on-prem-release/gkectl/VERSION/gkectl.1.sig /tmp/gkectl.1.sig
    echo "-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----" > key.pem
    openssl dgst -verify key.pem -signature /tmp/gkectl.1.sig ./gkectl
    

The expected output of this command is `Verified OK`.

## Download the OVA

In certain cases, you might want to download the admin workstation Open Virtual Appliance (OVA).

To download the admin workstation OVA:
    
    
    gcloud storage cp gs://gke-on-prem-release/admin-appliance/VERSION/gke-on-prem-admin-appliance-vsphere-VERSION.ova ./
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. The latest available patch version is 1.15.10-gke.32. For a list of available versions, see [Version history](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history#supported-versions).

### Verify the OVA using `openssl`

You can use `openssl` to verify the OVA file you downloaded against a signature file (SIG).
    
    
    gcloud storage cp gs://gke-on-prem-release/admin-appliance/VERSION/gke-on-prem-admin-appliance-vsphere-VERSION.ova.1.sig /tmp/gke-on-prem-admin-appliance-vsphere-VERSION.ova.1.sig
    echo "-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----" > key.pem
    openssl dgst -verify key.pem -signature /tmp/gke-on-prem-admin-appliance-vsphere-VERSION.ova.1.sig ./gke-on-prem-admin-appliance-vsphere-VERSION.ova
    

The expected output of this command is `Verified OK`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
