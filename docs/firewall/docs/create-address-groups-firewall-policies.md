---
url: https://docs.cloud.google.com/firewall/docs/create-address-groups-firewall-policies/
title: Create address groups for firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:09.074794+00:00
---

# Create address groups for firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/create-address-groups-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create address groups for firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

To create address groups, you must first identify the scope of the address group relevant to your requirement. The scope identifies the level at which the address group is applicable in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

If you want to use an address group in a firewall policy rule that applies to an individual project, use a project-scoped address group.

If you want to use an address group in a firewall policy rule that is applicable throughout the hierarchy on all resources in an organization or network, use an organization-scoped address group.

## Project-scoped address groups

This section provides detailed information about how to create project-scoped address groups.

Project-scoped address groups are defined at the project level, and only apply to the project where they are created. To use an address group, you must associate it to a firewall rule in a [global network firewall policy](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules) or [regional network firewall policy](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#rule_tasks). The location of the address group must be the same as the location of the firewall policy where it is used.

### Create an address group

The [container type](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification) of the project-scoped address group is always set to `projects`.

When you create an address group, you can specify the name of the address group as a string or as a unique URL identifier. The unique URL for a project-scoped address group can be constructed in the following format:
    
    
    projects/PROJECT_ID/locations/location/addressGroups/ADDRESS_GROUP_NAME
    

If you use a unique URL identifier for the address group name, the location of the address group is already included in the URL identifier. However, if you use only the address group name, you must specify the location separately. For more information about unique URL identifiers, see [Address group specifications](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification).

An address group can have IPv4 or IPv6 item types, but not both. You must also specify the maximum item capacity for an address group. After the address group is created, you cannot change the name, item type, or item capacity of the address group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regions.list`
  * `networksecurity.addressGroups.*`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your project.

  3. Click add_box**Create Address Group**.

  4. In the **Name** field, enter a name.

  5. Optional: In the **Description** field, enter a description.

  6. For **Scope** , choose **Global** or **Regional**.

If you choose **Regional** , specify the region where the address group is created.

  7. For **Type** , select **IPv4** or **IPv6**.

  8. For **Purpose** , select **Firewall**.

If you want to use the address group in both Cloud Next Generation Firewall policies and Google Cloud Armor security policies, choose **Cloud NGFW and Cloud Armor**.

For more information about this field , see [address group specification](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification).

  9. In the **Capacity** field, enter the capacity of the address group.

**Note:** After the address group capacity is set, it cannot be changed. Make sure that you set the capacity to an appropriate value based on your use case.
  10. In the **IP Addresses** field, list the IP addresses or IP ranges that you want to include in the address group. For example, `1.1.1.0/24,1.2.0.0`.

**Note:** The number of IP addresses or IP ranges cannot exceed the configured capacity.
  11. Click **Create**.




###  gcloud 

To create an address group, use the [`gcloud network-security address-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create):
    
    
    gcloud network-security address-groups create NAME \
       --type TYPE \
       --capacity CAPACITY \
       --location LOCATION \
       --description DESCRIPTION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `TYPE`: the type of address group—IPv4 or IPv6

  * `CAPACITY`: the capacity of the address group

  * `LOCATION`: the location of the address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.

  * `DESCRIPTION`: an optional description for the address group




### Clone items from another address group

You can clone items from one address group to another.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regions.list`
  * `networksecurity.addressGroups.update`
  * `networksecurity.addressGroups.get`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your project.

  3. The address groups are listed in the **Address groups** section.

  4. Click the name of your address group that you want to clone.

  5. Click **Clone**.

  6. In the **Clone address group** pane, for **Name** , enter a name.

  7. Optional: In the **Description** field, enter a description.

  8. For **Scope** , select **Global** or **Regional**.

If you choose **Regional** , specify the region where the address group is created.

  9. For **Type** , select **IPv4** or **IPv6**.

  10. For **Purpose** , select **Firewall**.

  11. In the **Capacity** field, enter the capacity of the address group.

**Note:** After the address group capacity is set, it cannot be changed. Make sure that you set the capacity to an appropriate value based on your use case.
  12. In the **IP Addresses** field, update the IP addresses or IP ranges that are cloned from the address group.

**Note:** The number of IP addresses or IP ranges cannot exceed the configured capacity.
  13. Click content_copy**Clone**.




###  gcloud 

To clone an address group by using Google Cloud CLI, follow these guidelines:

  * Both address groups must be of the same type.
  * Both address groups must be in the same region.
  * Make sure that the new address group has sufficient capacity to fit the items of the source address group that are being cloned.
  * To specify the source address group, use the following unique URL identifier format:
        
        projects/PROJECT_ID/locations/location/addressGroups/ADDRESS_GROUP_NAME
        

For more information about unique URL identifiers for address groups, see [Address group specifications](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification).




To clone items from an address group, use the [`gcloud network-security address-groups clone-items` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/address-groups/clone-items):
    
    
    gcloud network-security address-groups clone-items NAME \
        --source SOURCE_NAMED_LIST \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `SOURCE_NAMED_LIST`: a unique URL identifier of the source address group from where the items are cloned

  * `LOCATION`: the location of the destination address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.




## Organization-scoped address groups

This section provides detailed information about how to create organization-scoped address groups.

Organization-scoped address groups are defined at the organization level and apply to all the resources in the organization as specified in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). To use an address group, you must associate it to a firewall rule in a [hierarchical firewall policy](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks), a [global network firewall policy](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules), or a [regional network firewall policy](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#rule_tasks).

### Create an address group

The [container type](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification) of the organization-scoped address group is always set to `organization`.

When you create an address group, you can specify the name of the address group as a string or as a unique URL identifier. The unique URL for an organization-scoped address group can be constructed in the following format:
    
    
    organizations/ORGANIZATION_ID/locations/LOCATION/addressGroups/ADDRESS_GROUP_NAME
    
    

If you use a unique URL identifier for the address group name, the organization ID or location for the address group is already included in the URL identifier. However, if you use only the address group name, you must specify the ID of the organization and the location where you are defining the address group. For more information about unique URL identifiers, see [Address group specifications](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification).

An address group can have IPv4 or IPv6 item types, but not both. You must also specify the maximum item capacity for an address group. After the address group is created, you cannot change the name, item type, or item capacity of the address group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.*`
  * `networksecurity.locations.list`
  * `networksecurity.operations.get`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Address groups** page.

