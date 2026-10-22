---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads/
title: Google Distributed Cloud for bare metal downloads \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:58.337065+00:00
---

# Google Distributed Cloud for bare metal downloads  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Google Distributed Cloud for bare metal downloads Stay organized with collections  Save and categorize content based on your preferences. 

This page provides commands to download and verify the following artifacts for Distributed Cloud software only for bare metal (formerly known as Google Distributed Cloud Virtual, previously known as Anthos clusters on bare metal):

  * `bmctl` command-line tool.
  * Google Distributed Cloud software offline container images package.



This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Sign in

Sign in with any Google Account:
    
    
    gcloud auth login
    

## Download `bmctl`

`bmctl` is the command-line tool for Google Distributed Cloud that simplifies cluster creation and management. For more information about what you can do with `bmctl`, see [`bmctl` tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl).

From your Linux admin workstation, use the following commands to download `bmctl` and make it executable:
    
    
    gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmctl .
    
    chmod +x ./bmctl
    

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. Here's the list of the latest patch versions for supported minor versions:

  * 1.36.100-gke.144
  * 1.35.600-gke.141
  * 1.34.900-gke.135



For a list of all available versions, see [Version history](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history).

## Verify `bmctl` using `openssl`

Verify the `bmctl` binary against the public key using `openssl`, where `VERSION` is the file's version:

  1. If you haven't already, write the pubic key to a file, `public.key`:
         
         cat << EOF > public.key
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF
         

  2. Download the digital signature file for the specific version of `bmctl` that you downloaded:
         
         gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmctl.1.sig .
         

  3. Use OpenSSL to verify the signature:
         
         openssl dgst -verify public.key -signature ./bmctl.1.sig ./bmctl
         

Expected output of this command is `Verified OK`.




## Download the images package

You only need the images package if you plan on setting up a [registry mirror](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror). The package provides all of the container images used by Google Distributed Cloud for the specified version. Make sure the package you download is the same version as the `bmctl` download.

From your Linux admin workstation, run the following command to download the package:
    
    
    gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmpackages_VERSION.tar.xz .
    

## Verify the images package using `openssl`

Verify the images package binary against the public key using `openssl`, where `VERSION` is the file's version:

  1. If you haven't already, write the pubic key to a file, `public.key`:
         
         cat << EOF > public.key
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF
         

  2. Download the digital signature file for the specific version of `bmctl` that you downloaded:
         
         gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmpackages_VERSION.tar.xz.1.sig .
         

  3. Use OpenSSL to verify the signature:
         
         openssl dgst -verify public.key -signature \
             ./bmpackages_VERSION.tar.xz.1.sig \
             ./bmpackages_VERSION.tar.xz
         

Expected output of this command is `Verified OK`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
