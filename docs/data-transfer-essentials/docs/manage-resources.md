---
url: https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources/
title: Manage Data Transfer Essentials resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:49.307295+00:00
---

# Manage Data Transfer Essentials resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-transfer-essentials/docs/manage-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Data Transfer Essentials ](https://docs.cloud.google.com/data-transfer-essentials/docs)
  * [ Guides ](https://docs.cloud.google.com/data-transfer-essentials/docs/overview)



Send feedback 

#  Manage Data Transfer Essentials resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage [resources created by using Data Transfer Essentials](https://docs.cloud.google.com/data-transfer-essentials/docs/create-resources).

## Manage configurations

You can list Data Transfer Essentials configurations in your project, check the state of a configuration, update a configuration, or delete it.

### List the configurations in a project

To list all configurations in a location in a project, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/list).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs list \
        --location=LOCATION
    

Replace `LOCATION` with the region of the configuration.

###  API 

Use the [`multicloudDataTransferConfigs.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs/get).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `LOCATION`: the region of the configuration



Optionally, use the `requestID` query parameter to identify your API requests. If you retry your request, the server can use the identifier to ignore a request that has already been responded to.

### View the details of a configuration

To view the details of a configuration, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/describe).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs describe CONFIGURATION_NAME \
        --location=LOCATION
    

Replace the following:

  * `CONFIGURATION_NAME`: the name of the configuration
  * `LOCATION`: the region of the configuration



The following sample output shows that traffic from `compute-engine` is ready to be considered for Data Transfer Essentials billing. For `cloud-sql` and `cloud-storage`, the update is pending. The `effectiveTime` value indicates the time at which the state is expected to take effect. The sample also shows the total number of destinations in the configuration and the number of destinations that are active.
    
    
    description: 'sample config'
    destinationsCount: 2
    destinationsActiveCount: 0
    name: config1
    region: https://www.googleapis.com/network-connectivity/v1/projects/my-project/locations/europe-west3
    services:
    - cloud-sql:
      states:
      - effectiveTime: 2024-12-12T08:00:00Z
        state: DELETING
    - cloud-storage:
      states:
      - effectiveTime: 2024-12-12T08:00:00Z
        state: ADDING
    - compute-engine:
      states:
      - state: ACTIVE
    …
    

###  API 

Use the [`multicloudDataTransferConfigs.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs/list).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `LOCATION`: the region of the configuration
  * `CONFIGURATION_NAME`: the name of the configuration



The following sample output shows that traffic from `compute-engine` is ready to be considered for Data Transfer Essentials billing. For `cloud-storage` and `cloud-sql`, the update is pending. The `effectiveTime` value indicates the time at which the state is expected to take effect. The sample also shows the total number of destinations in the configuration and the number of destinations that are active.
    
    
    {
      "multicloudDataTransferConfig": [
        {
          "name": "projects/test-project/locations/europe-west1/multicloudDataTransferConfigs/config1",
          "createTime": "2025-05-14T10:16:22.761275571Z",
          "updateTime": "2025-05-14T10:16:25.872465362Z",
          "etag": "l-WY4OT6hBsMT8sAwEbuSpviLsE9iC_UDJXDyfE265I",
          "description": "sample config",
          "destinationsCount": 1,
          "destinationsActiveCount": 1,
          "services": {
            "cloud-sql": {
              "states": [
                {
                  "effectiveTime": "2025-05-29T07:00:00Z",
                  "state": "DELETING"
                }
              ]
            },
            "cloud-storage": {
              "states": [
                {
                  "effectiveTime": "2025-05-29T07:00:00Z",
                  "state": "ADDING"
                }
              ]
            },
            "compute-engine": {
              "states": [
                {
                  "state": "ACTIVE"
                }
              ]
            }
          }
        }
      ]
    }
    

The state of a service can be one of the following:

  * `ADDING`: the service is being added.
  * `DELETING`: the service is being deleted.
  * `ACTIVE`: the service is configured for Data Transfer Essentials billing.



### Update a configuration

To add or delete services from a configuration, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/update).

To specify services, use one of the following options:

  * `services`: replaces the services in the configuration with the specified list
  * `update-services`: adds the specified services to the configuration
  * `remove-services`: removes the specified services from the configuration
  * `clear-services`: removes all services from the configuration


    
    
    gcloud network-connectivity multicloud-data-transfer-configs update CONFIGURATION_NAME \
        --location=LOCATION \
        --description=DESCRIPTION \
        --services=SERVICE-A,... |
            --update-services=SERVICE-A,... |
            --remove-services=SERVICE-A,... |
            --clear-services
    

