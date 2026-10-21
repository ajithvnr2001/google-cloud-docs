---
url: https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect/
title: Configure Private Service Connect \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:46.847956+00:00
---

# Configure Private Service Connect  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Configure Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect "View this page for the PostgreSQL database engine") | SQL Server

This document describes how to set up and configure [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) for the private network connections of your Cloud SQL instances.

After you set up Private Service Connect and its endpoints, then you and your application clients can connect to either a primary Cloud SQL instance or any of its [read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica#create-read-replica-cloud-sql-instance-psc-enabled) from multiple Virtual Private Cloud (VPC) networks that belong to different groups, teams, projects, or organizations. You can also set up per-instance or global DNS names for DNS name-based client connections, which is useful for failover and disaster recovery use cases.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Service Networking, Network Connectivity, Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking.googleapis.com,networkconnectivity.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Compute Network Admin, Cloud SQL Admin, Cloud DNS Admin, Cloud SQL Instance User 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the Service Networking, Network Connectivity, Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking.googleapis.com,networkconnectivity.googleapis.com)

  12. Make sure that you have the following role or roles on the project: Compute Network Admin, Cloud SQL Admin, Cloud DNS Admin, Cloud SQL Instance User 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




###  Required roles for Private Service Connect 

The following table provides information about the roles required to configure and connect to a Private Service Connect with a Cloud SQL instance.

Role | Description  
---|---  
[`compute.networkAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) | Grants full control over the VPC network that initiates a connection to a Cloud SQL instance. You can create and manage IP addresses, firewall rules, service connection policies, and [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint). If you use Private Service Connect to connect to a Cloud SQL instance from multiple VPC networks, then each network has its own administrator.  
[`dns.admin`](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) | Grants full control over Cloud DNS resources, including [DNS zones and records.](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns)  
[`cloudsql.admin`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) | Provides full control of a Cloud SQL instance and controls the instance over its lifecycle.  
[`cloudsql.instanceUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.instanceUser) | Provides access to the Cloud SQL instance. If you connect through the Cloud SQL Auth Proxy client, then you must have the [Cloud SQL Client role](https://console.cloud.google.com/iam-admin/iam). If you connect directly, then you don't need any [Identity and Access Management (IAM) roles and permissions](https://docs.cloud.google.com/sql/docs/sqlserver/roles-and-permissions).  
  
To set up a service connection policy automatically when you create your Cloud SQL instance, you need additional roles and the ability to assign the roles to the Cloud SQL service agent. For more information, see Create a service connection policy.

## Create a Private Service Connect endpoint

Private Service Connect endpoints are internal IP addresses in a consumer VPC network, which clients in that network can access directly. Clients can use these endpoints to connect to Cloud SQL instances.

You can either have Cloud SQL create a Private Service Connect endpoint automatically in your VPC, or you can create the endpoint manually.

## Create the endpoint automatically

**Note** : If the service connection policy and the Cloud SQL instance are in different projects, then you must configure the service connection policy with a custom service instance scope. This scope defines the resource hierarchy as the IDs for the projects, folders, or organizations where the instance is located to ensure the policy can discover and connect to it.

To have Cloud SQL create the Private Service Connect endpoint automatically, do the following:

  1. Create a service connection policy in your VPC network. With this policy, you can provision Private Service Connect endpoints automatically.

**Note:** You can create a service connection policy automatically when you create the Cloud SQL instance; however, this option requires additional administrative permissions.
  2. Create a Cloud SQL instance with Private Service Connect enabled for the instance, and configure the instance to create Private Service Connect endpoints automatically.

  3. Retrieve the endpoint for the instance. This lets you use the endpoint to connect to the instance.




### Create a service connection policy

You can create a service connection policy by using the Google Cloud console, the [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connection Policies** tab.

  3. Click **Create connection policy**.

  4. Enter a **Name** for the connection policy.

  5. Specify the service class by doing the following:

     1. For **Source service class** , select **Google services**.
     2. From the **Service class** menu, select `google-cloud-sql` because Cloud SQL is the managed service for the connection policy.
  6. In the **Target endpoints scope** section, select a **Network** and **Region** to which this policy applies.

  7. Optional: If the service connection policy and the Cloud SQL instance are in different projects, folders, or organizations, then configure the **Custom service instance scope** :

     1. Toggle the **Custom service instance scope** switch to the **on** position.
     2. In the **Scopes** field, enter the IDs for the projects, folders, or organizations where the instance is located.
  8. In the **Policy** section, select one or more subnets from the **Subnetworks** menu. The subnets are used to allocate IP addresses for endpoints.

  9. Optional: Specify a **Connection limit** for the policy. The limit determines how many endpoints can be created by using this connection policy. If you don't specify a connection limit, then there's no limit.

  10. Click **Create policy**.




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
        --allowed-google-producers-resource-hierarchy-level=RESOURCE_HIERARCHY_LEVEL
    

Replace the following:

  * `POLICY_NAME`: the name of your service connection policy.
  * `NETWORK`: the network to which this policy applies.
  * `PROJECT_ID`: the project ID or number of the VPC network's project. For Shared VPC networks, you must deploy service connection policies in the host project because these policies aren't supported in service projects.
  * `REGION`: the region to which this policy applies. The same policy must exist for every region in which you want to automate service connectivity.
  * `SERVICE_CLASS`: the producer-supplied resource identifier of the service class. For Cloud SQL, the service class is `google-cloud-sql`.
  * `SUBNETS`: one or more [regular](https://docs.cloud.google.com/vpc/docs/subnets#purpose) consumer subnets that are used to allocate IP addresses for Private Service Connect endpoints. These IP addresses are allocated automatically and returned to the subnet's pool as managed service instances are created and deleted. The subnets must be in the same region as the service connection policy. If multiple connection policies share the same region, then you can reuse the same subnetwork in these policies. You can enter multiple subnets in a comma-separated list.
  * `LIMIT`: the maximum number of endpoints that you can create by using this policy. If you don't specify a limit, then there's no limit.
  * `DESCRIPTION`: an optional description of the service connection policy.
  * `PRODUCER_INSTANCE_LOCATION`: specify whether to authorize a custom hierarchy of locations for a Cloud SQL instance. If the instance is in a different project, folder, or organization than the policy, then you must set this value to `custom-resource-hierarchy-levels`.

  * `RESOURCE_HIERARCHY_LEVEL`: a list of projects, folders, or organizations where the instance is located. This list is in one of these forms:

    * `projects/PROJECT_ID`
    * `folders/FOLDER_ID`
    * `organizations/ORGANIZATION_ID`.



For example, the following command creates a service connection policy for the   
`google-cloud-sql` service class that allocates IP addresses from the `managed-services` subnet. A maximum of 10 Private Service Connect endpoints can be created by using this policy. The endpoints must be created in projects that are in the same organization as the managed service instance. The Cloud SQL instance is located in the `myproject` project.
    
    
    gcloud network-connectivity service-connection-policies create cloud-sql-policy \
        --network=default \
        --project=my-project \
        --region=us-central1 \
        --service-class=google-cloud-sql \
        --subnets=managed-service-subnet \
        --psc-connection-limit=10 \
        --producer-instance-location=custom-resource-hierarchy-levels \
        --allowed-google-producers-resource-hierarchy-level=projects/myproject
    

###  REST 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the region of your service connection policy.
  * `POLICY_NAME`: the name of your service connection policy.
  * `DESCRIPTION`: an optional description of your service connection policy.
  * `NETWORK`: the network of your service connection policy.
  * `LIMIT`: the maximum number of endpoints that you can create by using this policy. If you don't specify a limit, then there's no limit.
  * `SUBNETS`: one or more [regular](https://docs.cloud.google.com/vpc/docs/subnets#purpose) consumer subnets that are used to allocate IP addresses for Private Service Connect endpoints. These IP addresses are allocated automatically and returned to the subnet's pool as managed service instances are created and deleted. The subnets must be in the same region as the service connection policy. If multiple connection policies share the same region, then you can reuse the same subnetwork in these policies. You can enter multiple subnets in a comma-separated list. 
  * `SERVICE_CLASS`: the producer-supplied resource identifier of the service class.



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
      "name": "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.networkconnectivity.v1.OperationMetadata",
        "createTime": "2023-08-15T16:59:29.236110917Z",
        "target": "projects/PROJECT_ID/locations/REGION/serviceConnectionPolicies/POLICY_NAME",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

#### Create a service connection policy automatically

You can create a service connection policy automatically when you create the Cloud SQL instance; however, this option requires additional administrative permissions.

###  Console 

If you're using the Google Cloud console, then create the Cloud SQL instance with Private Service Connect enabled. The Google Cloud console checks for required roles and configures them automatically. You might need to enable the [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest) if it isn't already enabled for your project.

###  gcloud or REST 

If you're using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API, then you must grant additional roles to the Cloud SQL service agent before you create the instance.

  1. If a project-specific Cloud SQL service agent doesn't already exist in the project that will host the Cloud SQL instance, then create one.

To create the service agent, run the following command:
         
         gcloud beta services identity create \
           --service=sqladmin.googleapis.com \
           --project=INSTANCE_PROJECT
         

Replace the following:

     * `INSTANCE_PROJECT`: the project where you plan to create the Cloud SQL instance.

The command creates a service agent with the format `service-INSTANCE_PROJECT_NUMBER@gcp-sa-cloudsql.iam.gserviceaccount.com`.

  2. Provide the required IAM permissions to the Cloud SQL service agent by granting the following roles to the service agent:

     * Service Automation Consumer Network Admin (`roles/networkconnectivity.consumerNetworkAdmin`)
     * Compute Network Viewer (`roles/compute.networkViewer`)

To add the roles to the Cloud SQL service agent, run the following commands:
    
    gcloud projects add-iam-policy-binding CONSUMER_PROJECT \
      --member='serviceAccount:CLOUD_SQL_SERVICE_AGENT' \
      --role='roles/networkconnectivity.consumerNetworkAdmin'
    
    gcloud projects add-iam-policy-binding CONSUMER_PROJECT \
      --member='serviceAccount:CLOUD_SQL_SERVICE_AGENT' \
      --role='roles/compute.networkViewer'
    

Replace the following:

     * `CONSUMER_PROJECT`: the project where the Private Service Connect endpoint will be created. If you're using a Shared VPC network, then this can be either the host project or the service project.
     * `CLOUD_SQL_SERVICE_AGENT`: the email address of the Cloud SQL service agent account that you created.



### Create a Cloud SQL instance

You can create an instance with Private Service Connect enabled for the instance and configure the instance to create endpoints automatically by using the Google Cloud console, [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API.

**Note:** After you create the instance, a Private Service Connect endpoint is automatically created in the VPC networks that you specify. However, the endpoint might not be created because of reasons such as the specified network doesn't exist, there's no valid service connection policy, or there aren't any available IP addresses. If this occurs, then the endpoint won't be created. Optionally, you can create Private Service Connect endpoints manually.

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. In the **Customize your instance** section, expand the **Connections** section.
  3. Select the **Private IP** checkbox.
  4. In the **Choose a private connection method** section, select the **Private Service Connect (PSC)** checkbox.
  5. In the **Endpoint setup** section, click **Add an Endpoint**.
  6. In the **Endpoint setup** section, do the following: 
     1. In the **New Endpoint** card, select the project where you want to set up the endpoint from the **Project** menu.
     2. Select a network for your endpoint from the **Network** menu.
     3. If the [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest) isn't enabled yet, then click **Enable**.
  7. Click **Confirm Network Setup**. If a service connection policy is detected for your selected network, then a success message displays. If no service connection policy is detected but permissions have been granted successfully, then Google Cloud will create a service connection policy for you.
  8. Optional: Complete any other instance configuration options.
  9. Click **Create Instance**.



###  gcloud 

To create an instance with Private Service Connect enabled for the instance, use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command:
    
    
    gcloud sql instances create INSTANCE_NAME \
      --project=PROJECT_ID \
      --region=REGION_NAME \
      --cpu=NUMBER_OF_vCPUs \
      --memory=MEMORY_SIZE \
      --root-password=ROOT_PASSWORD \
      --availability-type=AVAILABILITY_TYPE \
      --database-version=DATABASE_VERSION \
      --no-assign-ip \
      --enable-private-service-connect \
      --allowed-psc-projects=ALLOWED_PROJECTS \
      --psc-auto-connections=network=CONSUMER_NETWORK,project=CONSUMER_PROJECT \
      --enable-psc-auto-dns \
      --enable-psc-write-endpoint-dns
    

Optional. To create or update a service connection policy automatically when you create the Cloud SQL instance, add the `--enable-psc-auto-connection-policy` parameter to the command. You need to configure additional permissions to use this parameter. For more information, see Create a service connection policy automatically.

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `PROJECT_ID`: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * `REGION_NAME`: the region name for the instance. 
  * `NUMBER_OF_vCPUs`: the number of cores for the instance.
  * `MEMORY_SIZE`: the amount of memory for the instance.
  * `ROOT_PASSWORD`: the password of the `root` Cloud SQL user. 
  * `AVAILABILITY_TYPE`: enables high availability for the instance. For this parameter, specify one of the following values:

    * `REGIONAL`: enables high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provides no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance).

  * `DATABASE_VERSION`: the database version for the instance (for example, `SQLSERVER_2019_STANDARD`).

  * `ALLOWED_PROJECTS`: a comma-separated list of allowed project IDs or numbers from where Private Service Connect endpoints can connect to Cloud SQL instances.

If a project isn't contained in this list, then you can't create [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) in the project to connect to the instance.

  * `CONSUMER_NETWORK`: the path to the VPC network from where Private Service Connect endpoints need to be created. For example: `projects/my-host-project/global/networks/default`.

  * `CONSUMER_PROJECT`: the project where the Private Service Connect endpoint is created. If you're using a Shared VPC network, then this can be either the host project or the service project.

Any projects that you specify in the auto-connection parameters are added to your allowed projects automatically. Optionally, for any projects where you want to create Private Service Connect endpoints manually, you can add these projects to your list of allowed projects.




Use these parameters to enable and configure Private Service Connect:

  * `--enable-private-service-connect`: Enables Private Service Connect.
  * `--allowed-psc-projects=ALLOWED_PROJECTS`: Specifies a comma-separated list of allowed project IDs or numbers. These are the projects from which Private Service Connect endpoints can connect to Cloud SQL instances.
  * `--psc-auto-connections=network=CONSUMER_NETWORK,project=CONSUMER_PROJECT`: Specifies the path to the VPC network for which Private Service Connect endpoints need to be created.
  * `--enable-psc-auto-dns`: Indicates whether Private Service Connect DNS automation should be enabled for this instance. Defaults to disabled for new instances when Private Service Connect is enabled using `--enable-private-service-connect`.

When DNS automation is enabled, Cloud SQL provisions a per-instance DNS record in all networks configured with Private Service Connect auto-connections.

  * `--enable-psc-write-endpoint-dns`: Indicates whether Private Service Connect write endpoint DNS automation is enabled for this instance. This feature is only supported for Enterprise Plus instances in which `--enable-psc-auto-dns` is also set, and it defaults to disabled when a new instance is created.

When write endpoint DNS automation is enabled, Cloud SQL provisions a Global DNS record to act as a Write Endpoint for the replication cluster in all networks that are configured with Private Service Connect auto-connections. This global DNS record always points to the current primary instance of the replication cluster, which enables seamless application failover without requiring any client-side connection-string updates in the case of a replica [failover or switchover operation](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery).




###  REST 

Before using any of the request data, make the following replacements: 

  * INSTANCE_NAME: the name of the Cloud SQL instance.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * REGION_NAME: the region name for the instance.
  * DATABASE_VERSION: the database version for the instance (for example, `SQLSERVER_2019_STANDARD`).
  * ROOT_PASSWORD: the password of the `root` Cloud SQL user.
  * AVAILABILITY_TYPE: the zonal availability type of the instance. Use this parameter to enable or disable high availability for the instance by specifying one of the following values: 
    * `REGIONAL`: enables high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provides no switchover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a comma-separated list of allowed project IDs or numbers from where Private Service Connect endpoints can connect to Cloud SQL instances. 

If a project isn't contained in this list, then you can't create [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) in the project to connect to the instance.

  * CONSUMER_PROJECT: the project where the Private Service Connect endpoint is created. If you're using a Shared VPC network, then this can be either the host project or the service project.

Any projects that you specify in the auto-connection parameters are added to your allowed projects automatically. Optionally, for any projects where you want to create Private Service Connect endpoints manually, you can add these projects to your list of allowed projects.

  * PARENT_PROJECT: the project that contains the network CONSUMER_NETWORK. If you don't specify a different project in CONSUMER_PROJECT, endpoints are automatically created in PARENT_PROJECT 
  * CONSUMER_PROJECT: Optional. Only specify this if CONSUMER_NETWORK is a Shared VPC network and you want to allow automatic creation of Private Service Connect endpoints in a service project.

Any projects that you specify in the auto-connection parameters are added to your allowed projects automatically. Optionally, for any projects where you want to create Private Service Connect endpoints manually, you can add these projects to your list of allowed projects.

  * CONSUMER_NETWORK: the VPC network where you want to allow automatic creation of Private Service Connect endpoints. For example:   
`projects/my-host-project/global/networks/default`.
  * MACHINE_TYPE: an enumerated string value that represents the machine type for the instance. For example: code>db-custom-NUMBER_OF_vCPUs-MEMORY_SIZE, where NUMBER_OF_vCPUs and MEMORY_SIZE are the number of cores and the amount of memory that you want for the instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_NAME",
      "project": PROJECT_ID",
      "region": "REGION_NAME",
      "databaseVersion": "SQLSERVER_2019_STANDARD",
      "rootPassword": "ROOT_PASSWORD",
      "kind": "sql#instance",
      "settings": {
        "availabilityType": "AVAILABILITY_TYPE",
        "ipConfiguration": {
          "ipv4Enabled": false,
          "pscConfig": {
            "allowedConsumerProjects": [
              "ALLOWED_PROJECTS"
            ],
            "pscAutoConnections": [
              {
                "consumerProject":"CONSUMER_PROJECT",
                "consumerNetwork":"projects/PARENT_PROJECT/global/networks/CONSUMER_NETWORK"
              }
            ],
            "pscEnabled": true,
            "pscAutoConnectionPolicyEnabled": true,
            "pscAutoDnsEnabled": true,
            "pscWriteEndpointDnsEnabled": true
          }
        },
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "tier": "MACHINE_TYPE"
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

These are the fields that you use to enable DNS automation and a global write endpoint DNS name:

  * `psc_auto_dns_enabled`: Indicates whether Private Service Connect DNS automation is enabled for this instance. Defaults to disabled for new instances when Private Service Connect is enabled using `--enable-private-service-connect`.

When DNS automation is enabled, Cloud SQL provisions a universal DNS record across all networks configured with Private Service Connect auto-connections.

  * `psc_write_endpoint_dns_enabled`: Indicates whether Private Service Connect write endpoint DNS automation is enabled for this instance. This feature is only supported for Enterprise Plus instances in which `--enable-psc-auto-dns` is also set, and it defaults to disabled when a new instance is created.

With write endpoint DNS automation enabled, Cloud SQL provisions a Global DNS record to act as a Write Endpoint in all networks configured with Private Service Connect auto-connections. This global DNS record always points to the current primary instance of the replication cluster, which enables seamless application failover without requiring any client-side connection-string updates in the case of a replica [failover or switchover operation](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery).




To create a service connection policy automatically when you create the instance, enable the following field:

  * `psc_auto_connection_policy_enabled`: Indicates whether to let Google Cloud create or update a service connection policy when creating the Cloud SQL instance. You need to configure additional permissions to use this option. For more information, see Create a service connection policy automatically.



###  Terraform 

To create the instance, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance) with a `psc_config` field:
    
    
    resource "google_sql_database_instance" "INSTANCE_NAME"
    {
      name = "INSTANCE_NAME"
      database_version = "DATABASE_VERSION"
      settings
      {
        tier = "MACHINE_TYPE"
        ip_configuration
        {
          psc_config
          {
            psc_enabled = true
            psc_auto_dns_enabled = true
            psc_write_endpoint_dns_enabled = true
            allowed_consumer_projects = ["ALLOWED_PROJECTS"]
            psc_auto_connections
            {
              consumer_network = "CONSUMER_NETWORK"
              consumer_service_project_id = "CONSUMER_PROJECT"
            }
          }
          ipv4_enabled = false
        }
      }
    }

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `DATABASE_VERSION`: the database version for the instance (for example, `SQLSERVER_2019_STANDARD`).
  * `MACHINE_TYPE`: the machine type for the instance.
  * `ALLOWED_PROJECTS`: a comma-separated list of allowed project IDs or numbers from where Private Service Connect endpoints can connect to Cloud SQL instances.

If a project isn't contained in this list, then you can't create [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) in the project to connect to the instance.

  * `CONSUMER_NETWORK`: the path to the VPC network from where Private Service Connect endpoints need to be created. For example: `projects/my-host-project/global/networks/default`.

  * `CONSUMER_PROJECT`: the project where the Private Service Connect endpoint is created. If you're using a Shared VPC network, then this can be either the host project or the service project.




Use these fields to enable DNS automation and a global write endpoint DNS name:

  * `psc_auto_dns_enabled`: Indicates whether Private Service Connect DNS automation is enabled for this instance. Defaults to disabled for new instances when Private Service Connect is enabled using `--enable-private-service-connect`.

When DNS automation is enabled, Cloud SQL provisions a universal DNS record across all networks configured with Private Service Connect auto-connections.

  * `psc_write_endpoint_dns_enabled`: Indicates whether Private Service Connect write endpoint DNS automation is enabled for this instance. This feature is only supported for Enterprise Plus instances in which `--enable-psc-auto-dns` is also set, and it defaults to disabled when a new instance is created.

With write endpoint DNS automation enabled, Cloud SQL provisions a Global DNS record to act as a Write Endpoint in all networks configured with Private Service Connect auto-connections. This global DNS record always points to the current primary instance of the replication cluster, which enables seamless application failover without requiring any client-side connection-string updates in the case of a replica [failover or switchover operation](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery).




To enable Private Service Connect and create a service connection policy automatically, use the following field:

  * `psc_auto_connection_policy_enabled`: Indicates whether to let Google Cloud create or update a service connection policy when creating the Cloud SQL instance. You need to configure additional permissions to use this option. For more information, see Create a service connection policy automatically.



#### Apply the changes

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

#### Delete the changes

To delete your changes, do the following:

  1. To disable deletion protection, in your Terraform configuration file set the `deletion_protection` argument to `false`. 
         
         deletion_protection =  "false"

  2. Apply the updated Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply



  3. Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
         
         terraform destroy




### Retrieve the endpoint

By retrieving the internal IP address, which is the Private Service Connect endpoint for an instance, you can use this endpoint to connect to the instance.

### gcloud

To view information about an instance, including the IP address that's the Private Service Connect endpoint for the instance, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
    
    
    gcloud sql instances describe INSTANCE_NAME \
    --project=PROJECT_ID \
    --format='json(settings.ipConfiguration.pscConfig.pscAutoConnections)'

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance. If this instance has [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) enabled for it, then [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) in VPC networks can connect to it.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.



In the response, note the value that appears next to the `pscConfig:pscAutoConnections:ipAddress` field. This value is the internal IP address that's also the Private Service Connect endpoint for the instance.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_NAME: the name of the Cloud SQL instance. If this instance has [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) enabled for it, then [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) in VPC networks can connect to it.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "SQLSERVER_2019_STANDARD",
      "settings": {
        "authorizedGaeApplications": [],
        "tier": "db-custom-2-7680",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration": {
          "authorizedNetworks": [],
          "pscConfig": {
            "allowedConsumerProjects": [
              "ALLOWED_PROJECTS"
            ],
          "pscAutoConnections": {
            consumerNetwork:"projects/PARENT_PROJECT/global/networks/CONSUMER_NETWORK",
            consumerNetworkStatus:"CONSUMER_NETWORK_STATUS",
            consumerProject:"CONSUMER_PROJECT",
            **ipAddress:" IP_ADDRESS",**
            **status:" STATUS"**
            },
            "pscEnabled": true
          },
          "ipv4Enabled": false
        },
    }
    

The following fields exist for instances that have Private Service Connect enabled for them:

  * `allowedConsumerProjects`: a list of the [allowed projects](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#allowed-psc-projects) for the instance. You can create Private Service Connect endpoints from any VPC networks in these projects to the [service attachment](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#service-attachment) of the instance.
  * `pscAutoConnections`: the allowed VPC network, the status of the service connection policy, and the status of the IP address that's the endpoint for the instance.
  * `pscEnabled`: whether an instance has Private Service Connect enabled for it.



To see how to construct the [underlying REST API request](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/get) for this task, see the [instances:get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/get) page.

**Note:** To obtain the write endpoint for your Cloud SQL instance, use the [`instances:get`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/get) method. This endpoint is the value that's associated with the `WriteEndpoint` parameter.

## Create the endpoint manually

To create the Private Service Connect endpoint manually, do the following:

  1. Create a Cloud SQL instance with Private Service Connect enabled for the instance.

  2. Get the service attachment URI. You use this URI to create the Private Service Connect endpoint.

  3. Reserve an internal IP address for the Private Service Connect endpoint and create an endpoint with that address.




### Create a Cloud SQL instance

You can create an instance with Private Service Connect enabled for the instance by using [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the API.

**Note:** You can now create an instance that supports both private services access and Private Service Connect. By using Private Service Connect, you can connect to either a primary instance or any of its read replicas from multiple VPC networks. For more information, see [Configure both private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access-and-private-service-connect).

### gcloud

To create an instance with Private Service Connect enabled for the instance, use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command:
    
    
    gcloud sql instances create INSTANCE_NAME \
    --project=PROJECT_ID \
    --region=REGION_NAME \
    --enable-private-service-connect \
    --allowed-psc-projects=ALLOWED_PROJECTS \
    --availability-type=AVAILABILITY_TYPE \
    --no-assign-ip \
    --database-version=DATABASE_VERSION
    --cpu=NUMBER_OF_vCPUs \
    --memory=MEMORY_SIZE \
    --root-password=ROOT_PASSWORD

Make the following replacements:

  * INSTANCE_NAME: the name of the instance.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * REGION_NAME: the region name for the instance.
  * ALLOWED_PROJECTS: a comma-separated list of allowed project IDs or numbers from where Private Service Connect endpoints can connect to Cloud SQL instances.

If a project isn't contained in this list, then you can't create [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) in the project to connect to the instance.

  * AVAILABILITY_TYPE: enable high availability for the instance. For this parameter, specify one of the following values: 
    * `REGIONAL`: enables high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provides no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance).

  * DATABASE_VERSION: the database version for the instance (for example, `SQLSERVER_2019_STANDARD`).
  * NUMBER_OF_vCPUs: the number of cores for the instance.
  * MEMORY_SIZE: the amount of memory for the instance.
  * ROOT_PASSWORD: the password of the `root` Cloud SQL user.



### Terraform

To create an instance with Private Service Connect enabled for the instance, use the [ `google_sql_database_instance`Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "default" {
      name             = "sqlserver-instance"
      region           = "us-central1"
      database_version = "SQLSERVER_2019_ENTERPRISE"
      root_password    = "INSERT-PASSWORD-HERE"
      settings {
        tier              = "db-custom-2-7680"
        availability_type = "REGIONAL"
        backup_configuration {
          enabled    = true
          start_time = "20:55"
        }
        ip_configuration {
          psc_config {
            psc_enabled               = true
            allowed_consumer_projects = [] # Add consumer project IDs here.
          }
          ipv4_enabled = false
        }
      }
    }

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_NAME: the name of the instance.
  * REGION_NAME: the region name for the instance.
  * ROOT_PASSWORD: the password of the `root` Cloud SQL user.
  * AVAILABILITY_TYPE: enables high availability for the instance. For this parameter, specify one of the following values: 
    * `REGIONAL`: enables high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provides no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a comma-separated list of allowed project IDs or numbers from where Private Service Connect endpoints can connect to Cloud SQL instances.

If a project isn't contained in this list, then you can't create [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) in the project to connect to the instance.

  * MACHINE_TYPE: an enumerated string value that represents the machine type for the instance. For example: `db-custom-NUMBER_OF_vCPUs-MEMORY_SIZE`, where NUMBER_OF_vCPUs and MEMORY_SIZE are the number of cores and the amount of memory that you want for the instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_NAME",
      "project": PROJECT_ID",
      "region": "REGION_NAME",
      "databaseVersion": "SQLSERVER_2019_STANDARD",
      "rootPassword": "ROOT_PASSWORD",
      "kind": "sql#instance",
      "settings": {
        "availabilityType": "AVAILABILITY_TYPE",
        "ipConfiguration": {
          "ipv4Enabled": false,
          "pscConfig": {
            "allowedConsumerProjects": [
              "ALLOWED_PROJECTS"
            ],
            "pscEnabled": true
          }
        },
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "tier": "MACHINE_TYPE"
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Get the service attachment

After creating a Cloud SQL instance with Private Service Connect enabled, get the service attachment URI and use it to create the Private Service Connect endpoint.

### gcloud

To view summary information about an instance with Private Service Connect enabled, such as the `pscServiceAttachmentLink` field which displays the URI that points to the service attachment of the instance, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
    
    
    gcloud sql instances describe INSTANCE_NAME \
    --project=PROJECT_ID

**Note:** The service attachment URI is used to create the Private Service Connect endpoint.

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance to which Private Service Connect endpoints in VPC networks can connect
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance



The following example shows a sample output for this command:
    
    
    gcloud sql instances describe myinstance \
    --project=12345
    
    ...
    pscServiceAttachmentLink: projects/45678/regions/myregion/serviceAttachments/myserviceattachment

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      ...
      pscServiceAttachmentLink: "projects/PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME"
    }
    

The `pscServiceAttachmentLink` field displays the URI that points to the service attachment of the instance.

### Create a Private Service Connect endpoint

You can reserve an internal IP address for the Private Service Connect endpoint and [create an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) with that address. To create the endpoint, you need the service attachment URI and the projects that are allowed for the instance.

### gcloud

  1. To reserve an internal IP address for the Private Service Connect endpoint, use the   
[`gcloud compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command:
         
         gcloud compute addresses create ADDRESS_NAME \
         --project=PROJECT_ID \
         --region=REGION_NAME \
         --subnet=SUBNET_URI \
         --addresses=INTERNAL_IP_ADDRESS

Make the following replacements:

     * ADDRESS_NAME: the name of the internal IP address.
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project for the endpoint.
     * REGION_NAME: the region name for the endpoint.
     * SUBNET_URI: the subnet name for the IP address. The format is: `projects/SUBNET_PROJECT_ID/regions/REGION_NAME/subnetworks/SUBNET_NAME`. If the subnet is in a Shared VPC network, then we recommend that the SUBNET_PROJECT_ID is the host project.
     * INTERNAL_IP_ADDRESS: the IP address to reserve. This IP address must be within the subnet's primary IP range. The IP address can be an [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) address or a subnet with non-RFC ranges. If you don't want to specify the IP address because you want Google Cloud to reserve an available IP address in the subnet, then omit this flag.
**Note:** If both the VPC network and the subnet support internal IPv4 and IPv6 IP addresses, then you can reserve an IPv6 address for the endpoint by adding the following line of code: 

`--ip-version=IPV6`

  2. To verify that the IP address is reserved, use the [`gcloud compute addresses list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/list) command:
         
         gcloud compute addresses list ADDRESS_NAME \
         --project=PROJECT_ID

In the response, verify that a `RESERVED` status appears for the IP address.

  3. To create the Private Service Connect endpoint and point it to the Cloud SQL service attachment, use the [`gcloud compute forwarding-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command:
         
         gcloud compute forwarding-rules create ENDPOINT_NAME \
         --address=ADDRESS_NAME \
         --project=PROJECT_ID \
         --region=REGION_NAME \
         --network=NETWORK_URI \
         --target-service-attachment=SERVICE_ATTACHMENT_URI \
         --allow-psc-global-access

Make the following replacements:

     * ENDPOINT_NAME: the name of the endpoint
     * NETWORK_URI: the URI of the VPC network for the endpoint. The format is: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_NAME`. If you want to use a Shared VPC network, then specify the host project as the NETWORK_PROJECT_ID.
     * SERVICE_ATTACHMENT_URI: the URI of the service attachment
By using the optional [`--allow-psc-global-access`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--allow-psc-global-access) parameter, clients from all regions can access this forwarding rule.
  4. To verify that the service attachment accepts the endpoint, use the   
[`gcloud compute forwarding-rules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe) command:
         
         gcloud compute forwarding-rules describe ENDPOINT_NAME \
         --project=PROJECT_ID \
         --region=REGION_NAME

In the response, verify that an `ACCEPTED` status appears for the `pscConnectionStatus` field. The endpoint can connect to the service attachment.




### Terraform

To create a Private Service Connect endpoint, use the [ `google_sql_database_instance`Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).

Use the following sample to create an IPv4 Private Service Connect endpoint.
    
    
    resource "google_compute_address" "default" {
      name         = "psc-compute-address-${google_sql_database_instance.default.name}"
      region       = "us-central1"
      address_type = "INTERNAL"
      subnetwork   = "default"     # Replace value with the name of the subnet here.
      address      = "10.128.0.44" # Replace value with the IP address to reserve.
    }
    
    data "google_sql_database_instance" "default" {
      name = resource.google_sql_database_instance.default.name
    }
    
    resource "google_compute_forwarding_rule" "default" {
      name                    = "psc-forwarding-rule-${google_sql_database_instance.default.name}"
      region                  = "us-central1"
      network                 = "default"
      ip_address              = google_compute_address.default.self_link
      load_balancing_scheme   = ""
      target                  = data.google_sql_database_instance.default.psc_service_attachment_link
      allow_psc_global_access = true
    }

Use the following sample to create an IPv6 Private Service Connect endpoint.
    
    
    resource "google_compute_network" "ipv6_default" {
      name                     = "net-ipv6"
      auto_create_subnetworks  = false
      enable_ula_internal_ipv6 = true
    }
    
    resource "google_compute_subnetwork" "ipv6_default" {
      name             = "subnet-internal-ipv6"
      ip_cidr_range    = "10.0.0.0/16"
      region           = "us-central1"
      stack_type       = "IPV4_IPV6"
      ipv6_access_type = "INTERNAL"
      network          = google_compute_network.ipv6_default.id
    }
    
    resource "google_compute_address" "ipv6_default" {
      name         = "psc-compute-ipv6-address-${google_sql_database_instance.default.name}"
      region       = "us-central1"
      address_type = "INTERNAL"
      subnetwork   = google_compute_subnetwork.ipv6_default.name
      ip_version   = "IPV6"
    }
    
    resource "google_compute_forwarding_rule" "ipv6_ilb_example" {
      name   = "ipv6-psc-forwarding-rule-${google_sql_database_instance.default.name}"
      region = "us-central1"
    
      load_balancing_scheme   = ""
      target                  = data.google_sql_database_instance.default.psc_service_attachment_link
      network                 = google_compute_network.ipv6_default.name
      subnetwork              = google_compute_subnetwork.ipv6_default.name
      ip_address              = google_compute_address.ipv6_default.id
      allow_psc_global_access = true
    }

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

### REST

  1. Reserve an internal IP address for the Private Service Connect endpoint.

**Note:** You can't use the API to reserve an internal IP address for the endpoint. To reserve this address, use the [`gcloud compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command.
  2. Verify that the IP address is reserved.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the Private Service Connect endpoint
     * REGION_NAME: the name of the region
     * ADDRESS_NAME: the name of the IP address

HTTP method and URL: 
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#address",
      "id": "ADDRESS_ID",
      "creationTimestamp": "2024-05-09T11:20:50.114-07:00",
      "name": "ADDRESS_NAME",
      "description": "This is the name of the internal IP address.",
      "address": "IP_ADDRESS",
      **"status": "RESERVED",**
      "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME",
      "networkTier": "PREMIUM",
      "labelFingerprint": "LABEL_FINGERPRINT_ID",
      "addressType": "EXTERNAL"
    }
    

In the response, verify that a `RESERVED` status appears for the IP address.

  3. Create the Private Service Connect endpoint and point it to the Cloud SQL service attachment.

**Note:** You can't use the API to create the Private Service Connect endpoint. To create this endpoint, use the [`gcloud compute forwarding-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command.
  4. Verify that the service attachment accepts the endpoint.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the Private Service Connect endpoint
     * REGION_NAME: the name of the region
     * ENDPOINT_NAME: the name of the endpoint

HTTP method and URL: 
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#forwardingRule",
      "id": "ENDPOINT_ID",
      "creationTimestamp": "2024-05-09T12:03:21.383-07:00",
      "name": "ENDPOINT_NAME",
      "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME",
      "IPAddress": "IP_ADDRESS",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME",
      "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default",
      "serviceDirectoryRegistrations": [
        {
          "namespace": "goog-psc-default"
        }
      ],
      "networkTier": "PREMIUM",
      "labelFingerprint": "LABEL_FINGERPRINT_ID",
      "fingerprint": "FINGERPRINT_ID",
      "pscConnectionId": "CONNECTION_ID",
      **"pscConnectionStatus": "ACCEPTED",**
      "allowPscGlobalAccess": true
    }
    

In the response, verify that an `ACCEPTED` status appears for the `pscConnectionStatus` field. The endpoint can connect to the service attachment.




## Connect to a Cloud SQL instance

You can connect to a Cloud SQL instance with Private Service Connect enabled by using an internal IP address, a DNS record, the Cloud SQL Auth Proxy, the Cloud SQL Language Connectors, or other Google Cloud applications.

### Connect using a DNS record

DNS is the recommended way to connect to instances with Private Service Connect enabled. A DNS name lets different networks connect to the same instance, where Private Service Connect endpoints in each network might have different IP addresses. Additionally, the Cloud SQL Auth Proxy requires DNS names to connect to these instances. For information about how to set up DNS, see [Configure DNS for Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns).

Before connecting to a Cloud SQL instance using a DNS record, do the following:

  1. Create a Private Service Connect endpoint.
  2. Confirm that the service attachment of the instance accepts the endpoint. To verify that the status of the endpoint is `ACCEPTED`, check the status.
  3. [Configure a DNS managed zone and a DNS record](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns).



After you meet these conditions, use the DNS record to connect to the instance from any VPC network where you created the endpoint.
    
    
    sqlcmd -S DNS_RECORD -d DATABASE_NAME -U USERNAME

Make the following replacements:

  * DNS_RECORD: the endpoint's DNS record
  * DATABASE_NAME: the name of the Cloud SQL for SQL Server database that's contained within the instance
  * USERNAME: the name of the user that's connecting to the instance



### Connect directly through an internal IP address

Before connecting to a Cloud SQL instance with Private Service Connect enabled, do the following:

  1. Create a Private Service Connect endpoint.
  2. Confirm that the service attachment of the instance accepts the endpoint. To verify that the status of the endpoint is `ACCEPTED`, check the status.



After you meet these conditions, use the endpoint's IP address to access the instance from any VPC network where you created the endpoint.

  1. Retrieve the internal IP address of the Private Service Connect endpoint using the name of the endpoint's IP address.

**Note:** You can use the commands in this section to retrieve the internal IP addresses of all endpoints that are created both manaully and automatically. To retrieve the internal IP addresses of endpoints that are created automatically, see Retrieve the endpoint.

### gcloud

To retrieve the IP address, use the [`gcloud compute addresses describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) command:
         
         gcloud compute addresses describe ADDRESS_NAME \
         --project=PROJECT_ID \
         --region=REGION_NAME

Make the following replacements:

     * ADDRESS_NAME: the name of the endpoint's IP address
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the endpoint
     * REGION_NAME: the region name for the endpoint

In the response, verify that an IP address appears for the `address` field. This is the internal IP address.

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the endpoint
     * REGION_NAME: the region name for the endpoint
     * ADDRESS_NAME: the name of the endpoint's IP address

HTTP method and URL: 
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#address",
      "id": "ADDRESS_ID",
      "creationTimestamp": "2024-05-09T11:20:50.114-07:00",
      "name": "ADDRESS_NAME",
      "description": "This is the name of the internal IP address.",
      **"address": " IP_ADDRESS",**
      "status": "RESERVED",
      "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/addresses/ADDRESS_NAME",
      "networkTier": "PREMIUM",
      "labelFingerprint": "LABEL_FINGERPRINT_ID",
      "addressType": "EXTERNAL"
    }
    

The internal IP address is the value that's associated with the `address` field.

  2. Alternatively, retrieve the internal IP address of the Private Service Connect endpoint using the service attachment of the Cloud SQL instance.

### gcloud

To retrieve the IP address, use the [`gcloud compute forwarding-rules list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/list) command:
         
         gcloud compute forwarding-rules list \
         --filter="TARGET:REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME" \
         --project=PROJECT_ID

Make the following replacements:

     * REGION_NAME: the region name for the endpoint
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the endpoint
     * SERVICE_ATTACHMENT_NAME: the name of the service attachment for the Cloud SQL instance

In the response, verify that an IP address appears. This is the internal IP address.

The following is a sample response:

`NAME` | `REGION` | `IP_ADDRESS` | `TARGET`  
---|---|---|---  
`myInstance` | `us-central1` | `10.10.10.10` | `us-central1/serviceAttachments/a-123456789e0a-psc-service-attachment-abc123d4e5f67gh8`  
  
### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the endpoint
     * REGION_NAME: the region name for the endpoint
     * SERVICE_ATTACHMENT_PROJECT_ID: the ID or project number of the Google Cloud project that contains the service attachment
     * SERVICE_ATTACHMENT_NAME: the name of the service attachment for the Cloud SQL instance

HTTP method and URL: 
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules?target="https://www.googleapis.com/compute/v1/projects/SERVICE_ATTACHMENT_PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME"

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules?target="https://www.googleapis.com/compute/v1/projects/SERVICE_ATTACHMENT_PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME""

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules?target="https://www.googleapis.com/compute/v1/projects/SERVICE_ATTACHMENT_PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME"" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#forwardingRuleList",
      "id": "projects/PROJECT_ID/regions/REGION_NAME/forwardingRules",
      "items": [
        {
          "kind": "compute#forwardingRule",
          "id": "FORWARDING_RULE_ID",
          "creationTimestamp": "2023-10-31T13:04:37.168-07:00",
          "name": "FORWARDING_RULE_NAME",
          "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME",
          **"IPAddress": " IP_ADDRESS",**
          "target": "https://www.googleapis.com/compute/v1/projects/SERVICE_ATTACHMENT_PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/FORWARDING_RULE_NAME",
          "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME",
          "serviceDirectoryRegistrations": [
            {
              "namespace": "goog-psc-default"
            }
          ],
          "networkTier": "PREMIUM",
          "labelFingerprint": "LABEL_FINGERPRINT_ID",
          "fingerprint": "FINGERPRINT_ID",
          "pscConnectionId": "PSC_CONNECTION_ID",
          "pscConnectionStatus": "CLOSED",
          "allowPscGlobalAccess": true
        }
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules"
    }
    

The internal IP address is the value that's associated with the `IPAddress` field.

  3. To connect to the Cloud SQL instance, use the internal IP address.
         
         sqlcmd -S IP_ADDRESS -d DATABASE_NAME -U USERNAME

Make the following replacements:

     * IP_ADDRESS: the endpoint's IP address
     * DATABASE_NAME: the name of the Cloud SQL for SQL Server database that's contained within the instance
     * USERNAME: the name of the user that's connecting to the instance



### Connect using the Cloud SQL Auth Proxy

The [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy) is a connector that provides secure access to an instance with Private Service Connect enabled without a need for authorized networks or for configuring SSL.

Configure the Cloud SQL Auth Proxy using the Private Service Connect DNS name of your instance. A DNS name identifies a DNS record that map a DNS resource to a domain name. For more information about enabling DNS for your project, see [Configure DNS in Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns). To locate existing DNS names for your instance, see [Find DNS names](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns#find_dns_names).

You can also configure the Cloud SQL Auth Proxy to use the Private Service Connect write endpoint DNS name of an advanced failover cluster, if you have one enabled. For example, if the Private Service Connect DNS write endpoint name for your cluster is `abcdef123456.987654321fedcb.global.sql-psc.goog` then you would start the auth proxy like this:
    
    
    ./cloud-sql-proxy abcdef123456.987654321fedcb.global.sql-psc.goog

If you're connecting through Private Service Connect, then [Cloud SQL Auth Proxy version v2.5.0](https://github.com/GoogleCloudPlatform/cloud-sql-proxy/) or later is required.

#### Download and install the Cloud SQL Auth Proxy

To connect to instances with Private Service Connect enabled, you must [download and install the binary for the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#install). The binary that you download depends on the operating system, and whether it uses a 32-bit or 64-bit kernel. Most newer hardware uses a 64-bit kernel.

If you're unsure whether your machine is running a 32-bit or 64-bit kernel, then use the `uname -a` command for Linux or macOS. For Windows, see the [Windows documentation](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d).

#### Start the Cloud SQL Auth Proxy

The Cloud SQL Auth Proxy supports connections to instances with Private Service Connect enabled. For more information, see [Start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#start-proxy).

  1. View summary information about a Cloud SQL instance, including the connection name of the instance. 

### gcloud

To view summary information about a Cloud SQL instance, use the   
[`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command.
         
         gcloud sql instances describe INSTANCE_NAME \
             --project=PROJECT_ID \
             --format='value(connectionName)'

Make the following replacements:

     * INSTANCE_NAME: the name of the Cloud SQL instance
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance

The connection name is in the format of `PROJECT_ID:REGION_NAME:INSTANCE_NAME`.

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      ...
      "connectionName": "PROJECT_ID:REGION_NAME:INSTANCE_NAME"
    }
    

The connection name is in the format of `PROJECT_ID:REGION_NAME:INSTANCE_NAME`.

  2. Copy the instance connection name.
  3. Launch the Cloud SQL Auth Proxy:
         
         ./cloud-sql-proxy INSTANCE_CONNECTION_NAME --psc

Replace INSTANCE_CONNECTION_NAME with the instance connection name that you copied in the previous step.

**Note:** Use the `psc` flag to start the Cloud SQL Auth Proxy to connect to instances with Private Service Connect enabled.




### Connect using the Cloud SQL Language Connectors

The [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors) are libraries that provide secure access to a Cloud SQL instance with Private Service Connect enabled without a need for authorized networks or for configuring SSL.

Configure the Cloud SQL Auth Proxy using the Private Service Connect DNS name of your instance, and the Private Service Connect write endpoint DNS name of an advanced failover cluster, if you have one enabled. A DNS name identifies a DNS record that map a DNS resource to a domain name. For more information about enabling DNS for your project, see [Configure DNS in Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns). To locate existing DNS names for your instance, see [Find DNS names](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns#find_dns_names).

The Cloud SQL Language Connectors support Private Service Connect connections through the `PSC` IP type within their respective libraries. Documentation for each connector is in the public documentation on GitHub for [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery):

  * [Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector) [(v1.3.0 or later)](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/releases/tag/v1.3.0)
  * [Cloud SQL Go Connector](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector) [(v1.4.0 or later)](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/releases/tag/v1.4.0)
  * [Cloud SQL Java Connector](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory) [(v1.13.0 or later)](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/releases/tag/v1.13.0)
  * [Cloud SQL Node.js Connector](https://github.com/GoogleCloudPlatform/cloud-sql-nodejs-connector) [(v0.5.0 or later)](https://github.com/GoogleCloudPlatform/cloud-sql-nodejs-connector/releases/tag/v0.5.0)



### Connect from App Engine Standard, Cloud Run, or Cloud Run functions

To connect to Cloud SQL instances with Private Service Connect enabled, you can use [App Engine Standard](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-standard) or [Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run).

In these supported serverless environments, both the [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors) and direct TCP connections by using an IP address and port number are supported. For direct TCP connections, this is the IP address that you reserve when you create the Private Service Connect endpoint. You can specify the IP address as the address for the database host.

If you [create a DNS record](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns) for the endpoint, then you can specify this record for the host.

### Connect from BigQuery

To access data in Cloud SQL and make queries against this data over an internal IP connection, use the   
`--enable-google-private-path` parameter . This parameter is valid only if: 

  * You use the `--no-assign-ip` parameter.
  * You use the `--network` parameter to specify the name of the VPC network that you want to use to create an internal connection.



## Configure outbound connectivity for your Cloud SQL instance

You can configure your Private Service Connect-enabled Cloud SQL instance to have outbound connectivity with your network using a Private Service Connect interface and a [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments). For more information about how Private Service Connect outbound connectivity works and its limitations, see [Private Service Connect outbound connectivity overview](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-outbound).

To use outbound connectivity with your Cloud SQL instance, you need to:

  1. [Create](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachment) or [update](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#update) a network attachment. This network attachment is used by the Cloud SQL instance to connect to your network's Private Service Connect interface.

     1. The network attachment must be in the same region as your Cloud SQL instance, and be [set up to automatically accept connections](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies) using a list from Private Service Connect interfaces.

**Note:** If a Cloud SQL instance is configured for [high availability](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability#HA-configuration), then the instance requires two IP addresses: one for the primary instance and one for the standby instance.
     2. Get the Cloud SQL tenant project ID. Use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command to retrieve details about the instance. You can find the tenant project ID in the service attachment URL shown in the output:
            
            ADMIN_PROJECT=PROJECT_ID
              INSTANCE_NAME=INSTANCE_NAME
            
              TENANT_PROJECT_ID=$(gcloud --project=$ADMIN_PROJECT sql instances describe $INSTANCE_NAME | grep pscServiceAttachmentLink | cut -f 2 -d "/")
            

Replace the following:

        * PROJECT_ID: the project ID for the Google Cloud project you're using.
        * INSTANCE_NAME: the name of the Private Service Connect-enabled Cloud SQL instance that you want to set up for outbound connectivity.

Save the value for the tenant project ID to later include in the list of [accepted project IDs](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#gcloud). This is required when you create or update a network attachment in your Google Cloud project.

  2. Identify your network that you want to receive Cloud SQL outbound connections from and ensure it has a Private Service Connect interface.

  3. Enable outbound connections to your Cloud SQL instance using the network attachment.




You can also disable outbound connectivity at any time when you no longer require outbound connections to your instance.

For more information about Private Service Connect outbound connectivity, see [Private Service Connect outbound connections](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-outbound).

### Enable outbound connections for your Cloud SQL instance

To enable outbound connectivity for your Cloud SQL instance, you need to first [create](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachments) or [update](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#update) a network attachment in your Google Cloud project.

**Note:** Enabling Private Service Connect outbound connectivity requires downtime. You can expect this operation to take about 8 minutes to complete with an approximate downtime of 3 minutes.

###  gcloud 

To enable outbound connectivity, run the following command:
    
    
    gcloud beta sql instances patch INSTANCE_NAME \
      --psc-network-attachment-uri=NETWORK_ATTACHMENT_URI \
      --project=PROJECT_ID
    

Replace the following:

  * INSTANCE_NAME: the name of the Private Service Connect-enabled Cloud SQL instance that you want to set up for outbound connectivity.
  * NETWORK_ATTACHMENT_URI: the URI of the network attachment within your Google Cloud project that you want to use to connect to your network's Private Service Connect interface.
  * PROJECT_ID: the project ID for the Google Cloud project you're using.



You can confirm that Private Service Connect outbound connectivity was enabled successfully by running [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe). If you see `psc-network-attachment-uri` in the output, then Private Service Connect outbound connectivity was enabled successfully.

###  REST v1 

To enable outbound connectivity, run the following command:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `NETWORK_ATTACHMENT_URI`: the URI of the network attachment in your project.
  * `INSTANCE_ID`: the name of your Cloud SQL instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "ipConfiguration": {
          "pscConfig: {
            "networkAttachmentUri": "NETWORK_ATTACHMENT_URI"
            "kind": "sql#settings"
          }
        },
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": USER,
      "insertTime": "2025-05-13T20:44:23.064Z",
      "operationType": "UPDATE",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID","
    }
    

###  REST v1beta4 

To enable outbound connectivity, run the following command:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `NETWORK_ATTACHMENT_URI`: the URI of the network attachment in your project.
  * `INSTANCE_ID`: the name of your Cloud SQL instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "ipConfiguration": {
          "pscConfig: {
            "networkAttachmentUri": "NETWORK_ATTACHMENT_URI"
          }
        },
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": USER,
      "insertTime": "2025-05-13T20:44:23.064Z",
      "operationType": "UPDATE",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID","
    }
    

For troubleshooting information related to Private Service Connect outbound connectivity, see [Private Service Connect troubleshooting](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshooting#psc).

### Disable outbound connections for your Cloud SQL instance

**Note:** Disabling Private Service Connect outbound connectivity requires downtime. You can expect this operation to take about 8 minutes to complete with an approximate downtime of 3 minutes.

###  gcloud 

To disable outbound connectivity, run the following command:
    
    
    gcloud beta sql instances patch INSTANCE_NAME \
      --clear-psc-network-attachment-uri \
      --project=PROJECT_ID
    

Replace the following:

  * INSTANCE_NAME: the name of the Private Service Connect-enabled Cloud SQL instance that you want to set up for outbound connectivity.
  * PROJECT_ID: the project ID for the Google Cloud project you're using.



###  REST v1 

To disable outbound connectivity, run the following command:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `NETWORK_ATTACHMENT_URI`: the URI of the network attachment in your project. To disable, set to `null`.
  * `INSTANCE_ID`: the name of your Cloud SQL instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "ipConfiguration": {
          "pscConfig: {
            "networkAttachmentUri": null,
            "kind": "sql#settings"
          }
        },
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": USER,
      "insertTime": "2025-05-13T20:44:23.064Z",
      "operationType": "UPDATE",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID","
    }
    
    

###  REST v1beta4 

To disable outbound connectivity, run the following command:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your project.
  * `NETWORK_ATTACHMENT_URI`: the URI of the network attachment in your project. To disable, set to `null`.
  * `INSTANCE_ID`: the name of your Cloud SQL instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "ipConfiguration": {
          "pscConfig: {
            "networkAttachmentUri": null,
            "kind": "sql#settings"
          }
        },
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": USER,
      "insertTime": "2025-05-13T20:44:23.064Z",
      "operationType": "UPDATE",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID","
    }
    
    

## Test connectivity

To test inbound connectivity to a Cloud SQL instance with Private Service Connect enabled, set the IP address of the Private Service Connect endpoint to be the destination IP address.

### gcloud

To create a connectivity test for a Cloud SQL instance with Private Service Connect enabled, use the [`gcloud network-management connectivity-tests create`](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create) command:
    
    
    gcloud network-management connectivity-tests create CONNECTIVITY_TEST_NAME \
    --source-instance=SOURCE_INSTANCE \
    --destination-cloud-sql-instance=DESTINATION_CLOUD_SQL_INSTANCE \
    --destination-network=DESTINATION_NETWORK \
    --destination-port=DESTINATION_PORT \
    --protocol=tcp \
    --round-trip

Make the following replacements:

  * CONNECTIVITY_TEST_NAME: the name of the connectivity test.
  * SOURCE_INSTANCE: the URI for the Compute Engine instance where the source IP address is located (for example, `projects/myproject/zones/myzone/instances/myinstance`).
  * DESTINATION_CLOUD_SQL_INSTANCE: the URL for the Cloud SQL instance (for example, `projects/myproject/instances/myinstance`).
  * DESTINATION_NETWORK: the URI for the VPC network where the destination IP address is located (for example, `projects/myproject/global/networks/mynetwork`).
  * DESTINATION_PORT: the port number reserved for the instance. For Cloud SQL for SQL Server instances, the port number is `1433`.



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * CONNECTIVITY_TEST_NAME: the name of the connectivity test.
  * SOURCE_IP_ADDRESS: the IP address of the source Compute Engine instance.
  * SOURCE_INSTANCE: the URI for the Compute Engine instance where the source IP address is located (for example, `projects/myproject/zones/myzone/instances/myinstance`).
  * SOURCE_NETWORK: the URI for the VPC network where the source IP address is located (for example, `projects/myproject/global/networks/mynetwork`).
  * DESTINATION_IP_ADDRESS: the IP address of the destination Cloud SQL instance.
  * DESTINATION_PORT: the port number reserved for the instance. For Cloud SQL for SQL Server instances, the port number is `1433`.
  * DESTINATION_NETWORK: the URI for the VPC network where the destination IP address is located (for example, `projects/myproject/global/networks/mynetwork`).



HTTP method and URL: 
    
    
    POST https://networkmanagement.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/connectivityTests?testId=CONNECTIVITY_TEST_NAME

Request JSON body: 
    
    
    {
      "source": {
        "ipAddress": "SOURCE_IP_ADDRESS",
        "instance": "SOURCE_INSTANCE",
        "network": "SOURCE_NETWORK"
      },
      "destination": {
        "ipAddress": "DESTINATION_IP_ADDRESS",
        "port": DESTINATION_PORT,
        "network": "DESTINATION_NETWORK",
        "projectId": "PROJECT_ID"
      },
      "protocol": "TCP"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://networkmanagement.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/connectivityTests?testId=CONNECTIVITY_TEST_NAME"

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
        -Uri "https://networkmanagement.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/connectivityTests?testId=CONNECTIVITY_TEST_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/operations/operation-OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.networkmanagement.v1.OperationMetadata",
        "createTime": "2024-05-23T16:43:49.313981473Z",
        "target": "projects/PROJECT_ID/locations/global/connectivityTests/CONNECTIVITY_TEST_NAME",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

**Note:** In addition to testing connectivity, you can restrict connectivity to Private Service Connect endpoints from service consumers in a VPC network. To do this, use the [`gcloud compute firewall-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) command to create a network egress firewall rule. This rule applies to the IP address of an endpoint. For the rule, define the source to be all VMs in the VPC network and specify a tag or service account.

## Limitations

  * You can set up to 20 Private Service Connect endpoints that connect to the service attachment of a Cloud SQL instance with Private Service Connect enabled.

If you need to connect from more VPC networks, then use Private Service Connect endpoint propagation through NCC. For more information, see [Private Service Connect endpoint propagation](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint-propagation).

  * You can have up to [64,512 concurrent connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) with Private Service Connect to a Cloud SQL instance.

**Note:** For Cloud SQL instances created on or after September 30, 2026 with 16 or more vCPUs, you can have up to 129,024 concurrent connections if the database engine supports it.
  * The following [flags](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance) are invalidated or impacted:

    * `--no-assign-ip:` use this flag because instances with Private Service Connect enabled aren't supported to use other connectivity types such as external IP connections
    * `--authorized-networks:` you can't use this flag to add [authorized networks](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks)
    * `--network:` you can't use this flag because it's associated with [private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access)
    * `--allocated-ip-range-name:` you can't use this flag because allowed IP range names aren't supported
  * You can't configure an instance that has Private Service Connect enabled to use private services access or external IP connections.

    * You can't enable external IP connections on an instance with Private Service Connect enabled.
    * You can't enable private services access or add authorized networks to the instance.
    * You can't change the [connectivity type](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) of the instance. 
    * You can't use the `gcloud sql connect` command, Cloud Shell, Cloud Build, Database Migration Service, or Datastream to connect to Cloud SQL instances with Private Service Connect enabled. 

    * When testing connectivity to a Cloud SQL instance with Private Service Connect enabled, you can't set the following items:

      * The instance's internal IP address or DNS name as the destination directly
      * The instance as the source
      * The IP address of the Private Service Connect endpoint as the source
    * IP-based allowlisting by using authorized networks isn't supported.

    * IP-based allowlisting enforced by [Context-Aware Access](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access) isn't supported. 

    * For Cloud SQL instances with Private Service Connect enabled, Managed Service for Microsoft Active Directory (also called Managed Microsoft AD) isn't supported. 

## Troubleshoot

This section contains information about issues associated with Cloud SQL instances with Private Service Connect enabled along with steps for troubleshooting the issues.

Issue | Troubleshooting  
---|---  
The service attachment of the instance doesn't accept the Private Service Connect endpoint. | 
      1. Check the endpoint's status. 

### gcloud

To check the status, use the   
[`gcloud compute forwarding-rules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe) command.
             
             gcloud compute forwarding-rules describe ENDPOINT_NAME \
             --project=PROJECT_ID \
             --region=REGION_NAME \
             | grep pscConnectionStatus

Make the following replacements:
         * ENDPOINT_NAME: the name of the endpoint
         * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the endpoint
         * REGION_NAME: the region name for the endpoint

### REST

Before using any of the request data, make the following replacements: 
         * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the Private Service Connect endpoint
         * REGION_NAME: the name of the region
         * ENDPOINT_NAME: the name of the endpoint
HTTP method and URL: 
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).  Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).  Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#forwardingRule",
      "id": "ENDPOINT_ID",
      "creationTimestamp": "2024-05-09T12:03:21.383-07:00",
      "name": "ENDPOINT_NAME",
      "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME",
      "IPAddress": "IP_ADDRESS",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME",
      "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default",
      "serviceDirectoryRegistrations": [
        {
          "namespace": "goog-psc-default"
        }
      ],
      "networkTier": "PREMIUM",
      "labelFingerprint": "LABEL_FINGERPRINT_ID",
      "fingerprint": "FINGERPRINT_ID",
      "pscConnectionId": "CONNECTION_ID",
      **"pscConnectionStatus": "ACCEPTED",**
      "allowPscGlobalAccess": true
    }
    

      2. Verify that the status of the endpoint is `ACCEPTED`. If the status is `PENDING`, then the instance isn't allowing the Google Cloud project that contains the endpoint. Make sure that the network project in which the endpoint is created is allowed. For more information, see [Edit an instance with Private Service Connect enabled](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance#edit-psc-instance).  
`ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: The resource 'projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME' was not found` | This error message can occur when reserving a static internal IP address for the Private Service Connect endpoint. Make sure the subnet specified exists in the project specified by the URI. If you want to create an endpoint in a service project but use a subnet from a Shared VPC network, you need to specify the subnet by its URI and use the host project's project ID in the URI. For more information, see [Create the endpoint manually](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-endpoint-manually).  
`ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: - The resource 'projects/PROJECT_ID/global/networks/NETWORK_NAME' was not found` | This error message can occur when you create a Private Service Connect endpoint manually. Make sure the network specified exists in the project specified by the URI. If you want to create an endpoint in a service project but use a Shared VPC network, you need to specify the network by its URI and use the host project's project ID in the URI. For more information, see [Create the endpoint manually](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-endpoint-manually).  
`Invalid consumer network status for PSC auto connection`. |  The consumer network is either not configured correctly, or not configured at all, and therefore, no endpoint is available to connect to. To connect to the endpoint, you'll need to check the status of the endpoint, and fix the error before trying to connect again.  
To check the status of an endpoint, see [Retrive the endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#retrieve-endpoint). The status of the endpoint can be one of the following:
      * `CONNECTION_POLICY_MISSING`: there is no matching service connection policy on the consumer network. Service connection policies are configured by network, by region. To reconfigure the network, see [Update a service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 
      * `CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED`: there is a matching service connection policy, but the [Service instance scope](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope) field in the policy is not configured to allow connection to this Cloud SQL instance. Update the policy to configure the value of the **Service instance scope** field (`--producer-instance-location`) with the project, folder, or organization where the Cloud SQL instance resides. To reconfigure the service connection policy, see [Update a service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 
      * `POLICY_LIMIT_REACHED`: the service connection policy has reached its endpoint limit. To resolve, you'll need to increase the endpoint limit by [updating the service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy).   
`No permission to create a service connection policy`. |  You don't have the required permissions to create a service connection policy. To create a service connection policy, you need the `Compute Network Admin IAM` role. For more information, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/sqlserver/roles-and-permissions).   
The network attachment is unable to accept connections from the Private Service Connect interface when using [Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-outbound).  |  If your external network is unable to accept connections from the Private Service Connect interface, then the connection policies on your network attachment may not be configured correctly.  
  
Network attachments need to be configured to either accept all connections automatically, or configured manually with a list of accepted connections. For more information, see [Connection policies](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies).  Use the following command to verify the accepted connections in your network attachment:
    
    gcloud compute network-attachments describe default
        --region=REGION_ID
        

If the Private Service Connect interface isn't on the accepted list, then [update your network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#update). For more information, see [Manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments).   
  
## What's next

      * Learn more about [private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip).
      * Learn more about [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect).
      * Learn more about [creating a read replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica#create-read-replica-cloud-sql-instance-psc-enabled) of an instance with Private Service Connect enabled.
      * Learn more about [cloning](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance#clone-instance) an instance with Private Service Connect enabled.
      * Learn more about [viewing summary information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info#info) about instances with Private Service Connect enabled.
      * Learn more about [setting](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [removing](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance) high availability for an instance with Private Service Connect enabled.
      * Learn more about [editing](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance#edit-psc-instance) and [deleting](https://docs.cloud.google.com/sql/docs/sqlserver/delete-instance#delete-cloud-sql-instance) an instance with Private Service Connect enabled.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
