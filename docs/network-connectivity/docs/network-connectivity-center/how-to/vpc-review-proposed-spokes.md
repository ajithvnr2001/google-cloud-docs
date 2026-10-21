---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes/
title: Review proposed VPC spokes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:04.748026+00:00
---

# Review proposed VPC spokes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Review proposed VPC spokes Stay organized with collections  Save and categorize content based on your preferences. 

As a hub administrator, you can review and subsequently accept or reject pending VPC spokes that a spoke administrator has proposed from a different project from the hub.

After a spoke is accepted or rejected, you can reject it or accept it as many times as necessary by running the commands described on this page. As a hub administrator, you can also reject spokes that have previously been accepted at any time. If a previously accepted spoke is rejected, it loses all its connectivity with other spokes after the rejection is complete.

Additionally, you can accept or reject updates to VPC spokes on the hub that are from different projects. The following spoke properties require your approval to update:

  * Whether the spoke exports IPv6 subnet ranges

  * Which subnet IPv4 address ranges are exported from the VPC spoke to the hub




For more information about updating spokes, see [Update a spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update-spoke).

You can also set up _auto-accept_ projects for [spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups) into a hub. Auto-accept lets you automatically accept into the hub any spokes or spoke updates that are in auto-accept projects, without having to review each spoke proposal.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.listSpokes` to list spokes
  * `networkconnectivity.groups.acceptSpoke` on the hub to accept a spoke
  * `networkconnectivity.groups.rejectSpoke` on the hub to reject a spoke
  * `networkconnectivity.groups.rejectSpokeUpdate` on the hub to reject a spoke update
  * `networkconnectivity.groups.acceptSpokeUpdate` on the hub to accept a spoke update
  * `networkconnectivity.groups.list` on the hub to list groups
  * `networkconnectivity.groups.get` on the hub to get a group
  * `networkconnectivity.groups.update` on the hub to update a group



**Roles**

  * `roles/networkconnectivity.hubAdmin`



## View proposals pending review

This section describes how to list all spoke proposals and view the details of an update proposal in Network Connectivity Center (NCC).

**Note:** You can view proposals for updates to existing spokes only by using the Google Cloud CLI or by calling the Network Connectivity API.

For spoke updates, you can compare existing values with proposed values to decide whether to accept or reject the updates.

###  Console 

  1. In the Google Cloud console, go to **Network Connectivity Center**.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project that contains the hub for which you want to list the existing spokes.

  3. In the **Hub** tab, select the hub.

  4. Click the **Spoke** tab. All the spokes attached to that hub are listed.

  5. To view the status for a specific spoke, check the **Spoke status** column.

     * New proposed spokes that are pending review have an `Inactive, pending` status.
     * Updates to existing spokes that are pending review have an `Active, updates pending review` status. The **Spoke details** page for a given spoke displays the proposed updates in the `VPC spoke filter update` message.



###  gcloud 

  * To list proposals pending review, run the [`gcloud network-connectivity hubs list-spokes` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/list-spokes).
        
        gcloud network-connectivity hubs list-spokes HUB_NAME \
            --filter="reasons:STATE_REASON" \
            --format=yaml
        

Replace the following:

    * `HUB_NAME`: the name of the hub for which you want to review proposals, such as `my-hub`.
    * `STATE_REASON`: the [state reason](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status#spoke_states) to filter on: 
      * `PENDING_REVIEW`: Use this value to view new spoke proposals.
      * `UPDATE_PENDING_REVIEW`: Use this value to view proposals for updates to existing spokes. For spoke update proposals, the command output shows the proposed update in the `proposed_include_export_ranges` field.



###  API 

  * To list proposals that are pending review for a hub, use the [`networkconnectivity.hubs.listSpokes` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes).
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:listSpokes?filter=reasons=STATE_REASON
        

Replace the following values:

    * `PROJECT_ID`: the project ID of the project that contains the spokes to list
    * `HUB_NAME`: the name of the hub for which you want to view spoke proposals pending review
    * `STATE_REASON`: the [state reason](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status#spoke_states) to filter on: 
      * `PENDING_REVIEW`: Use this value to view new spoke proposals.
      * `UPDATE_PENDING_REVIEW`: Use this value to view proposals for updates to existing spokes. For spoke update proposals, the response shows the proposed update in the `proposed_include_export_ranges` field.



## Accept proposals for a new spoke or an update to an existing spoke

This section describes how to accept proposals for new spokes or updates to existing spokes.

Note: You can't accept a proposed producer VPC spoke on the hub until you accept the associated VPC spoke for the peered consumer network. **Note:** You can accept proposed updates to existing spokes only by using the Google Cloud CLI or by calling the Network Connectivity API.

###  Console 

  1. In the Google Cloud console, go to **Network Connectivity Center**.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project that contains the hub for which you want to list the existing spokes.

  3. On the **Hub** tab, select the hub.

  4. Click the **Spoke** tab. All the spokes attached to that hub are listed.

  5. To view details for a specific spoke, click the spoke name.

If the spoke is an existing spoke with proposed updates, the **Spoke details** page displays the proposed updates.

  6. To accept the proposal, click **Accept spoke**.

     * For new spokes, click **Accept spoke**.
     * For existing spokes, click **Accept updates**.

The NCC page updates to show details about the spokes that you accepted and the spoke status changes to `Active`.




You can also select multiple spokes for a bulk accept. However, as the hub administrator, before accepting a spoke, you must check the **VPC spoke filters** for each spoke by clicking the individual spoke name and checking the spoke details.

###  gcloud 

  * To accept a proposed spoke to connect to a hub, run the [`gcloud network-connectivity hubs accept-spoke` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke).
        
        gcloud network-connectivity hubs accept-spoke HUB_NAME \
              --spoke=SPOKE_URI
        

Replace the following:

    * `HUB_NAME`: the name of the hub that is receiving the spoke proposal
    * `SPOKE_URI`: the URI of the spoke that you want to accept into the hub
  * To accept proposed updates to a spoke connected to a hub, follow these steps:

    1. Follow the Google Cloud CLI instructions to list spokes and record the spoke's `etag` value from the output.

    2. Run the [`gcloud network-connectivity hubs accept-spoke-update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke-update).
           
           gcloud network-connectivity hubs accept-spoke-update HUB_NAME \
               --spoke=SPOKE_URI \
               --spoke-etag=ETAG
           