Replace the following:

  * `CONFIGURATION_NAME`: the name of the configuration that you want to update.
  * `LOCATION`: the region of the configuration.
  * `DESCRIPTION`: a description of the configuration and its purpose.
  * `SERVICE-A,...`: a series of strings that represent the services that you want to add or delete from the configuration. For valid strings, see [Supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services). Use `clear-services` to remove all services from the configuration.



###  API 

Use the [`multicloudDataTransferConfigs.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs/patch).
    
    
    PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME
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
  * `CONFIGURATION_NAME`: the name of the configuration.
  * `DESCRIPTION`: a description of the configuration and its purpose.
  * `SERVICE-A`: a series of strings that represent the services that you want to add or delete from the configuration. For valid strings, see [Supported services and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services).



Additionally, to prevent a specified set of fields from being overwritten during an update operation, you can use the `updateMask` option, which follows the [fieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask) format.

Updates to Data Transfer Essentials configurations take effect in approximately 24 hours.

### Delete a configuration

You can delete a configuration only after you delete all destinations that are associated with it.

To delete a configuration, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/delete).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs delete CONFIGURATION_NAME \
        --location=LOCATION
    

###  API 

Use the [`multicloudDataTransferConfigs.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs/delete).
    
    
    DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME
    

## Manage destinations

You can list Data Transfer Essentials destinations in your project, check the state of a destination, update a destination, or delete it.

### List the destinations in a project

To list all destinations in a project, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs destinations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/destinations/list).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs destinations list \
        --multicloud-data-transfer-config=CONFIGURATION_NAME \
        --location=LOCATION
    

Replace the following:

  * `CONFIGURATION_NAME`: the name of the configuration whose destinations you want to list
  * `LOCATION`: the region of the configuration



###  API 

Use the [`multicloudDataTransferConfigs.destinations.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs.destinations/list).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `LOCATION`: the region of the configuration
  * `CONFIGURATION_NAME`: the name of the configuration whose destinations you want to list



### View the details of a destination

To view the details of a destination, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs destinations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/destinations/describe).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs destinations describe DESTINATION_NAME \
        --multicloud-data-transfer-config=CONFIGURATION_NAME \
        --location=LOCATION
    

Replace the following:

  * `DESTINATION_NAME`: the name of the destination
  * `CONFIGURATION_NAME`: the name of the configuration whose destination you want to view
  * `LOCATION`: the region of the configuration



The following sample shows that the endpoint specified for `destination1` is valid and the destination is being added by the time indicated by `effectiveTime`.
    
    
    createTime: '2025-05-28T13:08:00.171978514Z'
    description: 'sample destination'
    endpoints:
    - asn: 16509
      csp: aws
      state: VALID
    etag: tag1
    ipPrefix: 203.0.113.0/24
    name: projects/test-project/locations/europe-west3/multicloudDataTransferConfig/config1/destinations/destination1
    stateTimeline:
      states:
      - effectiveTime: '2025-05-29T07:00:00Z'
        state: ADDING
    updateTime: '2025-05-28T13:08:03.431862259Z'
    …
    

###  API 

Use the [`multicloudDataTransferConfigs.destinations.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs.destinations/get).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME/destinations/DESTINATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `LOCATION`: the region of the configuration
  * `CONFIGURATION_NAME`: the name of the configuration
  * `DESTINATION_NAME`: the name of the destination



The following sample output shows that the endpoint specified for `destination1` is valid and the destination is being added by the time indicated by `effectiveTime`.
    
    
    {
      "destination": [
        {
          "name": "projects/test-project/locations/europe-west3/multicloudDataTransferConfig/config1/destinations/destination1",
          "createTime": "2025-05-14T10:18:16.941520739Z",
          "updateTime": "2025-05-14T10:18:20.028116272Z",
          "etag": "tag1",
          "description": "sample destination",
          "ipPrefix": "203.0.113.0/24",
          "endpoints": [
            {
              "asn": 16509,
              "csp": "aws",
              "state": "VALID"
            }
          ],
          "stateTimeline": {
            "states": [
              {
                "state": "ADDING",
                "effectiveTime": "2025-05-29T07:00:00Z"
              }
            ]
          }
        }
      ]
    }
    

