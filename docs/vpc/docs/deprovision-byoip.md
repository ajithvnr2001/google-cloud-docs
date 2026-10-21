---
url: https://docs.cloud.google.com/vpc/docs/deprovision-byoip/
title: Deprovision bring your own IP \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:29.234239+00:00
---

# Deprovision bring your own IP  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/deprovision-byoip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deprovision bring your own IP

If you no longer want to use your IP addresses in Google Cloud, you can deprovision your BYOIP addresses.

Different components take different times to deprovision.

Configuration | Regional (v2) | Regional (v1) | Global (v1)  
---|---|---|---  
Public advertised prefix deprovisioning time | Approximately 2 weeks | Approximately 4 weeks | Approximately 4 weeks  
Public delegated prefix deprovisioning time | A few minutes | 4 weeks | 4 weeks  
Sub-prefix deprovisioning time | A few minutes | A few minutes | A few minutes  
  
### Roles

To get the permissions that you need to complete the tasks in this guide, ask your administrator to grant you the [Compute Public IP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) (`roles/compute.publicIpAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Deprovision BYOIP addresses

When you deprovision BYOIP addresses, complete the steps in the following sections in order.

### Delete a public delegated prefix or sub-prefix

You can delete a public delegated prefix or sub-prefix if all IP addresses in the prefix are not assigned to resources:

  * For IPv4 prefixes: the IP addresses are [unassigned](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip). When you delete the prefix, all associated IP addresses are deleted.

  * For IPv6 prefixes: no forwarding rules, subnets, or static IP addresses use IP address ranges from the sub-prefix.




Before you can delete a v2 regional public delegated prefix, the prefix must not be advertised. Check the [status](https://docs.cloud.google.com/vpc/docs/create-pdp#pdp-status), and if needed, [withdraw the prefix](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement#withdraw_advertisement_of_a_prefix).

After the deletion process is started, you cannot make changes to the public delegated prefix.

You can verify that the removal is pending by [checking the status of the public delegated prefix](https://docs.cloud.google.com/vpc/docs/create-pdp#pdp-status). The status is `DELETING` until the public delegated prefix is deleted.

When deletion is complete, the IP range from the deleted public delegated prefix is available in the public advertised prefix and can be delegated to a new public delegated prefix.

###  Console 

  1. In the Google Cloud console, go to the **Bring your own IP** page.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click the public delegated prefix that you want to delete, and then click **Delete**.




###  gcloud 

To delete a public delegated prefix or a sub-prefix, use the [`public-delegated-prefixes delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delete).
    
    
    gcloud compute public-delegated-prefixes delete PDP_NAME \
        --region=PDP_REGION
    

To delete a global public delegated prefix or sub-prefix, replace `--region=PDP_REGION` with `--global`.

If the prefix was delegated to another project from this project, use the `--project=PROJECT_NAME` flag with the `public-delegated-prefixes delete` command to specify the project where the prefix is located.

Or you can use the following command to delete a sub-prefix that is delegated to another project without having to include that project in the command.
    
    
    gcloud compute public-delegated-prefixes \
        delegated-sub-prefixes \
        delete SUB_PREFIX_NAME \
        --public-delegated-prefix=PARENT_PDP_NAME \
        --public-delegated-prefix-region=PDP_REGION
    

To delete a global public delegated prefix or sub-prefix, replace `--public-delegated-prefix-region=PDP_REGION` with `--global-public-delegated-prefix`.

### Delete a public advertised prefix

You can delete a public advertised prefix if it is not in use. After the deletion process is started, you cannot make changes to the public advertised prefix.

###  Console 

  1. In the Google Cloud console, go to the **Bring your own IP** page.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Select the public advertised prefix that you want to delete, and then click **Delete prefix**.




###  gcloud 

To delete a public advertised prefix, use the [`public-advertised-prefixes delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/delete).
    
    
    gcloud compute public-advertised-prefixes delete PAP_NAME \
    

You can verify that the removal is pending by [checking the status of the public advertised prefix](https://docs.cloud.google.com/vpc/docs/create-pap#pap-status). The status is `PREFIX_REMOVAL_IN_PROGRESS` until the public advertised prefix is deleted.

### Remove a ROA

After you successfully delete a public advertised prefix, you don't need to remove the ROA that points to the ASN for Google Cloud. If you want to remove this ROA, you must wait 14 days after deleting the public advertised prefix before you remove the ROA. This waiting period gives Google Cloud time to update configurations in order to stop advertising your IP address range.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
