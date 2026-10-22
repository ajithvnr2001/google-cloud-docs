---
url: https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions/
title: Restrict TLS versions \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:42.000743+00:00
---

# Restrict TLS versions  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Restrict TLS versions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can prevent access to Google Cloud resources by denying requests made using Transport Layer Security (TLS) 1.0 or 1.1. If you also want to prevent the use of TLS 1.2, use a TLS cipher restriction policy to allow only TLS 1.3 ciphers. For more information, see [Restrict TLS cipher suites](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-cipher-suites).

**Note:** You can only restrict TLS versions for Google Cloud fully qualified domain names. If you want to restrict TLS versions for other fully qualified domain names —such as a load balancer— refer to that specific product's guidance.

## Overview

Google Cloud supports multiple [TLS protocol versions](https://docs.cloud.google.com/docs/security/encryption-in-transit#transport_layer_security). To meet compliance requirements, you might want to deny handshake requests from clients that use earlier TLS versions. To do this, you can use the `gcp.restrictTLSVersion` [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints).

The `gcp.restrictTLSVersion` constraint can be applied to organizations, folders, or projects in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). The constraint uses a [deny list](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#list_constraint), which denies explicit values and allows all others. An error will occur if you try to use an allow list.

Due to the behavior of [organization policy hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy), the TLS version restriction applies to the specified resource node and all of its children. For example, if you deny TLS version 1.0 for an organization, it is also denied for all folders and projects (children) that descend from that organization.

You can override the inherited TLS version restriction by updating the organization policy on a child resource. For example, if your organization policy denies TLS 1.0 at the organization level, you can remove the restriction for a child folder by setting a separate organization policy on that folder. If the folder has any children, the folder's policy will also be applied on each child resource due to policy inheritance.

**Note:** The TLS version restriction policy provides additional security against using less secure 3DES encryption-based cipher suites. Specifically, if the policy disallows either TLS 1.0 or TLS 1.1 versions, access to Google Cloud resources is denied for requests using a 3DES encryption-based cipher suite such as `TLS_RSA_WITH_3DES_EDE_CBC_SHA`, regardless of the request's TLS version.**Note:** TLS version restrictions are enforced using eventual consistency, as they control runtime access to in-scope services resources. As a result, it may take up to tens of minutes for consistency to be fully applied when the organization policy is modified.

## Before you begin

  * To set, change, or delete an organization policy, you must first be granted the **Organization Policy Administrator** (`roles/orgpolicy.policyAdmin`) Identity and Access Management (IAM) role.



## Restrict a TLS version

To restrict one or more TLS versions, complete the following steps:

###  Console 

  1. Open the **Organization policies** page in the Google Cloud console.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Select the project picker at the top of the page.

  3. From the project picker, select the resource for which you want to set the organization policy.

  4. Select the **Restrict TLS Version** constraint from the list on the **Organization policies** page.

  5. To update the organization policy for this resource, click **Edit**.

  6. On the **Edit** page, select **Customize**.

  7. Under **Policy enforcement** , select an enforcement option:

     * To merge and evaluate your organization policies together, select **Merge with parent**. For more information about inheritance and the resource hierarchy, see [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

     * To override policies inherited from a parent resource, select **Replace**.

  8. Click **Add rule**.

  9. Under **Policy values** , the default value is set to **Deny all**. Select **Custom** instead.

  10. Under **Policy type** , select **Deny**.

  11. Under **Custom values** , enter a TLS version to deny. The following values are valid custom values:

     * `TLS_VERSION_1` for TLS 1.0
     * `TLS_VERSION_1_1` for TLS 1.1

If you are restricting more than one TLS version, click **Add value** and enter the value in the additional field.

  12. To finish and apply the organization policy, click **Save**.




###  gcloud 

Use the [`gcloud org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy) to set an organization policy on the resource:
    
    
    gcloud org-policies set-policy POLICY_PATH

POLICY_PATH is the full path to your organization policy file, which should look like the following if using the YAML format:
    
    
    name: RESOURCE_TYPE/RESOURCE_ID/policies/gcp.restrictTLSVersion
    spec:
      rules:
      - values:
        deniedValues:
        - TLS_VERSION_1
        - TLS_VERSION_1_1
    

Replace with the following:

  * `RESOURCE_TYPE` is `organizations`, `folders` or `projects`.

  * `RESOURCE_ID` is your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.




Run the following command to verify that your policy has been applied:
    
    
    gcloud org-policies describe gcp.restrictTLSVersion --RESOURCE_TYPE=RESOURCE_ID --effective

Replace with the following:

  * `RESOURCE_TYPE` is `organization`, `folder` or `project`.

  * `RESOURCE_ID` is your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.




## Test the policy

The TLS version restriction policy constraint can be tested for any in-scope service. The following example curl command validates the TLS version restriction for a Cloud Storage bucket.

**Note:** curl restricts TLS v1.0 and v1.1 due to [IETF RFC 8996](https://datatracker.ietf.org/doc/html/rfc8996). To allow its use, you must either append the `--ciphers DEFAULT@SECLEVEL=0` parameter or modify the OpenSSL configuration to set the `MinProtocol` system default to either 1.0 or 1.1. See the [OpenSSL](https://www.openssl.org/docs/man3.0/man5/config.html) documentation for more information.
    
    
      curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://storage.googleapis.com/storage/v1/b/GCS_BUCKET_NAME/o" \
      --tlsvTLS_VERSION --tls-max TLS_VERSION --ciphers DEFAULT@SECLEVEL=0

There is no space between `--tlsv` and the value. For example: `--tlsv1.1`

Replace with the following:

  * `GCS_BUCKET_NAME` is a Cloud Storage bucket name in your project, such as `mybucketname`.

  * `TLS_VERSION` is a TLS version like `1.0` or `1.1` denied in the configured policy.




The following example `curl` request shows GCS_BUCKET_NAME set to `mybucketname` and TLS_VERSION set to `1.1`:
    
    
      curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://storage.googleapis.com/storage/v1/b/mybucketname/o" \
      --tlsv1.1 --tls-max 1.1 --ciphers DEFAULT@SECLEVEL=0

If the organization policy is configured to restrict `TLS_VERSION_X`, then any attempt to access resources with `TLS_VERSION_X` in the policy-restricted project in this example command will fail. An error message is returned that describes the reason for this failure.
    
    
    Request is disallowed by organization's constraints/gcp.restrictTLSVersion
    constraint for 'projects/PROJECT_NUMBER' to use service
    'SERVICE_NAME.googleapis.com' by violated TLS version `TLS_VERSION_X`

This output includes the following values:

  * `PROJECT_NUMBER`: the project number hosting the resource referred in the earlier command.
  * `SERVICE_NAME`: the name of the in-scope service blocked by the TLS restriction policy.



## Supported services

TLS version restriction is supported by any Google Cloud resource APIs that have a header signed by [Google Front End (GFE)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service).

**Note:** The `gcp.restrictTLSVersion` organization policy constraint is not enforced on public Cloud Storage objects because the request is directly served from the Google Front End (GFE) cache.

## Unsupported services

The TLS version restriction organization policy constraint is _not_ applicable for the following services:

  * Apigee
  * App Engine (`*.appspot.com`)
  * Cloud Run functions (`*.cloudfunctions.net`),
  * Cloud Run (`*.run.app`)
  * Private Service Connect
  * Custom domains



To restrict TLS versions for these services, use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless) along with [SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies). You can also use the predefined [`constraints/compute.requireSslPolicy` constraint](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#restrict-tls-capabilities-custom-constraint) along with custom constraints for SSL policies to enforce TLS version and cipher suite restrictions for your load balancers.

## What's next

  * Learn which [products are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for each control package.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
