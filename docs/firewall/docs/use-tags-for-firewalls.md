---
url: https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls/
title: Manage VM traffic by using secure tags \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:10.975796+00:00
---

# Manage VM traffic by using secure tags  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage VM traffic by using secure tags Stay organized with collections  Save and categorize content based on your preferences. 

You can use secure tags with firewall policies to apply granular security policies based on resource identity. This document shows you how to configure required Identity and Access Management (IAM) permissions, create secure tag keys and values, define firewall policies and rules, bind secure tags to virtual machine (VM) instances, and manage traffic across peered Virtual Private Cloud (VPC) networks. Before you begin, review the concepts in [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview).

## Grant permissions to secure tags

An organization administrator can grant roles at the organization level, and a project owner can grant roles at the project level.

### Grant Tag Administrator role

The Tag Administrator role (`roles/resourcemanager.tagAdmin`) lets you create, update, and delete secure tags.

###  Console 

To grant the Tag Administrator role (`roles/resourcemanager.tagAdmin`) to the user, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the project selector list, select the organization or project that you want to grant the role to.

  3. Click person_add**Grant access**.

  4. In the **New principals** field, enter the email address of the user. For example, `my-user@example.com`.

  5. In the **Select a role** list, enter **Tag** in the **Filter** field and then select **Tag administrator**.

  6. Click **Save**.




###  gcloud 

To grant the Tag Administrator role (`roles/resourcemanager.tagAdmin`) to an IAM principal in an organization's IAM policy, use the [`gcloud organizations add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding):
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member=user:EMAIL_ADDRESS \
        --role=roles/resourcemanager.tagAdmin
    

Replace the following:

  * `ORGANIZATION_ID`: your organization's ID
  * `EMAIL_ADDRESS`: the email address of the user



### Grant Tag User role

The Tag User role (`roles/resourcemanager.tagUser`) lets you access the list of secure tags and manage their associations with the resources.

###  Console 

To grant the Tag User role (`roles/resourcemanager.tagUser`) to the user, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the project selector list, select the organization or project that you want to grant the role to.

  3. Click person_add**Grant access**.

  4. In the **New principals** field, enter the email address of the user. For example, `my-user@example.com`.

  5. In the **Select a role** list, enter **Tag** in the **Filter** field and then select **Tag user**.

  6. Optional: Add a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role.

  7. Click **Save**.




###  gcloud 

  1. To grant the Tag User role (`roles/resourcemanager.tagUser`) to the user for a specific tag, use the [`gcloud resource-manager tags keys add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/add-iam-policy-binding):
         
         gcloud resource-manager tags keys add-iam-policy-binding ORGANIZATION_ID/TAG_KEY \
             --member=user:EMAIL_ADDRESS \
             --role=roles/resourcemanager.tagUser
         

Replace the following:

     * `ORGANIZATION_ID`: your organization's ID
     * `TAG_KEY`: the secure tag key
     * `EMAIL_ADDRESS`: the email address of the user
  2. To grant the Tag User role (`roles/resourcemanager.tagUser`) to an IAM principal so that they can use all tag values of every tag key in the organization, use the [`gcloud organizations add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding):
         
         gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
             --member=user:EMAIL_ADDRESS \
             --role=roles/resourcemanager.tagUser
         