Replace the following:

       * `HUB_NAME`: the name of the hub that is receiving the spoke proposal
       * `SPOKE_URI`: the URI of the spoke that you want to accept into the hub
       * `ETAG`: the `etag` value of the VPC spoke for which you want to accept updates



###  API 

  * To accept a proposed spoke, use the [`networkconnectivity.hubs.acceptSpoke` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/acceptSpoke).
        
        POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:acceptSpoke
        
          {
          "spokeUri": SPOKE_URI
          }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that contains the hub
    * `HUB_NAME`: the name of the hub that is receiving the spoke proposal
    * `SPOKE_URI`: the URI of the spoke that you want to accept into the hub
  * To accept proposed updates to a spoke connected to a hub, follow these steps:

    1. Follow the API instructions to list spokes and record the spoke's `etag` value from the output.

    2. To accept proposed updates to a spoke, use the [`networkconnectivity.hubs.acceptSpokeUpdate` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/acceptSpokeUpdate).
           
           POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:acceptSpokeUpdate
           
           {
           "spokeUri": SPOKE_URI,
           "spokeEtag": ETAG
           }
           

Replace the following:

       * `PROJECT_ID`: the ID of the project that contains the hub
       * `HUB_NAME`: the name of the hub that is receiving the spoke proposal
       * `SPOKE_URI`: the URI of the spoke that you want to accept into the hub
       * `ETAG`: the `etag` value of the VPC spoke for which you want to accept updates



## Reject a spoke proposal

This section describes how to reject proposals for new spokes or updates to existing spokes.

As a hub administrator, you can also reject spokes that have previously been accepted at any time. If a previously accepted spoke is rejected, it loses all its connectivity with other spokes after the rejection is complete.

