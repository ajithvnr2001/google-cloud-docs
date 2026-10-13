---
url: https://docs.cloud.google.com/vpc/docs/using-vpc-peering/
title: Set up and manage VPC Network Peering \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:53.208323+00:00
---

# Set up and manage VPC Network Peering  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/using-vpc-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up and manage VPC Network Peering

Google Cloud VPC Network Peering enables [internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) connectivity across two Virtual Private Cloud (VPC) networks, regardless of whether they belong to the same Google Cloud project or organization. Peering supports connectivity between networks having any combination of IPv4-only, dual-stack, and IPv6-only subnets.

## Before you begin

  * Read [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) and [About peering connections](https://docs.cloud.google.com/vpc/docs/about-peering-connections).
  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the Compute Engine API in your project.



### IAM permissions

Make sure that you have one of the following roles on the project:

  * [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * A custom role that includes the following permissions: 
    * `compute.networks.addPeering`
    * `compute.networks.updatePeering`
    * `compute.networks.removePeering`
    * `compute.networks.listPeeringRoutes`



## Create a peering configuration

Before you begin, you must have the name of the VPC network that you intend to peer with. If that network is located in another project, you must also have its project ID. You can't list peering requests for your VPC network. If necessary, ask the administrator of the network that you intend to peer with for the network name and project ID.

Your network and the other network are connected after each network has a peering configuration that references the other network. For more information, see [About peering connections](https://docs.cloud.google.com/vpc/docs/about-peering-connections#peering-connection).

Google Cloud allows only one peering operation at a time across peered networks. For example, if you set up peering with one network and immediately try to set up another, the operation fails with the following: `Error: There is a peering operation in progress on the local or peer network. Try again later.`

###  Console 

Perform the following steps for each side of the peering connection.

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click **Create connection**.

  3. Click **Continue**.

  4. In the **Peering connection name** field, enter a name for your peering configuration.

  5. In the **Your VPC network** field, select a network you want to peer.

  6. In the **Peered VPC network** section, select the network to peer with:

     * If the network that you want to peer with is in the same project, select **In project [name-of-your-project]** and then the network to peer with.
     * If the network that you want to peer with is in a different project, select **In another project**. Specify the project ID that includes the network you want to peer with and the name of the VPC network.
  7. Select the IP version of routes that you want to exchange between the peered networks:

     * **IPv4 (single-stack)** : exchange IPv4 routes only. The peer network must also enable this option.
     * **IPv4 and IPv6 (dual-stack)** : exchange both IPv4 and IPv6 routes. The peer network must also enable this option.
  8. To exchange IPv4 custom routes, in the **Exchange IPv4 custom routes** section, choose one or both of the following options:

     * **Import custom routes** : import custom routes from the peer network. The peer network must enable custom route export for routes to be imported.
     * **Export custom routes** : export custom routes to the peer network. The peer network must enable custom route import for routes to be exported.
  9. If your network or the peer network has privately used public IPv4 ranges in their subnets, these routes are exported by default, but not imported by default.

To import privately used public IPv4 subnet routes, in the **Exchange subnet routes with privately used public IPv4 addresses** section, select **Import subnet routes with public IP**.

  10. In **Advanced options** section, choose the update strategy for the peering connection:

     * **Independent (default)** : when this option is selected, either side of the connection can update or delete the connection at any time. For more information, see [Connection mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-mode).
     * **Consensus** : when this option is selected, updating or deleting the connection requires acknowledgment from the peer network. For more information, see [Connection mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-mode).
  11. Click **Create**.




###  gcloud 

Use the [`gcloud compute networks peerings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create).

You can create a peering configuration using the default configuration, or you can customize your configuration.

#### Create a default peering configuration

To create a default peering configuration, run the following command:
    
    
    gcloud compute networks peerings create PEERING_NAME \
        --network=NETWORK \
        --peer-project=PEER_PROJECT_ID \
        --peer-network=PEER_NETWORK_NAME
    

Replace the following:

  * `PEERING_NAME`: the name of the peering configuration
  * `NETWORK`: the name of the network in your project that you want to peer
  * `PEER_PROJECT_ID`: the ID of the project that contains the network that you want to peer with

If the peer network is in the same project as your network, this flag is optional.

  * `PEER_NETWORK_NAME`: the name of the network that you want to peer with




For example, to peer `network-a` in `project-a` with `network-b` in `project-b`, do the following:

  1. Create a peering configuration for `network-a`.
         
         gcloud compute networks peerings create peering-a \
             --network=network-a \
             --peer-project=project-b \
             --peer-network=network-b
         

  2. Create the corresponding peering configuration for `network-b`. This step is usually performed by a network administrator for `network-b`.
         
         gcloud compute networks peerings create peering-b \
             --network=network-b \
             --peer-project=project-a \
             --peer-network=network-a
         




The peering state changes to `ACTIVE` in both networks.

#### Customize a peering configuration

To customize a peering configuration, you can use the following optional parameters:

  * `--stack-type` sets the stack type for the peering connection. By default, only IPv4 routes are exchanged, and the stack type is set to `IPV4_ONLY`. To exchange both IPv4 and IPv6 routes, specify `IPV4_IPV6` for both sides of the connection.
  * `--import-custom-routes` tells the network to accept [custom routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) from the peered network. The peered network must export the routes first.
  * `--export-custom-routes` tells the network to export [custom routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) to the peered network. The peered network must be set to import the routes.
  * `--import-subnet-routes-with-public-ip` tells the network to accept subnet routes from the peered network if that network has [privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) in its subnets. The peered network must export the routes first.
  * `--export-subnet-routes-with-public-ip` tells the network to export subnet routes that contain [privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). The peered network must be set to import the routes.
  * `--update-strategy` sets the update strategy for the peering connection. By default, the update strategy is `INDEPENDENT`. To configure the connection to use consensus mode, specify `CONSENSUS` for both sides of the connection. For more information, see [Connection mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-mode).



##### Example: Exchange custom routes in a peering connection

To enable `network-a` in `project-a` and `network-b` in `project-b` to exchange custom routes, do the following when creating the peering connection:

  1. Create a peering configuration for `network-a`.
         
         gcloud compute networks peerings create peering-a \
             --network=network-a \
             --peer-project=project-b \
             --peer-network=network-b \
             --import-custom-routes \
             --export-custom-routes
         

  2. Create the corresponding peering configuration for `network-b`. This step is usually performed by a network administrator for `network-b`.
         
         gcloud compute networks peerings create peering-b \
             --network=network-b \
             --peer-project=project-a \
             --peer-network=network-a \
             --import-custom-routes \
             --export-custom-routes
         




The peering state changes to `ACTIVE` in both networks. For more information about this example, see the [Peer two VPC networks](https://docs.cloud.google.com/vpc/docs/peer-two-networks) quickstart.

##### Example: Create a peering connection in consensus mode

To create a peering connection in consensus mode, set the update strategy to `CONSENSUS`. In this example, you configure `network-a` in `project-a` to peer with `network-b` in `project-b`.

  1. Create a peering configuration for `network-a`.
         
         gcloud compute networks peerings create peering-a \
             --network=network-a \
             --peer-project=project-b \
             --peer-network=network-b \
             --update-strategy=CONSENSUS
         

  2. Create the corresponding peering configuration for `network-b`. This step is usually performed by a network administrator for `network-b`.
         
         gcloud compute networks peerings create peering-b \
             --network=network-b \
             --peer-project=project-a \
             --peer-network=network-a \
             --update-strategy=CONSENSUS
         




The peering state changes to `ACTIVE` in both networks.

### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-network) to create a peering configuration.
    
    
    module "peering1" {
      source        = "terraform-google-modules/network/google//modules/network-peering"
      version       = "~> 18.0"
      local_network = var.local_network # Replace with self link to VPC network "foobar" in quotes
      peer_network  = var.peer_network  # Replace with self link to VPC network "other" in quotes
    }

For the two peered VPC networks, each self link includes a project ID and the name of the VPC network. To get the self link for a VPC network, you can use the [`gcloud compute networks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/describe) command or the [`networks.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/get) method in each VPC network's project.

When you create a peering from the `local_network` to the `peer_network`, the peering relationship is bidirectional. The peering from the `peer_network` to the `local_network` gets created automatically.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Verify that traffic is passing between peered VPC networks

You can use [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) to view network flows sent from and received by VM instances. You can also use [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging) to verify that traffic is passing between the networks. Create [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) that allow (or deny) traffic between the peered networks, and turn on Firewall Rules Logging for those rules. You can then view which firewall rules were hit using Cloud Logging.

## Update a peering connection

When you update an existing peering connection, you can do the following:

  * Change whether your VPC network exports or imports custom routes or privately used public IPv4 subnet routes to or from the peer VPC network.
  * Change whether your peering connection exchanges IPv6 routes between the peered networks.
  * Update the peering connection mode from independent (default) to consensus, by changing the update strategy for the connection. Before changing the update strategy, review the requirements for [consensus mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#consensus-mode).



Your network imports routes only if the peer network is also exporting the routes, and the peer network receives routes only if it imports them.

**Important:** Even if the dynamic routing mode of the VPC network is set to global, IPv6 routes learned from the Cloud Router are regional. For more information, see [Limitations](https://docs.cloud.google.com/vpc/docs/vpc-peering#peering-limitations).

### Update a connection (independent mode)

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select the peering connection to update.

  3. Click **Edit**.

  4. To update the IP version of routes that you want to exchange between the peered networks, select one of the following:

     * **IPv4 (single-stack)** : exchange only IPv4 routes. The peer network must also enable this option.
     * **IPv4 and IPv6 (dual-stack)** : exchange both IPv4 and IPv6 routes. The peer network must also enable this option.
  5. To exchange IPv4 custom routes, in the **Exchange IPv4 custom routes** section, choose one or both of the following options:

     * **Import custom routes** : import custom routes from the peer network. The peer network must enable custom route export for routes to be imported.
     * **Export custom routes** : export custom routes to the peer network. The peer network must enable custom route import for routes to be exported.
  6. If your network or the peer network has privately used public IPv4 ranges in its subnets, these routes are exported by default, but not imported by default.

To import privately used public IPv4 subnet routes, in the **Exchange subnet routes with privately used public IPv4 addresses** section, select **Import subnet routes with public IP**.

  7. To update the peering connection from independent (default) to consensus mode, in the **Advanced options** section, for **Update strategy** , select **Consensus**. After you click **Save** , the update strategy changes to **Consensus** for the local configuration.

To complete the update request, a network administrator for the peer network must accept the request by changing the update strategy to **Consensus** for the peer configuration.

  8. Click **Save**.




###  gcloud 

Use the [`gcloud compute networks peerings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update).

You can use the following optional parameters:

  * `--stack-type` sets the stack type for the peering connection. By default, only IPv4 routes are exchanged. 
    * To exchange both IPv4 and IPv6 routes, specify `IPV4_IPV6` for both networks.
    * To disable IPv6 route exchange, specify `IPV4_ONLY` for both networks.
  * `--import-custom-routes` tells the network to accept [custom routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) from the peered network. The peered network must export the routes first.

To disable this option, use `--no-import-custom-routes`.

  * `--export-custom-routes` tells the network to export [custom routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) to the peered network. The peered network must be set to import the routes.

To disable this option, use `--no-export-custom-routes`.

  * `--import-subnet-routes-with-public-ip` tells the network to accept subnet routes from the peered network if that network is using [privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) in its subnets. The peered network must export the routes first.

To disable this option, use `--no-import-subnet-routes-with-public-ip`.

  * `--export-subnet-routes-with-public-ip` tells the network to export subnet routes that contain [privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). The peered network must be set to import the routes.

To disable this option, use `--no-export-subnet-routes-with-public-ip`.

  * `--update-strategy` sets the update strategy for the peering connection. By default, the update strategy is `INDEPENDENT`. To configure the connection to use consensus mode, specify `CONSENSUS` for both sides of the connection.

To cancel a pending update request to configure consensus mode, reset the update strategy to `INDEPENDENT`. For more information, see [Connection mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-mode).




The following example shows how to update a peering connection to exchange both IPv4 and IPv6 routes.

  1. Update the stack type for the local network:
         
         gcloud compute networks peerings update PEERING_NAME_1 \
             --network=NETWORK_1 \
             --stack-type=IPV4_IPV6
         

  2. Update the stack type for the peer network. This step is usually performed by its network administrator.
         
         gcloud compute networks peerings update PEERING_NAME_2 \
             --network=NETWORK_2 \
             --stack-type=IPV4_IPV6
         




Replace the following:

  * `PEERING_NAME_1`: the name of the local peering configuration
  * `NETWORK_1`: the name of the local network
  * `PEERING_NAME_2`: the name of the corresponding configuration for the peer network
  * `NETWORK_2`: the name of the peer network



#### Update a connection to consensus mode

You update a peering connection from independent (default) to consensus mode by changing the update strategy for the connection. Before changing the update strategy, review the requirements for [consensus mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#consensus-mode).

  1. Update the local peering configuration:
         
         gcloud compute networks peerings update PEERING_NAME \
             --network=NETWORK \
             --update-strategy=CONSENSUS
         

Replace the following:

     * `PEERING_NAME`: the name of the existing peering configuration
     * `NETWORK`: the name of the network in your project that is peered
  2. View the status of the update request:
         
         gcloud compute networks describe NETWORK
         

Replace `NETWORK` with the name of the network in your project that is peered.

In the output, the `updateStatus` field must display the following status:

     * In the configuration for the local network, `PENDING_PEER_ACKNOWLEDGMENT`
     * In the corresponding configuration for the peer network, `PENDING_LOCAL_ACKNOWLEDGMENT`
  3. Accept the update request by running the command in step 1 for the peer side of the connection.

This step is usually performed by a network administrator for the peer network.




After the request is complete, the `updateStatus` field changes to `IN_SYNC` for both configurations, which updates the effective status of the connection.

### Update a connection (consensus mode)

When a peering connection is configured with consensus mode, updating the effective status of the connection requires acknowledgment from the peer network. For more information, see [Updating a connection in consensus mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#consensus-update).

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select the peering connection to update.

  3. Click **Edit**.

  4. Update the route exchange options:

     * If you update **IP stack type** , the peer network must also enable the same stack type.
     * If you update **Exchange IPv4 custom routes** or **Exchange subnet routes with privately used public IPv4 addresses** , the peer network must enable the [complementary setting](https://docs.cloud.google.com/vpc/docs/about-peering-connections#complementary-settings) for each setting that you modify. For example, if your network imports custom routes, the peer network must export custom routes.
  5. Click **Save** and **Request update**.

  6. Update the peer configuration. This step is usually performed by a network administrator for the peer network.




To cancel a pending update request, on the **Edit** page for the requesting network, click **Revert update**.

###  gcloud 

Use the [`gcloud compute networks peerings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update).

You can use the following optional parameters:

  * `--stack-type` sets the stack type for the peering connection. By default, only IPv4 routes are exchanged. 
    * To exchange both IPv4 and IPv6 routes, specify `IPV4_IPV6` for both networks.
    * To disable IPv6 route exchange, specify `IPV4_ONLY` for both networks.
  * `--import-custom-routes` tells the network to accept [custom routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) from the peered network. The peered network must export the routes first.

To disable this option, use `--no-import-custom-routes`.

  * `--export-custom-routes` tells the network to export [custom routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) to the peered network. The peered network must be set to import the routes.

To disable this option, use `--no-export-custom-routes`.

  * `--import-subnet-routes-with-public-ip` tells the network to accept subnet routes from the peered network if that network is using [privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) in its subnets. The peered network must export the routes first.

To disable this option, use `--no-import-subnet-routes-with-public-ip`.

  * `--export-subnet-routes-with-public-ip` tells the network to export subnet routes that contain [privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). The peered network must be set to import the routes.

To disable this option, use `--no-export-subnet-routes-with-public-ip`.




The following example shows how to update a peering connection to import custom routes from `network-a` to `network-b`.

  1. For `peering-a` in `network-a`, configure the network to export custom routes:
         
         gcloud compute networks peerings update peering-a \
             --network=network-a \
             --export-custom-routes
         

  2. View the status of the update request:
         
         gcloud compute networks describe network-a
         

In the output, the `updateStatus` field must display the following status:

     * In the configuration for `network-a` (local network), `PENDING_PEER_ACKNOWLEDGMENT`
     * In the corresponding configuration for `network-b` (peer network), `PENDING_LOCAL_ACKNOWLEDGMENT`
  3. Configure the peer network to import custom routes. This step is usually performed by a network administrator for the peer network.
         
         gcloud compute networks peerings update peering-b \
             --network=network-b \
             --import-custom-routes
         

The `updateStatus` field changes to `IN_SYNC` for both configurations, which updates the effective status of the connection.




To cancel a pending update request, reset each modified parameter to its previous value.

## List peering connections

List existing peering connections to view their status and whether they're importing or exporting custom routes.

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select the peering connection to view its details.




###  gcloud 
    
    
    gcloud compute networks peerings list
    

## View a peering connection

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. In the **Status** column, view the status of your connection.




###  gcloud 

Use the [`gcloud compute networks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/describe).
    
    
    gcloud compute networks describe NETWORK
    

Replace `NETWORK` with the name of the network in your project that is peered.

In the output, the `peerings.connectionStatus` field describes the effective status of the peering connection. For more information, see [Connection status](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-status).

## List peering routes

###  Console 

Use the **Effective routes** tab to view all applicable [route types](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) in a VPC network, including imported peering subnet, peering static, and peering dynamic routes.

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. On the **Effective routes** tab, do the following:

     * Select a **VPC network**.
     * Select a **Region**.
  3. Click **View**.

  4. Click the **Filter** text field, and do the following:

     * Choose **Type** from the **Properties** menu.
     * Choose one of the following from the **Values** menu. 
       * **Peering subnet** : to see subnet routes from peer VPC networks.
       * **Peering static** : to see imported static routes from peer VPC networks.
       * **Peering dynamic** : to see imported dynamic routes from peer VPC networks.
  5. Optionally, click **Show suppressed routes** to view routes that are suppressed. Place your pointer over the icon in the **Status** column to view the reason why a route has been suppressed. The reason includes a link to the [routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection) documentation with an explanation.




###  gcloud 

Use the following Google Cloud CLI command to:

  * List _route exports_ sent from your VPC network to peer VPC networks.
  * List _route import candidates_ for your VPC network.

**Important:** Route exports from your VPC network always become route import candidates in each peer VPC network, but neither list takes into consideration conflict resolution in the importing VPC network. To see which routes are actually imported and which routes are omitted, use the **Effective routes** tab in the Google Cloud console.
    
    
    gcloud compute networks peerings list-routes PEERING_NAME \
        --network=NETWORK \
        --region=REGION \
        --direction=DIRECTION
    

Replace the following:

  * `PEERING_NAME`: the name of an existing peering connection.
  * `NETWORK`: the name of the network in your project that is peered.
  * `REGION`: the region where you want to list all dynamic routes. Subnet and static routes are global and are shown for all regions.
  * `DIRECTION`: specifies whether to list imported (`incoming`) or exported (`outgoing`) routes.



## Delete a peering connection

When a peering configuration is deleted in your network, the peering connection becomes inactive in the other network, and all routes shared among the networks are removed.

The procedure for deleting a peering connection depends on the update strategy configured for the connection:

  * **Independent (default)** : you or a network administrator for the peer VPC network can delete the connection at any time. See Delete a connection (independent mode).
  * **Consensus** : both you and a network administrator for the peer VPC network must submit a delete request before the connection can be deleted. See Delete a connection (consensus mode).



**Warning:** Don't delete a VPC Network Peering connection that is already in use by Google Cloud resources. Deleting an in-use peering connection can cause problems, including the following: 

  * If you delete a peering connection that is used by private services access, then you can't create new private connections for private services access. For more information, see [Unable to create a new private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#unable-to-create-connection). 
  * If you delete a peering connection that is used by Google Kubernetes Engine (GKE), the cluster enters a repair state and all nodes show an `UNKNOWN` status. For more information, see [VPC Network Peering connection is accidentally deleted](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-isolation#vpc_peering_network). 



### Delete a connection (independent mode)

To delete a peering connection in independent mode (default), do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select the checkbox next to the peering connection that you want to remove.

  3. Click **Delete**.

The status of the connection changes to **Inactive** for the peer network. To remove the inactive configuration, a network administrator for the peer network performs these steps for the peer side of the connection.




###  gcloud 

Use the [`gcloud compute networks peerings delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/delete).
    
    
    gcloud compute networks peerings delete PEERING_NAME \
        --network=NETWORK
    

Replace the following:

  * `PEERING_NAME`: the name of the peering configuration
  * `NETWORK`: the name of the network in your project that is peered



The status of the connection changes to `INACTIVE` for the peer network. To remove the inactive configuration, a network administrator for the peer network performs this step for the peer side of the connection.

### Delete a connection (consensus mode)

To delete a peering connection in consensus mode, follow these steps. You can also cancel a deletion request.

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click the peering connection that you want to remove.

  3. On the **Peering connection details** page, click **Request delete** and then **Confirm**.

  4. Accept the deletion request by performing steps 1-3 for the peer side of the connection.

These steps are usually performed by a network administrator for the peer network. After both sides of the peering connection submit the deletion request, the status of the connection changes to **Active, delete acknowledged** for both configurations.

  5. Select the peering connection that you want to remove and then click **Delete**.

The status of the connection changes to **Inactive** for the peer network. To remove the inactive configuration, the network administrator for the peer network performs this step for the peer side of the connection.




###  gcloud 

Use the [`gcloud compute networks peerings request-delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/request-delete) and [`gcloud compute networks peerings delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/delete) commands.

  1. Initiate a deletion request:
         
         gcloud compute networks peerings request-delete PEERING_NAME \
             --network=NETWORK
         

Replace the following:

     * `PEERING_NAME`: the name of the peering configuration
     * `NETWORK`: the name of the network in your project that is peered
  2. View the status of the deletion request:
         
         gcloud compute networks describe NETWORK
         

Replace `NETWORK` with the name of your network.

In the output, the `deleteStatus` field must display the following status:

     * In the configuration for your network, `LOCAL_DELETE_REQUESTED`
     * In the corresponding configuration for the peer network, `PEER_DELETE_REQUESTED`
  3. Accept the deletion request by running the `request-delete` command for the peer side of the connection, specifying the peer network and its peering configuration names.

This step is usually performed by a network administrator for the peer network. After both sides of the connection submit the deletion request, the status of the `deleteStatus` field changes to `DELETE_ACKNOWLEDGED` for both configurations.

  4. Delete the peering connection:
         
         gcloud compute networks peerings delete PEERING_NAME \
             --network=NETWORK
         

Replace the following:

     * `PEERING_NAME`: the name of the peering configuration
     * `NETWORK`: the name of the network in your project that is peered

The status of the connection changes to `INACTIVE` for the peer network. To remove the inactive configuration, the network administrator for the peer network performs this step for the peer side of the connection.




#### Cancel a deletion request

You can cancel a deletion request before or after it is accepted by the peer network. While a request is pending, only the local network can cancel it. After the peer network accepts the request, either network can cancel the deletion.

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click the peering connection you want to cancel the deletion request for.

  3. On the **Peering connection details** page, click **Cancel delete request** and then **Confirm**.

If the peer network has already accepted the deletion request, an administrator for the peer network must also perform these steps for the peer side of the connection.




###  gcloud 

Use the [gcloud compute networks peerings cancel-request-delete command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/cancel-request-delete).

**Cancel before the deletion request is accepted** :

To cancel the deletion request before it is accepted, run the following command for the network that initiated the request:
    
    
    gcloud compute networks peerings cancel-request-delete PEERING_NAME \
        --network=NETWORK
    

Replace the following:

  * `PEERING_NAME`: the name of the peering configuration
  * `NETWORK`: the name of the network



**Cancel after the deletion request is accepted** :

  1. To cancel the deletion request after it is accepted, run the following command for either network:
         
         gcloud compute networks peerings cancel-request-delete PEERING_NAME \
           --network=NETWORK
         

Replace the following:

     * `PEERING_NAME`: the name of the peering configuration
     * `NETWORK`: the name of the network
  2. View the status of the request:
         
         gcloud compute networks describe NETWORK
         

Replace `NETWORK` with the name of your network.

In the output, the `deleteStatus` field displays the following status:

     * In the configuration for your network, `LOCAL_CANCEL_REQUESTED`
     * In the corresponding configuration for the peer network, `PEER_CANCEL_REQUESTED`
  3. Cancel the request for the peer side of the connection by running the `cancel-request-delete` command with the peer network and its peering configuration names.

This step is usually performed by a network administrator for the peer network.




## Troubleshooting

The following sections describe how to troubleshoot issues with VPC Network Peering.

### Peer VMs are unreachable

After the peering connection is ACTIVE, it may take up to a minute for all the traffic flows to be set up between the peered networks. This time depends on the size of the networks that are peering. If you have recently set up the peering connection, wait up to a minute and try again. Also, ensure that there are no firewall rules blocking access to or from peer VPC network subnet CIDRs.

### Custom routes are missing

This section describes how to troubleshoot missing custom routes.

#### Check the peering connection state

To check the state of your peering connection, do the following:

  1. List peering connections.
  2. Identify the peering connection to troubleshoot, and review its peering state. 
     1. If the state is `ACTIVE`, follow the steps in the next section.
     2. If the peering state is `INACTIVE`, a network administrator for the other network needs to create a peering configuration to your VPC network.



#### Troubleshoot an `ACTIVE` connection

To troubleshoot missing custom routes in an `ACTIVE` peering connection:

  1. List peering routes in your VPC network. In the **Effective routes** tab, do the following:

     1. Consider that the regions in which dynamic routes are programmed depends on the dynamic routing mode of the VPC network that exports custom routes. For more details, see [Effects of the dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc-peering#interaction-dynamic-routing-mode). In global dynamic routing mode, only the highest ranked dynamic route is programmed in regions that don't match the region of the next hop.

     2. Click the **Show suppressed routes** toggle to the on position, then check for your route. To view the reason why a route has been suppressed, point to the icon in the **Status** column. Google Cloud provides route conflict resolution on a region-by-region basis in the VPC network that imports routes using VPC Network Peering.

     3. Look for a warning indicating that your VPC network has reached the limit for the [dynamic routes per region per peering group quota](https://docs.cloud.google.com/vpc/docs/quota#per_network). If your VPC network has reached the limit for this quota, one or more peering dynamic routes aren't programmed. Because it's not possible to show exactly which peering dynamic routes aren't programmed, request a quota limit increase for the dynamic routes per region per peering group quota.

  2. If you still don't see the route you expect, do the following:

     1. Review your peering configuration, and update your peering configuration if necessary so that it imports custom routes.

     2. Ensure that the route is not one of the following route types that can't be exchanged using VPC Network Peering:

        * Peering subnet, peering static, and peering dynamic routes in a peered VPC network _that are received from its other peer networks_ cannot be exchanged to your VPC network using VPC Network Peering.

        * Static routes that use the default internet gateway next hop and static routes with network tags [cannot be exchanged](https://docs.cloud.google.com/vpc/docs/vpc-peering#static-route-exchange) using VPC Network Peering.

For more information, see [Route exchange options](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options).

     3. Ask a network administrator of the peered VPC network to:

        1. [List routes in their VPC network](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes), looking for the route you expect.

        2. Review their peering configuration, and update the peering configuration if necessary so that it exports custom routes.




### Traffic destined for a peer network is being dropped

You can use [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests) to help determine why traffic destined for a peer network is being dropped. If traffic should be sent using custom routes, see Custom routes are missing.

### Traffic is being sent to an unexpected next hop

You can use [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests) to help determine why traffic is being sent to an unexpected next hop. If traffic should be sent using custom routes, see Custom routes are missing.

### Unable to peer with a particular VPC network

If you cannot create a peering configuration with certain VPC networks, an organization policy might be constraining the VPC networks that your network can peer with. In the organization policy, add the network to the list of allowed peers or contact your organization administrator. For more information, refer to the [`constraints/compute.restrictVpcPeering`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) constraint.

### IPv6 routes are not exchanged

First, verify that both your peering connection and the peering connection of the peered VPC network have their stack types set to `IPV4_IPV6`. If necessary:

  * Update your peering connection to set its stack type to `IPV4_IPV6`.
  * Ask a network administrator of the peered VPC network to update their peering connection, setting its stack type to `IPV4_IPV6`.



After both peering connections have their stack types set to `IPV4_IPV6`, IPv6 subnet routes (both internal and external) are exchanged. IPv6 subnet routes are unique among all Google Cloud VPC networks.

To exchange IPv6 custom routes:

  * Update your peering connection to import and export custom routes.
  * Ask a network administrator of the peered VPC network to update their peering connection to import and export custom routes.



### Changes in effective limit for per-peering group quotas

You might notice changes in the [effective limits for per-peering group quotas](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering-effective-limit). The effective limits change because these quotas are dependent on the limits of peered networks—when peers are added or removed, the effective limit of the per-peering group quota changes accordingly.

## What's next

  * For more information about VPC routing, see [Routes](https://docs.cloud.google.com/vpc/docs/routes).
  * For limits related to VPC Network Peering, see [VPC Network Peering limits](https://docs.cloud.google.com/vpc/docs/quota).
  * For information about how to use an internal passthrough Network Load Balancer as the next hop for a custom static route, see [Use an internal passthrough Network Load Balancer as a next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
