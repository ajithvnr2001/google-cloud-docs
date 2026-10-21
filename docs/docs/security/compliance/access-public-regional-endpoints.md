---
url: https://docs.cloud.google.com/docs/security/compliance/access-public-regional-endpoints/
title: Access regional Google APIs through public endpoints \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:42.761346+00:00
---

# Access regional Google APIs through public endpoints  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/access-public-regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Access regional Google APIs through public endpoints Stay organized with collections  Save and categorize content based on your preferences. 

You can access regional and multi-regional endpoints publicly over the internet or privately from within your Virtual Private Cloud. This document explains how to access the endpoints publicly.

When you access regional endpoints from the public internet, traffic is routed through Google Cloud [Standard Tier networking](https://docs.cloud.google.com/network-tiers/docs/overview). The connection, including TLS termination, is handled within the destination region.

## Configure public internet access to the APIs

To configure public internet access to regional API endpoints, follow these steps.

### Roles

To get the permissions that you need to create a regional endpoint, ask your administrator to grant you the following IAM roles on your VPC network: 

  * [Compute Network Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [DNS Administrator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         $ gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. Enable the Compute Engine, Network Connectivity Center, and Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,networkconnectivity.googleapis.com,dns.googleapis.com)

  3. Additionally, [enable the API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for the target service that you want to access through the endpoint. For example, if you want to access `spanner.me-central2.rep.googleapis.com`, enable the Cloud Spanner API.

  4. Ensure that egress firewall rules permit traffic to the endpoint. The default firewall configuration for a VPC network permits this traffic because it contains an implied allow egress rule. Verify that you haven't created a higher priority egress rule that blocks the traffic.




### Identify the endpoint

Determine the service and the specific region or multi-region required for your workload.

  * Regional endpoints have the following format: `SERVICE.REGION.rep.googleapis.com`

  * Multi-regional endpoints have the following format: `SERVICE.MULTI_REGION.rep.googleapis.com`




### Modify the DNS configuration

If your environment overrides public DNS for `googleapis.com` using a private DNS zone, which is common in hybrid configurations, take these steps:

  * Update your DNS configuration to exclude `rep.googleapis.com`. For more information, see [Add, update, and delete records](https://docs.cloud.google.com/dns/docs/records).

  * Modify the DNS zone setup to exclude the `rep.googleapis.com` subdomain. Forward those queries to public DNS resolvers. For more information, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).




### Configure the Google Cloud CLI

To override the default API endpoint for specific services, use the Google Cloud CLI. The following example uses the [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command to set an override for Cloud Storage in `us-central1` and an override for Compute Engine in `europe-west1`.
    
    
    # Set an override for Cloud Storage in us-central1.
    
    gcloud config set api_endpoint_overrides/storage https://storage.us-central1.rep.googleapis.com/
    
    # Set an override for Compute Engine in europe-west1.
    
    gcloud config set api_endpoint_overrides/compute https://compute.europe-west1.rep.googleapis.com/compute/v1/
    

After you set the override, gcloud CLI commands for that service use the regional endpoint. To revert to using the default global endpoint, use the [`gcloud config unset`](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) command:
    
    
    gcloud config unset api_endpoint_overrides/SERVICE
    

### Update the client SDKs

Most Google Cloud client libraries let you specify a custom endpoint during client initialization.

### Python

Use `client_options` with `api_endpoint`.
    
    
    from google.cloud import SERVICE
    from google.api_core.client_options import ClientOptions
    
    options = ClientOptions(api_endpoint='https://SERVICE.REGION.rep.googleapis.com')
    SERVICE_client = SERVICE.Client(client_options=options, project='PROJECT_ID')
    # ... use SERVICE_client as usual
    

Replace the following:

  * `SERVICE`: the name of your service
  * `REGION`: the region for your endpoint
  * `PROJECT_ID`: the ID of your Google Cloud project



### Go

Use `option.WithEndpoint` during client creation.
    
    
    client, err := SERVICE.NewClient(ctx, projID, 
    option.WithEndpoint("https://SERVICE-my-endpoint.REGION.rep.googleapis.com"), // Override endpoint
    

Replace the following:

  * `SERVICE`: the name of your service
  * `REGION`: the region for your endpoint



### .NET

Configure `Endpoint` in the client builder.

### Java

Use `setEndpoint` on the service settings builder.

The following example uses Java to connect to the endpoint for the Cloud Vision API.
    
    
    ImageAnnotatorSettings settings = ImageAnnotatorSettings.newBuilder()
    .setEndpoint("https://vision.REGION.rep.googleapis.com")
    .build();
    ImageAnnotatorClient client = ImageAnnotatorClient.create(settings);
    

## Reference documentation

  * Use the [Google Cloud CLI to manage regional endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints).
  * See the [`regionalEndpoints` REST documentation](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints).



## What's next

  * [Access regional Google APIs through backends](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls).
  * See the Google Cloud [supported regional service endpoints](https://docs.cloud.google.com/docs/security/compliance/regional-service-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