Note: You can't reject a VPC spoke that is associated with an active producer VPC spoke on the hub. To reject an associated VPC spoke, first reject the producer VPC spoke. **Note:** You can reject proposed updates to existing spokes only by using the Google Cloud CLI or by calling the Network Connectivity API.

###  Console 

  1. In the Google Cloud console, go to **Network Connectivity Center**.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project that contains the hub for which you want to list the existing spokes.

  3. In the **Hub** tab, select the hub.

  4. Click the **Spoke** tab. All the spokes attached to that hub are listed.

  5. To view details for a specific spoke, click the spoke name.

If the spoke is an existing spoke with proposed updates, the **Spoke details** page displays the proposed updates.

  6. Depending on whether it's a new spoke or an update, do the following:

     * For new spoke proposals:

       1. Click **Reject spoke**.
       2. In the **Reject spoke?** dialog, confirm the rejection and optionally, provide a reason for the rejection.
       3. Click **Reject** again. The NCC page updates to show details about the spokes that you rejected, and the spoke status shows as `Inactive, rejected`.
     * For existing spoke updates:

       1. Click **Reject updates**.
       2. In the **Reject updates?** dialog, confirm the rejection and optionally, provide a reason for the rejection.
       3. Click **Reject** again. The NCC page updates to show details about the spokes that you rejected, and the spoke status shows as `Active, updates rejected`.



###  gcloud 

  * To reject a proposed spoke from connecting to a hub, run the [`gcloud network-connectivity hubs reject-spoke` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke).
        
        gcloud network-connectivity hubs reject-spoke HUB_NAME \
            --spoke=SPOKE_URI \
            --details=REJECT_REASON
        

Replace the following:

    * `HUB_NAME`: the name of the hub that contains the spoke that you want to reject
    * `SPOKE_URI`: the URI of the VPC spoke that you want to reject
    * `REJECT_REASON`: Optional: the reason for which you rejected the spoke
  * To reject proposed updates to an existing spoke, follow these steps:

    1. Follow the Google Cloud CLI instructions to list spokes and record the spoke's `etag` value from the output.

    2. Run the [`gcloud network-connectivity hubs reject-spoke-update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke).
           
           gcloud network-connectivity hubs reject-spoke-update HUB_NAME \
               --spoke=SPOKE_URI \
               --spoke-etag=ETAG \
               --details=REJECT_REASON
           

Replace the following:

       * `HUB_NAME`: the name of the hub that contains the spoke for which you want to reject updates
       * `SPOKE_URI`: the URI of the VPC spoke for which you want to reject updates
       * `ETAG`: the `etag` value of the VPC spoke for which you want to reject updates
       * `REJECT_REASON`: Optional: the reason for which you rejected the spoke



###  API 

  * To reject a proposed spoke, use the [`networkconnectivity.hubs.rejectSpoke` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/rejectSpoke).
        
        POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:rejectSpoke
        
          {
          "spokeUri": SPOKE_URI,
          "requestId": REQUEST_ID,
          "details": SPOKE_DETAILS
          }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that contains the hub
    * `HUB_NAME`: the name of the hub that contains the spoke that you want to reject
    * `SPOKE_URI`: the URI of the spoke that you want to reject from the hub
    * `REQUEST_ID`: Optional: the request ID to identify requests
    * `SPOKE_DETAILS`: Optional: the additional details that you provide, such as, reason for rejection
  * To reject proposed updates to an existing spoke, follow these steps:

    1. Follow the API instructions to list spokes and record the spoke's `etag` value from the output.

    2. Use the [`networkconnectivity.hubs.rejectSpokeUpdate` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/rejectSpokeUpdate).
           
           POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:rejectSpokeUpdate
           
           {
           "spokeUri": SPOKE_URI,
           "spokeEtag": ETAG,
           "requestId": REQUEST_ID,
           "details": SPOKE_DETAILS
           }
           

Replace the following:

       * `PROJECT_ID`: the ID of the project that contains the hub
       * `HUB_NAME`: the name of the hub that contains the spoke for which you want to reject updates
       * `SPOKE_URI`: the URI of the spoke for which you want to reject updates
       * `ETAG`: the `etag` value of the VPC spoke for which you want to reject updates
       * `REQUEST_ID`: Optional: the request ID to identify requests
       * `SPOKE_DETAILS`: Optional: the additional details that you provide, such as, reason for rejection



## Manage auto-accept projects for spoke groups

To automatically connect spokes to a hub without the need for individual spoke proposal review, you can set up auto-accept for spoke groups. To complete this task, you need the project IDs for which you want to set up automatic acceptance of spokes.

To add or remove auto-accept projects for spoke groups, follow these steps.

###  Console 

  1. In the Google Cloud console, go to **Network Connectivity Center**.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project that contains the hub for which you want to list the existing spokes.

  3. In the **Hub** tab, select the hub.

  4. In the **Groups** tab, click **Edit** next to the group name that you want to update.

  5. On the **Edit group** page, under **Auto-accept projects** , follow these steps for the action you want to take:

     * To add auto-accept for specific projects, enter the project ID for the appropriate project in the **Project ID 1** field. To add multiple project IDs, click **Add project ID** and enter the project ID.

     * To remove project IDs from the list, click delete**Delete** next to the project ID that you want to remove.

  6. Click **Save**.

The NCC **Hub details** page updates to show details about the auto-accept projects that you added, edited, or removed.




###  gcloud 

  * To set up auto-accept for spoke groups, run the [`gcloud network-connectivity hubs groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update).
        
        gcloud network-connectivity hubs groups update GROUP_NAME \
          --hub=HUB_NAME \
          --description=DESCRIPTION \
          --add-auto-accept-projects=PROJECT_ID_1,PROJECT_ID_2
        

