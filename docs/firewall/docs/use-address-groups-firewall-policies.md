---
url: https://docs.cloud.google.com/firewall/docs/use-address-groups-firewall-policies/
title: Manage address groups for firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:41.309194+00:00
---

# Manage address groups for firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/use-address-groups-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage address groups for firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

To manage address groups, you must first identify the scope of the address group relevant to your requirement. The scope identifies the level at which the address group is applicable in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

If you want to use an address group in a firewall policy rule that applies to an individual project, use a project-scoped address group.

If you want to use an address group in a firewall policy rule that is applicable throughout the hierarchy on all resources in an organization or network, use an organization-scoped address group. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies)

## Project-scoped address groups

This section provides detailed information about how to manage project-scoped address groups.

### Describe an address group

To view the details of an address group, you must specify the name and location of the address group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your project.

  3. The address groups are listed in the **Address groups** section.

  4. To view the details, click the name of your address group.




###  gcloud 

To describe an address group, use the [`gcloud network-security address-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/describe):
    
    
    gcloud network-security address-groups describe NAME \
        --location LOCATION
    

### Update an address group

You cannot update the name, type, or capacity of the address group. You can only update the address group description and IP addresses.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regions.list`
  * `networksecurity.addressGroups.update`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your project.

  3. The address groups are listed in the **Address groups** section.

  4. To edit an address group, click the name of your address group.

  5. Click edit**Edit**.

  6. Modify the required fields.

  7. Click **Save**.




###  gcloud 

To update an address group, use the [`gcloud network-security address-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/update):
    
    
    gcloud network-security address-groups update NAME \
        --description DESCRIPTION \
        --location LOCATION
    

### List address groups

You can list all the address groups in a location.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.list`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your project.

  3. The address groups are listed in the **Address groups** section.




###  gcloud 

To list the address groups, use the [`gcloud network-security address-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/list):
    
    
    gcloud network-security address-groups list \
        --location LOCATION
    

### Delete an address group

You can delete an address group by specifying its name and location. However, if the address group is referenced by a firewall policy, that address group cannot be deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.delete`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your project.

  3. The address groups are listed in the **Address groups** section.

  4. Select the checkbox next to the address group that you want to delete. Make sure that the selected address group is not referenced by any firewall policy.

  5. Click delete**Delete** , and then click **Delete** again to confirm.




###  gcloud 

To delete an address group in a project, use the [`gcloud network-security address-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/delete):
    
    
    gcloud network-security address-groups delete NAME \
      --location LOCATION
    

### Find address group references

An address group is used by firewall policies. You can find the list of all the firewall policies that use a specific address group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your project.

  3. The address groups are listed in the **Address groups** section.

  4. Click the name of your address group.

  5. In the **In use by** field, the firewall policies that use this address group are listed in the following format:

`POLICY_NAME(rule priority:PRIORITY_NUMBER)`




###  gcloud 

To list all the resources that reference a project-scoped address group, use the [`gcloud network-security address-groups list-references` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/list-references):
    
    
    gcloud network-security address-groups list-references NAME \
        --location LOCATION
    

### Add items to an address group

You can add multiple items such as IP addresses or IP ranges to an address group. If the request contains items that are already part of the address groups, those items are ignored. If the request contains invalid items, the entire request fails.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regions.list`
  * `networksecurity.addressGroups.update`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

To add an item to an address group by using Google Cloud console, follow the procedure mentioned in Update an address group.

###  gcloud 

To add items to an address group, use the [`gcloud network-security address-groups add-items` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/add-items):
    
    
    gcloud network-security address-groups add-items NAME \
        --items ITEMS \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `ITEMS`: a comma-separated list of IP addresses or IP ranges in CIDR format

  * `LOCATION`: the location of the address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.




### Remove items from an address group

You can remove existing items from an address group. If any of the items in the request are invalid, the request fails. If the request contains items that are not part of the address group, those items are ignored.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regions.list`
  * `networksecurity.addressGroups.update`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

To remove an item from an address group by using Google Cloud console, follow the procedure mentioned in Update an address group.

###  gcloud 

To remove items from an address group, use the [`gcloud network-security address-groups remove-items` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/remove-items):
    
    
    gcloud network-security address-groups remove-items NAME \
        --items ITEMS \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `ITEMS`: a comma-separated list of IP addresses or IP ranges in CIDR format to be removed

  * `LOCATION`: the location of the address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.




## Organization-scoped address groups

This section provides detailed information about how to manage organization-scoped address groups.

### Describe an address group

You can view the details of a specific address group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your organization.

  3. The address groups are listed in the **Address groups** section.

  4. To view the details, click the name of your address group.




###  gcloud 

To describe an organization-scoped address group, use the [`gcloud network-security org-address-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/describe):
    
    
    gcloud network-security org-address-groups describe NAME \
        --organization ORGANIZATION \
        --location LOCATION
    

### Update an address group

You cannot update the name, type, or capacity of the address group. You can only update the address group description and IP addresses.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.update`
  * `networksecurity.locations.list`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your organization.

  3. The address groups are listed in the **Address groups** section.

  4. To edit an address group, click the name of your address group.

  5. Click edit**Edit**.

  6. Modify the required fields.

  7. Click **Save**.




###  gcloud 

To update an organization-scoped address group, use the [`gcloud network-security org-address-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/update):
    
    
    gcloud network-security org-address-groups update NAME \
        --organization ORGANIZATION \
        --description DESCRIPTION \
        --location LOCATION
    

### List address groups

You can list all the address groups in a location.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.list`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your organization.

  3. The address groups are listed in the **Address groups** section.




###  gcloud 

To list the address groups in an organization, use the [`gcloud network-security org-address-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list):
    
    
    gcloud network-security org-address-groups list \
        --organization ORGANIZATION \
        --location LOCATION
    

### Delete an address group

You can delete an address group by specifying its name, organization, and location. If the address group is referenced by a firewall policy, that address group cannot be deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.delete`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your organization.

  3. The address groups are listed in the **Address groups** section.

  4. Select the checkbox next to the address group that you want to delete. Make sure that the selected address group is not referenced by any firewall policy.

  5. Click delete**Delete** , and then click **Delete** again to confirm.




###  gcloud 

To delete an organization-scoped address group, use the [`gcloud network-security org-address-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/delete):
    
    
    gcloud network-security org-address-groups delete NAME \
      --organization ORGANIZATION \
      --location LOCATION
    

