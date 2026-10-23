---
url: https://docs.cloud.google.com/armor/docs/hierarchical-policies-using/
title: Configure hierarchical security policies \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:22.811148+00:00
---

# Configure hierarchical security policies  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/hierarchical-policies-using/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Configure hierarchical security policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can configure hierarchical security policies to help protect your organization, folders, or projects. Before you configure hierarchical security policies, make sure that you're familiar with the information in the [hierarchical security policies overview](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview).

## Set up IAM permissions for hierarchical security policies

The following operations require that you have the Identity and Access Management (IAM) role [Compute Organization Security Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityPolicyAdmin) (`roles/compute.orgSecurityPolicyAdmin`) on the target resource hierarchy node, or on the policy itself if it already exists:

  * Create a new hierarchical security policy
  * Modify a hierarchical security policy by adding, updating, or deleting rules
  * Delete a hierarchical security policy



The following operations require that you have the IAM [Compute Organization Resource Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityResourceAdmin) (`roles/compute.orgSecurityResourceAdmin`) on the target resource hierarchy node, in addition to either the [Compute Organization Security Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityPolicyAdmin) (`roles/compute.orgSecurityPolicyAdmin`) or the [Compute Organization Security Policy User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityPolicyUser) (`roles/compute.orgSecurityPolicyUser`) on either the target resource hierarchy node or on the policy itself:

  * Associate a hierarchical security policy with a resource hierarchy node



Finally, see the following table for a list of miscellaneous operations that you can perform if you have any of the listed roles:

Operations | Roles  
---|---  
View all effective Google Cloud Armor rules for a backend resource | 

  * [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)
  * [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)
  * [Compute Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)

  
View effective backend resources covered by an `organizationSecurityPolicy`  
  
## Configure hierarchical security policies

The following sections explain how to create hierarchical security policies, associate them with resource hierarchy nodes, move them between nodes, delete them, and how to view all of the Cloud Armor security policy rules that apply to a protected resource.

### Create a hierarchical security policy

You create a hierarchical security policy by using the [`gcloud compute org-security-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/create). You create the hierarchical security policy under an organization or a folder using the `--organization` or `--folder` flag, along with the corresponding `ORGANIZATION_ID` or `FOLDER_ID`. Use the following examples to create hierarchical security policies, replacing `POLICY_NAME` with the name that you want to give the new security policy:

  * Create an organization-level hierarchical security policy:
        
        gcloud compute org-security-policies create \
            --organization=ORGANIZATION_ID \
            --type=CLOUD_ARMOR \
            --short-name=POLICY_NAME
        

  * Create a folder-level hierarchical security policy:
        
        gcloud compute org-security-policies create \ 
            --folder=FOLDER_ID \
            --type=CLOUD_ARMOR \
            --short-name=POLICY_NAME
        




### Associate an existing security policy with a resource hierarchy node

**Note:** If you create a hierarchical security policy in a project that isn't enrolled in Google Cloud Armor Enterprise, your project is automatically enrolled in Cloud Armor Enterprise Paygo. For more information about hierarchical security policy automatic enrollment behavior, see [hierarchical security policies](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#hierarchical).

If you have an existing security policy, you can associate it with a resource hierarchy node by using the [`gcloud compute org-security-policies associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/associations/create).

  * Associate a hierarchical security policy to an organization:
        
        gcloud compute org-security-policies associations create \
            --security-policy=POLICY_ID \
            --organization=ORGANIZATION_ID \
            --name=ASSOCIATION_NAME
        

  * Associate a hierarchical security policy to a folder:
        
        gcloud compute org-security-policies associations create \
            --security-policy=POLICY_ID \
            --folder=FOLDER_ID \
            --name=ASSOCIATION_NAME
        

  * Associate a hierarchical security policy to a project:
        
        gcloud compute org-security-policies associations create \
            --security-policy=POLICY_ID \
            --project-number=PROJECT_ID \
            --name=ASSOCIATION_NAME
        




Replace the following:

  * `POLICY_ID`: the ID of the security policy
  * `ORGANIZATION_ID`: the ID of the organization
  * `ASSOCIATION_NAME`: the name of the association
  * `FOLDER_ID`: the ID of the folder
  * `PROJECT_ID`: the ID of the project



#### Exclude projects from hierarchical security policies

In addition, you can exclude projects from your folder-level hierarchical security policies, and you can exclude both projects and folders from your organization-level hierarchical security policies:

  * You can exclude projects from a hierarchical security policy by using the [`gcloud compute org-security-policies associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/associations/create) with the `--excluded-projects` flag.

The following example command associates security policy `example-policy` with organization `10000001`, while excluding the project with the ID `2000000002`:
        
        gcloud compute org-security-policies associations create \
            --security-policy=example-policy \
            --excluded-projects="projects/2000000002" \
            --organization=10000001
        

  * You can exclude folders from an organization-level hierarchical security policy by using the [`gcloud compute org-security-policies associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/associations/create) with the `--excluded-folders` flag.

The following example command associates security policy `example-policy` with organization `10000001`, while excluding the folder with the ID `3000000003`:
        
        gcloud compute org-security-policies associations create \
            --security-policy=example-policy \
            --excluded-folders="folders/3000000003" \
            --organization=10000001
        




### Move a hierarchical security policy

