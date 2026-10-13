---
url: https://docs.cloud.google.com/vpc-service-controls/docs/protect-compute-engine-troubleshoot-denial/
title: Protect Compute Engine using a VPC Service Controls perimeter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:21.022574+00:00
---

# Protect Compute Engine using a VPC Service Controls perimeter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/protect-compute-engine-troubleshoot-denial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Protect Compute Engine using a VPC Service Controls perimeter Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to protect Compute Engine using a service perimeter and troubleshoot an ingress violation to allow authorized access to Compute Engine.

VPC Service Controls enables you to define a service perimeter around resources of Google-managed services to control communication to and between those services. You can establish a zero-trust perimeter around your sensitive resources, restricting access to authorized IP addresses, users, and devices. This capability lets you define security policies that prevent access to Google-managed services outside of a trusted perimeter, block access to data from untrusted locations, and mitigate data exfiltration risks.

This tutorial is intended for Google Cloud organization administrators who want to learn the basic VPC Service Controls concepts.

## Objectives

  * Understand the basics of VPC Service Controls.
  * Create a service perimeter.
  * Protect a project using VPC Service Controls.
  * Troubleshoot a VPC Service Controls ingress violation.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine VM instance](https://cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  * You need to have a Google Cloud [organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). If you don't have a Google Workspace or Cloud Identity account already, you must [acquire one](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#acquiring) and that creates an organization resource automatically for you.

  * [Create a folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#creating-folders), `Exercise`, at the organization level.

  * [Create two projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#creating_a_project_in_a_folder), `My-Project-1` and `My-Project-2`, in the `Exercise` folder within the same organization.

    * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Make sure that you have the following permissions and roles at the organization level:

    * [Permissions and roles](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) required to configure VPC Service Controls.

    * [Permissions and roles](https://docs.cloud.google.com/compute/docs/access) required to manage Compute Engine.




## Create a service perimeter

Create a service perimeter that protects the Compute Engine API in the `My-Project-2` project:

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

Make sure that you are in the organization scope.

  2. Click **Manage policies**.

  3. [Create a new access policy](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#create-access-policy) that is scoped to the `Exercise` folder.

  4. [Create a new perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) with the following details:

     * Title: `MyFirstPerimeter`

     * Perimeter type: **Regular**

     * Enforcement mode: **Enforced**

     * Resources to protect: `My-Project-2` project

     * Restricted services: **Compute Engine API**




## Verify the perimeter

In this section, you can make access requests to the resources in the projects to confirm whether the perimeter protects the intended resources.

  1. Access the `My-Project-1` project and verify that you can access Compute Engine by visiting **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

You should be able to access because `My-Project-1` is not protected by the perimeter that you created earlier.

  2. Access the `My-Project-2` project and verify that you can access Compute Engine by visiting **VM instances** page.

You should see that VPC Service Controls denies your request to access Compute Engine because the `MyFirstPerimeter` perimeter protects `My-Project-2` and the Compute Engine API.




## Troubleshoot a violation

[VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) include details about requests to protected resources and the reason why VPC Service Controls denied the request. You need this information to identify and troubleshoot the violation in the `My-Project-2` project.

### View audit logs

  1. Find the unique ID of the VPC Service Controls violation in the `My-Project-2` project's audit logs:

     1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. Select the `My-Project-2` project.

     3. To display all audit logs, enter the following query into the query-editor field:
            
            resource.type="audited_resource"
            protoPayload.metadata."@type"="type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
            

     4. Click **Run query**.

This query displays all VPC Service Controls audit logs. To find the violation details for accessing the Compute Engine API in the `My-Project-2` project, check the last error log.

**Note:** To filter the logs more granularly, you can use these [sample queries](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging#sample_queries) and add the VPC Service Controls unique ID that you received while [verifying the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/protect-compute-engine-troubleshoot-denial#verify-perimeter).

For more information, see [View logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging#viewing_logs).

  2. In the **Query results** pane, click **VPC Service Controls** next to the denial that you want to troubleshoot, and then click **Troubleshoot denial**.

The [VPC Service Controls violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer) page opens. This page shows the violation reason and other information such as if the violation is an ingress or egress violation.

In this tutorial, look for the following information:
         
         "principalEmail": "USER@DOMAIN"
         "callerIp": "PUBLIC_IP_ADDRESS"
         "serviceName": "compute.googleapis.com"
         "servicePerimeterName":
         "accessPolicies/POLICY_NUMBER/servicePerimeters/MyFirstPerimeter
         "ingressViolations": [
                 {
         "targetResource": "projects/PROJECT_NUMBER",
         "servicePerimeter": "accessPolicies/POLICY_NUMBER/servicePerimeters/MyFirstPerimeter"
                 }
               ],
         "violationReason": "NO_MATCHING_ACCESS_LEVEL",
         "resourceNames": "PROJECT_ID"
         

The violation reason is `"NO_MATCHING_ACCESS_LEVEL"`. The [`"NO_MATCHING_ACCESS_LEVEL"`](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#no-matching-access-level) violation occurs when the IP address, device type, or user identity doesn't match any ingress rules or access levels that are associated with the perimeter. If the caller IP address is missing or appears as an internal IP address in the log, then this violation can be due to a Google Cloud service that is not [supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).




To fix this denial in the `My-Project-2` project, you have two options:

  * Create an [access level](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) that allows access to your system IP address to the project inside the perimeter.

  * Create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#definition-ingress-egress) that allows access to an API client from outside the perimeter to resources within the perimeter.




The following section illustrates how to troubleshoot this denial by creating an access level.

### Create an access level

  1. In the Google Cloud console, go to the **Access Context Manager** page at the `Exercise` folder scope.

[Go to Access Context Manager](https://console.cloud.google.com/security/access-level)

  2. [Create an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) with the following details:

     * For **Create conditions in** , select **Basic mode**.

     * For **When condition is met, return** , select **True**.

     * Select the **IP Subnetworks** attribute, specify your system's public IP address.

     * Select the **Geographic locations** attribute, specify your geographic location.

This access level allows access only when the IP address and the geographic location is matched.

  3. Go to the **VPC Service Controls** page at the organization scope.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  4. Select the access policy that you created earlier in this tutorial.

  5. [Add the access level](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level) that you created at the `Exercise` folder scope to the `MyFirstPerimeter` perimeter.




## Test the access

After you add the access level, verify that you can access Compute Engine in the `My-Project-2` project and create a VM instance.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. [Create a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

**Note:** Retain the default values in the fields and create a low-cost VM instance.



After about a minute, Compute Engine creates a VM instance and this action verifies that you have full access to Compute Engine protected inside the perimeter.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

#### Delete VM instances

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



#### Delete VPC Service Controls resources

  1. [Delete the service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#delete).

  2. [Delete the access level](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels#delete_an_access_level) that you created at the `Exercise` folder scope.




## What's next

  * Learn how to [diagnose an access denial in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer) and view its comprehensive evaluation report.
  * [Diagnose an access denial and view the classic report](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
