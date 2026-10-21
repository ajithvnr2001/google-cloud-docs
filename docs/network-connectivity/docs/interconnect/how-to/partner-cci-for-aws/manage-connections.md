---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/manage-connections/
title: Manage connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:12.529958+00:00
---

# Manage connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/manage-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Manage connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view, update, and delete partner Cross-Cloud Interconnect for Amazon Web Services (AWS) connections. To view, update, or delete a connection, use the `transport` resource.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.remoteTransportProfiles.get` to get transport profiles
  * `networkconnectivity.remoteTransportProfiles.list` to list transport profiles
  * `networkconnectivity.transports.get` to view transports
  * `networkconnectivity.transports.list` to view transports
  * `networkconnectivity.transports.update` to update a transport
  * `Networkconnectivity.transports.delete` to delete a transport



**Roles** (one of the following)

  * `roles/networkconnectivity.transportAdmin` to create a transport
  * `roles/compute.networkAdmin` to create a transport
  * `roles/networkconnectivity.transportViewer` to view a transport



## View connections

To view connections, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Partner Cross-Cloud Interconnect** page.

[Go to Partner Cross-Cloud Interconnect](https://console.cloud.google.com/hybrid/transport)

  2. In the project menu, select your project.

The **Transports** page lists the transport resources in the project.

  3. To view details of a specific transport, click the name of the transport that you want to view details for.




###  gcloud 

Use the [`gcloud network-connectivity transports list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/list).
    
    
    gcloud network-connectivity transports list \
        --region=LOCATION
    

Your output is similar to the following:
    
    
    gcloud network-connectivity transport list --region us-east4
    
    | Name              | Profile              | Bandwidth | State  |
    |===================|======================|===========|========|
    | my-cci-aws        | aws-us-east-1        | 1 Gb/s    | Active |
    | my-cci-aws-123456 | aws-us-east-1        | 1 Gb/s    | Active |
    

Replace the following values:

  * `TRANSPORT_NAME`: the name of the transport for which you want to view details
  * `LOCATION`: the location where the connection resides



To get details of a single transport, use the [`gcloud network-connectivity transports describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/describe).
    
    
    gcloud network-connectivity transports describe TRANSPORT_NAME \
        --region=LOCATION
    

Replace the following values:

  * `TRANSPORT_NAME`: the name of the transport for which you want to view details
  * `LOCATION`: the location where the connection resides



###  API 

To list all the transports in a specific project and location, use the [`networkconnectivity.transports.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.transports/list) with an empty request body.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://networkconnectivity.googleapis.com/v1/projects/PROJECT/locations/LOCATION/transports"
    

Replace the following values:

  * `PROJECT`: the name of the project
  * `LOCATION`: the location where the connection resides



To get details of a single transport, use the [`networkconnectivity.transports.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.transports/get).
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://networkconnectivity.googleapis.com/v1/projects/PROJECT/locations/LOCATION/transports/TRANSPORT_NAME"
    

Replace the following values:

  * `PROJECT`: the name of the project
  * `LOCATION`: the location where the connection resides
  * `TRANSPORT_NAME`: the name of the transport for which you want to view details



## Update connections

You can update the following two parameters of the transport resource:

  * `description`
  * `advertisedRoutes`
  * `stackType`
  * `bandwidth` (if the profile supports the new bandwidth)

**Note:** You can only update the transport bandwidth if the transport speed is 1 Gbps or higher. Bandwidth updates to or from the 500 Mbps speed aren't supported.

Changing the advertised routes changes the routes reachable from AWS. You must provide the updated fields in a mask on the query parameter.

###  Console 

  1. In the Google Cloud console, go to the **Partner Cross-Cloud Interconnect** page.

[Go to Partner Cross-Cloud Interconnect](https://console.cloud.google.com/hybrid/transport)

  2. In the project menu, select your project.

The **Transports** page lists the transport resources in the project.

  3. Next to the transport that you want to update, click more_vert**View instructions**.

  4. Click **Edit transport**.

  5. Update the **Description** or the **Advertised routes** as needed.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud network-connectivity transports update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/update).
    
    
    gcloud network-connectivity transports update "TRANSPORT_NAME" \
        --region=LOCATION \
        --advertised-routes=ADVERTISED_ROUTES \
        [--description=DESCRIPTION] \
        --format json
    

Replace the following values:

  * `TRANSPORT_NAME`: the name of the transport that you want to update
  * `LOCATION`: the location where the connection resides
  * `ADVERTISED_ROUTES`: a comma-separated list of advertised routes of the transport resource
  * `DESCRIPTION`: an optional description of the transport resource



###  API 

Use the [`networkconnectivity.transports.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.transports/patch).
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://networkconnectivity.googleapis.com/v1/projects/PROJECT/locations/LOCATION/transports/TRANSPORT_NAME" --data '{
    "advertisedRoutes": ["IP_RANGE"]
    }'
    

Replace the following values:

  * `PROJECT`: the name of the project
  * `LOCATION`: the location where the connection resides
  * `TRANSPORT_NAME`: the name of the transport that you want to update
  * `IP_RANGE`: the IP range of the advertised routes, such as `10.128.0.0/9`



The response looks similar to the following: 
    
    
    {
      {
          "advertisedRoutes": [
           "10.128.0.0/9"
          ],
          "description": NEW_DESCRIPTION,
          "updateTime": TIME
      }
    }
    

## Delete connections

Deleting a transport doesn't delete your resource on the AWS side, so make sure to clean up both sides of the connection.

###  Console 

  1. In the Google Cloud console, go to the **Partner Cross-Cloud Interconnect** page.

[Go to Partner Cross-Cloud Interconnect](https://console.cloud.google.com/hybrid/transport)

  2. In the project menu, select your project.

The **Transports** page lists the transport resources in the project.

  3. Click the transport resource that you want to delete.

  4. Click delete**Delete**.




###  gcloud 

Use the [`gcloud network-connectivity transports delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/delete).
    
    
    gcloud network-connectivity transports delete TRANSPORT_NAME \
        --region=LOCATION
    

Replace the following values:

  * `TRANSPORT_NAME`: the name of the transport that you want to delete
  * `LOCATION`: the location where the transport resides



###  API 

To delete a single transport, use the [`networkconnectivity.transports.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.transports/delete) with an empty request body.
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    https://networkconnectivity.googleapis.com/v1/projects/PROJECT/locations/LOCATION/transports/TRANSPORT_NAME
    

Replace the following values:

  * `PROJECT`: the name of the project
  * `LOCATION`: the location where the connection resides
  * `TRANSPORT_NAME`: the name of the transport that you want to delete



## What's next

  * To find answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).
  * To find out more about Cloud Interconnect, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).
  * To find Google Cloud resource names, see the [Cloud Interconnect APIs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/reference/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
