---
url: https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect/
title: Connect to an instance using Private Service Connect \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:53.239451+00:00
---

# Connect to an instance using Private Service Connect  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect to an instance using Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

To connect to an AlloyDB for PostgreSQL primary, read pool, or secondary instance from multiple Virtual Private Cloud (VPC) networks that belong to different groups, teams, projects, or organizations without configuring VPC Network Peering, you can configure Private Service Connect.

## Required roles

Depending on whether you are configuring Private Service Connect infrastructure or connecting as a database client, grant the appropriate Identity and Access Management (IAM) roles:

Task | Role | Description  
---|---|---  
Configure Private Service Connect endpoints and network attachments | Compute Network Admin (`roles/compute.networkAdmin`) | Grants full control over the consumer VPC network that initiates a connection to an AlloyDB instance. If you connect from multiple VPC networks, each network is managed by its own administrator.  
Configure private DNS zones and records | DNS Administrator (`roles/dns.admin`) | Grants full control over Cloud DNS resources, including private DNS zones and record sets.  
Create and manage AlloyDB clusters and instances | AlloyDB Admin (`roles/alloydb.admin`) | Provides full control of AlloyDB clusters and instances over their lifecycle. If you use a custom role instead, grant `alloydb.clusters.create` (to enable Private Service Connect on a cluster) and `alloydb.instances.create` and `alloydb.instances.update` (to configure allowed consumer projects and network attachment URIs).  
Connect to an instance as a client | AlloyDB Client (`roles/alloydb.client`) and Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) (Optional) | Required if you connect through the AlloyDB Auth Proxy or AlloyDB Language Connectors. If you also use IAM database authentication, grant the AlloyDB Database User (`roles/alloydb.databaseUser`) role. If you connect directly by using built-in database authentication, no IAM roles are required for the client connection.  
  
## Create a Private Service Connect endpoint

Private Service Connect endpoints are internal IP addresses in a consumer VPC network that clients in that network can access directly to connect to AlloyDB instances.

To have AlloyDB create the Private Service Connect endpoint automatically, do the following:

  * Reuse an existing service connection policy or create a service connection policy in your VPC networks. With this policy, you can provision Private Service Connect endpoints automatically.
  * Create an AlloyDB cluster and instance with Private Service Connect enabled for the instance, and configure the instance to create Private Service Connect endpoints automatically.
  * Retrieve the endpoint for the instance. This lets you use the endpoint to connect to the instance.
  * Optional: Update an existing AlloyDB cluster and instance with Private Service Connect enabled to generate endpoints automatically.



You can also create the Private Service Connect endpoint manually.

### Create the endpoint automatically

To configure your instance so that AlloyDB creates the Private Service Connect endpoint automatically, follow these high-level steps:

  1. Create a service connection policy.
  2. Create an AlloyDB instance.
  3. Retrieve the endpoint.
  4. Update an instance for creating endpoints automatically.
  5. Configure outbound connectivity.



#### Create a service connection policy

You can reuse an existing service connection policy or create a service connection policy using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