Replace the following:

     * `ORGANIZATION_ID`: your organization's ID
     * `EMAIL_ADDRESS`: the email address of the user
  3. To grant the Tag User role (`roles/resourcemanager.tagUser`) to an IAM principal so that they can use a specific tag value of a tag key whose parent is the organization, use the [`gcloud resource-manager tags values add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/add-iam-policy-binding):
         
         gcloud resource-manager tags values add-iam-policy-binding ORGANIZATION_ID/TAG_KEY/TAG_VALUE \
             --member=user:EMAIL_ADDRESS \
             --role=roles/resourcemanager.tagUser
         

Replace the following:

     * `ORGANIZATION_ID`: your organization's ID
     * `TAG_KEY`: the secure tag key
     * `TAG_VALUE`: the secure tag value
     * `EMAIL_ADDRESS`: the email address of the user
  4. To grant the Tag User role (`roles/resourcemanager.tagUser`) to an IAM principal so that they can use all tag values of every tag key in a project, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
         
         gcloud projects add-iam-policy-binding PROJECT_NAME \
             --member=user:EMAIL_ADDRESS \
             --role=roles/resourcemanager.tagUser
         

Replace the following:

     * `PROJECT_NAME`: name of your project
     * `EMAIL_ADDRESS`: the email address of the user



### Custom roles to manage secure tags

The Tag Administrator role (`roles/resourcemanager.tagAdmin`) lets you create, update, and delete secure tags. If you need a few of these capabilities, you can create a custom IAM role with the relevant permissions and then grant the new role to the target user. For the list of relevant permissions, see [IAM roles](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#iam).

Secure tags used in firewall policies must be designated with a `GCE_FIREWALL` purpose. While the `GCE_FIREWALL` purpose is required for the secure tag to be used in networking features, you can use the secure tag for other actions.

## Create the secure tag keys and values

Before associating secure tags to firewall policies, you must create the secure tag keys and values.

After the tag key is created, it cannot be changed, and it must be unique within the same namespace.

###  Console 

To create a secure tag key and values, do the following:

  1. In the Google Cloud console, go to the **Tags** page.

[Go to Tags](https://console.cloud.google.com/iam-admin/tags)

  2. In the project selector list, select the organization or project under which you want to create a tag key.

  3. Click add**Create**.

  4. In the **Tag key** field, enter the display name of your tag key. This becomes part of the namespace name of your tag.

  5. Optional: In the **Tag key description** field, enter a description of your tag key.

  6. For **Tag purpose** select **For use with Cloud NGFW**.

  7. To create a secure tag, do one of the following:

     * If purpose data specifies a network, select **Restrict scope to a single network**.

     * If purpose data specifies an organization, clear **Restrict scope to a single network**.

  8. In the **Network selection** tab, select the organization or project under which you want to create a secure tag key.

  9. In the **Network** list, select the network.

  10. If you want to add tag values to this key, click add**Add value** for each tag value you want to create.

  11. In the **Tag value** field, enter the display name of your tag value. This becomes part of the namespace name of your tag.

  12. Optional: In the **Tag value description** field, enter a description of your tag value.

  13. When you have finished adding tag values, click **Create tag key**.




###  gcloud 

  1. After getting the required permissions, create the secure tag key at the organization or project level.

     * To create secure tag key for an organization, use the [`gcloud resource-manager tags keys create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create):
           
           gcloud resource-manager tags keys create TAG_KEY \
               --parent organizations/ORGANIZATION_ID \
               --purpose GCE_FIREWALL \
               --purpose-data organization=auto
           

Replace the following:

       * `TAG_KEY`: the secure tag key
       * `ORGANIZATION_ID`: your organization's ID
     * To create a secure tag key for a parent project or an organization whose purpose data identifies a single VPC network, use the [`gcloud resource-manager tags keys create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create):
           
           gcloud resource-manager tags keys create TAG_KEY \
               --parent organizations/ORGANIZATION_ID \
               --purpose GCE_FIREWALL \
               --purpose-data network=PROJECT_ID/NETWORK
           

Replace the following:

       * `TAG_KEY`: the secure tag key
       * `ORGANIZATION_ID`: your organization's ID
       * `PROJECT_ID`: your project's ID
       * `NETWORK`: the name of your network
  2. To add the relevant secure tag values to the secure tag keys, use the [`gcloud resource-manager tags values create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create):
         
         gcloud resource-manager tags values create TAG_VALUE \
               --parent ORGANIZATION_ID/TAG_KEY
         

Replace the following:

     * `TAG_VALUE`: the value to assign to the secure tag key
     * `ORGANIZATION_ID`: your organization's ID
     * `TAG_KEY`: the secure tag key

Run the command multiple times to add multiple values. Make sure that each secure tag value added to the secure tag key is unique.




## Create a firewall policy

You can use secure tag keys in firewall policies after you create them. You can use secure tag keys defined at the organization level in hierarchical firewall policies or network firewall policies. You can only use secure tags defined at the network level in network firewall policies.

### Create a hierarchical firewall policy

You can create a policy under any resource (organization or folder) of your organization hierarchy.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your organization ID or a folder within your organization.

  3. Click **Create firewall policy**.

  4. In the **Policy name** field, enter the name.

  5. If you want to create rules for your policy, click **Continue > Create firewall rule**.

For details, see Create a hierarchical firewall policy rule with secure tags.

  6. If you want to associate the policy with a resource, click **Continue > Add**.

