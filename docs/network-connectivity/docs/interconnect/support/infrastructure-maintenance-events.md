---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events/
title: Infrastructure maintenance events \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:20.079861+00:00
---

# Infrastructure maintenance events  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Infrastructure maintenance events Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes infrastructure maintenance events and how they can affect Cloud Interconnect connections.

## What infrastructure maintenance events are

Infrastructure maintenance events are times that Google Cloud performs maintenance on network equipment, including equipment for Cloud Interconnect. We provide notification, when possible, so that you can plan for the infrastructure maintenance event and prevent downtime.

### Planned maintenance

Google Cloud performs many different types of maintenance events. The differences between the types of maintenance events are simplified, so that maintenance events of different types look the same in the Google Cloud console. Most types of planned maintenance events occur between 10 PM to 5 AM local time to where the network device is located. For example, if the device is located in asia-south1, then planned maintenance typically occurs between 10 PM and 5 AM India Standard Time (UTC+5:30). Planned maintenance events don't have a set interval between occurrences, but generally occur several times a year.

One type of planned maintenance event, a physical migration, happens Monday to Friday, 9am to 5pm Eastern Time.

### Unplanned maintenance

Emergency, or unscheduled maintenance events, might also occur. Emergency events are irregular and unplanned-for events that can affect Cloud Interconnect connections. Unfortunately, emergency events can happen at any time, without warning. Google recommends that you create high availability hybrid network topologies to mitigate network outages caused by emergency maintenance events.

The total capacity that is impacted by an unplanned maintenance event varies based on the nature of the event. It could be up to 100% of your capacity on one or more of your Cloud Interconnect connections.

### Urgent maintenance

Urgent maintenance events are similar to planned maintenance events, but they are scheduled less than 14 days in advance. In addition, they impact up to 100% of the total capacity on each of your affected Cloud Interconnect connections.

### Single links and SLA

A single link in one edge availability domain carries no [SLA](https://cloud.google.com/network-connectivity/docs/interconnect/sla). To prevent loss of access to your services during maintenance, make sure that you provision two links in different edge availability domains. For more information, see [Create redundant Cloud Interconnect connections with sufficient capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity).

## Receiving event notifications

You receive notifications for planned, unplanned, and urgent maintenance events.

Notifications for planned maintenance events are sent at least 14 days ahead of the event to the email listed in the `nocContactEmail` field of the Cloud Interconnect object and are displayed in the [`interconnects.get` API method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/get). For more information, see Assigning contacts for event notifications.

During unplanned or urgent events, you might receive a notification for an interruption but not have sufficient time to redirect traffic. To reduce the chances of traffic disruptions due to emergency interruptions, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).

Maintenance events might not happen as planned. We send updated event notifications if a maintenance event is rescheduled or canceled.

Notifications don't appear in Google Cloud console for Partner Interconnect users.

## Assigning contacts for event notifications

Cloud Interconnect notifies the project owners and also uses the [Essential Contacts API](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest) to send notifications about maintenance events. If you don't assign a technical contact to a project, then notifications are sent to [fallback contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories), which are based on IAM roles.

To ensure that you receive proper notification about maintenance events, specify at least one technical contact for any project that hosts a Cloud Interconnect connection or VLAN attachment.

For more information about assigning technical contacts for a project, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## Event notification properties

This section applies to Dedicated Interconnect, Cross-Cloud Interconnect, and Cross-Site Interconnect.

Prior to a _planned_ infrastructure maintenance event, users receive the following notifications:

  * An email is sent to all Cloud Interconnect connection project owners as soon as an impacting maintenance is scheduled.

  * An email is sent to the address listed in the **`nocContactEmail`** field of the Cloud Interconnect object. You can find and edit this object in the Google Cloud console on the Cloud Interconnect details page, or by using the following Google Cloud CLI command:
        
        gcloud compute interconnects describe my-interconnect
        

  * An email is sent to any [technical contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) listed for the project that hosts the Cloud Interconnect connection.




During an _unplanned_ or _urgent_ infrastructure maintenance event, users receive the following notifications:

  * An email is sent to all Cloud Interconnect connection project owners as soon as an impacting maintenance is scheduled.

  * An email is sent to the address listed in the **`nocContactEmail`** field of the Cloud Interconnect object.

  * An email is sent to any [technical contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) listed for the project that hosts the Cloud Interconnect connection.




### Partner Interconnect event notifications

Prior to a scheduled infrastructure maintenance event, Partner Interconnect users receive the following notifications:

  * An email is sent to any [technical contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) for the project that hosts the VLAN attachment.

  * An email is sent to all project owners for the project that hosts the VLAN attachment.




## Outage statuses

Event emails sent to project owners and `nocContactEmail` contacts include a section titled "Outage Status". The following describes the possible outage status states:

  * **Updated** : a previously scheduled maintenance event that is updated or rescheduled.

  * **Overrun** : a previously scheduled maintenance event that is in progress and taking longer than expected to complete.

  * **Completed** : a completed maintenance event.

  * **Canceled** : a previously scheduled maintenance event that is canceled.

  * **New** : a new maintenance event.

  * **No change** : a previously scheduled maintenance event that is still scheduled as previously planned.




## View maintenance events

**Note:** You can't view unplanned maintenance events with the Google Cloud CLI or the API. You can view urgent maintenance requests with the Google Cloud CLI and the API, but they're shown as planned maintenance requests.

Select one of the following options:

### gcloud

To display information about your connection, including upcoming planned maintenance events, run the following command:
    
    
    gcloud compute interconnects describe INTERCONNECT_NAME
    

Replace `INTERCONNECT_NAME` with the name of the Cloud Interconnect.