For a destination, the state can be one of the following:

  * `ADDING`: the destination is being added.
  * `DELETING`: the destination is being deleted.
  * `SUSPENDING`: the destination is being suspended based on [auditing](https://docs.cloud.google.com/data-transfer-essentials/docs/overview#auditing).
  * `ACTIVE`: the destination is considered for Data Transfer Essentials billing.
  * `SUSPENDED`: the destination was either deleted or violates the terms of usage and won't be considered for Data Transfer Essentials billing.



For an endpoint, the state can be one of the following:

  * `VALID`: the combination of ASN and CSP values is valid.
  * `INVALID`: the combination of ASN and CSP values isn't valid.



If the state for even one endpoint is `VALID`, then the destination is considered as qualifying for Data Transfer Essentials billing.

If the state for all endpoints is `INVALID`, then the destination is considered as _not_ qualifying for Data Transfer Essentials billing. In this case, the state of the destination is set to `SUSPENDING` or `SUSPENDED`, depending on whether the current state is `ADDING` or `ACTIVE`, respectively. The traffic to such a destination is treated as regular internet traffic.

### Update a destination

A destination must have at least one endpoint and can't have more than five endpoints.

To add or delete endpoints from a destination, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs destinations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/destinations/update).

To specify endpoints, use one of the following options. You can specify the `add-endpoints` or `remove-endpoints` flags multiple times in the same command.

  * `endpoints`: replaces the endpoints in the destination with the specified list
  * `add-endpoints`: adds the specified endpoints to the destination
  * `remove-endpoints`: removes the specified endpoints from the destination


    
    
    gcloud network-connectivity multicloud-data-transfer-configs destinations update DESTINATION_NAME \
        --multicloud-data-transfer-config=CONFIGURATION_NAME \
        --location=LOCATION \
        --description=DESCRIPTION \
        --ip-prefix=IP_PREFIX \
        --endpoints=asn=ASN,csp=CSP |
            --add-endpoints=asn=ASN,csp=CSP |
            --remove-endpoints=asn=ASN,csp=CSP
    

Replace the following:

  * `DESTINATION_NAME`: the name of the destination.
  * `CONFIGURATION_NAME`: the name of the configuration that you want to update.
  * `LOCATION`: the region of the configuration.
  * `DESCRIPTION`: a description of the destination and its purpose.
  * `IP_PREFIX`: the IP prefix of the destination specified as a range or a value.
  * For each endpoint, specify the following:

    * `ASN`: the ASN that is expected to announce the prefix. See [Recognized ASNs](https://docs.cloud.google.com/data-transfer-essentials/docs/asn).
    * `CSP`: a string that represents the CSP of the ASN that is announcing the prefix.



###  API 

Use the [`multicloudDataTransferConfigs.destinations.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs.destinations/patch).
    
    
    PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME/destinations/DESTINATION_NAME
    {
      "description": "DESCRIPTION",
      "ip_prefix": "IP_PREFIX",
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
  * `DESTINATION_NAME`: the name of the destination.
  * `DESCRIPTION`: a description of the destination and its purpose.
  * `IP_PREFIX`: the IP prefix of the destination specified as a range (for example, `203.0.113.0/24` or `2001:db8::/32`) or a value (for example, `203.0.113.6` or `2001:db8:2:2:2:2:2:2`). An IP prefix must be used only once in a configuration and for only one ASN.

  * Specify strings corresponding to endpoints that you want to add to the destination or remove endpoints that you don't want to retain in the destination:

    * `ASN`: the ASN that is expected to announce the prefix. See [Recognized ASNs](https://docs.cloud.google.com/data-transfer-essentials/docs/asn).
    * `CSP`: a string that represents the CSP of the ASN that is announcing the prefix.



Additionally, to prevent a specified set of fields from being overwritten during an update operation, you can use the `updateMask` option, which follows the [fieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask) format.

Updates to Data Transfer Essentials destinations and the related configurations take effect in approximately 24 hours.

### Delete a destination

To delete a destination, use one of the following ways:

###  gcloud 

Use the [`gcloud network-connectivity multicloud-data-transfer-configs destinations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/destinations/delete).
    
    
    gcloud network-connectivity multicloud-data-transfer-configs destinations delete DESTINATION_NAME \
        --multicloud-data-transfer-config=CONFIGURATION_NAME \
        --location=LOCATION
    

###  API 

Use the [`multicloudDataTransferConfigs.destinations.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs.destinations/delete).
    
    
    DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/multicloudDataTransferConfigs/CONFIGURATION_NAME/destinations/DESTINATION_NAME
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
