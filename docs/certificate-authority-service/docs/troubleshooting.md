---
url: https://docs.cloud.google.com/certificate-authority-service/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:04.921927+00:00
---

# Troubleshooting  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshooting

This page shows you how to resolve common issues with Certificate Authority Service.

## API request returns HTTP 403 Forbidden

If an API request returns HTTP 403 Forbidden with the message `Read access to project PROJECT_NAME was denied`, then use the following resolution.

**Resolution**

  1. Check the IAM permissions of the requester.
  2. Check the location for the request. Unsupported regions can return a permission denied error. For more information about supported locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).



## Deleting a CA returns HTTP 412 Failed Precondition

If you see the following failed precondition errors when deleting a CA, use the resolution in this section.

  * `Cannot perform Certificate Authority deletion, Certificate Authority is in state ENABLED.`



**Resolution**

A CA needs to be in `DISABLED` or `STAGED` state for it to be deleted. Ensure the state of your CA before scheduling it for deletion. For more information about CA states, see [CA states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).

## Certificate issuance failure

CA Service provides several policy controls that you can use to manage certificate issuance. For more information about the policy controls, see [Overview of certificate templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).

Certificate issuance can fail because of several reasons. Some of these reasons are as follows.

  * Conflict between CA pool's certificate issuance policy and certificate template.

For example, consider that the issuance policy defines an extension `foo` and assigns it the value `bar` and the certificate template defines extension `foo` and assigns it the value `bat`. Assigning two different values to the same extension creates a conflict.

**Resolution**

Review the CA pool's certificate issuance policy against the certificate template, and identify and resolve the conflicts.

For more information about issuance policies, see [Add a certificate issuance policy to a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).

  * Subject or Subject Alternate Names (SANs) fail the CEL expression evaluation in either the certificate template or the CA pool's certificate issuance policy.

**Resolution**

Review the CA pool's certificate issuance policy and certificate template, and ensure that the subject and SAN satisfy the conditions set by Common Expression Language (CEL) expressions. For more information about CEL expressions, see [Using Common Expression Language](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).

  * Incorrect IAM role being granted for a use case. For example, assigning the `roles/privateca.certificateRequester` role for reflected identity or assigning the `roles/privateca.workloadCertificateRequester` role for default identity mode.

**Resolution**

Confirm that you have assigned the `roles/privateca.certificateRequester` role for default identity mode and the `roles/privateca.workloadCertificateRequester` role for reflected identity. For more information about using identity reflection, see [Identity reflection for federated workloads](https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection).

  * Attempting to use the reflected identity mode in an unsupported scenario, such as without Hub workload identity. An unsupported scenario for identity reflection returns the following error message:
        
        Could not use the REFLECTED_SPIFFE subject mode because the caller does not have a SPIFFE identity. Please visit the CA Service documentation to ensure that this is a supported use-case.
        

**Resolution**

Determine which type of identity you need to use: default identity or reflected identity. If you need to use reflected identity, make sure that you are using it in one of the supported scenarios. For more information about identity reflection, see [Identity reflection for federated workloads](https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection).

  * The default key size restriction rejects RSA keys with modulus size less than 2048 bits.

Industry best practices recommend using an RSA key of at least 2048 bits. By default, CA Service prevents issuing certificates using an RSA key whose modulus size is less than 2048 bits.

**Resolution**

If you want to use a RSA key with modulus size less than 2048 bits, you must explicitly allow it [using the certificate issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy#gcloud). Use the following YAML example to allow such RSA keys:
        
        allowedKeyTypes:
        - rsa:
            minModulusSize: 1024
        




## What's next

  * Learn about the [best practices for using Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/best-practices).
  * [Frequently asked questions](https://docs.cloud.google.com/certificate-authority-service/docs/faqs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
