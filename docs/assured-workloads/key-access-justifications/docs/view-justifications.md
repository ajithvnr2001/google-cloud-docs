---
url: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/view-justifications/
title: View and act on justifications \u00a0|\u00a0 Key Access Justifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:40.978107+00:00
---

# View and act on justifications  |  Key Access Justifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/view-justifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management)
  * [ Key Access Justifications ](https://docs.cloud.google.com/assured-workloads/key-access-justifications)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View and act on justifications

This page describes how you can view and act on justifications that Key Access Justifications sends to request access to your encryption keys. Whenever your information is encrypted or decrypted, Key Access Justifications sends you a justification describing the reason for the access. The way you view and act on justifications depends on the type of keys you're using with Key Access Justifications:

  * For externally managed keys, the Cloud EKM partner may provide the ability to set a policy that automatically approves or denies access requests based on the content of the justifications. For more information about setting a policy, see the relevant documentation for your chosen key manager. The following partners support Key Access Justifications: 
    * Fortanix
    * Thales
  * For all keys configured with Key Access Justifications policies—regardless of key type—you can view access requests in the Cloud KMS audit logs.



Denying access can hinder the ability of Google personnel to help you with a contracted service. For example:

  * Denying access for requests with reasons of `CUSTOMER_INITIATED_ACCESS` or `GOOGLE_INITIATED_SYSTEM_OPERATION` results in your service becoming unavailable.
  * Denying access for requests with the reason of `CUSTOMER_INITATED_SUPPORT` limits the ability of Google personnel to respond to support tickets on the rare occasion that your support ticket requires access to sensitive customer information. Support tickets typically don't require this access and our frontline support personnel don't have this access.
  * Denying access for request with the reason of `GOOGLE_INITIATED_SERVICE` reduces service availability and reliability and inhibits Google's ability to recover from outages.

**Important:** Justification codes for Key Access Justifications are similar to [Access Transparency codes](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#justification-reason-codes), but they are not equivalent and shouldn't be directly compared.

## View justifications for EKM keys

You can use the Google Cloud console to view the justification Key Access Justifications sends to your external key manager when your data is accessed. To access the justification, you first need to enable Cloud Audit Logs with Cloud KMS on the project containing the key used for encryption.

After you have completed the setup, the Cloud Audit Logs also includes the justification used in the external request for cryptographic operations. The justification is included in the Data Access logs on the resource key, in the `metadata` entries for `protoPayload`. For more information on these fields, see [Understanding audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs). For more information about using Cloud Audit Logs with Cloud KMS, see [Cloud KMS audit logging information](https://docs.cloud.google.com/kms/docs/audit-logging).

Note that unlike the justification shared with the external key manager, the justification in the Cloud Audit Logs cannot be used for approving or denying the associated cryptographic operation. Google Cloud logs the justification only after the operation is completed. Therefore, the logs in Google Cloud must be used primarily for record keeping.

## View justifications for Cloud HSM and software keys

When Cloud HSM and software keys [configured with Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/configure-kaj) have been used to perform encryption or decryption operations, you can view the [Cloud KMS audit logs](https://docs.cloud.google.com/kms/docs/audit-logging#viewing_logs) to view the following information:

  * `key_access_justification`: The [justification code](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes) associated with the request.
  * `key_access_justification_policy_metadata`: The Key Access Justifications policy metadata for the key containing the following information: 
    * `customer_configured_policy_enforced`: Indicates whether or not the Key Access Justifications policy set on the key was enforced for the operation.
    * `customer_configured_policy`: Indicates the justification codes that allow access to the key.
    * `justification_propagated_to_ekm`: Indicates whether the access request was propagated to the external key manager (if configured).



The following example demonstrates a Cloud KMS audit log entry for an Cloud HSM key configured with Key Access Justifications:
    
    
      {
        @type: "type.googleapis.com/google.cloud.audit.AuditLog"
        (...)
        metadata: {
          entries: {
            key_access_justification: {
              @type: "type.googleapis.com/google.cloud.ekms.v0.AccessReasonContext"
              reason: "CUSTOMER_INITIATED_ACCESS"
            }
            key_access_justification_policy_metadata: {
              customer_configured_policy_enforced: "true"
              customer_configured_policy: {
                allowed_access_reasons: ["CUSTOMER_INITIATED_ACCESS", "GOOGLE_INITIATED_SYSTEM_OPERATION"]
              }
            justification_propagated_to_ekm: "false"
            }
          }
        }
        methodName: "useVersionToDecrypt"
        serviceName: "cloudkms.googleapis.com"
        (...)
      }
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
