---
url: https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc/
title: Provision Shared VPC \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.310512+00:00
---

# Provision Shared VPC  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Provision Shared VPC

Shared VPC lets you export subnets from a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) in a _host project_ to other _service projects_ in the same [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). Instances in the service projects can have network connections in the shared subnets of the host project. This page describes how to set up and use Shared VPC, including some necessary administrative preparation for your organization.

**Note:** If you're getting started with Google Cloud, you can create an initial Shared VPC network as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

Shared VPC supports exporting subnets of any [stack type](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

For information about detaching service projects or removing the Shared VPC configuration completely, see [Deprovision Shared VPC](https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc).

Shared VPC is also referred to as "XPN" in the API and command-line interface.

## Quotas, limits, and eligible resources

Before you begin, make sure that you are familiar with [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) and [IAM](https://docs.cloud.google.com/iam/docs/overview), specifically:

  * Make note of the [quotas and limits](https://docs.cloud.google.com/vpc/docs/quota#shared-vpc) that pertain to Shared VPC.

  * Be sure to understand which [resources can participate](https://docs.cloud.google.com/vpc/docs/shared-vpc#eligible-resources).

  * Ensure that you have [enabled](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) and billing for your host project and all service projects that you plan to attach to the host project.




## Prepare your organization

Keep the following information in mind, when you prepare your organization.

### Administrators and IAM

Preparing your organization, setting up Shared VPC host projects, and using Shared VPC networks involves a minimum of three different administrative Identity and Access Management (IAM) roles. For more details about each role and information about optional ones, see the [administrators and IAM](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc) section of the Shared VPC overview.

**Important:** The Network User and Network Admin roles are different. For details, see the [Network and Security Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#net_and_security_admins) section of the Shared VPC overview.

### Organization policy constraints

Organization policy constraints can protect Shared VPC resources at the project, folder, or organization level. The following sections describe each policy.

#### Prevent accidental deletion of host projects

The accidental deletion of a host project would lead to outages in all service projects attached to it. When a project is configured to be a Shared VPC host project, a special lock—called a _lien_ —is placed upon it. As long as the lien is present, it prevents the project from being deleted accidentally. The lien is automatically removed from the host project when it is no longer configured for Shared VPC.

**Caution:** By default, a project owner can remove a lien from a project, including a Shared VPC host project, unless an organization-level policy is defined to limit lien removal. (Specifically, lien removal requires an IAM principal with the `resourcemanager.projects.get` and `resourcemanager.projects.updateLiens` permissions on the project.) The project owner for the host project could remove the lien then delete the Shared VPC project. To prevent this from happening, follow the directions in this section.

A user with the `orgpolicy.policyAdmin` role can define an organization-level policy constraint (constraints/compute.restrictXpnProjectLienRemoval) that limits the removal of liens to just the following roles:

  * Users with `roles/owner` or `roles/resourcemanager.lienModifier` at the organization level
  * User with custom roles that include the `resourcemanager.projects.get` _and_ `resourcemanager.projects.updateLiens` permissions at the organization level



This effectively prevents a project owner who does not have the `roles/owner` role at the organization level or the `resourcemanager.lienModifier` role at the organization level from being able to accidentally delete a Shared VPC host project. For more information about the permissions associated with the `resourcemanager.lienModifier` role, refer to [Placing a lien on a project](https://docs.cloud.google.com/resource-manager/docs/project-liens#placing_a_lien_on_a_project) in the Resource Manager documentation.

Because an organization policy applies to all projects in the organization, you only need to follow these steps once to restrict lien removal.

  1. Authenticate to `gcloud` as an Organization Admin or IAM principal with the `orgpolicy.policyAdmin` role. Replace `ORG_ADMIN` with the name of an Organization Admin:
         
         gcloud auth login ORG_ADMIN
         

  2. Determine your organization ID number by looking at the output of this command.
         
         gcloud organizations list
         

  3. Enforce the `compute.restrictXpnProjectLienRemoval` policy for your organization by running this command. Replace `ORG_ID` with the number you determined from the previous step.
         
         gcloud resource-manager org-policies enable-enforce \
             --organization ORG_ID compute.restrictXpnProjectLienRemoval
         

  4. Log out of `gcloud` if you are finished performing tasks as an Organization Admin to protect your account.
         
         gcloud auth revoke ORG_ADMIN
         




#### Constrain host project attachments

By default, a Shared VPC Admin can attach a non-host to any host project in the same organization. An organization policy administrator can limit the set of hosts projects to which a non-host project or non-host projects in a folder or organization can be attached. For more information, see the [`constraints/compute.restrictSharedVpcHostProjects` constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

#### Constrain the subnets in the host project that a service project can use

By default, after you configure Shared VPC, IAM principals in service projects can use any subnet in the host project if they have the [appropriate IAM permissions](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins). In addition to managing individual user permissions, an organization policy administrator can set a policy to define the set of subnets that can be accessed by a particular project or by projects in a folder or organization. For more information, see the [`constraints/compute.restrictSharedVpcSubnetworks` constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

### Prevent accidental shutdown of host projects

Disconnecting billing on a Shared VPC network can lead to a complete shutdown of all dependent resources including service projects. To prevent a possible occurrence of an accidental Shared VPC shutdown due to inactive or disabled billing, [secure the link between the host project and its billing account](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link).

### Nominate Shared VPC Admins

An Organization Admin can grant one or more IAM principals the [**Shared VPC Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.xpnAdmin) and [**Project IAM Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) roles.

The Project IAM Admin role grants Shared VPC Admins permission to share all existing and future subnets, not just individual subnets. This grant creates a binding at the organization or folder level, not the project level. So the IAM principals must be defined in the organization, not just a project therein.

###  Console 

**To grant the Shared VPC Admin role at the organization level**

  1. Log into the Google Cloud console as an Organization Admin, then go to the IAM page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam/organization)

  2. From the project menu, select your organization.

If you select a project, the **Roles** menu shows incorrect entries.

  3. Click **Add**.

  4. Enter the email addresses of the **New principals**.

  5. In the **Roles** menu, select **Compute Engine > Compute Shared VPC Admin**.

**Note:** If you don't see the **Compute Shared VPC Admin** role as an option, you might not be logged in to the Google Cloud console as an Organization Admin, or you might have selected a project instead of the whole organization.
  6. Click **Add another role**.

  7. In the **Roles** drop down, select **Resource Manager** > **Project IAM Admin**.

  8. Click **Save**.




**To grant the Shared VPC Admin role at the folder level**

  1. Log into the Google Cloud console as an Organization Admin, then go to the IAM page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam/organization)

  2. From the project menu, select your folder.

If you select a project or organization, the options you see are incorrect.

  3. Click **Add**.

  4. Enter the email addresses of the **New principals**.

  5. Under **Select a role** , select **Compute Engine > Compute Shared VPC Admin**.

  6. Click **Add another role**.

  7. In the **Roles** menu, select **Resource Manager > Project IAM Admin**.

  8. Click **Add another role**.

  9. In the **Roles** menu, select **Resource Manager > Compute Network Viewer**.

  10. Click **Save**.




###  gcloud 

  1. Authenticate to `gcloud` as an Organization Admin. Replace `ORG_ADMIN` with the name of an Organization Admin:
         
         gcloud auth login ORG_ADMIN
         

  2. Determine your organization ID number by looking at the output of this command.
         
         gcloud organizations list
         

  3. To assign the Shared VPC Admin role at the **organization** level, do the following:

     1. Apply Shared VPC Admin role to an existing IAM principal. Replace `ORG_ID` with the organization ID number from the previous step, and `EMAIL_ADDRESS` with the email address of the user to whom you are granting the Shared VPC Admin role.
            
            gcloud organizations add-iam-policy-binding ORG_ID \
              --member='user:EMAIL_ADDRESS' \
              --role="roles/compute.xpnAdmin"
            
            
            gcloud organizations add-iam-policy-binding ORG_ID \
              --member='user:EMAIL_ADDRESS' \
              --role="roles/resourcemanager.projectIamAdmin"
            

  4. To assign the Shared VPC Admin role at the **folder** level, do the following:

     1. Determine your folder ID by looking at the output of this command.
            
            gcloud resource-manager folders list --organization=ORG_ID
            

     2. Apply Shared VPC Admin role to an existing IAM principal. Replace `ORG_ID` with the organization ID number from the previous step, and `EMAIL_ADDRESS` with the email address of the user to whom you are granting the Shared VPC Admin role.
            
            gcloud resource-manager folders add-iam-policy-binding FOLDER_ID \
               --member='user:EMAIL_ADDRESS' \
               --role="roles/compute.xpnAdmin"
            
            
            gcloud resource-manager folders add-iam-policy-binding FOLDER_ID \
               --member='user:EMAIL_ADDRESS' \
               --role="roles/resourcemanager.projectIamAdmin"
            
            
            gcloud resource-manager folders add-iam-policy-binding FOLDER_ID \
               --member='user:EMAIL_ADDRESS' \
               --role="roles/compute.networkViewer"
            

  5. Revoke your Organization Admin account token for in the `gcloud` command-line tool when you are finished performing tasks to protect your account.
         
         gcloud auth revoke ORG_ADMIN
         




###  API 

  * To assign the Shared VPC Admin role at the **organization** level, use the following procedure:

    1. Determine your organization ID number.
           
           POST https://cloudresourcemanager.googleapis.com/v1/organizations
           

    2. Describe and then record the details of your existing organization policy.
           
           POST https://cloudresourcemanager.googleapis.com/v1/organizations/ORG_ID:getIamPolicy
           

Replace `ORG_ID` with the ID of your organization.

    3. Assign the Shared VPC Admin role.
           
           POST https://cloudresourcemanager.googleapis.com/v1/organizations/ORG_ID:setIamPolicy
           {
             "bindings": [
               ...copy existing bindings
               {
                 "members": [
                   "user:EMAIL_ADDRESS"
                 ],
                 "role": "roles/compute.xpnAdmin"
               },
               {
                 "members": [
                   "user:EMAIL_ADDRESS"
                 ],
                 "role": "roles/resourcemanager.projectIamAdmin"
               }
             ],
             "etag": "ETAG",
             "version": 1,
             ...other existing policy details
           }
           

Replace the following:

       * `ORG_ID`: the ID of the organization that contains the user who you're granting the Shared VPC Admin role.
       * `EMAIL_ADDRESS`: the email address of the user.
       * `ETAG`: a unique identifier that you got when you described the existing policy. It prevents collisions if multiple updates requests are sent at the same time.

For more information, see the [`organizations.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/setIamPolicy).

  * To assign the Shared VPC Admin role at the **folder** level, use the following request:

    1. Determine your organization ID number.
           
           POST https://cloudresourcemanager.googleapis.com/v1/organizations
           

    2. Find your folder ID.
           
           GET https://cloudresourcemanager.googleapis.com/v2/folders?parent=organizations/ORG_ID
           

Replace `ORG_ID` with the ID of your organization.

    3. Describe and then record the details of your existing folder policy.
           
           POST https://cloudresourcemanager.googleapis.com/v2/folders/FOLDER_ID:getIamPolicy
           

Replace `FOLDER_ID` with the ID of your folder.

    4. Assign the Shared VPC Admin role.
           
           POST https://cloudresourcemanager.googleapis.com/v1/organizations/FOLDER_ID:setIamPolicy
           {
             "bindings": [
               ...copy existing bindings
               {
                 "members": [
                   "user:EMAIL_ADDRESS"
                 ],
                 "role": "roles/compute.xpnAdmin"
               },
               {
                 "members": [
                   "user:EMAIL_ADDRESS"
                 ],
                 "role": "roles/resourcemanager.projectIamAdmin"
               },
               {
                 "members": [
                   "user:EMAIL_ADDRESS"
                 ],
                 "role": "roles/compute.networkViewer"
               }
             ],
             "etag": "ETAG",
             "version": 1,
             ...other existing policy details
           }
           

Replace the following:

       * `FOLDER_ID`: the ID of the organization that contains the user to whom you're granting the Shared VPC Admin role.
       * `EMAIL_ADDRESS`: the email address of the user.
       * `ETAG`: a unique identifier that you got when you described the existing policy. It prevents collisions if multiple updates requests are sent at the same time.

For more information, see the [`folders.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/setIamPolicy).




## Set up Shared VPC

All tasks in this section must be performed by a Shared VPC Admin.

### Enable a host project

Within an organization, Shared VPC Admins can designate projects as Shared VPC _host projects_ , subject to [quotas and limits](https://docs.cloud.google.com/vpc/docs/quota#shared-vpc), by following this procedure. Shared VPC Admins can also create and delete projects if they have the [Project Creator role and Project Deleter role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) (`roles/resourcemanager.projectCreator` and `roles/resourcemanager.projectDeleter`) for your organization.

When you enable a host project, the project's network resources are not automatically shared with service projects. You need to attach service projects to the host project to share selected networks and subnets with the service projects.

**Note:** The [Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com) must be enabled for the project that becomes the Shared VPC host project and for any service projects that will attach to it. For more information, see the [Compute Engine API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1).**Caution:** To prevent outages caused by accidental deletion or shutdown of a host project, see Prevent accidental deletion of host projects and Prevent accidental shutdown of host projects.

###  Console 

If you don't yet have the Compute Shared VPC Admin role (`roles/compute.xpnAdmin`), then you cannot view this page in the Google Cloud console.

  1. In the Google Cloud console, go to the **Shared VPC** page.

[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/details)

  2. Sign in as a Shared VPC Admin.

  3. Select the project you want to enable as a Shared VPC host project from the project picker.

  4. Click **Set up Shared VPC**.

  5. On the next page, click **Save & continue** under **Enable host project**.

  6. Under **Select subnets** , do one of the following:

     1. Click **Share all subnets (project-level permissions)** if you need to share all current and future subnets in the VPC networks of the host project with service projects and Service Project Admins specified in the next steps.
     2. Click **Individual subnets (subnet-level permissions)** if you need to selectively share subnets from the VPC networks of the host project with service projects and Service Project Admins. Then, select **Subnets to share**.
  7. Click **Continue**.  
The next screen is displayed.

  8. In **Project names** , specify the service projects to attach to the host project. Note that attaching service projects does not define any Service Project Admins; that is done in the next step.

  9. In the **Select users by role** section, add Service Project Admins. These users will be granted the IAM role of `compute.networkUser` for the shared subnets. Only Service Project Admins can create resources in the subnets of the Shared VPC host project.

  10. Click **Save**.




###  gcloud 

**Note:** These steps designate a project as a Shared VPC host project. Unlike the Console directions, no service projects are attached to the host project, and no Service Project Admins are defined. After you complete these steps, you can attach service projects.

  1. Authenticate to `gcloud` as a Shared VPC Admin. Replace `SHARED_VPC_ADMIN` with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. Enable Shared VPC for the project that you need to become a host project. Replace `HOST_PROJECT_ID` with the ID of the project.
         
         gcloud compute shared-vpc enable HOST_PROJECT_ID
         

  3. Confirm that the project is listed as a host project for your organization. Replace `ORG_ID` with your organization ID (determined by `gcloud organizations list`).
         
         gcloud compute shared-vpc organizations list-host-projects ORG_ID
         

  4. If you only needed to enable a host project, you can log out of `gcloud` to protect your Shared VPC Admin account credentials. Otherwise, skip this step and continue with the steps to attach service projects.
         
         gcloud auth revoke SHARED_VPC_ADMIN
         




###  API 

  1. Enable Shared VPC for the project by using credentials with Shared VPC Admin permissions.
         
         POST https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/enableXpnHost
         

Replace `HOST_PROJECT_ID` with the ID of the project that will be a Shared VPC host project.

For more information, see the [`projects.enableXpnHost` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/enableXpnHost).

  2. Confirm that the project is listed as a host project.
         
         POST https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/listXpnHosts
         

Replace `HOST_PROJECT_ID` with the ID of the Shared VPC host project.

For more information, see the [`projects.listXpnHosts` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/listXpnHosts).




### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_shared_vpc_host_project) to enable a host project.
    
    
    resource "google_compute_shared_vpc_host_project" "host" {
      project = var.project # Replace this with your host project ID in quotes
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Attach service projects

A service project must attach to a host project before its Service Project Admins can use the Shared VPC. A Shared VPC Admin must perform the following steps to complete the attachment.

A service project can only attach to one host project, but a host project supports multiple service project attachments. Refer to [limits specific to Shared VPC](https://docs.cloud.google.com/vpc/docs/quota#shared-vpc) on the VPC quotas page for details.

**Note:** Before you can attach to a host project, you must enable the [Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com) for the service project.

###  Console 

**Note:** If you used the Console to enable a host project, you already attached one or more service projects to it. The following directions detail how to modify the configuration of an existing host project.

  1. Log into the Google Cloud console as a Shared VPC Admin.
  2. In the Google Cloud console, go to the **Shared VPC** page.   
[Go to the Shared VPC page](https://console.cloud.google.com/networking/xpn/details)
  3. Click the **Attached projects** tab.
  4. Under the **Attached projects** tab, click the **Attach projects** button.
  5. Check the boxes for the service projects to attach in the **Project names** section. Note that attaching service projects does not define any Service Project Admins; that is done in the next step.
  6. In the **VPC network permissions** section, select the roles whose principals will get the `compute.networkUser` role. IAM principals are granted the Network User role for the entire host project or certain subnets in the host project, based on the **VPC network sharing mode**. These principals are known as Service Project Admins in their respective service projects.
  7. In the **VPC network sharing mode** section, select one of the following: 
     1. Click **Share all subnets (project-level permissions)** to share all current and future subnets in VPC networks of the host project with all service projects and Service Project Admins.
     2. Click **Individual subnets (subnet-level permissions)** if you need to selectively share subnets from VPC networks of the host project with service projects and Service Project Admins. Then, select **Subnets to share**.
  8. Click **Save**.



###  gcloud 

**Note:** These steps only cover attaching a service project to a host project. You must first have enabled a host project.

  1. If you have not already, authenticate to `gcloud` as a Shared VPC Admin. Replace `SHARED_VPC_ADMIN` with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. Attach a service project to a previously enabled host project. Replace `SERVICE_PROJECT_ID` with the project ID for the service project and `HOST_PROJECT_ID` with the project ID for the host project.
         
         gcloud compute shared-vpc associated-projects add SERVICE_PROJECT_ID \
             --host-project HOST_PROJECT_ID
         

  3. Confirm that the service project has been attached.
         
         gcloud compute shared-vpc get-host-project SERVICE_PROJECT_ID
         

  4. Optionally, you can list the service projects that are attached to the host project:
         
         gcloud compute shared-vpc list-associated-resources HOST_PROJECT_ID
         

  5. If you only needed to attach a service project, you can log out of `gcloud` to protect your Shared VPC Admin account credentials. Otherwise, skip this step and define Service Project Admins for all subnets or for just some subnets.
         
         gcloud auth revoke SHARED_VPC_ADMIN
         




###  API 

**Note:** These steps only cover attaching a service project to a host project. You must first have enabled a host project.

  1. Attach a service project to the Shared VPC host project.
         
         POST https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/enableXpnResource
         {
           "xpnResource": {
             "id": "SERVICE_PROJECT"
           }
         }
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
     * `SERVICE_PROJECT`: the ID of the service project to attach.

For more information, see the [`projects.enableXpnResource` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/enableXpnResource).

  2. Confirm that the service projects are attached to the host project.
         
         GET https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/getXpnResources
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.

For more information, see the [`projects.getXpnResources` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/getXpnResources).




### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_shared_vpc_service_project) to attach a service project.
    
    
    resource "google_compute_shared_vpc_service_project" "service1" {
      host_project    = google_compute_shared_vpc_host_project.host.project
      service_project = var.service_project # Replace this with your service project ID in quotes
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Service Project Admins for all subnets

A Shared VPC Admin can assign an IAM principal from a service project to be a _Service Project Admin_ with access to all subnets in the host project. Service Project Admins of this type are granted the role of `compute.networkUser` for _the whole host project_. This means that they have access to all of the defined and future subnets in the host project.

A user who has the `compute.networkUser` role in the host project can see all subnets within attached service projects.

**Note:** If you cannot create new resources in a particular subnet, an organization policy might be constraining the subnets that this project can use. For more information, see [`constraints/compute.restrictSharedVpcSubnetworks` constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

###  Console 

To define an IAM principal from a service project as Service Project Admin with access to all subnets in a host project using the Google Cloud console, see the attach service projects section.

###  gcloud 

These steps cover defining an IAM principal from a service project as a Service Project Admin with access to all subnets in a host project. Before you can perform these steps, you must have enabled a host project and attached the service project to the host project.

  1. If you have not already, authenticate to `gcloud` as a Shared VPC Admin. Replace `SHARED_VPC_ADMIN` with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. Create a policy binding to make an IAM principal from the service project a Service Project Admin. Replace `HOST_PROJECT_ID` with the project ID for the host project and `SERVICE_PROJECT_ADMIN` with the email address of the Service Project Admin user.
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
         --member "user:SERVICE_PROJECT_ADMIN" \
         --role "roles/compute.networkUser"
         

You can specify different types of principals by [changing the format of the `--member` argument](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):

     * Use `group:` to specify a Google group (by email address) as a principal.
     * Use `domain:` to specify a Google domain as a principal.
     * Use `serviceAccount:` to specify a service account. Refer to Service Accounts as Service Project Admins for more information about this use case.
  3. Repeat the previous step for each additional Service Project Admin you need to define.

  4. If you are finished defining Service Project Admins, you can log out of `gcloud` to protect your Shared VPC Admin account credentials.
         
         gcloud auth revoke SHARED_VPC_ADMIN
         




###  API 

  1. Describe and then record the details of your existing project policy. You'll need the existing policy and `etag` value.
         
         POST https://cloudresourcemanager.googleapis.com/v2/projects/HOST_PROJECT_ID:getIamPolicy
         

Replace `HOST_PROJECT_ID` with the ID of the Shared VPC host project.

  2. Create a policy binding to designate IAM principals in the service project as Service Project Admins.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/HOST_PROJECT_ID:setIamPolicy
         {
           "bindings": [
             ...copy existing bindings
             {
               "members": [
                 PRINCIPAL,
                 ...additional principals
               ],
               "role": "roles/compute.networkUser"
             },
           ],
           "etag": "ETAG",
           "version": 1,
           ...other existing policy details
         }
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the host project that contains the Shared VPC network.
     * `PRINCIPAL`: an identity that the role is associated with, such as a user, group, domain, or service account. For more information, see the [`members`](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Binding) field in the Resource Manager documentation.
     * `ETAG`: a unique identifier that you got when you described the existing policy. It prevents collisions if multiple updates requests are sent at the same time.

For more information, see the [`projects.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy).




### Service Project Admins for some subnets

A Shared VPC Admin can assign an IAM principal from a service project to be a _Service Project Admin_ with access to only some of the subnets in the host project. This option provides a more granular means to define Service Project Admins by granting them the `compute.networkUser` role for only some subnets in the host project.

A user who has the `compute.networkUser` role in the host project can see all subnets within attached service projects.

###  Console 

To define an IAM principal from a service project as Service Project Admin with access to only some subnets in a host project using the Google Cloud console, see the attach service projects section.

###  gcloud 

These steps cover defining IAM principals from a service project as Service Project Admins with access to only some subnets in a host project. Before you can define them, you must have enabled a host project and attached the service project to the host project.

  1. If you have not already, authenticate to `gcloud` as a Shared VPC Admin. Replace `SHARED_VPC_ADMIN` with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. Choose the subnet in the host project to which the Service Project Admins should have access. Get its current IAM policy in JSON format. Replace `SUBNET_NAME` with the name of the subnet in the host project and `HOST_PROJECT_ID` with the project ID for the host project.
         
         gcloud compute networks subnets get-iam-policy SUBNET_NAME \
             --region SUBNET_REGION \
             --project HOST_PROJECT_ID \
             --format json
         

  3. Copy the JSON output from the previous step and save it to a file. For instructional clarity, these steps save it to a file named `subnet-policy.json`.

  4. Modify the `subnet-policy.json` file, adding the IAM principals who will become Service Project Admins with access to the subnet. Replace each `SERVICE_PROJECT_ADMIN` with the email address of an IAM user from the service project.
         
         {
           "bindings": [
           {
              "members": [
                    "user:[SERVICE_PROJECT_ADMIN]",
                    "user:[SERVICE_PROJECT_ADMIN]"
                 ],
                 "role": "roles/compute.networkUser"
           }
           ],
           "etag": "[ETAG_STRING]"
         }
         

Note that you can specify different types of IAM principals (other than users) in [the policy](https://docs.cloud.google.com/iam/reference/rest/v1/Policy):

     * Switch `user:` with `group:` to specify a Google group (by email address) as a principal.
     * Switch `user:` with `domain:` to specify a Google domain as a principal.
     * Use `serviceAccount:` to specify a service account. Refer to Service Accounts as Service Project Admins for more information for this use case.
  5. Update the policy binding for the subnet using the contents of the `subnet-policy.json` file.
         
         gcloud compute networks subnets set-iam-policy SUBNET_NAME subnet-policy.json \
             --region SUBNET_REGION \
             --project HOST_PROJECT_ID
         

  6. If you are finished defining Service Project Admins, you can log out of `gcloud` to protect your Shared VPC Admin account credentials.
         
         gcloud auth revoke SHARED_VPC_ADMIN
         




###  API 

  1. Describe and then record the details of your existing subnet policy. You'll need the existing policy and `etag` value.
         
         GET https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/SUBNET_REGION/subnetworks/SUBNET_NAME/getIamPolicy
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the host project that contains the Shared VPC network.
     * `SUBNET_NAME`: the name of the subnet to share.
     * `SUBNET_REGION`: the region in which the subnet is located.
  2. Grant Service Project Admins access to subnets in the host project by updating the subnet policy.
         
         POST https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/SUBNET_REGION/subnetworks/SUBNET_NAME/setIamPolicy
         {
           "bindings": [
             ...copy existing bindings
             {
               "members": [
                 PRINCIPAL,
                 ...additional principals
               ],
               "role": "roles/compute.networkUser"
             },
           ],
           "etag": "ETAG",
           "version": 1,
           ...other existing policy details
         }
         

Replace the following:

     * `ETAG`: a unique identifier that you got when you described the existing policy. It prevents collisions if multiple updates requests are sent at the same time.
     * `HOST_PROJECT_ID`: the ID of the host project that contains the Shared VPC network.
     * `PRINCIPAL`: an identity that the role is associated with, such as a user, group, domain, or service account. For more information, see the [`members`](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Binding) field in the Resource Manager documentation.
     * `SUBNET_NAME`: the name of the subnet to share.
     * `SUBNET_REGION`: the region in which the subnet is located.

For more information, see the [`subnetworks.setIamPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/setIamPolicy).




### Service Accounts as Service Project Admins

A Shared VPC Admin can also define [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) from service projects as Service Project Admins. This section illustrates how to define _two different types of service accounts_ as Service Project Admins:

  * [User-managed service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) having this format: `USER_ID`@`SERVICE_PROJECT_ID`.iam.gserviceaccount.com

  * The [Google APIs service account](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed_service_accounts) having this format: `SERVICE_PROJECT_NUMBER`@cloudservices.gserviceaccount.com




The Service Project Admin role (`compute.networkUser`) [can be granted](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts) for all subnets or only some subnets of the host project. However, for instructional simplicity, this section only illustrates how to define each of the two service account types as Service Project Admins for all subnets of the host project.

#### User-managed service accounts as Service Project Admins

These directions describe how to define a user-managed service account as a Service Project Admin for all subnets of the Shared VPC host project.

###  Console 

  1. Log into the Google Cloud console as a Shared VPC Admin.
  2. In the Google Cloud console, go to the **Settings** page.   
[Go to the Settings page](https://console.cloud.google.com/iam-admin/settings/project)
  3. Change the project to the service project that contains the service account that needs to be defined as a Service Project Admin.
  4. Copy the **Project ID** of the service project. For instructional clarity, this procedure refers to the service project ID as `SERVICE_PROJECT_ID`.
  5. Change the project to the Shared VPC host project.
  6. Go to the IAM page in the Google Cloud console.   
[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam/project)
  7. Click **Add**.
  8. Add `SERVICE_ACCOUNT_NAME`@`SERVICE_PROJECT_ID`.iam.gserviceaccount.com to the **Principals** field, replacing `SERVICE_ACCOUNT_NAME` with the name of the service account.
  9. Select **Compute Engine > Compute Network User** from the **Roles** menu.
  10. Click **Add**.



###  gcloud 

  1. If you have not already, authenticate to `gcloud` as a Shared VPC Admin. Replace `SHARED_VPC_ADMIN` with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. If you don't know the project ID for the service project, you can list all projects in your organization. This list shows the project ID for each.
         
         gcloud projects list
         

  3. Create a policy binding to make the service account a Service Project Admin. Replace `HOST_PROJECT_ID` with the project ID for the host project,`SERVICE_ACCOUNT_NAME` with the name of the service account, and `SERVICE_PROJECT_ID` with the service project ID.
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
             --member "serviceAccount:SERVICE_ACCOUNT_NAME@SERVICE_PROJECT_ID.iam.gserviceaccount.com" \
             --role "roles/compute.networkUser"
         




###  API 

  1. Describe and then record the details of your existing project policy. You'll need the existing policy and `etag` value.
         
         POST https://cloudresourcemanager.googleapis.com/v2/projects/HOST_PROJECT_ID:getIamPolicy
         

Replace `HOST_PROJECT_ID` with the ID of the Shared VPC host project.

  2. Create a policy binding to designate service accounts as Service Project Admins.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/HOST_PROJECT_ID:setIamPolicy
         {
           "bindings": [
             ...copy existing bindings
             {
               "members": [
                 "serviceAccount:SERVICE_ACCOUNT_NAME@SERVICE_PROJECT_ID.iam.gserviceaccount.com",
                 ...include additional service accounts
               ],
               "role": "roles/compute.networkUser"
             },
           ],
           "etag": "ETAG",
           "version": 1,
           ...other existing policy details
         }
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the host project that contains the Shared VPC network.
     * `SERVICE_ACCOUNT_NAME`: the name of the service account.
     * `SERVICE_PROJECT_ID`: the ID of the service project that contains the service account.
     * `ETAG`: a unique identifier that you got when you described the existing policy. It prevents collisions if multiple updates requests are sent at the same time.

For more information, see the [`projects.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy).




#### Google APIs service account as a Service Project Admin

These directions describe how to define the _Google APIs service account_ as a Service Project Admin for all subnets of the Shared VPC host project. Making the Google APIs service account a Service Project Admin is a requirement for [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) used with Shared VPC because tasks like instance creation are performed by this type of service account. For more information about this relationship, see [Managed Instance Groups and IAM](https://docs.cloud.google.com/compute/docs/access/iam#managed-instance-groups-and-iam).

###  Console 

  1. Log into the Google Cloud console as a Shared VPC Admin.
  2. In the Google Cloud console, go to the **Settings** page.   
[Go to the Settings page](https://console.cloud.google.com/iam-admin/settings/project)
  3. Change the project to the service project that contains the service account that needs to be defined as a Service Project Admin.
  4. Copy the **Project number** of the service project. For instructional clarity, this procedure refers to the service project number as `SERVICE_PROJECT_NUMBER`.
  5. Change the project to the Shared VPC host project.
  6. Go to the IAM page in the Google Cloud console.   
[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam/project)
  7. Click **Add**.
  8. Add `SERVICE_PROJECT_NUMBER`@cloudservices.gserviceaccount.com to the **Members** field.
  9. Select **Compute Engine > Compute Network User** from the **Roles** menu.
  10. Click **Add**.



###  gcloud 

  1. If you have not already, authenticate to `gcloud` as a Shared VPC Admin. Replace `SHARED_VPC_ADMIN` with the name of the Shared VPC Admin:
         
         gcloud auth login SHARED_VPC_ADMIN
         

  2. Determine the _project number_ for the service project. For instructional clarity, this procedure refers to the service project number as `SERVICE_PROJECT_NUMBER`. Replace `SERVICE_PROJECT_ID` with the project ID for the service project.
         
         gcloud projects describe SERVICE_PROJECT_ID --format='get(projectNumber)'
         

     * If you don't know the project ID for the service project, you can list all projects in your organization. This list shows the project number for each.
           
           gcloud projects list
           

  3. Create a policy binding to make the service account a Service Project Admin. Replace `HOST_PROJECT_ID` with the project ID for the host project and `SERVICE_PROJECT_NUMBER` with the service project number.
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
             --member "serviceAccount:SERVICE_PROJECT_NUMBER@cloudservices.gserviceaccount.com" \
             --role "roles/compute.networkUser"
         




###  API 

  1. Describe and then record the details of your existing project policy. You'll need the existing policy and `etag` value.
         
         POST https://cloudresourcemanager.googleapis.com/v2/projects/HOST_PROJECT_ID:getIamPolicy
         

Replace `HOST_PROJECT_ID` with the ID of the Shared VPC host project.

  2. List your project to find its project number.
         
         GET https://cloudresourcemanager.googleapis.com/v1/projects?filter=projectId="SERVICE_PROJECT_ID"
         

Replace `SERVICE_PROJECT_ID` with the ID of the service project where the service account is located.

  3. Create a policy binding to designate service accounts as Service Project Admins.
         
         POST https://cloudresourcemanager.googleapis.com/v1/projects/HOST_PROJECT_ID:setIamPolicy
         {
           "bindings": [
             ...copy existing bindings
             {
               "members": [
                 "serviceAccount:SERVICE_PROJECT_NUMBER@cloudservices.gserviceaccount.com"
               ],
               "role": "roles/compute.networkUser"
             },
           ],
           "etag": "ETAG",
           "version": 1,
           ...other existing policy details
         }
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the host project that contains the Shared VPC network.
     * `SERVICE_PROJECT_NUMBER`: the number of the service project that contains the service account.
     * `ETAG`: a unique identifier that you got when you described the existing policy. It prevents collisions if multiple updates requests are sent at the same time.

For more information, see the [`projects.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy).




## Use Shared VPC

After a Shared VPC Admin completes the tasks of enabling a host project, attaching the necessary service projects to it, and defining Service Project Admins for all or some of the host project subnets, the Service Project Admins can create instances, templates, and internal load balancers in the service projects by using the subnets of the host project.

All tasks in this section must be performed by a Service Project Admin.

It's important to note that a Shared VPC Admin only grants the Service Project Admins the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) to either the entire host project or only some of its subnets. Service Project Admins should also have the other roles necessary to administer their respective service projects. For example, a Service Project Admin could also be a [project owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or should at least have the [Compute Instance Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.instanceAdmin`) for the project.

**Caution:** The Compute Network User role and the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) have different permission sets. The Compute Network User role includes permissions that are not available in the Compute Network Admin role. An IAM principal that has the Compute Network Admin role for an organization or project but lacks the Compute Network User role for the host project, or at least one of the subnets in the host project, is not a Service Project Admin.

### List available subnets

Service Project Admins can list the subnets to which they have been given permission by following these steps.

###  Console 

In the Google Cloud console, go to the **Shared VPC** page.

[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/details)

###  gcloud 

  1. If you have not already, authenticate to `gcloud` as a Service Project Admin. Replace `SERVICE_PROJECT_ADMIN` with the name of the Service Project Admin:
         
         gcloud auth login SERVICE_PROJECT_ADMIN
         

  2. Run the following command, replacing `HOST_PROJECT_ID` with the project ID of the Shared VPC host project:
         
         gcloud compute networks subnets list-usable --project HOST_PROJECT_ID
         

The following example lists the available subnets in the `project-1` host project:
         
         $ gcloud compute networks subnets list-usable --project project-1
         
         PROJECT    REGION       NETWORK  SUBNET    RANGE          SECONDARY_RANGES
         project-1  us-west1     net-1    subnet-1  10.138.0.0/20
         project-1  us-central1  net-1    subnet-2  10.128.0.0/20  r-1 192.168.2.0/24
                                                                   r-2 192.168.3.0/24
         project-1  us-east1     net-1    subnet-3  10.142.0.0/20
         




For more information, see the [`list-usable` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list-usable) in the SDK documentation.

###  API 

List the available subnets in the host project. Make the request as a Service Project Admin.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/aggregated/subnetworks/listUsable
    

Replace `HOST_PROJECT_ID` with the ID of the Shared VPC host project.

For more information, see the [`subnetworks.listUsable` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/listUsable).

### Reserve a static internal IPv4 or IPv6 address

Service Project Admins can reserve an internal IPv4 or IPv6 address in a subnet of a Shared VPC network. The IP address configuration object is created _in the service project_ , while its value comes from the range of available IPv4 addresses in the chosen shared subnet.

**Important:** A static internal IPv6 address that is reserved in a service project can be used only by resources within the same service project. Resources in the host project can't use a static internal IPv6 address that is reserved in a service project.

To reserve a standalone internal IP address in the service project, complete the following steps.

###  Console 

  1. Set up Shared VPC.
  2. In the Google Cloud console, go to the **Shared VPC** page.

[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/details)

  3. Sign in as a Shared VPC Admin.

  4. Select the service project from the project picker.

  5. Go to the **IP addresses** page by selecting **VPC network > IP addresses**.

  6. Click **Reserve internal**.

  7. In the **Name** field, enter an IP address name.

  8. In the **IP version** list, select the required IP version:

     * To reserve a static internal IPv4 address, select **IPv4**.
     * To reserve a static internal IPv6 address, select **IPv6**.
  9. Click the **Networks shared with me** button.

  10. In the **Network** and **Subnetwork** lists, select a VPC network and a subnet respectively.

  11. Specify how you want to reserve the IP address:

     * If you are reserving an IPv4 address, for **Static IP address** , choose one of the following: 
       * Select **Auto-allocated** to automatically allocate an IPv4 address.
       * Select **Let me choose** to choose a specific address. Enter the address in the **Custom IP address** field.
     * If you are reserving an IPv6 address, for **Static IPv6 range** , choose one of the following: 
       * Select **Auto-allocated (/96)** to automatically allocate an IPv6 address.
       * Select **Let me choose** to choose a specific address. Enter the address in the **Custom IPv6 address** field.
  12. Optional: If you want to share a static internal IPv4 address in different frontends, for **Purpose** , choose **Shared**. The default selection is **Non-shared**.

**Note:** You can't share a static internal IPv6 address across multiple load balancer frontends.
  13. Click **Reserve**.




###  gcloud 

  1. If you have not already, authenticate to the Google Cloud CLI as a Service Project Admin. Replace `SERVICE_PROJECT_ADMIN` with the name of the Service Project Admin:
         
         gcloud auth login SERVICE_PROJECT_ADMIN
         

  2. Use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).

     * Reserve IPv4 addresses:
           
           gcloud compute addresses create IP_ADDR_NAME \
               --project SERVICE_PROJECT_ID \
               --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET \
               --region=REGION
               --ip-version=IPV4
           

     * Reserve IPv6 addresses:
           
           gcloud compute addresses create IP_ADDR_NAME \
               --project SERVICE_PROJECT_ID \
               --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET \
               --region=REGION
               --ip-version=IPV6
           

Replace the following:

     * `IP_ADDR_NAME`: a name for the IPv4 address object.
     * `SERVICE_PROJECT_ID`: the ID of the service project.
     * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
     * `REGION`: the region that contains the shared subnet.
     * `SUBNET`: the name of the shared subnet.



Additional details for creating IP addresses are published in the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).

###  API 

Use the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert).

  * Reserve a static internal IPv4 address as a Service Project Admin:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/regions/REGION/addresses
        {
        "name": "ADDRESS_NAME",
        "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
        "addressType": "INTERNAL"
        }
        




Replace the following:

  * `ADDRESS_NAME`: a name for the reserved internal IP address.
  * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
  * `REGION`: the region where the reserved IPv4 address will be located and where the shared subnet is located.
  * `SERVICE_PROJECT_ID`: the ID of the service project where you are reserving the IPv4 address.
  * `SUBNET_NAME`: the name of the shared subnet.



For more information, see the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert).

### Terraform

You can use a Terraform data block to specify the [host subnet information](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork). Then use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_address) to reserve a static internal IPv4 address. If you omit the optional `address` argument, an available IPv4 address is selected and reserved.

Specify the host subnet:
    
    
    data "google_compute_subnetwork" "subnet" {
      name    = "my-subnet-123"
      project = var.project
      region  = "us-central1"
    }

Reserve an IPv4 address from the host project's subnet to use in the service project:
    
    
    resource "google_compute_address" "internal" {
      project      = var.service_project
      region       = "us-central1"
      name         = "int-ip"
      address_type = "INTERNAL"
      address      = "10.0.0.8"
      subnetwork   = data.google_compute_subnetwork.subnet.self_link
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Reserve a static external IPv4 address

A resource in a service project can use a regional static external IPv4 address that is defined in either the service project or the host project. Therefore, a resource in the attached service projects can use a regional static [external IPv4 address that is reserved](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static) in the host project.

### Reserve a static external IPv6 address

**Note:** The Google Cloud console doesn't support selecting the IPv6 network tier. To explicitly set external IPv6 addresses to Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages)), use the gcloud CLI or the API.

Service Project Admins can reserve a static external IPv6 address in a service project. The IPv6 address configuration object is created _in the service project_ , while its value comes from the range of available IPv6 addresses in the chosen shared subnet.

###  Console 

You can reserve a standalone external IPv6 address in the service project using the Google Cloud console:

  1. [Set up Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#set-up-shared-vpc).
  2. In the Google Cloud console, go to the Shared VPC page.   
[Go to the Shared VPC page](https://console.cloud.google.com/networking/xpn/details)
  3. Sign in as a Shared VPC Admin.
  4. Select the service project from the project picker.
  5. To go to the **IP addresses** page, select **VPC network > IP addresses**.
  6. Click **Reserve external**.
  7. Choose a name for the new address.
  8. Specify whether the network service tier is **Premium** or **Standard**.
  9. Under **IP version** , select **IPv6**.
  10. To reserve a global IPv6 address for a global load balancer, choose **Global** and click **Reserve**.
  11. To reserve a regional IPv6 address for an instance or a regional load balancer, click **Regional** and then do the following:

     1. Select the region to create the address in.
     2. Select **Networks shared with me**.
     3. Select the VPC network and subnet that you want to reserve the IP address from.
     4. For **Static IPv6 range** , select one of the following: 
        * Select **Auto-allocated** to automatically allocate an IPv6 address.
        * Select **Let me choose** to choose a specific address. Enter the address in the **Custom IPv6 address** field.
     5. For **Endpoint type** , select **VM instance** or **External passthrough Network Load Balancer**.

Optional: If you select **VM instance** , you can select a VM instance to attach the IPv6 address to.

     6. Click **Reserve**.




###  gcloud 

  1. If you have not already, authenticate to `gcloud` as a Service Project Admin. Replace `SERVICE_PROJECT_ADMIN` with the name of the Service Project Admin:
         
         gcloud auth login SERVICE_PROJECT_ADMIN
         

  2. Use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create):
         
         gcloud compute addresses create IP_ADDR_NAME \
             --project SERVICE_PROJECT_ID \
             --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET \
             --region=REGION \
             --ip-version=IPV6 \
             --endpoint-type=[VM | NETLB]
         

Replace the following:

     * `IP_ADDR_NAME`: a name for the IPv6 address object.
     * `SERVICE_PROJECT_ID`: the ID of the service project.
     * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
     * `SUBNET`: the name of the shared subnet.
     * `REGION`: the region that contains the shared subnet.



###  API 

To reserve a static internal IPv6 address as a Service Project Admin, use the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/regions/REGION/addresses
    {
      "name": "ADDRESS_NAME",
      "ipVersion": "IPV6",
      "ipv6EndpointType": "VM|LB",
      "networkTier": "IPV6_NETWORK_TIER",
      "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
      "addressType": "EXTERNAL"
    }
    

Replace the following:

  * `SERVICE_PROJECT_ID`: the ID of the service project where you are reserving the IPv6 address.
  * `REGION`: the region where the reserved IPv6 address and the shared subnet are located.
  * `ADDRESS_NAME`: a name for the reserved static external IPv6 address.
  * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.
  * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
  * `SUBNET_NAME`: the name of the shared subnet.



### Create an instance

Keep the following in mind when you use Shared VPC to create an instance:

  * The standard process for [creating an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) involves selecting a zone, a network, and a subnet. Both the selected subnet and the selected zone must be in the same region. When a Service Project Admin creates an instance by using a subnet from a Shared VPC network, the zone selected for that instance must be in the same region as the selected subnet.

When you create an instance with a reserved static internal IPv4 address, the subnet and region are already selected when the static IPv4 address is created. A `gcloud` example for creating an instance with a static internal IPv4 address is given in this section.

  * Service Project Admins can only create instances by using subnets to which they have been granted permission. To determine which subnets are available, see List available subnets.

  * When Google Cloud receives a request to create an instance in a subnet of a Shared VPC network, it checks to see if the IAM principal making the request has permission to use that shared subnet. If the check fails, the instance is not created, and Google Cloud returns a permissions error. For assistance, contact the Shared VPC Admin.

  * The stack type of the instance that you create must be supported by the shared subnetwork in which you create the instance. For more information, see [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types). For instances with IPv6 addresses, the IPv6 access type of the subnet determines whether the IPv6 address assigned to the instance is an internal or external IPv6 address.


**Note:** The Google Cloud console doesn't support selecting the IPv6 network tier. To explicitly set external IPv6 addresses to Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages)), use the gcloud CLI or the API.

###  Console 

  1. [Set up Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#set-up-shared-vpc).
  2. In the Google Cloud console, go to the **Shared VPC** page.

[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/details)

  3. Sign in as a Shared VPC Admin.

  4. Select the service project from the project picker.

  5. To go to the **Create an instance** page, select **Compute Engine > VM instances > Create instance**.

  6. Specify a **Name** for the instance.

  7. For **Region** , select a region that contains a shared subnetwork.

  8. Click **Networking** under **Advanced options**.

  9. Under **Network interfaces** , click the **Networks shared with me** radio button.

  10. In the **Shared subnetwork** list, select the required subnet where you want to create the instance:

     * For an IPv4-only instance, select an IPv4-only or dual-stack (IPv4 and IPv6) subnet.
     * For a dual-stack instance, select a dual-stack subnet with the required IPv6 access type.
     * For an IPv6-only instance, select a dual-stack subnet or an IPv6-only subnet with the required IPv6 access type.
  11. Select the **IP stack type** :

     * **IPv4 (single-stack)**
     * **IPv4 and IPv6 (dual-stack)**
     * **IPv6 (single-stack)**
  12. Specify any other necessary parameters for the instance.

  13. Click **Create**.




###  gcloud 

See the following examples:

  * Create an instance with an ephemeral internal IPv4 address in a shared subnet of a Shared VPC network:
        
        gcloud compute instances create INSTANCE_NAME \
            --project SERVICE_PROJECT_ID \
            --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET \
            --zone ZONE
        

Replace the following:

    * `INSTANCE_NAME`: the name of the instance.
    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET`: the name of the shared subnet.
    * `ZONE`: a zone in the specified region.
  * Create an instance with a reserved static internal IPv4 address in a Shared VPC network:

    1. Reserve a static internal IPv4 address in the service project from the range of available addresses of the host project.
    2. Create the instance:
           
           gcloud compute instances create INSTANCE_NAME \
               --project SERVICE_PROJECT_ID \
               --private-network-ip IP_ADDR_NAME \
               --zone ZONE \
               --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET
           

Replace the following:

       * `INSTANCE_NAME`: the name of the instance.
       * `SERVICE_PROJECT_ID`: the ID of the service project.
       * `IP_ADDR_NAME`: the name of the static IP address.
       * `ZONE`: a zone in the same region as `IP_ADDR_NAME`.
       * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
       * `REGION`: the region that contains the shared subnet.
       * `SUBNET`: the name of the shared subnet that's associated with the static internal IPv4 address.
  * Create an instance with an ephemeral internal IPv4 address and an ephemeral IPv6 address:
        
        gcloud compute instances create INSTANCE_NAME \
            --project SERVICE_PROJECT_ID \
            --stack-type IPV4_IPV6 \
            --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET \
            --zone ZONE
        

Replace the following:

    * `INSTANCE_NAME`: the name of the instance.
    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET`: the name of the shared subnet.
    * `ZONE`: a zone in the specified region.
  * Create an instance with a reserved static external IPv6 address:
        
        gcloud compute instances create INSTANCE_NAME \
            --project SERVICE_PROJECT_ID \
            --stack-type STACK_TYPE \
            --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET \
            --ipv6-address IPV6_ADDRESS \
            --external-ipv6-prefix-length=96 \
            --ipv6-network-tier IPV6_NETWORK_TIER \
            --zone ZONE
        

Replace the following:

    * `INSTANCE_NAME`: the name of the instance.
    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `STACK_TYPE`: `IPV4_IPV6` or `IPV6_ONLY`, depending on whether you want the instance to also have an IPv4 address.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET`: the name of the shared subnet.
    * `IPV6_ADDRESS`: the IPv6 address to assign to the VM.
    * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.
    * `ZONE`: a zone in the specified region.



###  API 

See the following examples:

  * To create an instance with an ephemeral internal IPv4 address, specify only the subnet:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/zones/ZONE/instances
        {
          "machineType": "MACHINE_TYPE",
          "name": "INSTANCE_NAME",
          "networkInterfaces": [
            {
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"
            }
          ],
          "disks": [
            {
              "boot": true,
              "initializeParams": {
                "sourceImage": "SOURCE_IMAGE"
              }
            }
          ]
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `ZONE`: a zone in the specified region.
    * `MACHINE_TYPE`: a machine type for the instance.
    * `INSTANCE_NAME`: a name for the instance.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET`: the name of the shared subnet.
    * `SOURCE_IMAGE`: an image for the instance.

For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

  * To create an instance with a reserved internal IPv4 address, specify the subnet and the name of the reserved IPv4 address:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/zones/ZONE/instances
        {
          "machineType": "MACHINE_TYPE",
          "name": "INSTANCE_NAME",
          "networkInterfaces": [
            {
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
              "networkIP": "projects/SERVICE_PROJECT_ID/regions/REGION/addresses/ADDRESS_NAME"
            }
          ],
          "disks": [
            {
              "boot": true,
              "initializeParams": {
                "sourceImage": "SOURCE_IMAGE"
              }
            }
          ]
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `ZONE`: a zone in the specified region.
    * `MACHINE_TYPE`: a machine type for the instance.
    * `INSTANCE_NAME`: a name for the instance.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET_NAME`: the name of the shared subnet.
    * `ADDRESS_NAME`: the name of the reserved internal IPv4 address.
    * `SOURCE_IMAGE`: an image for the instance.

For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

  * To create an instance with an ephemeral internal IPv4 address and an ephemeral IPv6 address, specify the subnet and the stack type:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/zones/ZONE/instances
        {
          "machineType": "MACHINE_TYPE",
          "name": "INSTANCE_NAME",
          "networkInterfaces": [
            {
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
              "stackType": "IPV4_IPV6"
            }
          ],
          "disks": [
            {
              "boot": true,
              "initializeParams": {
                "sourceImage": "SOURCE_IMAGE"
              }
            }
          ]
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `ZONE`: a zone in the specified region.
    * `MACHINE_TYPE`: a machine type for the instance.
    * `INSTANCE_NAME`: a name for the instance.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET`: the name of the shared subnet.
    * `SOURCE_IMAGE`: an image for the instance.

For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

  * To create an instance with an ephemeral IPv6 address, specify the subnet and the stack type:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/zones/ZONE/instances
        {
          "machineType": "MACHINE_TYPE",
          "name": "INSTANCE_NAME",
          "networkInterfaces": [
            {
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
              "stackType": "IPV6_ONLY"
            }
          ],
          "disks": [
            {
              "boot": true,
              "initializeParams": {
                "sourceImage": "SOURCE_IMAGE"
              }
            }
          ]
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `ZONE`: a zone in the specified region.
    * `MACHINE_TYPE`: a machine type for the instance.
    * `INSTANCE_NAME`: a name for the instance.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET`: the name of the shared subnet.
    * `SOURCE_IMAGE`: an image for the instance.

For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).




### Terraform

You can use a Terraform data block to specify the [host subnet information](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork). Then use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to create a VM instance in a service project.

Specify the host subnet:
    
    
    data "google_compute_subnetwork" "subnet" {
      name    = "my-subnet-123"
      project = var.project
      region  = "us-central1"
    }

Create a VM instance in a service project with an ephemeral IPv4 address from the host project's shared subnet:
    
    
    resource "google_compute_instance" "ephemeral_ip" {
      project      = var.service_project
      zone         = "us-central1-a"
      name         = "my-vm"
      machine_type = "e2-medium"
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-9"
        }
      }
      network_interface {
        subnetwork = data.google_compute_subnetwork.subnet.self_link
      }
    }

Create a VM instance in a service project with a reserved static IPv4 address from the host project's shared subnet:
    
    
    resource "google_compute_instance" "reserved_ip" {
      project      = var.service_project
      zone         = "us-central1-a"
      name         = "reserved-ip-instance"
      machine_type = "e2-medium"
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-9"
        }
      }
      network_interface {
        subnetwork = data.google_compute_subnetwork.subnet.self_link
        network_ip = google_compute_address.internal.address
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Create an instance template

**Note:** Connecting to a Shared VPC network by using interfaces other than `nic0` is supported for the following configurations: 

* Instance templates: supported in the gcloud CLI and the API.
* Managed instance groups: supported in the gcloud CLI and the API.

Keep the following in mind when you use Shared VPC to create an instance template:

  * The process for [creating an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) involves selecting a network and a subnet.

    * Templates created for use in a custom mode Shared VPC network must specify both the network and a subnet.

    * Templates created for use in an [auto mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) Shared VPC network may optionally defer selecting a subnet. In these cases, a subnet is automatically selected in the same region as any managed instance group that uses the template. (Auto mode networks have a subnet in every region by definition.)

  * When an IAM principal creates an instance template, Google Cloud does not perform a permissions check to see if the principal can use the specified subnet. This permissions check is always deferred to when a managed instance group that uses the template is requested.

  * The stack type of the instance template that you create must be supported by the shared subnetwork in which you create the instance template. For more information, see [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types). For instances with IPv6 addresses, the IPv6 access type of the subnet determines whether the IPv6 address assigned to the instance is an internal or external IPv6 address.




###  Console 

  1. [Set up Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#set-up-shared-vpc).
  2. In the Google Cloud console, go to the Shared VPC page.   
[Go to the Shared VPC page](https://console.cloud.google.com/networking/xpn/details)
  3. Sign in as a Shared VPC Admin.
  4. Select the service project from the project picker.
  5. To go to the **Create an instance template** page, select **Compute Engine > Instance templates > Create instance templates**.
  6. Specify a **Name** for the instance template.
  7. In the **Advanced options** section, click **Networking**.
  8. In the **Network interfaces** section, click the **Networks shared with me** radio button.
  9. In the **Shared subnetwork** list, select the required subnet where you want to create the instance template: 
     * For an IPv4-only instance template, select an IPv4-only or dual-stack (IPv4 and IPv6) subnet.
     * For a dual-stack instance template, select a dual-stack subnet with the required IPv6 access type.
     * For an IPv6-only instance template, select a dual-stack subnet or an IPv6-only subnet with the required IPv6 access type.
  10. Select the **IP stack type** of the instance template: 
     * **IPv4 (single-stack)**
     * **IPv4 and IPv6 (dual-stack)**
     * **IPv6 (single-stack)**
  11. Specify any other necessary parameters for the instance template.
  12. Click **Create**.



###  gcloud 

  * Create an IPv4-only instance template for use in any automatically created subnet of an auto mode Shared VPC network:
        
        gcloud compute instance-templates create TEMPLATE_NAME \
            --project SERVICE_PROJECT_ID \
            --network projects/HOST_PROJECT_ID/global/networks/NETWORK
        

Replace the following:

    * `TEMPLATE_NAME`: the name of the template.
    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `NETWORK`: the name of the Shared VPC network.
  * To create an IPv4-only instance template for a manually created subnet in a Shared VPC network (either auto or custom mode):
        
        gcloud compute instance-templates create TEMPLATE_NAME \
            --project SERVICE_PROJECT_ID \
            --region REGION \
            --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET
        

Replace the following:

    * `TEMPLATE_NAME`: the name of the template.
    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `REGION`: the region that contains the shared subnet.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `SUBNET`: the name of the shared subnet.
  * Create a dual-stack instance template that uses a subnet in a custom mode Shared VPC network:
        
        gcloud compute instance-templates create TEMPLATE_NAME \
            --project SERVICE_PROJECT_ID \
            --stack-type IPV4_IPV6 \
            --region REGION \
            --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET
        

Replace the following:

    * `TEMPLATE_NAME`: the name of the template.
    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `REGION`: the region that contains the shared subnet.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `SUBNET`: the name of the shared subnet.
  * Create a IPv6-only instance template that uses a subnet in a custom mode Shared VPC network:
        
        gcloud compute instance-templates create TEMPLATE_NAME \
            --project SERVICE_PROJECT_ID \
            --stack-type IPV6_ONLY \
            --region REGION \
            --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET
        

Replace the following:

    * `TEMPLATE_NAME`: the name of the template.
    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `REGION`: the region that contains the shared subnet.
    * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
    * `SUBNET`: the name of the shared subnet.



###  API 

  * To create an IPv4-only instance template that uses any automatically created subnet of an auto mode Shared VPC network, specify the VPC network:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/global/instanceTemplates
        {
        "properties": {
          "networkInterfaces": [
            {
              "network": "projects/HOST_PROJECT_ID/global/networks/NETWORK"
            }
          ]
        ...
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `HOST_PROJECT_ID`: the ID of the project that contains the Shared VPC network.
    * `NETWORK`: the name of the Shared VPC network.

For more information, see the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create an IPv4-only instance template that uses a manually created subnet in a Shared VPC network (auto or custom mode), specify the subnet:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/global/instanceTemplates
        {
        "properties": {
          "networkInterfaces": [
            {
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"
            }
          ]
        ...
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `HOST_PROJECT_ID`: the ID of the project that contains the Shared VPC network.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET_NAME`: the name of the shared subnet.

For more information, see the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create a dual-stack instance template that uses a subnet in a custom mode Shared VPC network, specify the subnet and the stack type:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/global/instanceTemplates
        {
        "properties": {
          "networkInterfaces": [
            {
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
              "stackType": "IPV4_IPV6"
            }
          ]
        ...
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `HOST_PROJECT_ID`: the ID of the project that contains the Shared VPC network.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET_NAME`: the name of the shared subnet.

For more information, see the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create an IPv6-only instance template that uses a subnet in a custom mode Shared VPC network, specify the subnet and the stack type:
        
        POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/global/instanceTemplates
        {
        "properties": {
          "networkInterfaces": [
            {
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
              "stackType": "IPV6_ONLY"
            }
          ]
        ...
        }
        

Replace the following:

    * `SERVICE_PROJECT_ID`: the ID of the service project.
    * `HOST_PROJECT_ID`: the ID of the project that contains the Shared VPC network.
    * `REGION`: the region that contains the shared subnet.
    * `SUBNET_NAME`: the name of the shared subnet.

For more information, see the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).




### Terraform

You can use a Terraform data block to specify the [host subnet information](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork). Then use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template) to create a VM instance template. The IPv4 addresses for the VMs come from the host project's shared subnet.

The subnet must exist in the same region where the VM instances will be created.

Specify the host subnet:
    
    
    data "google_compute_subnetwork" "subnet" {
      name    = "my-subnet-123"
      project = var.project
      region  = "us-central1"
    }

Create a VM instance template in the service project:
    
    
    resource "google_compute_instance_template" "default" {
      project      = var.service_project
      name         = "appserver-template"
      description  = "This template is used to create app server instances."
      machine_type = "n1-standard-1"
      disk {
        source_image = "debian-cloud/debian-9"
      }
      network_interface {
        subnetwork = data.google_compute_subnetwork.subnet.self_link
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Create a managed instance group

**Note:** Connecting to a Shared VPC network using interfaces other than `nic0` is supported for the following configurations: 

  * Instance templates: supported in the gcloud CLI and the API.
  * Managed instance groups: supported in the gcloud CLI and the API. 



Keep the following in mind when creating a managed instance group using Shared VPC:

  * Managed instance groups used with Shared VPC require making the Google APIs service account a Service Project Admin because tasks like automatic instance creation using autoscaling are performed by that service account.

  * The standard process for [creating a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) involves selecting a zone or region, depending on the group type, and an instance template. (Network and subnet details are tied to the instance template.) Eligible instance templates are restricted to those that reference subnets in the same region used by the managed instance group.

  * Service Project Admins can only create managed instance groups whose member instances use subnets to which they have been granted permission. Because the network and subnet details are tied to the instance template, Service Project Admins can only use templates that reference subnets that they are authorized to use.

  * When Google Cloud receives a request to create a managed instance group, it checks to see if the IAM principal making the request has permission to use the subnet (in the same region as the group) specified in the instance template. If the check fails, the managed instance group is not created, and Google Cloud returns an error: `Required 'compute.subnetworks.use' permission for 'projects/SUBNET_NAME`.

List available subnets to determine which ones can be used, and contact the Shared VPC Admin if the service account needs additional access. For more information, see [Service Accounts as Service Project Admins](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#sa-as-spa).




For more information, refer to [Creating Groups of Managed Instances](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) in the Compute Engine documentation.

### Create an HTTP(S) load balancer

There are many ways to configure external Application Load Balancers within a Shared VPC network. Regardless of the type of deployment, all the components of the load balancer must be in the same organization and the same Shared VPC network.

To learn more about supported Shared VPC architectures, see the following:

  * [Shared VPC architecture for external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https).
  * [Shared VPC architecture for internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal).



### Create an internal passthrough Network Load Balancer

The following example illustrates what you must consider when creating an internal passthrough Network Load Balancer in a Shared VPC network. Service Project Admins can create an internal passthrough Network Load Balancer that uses a subnet (in the host project) to which they have access. The load balancer's [internal forwarding rule](https://docs.cloud.google.com/load-balancing/docs/internal#forwarding_rule) is defined in the service project, but its [subnet reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) points to a subnet in a Shared VPC network of the host project.

Before you create an internal passthrough Network Load Balancer in a Shared VPC environment, see the [Shared VPC architecture](https://docs.cloud.google.com/load-balancing/docs/internal#shared-vpc).

###  Console 

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/loadBalancers)

  2. Create your internal TCP/UDP load balancer, making the following adjustment: In the **Configure frontend services** section, select the Shared VPC subnet you need from the **Networks shared by other projects** section of the **Subnet** menu.

  3. Finish creating the load balancer.




###  gcloud 

When you create the internal forwarding rule, specify a subnet in the host project with the `--subnet` flag:
    
    
    gcloud compute forwarding-rules create FR_NAME \
        --project SERVICE_PROJECT_ID \
        --load-balancing-scheme internal \
        --region REGION \
        --ip-protocol IP_PROTOCOL \
        --ports PORT,PORT,... \
        --backend-service BACKEND_SERVICE_NAME \
        --subnet projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET \
        --address INTERNAL_IP
    

Replace the following:

  * `FR_NAME`: the name of the forwarding rule.
  * `SERVICE_PROJECT_ID`: the ID of the service project.
  * `REGION`: the region that contains the shared subnet.
  * `IP_PROTOCOL`: either `TCP` or `UDP`, matching the protocol of the load balancer's backend service.
  * `PORT`: the numeric port or list of ports for the load balancer.
  * `BACKEND_SERVICE_NAME`: the name of the backend service (created already as part of the general procedure for [creating an internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal)).
  * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
  * `SUBNET`: the name of the shared subnet.
  * `INTERNAL_IP`: an internal IP address in the shared subnet (if unspecified, an available one will be selected).



For more options, see the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).

###  API 

Create the internal forwarding rule and specify a subnet in the host project.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/regions/REGION/forwardingRules
    {
      "name": "FR_NAME",
      "IPAddress": "IP_ADDRESS",
      "IPProtocol": "IP_PROTOCOL",
      "ports": [ "PORT", ... ],
      "loadBalancingScheme": "INTERNAL",
      "subnetwork": "https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET",
      "network": "https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/global/networks/NETWORK_NAME",
      "backendService": "https://www.googleapis.com/compute/v1/projects/SERVICE_PROJECT_ID/regions/us-west1/backendServices/BE_NAME",
      "networkTier": "PREMIUM"
    }
    

Replace the following:

  * `SERVICE_PROJECT_ID`: the ID of the service project.
  * `REGION`: the region that contains the shared subnet.
  * `FR_NAME`: a name for the forwarding rule.
  * `IP_ADDRESS`: an internal IP address in the shared subnet.
  * `IP_PROTOCOL`: either `TCP` or `UDP`, matching the protocol of the load balancer's backend service.
  * `PORT`: the numeric port or list of ports for the load balancer.
  * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
  * `SUBNET`: the name of the shared subnet.
  * `NETWORK_NAME`: the name of the network.
  * `BE_NAME`: the name of the backend service (created already as part of the general procedure for [creating an internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal)).



For more information, see the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).

### Terraform

You can use a Terraform data block to specify the [host subnet](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork) and [host network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network). Then use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_forwarding_rule) to create the forwarding rule.

Specify the host network:
    
    
    data "google_compute_network" "network" {
      name    = "my-network-123"
      project = var.project
    }

Specify the host subnet:
    
    
    data "google_compute_subnetwork" "subnet" {
      name    = "my-subnet-123"
      project = var.project
      region  = "us-central1"
    }

In the service project, create a forwarding rule in the host project's network and subnet:
    
    
    resource "google_compute_forwarding_rule" "default" {
      project               = var.service_project
      name                  = "l4-ilb-forwarding-rule"
      backend_service       = google_compute_region_backend_service.default.id
      region                = "europe-west1"
      ip_protocol           = "TCP"
      load_balancing_scheme = "INTERNAL"
      all_ports             = true
      allow_global_access   = true
      network               = data.google_compute_network.network.self_link
      subnetwork            = data.google_compute_subnetwork.subnet.self_link
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## What's next

  * For more information about Shared VPC, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).
  * For instructions about setting up Google Kubernetes Engine clusters with Shared VPC, see [Set up clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc).
  * Learn how to set up access to a Shared VPC network from [Cloud Run](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#shared-vpc), [Cloud Run functions](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#shared-vpc), or the [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard/python3/connecting-vpc#shared-vpc).
  * For instructions about deleting a Shared VPC setup, see [Deprovision Shared VPC](https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