For details, see [Associate a policy with the organization or folder](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#associate).

  7. Click **Continue > Create**.




###  gcloud 

To create a hierarchical firewall policy, use the [`gcloud compute firewall-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/create):
    
    
    gcloud compute firewall-policies create \
        [--organization ORGANIZATION_ID] | [--folder FOLDER_ID] \
        --short-name SHORT_NAME
    

Replace the following:

  * `ORGANIZATION_ID`: your organization's ID

Specify this ID if you are creating the policy at the organization level. This ID only indicates where the policy _lives_ ; it doesn't automatically associate the policy with the organization resource.

  * `FOLDER_ID`: the ID of a folder

Specify this ID if you are creating the policy in a given folder. This ID only indicates where the policy _lives_ ; it doesn't automatically associate the policy with that folder.

  * `SHORT_NAME`: a name for the policy

A policy created by using the Google Cloud CLI has two names: a system-generated name and a short name provided by you. When using the Google Cloud CLI to update an existing policy, you can provide either the system-generated name or the short name and the organization ID. When using the API to update the policy, you must provide the system-generated name.




### Create a global network firewall policy

After creating a secure tag, you can use it in rules of a global network firewall policy.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your project within your organization.

  3. Click **Create firewall policy**.

  4. In the **Policy name** field, enter the name.

  5. For **Deployment scope** , select **Global**.

  6. If you want to create rules for your policy, click **Continue > Create firewall rule**.

For details, see Create a network firewall policy rule with secure tags.

  7. If you want to associate the policy with a network, click **Continue > Associate**.

For details, see [Associate a policy with the network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate).

  8. Click **Continue > Create**.




###  gcloud 

To create a network firewall policy, use the [`gcloud compute network-firewall-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create):
    
    
     gcloud compute network-firewall-policies create \
         NETWORK_FIREWALL_POLICY_NAME \
         --description DESCRIPTION \
         --global
    

Replace the following:

  * `NETWORK_FIREWALL_POLICY_NAME`: a name for the policy
  * `DESCRIPTION`: a description for the policy



## Create a firewall policy rule with secure tags

After creating a secure tag and a firewall policy, you can create a firewall policy rule with the specific source tag values and target tag values to allow the chosen traffic between the VMs with the source tags and destination tags.

### Create a hierarchical firewall policy rule with secure tags

You can create a hierarchical firewall policy rule with the specific source and target keys and values only if you have created a hierarchical firewall policy. For more information, see Create a hierarchical firewall policy.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your organization ID or the folder that contains your policy.

  3. Click the name of your policy and then click **Create firewall rule**.

  4. Enter the priority of the rule.

  5. Specify the direction of traffic.

  6. For **Action on match** , choose a setting.

  7. For **Logs** , choose **On** or **Off**.

  8. For **Target** , select **Secure tags** , and then click **Select scope for tags**.

  9. On the **Select a resource** page, select the organization or project in which you want to create secure tags.

  10. Enter the key-value pairs to which the rule is to apply.

  11. To add more key-value pairs, click **Add tag**.

  12. In the **Source** section, for **Tags** , click **Select scope for tags**.

  13. On the **Select a resource** page, select the organization or folder that contains the secure tag keys.

  14. Click **Create**.




###  gcloud 

To create a hierarchical firewall policy rule, use the [`gcloud compute firewall-policies rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/create):
    
    
     gcloud compute firewall-policies rules create \
         --firewall-policy FIREWALL_POLICY_NAME \
         --src-secure-tags ORGANIZATION_ID/TAG_KEY/TAG_VALUE \
         --target-secure-tags ORGANIZATION_ID/TAG_KEY/TAG_VALUE \
         --direction DIRECTION \
         --action ACTION \
         --layer4-configs tcp:PORT
    

Replace the following:

  * `FIREWALL_POLICY_NAME`: the name of the hierarchical firewall policy
  * `ORGANIZATION_ID`: your organization's ID
  * `TAG_KEY`: the secure tag key
  * `TAG_VALUE`: the value to assign to the secure tag key
  * `DIRECTION`: indicates whether the rule is an `ingress` or `egress` rule
  * `ACTION`: one of the following actions: 
    * `allow`: allows connections that match the rule
    * `deny`: denies connections that match the rule
    * `goto_next`: passes connection evaluation to the next level in the hierarchy, either a folder or the network
  * `PORT`: the port number to access the resource



### Create a network firewall policy rule with secure tags

You can create a network firewall policy rule with the specific source tag values and target tag values that allow the chosen traffic between the VMs with the source tags and destination tags. For more information, see Create a global network firewall policy.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your project or the folder that contains your policy.

  3. Click the name of your policy and then click **Create firewall rule**.

  4. Enter the priority of the rule.

  5. Specify the direction of traffic.

  6. For **Action on match** , choose a setting.

  7. For **Logs** , choose **On** or **Off**.

  8. For **Target** , select **Secure tags** , and then click **Select scope for tags**.

  9. On the **Select a resource** page, select the organization or project in which you want to create secure tags.

  10. Enter the key-value pairs to which the rule is to apply.

  11. To add more key-value pairs, click **Add tag**.

  12. In the **Source** section, for **Tags** , click **Select scope for tags**.

  13. On the **Select a resource** page, select the organization or folder that contains the secure tag keys.

  14. Click **Create**.




###  gcloud 

To create a network firewall policy rule, use the [`gcloud compute network-firewall-policies rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/create):
    
    
     gcloud compute network-firewall-policies rules create \
         --firewall-policy FIREWALL_POLICY_NAME \
         --src-secure-tags ORGANIZATION_ID/TAG_KEY/TAG_VALUE \
         --target-secure-tags ORGANIZATION_ID/TAG_KEY/TAG_VALUE \
         --direction DIRECTION \
         --action ACTION \
         --layer4-configs tcp:PORT \
         --global-firewall-policy
    

Replace the following:

  * `FIREWALL_POLICY_NAME`: the name of the new network global network firewall policy
  * `ORGANIZATION_ID`: your organization's ID
  * `TAG_KEY`: the Tag key
  * `TAG_VALUE`: the value to assign to the Tag key
  * `DIRECTION`: indicates whether the rule is an `ingress` or `egress` rule
  * `ACTION`: one of the following actions: 
    * `allow`: allows connections that match the rule
    * `deny`: denies connections that match the rule
    * `goto_next`: passes connection evaluation to the next level in the hierarchy, either a folder or the network
  * `PORT`: the port number to access the resource



## Bind secure tags

To understand how secure tag binding works for both network firewall policies and hierarchical firewall policies, see [Bind secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#bind-secure-tags).

### Before you begin

  * Make sure that you have the Tag Administrator role (`roles/resourcemanager.tagAdmin`). As a tag administrator you can bind the secure tags to individual VM instances.

  * If you don't have the Tag Administrator role (`roles/resourcemanager.tagAdmin`), you can ask the organization administrator to grant you the Tag User role (`roles/resourcemanager.tagUser`). For more information, see Grant permissions to secure tags.

  * Make sure that you have the Tag User role (`roles/resourcemanager.tagUser`) on the resources to which the tags are bound. For more information about how to grant the Tag User role (`roles/resourcemanager.tagUser`) on the resources to which the tags are to be bound, see Grant permissions to secure tags.

  * Make sure that you have created the secure tag keys and values and firewall policy rule with secure tags.

  * Make sure that you have created a VM instance. For more information, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).




### Bind secure tags to VM instances

You can attach existing tags to certain resources. After the resource is created, attach tags to that resource by using the following instructions.

###  Console 

To bind the secure tags to VM instances, do the following: 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. In the **Name** column, click the name of the VM for which you want to add tags.

  4. From the **VM instance** details page, complete the following steps:

     1. Click **Edit**.
     2. In the **Basic information** section, click **Manage tags** and add the tags that you want for the instance.
     3. Click **Save**.



###  gcloud 

For information about how to use these flags, read [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#gcloud_8) in the Resource Manager documentation.

For example, the following command attaches a tag to a VM:
    
    
    gcloud resource-manager tags bindings create \
        --location=LOCATION_NAME \
        --tag-value=tagValues/TAGVALUE_ID \
        --parent=FULL_RESOURCE_NAME
    

Replace the following:

  * `LOCATION_NAME`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the instance is located. For a global resource, omit the `--location` flag.
  * `TAGVALUE_ID`: the numeric ID of the tag value
  * `FULL_RESOURCE_NAME`: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target resource; in this example, the full resource name of the VM instance:
        
        //compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID
        

Replace the following:

    * `PROJECT_NUMBER`: the numeric ID of your project that contains the target resource
    * `ZONE`: the zone that contains the instance
    * `INSTANCE_ID`: the [VM instance ID](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)



###  REST 

To attach a tag to a resource, you must first create a JSON representation of a tag binding that includes the permanent ID or namespace name of the tag value and the permanent ID of the resource. For more information about the format of a tag binding, see the [tagBindings reference](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings).

To attach the tag to a zonal resource, such as a VM instance, use the `tagBindings.create` method with the regional endpoint where your resource is located. For example:
    
    
    POST https://LOCATION_NAME-cloudresourcemanager.googleapis.com/v3/tagBindings

The request body can be one of the following two options:
    
    
    {
      "parent": "FULL_RESOURCE_NAME",
      "tagValue": "tagValue/TAGVALUE_ID"
    }
    
    
    
    {
      "parent": "FULL_RESOURCE_NAME",
      "tagValueNamespacedName": TAGVALUE_NAMESPACED_NAME
    }

Replace the following:

  * `LOCATION_NAME`: the zonal or regional [location of the resource](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). For a VM instance, specify the zone. For a global resource, omit the `LOCATION_NAME-` parameter
  * `FULL_RESOURCE_NAME`: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target resource; in this example, the full resource name of the VM instance:
        
        //compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID
        

Replace the following:

    * `PROJECT_NUMBER`: the numeric ID of your project that contains the target resource
    * `ZONE`: the zone that contains the instance
    * `INSTANCE_ID`: the [VM instance ID](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)
  * `TAGVALUE_ID`: the permanent ID of the tag value that is attached—for example: `4567890123`

  * `TAGVALUE_NAMESPACED_NAME`: the namespace name of the tag value that is attached and is of the format: `parentNamespace/tagKeyShortName/tagValueShortName`




### Add secure tags to a VM instance during VM creation

In certain scenarios, you might want to tag resources during resource creation, rather than after the resource is created.

###  Console 

Depending on the resource type, the exact steps might vary. The following steps are for a VM:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. Click **Create instance**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  4. In the navigation menu, click **Advanced**. In the **Advanced** pane that appears, do the following:

     1. Expand the expand_more**Manage tags and labels** section.
     2. Click add**Add tags**.
     3. In the **Tags** pane that opens, follow the instructions to add a tag to the instance.
     4. Click **Save**.
  5. Specify other configuration options for your instance. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  6. To create and start the VM, click **Create**.




###  gcloud 

To attach a tag to a resource during resource creation, add the `--resource-manager-tags` flag with the respective `create` command. For example, to attach a tag to a VM, use the following command:
    
    
      gcloud compute instances create INSTANCE_NAME \
          --zone=ZONE \
          --resource-manager-tags=tagKeys/TAGKEY_ID=tagValues/TAGVALUE_ID

Replace the following:

  * `INSTANCE_NAME`: the name of your VM instance
  * `ZONE`: the zone that contains the VM instance
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



Specify multiple tags by separating the tags with a comma, for example, `TAGKEY1=TAGVALUE1,TAGKEY2=TAGVALUE2`.

###  REST 

Make a `POST` request to the following URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances

Include the following request JSON body:
    
    
    {
      "name": INSTANCE_NAME,
      "params": {
        "resourceManagerTags": {
          "tagKeys/TAGKEY_ID": "tagValues/TAGVALUE_ID",
        },
      }
      // other fields omitted
    }

Replace the following:

  * `INSTANCE_NAME`: the name of your VM instance
  * `TAGKEY_ID`: the tag key number numeric ID
  * `TAGVALUE_ID`: the permanent numeric ID of the tag value that is attached—for example: `4567890123`



## Use secure tags across peered networks

You can use secure tags in VPC Network Peering. Assume that the connected networks are `server` and `client`. To use secure tags across two connected Google Cloud networks, complete the following tasks in the specified order.

  1. Assign the Tag Administrator role (`roles/resourcemanager.tagAdmin`) to the user. An organization administrator grants the Tag Administrator role (`roles/resourcemanager.tagAdmin`) to users at the organization level, and a project owner can grant the Tag Administrator role (`roles/resourcemanager.tagAdmin`) at the project level. For more information, see Grant permissions to secure tags.

  2. Create a secure tag key and value in the `server` network. For information about how to create secure tag keys and values, see Create secure tag keys and values.

  3. Create a firewall policy rule in the `server` network to allow ingress traffic from the secure tag created in the preceding step. For more information, see Create a firewall policy rule with secure tags.

  4. Grant the required permissions to the `client` user to secure tags in both VPC networks. For more information, see Grant permissions to secure tags.

  5. In the `client` network, bind the secure tags to a VM instance. For more information, see Bind secure tags. Now the `client` VM opens connections to the `server` VM.

  6. The server's firewall policy rule allows the traffic because the traffic comes from the secure tags that they are bound to. The rule also allows the response packet because egress traffic is allowed by default.




## What's next

  * [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
