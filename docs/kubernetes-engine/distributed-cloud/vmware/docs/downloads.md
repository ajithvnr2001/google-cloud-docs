---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads/
title: Google Distributed Cloud for VMware downloads \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:22.370651+00:00
---

# Google Distributed Cloud for VMware downloads  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Google Distributed Cloud for VMware downloads Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to download the `gkeadm` command-line tool and other components that are part of Google Distributed Cloud (software only) for VMware.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

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
    
    
    gcloud storage cp gs://gke-on-prem-release/gkeadm/VERSION/linux/gkeadm ./
    chmod +x gkeadm

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. Here's the list of the latest patch versions for supported minor versions:

  * 1.36.200-gke.118
  * 1.35.600-gke.141
  * 1.34.900-gke.135



For a list of available versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

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

Google Distributed Cloud offers two types of bundles: a regular bundle (metadata and manifests) and a full bundle (includes OS and container images). For a detailed comparison of each bundle type, see [About Google Distributed Cloud bundles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/bundles).

### Download the regular bundle

If you have high-bandwidth access to Google Cloud, download the regular bundle:
    
    
    gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION.tgz /var/lib/gke/bundles/gke-onprem-vsphere-VERSION.tgz
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to.

### Download the full bundle

If your environment is air-gapped or if your proxy connection is slow, you can download the full bundle to avoid installation timeouts:
    
    
    gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION-full.tgz /var/lib/gke/bundles/gke-onprem-vsphere-VERSION-full.tgz
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. Here's the list of the latest patch versions for supported minor versions:

  * 1.36.200-gke.118
  * 1.35.600-gke.141
  * 1.34.900-gke.135



For a list of all available versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

### Verify the bundle

Verify the signature of the bundle you downloaded against the public key.

Verify the regular bundle:
    
    
    gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION.tgz.1.sig /tmp/gke-onprem-vsphere-VERSION.tgz.1.sig
    echo "-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----" > key.pem
    openssl dgst -verify key.pem -signature /tmp/gke-onprem-vsphere-VERSION.tgz.1.sig /var/lib/gke/bundles/gke-onprem-vsphere-VERSION.tgz
    

Verify the full bundle:
    
    
    gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION-full.tgz.1.sig /tmp/gke-onprem-vsphere-VERSION-full.tgz.1.sig
    echo "-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----" > key.pem
    openssl dgst -verify key.pem -signature /tmp/gke-onprem-vsphere-VERSION-full.tgz.1.sig /var/lib/gke/bundles/gke-onprem-vsphere-VERSION-full.tgz
    

## Download `gkectl`

Normally there is no reason for your to download the `gkectl` command-line tool. In the rare case that you want to download `gkectl`, you can find it here:
    
    
    gcloud storage cp gs://gke-on-prem-release/gkectl/VERSION/gkectl ./
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. Here's the list of the latest patch versions for supported minor versions:

  * 1.36.200-gke.118
  * 1.35.600-gke.141
  * 1.34.900-gke.135



For a list of available versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

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
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. Here's the list of the latest patch versions for supported minor versions:

  * 1.36.200-gke.118
  * 1.35.600-gke.141
  * 1.34.900-gke.135



For a list of available versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

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

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
