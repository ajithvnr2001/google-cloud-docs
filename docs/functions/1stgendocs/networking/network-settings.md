---
url: https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings/
title: Configure network settings (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.002169+00:00
---

# Configure network settings (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure network settings (1st gen)

Cloud Run functions network settings enable you to control network ingress and egress to and from individual functions. For example, you can use network settings for the following use cases:

  * Secure your functions by implementing network-based access control.
  * Make a function's egress traffic adhere to firewall, DNS, and routing rules associated with your VPC network.
  * Associate a function's egress traffic with a static IP address.



For more details about use cases, see the Example use cases section.

## Ingress settings

Ingress settings control whether resources outside of your Google Cloud project or [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) service perimeter can invoke a function.

To be subject to a VPC Service Controls perimeter's policy, a resource must belong to the [service to be restricted](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#creating_a_service_perimeter). For Cloud Run functions (1st gen), the restricted service is Cloud Functions API.

### Limitations

Internal-only, HTTP-triggered functions can **only** be invoked by HTTP requests that are either created within a VPC network, such as those from [Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine), [Compute Engine](https://docs.cloud.google.com/compute), the [App Engine Flexible Environment](https://docs.cloud.google.com/appengine/docs/flexible), or are made by Cloud Scheduler, Cloud Tasks, Workflows, or BigQuery resources that are in the same project or VPC Service Controls perimeter. This means that HTTP requests created by **or** routed through Pub/Sub or Eventarc _cannot_ trigger these functions. Event triggers are always considered "internal" and are allowed regardless of ingress setting.

### Configure ingress settings

To restrict resources from outside of your project or perimeter, specify one of the following ingress setting values:

  * **Allow all traffic** : Default. All inbound requests to the function are allowed, from both the internet and resources within the same project.
  * **Allow internal traffic only** : Only traffic from Cloud Scheduler, Cloud Tasks, Eventarc, Workflows, [BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions), and VPC networks in the same project or [VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) is allowed. All other requests are denied with a `404` error.

For requests from a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), note the following considerations:

    * Traffic is considered internal if the function is deployed in the Shared VPC host project.
    * Traffic is considered internal if the Shared VPC host and all service projects are placed inside the same [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter.
    * All other traffic from Shared VPC networks is denied.
  * **Allow internal traffic and traffic from Cloud Load Balancing** : Traffic from Cloud Scheduler, Cloud Tasks, Eventarc, Workflows, [BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions), and VPC networks in the same project or VPC Service Controls perimeter is allowed. Traffic from Cloud Load Balancing is allowed.




You can specify ingress settings when you deploy or update your function by using the Google Cloud console, Google Cloud CLI, or Terraform:

### Console

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list)

  2. Click **Create function**. Alternatively, click an existing function to go to its details page, and click **Edit**.

  3. Expand the advanced settings by clicking **Runtime, build ...**.

  4. In the **Connections** section, select a value for **Ingress settings**.




### gcloud

Use the `gcloud functions deploy` command to deploy or update the function and specify the [`--ingress-settings`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--ingress-settings) flag:
    
    
      gcloud functions deploy FUNCTION_NAME   
    
      --trigger-http   
    
      --ingress-settings INGRESS_SETTINGS   
    FLAGS...
      

where:

  * `FUNCTION_NAME` is the name of your function.
  * `INGRESS_SETTINGS` is one of the supported values for [ingress settings](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--ingress-settings). The possible values are:

    * `all`
    * `internal-only`
    * `internal-and-gclb`: allows internal traffic as well as traffic sent to a public IP exposed by [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https). Blocks traffic sent to `cloudfunctions.net` or any custom domain set up through Cloud Run functions. Prevents users from circumventing any access controls (Cloud Armor, IAP) they set up through Cloud Load Balancing.
  * `FLAGS...` refers to other flags you pass to the [`deploy` command](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy).




### Terraform

Optional. To update the ingress settings field of the `main.tf` file of your [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service), include the [`ingress_settings`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions_function#ingress_settings) argument that you want to deploy or update. Making changes to the ingress settings recreates the function.

**Note:** The following example omits additional required information for creating a function with Terraform. For an example that creates a new function, see the [Cloud Run functions Terraform module](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions_function).

  1. From your `main.tf` file, locate the resource that you want to restrict ingress settings for and update it to the setting you want, for example:
         
         resource "google_cloudfunctions_function" "function" {
           name             = "function"
           location         = "us-central1"
           description      = "Sample function"
           ingress_settings = "INGRESS_SETTINGS"
         }

where INGRESS_SETTINGS is one of the supported values for [ingress settings](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--ingress-settings). The possible values are:

     * `ALLOW_ALL` (default): All inbound requests to the function are allowed, from both the internet and resources within the same project.
     * `ALLOW_INTERNAL_ONLY`: Only traffic from Cloud Scheduler, Cloud Tasks, Eventarc, Workflows, and VPC networks in the same project or [VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) is allowed.
     * `ALLOW_INTERNAL_AND_GCLB`: Allows internal traffic as well as traffic sent to a public IP exposed by [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https). Blocks traffic sent to `cloudfunctions.net` or any custom domain set up through Cloud Run functions. Prevents users from circumventing any access controls (Cloud Armor, IAP) they set up through Cloud Load Balancing.



If you use Google Cloud Armor with [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless#deploy_serverless_app), you can create security policies that filter traffic-based conditions such as an incoming request's IP address, IP range, region code, or request headers. For more information, see [Google Cloud Armor security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

**Note:** Administrators can restrict the ingress settings that developers can select by setting the [`cloudfunctions.allowedIngressSettings`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

## Egress settings

Egress settings control the routing of outbound HTTP requests from a function. To specify egress settings, you must [connect the function to a VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc) by using a Serverless VPC Access connector. Egress settings control when traffic is routed through the connector in your VPC network.

### Limitations

  * Serverless VPC Access only supports routing IPv4 traffic. IPv6 traffic is not supported, even if you have IPv6 routes in your VPC network.

  * For added security, Google Cloud blocks egress packets to external IP addresses on TCP destination port 25.

  * User functions or services that invoke functions or services protected by a VPC network must route those invocations through a VPC connector.




### Configure egress settings

For egress settings, you can specify the following:

  * **Route only requests to private IPs through the VPC connector** : Default. Traffic is routed through the VPC network only if the packets carrying the traffic have destinations that match the following:

    * [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)
    * [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7)
    * [`199.36.153.4/30` and `199.36.153.8/30`](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options)

Packets to any other destination are routed from Cloud Run functions to the internet and not through any VPC network.

  * **Route all traffic through the VPC connector** : Traffic is always routed through the VPC network associated with the connector, for all packet destinations. You must use this option in the following circumstances:

    * If you need to send traffic to VPC subnet ranges with privately used external IP address ranges. For more information about VPC subnet ranges, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) in the Subnets overview.
    * If you need to send traffic to a Private Service Connect endpoint for Google APIs whose address is a privately used external IP address. For more information about Private Service Connect endpoints for Google APIs, see [Access Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).
    * If you need to send traffic to any other privately used external IP address destination that's routable within the connector's VPC network. Examples of other destinations covering privately used external IP addresses might include peering subnet ranges, peering subnet ranges created from [Allocated IP address ranges for services](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range), and those destinations that are accessible using custom routes in the VPC network.

If your VPC network includes a default route, packets can still be routed to the internet after being processed by the connector if you configure a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway to provide NAT services to the subnet used by the connector. These packets are subject to the routes in your VPC network and the firewall rules that apply to your VPC network. You can use route and firewall configuration to control internet egress for all outbound requests sent by your function through a Serverless VPC Access connector.

**Note:** Serverless VPC Access billing scales in proportion to the amount of traffic that passes through the connector. To understand cost implications, review [Serverless VPC Access pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing).



You can specify egress settings when you deploy or update your function by using the Google Cloud console or the Google Cloud CLI.

### Console

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list)

  2. Click **Create function**. Alternatively, click an existing function to go to its details page, and click **Edit**.

  3. Expand the advanced settings by clicking **Runtime, build ...**.

  4. In the **Connections** section, under **Egress settings** , select a Serverless VPC Access connector.

  5. Select the appropriate egress setting based on how you want to route outbound traffic through the connector.




### gcloud

Use the `gcloud functions deploy` command to deploy or update the function and specify the [`--egress-settings`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--egress-settings) flag:
    
    
      gcloud functions deploy FUNCTION_NAME   
    
      --vpc-connector CONNECTOR_NAME   
    
      --egress-settings EGRESS_SETTINGS   
    FLAGS...
      

where:

  * `FUNCTION_NAME` is the name of your function.
  * `CONNECTOR_NAME` is the name of the Serverless VPC Access connector to use. See the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--vpc-connector) for more information.

**Note:** You can omit the `--vpc-connector` flag if you are updating egress settings on an existing function that already has a connector.
  * `EGRESS_SETTINGS` is one of the supported values for egress settings: see [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--egress-settings).

  * `FLAGS...` refers to other flags you pass to the [`deploy` command](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy).




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`cloudfunctions.allowedVpcConnectorEgressSettings`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

## Example use cases

The following examples demonstrate how to configure network access in several common scenarios.

### Creating a function that cannot be called by external clients

You can secure your HTTP functions by allowing them to be called only by resources in the same Google Cloud project or VPC Service Controls service perimeter.

  1. **Deploy your function and allow internal traffic only.** Use the Google Cloud console or the Google Cloud CLI:

### Console

     1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list)

     2. Click **Create function**. Alternatively, click an existing function to go to its details page, and click **Edit**.

     3. Expand the advanced settings by clicking **Runtime, build ...**.

     4. In the **Connections** section, under **Ingress settings** , select **Allow internal traffic only**.

