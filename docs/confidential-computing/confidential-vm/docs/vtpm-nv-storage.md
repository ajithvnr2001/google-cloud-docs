---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/vtpm-nv-storage/
title: Confidential VM vTPM non-volatile storage contents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:57.802193+00:00
---

# Confidential VM vTPM non-volatile storage contents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/vtpm-nv-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Reference ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents)



Send feedback 

#  Confidential VM vTPM non-volatile storage contents Stay organized with collections  Save and categorize content based on your preferences. 

A Confidential VM instance uses its Shielded VM vTPM's non-volatile storage to store attestation key certificates and templates. The following table details the addresses for where these elements are stored.

Index | Contents  
---|---  
`0x01c10000` | Compute Engine RSA attestation key certificate.  
`0x01c10001` |  Template for the Compute Engine RSA attestation key, in the `TPMT_PUBLIC` structure.  For details on the `TPMT_PUBLIC` structure, see [ Trusted Platform Module Library, Part 2: Structures (PDF)](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TPM2_r1p59_Part2_Structures_pub.pdf).   
`0x01c10002` | Compute Engine ECC attestation key certificate.  
`0x01c10003` |  Template for the Compute Engine ECC attestation key, in the `TPMT_PUBLIC` structure.  For details on the `TPMT_PUBLIC` structure, see [ Trusted Platform Module Library, Part 2: Structures (PDF)](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TPM2_r1p59_Part2_Structures_pub.pdf).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
