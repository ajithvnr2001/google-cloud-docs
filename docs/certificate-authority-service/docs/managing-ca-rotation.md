---
url: https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-rotation/
title: Managing CA rotation \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:27.758202+00:00
---

# Managing CA rotation  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing CA rotation

This page explains how you can manage the rotation of a CA in a CA pool. For more information about CA pools, see [Overview of CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool).

**Note:** This document provides general guidance on managing CA rotation. We recommend that organizations carefully construct their processes in consultation with security experts.

## Ensure seamless CA rotation

Ensuring seamless CA rotation is essential to avoid service downtime, or to deal with an emergency. The following procedure explains how you can seamlessly rotate a CA.

  1. Find the CA pool for the existing CA that is due to expire.
  2. Create a CA in the same CA pool. The CA is created in the `STAGED` state and cannot issue certificates through CA pool load-balancing. CAs in the `STAGED` state can only issue certificates when requested directly by the clients. For more information about CA states, see [CA states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).

  3. Ensure that all clients have downloaded the latest set of CA certificates from the CA pool.

**Note:** Verify that all your clients have received the new certificates. The clients must use the [fetchCaCerts](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools/fetchCaCerts) API to retrieve the CA certificates. If you have configured your clients to automatically download the latest set of certificates from the CA pool, then you have to wait until all your clients get the new certificates. Otherwise, you can explicitly publish the new set of certificates to your clients.
  4. Change the state of the new CA to `ENABLED`. This ensures that certificates can be issued from both the old and the new CA. For information about enabling certificate authorities, see [Enable a CA](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state#enable).

**Note:** To ensure that the new certificates aren't causing outages, you can now choose to wait and monitor your environment.
  5. Change the state of the old CA to `DISABLED`. This ensures that certificates won't be issued by the old CA. For information about disabling certificate authorities, see [Disable a CA](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state#disable).

**Note:** CAs in the `DISABLED` state are still trusted by the clients and provided in the trust anchor for the CA pool.
  6. Wait until all clients have stopped using the certificates issued from the old CA. You can ensure that in two ways:

     * You can wait for the maximum certificate lifetime.
     * You can monitor the certificates being used by your clients.
  7. Delete the old CA. For more information about deleting a CA, see [Delete certificate authorities](https://docs.cloud.google.com/certificate-authority-service/docs/deleting-certificate-authorities).




## What's next

  * Learn more about [CA states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).
  * Learn how to [manage CA states](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state).
  * Learn how to [update CAs](https://docs.cloud.google.com/certificate-authority-service/docs/updating-certificate-authorities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
