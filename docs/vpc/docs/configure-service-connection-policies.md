---
url: https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies/
title: Configure service connection policies \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:56.762443+00:00
---

# Configure service connection policies  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure service connection policies

This page describes how a network administrator can configure [service connection policies](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) to automate private connectivity to a managed service.

## Before you begin

  * Make sure that the managed service that you want to deploy supports service connection policies.

For more information about services that support service connection policies, see [Supported services](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#supported-services).

  * You must know the name of the [service class](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#service-class) for the managed service instance that you want to deploy connectivity for.

  * Read about [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints).

  * You need a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and a [subnet](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#specifications).

  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.

  * You must [enable](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com) the [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest) in your project.

  * You must [enable](https://console.cloud.google.com/apis/library/serviceconsumermanagement.googleapis.com) the [Service Consumer Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest) in the consumer project that Private Service Connect endpoints are deployed in. This API lets Google Cloud create the Network Connectivity Service Account that deploys Private Service Connect endpoints.




### Required roles

To get the permissions that you need to configure a network and create a service connection policy, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To use service connection policies with Shared VPC, [Network Connectivity Service Accounts](https://docs.cloud.google.com/iam/docs/service-agents#network-connectivity-service-account) must be granted roles on the service and host projects. These service accounts are configured automatically when a service connection policy is created, but the roles can be manually removed. If you see errors about missing permissions, a [Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) might need to grant the roles again. For more information, see Configure service accounts for Shared VPC.

## Create a service connection policy

A service connection policy lets you authorize the specified service class to create a Private Service Connect connection between producer and consumer VPC networks.

You can create a maximum of one policy for each service class, region, and VPC network combination. A policy dictates service connectivity automation for that specific combination.

When you configure a policy, you select one or more subnets. These subnets are used to allocate IP addresses for the endpoints that are created through the policy. The stack type of a subnet [affects the possible IP version of endpoints that you can deploy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#ip-versions). You can reuse the same subnet in multiple connection policies if the policies share the same region.

For example, if you want to use service connectivity automation with two services in three different regions, create six policies. You can use a minimum of three subnets—one for each region.

After you create a service connection policy, you can only update the policy's subnets, connection limit, and service instance scope. If you need to update other fields, delete the policy and create a new one.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networkconnectivity.serviceConnectionPolicies.create` on the project
  * `compute.networks.get` and `compute.networks.use` on the VPC network
  * `compute.subnetworks.get` and `compute.subnetworks.use` on each subnet



**Roles**

  * [ Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connection Policies** tab.

  3. Click **Create connection policy**.

  4. Enter a **Name** for the connection policy.

  5. In the **Service details** section, select a service class from the **Service class** menu.

To determine which service class to use, see the documentation for the service that you're configuring.

  6. In the **Endpoints scope** section, select a **Network** and **Region** that this policy applies to.

  7. In the **Endpoints configuration** section, select one or more subnets from the **Subnetworks** menu. The subnets are used to allocate IP addresses for endpoints.

  8. Optional: Specify a **Connection limit** for the policy. The limit determines how many endpoints can be created by using this connection policy. If omitted, there is no limit.

  9. By default, endpoints are created for service instances that are in the same project as the connection policy. If you've selected a supported Google service, you can configure the connection policy to let you connect to service instances that are in a different part of the [Resource Manager hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

To select different Resource Manager nodes, do the following:

     1. Select **Custom service instance scope**.
     2. Choose the organizations, folders, and projects that contain service instances that you want to connect to.
  10. Click **Create policy**.




###  gcloud 

Use the [`service-connection-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create).
    
    
    gcloud network-connectivity service-connection-policies create POLICY_NAME \
        --network=NETWORK \
        --project=PROJECT_ID \
        --region=REGION \
        --service-class=SERVICE_CLASS \
        --subnets=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETS \
        --psc-connection-limit=LIMIT \
        --description=DESCRIPTION \
        --producer-instance-location=SERVICE_INSTANCE_SCOPE \
        --allowed-google-producers-resource-hierarchy-level=LIST_OF_NODES
    

Replace the following:

  * `POLICY_NAME`: the name of your service connection policy.
  * `NETWORK`: the network to apply this policy to.
  * `PROJECT_ID`: the project ID or number of the VPC network's project. For Shared VPC networks, service connection policies must be deployed in the host project and are not supported in service projects.
  * `REGION`: the region to apply this policy to. The same policy must exist for every region in which you want to automate service connectivity.
  * `SERVICE_CLASS`: the producer-supplied resource identifier of the service class.
  * `SUBNETS`: one or more [regular](https://docs.cloud.google.com/vpc/docs/subnets#purpose) consumer subnets that are used to allocate IP addresses for Private Service Connect endpoints. The subnets must be in the same region as the service connection policy. You can reuse the same subnetwork in multiple connection policies if the policies share the same region. You can enter multiple subnets in a comma-separated list.
  * `LIMIT`: the maximum number of endpoints that can be created by using this policy. If not specified, there is no limit.
  * `DESCRIPTION`: an optional description of the service connection policy.
  * `SERVICE_INSTANCE_SCOPE`: for supported Google managed services, specifies whether this policy automates connections to service instances that are in [custom Resource Manager locations](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope). If set to `none`, endpoints are created that connect to service instances that are in the same project as the service connection policy (or in the case of Shared VPC, in connected projects). The default value is `none`. If set to `custom-resource-hierarchy-levels`, you specify the custom locations by using the `--allowed-google-producers-resource-hierarchy-level` flag.
  * `LIST_OF_NODES`: for supported Google managed services, specifies a list of [Resource Manager nodes](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) (projects, folders, and organizations) that contain the service instances that you want to connect to. This field is checked only when the `--producer-instance-location` flag is set to `custom-resource-hierarchy-levels`. The list can contain any combination of projects, folders, and organizations. For an example list, see the following: 
        
        "projects/1111111111",
        "folders/2222222222",
        "folders/3333333333",
        "organizations/4444444444"
        




For example, the following command creates a service connection policy for the Google-published `google-cloud-sql` service class. The policy can be used to automate connectivity to service instances deployed in `shared-db-service-project`. Private Service Connect endpoints that are created by using this policy are allocated IP addresses from the `endpoint-subnet` subnet. A maximum of 10 endpoints can be created by using this policy.
    
    
    gcloud network-connectivity service-connection-policies create google-cloud-sql-policy \
        --network=default \
        --project=my-project \
        --region=us-central1 \
        --service-class=google-cloud-sql \
        --subnets=endpoint-subnet \
        --psc-connection-limit=10 \
        --producer-instance-location=custom-resource-hierarchy-levels \
        --allowed-producer-instance-scope=projects/shared-db-service-project
    

###  Terraform 

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_connectivity_service_connection_policy) to create a service connection policy.
    
    
    # Create a VPC network
    resource "google_compute_network" "default" {
      name                    = "consumer-network"
      auto_create_subnetworks = false
    }
    
    # Create a subnetwork
    resource "google_compute_subnetwork" "default" {
      name          = "consumer-subnet"
      ip_cidr_range = "10.0.0.0/16"
      region        = "us-central1"
      network       = google_compute_network.default.id
    }
    
    # Create a service connection policy
    resource "google_network_connectivity_service_connection_policy" "default" {
      name          = "service-connection-policy"
      location      = "us-central1"
      service_class = "gcp-memorystore-redis"
      network       = google_compute_network.default.id
      psc_config {
        subnetworks = [google_compute_subnetwork.default.id]
        limit       = 2
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the region of your service connection policy.
  * `POLICY_NAME`: the name of your service connection policy.
  * `DESCRIPTION`: an optional description of your service connection policy.
  * `NETWORK`: the network of your service connection policy.
  * `LIMIT`: the maximum number of endpoints that can be created by using this policy. If not specified, there is no limit. 
  * `SUBNET`: one or more [regular](https://docs.cloud.google.com/vpc/docs/subnets#purpose) consumer subnets that are used to allocate IP addresses for Private Service Connect endpoints. The subnets must be in the same region as the service connection policy. You can reuse the same subnetwork in multiple connection policies if the policies share the same region. You can enter multiple subnet URIs in a comma-separated list. 
  * `SERVICE_CLASS`: the producer-supplied resource identifier of the service class.
  * `PRODUCER_INSTANCE_LOCATION`: `PRODUCER_INSTANCE_LOCATION_UNSPECIFIED` (default) or `CUSTOM_RESOURCE_HIERARCHY_LEVELS`.
  * `LIST_OF_NODES`: A list of [Resource Manager nodes](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) (projects, folders, and organizations) that contain the service instances that you want to connect to. This field is checked only when the `PRODUCER_INSTANCE_LOCATION` flag is set to `CUSTOM_RESOURCE_HIERARCHY_LEVELS`. The list can contain any combination of projects, folders, and organizations. For an example list, see the following: 
        
        "projects/1111111111",
            "folders/2222222222",
            "folders/3333333333",
            "organizations/4444444444"
            




HTTP method and URL: 
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies?serviceConnectionPolicyId=POLICY_NAME

Request JSON body: 
    
    
    {
      "description": "DESCRIPTION",
      "network": "projects/PROJECT_ID/global/networks/NETWORK",
      "pscConfig": {
        "limit": "LIMIT",
        "subnetworks": [
          "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET"
        ]
        "producerInstanceLocation": "CUSTOM_RESOURCE_HIERARCHY_LEVELS",
        "allowedGoogleProducersResourceHierarchyLevel": [
          LIST_OF_NODES
        ]
      },
      "serviceClass": "SERVICE_CLASS"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies?serviceConnectionPolicyId=POLICY_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies?serviceConnectionPolicyId=POLICY_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/us-central1/operations/operation-1692118768698-602f91a204523-8c6a2d93-d5c20a6a",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.networkconnectivity.v1.OperationMetadata",
        "createTime": "2023-08-15T16:59:29.236110917Z",
        "target": "projects/project-id/locations/us-central1/serviceConnectionPolicies/policy-name",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## List service connection policies

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networkconnectivity.serviceConnectionPolicies.list`



**Roles**

  * [ Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connection Policies** tab.

  3. The connection policies are displayed.




###  gcloud 

Use the [`service-connection-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list).
    
    
    gcloud network-connectivity service-connection-policies list \
        --region=REGION
    

Replace `REGION` with the region that you want to list service connection policies in.

###  API 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the region to list service connection policies in.



HTTP method and URL: 
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "serviceConnectionPolicies": [
        {
          "name": "projects/project-id/locations/us-central1/serviceConnectionPolicies/policy-1",
          "createTime": "2023-08-15T15:33:54.712819865Z",
          "updateTime": "2023-08-15T15:33:54.945630882Z",
          "description": "descriptor",
          "network": "projects/project-id/global/networks/network-two",
          "serviceClass": "service-class",
          "infrastructure": "PSC",
          "pscConfig": {
            "subnetworks": [
              "projects/project-id/regions/us-west1/subnetworks/us-west1-subnet"
            ],
            "limit": "12"
          },
          "etag": "zCqDFBG1dS7B4gNdJKPR98YMUXpSrBIz0tZB_hwOIZI"
        },
        {
          "name": "projects/project-id/locations/us-central1/serviceConnectionPolicies/policy-2",
          "createTime": "2023-08-15T16:59:29.230257109Z",
          "updateTime": "2023-08-15T16:59:29.508994923Z",
          "description": "descriptor",
          "network": "projects/project-id/global/networks/custom-test",
          "serviceClass": "service-class",
          "infrastructure": "PSC",
          "pscConfig": {
            "subnetworks": [
              "projects/project-id/regions/us-central1/subnetworks/subnet-one"
            ],
            "limit": "25"
          },
          "etag": "nB603i61nRGMZpNjWoWMM6wRzsgM8QN9C9v5QFLyOa8"
        }
      ]
    }
    

## Describe a service connection policy

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networkconnectivity.serviceConnectionPolicies.get`



**Roles**

  * [ Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connection Policies** tab.

  3. Click the service connection policy that you want to view.




###  gcloud 

Use the [`service-connection-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/describe).
    
    
    gcloud network-connectivity service-connection-policies describe POLICY_NAME \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of the service connection policy that you want to describe.
  * `REGION`: the region of the service connection policy that you want to describe.



###  API 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the region of your service connection policy.
  * `POLICY_NAME`: the name of the service connection policy to describe.



HTTP method and URL: 
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/us-central1/serviceConnectionPolicies/policy-name",
      "createTime": "2023-08-15T16:59:29.230257109Z",
      "updateTime": "2023-08-15T16:59:29.508994923Z",
      "description": "description",
      "network": "projects/project-id/global/networks/custom-test",
      "serviceClass": "gcp-memorystore-redis",
      "infrastructure": "PSC",
      "pscConfig": {
        "subnetworks": [
          "projects/project-id/regions/us-central1/subnetworks/subnet-one"
        ],
        "limit": "25"
      },
      "etag": "nB603i61nRGMZpNjWoWMM6wRzsgM8QN9C9v5QFLyOa8"
    }
    

## Update a service connection policy

You can update the subnets, connection limit, and service instance scope for a service connection policy.

If you remove a subnet from the service connection policy, the following applies:

  * Existing Private Service Connect endpoints are not affected.
  * New endpoints don't use the removed subnet.



If you update the connection limit of a service connection policy, the following applies:

  * Existing endpoints are not affected.
  * If the new connection limit is lower than the existing number of endpoints that are associated with the policy, service connectivity automation blocks the creation of new endpoints that use this policy.
  * If the new connection limit is higher than the existing number of endpoints that are associated with the policy, endpoints that were previously blocked by the connection limit can be created.



If you update a service connection policy and don't specify a connection limit, the updated policy has no connection limit.

If you update the service instance scope for a service connection policy, existing endpoints aren't affected.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networkconnectivity.serviceConnectionPolicies.update` on the project
  * `compute.subnetworks.get` and `compute.subnetworks.use` on each subnet



**Roles**

  * [ Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connection Policies** tab.

  3. Click the service connection policy that you want to edit.

  4. Click **Edit**.

  5. Make the updates to the service connection policy.

  6. Click **Update policy**.




###  gcloud 

Use the [`service-connection-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update).
    
    
    gcloud network-connectivity service-connection-policies update POLICY_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --subnets=SUBNETS \
        --psc-connection-limit=LIMIT
        --producer-instance-location=SERVICE_INSTANCE_SCOPE \
        --allowed-google-producers-resource-hierarchy-level=LIST_OF_NODES
    

  * `POLICY_NAME`: the name of your service connection policy.
  * `REGION`: the region of the service connection policy. You cannot update a policy's region.
  * `PROJECT_ID`: the project ID or number of the policy's project.
  * `SUBNETS`: one or more [regular](https://docs.cloud.google.com/vpc/docs/subnets#purpose) consumer subnets that are used to allocate IP addresses for Private Service Connect endpoints. The subnets must be in the same region as the service connection policy. You can reuse the same subnetwork in multiple connection policies if the policies share the same region. You can enter multiple subnets in a comma-separated list.
  * `LIMIT`: the maximum number of endpoints that can be created by using this policy. If not specified, there is no limit.
  * `SERVICE_INSTANCE_SCOPE`: for supported Google managed services, specifies whether this policy automates connections to service instances that are in [custom Resource Manager locations](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope). If set to `none`, endpoints are created that connect to service instances that are in the same project as the service connection policy (or in the case of Shared VPC, in connected projects). This is the default value. If set to `custom-resource-hierarchy-levels`, you specify the custom locations by using the `--allowed-google-producers-resource-hierarchy-level` flag.
  * `LIST_OF_NODES`: for supported Google managed services, specifies a list of [Resource Manager nodes](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) (projects, folders, and organizations) that contain the service instances that you want to connect to. This field is checked only when the `--producer-instance-location` flag is set to `custom-resource-hierarchy-levels`. The list can contain any combination of projects, folders, and organizations. For an example list, see the following: 
        
        "projects/1111111111",
        "folders/2222222222",
        "folders/3333333333",
        "organizations/4444444444"
        




###  API 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the region of your service connection policy. You cannot update a policy's region.
  * `POLICY_NAME`: the name of your service connection policy.
  * `LIMIT`: the maximum number of endpoints that can be created by using this policy. If not specified, there is no limit.
  * `SUBNET`: one or more [regular](https://docs.cloud.google.com/vpc/docs/subnets#purpose) consumer subnets that are used to allocate IP addresses for Private Service Connect endpoints. The subnets must be in the same region as the service connection policy. You can reuse the same subnetwork in multiple connection policies if the policies share the same region. You can enter multiple subnet URIs in a comma-separated list.
  * `NETWORK`: the network of your service connection policy.



HTTP method and URL: 
    
    
    PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME

Request JSON body: 
    
    
    {
      "pscConfig": {
        "limit": "LIMIT",
        "subnetworks": [
          "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET"
        ]
      },
      "network": "projects/PROJECT_ID/global/networks/NETWORK"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/us-central1/operations/operation-1692118768698-602f91a204523-8c6a2d93-d5c20a6a",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.networkconnectivity.v1.OperationMetadata",
        "createTime": "2023-08-15T16:59:29.236110917Z",
        "target": "projects/project-id/locations/us-central1/serviceConnectionPolicies/policy-name",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Delete a service connection policy

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networkconnectivity.serviceConnectionPolicies.delete`



**Roles**

  * [ Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)



You can delete a service connection policy if you are finished using the service or want to stop automating connectivity. Deletion of the policy is blocked if active Private Service Connect connections are associated with the policy. Before deleting a service connection policy, delete all active connections by [decommissioning all associated service instances](https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies#decommission-service).

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connection Policies** tab.

  3. Select the service connection policies that you want to delete, and then click **Delete**.




###  gcloud 

Use the [`service-connection-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/delete).
    
    
    gcloud network-connectivity service-connection-policies delete POLICY_NAME \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of the service connection policy that you want to delete.
  * `REGION`: the region of the service connection policy that you want to delete.



###  API 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the region of your service connection policy.
  * `POLICY_NAME`: the name of the service connection policy to delete.



HTTP method and URL: 
    
    
    DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/us-central1/operations/operation-1692128792549-602fb6f98194a-e0275435-36edc095",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.networkconnectivity.v1.OperationMetadata",
        "createTime": "2023-08-15T19:46:32.605032867Z",
        "target": "projects/project-id/locations/us-central1/serviceConnectionPolicies/policy-name",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Configure service accounts for Shared VPC

Service accounts are configured automatically when you use service connection policies with Shared VPC, but the roles can be manually removed. If you see errors about missing permissions, try granting the roles again.

To grant the required roles, a [Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) can do the following.

### Grant roles to service account in service project

###  gcloud 

  1. Grant the [Network Connectivity Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) to the service project's [Network Connectivity Service Account](https://docs.cloud.google.com/iam/docs/service-agents#network-connectivity-service-account). Grant the role on the service project.
         
         gcloud projects add-iam-policy-binding SERVICE_PROJECT_NUMBER \
             --member=serviceAccount:service-SERVICE_PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com \
             --role=roles/networkconnectivity.serviceAgent
         

Replace `SERVICE_PROJECT_NUMBER` with the project number of the service project.

  2. Grant the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) to the service project's Network Connectivity Service Account. Do one of the following.

     * Grant the role on the host project.
           
           gcloud projects add-iam-policy-binding HOST_PROJECT_NUMBER \
               --member=serviceAccount:service-SERVICE_PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com \
               --role=roles/compute.networkUser
           

Replace `HOST_PROJECT_NUMBER` with the project number of the host project.

     * Grant the role on each of the subnets in the host project that are associated with the service connection policy. Use the following command for each subnet.
           
           gcloud compute networks subnets add-iam-policy-binding SUBNET \
               --member=serviceAccount:service-SERVICE_PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com \
               --role=roles/compute.networkUser \
               --region=REGION \
               --project=HOST_PROJECT_NUMBER
           

Replace the following:

       * `SUBNET`: the name of the subnet that's associated with your service connection policy.
       * `REGION`: the region of the subnet.



### Grant role to service account in host project

###  gcloud 

  1. Grant the Network Connectivity Service Agent role (`roles/networkconnectivity.serviceAgent`) to the host project's Network Connectivity Service Account. Grant the role on the host project.
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_NUMBER \
             --member=serviceAccount:service-HOST_PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com \
             --role=roles/networkconnectivity.serviceAgent
         

Replace `HOST_PROJECT_NUMBER` with the project number of the host project.




## What's next

  * [Deploy a managed service instance by using service connection policies](https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
