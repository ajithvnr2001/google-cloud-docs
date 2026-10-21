---
url: https://docs.cloud.google.com/vpc/docs/about-peering-connections/
title: About peering connections \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:12.678642+00:00
---

# About peering connections  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-peering-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About peering connections

This page provides an overview of administering VPC Network Peering connections.

## Peering connection

A _peering connection_ connects two Virtual Private Cloud (VPC) networks. To establish a peering connection, each side separately creates a _peering configuration_ that references the other network.

You initiate the request to connect to another VPC network by creating a peering configuration. After the other network has a corresponding configuration to peer with your network, the peering connection is established and the peering state is changed to `ACTIVE` in both networks. The peering state remains `INACTIVE` if the other network doesn't have a matching peering configuration, indicating that your network isn't connected to the other one.

Creating a peering connection doesn't grant you any Identity and Access Management roles on the other VPC network. For example, if you have the Compute Network Admin role (`roles/compute.networkAdmin`) or the Compute Security Admin role (`roles/compute.securityAdmin`) for one network, you don't become a network administrator or a security administrator for the other network.

After the peering connection is established, the two VPC networks always exchange IPv4 subnet routes that use private IPv4 address ranges. For more information about route exchange options, see the following:

  * [Options for exchanging subnet routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#subnet-route-exchange)
  * [Options for exchanging static routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#static-route-exchange)
  * [Options for exchanging dynamic routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#dynamic-route-exchange)



## Connection mode

The _connection mode_ determines how a peering connection is administered. VPC Network Peering supports two connection modes:

  * Independent mode (default)
  * Consensus mode



For standard deployments, independent mode is generally preferred. However, for deployments supporting a critical service where accidental deletion of the peering connection would cause a service outage, we recommend using consensus mode. This mode requires agreement from both networks and prevents unilateral changes to the effective status of the peering connection.

When creating a peering connection, both peering configurations must specify the same connection mode: either independent or consensus.

To change the peering mode of an existing connection from independent to consensus, both peering configurations must be updated. Changing the connection mode from consensus to independent isn't supported.

### Independent mode

When a peering connection is in independent mode (default), either network can update or delete the connection at any time. You can optionally restrict this behavior by updating the connection mode to consensus.

### Consensus mode

Consensus mode prevents accidental, unilateral changes to network behavior. When a peering connection is in consensus mode, every request to update or delete the peering connection requires agreement from both networks.

#### Configure consensus mode for a connection

You can configure a new or existing peering connection to use consensus mode by setting the `update_strategy` parameter:

  * **New connection**. Both networks must set the update strategy to `CONSENSUS`. If the update strategy isn't specified, the connection is created in independent mode.
  * **Existing connection**. Both networks must change the update strategy to `CONSENSUS`. Until both values match, the effective update strategy remains `INDEPENDENT` and unilateral update and deletion requests are permitted.

Pending requests to update the connection mode don't cause downtime, and the connection remains active while the request is in progress.




Additionally, to configure consensus mode for a connection, each [route exchange option](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options) in your configuration must have the same value as the complementary flag in the peer configuration. If the values for the following flags don't match, the request to create or update the connection is rejected.

Local flag | Complementary peer flag  
---|---  
`import_custom_route` | `export_custom_route`  
`export_custom_route` | `import_custom_route`  
`import_subnet_routes_with_public_ip` | `export_subnet_routes_with_public_ip`  
`export_subnet_routes_with_public_ip` | `import_subnet_routes_with_public_ip`  
`stack_type` | `stack_type`  
  
For example, if your network imports custom routes, the peer network must export custom routes. If any of these values don't match for an existing connection, either network can update them before or when changing the connection mode.

To cancel a pending request to configure consensus mode for an existing connection, the requesting network must reset the update strategy to `INDEPENDENT`.

For more information, see [Create a peering connection in consensus mode](https://docs.cloud.google.com/vpc/docs/using-vpc-peering?tab=gcloud#create-consensus-mode) and [Update a connection to consensus   
mode](https://docs.cloud.google.com/vpc/docs/using-vpc-peering?tab=gcloud#change-update-strategy).

#### Update a connection in consensus mode

Either side of a peering connection can submit an update request. A pending update request doesn't cause downtime, and the connection remains active. If a deletion request is in progress, all update requests (including accepting or canceling a pending update request) are rejected.

To update a peering connection configured with consensus mode, the local network administrator first updates the local configuration. Then, the peer network administrator must make a complementary update to the peer configuration. For example, if you update the `--export-custom-routes` flag to `true`, the peer network must set the `--import-custom-routes` flag to `true`. The effective status of the peering connection doesn't change until the peer network updates the corresponding configuration.

After the local peering configuration is updated, neither side of the connection can submit further update requests until the initial update is accepted or canceled. Partial updates aren't supported—if a request updates multiple parameters, all of them must be accepted or canceled. To cancel an update, the the requesting network resets each modified parameter to its previous value.

The following diagram shows how the status of a peering connection changes when an update request is submitted.

[ ![Updating a peering connection in consensus mode](https://docs.cloud.google.com/static/vpc/images/peering/consensus-update.svg)](https://docs.cloud.google.com/static/vpc/images/peering/consensus-update.svg) Updating a peering connection in consensus mode (click to enlarge).

In the preceding diagram, after network A submits the update request, the update status of the connection changes from `IN_SYNC` to `PENDING_PEER_ACKNOWLEDGMENT` in the local configuration and to `PENDING_LOCAL_ACKNOWLEDGMENT` in the peer configuration.

To return to the `IN_SYNC` status, network B must make the complementary change or network A must cancel its request. For more information about these connection statuses, see Connection status.

To update a peering connection, see [Update a connection (consensus mode)](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-consensus).

#### Delete a connection in consensus mode

To delete a peering connection in consensus mode, both sides of the connection must submit a deletion request. You can [cancel a deletion request](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#cancel-delete) either before or after it is accepted by the peer network.

The following conditions apply to deletion requests:

  * If an update request is pending, you can still delete the peering connection.
  * If a deletion request is pending, all update requests, including accepting or canceling a pending update, are rejected. To complete a pending update, you must first cancel the deletion request.



For more information, see [Delete a connection (consensus mode)](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#delete-consensus).

## Connection status

The [`gcloud compute networks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/describe) shows both the effective status of a peering connection and your local peering configuration.

You can view the effective connection status by examining the `peerings.connectionStatus` field. The following table describes its available configuration statuses. The checkmark indicates that the field is available.

Field | Independent mode | Consensus mode | Description  
---|---|---|---  
`trafficConfiguration` |  |  | Shows the effective [route exchange options](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options) of the peering connection.  
`updateStrategy` |  |  | Shows the effective connection mode: either `INDEPENDENT` or `CONSENSUS`.  
`consensusState.deleteStatus` |  |  | 

  * `UNSPECIFIED`: no `requestRemovePeering` requests are pending for this peering connection. The `deleteStatus` field doesn't appear in the output when the status is `UNSPECIFIED`.
  * `LOCAL_DELETE_REQUESTED`: the owner of this peering has requested the deletion of the peering connection.
  * `PEER_DELETE_REQUESTED`: the owner of the matching peering has requested the deletion of the peering connection.
  * `DELETE_ACKNOWLEDGED`: both peering owners of this connection have requested the deletion of the peering connection. Subsequent `removePeering` requests will succeed for either peering.
  * `LOCAL_CANCEL_REQUESTED`: the peering connection was in the `DELETE_ACKNOWLEDGED` state, but the local network has canceled the deletion.
  * `PEER_CANCEL_REQUESTED`: the peering connection was in the `DELETE_ACKNOWLEDGED` state, but the peer network has canceled the deletion.

  
`consensusState.updateStatus` |  |  | 

  * `IN_SYNC`: neither peering owner has pending updates.
  * `PENDING_PEER_ACKNOWLEDGMENT`: the local peering owner has made a change but the matching peering owner hasn't applied the corresponding changes to their peering.
  * `PENDING_LOCAL_ACKNOWLEDGMENT`: the matching peering owner has made a change but the local peering owner hasn't applied the corresponding changes to this peering.

  
  
To list all peering configurations in a Google Cloud project, see [List peering connections](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#list-peer-connections).

## What's next

  * To create and manage VPC Network Peering connections, see [Set up and manage VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
