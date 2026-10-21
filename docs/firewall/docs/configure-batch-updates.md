---
url: https://docs.cloud.google.com/firewall/docs/configure-batch-updates/
title: Configure batch updates to firewall policy rules \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:27.183010+00:00
---

# Configure batch updates to firewall policy rules  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/configure-batch-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Configure batch updates to firewall policy rules Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how network administrators can batch update multiple hierarchical and network firewall policy rules using YAML configuration files. The batch update process involves creating or exporting rules to a YAML file, modifying the file, and then applying the changes using the Google Cloud CLI or Compute Engine API.

If you are using REST APIs to batch update the firewall policy rules, use the `patch` method. The `patch` method lets you replace all rules in the firewall policy by providing the `rules` field in the request; you don't need to create a YAML file. When using the `patch` method, keep the default `goto_next` rules with the lowest priority.

If you are using gcloud CLI to batch update the firewall policy rules, use the following gcloud CLI commands:

  * **`export-rules`** : lets you export the firewall policy rules configuration to a YAML file. In the YAML file, you can then add, modify, and remove the firewall policy rules configuration according to your requirements.

**Note:** The `export-rules` command lets you create a YAML file, but you can also create a file manually without using this command.
  * **`import-rules`** : lets you import the modified firewall policy rules configuration file. This replaces the existing rules of the specified firewall policy.




