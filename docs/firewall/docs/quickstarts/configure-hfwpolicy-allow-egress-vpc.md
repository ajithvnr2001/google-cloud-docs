---
url: https://docs.cloud.google.com/firewall/docs/quickstarts/configure-hfwpolicy-allow-egress-vpc/
title: Configure a hierarchical firewall policy to allow egress traffic from a specific VPC network \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:13.540350+00:00
---

# Configure a hierarchical firewall policy to allow egress traffic from a specific VPC network  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/quickstarts/configure-hfwpolicy-allow-egress-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Configure a hierarchical firewall policy to allow egress traffic from a specific VPC network Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to create and configure a hierarchical firewall policy to allow egress traffic originating from a specific Virtual Private Cloud (VPC) network in your folder to a specific IP address as the destination. The firewall policy blocks all other egress traffic originating from your folder. The page walks through an example of creating two VPC networks, creating virtual machine (VM) instances in the VPC networks, setting up a hierarchical firewall policy with firewall rules, and then testing the firewall policy.

## Before you begin

  * Make sure that you have access to an [organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).
  * Make sure that you have the following Identity and Access Management (IAM) roles: 
    * [Organization Administrator role](https://docs.cloud.google.com/resource-manager/docs/access-control-org#resourcemanager.organizationAdmin) `(roles/resourcemanager.organizationAdmin)`
    * [Folder Admin role](https://docs.cloud.google.com/resource-manager/docs/access-control-folders#resourcemanager.folderAdmin) `(roles/resourcemanager.folderAdmin)`
    * [Project Creator role](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectCreator) `(roles/resourcemanager.projectCreator)`
    * [Project Deleter role](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectDeleter) `(roles/resourcemanager.projectDeleter)`
    * [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) 
    * [Compute Organization Firewall Policy Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`) 
  * Enable the Compute Engine and Identity-Aware Proxy (IAP) APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,iap.googleapis.com)




## Create a folder

Create a folder in your organization.

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Click **Create folder**.

  3. For **Folder name** , enter `test-folder`.

  4. In the **Organization** list, select the name of your organization resource.

  5. In the **Location** field, click **Browse** , and then select your organization resource.

  6. Click **Create**.




## Create a project

Create a project in the folder that you created in the preceding section.

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Click **Create project**.

  3. For **Project name** , enter `test-project`.

  4. Select a billing account for the project.

  5. In the **Organization** list, select the name of your organization resource.

  6. In the **Location** field, click **Browse** , expand your organization resource name, and then select **test-folder**.

  7. Click **Create**.




[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

## Create two custom VPC networks with IPv4 subnets

Create two custom mode VPC networks, `myvpc` with an IPv4-only subnet and `test-vpc` with two IPv4-only subnets, in the project that you created in the preceding section.

  1. In the Google Cloud console, on the project selector page, select **test-project**.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  3. Click **Create VPC network**.

  4. For **Name** , enter `myvpc`.

  5. For **Subnet creation mode** , select **Custom**.

  6. In the **New subnet** section, specify the following configuration parameters for a subnet:

     * **Name** : Enter `myvpc-subnet-1`.
     * **Region** : Select **us-central1**.
     * **IPv4 range** : Enter `10.0.0.0/24`.
  7. Click **Done** , and then click **Create**.

  8. To create another VPC network, click **Create VPC network**.

  9. For **Name** , enter `test-vpc`.

  10. For **Subnet creation mode** , select **Custom**.

  11. In the **New subnet** section, specify the following configuration parameters for the subnet, and then click **Done** :

     * **Name** : Enter `testvpc-subnet-1`.
     * **Region** : Select **us-central1**.
     * **IPv4 range** : Enter `10.0.0.0/16`.
  12. To add another subnet to the `test-vpc` network, click **Add subnet**.

  13. In the **New subnet** section, specify the following configuration parameters for the subnet, and then click **Done** :

     * **Name** : Enter `testvpc-subnet-ext`.
     * **Region** : Select **us-central1**.
     * **IPv4 range** : Enter `192.168.1.0/24`.
  14. Click **Create**.




## Create VMs

Create three VMs in the subnets that you configured in the preceding section.

### Create a VM in the `myvpc` network

Create a VM without an external IP address in the `myvpc` network.

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `myvpc-vm`.
     2. For **Region** , select `us-central1 (Iowa)`.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`myvpc`**
        * **Subnetwork** : **`myvpc-subnet-1 IPv4 (10.0.0.0/24)`**
        * **External IPv4 address** : **None**
     2. Click **Done**.
  4. Click **Create**.




### Create two VMs in the `test-vpc` network

Create two VMs, one without an external IP address and another with an external IP address. When you create the VM with an external IP address, pass a startup script to install and start an Apache web server in that VM.

Create a VM without an external IP address:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `testvpc-vm`.
     2. For **Region** , select `us-central1 (Iowa)`.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`test-vpc`**
        * **Subnetwork** : **`testvpc-subnet-1 IPv4 (10.0.0.0/16)`**
        * **External IPv4 address** : **None**
     2. Click **Done**.
  4. Click **Create**.




Create a VM with an ephemeral external IP address, and pass a startup script to install and start an Apache web server:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. For **Name** , enter `testvpc-apache-vm`.
     2. For **Region** , select `us-central1 (Iowa)`.
  3. In the navigation menu, click **Networking**.

     1. In the **Network interfaces** section, click **`default`** and specify the following configuration parameters: 
        * **Network** : **`test-vpc`**
        * **Subnetwork** : **`testvpc-subnet-ext IPv4 (192.168.1.0/24)`**
        * **External IPv4 address** : **Ephemeral**
     2. Click **Done**.
  4. In the navigation menu, click **Advanced** and enter the following script in the **Startup script** field:
         
         #! /bin/bash
         apt-get update
         apt-get install apache2 -y
         a2ensite default-ssl
         a2enmod ssl
         # Read VM network configuration:
         md_vm="http://169.254.169.254/computeMetadata/v1/instance/"
         vm_hostname="$(curl $md_vm/name -H "Metadata-Flavor:Google" )"
         filter="{print \$NF}"
         vm_network="$(curl $md_vm/network-interfaces/0/network \
         -H "Metadata-Flavor:Google" | awk -F/ "${filter}")"
         vm_zone="$(curl $md_vm/zone \
         -H "Metadata-Flavor:Google" | awk -F/ "${filter}")"
         # Apache configuration:
         echo "Page on $vm_hostname in network $vm_network zone $vm_zone" | \
         tee /var/www/html/index.html
         systemctl restart apache2
         

The preceding script deploys and starts an Apache web server in this VM.

  5. Click **Create**.

  6. Note the ephemeral external IP address assigned to this VM from the **VM instances** page. You need this external IP address later.




## Create a Cloud Router and a Cloud NAT gateway

In the previous section, in the `myvpc` network, you created the `myvpc-vm` VM without any external IP address. To enable the `myvpc-vm` VM to access the Apache web server running in `testvpc-apache-vm` over the public internet, create a Cloud Router and a Cloud NAT gateway on the same subnet where you created your `myvpc-vm` VM.

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create Cloud NAT gateway**.

**Note:** If this is the first Cloud NAT gateway that you're creating, click **Get started**. If you already have existing gateways, Google Cloud displays the **Create Cloud NAT** gateway button. To create another gateway, click **Create Cloud NAT** gateway.

  3. For **Gateway name** , enter `myvpc-gateway`.

  4. For **NAT type** , select **Public**.

  5. In the **Select Cloud Router** section, specify the following configuration parameters:

     * **Network** : Select **myvpc**.
     * **Region** : Select **us-central1 (Iowa)**.
     * **Cloud Router** : Click **Create new router**. 
       1. For **Name** , enter `myvpc-router`.
       2. Click **Create**.
  6. Click **Create**.




## Create a hierarchical firewall policy and add firewall rules

Create a hierarchical firewall policy and add the following firewall policy rules to it:

  * Enable IAP for all the VMs in `test-folder` to enable administrative access to the VMs.
  * Allow ingress traffic to all VMs in the `test-vpc` network.
  * Delegate the egress traffic from the `myvpc` network to the next rule in the hierarchy, which is the [`VPC firewall implied IPv4 rule egress all` rule](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules).
  * Deny egress traffic originating from all other VPC networks in `test-folder`.



To create a hierarchical firewall policy, follow these steps:

  1. In the Google Cloud console, go to the project selector page and select **test-folder**.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  3. Click **Create firewall policy**.

  4. In the **Configure policy** section, for **Policy name** , enter `fw-egress-specific-vpc`.

  5. For **Description** , enter `example-firewall-policy`.

  6. Click **Continue**.

  7. In the **Add rules** section, click **Continue**. You will add the firewall rules in the subsequent sections of this quickstart.

  8. In the **Associate policy with resources** section, click **Add**.

  9. Expand your organization, select **test-folder** , and then click **Add**.

**Warning:** Ensure that you associate the hierarchical firewall policy with `test-folder` only. Associating the policy with any other resource can be disruptive.
  10. Click **Create**.




### Add a firewall rule to enable IAP in all the VMs in the `test-folder`

To enable IAP to connect to all the VMs in the `test-folder`, you need a firewall rule in the hierarchical firewall policy with the following characteristics:

  * Applies to all VMs in the `test-folder` that you want to be accessible by using IAP TCP forwarding.
  * Allows ingress traffic from the IP address range `35.235.240.0/20`. This range contains all the IP addresses that IAP uses for TCP forwarding.
  * Allows connections to all ports that you want to be accessible by using IAP TCP forwarding, for example, port `22` for SSH.



To add the firewall rule, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **fw-egress-specific-vpc** , and then click **Add rule**.

  3. For **Priority** , enter `100`.

  4. For **Description** , enter `enable-iap`.

  5. For **Direction of traffic** , select **Ingress**.

  6. For **Action on match** , select **Allow**.

  7. In the **Source** section, for **IP ranges** , enter `35.235.240.0/20`.

  8. In the **Protocols and ports** section, select **Specified protocols and ports**.

  9. Select the **TCP** checkbox, and for **Ports** , enter `22`.

  10. Click **Create**.




### Add a firewall rule to allow ingress traffic in the `test-vpc` network

Add a firewall rule to allow incoming HTTP web traffic on TCP port 80 to all VMs in the `test-vpc` network:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **fw-egress-specific-vpc** and then click **Add rule**.

  3. For **Priority** , enter `200`.

  4. For **Description** , enter `allow-ingress-testvpc`.

  5. For **Direction of traffic** , select **Ingress**.

  6. For **Action on match** , select **Allow**.

  7. In the **Target** section, click **Add network**.

  8. Select the test project that contains the `test-vpc` network, and then select **test-vpc** as the network.

  9. In the **Source** section, for **IP ranges** , enter `0.0.0.0/0`.

  10. In the **Protocols and ports** section, select **Specified protocols and ports**.

  11. Select the **TCP** checkbox, and for **Ports** , enter `80`.

  12. Click **Create**.




### Add a firewall rule to delegate the egress traffic from the `myvpc` network to the next rule in the hierarchy

Add a firewall rule that uses the `goto_next` action to delegate the egress traffic from the `myvpc` network to the next rule in the firewall, which is the _implied IPv4 allow egress_ VPC firewall rule.

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **fw-egress-specific-vpc** and then click **Add rule**.

  3. For **Priority** , enter `300`.

  4. For **Description** , enter `delegate-egress-myvpc`.

  5. For **Direction of traffic** , select **Egress**.

  6. For **Action on match** , select **Go to next**.

  7. In the **Target** section, click **Add network**.

  8. Select the test project name that contains `myvpc`, and then select `myvpc` as the network.

  9. In the **Destination** section, for **IP ranges** , enter the ephemeral external IP address for the VM running the Apache web server. You have noted this IP address in the Create two VMs in the `test-vpc` network section.

  10. Click **Create**.




### Add a firewall rule to deny egress traffic originating from all other VPC networks

Finally, add a firewall rule that denies traffic egressing from all other VPC networks in `test-folder`.

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **fw-egress-specific-vpc** , and then click **Add rule**.

  3. For **Priority** , enter `400`.

  4. For **Description** , enter `block-egress-all-traffic`.

  5. For **Direction of traffic** , select **Egress**.

  6. For **Action on match** , select **Deny**.

  7. In the **Destination** section, for **IP ranges** , enter `0.0.0.0/0`.

  8. Click **Create**.




## Test the hierarchical firewall policy

After you have configured the hierarchical firewall policy, follow these steps to test the policy:

  1. Go to the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. From the project picker at the top of the page, select `test-project` where you have created the VPC networks.

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. In the **Connect** column for `myvpc-vm`, click **SSH**.

  5. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  6. To verify that the egress traffic to `testvpc-apache-vm` from `myvpc` is allowed, run the following command:
         
         curl <_external_ephemeral_IP_testvpc_apache_vm_ > -m 2
         

The preceding command returns the content that you have specified for the `index.html` page of the Apache web server, which means that egress connections from `myvpc` are allowed.

  7. To verify that the egress traffic is blocked from any other VPC network in the organization, do the following:

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. In the **Connect** column for `testvpc-vm`, click **SSH**.

     3. In the **SSH-in-browser** dialog, click **Authorize** , and wait for the connection to establish.

     4. To verify that the egress traffic from `testvpc-vm` to `testvpc-apache-vm` is blocked, run the following command:
            
            curl <_internal_IP_testvpc_apache_vm_ > -m 2
            

The preceding command returns a `Connection timed out` message, which is expected because you created a firewall rule to deny egress traffic from all VPC networks in the organization except from `myvpc`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, delete the individual resources, and then delete the project and the folder.

To delete the resources created in this quickstart, complete the following tasks.

### Delete the hierarchical firewall policy

  1. Go to the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. From the project picker at the top of the page, select `test-folder` where you created your resources for this quickstart.

  3. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  4. In the **Firewall policies associated with this node or inherited by the node** section, click **fw-egress-specific-vpc**.

  5. Click the **Associations** tab.

  6. Select the checkbox for **test-folder** , and click **Remove association**.

  7. In the **Remove association with`test-folder`** dialog, click **Delete**.

  8. Click **Delete**.

  9. In the **Delete`fw-egress-specific-vpc`** dialog, click **Delete**




### Delete the VMs

  1. Go to the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. From the project picker at the top of the page, select **test-project**.

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. Select the checkboxes for **myvpc-vm** , **testvpc-vm** , and **testvpc-apache-vm**.

  5. Click **Delete**.

  6. In the **Delete instance 3 instances** dialog, click **Delete**.




### Delete the Cloud Router and the Cloud NAT gateway

  1. In the Google Cloud console, go to the **Cloud routers** page.

[Go to Cloud routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the checkbox for **myvpc-router**.

  3. Click **Delete**.

  4. In the **Delete`myvpc-router`** dialog, click **Delete**.




When you delete a Cloud Router, the associated Cloud NAT gateway is also deleted.

### Delete the VPC network and its subnets

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Name** column, click **myvpc**.

  3. Click **Delete VPC network**.

  4. In the **Delete a network** dialog, click **Delete**.

Similarly, delete the `test-vpc` network.




When you delete a VPC network, its subnets are also deleted.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. If the project that you plan to delete is attached to an organization, expand the **Organization** list in the **Name** column. 
  3. In the project list, select the project that you want to delete, and then click **Delete**. 
  4. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the folder

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. If the folder that you plan to delete is attached to an organization, expand the **Organization** list in the **Name** column.

  3. In the folder list, select **test-folder** , and then click **Delete**.

  4. In the dialog, type the folder ID, and then click **Delete anyway** to delete the project.




## What's next

  * For firewall policies concepts, see [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).
  * For firewall policy rules concepts, see the [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To create, update, monitor, and delete VPC firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).
  * To determine costs, see [Cloud NGFW pricing](https://cloud.google.com/firewall/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
