---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/automating-cert-updates/
title: Best practices for automating certificate renewal \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:36.863388+00:00
---

# Best practices for automating certificate renewal  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/automating-cert-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Best practices for automating certificate renewal Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes the best practices for automating certificate renewal for LDAPS.

## Overview

If you are issuing shorter-lived certificates, we recommend that you automate the renewal of these certificates.

## Dealing with API errors

Automation should check for errors both on the initial blocking API call as well as when polling the returned long-running operation. The update can only be considered as successful if the long-running operation is marked as done without error.

If `UpdateLdapsSettings` returns an error with code `INVALID_ARGUMENT`, the error message can explain what is wrong with the uploaded certificate. This error is typically returned during the initial blocking call to the API. In such cases, retries are ineffective and the automation should send an alert.

If the API returns any other error code which is retriable (such as `UNAVAILABLE`), the automation should retry the call with the appropriate backoff. These errors are typically returned when polling the long-running operation that is returned by the initial blocking call to `UpdateLdapsSettings`.

Learn more about [`UpdateLdapsSettings`](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/updateLdapssettings).

## Checking the `LDAPSSettings` state

After calling `UpdateLdapsSettings`, it is good practice to check that `LDAPSSettings` meets expectations and is in a good state (`ACTIVE`). You can call `GetLdapsSettings` to compare the fingerprints of certificates in the intended state against the deployed certificate fingerprints. You can use tools like OpenSSL to calculate the fingerprints of your new certificates.

Do take note of any display differences between the method the automation uses to compute fingerprints versus how Managed Microsoft AD stores them. For example, Managed Microsoft AD stores a thumbprint as a single undelimited hexadecimal string: `771B8FD90806E074A7AD49B1624D2761137557D2`. OpenSSL returns the following for the same certificate: `SHA1 Fingerprint=77:1B:8F:D9:08:06:E0:74:A7:AD:49:B1:62:4D:27:61:13:75:57:D2`.

Learn more about [`LDAPSSettings`](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/LDAPSSettings) and [`GetLdapsSettings`](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/getLdapssettings).

## Building a PFX certificate chain

If your automation procures certificates in the PEM or CRT formats, you must convert them to PFX and include the entire certificate chain.

To convert to PFX and include the entire chain, complete the following steps using shell and OpenSSL.

  1. Create a single PEM file that includes all intermediate certificates as well as the root certificate.
         
         cat root-ca-cert.pem >> temp.pem
         echo -e "\n" >> temp.pem
         cat intermediate-ca-cert.pem >> temp.pem
         

  2. Build the output PFX file. `leaf.key` is the private key.
         
         openssl pkcs12 -export -out out.pfx -inkey leaf.key -in leaf-cert.pem \
             -certfile temp.pem -passout "EXPORT_PASSWORD"
         

  3. Show info of the PFX file. This should show the entire root to leaf chain and the private key.
         
         openssl pkcs12 -in out.pfx -nodes -passin "EXPORT_PASSWORD"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