### gcloud

Use the `gcloud functions deploy` command:
    
    gcloud functions deploy FUNCTION_NAME \
    --ingress-settings internal-only \
    FLAGS...
    




After you deploy your function, requests originating from outside of your Google Cloud project are blocked from reaching the function. If you use VPC Service Controls, requests from outside of the service perimeter are blocked. VM instances inside your project or service perimeter can still reach your function by making requests to its HTTPS endpoint.

If you want to call this restricted function from another function, the calling function must route its egress through your VPC network.

### Using egress and ingress settings to restrict access

You can incorporate both ingress and egress to your services to add an additional layer of restriction.

  1. Clone the `cloud-run-sample` repository and change to the `vpc-sample` directory: 
         
         git clone https://github.com/GoogleCloudPlatform/cloud-run-samples
         cd vpc-sample

  2. Install Python dependencies: 
         
         pip3 install -r requirements.txt

  3. You can open the `main.py` file in the `vpc-sample` directory to see the function you are deploying: 
         
         def hello_world(request):
             return "Hello World!"

  4. Deploy the function: 
         
         gcloud functions deploy restricted-function   
           --runtime=python38   
           --trigger-http   
           --no-allow-unauthenticated   
           --ingress-settings=internal-only   
           --entry-point=hello_world

  5. Set up a Serverless VPC Access connector: 
         
         gcloud compute networks vpc-access connectors create serverless-connector   
           --region=SERVICE_REGION   
           --range=10.8.0.0/28

