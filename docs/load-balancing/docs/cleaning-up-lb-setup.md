---
url: https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup/
title: Clean up a load balancing setup \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:39.090952+00:00
---

# Clean up a load balancing setup  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Clean up a load balancing setup Stay organized with collections  Save and categorize content based on your preferences. 

After you set up a load balancer, you can delete the resources that you made so that you aren't billed for them in the future. If these resources were created within their own project, you can delete the entire project. Otherwise, you can delete the resources individually.

## Delete the project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project, when you delete it, you also delete any other work that you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as a `YOUR_PROJECT_ID.REGION_ID.r.appspot.com` URL, delete selected resources inside the project instead of deleting the project. 



###  Console

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. In the project list, select the project that you want to delete, and then click delete**Delete**.

  3. In the dialog, type the `PROJECT_ID`, and then click **Shut down** to delete the project.




###  gcloud 

Run the following command, replacing `PROJECT_ID` with your project ID:
    
    
    gcloud projects delete PROJECT_ID
    

## Delete individual resources

If you don't want to delete the entire project, you can delete the individual resources that you created for your load balancer setup.

### Delete the load balancer

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Select the checkbox next to your load balancer name.

  3. Click delete**Delete**.

  4. Select the checkboxes next to all the additional resources, including backend services, backend buckets, health checks, and SSL certificates.

  5. Click **Delete**.


**Note:** If you try to delete a regional external passthrough Network Load Balancer with target pool backends by using a mixed TCP/UDP configuration from the Google Cloud console, you might get the following message: **This load balancer has TCP/UDP mixed configuration. Use Google Cloud CLI or REST API to delete it.** You first need to remove the individual resources (forwarding rules, target proxy, URL map, health checks or target pool) by using the Google Cloud CLI or REST API depending on whatever is configured for the load balancer.

### Delete the Cloud Storage buckets

If you created backend buckets, deleting the load balancer and backend buckets doesn't delete the underlying Cloud Storage buckets or the objects contained within them.

For information about deleting Cloud Storage buckets and the objects contained within them, see [Deleting buckets](https://docs.cloud.google.com/storage/docs/deleting-buckets).

### Delete the instance groups

If you created instance groups, delete them. Deleting the instance group also deletes the individual VMs.

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. To select all instance groups, select the checkbox next to **Name** , and then click delete**Delete**.

  3. In the confirmation window, click delete**Delete**.




### Delete the VM instances

If you created standalone VM instances, delete them.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox next to **Name** to select all instances, and then click delete**Delete**.

  3. In the confirmation window, click delete**Delete**.




### Delete the NEGs

If you created any network endpoint groups (NEGs), delete them. Deleting a NEG also deletes [network endpoints](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups/listNetworkEndpoints) contained in the NEG.

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Locate the network endpoint group that you want to delete.

  3. In that row, click delete**Delete**.




### Release reserved IP addresses

If your load balancer uses one or more reserved IP addresses, make sure you delete them.

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Select the checkboxes next to your reserved IP addresses.

  3. Click the **More actions** menu (more_vert), and then click **Release static address**.

  4. In the confirmation window, click **Release**.




### Delete the VPC network

If you created a custom VPC network, delete it. Deleting a VPC network also deletes its subnetworks, routes, and firewall rules.

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click your custom VPC network.

  3. On the network details page, click **Delete VPC network**.

  4. In the confirmation window, click delete**Delete**.




### Delete custom firewall rules in the default VPC network

If you created custom firewall rules in the default VPC network, delete them.

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Select the checkboxes next to your custom firewall rules.

  3. Click delete**Delete**.

  4. In the confirmation window, click delete**Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