You can change the parent of a hierarchical security policy by using the [`gcloud compute org-security-policies move` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/move) to move the hierarchical security policy under a different parent resource hierarchy node. You supply the source as the first flag, and the destination as the second flag. Moving a hierarchical security policy changes its ownership, not the resource that it's associated with. Only organizations and folders can own hierarchical security policies, so you can't move them under projects.

In the following example, you move a hierarchical security policy from the organization `ORGANIZATION_ID` to the folder `FOLDER_ID`:
    
    
    gcloud compute org-security-policies move policy-1 \
        --organization ORGANIZATION_ID \
        --folder FOLDER_ID
    

### Delete a hierarchical security policy

Before you can delete a hierarchical security policy, you must first delete all associations that the policy has to resource hierarchy nodes. In the following example, you use the [`gcloud compute org-security-policies associations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/associations/delete) to remove the association named `ASSOCIATION_NAME` between the hierarchical security policy with the name `POLICY_NAME` and the organization `ORGANIZATION_ID`:
    
    
    gcloud compute org-security-policies associations delete ASSOCIATION_NAME \
        --security-policy=POLICY_NAME \
        --organization=ORGANIZATION_ID
    

If this isn't the only association that the security policy has, repeat the previous step for each association. When the hierarchical security policy has no associations, you can delete it by using the [`gcloud compute org-security-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/delete), like in the following example:
    
    
    gcloud compute org-security-policies delete POLICY_NAME \
        --organization=ORGANIZATION_ID
    

### View all effective Cloud Armor rules for a protected resource

You can view all of the Cloud Armor security policy rules that apply to a protected resource by using the [`gcloud compute backend-services get-effective-security-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/get-effective-security-policies).
    
    
    gcloud compute backend-services get-effective-security-policies PROTECTED_RESOURCE
    

Replace `PROTECTED_RESOURCE` with the name of the protected resource that you want to check.

When you run the [`gcloud compute backend-services get-effective-security-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/get-effective-security-policies) on a backend service within a project that inherits a hierarchical security policy, the response might include the hierarchical security policy even if that specific backend service's type isn't supported by hierarchical security policies. For a list of supported backend configurations for hierarchical security policies, see the [hierarchical security policies overview](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview).

## Use cases

The following sections describe use cases for hierarchical security policies.

### Deny traffic from a set of IP addresses to all Application Load Balancers in your organization

You can use hierarchical security policies to manage a list of IP addresses that aren't allowed to access your entire organization network, or to deny traffic from a specific region or country. This can help you address company-specific security concerns or help you maintain compliance. The following steps show you how to create an organization-level hierarchical security policy that denies traffic from IP address range `192.0.2.0/24`:

  1. Create a hierarchical security policy called `org-level-deny-ip-policy`, attached to an organization with ID 1000000001:
         
         gcloud compute org-security-policies create \
              --organization=1000000001 \
              --type=CLOUD_ARMOR \
              --description= "this org policy denies a set of IP addresses for all resources" \
              --short-name=org-level-deny-ip-policy
         

  2. Add a rule at priority `1000` with a match condition for the IP address range `192.0.2.0/24` and a `deny` action:
         
         gcloud compute org-security-policies rules create 1000 \
              --action=deny \
              --security-policy=org-level-deny-ip-policy \
              --organization=1000000001 \
              --description "Deny traffic from 192.0.2.0/24" \
              --src-ip-ranges "192.0.2.0/24"
         

  3. Finally, associate the security policy with the organization, denying requests from the `192.0.2.0/24` IP address to all services in the organization:
         
         gcloud compute org-security-policies associations create \
              --security-policy=org-level-deny-ip-policy \
              --organization=ORGANIZATION_ID
         




### Grant a set of source IP addresses access to some projects within your organization

You can grant access to some projects within your organization to an IP address or to several IP addresses. You might want to do this if you have a trusted upstream proxy that you want to exclude from rule evaluation for only some of your projects. In the following Cloud CDN-based example, you use a folder-level hierarchical security policy to grant the IP address range `192.0.2.0/24` access to projects named `project-1`, `project-2`, and `project-3` in organization `10000001`:

  1. Use the following commands to move `project-1`, `project-2`, and `project-3` into a folder with ID `20000002`:
         
         gcloud projects move project-1 --folder=20000002
         gcloud projects move project-2 --folder=20000002
         gcloud projects move project-3 --folder=20000002
         

  2. Use the following command to create a security policy named `org-level-proxy-filtering`:
         
         gcloud compute org-security-policies create \
              --folder=20000002 \
              --type=CLOUD_ARMOR \
              --short-name=org-level-proxy-filtering
         

  3. Add a rule at priority `1000` with a match condition for the IP address range `192.0.2.0/24` and a `goto_next` rule action. If a request matches this condition, Cloud Armor stops evaluating rules within this security policy:
         
         gcloud compute org-security-policies rules create 1000 \
              --action=goto_next \
              --security-policy=org-level-proxy-filtering \
              --organization=10000001 \
              --src-ip-ranges="192.0.2.0/24"
         

  4. Optional: If you want to apply security policy rules to these projects for requests that aren't from `192.0.2.0/24` , add more rules at a priority lower than `1000`. You can perform this step later.

  5. Use the following command to associate the policy to the folder with ID `20000002`, which you moved the projects to in step 1:
         
         gcloud compute org-security-policies associations create \
              --security-policy=org-level-proxy-filtering \
              --folder=20000002
         




## What's next

  * [Add rules to a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policies#create-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