Replace the following:

    * `GROUP_NAME`: the name of the group that you want to set up auto-accept for
    * `HUB_NAME`: the name of the hub that contains the spoke that you want to accept
    * `DESCRIPTION`: Optional: a description of the spoke group
    * `PROJECT_ID`: a comma-separated list of project IDs for which auto-accept is to be enabled. Use `*` to represent all projects.
  * To clear auto-accept for a hub entirely, run the [`gcloud network-connectivity hubs groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update) with the `--clear-auto-accept-projects` flag.
        
        gcloud network-connectivity hubs groups update GROUP_NAME \
          --hub=HUB_NAME \
          --description=DESCRIPTION \
          --clear-auto-accept-projects
        

Replace the following:

    * `GROUP_NAME`: the name of the group that you want to update
    * `HUB_NAME`: the name of the hub that contains the spoke that you want to update
    * `DESCRIPTION`: Optional: a description of the spoke group
  * To remove auto-accept for specific projects, run the [`gcloud network-connectivity hubs groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update) with the `--remove-auto-accept-projects` flag.
        
        gcloud network-connectivity hubs groups update GROUP_NAME \
          --hub=HUB_NAME \
          --description=DESCRIPTION \
          --remove-auto-accept-projects=PROJECT_ID_1,PROJECT_ID_2
        




Replace the following:

  * `GROUP_NAME`: the name of the group that you want to update
  * `HUB_NAME`: the name of the hub that contains the spoke that you want to reject
  * `DESCRIPTION`: Optional: a description of the hub
  * `PROJECT_ID`: a comma-separated list of project IDs that you want to remove from the auto-accept list.



###  API 

To update the auto-accept projects list, use the [`networkconnectivity.hubs.rejectSpoke` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/rejectSpoke).
    
    
      PATCH https://networkconnectivity.googleapis.com/v1/projects/test-project/locations/global/hubs/HUB_NAME/groups/center?updateMask=auto_accept.auto_accept_projects
    
      {
       "auto_accept": {
            "auto_accept_projects": ["PROJECT_ID_1", "PROJECT_ID_2"],
       }
      }
    
    

Replace the following:

  * `HUB_NAME`: the name of the hub that contains the spoke that you want to reject
  * `PROJECT_ID`: a comma-separated list of project IDs that you want to remove from the auto-accept list.



## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for NCC issues, see [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
