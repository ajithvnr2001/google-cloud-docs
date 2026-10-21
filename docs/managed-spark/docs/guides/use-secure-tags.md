---
url: https://docs.cloud.google.com/managed-spark/docs/guides/use-secure-tags/
title: Use secure tags \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:40.308643+00:00
---

# Use secure tags  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/use-secure-tags/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use secure tags Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create secure tags, attach them to a Managed Service for Apache Spark cluster, and then use the tags to secure cluster networking.

**Note:** In this document, [Resource Manager tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) attached to Managed Service for Apache Spark clusters are called `secure tags`.

## Benefits of using secure tags

Secure tags have key differences from [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags), including Identity and Access Management access control, tag inheritance, and single VPC network binding, which produce the following key benefits:

Enhanced access control and security
    Secure tags resolve the security issues inherent with network tags by providing IAM controlled access. Unlike network tags, which can be modified by a user with cluster access, secure tags prevent unauthorized modification of tags and the resulting unwanted changes to firewall rules. 

Using secure tags in IAM policies enable [conditional access control](https://docs.cloud.google.com/iam/docs/conditions-overview), strengthening security by granting or denying roles based on the presence of tags. 

Simplified firewall management
    The [global](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) and [regional](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies) network firewall policies support secure tags. This support simplifies firewall management in Managed Service for Apache Spark across shared networks. 

Unlike VPC firewall rules, network firewall policies that are enhanced by secure tags enable efficient grouping and simultaneous updating of multiple rules, all governed by IAM access controls. Compared to VPC firewall rules that utilize network tags, secure tags provide enhanced security and management capabilities within network firewall policies. 

Hierarchical resource inheritance for efficient management
    Secure tags inherit from parent resources within the Google Cloud hierarchy. This inheritance simplifies management by letting you define tags at a higher level—for example, at the organization level—so that they automatically propagate to child resources, such as folders and projects. This enables consistent tagging across your organization. For more information, see [Tag inheritance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance). 

Improved network management across shared and peered VPCs
    Network tags identify sources or targets in firewall rules within a specified VPC network. Secure tags, when used to specify a source for an ingress rule in a network firewall policy, identify traffic sources in both the Managed Service for Apache Spark cluster VPC network and peered VPC networks. When secure tags are used to specify targets for ingress or egress rules, they identify targets only within their own VPC network. 

To learn more about the differences between Resource Manager tags and network tags, see [Comparison of Tags and network tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#differences).

To learn more about the differences between Resource Manager tags and labels, see [Tags and labels](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels).

## Before you begin

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects,folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### User role

To get the permissions that you need to create tags, ask your administrator to grant you the [](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin)[Tag Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) IAM role on Resource Manager tags. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Service account role

To ensure that [Managed Service for Apache Spark Service Agent service account ](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_agent_account) has the necessary permissions to attach secure tags to a Managed Service for Apache Spark cluster, ask your administrator to grant the [](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent)[Managed Service for Apache Spark Service Agent role](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) IAM role to [Managed Service for Apache Spark Service Agent service account ](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_agent_account) on the project. **Important:** You must grant this role to [Managed Service for Apache Spark Service Agent service account ](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_agent_account), _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

## Limitations

  * You can attach secure tags to a cluster only at the time of cluster creation.
  * Updation and deletion of secure tags aren't supported.



## Create a secure tag

To attach a secure tag to a Managed Service for Apache Spark cluster, you must first [create a Resource Manager tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) with a specified key and one or more values.

## Attach secure tags to the Managed Service for Apache Spark cluster

Create a Managed Service for Apache Spark cluster, specifying the secure tag `TAG_KEY:TAG_VALUE` pair. 

###  Google Cloud CLI 

To create a Managed Service for Apache Spark cluster and add a secure tag to the cluster, run the [gcloud Managed Service for Apache Spark clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--resource-manager-tags` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
      --region REGION \
      --resource-manager-tags=TAG_KEY=TAG_VALUE
    

Replace the following:

  * CLUSTER_NAME: the name of the new cluster.
  * REGION: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which to locate the cluster.
  * TAG_KEY and TAG_VALUE: the key and a value of the Resource Manager tag that you created. Tag keys can be specified in namespaced or non-namespaced format, as follows: 
    * Namespace format: `PROJECT-ID/KEY_NAME`=`PROJECT-ID/KEY_NAME/KEY_VALUE`. 

Example:
          
          --resource-manager-tags="test-project/testkey"=test-project/testkey/testvalue

    * Non-namespaced format: `tagKeys/TAG_KEY_ID`=`tagValues/TAG_VALUE_ID`

Example:
          
          --resource-manager-tags=tagKeys/123456789012=tagValues/987654321098

      * You can specify a comma-separated list to attach multiple secure tags comprised of the same key with different values, or different keys and values.
      * You must provide all tag key-value pairs in either namespaced or non-namespaced format; if both formats are used, an error is generated.



###  REST 

To create a Managed Service for Apache Spark cluster and add a secure tag to the cluster, include the [`resourceManagerTags`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig.FIELDS.resource_manager_tags) field as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request that includes attaching a `"TAG_KEY":"TAG_VALUE"` secure tag to the cluster.
    
    
    {
      "clusterName": "CLUSTER_NAME",
      "config": {
        "gceClusterConfig": {
          "resourceManagerTags": {
            "TAG_KEY":"TAG_VALUE"
          }
        }
      }
    }
    

Replace the following:

  * CLUSTER_NAME: the name of the new cluster.
  * TAG_KEY and TAG_VALUE: the key and a value of the Resource Manager tag that you created. Tag keys can be specified in namespaced or non-namespaced format, as follows: 
    * Namespace format: `PROJECT-ID/KEY_NAME`:`PROJECT-ID/KEY_NAME/KEY_VALUE`. 

Example:
          
          "test-project/testkey":"test-project/testkey/testvalue"

    * Non-namespaced format: `tagKeys/TAG_KEY_ID`:`tagValues/TAG_VALUE_ID`

Example:
          
          "tagKeys/123456789012":"tagValues/987654321098"

      * You can specify a comma-separated list to attach multiple secure tags comprised of the same key with different values, or different keys and values.
      * You must provide all tag key:value pairs in either namespaced or non-namespaced format; if both formats are used, an error is generated.



## Use secure tags for cluster networking

After attaching secure tags to a cluster, use secure tags to configure cluster networking:

  * Use secure tags to [define firewall rules](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#firewall_requirements).



## What's next

  * Learn more about [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).
  * Learn more about [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
