---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-aws-to-gcp/
title: Create a connection initiated from AWS with VPC Network Peering \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:49.326299+00:00
---

# Create a connection initiated from AWS with VPC Network Peering  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-aws-to-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Create a connection initiated from AWS with VPC Network Peering Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to successfully create and provision a partner Cross-Cloud Interconnect for Amazon Web Services (AWS) connection from AWS if you already have an activation key.

If you want to initiate a connection from the AWS Console, see [Getting started with AWS Interconnect](https://docs.aws.amazon.com/interconnect/latest/userguide/getting-started.html) for creating the required resource. Provide the project and region information where you want the connection to land in Google Cloud. After AWS has created the resource, you must create the Google Cloud resource with the provided activation key.

Connecting with VPC Network Peering doesn't let you access Google APIs through Private Service Connect.

## Configuration requirements

Before you start the partner Cross-Cloud Interconnect for AWS provisioning process, ensure that the following conditions are met:

  * You must already have an AWS account.
  * You must also [create a Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks), if it doesn't already exist, to connect your transport resource to.



To achieve a successful connection, you must create the `transport` resource. Follow these instructions to create the transport.

## Before you begin

Before you get started, review the following sections.

### Create or select a project

To make it easier to configure partner Cross-Cloud Interconnect for AWS, start by identifying a valid project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. If you are using the Google Cloud CLI, set your project ID by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
         
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your unique project ID.

The gcloud CLI instructions on this page assume that you have set your project ID. 

  13. To confirm that you set the project ID correctly, use the [`gcloud config list` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/list).
         
         gcloud config list --format='text(core.project)'




### Enable the Network Connectivity API

Before you can perform _any_ tasks using partner Cross-Cloud Interconnect for AWS, you must enable the Network Connectivity API.

###  Console

To enable the Network Connectivity API, do the following:

  1. In the Google Cloud console, go to the **Network Connectivity API** page.

[Go to Network Connectivity API](https://console.cloud.google.com/marketplace/product/google/networkconnectivity.googleapis.com)

  2. Click **Enable**.




Alternatively, you can enable the API by using the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_), as described in [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

## Initiate a connection from AWS with an AWS activation key

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.remoteTransportProfiles.get` to get transport profiles
  * `networkconnectivity.remoteTransportProfiles.list` to list transport profiles
  * `networkconnectivity.transports.get` to view transports
  * `networkconnectivity.transports.list` to view transports
  * `networkconnectivity.transports.create` to create a transport
  * `networkconnectivity.transports.update` to update a transport
  * `Networkconnectivity.transports.delete` to delete a transport
  * `compute.networks.use` to establish VPC Network Peering
  * `compute.networks.addPeering` to establish VPC Network Peering



**Roles**

You need the following roles to create a transport resource:

  * `roles/networkconnectivity.transportAdmin` to create a transport
  * `roles/compute.networkAdmin` to create a transport



### Create the `transport` resource

###  Console 

  1. In the Google Cloud console, go to the **Partner Cross-Cloud Interconnect** page.

[Go to Partner Cross-Cloud Interconnect](https://console.cloud.google.com/hybrid/transport)

  2. In the project menu, select a project.

  3. Click **Create transport**.

  4. Under **Connection start point** , click **Remote Cloud Service Provider (e.g. AWS)**.

  5. In the **Activation key** field, enter the activation key that you have from AWS.

  6. Click **Validate**. If you see an error message, make sure that the activation key that you have entered is accurate.

  7. After your key is validated, click **Continue**.

  8. Under **Transport profile** , choose the transport in the region where you want to provision connectivity.

  9. In the **Remote ID** field, enter the account ID of your AWS account.

  10. Click **Continue**.

  11. In the **Basic configuration** field, enter the following:

     * A **Transport name** for the transport resource that you want to create.
     * An optional **Description** for the transport resource.
     * (Optional) Choose the **Bandwidth** for your connection, such as `1G`. Make sure that the value matches the value selected when the key was created with AWS.
     * (Optional) Choose the **IP stack type**. By default, **IPv4** is selected.
     * Choose the **Transport connectivity**.
  12. Click **Continue**.

  13. Under **Connection** , choose the name of your VPC network.

  14. In the **Advertised routes** field, enter a comma-separated list of the IP addresses for the Google Cloud VPC network's routes to be advertised to AWS.

  15. Click **Create**.

  16. To verify your connection, click **View transport details**. The **Transport details** page shows the transport details and the connection status.




###  gcloud 

Use the [`gcloud network-connectivity transports create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/create):
    
    
    gcloud network-connectivity transports create TRANSPORT_NAME \
        --region=REGION \
        --activation-key=ACTIVATION_KEY \
        --network=NETWORK \
        --advertised-routes=ADVERTISED_ROUTES \
        --stack-type=STACK_TYPE
    

Replace the following values:

  * `TRANSPORT_NAME`: a name for the transport resource that you want to create
  * `LOCATION`: the name of the region where you want to provision connectivity, such as, `us-west1`
  * `ACTIVATION_KEY`: the activation key that you have received from AWS
  * `NETWORK`: the name of your VPC network
  * `ADVERTISED_ROUTE`: IP addresses for the Google Cloud VPC network's routes to be advertised to AWS.
  * `STACK_TYPE` (optional): IP address version stack type. Must be `IPV4_ONLY` or `IPV4_IPV6`. Defaults to `IPV4_ONLY`



###  API 

Use the [`networkconnectivity.transports.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.transports/create) specifying the `TRANSPORT_ID`, similar to the following example:
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" "https://networkconnectivity.googleapis.com/v1/projects/PROJECT/locations/REGION/transports?transportId="TRANSPORT_NAME" --data '{
    "network": "NETWORK",
    "remoteProfile": "REMOTE_PROFILE_NAME",
    "bandwidth": "BANDWIDTH",
    "remoteAccountId": "REMOTE_ACCOUNT_ID",
    "advertisedRoutes": ["ADVERTISED_ROUTE"],
    "stackType": "STACK_TYPE"
    }'
    

Replace the following values:

  * `PROJECT`: the name of the project in which you want to create the transport.
  * `REGION`: the name of the Google Cloud region where you want to provision connectivity, such as `us-west1`.
  * `TRANSPORT_NAME`: a name for the transport resource.
  * `REMOTE_ACCOUNT_ID`: the ID of the remote provider's account.
  * `REMOTE_PROFILE_NAME`: the provider's remote profile name associated with the Google Cloud region returned by the `gcloud network-connectivity transports remote-profiles list` command in the previous step.
  * `BANDWIDTH`: the chosen bandwidth for your connection, such as `1G`, must be a supported bandwidth on the chosen `remoteProfile`.
  * `NETWORK`: the name of your VPC network.
  * `ADVERTISED_ROUTE`: IP addresses for the Google Cloud VPC network's routes to be advertised to the provider.
  * `STACK_TYPE` (optional): IP address version stack type. Must be `IPV4_ONLY` or `IPV4_IPV6`. Defaults to `IPV4_ONLY`.



### Retrieve the peering network name

After you create the `transport` resource, retrieve the name of the peering network it is attached to. The name of the peering network is used to establish VPC Network Peering.

To view the peering network name, do the following:

###  gcloud 

Use the [`network-connectivity transports describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/describe).
    
    
    gcloud network-connectivity transports describe "TRANSPORT_NAME"
    

Replace `TRANSPORT_NAME` with the name of the transport that you created.

If the command is successful, copy the output's `peeringNetwork` field to use when establishing VPC Network Peering.

###  API 

Use the [`networkconnectivity.transports.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.transports/get):
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT/locations/LOCATION/transport/TRANSPORT_NAME
    

Replace the following values:

  * `PROJECT`: the name of the project that you created the transport resource in
  * `LOCATION`: the name of the Google Cloud region where you want to provision connectivity, such as, `us-west1`
  * `TRANSPORT_NAME`: the name of the transport that you created



### Establish VPC Network Peering

You can proactively establish VPC Network Peering at the Google Cloud end. To do this, use the `peeringNetwork` resource and ensure that you create a peering with the same stack type. The default stack type matches the `transport` resource using `IPV4_ONLY`.

To receive the AWS routes, you must enable the `Import custom routes` field.

The MTU in the peering VPC network is explicitly set to the maximum in order to avoid MTU issues in the connectivity. If you're using an MTU less than 8896, you might get a warning `WARNING: Some requests generated warnings: - Network MTU 1460B does not match the peer's MTU 8896B`. In that case, you must ensure that you're using matching MTU configurations between your Google Cloud VPC network and the AWS VPC network. If these are mismatched, you might need to override MTU values to the lowest common denominator. For example, if you're using 8896 in Google Cloud and 8800 in AWS, everything in Google Cloud must be configured as 8800.

###  gcloud 

To establish VPC Network Peering, use the [`gcloud compute networks peerings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create).
    
    
    gcloud compute networks peerings create "TRANSPORT_NAME" \
        --network="VPC_NETWORK" \
        --peer-network="PEERING_NETWORK" \
        --stack-type=STACK_TYPE \
        --import-custom-routes \
        --export-custom-routes
    

Replace the following values:

  * `TRANSPORT_NAME`: the name of the transport that you created
  * `VPC_NETWORK`: the name of the VPC network that you want to list the routes for
  * `PEERING_NETWORK`: the name of the VPC network provided by the `Transport` resource
  * `STACK_TYPE`: IP address version stack type. Must be `IPV4_ONLY` or `IPV4_IPV6`. Defaults to `IPV4_ONLY`



If the command is successful, the output's `state` field has the value `ACTIVE`.

###  API 

To establish VPC Network Peering, use the [`compute.networks.addPeering` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/addPeering).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/global/networks/NETWORK/addPeering
    

Replace the following values:

  * `PROJECT`: the name of the project that you are peering
  * `NETWORK`: the name of the network resource to add peering to



### Verify your connection

You can verify that connectivity has been established by listing the peered VPC networks and the route tables. After the AWS configuration is complete, you can see your AWS routes in the list.

###  Console 

  1. In the Google Cloud console, go to the **Partner Cross-Cloud Interconnect** page.

[Go to Partner Cross-Cloud Interconnect](https://console.cloud.google.com/hybrid/transport)

  2. In the project menu, select your project.

  3. On the **Transports** page, click the transport that you just created.

  4. The **Transport details** page shows the transport details and the connection status.




###  gcloud 

To list the peered VPC networks, use the [`gcloud compute networks peerings list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list).
    
    
    gcloud compute networks peerings list
    

The output is similar to the following:
    
    
    NAME           NETWORK  PEER_PROJECT           PEER_NETWORK                   STACK_TYPE  PEER_MTU  IMPORT_CUSTOM_ROUTES  EXPORT_CUSTOM_ROUTES  UPDATE_STRATEGY  STATE   STATE_DETAILS
    cci-virginia  cci      ke526b767340356b7p-tp  transport-b52816f13d929baf-vpc  IPV4_ONLY   8896      True                  True                  INDEPENDENT      ACTIVE  [2026-01-22T07:20:58.891-08:00]: Connected.
    

To list routes for a specific transport, use the [`gcloud compute networks peerings list-routes` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes).
    
    
    gcloud compute networks peerings list-routes TRANSPORT_NAME \
        --direction=INCOMING \
        --network=NETWORK \
        --region=REGION
    

Replace the following values:

  * `TRANSPORT_NAME`: the name of the transport resource
  * `NETWORK`: the name of the VPC network that you want to list the route tables for
  * `REGION`: the region of the transport resource



The output is similar to the following:
    
    
    DEST_RANGE   TYPE                   NEXT_HOP_REGION  PRIORITY  STATUS
    10.0.0.0/16  DYNAMIC_PEERING_ROUTE  us-east4         0         accepted
    

###  API 

To list peered networks, use the [`compute.networks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/global/networks
    

Replace `PROJECT` with the name of the project that you want to list the networks for.

To list routes, use the [`compute.routes.listPeeringRoutes` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/list)
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/global/networks/NETWORK/listPeeringRoutes
    

Replace the following values:

  * `PROJECT` with the name of the project that you want to list the routes for
  * `NETWORK`: the name of the VPC network that you want to list the route tables for



## What's next

  * To find answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).
  * To find out more about Cloud Interconnect, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).
  * To find Google Cloud resource names, see the [Cloud Interconnect APIs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/reference/apis). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
