---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc/
title: Configure clusters with Shared VPC \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:00.681367+00:00
---

# Configure clusters with Shared VPC  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure clusters with Shared VPC Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows how to create two Google Kubernetes Engine (GKE) clusters, in separate projects, that use a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). For general information about GKE networking, visit the [Network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).

The examples in this guide configure the infrastructure for a two-tier web application, as described in [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc#two-tier_web_service).

## Why use Shared VPC with GKE

With [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you designate one project as the host project, and you can attach other projects, called service projects, to the host project. You create networks, subnets, secondary address ranges, firewall rules, and other network resources in the host project. Then you share selected subnets, including secondary ranges, with the service projects. Components running in a service project can use the Shared VPC to communicate with components running in the other service projects.

You can use Shared VPC with [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) and with [zonal](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters) and [regional](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) Standard clusters.

Standard clusters that use Shared VPC cannot use [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) and must have [VPC-native traffic routing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) enabled. Autopilot clusters always enable VPC-native traffic routing.

You can configure Shared VPC when you create a new cluster. GKE does not support converting existing clusters to the Shared VPC model.

With Shared VPC, certain quotas and limits apply. For example there is a quota for the number of networks in a project, and there is a limit on the number of service projects that can be attached to a host project. For details, see [Quotas and limits](https://docs.cloud.google.com/vpc/docs/shared-vpc#quota).

## Before you begin

Before you start to set up a cluster with Shared VPC:

  * Ensure you have a [Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).
  * Ensure your organization has three [Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * Ensure that you're familiar with the [Shared VPC concepts](https://docs.cloud.google.com/vpc/docs/shared-vpc#concepts_and_terminology) including the various [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc) used by Shared VPC. The tasks in this guide need to be performed by a _Shared VPC Admin_.
  * Ensure that you're familiar with any organization policy constraints applicable to your organization, folder, or projects. An Organization Policy Administrator might have defined constraints that limit which projects can be Shared VPC host projects or that limit which subnets can be shared. Refer to [organization policy constraints](https://docs.cloud.google.com/vpc/docs/shared-vpc#organization_policy_constraints) for more information.



Before you perform the exercises in this guide:

  * Choose one of your projects to be the host project.
  * Choose two of your projects to be service projects.



Each project has a name, an ID, and a number. In some cases, the name and the ID are the same. This guide uses the following friendly names and placeholders to refer to your projects:

Friendly name | Project ID   
placeholder | Project number   
placeholder  
---|---|---  
Your host project | `HOST_PROJECT_ID` | `HOST_PROJECT_NUM`  
Your first service project | `SERVICE_PROJECT_1_ID` | `SERVICE_PROJECT_1_NUM`  
Your second service project | `SERVICE_PROJECT_2_ID` | `SERVICE_PROJECT_2_NUM`  
**Note:** Your first and second service projects don't come in order. The terms "first" and "second" are used only to distinguish one project from the other.

### Find your project IDs and numbers

You can find your project ID and numbers by using the gcloud CLI or the Google Cloud console.

### Console

  1. Go to the **Home** page of the Google Cloud console.

[Go to the Home page](https://console.cloud.google.com/)

  2. In the project picker, select the project that you have chosen to be the host project.

  3. Under **Project info** , you can see the project name, project ID, and project number. Make a note of the ID and number for later.

  4. Do the same for each of the projects that you have chosen to be service projects.




### gcloud

List your projects with the following command:
    
    
    gcloud projects list
    

The output shows your project names, IDs and numbers. Make a note of the ID and number for later:
    
    
    PROJECT_ID        NAME        PROJECT_NUMBER
    host-123          host        1027xxxxxxxx
    srv-1-456         srv-1       4964xxxxxxxx
    srv-2-789         srv-2       4559xxxxxxxx
    

### Enable the GKE API in your projects

Before you continue with the exercises in this guide, make sure that the GKE API is enabled in all three of your projects. Enabling the API in a project creates a GKE service agent for the project. To perform the remaining tasks in this guide, each of your projects must have a GKE service agent.

You can enable the GKE API using the Google Cloud console or the Google Cloud CLI.

### Console

  1. Go to the **Kubernetes Engine API page** in the Google Cloud console:

[Go to the **Kubernetes Engine API page**](https://console.cloud.google.com/apis/library/container.googleapis.com)

  2. Select your project.

  3. The GKE API is enabled if you see **API enabled** in the page header. If you don't see **API enabled** , then click the **Enable** button.

  4. Repeat these steps for each project that you have chosen to be a service project. Each operation may take some time to complete.




### gcloud

Enable the GKE API for your three projects. Each operation may take some time to complete:
    
    
    gcloud services enable container.googleapis.com --project HOST_PROJECT_ID
    gcloud services enable container.googleapis.com --project SERVICE_PROJECT_1_ID
    gcloud services enable container.googleapis.com --project SERVICE_PROJECT_2_ID
    

## Create a network and two subnets

In this section, you will perform the following tasks:

  1. In your host project, create a network named `shared-net`.
  2. Create two subnets named `tier-1` and `tier-2`.
  3. For each subnet, create two secondary address ranges: one for Services, and one for Pods.

**Note:** The secondary address ranges for Pods, Services and nodes must not overlap `172.17.0.0/16` and must follow [the defaults and limits for range sizes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#defaults_limits).

### Console

  1. Go to the **VPC networks** page in the Google Cloud console.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the project picker, select your host project.

  3. Click _add_box_ **Create VPC Network**.

  4. For **Name** , enter `shared-net`.

  5. Under **Subnet creation mode** , select **Custom**.




#### Add `tier-1`

  1. Under **Subnets** in the **New subnet** box, for **Name** , enter `tier-1`.
  2. For **Region** , select a region.
  3. Under **IP stack type** , select **IPv4 (single-stack)**.
  4. For **IPv4 range** , enter `10.0.4.0/22` as the [primary address range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges) for the subnet.
  5. Click **Add a secondary IPv4 range**.

     * For **Subnet range name** , enter `tier-1-services`.
     * For **Secondary IPv4 range** , enter `10.0.32.0/20`.
  6. Click **Done**.

  7. Click **Add a secondary IPv4 range**.

     * For **Subnet range name** , enter `tier-1-pods`.
     * For **Secondary IPv4 range** , enter `10.4.0.0/14`.
  8. Click **Done**.




#### Add `tier-2`

  1. Click **Add subnet**.
  2. For **Name** , enter `tier-2`.
  3. For **Region** , select the same region that you selected for the previous subnet.
  4. For **IPv4 range** , enter `172.16.4.0/22` as the primary address range for the subnet.
  5. Click **Add a secondary IPv4 range**.

     * For **Subnet range name** , enter `tier-2-services`.
     * For **Secondary IPv4 range** , enter `172.16.16.0/20`.
  6. Click **Done**.

  7. Click **Add a secondary IPv4 range**.

     * For **Subnet range name** , enter `tier-2-pods`.
     * For **Secondary IPv4 range** , enter `172.20.0.0/14`.
  8. Click **Done**.

  9. Go to the bottom of the page and click **Create**.




### gcloud

In your host project, create a network named `shared-net`:
    
    
    gcloud compute networks create shared-net \
        --subnet-mode custom \
        --project HOST_PROJECT_ID
    

In your new network, create a subnet named `tier-1`:
    
    
    gcloud compute networks subnets create tier-1 \
        --project HOST_PROJECT_ID \
        --network shared-net \
        --range 10.0.4.0/22 \
        --region COMPUTE_REGION \
        --secondary-range tier-1-services=10.0.32.0/20,tier-1-pods=10.4.0.0/14
    

Create another subnet named `tier-2`:
    
    
    gcloud compute networks subnets create tier-2 \
        --project HOST_PROJECT_ID \
        --network shared-net \
        --range 172.16.4.0/22 \
        --region COMPUTE_REGION \
        --secondary-range tier-2-services=172.16.16.0/20,tier-2-pods=172.20.0.0/14
    

Replace `COMPUTE_REGION` with a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).

## Determine the names of service agents in your service projects

You have two service projects, each of which has several [service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts). In the sections that follow, you interact with Google-managed service accounts, which are called [service agents](https://docs.cloud.google.com/iam/docs/service-accounts#service-agents), in these service projects. You need the names of these service agents for the next section.

The following table lists the names of the GKE and Google APIs service agents in your two service projects:

Service agent type | Service agent name  
---|---  
GKE | service-SERVICE_PROJECT_1_NUM@container-engine-robot.iam.gserviceaccount.com  
service-SERVICE_PROJECT_2_NUM@container-engine-robot.iam.gserviceaccount.com  
Google APIs | SERVICE_PROJECT_1_NUM@cloudservices.gserviceaccount.com  
SERVICE_PROJECT_2_NUM@cloudservices.gserviceaccount.com  
  
## Enable Shared VPC and grant roles

To perform the tasks in this section, you must be a [Shared VPC Admin](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_roles_required_for_shared_vpc). If you aren't a Shared VPC Admin, ask someone who is an Organization Admin to grant you the Compute Shared VPC Admin (**compute.xpnAdmin**) and Project IAM Admin (**resourcemanager.projectIamAdmin**) roles for the organization or one or more folders.

In this section, you will perform the following tasks:

  1. In your host project, enable Shared VPC.
  2. Attach your two service projects to the host project.
  3. Either remove or grant the `Compute Network User` role to the service agents that belong to your service projects. If you are using the Google Cloud console, you remove the role; and if you are using the gcloud CLI, you grant the role.



###  Console 

  1. Go to the **Shared VPC page** in the Google Cloud console.

[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/details)

  2. In the project picker, select your host project.

  3. Click **Set up Shared VPC**. The **Enable host project** screen is displayed.

  4. Click **Enable & continue**. The **Attach service projects and select principals** section is displayed.

  5. Under **Kubernetes Engine access** , select **Enabled**.

  6. Under **Select projects to attach** , click _add_box_**Add item**.

  7. In the **Select project** field, click **Select** and choose your first service project.

  8. Click _add_box_ **Add item** again, and select your second service project.

  9. Click **Continue**. The **Grant access** section is displayed.

  10. Under **Access mode** , select **Individual subnet access**.

  11. Under **Subnets with individual subnet access** , scroll through the list and select **tier-1** and **tier-2**.

  12. Click **Save**. A new page is displayed.

  13. Select **Only show subnets that have individual IAM policies**.




#### Remove service agents from `tier-1`

  1. Under **Individual subnet access** , select **tier-1** and click **Show Permissions Panel**.
  2. In the **Permissions Panel** under **Role/Principal** , expand **Compute Network User**.
  3. Search for `SERVICE_PROJECT_2_NUM`.
  4. Delete all the service agents that belong to your _second_ service project. That is, delete the service agents that contain `SERVICE_PROJECT_2_NUM`.
  5. Confirm that the following service agents for your _first_ service project are in the list with the **Compute Network User** role:

     * `service-SERVICE_PROJECT_1_NUM@container-engine-robot.iam.gserviceaccount.com`
     * `SERVICE_PROJECT_1_NUM@cloudservices.gserviceaccount.com`
     * `SERVICE_PROJECT_1_NUM-compute@developer.iam.gserviceaccount.com`

If a service agent isn't in the list, do the following to add it:

     1. Click _add_box_ **Add Principal**.
     2. In the **New principals** field, enter the service agent name.
     3. Under **Assign Roles** , select **Compute Network User**.
     4. Click **Save**.
  6. Under **Individual subnet access** , clear the **tier-1** checkbox.




#### Remove service agents from `tier-2`

  1. Under **Individual subnet access** , select **tier-2**.
  2. In the **Permissions Panel** under **Role/Principal** , expand **Compute Network User**.
  3. Search for `SERVICE_PROJECT_1_NUM`.
  4. Delete all the service agents that belong to your _first_ service project. That is, delete any service agents that contain `SERVICE_PROJECT_1_NUM`.
  5. Confirm that the following service agents for your _second_ service project are in the list with the **Compute Network User** role:

     * `service-SERVICE_PROJECT_2_NUM@container-engine-robot.iam.gserviceaccount.com`
     * `SERVICE_PROJECT_2_NUM@cloudservices.gserviceaccount.com`
     * `SERVICE_PROJECT_2_NUM-compute@developer.iam.gserviceaccount.com`

If a service agent isn't in the list, do the following to add it:

     1. Click _add_box_ **Add Principal**.
     2. Enter the service agent name in the **New principals** field.
     3. Under **Assign Roles** , select **Compute Network User**.
     4. Click **Save**.



###  gcloud 

  1. Enable Shared VPC in your host project. The command that you use depends on the [required administrative role](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_roles_required_for_shared_vpc) that you have.

**If you have Shared VPC Admin role at the organizational level:**
         
         gcloud compute shared-vpc enable HOST_PROJECT_ID
         

**If you have Shared VPC Admin role at the folder level:**
         
         gcloud beta compute shared-vpc enable HOST_PROJECT_ID
         

  2. Attach your first service project to your host project:
         
         gcloud compute shared-vpc associated-projects add SERVICE_PROJECT_1_ID \
             --host-project HOST_PROJECT_ID
         

  3. Attach your second service project to your host project:
         
         gcloud compute shared-vpc associated-projects add SERVICE_PROJECT_2_ID \
             --host-project HOST_PROJECT_ID
         

  4. Get the IAM policy for the `tier-1` subnet:
         
         gcloud compute networks subnets get-iam-policy tier-1 \
            --project HOST_PROJECT_ID \
            --region COMPUTE_REGION
         

The output contains an `etag` field. Make a note of the `etag` value.

  5. Create a file named `tier-1-policy.yaml` that has the following content:
         
         bindings:
         - members:
           - serviceAccount:SERVICE_PROJECT_1_NUM@cloudservices.gserviceaccount.com
           - serviceAccount:service-SERVICE_PROJECT_1_NUM@container-engine-robot.iam.gserviceaccount.com
           role: roles/compute.networkUser
         etag: ETAG_STRING
         

Replace `ETAG_STRING` with the `etag` value that you noted previously.

  6. Set the IAM policy for the `tier-1` subnet:
         
         gcloud compute networks subnets set-iam-policy tier-1 \
             tier-1-policy.yaml \
             --project HOST_PROJECT_ID \
             --region COMPUTE_REGION
         

  7. Get the IAM policy for the `tier-2` subnet:
         
         gcloud compute networks subnets get-iam-policy tier-2 \
             --project HOST_PROJECT_ID \
             --region COMPUTE_REGION
         

The output contains an `etag` field. Make a note of the `etag` value.

  8. Create a file named `tier-2-policy.yaml` that has the following content:
         
         bindings:
         - members:
           - serviceAccount:SERVICE_PROJECT_2_NUM@cloudservices.gserviceaccount.com
           - serviceAccount:service-SERVICE_PROJECT_2_NUM@container-engine-robot.iam.gserviceaccount.com
           role: roles/compute.networkUser
         etag: ETAG_STRING
         

Replace `ETAG_STRING` with the `etag` value that you noted previously.

  9. Set the IAM policy for the `tier-2` subnet:
         
         gcloud compute networks subnets set-iam-policy tier-2 \
             tier-2-policy.yaml \
             --project HOST_PROJECT_ID \
             --region COMPUTE_REGION
         




## Manage firewall resources

For a GKE cluster in a service project to create and manage the firewall resources in your host project, the service project's GKE service agent must be granted the appropriate IAM permissions. You can grant these permissions by using one of the following strategies:

**Note:** To follow security best practices, choose the finer grained approach. Granting the service project's GKE service agent the Compute Security Admin role will allow it more IAM permissions than is necessary for the purposes of this guide.

  * Grant the service project's GKE service agent the [`Compute Security Admin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) role to the host project.




###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select the host project.

  3. Click person_add **Grant access** , then enter the service project's GKE service agent principal, `service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com`.

  4. Select the `Compute Security Admin` role from the drop-down list.

  5. Click **Save**.




###  gcloud 

Grant the service project's GKE service agent the `Compute Security Admin` role within the host project:
    
    
    gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
        --member=serviceAccount:service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com \
        --role=roles/compute.securityAdmin
    

Replace the following:

  * `HOST_PROJECT_ID`: the shared VPC host project ID
  * `SERVICE_PROJECT_NUM`: the ID of the service project containing the GKE service agent



  * For a finer grained approach, [create a custom IAM role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role) that includes only the following permissions: `compute.networks.updatePolicy`, `compute.firewalls.list`, `compute.firewalls.get`, `compute.firewalls.create`, `compute.firewalls.update`, and `compute.firewalls.delete`. Grant the service project's GKE service agent that custom role to the host project.




###  Console 

Create a custom role within the host project containing the IAM permissions mentioned earlier:

  1. In the Google Cloud console, go to the **Roles** page.

[ Go to the Roles page](https://console.cloud.google.com/iam-admin/roles)

  2. Using the drop-down list at the top of the page, select the host project.

  3. Click **Create Role**.

  4. Enter a **Title** , **Description** , **ID** and **Role launch stage** for the role. The role name cannot be changed after the role is created.

  5. Click **Add Permissions**.

  6. Filter for `compute.networks` and select the IAM permissions mentioned previously.

  7. Once all required permissions are selected, click **Add**.

  8. Click **Create**.




Grant the service project's GKE service agent the newly created custom role within the host project:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select the host project.

  3. Click person_add **Grant access** , then enter the service project's GKE service agent principal, `service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com`.

  4. Filter for the **Title** of the newly created custom role and select it.

  5. Click **Save**.




###  gcloud 

  1. Create a custom role within the host project containing the IAM permissions mentioned earlier:
         
         gcloud iam roles create ROLE_ID \
             --title="ROLE_TITLE" \
             --description="ROLE_DESCRIPTION" \
             --stage=LAUNCH_STAGE \
             --permissions=compute.networks.updatePolicy,compute.firewalls.list,compute.firewalls.get,compute.firewalls.create,compute.firewalls.update,compute.firewalls.delete \
             --project=HOST_PROJECT_ID
         

  2. Grant the service project's GKE service agent the newly created custom role within the host project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
             --member=serviceAccount:service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com \
             --role=projects/HOST_PROJECT_ID/roles/ROLE_ID
         

Replace the following:

     * `ROLE_ID`: the name of the role, such as `gkeFirewallAdmin`
     * `ROLE_TITLE`: a friendly title for the role, such as `GKE Firewall Admin`
     * `ROLE_DESCRIPTION`: a short description of the role, such as `GKE service agent FW permissions`
     * `LAUNCH_STAGE`: the [launch stage](https://cloud.google.com/products#section-22) of the role in its lifecycle, such as `ALPHA`, `BETA`, or `GA`
     * `HOST_PROJECT_ID`: the shared VPC host project ID
     * `SERVICE_PROJECT_NUM`: the ID of the service project containing the GKE service agent



If you have clusters in more than one service project, you must choose one of the strategies and repeat it for each service project's GKE service agent.

**Note:** If you are using Ingress for internal Application Load Balancers, the Ingress controller does not create a firewall rule to allow connections from the load balancer proxies in the proxy-subnet. You must create this firewall rule manually. However, the Ingress controller does create firewall rules to allow ingress for Google Cloud health-checks.

### Summary of roles granted on subnets

Here's a summary of the roles granted on the subnets:

Service agent | Role | Subnet  
---|---|---  
service-SERVICE_PROJECT_1_NUM@container-engine-robot.iam.gserviceaccount.com | Compute Network User | tier-1  
SERVICE_PROJECT_1_NUM@cloudservices.gserviceaccount.com | Compute Network User | tier-1  
service-SERVICE_PROJECT_2_NUM@container-engine-robot.iam.gserviceaccount.com | Compute Network User | tier-2  
SERVICE_PROJECT_2_NUM@cloudservices.gserviceaccount.com | Compute Network User | tier-2  
  
### Verify GKE access

When attaching a service project, enabling GKE access grants the service project's GKE service agent the permissions to perform network management operations in the host project.

GKE assigns the following role automatically in the host project when enabling GKE access:

Member | Role | Resource  
---|---|---  
service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com | Host Service Agent User | GKE service agent in the host project  
  
However, you must add the `Compute Network User` IAM permission manually to the GKE service agent of the service project to access the host network.

Member | Role | Resource  
---|---|---  
service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com | Compute Network User | Specific subnet or whole host project  
  
If a service project was attached without enabling GKE access, assuming the GKE API has already been enabled in both the host and service project, you can manually assign the permissions to the service project's GKE service agent by adding the following IAM role bindings in the host project:

Member | Role | Resource  
---|---|---  
service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com | Compute Network User | Specific subnet or whole host project  
service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com | Host Service Agent User | GKE service agent in the host project  
  
## Grant the Host Service Agent User role

Each service project's GKE service agent must have a binding for the [Host Service Agent User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.hostServiceAgentUser) (`roles/container.hostServiceAgentUser`) role on the host project. The GKE service agent takes the following form:
    
    
    service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com
    

Where `SERVICE_PROJECT_NUM` is the project number of your service project.

This binding allows the service project's GKE service agent to perform network management operations in the host project, as if it were the host project's GKE service agent. This role can only be granted to a service project's GKE service agent.

### Console

If you have been using the Google Cloud console, you do not have to grant the Host Service Agent User role explicitly. That was done automatically when you used the Google Cloud console to attach service projects to your host project.

### gcloud

  1. For your first project, grant the Host Service Agent User role to the project's GKE service agent. This role is granted on your host project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
             --member serviceAccount:service-SERVICE_PROJECT_1_NUM@container-engine-robot.iam.gserviceaccount.com \
             --role roles/container.hostServiceAgentUser
         

  2. For your second project, grant the Host Service Agent User role to the project's GKE service agent. This role is granted on your host project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
             --member serviceAccount:service-SERVICE_PROJECT_2_NUM@container-engine-robot.iam.gserviceaccount.com \
             --role roles/container.hostServiceAgentUser
         




## Verify usable subnets and secondary IP address ranges

When creating a cluster, you must specify a subnet and the secondary IP address ranges to be used for the cluster's Pods and Services. There are several reasons that an IP address range might not be available for use. Whether you are creating the cluster with the Google Cloud console or the gcloud CLI, you should specify usable IP address ranges.

An IP address range is usable for the new cluster's [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) if the range isn't already in use. The IP address range that you specify for the new cluster's Pods can either be an unused range, or it can be a range that's shared with Pods in your other clusters. IP address ranges that are created and managed by GKE can't be used by your cluster.

You can list a project's usable subnets and secondary IP address ranges by using the gcloud CLI.

### gcloud
    
    
    gcloud container subnets list-usable \
        --project SERVICE_PROJECT_ID \
        --network-project HOST_PROJECT_ID
    

Replace `SERVICE_PROJECT_ID` with the project ID of the service project.

If you omit the `--project` or `--network-project` option, the gcloud CLI command uses the default project from your [active configuration](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). Because the host project and network project are distinct, you must specify one or both of `--project` and `--network-project`.

The output is similar to the following:
    
    
    PROJECT               REGION    NETWORK     SUBNET  RANGE
    example-host-project  us-west1  shared-net  tier-1  10.0.4.0/22
    ┌──────────────────────┬───────────────┬─────────────────────────────┐
    │ SECONDARY_RANGE_NAME │ IP_CIDR_RANGE │            STATUS           │
    ├──────────────────────┼───────────────┼─────────────────────────────┤
    │ tier-1-services      │ 10.0.32.0/20  │ usable for pods or services │
    │ tier-1-pods          │ 10.4.0.0/14   │ usable for pods or services │
    └──────────────────────┴───────────────┴─────────────────────────────┘
    example-host-project  us-west1  shared-net  tier-2  172.16.4.0/22
    ┌──────────────────────┬────────────────┬─────────────────────────────┐
    │ SECONDARY_RANGE_NAME │ IP_CIDR_RANGE  │            STATUS           │
    ├──────────────────────┼────────────────┼─────────────────────────────┤
    │ tier-2-services      │ 172.16.16.0/20 │ usable for pods or services │
    │ tier-2-pods          │ 172.20.0.0/14  │ usable for pods or services │
    └──────────────────────┴────────────────┴─────────────────────────────┘
    

The `list-usable` command returns an empty list in the following situations:

  * When the service project's GKE service agent does not have the Host Service Agent User role to the host project.
  * When the GKE service agent in the host project does not exist (for example, if you've deleted that agent accidentally).
  * When the GKE API is not enabled in the host project, which implies the GKE service agent in the host project is missing.



For more information, see the troubleshooting section.

### Secondary IP address range limits

You can create 30 secondary ranges in a given subnet. For each cluster, you need two secondary ranges: one for Pods and one for Services.

**Note:** The primary range and the Pod secondary range can be shared between clusters, but this is not a recommended configuration.

## Create a cluster in your first service project

To create a cluster in your first service project, perform the following steps using the gcloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the project picker, select your first service project.

  3. Click _add_box_ **Create**.

  4. In the Autopilot or Standard section, click **Configure**.

  5. For **Name** , enter `tier-1-cluster`.

  6. In the **Region** drop-down list, select the same region that you used for the subnets.

  7. From the navigation pane, click **Networking**.

  8. Under **Cluster networking** , click **Networks shared with me**.

  9. In the **Network** field, select **shared-net**.

  10. For **Node subnet** , select **tier-1**.

  11. Under **Advanced networking options** , for **Pod secondary CIDR range** , select **tier-1-pods**.

  12. For **Services secondary CIDR range** , select **tier-1-services**.

  13. Click **Create**.




If you created a Standard cluster, you can see that the nodes of the cluster are in the primary address range of the tier-1 subnet by doing the following:

  1. When the creation is complete, the **Cluster details** page is displayed.
  2. Click the **Nodes** tab.
  3. Under **Node Pools** , click **default-pool**.
  4. Under **Instance groups** , click the name of the instance group you want to inspect. For example, gke-tier-1-cluster-default-pool-5c5add1f-grp.
  5. In the list of instances, verify that the internal IP addresses of your nodes are in the primary range of the tier-1 subnet: `10.0.4.0/22`.



### gcloud

Create a cluster named `tier-1-cluster` in your first service project:
    
    
    gcloud container clusters create-auto tier-1-cluster \
        --project=SERVICE_PROJECT_1_ID \
        --location=CONTROL_PLANE_LOCATION \
        --network=projects/HOST_PROJECT_ID/global/networks/shared-net \
        --subnetwork=projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/tier-1 \
        --cluster-secondary-range-name=tier-1-pods \
        --services-secondary-range-name=tier-1-services
    

Replace the `CONTROL_PLANE_LOCATION` with the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.

When the creation is complete, verify that your cluster nodes are in the primary range of the tier-1 subnet: `10.0.4.0/22`.
    
    
    gcloud compute instances list --project SERVICE_PROJECT_1_ID
    

The output shows the internal IP addresses of the nodes:
    
    
    NAME                    ZONE           ... INTERNAL_IP
    gke-tier-1-cluster-...  ZONE_NAME      ... 10.0.4.2
    gke-tier-1-cluster-...  ZONE_NAME      ... 10.0.4.3
    gke-tier-1-cluster-...  ZONE_NAME      ... 10.0.4.4
    

## Create a cluster in your second service project

To create a cluster in your second service project, perform the following steps using the gcloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the project picker, select your second service project.

  3. Click _add_box_ **Create**.

  4. In the Standard or Autopilot section, click **Configure**.

  5. For **Name** , enter `tier-2-cluster`.

  6. In the **Region** drop-down list, select the same region that you used for the subnets.

  7. From the navigation pane, click **Networking**.

  8. Under **Cluster networking** , click **Networks shared with me**.

  9. In the **Network** field, select **shared-net**.

  10. For **Node subnet** , select **tier-2**.

  11. Under **Advanced networking options** , for **Pod secondary CIDR range** , select **tier-2-pods**.

  12. For **Service secondary CIDR range** , select **tier-2-services**.

  13. Click **Create**.




If you created a Standard cluster, you can see that the nodes of the cluster are in the primary address range of the tier-2 subnet by doing the following:

  1. When the creation is complete, the **Cluster details** page is displayed.
  2. Click the **Nodes** tab.
  3. Under **Node Pools** , click **default-pool**.
  4. Under **Instance groups** , click the name of the instance group you want to inspect. For example, `gke-tier-2-cluster-default-pool-5c5add1f-grp`.
  5. In the list of instances, verify that the internal IP addresses of your nodes are in the primary range of the tier-2 subnet: `172.16.4.0/22`.



### gcloud

Create a cluster named `tier-2-cluster` in your second service project:
    
    
    gcloud container clusters create-auto tier-2-cluster \
        --project=SERVICE_PROJECT_2_ID \
        --location=CONTROL_PLANE_LOCATION \
        --network=projects/HOST_PROJECT_ID/global/networks/shared-net \
        --subnetwork=projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/tier-2 \
        --cluster-secondary-range-name=tier-2-pods \
        --services-secondary-range-name=tier-2-services
    

When the creation is complete, verify that your cluster nodes are in the primary range of the tier-2 subnet: `172.16.4.0/22`.
    
    
    gcloud compute instances list --project SERVICE_PROJECT_2_ID
    

The output shows the internal IP addresses of the nodes:
    
    
    NAME                    ZONE           ... INTERNAL_IP
    gke-tier-2-cluster-...  ZONE_NAME      ... 172.16.4.2
    gke-tier-2-cluster-...  ZONE_NAME      ... 172.16.4.3
    gke-tier-2-cluster-...  ZONE_NAME      ... 172.16.4.4
    

**Note:** During GKE cluster upgrades, GKE automatically adds project-level metadata entries like `google_compute_project_metadata` to track secondary IP address range usage. For details and guidance on managing this metadata with Infrastructure as Code (IaC) tools, see [Project metadata for secondary IP address ranges](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#project-metadata).

## Create firewall rules

To allow traffic into the network and between the clusters within the network, you need to create [firewalls](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules). The following sections demonstrate how to create and update firewall rules:

  * Creating a firewall rule to enable SSH connection to a node: Demonstrates how to create a firewall rule that enables traffic from outside of the clusters using SSH.
  * Updating the firewall rule to ping between nodes: Demonstrates how to update the firewall rule to permit ICMP traffic between the clusters.

SSH and ICMP are used as examples, you must create firewall rules that enable your specific application's networking requirements.


**Note:** Shared VPC Admins are responsible for creating firewall rules in the Shared VPC network.

### Create a firewall rule to enable SSH connection to a node

In your host project, create a firewall rule for the `shared-net` network. Allow traffic to enter on TCP port `22`, which permits you to connect to your cluster nodes using SSH.

### Console

  1. Go to the **Firewall** page in the Google Cloud console.

[Go to Firewall](https://console.cloud.google.com/networking/firewalls)

  2. In the project picker, select your host project.

  3. From the **VPC Networking** menu, click **Create Firewall Rule**.

  4. For **Name** , enter `my-shared-net-rule`.

  5. For **Network** , select **shared-net**.

  6. For **Direction of traffic** , select **Ingress**.

  7. For **Action on match** , select **Allow**.

  8. For **Targets** , select **All instances in the network**.

  9. For **Source filter** , select **IP ranges**.

  10. For **Source IP ranges** , enter `0.0.0.0/0`.

  11. For **Protocols and ports** , select **Specified protocols and ports**. In the box, enter `tcp:22`.

  12. Click **Create**.




### gcloud

Create a firewall rule for your shared network:
    
    
    gcloud compute firewall-rules create my-shared-net-rule \
        --project HOST_PROJECT_ID \
        --network shared-net \
        --direction INGRESS \
        --allow tcp:22
    

#### Connect to a node by using SSH

After creating the firewall that allows ingress traffic on TCP port `22`, connect to the node using SSH.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the project picker, select your first service project.

  3. Click **tier-1-cluster**.

  4. On the **Cluster details** page, click the **Nodes** tab.

  5. Under **Node Pools** , click the name of your node pool.

  6. Under **Instance groups** , click the name of your instance group. For example, gke-tier-1-cluster-default-pool-faf87d48-grp.

  7. In the list of instances, make a note of the internal IP addresses of the nodes. These addresses are in the `10.0.4.0/22` range.

  8. For one of your nodes, click **SSH**. This succeeds because SSH uses TCP port `22`, which is allowed by your firewall rule.




### gcloud

List the nodes in your first service project:
    
    
    gcloud compute instances list --project SERVICE_PROJECT_1_ID
    

The output includes the names of the nodes in your cluster:
    
    
    NAME                                           ...
    gke-tier-1-cluster-default-pool-faf87d48-3mf8  ...
    gke-tier-1-cluster-default-pool-faf87d48-q17k  ...
    gke-tier-1-cluster-default-pool-faf87d48-x9rk  ...
    

Connect to one of your nodes using SSH:
    
    
    gcloud compute ssh NODE_NAME \
        --project SERVICE_PROJECT_1_ID \
        --zone COMPUTE_ZONE
    

Replace the following:

  * `NODE_NAME`: the name of one of your nodes.
  * `COMPUTE_ZONE`: the name of a [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) within the region.



### Update the firewall rule to allow traffic between nodes

  1. In your SSH command-line window, start the [CoreOS Toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox):
         
         /usr/bin/toolbox
         

  2. In the toolbox shell, ping one of your other nodes in the same cluster. For example:
         
         ping 10.0.4.4
         

The `ping` command succeeds, because your node and the other node are both in the `10.0.4.0/22` range.

  3. Now, try to ping one of the nodes in the cluster in your other service project. For example:
         
         ping 172.16.4.3
         

This time the `ping` command fails, because your firewall rule does not allow Internet Control Message Protocol (ICMP) traffic.

  4. At an ordinary command prompt, not your toolbox shell, Update your firewall rule to allow ICMP:
         
         gcloud compute firewall-rules update my-shared-net-rule \
             --project HOST_PROJECT_ID \
             --allow tcp:22,icmp
         

  5. In your toolbox shell, ping the node again. For example:
         
         ping 172.16.4.3
         

This time the `ping` command succeeds.




### Create additional firewall rules

You can create additional firewall rules to allow communication between nodes, Pods, and Services in your clusters.

For example, the following rule allows traffic to enter from any node, Pod, or Service in `tier-1-cluster` on any TCP or UDP port:
    
    
    gcloud compute firewall-rules create my-shared-net-rule-2 \
        --project HOST_PROJECT_ID \
        --network shared-net \
        --allow tcp,udp \
        --direction INGRESS \
        --source-ranges 10.0.4.0/22,10.4.0.0/14,10.0.32.0/20
    

The following rule allows traffic to enter from any node, Pod, or Service in `tier-2-cluster` on any TCP or UDP port:
    
    
    gcloud compute firewall-rules create my-shared-net-rule-3 \
        --project HOST_PROJECT_ID \
        --network shared-net \
        --allow tcp,udp \
        --direction INGRESS \
        --source-ranges 172.16.4.0/22,172.20.0.0/14,172.16.16.0/20
    

Kubernetes will also try to create and manage firewall resources when necessary, for example when you create a load balancer service. If Kubernetes finds itself unable to change the firewall rules due to a permission issue, a Kubernetes Event will be raised to guide you on how to make the changes.

If you want to grant Kubernetes permission to change the firewall rules, see Manage firewall resources.

For Ingress Load Balancers, if Kubernetes can't change the firewall rules due to insufficient permission, a `firewallXPNError` event is emitted every several minutes. In [GLBC 1.4](https://github.com/kubernetes/ingress-gce) and later, you can mute the `firewallXPNError` event by adding `networking.gke.io/suppress-firewall-xpn-error: "true"` annotation to the ingress resource. You can always remove this annotation to unmute.

## Create a cluster based on VPC Network Peering in a Shared VPC

You can use Shared VPC with clusters based on VPC Network Peering.

This requires that you grant the following permissions on the host project, either to the user account or to the service account, used to create the cluster:

  * `compute.networks.get`

  * `compute.networks.updatePeering`




You must also ensure that the control plane IP address range does not overlap with other reserved ranges in the shared network.

In this section, you create a VPC-native cluster named `cluster-vpc` in a predefined shared VPC network.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. In the Autopilot or Standard section, click **Configure**.

  4. For **Name** , enter `cluster-vpc`.

  5. From the navigation pane, click **Networking**.

  6. In the **Cluster networking** section, select the **Enable Private nodes** checkbox.

  7. (Optional for Autopilot): Set **Control plane IP range** to `172.16.0.16/28`.

  8. In the **Network** drop-down list, select the VPC network you created previously.

  9. In the **Node subnet** drop-down list, select the shared subnet you created previously.

  10. Configure your cluster as needed.

  11. Click **Create**.




### gcloud

Run the following command to create a cluster named `cluster-vpc` in a predefined Shared VPC:
    
    
    gcloud container clusters create-auto private-cluster-vpc \
        --project=PROJECT_ID \
        --location=CONTROL_PLANE_LOCATION \
        --network=projects/HOST_PROJECT/global/networks/shared-net \
        --subnetwork=SHARED_SUBNETWORK \
        --cluster-secondary-range-name=tier-1-pods \
        --services-secondary-range-name=tier-1-services \
        --enable-private-nodes \
        --master-ipv4-cidr=172.16.0.0/28
    

## Reserve IP addresses

You can reserve [internal](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) and [external IP addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) for your Shared VPC clusters. Ensure that the IP addresses are reserved in the service project.

For internal IP addresses, you must provide the subnetwork where the IP address belongs. To reserve an IP address across projects, use the full resource URL to identify the subnetwork.

You can use the following command in the Google Cloud CLI to reserve an internal IP address:
    
    
    gcloud compute addresses create RESERVED_IP_NAME \
        --region=COMPUTE_REGION \
        --subnet=projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/SUBNETWORK_NAME \
        --addresses=IP_ADDRESS \
        --project=SERVICE_PROJECT_ID
    

To call this command, you must have the `compute.subnetworks.use` permission added to the subnetwork. You can either grant the caller a `compute.networkUser` role on the subnetwork, or you can [grant the caller a customized role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with `compute.subnetworks.use` permission at the project level.

## Clean up

After completing the exercises in this guide, perform the following tasks to remove the resources to prevent unwanted charges incurring on your account:

### Delete the clusters

Delete the two clusters you created.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the project picker, select your first service project.

  3. Select the **tier-1-cluster** , and click **Delete**.

  4. In the project picker, select your second service project.

  5. Select the **tier-2-cluster** , and click **Delete**.




### gcloud
    
    
    gcloud container clusters delete tier-1-cluster \
        --project SERVICE_PROJECT_1_ID \
        --location CONTROL_PLANE_LOCATION
    
    gcloud container clusters delete tier-2-cluster \
        --project SERVICE_PROJECT_2_ID \
        --location CONTROL_PLANE_LOCATION
    

### Disable Shared VPC

Disable Shared VPC in your host project.

### Console

  1. Go to the **Shared VPC** page in the Google Cloud console.

[Go to Shared VPC](https://console.cloud.google.com/networking/xpn/list)

  2. In the project picker, select your host project.

  3. Click **Disable Shared VPC**.

  4. Enter the `HOST_PROJECT_ID` in the field, and click **Disable**.




### gcloud
    
    
    gcloud compute shared-vpc associated-projects remove SERVICE_PROJECT_1_ID \
        --host-project HOST_PROJECT_ID
    
    gcloud compute shared-vpc associated-projects remove SERVICE_PROJECT_2_ID \
        --host-project HOST_PROJECT_ID
    
    gcloud compute shared-vpc disable HOST_PROJECT_ID
    

### Delete your firewall rules

Remove the firewall rules you created.

### Console

  1. Go to the **Firewall** page in the Google Cloud console.

[Go to Firewall](https://console.cloud.google.com/networking/firewalls)

  2. In the project picker, select your host project.

  3. In the list of rules, select **my-shared-net-rule** , **my-shared-net-rule-2** , and **my-shared-net-rule-3**.

  4. Click **Delete**.




### gcloud

Delete your firewall rules:
    
    
    gcloud compute firewall-rules delete \
        my-shared-net-rule \
        my-shared-net-rule-2 \
        my-shared-net-rule-3 \
        --project HOST_PROJECT_ID
    

### Delete the shared network

Delete the shared network you created.

### Console

  1. Go to the **VPC networks** page in the Google Cloud console.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the project picker, select your host project.

  3. In the list of networks, click the **shared-net** link.

  4. Click **Delete VPC Network**.




### gcloud
    
    
    gcloud compute networks subnets delete tier-1 \
        --project HOST_PROJECT_ID \
        --region COMPUTE_REGION
    
    gcloud compute networks subnets delete tier-2 \
        --project HOST_PROJECT_ID \
        --region COMPUTE_REGION
    
    gcloud compute networks delete shared-net --project HOST_PROJECT_ID
    

### Remove the Host Service Agent User role

Remove the Host Service Agent User roles from your two service projects.

### Console

  1. Go to the **IAM** page in the Google Cloud console.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the project picker, select your host project.

  3. Select **Include Google-provided role grants**.

  4. In the list of members, select the row that shows `service-SERVICE_PROJECT_1_NUM@container-engine-robot.iam.gserviceaccount.com` is granted the Kubernetes Engine Host Service Agent User role.

  5. Click _edit_ **Edit principal**.

  6. Under **Kubernetes Engine Host Service Agent User** , click the _delete_ icon to remove the role.

  7. Click **Save**.

  8. Select the row that shows `service-SERVICE_PROJECT_2_NUM@container-engine-robot.iam.gserviceaccount.com` is granted the Kubernetes Engine Host Service Agent User role.

  9. Click _edit_ **Edit principal**.

  10. Under **Kubernetes Engine Host Service Agent User** , click the _delete_ icon to remove the role.

  11. Click **Save**.




### gcloud

  1. Remove the Host Service Agent User role from the GKE service agent of your first service project:
         
         gcloud projects remove-iam-policy-binding HOST_PROJECT_ID \
             --member serviceAccount:service-SERVICE_PROJECT_1_NUM@container-engine-robot.iam.gserviceaccount.com \
             --role roles/container.hostServiceAgentUser
         

  2. Remove the Host Service Agent User role from the GKE service agent of your second service project:
         
         gcloud projects remove-iam-policy-binding HOST_PROJECT_ID \
             --member serviceAccount:service-SERVICE_PROJECT_2_NUM@container-engine-robot.iam.gserviceaccount.com \
             --role roles/container.hostServiceAgentUser
         




## Troubleshooting

The following sections help you to resolve common issues with Shared VPC clusters.

### Error: Failed to get metadata from network project

The following message is a common error when working with Shared VPC clusters:
    
    
    Failed to get metadata from network project. GCE_PERMISSION_DENIED: Google
    Compute Engine: Required 'compute.projects.get' permission for
    'projects/HOST_PROJECT_ID
    

This error can occur for the following reasons:

  * The GKE API has not been enabled in the host project.

  * The host project's GKE service agent does not exist. For example, it might have been deleted.

  * The host project's GKE service agent does not have the _Kubernetes Engine Service Agent_ (`container.serviceAgent`) role in the host project. The binding might have been accidentally removed.

  * The service project's GKE service agent does not have the Host Service Agent User role in the host project.




To resolve the issue, determine whether the host project's GKE service agent exists.

If the service agent doesn't exist, do the following:

  * If the GKE API is not enabled in the host project, enable it. This creates the host project's GKE service agent and grants the host project's GKE service agent the _Kubernetes Engine Service Agent_ (`container.serviceAgent`) role in the host project.

  * If the GKE API is enabled in the host project, this means that either the host project's GKE service agent has been deleted or it doesn't have the _Kubernetes Engine Service Agent_ (`container.serviceAgent`) role in the host project. To resolve this issue, see [Error 400/403: Missing edit permissions on account](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/4xx-errors#gke_service_account_deleted).




### Issue: Connectivity

If you're experiencing connectivity issues between Compute Engine VMs that are in the same Virtual Private Cloud (VPC) network or two VPC networks connected with VPC Network Peering, refer to [Troubleshooting connectivity between virtual machine (VM) instances with internal IP addresses](https://docs.cloud.google.com/vpc/docs/ts-vm-vm-internal) in the Virtual Private Cloud (VPC) documentation.

### Issue: Packet loss

If you're experiencing issues with packet loss when sending traffic from a cluster to an external IP address using [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview), [VPC-native clusters](https://docs.cloud.google.com/vpc/docs/alias-ip), or [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent), see [Troubleshoot Cloud NAT packet loss from a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-nat-packet-loss).

## What's next

  * [Read the Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc).
  * [Learn about provisioning a Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc).
  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * [Read about automatically created firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules).
  * [Learn how to troubleshoot connectivity between virtual machine (VM) instances with internal IP addresses](https://docs.cloud.google.com/vpc/docs/ts-vm-vm-internal).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
