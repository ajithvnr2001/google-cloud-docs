---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-aws-to-gcp/
title: Create a connection initiated from AWS using NCC \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:12.877360+00:00
---

# Create a connection initiated from AWS using NCC  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-aws-to-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Create a connection initiated from AWS using NCC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and provision a partner Cross-Cloud Interconnect for Amazon Web Services (AWS) connection from AWS using [Network Connectivity Center (NCC)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) if you already have an activation key.

Before you start the partner Cross-Cloud Interconnect for AWS provisioning process, ensure that the following conditions are met:

  * You already have an AWS account.
  * You [create an NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-hub), if it doesn't already exist, to connect your transport resource to.



If you want to initiate a connection from the AWS Console, see [Getting started with AWS Interconnect](https://docs.aws.amazon.com/interconnect/latest/userguide/getting-started.html) for creating the required resource. Provide the project and region information where you want the connection to land in Google Cloud. After AWS has created the resource, you must create the Google Cloud resource with the provided activation key.

To achieve a successful connection, you must create the `transport` resource. Follow the instructions on this page to create the transport.

## Considerations

Keep in mind the following considerations when using NCC to provision your partner Cross-Cloud Interconnect for AWS connection:

  * The default [connectivity topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies) for the configuration is mesh topology.
  * If you use [star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#star-topology), the hybrid spokes are added to the center group. Edge group isn't supported for partner Cross-Cloud Interconnect for AWS hybrid spokes.
  * Spokes are auto accepted into a project.
  * NCC supports up to 40 routing VPC networks, but you can add only one of those routing VPC networks as a spoke.
  * If you use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) connection propagation with partner Cross-Cloud Interconnect for AWS, you can't have any other hybrid spokes on that NCC hub. Conversely, if you want additional hybrid spokes connected to the hub, you can't enable Private Service Connect propagation.

For detailed information about Private Service Connect connection propagation using NCC, see [Private Service Connect connection propagation through NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview).




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
  * `networkconnectivity.transports.delete` to delete a transport
  * `networkconnectivity.groups.update` to update hubs and spoke groups



**Roles**

You need the following role to create transports and update hubs:

  * `roles/networkconnectivity.transportAdmin`



and at least one of the following roles:

  * `roles/networkconnectivity.groupAdmin`
  * `roles/networkconnectivity.hubAdmin`



### Create an NCC hub

If you haven't already, [create an NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-hub) to connect your `transport` resource to.

### Create the `transport` resource

**Note:** You cannot change the IP address version stack type of a `transport` resource after you have created it.

###  Console 

  1. In the Google Cloud console, go to the **Partner Cross-Cloud Interconnect** page.

[Go to Partner Cross-Cloud Interconnect](https://console.cloud.google.com/hybrid/transport)

  2. In the project menu, select a project.

  3. Click **Create transport**.

  4. Under **Connection start point** , click **Remote Cloud Service Provider (e.g. AWS)**.

  5. In the **Activation key** field, enter the activation key that you have from AWS.

  6. Click **Validate**. If you see an error message, make sure that the activation key that you have entered is accurate.

  7. After your key is validated, click **Continue**.

  8. (Optional) Under **Transport profile** , choose the transport in the region where you want to provision connectivity.

  9. In the **Remote ID** field, enter the ID of your AWS account.

  10. Click **Continue**.

  11. In the **Basic configuration** field, enter the following:

     * A **Transport name** for the transport resource that you want to create.
     * An optional **Description** for the transport resource.
     * (Optional) Choose the **Bandwidth** for your connection, such as `1G`. Make sure that the value matches the value selected when the key was created with AWS.
     * (Optional) Choose the **IP stack type**. You can only choose **IPv4**.
     * Choose the **Transport connectivity**.
  12. Click **Continue**.

  13. Under **Connection** , choose **Network Connectivity Center**.

  14. Under **Hub** , choose the hub name that you want to use. If you haven't created a hub, choose **Create hub**.

A new window with the **Create hub** workflow opens.

  15. Follow instructions to [Create a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-hub).

  16. Return to the **Create transport** window. Then choose the hub that you just created.

  17. To enable [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect), select **Enable Private Service Connect Routing**.

  18. Click **Create**.

  19. To verify your connection, click **View transport details**. The **Transport details** page shows the transport details and the connection status.




###  gcloud 

Use the [`gcloud network-connectivity transports create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/create). To enable [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect), use the optional `--psc-routing-enabled` flag.
    
    
    gcloud network-connectivity transports create TRANSPORT_NAME \
        --region=REGION \
        --remote-account-id=REMOTE_ACCOUNT_ID \
        --remote-profile=REMOTE_PROFILE_NAME \
        --bandwidth=BANDWIDTH \
        --hub=HUB_NAME \
        --advertised-routes=ADVERTISED_ROUTES \
        --stack-type=STACK_TYPE \
        --auto-accept
        [--psc-routing-enabled]
    

Replace the following values:

  * `TRANSPORT_NAME`: a name for the transport resource that you want to create
  * `REGION`: the name of the region where you want to provision connectivity, such as `us-west1`
  * `REMOTE_ACCOUNT_ID`: the ID of your AWS account
  * `REMOTE_PROFILE_NAME`: the AWS remote profile name associated with the Google Cloud region returned by the `gcloud network-connectivity transports remote-profiles list` command in the previous step
  * `BANDWIDTH`: the chosen bandwidth for your connection, such as `1G`. The bandwidth must be supported on the chosen `remoteProfile`.
  * `HUB_NAME`: the name of the NCC hub to connect the transport to
  * `ADVERTISED_ROUTES`: Additional IP addresses advertised to AWS. All routes learned in the hub's routing table are advertised to AWS
  * `STACK_TYPE` (optional): IP address version stack type. Must be `IPV4_ONLY`



###  API 

Use the [`networkconnectivity.transports.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.transports/create) specifying the `TRANSPORT_ID`, similar to the following example. To enable [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect), use the optional `"pscRoutingEnabled": "true"` in the body.
    
    
    curl -X POST \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json" \
       "https://networkconnectivity.googleapis.com/v1/projects/PROJECT/locations/REGION/transports?transportId="TRANSPORT_NAME"
       --data '{
    "hub": "HUB_NAME",
    "remoteProfile": "REMOTE_PROFILE_NAME",
    "bandwidth": "BANDWIDTH",
    "remoteAccountId": "REMOTE_ACCOUNT_ID",
    "advertisedRoutes": ["ADVERTISED_ROUTES"],
    "stackType": "STACK_TYPE",
    "autoAccept": "true"
    "pscRoutingEnabled": "true"
    }'
    

Replace the following values:

  * `PROJECT`: the name of the project in which you want to create the transport
  * `REGION`: the name of the Google Cloud region where you want to provision connectivity, such as `us-west1`
  * `TRANSPORT_NAME`: a name for the transport resource
  * `REMOTE_ACCOUNT_ID`: the ID of your AWS account
  * `REMOTE_PROFILE_NAME`: the AWS remote profile name associated with the Google Cloud region returned by the `gcloud network-connectivity transports remote-profiles list` command in the previous step
  * `BANDWIDTH`: the chosen bandwidth for your connection, such as `1G`, must be a supported bandwidth on the chosen `remoteProfile`
  * `HUB_NAME`: the name of the NCC hub to connect the transport to
  * `ADVERTISED_ROUTES`: Additional IP addresses advertised to AWS. All routes learned in the hub's routing table are advertised to AWS
  * `STACK_TYPE` (optional): IP address version stack type. Must be `IPV4_ONLY`



### Verify your connection

You can verify that connectivity has been established by listing spokes attached to the hub that you created. You can also list NCC routes for your hub.

###  gcloud 

To list spokes associated with a hub across all projects use the [`gcloud network-connectivity hubs list-spokes` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/list-spokes).
    
    
    gcloud network-connectivity hubs list-spokes HUB_NAME
    

Replace `HUB_NAME` with the name of the hub for which you want to list spokes, such as `my-hub`.

To list NCC routes for a hub, run the [`gcloud network-connectivity hubs route-tables routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list).
    
    
    gcloud network-connectivity hubs route-tables routes list \
        --hub=HUB_NAME \
        --route_table=default
    

Replace `HUB_NAME` with the name of the hub, such as `my-hub`.

Your output looks similar to the following:
    
    
    IP_CIDR_RANGE  PRIORITY  LOCATION   STATE   TYPE           SITE_TO_SITE  NEXT_HOP                                     HUB          ROUTE_TABLE
    10.0.0.0/9     65536     us-east1   ACTIVE  DYNAMIC_ROUTE  OFF           transport-c24daa3d1fa6969a-7a3f13c5553ee9a0  HUB_NAME     default
    

###  API 

To list all spokes associated with a hub across all projects, use the [`networkconnectivity.hubs.listSpokes` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:listSpokes
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the hub
  * `HUB_NAME`: the name of the hub for which you want to list spokes



To list NCC routes for a hub, use the [`networkconnectivity.hubs.routeTables.routes.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes/list) with an empty request body.
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME/routeTables/NAME/routes
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the hub
  * `HUB_NAME`: the name of the hub
  * `NAME`: the name of the hub route table resource



## What's next

  * To find answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).
  * To find out more about Cloud Interconnect, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).
  * To find Google Cloud resource names, see the [Cloud Interconnect APIs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/reference/apis). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