### Find address group references

An address group is used by the firewall policies. You can find the list of all the firewall policies that use a specific address group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`
  * `compute.networkUser`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your organization.

  3. The address groups are listed in the **Address groups** section.

  4. Click the name of your address group.

  5. In the **In use by** field, the firewall policies that use this address group are listed in the following format:

`POLICY_NAME(rule priority:PRIORITY_NUMBER)`




###  gcloud 

To list all the resources that reference an organization-scoped address group, use the [`gcloud network-security org-address-groups list-references` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/list-references):
    
    
    gcloud network-security org-address-groups list-references NAME \
        --organization ORGANIZATION \
        --location LOCATION
    

### Add items to an address group

You can add multiple items such as IP addresses or IP ranges to an address group. If the request contains items that are already part of the address group, such items are ignored. If the request contains invalid items, the entire request fails.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.update`
  * `networksecurity.locations.list`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

To add an item to an organization-scoped address group by using Google Cloud console, follow the procedure mentioned in Update an address group.

###  gcloud 

To add items to an organization-scoped address group, use the [`gcloud network-security org-address-groups add-items` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/add-items):
    
    
    gcloud network-security org-address-groups add-items NAME \
        --organization ORGANIZATION \
        --items ITEMS \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `ORGANIZATION`: the organization ID where the address group is created

If you use a unique URL identifier for the `name` parameter, you can omit the `organization` parameter.

  * `ITEMS`: a comma-separated list of IP addresses or IP ranges in CIDR format

  * `LOCATION`: the location of the address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.




### Remove items from an address group

You can remove existing items from an address group. If any of the items in the request are invalid, the request fails. If the request contains items that are not part of the address group, those items are ignored.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.update`
  * `networksecurity.locations.list`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

To remove an item from an organization-scoped address group by using Google Cloud console, follow the procedure mentioned in Update an address group.

###  gcloud 

To remove an item from an organization-scoped address group, use the [`gcloud network-security org-address-groups remove-items` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items):
    
    
    gcloud network-security org-address-groups remove-items NAME \
        --organization ORGANIZATION \
        --items ITEMS \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `ORGANIZATION`: the organization ID where the address group is created

If you use a unique URL identifier for the `name` parameter, you can omit the `organization` parameter.

  * `ITEMS`: a comma-separated list of IP addresses or IP ranges in CIDR format to be removed

  * `LOCATION`: the location of the address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.




## What's next

  * [Use hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks)
  * [Use global network firewall policies](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules)
  * [Use regional network firewall policies](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#rule_tasks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
