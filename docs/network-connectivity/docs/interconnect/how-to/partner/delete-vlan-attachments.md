---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/delete-vlan-attachments/
title: Delete VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:36.618036+00:00
---

# Delete VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/delete-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Delete VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

To disconnect your Virtual Private Cloud (VPC) network and on-premises network, you must delete the VLAN attachment for the Partner Interconnect connection. Work with your service provider to initiate the deletion. That way billing by Google and your service provider stops at the same time.

If you delete the VLAN attachment in Google Cloud first, the attachment is deleted and Google stops billing you for it. However, your service provider might not be aware of this change and might continue to charge you for the connection. Contact your service provider to ensure that they delete your connection and stop billing you.

After your service provider disconnects your VLAN attachment, the state of your attachment changes to `DEFUNCT`, and you can delete the attachment. Both Google and your service provider stop billing you.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment to delete. If your service provider disconnected your attachment, its status is `Defunct`. If it's in any other state, you can still delete the attachment, but contact your service provider to make sure they're aware of this change.

  3. On the **VLAN attachment details** page, click **Delete**.

  4. Click **Delete** to confirm.




###  gcloud 

  1. Describe the VLAN attachment to check whether your service provider disconnected it; if they did, the state of the attachment is `DEFUNCT`. If the state of the attachment is in any other state, you can still delete the attachment, but contact your service provider to make sure they're aware of this change.
         
         gcloud compute interconnects attachments describe my-attachment \
            --region us-central1
         

  2. Delete the VLAN attachment:
         
         gcloud compute interconnects attachments delete my-attachment
            --region us-central1
         




## What's next

  * To create a Partner Interconnect connection, see the [Partner Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Partner Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
