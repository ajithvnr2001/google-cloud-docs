---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/download-gkeadm/
title: Download gkeadm \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:58.796033+00:00
---

# Download gkeadm  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/download-gkeadm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Download gkeadm Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to download the `gkeadm` command-line tool that you can use to create an admin workstation for Google Distributed Cloud.

Typically, `gkeadm` is the only component that you have to download manually. In some cases, you might want to manually download one or more of these other components:

  * Admin workstation Open Virtual Appliance (OVA)
  * Google Distributed Cloud bundle
  * `gkectl` command-line tool



For more information, see [Downloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads).

You can also set up an admin workstation on any computer of your choice. For more information, see [Choose how to create the admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation#choose_how_to_create_the_admin_workstation).

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

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. The latest available patch version is 1.36.100-gke.144. For a list of available versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

### Verify `gkeadm` using `openssl`

You can use `openssl` to verify the `gkeadm` binary against the public key.
    
    
    gcloud storage cp gs://gke-on-prem-release/gkeadm/VERSION/linux/gkeadm.1.sig /tmp/gkeadm.1.sig
    echo "-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----" > key.pem
    openssl dgst -verify key.pem -signature /tmp/gkeadm.1.sig ./gkeadm
    

The expected output of this command is `Verified OK`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
