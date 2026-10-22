---
url: https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type/
title: Change environment networking type (Private or Public IP) \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:10.506688+00:00
---

# Change environment networking type (Private or Public IP)  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Change environment networking type (Private or Public IP) Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains the difference between Private IP and Public IP environment networking types in Managed Airflow (Gen 3) and provides instructions for switching the networking type of your environment.

If you want to disable or enable internet access only when installing PyPI packages, see [Configure internet access when installing PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/packages-internet-access).

If you want to enable access to your VPC network from your environment, see [Connect an environment to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network).

## About environment networking types

Managed Airflow (Gen 3) uses two environment networking types:

  * _Public IP networking_ :

    * Airflow components of the environment can access the internet. This is the default networking type.

    * In Public IP environments, all outbound traffic to public IP ranges is routed through the default internet gateway. This limitation includes [Privately Used Public IPs (PUPI)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configuring-privately-used-public-ips-for-gke) used in GKE since they overlap with public IP ranges. As a result, traffic intended for your PUPI address doesn't reach your private GKE address, but is routed to the public internet. To enable connections to PUPI ranges, we recommend that you switch your environment to Private IP networking and [connect it to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network).

    * Airflow components in Public IP environments establish outbound connections from automatically allocated public IP addresses and ports. If you want your Public IP environments to use predetermined IP addresses and ports, you can do so through [connecting a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network) to your environment and switching it to Private IP. In this case, Managed Airflow routes all traffic except traffic to Google services through this network. 

  * _Private IP networking_ :

    * Private IP networking is a more secure option compared to Public IP networking.

    * Airflow components of the environment don't have access to the internet. For environments [attached to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network), the network configuration controls internet access.

    * Private IP environments configure Private Google Access through the `private.googleapis.com` range, which enables access to Google APIs, services, and domains supported by this range.

For more information and the list of services and domains available through `private.googleapis.com`, see [Network configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#config-choose-domain) in the Virtual Private Cloud documentation.

    * [Private IP environments with VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc) configure Private Google Access through the `restricted.googleapis.com` range, which enables access to Google APIs, services, and domains supported by this range.

For more information and the list of services and domains available through `restricted.googleapis.com`, see [Network configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#config-choose-domain) in the Virtual Private Cloud documentation.

    * If a Private IP environment is [attached to a custom VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network), then all traffic is routed to the VPC network, except the traffic to Google APIs, services, and domains that are available to Private IP environments through Private Google Access. This approach lets your Airflow components connect to [Privately Used Public IPs (PUPI)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configuring-privately-used-public-ips-for-gke) in GKE, as the traffic will be routed through the VPC network instead of being sent to the public internet.




### Managed Airflow (Gen 2) networking compared to Managed Airflow (Gen 3)

In Managed Airflow (Gen 3), Private IP environments require no configuration.

The following Managed Airflow (Gen 2) networking features are no longer relevant in Managed Airflow (Gen 3):

  * [Configuring Private IP networking](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip). You don't need to specify IP ranges, networks, or configure connectivity and firewall rules.

  * [Configuring Private Service Connect](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect). You don't need to set ranges for Private Service Connect in Managed Airflow (Gen 3).

**Note:** [Custom VPC network attachments](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network) in Managed Airflow (Gen 3) are based on Private Service Connect. This implementation is **not related** to how Private Service Connect is used in Managed Airflow (Gen 2) (for connectivity between the environment's cluster and the resources located in the tenant project). In Managed Airflow (Gen 3), network attachments are used differently, you don't need to reflect your Managed Airflow (Gen 2) networking setup in them.
  * [Using privately used public IP ranges](https://docs.cloud.google.com/composer/docs/composer-2/configure-privately-used-public-ip). This feature provided an option to extend the available IP ranges, which are not required in Managed Airflow (Gen 3).

  * [Using the IP Masquerade agent](https://docs.cloud.google.com/composer/docs/composer-2/enable-ip-masquerade-agent). You don't need to configure cluster connectivity in Managed Airflow (Gen 3).

  * [Configuring authorized networks](https://docs.cloud.google.com/composer/docs/composer-2/configure-authorized-networks). It is not possible to access the environment's cluster in Managed Airflow (Gen 3).




The following DNS configuration isn't supported in Managed Airflow (Gen 3):

  * Managed Airflow (Gen 3) doesn't support a user-defined [`.internal` DNS zone](https://docs.cloud.google.com/compute/docs/internal-dns). If you create a DNS zone for `.internal`, it won't be possible to reach that zone.



## Change environment networking type

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Networking configuration** section, find the **Networking type** item and click **Edit**.

  5. In the **Networking type** dialog, select:

     * **Public IP environment (default)** for Public IP networking.
     * **Private IP environment** for Private IP networking.
  6. Click **Save**.




###  gcloud 

The Following Google Cloud CLI arguments change the environment's networking type:

  * `--enable-private-environment`: changes to Private IP networking.
  * `--disable-private-environment`: changes to Public IP networking (default).



Change to Private IP networking:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --enable-private-environment
    

Change to Public IP networking:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --disable-private-environment
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.



Example (Private IP):
    
    
    gcloud beta composer environments update example-environment \
      --location us-central1 \
      --enable-private-environment
    

Example (Public IP):
    
    
    gcloud beta composer environments update example-environment \
      --location us-central1 \
      --disable-private-environment
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.private_environment_config.enable_private_environment` mask.

     2. In the request body, in the `enablePrivateEnvironment` field:

        * Specify `true` to change to Private IP networking.
        * Specify `false` to change to Public IP networking (default).



Example (Private IP):
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.private_environment_config.enable_private_environment
    
    "config": {
      "privateEnvironmentConfig": {
        "enablePrivateEnvironment": true
      }
    }
    

###  Terraform 

The `enable_private_environment` field in the `config` block specifies the environment's networking type:

  * `true`: Private IP networking.
  * `false` or omitted: Public IP networking (default).


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        enable_private_environment = PRIVATE_IP_STATUS
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `PRIVATE_IP_STATUS`: `true` for Private IP, `false` for Public IP



Example (Private IP):
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        enable_private_environment = true
    
        ... other configuration parameters
      }
    }
    

## Configure proxy server variables

**Important:** Routing with proxy variables is done on a best-effort basis. **There's no guarantee that every request goes through the proxy**. Instead, we recommend to route traffic by [attaching a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network) to your environment and configuring traffic routing rules in this network.

You can set `http_proxy` and `https_proxy` [environment variables](https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables) in your environment. These standard Linux variables are used by web clients that run in containers of your environment's cluster to route traffic through the specified proxies.

The `NO_PROXY` variable by default is set to a list of Google domains, the IP address of the environment's cluster Compute Engine metadata server, and `localhost` so that they are excluded from proxying:
    
    
    .google.com,.googleapis.com,metadata.google.internal,169.254.169.254,localhost
    

This configuration makes it possible to create an environment with set `http_proxy` and `https_proxy` environment variables in cases when the proxy isn't configured to handle traffic to Google services.

## What's next

  * [Configure VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
