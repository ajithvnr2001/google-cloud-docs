---
url: https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access/
title: Connect to a VPC network \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:47.142076+00:00
---

# Connect to a VPC network  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to a VPC network

We recommend using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) to send traffic to a VPC network—with no connector required.

However, if Direct VPC egress isn't an option for you, you can configure a [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) connector instead. This page shows you how to connect a Cloud Run service or job to your VPC network with a connector, allowing egress (outbound) traffic from Cloud Run to Compute Engine VM instances, Memorystore instances, and any other resources with an internal IP address.

## Before you begin

  * If you don't already have a VPC network in your project, [create one](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  * If you use Shared VPC, see the documentation that specifically covers configuration of Serverless VPC Access for your product.

    * **Cloud Run** : [Connecting to a Shared VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-shared-vpc)
    * **Cloud Run functions** : [Connecting to a Shared VPC network](https://docs.cloud.google.com/functions/docs/networking/connecting-shared-vpc)
    * **App Engine** : [Connecting to a Shared VPC network](https://docs.cloud.google.com/appengine/docs/standard/python3/connecting-shared-vpc)
  * If you have an organizational policy constraint that prevents the use of Cloud Deployment Manager, you won't be able to create or delete Serverless VPC Access connectors. Creating or deleting a connector requires Deployment Manager functionality.

  * If you have a [trusted image policy](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) set up for your project, make sure to allow the `serverless-vpc-access-images` project in the `constraints/compute.trustedimageProjects` organization policy.

### Connector subnet requirements

  * Each connector requires its own dedicated, `PRIVATE`-purpose subnet with a `/28` primary IPv4 address range. This subnet cannot be used by other resources, such as VMs, Private Service Connect, or load balancers. After creating the connector, the subnet cannot be expanded. It must stay as a `/28`.

  * To create a connector in a service project that uses a Shared VPC network in a host project, a network administrator for the Shared VPC network must manually create the connector's subnet before you can create the connector.

  * To determine if an existing, manually created subnet can be used by a connector, describe the subnet:
        
        gcloud compute networks subnets describe SUBNET --region=REGION

Replace SUBNET with the subnet's name and REGION with the region that contains the subnet.

In the output, verify the following:

    * The subnet is a regular subnet. In the Google Cloud CLI, this means that the value for [purpose](https://docs.cloud.google.com/vpc/docs/subnets#purpose) is `PRIVATE`.
    * The subnet's primary IPv4 address range, `ipCidrRange`, is a `/28`.
**Note:** Regular subnet is the default subnet type. Regular subnets have a purpose of `PRIVATE` in the gcloud or API. The purpose is `None` in the Google Cloud console.
  * If you need to create a Serverless VPC Access connector in the same project that contains the VPC network used by the connector, you can either manually create the connector's subnet before creating the connector, or Google Cloud can create the subnet for the connector automatically.

When Google Cloud creates a subnet for a connector, note the following:

    * Automatically created subnets for connectors aren't visible when you [list subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#listing_existing_subnets), regardless of whether you use the Google Cloud console, the Google Cloud CLI, or the Compute Engine API.

    * Automatically created subnets for connectors cannot be [described](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet).

    * Automatically created subnets are included in the list of subnets that is presented when you [describe a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#viewing-networks).




For more information about subnets, including how to list existing ones to determine which IP address ranges are already used, see [Work with subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).

## Limitations

  * IPv6 traffic is not supported.
  * Creating Serverless VPC Access connectors in the `asia-southeast3` region is not supported.
  * Creating Serverless VPC Access connectors fails in Assured Workloads environments. As a workaround, configure [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) for your serverless resources instead.



## Create a connector

To send requests to your VPC network and receive the corresponding responses without using the public internet, you can use a Serverless VPC Access connector.

If your connector is located in the same project as its VPC network, you can either create a connector using an existing subnet or create a connector and a new subnet.

If your connector is located in a service project and uses a Shared VPC network, the connector and its associated VPC network are in different projects. When a connector and its VPC network are in different projects, a Shared VPC network administrator must create the connector's subnet in the Shared VPC network _before_ you can create the connector, _and_ you must create the connector using an existing subnet.

To learn more about subnet requirements, see [connector subnet requirements](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#connector_subnet_requirements).

To learn about connector throughput, including machine type and scaling, see [Throughput and scaling](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#scaling).

You can create a connector by using the Google Cloud console, Google Cloud CLI, or Terraform.

###  Console 

  1. Go to the Serverless VPC Access overview page.

[Go to Serverless VPC Access](https://console.cloud.google.com/networking/connectors)

  2. Click **Create connector**.

  3. In the **Name** field, enter a name for your connector, matching Compute Engine [naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format), with the additional requirements that the name must be less than 21 characters long, and that hyphens (-) count as two characters.

  4. In the **Region** field, select a region for your connector. This must match the region of your serverless service.

  5. In the **Network** field, select the VPC network to attach your connector to.

  6. In the **Subnet** field, select one of the following options:

     * **Create a connector using an existing subnet:** Select the existing subnet in the _Subnet_ field.

     * **Create a connector and a new subnet:** Select **Custom IP range** in the _Subnet_ field. Then, enter the first address in an unused `/28` CIDR (for example `10.8.0.0/28`) to use as the primary IPv4 address range of a new subnet that Google Cloud creates in the connector's VPC network. Ensure that the IP range does not conflict with any existing routes in the connector's VPC network. The name of the new subnet begins with the "aet-" prefix.

  7. (Optional) To set scaling options for additional control over the connector, click **Show Scaling Settings** to display the scaling form.

     1. Set the minimum and maximum number of instances for your connector, or use the defaults, which are 2 (min) and 10 (max). The connector scales up to the maximum specified if traffic usage requires it. You must use values between `2` and `10`.
     2. In the **Instance Type** menu, choose the machine type to be used for the connector, or use the default `e2-micro`. Notice the cost sidebar on the right when you choose the instance type, which displays bandwidth and cost estimations.
  8. Click **Create**.

  9. A green check mark will appear next to the connector's name when it is ready to use.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Update `gcloud` components to the latest version:
         
         gcloud components update

  3. Ensure that the Serverless VPC Access API is enabled for your project:
         
         gcloud services enable vpcaccess.googleapis.com

  4. Create the connector using one of the following options:

For more details and optional arguments, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create).

     * **Create a connector using an existing subnet** :
           
           gcloud compute networks vpc-access connectors create CONNECTOR_NAME \
            --region REGION \
            --subnet SUBNET_NAME \
            --subnet-project HOST_PROJECT_ID \
            --min-instances MIN \
            --max-instances MAX \
            --machine-type MACHINE_TYPE

Replace the following:

       * `CONNECTOR_NAME`: a name for your connector, matching Compute Engine [naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format), with the additional requirements that the name must be less than 21 characters long, and that hyphens (-) count as two characters.
       * `REGION`: a region for your connector, matching the region of your serverless service or job.
       * `SUBNET_NAME`: the name of the existing subnet.
       * `HOST_PROJECT_ID`: the Shared VPC host project ID. If the connector and existing subnet are located the same project, omit the `--subnet-project` flag.
       * `MIN`: the minimum number of instances to use for the connector. Use an integer between `2`(the default) and `9`.
       * `MAX`: the maximum number of instances to use for the connector. Use an integer between `3` and `10` (the default).
       * `MACHINE_TYPE`: must be one of the following: `f1-micro`, `e2-micro`, or `e2-standard-4`.
     * **Create a connector and a new subnet** :
           
           gcloud compute networks vpc-access connectors create CONNECTOR_NAME \
            --region REGION \
            --network VPC_NETWORK \
            --range IP_RANGE
            --min-instances MIN \
            --max-instances MAX \
            --machine-type MACHINE_TYPE

Replace the following:

       * `CONNECTOR_NAME`: a name for your connector, matching Compute Engine [naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format), with the additional requirements that the name must be less than 21 characters long, and that hyphens (-) count as two characters.
       * `REGION`: a region for your connector, matching the region of your serverless service or job.
       * `VPC_NETWORK`: the name of the VPC network to attach your connector to. The connector and VPC network must be located in the same project.
       * `IP_RANGE`: provide an unused `/28` CIDR (for example `10.8.0.0/28`) to use as the primary IPv4 address range of a new subnet that Google Cloud creates in the connector's VPC network. Ensure that the IP range does not conflict with any existing routes in the connector's VPC network. The name of the new subnet begins with the "aet-" prefix.
       * `MIN`: the minimum number of instances to use for the connector. Use an integer between `2`(the default) and `9`.
       * `MAX`: the maximum number of instances to use for the connector. Use an integer between `3` and `10` (the default). If the connector scales up to the maximum number of instances, _it does not scale back down_.
       * `MACHINE_TYPE`: must be one of the following: `f1-micro`, `e2-micro`, or `e2-standard-4`.
  5. Verify that your connector is in the `READY` state before using it:
         
         gcloud compute networks vpc-access connectors describe CONNECTOR_NAME \
         --region REGION

Replace the following:

     * `CONNECTOR_NAME`: the name of your connector; this is the name that you specified in the previous step.
     * `REGION`: the region of your connector; this is the region that you specified in the previous step.

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

## Configure your serverless environment to use a connector

**Note:** Deploying a service with a connector requires the [Serverless VPC Access User](https://console.cloud.google.com/iam-admin/roles/details/roles%3Cvpcaccess.user) and [Compute Viewer](https://console.cloud.google.com/iam-admin/roles/details/roles%3Ccompute.viewer) IAM roles.

After you create a Serverless VPC Access connector, configure your serverless environment to use the connector by following the instructions for your serverless environment:

  * Configure Cloud Run
  * Configure Cloud Run functions
  * Configure App Engine



### Configure Cloud Run to use a connector

When you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision), you can configure the service to use a connector by using the Google Cloud console, Google Cloud CLI, a YAML file, or a Terraform resource.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Connections** tab.

  4. In the **VPC Connector** field, select a connector to use or select **None** to disconnect your service from a VPC network.

  5. Click **Create** or **Deploy**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To specify a connector during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy), use the [`--vpc-connector`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-connector) flag:
         
         gcloud run deploy SERVICE --image IMAGE_URL --vpc-connector CONNECTOR_NAME

     * Replace `SERVICE` with the name of your service.
     * Replace `IMAGE_URL`.
     * Replace `CONNECTOR_NAME` with the name of your connector. If your connector is in the host project of a Shared VPC, this must be the fully specified name, for example: 
           
           projects/HOST_PROJECT_ID/locations/CONNECTOR_REGION/connectors/CONNECTOR_NAME

where HOST_PROJECT_ID is the ID of the host project, CONNECTOR_REGION is the region of your connector, and CONNECTOR_NAME is the name that you gave your connector.

To attach, update, or remove a connector for an existing service, use the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with either of the following flags as needed:

     * [`--vpc-connector`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--vpc-connector)
     * [`--clear-vpc-connector`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--clear-vpc-connector)

For example to attach or update a connector:
    
    gcloud run services update SERVICE --vpc-connector CONNECTOR_NAME

     * Replace `SERVICE` with the name of your service.
     * Replace `CONNECTOR_NAME` with the name of your connector.



### YAML

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

     * Replace `SERVICE` with the name of your Cloud Run service.
     * Replace `CONNECTOR_NAME` with the name of your connector. If your connector is in the host project of a Shared VPC, this must be the fully specified name, for example: 
           
           projects/HOST_PROJECT_ID/locations/CONNECTOR_REGION/connectors/CONNECTOR_NAME

where HOST_PROJECT_ID is the ID of the host project, CONNECTOR_REGION is the region of your connector, and CONNECTOR_NAME is the name that you gave your connector.
  3. Replace the service with its new configuration using the following command:
         
         gcloud beta run services replace service.yaml




###  Terraform 

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_service) to create a service and configure it to use your connector.
    
    
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

### Configure Cloud Run functions to use a connector

You can configure a function to use a connector from the Google Cloud console or the Google Cloud CLI:

###  Console 

  1. Go to the Cloud Run functions overview page in the Google Cloud console:

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

  2. Click **Create function**. Alternatively, click an existing function to go to its details page, and click **Edit**.

  3. Expand the advanced settings by clicking **RUNTIME, BUILD AND CONNECTIONS SETTINGS**.

  4. In the **Connections** tab under Egress settings, enter the name of your connector in the **VPC connector** field.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the `gcloud functions deploy` command to deploy the function and specify the [`--vpc-connector`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--vpc-connector) flag:
         
         gcloud functions deploy FUNCTION_NAME \
         --vpc-connector CONNECTOR_NAME \
         FLAGS...
         

where:

     * `FUNCTION_NAME` is the name of your function.
     * `CONNECTOR_NAME` is the name of your connector. If your connector is in the host project of a Shared VPC, this must be the fully specified name, for example: 
           
           projects/HOST_PROJECT_ID/locations/CONNECTOR_REGION/connectors/CONNECTOR_NAME

where HOST_PROJECT_ID is the ID of the host project, CONNECTOR_REGION is the region of your connector, and CONNECTOR_NAME is the name that you gave your connector.
     * `FLAGS...` refers to other flags you pass during [function deployment](https://docs.cloud.google.com/functions/docs/deploying/filesystem).



For more control over which requests are routed through the connector, see [Egress settings](https://docs.cloud.google.com/functions/docs/networking/network-settings#egress_settings).

**Note:** Administrators can require that functions specify a Serverless VPC Access connector by setting the [`cloudfunctions.requireVPCConnector`](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints#legacy_managed_constraints_2) organization policy.

### Configure App Engine to use a connector

### Python 2

  1. Discontinue use of the App Engine URL Fetch service.

By default, all requests are routed through URL Fetch service. This causes requests to your VPC network to fail. To disable this default, see [Disabling URL Fetch from handling all outbound requests](https://docs.cloud.google.com/appengine/docs/standard/python/sockets#making_httplib_use_sockets).

You can still use the [`urlfetch` library](https://docs.cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.api.urlfetch) directly for individual requests if needed, however this is not recommended.

  2. Add the Serverless VPC Access field to your `app.yaml` file:
         
         vpc_access_connector:
          name: projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME
         

Replace the following:

     * `PROJECT_ID` with your Google Cloud project ID. If your connector is in the host project of a Shared VPC, this must be the ID of the host project.
     * `REGION` with the region that your connector is in.
     * `CONNECTOR_NAME` with the name of your connector.
  3. Deploy the service:
         
         gcloud app deploy

After you deploy your service, it is able to send requests to internal IP addresses in order to access resources in your VPC network.




### Java 8

  1. Discontinue use of the App Engine URL Fetch service `URLFetchService`.

  2. Add the Serverless VPC Access element to your service's `appengine-web.xml` file:
         
         <vpc-access-connector>
         <name>projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME</name>
         </vpc-access-connector>
         

Replace the following:

     * `PROJECT_ID` with your Google Cloud project ID. If your connector is in the host project of a Shared VPC, this must be the ID of the host project.
     * `REGION` with the region that your connector is in.
     * `CONNECTOR_NAME` with the name of your connector.
  3. Deploy the service:
         
         gcloud app deploy WEB-INF/appengine-web.xml

After you deploy your service, it is able to send requests to internal IP addresses in order to access resources in your VPC network.




### Go 1.11

  1. Discontinue use of the App Engine URL Fetch service.

Serverless VPC Access does not support URL Fetch, and requests made using URL Fetch will ignore Serverless VPC Access settings. Make outbound connections with [sockets](https://docs.cloud.google.com/appengine/docs/standard/go111/sockets) instead.

  2. Add the Serverless VPC Access field to your `app.yaml` file:
         
         vpc_access_connector:
          name: projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME
         

Replace the following:

     * `PROJECT_ID` with your Google Cloud project ID
     * `REGION` with the region that your connector is in
     * `CONNECTOR_NAME` with the name of your connector
  3. Deploy the service:
         
         gcloud app deploy

After you deploy your service, it is able to send requests to internal IP addresses in order to access resources in your VPC network.




### All other runtimes

  1. Add the Serverless VPC Access field to your `app.yaml` file:
         
         vpc_access_connector:
          name: projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME
         

Replace the following:

     * `PROJECT_ID` with your Google Cloud project ID. If your connector is in the host project of a Shared VPC, this must be the ID of the host project.
     * `REGION` with the region that your connector is in.
     * `CONNECTOR_NAME` with the name of your connector.
  2. Deploy the service:
         
         gcloud app deploy

After you deploy your service, it is able to send requests to internal IP addresses in order to access resources in your VPC network.




## Configure firewall rules for connectors

### Required firewall rules for connectors in service projects

If you create a connector in a standalone VPC network or in the host project of a Shared VPC network, Google Cloud creates all necessary firewall rules for the connector's operation. For more information, see [Firewall rules for connectors in standalone VPC networks or Shared VPC host projects](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#connector-fw-rules-standalone-vpc-or-host-prj).

However, if you create a connector in a service project and the connector targets a Shared VPC network in the host project, you must add firewall rules to allow necessary traffic for the connector's operation from the following ranges:

  * [Serverless infrastructure IP range](https://docs.cloud.google.com/vpc/docs/routes#serverless-vpc-return-path): `35.199.224.0/19`
  * [Health check probe IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges): `35.191.0.0/16`, `35.191.192.0/18`, and `130.211.0.0/22`



These ranges are used by the Google infrastructure underlying Cloud Run, Cloud Run functions, and App Engine standard environment. All requests from these IP addresses originate from Google infrastructure to make sure that each serverless resource only communicates with the connector that it's connected to.

You must also allow traffic from the connector's subnet to resources in your VPC network.

To perform these steps, you must have one of the following roles on the host project:

  * [Owner role](https://docs.cloud.google.com/compute/docs/access#basic-iam-roles) (`roles/owner`)
  * [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`)
  * Custom [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) role with the [`compute.firewalls.create` permission](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert#iam-permissions) enabled



For a basic configuration, apply the rules to allow serverless resources in any service project connected to the Shared VPC network to send requests to any resource in the network.

**Important:** The rules you create using the following process apply to existing and future connectors that target a given Shared VPC network. If you want to scope these rules so they only apply to specified connectors, see Create firewall rules for specific connectors.

To apply these rules, run the following commands in the host project:

  1. Create firewall rules that allow requests from Google's serverless infrastructure and health check probes to reach all connectors in the network. In these commands, UDP and TCP ports are used as proxies and for HTTP health checks, respectively. Don't change the specified ports.
         
         gcloud compute firewall-rules create serverless-to-vpc-connector \
             --allow tcp:667,udp:665-666,icmp \
             --source-ranges=35.199.224.0/19 \
             --direction=INGRESS \
             --target-tags vpc-connector \
             --network=VPC_NETWORK
         
         gcloud compute firewall-rules create vpc-connector-to-serverless \
             --allow tcp:667,udp:665-666,icmp \
             --destination-ranges=35.199.224.0/19 \
             --direction=EGRESS \
             --target-tags vpc-connector \
             --network=VPC_NETWORK
         
         gcloud compute firewall-rules create vpc-connector-health-checks \
             --allow tcp:667 \
             --source-ranges=35.191.0.0/16,35.191.192.0/18,130.211.0.0/22 \
             --direction=INGRESS \
             --target-tags vpc-connector \
             --network=VPC_NETWORK

Replace `VPC_NETWORK` with the name of the VPC network to attach your connector to.

  2. Create an ingress firewall rule on your VPC network to allow requests from connectors that target this network:
         
         gcloud compute firewall-rules create vpc-connector-requests \
             --allow tcp,udp,icmp \
             --direction=INGRESS \
             --source-tags vpc-connector \
             --network=VPC_NETWORK

This rule gives the connector access to every resource in the network. To limit the resources that your serverless environment can reach by using Serverless VPC Access, see Restrict connector VM access to VPC network resources.




#### Create firewall rules for specific connectors

Following the procedure in Required firewall rules for connectors in service projects results in firewall rules that apply to _all_ connectors, both current ones and ones created in the future. If you don't want this, but instead want to create rules for specific connectors only, you can scope the rules so that they apply only to those connectors.

To limit the scope of the rules to specific connectors, you can use one of the following mechanisms:

  * Network tags: Every connector has two network tags: `vpc-connector` and `vpc-connector-REGION-CONNECTOR_NAME`. Use the latter format to limit the scope of your firewall rules to a specific connector.
  * IP ranges: Use this for the egress rules only, because it doesn't work for ingress rules. You can use the IP range of the connector subnet to limit the scope of your firewall rules to a single VPC connector.



### Restrict connector VM access to VPC network resources

You can restrict your connector's access to resources in its target VPC network by using [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) or rules in [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview). You can accomplish these restrictions using one of the following strategies:

  * Create ingress rules whose targets represent the resources that you want to limit connector VM access to and whose sources represent the connector VMs.
  * Create egress rules whose targets represent the connector VMs and whose destinations represent the resources that you want to limit connector VM access to.



The following examples illustrate each strategy.

#### Restrict access using ingress rules

Choose either [network tags](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#network-tags) or CIDR ranges to control the incoming traffic to your VPC network.

###  Network tags 

The following steps show how to create ingress rules that restrict a connector's access to your VPC network based on the connector network tags.

  1. Ensure that you have the required permissions to insert firewall rules. You must have one of the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles:

     * [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)
     * Custom IAM role with the [`compute.firewalls.create`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert#iam-permissions) permission enabled
  2. Deny connector traffic across your VPC network.

Create an ingress firewall rule with priority lower than 1000 on your VPC network to deny ingress from the connector network tag. This overrides the implicit firewall rule that Serverless VPC Access creates on your VPC network by default.
         
         gcloud compute firewall-rules create RULE_NAME \
         --action=DENY \
         --rules=PROTOCOL \
         --source-tags=VPC_CONNECTOR_NETWORK_TAG \
         --direction=INGRESS \
         --network=VPC_NETWORK \
         --priority=PRIORITY

Replace the following:

     * RULE_NAME: the name of your new firewall rule. For example, `deny-vpc-connector`.

     * PROTOCOL: one or more protocols that you want to allow from your VPC connector. Supported protocols are `tcp` or `udp`. For example, `tcp:80,udp` allows TCP traffic through port 80 and UDP traffic. For more information, see the documentation for the [`allow`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--allow) flag. 

For security and validation purposes, you can also configure deny rules to block traffic for the following unsupported [protocols](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml): `ah`, `all`, `esp`, `icmp`, `ipip`, and `sctp`. 

     * VPC_CONNECTOR_NETWORK_TAG: the universal connector network tag if you want to restrict access for all connectors (including any connectors made in the future), or the unique network tag if you want to restrict access for a specific connector.

       * **Universal network tag:** `vpc-connector`
       * **Unique network tag:** `vpc-connector-REGION-CONNECTOR_NAME`

Replace:

         * REGION: the region of the connector that you want to restrict
         * CONNECTOR_NAME: the name of the connector that you want to restrict

To learn more about connector network tags, see [Network tags](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#network-tags).

     * VPC_NETWORK: the name of your VPC network

     * PRIORITY: an integer between 0-65535. For example, 0 sets the highest priority.

  3. Allow connector traffic to the resource that should receive connector traffic.

Use the `allow` and `target-tags` flags to create an ingress firewall rule targeting the resource in your VPC network that you want the VPC connector to access. Set the priority for this rule to be a lower value than the priority of the rule you made in the previous step.
         
         gcloud compute firewall-rules create RULE_NAME \
         --allow=PROTOCOL \
         --source-tags=VPC_CONNECTOR_NETWORK_TAG \
         --direction=INGRESS \
         --network=VPC_NETWORK \
         --target-tags=RESOURCE_TAG \
         --priority=PRIORITY

Replace the following:

     * RULE_NAME: the name of your new firewall rule. For example, `allow-vpc-connector-for-select-resources`.

     * PROTOCOL: one or more protocols that you want to allow from your VPC connector. Supported protocols are `tcp` or `udp`. For example, `tcp:80,udp` allows TCP traffic through port 80 and UDP traffic. For more information, see the documentation for the [`allow`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--allow) flag. 

     * VPC_CONNECTOR_NETWORK_TAG: the universal connector network tag if you want to restrict access for all connectors (including any connectors made in the future), or the unique network tag if you want to restrict access for a specific connector. This must match the network tag that you specified in the previous step.

       * **Universal network tag:** `vpc-connector`
       * **Unique network tag:** `vpc-connector-REGION-CONNECTOR_NAME`

Replace:

         * REGION: the region of the connector that you want to restrict
         * CONNECTOR_NAME: the name of the connector that you want to restrict

To learn more about connector network tags, see [Network tags](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#network-tags).

     * VPC_NETWORK: the name of your VPC network

     * RESOURCE_TAG: the network tag for the VPC resource that you want your VPC connector to access

     * PRIORITY: an integer less than the priority you set in the previous step. For example, if you set the priority for the rule you created in the previous step to 990, try 980.




For more information about the required and optional flags for creating firewall rules, refer to the [documentation for `gcloud compute firewall-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).

###  CIDR range 

The following steps show how to create ingress rules that restrict a connector's access to your VPC network based on the connector's CIDR range.

  1. Ensure that you have the required permissions to insert firewall rules. You must have one of the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles:

     * [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)
     * Custom IAM role with the [`compute.firewalls.create`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert#iam-permissions) permission enabled
  2. Deny connector traffic across your VPC network.

Create an ingress firewall rule with priority lower than 1000 on your VPC network to deny ingress from the connector's CIDR range. This overrides the implicit firewall rule that Serverless VPC Access creates on your VPC network by default.
         
         gcloud compute firewall-rules create RULE_NAME \
         --action=DENY \
         --rules=PROTOCOL \
         --source-ranges=VPC_CONNECTOR_CIDR_RANGE \
         --direction=INGRESS \
         --network=VPC_NETWORK \
         --priority=PRIORITY

Replace the following:

     * RULE_NAME: the name of your new firewall rule. For example, `deny-vpc-connector`.

     * PROTOCOL: one or more protocols that you want to allow from your VPC connector. Supported protocols are `tcp` or `udp`. For example, `tcp:80,udp` allows TCP traffic through port 80 and UDP traffic. For more information, see the documentation for the [`allow`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--allow) flag. 

For security and validation purposes, you can also configure deny rules to block traffic for the following unsupported [protocols](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml): `ah`, `all`, `esp`, `icmp`, `ipip`, and `sctp`. 

     * VPC_CONNECTOR_CIDR_RANGE: the CIDR range for the connector whose access you are restricting

     * VPC_NETWORK: the name of your VPC network

     * PRIORITY: an integer between 0-65535. For example, 0 sets the highest priority.

  3. Allow connector traffic to the resource that should receive connector traffic.

Use the `allow` and `target-tags` flags to create an ingress firewall rule targeting the resource in your VPC network that you want the VPC connector to access. Set the priority for this rule to be a lower value than the priority of the rule you made in the previous step.
         
         gcloud compute firewall-rules create RULE_NAME \
         --allow=PROTOCOL \
         --source-ranges=VPC_CONNECTOR_CIDR_RANGE \
         --direction=INGRESS \
         --network=VPC_NETWORK \
         --target-tags=RESOURCE_TAG \
         --priority=PRIORITY

Replace the following:

     * RULE_NAME: the name of your new firewall rule. For example, `allow-vpc-connector-for-select-resources`.

     * PROTOCOL: one or more protocols that you want to allow from your VPC connector. Supported protocols are `tcp` or `udp`. For example, `tcp:80,udp` allows TCP traffic through port 80 and UDP traffic. For more information, see the documentation for the [`allow`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--allow) flag. 

     * VPC_CONNECTOR_CIDR_RANGE: the CIDR range for the connector you whose access you are restricting

     * VPC_NETWORK: the name of your VPC network

     * RESOURCE_TAG: the network tag for the VPC resource that you want your VPC connector to access

     * PRIORITY: an integer less than the priority you set in the previous step. For example, if you set the priority for the rule you created in the previous step to 990, try 980.




For more information about the required and optional flags for creating firewall rules, see the [documentation for `gcloud compute firewall-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).

#### Restrict access using egress rules

The following steps show how to create egress rules to restrict connector access.

  1. Ensure that you have the required permissions to insert firewall rules. You must have one of the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles:

     * [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)
     * Custom IAM role with the [`compute.firewalls.create`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert#iam-permissions) permission enabled
  2. Deny egress traffic from your connector.

Create an egress firewall rule on your Serverless VPC Access connector to prevent it from sending outgoing traffic, with the exception of established responses, to any destination.
         
         gcloud compute firewall-rules create RULE_NAME \
         --action=DENY \
         --rules=PROTOCOL \
         --direction=EGRESS \
         --target-tags=VPC_CONNECTOR_NETWORK_TAG \
         --network=VPC_NETWORK \
         --priority=PRIORITY

Replace the following:

     * RULE_NAME: the name of your new firewall rule. For example, `deny-vpc-connector`.

     * PROTOCOL: one or more protocols that you want to allow from your VPC connector. Supported protocols are `tcp` or `udp`. For example, `tcp:80,udp` allows TCP traffic through port 80 and UDP traffic. For more information, see the documentation for the [`allow`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--allow) flag. 

For security and validation purposes, you can also configure deny rules to block traffic for the following unsupported [protocols](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml): `ah`, `all`, `esp`, `icmp`, `ipip`, and `sctp`. 

     * VPC_CONNECTOR_NETWORK_TAG: the universal VPC connector network tag if you want the rule to apply to all existing VPC connectors and any VPC connectors made in the future. Or, the unique VPC connector network tag if you want to control a specific connector.

     * VPC_NETWORK: the name of your VPC network

     * PRIORITY: an integer between 0-65535. For example, 0 sets the highest priority.

  3. Allow egress traffic when the destination is in the CIDR range that you want your connector to access.

Use the `allow` and `destination-ranges` flags to create a firewall rule allowing egress traffic from your connector for a specific destination range. Set the destination range to the CIDR range of the resource in your VPC network that you want your connector to be able to access. Set the priority for this rule to be a lower value than the priority of the rule you made in the previous step.
         
         gcloud compute firewall-rules create RULE_NAME \
         --allow=PROTOCOL \
         --destination-ranges=RESOURCE_CIDR_RANGE \
         --direction=EGRESS \
         --network=VPC_NETWORK \
         --target-tags=VPC_CONNECTOR_NETWORK_TAG \
         --priority=PRIORITY

Replace the following:

     * RULE_NAME: the name of your new firewall rule. For example, `allow-vpc-connector-for-select-resources`.

     * PROTOCOL: one or more protocols that you want to allow from your VPC connector. Supported protocols are `tcp` or `udp`. For example, `tcp:80,udp` allows TCP traffic through port 80 and UDP traffic. For more information, see the documentation for the [`allow`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create#--allow) flag. 

     * RESOURCE_CIDR_RANGE: the CIDR range for the connector whose access you are restricting

     * VPC_NETWORK: the name of your VPC network

     * VPC_CONNECTOR_NETWORK_TAG: the universal VPC connector network tag if you want the rule to apply to all existing VPC connectors and any VPC connectors made in the future. Or, the unique VPC connector network tag if you want to control a specific connector. If you used the unique network tag in the previous step, use the unique network tag.

     * PRIORITY: an integer less than the priority you set in the previous step. For example, if you set the priority for the rule you created in the previous step to 990, try 980.




For more information about the required and optional flags for creating firewall rules, refer to the [documentation for `gcloud compute firewall-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).

## Update a connector

You can update and monitor the following attributes of your connector by using the Google Cloud console, Google Cloud CLI, or the API:

  * Machine (instance) type
  * Minimum and maximum number of instances
  * Recent throughput, number of instances, and CPU utilization



#### Update machine type

**Caution:** Changing machine type can cause some long-running connections to drop.

###  Console 

  1. Go to the Serverless VPC Access overview page.

[Go to Serverless VPC Access](https://console.cloud.google.com/networking/connectors)

  2. Select the connector you want to edit and click **Edit**.

  3. In the **Instance type** list, select your preferred machine (instance) type. To learn about available machine types, see the documentation on [Throughput and scaling](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#scaling).




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To update the connector machine type, run the following command in your terminal: 
         
         gcloud beta compute networks vpc-access connectors update CONNECTOR_NAME --region=REGION --machine-type=MACHINE_TYPE

Replace the following: 
     * `CONNECTOR_NAME`: the name of your connector
     * `REGION`: the name of your connector's region
     * `MACHINE_TYPE`: your preferred machine type. To learn about available machine types, see the documentation on [Throughput and scaling](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#scaling).



#### Decrease minimum and maximum number of instances

**Note:** Decreasing the number of instances for existing connectors is not supported.

To decrease the number of minimum and maximum number of instances, you must do the following:

  1. Create a new connector with your preferred values.
  2. Update your service or function to use the new connector.
  3. Delete the old connector when you've moved its traffic.



#### Increase minimum and maximum number of instances

###  Console 

  1. Go to the Serverless VPC Access overview page.

[Go to Serverless VPC Access](https://console.cloud.google.com/networking/connectors)

  2. Select the connector you want to edit and click **Edit**.

  3. In the **Minimum instances** field, select your preferred minimum number of instances.

The smallest possible value for this field is the current value. The largest possible value for this field is the current value in the **Maximum instances** field minus 1. For example, if the value in the **Maximum instances** field is 8, then the largest possible value for the **Minimum instances** field is 7.

  4. In the **Maximum instances** field, select your preferred maximum number of instances.

The smallest possible value for this field is the current value. The largest possible value for this field is 10.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To increase the minimum or maximum number of instances for the connector, run the following command in your terminal: 
         
         gcloud beta compute networks vpc-access connectors update CONNECTOR_NAME --region=REGION --min-instances=MIN_INSTANCES --max-instances=MAX_INSTANCES

Replace the following:


  * `CONNECTOR_NAME`: the name of your connector
  * `REGION`: the name of your connector's region
  * `MIN_INSTANCES`: your preferred minimum number of instances. 
    * Smallest possible value for this field is the current value of `min_instances`. To find the current value, see Find the current attribute values.
    * Largest possible value for this field is the current `max_instances` value minus 1, because `min_instances` must be less than `max_instances`. For example, if `max_instances` is 8, the largest possible value for this field is 7. If your connector uses the default `max-instances` value of 10, the largest possible value of this field is 9. To find the value of `max-instances`, see Find the current attribute values.
  * `MAX_INSTANCES`:

    * Smallest possible value for this field is the current value of `max_instances`. To find the current value, see Find the current attribute values.
    * Largest possible value for this field is 10.

If you only want to increase the minimum number of instances but not the maximum, you must still specify the maximum number of instances. Conversely, if you only want to update the maximum number of instances but not the minimum, you must still specify the minimum number of instances. To keep either the minimum or maximum number of instances at their current value, specify their current value. To find their current value, see Find the current attribute values.




#### Find the current attribute values

To find the current attribute values for your connector, run the following in your terminal: 
    
    
    gcloud compute networks vpc-access connectors describe CONNECTOR_NAME --region=REGION --project=PROJECT

Replace the following: 

  * `CONNECTOR_NAME`: the name of your connector
  * `REGION`: the name of your connector's region
  * `PROJECT`: the name of your Google Cloud project



#### Monitor connector usage

Monitoring usage over time can help you determine when to adjust a connector's settings. For example, if CPU utilization spikes, you might try increasing the maximum number of instances for better results. Or if you are maxing out throughput, you might decide to switch to a larger machine type.

To display charts for the connector's throughput, number of instances, and CPU utilization metrics over time by using the Google Cloud console:

  1. Go to the Serverless VPC Access overview page.

[Go to Serverless VPC Access](https://console.cloud.google.com/networking/connectors)

  2. Click the name of the connector you want to monitor.

  3. Select the number of days you want to display between 1 and 90 days.

  4. In the **Throughput** chart, hold the pointer over the chart to view the connector's recent throughput.

  5. In the **Number of instances** chart, hold the pointer over the chart to view the number of instances recently used by the connector.

  6. In the **CPU Utilization** chart, hold the pointer over the chart to view the connector's recent CPU usage. The chart displays the CPU usage distributed across instances for the 50th, 95th, and 99th percentiles.




## Delete a connector

Before you delete a connector, you must remove it from any serverless resources that still use it. Deleting a connector before removing it from your serverless resources prohibits you from deleting the VPC network later.

**Caution:** Deleting a connector does not trigger any warnings or alerts indicating that active resources are using the connector. After a connector is deleted, it cannot be restored. To restore connectivity, you must manually recreate the VPC connector with the original parameters.

For Shared VPC users who set up connectors in the Shared VPC host project, you can use the command [`gcloud compute networks vpc-access connectors describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/describe) to list the projects in which there are serverless resources that use a given connector.

To delete a connector, use the Google Cloud console or the Google Cloud CLI:

###  Console 

  1. Go to the Serverless VPC Access overview page in the Google Cloud console:

[Go to Serverless VPC Access](https://console.cloud.google.com/networking/connectors)

  2. Select the connector you want to delete.

  3. Click **Delete**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the following `gcloud` command to delete a connector:
         
         gcloud compute networks vpc-access connectors delete CONNECTOR_NAME --region=REGION
         

Replace the following:

     * CONNECTOR_NAME with the name of the connector you want to delete
     * REGION with the region where the connector is located



## Manage custom constraints for projects

This section describes how to create custom constraints for Serverless VPC Access connectors and enforce them at the project level. For information about custom organization policies, see [Creating and managing custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints).

Google Cloud Organization Policy gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides [predefined constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create custom organization policies.

#### Benefits

Serverless VPC Access lets you write any number of custom constraints using most user-configured fields in the Serverless VPC Access API. For example, you can create a custom constraint specifying which subnets a Serverless VPC Access connector can use.

Once applied, requests that violate a policy that enforces a custom constraint show an error message in the gcloud CLI and in Serverless VPC Access logs. The error message contains the constraint ID and description of the violated custom constraint.

**Note:** Use the [policy simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies) to check whether existing connectors in your organization are in violation of a new custom organization policy.

#### Policy inheritance

By default, organization policies are inherited by the descendants of the resources that you enforce the policy on. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#disallow_inheritance).

#### Limitations

Specifying machine type, minimum instances, or maximum instances is not supported.

#### Before you begin

Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

##### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Create a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service that you are enforcing the organization policy on. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language).

To create a YAML file for a Serverless VPC Access custom constraint, refer to the following example:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - vpcaccess.googleapis.com/Connector
    methodTypes:
    - CREATE
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers, for example, custom.defaultNetworkConstraint. The maximum length of this field is 70 characters, not counting the prefix.

  * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field has a maximum length of 1000 characters. For example, `"resource.network == default"`.

  * `ACTION`: the action to take if the `condition` is met. This can be either `ALLOW` or `DENY`.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated, for example, `"Require network to not be set to default."` This field has a maximum length of 2000 characters.




For more information about how to create a custom constraint, see [Defining custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#defining_custom_constraints).

#### Set up a custom constraint

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.defaultNetworkConstraint`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. This constraint can only be enforced on the REST `CREATE` method. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.defaultNetworkConstraint`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `vpcaccess.googleapis.com/Connector`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.network == default"`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Can only be `ALLOW`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




#### Enforce a custom constraint

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.defaultNetworkConstraint`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




#### Test the custom constraint

To test the example that restricts ingress settings, deploy a connector in the project with network set to `default`:
    
    
    gcloud compute networks vpc-access connectors create org-policy-test \
        --project=PROJECT_ID \
        --region=REGION_ID \
        --network=default
    

The output is the following:
    
    
    Operation denied by custom org policies: ["customConstraints/custom.defaultNetworkConstraint": "Require network to not be set to default."]
    

#### Example custom organization policies for common use cases

The following table provides examples of custom constraints that you might find useful with Serverless VPC Access connectors:

Description | Constraint syntax  
---|---  
Require that Serverless VPC Access connectors can only use a specific network. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.allowlistNetworks
        resourceTypes:
        - vpcaccess.googleapis.com/Connector
        methodTypes:
        - CREATE
        condition: "resource.network == 'allowlisted-network'"
        actionType: ALLOW
        displayName: allowlistNetworks
        description: Require connectors to use a specific network.  
  
Description | Constraint syntax  
Require that Serverless VPC Access connectors have access to only a specific subnet. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictSubnetForProject
        resourceTypes:
        - vpcaccess.googleapis.com/Connector
        methodTypes:
        - CREATE
        condition: "resource.subnet.name == 'allocated-subnet'"
        actionType: ALLOW
        displayName: restrictSubnetForProject
        description: This project is only allowed to use the subnet "allocated-subnet".  
  
## Configure your Cloud Run environment to use Direct VPC instead of a connector

You can enable your Cloud Run [service](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#configuring) to send egress (outbound) traffic directly to a VPC network, allowing access to Compute Engine VM instances, Memorystore instances, and any other resources with an internal IP address.

### Configure your service to use Direct VPC

Direct VPC egress allows your Cloud Run service to send traffic to a VPC network without a Serverless VPC Access connector. Network costs scale to zero just like the service itself. You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run service revisions for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC egress with a service by using the Google Cloud console, Google Cloud CLI, YAML, or Terraform.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring and deploying an existing service, click the service.

  3. If you are configuring a new service, fill out the initial service settings page as needed, then click **Containers, Networking, Security** to expand the service configuration page.

  4. Click the **Networking** tab.

  5. Click **Connect to a VPC for outbound traffic**.

  6. Click **Send traffic directly to a VPC**.

  7. In the **Network** field, select the VPC network that you want to send traffic to.

  8. In the **Subnet** field, select the subnet where your service receives IP addresses from. You can deploy multiple services on the same subnet.

  9. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  10. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the VPC network.
  11. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.

  12. To verify that your service is on your VPC network, click the service, then click the **Networking** tab. The network and subnet are listed in the **VPC** card.

You can now send requests from your Cloud Run service to any resource on the VPC network, as allowed by your firewall rules.




### gcloud

### Service

To deploy a Cloud Run service without a connector from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Deploy your Cloud Run service with the following command:
         
         gcloud run deploy SERVICE_NAME \
             --image=IMAGE_URL \
             --network=NETWORK \
             --subnet=SUBNET \
             --network-tags=NETWORK_TAG_NAMES \
             --vpc-egress=EGRESS_SETTING \
             --region=REGION

Replace:

     * SERVICE_NAME with the name of your Cloud Run service.
     * `IMAGE_URLus-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. The subnet must be `/26` or larger. Direct VPC egress supports IPv4 ranges [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3), [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7), and Class E. You can deploy or execute multiple services or jobs on the same subnet, but the subnet cannot be shared by any existing connectors. 
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * REGION with a region for your service.
  4. To verify that your service is on your VPC network, run the following command:
         
         gcloud run services describe SERVICE_NAME \
             --region=REGION

Replace:

     * `SERVICE_NAME` with the name of your service.
     * `REGION` with the region for your service that you specified in the previous step.

The output should contain the name of your network, subnet, and egress setting, for example:
    
    VPC access:
      Network:       default
      Subnet:        subnet
      Egress:        private-ranges-only
    




You can now send requests from your Cloud Run service to any resource on the VPC network, as allowed by your firewall rules.

### Function

To deploy a Cloud Run function without a connector from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Deploy your Cloud Run function with the following command:
         
         gcloud run deploy FUNCTION_NAME \
             --image=IMAGE_URL \
             --network=NETWORK \
             --subnet=SUBNET \
             --network-tags=NETWORK_TAG_NAMES \
             --vpc-egress=EGRESS_SETTING \
             --region=REGION \
             --function=FUNCTION_ENTRYPOINT

Replace:

     * FUNCTION_NAME with the name of your Cloud Run function.
     * `IMAGE_URLus-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. The subnet must be `/26` or larger. Direct VPC egress supports IPv4 ranges [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3), [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7), and Class E. You can deploy or execute multiple services or jobs on the same subnet, but the subnet cannot be shared by any existing connectors. 
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a function. For functions, network tags are specified at the revision-level. Each revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * REGION with a region for your function.
     * Optional: FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully qualified class name that exists in your source code.
  4. To verify that your function is on your VPC network, run the following command:
         
         gcloud run services describe FUNCTION_NAME \
             --region=REGION

Replace:

     * `FUNCTION_NAME` with the name of your function.
     * `REGION` with the region for your function that you specified in the previous step.

The output should contain the name of your network, subnet, and egress setting, for example:
    
    VPC access:
      Network:       default
      Subnet:        subnet
      Egress:        private-ranges-only
    




You can now send requests from your Cloud Run function to any resource on the VPC network, as allowed by your firewall rules.

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the following attributes:
         
         apiVersion: serving.knative.dev/v1
           kind: Service
           metadata:
             name: SERVICE_NAME
             labels:
               cloud.googleapis.com/location: REGION
           spec:
             template:
               metadata:
                 annotations:
                   run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'
                   run.googleapis.com/vpc-access-egress: EGRESS_SETTING
               spec:
                 containers:
                 - image: IMAGE

Replace:

     * SERVICE_NAME with the name of your Cloud Run service. Service names must be 49 characters or less and must be unique per region and project.
     * REGION with the region for your Cloud Run service, which must match the region of your subnet.
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. The subnet must be `/26` or larger. Direct VPC egress supports IPv4 ranges [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3), [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7), and Class E. You can deploy or execute multiple services or jobs on the same subnet, but the subnet cannot be shared by any existing connectors. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * IMAGE with the URL of your service container image.

You can also [specify more configuration](https://docs.cloud.google.com/run/docs/how-to#configure), such as environment variables or memory limits.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Add the following to your `main.tf` file:
         
         /**
          * Copyright 2024 Google LLC
          *
          * Licensed under the Apache License, Version 2.0 (the "License");
          * you may not use this file except in compliance with the License.
          * You may obtain a copy of the License at
          *
          *      http://www.apache.org/licenses/LICENSE-2.0
          *
          * Unless required by applicable law or agreed to in writing, software
          * distributed under the License is distributed on an "AS IS" BASIS,
          * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
          * See the License for the specific language governing permissions and
          * limitations under the License.
          */
         
         # Example configuration of a Cloud Run service with direct VPC
         
         resource "google_cloud_run_v2_service" "default" {
           name     = "cloudrun-service"
           location = "us-central1"
         
           deletion_protection = false # set to "true" in production
         
           template {
             containers {
               image = "us-docker.pkg.dev/cloudrun/container/hello"
             }
             vpc_access {
               network_interfaces {
                 network    = "default"
                 subnetwork = "default"
                 tags       = ["tag1", "tag2", "tag3"]
               }
             }
           }
         }
         




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

Optionally, [make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.

### Configure your job to use Direct VPC

Direct VPC egress allows your Cloud Run job to send traffic to a VPC network without a Serverless VPC Access connector. You can also [add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) directly on Cloud Run jobs for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

You can configure Direct VPC egress with a job by using the Google Cloud console, Google Cloud CLI, or YAML.

### Console

  1. [Go to Cloud Run](https://console.cloud.google.com/run)

  2. If you are configuring a new job, click the **Jobs** tab and fill out the initial job settings page as needed. If you are configuring an existing job, click the job, then click **Edit**.

  3. Click **Container, Variables & Secrets, Connections, Security** to expand the job properties page.

  4. Click the **Connections** tab.

  5. Click **Connect to a VPC for outbound traffic**.

  6. Click **Send traffic directly to a VPC**.

  7. In the **Network** field, select the VPC network that you want to send traffic to.

  8. In the **Subnet** field, select the subnet where your job receives IP addresses from. You can execute multiple jobs on the same subnet.

  9. For **Traffic routing** , select one of the following:

     * **Route only requests to private IPs to the VPC** to send only traffic to internal addresses through the VPC network.
     * **Route all traffic to the VPC** to send all outbound traffic through the VPC network.
  10. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your service or services. Network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.

  11. Optional: Enter the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that you want to associate with your job or jobs. For jobs, network tags are specified at the execution level. Each job execution can have different network tags, such as `network-tag-2`.

  12. Click **Create** or **Update**.

  13. To verify that your job is on your VPC network, click the job, then click the **Configuration** tab. The network and subnet are listed in the **VPC** card.

You can now execute your Cloud Run job and send requests from the job to any resource on the VPC network, as allowed by your firewall rules.




### gcloud

To create a Cloud Run job without a connector from the Google Cloud CLI:

  1. Update `gcloud` components to the latest version:
         
         gcloud components update

  2. Ensure that the Compute Engine API is enabled for your project:
         
         gcloud services enable compute.googleapis.com
         

  3. Create a Cloud Run job with the following command:
         
         gcloud run jobs create JOB_NAME \
         --image=IMAGE_URL \
         --network=NETWORK \
         --subnet=SUBNET \
         --network-tags=NETWORK_TAG_NAMES \
         --vpc-egress=EGRESS_SETTING \
         --region=REGION

Replace:

     * JOB_NAME with the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. The subnet must be `/26` or larger. Direct VPC egress supports IPv4 ranges [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3), [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7), and Class E. You can deploy or execute multiple services or jobs on the same subnet, but the subnet cannot be shared by any existing connectors. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * REGION with a region for your job.
  4. To verify that the job is on your VPC network, run the following command:
         
         gcloud run jobs describe JOB_NAME \
           --region=REGION
           

Replace:

     * `JOB_NAME` with the name of your job.
     * `REGION` with the region for your job that you specified in the previous step.

The output should contain the name of your network and subnet, for example:
    
    VPC network:
      Network:       default
      Subnet:        default
    




You can now execute your Cloud Run job and send requests from the job to any resource on the VPC network, as allowed by your firewall rules.

### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the following attributes:
         
         apiVersion: run.googleapis.com/v1
           kind: Job
           metadata:
             name: JOB_NAME
             labels:
               cloud.googleapis.com/location: REGION
           spec:
             template:
               metadata:
                 annotations:
                   run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'
                   run.googleapis.com/vpc-access-egress: EGRESS_SETTING
               spec:
                 containers:
                 - image: IMAGE

Replace:

     * JOB_NAME with the name of your Cloud Run job. Job names must be 49 characters or less and must be unique per region and project.
     * REGION with the region for your Cloud Run job, which must match the region of your subnet.
     * NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * SUBNET with the name of your subnet. The subnet must be `/26` or larger. Direct VPC egress supports IPv4 ranges [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3), [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7), and Class E. You can deploy or execute multiple services or jobs on the same subnet, but the subnet cannot be shared by any existing connectors. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a job. For jobs, network tags are specified at the execution-level. Each job execution can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * IMAGE with the URL of your job container image.
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

## Troubleshooting

### Service account permissions

#### Serverless VPC Access Service Agent

To perform operations in your Google Cloud project, Serverless VPC Access uses the **Serverless VPC Access Service Agent** service account. This service account's email address has the following form:
    
    
    service-PROJECT_NUMBER@gcp-sa-vpcaccess.iam.gserviceaccount.com
    

By default, this service account has the **Serverless VPC Access Service Agent** role (`roles/vpcaccess.serviceAgent`). Serverless VPC Access operations may fail if you change this account's permissions.

#### Google APIs Service Agent

The Serverless VPC Access API depends on Deployment Manager to provision the underlying resources that implement the connector. To perform operations in your Google Cloud project, Deployment Manager uses the [Google APIs Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent). This service account's email address has the following form:
    
    
    PROJECT_NUMBER@cloudservices.gserviceaccount.com
    

By default, this service account has the Editor role (`roles/project.editor`) / Editor role permissions. If you want to grant the Google APIs Service Agent more limited permissions, without affecting Serverless VPC Access connector functionality, you can grant this service account the **Serverless VPC Access Service Agent** role (`roles/vpcaccess.serviceAgent`) instead.

Certain services other than Deployment Manager also rely on the default Editor role permissions of the Google APIs Service Agent. Removing this role might affect other services and resources besides the Serverless VPC Access API. For more information on the implications of removing the Editor role from the Google APIs Service Agent, see [Google APIs Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent).

### Poor network performance or high idle CPU utilization

Using a single connector for thousands of instances can cause performance degradation and elevated idle CPU utilization. To fix this, shard your services between multiple connectors.

### Issues with custom MTU

If you experience issues with a custom MTU, ensure that you [use the default MTU setting for Cloud Run](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#mtu).

### Errors

#### Service account needs Service Agent role error

If you use the **Restrict Resource Service Usage** [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to block Cloud Deployment Manager (`deploymentmanager.googleapis.com`), you might see the following error message:

`Serverless VPC Access service account (service-<PROJECT_NUMBER>@gcp-sa-vpcaccess.iam.gserviceaccount.com) needs Serverless VPC Access Service Agent role in the project.`

[Set the organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources#setting_the_organization_policy) to either remove Deployment Manager from the denylist or add it to the allowlist.

#### Connector creation error

If creating a connector results in an error, try the following:

  * Specify an [RFC 1918](https://tools.ietf.org/html/rfc1918) internal IP range that does not overlap with any existing IP address reservations in the VPC network.
  * Grant your project permission to use Compute Engine VM images from the project with ID `serverless-vpc-access-images`. For more information about how to update your organization policy accordingly, see [Set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images).



#### Unable to access resources

If you specified a connector but still cannot access resources in your VPC network, make sure that there are no firewall rules on your VPC network with a priority lower than 1000 that deny ingress from your connector's IP address range.

If you [configure a connector in a Shared VPC service project](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-service-projects), make sure that your firewall rules [allow ingress from your serverless infrastructure to the connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#allow-ranges).

#### Connection refused error

If you receive `connection refused` or `connection timeout` errors that degrade network performance, your connections could be growing without limit across invocations of your serverless application. To limit the maximum number of connections used per instance, use a client library that supports connection pools. For detailed examples of how to use connection pools, see [Manage database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections#pools).

#### Resource not found error

When deleting a VPC network or a firewall rule, you might see a message that is similar to the following: `The resource "aet-uscentral1-subnet--1-egrfw" was not found.`

For information about this error and its solution, see [Resource not found error](https://docs.cloud.google.com/vpc/docs/using-firewalls#resource-not-found) in the VPC firewall rules documentation.

## Next steps

  * Monitor admin activity with [Serverless VPC Access audit logging](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access-audit-logging).
  * Protect resources and data by [creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) with VPC Service Controls.
  * Learn about the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles associated with Serverless VPC Access. See [Serverless VPC Access roles](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess) in the IAM documentation for a list of permissions associated with each role.
  * Learn how to connect to Memorystore from: 
    * [Cloud Run](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run)
    * [Cloud Run functions](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-functions)
    * [App Engine standard environment](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-standard)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
