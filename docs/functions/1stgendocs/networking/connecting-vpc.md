---
url: https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc/
title: Connect to a VPC network \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.520893+00:00
---

# Connect to a VPC network  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to a VPC network

This page shows how to use [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) to connect Cloud Run functions directly to your VPC network, allowing access to Compute Engine VM instances, Memorystore instances, and any other resources with an internal IP address.

**Note:** Serverless VPC Access connectors incur a monthly charge. For more information, see Serverless VPC Access [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing).

## Before you begin

  * If you don't already have a VPC network in your project, [create one](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  * If you use Shared VPC, [provide access to the connector](https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-host-project#provide_access_to_the_connector), and see [Connecting to a Shared VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-shared-vpc).

  * In the Google Cloud console, ensure that the Serverless VPC Access API is enabled for your project.

[Enable API](https://console.cloud.google.com/marketplace/details/google/vpcaccess.googleapis.com)




## Create a Serverless VPC Access connector

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

## Configure your function to connect to a VPC network

You must configure each function to use a Serverless VPC Access connector to connect to your VPC network for sending egress traffic. You can configure a function to use a connector from the Google Cloud console or the Google Cloud CLI:

###  Console 

  1. [Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

  2. Click **Create Function** if you are configuring a new function. If you are configuring an existing function, click on the function, then click **Edit**.

  3. If you are configuring a new function, fill out the initial function settings page as desired, then click **Runtime, build...** to expand the function configuration page.

  4. Click the **Connections** tab and under Egress settings, choose one of the following options from the **VPC Network** menu:

     * To disconnect your function from a VPC network, select **None**.
     * To use an existing connector, select it from the drop-down list or select **Custom** to use an existing connector that's not shown in the drop-down list.
     * To create a new connector, select **Add new VPC connector**. ([Preview](https://cloud.google.com/products#product-launch-stages))

See Create a Serverless VPC Access connector for details on creating a connector.

  5. Click **Next**.




###  gcloud 

Use the `gcloud functions deploy` command to deploy the function and specify the [`--vpc-connector`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--vpc-connector) flag:
    
    
    gcloud functions deploy FUNCTION_NAME \
    --vpc-connector CONNECTOR_NAME \
    FLAGS...
    

where:

  * `FUNCTION_NAME` is the name of your function.
  * `CONNECTOR_NAME` is the name of your connector.
  * `FLAGS...` refers to other flags you pass during [function deployment](https://docs.cloud.google.com/functions/docs/deploy).



Use the [`--clear-vpc-connector`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-vpc-connector) flag to to disconnect your function from a VPC network:
    
    
    gcloud functions deploy FUNCTION_NAME \
    --clear-vpc-connector \
    FLAGS...
    

For more control over which requests are routed through the connector, see [Egress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#egress_settings).

## Access to VPC resources

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

## Manage your connector

### Disconnect a function from a VPC network

You can disconnect a function from your VPC network using the Google Cloud console or the Google Cloud CLI:

###  Console 

  1. Go to the Cloud Run functions overview page in the Google Cloud console:

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

  2. Click an existing function to go to its details page, and click **Edit**.

  3. Expand the advanced settings by clicking **Runtime, build...**.

  4. In the **Connections** tab under Egress settings, enter the name of your connector in the **VPC connector** field, or clear the field to disconnect your function from a VPC network.




###  gcloud 

Use the [`--clear-vpc-connector`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-vpc-connector) flag to to disconnect your function from your VPC network:
    
    
    gcloud functions deploy FUNCTION_NAME \
    --clear-vpc-connector \
    FLAGS...
    

where:

  * `FUNCTION_NAME` is the name of your function.
  * `CONNECTOR_NAME` is the name of your connector.
  * `FLAGS...` refers to other flags you pass during [function deployment](https://docs.cloud.google.com/functions/docs/deploy).



Connectors continue to incur charges even if they have no traffic and are disconnected. For details, see [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing). If you no longer need your connector, be sure to delete it to avoid continued billing.

### Update a connector

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




### Delete a connector

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

### Missing necessary permission vpcaccess.connectors.use for service account...

First, make sure that the role `roles/vpcaccess.user` is assigned to the service account.

If you still run into permission issues with the VPC connector, check if it is in fact a Shared VPC. In that case, [additional setup](https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-host-project#provide_access_to_the_connector) is required on the host project.

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
