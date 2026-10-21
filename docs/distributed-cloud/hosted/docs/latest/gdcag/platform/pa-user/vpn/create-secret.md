---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/create-secret/
title: Create the secret with a PSK \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:54.410047+00:00
---

# Create the secret with a PSK  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/create-secret/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create the secret with a PSK Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate a pre-shared key (PSK) and use that PSK to create an authentication secret.

A PSK is a shared secret password that is used to authenticate and encrypt communication between two devices. It is a form of symmetric encryption.

## Before you begin

To create a secret, you must have the necessary identity and access roles:

  * VPN Admin: Has read and write permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Admin (`vpn-admin`) role.
  * VPN Viewer: Has read permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Viewer (`vpn-viewer`) role.
  * For more information, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions).



## Generate a PSK

Use the following methods to generate a strong 32-character pre-shared key.

### OpenSSL

For more information about OpenSSL, see <https://www.openssl.org/>. On a Linux or macOS system, run the following OpenSSL command:
    
    
    openssl rand -base64 24
    

### /dev/urandom

On a Linux or macOS system, you can also use `/dev/urandom` as a pseudorandom source to generate a pre-shared key:

  * On Linux or macOS, send the random input to `base64`:
        
        head -c 24 /dev/urandom | base64
        

  * Pass the random input through a hashing function, such as `sha256`:

    * On Linux:
          
          head -c 4096 /dev/urandom | sha256sum | cut -b1-32
          

    * On macOS:
          
          head -c 4096 /dev/urandom | openssl sha256 | cut -b1-32
          




### JavaScript

Generate the pre-shared key directly in a document by using JavaScript with the W3C Web Cryptography API. For more information, see <https://www.w3.org/TR/WebCryptoAPI/#Crypto-method-getRandomValues>

This API uses the `Crypto.getRandomValues()` method detailed here: <https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues> which provides a cryptographically sound way of generating a pre-shared key.

The following code creates an array of 24 random bytes, and then base64 encodes those bytes to produce a random 32-character string:
    
    
      var a = new Uint8Array(24);
      window.crypto.getRandomValues(a);
    
      console.log(btoa(String.fromCharCode.apply(null, a)));
    

## Create the secret

Create a secret with a PSK key in the platform namespace:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER create secret -n platform generic PSK_NAME --from-literal=psk=PSK
    

Replace the following:

  * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PSK_NAME`: The name of the PSK key.
  * `PSK`: The value of the PSK key.



## What's next

  * [Create a VPN tunnel](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
