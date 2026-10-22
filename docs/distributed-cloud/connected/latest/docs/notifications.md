---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/notifications/
title: Order communications and alerts \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:55.762774+00:00
---

# Order communications and alerts  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/notifications/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Order communications and alerts Stay organized with collections  Save and categorize content based on your preferences. 

Follow your Google Distributed Cloud connected hardware procurement journey from the initial order to final activation. Google and its partners coordinate with you using the contact details provided during order placement. The primary channel for status updates and information requests is the **Comments** tab in the Google Cloud console.

## Order lifecycle and coordination

As your order progresses through different stages, Google or its partners contact you to coordinate delivery, installation, and configuration. Ensure that your contact information is correct.

The following table summarizes the milestones and coordination steps during the procurement and delivery process.

Order state | Milestone | Coordination details | Required action  
---|---|---|---  
**Draft** | Order preparation | Your order is being drafted in the Google Cloud console. | Complete order details, network configuration, and hardware selection.  
**In review** | Order review | A Google Cloud sales representative might contact you to review and finalize your order. | Work with your representative to finalize the configurations.  
**Accepted** | Order accepted | Google accepts the order and relays it to your Google-certified SI for fulfillment. | None.  
**Building Hardware** | Hardware provisioning | Your Google-certified SI builds and configures the hardware. | Prepare your site (power, space, cooling) according to the [installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/requirements).  
**Shipping Hardware** | Delivery scheduling | The logistics carrier or delivery partner working with your Google-certified SI contacts you using the details provided on the order. | Coordinate with the carrier to schedule the delivery date and time.  
**Installing** | On-site installation | Google-certified technicians or partners coordinate access and perform the physical installation. | Ensure site access is granted for the technicians. Prepare network ports.  
**Accepted** , **Shipping Hardware** , or **Installing** | Schedule change | You can update preferences in the Google Cloud console or coordinate with your Google contact. | Edit delivery or installation preferences in the Google Cloud console.  
**Missing info** or **Action required** | Fulfillment blocker | The Google team posts a request for details, such as invalid IP settings or a missing Customer Intake Questionnaire (CIQ), in the **Comments** tab. | View comments in the Google Cloud console and respond to them to unblock fulfillment.  
**Completed** | Activation | Check the Google Cloud console to confirm that hardware is online and configured. | Verify cluster availability in the Google Cloud console, and start deploying workloads. Billing begins.  
  
## Required actions

This section explains the actions you must take during the procurement and delivery process.

### Respond to "Missing info" or "Action required" status

If your order status changes to **Missing info** or **Action required** , or if you receive a comment on your order, respond to the comment to unblock the order.

  1. In the Google Cloud console, go to the **Orders** page. 

[Go to Orders](https://console.cloud.google.com/distributed-cloud/edgezones/order-management/orders?project=_)

  2. Select your Google Cloud project.
  3. Click the order that requires attention.
  4. To view the request from the Google fulfillment team, open the **Comments** tab.
  5. Enter your response.
  6. Click **Comment**.



### Schedule delivery

When the hardware is ready to ship, the logistics partner or delivery carrier working with your Google-certified SI contacts you to schedule delivery.

  1. Reply to the logistics carrier promptly to coordinate a delivery slot.
  2. Ensure that an authorized representative is present at the delivery location during the agreed window.
  3. Verify that the delivery path is clear and can accommodate the shipment size.



### Prepare for installation

Prior to the scheduled installation date:

  1. Provide the technician details to your facility's security team to pre-authorize access.
  2. Ensure that the target rack space is ready and meets the physical and environmental requirements.
  3. Confirm that the network ports on your switches or routers are patched and configured according to the network design. For more information, see [Networking](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/requirements#networking).
  4. Ensure that your network administrator is available to assist with network integration and troubleshooting during turnup.



### Handle schedule changes

If you need to change the scheduled delivery or installation date, or if Google requests a change:

  1. In the Google Cloud console, go to the **Orders** page. 

[Go to Orders](https://console.cloud.google.com/distributed-cloud/edgezones/order-management/orders?project=_)

  2. Select your Google Cloud project.
  3. Click the order that requires attention.
  4. To change the delivery date, for **Delivery preference** , click **Edit delivery preference**. To change the installation date, for **Installation preference** , click **Edit installation preference**.
  5. For **New delivery preference** or **New installation preference** , select a date, and then click **Save**.



### Verify activation

When the installation is complete and the hardware is online:

  1. Confirm your hardware status based on your provisioning choice: 
     * **Pre-configured clusters** : Go to the **Clusters** page to verify that your clusters are visible and reporting a healthy status. 

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

     * **Self-configured clusters** : Go to the **Edge Zones** page to verify that your machines are online, and then create your clusters. 

[Go to Edge Zones](https://console.cloud.google.com/distributed-cloud/edgezones/list)

  2. Verify that you can access the clusters using `kubectl`. For more information, see [Configure kubectl connectivity](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/kubectl).
  3. Start [deploying workloads](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
