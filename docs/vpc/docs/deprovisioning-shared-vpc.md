---
url: https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc/
title: Deprovision Shared VPC \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:53.085701+00:00
---

# Deprovision Shared VPC  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deprovision Shared VPC

This page describes how to deprovision an existing Shared VPC configuration, disconnecting all service projects from a Shared VPC host project. Deprovisioning is a one-way process. Make sure that you are familiar with the [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) and [Provision Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc) pages first.

**Note:** Shared VPC is also referred to as "XPN" in the API and command-line interface.**Caution:** Deleting a Shared VPC host project without following the processes described here will cause an outage for instances in all service projects attached to the host project. The directions for provisioning a Shared VPC explain how to [create an organization-level policy to limit IAM principals who can remove the lien that prevents deletion of host projects](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#protectsharedvpc). If you have that policy in place, then you limit the risk of deleting a host project without properly deprovisioning it.

## Service Project Admin tasks

In each service project attached to the Shared VPC host project, a [Service Project Admin](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc) must remove all dependencies on the host project. Dependencies might include instances, instance groups, instance templates, backend services, and forwarding rules.

### Determine affected resources

To identify resources that depend on the Shared VPC host project, a Service Project Admin can [list its shared subnets](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#discovering_subnets_that_can_be_used). When the service project is detached from the host project, these subnets will no longer be available to it; thus, any resources that depend on them will be affected.

### Delete resources

Once a Service Project Admin has identified the resources that will be affected by the deprovisioning process, those resources will need to be deleted:

  * [Delete instances](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#delete_an_instance) that use subnets in the host project.

  * Delete [managed instance groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete) and [unmanaged instance groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete) that use subnets in the host project.

  * [Delete instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#deleting_an_instance_template) whose definitions depend on the host project.

  * If any serverless resources in the service project connect to a Shared VPC network in the host project by using Serverless VPC Access, follow the corresponding procedure to disconnect the resources: [Cloud Run services and functions](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#disconnect-service), [Cloud Run jobs](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#disconnect-job), or [App Engine services](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#disconnect). After you disconnect the resources, if the corresponding Serverless VPC Access connector was created in the service project, then [delete the connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#delete-connector).

  * Delete [internal forwarding rules for internal TCP/UDP load balancers](https://docs.cloud.google.com/load-balancing/docs/internal#forwarding_rule) that reference a subnet in a Shared VPC network of the host project.

  * Delete static internal IP addresses used by [network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces) from VMs in other networks.

To do this, you must first get a [list](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#list_static_internal_ip_addresses) of the reserved addresses, then [delete](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#delete_a_static_internal_ip_address) them.


**Caution:** If a service project should eventually be shut down (deleted), it must first be detached from the host project. **Do not simply delete it.** For details about why detaching must be done first, refer to the delete service projects section.

## Load Balancer Admin tasks

**Note:** This section only covers tasks that relate to internal Application Load Balancers and regional external Application Load Balancers.

Internal Application Load Balancers and regional external Application Load Balancers allow you to configure the load balancer so that a URL map in one host or service project can reference backend services (and backends) located across multiple projects in Shared VPC environments.

Before you can delete a service project, you must make sure that any such cross-project references to backend services in your service project have been removed. Load Balancer Admins will need to modify their URL maps to remove references to backend services in your service project.

## Shared VPC Admin tasks

All tasks in this section must be performed by a [Shared VPC Admin](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc).

### Detach service projects

Repeat these steps for each service project you need to detach from the Shared VPC host project.

**Caution:** Detaching a service project can only be done after the Service Project Admins have deleted all service project resources that depend on the host project. Before performing these steps, make sure that Service Project Admins have completed Service Project Admin tasks.

###  Console 

To view the Shared VPC page in the Google Cloud console, you must have the Shared VPC Admin role.

  1. Go to the **Shared VPC** page in the Google Cloud console.   
[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/details)
  2. Log in as a Shared VPC Admin.
  3. Select the host project you are removing service projects from.
  4. Click the **Attached projects** tab.
  5. Select the service project that you want to detach.
  6. Click the **Detach Projects** button.
  7. Review the information in the dialog.
  8. Click **Detach**.



###  gcloud 

  1. If you have not already, authenticate to `gcloud` as a Shared VPC Admin. Replace SHARED_VPC_ADMIN with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. Detach the service project from the host project. Replace SERVICE_PROJECT_ID with the project ID for the service project and HOST_PROJECT_ID with the project ID for the host project.
         
         gcloud compute shared-vpc associated-projects remove SERVICE_PROJECT_ID
             --host-project HOST_PROJECT_ID
         

  3. Confirm that the service project has been detached using one of these commands:
         
         gcloud compute shared-vpc get-host-project SERVICE_PROJECT_ID
         
         
         gcloud compute shared-vpc list-associated-resources HOST_PROJECT_ID
         

  4. If you only needed to detach service projects, log out of `gcloud` to protect your Shared VPC Admin account credentials. Otherwise, skip this step and proceed with disable the host project.
         
         gcloud auth revoke SHARED_VPC_ADMIN
         




###  API 

  1. Detach the service project.
         
         POST https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/disableXpnResource
         {
           "xpnResource": {
             "id": "SERVICE_PROJECT_ID"
           }
         }
         

Replace the placeholders with valid values:

     * HOST_PROJECT_ID is the ID of the host project.
     * SERVICE_PROJECT_ID is the ID of the service project to detach.

For more information, refer to the [`projects.disableXpnResource`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/disableXpnResource) method.

  2. Confirm that the service project has been detached.

     * Check that the service project isn't attached to any host project.
           
           GET https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/getXpnHost
           

Replace SERVICE_PROJECT_ID with the ID of the service project.

For more information, refer to the [`projects.getXpnHost`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/getXpnHost) method.

     * List the service projects attached the Shared VPC host project to confirm that the project is no longer listed.
           
           GET https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/getXpnResources
           

Replace HOST_PROJECT_ID with the ID of the host project.

For more information, refer to the [`projects.getXpnResources`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/getXpnResources) method.




### Disable host project

Disabling Shared VPC for the host project is only possible after all service projects have been detached. When disabled, the lien that prevents it from being easily deleted is removed automatically.

###  Console 

To view the Shared VPC page in the Google Cloud console, you must have the Shared VPC Admin role.

  1. Go to the **Shared VPC** page in the Google Cloud console.   
[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/details)
  2. Log in as a Shared VPC Admin.
  3. Select the Host Project you want to disable.
  4. Click the **Disable Shared VPC** button.
  5. In the dialog, read the description carefully.
  6. Enter the project ID of the host project for **Host project ID**.
  7. Click **Disable**.



###  gcloud 

  1. If you have not already, authenticate to `gcloud` as a Shared VPC Admin. Replace SHARED_VPC_ADMIN with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. Disable Shared VPC for the host project. Replace HOST_PROJECT_ID with the ID of the host project.
         
         gcloud compute shared-vpc disable HOST_PROJECT_ID
         

  3. Confirm that the project is no longer listed as a host project for your organization. Replace ORG_ID with your organization ID (determined by `gcloud organizations list`).
         
         gcloud compute shared-vpc organizations list-host-projects ORG_ID
         

  4. If you only needed to disable a host project, you can log out of `gcloud` to protect your Shared VPC Admin account credentials. Otherwise, skip this step and continue with delete projects.
         
         gcloud auth revoke SHARED_VPC_ADMIN
         




###  API 

  1. Disable Shared VPC for the project.
         
         POST https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/disableXpnHost
         

Replace HOST_PROJECT_ID with the ID of the host project.

For more information, refer to the [`projects.disableXpnHost`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/disableXpnHost) method.

  2. List your host projects to confirm that the project isn't listed.
         
         POST https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/listXpnHosts
         

Replace HOST_PROJECT_ID with the ID of the host project.

For more information, refer to the [`projects.listXpnHosts`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/listXpnHosts) method.




## Delete projects

This section discusses deleting projects that are no longer used; for example, you may have service projects that need to be deleted after they have been detached from a host project, or you may no longer need the host project after it has been disabled.

### Delete host project

You may choose to keep it as a normal project or [shut it down](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects). Shutting down a project deletes it.

An IAM principal can delete the host project if the principal has the [`resourcemanager.projectDeleter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) for your organization or if the principal is the owner of the host project. Shared VPC Admins may be able to delete host projects if they have the correct role or ownership.

**Important:** If you have not first detached all service projects from the host project and disabled Shared VPC, a lien will prevent the host project from being deleted. If you need to forcibly delete a host project, refer to this section..

### Delete service project

You may choose to [shut down each service project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) if you no longer need them. Before doing so, make sure that the service project has been detached from the host project.

An IAM principal can delete a service project if the principal has the [`resourcemanager.projectDeleter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) for your organization or if the principal is the owner of the service project. Service Project Admins may be able to delete service projects if they have the correct role or ownership.

**Caution:** If you shut down a service project without first detaching it from the host project, you will be unable to destroy its attachment (and the host project cannot be disabled). This happens because Google Cloud considers the service project attachment valid for the duration of the service project's recoverable period (30 days). If this happens, you must first [restore the deleted service project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project) or wait for its recoverable period to expire, detach it from the host project, then shut down the service project again. For more information, refer to [this page](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

## Forcibly delete a host project

While Shared VPC is active for a host project, a lien is placed on the project to prevent it from being accidentally deleted. Because this lien can be removed by a project owner, the [guidelines for provisioning a Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#protectsharedvpc) include steps to define an organizational policy that limits which IAM principals have the ability to remove a project lien.

Normally, a host project should be deleted _after_ the following tasks have been completed in this order:

  * All service projects have been detached from the host project, and
  * Shared VPC has been disabled.



When Shared VPC has been disabled, the lien that protects the host project is automatically removed.

This section details how to forcibly shut down a host project. You should only consider this option under these circumstances:

  * You cannot follow the normal steps of detaching service projects and disabling Shared VPC.
  * There are additional liens protecting the host project beyond the one that is added automatically.



If you forcibly shut down a host project and you have resources in service projects that use the Shared VPC network, the following events occur:

  * All Shared VPC networks, their subnets, routes, firewall rules, and all networking resources in the host project are deleted.
  * Resources, such as running instances in the service projects attached to the host project, are stopped.
  * Internal TCP/UDP load balancers are disabled if their forwarding rules depend on the Shared VPC network.

**Note:** The host project can be [restored](https://support.google.com/cloud/answer/6251787) within 30 days of being shut down. If restored, resources in service projects attached to it can be restarted.

###  gcloud 

  1. Authenticate to `gcloud` as an IAM principal who can remove a project lien. If you have [an organizational policy that limits which principals can remove liens](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#protectsharedvpc), you must authenticate as an IAM principal with the `resourcemanager.lienModifier` role for your organization. If you do not have such a policy in place, the project owner for the host project can remove the lien.

Replace ACCOUNT with the name of the appropriate IAM principal:
         
         gcloud auth login ACCOUNT
         

  2. List the liens associated with the host project. Replace HOST_PROJECT_ID with the ID of the host project.
         
         gcloud alpha resource-manager liens list \
         --project HOST_PROJECT_ID
         

  3. Remove each lien by name, one at a time, until no more liens are present. Replace LIEN_NAME with the name of the lien to remove.
         
         gcloud alpha resource-manager liens delete LIEN_NAME \
         --project HOST_PROJECT_ID
         

  4. Confirm that all liens have been removed.
         
         gcloud alpha resource-manager liens list \
         --project HOST_PROJECT_ID
         

  5. After removing the lien, you can log out of `gcloud` to protect the credentials of the IAM principal which has permission to remove liens.
         
         gcloud auth revoke ACCOUNT
         

  6. The host project can now be [shut down](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).




###  API 

  1. List the liens that are associated with the host project.
         
         GET https://cloudresourcemanager.googleapis.com/v1/liens?parent=projects:HOST_PROJECT_ID
         

Replace HOST_PROJECT_ID with the ID of the host project.

For more information, refer to the [`liens.list`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/list) method.

  2. Remove each lien by name until no more liens are present.
         
         DELETE https://cloudresourcemanager.googleapis.com/v1/liens/LIEN_NAME
         

Replace LIEN_NAME with the name of the lien to delete.

For more information, refer to the [`liens.delete`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/delete) method.

  3. List the liens again to confirm that they have been removed.




## Troubleshooting

### Can't detach a service project that used Serverless VPC Access

You might receive an error when attempting to detach a service project for which Serverless VPC Access was configured even if you have deleted the associated Serverless VPC Access connector. This error occurs because there is still an association between one or more serverless resources in the service project and the Shared VPC network in the host project.

To resolve this issue, remove any associations to the Serverless VPC Access connector from the serverless resources:

  1. If any Cloud Run services or functions used a connector associated with the Shared VPC network, then for each service or function, follow the steps to [Disconnect a Cloud Run service from a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#disconnect-service).

  2. If any Cloud Run jobs used a connector associated with the Shared VPC network, then for each job, follow the steps to [Disconnect a Cloud Run job from a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#disconnect-job)

  3. If any App Engine services used a connector associated with the Shared VPC network, then for each service, follow the steps to [Disconnect an App Engine service from a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#disconnect).

  4. After you disconnect all serverless resources from the VPC network, detach the service project.




To prevent this issue from happening again, ensure that you disconnect any serverless resources before deleting a connector as described in [Delete a connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#delete).

In rare cases, you might still receive an error after completing the steps in this section. If you still can't delete the VPC network, contact [Cloud Customer Care](https://cloud.google.com/support).

## What's next

  * For more information about Shared VPC, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).
  * For instructions about setting up Shared VPC, see [Provision Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc).
  * For instructions about setting up Google Kubernetes Engine clusters with Shared VPC, see [Set up clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
