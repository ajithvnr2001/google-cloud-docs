---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads/
title: Distributed Cloud downloads \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:01.711588+00:00
---

# Distributed Cloud downloads  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Distributed Cloud downloads Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page provides commands to download and verify the following Google Distributed Cloud artifacts:

  * `bmctl` command-line tool.
  * Distributed Cloud offline container images package.



## Log in

Log in with any Google Account:
    
    
    gcloud auth login

## Download `bmctl`

`bmctl` is the command-line tool for Google Distributed Cloud that simplifies cluster creation and management. For more information about what you can do with `bmctl`, see [`bmctl` tool](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/bmctl).

From your Linux admin workstation, use the following commands to download `bmctl` and make it executable:
    
    
    gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmctl .
    chmod +x ./bmctl

Replace `VERSION` with the version of Google Distributed Cloud you want to install or upgrade your clusters to. The latest available patch version is 1.16.8.

## Verify `bmctl` using `openssl`

Verify the `bmctl` binary against the public key using `openssl`, where `VERSION` is the file's version:
    
    
    gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmctl.1.sig .
    openssl dgst -verify - -signature ./bmctl.1.sig ./bmctl <<'EOF'
    -----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----
    EOF

Expected output of this command is `Verified OK`.

## Download the images package

You only need the images package if you plan on setting up a [registry mirror](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/registry-mirror). The package provides all of the container images used by Google Distributed Cloud for the specified version. Make sure the package you download is the same version as the `bmctl` download.

From your Linux admin workstation, run the following command to download the package:
    
    
    gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmpackages_VERSION.tar.xz .

## Verify the images package using `openssl`

Verify the images package binary against the public key using `openssl`, where `VERSION` is the file's version:
    
    
    gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmpackages_VERSION.tar.xz.1.sig .
    openssl dgst -verify - -signature ./bmpackages_VERSION.tar.xz.1.sig ./bmpackages_VERSION.tar.xz <<'EOF'
    -----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
    wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
    -----END PUBLIC KEY-----
    EOF

Expected output of this command is `Verified OK`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
