---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication/
title: Use MD5 authentication \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:19.502796+00:00
---

# Use MD5 authentication  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use MD5 authentication

Cloud Router uses Border Gateway Protocol (BGP) to exchange routes between a Virtual Private Cloud (VPC) network and a peer network. By default, Cloud Router BGP sessions are unauthenticated. However, when you use Cloud Router with certain products, you can optionally configure your BGP sessions to use MD5 authentication.

Products that can use MD5 authentication include the following:

  * [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn)
  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



You can also use MD5 authentication with third-party network virtual appliances. For more information, see [Router appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview) in the NCC documentation.

When you configure a session to use MD5 authentication, you provide a secret shared key—a key that you use when configuring Cloud Router and again when you configure your peer router. After you complete the required setup steps, Cloud Router uses that key to authenticate the BGP peer. Cloud Router enforces MD5 authentication by using the model described in [RFC 2385](https://datatracker.ietf.org/doc/html/rfc2385).

You can add MD5 authentication when you create a peer. You can also add authentication to an existing session, change the key that a session uses, or remove authentication.

## Before you begin

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



  1. If you are using the Google Cloud CLI, set your project ID by running the following command. The `gcloud` instructions on this page assume that you have set your project ID. 
         
         gcloud config set project PROJECT_ID
             



  1. Confirm that the ID was set by running the following command: 
         
         gcloud config list --format='text(core.project)'
             




## Create a session that uses authentication

For some Network Connectivity products, you can configure a BGP peer to use MD5 authentication while you are creating the resource. These products include HA VPN and Dedicated Interconnect.

For more information, see the following sections:

  * [Create an HA VPN tunnel to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_bgp_sessions)
  * [Create an HA VPN tunnel between Google Cloud networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create_bgp_sessions)
  * [Create VLAN attachments (Dedicated Interconnect)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#creating_vlan_attachments)



If you are creating a Layer 2 Partner Interconnect VLAN attachment, [create the attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#creating_vlan_attachments) first, and then update the BGP peer to add MD5 authentication. For information about how to add authentication while updating a BGP session, see the following section. If you have a Layer 3 connection, contact your service provider for instructions.

## Add authentication to an existing session

To add authentication to an existing BGP peer, use one of the following procedures. When you add authentication, make sure that the key that you use is identical to the one used by your peer router.

Google Cloud doesn't display the MD5 authentication key and _only_ show the key-name upon successful configuration.

  * If you configure MD5 authentication through gcloud or UI, Google Cloud automatically generates the key-name in the form of `PEER_NAME-key`.
  * If you configure MD5 authentication through API, you can specify the key-name.

**Caution:** When you add authentication to a BGP session, it's expected that the session flaps. If the session doesn't come back up, see [Authentication issues](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshooting#authentication).

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. To add MD5 authentication: 

     1. In the **MD5 Authentication** section, select **Enabled**. The page updates to include a text field.
     2. Enter a security key or, to generate a new security key, click **Generate and copy**.
     3. Make a note of the key. After you leave this page, you cannot retrieve the key.
  6. Click **Save.**




###  gcloud 

To update the session by using gcloud CLI, use the [`gcloud compute routers update-bgp-peer`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer) command:
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
         --peer-name=PEER_NAME \
         --region=REGION \
         --md5-authentication-key=SECRET_KEY
     

Replace the following values:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of the BGP peer
  * `REGION`: the Google Cloud region
  * `SECRET_KEY`: your secret shared MD5 authentication key



###  API 

To update the session by using the API, use the [`compute.routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method. When you use this method to add authentication to the session, your request must do two things:

  * Add an entry for the key in the `md5AuthenticationKeys` array. When you add the entry, you provide both a name and a value for the key.
  * Update the `bgpPeers` array to include a value for the `md5AuthenticationKeyName` field. This field references the key by name.



When you patch the `md5AuthenticationKeys` array, you must provide the `name` of each item in the array (unless you want to remove some items). However, you do not have to provide the value for each item's `key` field. If you omit this value, Cloud Router retains the previous value that was used. This behavior is designed to protect the secrecy of keys. It differs from other patch methods, which typically require you to specify a value for each field on an array item.

When you patch the `bgpPeers` array, you _do_ have to provide values for every field on every item (unless you want to remove some peers or some values).

For example, suppose the Cloud Router has two peers, one that uses MD5 authentication and one that doesn't. If you want to leave the first peer unchanged but add MD5 authentication to the second peer, you would use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "md5AuthenticationKeys": [
          {
            "name": "KEY_NAME_1",
          },
          {
            "name": "KEY_NAME_2",
            "key": "SECRET_KEY"
          }
        ],
        "bgpPeers": [
          {
            "name": "PEER_NAME_1",
            "md5AuthenticationKeyName": "KEY_NAME_1",
            "interfaceName": "INTERFACE_NAME_1",
            "ipAddress": "IP_ADDRESS_1",
            "peerIpAddress": "PEER_IP_ADDRESS_1",
            "peerAsn": "PEER_ASN_1"
          },
          {
            "name": "PEER_NAME_2",
            "md5AuthenticationKeyName": "KEY_NAME_2",
            "interfaceName": "INTERFACE_NAME_2",
            "ipAddress": "IP_ADDRESS_2",
            "peerIpAddress": "PEER_IP_ADDRESS_2",
            "peerAsn": "PEER_ASN_2"
          }
        ],
      }
     

Replace the following values:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the Google Cloud region
  * `ROUTER_NAME`: the name of the Cloud Router
  * `KEY_NAME_1`: The name of the key that is in current use (by`PEER_NAME_1`)
  * `KEY_NAME_2`: the name of the new key that you want to add for `PEER_NAME_2`. Make a note of the name. If you want to make changes later by using the API, you need the name.
  * `SECRET_KEY`: your secret MD5 authentication key that you are adding for `PEER_NAME_2`
  * `PEER_NAME_1`: the name of the BGP peer that you are _not_ changing
  * `INTERFACE_NAME_1`: the name of the interface for the BGP peering session that is not changing
  * `IP_ADDRESS_1`: the IP address on the Cloud Router (for the peer that is not changing)
  * `PEER_IP_ADDRESS_1`: the IP address of the peer that is not changing
  * `PEER_ASN_1`: the BGP autonomous system number (ASN) for the peer that is not changing
  * `PEER_NAME_2`: the name of the BGP peer that you want to update so that it uses MD5 authentication
  * `INTERFACE_NAME_2`: the name of the interface for the BGP peering session
  * `IP_ADDRESS_2`: the IP address on the Cloud Router
  * `PEER_IP_ADDRESS_2`: the IP address of the peer router
  * `PEER_ASN_2`: the BGP autonomous system number (ASN) for this BGP peer



## Update the authentication key

To change the key that Cloud Router uses for a peering session, use one of the following procedures. When you update the key on the Cloud Router, make sure that the key that you use is identical to the one used by your peer router.

Google Cloud doesn't display the MD5 authentication key and _only_ show the key-name upon successful configuration.

  * If you configure MD5 authentication through gcloud or UI, Google Cloud automatically generates the key-name in the form of `PEER_NAME-key`.
  * If you configure MD5 authentication through API, you can specify the key-name.

**Caution:** When you update the authentication key, it's expected that the session flaps. If the session doesn't come back up, see [Authentication issues](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshooting#authentication).

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. In the **MD5 Authentication** section, click **Update MD5 Authentication Key**.

  6. In the **MD5 Authentication key** field, enter the new secret authentication key or, to populate the field, click **Generate and copy**.

  7. Make a note of the key. After you leave this page, you cannot retrieve the key.

  8. Click **Save**.




###  gcloud 

To update the session, use the [`gcloud compute routers update-bgp-peer`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer) command.
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
         --peer-name=PEER_NAME \
         --region=REGION \
         --md5-authentication-key=SECRET_KEY
     

Replace the following values:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of the BGP peer
  * `REGION`: the Google Cloud region
  * `SECRET_KEY`: the new secret MD5 authentication key that you want to use



###  API 

To update the session, use the [`compute.routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method. For example, use a request like the following.

This example replaces the entire peer array, not just the specific peer that is identified. That is, it removes all peers except `PEER_NAME`. It removes all keys except `KEY_NAME` and updates the `KEY_NAME` with the new value `UPDATED_SECRET_KEY`.
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "md5AuthenticationKeys": [
           {
            "name": "KEY_NAME",
            "key": "UPDATED_SECRET_KEY"
          }
        ],
    
        "bgpPeers": [
          {
            "name": "PEER_NAME",
            "md5AuthenticationKeyName": "KEY_NAME",
            "interfaceName": "INTERFACE_NAME",
            "ipAddress": "IP_ADDRESS",
            "peerIpAddress": "PEER_IP_ADDRESS",
            "peerAsn": "PEER_ASN"
          }
        ],
      }
     

Replace the following values:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the Google Cloud region
  * `ROUTER_NAME`: the name of the Cloud Router
  * `KEY_NAME`: the name of the key you want to update; whenever you work with MD5 authentication by using the API, you must refer to the key by its name
  * `UPDATED_SECRET_KEY`: your new secret MD5 authentication key
  * `PEER_NAME`: the name of the BGP peer
  * `INTERFACE_NAME`: the name of the interface for the BGP peering session
  * `IP_ADDRESS`: the IP address on the Cloud Router
  * `PEER_IP_ADDRESS`: the IP address of the peer router
  * `PEER_ASN`: the BGP autonomous system number (ASN) for this BGP peer

**Note:** When you patch the `md5AuthenticationKeys` array, you must provide the name of each key in the array that you want to retain. However, you do not have to specify the value of each key. You can omit the `key` field, and the previous value is retained. This behavior, which differs from most other patch methods, is designed to protect the secrecy of keys.

## Check authentication status

Use the following steps to check the status of MD5 authentication. See also [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#gcloud_1).

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, look for the **MD5 Authentication** column. For each session, the value in this column indicates whether MD5 authentication is enabled.




###  gcloud 

To check the session by using gcloud CLI, use the [`gcloud compute routers get-status`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-status) command.
    
    
      gcloud compute routers get-status ROUTER_NAME \
         --project=PROJECT \
         --region=REGION \
     

Replace the following values:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PROJECT`: the name of the project
  * `REGION`: the Google Cloud region



The output includes the `result.bgpPeerStatus[]` object, which contains information about the Cloud Router's BGP sessions. The data about each session includes the following two fields:

  * `md5AuthEnabled`—a boolean field that indicates whether MD5 authentication is enabled for the session
  * `statusReason`—a field that describes the status of the session



###  API 

Use the [`routers.getRouterStatus`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus) method:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME/getRouterStatus
    

Replace the following:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router



The output includes information about each BGP session. The data about each session includes the following two fields:

  * `md5AuthEnabled`: a boolean field that indicates whether MD5 authentication is enabled for the session
  * `statusReason`: a field that describes the status of the session. This field is displayed only when there is a problem with MD5 authentication. (In that case, the value of the field is `MD5_AUTH_INTERNAL_PROBLEM`.)



To set up continuous monitoring of your BGP sessions, use [Cloud Logging](https://docs.cloud.google.com/logging). Logging records information about MD5 authentication status in the BGP event, which is part of the [Info log](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#info_log).

## Remove authentication from a session

If you want to remove MD5 authentication from a BGP session, you must remove MD5 authentication from both the Cloud Router and your peer router.

To remove MD5 authentication from the BGP session on the Cloud Router, use one of the following procedures.

**Caution:** When you remove authentication from a BGP session, it's expected that the session flaps. If the session doesn't come back up, see [Authentication issues](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshooting#authentication).

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. For **MD5 Authentication** , click **Disabled**.

  6. Click **Save**. The **Disable MD5 Authentication key** dialog box appears.

  7. In the confirmation dialog, click **Confirm**.




###  gcloud 

To remove MD5 authentication, use the [`gcloud compute routers update-bgp-peer`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer) command:
    
    
       gcloud compute routers update-bgp-peer ROUTER_NAME \
         --peer-name=PEER_NAME \
         --region=REGION \
         --clear-md5-authentication-key
    

Replace the following values:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of the BGP peer
  * `REGION`: the Google Cloud region



###  API 

To remove MD5 authentication, use the [`compute.routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method.

When you remove authentication by using the API, your update must do two things:

  * Update the `md5AuthenticationKeys` array
  * Remove the `md5AuthenticationKey` value from the relevant `bgpPeers` entry



For example, if your Cloud Router has two BGP peers and you want to remove MD5 authentication from one of them. In this case, use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "md5AuthenticationKeys": [
            "name": "KEY_NAME_FOR_UNCHANGED_PEER",
            ],
        "bgpPeers": [
          {
            "name": "NAME_OF_UPDATED_PEER",
            "interfaceName": "INTERFACE_NAME_FOR_UPDATED_PEER",
            "ipAddress": "IP_ADDRESS_FOR_UPDATED_PEER",
            "peerIpAddress": "PEER_IP_ADDRESS_FOR_UPDATED_PEER",
            "peerAsn": "PEER_ASN_FOR_UPDATED_PEER"
          },
          {
            "name": "NAME_OF_UNCHANGED_PEER",
            "interfaceName": "INTERFACE_NAME_FOR_UNCHANGED_PEER",
            "ipAddress": "IP_ADDRESS_FOR_UNCHANGED_PEER",
            "peerIpAddress": "PEER_IP_ADDRESS_FOR_UNCHANGED_PEER",
            "peerAsn": "PEER_ASN_FOR_UNCHANGED_PEER"
            "md5AuthenticationKeyName": "KEY_NAME_FOR_UNCHANGED_PEER"
          }
        ],
        ],
      }
     

Replace the following values:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the Google Cloud region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router
  * `NAME_OF_UPDATED_PEER`: the name of the peering session you want to modify
  * `INTERFACE_NAME_FOR_UPDATED_PEER`: the name of the interface for the BGP peer that you want to modify
  * `IP_ADDRESS_FOR_UPDATED_PEER`: the IP address on the Cloud Router that is used by the peer you want to modify
  * `PEER_IP_ADDRESS_FOR_UPDATED_PEER`: the IP address of the peer router for the peering session you want to modify
  * `PEER_ASN`: the BGP autonomous system number (ASN) for this BGP peer you want to modify
  * `NAME_OF_UNCHANGED_PEER`: the name of the peering session you want to keep as is
  * `INTERFACE_NAME_FOR_UNCHANGED_PEER`: the name of the interface for the BGP peer that you want to keep as is
  * `IP_ADDRESS_FOR_UNCHANGED_PEER`: the IP address on the Cloud Router that is used by the peer that you want to keep as is
  * `PEER_IP_ADDRESS_FOR_UNCHANGED_PEER`: the IP address of the peer router for the peering session that you want to keep as is
  * `PEER_ASN_FOR_UNCHANGED_PEER`: the BGP autonomous system number (ASN) for the BGP peer that you want to keep as is
  * `KEY_NAME_FOR_UNCHANGED_PEER`: the name of the MD5 authentication key for the BGP peer that you want to keep as is

**Note:** When you patch the `md5AuthenticationKeys` array, you must provide the name of each key in the array that you want to retain. However, you do not have to specify the value of each key. You can omit the `key` field, and the previous value is retained. This behavior, which differs from most other patch methods, is designed to protect the secrecy of keys.

## Remove a session that uses authentication

To remove a peering session that uses MD5 authentication, use one of the following procedures.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the router that you want to remove a BGP session from.
  3. For **BGP sessions** , select the BGP session that you want to remove.
  4. At the top of the page, click delete**Delete** , and then confirm the deletion.



###  gcloud 

To remove a BGP session with MD5 authentication enabled, use the [`gcloud compute routers remove-bgp-peer`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer) command.

For more information, see [Disable or remove BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#remove_a_bgp_session).

###  API 

To remove a BGP session with MD5 authentication enabled, use the [`compute.routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method.

When you remove a BGP session with MD5 authentication by using the API, your update must do two things: remove the key from `md5AuthenticationKeys` array and remove the `bgpPeer` itself.

For example, suppose the Cloud Router has two peers and you want to remove one of them. In this case, use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "md5AuthenticationKeys": [
            "name": "KEY_NAME_FOR_RETAINED_PEER",
            ],
        "bgpPeers": [
          {
            "name": "NAME_OF_RETAINED_PEER",
            "interfaceName": "INTERFACE_FOR_RETAINED_PEER",
            "ipAddress": "IP_ADDRESS_FOR_RETAINED_PEER",
            "peerIpAddress": "PEER_IP_ADDRESS_FOR_RETAINED_PEER",
            "peerAsn": "PEER_ASN_FOR_RETAINED_PEER",
            "md5AuthenticationKeyName": "KEY_NAME_FOR_RETAINED_PEER"
          }
        ],
      }
     

Replace the following values:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the Google Cloud region
  * `ROUTER_NAME`: the name of the Cloud Router
  * `KEY_NAME_FOR_RETAINED_PEER`: the name of the key used by the peer that you are keeping
  * `NAME_OF_RETAINED_PEER`: the name of the BGP peer that you are keeping
  * `INTERFACE_FOR_RETAINED_PEER`: the name of the interface for the BGP peer that you are keeping
  * `IP_ADDRESS_FOR_RETAINED_PEER`: the IP address on the Cloud Router for the peer that you are keeping
  * `PEER_IP_ADDRESS_FOR_RETAINED_PEER`: the IP address of the peer that you are keeping
  * `PEER_ASN_FOR_RETAINED_PEER`: the BGP autonomous system number (ASN) for the peer that you are keeping
  * `KEY_NAME_FOR_RETAINED_PEER`: the name of the MD5 authentication key for the BGP peer that you are keeping

**Note:** When you patch the `md5AuthenticationKeys` array, you must provide the name of each key in the array that you want to retain. However, you do not have to specify the value of each key. You can omit the `key` field, and the previous value is retained. This behavior, which differs from most other patch methods, is designed to protect the secrecy of keys.

For example, suppose you created the following peers:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/project_id/regions/region_name/routers/cloud_router_name
      {
        "md5AuthenticationKeys": [
          {
            "name":  "first_key_name",
            "key":  "first_secret_key_value"
          },
          {
            "name":  "second_key_name",
            "key":  "second_secret_key_value"
          }
        ],
        "bgpPeers": [
          {
            "name": "first_peer",
            "md5AuthenticationKeyName": "first_key_name",
            "interfaceName": "first_interface",
            "ipAddress": "first_address",
            "peerIpAddress": "first_peer_interface",
            "peerAsn": "first_peer_asn"
          },
          {
            "name": "second_peer",
            "md5AuthenticationKeyName": "second_key_name",
            "interfaceName": "second_interface",
            "ipAddress": "second_address",
            "peerIpAddress": "second_peer_interface",
            "peerAsn": "second_peer_asn"
          }
        ],
      }
     

If you then wanted to remove the second peer, you would use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/project_id/regions/region_name/routers/cloud_router_name
      {
        "md5AuthenticationKeys": [
          {
            "name":  "first_key_name",
          }
        ],
        "bgpPeers": [
          {
            "name": "first_peer",
            "md5AuthenticationKeyName": "first_key_name",
            "interfaceName": "first_interface",
            "ipAddress": "first_address",
            "peerIpAddress": "first_peer_interface",
            "peerAsn": "first_peer_asn"
          }
        ],
      }
     

## What's next

  * [Set up MD5 authentication on third-party routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/md5-interop)

  * [Update the base advertised route priority](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority)

  * [Disable or remove BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp)

  * [View router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details)

  * [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
