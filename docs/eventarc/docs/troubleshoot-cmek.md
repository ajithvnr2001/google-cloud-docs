---
url: https://docs.cloud.google.com/eventarc/docs/troubleshoot-cmek/
title: Troubleshoot CMEK issues \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:58.110781+00:00
---

# Troubleshoot CMEK issues  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/troubleshoot-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Troubleshoot CMEK issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

You can [use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek) to protect Eventarc. The keys are created and managed through Cloud Key Management Service (Cloud KMS). The following table describes different CMEK issues and how to resolve them when using Cloud KMS with Eventarc. 

### Issues that occur when creating or updating Eventarc resources

CMEK issue | Error message | Description  
---|---|---  
Disabled key | `$KEY is not enabled, current state is: DISABLED` | The provided Cloud KMS key has been disabled for an Eventarc resource. Events or messages associated with the resource are no longer protected. **Solution:**

  1. [Display the key used for a channel](https://docs.cloud.google.com/eventarc/docs/use-cmek#display-key).
  2. [Re-enable the Cloud KMS key](https://docs.cloud.google.com/eventarc/docs/use-cmek#re-enable-kms).

  
Exceeded quota | `Quota exceeded for limit` | Your quota limit for Cloud KMS requests has been reached. **Solution:**

  * Limit the number of Cloud KMS calls.
  * Increase the quota.

For more information, see [Monitor and adjust Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas).   
Mismatched region | `Key region $REGION must match the resource to be protected` |  The provided KMS key region is different from the region of the channel. **Solution:** Use a Cloud KMS key from the same region. Note that for channels in multi-region `eu`, you should protect it using a Cloud KMS key in multi-region `europe`. For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations#multi_regional) and [Eventarc multi-region](https://docs.cloud.google.com/eventarc/docs/locations#gcs-triggers) locations.   
Organization policy constraint | `project/PROJECT_ID violated org policy constraint` | Eventarc is integrated with the following two organization policy constraints to help ensure CMEK usage across an organization. Any existing Eventarc resource isn't subject to a policy that is set after the resource is created; however, updating the resource might fail.

  * `constraints/gcp.restrictNonCmekServices` causes all resource creation requests without a specified Cloud KMS key to fail. **Solution:** Specify a Cloud KMS key for the Eventarc resource. For more information, see [Require CMEKs for new Eventarc resources](https://docs.cloud.google.com/eventarc/docs/use-cmek#resources-constraint).
  * `constraints/gcp.restrictCmekCryptoKeyProjects` restricts the Cloud KMS keys that you can use to protect an Eventarc resource. **Solution:** Use a supported Cloud KMS key for the Eventarc project. For more information, see [Restrict Cloud KMS keys for an Eventarc project](https://docs.cloud.google.com/eventarc/docs/use-cmek#projects-constraint).

  
  
### Issues that occur during event delivery

CMEK issue | Error message | Description  
---|---|---  
Disabled key | `$KEY is not enabled, current state is: DISABLED` | The provided Cloud KMS key has been disabled for an Eventarc resource. Events or messages associated with the resource are no longer protected. **Solution:**

  1. [Display the key used for a channel](https://docs.cloud.google.com/eventarc/docs/use-cmek#display-key).
  2. [Re-enable the Cloud KMS key](https://docs.cloud.google.com/eventarc/docs/use-cmek#re-enable-kms).

  
Exceeded quota | `Quota exceeded for limit` | Your quota limit for Cloud KMS requests has been reached. **Solution:**

  * Limit the number of Cloud KMS calls.
  * Increase the quota.

For more information, see [Monitor and adjust Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas).   
Permission error | `Permission 'cloudkms.cryptoKeyVersions.useToEncrypt' denied on resource $KEY (or it may not exist)` | Either the provided Cloud KMS key doesn't exist or the Identity and Access Management (IAM) permission is not properly configured. **Solution:**

  * Verify Cloud KMS usage: 
    * [Google event types](https://docs.cloud.google.com/eventarc/docs/use-cmek#verify-kms)
    * [Third-party channel](https://docs.cloud.google.com/eventarc/docs/use-cmek#verify-kms-thirdparty-channel)
  * Ensure that the Eventarc service agent has been granted the `cloudkms.cryptoKeyEncrypterDecrypter` role and has been added as a principal to the Cloud KMS key. For more information, see [Grant the Eventarc service account access to a key](https://docs.cloud.google.com/eventarc/docs/use-cmek#key-access).

  
  
To resolve issues that you might encounter when using externally managed keys through Cloud External Key Manager (Cloud EKM), see [Cloud EKM error reference](https://docs.cloud.google.com/kms/docs/reference/ekm_errors).

## What's next

  * [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events)
  * [View audit logs](https://docs.cloud.google.com/eventarc/docs/reference/audit-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
