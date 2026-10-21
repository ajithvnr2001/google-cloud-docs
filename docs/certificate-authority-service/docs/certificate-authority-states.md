---
url: https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states/
title: Certificate authority states \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:30:14.796674+00:00
---

# Certificate authority states  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Certificate authority states

This page describes the operational states that apply to certificate authorities (CAs).

Once created, a CA is in one of the following states throughout its lifecycle.

  * Enabled
  * Disabled
  * Staged
  * Awaiting user activation
  * Deleted



Subordinate CAs are created in the `AWAITING_USER_ACTIVATION` state, and they are set to the `STAGED` state after activation.

**Note:** If you don't activate subordinate CAs within 30 days of creation, the subordinate CAs are deleted.

Root CAs are created in the `STAGED` state. A root CA can never be in the `AWAITING_USER_ACTIVATION` state.

We recommend that you create and test certificates while the CA is still in the `STAGED` state. Once you have verified that the CA certificate has been published to all clients and tested certificate issuance from the CA, you can enable the CA to start issuing load-balanced certificates for the CA pool. For information on enabling a CA, see [Enable a CA](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state#enable).

A CA pool cannot issue certificates until it has at least one CA in the `ENABLED` state.

**Note:** Once you enable a CA, it cannot be transitioned back to the `STAGED` state.

The following table illustrates the properties of a CA in each of the states.

CA state | Can issue certificates? | Included in CA pool certificate issuance rotation? | Included in CA pool Trust Anchor? | Can revoke certificates and publish CRLs? | Is billed? | Are resources accessible? | Can accept update requests?  
---|---|---|---|---|---|---|---  
Enabled | Yes | Yes | Yes | Yes | Yes | Yes | Yes  
Disabled | No | No | Yes | Yes | Yes | Yes | No  
Staged | Yes1 | No | Yes | Yes | Yes | Yes | Yes  
Awaiting user activation | No | No | No | No | No | Yes | No  
Deleted | No | No | No | No | No | No | No  
  
1CAs in the `STAGED` state cannot issue certificates through CA pool load-balancing. They can only issue certificates when requested directly by the clients.

## What's next

  * Learn how to [enable, disable, and restore CAs](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state).
  * Learn how to [request certificates](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
