---
url: https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints/
title: Organization policy constraints for Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:59.646556+00:00
---

# Organization policy constraints for Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Organization policy constraints for Cloud Load Balancing Stay organized with collections  Save and categorize content based on your preferences. 

Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#required-roles), you can define an organization policy, which is a set of restrictions called constraints that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

This page provides supplemental information about [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) constraints that apply to Cloud Load Balancing. You use organization policy constraints to enforce settings across an entire project, folder, or organization.

Organization policies only apply to new resources. Constraints are not enforced retroactively. If you have pre-existing load-balancing resources that are in [violation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#violations) of a new organization policy, you will need to address such violations manually.

For a complete list of available constraints, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Restrict load balancer types

Use an organization policy to restrict the Cloud Load Balancing types that can be created in your organization. Set the following organization policy constraint:

  * **Name:** Restrict Load Balancer Creation Based on Load Balancer Types
  * **ID:** `constraints/compute.restrictLoadBalancerCreationForTypes`



When you set the `compute.restrictLoadBalancerCreationForTypes` constraint, you specify an allowlist or denylist of the Cloud Load Balancing types. The list of allowed or denied values can only include values from the following list:

  * Application Load Balancers

    * `GLOBAL_EXTERNAL_MANAGED_HTTP_HTTPS` for the global external Application Load Balancer
    * `EXTERNAL_HTTP_HTTPS` for the classic Application Load Balancer
    * `GLOBAL_INTERNAL_MANAGED_HTTP_HTTPS` for the cross-region internal Application Load Balancer
    * `EXTERNAL_MANAGED_HTTP_HTTPS` for the regional external Application Load Balancer
    * `INTERNAL_HTTP_HTTPS` for the regional internal Application Load Balancer
  * Proxy Network Load Balancers

    * `GLOBAL_EXTERNAL_MANAGED_TCP_PROXY` for the global external proxy Network Load Balancer with a TCP proxy
    * `GLOBAL_EXTERNAL_MANAGED_SSL_PROXY` for the global external proxy Network Load Balancer with an SSL proxy
    * `EXTERNAL_TCP_PROXY` for the classic proxy Network Load Balancer with a TCP proxy
    * `EXTERNAL_SSL_PROXY` for the classic proxy Network Load Balancer with an SSL proxy
    * `GLOBAL_INTERNAL_MANAGED_TCP_PROXY` for the cross-region internal proxy Network Load Balancer with a TCP proxy
    * `REGIONAL_EXTERNAL_MANAGED_TCP_PROXY` for the regional external proxy Network Load Balancer with a TCP proxy
    * `REGIONAL_INTERNAL_MANAGED_TCP_PROXY` for the regional internal proxy Network Load Balancer with a TCP proxy
  * Passthrough Network Load Balancers

    * `EXTERNAL_NETWORK_TCP_UDP` for the regional external passthrough Network Load Balancer
    * `INTERNAL_TCP_UDP` for the internal passthrough Network Load Balancer



To include all internal or all external load balancer types, use the `in:` prefix followed by `INTERNAL` or `EXTERNAL`. For example, allowing `in:INTERNAL` allows all internal load balancers from the preceding list.

For sample instructions about how to use this constraint, see Set up list constraints with organization policies. 

After you set the policy, the policy is enforced when adding the respective Google Cloud [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts). The constraint is not enforced on existing Cloud Load Balancing configurations.

If you attempt to create a load balancer of a type that violates the constraint, the attempt fails and an error message is generated. The error message has the following format:
    
    
    Constraint constraints/compute.restrictLoadBalancerCreationForTypes
    violated for projects/PROJECT_NAME. Forwarding Rule projects/PROJECT_NAME/region/REGION/forwardingRules/FORWARDING_RULE_NAME
    of type SCHEME is not allowed.
    

If you set multiple `restrictLoadBalancerCreationForTypes` constraints at different resource levels, they are [enforced hierarchically](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#hierarchy_evaluation_rules). For this reason, we recommended that you set the `inheritFromParent` field to `true`, which ensures that policies at higher layers are also considered.

### GKE error messages

If you are using Google Kubernetes Engine (GKE), and someone in your organization has created an organization policy that limits which types of load balancers can be created, then you'll see an error message similar to the following:
    
    
    Warning  Sync    28s   loadbalancer-controller  Error during sync: error running
    load balancer syncing routine: loadbalancer FORWARDING_RULE_NAME
    does not exist: googleapi: Error 412:
    Constraint constraints/compute.restrictLoadBalancerCreationForTypes violated for
    projects/PROJECT_ID. Forwarding Rule
    projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_NAME
    of type LOAD_BALANCER_TYPE is not allowed, conditionNotMet
    

Depending on the policy, this might limit your ability to create new load balancer resources such as [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), [Ingresses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress), or [Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api). Contact your organization policy administrators to help you understand which restrictions are in place.

You can view GKE error messages by running the following commands:
    
    
    kubectl get events -w
    
    
    
    kubectl describe RESOURCE_KIND NAME
    

Replace the following:

  * `RESOURCE_KIND`: the kind of load balancer, `ingress` or `service`
  * `NAME`: the name of the load balancer



## Disable global load balancing

This legacy managed constraint disables creation of [global load-balancing products](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). When enforced, only regional load-balancing products without global dependencies can be created.

  * **Name:** Disable Global Load Balancing
  * **ID:** `constraints/compute.disableGlobalLoadBalancing`



By default, users are allowed to create global load-balancing products.

For sample instructions about how to use this constraint, see Set up boolean constraints with organization policies. 

## Restrict the types of protocol forwarding deployments

Use an [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to restrict the types of protocol forwarding deployments (internal or external) that can be created in your organization. Set the following organization policy constraint:

  * **Name:** Restrict Protocol Forwarding Based on type of IP Address
  * **ID:** `constraints/compute.managed.restrictProtocolForwardingCreationForTypes`



To configure the `compute.managed.restrictProtocolForwardingCreationForTypes` constraint, you specify an allowlist or denylist of the type of protocol forwarding deployment to be allowed or denied. The list of allowed or denied values can only include the following values:

  * `INTERNAL`
  * `EXTERNAL`



By default, newly created organizations have this policy configured to allow only `INTERNAL` protocol forwarding. That is, any forwarding rules associated with target instances are limited to using internal IP addresses only. If you want to use protocol forwarding with external IP addresses, or, if you want to prohibit users from using protocol forwarding with internal IP addresses, then you need to update this organization policy.

After you update the policy, the changes are enforced when you create any new forwarding rules associated with target instances. The constraint is not enforced retroactively on existing protocol forwarding configurations.

For sample instructions about how to use this constraint, see Set up list constraints with organization policies. 

If you attempt to create a protocol forwarding deployment of a type that violates the constraint, the attempt fails and an error message is generated. The error message has the following format:
    
    
    Constraint constraints/compute.managed.restrictProtocolForwardingCreationForTypes
    violated for projects/PROJECT_NAME. Forwarding Rule
    projects/PROJECT_NAME/region/REGION/forwardingRules/FORWARDING_RULE_NAME
    of type SCHEME is not allowed.
    

If you set multiple `compute.managed.restrictProtocolForwardingCreationForTypes` constraints at different resource levels, and if you set the `inheritFromParent` field to `true`, then the constraints are enforced hierarchically.

## Enforce Shared VPC restrictions

Use the following organization policies to restrict how users are allowed to set up Shared VPC deployments.

### Restrict Shared VPC host projects

This legacy managed constraint lets you restrict the Shared VPC host projects that a resource can attach to.

  * **Name:** Restrict Shared VPC host projects
  * **ID:** `constraints/compute.restrictSharedVpcHostProjects`



By default, a project can attach to any host project in the same organization, thereby becoming a service project. When you set the `compute.restrictSharedVpcHostProjects` constraint, you specify an allowlist or denylist of host projects in the following ways:

  * Specify a project in the following format: 
    * `projects/PROJECT_ID`
  * Specify a project, folder, or organization. The constraint applies to all projects under the specified resource in the resource hierarchy. Use the following format: 
    * `under:organizations/ORGANIZATION_ID`
    * `under:folders/FOLDER_ID`



For sample instructions about how to use this constraint, see Set up list constraints with organization policies. 

### Restrict Shared VPC subnetworks

This legacy managed constraint defines the set of Shared VPC subnets that eligible resources can use. This constraint does not apply to resources within the same project.

  * **Name:** Restrict Shared VPC subnetworks
  * **ID:** `constraints/compute.restrictSharedVpcSubnetworks`



By default, eligible resources can use any Shared VPC subnet. When you set the `compute.restrictSharedVpcSubnetworks` constraint, you specify a restricted list of subnets in the following ways:

  * Specify a subnet in the following format: 
    * `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME`
  * Specify a project, folder, or organization. The constraint applies to all subnets under the specified resource in the resource hierarchy. Use the following format: 
    * `under:organizations/ORGANIZATION_ID`
    * `under:folders/FOLDER_ID`
    * `under:projects/PROJECT_ID`



For sample instructions about how to use this constraint, see Set up list constraints with organization policies. 

### Restrict cross-project backend buckets and backend services

You can use this constraint to limit the backend services and backend buckets that a URL map can reference. This constraint does not apply to backend services and backend buckets within the same project as the URL map.

  * **Name:** Restrict cross-project backend buckets and backend services
  * **ID:** `constraints/compute.restrictCrossProjectServices`



By default, a URL map in one project can reference compatible backend services and backend buckets from other projects in the same organization as long as the user performing the action has the `compute.backendServices.use`, `compute.regionBackendServices.use`, or `compute.backendBuckets.use` permission.

To configure the `restrictCrossProjectServices` constraint, you can specify an allowlist or denylist of backend services or backend buckets in the following ways:

  * Specify backend services in the following format: 
    * `projects/PROJECT_ID/regions/REGION/backendservices/BACKEND_SERVICE_NAME`
    * `projects/PROJECT_ID/global/backendservices/BACKEND_SERVICE_NAME`
  * Specify backend buckets in the following format:

    * `projects/PROJECT_ID/regions/REGION/backendbuckets/BACKEND_BUCKET_NAME`
    * `projects/PROJECT_ID/global/backendbuckets/BACKEND_BUCKET_NAME`
  * Specify a project, folder, or organization. The constraint applies to all backend services and backend buckets under the specified resource in the resource hierarchy. Use the following format:

    * `under:organizations/ORGANIZATION_ID`
    * `under:folders/FOLDER_ID`
    * `under:projects/PROJECT_ID`



After you set up an organization policy with this constraint, the constraint goes into effect the next time you use the `gcloud compute url-maps` command to attach a backend service or a backend bucket to a URL map. The constraint does not retroactively affect existing references to any cross-project backend services or backend buckets.

This constraint applies to all deployment types, Shared VPC included. To avoid conflicts, we recommend not using both this constraint and the `compute.restrictSharedVpcBackendServices` constraint described in the next section.

For sample instructions about how to use this constraint, see Set up list constraints with organization policies. 

### Restrict Shared VPC backend services

You can use this constraint to limit the backend services that a URL map can reference in Shared VPC deployments that use [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project). This constraint does not apply to backend services within the same project as the URL map.

  * **Name:** Restrict Shared VPC backend services
  * **ID:** `constraints/compute.restrictSharedVpcBackendServices`



We recommend using the `compute.restrictCrossProjectServices` constraint documented in the previous section instead. The `compute.restrictCrossProjectServices` constraint applies to all deployment types, Shared VPC or otherwise, and applies to both backend buckets and backend services.

### Restrict Shared VPC project lien removal

This legacy managed constraint restricts the set of users that can remove a Shared VPC host project lien without organization-level permission where this constraint is already set to `True`.

  * **Name:** Restrict Shared VPC project lien removal
  * **ID:** `constraints/compute.restrictXpnProjectLienRemoval`



By default, any user with the permission to update liens can remove a Shared VPC host project lien. Enforcing this constraint requires that permission be granted at the organization level.

For sample instructions about how to use this constraint, see Set up boolean constraints with organization policies. 

## Restrict TLS capabilities with custom constraints

To meet your compliance requirements and restrict certain Transport Layer Security (TLS) capabilities, you can create the following organization policy constraint and use it along with [custom constraints for SSL policy resources](https://docs.cloud.google.com/compute/docs/access/custom-constraints#example-restrict-tls-capabilities):

  * Name: Require SSL policy
  * ID: `constraints/compute.requireSslPolicy`



By using the `compute.requireSslPolicy` constraint along with your own [custom constraints for SSL policy fields](https://docs.cloud.google.com/load-balancing/docs/custom-constraints#example-restrict-tls-capabilities), you can create restrictions tailored to your deployments. For example, you can do the following:

  * Improve security and meet compliance requirements by restricting the use of earlier TLS versions (such as 1.0 and 1.1) and cipher suites.
  * Improve performance by reducing the number of required handshakes and by improving the compatibility of the load balancer with clients.
  * Apply a restriction to a specific resource node and its children. For example, if you deny TLS version 1.0 for an organization, it is also denied for all folders and projects (children) that descend from that organization.



To enforce an SSL policy for an Application Load Balancer or a proxy Network Load Balancer, you must [attach it to the load balancer's target HTTPS proxy or target SSL proxy](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#attach-policy).

To update existing SSL policies, see [Manage SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#update-ssl-policies-target-proxies).

## Use boolean rules in organization policies

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * [Organization Policy Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`). For more information, see [Access control for organization resources with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).



###  Console 

To set an organization policy from the console, complete the following steps:

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/)

  2. In the **Filter** field, search for the constraint either by **Name** or by **ID**.
  3. Click the name of the constraint.
  4. Click **Edit** to edit the constraint.
  5. On the **Edit** page, select **Customize**.
  6. Under **Enforcement** , select an enforcement option: 
     * To enable enforcement of this constraint, select **On**.
     * To disable enforcement of this constraint, select **Off**.
  7. After making changes, click **Save** to apply the constraint settings.



For detailed instructions about customizing organization policies by using the Google Cloud console, see [Customizing policies for boolean constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints).

###  gcloud 

To enable enforcement of a constraint that uses boolean rules, use the [`gcloud resource-manager org-policies enable-enforce`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce) command as follows.

To enable restriction of Shared VPC project lien removal:
    
    
    gcloud resource-manager org-policies enable-enforce \
        --organization ORGANIZATION_ID \
        constraints/compute.restrictXpnProjectLienRemoval
    

To disable global load balancing:
    
    
    gcloud resource-manager org-policies enable-enforce \
        --organization ORGANIZATION_ID \
        constraints/compute.disableGlobalLoadBalancing
    

For detailed instructions about working with boolean rules in `gcloud`, see [Use boolean rules in organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint).

## Set up list rules in organization policies

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * [Organization Policy Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`). For more information, see [Access control for organization resources with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).



###  Console 

To set an organization policy from the console, complete the following steps:

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/)

  2. In the **Filter** field, search for the constraint either by **Name** or by **ID**. For example, to restrict Shared VPC host projects, you search for the ID: `constraints/compute.restrictSharedVpcHostProjects`.
  3. Click the name of the constraint.
  4. Click **Edit** to edit the constraint.
  5. To create a custom policy, select **Customize** and specify the allowlist or denylist of resources. For more detailed instructions about customizing organization policies by using the Google Cloud console, see [Customizing policies for list constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints).
  6. After making changes, click **Save** to apply the constraint settings.



###  gcloud 

This section provides a few configuration examples to show you how to create and set an organization policy with a legacy managed constraint using list rules. For more detailed instructions about working with list rules and organization policies in `gcloud`, see [Use list rules in organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#list-constraint).

  1. Create the policy file. Use the following JSON configuration samples to create your own policy file based on your requirements.

     * **Restrict load balancer types**

       * **Allow only a subset of load balancers**
             
             {
             "constraint": "constraints/compute.restrictLoadBalancerCreationForTypes",
             "listPolicy": {
               "allowedValues": [
                 "INTERNAL_TCP_UDP",
                 "EXTERNAL_NETWORK_TCP_UDP"
               ]
             }
             }
             

       * **Deny all external load balancers**
             
             {
             "constraint": "constraints/compute.restrictLoadBalancerCreationForTypes",
             "listPolicy": {
               "deniedValues": [
                 "in:EXTERNAL"
               ]
             }
             }
             

       * **Deny all load balancers**
             
             {
             "constraint": "constraints/compute.restrictLoadBalancerCreationForTypes",
             "listPolicy": {
               "allValues": "DENY"
             }
             }
             

     * **Restrict protocol forwarding types**

       * **Deny all protocol forwarding**
             
             {
             "name": "RESOURCE_TYPE/RESOURCE_ID/policies/compute.managed.restrictProtocolForwardingCreationForTypes",
             "spec": {
               "rules": [
                 {
                   "enforce": ["true"],
                   "parameters": {
                     "denyAll": "true"
                   }
                 }
               ]
             }
             }
             

       * **Allow only internal protocol forwarding**
             
             {
             "name": "RESOURCE_TYPE/RESOURCE_ID/policies/compute.managed.restrictProtocolForwardingCreationForTypes",
             "spec": {
               "rules": [
                 {
                   "enforce": ["true"],
                   "parameters": {
                     "allowedSchemes": "EXTERNAL"
                   }
                 }
               ]
             }
             }
             

     * **Restrict Shared VPC configurations**

       * **Restrict Shared VPC host projects**
             
             {
             "constraint": "constraints/compute.restrictSharedVpcHostProjects",
             "listPolicy": {
               "allowedValues": [
                 "under:folders/FOLDER_ID",
                 "under:projects/PROJECT_ID"
               ]
             }
             }
             

       * **Restrict Shared VPC subnetworks**
             
             {
             "constraint": "constraints/compute.restrictSharedVpcSubnetworks",
             "listPolicy": {
               "deniedValues": [
                 "under:organizations/ORGANIZATION_ID",
                 "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"
               ]
             }
             }
             

       * **Restrict Shared VPC backend services**
             
             {
             "constraint": "constraints/compute.restrictCrossProjectServices",
             "listPolicy": {
               "allowedValues": [
                 "under:folders/FOLDER_ID",
                 "under:projects/PROJECT_ID",
                 "projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_NAME"
               ]
             }
             }
             

  2. Apply the constraint to a resource: either an organization, folder, or project.

For organizations, run the following command:
         
         gcloud resource-manager org-policies set-policy POLICY_FILE \
             --organization=ORGANIZATION_ID
         

For folders, run the following command:
         
         gcloud resource-manager org-policies set-policy POLICY_FILE \
             --folder=FOLDER_ID
         

For projects, run the following command:
         
         gcloud resource-manager org-policies set-policy POLICY_FILE \
             --project=PROJECT_ID
         

Replace the following:

     * `POLICY_FILE`: The full path to your organization policy YAML file.
     * `ORGANIZATION_ID`: Your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * `FOLDER_ID`: Your [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
     * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).



## Set up an organization policy to apply an SSL policy to target HTTPS proxies and target SSL proxies

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * [Organization Policy Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`). For more information, see [Access control for organization resources with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).



###  Console 

To set an organization policy from the console, complete the following steps:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/)

  2. In the **Filter** field, search for the constraint either by **Name** or by **ID**.

  3. Click the name of the constraint.

  4. Click **Edit** to edit the constraint.

  5. To create a custom policy, select **Customize** and specify the allowlist or denylist of resources.

  6. After making changes, click **Save** to apply the constraint settings.




###  gcloud 

This section provides a few configuration examples that show how to create and set an organization policy file with the `compute.requireSslPolicy` constraint.

  * Create a policy file to disallow SSL policy usage.
        
        {
          "constraint": "constraints/compute.requireSslPolicy",
          "listPolicy": {
            "allValues": "DENY"
          }
        }
        

  * Create a policy file to apply an SSL policy to all target HTTPS and SSL proxies under the specified resource in the resource hierarchy:
        
        {
          "constraint": "constraints/compute.requireSslPolicy",
          "listPolicy": {
            "allowedValues": [
              "under:folders/FOLDER_ID",
              "under:projects/PROJECT_ID"
            ]
          }
        }
        

  * Apply the constraint to target HTTPS and SSL proxies: either an organization, folder, or project.

For organizations, run the following command:
        
        gcloud resource-manager org-policies set-policy PATH_TO_POLICY_FILE \
            --organization=ORGANIZATION_ID
        

For folders, run the following command:
        
        gcloud resource-manager org-policies set-policy PATH_TO_POLICY_FILE \
            --folder=FOLDER_ID
        

For projects, run the following command:
        
        gcloud resource-manager org-policies set-policy PATH_TO_POLICY_FILE \
            --project=PROJECT_ID
        

Replace the following:

    * `PATH_TO_POLICY_FILE`: the path to your policy file
    * `ORGANIZATION_ID`: your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id)
    * `FOLDER_ID`: your [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders)
    * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * To get the effective policy to verify the default behavior of the resource (organization, folder, or project), run the following commands:

For organizations:
        
        gcloud resource-manager org-policies describe compute.requireSslPolicy \
            --effective \
            --organization=ORGANIZATION_ID
        

For folders:
        
        gcloud resource-manager org-policies describe compute.requireSslPolicy \
            --effective \
            --folder=FOLDER_ID
        

For projects:
        
        gcloud resource-manager org-policies describe compute.requireSslPolicy \
            --effective \
            --project=PROJECT_ID
        

  * To delete the policy from the resource (organization, folder, or project), run the following commands:

For organizations:
        
        gcloud resource-manager org-policies delete compute.requireSslPolicy \
            --organization=ORGANIZATION_ID
        

For folders:
        
        gcloud resource-manager org-policies delete compute.requireSslPolicy \
            --folder=FOLDER_ID
        

For projects:
        
        gcloud resource-manager org-policies delete compute.requireSslPolicy \
            --project=PROJECT_ID
        




To set up custom constraints, see [Use custom constraints to restrict TLS capabilities](https://docs.cloud.google.com/load-balancing/docs/custom-constraints#example-restrict-tls-capabilities).

## What's next

  * To learn about the resource hierarchy that applies to organization policies, see [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail).
  * For an overview of organization policies and constraints, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * For instructions about working with constraints and organization policies in the Google Cloud console, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * For instructions about working with constraints and organization policies in `gcloud`, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).
  * For a complete list of available constraints, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).
  * For API methods relevant to organization policies, see the [Cloud Resource Manager API reference documentation](https://docs.cloud.google.com/resource-manager/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
