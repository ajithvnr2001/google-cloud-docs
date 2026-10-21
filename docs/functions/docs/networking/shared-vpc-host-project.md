---
url: https://docs.cloud.google.com/functions/docs/networking/shared-vpc-host-project/
title: Configure connectors in the Shared VPC host project \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:40:58.063737+00:00
---

# Configure connectors in the Shared VPC host project  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/networking/shared-vpc-host-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure connectors in the Shared VPC host project Stay organized with collections  Save and categorize content based on your preferences. 

If your organization uses Shared VPC, you can set up a Serverless VPC Access connector in either the service project or the host project. This guide shows how to set up a connector in the host project.

If you need to set up a connector in a service project, see [Configure connectors in service projects](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-service-projects). To learn about the advantages of each method, see [Connecting to a Shared VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-shared-vpc).

## Before you begin

  1. Check the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles for the account you are currently using. The active account must have the following roles on the host project:

     * [Compute Network Viewer (`compute.networkViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer)
     * [Project IAM Admin (`resourcemanager.projectIamAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)
     * [Service Usage Admin (`serviceusage.serviceUsageAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)
     * [Serverless VPC Access Admin (`vpcaccess.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin)
  2. Select the host project in your preferred environment.




### Console

  1. Open the Google Cloud console dashboard.

[Go to Google Cloud console dashboard](https://console.cloud.google.com/)

  2. In the menu bar at the top of the dashboard, click the project dropdown menu and select the host project.




###  gcloud 

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

## Enable Cloud Run for the service project

Enable the Cloud Run API for the service project. This is necessary for adding IAM roles in subsequent steps and for the service project to use Cloud Run.

###  Console 

  1. Open the page for the Cloud Run API.

[Cloud Run API](https://console.cloud.google.com/marketplace/details/google/run.googleapis.com)

  2. In the menu bar at the top of the dashboard, click the project dropdown menu and select the service project.

  3. Click **Enable**.




###  gcloud 

Run the following in your terminal:
    
    
    gcloud services enable run.googleapis.com --project=SERVICE_PROJECT_ID
    

Replace the following:

  * `SERVICE_PROJECT_ID`: the ID of the service project



## Provide access to the connector

Provide access to the connector by granting the service project [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) the **Serverless VPC Access User** IAM role on the host project.

###  Console 

  1. Open the IAM page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the project dropdown menu and select the host project.

  3. Click **Add**.

  4. In the **New principals** field, enter the email address of the Cloud Run Service Agent for the Cloud Run service: 
         
         service-SERVICE_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com

Replace the following:

     * `SERVICE_PROJECT_NUMBER`: the project number associated with the service project. This is different than the project ID. You can find the project number on the service project's [Project Settings](https://console.cloud.google.com/iam-admin/settings) page in the Google Cloud console.
  5. In the **Role** field, select **Serverless VPC Access User**.

  6. Click **Save**.




###  gcloud 

Run the following in your terminal:
    
    
    gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
    --member=serviceAccount:service-SERVICE_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com \
    --role=roles/vpcaccess.user
    

Replace the following:

  * `HOST_PROJECT_ID`: the ID of the Shared VPC host project
  * `SERVICE_PROJECT_NUMBER`: the project number associated with the service account. This is different than the project ID. You can find the project number by running the following:
        
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

  3. Click **Add**.

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
  * `PRINCIPAL`: the principal who deploys Cloud Run services. Learn more about the [`--member` flag](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding#--member).



## Configure your service to use the connector

For each Cloud Run service that requires access to your Shared VPC, you must specify the connector for the service. You can specify the connector by using the Google Cloud console, Google Cloud CLI, YAML file or Terraform when deploying a new service or updating an existing service.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Networking** tab.

  4. In the **Network** menu, select a connector to use.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

  1. Set the gcloud CLI to use the project containing the Cloud Run resource: 
         
         gcloud config set project PROJECT_ID

Replace the following: 
     * `PROJECT_ID`: the ID of the project containing the Cloud Run resource that requires access to your Shared VPC. If the Cloud Run resource is in the host project, this is the host project ID. If the Cloud Run resource is in a service project, this is the service project ID.
  2. Use the `--vpc-connector` flag.



  * For existing services: 
        
        gcloud run services update SERVICE --vpc-connector=CONNECTOR_NAME

  * For new services: 
        
        gcloud run deploy SERVICE --image=IMAGE_URL --vpc-connector=CONNECTOR_NAME

Replace the following: 
    * `SERVICE`: the name of your service
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`
    * `CONNECTOR_NAME`: the name of your connector. Use the fully qualified name when deploying from a Shared VPC service project (as opposed to the host project), for example: 
          
          projects/HOST_PROJECT_ID/locations/CONNECTOR_REGION/connectors/CONNECTOR_NAME

where `HOST_PROJECT_ID` is the ID of the host project, `CONNECTOR_REGION` is the region of your connector, and `CONNECTOR_NAME` is the name that you gave your connector.



### YAML

Set the gcloud CLI to use the project containing the Cloud Run resource: 
    
    
    gcloud config set project PROJECT_ID

Replace the following:

  * `PROJECT_ID`: the ID of the project containing the Cloud Run resource that requires access to your Shared VPC. If the Cloud Run resource is in the host project, this is the host project ID. If the Cloud Run resource is in a service project, this is the service project ID.


  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Add or update the `run.googleapis.com/vpc-access-connector` attribute under the `annotations` attribute under the top-level `spec` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/vpc-access-connector: CONNECTOR_NAME
               name: REVISION

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * CONNECTOR_NAME: the name of your connector. Use the fully qualified name when deploying from a Shared VPC service project (as opposed to the host project), for example: 
           
           projects/HOST_PROJECT_ID/locations/CONNECTOR_REGION/connectors/CONNECTOR_NAME

where `HOST_PROJECT_ID` is the ID of the host project, `CONNECTOR_REGION` is the region of your connector, and `CONNECTOR_NAME` is the name that you gave your connector.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) to create a service and configure it to use your connector.
    
    
    # Cloud Run service
    resource "google_cloud_run_v2_service" "gcr_service" {
      name     = "mygcrservice"
      location = "us-west1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
          resources {
            limits = {
              cpu    = "1000m"
              memory = "512Mi"
            }
          }
          # the service uses this SA to call other Google Cloud APIs
          # service_account_name = myservice_runtime_sa
        }
    
        scaling {
          # Limit scale up to prevent any cost blow outs!
          max_instance_count = 5
        }
    
        vpc_access {
          # Use the VPC Connector
          connector = google_vpc_access_connector.connector.id
          # all egress from the service should go through the VPC Connector
          egress = "ALL_TRAFFIC"
        }
      }
    }

## Next steps

  * Monitor administrative activities with [Serverless VPC Access audit logging](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access-audit-logging).
  * Protect resources and data by [creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) with VPC Service Controls.
  * Use network tags to [restrict connector VM access to VPC resources](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#connector-to-resource).
  * Learn about the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles associated with Serverless VPC Access. See [Serverless VPC Access roles](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess) in the IAM documentation for a list of permissions associated with each role.
  * Learn how to [connect to Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