The output is similar to the following; look for `expectedOutages`:
    
    
    adminEnabled: true
    availableFeatures:
    - IF_MACSEC
    circuitInfos:
    - customerDemarcId: demarc-0
      googleCircuitId: circuit-0
      googleDemarcId: local-demarc-0
    creationTimestamp: '2021-12-15T17:02:48.829-08:00'
    customerName: Cymbal Group
    description: Interconnect connection
    expectedOutages:
    - description: ''
      endTime: '1705520100000'
      issueType: IT_OUTAGE
      name: pcr-764913
      source: NSRC_GOOGLE
      startTime: '1705501500000'
      state: CANCELLED
    - description: ''
      endTime: '1707304200000'
      issueType: IT_OUTAGE
      name: pcr-777490
      source: NSRC_GOOGLE
      startTime: '1707285600000'
      state: COMPLETED
    googleIpAddress: 192.0.2.0/24
    googleReferenceId: '6006458259035'
    id: '249691500371717847'
    interconnectType: IT_PRIVATE
    kind: compute#interconnect
    labelFingerprint: 42WmSpB8rSM=
    linkType: LINK_TYPE_ETHERNET_10G_LR
    location: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/interconnectLocations/sjc-zone1-6
    macsec:
      failOpen: false
      preSharedKeys:
      - name: key-1
        startTime: '2023-08-08T21:09:21.385Z'
    macsecEnabled: false
    name: cymbal-group-interconnect
    nocContactEmail: cloudysanfrancisco@gmail.com
    operationalStatus: OS_ACTIVE
    peerIpAddress: 192.0.2.0/24
    provisionedLinkCount: 1
    requestedLinkCount: 1
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/interconnects/INTERCONNECT_NAME
    state: ACTIVE
    

### REST API

To list information about your connection, including upcoming maintenance events, use [interconnects.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/interconnects/INTERCONNECT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID that the Cloud Interconnect is located in

  * `INTERCONNECT_NAME`: the name of the Cloud Interconnect




The output is similar to the following:
    
    
    {
    "kind": "compute#interconnect",
    "description": "Interconnect connection",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/interconnects/INTERCONNECT_NAME",
    "id": "249691500371717847",
    "creationTimestamp": "2021-12-15T17:02:48.829-08:00",
    "name": "INTERCONNECT_NAME",
    "location": "https://www.googleapis.com/compute/v1/projects/INTERCONNECT_NAME/global/interconnectLocations/sjc-zone1-6",
    "linkType": "LINK_TYPE_ETHERNET_10G_LR",
    "requestedLinkCount": 1,
    "interconnectType": "IT_PRIVATE",
    "adminEnabled": true,
    "nocContactEmail": "",
    "customerName": "Cymbal Group",
    "operationalStatus": "OS_ACTIVE",
    "provisionedLinkCount": 1,
    "peerIpAddress": "192.0.2.0/24",
    "googleIpAddress": "192.0.2.0/24",
    "googleReferenceId": "6006458259035",
    "expectedOutages": [
      {
        "name": "pcr-764913",
        "description": "",
        "source": "NSRC_GOOGLE",
        "state": "CANCELLED",
        "issueType": "IT_OUTAGE",
        "startTime": "1705501500000",
        "endTime": "1705520100000"
      },
      {
        "name": "pcr-777490",
        "description": "",
        "source": "NSRC_GOOGLE",
        "state": "COMPLETED",
        "issueType": "IT_OUTAGE",
        "startTime": "1707285600000",
        "endTime": "1707304200000"
      }
    ],
    "circuitInfos": [
      {
        "googleCircuitId": "circuit-0",
        "googleDemarcId": "local-demarc-0",
        "customerDemarcId": "demarc-0"
      }
    ],
    "labelFingerprint": "42WmSpB8rSM=",
    "state": "ACTIVE",
    "macsec": {
      "preSharedKeys": [
        {
          "name": "key-1",
          "startTime": "2023-08-08T21:09:21.385Z"
        }
      ],
      "failOpen": false
    },
    "macsecEnabled": false,
    "availableFeatures": [
      "IF_MACSEC"
    ]
    }

## View maintenance events in Unified Maintenance

You can use Unified Maintenance to view Cloud Interconnect infrastructure maintenance events, and you can configure Unified Maintenance to send alerts and notifications about maintenance events. Notifications don't appear in Unified Maintenance for Partner Interconnect users.

Follow the steps on the [Configure alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications) page, but use one of the following inclusion filters when you are prompted to create one:

  * This filter includes only planned maintenance notifications:
        
        log_id("maintenance.googleapis.com/maintenance_events") AND jsonPayload.resource.type="compute.googleapis.com/Interconnect" AND jsonPayload.maintenance.title =~ "Planned Outage.*"
        

  * This filter includes only urgent maintenance notifications:
        
        log_id("maintenance.googleapis.com/maintenance_events") AND jsonPayload.resource.type="compute.googleapis.com/Interconnect" AND jsonPayload.maintenance.title =~ "Urgent Maintenance.*"
        

  * This filter contains only unplanned maintenance notifications:
        
        log_id("maintenance.googleapis.com/maintenance_events") AND jsonPayload.resource.type="compute.googleapis.com/Interconnect" AND jsonPayload.maintenance.title =~ "Unplanned Outage.*"
        




Alternatively, to view maintenance events with the _Scheduled_ state see [View resource maintenances by using the API](https://docs.cloud.google.com/unified-maintenance/docs/view-maintenance-api).
    
    
    $ curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://maintenance.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/resourceMaintenances?filter=resource.type%3D%22compute.googleapis.com/Interconnect%22%20AND%20state%3D%22SCHEDULED%22"
    

## Next steps

  * Implement Cloud Interconnect [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices)

  * [Manage contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
