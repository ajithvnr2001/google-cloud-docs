---
url: https://docs.cloud.google.com/data-transfer-essentials/docs/create-resources/
title: Create Data Transfer Essentials resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:50.016028+00:00
---

# Create Data Transfer Essentials resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-transfer-essentials/docs/create-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Data Transfer Essentials ](https://docs.cloud.google.com/data-transfer-essentials/docs)
  * [ Guides ](https://docs.cloud.google.com/data-transfer-essentials/docs/overview)



Send feedback 

#  Create Data Transfer Essentials resources Stay organized with collections  Save and categorize content based on your preferences. 

For traffic to be identified as configured for Data Transfer Essentials billing, you need to select services and associate them with selected endpoints. This page shows you how to create the required Data Transfer Essentials resources, which are configurations and destinations.

## Before you begin

Before you create Data Transfer Essentials configurations or destinations, do the following:

  1. If you haven't already done so, [install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  2. Authenticate the gcloud CLI with your account:
         
         gcloud auth login
         

  3. Set your project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  4. [Enable the Network Connectivity API](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com) in your project.

  5. Configure [permissions](https://docs.cloud.google.com/data-transfer-essentials/docs/access-control).

  6. Check whether the services that you want to select for Data Transfer Essentials are supported. You can configure Data Transfer Essentials only for [supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services).

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-supported-services list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-supported-services/list).
         
         gcloud network-connectivity multicloud-data-transfer-supported-services list \
             --location=LOCATION
         

Replace `LOCATION` with a Google Cloud region ID—for example, `europe-west3`.

The following sample output shows that the services are eligible to be configured by using Data Transfer Essentials because they use supported tiers.
         
         NAME                   SERVICE_CONFIGS
         cloud-sql              [{'eligibilityCriteria': 'NETWORK_SERVICE_TIER_PREMIUM_ONLY'}]
         cloud-storage          [{'eligibilityCriteria': 'REQUEST_ENDPOINT_REGIONAL_ENDPOINT_ONLY'}]
         compute-engine         [{'eligibilityCriteria': 'NETWORK_SERVICE_TIER_STANDARD_ONLY'}]
         

To check the eligibility of a specific service, use the [`gcloud network-connectivity multicloud-data-transfer-supported-services describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-supported-services/describe).
         
         gcloud network-connectivity multicloud-data-transfer-supported-services describe SERVICE1 \
             --location=LOCATION
         

Replace `SERVICE1` with a valid string that represents the service. See [Supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services).

###  API 

Use the [`multicloudDataTransferSupportedServices.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferSupportedServices/get).
         
         GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:getMulticloudDataTransferSupportedServices
         

Replace the following:

     * `PROJECT_ID`: the ID of your project
     * `LOCATION`: a Google Cloud region ID, for example, `europe-west3`

The following sample output lists the services that are eligible to be configured by using Data Transfer Essentials because they use supported tiers.
    
    {
      "multicloudDataTransferSupportedServices": [
        {
          "name": "cloud-sql",
          "serviceConfigs": [
            {
              "eligibilityCriteria": "NETWORK_SERVICE_TIER_PREMIUM_ONLY"
            }
          ]
        },
        {
          "name": "cloud-storage",
          "serviceConfigs": [
            {
              "eligibilityCriteria": "REQUEST_ENDPOINT_REGIONAL_ENDPOINT_ONLY"
            }
          ]
        },
        {
          "name": "compute-engine",
          "serviceConfigs": [
            {
              "eligibilityCriteria": "NETWORK_SERVICE_TIER_STANDARD_ONLY"
            }
          ]
        }
      ]
    }
    

To check the eligibility of a specific service, use the following method:
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:getMulticloudDataTransferSupportedServices
    {
    "service": "SERVICE1"
    }
    

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `LOCATION`: a Google Cloud region ID, for example, `europe-west3`.
     * `SERVICE1`: a valid string that represents the service. See [Supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services).

  7. Check whether the autonomous system numbers (ASNs) that you want to specify are recognized. You can configure traffic only to destinations that use [recognized ASNs](https://docs.cloud.google.com/data-transfer-essentials/docs/asn).




## Create a configuration

Create a Data Transfer Essentials configuration that includes specified services. You can create only one configuration per region per project.

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/create).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs create CONFIGURATION_NAME \
        --location=LOCATION \
        --description=DESCRIPTION \
        --services=SERVICE-A,...
    

Replace the following:

  * `CONFIGURATION_NAME`: a name for the configuration.
  * `LOCATION`: the region of the configuration.
  * `DESCRIPTION`: a description of the configuration and its purpose.
  * `SERVICE-A,...`: a series of strings that represent the services for which you want to configure Data Transfer Essentials. For valid strings, see [Supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services).



The following sample command creates a configuration named `config1` in the `europe-west3` region for the `compute-engine`, `cloud-storage`, and `cloud-sql` services.
    
    
    gcloud network-connectivity multicloud-data-transfer-configs create config1 \
        --location=europe-west3 \
        --description="configuration for europe-west3" \
        --services=compute-engine,cloud-storage,cloud-sql
    

###  API 

Use the [`multicloudDataTransferConfigs.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs/create).
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME
    {
      "description": "DESCRIPTION",
      "services": {
        "SERVICE-A",
        "SERVICE-B"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the region of the configuration.
  * `CONFIGURATION_NAME`: a name for the configuration.
  * `DESCRIPTION`: a description of the configuration and its purpose.
  * `SERVICE-A,...`: a series of strings that represent the services for which you want to configure Data Transfer Essentials. For valid strings, see [Supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services).



Optionally, use the `requestID` query parameter to identify your API requests. If you retry your request, the server can use the identifier to ignore a request that has already been responded to.

The following JSON snippet creates a configuration named `config1` in the `europe-west3` region for the `compute-engine`, `cloud-storage`, and `cloud-sql` services.
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/my-project/locations/europe-west3/multicloudDataTransferConfigs/config1
    {
      "description": "configuration for europe-west3",
      "services": {
        "compute-engine": {},
        "cloud-storage": {},
        "cloud-sql": {}
    }
    

###  Terraform 

The following Terraform example creates a configuration.
    
    
    resource "google_network_connectivity_multicloud_data_transfer_config" "default" {
      name        = "config"
      location    = "europe-west1"
      description = "A basic multicloud data transfer config"
      services {
        service_name = "big-query"
      }
      services {
        service_name = "cloud-storage"
      }
    }

Data Transfer Essentials configurations take up to 24 hours to be created. To check the state of the configuration, [view the details of the configuration](https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources#view-config-details).

To add or remove services, [update a configuration](https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources#update-config).

Before attempting to create a new configuration, [delete the existing configuration](https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources#delete-config).

## Create a destination for the configuration

Create a destination for the Data Transfer Essentials configuration. A destination resource creates an association between an existing configuration and an external IP prefix with an endpoint. An endpoint contains a cloud service provider (CSP) identifier and its ASN.

Create one destination at a time.

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs destinations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/destinations/create).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs destinations create DESTINATION_NAME \
        --multicloud-data-transfer-config=CONFIGURATION_NAME \
        --location=LOCATION \
        --description=DESCRIPTION \
        --ip-prefix=IP_PREFIX \
        --endpoints=asn=ASN,csp=CSP
    

Replace the following:

  * `DESTINATION_NAME`: a name for the destination. The name must be unique within a region.
  * `CONFIGURATION_NAME`: the name of the configuration.
  * `LOCATION`: the region of the configuration.
  * `DESCRIPTION`: a description of the destination and its purpose.
  * `IP_PREFIX`: the IP prefix of the destination specified as a range (for example, `203.0.113.0/24` or `2001:db8::/32`) or a value (for example, `203.0.113.6` or `2001:db8:2:2:2:2:2:2`). An IP prefix must be used only once in a configuration, must be associated with at least one endpoint, and can be associated with up to 5 endpoints.

  * Specify strings corresponding to the endpoints that you want to add to the destination:

    * `ASN`: the ASN expected to announce the prefix. See [Recognized ASNs](https://docs.cloud.google.com/data-transfer-essentials/docs/asn).
    * `CSP`: a string that represents the CSP of the ASN that is announcing the prefix.

You can specify the `endpoints` flag multiple times in the same command. A destination must have at least one endpoint and can't have more than five endpoints.




The following sample command creates a destination named `destination1` for configuration `config1` in the `europe-west3` region for the specified IP prefix and endpoint.
    
    
    gcloud network-connectivity multicloud-data-transfer-configs destinations create destination1 \
        --multicloud-data-transfer-config=config1 \
        --location=europe-west3 \
        --description="destination1 for config1" \
        --ip-prefix=203.0.113.0/24 \
        --endpoints=asn=16509,csp="aws"
    

###  API 

Use the [`multicloudDataTransferConfigs.destinations.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs.destinations/create).
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME/destinations/DESTINATION_NAME
    {
      "description": "DESCRIPTION",
      "ipPrefix": "IP_PREFIX",
      "endpoints": [
        {
          "asn": "ASN",
          "csp": "CSP"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the region of the configuration.
  * `CONFIGURATION_NAME`: the name of the configuration.
  * `DESTINATION_NAME`: a name for the destination. The name must be unique within a region.
  * `DESCRIPTION`: a description of the destination and its purpose.
  * `IP_PREFIX`: the IP prefix of the destination specified as a range (for example, `203.0.113.0/24` or `2001:db8::/32`) or a value (for example, `203.0.113.6` or `2001:db8:2:2:2:2:2:2`). An IP prefix must be used only once in a configuration and for only one ASN.

  * Specify strings corresponding to the endpoints that you want to add to the destination:

    * `ASN`: the ASN expected to announce the prefix. See [Recognized ASNs](https://docs.cloud.google.com/data-transfer-essentials/docs/asn).
    * `CSP`: a string that represents the CSP of the ASN that is announcing the prefix.

You can specify multiple endpoints in the same call. A destination must have at least one endpoint and can't have more than five endpoints.




The following sample command creates a destination named `destination1` for configuration `config1` in the `europe-west3` region for the specified IP prefix and endpoint.
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/my-project/locations/europe-west3/multicloudDataTransferConfigs/config1/destinations/destination1
    {
      "description": "destination1 for config1",
      "ipPrefix": "203.0.113.0/24",
      "endpoints": [
        {
          "asn": "16509",
          "csp": "aws"
        }
      ]
    }
    

###  Terraform 

The following Terraform example creates a destination.
    
    
    resource "google_network_connectivity_destination" "default" {
      name                            = "destination"
      location                        = "europe-west1"
      multicloud_data_transfer_config = google_network_connectivity_multicloud_data_transfer_config.default.name
      description                     = "A basic destination"
      ip_prefix                       = "10.0.0.0/8"
      endpoints {
        asn = "14618"
        csp = "AWS"
      }
    }

To check the state of the destination, [view the details of the destination](https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources#view-destination-details).

To add or remove endpoints, [update the destination](https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources#update-destination).

Alternatively, [delete the destination](https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources#delete-destination).

**Note:** If billing doesn't match your configuration, the reason might be that egress traffic doesn't match the configured source service, the destination IP prefix, or the time of usage. Use [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) to verify that egress traffic is originating from the configured services and, as expected, reaching the configured destination IP prefix.

## What's next

  * [Manage Data Transfer Essentials resources](https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