Before you begin, review the concepts in the [Batch updates overview](https://docs.cloud.google.com/firewall/docs/batch-update-overview).

## Before you begin

To perform the batch update, ensure you have the following tools installed and configured:

  * [Google Cloud CLI](https://docs.cloud.google.com/sdk/install)
  * [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies#get)
  * If you haven't already, set up authentication. [Authentication](https://docs.cloud.google.com/compute/docs/authentication) is the process by which your identity is verified for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine as described in this section.




###  Console 

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication.

###  gcloud 

  1. After [installing](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI, [initialize it](https://docs.cloud.google.com/sdk/docs/initialize) by running the following command:
         
         gcloud init
         
         

If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).
  2. Set the [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client) in your local client.




###  REST 

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI.

After [installing](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI, [initialize it](https://docs.cloud.google.com/sdk/docs/initialize) by running the following command:
    
    
    
    gcloud init
    
    

If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation.

## Create a YAML file

You can use the `export-rules` command to export existing firewall policy rules to a YAML file. For more information, see Export firewall policy rule. The exported YAML file includes the default `goto_next` rules with the lowest priority (rules with priority greater than or equal to 2147483644), make sure that you don't modify these default `goto_next` rules.

However, if you don't want to use the `export-rules` command, you can also create a new YAML file manually to edit the rules. To create a new YAML file manually, do the following:

  1. Create a YAML file `RULES_YAML_FILE`. Replace `RULES_YAML_FILE` with a filename of your choice.

  2. Add the `rules` field to the YAML file. The `rules` field contains a list of your firewall policy rules. For a schema describing the export or import format, see `CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/beta/FirewallPolicy.yaml`. Where `CLOUDSDKROOT` is the Google Cloud CLI installation directory.

Following is an example of a YAML schema.
         
         rules:
             -action: deny
              description:
              priority: 1
              disabled: false
              enable-logging: false
              kind: compute#firewallPolicyRule
              ...
             -action: goto_next
              priority: 2
              disabled: false
              enable-logging: false
              ...
           

To modify firewall policy rules, see Modify firewall policy rules.




## Export firewall policy rule

You can initiate updates using either the gcloud CLI or the Compute Engine API.

### Export hierarchical firewall policy

Export the firewall policy rules from the hierarchical firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`)



###  gcloud 

To export rules from hierarchical firewall policy, use the [`gcloud compute firewall-policies export-rules` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules):
    
    
    gcloud compute firewall-policies export-rules FIREWALL_POLICY \
        --destination=DESTINATION \
        --organization=ORGANIZATION
    
    

Replace the following:

  * `FIREWALL_POLICY`: the short name or ID of your hierarchical firewall policy to export rules from
  * `DESTINATION`: path to a YAML file where the configuration will be exported
  * `ORGANIZATION`: organization in which the organization firewall policy is to be updated. Must be set if `FIREWALL_POLICY` is a short name



###  API 

To export the existing rules from the hierarchical firewall policy, use the [`firewallPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/get) in the Compute Engine API:
    
    
      GET https://compute.googleapis.com/compute/v1/locations/global/firewallPolicy/FIREWALL_POLICY_NAME
      

Replace the following:

  * `FIREWALL_POLICY_NAME`: the name of the firewall policy that you want to export

This request returns a [firewall policy resource definition](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies).




### Export network firewall policy

Export firewall rules from the network firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`
  * `compute.regionFirewallPolicies.get`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the resource where you want to create the policy



###  gcloud 

To export network firewall policy rules configuration to a file, use the [`gcloud compute network-firewall-policies export-rules` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/export-rules):
    
    
    gcloud compute network-firewall-policies export-rules FIREWALL_POLICY \
        --destination=RULES_YAML_FILE_PATH \
        --global | --region=REGION
    
    

Replace the following:

  * `FIREWALL_POLICY`: name of the network firewall policy to export rules from
  * `RULES_YAML_FILE_PATH`: path to a YAML file where the configuration is exported
  * `REGION`: specify either `--global` if it's a global policy or `REGION` if it's a regional policy.



###  API 

To export the existing rules from the global network firewall policy, use the [`networkFirewallPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies/get) in the Compute Engine API:
    
    
      GET https://compute.googleapis.com/compute/v1/projects/PROJECT/global/firewallPolicies/FIREWALL_POLICY_NAME
       

Replace the following:

  * `PROJECT`: the ID of your project
  * `FIREWALL_POLICY_NAME`: the name of the firewall policy that you want to export



To export the existing rules from the regional network firewall policy, use the [`regionNetworkFirewallPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/get) in the Compute Engine API:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/firewallPolicies/FIREWALL_POLICY_NAME
    

Replace the following:

  * `PROJECT`: the ID of your project
  * `REGION`: the region of the firewall policy rules
  * `FIREWALL_POLICY_NAME`: the name of the firewall policy that you want to export



This request returns a [firewall policy resource definition](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies).

## Modify firewall policy rules

Modify the firewall policy rules that you exported in the preceding section.

  1. Open the exported file. For example, `RULES_YAML_FILE`.

  2. Add the `rules` field as shown in the following example.
         
         rules:
              -action: allow
               description: test-rule1
               direction: INGRESS
               disabled: false
               enableLogging: false
               kind: compute#firewallPolicyRule
           

  3. Add the additional configuration fields such as `action`, `direction`, and `priority`. Following is an example of a basic YAML file.
         
         rules:
              -action: allow
               description: test-rule1
               direction: INGRESS
               disabled: false
               enableLogging: false
               kind: compute#firewallPolicyRule
               match:
                 layer4Configs:
                 -ipProtocol: all
                 srcIpRanges:
                 -192.0.2.0/24
               priority: 1
               ruleTupleCount: 2
              -action: goto_next
               description: default egress rule
               direction: EGRESS
               enableLogging: false
               kind: compute#firewallPolicyRule
               match:
                 destIpRanges:
                 -::/0
                 layer4Configs:
                 -ipProtocol: all
               priority: 2147483644
               ruleTupleCount: 2
              -action: goto_next
               description: default ingress rule
               direction: INGRESS
               enableLogging: false
               kind: compute#firewallPolicyRule
               match:
                 layer4Configs:
                 -ipProtocol: all
                 srcIpRanges:
                 -::/0
               priority: 2147483645
               ruleTupleCount: 2
              -action: goto_next
               description: default egress rule
               direction: EGRESS
               enableLogging: false
               kind: compute#firewallPolicyRule
               match:
                 destIpRanges:
                 -198.51.100.0/24
                 layer4Configs:
                 -ipProtocol: all
               priority: 2147483646
               ruleTupleCount: 2
              -action: goto_next
               description: default ingress rule
               direction: INGRESS
               enableLogging: false
               kind: compute#firewallPolicyRule
               match:
                 layer4Configs:
                 -ipProtocol: all
                 srcIpRanges:
                 -192.0.2.0/24
               priority: 2147483647
               ruleTupleCount: 2
           




## Import firewall policy rules

Import the rules into your firewall policy after changing the file with your required batch updates. Importing the modified file replaces the existing firewall policy rules with the provided rules.

### Import hierarchical firewall policy rules

Import firewall rules to the hierarchical firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`)



###  gcloud 

To import rules to the hierarchical firewall policy, use the [`gcloud compute firewall-policies import-rules` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/import-rules):
    
    
    gcloud compute firewall-policies import-rules FIREWALL_POLICY \
        --source=RULES_YAML_FILE_PATH \
        --organization=ORGANIZATION
    
    

Replace the following:

  * `FIREWALL_POLICY`: the short name or ID of your hierarchical firewall policy to update
  * `RULES_YAML_FILE_PATH`: path to the YAML file from which to import rules
  * `ORGANIZATION`: organization in which the organization firewall policy is to be updated. Must be set if `FIREWALL_POLICY` is a short name.



###  API 

To import the firewall policy rules, use the [`firewallPolicies.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patch) in the Compute Engine API:
    
    
      PATCH https://compute.googleapis.com/compute/v1/locations/global/firewallPolicy/FIREWALL_POLICY_NAME
      

Replace the following:

  * `FIREWALL_POLICY_NAME`: the name of the firewall policy that you want to export

This request returns a [firewall policy resource definition](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies).




### Import network firewall policy

Import the modified firewall rules YAML file to the network firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`
  * `compute.regionFirewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`)



###  gcloud 

To import rules to the network firewall policy, use the [`gcloud compute network-firewall-policies import-rules` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/import-rules):
    
    
    gcloud compute network-firewall-policies import-rules FIREWALL_POLICY \
        --source=RULES_YAML_FILE_PATH \
        --global | --region=REGION
    

Replace the following:

  * `FIREWALL_POLICY`: name of your network firewall policy to update
  * `RULES_YAML_FILE_PATH`: the chosen path for importing the rules
  * `REGION`: specify either `--global` if it's a global policy or`REGION` if it's a regional policy.



###  API 

To import the modified network firewall policy rules, use the [`networkFirewallPolicies.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies/patch) in the Compute Engine API:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/global/firewallPolicy/FIREWALL_POLICY_NAME
      

Replace the following:

  * `PROJECT`: the project ID of the network firewall policy rules
  * `FIREWALL_POLICY_NAME`: the name of the network firewall policy that you want to export



To import the modified regional network firewall policy rules, use the [`regionNetworkFirewallPolicies.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/patch) in the Compute Engine API:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/firewallPolicies/FIREWALL_POLICY_NAME
       

Replace the following:

  * `PROJECT`: the project ID of the regional network firewall policy rules
  * `REGION`: the region of the firewall policy rules
  * `FIREWALL_POLICY_NAME`: the name of the firewall policy that you want to export

This request returns a [network firewall policy resource definition](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies).




## What's next

  * For an introduction to firewall rules, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * For an overview of batch update to firewall policy rules, see [Overview](https://docs.cloud.google.com/firewall/docs/batch-update-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
