---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/downloading-istioctl/
title: Downloading the correct istioctl version \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:18.620268+00:00
---

# Downloading the correct istioctl version  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/downloading-istioctl/

You are viewing archived v1.20 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.20 ](https://docs.cloud.google.com/service-mesh/v1.20/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.20/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Downloading the correct istioctl version

## Cloud Service Mesh and istioctl versions

Your Cloud Service Mesh version must match the `istioctl` client version. Download the installation file to ensure that these versions match.

### Downloading the installation file

The following commands download the installation file for the most recent version of Cloud Service Mesh 1.31.1. You can update the following commands with any supported version listed on the [Versions page](https://docs.cloud.google.com/service-mesh/versions) to download the installation file for a different version.

**Note:** If you are using [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh), then download the version currently on the [Rapid channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) (currently version 1.21).

### Linux

  1. Download the Cloud Service Mesh installation file to your current working directory:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.19-linux-amd64.tar.gz

  2. Download the signature file and use `openssl` to verify the signature:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.19-linux-amd64.tar.gz.1.sig
         openssl dgst -verify /dev/stdin -signature istio-1.31.1-asm.19-linux-amd64.tar.gz.1.sig istio-1.31.1-asm.19-linux-amd64.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

The expected output is: `Verified OK`.

  3. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory:
         
         tar xzf istio-1.31.1-asm.19-linux-amd64.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.19` that contains:

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Cloud Service Mesh is in the `bin` directory.
     * The Cloud Service Mesh configuration profiles are in the `manifests/profiles` directory.
  4. Ensure that you're in the Cloud Service Mesh installation's root directory.
         
         cd istio-1.31.1-asm.19




### Mac OS

  1. Download the Cloud Service Mesh installation file to your current working directory:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.19-osx.tar.gz

  2. Download the signature file and use `openssl` to verify the signature:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.19-osx.tar.gz.1.sig
         openssl dgst -sha256 -verify /dev/stdin -signature istio-1.31.1-asm.19-osx.tar.gz.1.sig istio-1.31.1-asm.19-osx.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

The expected output is: `Verified OK`.

  3. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory:
         
         tar xzf istio-1.31.1-asm.19-osx.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.19` that contains:

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Cloud Service Mesh is in the `bin` directory.
     * The Cloud Service Mesh configuration profiles are in the `manifests/profiles` directory.
  4. Ensure that you're in the Cloud Service Mesh installation's root directory.
         
         cd istio-1.31.1-asm.19




### Windows

  1. Download the Cloud Service Mesh installation file to your current working directory:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.19-win.zip

  2. Download the signature file and use `openssl` to verify the signature:
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.19-win.zip.1.sig
         openssl dgst -verify - -signature istio-1.31.1-asm.19-win.zip.1.sig istio-1.31.1-asm.19-win.zip <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

The expected output is: `Verified OK`.

  3. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory:
         
         tar xzf istio-1.31.1-asm.19-win.zip

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.19` that contains:

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Cloud Service Mesh is in the `bin` directory.
     * The Cloud Service Mesh configuration profiles are in the `manifests/profiles` directory.
  4. Ensure that you're in the Cloud Service Mesh installation's root directory.
         
         cd istio-1.31.1-asm.19




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