where `SERVICE_REGION` is a region for your connector; this must match the region of your serverless service. If your service is in the region `us-central` or `europe-west`, use `us-central1` or `europe-west1`.

  6. Build your container image: 
         
         gcloud builds submit --tag=gcr.io/PROJECT_ID/restricted-function-caller .

where `PROJECT_ID` is the project ID.

This builds a container image that invokes `get_hello_world` when deployed from the `main.py` file: 
         
         import os
         import urllib
         
         import google.auth.transport.requests
         import google.oauth2.id_token
         
         
         def get_hello_world(request):
             try:
                 url = os.environ.get("URL")
                 req = urllib.request.Request(url)
         
                 auth_req = google.auth.transport.requests.Request()
                 id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
                 req.add_header("Authorization", f"Bearer {id_token}")
         
                 response = urllib.request.urlopen(req)
                 return response.read()
         
             except Exception as e:
                 print(e)
                 return str(e)

  7. Use the `gcloud run deploy run-function` command to deploy the Cloud Run container: 
         
         gcloud run deploy run-function   
         
             --image gcr.io/PROJECT_ID/restricted-function-caller   
         
             --no-allow-unauthenticated   
         
             --update-env-vars=URL=https://SERVICE_REGION-PROJECT_ID.cloudfunctions.net/restricted-function-caller   
         
             --vpc-egress=all   
         
             --vpc-connector=serverless-connector   
         
             --region=SERVICE_REGION

