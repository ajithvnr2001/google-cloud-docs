---
url: https://docs.cloud.google.com/vpc-service-controls/quotas/
title: Quotas and limits \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:47.864454+00:00
---

# Quotas and limits  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Resources ](https://docs.cloud.google.com/vpc-service-controls/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and limits that apply to VPC Service Controls. Quotas and limits specified in this document are subject to change.

The quota utilization computation is based on the sum of the utilization across the enforced and the dry-run modes. For example, if a service perimeter protects five resources in enforced mode and seven resources in dry-run mode, then the sum of both, which is 12, is tested against the corresponding limit. Also, each individual entry is counted as one even if it occurs elsewhere in the policy. For example, if a project is included in one regular perimeter and five bridge perimeters, all six instances are counted and no deduplication is performed.

However, VPC Service Controls calculates the service perimeter limits differently. For more information, see the [Service perimeter limits](https://docs.cloud.google.com/vpc-service-controls/quotas#perimeter-limits) section of this document.

## View quotas in the Google Cloud console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. On the **VPC Service Controls** page, select the access policy for which you want to view quotas.

  4. Click **View Quota**.

The **Quota** page displays the usage metrics for the following [access policy](https://docs.cloud.google.com/access-context-manager/docs/scoped-policies) limits that apply cumulatively across all service perimeters in a given access policy:

     * Service perimeters
     * Protected resources
     * Access levels
     * Total ingress and egress attributes



## Service perimeter limits

The following limit applies to each service perimeter configuration. That is, this limit applies separately for the dry-run and enforced configurations of a perimeter:

Type | Limit | Notes  
---|---|---  
Attributes  |  6,000  | This limit applies to the total number of attributes specified in the ingress and egress rules. The attribute limit includes the references to projects, VPC networks, access levels, method selectors, identities, and roles in these rules. The total attribute count also includes the use of wildcard characters, `*`, in the methods, services, and project attributes.   
[ Private Service Connect endpoints](https://docs.cloud.google.com/vpc-service-controls/docs/psc-endpoint) |  500  | This limit applies to the total number of Private Service Connect endpoints you can specify across all ingress and egress rules in a single service perimeter.   
  
### Attribute limit considerations

VPC Service Controls counts each entry in the following ingress and egress rule fields as one attribute:

Rule block | Fields  
---|---  
`ingressFrom` | 

  * `sources`
  * `identities`

  
`ingressTo` | 

  * `resources`
  * `methodSelectors`
  * `roles`

  
`egressFrom` | 

  * `sources`
  * `identities`

  
`egressTo` | 

  * `resources`
  * `methodSelectors`
  * `externalResources`
  * `roles`

  
  
For more information about these fields, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) and [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

VPC Service Controls considers the following rules to check if a perimeter exceeds the attribute limit:

  * Each field in an ingress and egress rule can have multiple entries, and each entry counts towards the limit.

For example, if you mention a service account and a user account in the `identities` field of an `egressFrom` rule block, VPC Service Controls counts two attributes towards the limit.

  * VPC Service Controls counts each occurrence of a resource in the rules separately, even if you repeat the same resource in multiple rules.

For example, if you mention a project, `project-1`, in two different ingress or egress rules, `rule-1` and `rule-2`, VPC Service Controls counts two attributes towards the limit.

  * Each service perimeter can have an [enforced](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#enforced-mode) and a [dry run](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#dry-run-mode) configuration. VPC Service Controls applies the attribute limit separately for each configuration.

For example, if the total attribute counts for the enforced and dry run configurations of a perimeter are 3,500 and 3,000 attributes, respectively, VPC Service Controls considers that the perimeter is still within the attribute limit.




## Access policy limits

The following [access policy](https://docs.cloud.google.com/access-context-manager/docs/scoped-policies) limits apply cumulatively across all service perimeters in a given access policy:

Type | Limit | Notes  
---|---|---  
Service perimeters  |  10,000  |  Service perimeter bridges count towards this limit.   
Protected resources  |  40,000  | Projects that are only referenced in ingress and egress policies don't count towards this limit. Add protected resources to a policy only in batches of 10,000 resources or fewer to prevent policy modification requests from timing out. We recommend that you wait 30 seconds before making the next policy modification.  
Identity groups  |  1,000  |  This limit is on the count of identity groups configured in the ingress and egress rules.   
Agent identities  |  1,000  |  This limit is on the count of agent identities configured in the ingress and egress rules.   
Deleted identities ([Preview](https://cloud.google.com/products/#product-launch-stages))  |  500  |  This limit applies to the number of deleted identities configured in the access policy.   
Workload Identity Federation for GKE ([Preview](https://cloud.google.com/products#product-launch-stages))  |  1,000  |  The maximum number of Workload Identity Federation for GKE principals that you can configure across ingress and egress rules.   
VPC networks  | 500  | This limit is on the count of VPC networks referenced in the enforced mode, dry-run mode, and ingress rules.   
Total character length of all rule titles  | 240,000  | The combined length of all ingress and egress rule titles must not exceed this limit. Whitespace characters in the rule titles also count toward this limit. However, any rule for which you haven't provided a title doesn't count toward this limit.   
  
The following [access policy](https://docs.cloud.google.com/access-context-manager/docs/scoped-policies) limits apply cumulatively across all access levels in a given access policy:

Type | Limit | Notes  
---|---|---  
VPC networks  | 500  | This limit is on the count of VPC networks referenced in access levels.   
  
## Organization limits

The following limits apply across all access policies in a given organization:

Type | Limit  
---|---  
Organization-level access policy  |  1   
Folder and project-scoped access policies  |  50   
  
## Access Context Manager quotas and limits

You're also subject to the [Access Context Manager quotas and limits](https://docs.cloud.google.com/access-context-manager/quotas#limits) because VPC Service Controls uses Access Context Manager APIs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
