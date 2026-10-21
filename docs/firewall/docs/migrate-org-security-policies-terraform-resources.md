---
url: https://docs.cloud.google.com/firewall/docs/migrate-org-security-policies-terraform-resources/
title: Migrate Terraform resources from organizationSecurityPolicies to firewallPolicies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:32.000816+00:00
---

# Migrate Terraform resources from organizationSecurityPolicies to firewallPolicies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/migrate-org-security-policies-terraform-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Migrate Terraform resources from organizationSecurityPolicies to firewallPolicies Stay organized with collections  Save and categorize content based on your preferences. 

Google recommends using the `firewallPolicies` methods for configuring Cloud Next Generation Firewall policies. This document guides you through migrating your Terraform configurations to use [firewallPolicies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies) methods instead of [organizationSecurityPolicies](https://docs.cloud.google.com/compute/docs/reference/rest/beta/organizationSecurityPolicies) methods.

**Note:** This document shows you how to update and migrate Terraform resources only. The underlying Google Cloud resources remain unchanged.

The `firewallPolicies` methods provide organizational management options with fine-grained controls. We recommend the `firewallPolicies` methods for resource management using Terraform. This document assumes you are familiar with Terraform best practices and basic Terraform operations.

Firewall policies let you group several firewall rules that can explicitly deny or allow connections. For more information about firewall policies, see [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).

**Caution:** To maintain service continuity, don't apply any changes or perform Terraform actions during the migration process to keep the Google Cloud configuration and resources unchanged.

## Benefits of migrating to `firewallPolicies` methods

The `firewallPolicies` methods deliver a consistent firewall experience across the Google Cloud resource hierarchy and offer multiple operational benefits.

  * **Enhanced organization security** : the `firewallPolicies` methods apply organization security by using advanced Identity and Access Management (IAM) permission controls.

  * **Ease of operations** : the `firewallPolicies` methods support the use of advanced features—such as fully qualified domain name (FQDN) objects, geolocation objects, threat detection, intrusion prevention, and address groups—for operational ease and efficiency.




## How migration works

Before you begin the migration process, you need to complete the following steps, which are described in the Before you begin section:

  * Ensure that you are using version 6.16.0 or later of the Terraform provider for Google Cloud.
  * Ensure that the Terraform state matches the current configuration.
  * Identify resources that are in the scope of migration, including policies, rules, and associations.
  * Prepare commands to import the new `firewallPolicies` resources to the Terraform state either manually or by using an automated script.
  * Review the recommended backup and recovery procedures for your version of Terraform, and create a backup of your current Terraform state.



The process of reconfiguring Terraform to migrate the `organizationSecurityPolicies` resources includes these steps:

  1. **Remove existing resources from the Terraform state**. Remove existing `organizationSecurityPolicies` resources from the Terraform state.

  2. **Update the Terraform configuration**. Edit the Terraform configuration files to replace the existing resource type, names, and attributes with the new resource type, names, and attributes.

  3. **Import new resources to the Terraform state**. Import the new `firewallPolicies` resources to the Terraform state.




## Before you begin

This section explains the prerequisites for the migration process.

### Ensure that the Terraform provider is supported

We recommend using version 6.16.0 or later of the Terraform provider for Google Cloud for the migration. Earlier versions might fail to import in certain configurations, such as those with slashes in association names.

After the migration, you must use version 4.0.0 or later, which includes the following resources from the Terraform registry:

  * [google_compute_firewall_policy](https://registry.terraform.io/providers/hashicorp/google/4.0.0/docs/resources/compute_firewall_policy)
  * [google_compute_firewall_policy_association](https://registry.terraform.io/providers/hashicorp/google/4.0.0/docs/resources/compute_firewall_policy_association)
  * [google_compute_firewall_policy_rule](https://registry.terraform.io/providers/hashicorp/google/4.0.0/docs/resources/compute_firewall_policy_rule)



### Ensure that the Terraform state is up-to-date

Run the following Terraform command to check that the Terraform state matches the current configuration.
    
    
    terraform plan
    

To avoid any inconsistencies, we recommend that you apply any pending changes or actions before proceeding with the migration process.

### Identify the resources to migrate

Run the following Terraform command to generate a list of resources that are in the scope of migration, including policies, rules, and associations.
    
    
    terraform state list | grep ^google_compute_organization_security_policy
    

The output is similar to the following:
    
    
    google_compute_organization_security_policy.policy
    google_compute_organization_security_policy_association.association["folders/45678"]
    google_compute_organization_security_policy_rule.rule["allow-inbound-ssh"]
    google_compute_organization_security_policy_rule.rule["deny-all-egress"]
    

You need these resources to migrate to the `firewallPolicies` methods. Save them for later.

### Prepare import commands using an automated script

To avoid errors or missed configurations during your migration, we recommend using an automated script to generate the commands that are required for importing the `firewallPolicies` resources to the Terraform state.

Run the following Terraform script to perform these tasks:

  * Generate new resource addresses from the existing resource addresses.
  * Get resource identifiers (or resource IDs) from the existing resource addresses.
  * Generate import identifiers (or import IDs) from the resource IDs.
  * Display the import commands for all the new `firewallPolicies` resources.


    
    
    terraform state list | grep ^google_compute_organization_security_policy | while read -r resource_address; do
    # Generate the new resource address for google_compute_firewall_policy
    new_address=$(echo "$resource_address" | sed 's/google_compute_organization_security_policy/google_compute_firewall_policy/')
    
    # Get the full resource ID from terraform state and remove quotes
    resource_id=$(echo "$resource_address.id" | terraform console | tr -d '"')
    
    # Use awk to parse the resource_id and generate the correct import identifier
    import_id=$(echo "$resource_id" | awk -F'/' '
      /association/ {
        split($0, a, "/association/");
        assoc_name = a[2];
        gsub(/\//, "%2F", assoc_name);
        print $4 "/" assoc_name;
        next
      }
      /priority/ {
        print $4 "/" $6;
        next
      }
      {
        print $4
      }
    ')
    
    # Print the final import command
    echo "terraform import '$new_address' '$import_id'"
    done
    

You need the output from this script to import the resources. Save the output for later.

### Prepare import commands manually

If the automated approach isn't feasible, you can generate the commands for importing the `firewallPolicies` resources manually. You can use the `terraform console` command to get the identifiers (IDs) of the resources.

The following Terraform command displays the resource ID of the `google_compute_organization_security_policy.policy` resource:
    
    
    echo google_compute_organization_security_policy.policy.id | terraform console
    

The output is similar to the following:
    
    
    "locations/global/securityPolicies/12345"
    

Similarly, obtain the resource IDs for the other resources you identified in the Identify resources to migrate section.

Alternatively, you can use the following Terraform command to obtain the resource IDs of all the identified resources together:
    
    
    terraform state list | grep ^google_compute_organization_security_policy | while read -r line; do echo "$line".id | terraform console; done
    

The output is similar to the following:
    
    
    "locations/global/securityPolicies/12345"
    "locations/global/securityPolicies/12345/association/locations/global/securityPolicies/23456-folders/56789"
    "locations/global/securityPolicies/12345/priority/1000"
    "locations/global/securityPolicies/12345/priority/65535"
    

To import the `firewallPolicies` resources, you need their import IDs. Import IDs are made up of a numeric identifier called a policy number, an association name, and a rule priority number, as described in this section.

  * The numeric identifier after the third forward slash character (/) is the policy number, which represents the import ID for policies. The following table shows an example of a resource ID and an import ID for a policy.

Resource ID | Import ID  
---|---  
`"locations/global/securityPolicies/12345"` | `12345`  
  * The policy number along with the association name represents the import ID for associations. An association name is the part of the resource ID shown after the element `/association/`.

Replace any forward slash character (/) in the association name with `%2F` to enable the `terraform import` command to interpret the association name as a single entity. The following table shows examples of resource ID and import ID for associations.

Resource ID | Import ID  
---|---  
`"locations/global/securityPolicies/12345/association/assoc-name"` | `12345/assoc-name`  
`"locations/global/securityPolicies/12345/association/locations/global/securityPolicies/23456-folders/56789"` | `12345/locations%2Fglobal%2FsecurityPolicies%2F23456-folders%2F56789`  
  * The policy number along with the rule priority number represents the import ID for rules. The following table shows an example of a resource ID and an import ID for a rule.

Resource ID | Import ID  
---|---  
`"locations/global/securityPolicies/12345/priority/1000"` | `12345/1000`  



To import the `firewallPolicies` resources, you need their updated resource instance names. Generate the resource instance names by replacing the prefix `google_compute_organization_security_policy` with `google_compute_firewall_policy` for all the resources that you identified in the Identify resources to migrate section. The following list shows an example of the updated resource instance names:
    
    
    google_compute_firewall_policy.policy
    google_compute_firewall_policy_association.association["folders/45678"]
    google_compute_firewall_policy_rule.rule["allow-inbound-ssh"]
    google_compute_firewall_policy_rule.rule["deny-all-egress"]
    

Combine the resource instance names with the associated import IDs to obtain the `terraform import` commands. The following list shows an example of the `terraform import` commands:
    
    
    terraform import 'google_compute_firewall_policy.policy' '12345'
    terraform import 'google_compute_firewall_policy_association.association["folders/23456"]' '12345/locations%2Fglobal%2FsecurityPolicies%2F23456-folders%2F56789'
    terraform import 'google_compute_firewall_policy_rule.rule["allow-inbound-ssh"]' '12345/1000'
    terraform import 'google_compute_firewall_policy_rule.rule["deny-all-egress"]' '12345/65535'
    

Save these import commands for later reference.

### Back up the Terraform state

Before proceeding with the migration process, we recommend that you create a backup of the Terraform state. Use the following Terraform command to create a backup in the file `terraform.tfstate.backup`.
    
    
    terraform state pull > terraform.tfstate.backup
    

If you change the Terraform state in unintended ways, you can use the backup file `terraform.tfstate.backup` to restore the original Terraform state by using the following command:
    
    
    terraform state push terraform.tfstate.backup
    

**Caution:** Restoring the Terraform state replaces the entire state with the contents of the file `terraform.tfstate.backup`.

## Migrate `organizationSecurityPolicies` resources

This section explains the procedure for migrating your Terraform configurations from `organizationSecurityPolicies` methods to `firewallPolicies` methods.

### Remove existing resources from the Terraform state

To remove the `organizationSecurityPolicies` resources found in the Identify resources to migrate section from the Terraform state, run the following Terraform command.
    
    
    terraform state list | grep ^google_compute_organization_security_policy | while read -r resource; do
      terraform state rm "$resource"
    done
    

### Update the Terraform configuration

To update your Terraform configuration file, find the definitions of the resources that you found in the Identify resources to migrate section. Use the following command to find the definitions.
    
    
    grep -r google_compute_organization_security_policy .
    

For example, the Terraform configuration file defines the policy `google_compute_organization_security_policy.policy` in the following manner:
    
    
    resource "google_compute_organization_security_policy" "policy" {
      …
      }
    

Use the following table to edit the definition of an organization security policy resource to create a new hierarchical firewall policy resource.

| Existing Terraform resource | New Terraform resource  
---|---|---  
**Resource name** | [google_compute_organization_security_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_organization_security_policy) | [google_compute_firewall_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy)  
Name of field in policy | `display_name` | `short_name`  
  
Use the following table to edit the definition of an organization security policy association resource to create a new hierarchical firewall policy association resource.

| Existing Terraform resource | New Terraform resource  
---|---|---  
**Resource name** | [google_compute_organization_security_policy_association](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_organization_security_policy_association) | [google_compute_firewall_policy_association](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy_association)  
Name of field in association | `policy_id` | `firewall_policy`  
Name of field in association | `attachment_id` | `attachment_target`  
  
Use the following table to edit the definition of an organization security policy rule resource to create a new hierarchical firewall policy rule resource.

| Existing Terraform resource | New Terraform resource  
---|---|---  
**Resource name** | [google_compute_organization_security_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_organization_security_policy_rule) | [google_compute_firewall_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy_rule)  
Name of field in rule | `policy_id` (Security policy ID) | `firewall_policy`  
Name of field removed from rule | `versioned_expr` | — (field does not exist)  
Definition of `match` object: Remove `config` set and change `layer4_config` to `layer4_configs` | 
    
    
    match {
      config {
        src_ip_ranges = SRC_IP_RANGES
        dest_ip_ranges = DEST_IP_RANGES
        layer4_config {
          ip_protocol = IP_PROTOCOL
          ports = [PORT1, PORT2]
        }
        layer4_config {
          ip_protocol = IP_PROTOCOL
        }
      }
    }
      

| 
    
    
    match {
      src_ip_ranges = SRC_IP_RANGES
      dest_ip_ranges = DEST_IP_RANGES
      layer4_configs {
        ip_protocol = IP_PROTOCOL
        ports = [PORT1, PORT2]
      }
      layer4_configs {
        ip_protocol = IP_PROTOCOL
      }
    }
        
  
Name of field in rule | `layer4_config` | `layer4_configs`  
  
You can use the following Terraform command to verify whether the modified Terraform configuration is valid:
    
    
    terraform validate
    

### Import resources to the Terraform state

To import `firewallPolicies` resources to your Terraform configuration file, run the Terraform import commands that you generated in the Prepare import commands using an automated script or Prepare import commands manually section.

After you import the `firewallPolicies` resources, Terraform accesses them using the [firewallPolicies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies) methods.

## Verify your Terraform configuration and fix discrepancies

Run the following Terraform command to check for any actions.
    
    
    terraform plan
    

Because the migration doesn't change any underlying Google Cloud resources, the plan that Terraform creates must not contain any actions.

For example, in the following output obtained by running the `terraform plan` command, the Terraform actions indicate that the `name` in the resource `google_compute_firewall_policy_association` must be updated.
    
    
    Terraform will perform the following actions:
    
     # google_compute_firewall_policy_association.association["folders/23456"] must be replaced
    -/+ resource "google_compute_firewall_policy_association" "association" {
        ~ firewall_policy   = "12345" -> "locations/global/firewallPolicies/12345"
        ~ id                = "locations/global/firewallPolicies/12345/associations/locations%2Fglobal%2FsecurityPolicies%2F12345-folders%2F23456" -> (known after apply)
        ~ name              = "locations/global/securityPolicies/12345-folders/23456" -> "locations/global/firewallPolicies/12345-folders/23456" # forces replacement
        + short_name        = (known after apply)
          # (1 unchanged attribute hidden)
      }
    

In this case, you must verify and update the Terraform configuration file such that the `name` attribute is consistent with the name that is already installed.

You can configure Terraform to change the expected `name` in the resource `google_compute_firewall_policy_association` to its original value `locations/global/securityPolicies/12345-folders/23456` by replacing the `name` field in the configuration as follows:
    
    
    name = "${replace(local.policy_id, "firewallPolicies", "securityPolicies")}-${each.value}"
    

The preceding change uses the replace function to update the value of `local.policy_id` to `securityPolicies` instead of `firewallPolicies`. Because Terraform now expects `locations/global/securityPolicies/12345-folders/23456` for the `name` attribute, running `terraform plan` no longer shows Terraform action related to the `name` attribute.

**Caution:** To maintain service continuity, don't apply any changes or perform Terraform actions during the migration process to keep the Google Cloud configuration and resources unchanged.

If the `terraform plan` command doesn't indicate any changes or Terraform actions, the migration is complete.

## What's next

  * Learn more about [firewallPolicies methods](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
