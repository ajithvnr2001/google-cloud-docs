---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/downloading-istioctl/
title: Downloading the troubleshooting tool \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:24.721720+00:00
---

# Downloading the troubleshooting tool  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/downloading-istioctl/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Downloading the troubleshooting tool

This page shows you how to download the troubleshooting tool for Cloud Service Mesh. To debug and review your Cloud Service Mesh deployment you need to install the istioctl component for Google Cloud CLI.

## Download istioctl

### Managed control plane

  1. Update Google Cloud CLI:
         
         gcloud components update
         

  2. Download the embedded Cloud Service Mesh troubleshooting tool:
         
         gcloud components install istioctl
         




If you receive error message `You cannot perform this action because the Google Cloud CLI component manager is disabled for this installation`, you have previously installed Google Cloud CLI through [Debian/Ubuntu](https://cloud.google.com/sdk/docs/install#deb). Use the following commands instead: 

  1. Update Google Cloud CLI
         
         sudo apt-get update
         

  2. Download the embedded Cloud Service Mesh troubleshooting tool:
         
         sudo apt-get install google-cloud-sdk-istioctl
         




### In-cluster control plane

### Linux

  1. Download the Cloud Service Mesh installation file to your current working directory:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.29.8-asm.11-linux-amd64.tar.gz

  2. Download the signature file and use `openssl` to verify the signature:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.29.8-asm.11-linux-amd64.tar.gz.1.sig
         openssl dgst -verify /dev/stdin -signature istio-1.29.8-asm.11-linux-amd64.tar.gz.1.sig istio-1.29.8-asm.11-linux-amd64.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

The expected output is: `Verified OK`.

  3. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory:
         
         tar xzf istio-1.29.8-asm.11-linux-amd64.tar.gz

The command creates an installation directory in your current working directory named `istio-1.29.8-asm.11` that contains:
         
         - Sample applications in the `samples` directory.
         - The `istioctl` command-line tool that you use to install Cloud Service Mesh is
         in the <code>bin</code> directory.
         - The Cloud Service Mesh configuration profiles are in the `manifests/profiles`
         directory.
         

  4. Ensure that you're in the Cloud Service Mesh installation's root directory.
         
         cd istio-1.29.8-asm.11




### Mac OS

  1. Download the Cloud Service Mesh installation file to your current working directory:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.29.8-asm.11-osx.tar.gz

  2. Download the signature file and use `openssl` to verify the signature:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.29.8-asm.11-osx.tar.gz.1.sig
         openssl dgst -sha256 -verify /dev/stdin -signature istio-1.29.8-asm.11-osx.tar.gz.1.sig istio-1.29.8-asm.11-osx.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

The expected output is: `Verified OK`.

  3. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory:
         
         tar xzf istio-1.29.8-asm.11-osx.tar.gz

The command creates an installation directory in your current working directory named `istio-1.29.8-asm.11` that contains:
         
         - Sample applications in the `samples` directory.
         - The `istioctl` command-line tool that you use to install Cloud Service Mesh is
         in the <code>bin</code> directory.
         - The Cloud Service Mesh configuration profiles are in the `manifests/profiles`
         directory.
         

  4. Ensure that you're in the Cloud Service Mesh installation's root directory.
         
         cd istio-1.29.8-asm.11




### Windows

  1. Download the Cloud Service Mesh installation file to your current working directory:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.29.8-asm.11-win.zip

  2. Download the signature file and use `openssl` to verify the signature:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.29.8-asm.11-win.zip.1.sig
         openssl dgst -verify - -signature istio-1.29.8-asm.11-win.zip.1.sig istio-1.29.8-asm.11-win.zip <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

The expected output is: `Verified OK`.

  3. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory:
         
         tar xzf istio-1.29.8-asm.11-win.zip

The command creates an installation directory in your current working directory named `istio-1.29.8-asm.11` that contains:
         
         - Sample applications in the `samples` directory.
         - The `istioctl` command-line tool that you use to install Cloud Service Mesh is
         in the <code>bin</code> directory.
         - The Cloud Service Mesh configuration profiles are in the `manifests/profiles`
         directory.
         

  4. Ensure that you're in the Cloud Service Mesh installation's root directory.
         
         cd istio-1.29.8-asm.11




## What's next

  * [Troubleshoot Cloud Service Mesh step-by-step](https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-intro)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
