---
url: https://docs.cloud.google.com/eventarc/advanced/docs/troubleshoot/
title: Troubleshoot issues \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:27.087499+00:00
---

# Troubleshoot issues  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

This page shows you how to resolve issues that you might encounter when using Eventarc Advanced.

## CMEK issues

You can [use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek) to protect Eventarc. The keys are created and managed through Cloud Key Management Service (Cloud KMS). The following table describes different CMEK issues and how to resolve them when using Cloud KMS with Eventarc. 

### Issues that occur when creating or updating Eventarc resources

CMEK issue | Error message | Description  
---|---|---  
Disabled key | `$KEY is not enabled, current state is: DISABLED` | The provided Cloud KMS key has been disabled for an Eventarc resource. Events or messages associated with the resource are no longer protected. **Solution:**

  1. Display the key used for a resource: 
     * [Bus](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms)
     * [Pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms-pipeline)
     * [Google API sources](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms-api-source)
  2. [Re-enable the Cloud KMS key](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#re-enable-kms).

  
Exceeded quota | `Quota exceeded for limit` | Your quota limit for Cloud KMS requests has been reached. **Solution:**

  * Limit the number of Cloud KMS calls.
  * Increase the quota.

For more information, see [Monitor and adjust Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas).   
Mismatched region | `Key region $REGION must match the resource to be protected` |  The provided KMS key region is different from the region of the resource. **Solution:** Use a Cloud KMS key from the same region.  
Organization policy constraint | `project/PROJECT_ID violated org policy constraint` | Eventarc is integrated with the following two organization policy constraints to help ensure CMEK usage across an organization. Any existing Eventarc resource isn't subject to a policy that is set after the resource is created; however, updating the resource might fail.

  * `constraints/gcp.restrictNonCmekServices` causes all resource creation requests without a specified Cloud KMS key to fail. **Solution:** Specify a Cloud KMS key for the Eventarc resource. For more information, see [Require CMEKs for new Eventarc resources](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#resources-constraint).
  * `constraints/gcp.restrictCmekCryptoKeyProjects` restricts the Cloud KMS keys that you can use to protect an Eventarc resource. **Solution:** Use a supported Cloud KMS key from an allowed Eventarc project, folder, or organization. For more information, see [Restrict Cloud KMS keys for an Eventarc project](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#projects-constraint).

  
  
### Issues that occur during event delivery

CMEK issue | Error message | Description  
---|---|---  
Disabled key | `$KEY is not enabled, current state is: DISABLED` | The provided Cloud KMS key has been disabled for an Eventarc resource. Events or messages associated with the resource are no longer protected. **Solution:**

  1. Display the key used for a resource: 
     * [Bus](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms)
     * [Pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms-pipeline)
     * [Google API sources](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms-api-source)
  2. [Re-enable the Cloud KMS key](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#re-enable-kms).

  
Exceeded quota | `Quota exceeded for limit` | Your quota limit for Cloud KMS requests has been reached. **Solution:**

  * Limit the number of Cloud KMS calls.
  * Increase the quota.

For more information, see [Monitor and adjust Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas).   
Permission error | `Permission 'cloudkms.cryptoKeyVersions.useToEncrypt' denied on resource $KEY (or it may not exist)` | Either the provided Cloud KMS key doesn't exist or the Identity and Access Management (IAM) permission is not properly configured. **Solution:**

  * Verify Cloud KMS usage: 
    * [Bus](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms)
    * [Pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms-pipeline)
    * [Google API sources](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#verify-kms-api-source)
  * Ensure that the Eventarc service agent has been granted the `cloudkms.cryptoKeyEncrypterDecrypter` role and has been added as a principal to the Cloud KMS key. For more information, see [Grant the Eventarc service account access to a key](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#key-access).

  
  
To resolve issues that you might encounter when using externally managed keys through Cloud External Key Manager (Cloud EKM), see [Cloud EKM error reference](https://docs.cloud.google.com/kms/docs/reference/ekm_errors).

## HTTP `400 Bad Request` errors

Encountering a generic HTTP `400 Bad Request` error for a pipeline often signals a transformation or message binding issue, or an issue related to the targeted endpoint. Make sure to do the following:

  * Look for syntax or logic errors in your CEL expressions. For example, in this document, see Transformation issues.
  * Verify that event messages conform to the expected schema. For example, in this document, see Invalid request format.
  * If the event destination itself is returning the error, check your targeted endpoint.



## HTTP `503 Service Unavailable` errors

If you encounter an HTTP `503 Service Unavailable` error for a pipeline that routes messages to a Google destination using a DNS address—for example, Cloud Run—make sure that [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) is enabled on the subnet used in the network attachment; otherwise, the DNS address can't be resolved.

## Permission denied while using Eventarc service agent

If you encounter the following error while trying to create an Eventarc Advanced resource, wait a few minutes ([potentially, seven](https://docs.cloud.google.com/iam/docs/access-change-propagation)), and then try creating the resource again:
    
    
    Permission denied while using the Eventarc Service Agent. If you recently started to use
    Eventarc, it may take a few minutes before all necessary permissions are propagated to the
    Service Agent. Otherwise, verify that it has Eventarc Service Agent role.
    

A service agent acts as the identity of a given Google Cloud service for a particular project. For more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents) and view the Identity and Access Management (IAM) permissions for the [Eventarc Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`).

If you are still running into the previous error after attempting to create your resource again, complete the following steps to verify that the Eventarc service agent exists in your Google Cloud project and has the necessary role:

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. On the **View by principals** tab, select the **Include Google-provided role grants** checkbox.
  3. In the list of principals, locate the Eventarc service agent, which uses the following format:

`service-`PROJECT_NUMBER`@gcp-sa-eventarc.iam.gserviceaccount.com`

  4. Verify that the service agent has the **Eventarc Service Agent** role. If the service agent doesn't have the role, then [grant the role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).
**Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).


## Publishing to Cloud Run job issues

This section describes how to resolve issues that you might encounter when publishing events to a Cloud Run job. For an end-to-end demonstration, see the [quickstart](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-cloud-run-job).

### HTTP `403 Forbidden` errors

If you encounter an HTTP `403 Forbidden` error while trying to execute a Cloud Run job that overrides the job configuration—for example, by defining a message binding—make sure that you have granted the [Cloud Run Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) or [Cloud Run Jobs Executor With Overrides](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.jobsExecutorWithOverrides) (`roles/run.jobsExecutorWithOverrides`) IAM role to the OAuth service account used by the Eventarc pipeline. For more information, see [Override job configuration for a specific execution](https://docs.cloud.google.com/run/docs/execute/jobs#override-job-configuration).

### Invalid request format

When defining a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding), you must use the `http_endpoint_message_binding_template` key to transform the event into the format expected by the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/run)—for example: `{"body": ""}`.

If the key is missing or empty, the event message routed to the job won't conform to the expected schema for the Cloud Run job endpoint, and this prevents the event message from successfully triggering the job execution.

## Transformation issues

If your event data can't be or isn't transformed as expected when specifying a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding), make sure that the syntax of your CEL expression is correct.

#### Incorrect CEL expression

For example, in the following expression, quoted string substitutions—such as `\"${message.data}\"`—are used to evaluate and insert variable values when CEL extension functions should be used instead:
    
    
    cel_expression: "{\"body\":{\"overrides\":{\"containerOverrides\":[{\"env\":[{\"name\":\"CLOUD_EVENT_PAYLOAD\",\"value\":\"${message.data}\"},{\"name\":\"CLOUD_EVENT_ATTRIBUTES\",\"value\":\"${message.attributes}\"}]}]}}}"

Additionally, event attributes are top-level fields on the message object and aren't contained within a separate attributes field—such as `message.attributes`. Each attribute of an incoming CloudEvents message should be accessed using the `message.key` value, where `key` is the name of the attribute.

#### Correct CEL expression

To resolve these issues, append the `toJsonString()` function directly to the object to pass the message data as a JSON string. To capture the event attributes as a JSON string while excluding the payload, use `message.removeFields(["data"]).toJsonString()`. For example:
    
    
    cel_expression: "{\"body\":{\"overrides\":{\"containerOverrides\":[{\"env\":[{\"name\":\"CLOUD_EVENT_PAYLOAD\",\"value\":\"message.data.toJsonString()\"},{\"name\":\"CLOUD_EVENT_ATTRIBUTES\",\"value\":\"message.removeFields(['data']).toJsonString()\"}]}]}}}"

For more information, see [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events).

## What's next

  * [Retry events](https://docs.cloud.google.com/eventarc/advanced/docs/retry-events)
  * [View audit logs](https://docs.cloud.google.com/eventarc/advanced/docs/audit-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
