---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/preventative-controls/
title: Preventative controls for acceptable resource configurations \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:29.410663+00:00
---

# Preventative controls for acceptable resource configurations  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/preventative-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Preventative controls for acceptable resource configurations Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

We recommend that you define policy constraints that enforce acceptable resource configurations and prevent risky configurations. The blueprint uses a combination of organization policy constraints and infrastructure-as-code (IaC) validation in your pipeline. These controls prevent the creation of resources that don't meet your policy guidelines. Enforcing these controls early in the design and build of your workloads helps you to avoid remediation work later.

## Organization policy constraints

The [Organization Policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) service enforces constraints to ensure that certain resource configurations can't be created in your Google Cloud organization, even by someone with a sufficiently privileged IAM role.

The blueprint enforces policies at the organization node so that these controls are inherited by all folders and projects within the organization. This bundle of policies is designed to prevent certain high-risk configurations, such as exposing a VM to the public internet or granting public access to storage buckets, unless you deliberately allow an exception to the policy.

The following table introduces the [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that are implemented in the blueprint:

Organization policy constraint | Description  
---|---  
`compute.disableNestedVirtualization` | [Nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) on Compute Engine VMs can evade monitoring and other security tools for your VMs if poorly configured. This constraint prevents the creation of nested virtualization.  
`compute.disableSerialPortAccess` | IAM roles like `compute.instanceAdmin` allow privileged access to an [instance's serial port](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) using SSH keys. If the SSH key is exposed, an attacker could access the serial port and bypass network and firewall controls. This constraint prevents serial port access.  
`compute.disableVpcExternalIpv6` | [External IPv6 subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types) can be exposed to unauthorized internet access if they are poorly configured. This constraint prevents the creation of external IPv6 subnets.  
`compute.requireOsLogin` | The default behavior of setting [SSH keys in metadata](https://docs.cloud.google.com/compute/docs/instances/access-overview#ssh-access) can allow unauthorized remote access to VMs if keys are exposed. This constraint enforces the use of [OS Login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) instead of metadata-based SSH keys.  
`compute.restrictProtocolForwardingCreationForTypes` | [VM protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding) for external IP addresses can lead to unauthorized internet egress if forwarding is poorly configured. This constraint allows VM protocol forwarding for internal addresses only.  
`compute.restrictXpnProjectLienRemoval` | Deleting a Shared VPC host project can be disruptive to all the service projects that use networking resources. This constraint prevents accidental or malicious deletion of the Shared VPC host projects by preventing the removal of the [project lien](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#protectsharedvpc) on these projects.  
`compute.setNewProjectDefaultToZonalDNSOnly` | A legacy setting for [global (project-wide) internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) is not recommended because it reduces service availability. This constraint prevents the use of the legacy setting.  
`compute.skipDefaultNetworkCreation` | A default VPC network and overly permissive default VPC firewall rules are created in every new project that enables the Compute Engine API. This constraint skips the creation of the default network and default VPC firewall rules.  
`compute.vmExternalIpAccess` | By default, a VM is created with an external IPv4 address that can lead to unauthorized internet access. This constraint configures an empty allowlist of external IP addresses that the VM can use and denies all others.  
`essentialcontacts.allowedContactDomains` | By default, [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) can be configured to send notifications about your domain to any other domain. This constraint enforces that only email addresses in approved domains can be set as recipients for Essential Contacts.  
`iam.allowedPolicyMemberDomains` | By default, [allow policies](https://docs.cloud.google.com/iam/docs/policies) can be granted to any Google Account, including unmanaged accounts, and accounts belonging to external organizations. This constraint ensures that allow policies in your organization can only be granted to managed accounts from your own domain. Optionally, you can [allow additional domains](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).  
`iam.automaticIamGrantsForDefaultServiceAccounts` | By default, [default service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) are automatically granted overly permissive roles. This constraint prevents the automatic IAM role grants to default service accounts.  
`iam.disableServiceAccountKeyCreation` | Service account keys are a high-risk persistent credential, and in most cases a [more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) can be used. This constraint prevents the creation of service account keys.  
`iam.disableServiceAccountKeyUpload` | Uploading service account key material can increase risk if key material is exposed. This constraint prevents the uploading of service account keys.  
`sql.restrictAuthorizedNetworks` | Cloud SQL instances can be exposed to unauthenticated internet access if the instances are configured to use [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) without a [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy). This policy prevents the configuration of authorized networks for database access and forces the use of the Cloud SQL Auth Proxy instead.  
`sql.restrictPublicIp`| Cloud SQL instances can be exposed to unauthenticated internet access if the instances are created with public IP addresses. This constraint prevents [public IP addresses](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) on Cloud SQL instances.  
`storage.uniformBucketLevelAccess` | By default, objects in Cloud Storage can be accessed through legacy [Access Control Lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) instead of IAM, which can lead to inconsistent access controls and accidental exposure if misconfigured. Legacy ACL access is not affected by the `iam.allowedPolicyMemberDomains` constraint. This constraint enforces that access can only be configured through IAM [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access), not legacy ACLs.  
`storage.publicAccessPrevention` | Cloud Storage buckets can be exposed to unauthenticated internet access if misconfigured. This constraint prevents ACLs and IAM permissions that grant access to `allUsers` and `allAuthenticatedUsers`.  
  
These policies are a starting point that we recommend for most customers and most scenarios, but you might need to modify organization policy constraints to accommodate certain workload types. For example, a workload that uses a Cloud Storage bucket as the backend for Cloud CDN to host public resources is blocked by `storage.publicAccessPrevention`, or a public-facing Cloud Run app that doesn't require authentication is blocked by `iam.allowedPolicyMemberDomains`. In these cases, modify the organization policy at the folder or project level to allow a narrow exception. You can also [conditionally add constraints to organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy#conditionally_add_constraints_to_organization_policy) by defining a tag that grants an exception or enforcement for policy, then applying the tag to projects and folders.

For additional constraints, see [available constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) and [custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints).

## Pre-deployment validation of infrastructure-as-code

The blueprint uses a GitOps approach to manage infrastructure, meaning that all infrastructure changes are implemented through version-controlled infrastructure-as-code (IaC) and can be validated before deploying.

The [policies enforced in the blueprint](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/policy-library/policies/constraints) define acceptable resource configurations that can be deployed by your pipeline. If code that is submitted to your GitHub repository does not pass the policy checks, no resources are deployed.

For information on how pipelines are used and how controls are enforced through CI/CD automation, see [deployment methodology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology).

## What's next

  * Read about [deployment methodology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology) (next document in this series)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