[Go to Address groups](https://console.cloud.google.com/net-security/address-groups/list)

  2. In the project selector menu, select your organization.

  3. Click add_box**Create Address Group**.

  4. In the **Name** field, enter a name.

  5. Optional: In the **Description** field, enter a description.

  6. For **Scope** , select **Global** or **Regional**.

If you choose **Regional** , specify the region where the address group is created.

  7. For **Type** , select **IPv4** or **IPv6**.

  8. For **Purpose** , select **Firewall**.

  9. In the **Capacity** field, enter the capacity of the address group.

**Note:** After the address group capacity is set, it cannot be changed. Make sure that you set the capacity to an appropriate value based on your use case.
  10. In the **IP Addresses** field, list the IP addresses or IP ranges that you want to include in the address group. For example, `1.1.1.0/24,1.2.0.0`.

**Note:** The number of IP addresses or IP ranges cannot exceed the configured capacity.
  11. Click **Create**.




###  gcloud 

To create an organization-scoped address group, use the [`gcloud network-security org-address-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/create):
    
    
    gcloud network-security org-address-groups create NAME \
       --organization ORGANIZATION \
       --type TYPE \
       --capacity CAPACITY \
       --location LOCATION \
       --description DESCRIPTION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `ORGANIZATION`: the organization ID where the address group is created

If you use a unique URL identifier for the `name` parameter, you can omit the `organization` parameter.

  * `TYPE`: the type of address group—IPv4 or IPv6

  * `CAPACITY`: the capacity of the address group

  * `LOCATION`: the location of the address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.

  * `DESCRIPTION`: an optional description for the address group




### Clone items from another address group

You can clone items from one address group to another.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networksecurity.addressGroups.update`
  * `networksecurity.addressGroups.get`
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

  4. Click the name of your address group that you want to clone.

  5. Click **Clone**.

  6. In the **Clone address group** pane, for **Name** , enter a name.

  7. Optional: In the **Description** field, enter a description.

  8. For **Scope** , select **Global** or **Regional**.

If you choose **Regional** , specify the region where the address group is created.

  9. For **Type** , select **IPv4** or **IPv6**.

  10. For **Purpose** , select **Firewall**.

  11. In the **Capacity** field, enter the capacity of the address group.

**Note:** After the address group capacity is set, it cannot be changed. Make sure that you set the capacity to an appropriate value based on your use case.
  12. In the **IP Addresses** field, update the IP addresses or IP ranges that are cloned from the address group.

**Note:** The number of IP addresses or IP ranges cannot exceed the configured capacity.
  13. Click content_copy**Clone**.




###  gcloud 

To clone an address group by using gcloud CLI, follow these guidelines:

  * Both address groups must be of the same type.
  * Both address groups must be in the same location.
  * Make sure that the new address group has sufficient capacity to fit the items of the source address group that are being cloned.
  * To specify the source address group, you must use the following unique URL identifier:
        
        organizations/ORGANIZATION_ID/locations/LOCATION/addressGroups/ADDRESS_GROUP_NAME
        




For more information about unique URL identifiers for address groups, see [Address group specifications](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification).

To clone items from an organization-scoped address group, use the [`gcloud network-security org-address-groups clone-items` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/clone-items):
    
    
    gcloud network-security org-address-groups clone-items NAME \
        --organization ORGANIZATION \
        --source SOURCE_NAMED_LIST \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the address group; you can specify the name as a string or as a unique URL identifier

  * `ORGANIZATION`: the organization ID where the address group is created

If you use a unique URL identifier for the `name` parameter, you can omit the `organization` parameter.

  * `SOURCE_NAMED_LIST`: a unique URL identifier of the source address group from where the items are cloned

  * `LOCATION`: the location of the destination address group

This can be set to `global` or a region code (such as `europe-west`). If you use a unique URL identifier for the `name` parameter, you can omit the `location` parameter.




## What's next

  * [Use hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks)
  * [Use global network firewall policies](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules)
  * [Use regional network firewall policies](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#rule_tasks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
