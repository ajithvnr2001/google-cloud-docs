---
url: https://docs.cloud.google.com/vpc-service-controls/docs/access-level-design/
title: Design access levels \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:50.222978+00:00
---

# Design access levels  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/access-level-design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Design access levels Stay organized with collections  Save and categorize content based on your preferences. 

This document describes access-level implementations and provides recommendations for initiating service perimeter enforcement based on allowlists.

When you complete a dry-run execution of workloads, you identify a list of IP addresses and identities that you need to add to an allowlist. You might also find that some workloads need a device-based allowlist. To grant controlled access to protected Google Cloud resources, you can use VPC Service Controls access levels. Some practical ways that you can implement access levels are based on IP address, identity, or device.

For more information, see [Context-aware access with ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access).

### Granting access based on source IP

You can only use [public IP CIDR ranges](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#ip-subnetworks) in the access levels for IP-based allowlists. Since this method allows all protected APIs from this IP range, the environment behind these IPs must be trusted and controlled. A typical usage scenario for this allowlist is to allow perimeter access from on-premises networks. The following diagram shows how an IP-based allowlist blocks and allows perimeter access:

![The VPC Service Controls network and service perimeter prevents access from a valid identity on an untrusted network.](https://docs.cloud.google.com/static/vpc-service-controls/images/vpc-service-controls-enterprise-best-practices-ip-based-allowlist.png)

In the preceding diagram, a valid identity attempts to access the perimeter. The access attempts are rejected when they originate from any internet IP addresses. However, access is allowed when it is sourced from the corporate public IP addresses.

A variation on this scenario is when you allow perimeter access from private resources deployed in a different project or organization. In this use case, a Cloud NAT gateway is required in the source project. [Cloud NAT](https://docs.cloud.google.com/nat/docs/nat-product-interactions#interaction-pga) has an integration with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) that automatically enables Private Google Access on the resource's subnet, and keeps the traffic to Google APIs and services internal, instead of routing it to the internet using the Cloud NAT gateway external IP address. As the traffic is routed within the internal Google network, the `RequestMetadata.caller_ip` field of the `AuditLog` object is redacted to `gce-internal-ip`. To allow perimeter access in this case, you need to configure an ingress rule to allow access based on other attributes such as the project or service account, instead of configuring an access level based on the external source IP address.

### Granting access based on caller identity

To implement an identity-based allowlist, you add service accounts and [organization super administrators](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices) to an allowlist. The perimeter is open for these identities from any IP address, so you need to make sure that the identities are well-guarded. You also need to make sure that you avoid minting keys for service accounts that you have added to an allowlist. It is uncommon to add user identities to an allowlist (groups can't be added to an allowlist) on a perimeter.

Resources within the perimeter can be accessed through VMs within the perimeter, from trusted on-premises networks, or from trusted devices. We recommend using [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) to access resources within perimeters because VPC Service Controls doesn't support [Cloud Shell](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#shell).

**Note:** You can only implement an identity-based allowlist using access levels by using the [gcloud CLI](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example). You can use the Google Cloud console to configure ingress rules that implement identity-based access levels.

### Qualifying access based on the caller device attributes

Device trust, also called _trusted endpoint_ , relies on having a valid organization user signed in to a Chrome browser or to a Chromebook. The trust applies to the OS signed-in session. For example, a Windows user that is signed in and running a Chrome session (the browser doesn't need to be open) can successfully call gcloud CLI commands on protected perimeter APIs. However, a different Windows user session on the same machine can't call commands on the protected perimeter APIs.

**Note:** Caller device attributes are available only if you are using Chrome Enterprise Premium.

The following device conditions are useful to establish device trust:

  * [**Verified Chrome OS**](https://developers.google.com/chrome/verified-access/developer-guide) is a highly secure, cryptographically verified condition that indicates that a valid organization user is signed in to a securely booted Chromebook. This is a recommended tier 1 trust condition.

![The Operating system policy with the Verified Chrome OS option enabled.](https://docs.cloud.google.com/static/vpc-service-controls/images/vpc-service-controls-enterprise-best-practices-verified-chrome-os.png)

  * [**Require admin approval for device access**](https://support.google.com/cloudidentity/answer/7508418) allows Cloud Identity administrators to approve each device before any access is granted. By default, devices are auto-approved if they have a valid organization user signed in. However, we recommend turning off the auto-approval option.

  * **Require corp owned device** relies on the Chrome agent retrieving the serial number from the OS, which usually comes from the BIOS. This number must match existing serial numbers that you have [entered into Cloud Identity](https://support.google.com/cloudidentity/answer/7129612).

Because the serial number isn't authoritative in non-Chrome OS devices, a user with elevated administrator privileges might be able to spoof the serial number. We recommend using this condition only as a tier 2 check.


**Note:** For trust to apply, the user and device must be in the same organization as the Google Cloud resources.

For a sample tracker for granting controlled access based on the conditions discussed in the preceding list, see [VPC Service Controls onboarding template - allowlist (PDF)](https://docs.cloud.google.com/static/solutions/vpc-service-controls-enterprise-best-practices-use-cases-template.pdf).

### Initiate enforcement

After you design the allowlist and update access levels, we recommend that you execute the workloads again to confirm that there aren't any violations. If the workloads execute without violations, you can initiate VPC Service Controls enforcement without impacting the applications.

When you plan for enforcement, include the following:

  * Choose an enforcement date and communicate that date to all related teams.
  * Ensure that the security operations and incident response teams are aware of the deployment. Additionally, make sure that individuals with appropriate permissions inspect logs and approve additional allowlists, if necessary.
  * Ensure that the situation response team can open a Google Cloud support case, if any questions or issues arise.
  * Create or modify perimeter and access levels using automation tools like [Terraform](https://registry.terraform.io/modules/terraform-google-modules/vpc-service-controls/google/0.1.0/submodules/regular_service_perimeter). We recommend against performing these tasks manually.



When you initiate enforcement, start by moving projects that are associated with a single workload from the dry run perimeter to the live perimeter. Make sure to allow time for the application to run correctly while you observe the violation logs. Repeat the process for remaining workloads one at a time.

To surface blocked violations, [configure an aggregated logging sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) that sends audit logs for all projects in the perimeter to BigQuery. Then, run the following query:
    
    
    SELECT
    receiveTimestamp, #time of violation
    Resource.labels.service, #protected Google Cloud service being blocked
    protopayload_auditlog.methodName, #method name being called
    resource.labels.project_id as PROJECT, #protected project blocking the call
    protopayload_auditlog.authenticationInfo.principalEmail, #caller identity
    protopayload_auditlog.requestMetadata.callerIp, #caller IP
    JSON_EXTRACT(protopayload_auditlog.metadataJson, '$.dryRun') as DRYRUN, #dry-run indicator
    JSON_EXTRACT(protopayload_auditlog.metadataJson, '$.violationReason') as REASON, #reason for violation
    protopayload_auditlog.metadataJson, #raw violation entry
    FROM `BQ_DATASOURCE_NAME.cloudaudit_googleapis_com_policy_*`
    WHERE JSON_EXTRACT(protopayload_auditlog.metadataJson, '$.dryRun') is null #exclude logs from a dry-run perimeter
    

## What's next

  * Learn how to [allow access to protected resources from outside the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).
  * Learn how to [list, update, and delete service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
