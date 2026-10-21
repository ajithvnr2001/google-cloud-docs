---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key/
title: Generate a strong pre-shared key \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:50.749322+00:00
---

# Generate a strong pre-shared key  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Generate a strong pre-shared key Stay organized with collections  Save and categorize content based on your preferences. 

You can use a _pre-shared key (PSK)_ (also called a _shared secret_) to authenticate the Cloud VPN tunnel to your peer VPN gateway. As a security best practice, we recommend that you generate a strong 32-character pre-shared key.

Use the following methods to generate a strong 32-character pre-shared key.

For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).

## Generate a PSK by using JavaScript

You can generate the pre-shared key directly in a document by using JavaScript with the [W3C Web Cryptography API](https://www.w3.org/TR/WebCryptoAPI/#Crypto-method-getRandomValues). This API uses the [Crypto.getRandomValues() method](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues), which provides a cryptographic way of generating a pre-shared key.

The following code generates a random 32-character string by creating an array of 24 random bytes and then base64 encoding those bytes:
    
    
      var a = new Uint8Array(24);
      window.crypto.getRandomValues(a);
    
      console.log(btoa(String.fromCharCode.apply(null, a)));
    

To generate a PSK now, click **Regenerate** :

## Generate a PSK by using OpenSSL

In the Linux or macOS command-line interface, run the following [OpenSSL](https://www.openssl.org/) command:
    
    
    openssl rand -base64 32
    

## Generate a PSK by using `/dev/urandom`

On a Linux or macOS operating system, use `/dev/urandom` as a pseudorandom source to generate a pre-shared key.

  1. In the Linux or macOS command-line interface, run the following command to send the random input to `base64`:
         
         head -c 32 /dev/urandom | base64
         

  2. Pass the random input through a hashing function, such as `sha256`:

     * On Linux:
           
           head -c 4096 /dev/urandom | sha256sum | cut -b1-32
           

     * On macOS:
           
           head -c 4096 /dev/urandom | openssl sha256 | cut -b1-32
           




## What's next

  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
