---
url: https://docs.cloud.google.com/organization-policy/restrict-locations/
title: Restrict resource locations \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:14.668587+00:00
---

# Restrict resource locations  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/restrict-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Restrict resource locations Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** The information on this page does _not_ describe Google Cloud Platform's data location commitments for Customer Data (as defined in the agreement under which Google has agreed to provide Google Cloud Platform services and as described in the [Google Cloud Platform Services Summary](https://cloud.google.com/terms/services)) to its customers. For the list of Google Cloud Platform services for which Customer Data location may be selected by customers, see [Google Cloud Platform Services with Data Residency](https://cloud.google.com/terms/data-residency).

## Overview

This guide describes how to set an [organization policy](https://docs.cloud.google.com/organization-policy/overview) that includes the resource locations constraint.

You can limit the physical location of a new resource with the Organization Policy Service resource locations constraint. You can use the location property of a resource to identify where it is deployed and maintained by the service. For data-containing resources of some Google Cloud services, this property also reflects the location where data is stored. This constraint lets you define the allowed Google Cloud locations where the resources for supported services in your hierarchy can be created.

After you define resource locations, this limitation will apply only to newly-created resources. Resources you created before setting the resource locations constraint will continue to exist and perform their function.

A policy that includes this constraint won't be enforced on sub-resource creation for certain services, such as Cloud Storage and Managed Service for Apache Spark.

**Warning:** An organization policy that includes this constraint will prevent services from creating new resources that violate the constraint, which can stop those services from working correctly. Some services interact with and implement the resource location constraint in different ways. For details and examples of these special cases, see the [Services that support restricting resource locations](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services) page.

## Limitations

The resource locations Organization Policy Service constraint controls the ability to create resources for which a location can be selected. This constraint does not affect where global resources, such as Compute Engine global addresses, or resources that don't support selecting a location are created.

To avoid breaking existing serving infrastructure, you should test any new policy on non-production projects and folders, then apply the policy gradually within your organization.

**Note:** The resource locations constraint controls only where resources are created. Some Google Cloud services might not store or process data contained by a resource in the same location where that resource was created.

For data storage commitments, see the [Google Cloud Terms of Service](https://cloud.google.com/terms) and the [Service Specific Terms](https://cloud.google.com/terms/service-terms). Organization policies that contain the resource locations constraint aren't data storage commitments.

This constraint applies to a specific subset of products and resource types. For a list of supported services and details on the behavior of each service, see the [Services that support restricting resource locations](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services) page.

## Location types

You can deploy Google Cloud resources in [location](https://cloud.google.com/about/locations) types that represent different size categories. The largest location type is the `multi-region`, which includes more than one `region`. Each `region` is further subdivided into `zones`. For more information about regions and zones, see the [Regions and Zones overview](https://docs.cloud.google.com/compute/docs/regions-zones).

  * `Multi-region` locations are backed by physical resources in more than one `region` and are typically only used by storage-based resources. Some examples include `us`, `asia`, `europe`, and `global`.

  * `Region` locations are geographically isolated from each other. Some examples include `us-west1` (Oregon), `asia-northeast1` (Tokyo), and `europe-west1` (Belgium).

  * `Zone` locations are the most granular and isolated location type used for deploying resources. A `zone` is an independent failure domain within a `region`. Some examples are `us-east1-b`, `us-west1-b`, and `asia-northeast1-a`. Google Cloud also offers specialized [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) that are tailored for AI and ML workloads—for example, `us-central1-ai1a`.




When setting up locations, you should use the `in:` prefix and a Value Group. Using a Value Group curated by Google Cloud lets you choose geographic location(s), without having to specify current or future Cloud locations.

The `in:` prefix to a Value Group specifies that all values that exist within the value group are considered to be part of the policy. If you enter a group value or a Google Cloud region without the prefix, the `in:` prefix will be automatically added, per these rules:

  * If you enter a location that uses the `in:` prefix, and it contains any invalid group, the policy change will fail.
  * If you enter a location that is a region, such as `us-east1`, it will have the `in:` prefix prepended, to `in:us-east1-locations` in this example.
  * If you enter a region or multi-region value group such as `us-locations`, it will have the `in:` prefix prepended, to `in:us-locations` in this example.
  * If you enter a zone or multi-region such as `us-east1-b` or `us`, the values won't be changed.



## Setting the organization policy

The resource locations constraint is a type of legacy managed constraint with [list rules](https://docs.cloud.google.com/organization-policy/create-organization-policies#list-constraint). You can add and remove locations from the `allowed_values` or `denied_values` lists of a resource locations constraint. To prevent organization policies from unexpectedly restricting service behavior as new locations are added to the available list, use a value group, or a list of `allowed_values` that represents the entire geographic boundary you want to define.

To set an [organization policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy) including a resource locations constraint:

### Console

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the organization, folder, or project for which you want to set the organization policy.

  3. Select the **Google Cloud Platform - Resource Location Restriction** constraint to open its **Policy details** page.

  4. Click **Manage policy**.

  5. On the **Edit policy** page, select **Override parent's policy**.

  6. Under **Policy enforcement** , select **Replace**.

  7. Click **Add rule**.

  8. Under **Policy values** , select **Custom**.

  9. Under **Policy type** , select **Allow** to create a list of allowed locations, or select **Deny** to create a list of denied locations.

  10. In the **Policy value** box, enter the `in` prefix and a value group location string, then press **Enter**.

For example, `in:us-locations` or `in:us-west1-locations`. You can enter multiple location strings by clicking **Add value**.

You can also enter specific zone, region, or multi-region locations as location strings. For a list of available locations, see the [Services that support restricting resource locations](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services) page.

  11. To enforce the policy, click **Set policy**.




### gcloud

To create an organization policy that enforces the resource locations constraint, create a policy YAML file that references the constraint:
    
    
    name: organizations/ORGANIZATION_ID/policies/gcp.resourceLocations
    spec:
      rules:
      - values:
          deniedValues:
          - in:us-east1-locations
          - in:northamerica-northeast1-locations
    

To enforce the organization policy containing the constraint, run the following command:
    
    
    gcloud org-policies set-policy POLICY_PATH
    

Replace the following:

  * [`ORGANIZATION_ID`](https://docs.cloud.google.com/organization-policy/restrict-domains#retrieving_customer_id): your organization ID, such as 01234567890.
  * `POLICY_PATH`: the full path to the YAML file containing the organization policy.



A response will be returned with the results of the new organization policy:
    
    
    name: organizations/01234567890/policies/gcp.resourceLocations
    spec:
      rules:
      - values:
          deniedValues:
          - in:us-east1-locations
          - in:northamerica-northeast1-locations
    

You can also enter specific zone, region, or multi-region locations as location strings. For a list of available locations, see the [Resource locations supported services](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services) page.

### API

You can use the Resource Manager API to set an organization policy on a resource. You will need an OAuth 2.0 bearer token for authentication and authorization.

To set an organization policy using the resource locations constraint:
    
    
    curl -X POST -H "Content-Type: application/json" -H "Authorization: \
    Bearer ${bearer_token}" -d '{policy: {etag: "BwVtXec438Y=", constraint: \
    "constraints/gcp.resourceLocations", list_policy: {denied_values: \
    ["in:europe-locations", "in:southamerica-locations"] }}}' \
    https://cloudresourcemanager.googleapis.com/v1/organizations/123456789:setOrgPolicy
    

A response will be returned with the results of the new organization policy:
    
    
    name: organizations/01234567890/policies/gcp.resourceLocations
    spec:
      rules:
      - values:
          deniedValues:
          - in:europe-locations
          - in:southamerica-locations
    

You can also enter specific zone, region, or multi-region locations as location strings. For a list of available locations, see the [Resource locations supported services](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services) page.

To learn about using constraints in organization policies, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#list-constraint).

### Using inheritance in organization policy

You can refine your organization policy to inherit the organization policy from the resource's parent nodes. [Inheritance](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation) gives you granular control over the organization policies used throughout your resource hierarchy.

To enable inheritance on a resource node, set `inheritFromParent = true` in the organization policy YAML file. For example:
    
    
    name: organizations/01234567890/policies/gcp.resourceLocations
    spec:
      inheritFromParent: true
      rules:
      - values:
          deniedValues:
          - in:us-west1
    

## Allow or deny VM creation in AI zones

You can allow or deny VMs from being created in AI zones by creating and enforcing a custom constraint in a custom organization policy.

An AI zone is identified with the string `ai` in its name. For example, `us-west4-ai2b` is an AI zone in the `us-west4` region, and `us-west4-b` is the parent zone. When creating a custom constraint, use the string `-ai` in your condition. For more information about AI zones, see [About AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).

**Note:** Conditions can only evaluate individual values, as custom organization policy doesn't support value groups. The custom constraint described in this section applies only to VMs and not to other resources, such as disks.

For permissions required to manage organization policies, see [Required roles](https://docs.cloud.google.com/organization-policy/create-custom-constraints#required-roles) in the _Creating and managing custom constraints_ page.

To set a custom organization policy to allow or deny VMs from being created in AI zones, complete the following steps:

  1. **Create a custom constraint for AI zones**

Depending on whether you want to allow or deny VMs from being created in AI zones, create a YAML file with one of the following constraints.

     * To allow VMs to be created in AI zones only, use the following constraint:
           
           name: organizations/ORGANIZATION_ID/customConstraints/custom.allowOnlyAiZones
           resource_types:
           - compute.googleapis.com/Instance
           method_types:
           - CREATE
           - UPDATE
           actionType: ALLOW
           condition: "resource.zone.contains('-ai')"
           displayName: allowOnlyAiZones
           description: Allow VMs to be created in AI zones only.
           

     * To deny VMs from being created in AI zones, use the following constraint:
           
           name: organizations/ORGANIZATION_ID/customConstraints/custom.denyAiZones
           resource_types:
           - compute.googleapis.com/Instance
           method_types:
           - CREATE
           - UPDATE
           actionType: DENY
           condition: "resource.zone.contains('-ai')"
           displayName: denyAiZones
           description: Deny VMs from being created in AI zones.
           

Replace [`ORGANIZATION_ID`](https://docs.cloud.google.com/organization-policy/restrict-domains#retrieving_customer_id) with your organization ID—for example, `01234567890`.

  2. **Set the custom constraint**

After you've created the YAML file for the custom constraint, you must set the custom constraint to make it available for organization policies.

To set the custom constraint, use the `gcloud org-policies set-custom-constraint` command:
         
         gcloud org-policies set-custom-constraint CONSTRAINT_PATH
         

Replace `CONSTRAINT_PATH` with the full path to your custom constraint YAML file—for example, `/home/user/customconstraint.yaml`.

  3. **Create an organization policy**

To create an organization policy that enforces the custom constraint, create a policy YAML file that references the constraint:
         
         name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - enforce: true
         

Replace the following:

     * `PROJECT_ID`: the project that you want to enforce your constraint on.

     * `CONSTRAINT_NAME`: the name of your custom constraint—`custom.allowOnlyAiZones` or `custom.denyAiZones`.

  4. **Enforce the custom organization policy on your project**

To enforce the organization policy containing the custom constraint, run the following command:
         
         gcloud org-policies set-policy POLICY_PATH
         

Replace `POLICY_PATH` with the full path to your organization policy YAML file. Changes to organization policies can take up to 15 minutes to be fully enforced.




For more information about custom constraints, see [Create custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints). For troubleshooting, see [Troubleshooting custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#troubleshooting_constraints).

## Example error message

Services that support the resource location constraint are prevented from creating new resources in locations that would violate the constraint. If a service attempts to create a resource in a location that violates the constraint, the attempt will fail and an error message will be generated.

This error message will have this format: `LOCATION_IN_REQUEST violates constraint constraints/gcp.resourceLocations on the resource RESOURCE_TESTED. `

In the following example, a Compute Engine resource fails to create a new [instance](https://docs.cloud.google.com/compute/docs/instances) due to policy enforcement:
    
    
    Location ZONE:us-east1-b violates constraint constraints/gcp.resourceLocations
    on the resource
    projects/policy-violation-test/zones/us-east1-b/instances/instance-3.
    

Google Cloud Observability and Cloud Audit Logs log entry:
    
    
    {
     insertId: "5u759gdngec"
     logName: "projects/policy-violation-test/logs/cloudaudit.googleapis.com%2Factivity"
     protoPayload: {
      @type: "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {…}
      authorizationInfo: [6]
      methodName: "beta.compute.instances.insert"
      request: {…}
      requestMetadata: {…}
      resourceLocation: {…}
      resourceName: "projects/policy-violation-test/zones/us-east1-b/instances/instance-3"
      response: {
       @type: "type.googleapis.com/error"
       error: {
        code: 412
        errors: [
         0: {
          domain: "global"
          location: "If-Match"
          locationType: "header"
          message: "Location ZONE:us-east1-b violates constraint constraints/gcp.resourceLocations on the resource projects/policy-violation-test/zones/us-east1-b/instances/instance-3."
          reason: "conditionNotMet"
         }
        ]
        message: "Location ZONE:us-east1-b violates constraint constraints/gcp.resourceLocations on the resource projects/policy-violation-test/zones/us-east1-b/instances/instance-3."
       }
      }
      serviceName: "compute.googleapis.com"
      status: {
       code: 3
       message: "INVALID_ARGUMENT"
      }
     }
     receiveTimestamp: "2019-06-14T03:04:23.660988360Z"
     resource: {
      labels: {…}
      type: "gce_instance"
     }
     severity: "ERROR"
     timestamp: "2019-06-14T03:04:22.783Z"
    }
    

## Vulnerability findings and remediation

The resource location constraint restricts the creation of resources at runtime. This feature helps to prevent location violations from occurring, but does not identify or remediate existing violations. You can use Security Health Analytics, a built-in service of Security Command Center, to discover location violations in your resource hierarchy. For more information, see [Organization Policy vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#org-findings).

If there are Security Health Analytics findings of location violations, see [Remediating Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#org_policy_location_restriction) for steps to remediate those findings.

## Value groups

Value groups are collections of groups and locations that are curated by Google to provide a simple way to define your resource locations. Value groups include many related locations and are expanded over time by Google without needing to change your organization policy to accommodate the new locations.

To use value groups in your organization policy, prefix your entries with the string `in:`. For more information on using value prefixes, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#hierarchy_subtree). Group names are validated on the call to set the organization policy. Using an invalid group name will cause the policy setting to fail.

**Note:** The `global` location is considered a [multi-region](https://docs.cloud.google.com/organization-policy/restrict-locations#location_types). Its datacenters are spread throughout the world. It is not possible to predict or control exactly which datacenters are selected or where they are located. Depending on the service, there is a distinction between "US" and "us","EU" and "eu". For the list of services and the corresponding values, see the [multi-regional locations](https://cloud.google.com/about/locations#multi-region).

The following table contains the current list of available groups:

Group | Details | Direct members  
---|---|---  
Johannesburg  |  All locations within Johannesburg:  
`in:africa-south1-locations` | _Values:_  


  * `africa-south1`
  * `africa-south1-a`
  * `africa-south1-b`
  * `africa-south1-c`

  
Asia  |  All locations within Asia:  
`in:asia-locations` | _Groups:_  


  * `asia-east2-locations`
  * `id-locations`
  * `il-locations`
  * `in-locations`
  * `jp-locations`
  * `kr-locations`
  * `me-central1-locations`
  * `sa-locations`
  * `sg-locations`
  * `tw-locations`

  
_Values:_  


  * `asia`
  * `asia1`
  * `aws-ap-northeast-2`

  
Hong Kong  |  All locations within Hong Kong:  
`in:asia-east2-locations` | _Values:_  


  * `asia-east2`
  * `asia-east2-a`
  * `asia-east2-b`
  * `asia-east2-c`

  
Indonesia  |  All locations within Indonesia:  
`in:id-locations` | _Groups:_  


  * `asia-southeast2-locations`

  
_Values:_  


  * `id`

  
Jakarta  |  All locations within Jakarta:  
`in:asia-southeast2-locations` | _Values:_  


  * `asia-southeast2`
  * `asia-southeast2-a`
  * `asia-southeast2-b`
  * `asia-southeast2-c`

  
Israel  |  All locations within Israel:  
`in:il-locations` | _Groups:_  


  * `me-west1-locations`

  
_Values:_  


  * `il`

  
Israel  |  All locations within Israel:  
`in:me-west1-locations` | _Values:_  


  * `me-west1`
  * `me-west1-a`
  * `me-west1-b`
  * `me-west1-c`

  
India  |  All locations within India:  
`in:in-locations` | _Groups:_  


  * `asia-south1-locations`
  * `asia-south2-locations`

  
_Values:_  


  * `in`

  
Mumbai  |  All locations within Mumbai:  
`in:asia-south1-locations` | _Values:_  


  * `asia-south1`
  * `asia-south1-a`
  * `asia-south1-b`
  * `asia-south1-c`

  
Delhi  |  All locations within Delhi:  
`in:asia-south2-locations` | _Values:_  


  * `asia-south2`
  * `asia-south2-a`
  * `asia-south2-b`
  * `asia-south2-c`

  
Japan  |  All locations within Japan:  
`in:jp-locations` | _Groups:_  


  * `asia-northeast1-locations`
  * `asia-northeast2-locations`

  
_Values:_  


  * `jp`

  
Tokyo  |  All locations within Tokyo:  
`in:asia-northeast1-locations` | _Values:_  


  * `asia-northeast1`
  * `asia-northeast1-a`
  * `asia-northeast1-b`
  * `asia-northeast1-c`

  
Osaka  |  All locations within Osaka:  
`in:asia-northeast2-locations` | _Values:_  


  * `asia-northeast2`
  * `asia-northeast2-a`
  * `asia-northeast2-b`
  * `asia-northeast2-c`

  
South Korea  |  All locations within South Korea:  
`in:kr-locations` | _Groups:_  


  * `asia-northeast3-locations`

  
_Values:_  


  * `kr`

  
Seoul  |  All locations within Seoul:  
`in:asia-northeast3-locations` | _Values:_  


  * `asia-northeast3`
  * `asia-northeast3-a`
  * `asia-northeast3-b`
  * `asia-northeast3-c`

  
Doha  |  All locations within Doha:  
`in:me-central1-locations` | _Values:_  


  * `me-central1`
  * `me-central1-a`
  * `me-central1-b`
  * `me-central1-c`

  
Saudi Arabia  |  All locations within Saudi Arabia:  
`in:sa-locations` | _Groups:_  


  * `me-central2-locations`

  
_Values:_  


  * `sa`

  
Dammam  |  All locations within Dammam:  
`in:me-central2-locations` | _Values:_  


  * `me-central2`
  * `me-central2-a`
  * `me-central2-b`
  * `me-central2-c`

  
Singapore  |  All locations within Singapore:  
`in:sg-locations` | _Groups:_  


  * `asia-southeast1-locations`

  
_Values:_  


  * `sg`

  
Singapore  |  All locations within Singapore:  
`in:asia-southeast1-locations` | _Values:_  


  * `asia-southeast1`
  * `asia-southeast1-a`
  * `asia-southeast1-b`
  * `asia-southeast1-c`

  
Taiwan  |  All locations within Taiwan:  
`in:tw-locations` | _Groups:_  


  * `asia-east1-locations`

  
_Values:_  


  * `tw`

  
Taiwan  |  All locations within Taiwan:  
`in:asia-east1-locations` | _Values:_  


  * `asia-east1`
  * `asia-east1-a`
  * `asia-east1-b`
  * `asia-east1-c`

  
Australia  |  All locations within Australia:  
`in:australia-locations` | _Groups:_  


  * `australia-southeast1-locations`
  * `australia-southeast2-locations`

  
_Values:_  


  * `au`

  
Sydney  |  All locations within Sydney:  
`in:australia-southeast1-locations` | _Values:_  


  * `australia-southeast1`
  * `australia-southeast1-a`
  * `australia-southeast1-b`
  * `australia-southeast1-c`

  
Melbourne  |  All locations within Melbourne:  
`in:australia-southeast2-locations` | _Values:_  


  * `australia-southeast2`
  * `australia-southeast2-a`
  * `australia-southeast2-b`
  * `australia-southeast2-c`

  
AWS  |  All AWS locations:  
`in:aws-locations` | _Values:_  


  * `aws-ap-northeast-2`
  * `aws-ap-southeast-2`
  * `aws-eu-central-1`
  * `aws-us-east-1`

  
Azure  |  All Azure locations:  
`in:azure-locations` | _Values:_  


  * `azure-eastus2`
  * `azure-westus2`

  
European Union  |  All locations within European Union:  
`in:eu-locations` | _Groups:_  


  * `de-locations`
  * `europe-central2-locations`
  * `europe-north1-locations`
  * `europe-north2-locations`
  * `europe-southwest1-locations`
  * `europe-west1-locations`
  * `europe-west4-locations`
  * `europe-west9-locations`
  * `it-locations`

  
_Values:_  


  * `EU`
  * `eu`
  * `eur3`
  * `eur4`
  * `eur8`
  * `europe-west`

  
Germany  |  All locations within Germany:  
`in:de-locations` | _Groups:_  


  * `europe-west10-locations`
  * `europe-west3-locations`

  
_Values:_  


  * `de`

  
Berlin  |  All locations within Berlin:  
`in:europe-west10-locations` | _Values:_  


  * `europe-west10`
  * `europe-west10-a`
  * `europe-west10-b`
  * `europe-west10-c`

  
Frankfurt  |  All locations within Frankfurt:  
`in:europe-west3-locations` | _Values:_  


  * `europe-west3`
  * `europe-west3-a`
  * `europe-west3-b`
  * `europe-west3-c`

  
Warsaw  |  All locations within Warsaw:  
`in:europe-central2-locations` | _Values:_  


  * `europe-central2`
  * `europe-central2-a`
  * `europe-central2-b`
  * `europe-central2-c`

  
Finland  |  All locations within Finland:  
`in:europe-north1-locations` | _Values:_  


  * `europe-north1`
  * `europe-north1-a`
  * `europe-north1-b`
  * `europe-north1-c`

  
Stockholm  |  All locations within Stockholm:  
`in:europe-north2-locations` | _Values:_  


  * `europe-north2`
  * `europe-north2-a`
  * `europe-north2-b`
  * `europe-north2-c`

  
Madrid  |  All locations within Madrid:  
`in:europe-southwest1-locations` | _Values:_  


  * `europe-southwest1`
  * `europe-southwest1-a`
  * `europe-southwest1-b`
  * `europe-southwest1-c`

  
Belgium  |  All locations within Belgium:  
`in:europe-west1-locations` | _Values:_  


  * `europe-west1`
  * `europe-west1-b`
  * `europe-west1-c`
  * `europe-west1-d`

  
Netherlands  |  All locations within Netherlands:  
`in:europe-west4-locations` | _Values:_  


  * `europe-west4`
  * `europe-west4-a`
  * `europe-west4-b`
  * `europe-west4-c`

  
Paris  |  All locations within Paris:  
`in:europe-west9-locations` | _Values:_  


  * `europe-west9`
  * `europe-west9-a`
  * `europe-west9-b`
  * `europe-west9-c`

  
Italy  |  All locations within Italy:  
`in:it-locations` | _Groups:_  


  * `europe-west12-locations`
  * `europe-west8-locations`

  
_Values:_  


  * `it`

  
Turin  |  All locations within Turin:  
`in:europe-west12-locations` | _Values:_  


  * `europe-west12`
  * `europe-west12-a`
  * `europe-west12-b`
  * `europe-west12-c`

  
Milan  |  All locations within Milan:  
`in:europe-west8-locations` | _Values:_  


  * `europe-west8`
  * `europe-west8-a`
  * `europe-west8-b`
  * `europe-west8-c`

  
Europe  |  All locations within Europe:  
`in:europe-locations` | _Groups:_  


  * `ch-locations`
  * `de-locations`
  * `europe-central2-locations`
  * `europe-north1-locations`
  * `europe-north2-locations`
  * `europe-southwest1-locations`
  * `europe-west1-locations`
  * `europe-west4-locations`
  * `europe-west9-locations`
  * `gb-locations`
  * `it-locations`

  
_Values:_  


  * `EU`
  * `eu`
  * `eur3`
  * `eur4`
  * `eur5`
  * `eur7`
  * `eur8`
  * `europe`
  * `europe-west`

  
Switzerland  |  All locations within Switzerland:  
`in:ch-locations` | _Groups:_  


  * `europe-west6-locations`

  
_Values:_  


  * `ch`

  
Zurich  |  All locations within Zurich:  
`in:europe-west6-locations` | _Values:_  


  * `europe-west6`
  * `europe-west6-a`
  * `europe-west6-b`
  * `europe-west6-c`

  
United Kingdom  |  All locations within United Kingdom:  
`in:gb-locations` | _Groups:_  


  * `europe-west2-locations`

  
_Values:_  


  * `gb`

  
London  |  All locations within London:  
`in:europe-west2-locations` | _Values:_  


  * `europe-west2`
  * `europe-west2-a`
  * `europe-west2-b`
  * `europe-west2-c`

  
Low carbon locations  |  All locations with low carbon impact:  
`in:low-carbon-locations` | _Groups:_  


  * `canada-low-carbon-locations`
  * `eu-low-carbon-locations`
  * `europe-low-carbon-locations`
  * `northamerica-low-carbon-locations`
  * `southamerica-low-carbon-locations`
  * `us-low-carbon-locations`

  
Low carbon Canada  |  All locations within Canada with low carbon impact:  
`in:canada-low-carbon-locations` | _Groups:_  


  * `northamerica-northeast1-locations`
  * `northamerica-northeast2-locations`

  
Montréal  |  All locations within Montréal:  
`in:northamerica-northeast1-locations` | _Values:_  


  * `northamerica-northeast1`
  * `northamerica-northeast1-a`
  * `northamerica-northeast1-b`
  * `northamerica-northeast1-c`

  
Toronto  |  All locations within Toronto:  
`in:northamerica-northeast2-locations` | _Values:_  


  * `northamerica-northeast2`
  * `northamerica-northeast2-a`
  * `northamerica-northeast2-b`
  * `northamerica-northeast2-c`

  
Low carbon European Union  |  All locations within European Union with low carbon impact:  
`in:eu-low-carbon-locations` | _Groups:_  


  * `europe-north1-locations`
  * `europe-southwest1-locations`
  * `europe-west1-locations`
  * `europe-west9-locations`

  
Low carbon Europe  |  All locations within Europe with low carbon impact:  
`in:europe-low-carbon-locations` | _Groups:_  


  * `europe-north1-locations`
  * `europe-southwest1-locations`
  * `europe-west1-locations`
  * `europe-west6-locations`
  * `europe-west9-locations`

  
Low carbon North America  |  All locations within North America with low carbon impact:  
`in:northamerica-low-carbon-locations` | _Groups:_  


  * `northamerica-northeast1-locations`
  * `northamerica-northeast2-locations`
  * `us-central1-locations`
  * `us-west1-locations`

  
Iowa  |  All locations within Iowa:  
`in:us-central1-locations` | _Values:_  


  * `us-central1`
  * `us-central1-a`
  * `us-central1-b`
  * `us-central1-c`
  * `us-central1-f`

  
Oregon  |  All locations within Oregon:  
`in:us-west1-locations` | _Values:_  


  * `us-west1`
  * `us-west1-a`
  * `us-west1-b`
  * `us-west1-c`

  
Low carbon South America  |  All locations within South America with low carbon impact:  
`in:southamerica-low-carbon-locations` | _Groups:_  


  * `southamerica-east1-locations`

  
São Paulo  |  All locations within São Paulo:  
`in:southamerica-east1-locations` | _Values:_  


  * `southamerica-east1`
  * `southamerica-east1-a`
  * `southamerica-east1-b`
  * `southamerica-east1-c`

  
Low carbon United States  |  All locations within United States with low carbon impact:  
`in:us-low-carbon-locations` | _Groups:_  


  * `us-central1-locations`
  * `us-west1-locations`

  
North America  |  All locations within North America:  
`in:northamerica-locations` | _Groups:_  


  * `canada-locations`
  * `northamerica-south1-locations`
  * `us-locations`

  
_Values:_  


  * `nam14`

  
Canada  |  All locations within Canada.  
`in:canada-locations` | _Groups:_  


  * `northamerica-northeast1-locations`
  * `northamerica-northeast2-locations`

  
_Values:_  


  * `ca`

  
Mexico  |  All locations within Mexico:  
`in:northamerica-south1-locations` | _Values:_  


  * `northamerica-south1`
  * `northamerica-south1-a`
  * `northamerica-south1-b`
  * `northamerica-south1-c`

  
United States  |  All locations within the United States:  
`in:us-locations` | _Groups:_  


  * `us-central1-locations`
  * `us-central2-locations`
  * `us-east1-locations`
  * `us-east4-locations`
  * `us-east5-locations`
  * `us-south1-locations`
  * `us-west1-locations`
  * `us-west2-locations`
  * `us-west3-locations`
  * `us-west4-locations`

  
_Values:_  


  * `US`
  * `aws-us-east-1`
  * `azure-eastus2`
  * `nam10`
  * `nam11`
  * `nam12`
  * `nam13`
  * `nam15`
  * `nam3`
  * `nam4`
  * `nam5`
  * `nam6`
  * `nam7`
  * `nam8`
  * `nam9`
  * `us`
  * `us-central`

  
Oklahoma  |  All locations within Oklahoma:  
`in:us-central2-locations` | _Values:_  


  * `us-central2`
  * `us-central2-a`
  * `us-central2-b`
  * `us-central2-c`
  * `us-central2-d`

  
South Carolina  |  All zones within South Carolina:  
`in:us-east1-locations` | _Values:_  


  * `us-east1`
  * `us-east1-a`
  * `us-east1-b`
  * `us-east1-c`
  * `us-east1-d`

  
Northern Virginia  |  All locations within Northern Virginia:  
`in:us-east4-locations` | _Values:_  


  * `us-east4`
  * `us-east4-a`
  * `us-east4-b`
  * `us-east4-c`

  
Columbus  |  All locations within Columbus:  
`in:us-east5-locations` | _Values:_  


  * `us-east5`
  * `us-east5-a`
  * `us-east5-b`
  * `us-east5-c`

  
Dallas  |  All locations within Dallas:  
`in:us-south1-locations` | _Values:_  


  * `us-south1`
  * `us-south1-a`
  * `us-south1-b`
  * `us-south1-c`

  
Los Angeles  |  All locations within Los Angeles:  
`in:us-west2-locations` | _Values:_  


  * `us-west2`
  * `us-west2-a`
  * `us-west2-b`
  * `us-west2-c`

  
Salt Lake City  |  All locations within Salt Lake City:  
`in:us-west3-locations` | _Values:_  


  * `us-west3`
  * `us-west3-a`
  * `us-west3-b`
  * `us-west3-c`

  
Las Vegas  |  All locations within Las Vegas:  
`in:us-west4-locations` | _Values:_  


  * `us-west4`
  * `us-west4-a`
  * `us-west4-b`
  * `us-west4-c`

  
South America  |  All locations within South America:  
`in:southamerica-locations` | _Groups:_  


  * `br-locations`
  * `cl-locations`

  
Brazil  |  All locations within Brazil:  
`in:br-locations` | _Groups:_  


  * `southamerica-east1-locations`

  
_Values:_  


  * `br`

  
Chile  |  All locations within Chile:  
`in:cl-locations` | _Groups:_  


  * `southamerica-west1-locations`

  
_Values:_  


  * `cl`

  
Santiago  |  All locations within Santiago:  
`in:southamerica-west1-locations` | _Values:_  


  * `southamerica-west1`
  * `southamerica-west1-a`
  * `southamerica-west1-b`
  * `southamerica-west1-c`

  
Thailand  |  All locations within Thailand:  
`in:th-locations` | _Groups:_  


  * `asia-southeast3-locations`

  
_Values:_  


  * `th`

  
Bangkok  |  All locations within Bangkok:  
`in:asia-southeast3-locations` | _Values:_  


  * `asia-southeast3`
  * `asia-southeast3-a`
  * `asia-southeast3-b`
  * `asia-southeast3-c`

  
  
## Authentication

Organization Policy Service uses [OAuth 2.0](http://tools.ietf.org/html/rfc6749) for API authentication and authorization. To get an OAuth 2.0 bearer token:

  1. Go to the [OAuth 2.0 Playground page](https://developers.google.com/oauthplayground/).

  2. In the **Step 1** list of scopes, select the **Cloud Resource Manager API v2** > **https://www.googleapis.com/auth/cloud-platform** , and then click **Authorize APIs**.

  3. On the **Sign in with Google** page that appears, select your account and sign in.

  4. To provide access to **Google OAuth 2.0 Playground** , click **Allow** on the prompt that appears.

  5. In **Step 2** , click **Exchange authorization code for tokens**.

  6. At the bottom of the **Request / Response** pane on the right, your access token string is displayed:
         
         {
           "access_token": "ACCESS_TOKEN",
           "token_type": "Bearer",
           "expires_in": 3600
         }
         

Where ACCESS_TOKEN is the OAuth 2.0 bearer token string that you can use for API authorization.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