A [service connection policy](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect#service-connection-policy) lets you authorize a specified service class to create a Private Service Connect endpoint in your consumer VPC network. You can use the service connection policy to let AlloyDB create Private Service Connect endpoints automatically.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connection policies** tab.

  3. Click **Create connection policy**.

  4. Enter a **Name** for the connection policy.

  5. In the **Service details** section, for **Service class** , select `google-cloud-alloydb`.

  6. In the **Endpoints scope** section, select a **Network** and **Region** this policy applies to.

  7. In the **Endpoints configuration** section, select one or more subnets from the **Subnetworks** menu. The subnets are used to allocate IP addresses for endpoints.

  8. Optional: Specify a **Connection limit** for the policy. The limit determines how many endpoints AlloyDB can create for this connection policy. If you don't specify a connection limit, then there's no limit.

  9. Click **Create policy**.




###  gcloud 

To create a service connection policy, use the [`service-connection-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create).
    
    
    gcloud network-connectivity service-connection-policies create POLICY_NAME \
        --network=NETWORK \
        --project=PROJECT_ID \
        --region=REGION \
        --service-class=SERVICE_CLASS \
        --subnets=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETS \
        --psc-connection-limit=LIMIT \
        --description="DESCRIPTION" \
        --producer-instance-location=PRODUCER_INSTANCE_LOCATION \
        --allowed-google-producers-resource-hierarchy-level=LIST_OF_NODES
    

Replace the following:

  * `POLICY_NAME`: the name of your service connection policy.
  * `NETWORK`: the network this policy applies to.
  * `PROJECT_ID`: the project ID or number of the VPC network's project. For Shared VPC networks, you must deploy service connection policies in the host project because these policies aren't supported in service projects.
  * `REGION`: the region this policy applies to. The same policy must exist for every region where you want to automate service connectivity.
  * `SERVICE_CLASS`: the producer-supplied resource identifier of the service class. For AlloyDB, the service class is `google-cloud-alloydb`.
  * `SUBNETS`: one or more [regular](https://docs.cloud.google.com/vpc/docs/subnets#purpose) consumer subnets that are used to allocate IP addresses for Private Service Connect endpoints. These IP addresses are allocated automatically and returned to the subnet's pool as managed service instances are created and deleted. The subnets must be in the same region as the service connection policy. If multiple connection policies share the same region, then you can reuse the same subnetwork in these policies. You can enter multiple subnets in a comma-separated list.
  * `LIMIT`: the maximum number of endpoints that you can create with this policy. If you don't specify a limit, then there's no limit.
  * `DESCRIPTION`: an optional description of the service connection policy.
  * `PRODUCER_INSTANCE_LOCATION`: specifies whether the policy automates connections to AlloyDB instances. You can set this value to one of the following:

    * `none` (default): the AlloyDB instance is in the same project as the service connection policy. In a Shared VPC environment, if the AlloyDB instance resides in a service project and you are creating the connection policy in the host project, you must set this parameter to `custom-resource-hierarchy-levels`.
    * `custom-resource-hierarchy-levels`: requires that you set the Resource Manager location path for the projects that you want to automate connectivity for through the `allowed-google-producers-resource-hierarchy-level` parameter.
  * `LIST_OF_NODES`: set this parameter if your producer instance location is set to `custom-resource-hierarchy-levels`. This parameter is a list of projects, folders, and organizations where the instances for which you want to automate connectivity reside. The list is in the form of `projects/PROJECT_ID`, `folders/FOLDER_ID`, or `organizations/ORGANIZATION_ID`.




For example, the following command creates a service connection policy for the `google-cloud-alloydb` service class that allocates IP addresses from the `managed-service-subnet` subnet. A maximum of 10 Private Service Connect endpoints can be created with this policy. The endpoints must be created in projects that are in the same organization as the managed service instance. The AlloyDB instance is located in the `myproject` project.
    
    
    gcloud network-connectivity service-connection-policies create alloydb-policy \
        --network=default \
        --project=my-project \
        --region=us-central1 \
        --service-class=google-cloud-alloydb \
        --subnets=managed-service-subnet \
        --psc-connection-limit=10 \
        --producer-instance-location=custom-resource-hierarchy-levels \
        --allowed-google-producers-resource-hierarchy-level=projects/myproject
    

#### Create an AlloyDB instance

You can create an instance with Private Service Connect enabled and configure the instance to create endpoints automatically using the Google Cloud console, gcloud CLI, or Terraform.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Create cluster**.

  3. In **Cluster ID** , enter `my-cluster`.

  4. Enter a password. Take note of this password because you use it in this quickstart.

  5. Retain the default database version.

  6. Select the `us-central1 (Iowa)` region.

  7. Retain the default instance ID, `my-cluster-primary`.

  8. In **Zonal availability** , retain **Single zone** as the selected option. While we don't recommend a single zone instance for production, you use a single zone in this quickstart to minimize costs. For more information, see [Reduce costs using basic instances](https://docs.cloud.google.com/alloydb/docs/basic-instance).

  9. Select the `2 vCPU, 16 GB` machine type.

  10. Retain private IP connectivity.

     1. Select **Private Service Connect (PSC)**.
     2. Click **Add an endpoint**.
     3. Select the project where you want to create the endpoint.
     4. Select the network.
     5. Click **Check policy** for service connection policy information.
**Note:** Make sure that the service connection policy is created. You can create the policy before or after creating the instance.
  11. Retain the default settings under **Network security**.

  12. Don't make changes in **Show advanced options**.

  13. Click **Create cluster**. It might take several minutes for AlloyDB to create the cluster and display it on the primary cluster **Overview** page.




###  gcloud 

To create the cluster, use the [`gcloud alloydb clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create) command.
    
    
    gcloud alloydb clusters create CLUSTER_ID \
      --password=PASSWORD \
      --region=REGION_ID \
      --project=PROJECT_ID \
      --enable-private-service-connect

Replace the following:

  * `CLUSTER_ID`: the ID of the cluster that you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.

  * `PASSWORD`: the password to use for the default `postgres` user.

  * `REGION_ID`: the region where the cluster is located.

  * `PROJECT_ID`: the ID of the project where the cluster is located.




This command initiates a long-running operation, returning an operation ID.

To create the AlloyDB instance, either primary or a read pool for using Private Service Connect, use the [`gcloud alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create) command. Include the `--allowed-psc-projects` parameter to specify which consumer projects can create endpoints to connect to this instance.
    
    
    gcloud alloydb instances create INSTANCE_ID \
        --instance-type=PRIMARY \
        --cpu-count=CPU_COUNT \
        --availability-type=AVAILABILITY \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --allowed-psc-projects=ALLOWED_PROJECT_LIST \
        --psc-network-attachment-uri=NETWORK_ATTACHMENT_URI \
        --psc-auto-connections=network=CONSUMER_NETWORK,project=CONSUMER_PROJECT

Replace the following:

  * `INSTANCE_ID`: the ID of the instance you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `CPU_COUNT`: the number of vCPUs you want for the instance. Valid values include the following: 
    * `2`: 2 vCPUs, 16 GB RAM
    * `4`: 4 vCPUs, 32 GB RAM
    * `8`: 8 vCPUs, 64 GB RAM
    * `16`: 16 vCPUs, 128 GB RAM
    * `32`: 32 vCPUs, 256 GB RAM
    * `64`: 64 vCPUs, 512 GB RAM
    * `96`: 96 vCPUs, 768 GB RAM
    * `128`: 128 vCPUs, 864 GB RAM
  * `AVAILABILITY`: indicates whether or not this instance should be highly available (HA), with nodes in multiple zones. Valid values include: 
    * `REGIONAL`: creates an HA instance with separate active and standby nodes, and automated failover between them. This is the default value, suitable for production environments.
    * `ZONAL`: creates a basic instance, containing only one node, and no automated failover.
  * `REGION_ID`: the region where the instance is located.
  * `CLUSTER_ID`: the ID of the cluster you created earlier.
  * `ALLOWED_PROJECT_LIST`: the comma-separated list of project IDs or [project numbers](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) that you want to allow access to the instance—for example, `my-project-1`, `12345`, `my-project-n`.
  * `NETWORK_ATTACHMENT_URI` (Optional): the full resource name of the [network attachment URI](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments) that you create for outbound connectivity. For example: `projects/PROJECT_ID/regions/REGION_ID/networkAttachments/NETWORK_ATTACHMENT_ID`.
  * `CONSUMER_NETWORK`: the path to the VPC network where Private Service Connect endpoints are created. For example: `projects/my-host-project/global/networks/default`. This option applies when you are creating endpoints automatically. Make sure that the service connection policy is created. You can create the policy before or after creating the instance.
  * `CONSUMER_PROJECT`: the project where the Private Service Connect endpoint is created. If you're using a Shared VPC network, then this can be either the host project or the service project. Any projects that you specify in the auto-connection parameters are added to your allowed projects automatically. Optionally, for any projects where you want to create Private Service Connect endpoints manually, you can add these projects to your list of allowed projects.

**Note:** The `--allowed-psc-projects` parameter is required for any instance type, including primary and read pool, that needs to be accessible using Private Service Connect. See [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create#create-read-pool) for more details on read pool creation.

A secondary cluster created for a Private Service Connect-enabled primary cluster automatically inherits the Private Service Connect configuration. For more information, see [Create a secondary cluster](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance).

###  Terraform 

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To create an AlloyDB cluster and instance with Private Service Connect enabled, use the [`google_alloydb_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_cluster) and [`google_alloydb_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance) Terraform resources:
    
    
    resource "google_alloydb_cluster" "default" {
      cluster_id = "alloydb-cluster"
      location   = "us-central1"
      psc_config {
        psc_enabled = true
      }
    }
    
    resource "google_alloydb_instance" "default" {
      cluster       = google_alloydb_cluster.default.name
      instance_id   = "alloydb-instance"
      instance_type = "PRIMARY"
      machine_config {
        cpu_count = 2
      }
      psc_instance_config {
        allowed_consumer_projects = [data.google_project.project.number]
        psc_auto_connections {
          consumer_network = google_compute_network.default.id
          consumer_project = data.google_project.project.project_id
        }
        psc_interface_configs {
          network_attachment_resource = google_compute_network_attachment.default.id
        }
      }
    }
    
    resource "google_compute_network" "default" {
      name                    = "alloydb-network"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "default" {
      name          = "alloydb-subnetwork"
      region        = "us-central1"
      network       = google_compute_network.default.id
      ip_cidr_range = "10.0.0.0/16"
    }
    
    resource "google_compute_network_attachment" "default" {
      name                  = "alloydb-network-attachment"
      region                = "us-central1"
      connection_preference = "ACCEPT_AUTOMATIC"
      subnetworks = [
        google_compute_subnetwork.default.self_link
      ]
    }
    
    data "google_project" "project" {}
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

#### Retrieve the endpoint

By retrieving the internal IP address, which is the Private Service Connect endpoint for an instance, you can use this endpoint to [connect to the instance](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#connect-ip-address).

To view information about an instance, including the IP address that's the Private Service Connect endpoint for the instance, use the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command:
    
    
    gcloud alloydb instances describe INSTANCE_NAME \
    --project=PROJECT_ID \
    --cluster=CLUSTER_ID \
    --region=REGION_ID \
    --format='json(pscInstanceConfig.pscAutoConnections)'

Replace the following:

  * INSTANCE_NAME: the name of the AlloyDB instance. If this instance has [Private Service Connect](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect) enabled for it, then [Private Service Connect endpoints](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect#endpoint) in VPC networks can connect to it.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * CLUSTER_ID: the ID of the cluster.
  * REGION_ID: the region where the instance is located.



In the response, note the value that appears next to the `pscInstanceConfig.pscAutoConnections.ipAddress` field. This value is the internal IP address that's also the Private Service Connect endpoint for the instance.

#### Update an instance for creating endpoints automatically

To update an instance to create endpoints automatically, use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command with the `--psc-auto-connections` parameter:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --project=PROJECT_ID \
        --psc-auto-connections=network=CONSUMER_NETWORK,project=CONSUMER_PROJECT

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you're updating.
  * `CLUSTER_ID`: the ID of the cluster.
  * `REGION_ID`: the region where the instance is located.
  * `PROJECT_ID`: the ID of the project where the instance is located.
  * `CONSUMER_NETWORK`: the path to the VPC network where Private Service Connect endpoints are created—for example, `projects/my-host-project/global/networks/default`.
  * `CONSUMER_PROJECT`: the project where the Private Service Connect endpoint is created.



#### Configure outbound connectivity

To enable outbound connectivity for your AlloyDB instance with Private Service Connect enabled, you must set the network attachment URI for the instance. For more information, see [Configure outbound connectivity](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#configure-outbound-connectivity).

### Create the endpoint manually

The following sections explain how to create a Private Service Connect endpoint manually.

#### Create an AlloyDB instance

You can create an instance with Private Service Connect enabled using the Google Cloud console, gcloud CLI, or Terraform.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Create cluster**.

  3. In **Cluster ID** , enter `my-cluster`.

  4. Enter a password. Take note of this password because you use it in this quickstart.

  5. Retain the default database version.

  6. Select the `us-central1 (Iowa)` region.

  7. Retain the default instance ID, `my-cluster-primary`.

  8. In **Zonal availability** , retain **Single zone** as the selected option. While we don't recommend a single zone instance for production, you use a single zone in this quickstart to minimize costs. For more information, see [Reduce costs using basic instances](https://docs.cloud.google.com/alloydb/docs/basic-instance).

  9. Select the `2 vCPU, 16 GB` machine type.

  10. Retain private IP connectivity, and select **Private Service Connect (PSC)**.

  11. Under **Allowed consumer projects** , enter the project IDs or project numbers that you want to allow to connect to the instance.

  12. Retain the default settings under **Network security**.

  13. Don't make changes in **Show advanced options**.

  14. Click **Create cluster**. It might take several minutes for AlloyDB to create the cluster and display it on the primary cluster **Overview** page.




###  gcloud 

To create the cluster, use the [`gcloud alloydb clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create) command.
    
    
    gcloud alloydb clusters create CLUSTER_ID \
      --password=PASSWORD \
      --region=REGION_ID \
      --project=PROJECT_ID \
      --enable-private-service-connect

Replace the following:

  * `CLUSTER_ID`: the ID of the cluster that you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.

  * `PASSWORD`: the password to use for the default `postgres` user.

  * `REGION_ID`: the region where the cluster is located.

  * `PROJECT_ID`: the ID of the project where the cluster is located.




This command initiates a long-running operation, returning an operation ID.

To create the primary instance, use the [`gcloud alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create) command.
    
    
    gcloud alloydb instances create INSTANCE_ID \
        --instance-type=PRIMARY \
        --cpu-count=CPU_COUNT \
        --availability-type=AVAILABILITY \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --allowed-psc-projects=ALLOWED_PROJECT_LIST \
        --psc-network-attachment-uri=NETWORK_ATTACHMENT_URI

Replace the following:

  * `INSTANCE_ID`: the ID of the instance you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `CPU_COUNT`: the number of vCPUs you want for the instance. Valid values include the following: 
    * `2`: 2 vCPUs, 16 GB RAM
    * `4`: 4 vCPUs, 32 GB RAM
    * `8`: 8 vCPUs, 64 GB RAM
    * `16`: 16 vCPUs, 128 GB RAM
    * `32`: 32 vCPUs, 256 GB RAM
    * `64`: 64 vCPUs, 512 GB RAM
    * `96`: 96 vCPUs, 768 GB RAM
    * `128`: 128 vCPUs, 864 GB RAM
  * `AVAILABILITY`: indicates whether or not this instance should be highly available (HA), with nodes in multiple zones. Valid values include: 
    * `REGIONAL`: creates an HA instance with separate active and standby nodes, and automated failover between them. This is the default value, suitable for production environments.
    * `ZONAL`: creates a basic instance, containing only one node, and no automated failover.
  * `REGION_ID`: the region where the instance is located.
  * `CLUSTER_ID`: the ID of the cluster you created earlier.
  * `ALLOWED_PROJECT_LIST`: the comma-separated list of project IDs or [project numbers](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) that you want to allow access to the instance—for example, `my-project-1`, `12345`, `my-project-n`.
  * `NETWORK_ATTACHMENT_URI` (Optional): the full resource name of the [network attachment URI](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments) that you create for outbound connectivity. For example: `projects/PROJECT_ID/regions/REGION_ID/networkAttachments/NETWORK_ATTACHMENT_ID`.



A secondary cluster created for a Private Service Connect-enabled primary cluster automatically inherits the Private Service Connect configuration. For more information, see [Create a secondary cluster](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance).

###  Terraform 

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To create an AlloyDB cluster and instance with Private Service Connect enabled, use the [`google_alloydb_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_cluster) and [`google_alloydb_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance) Terraform resources:
    
    
    resource "google_alloydb_cluster" "default" {
      cluster_id = "alloydb-cluster"
      location   = "us-central1"
      psc_config {
        psc_enabled = true
      }
    }
    
    resource "google_alloydb_instance" "default" {
      cluster       = google_alloydb_cluster.default.name
      instance_id   = "alloydb-instance"
      instance_type = "PRIMARY"
      machine_config {
        cpu_count = 2
      }
      psc_instance_config {
        allowed_consumer_projects = [data.google_project.project.number]
        psc_interface_configs {
          network_attachment_resource = google_compute_network_attachment.default.id
        }
      }
    }
    
    resource "google_compute_network" "default" {
      name                    = "alloydb-network"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "default" {
      name          = "alloydb-subnetwork"
      region        = "us-central1"
      network       = google_compute_network.default.id
      ip_cidr_range = "10.0.0.0/16"
    }
    
    resource "google_compute_network_attachment" "default" {
      name                  = "alloydb-network-attachment"
      region                = "us-central1"
      connection_preference = "ACCEPT_AUTOMATIC"
      subnetworks = [
        google_compute_subnetwork.default.self_link
      ]
    }
    
    data "google_project" "project" {}
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

#### Get the service attachment

After creating an AlloyDB instance with Private Service Connect enabled, get the service attachment URL and use it to create the Private Service Connect endpoint.

To view details about an instance, use the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command.
    
    
    gcloud alloydb instances describe INSTANCE_ID \
     --cluster=CLUSTER_ID \
     --region=REGION_ID

Replace the following:

  * `INSTANCE_ID`: the ID of the instance.
  * `CLUSTER_ID`: the ID of the cluster.
  * `REGION_ID`: the region in which the AlloyDB cluster is deployed.



A sample response for the command is as follows:
    
    
    {
      "pscInstanceConfig": {
        "serviceAttachmentLink": "https://www.googleapis.com/compute/v1/projects/my-project/regions/my-region/serviceAttachments/my-service-attachment-id",
        "allowedConsumerProjects": [
          "45678",
          "12345",
          "67890"
        ],
        "pscDnsName": "015f5524-0555-4a0a-ac5a-0d15d64b15cb.008225d5-070a-4566-aaad-fcb3c87c5901.us-east4.alloydb-psc.goog."
      }
    }
    

The `serviceAttachmentLink` parameter holds the value of the service attachment URL.

#### Create a Private Service Connect endpoint

To create a Private Service Connect endpoint, pass the service attachment URL along with a unique endpoint name. For more information about creating a Private Service Connect endpoint, see [Create an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint).

You can also reserve an internal IP address for the Private Service Connect endpoint using the [`gcloud compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command, and then use the reserved IP address when creating the endpoint, or provision the internal IP address and forwarding rule using Terraform:
    
    
    resource "google_compute_address" "psc_endpoint_ip" {
      name         = "alloydb-psc-endpoint-ip"
      region       = "us-central1"
      subnetwork   = google_compute_subnetwork.default.id
      address_type = "INTERNAL"
    }
    
    resource "google_compute_forwarding_rule" "psc_endpoint" {
      name                  = "alloydb-psc-endpoint"
      region                = "us-central1"
      network               = google_compute_network.default.id
      ip_address            = google_compute_address.psc_endpoint_ip.self_link
      load_balancing_scheme = ""
      target                = google_alloydb_instance.default.psc_instance_config[0].service_attachment_link
    }
    

## Configure outbound connectivity

To enable outbound connectivity, set the network attachment URI when you create or update an AlloyDB instance. This URI allows secure connectivity between your project and the AlloyDB instance during outbound operations such as migrations.

### Create the network attachment

You can create a network attachment that can accept connections automatically (`ACCEPT_AUTOMATIC`) or manually (`ACCEPT_MANUAL`). For more information about creating a network attachment, see [Create and manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments).

If you choose to create a network attachment that accepts connections automatically, then you don't need to set a list of accepted projects explicitly. For accepting connections manually, you must add the service-owned project number of the project where your AlloyDB instance is located to the list of accepted projects.

To find the service-owned project number, run the following command:
    
    
    gcloud alloydb clusters describe CLUSTER_ID --region=REGION_ID

The following is a sample response:
    
    
    pscConfig:
      pscEnabled: true
      serviceOwnedProjectNumber: 123456789012
    

After you identify the service-owned project number, add the project to the list of accepted projects and then create the network attachment.

Make sure that the region of the network attachment is the same as the region of the AlloyDB instance. In addition, the subnet used to create the network attachment must belong to the [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) IP ranges, which are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.

### Update an instance for outbound connectivity

To enable outbound connectivity for an existing AlloyDB instance with Private Service Connect enabled, use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command with the `--psc-network-attachment-uri` parameter:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --project=PROJECT_ID \
        --psc-network-attachment-uri=NETWORK_ATTACHMENT_URI

Replace the following:

  * `INSTANCE_ID`: the ID of the instance.
  * `CLUSTER_ID`: the ID of the cluster.
  * `REGION_ID`: the region where the instance is located.
  * `PROJECT_ID`: the ID of the project where the instance is located.
  * `NETWORK_ATTACHMENT_URI`: the full resource name of the network attachment URI that you create for outbound connectivity—for example, `projects/PROJECT_ID/regions/REGION_ID/networkAttachments/NETWORK_ATTACHMENT_ID`.



AlloyDB instances created prior to March 01, 2025, can't be updated to enable outbound connections. As an alternative approach, we recommend using either of the following options:

  * Create a [regional Cross-Region Replication (CRR) replica of your primary instance](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication) with outbound connectivity enabled. Then, [perform a switchover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#switchover-secondary) to designate the replica instance as the new primary instance.
  * [Perform a backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand) of your existing AlloyDB cluster and primary instance. Then, [create a new AlloyDB cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) with outbound connectivity enabled. Finally, [restore](https://docs.cloud.google.com/alloydb/docs/backup/restore) the previously created backup into the new cluster.

  


### Deactivate outbound connectivity

To deactivate outbound connectivity for an existing AlloyDB instance, use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command with the `--clear-psc-network-attachment-uri` parameter:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --project=PROJECT_ID \
        --clear-psc-network-attachment-uri

Replace the following:

  * `INSTANCE_ID`: the ID of the instance.
  * `CLUSTER_ID`: the ID of the cluster.
  * `REGION_ID`: the region where the instance is located.
  * `PROJECT_ID`: the ID of the project where the instance is located.



## Connect to an AlloyDB instance

You can connect to an AlloyDB instance with Private Service Connect enabled by using one of the following options:

  * Connect directly using a DNS record
  * Use the AlloyDB Auth Proxy with a DNS record
  * Use the AlloyDB Language Connectors with a DNS record
  * Connect directly using an internal IP address



You must configure a private DNS record that maps the instance's pre-generated `pscDnsName` to the Private Service Connect endpoint's internal IP address when you connect by using the AlloyDB Auth Proxy or the AlloyDB Language Connectors.

For methods that use a DNS record, you must create the record in a [private DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#private_zone) in the corresponding consumer VPC network. The `pscDnsName` returned by the AlloyDB API is a pre-generated hostname string and does not resolve until you create a private DNS zone and `A` record in your consumer VPC network.

### Configure a DNS managed zone and a DNS record

To configure a DNS managed zone and a DNS record in your consumer network, follow these steps:

###  gcloud 

  1. To view summary information about an AlloyDB instance—including the pre-generated `pscDnsName` of the instance—use the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command:
         
         gcloud alloydb instances describe INSTANCE_ID \
         --cluster=CLUSTER_ID \
         --region=REGION_ID \
         --format='json(pscInstanceConfig)'

Replace the following:

     * `INSTANCE_ID`: the ID of the instance.
     * `CLUSTER_ID`: the ID of the cluster.
     * `REGION_ID`: the region where the instance is located.

In the response, verify that the `pscDnsName` field appears. The DNS name has the `INSTANCE_UID.CLUSTER_UID.REGION_NAME.alloydb-psc.goog.` pattern—for example, `015f5524-0555-4a0a-ac5a-0d15d64b15cb.008225d5-070a-4566-aaad-fcb3c87c5901.us-east4.alloydb-psc.goog.`

  2. To create a private DNS zone, use the [`gcloud dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command. This zone is associated with the VPC network that's used to connect to the AlloyDB instance through the Private Service Connect endpoint.

**Note:** For each consumer VPC network, create a separate private DNS zone. If you connect using the AlloyDB Auth Proxy or AlloyDB Language Connectors, the DNS name of the record must exactly match the instance's `pscDnsName` (including the trailing dot).
         
         gcloud dns managed-zones create ZONE_NAME \
         --project=PROJECT_ID \
         --description=DESCRIPTION \
         --dns-name=DNS_NAME \
         --networks=NETWORK_NAME \
         --visibility=private

Replace the following:

     * `ZONE_NAME`: the name of the DNS zone.
     * `PROJECT_ID`: the ID or project number of the Google Cloud project that contains the zone.
     * `DESCRIPTION`: a description of the zone (for example, `DNS zone for the AlloyDB instance`).
     * `DNS_NAME`: the DNS name for the zone, such as `INSTANCE_UID.CLUSTER_UID.REGION_NAME.alloydb-psc.goog.` (or the parent domain `alloydb-psc.goog.`).
     * `NETWORK_NAME`: the name of the consumer VPC network. For a Shared VPC network, set this to the fully qualified path of the VPC network—for example, `projects/cymbal-project/global/networks/shared-vpc-network`.
  3. After you create the Private Service Connect endpoint, create a DNS `A` record in the zone by using the [`gcloud dns record-sets create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/create) command:
         
         gcloud dns record-sets create DNS_NAME \
         --project=PROJECT_ID \
         --type=RRSET_TYPE \
         --rrdatas=RR_DATA \
         --zone=ZONE_NAME

Replace the following:

     * `DNS_NAME`: the `pscDnsName` that you retrieved earlier in this procedure.
     * `RRSET_TYPE`: the resource record type of the DNS record set (`A`).
     * `RR_DATA`: the internal IP address allocated for the Private Service Connect endpoint (for example, `198.51.100.5`).



###  Terraform 

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To create a private Cloud DNS zone and `A` record that maps the instance's `pscDnsName` to the Private Service Connect endpoint's internal IP address, use the [`google_dns_managed_zone`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dns_managed_zone) and [`google_dns_record_set`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dns_record_set) Terraform resources:
    
    
    resource "google_dns_managed_zone" "psc_dns_zone" {
      name        = "alloydb-psc-zone"
      dns_name    = google_alloydb_instance.default.psc_instance_config[0].psc_dns_name
      description = "Private DNS zone for AlloyDB PSC endpoint"
      visibility  = "private"
    
      private_visibility_config {
        networks {
          network_url = google_compute_network.default.id
        }
      }
    }
    
    resource "google_dns_record_set" "psc_dns_record" {
      name         = google_alloydb_instance.default.psc_instance_config[0].psc_dns_name
      type         = "A"
      ttl          = 300
      managed_zone = google_dns_managed_zone.psc_dns_zone.name
      rrdatas      = [google_compute_address.psc_endpoint_ip.address]
    }
    

### Connect directly using a DNS record

After you create a Private Service Connect endpoint and configure a private DNS `A` record for the instance's `pscDnsName`, you can connect directly from a client in the consumer VPC network by using the DNS name (without the trailing dot):
    
    
    psql -U USERNAME -h DNS_NAME -d DATABASE_NAME

Replace the following:

  * `USERNAME`: the name of the database user that's connecting to the instance.
  * `DNS_NAME`: the DNS record name (such as the instance's `pscDnsName` without the trailing dot) that resolves to the Private Service Connect endpoint.
  * `DATABASE_NAME`: the name of the database to connect to (for example, `postgres`).



### Connect using the AlloyDB Auth Proxy

The AlloyDB Auth Proxy is a connector that lets you make authorized, encrypted connections to AlloyDB databases. The AlloyDB Auth Proxy works by having a local client running in the local environment. Your application communicates with the AlloyDB Auth Proxy with the standard database protocol used by your database.

When you set the `--psc` flag while starting the Auth Proxy client, the AlloyDB Auth Proxy resolves the instance's `pscDnsName` using the private DNS record that you created to connect to the Private Service Connect-enabled instance.

Start the Auth Proxy client by passing the instance URI that you retrieve using the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command, and set the `--psc` flag.

For more information about connecting to an instance using the Auth Proxy, see [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect).

### Connect using the AlloyDB Language Connectors

AlloyDB Language Connectors are libraries that provide automated mTLS with TLS 1.3 and IAM authorization when connecting to an AlloyDB instance.

After the Language Connector is configured for Private Service Connect, it resolves the instance's `pscDnsName` using the private DNS record that you created to connect to the instance.

### Java

If you're using Private Service Connect to connect to your AlloyDB instance, include the following:
    
    
    config.addDataSourceProperty("alloydbIpType", "PSC");
    

For more information about using a Private Service Connect endpoint in the AlloyDB Java Connector, see the [GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-java-connector).

### Python (pg8000)

If you're using Private Service Connect to connect to your AlloyDB instance, include the following:
    
    
      def getconn() -> pg8000.dbapi.Connection:
          conn: pg8000.dbapi.Connection = connector.connect(
              inst_uri,
              "pg8000",
              user=user,
              password=password,
              db=db,
              # use ip_type to specify PSC
              ip_type=IPTypes.PSC,
          )
          return conn
    

For more information about using a Private Service Connect endpoint in the AlloyDB Python Connector, see the [GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-python-connector).

### Python (asyncpg)

If you're using Private Service Connect to connect to your AlloyDB instance, include the following:
    
    
      async def getconn() -> asyncpg.Connection:
        conn: asyncpg.Connection = await connector.connect(
            inst_uri,
            "asyncpg",
            user=user,
            password=password,
            db=db,
            # use ip_type to specify PSC
            ip_type=IPTypes.PSC,
        )
        return conn
    

For more information about using a Private Service Connect endpoint in the AlloyDB Python Connector, see the [GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-python-connector).

### Go (pgx)

If you're using Private Service Connect to connect to your AlloyDB instance, include the following:
    
    
    d.Dial(ctx, instURI, alloydbconn.WithPSC())
    

For more information about using a Private Service Connect endpoint in the AlloyDB Go Connector, see the [GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-go-connector).

### Go (database/sql)

If you're using Private Service Connect to connect to your AlloyDB instance, include the following:
    
    
      cleanup, err := postgres.RegisterDriver(
        "alloydb",
        alloydbconn.WithDefaultDialOptions(alloydbconn.WithPSC()),
      )
    

For more information about using a Private Service Connect endpoint in the AlloyDB Go Connector, see the [GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-go-connector).

### Connect directly through an internal IP address

After you create a Private Service Connect endpoint, you can directly connect to an AlloyDB instance using the endpoint's internal IP address without configuring a DNS record.

  1. To retrieve the IP address of a manually created Private Service Connect endpoint, use the [`gcloud compute addresses describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) command:
         
         gcloud compute addresses describe ADDRESS_NAME \
         --project=PROJECT_ID \
         --region=REGION_NAME

Replace the following:

     * `ADDRESS_NAME`: the name of the endpoint's reserved IP address resource.
     * `PROJECT_ID`: the ID or project number of the Google Cloud project that contains the endpoint.
     * `REGION_NAME`: the region name for the endpoint.
  2. To connect to the AlloyDB instance, use the internal IP address:
         
         psql -U USERNAME -h IP_ADDRESS

Replace the following:

     * `USERNAME`: the name of the user that's connecting to the instance.
     * `IP_ADDRESS`: the endpoint's internal IP address.



## Limitations

  * You can set up to 20 Private Service Connect endpoints that connect to the service attachment of an AlloyDB instance with Private Service Connect enabled.
  * You can't use the [`--network`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create) flag when you create a Private Service Connect-enabled cluster because it's associated with [private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).
  * You can't activate or deactivate Private Service Connect on an existing instance.
  * You can't configure an instance that has Private Service Connect enabled to use private services access.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
