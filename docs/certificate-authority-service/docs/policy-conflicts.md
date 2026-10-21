---
url: https://docs.cloud.google.com/certificate-authority-service/docs/policy-conflicts/
title: Avoid and resolve policy conflicts \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:36.142264+00:00
---

# Avoid and resolve policy conflicts  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/policy-conflicts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Avoid and resolve policy conflicts

A _policy_ in Certificate Authority Service can either be a CA pool's issuance policy or a certificate template. Certificate issuance policies set the broad rules for a CA pool, whereas certificate templates provide more specific instructions for different certificate types. To learn about policy controls, see [About policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls). A policy has two main parts:

  * **Baseline values** : Baseline values (also known as _predefined values_) are mandatory settings for all certificates issued by a specific policy. For example, you might have a policy that says, "Every certificate issued under this policy must have the `digitalSignature` flag enabled in the `keyUsage` extension." This ensures that all certificates issued by this policy can be used for digital signatures.

  * **Extension constraints** : Extension constraints restrict which extensions can be added to certificates outside of the policy itself. For example, a policy might state, "Only the AIA-OCSP extension is allowed to be added to certificates outside of this policy." This means that if someone tries to add other extensions (like Subject Alternative Name) through a different policy or directly in the certificate request, those extension are ignored.




When you request a certificate, the CA pool uses the specified template to create the certificate. However, the issuance policy attached to the CA pool also evaluates the request against its own rules. Conflicts occur when the settings in a certificate template contradict the settings in the certificate issuance policy added to the CA pool because they are both trying to enforce rules on the same certificate. Here are some possible scenarios:

### Overlapping extension definitions

Conflicts occur when the same extension is defined in the baseline values of both policies. For example, if you define the same extension `keyUsage` in the CA pool's issuance policy and your certificate template, Certificate Authority Service detects this as a conflict even if you specify different parts of the extension in each place.

Example:

  * Issuance policy: Requires `digitalSignature: true` in the `keyUsage` extension.
  * Certificate template: Requires `keyEncipherment: true` in the `keyUsage` extension.



This is still considered a conflict because Certificate Authority Service considers the entire extension as a single unit and checks if the extension is defined in both places, not the specific values within the extension.

To avoid conflicts, make sure you define each extension only once, either in your CA pool's issuance policy or in your certificate template, but not both. This ensures clarity and prevents unexpected certificate issuance failures.

### Conflicting extension constraints and baseline values

A policy conflict occurs when one policy's extension constraints clash with another policy's baseline values. This happens in the following cases:

  * One policy restricts or forbids an extension: This may be through a general exclusion of all extensions or a specific list of allowed extensions that doesn't include the extension in question.
  * Another policy requires that same extension: This means that the second policy has a baseline value defined for that specific extension.



Example:

  * Issuance policy: Has extension constraints that allow only the `keyUsage` extension.
  * Certificate template: Requires the `certificatePolicies` extension in its baseline values.



This creates a conflict because the issuance policy effectively prohibits the `certificatePolicies` extension, while the certificate template requires it.

When defining your policies, carefully consider both baseline values and extension constraints to ensure they work together. Avoid situations where one policy restricts an extension that another policy requires. This prevents conflicts and ensures smooth certificate issuance.

### Common Expression Language (CEL) expression conflicts

If you're using Common Expression Language (CEL) for fine-grained control, conflicting expressions in the certificate template and the issuance policy can cause conflicts. These conflicts disallow certificates to be issued from the CA pool. For example, you might have one expression requiring a domain name to end in `.example.com` and another requiring it to end in `.example.net`. Since these two CEL expressions place different restrictions on the same field, all certificate issuance requests fail.

If you are using both certificate issuance policies and certificate templates, we recommend that you ensure that their CEL expressions don't conflict.

In all of these scenarios, the CA Service API returns an invalid argument error.

### Resolve policy conflicts

When the CA Service API detects a policy conflict, the API returns an invalid argument error and the certificate request fails. To view and resolve the policy conflicts, follow these steps:

  1. Click the **Issuance policy troubleshooter** link that is displayed with the error message. A troubleshooter page appears where you can compare the baseline values and extension constraints in the CA pool's issuance policy with the baseline values and extension constraints in the certificate template. Notice that the policy conflicts are highlighted.
  2. Access either the CA pool or the certificate template to update the conflicting values and resolve the conflict.



After the conflict is resolved, submit the certificate request again.

## What's next

  * [Create a certificate request](https://docs.cloud.google.com/certificate-authority-service//docs/requesting-certificates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
