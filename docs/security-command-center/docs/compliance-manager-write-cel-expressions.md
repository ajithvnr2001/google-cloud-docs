---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions/
title: Write rules for custom cloud controls \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:19.984358+00:00
---

# Write rules for custom cloud controls  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Write rules for custom cloud controls Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When you create a [custom cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control), you use Common Expression Language (CEL) expressions to create the rules that evaluate the properties of the scanned resource. Supported resources are Cloud Asset Inventory [resource types](https://docs.cloud.google.com/asset-inventory/docs/asset-types#resource-types). REST APIs are not supported.

Your expressions can be checks of a single value or more complex compound expressions that check multiple values or conditions. Either way, the expression must resolve to a boolean `false` to trigger a finding.

CEL expressions that evaluate resource properties must conform to the following rules:

  * The properties that you specify in a CEL expression must be properties of the scanned resource, as defined in the API definition of the resource type.

  * All enums in a CEL expression must be represented as strings. For example, the following is a valid expression for the `cloudkms.googleapis.com/CryptoKeyVersion` resource type:
        
        resource.data.state = "PENDING_GENERATION"

  * The result of the CEL expressions that you define in the `condition` property must be a Boolean. A finding is triggered only if the result is `false`.




To find the name for a resource, see [Asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types).

For more information about CEL, see the following:

  * [The CEL spec](https://github.com/google/cel-spec)
  * [The CEL language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md)



## Example CEL expressions

The following table lists some CEL expressions that you can use to evaluate resource properties.

Resource type | Description | CEL expression  
---|---|---  
`cloudkms.googleapis.com/CryptoKey` | Check the Cloud KMS key rotation period | `has(resource.data.rotationPeriod) && resource.data.rotationPeriod < duration('60h')`  
`compute.googleapis.com/Network` | Match Virtual Private Cloud peering rule to network peers | `resource.data.selfLink.matches('https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default') || resource.data.peerings.exists(p, p.network.matches('https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/shared$'))`  
`cloudfunctions.googleapis.com/CloudFunction` | Only allow internal ingress traffic for a Cloud Run function  | `has(resource.data.ingressSettings) && resource.data.ingressSettings.matches('ALLOW_INTERNAL_ONLY')`  
`compute.googleapis.com/Instance` | Resource name matches pattern | `resource.data.name.matches('^gcp-vm-(linux|windows)-v\\\\d+$')`  
`serviceusage.googleapis.com/Service` | Only allow storage-related APIs to be enabled  | `resource.data.state == 'ENABLED' && !( resource.data.name.matches('storage-api.googleapis.com') || resource.data.name.matches('bigquery-json.googleapis.com') || resource.data.name.matches('bigquery.googleapis.com') || resource.data.name.matches('sql-component.googleapis.com') || resource.data.name.matches('spanner.googleapis.com'))`  
`sqladmin.googleapis.com/Instance` | Only permit public IP addresses that are on the allowlist  | `(resource.data.instanceType == 'CLOUD_SQL_INSTANCE' && resource.data.backendType == 'SECOND_GEN' && resource.data.settings.ipConfiguration.ipv4Enabled ) && (resource.data.ipAddresses.all(ip, ip.type != 'PRIMARY' || ip.ipAddress.matches('IP_ADDRESS')))`  
`dataproc.googleapis.com/Cluster` | Check if project IDs in a Managed Service for Apache Spark cluster contain the substrings `testing` or `development` | `has(resource.data.projectId) && !resource.data.projectId.contains('testing') || !resource.data.projectId.contains('development')`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