where:

     * `PROJECT_ID` is the project ID.
     * `SERVICE_REGION` is a region for your connector; this must match the region of your serverless service. If your service is in the region `us-central` or `europe-west`, use `us-central1` or `europe-west1`.

The Cloud Run `run-function` service is now set to send a `GET` request from the VPC connector to the network-restricted function.




### Routing function egress through your VPC network

VPC networks in Google Cloud support a rich set of configurations and networking features. By routing egress traffic from your function into your VPC network, you can ensure that Cloud Run functions egress traffic follows your VPC network's firewall, DNS, routing, and other rules, and you can use products such as [Cloud NAT](https://docs.cloud.google.com/nat).

  1. **Set up a VPC network.** Configure an existing VPC network or create a new one by following the guide at [Using VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  2. **Set up a Serverless VPC Access connector.** Cloud Run functions need a Serverless VPC Access connector to route traffic into your VPC network. Create a connector and set up the appropriate permissions by following the instructions at [Connecting to a VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc).

  3. **Deploy a function that uses the connector and route all egress through the connector.** Use the Google Cloud console or the `gcloud` command-line tool:

### Console

     1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list)

     2. Click **Create function**. Alternatively, click an existing function to go to its details page, and click **Edit**.

     3. Expand the advanced settings by clicking **Runtime, build ...**.

     4. In the **Connections** section, under **Egress settings** , select your Serverless VPC Access connector and select **Route all traffic through the VPC connector**.

### gcloud

Use the `gcloud functions deploy` command:
    
    gcloud functions deploy FUNCTION_NAME \
    --vpc-connector CONNECTOR_NAME \
    --egress-settings all \
    FLAGS...
    




After you deploy your function, all traffic originating from your function is routed through your VPC network and adheres to the rules set on your VPC network. Note that your function is unable to access the public internet unless you [configure Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation). Further note that you need your Cloud NAT to map all primary and secondary IP ranges for all subnets to the NAT gateway, in order to include the connector's subnet in the mapping.

### Associating function egress with a static IP address

In some cases, you might want traffic originating from your function to be associated with a static IP address. For example, this is useful if you are calling an external service that only allows requests from explicitly specified IP addresses.

  1. **Route your function's egress through your VPC network.** See the previous section, Routing function egress through your VPC network.

  2. **Set up Cloud NAT and specify a static IP address.** Follow the guides at [Specify subnet ranges for NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#specify_subnet_ranges_for_nat) and [Specify IP addresses for NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#specify_ip_addresses_for_nat) to set up Cloud NAT for the subnet associated with your function's Serverless VPC Access connector. Your Cloud NAT must map all primary and secondary IP ranges for all subnets to the NAT gateway to include the connector's subnet in the mapping.




### Multi-region load balancing

You can deploy a function to different regions, and allow the request to be be sent to the closest healthy region. To achieve this, you need to set up a serverless network endpoint group (NEG) for the function and connect it to a load balancer, as described in [Setting up an HTTP(S) load balancer with serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless#multi_region_lb).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
