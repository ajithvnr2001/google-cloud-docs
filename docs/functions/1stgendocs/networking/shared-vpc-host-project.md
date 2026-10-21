---
url: https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-host-project/
title: Configure connectors in the Shared VPC host project \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.899707+00:00
---

# Configure connectors in the Shared VPC host project  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-host-project/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure connectors in the Shared VPC host project

If your organization uses Shared VPC, you can set up Serverless VPC Access connectors in either the service project or the host project. This guide shows how to set up a connector in the host project.

If you need to set up a connector in a service project, see [Configure connectors in service projects](https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-service-projects). To learn about the advantages of each method, see [Connecting to a Shared VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-shared-vpc).

**Note:** Serverless VPC Access connectors incur a monthly charge. For more information, see Serverless VPC Access [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing).

## Before you begin

  1. Check the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles for the account you are currently using. The active account must have the following roles on the host project:

     * [Compute Network Viewer (`compute.networkViewer`)](https://cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer)
     * [Project IAM Admin (`resourcemanager.projectIamAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)
     * [Service Usage Admin (`serviceuseage.serviceUsageAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)
     * [Serverless VPC Access Admin (`vpcaccess.admin`)](https://cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin)
  2. Select the host project in your preferred environment.




### Console

  1. Open the Google Cloud console dashboard.

[Go to Google Cloud console dashboard](https://console.cloud.google.com/)

  2. In the menu bar at the top of the dashboard, click the project dropdown menu and select the host project.




### gcloud

Set the default project in the gcloud CLI to the host project by running the following in your terminal: 
    
    
    gcloud config set project HOST_PROJECT_ID

Replace the following:

  * `HOST_PROJECT_ID`: the ID of the Shared VPC host project



## Create a Serverless VPC Access connector

To send requests to your VPC network and receive the corresponding responses, you must create a Serverless VPC Access connector. You can create a connector by using the Google Cloud console, Google Cloud CLI, or Terraform:

###  Console 

  1. Enable the Serverless VPC Access API for your project.

[Enable API](https://console.cloud.google.com/marketplace/details/google/vpcaccess.googleapis.com)

  2. Go to the Serverless VPC Access overview page.

[Go to Serverless VPC Access](https://console.cloud.google.com/networking/connectors)

  3. Click **Create connector**.

  4. In the **Name** field, enter a name for your connector. The name must follow the Compute Engine [naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) and be less than 21 characters. Hyphens (`-`) count as two characters.

  5. In the **Region** field, select a region for your connector. This must match the region of your serverless service.

If your service is in the region `us-central` or `europe-west`, use `us-central1` or `europe-west1`.

  6. In the **Network** field, select the VPC network to attach your connector to.

  7. Click the **Subnetwork** pulldown menu:

Select an unused `/28` subnet.

     * Subnets must be used exclusively by the connector. They cannot be used by other resources such as VMs, Private Service Connect, or load balancers.
     * To confirm that your subnet is not used for Private Service Connect or Cloud Load Balancing, check that the subnet [`purpose`](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--purpose) is `PRIVATE` by running the following command in the gcloud CLI: 
           
           gcloud compute networks subnets describe SUBNET_NAME
           

Replace `SUBNET_NAME` with the name of your subnet.
  8. (Optional) To set scaling options for additional control over the connector, click **Show Scaling Settings** to display the scaling form.

     1. Set the minimum and maximum number of instances for your connector, or use the defaults, which are 2 (min) and 10 (max). The connector scales out to the maximum specified as traffic increases, but _the connector does not scale back in when traffic decreases_. You must use values between `2` and `10`, and the `MIN` value must be less than the `MAX` value.
     2. In the **Instance Type** pulldown menu, choose the machine type to be used for the connector, or use the default `e2-micro`. Notice the cost sidebar on the right when you choose the instance type, which displays bandwidth and cost estimations.
  9. Click **Create**.

  10. A green check mark will appear next to the connector's name when it is ready to use.




###  gcloud 

  1. Update `gcloud` components to the latest version:
         
         gcloud components update
         

  2. Enable the Serverless VPC Access API for your project:
         
         gcloud services enable vpcaccess.googleapis.com
         

  3. Create a Serverless VPC Access connector:
         
         gcloud compute networks vpc-access connectors create CONNECTOR_NAME \
         --region=REGION \
         --subnet=SUBNET \
         --subnet-project=HOST_PROJECT_ID \
         # Optional: specify minimum and maximum instance values between 2 and 10, default is 2 min, 10 max.
         --min-instances=MIN \
         --max-instances=MAX \
         # Optional: specify machine type, default is e2-micro
         --machine-type=MACHINE_TYPE

Replace the following:

     * `CONNECTOR_NAME`: a name for your connector. The name must follow the Compute Engine [naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) and be less than 21 characters. Hyphens (`-`) count as two characters.
     * `REGION`: a region for your connector; this must match the region of your serverless service. If your service is in the region `us-central` or `europe-west`, use `us-central1` or `europe-west1`.
     * `SUBNET`: the name of an unused `/28` subnet. 
       * Subnets must be used exclusively by the connector. They cannot be used by other resources such as VMs, Private Service Connect, or load balancers.
       * To confirm that your subnet is not used for Private Service Connect or Cloud Load Balancing, check that the subnet [`purpose`](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create#--purpose) is `PRIVATE` by running the following command in the gcloud CLI: 
             
             gcloud compute networks subnets describe SUBNET_NAME
             

Replace the following: 
         * `SUBNET_NAME`: the name of your subnet
     * `HOST_PROJECT_ID`: the ID of the host project
     * `MIN`: the minimum number of instances to use for the connector. Use an integer between `2` and `9`. Default is `2`. To learn about connector scaling, see [Throughput and scaling](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#scaling).
     * `MAX`: the maximum number of instances to use for the connector. Use an integer between `3` and `10`. Default is `10`. If traffic requires it, the connector scales out to `[MAX]` instances, _but does not scale back in_. To learn about connector scaling, see [Throughput and scaling](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#scaling).
     * `MACHINE_TYPE`: `f1-micro`, `e2-micro`, or `e2-standard-4`. To learn about connector throughput, including machine type and scaling, see [Throughput and scaling](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#scaling).

For more details and optional arguments, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/vpc-access/connectors/create).

  4. Verify that your connector is in the `READY` state before using it:
         
         gcloud compute networks vpc-access connectors describe CONNECTOR_NAME \
         --region=REGION

Replace the following:

     * `CONNECTOR_NAME`: the name of your connector; this is the name that you specified in the previous step
     * `REGION`: the region of your connector; this is the region that you specified in the previous step

The output should contain the line `state: READY`.




### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service) to enable the `vpcaccess.googleapis.com` API.
    
    
    resource "google_project_service" "vpcaccess-api" {
      project = var.project_id # Replace this with your project ID in quotes
      service = "vpcaccess.googleapis.com"
    }

You can use [Terraform modules](https://github.com/terraform-google-modules/terraform-google-network) to create a VPC network and subnet and then create the connector.
    
    
    module "test-vpc-module" {
      source       = "terraform-google-modules/network/google"
      version      = "~> 18.0"
      project_id   = var.project_id # Replace this with your project ID in quotes
      network_name = "my-serverless-network"
      mtu          = 1460
    
      subnets = [
        {
          subnet_name   = "serverless-subnet"
          subnet_ip     = "10.10.10.0/28"
          subnet_region = "us-central1"
        }
      ]
    }
    
    module "serverless-connector" {
      source     = "terraform-google-modules/network/google//modules/vpc-serverless-connector-beta"
      version    = "~> 18.0"
      project_id = var.project_id
      vpc_connectors = [{
        name        = "central-serverless"
        region      = "us-central1"
        subnet_name = module.test-vpc-module.subnets["us-central1/serverless-subnet"].name
        # host_project_id = var.host_project_id # Specify a host_project_id for shared VPC
        machine_type  = "e2-standard-4"
        min_instances = 2
        max_instances = 7
        }
        # Uncomment to specify an ip_cidr_range
        #   , {
        #     name          = "central-serverless2"
        #     region        = "us-central1"
        #     network       = module.test-vpc-module.network_name
        #     ip_cidr_range = "10.10.11.0/28"
        #     subnet_name   = null
        #     machine_type  = "e2-standard-4"
        #     min_instances = 2
        #   max_instances = 7 }
      ]
      depends_on = [
        google_project_service.vpcaccess-api
      ]
    }

## Enable Cloud Run functions for the service project

Enable the Cloud Run functions API for the service project. This is necessary for adding IAM roles in subsequent steps and for the service project to use Cloud Run functions.

###  Console 

  1. Open the page for the Cloud Run functions API.

[Cloud Run functions API](https://console.cloud.google.com/marketplace/details/google/cloudfunctions.googleapis.com)

  2. In the menu bar at the top of the dashboard, click the project dropdown menu and select the service project.

  3. Click **Enable**.




###  gcloud 

Run the following in your terminal:
    
    
    gcloud services enable cloudfunctions.googleapis.com --project=SERVICE_PROJECT_ID
    

Replace the following:

  * `SERVICE_PROJECT_ID`: the ID of the service project



## Provide access to the connector

Provide access to the connector by granting the [Cloud Run functions Service Agent](https://docs.cloud.google.com/functions/1stgendocs/concepts/iam#access_control_for_service_accounts) **Serverless VPC Access User** IAM role to the service project on the host project.

###  Console 

  1. Open the IAM page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the project dropdown menu and select the host project.

  3. Click **Grant access**.

  4. In the **New principals** field, enter the email address of the Cloud Run functions Service Agent for the service project: 
         
         service-SERVICE_PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com

Replace the following:

     * `SERVICE_PROJECT_NUMBER`: the project number associated with the service project. This is different than the project ID. You can find the project number on the service project's [Project Settings](https://console.cloud.google.com/iam-admin/settings) page in the Google Cloud console.
  5. In the **Role** field, select **Serverless VPC Access User**.

  6. Click **Save**.




###  gcloud 

  1. Run the following command in your terminal:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
         --member=serviceAccount:service-SERVICE_PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com \
         --role=roles/vpcaccess.user
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the Shared VPC host project
     * `SERVICE_PROJECT_NUMBER`: the project number associated with the service project. This is different than the project ID. You can find the project number by running the following command:
           
           gcloud projects describe SERVICE_PROJECT_ID
           




## Make the connector discoverable

On the host project's IAM policy, you must grant the following two predefined roles to the principals who deploy Cloud Run services:

  * [Serverless VPC Access Viewer (`vpcaccess.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.viewer): Required.
  * [Compute Network Viewer (`compute.networkViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer): Optional but recommended. Allows the IAM principal to enumerate subnets in the Shared VPC network.



Alternatively, you can use custom roles or other predefined roles that include all the permissions of the Serverless VPC Access Viewer (`vpcaccess.viewer`) role.

###  Console 

  1. Open the IAM page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the project dropdown menu and select the host project.

  3. Click **Grant access**.

  4. In the **New principals** field, enter the email address of the principal that should be able to see the connector from the service project. You can enter multiple emails in this field.

  5. In the **Role** field, select both of the following roles:

     * **Serverless VPC Access Viewer**
     * **Compute Network Viewer**
  6. Click **Save**.




###  gcloud 

Run the following commands in your terminal:
    
    
    gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
    --member=PRINCIPAL \
    --role=roles/vpcaccess.viewer
    
    gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
    --member=PRINCIPAL \
    --role=roles/compute.networkViewer
    

Replace the following:

  * `HOST_PROJECT_ID`: the ID of the Shared VPC host project
  * `PRINCIPAL`: the principal who deploys Cloud Run services. Learn more about the [`--member` flag](https://cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding#--member).



## Configure your function to use the connector

For each function that requires access to your Shared VPC, you must specify the connector for the function. The following steps show how to configure your function to use a connector.

###  Console 

  1. Open the Cloud Run functions overview page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

  2. Click the project dropdown menu and select the service project.

  3. Click **Create function**. Alternatively, click an existing function to go to its details page, and click **Edit**.

  4. Expand the advanced settings by clicking **Runtime, build...**.

  5. In the **Connections** tab under Egress settings, select your connector in the **VPC connector** field.




###  gcloud 

  1. Set the gcloud CLI to use the project containing the function: 
         
         gcloud config set project PROJECT_ID

Replace the following: 
     * `PROJECT_ID`: the ID of the project containing the function that requires access to your Shared VPC. If the function is in the host project, this is the host project ID. If the function is in a service project, this is the service project ID.
  2. Use the [`--vpc-connector` flag](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--vpc-connector) and deploy your function:
         
         gcloud functions deploy FUNCTION_NAME --vpc-connector=CONNECTOR_NAME
         




Replace the following:

  * `FUNCTION_NAME`: the name of your function
  * `CONNECTOR_NAME`: the name of your connector. Use the fully qualified name when deploying from a Shared VPC service project (as opposed to the host project), for example: 
        
        projects/HOST_PROJECT_ID/locations/CONNECTOR_REGION/connectors/CONNECTOR_NAME

where `HOST_PROJECT_ID` is the ID of the host project, `CONNECTOR_REGION` is the region of your connector, and `CONNECTOR_NAME` is the name that you gave your connector.



For more control over which requests are routed through the connector, see [Egress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#egress_settings).

**Note:** Administrators can require that functions specify a Serverless VPC Access connector by setting the [`cloudfunctions.requireVPCConnector`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

## Next steps

  * [Connect to Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-functions) from Cloud Run functions.
  * [Configure network settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings) for Cloud Run functions.
  * Monitor admin activity with [Serverless VPC Access audit logging](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access-audit-logging).
  * Protect resources and data by [creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) with VPC Service Controls.
  * Learn about the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles associated with Serverless VPC Access. See [Serverless VPC Access roles](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess) in the IAM documentation for a list of permissions associated with each role.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
