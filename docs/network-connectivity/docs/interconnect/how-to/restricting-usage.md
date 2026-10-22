---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage/
title: Restrict Cloud Interconnect usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:40.083487+00:00
---

# Restrict Cloud Interconnect usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Restrict Cloud Interconnect usage Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to restrict the set of Virtual Private Cloud (VPC) networks that can use Cloud Interconnect.

By default, any VPC network can use Cloud Interconnect. To control which VPC networks can use Cloud Interconnect, you can set an organization policy. For general information about organization policies, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

Using Cloud Interconnect to connect a VPC network to your on-premises network requires a [VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments). An organization policy for restricting Cloud Interconnect usage allows or denies the creation of VLAN attachments from specified VPC networks. You can set a policy that allows or denies the creation of VLAN attachments from a specific VPC network or all VPC networks in a project, folder, or organization resource.

You can use the following constraints when defining your policy:

  * `constraints/compute.restrictDedicatedInterconnectUsage`

This constraint defines the set of VPC networks that you can use when creating a VLAN attachment using Dedicated Interconnect.

  * `constraints/compute.restrictPartnerInterconnectUsage`

This constraint defines the set of VPC networks that you can use when creating a VLAN attachment using Partner Interconnect.




When you set an organization policy, it only constrains the creation of VLAN attachments in the future. The policy does not affect previously created VLAN attachments.

If a user attempts to create a VLAN attachment that violates an organization policy, they see an error message. The following is an example error message from running `gcloud compute interconnects attachments partner create`:
    
    
    ERROR: (gcloud.compute.interconnects.attachments.partner.create) Could not fetch resource:
    - Constraint constraints/compute.restrictPartnerInterconnectUsage violated for projects/example-project.
    projects/example-project/global/networks/example-network is not allowed to use the Partner Interconnect.
    

This page includes example procedures for setting organization policies to restrict Cloud Interconnect usage.

For more information, including general procedures for setting organization policies, see the following:

  * [Understanding constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints)
  * [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints)
  * [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies)



## Before you begin

To set organization policies, you must have the [Organization Policy Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy) (`roles/orgpolicy.policyAdmin`).

## Set a policy to deny a specific VPC network

To set a policy to deny a specific VPC network from using Cloud Interconnect, follow these steps:

  1. Find your organization ID by entering the following command:
         
         gcloud organizations list

The command output looks like the following example:
         
         DISPLAY NAME             ID
         example-organization     29252605212
         

  2. Create a JSON file that defines your policy. The following example JSON file defines a policy that prevents `network-1` in `project-1` from using Dedicated Interconnect:
         
         {
           "Constraint": "constraints/compute.restrictDedicatedInterconnectUsage",
           "listPolicy": {
             "deniedValues": [
               "projects/project-1/global/networks/network-1"
            ]
           }
         }
         

  3. Use the `gcloud` Resource Manager `set-policy` command to set the organization policy:
         
         gcloud resource-manager org-policies set-policy JSON_FILE_NAME
            --organization=ORGANIZATION_ID
         

Replace the following:

     * `JSON_FILE_NAME`: the name of the JSON file that you created in the previous step, such as `policy-name.json`

     * `ORGANIZATION_ID`: the ID of the organization that you previously found




## Set a policy to deny all VPC networks

To set a policy to deny all VPC networks from using Cloud Interconnect, follow these steps:

  1. Find your organization ID by entering the following command:
         
         gcloud organizations list

The command output looks like the following example:
         
         DISPLAY NAME             ID
         example-organization     29252605212
         

  2. Create a JSON file that defines your policy. The following example JSON file defines a policy that prevents all VPC networks from using Dedicated Interconnect:
         
         {
           "Constraint": "constraints/compute.restrictDedicatedInterconnectUsage",
           "listPolicy": {
             "allValues": "DENY"
            }
         }
         

  3. Use the `gcloud` Resource Manager `set-policy` command to set the organization policy:
         
         gcloud resource-manager org-policies set-policy JSON_FILE_NAME
            --organization=ORGANIZATION_ID
         

Replace the following:

     * `JSON_FILE_NAME`: the name of the JSON file that you created in the previous step, such as `policy-name.json`

     * `ORGANIZATION_ID`: the ID of the organization that you previously found




## Set a policy at the organization, folder, or project level

The previous sections describe how to deny a specific VPC network or all VPC networks. You can also use the syntax described in [List constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#list_constraint) to allow or deny VPC networks at the organization, project, or folder level.

## What's next

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
