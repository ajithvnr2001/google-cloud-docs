---
url: https://docs.cloud.google.com/iap/docs/tutorial-gce/
title: Setting up IAP for Compute Engine \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:16.949365+00:00
---

# Setting up IAP for Compute Engine  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/tutorial-gce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Setting up IAP for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to set up a Compute Engine instance with Identity-Aware Proxy (IAP). If you already have your Compute Engine instance set up and only need to enable IAP, see [Enabling IAP for Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto). 

## Objectives

In this tutorial, you learn about the following:

  * Creating a Compute Engine instance template and managed instance group (MIG).
  * Getting a domain name and certificate.
  * Creating an HTTPS load balancer with a certificate.
  * Enabling IAP.
  * Testing that IAP is working.



## Costs

This tutorial uses billable components of Google Cloud, including the following:

  * Compute Engine 
    * 4 Virtual Machines (VMs)
  * Networking 
    * Global Load Balancer Forwarding Rule
    * Ingress Traffic



For a cost estimate based on projected usage, see this [Pricing Calculator](https://cloud.google.com/products/calculator/#id=5738361c-f9fd-45c7-927e-f5fd36cce862).

New Cloud Platform users might be eligible for a [free trial](https://cloud.google.com/free/). 

## Before you begin

Before you start this tutorial, you need the following:

  1. Select or create a Google Cloud project.   
[GO TO THE PROJECTS PAGE](https://console.cloud.google.com/project)

  2. Enable billing for your project. Read about how to [Modify a project's billing settings](https://support.google.com/cloud/answer/6293499#enable-billing)




## Step 1: Create a Compute Engine template

In the Google Cloud console, go to the [Compute Engine > Create an instance template](https://console.cloud.google.com/compute/instanceTemplates/add) page and select the project where you want to create a template.

[GO TO THE CREATE AN INSTANCE TEMPLATE PAGE](https://console.cloud.google.com/compute/instanceTemplates/add)

Use the default values except for the following:

  * **Machine type:**
    * micro (f1-micro)
  * **Access scopes:**
    * Set access for each API
    * Compute Engine: Read Only
  * **Firewall:**
    * Allow HTTP traffic
  * In the **Management** section, under **Automation > Startup script**, copy and paste the following script: 
        
        # Copyright 2021 Google LLC
        #
        # Licensed under the Apache License, Version 2.0 (the "License");
        # you may not use this file except in compliance with the License.
        # You may obtain a copy of the License at
        #
        #      http://www.apache.org/licenses/LICENSE-2.0
        #
        # Unless required by applicable law or agreed to in writing, software
        # distributed under the License is distributed on an "AS IS" BASIS,
        # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        # See the License for the specific language governing permissions and
        # limitations under the License.
        
        apt-get -y update
        apt-get -y install git
        apt-get -y install virtualenv
        git clone https://github.com/GoogleCloudPlatform/python-docs-samples
        cd python-docs-samples/iap
        virtualenv venv -p python3
        source venv/bin/activate
        pip install -r requirements.txt
        cat example_gce_backend.py |
          sed -e "s/YOUR_BACKEND_SERVICE_ID/$(gcloud compute backend-services describe my-backend-service --global --format="value(id)")/g" |
          sed -e "s/YOUR_PROJECT_ID/$(gcloud config get-value account | tr -cd "[0-9]")/g" > real_backend.py
        gunicorn real_backend:app -b 0.0.0.0:80
        




When you're finished updating values, click **Create** to create the template.

## Step 2: Create a Managed Instance Group

In the Google Cloud console, go to the [Compute Engine > Create a new instance group](https://console.cloud.google.com/compute/instanceGroups/add) page and select the project where you want to create a Managed Instance Group.

[GO TO THE CREATE AN INSTANCE GROUP PAGE](https://console.cloud.google.com/compute/instanceGroups/add)

Use the default values except for the following:

  * **Name:** my-managed-instance-group
  * **Location:** Multi-zone
  * **Instance template:** Select the instance template you created in Step 1
  * **Number of instances:** To change the number of instances, you must first turn off autoscaling.
  * **Autoscaling mode:** Don't autoscale
  * **Health check:** select **Create a health check** , then enter the following values:

    * **Name:** my-health-check
    * **Protocol:** HTTP

Use your new health check by clicking **Save and continue**.




When you're finished updating values, click **Create** to create the Managed Instance Group (MIG).

## Step 3: Get a domain name and certificate

To use the Load Balancer with HTTPS traffic, you need a domain name and a signed certificate. You can register a domain on [Cloud Domains](https://docs.cloud.google.com/domains/docs/overview), or use the domain registrar of your choice. Register your domain before you continue.

### Set up your certificate

Create a certificate that identifies your website to your users. For information about how to create a certificate, see [Using Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs).

Your CA has to verify that you own the domain name you registered. In the following steps, you create a VM to authenticate your domain with the CA.

#### Create a VM to authenticate your domain ownership

In the Google Cloud console, go to the [Compute Engine > Create an instance page](https://console.cloud.google.com/compute/instancesAdd).

[GO TO THE CREATE AN INSTANCE PAGE](https://console.cloud.google.com/compute/instancesAdd)

Use the default values except for the following:

  * **Name:** certbot-vm
  * **Machine type:** micro (f1-micro)
  * **Access scopes:**
    * Set access for each API
    * Compute Engine: Read/Write
  * **Boot disk image:**
    * Debian GNU/Linux 9 (stretch)
  * **Firewall:**
    * Allow HTTP traffic
    * Allow HTTPS traffic



When you finish updating values, click **Create** to create the VM instance. Note the external IP address of the VM that you just created. You'll need it in the next step.

#### Set up your domain to point to the VM

To set up your domain to point to the VM, follow these steps to configure A records:

  1. Sign in to your domain's account at your domain host.
  2. Find the page to update your domain's DNS records. This page might be called something like DNS Management, Name Server Management, or Advanced Settings.
  3. Change your A records to the following values: 
     * **Name/Host/Alias:** @
     * **Value:** the external IP address of the VM that you created to authenticate your domain ownership above.
     * **TTL:** the default for your registrar, or 86400 (one day).
  4. Wait for the DNS record to update. It can take up to one day for the record you added to propagate.



To learn more, see [About A records](https://support.google.com/a/answer/2576578).

#### Test your server

To test that your server is working correctly, follow these steps:

  1. In the Google Cloud console, go to the [Compute Engine > VM Instances](https://console.cloud.google.com/compute/instances) page.   
[GO TO THE VM INSTANCES PAGE](https://console.cloud.google.com/compute/instances)

  2. Under **Connect** for **certbot-vm** , click **SSH**.

  3. Run the following commands to run a small web server on your VM:
         
         mkdir web
           cd web
           echo "Hello" > index.html
           sudo busybox httpd -v -f
         

  4. In a web browser, go to the domain name you registered earlier. Your web browser should display `Hello`, and your SSH session should display a message that contains `... response:200`. If not, wait a few minutes, then repeat this step.

  5. After the test is successful, press `Ctrl+C` to stop the web server.




#### Create a certificate

To create a certificate, register with [Let's Encrypt](https://letsencrypt.org/) by running the following commands on the VM where YOUR_DOMAIN is your domain name, not including the protocol:
    
    
    sudo pkill busybox
    sudo apt-get install -y certbot
    sudo certbot certonly --standalone -d YOUR-DOMAIN
    

During this process, Let's Encrypt might request an email address to send a reminder when your certificate expires (by default, 3 months after it's issued). You must also agree to Let's Encrypt's Terms of Service.

When you're successfully registered, a message that reads `Congratulations! Your certificate and chain have been saved at...` appears.

#### Add the certificate to your project

To add the certificate to your project, run the following commands on the VM:
    
    
    sudo su
    cd /etc/letsencrypt/live/YOUR_DOMAIN
    gcloud compute ssl-certificates create my-cert --certificate=fullchain.pem --private-key=privkey.pem
    

After you've successfully created your certificate, a message appears that's similar to: `Created [https://www.googleapis.com/compute/v1/projects/example-project/global/sslCertificates/my-cert]`

Before you continue, close the SSH session.

## Step 4: Create a load balancer

Before you start this step, make sure you closed the SSH session you started in the previous step. When you're ready, follow the steps below to create a load balancer:

  1. In the Google Cloud console, go to the [Network Services > Create a load balancer](https://console.cloud.google.com/net-services/loadbalancing/add) page and select the project where you want to create a load balancer.   
[GO TO THE CREATE A LOAD BALANCER PAGE](https://console.cloud.google.com/net-services/loadbalancing/add)

  2. Under **HTTP(S) Load Balancing** , click **Start configuration**.

  3. Select **From Internet to my VMs**.

  4. On the **New external Application Load Balancer** page that appears, enter a **Name** for your load balancer.

  5. Click **Backend configuration**.

  6. Under **Backend services & backend buckets**, select **Create a backend service**.

  7. Add a name for your backend service, such as `my-backend-service`.   
**Caution:** You must use the exact `my-backend-service` name. If you use a different name, the startup script on your VMs cannot find the correct Backend Service ID to authenticate requests.

  8. Go to the **Security** section, and then select **Enable IAP to secure access to your applications**.

Cloud CDN and IAP are not compatible. If you have Cloud CDN enabled and you select to enable IAP, Cloud CDN is automatically disabled.

  9. Click **Create**. The **Load balancing** page loads, with your new load balancer displayed in the list of load balancers.

  10. After the Google Cloud console finishes creating the new load balancer, click the name of the load balancer and note the external IP address under **Details > Frontend**. You use it in the next step.




### Set up your domain to point to the load balancer

To set up your domain to point to the load balancer, configure A records using the following steps:

  1. Sign in to your domain's account at your domain host.
  2. Find the page to update your domain's DNS records. This page might be called something like DNS Management, Name Server Management, or Advanced Settings.
  3. Change your A records to the following values: 
     * **Name/Host/Alias:** @
     * **Value:** the external IP address of the load balancer you created earlier. Don't include the port `:443` in your DNS record.
     * **TTL:** the default for your registrar, or 86400 (one day).
  4. Wait for the DNS record to update. It can take up to a day for the record you just added to propagate.
  5. To test the load balancer, use a web browser to go to your domain with an `https://` protocol. 
     * If the load balancer isn't set up yet, you see "HTTP 502" errors.
     * When the load balancer is ready, you see "Unauthorized request."



To learn more, see [About A records](https://support.google.com/a/answer/2576578).

### Restart your VMs

To correctly authenticate requests from IAP, you must restart the VMs in your MIG.

  1. In the Google Cloud console, go to the [Compute Engine > Instance groups page](https://console.cloud.google.com/compute/instanceGroups/list).   
[GO TO THE INSTANCE GROUPS PAGE](https://console.cloud.google.com/compute/instanceGroups/list)
  2. Click **my-managed-instance-group**.
  3. On the top of the instance group details that appear, click **Rolling Restart/Replace**.
  4. On the **Restart/replace instances of my-managed-instance-group** page, set the following values: 
     * **Operation:** Restart
     * **Maximum unavailable:** 3 instances out of 3 instances
     * **Minimum wait time:** 0 s
  5. When you're finished updating values, click **Restart**.



## Step 5: Set up IAP

### Configure your firewall

Next, configure your firewall to block access to the underlying VMs and only allow access through IAP:

  1. Go to the Google Cloud console [VPC network > Firewall rules](https://console.cloud.google.com/networking/firewalls/list).   
[GO TO THE FIREWALL RULES PAGE](https://console.cloud.google.com/networking/firewalls/list)

  2. Select the checkbox next to the following rules:

     * default-allow-http

     * default-allow-https

     * default-allow-internal

  3. Click **Delete**.

  4. Click **Create firewall rule** and set the following values:

     * **Name:** allow-iap-traffic

     * **Targets:** All instances in the network

     * **Source IP ranges** (press `Enter` after you paste each value into the field): You must allow traffic from these IP address ranges so that the load balancer can communicate with your backends.

       * 130.211.0.0/22

       * 35.191.0.0/16

     * **Protocols and ports:**

       * Specified protocols and ports

       * tcp:80

  5. When you're finished updating values, click **Create**.




### Set up IAP

To set up IAP for your project, follow these steps:

1\. In the Google Cloud console, go to the [Security > Identity-Aware Proxy](https://console.cloud.google.com/security/iap/) page and select the project that you want to enable IAP for.   
[GO TO THE IDENTITY-AWARE PROXY PAGE](https://console.cloud.google.com/security/iap/) 1\. If you haven't configured your project's OAuth consent screen, you're prompted to do so: **Caution:** Don't enter any confidential information on the OAuth consent screen. Any information you save to the OAuth consent screen may be publicly visible for anyone who accesses your URL. Email and product details are displayed on the login screen and when someone tries to access a resource for which they don't have permission. 

  1. Go to the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent).   
[Configure consent screen](https://console.cloud.google.com/apis/credentials/consent)
  2. Under **Support email** , select the email address you want to display as a public contact. The email address must belong to the currently logged in user account or to a Google Group for which the currently logged in user is a [manager or owner](https://support.google.com/a/answer/167094). 
  3. Enter the **Application name** you want to display.
  4. Add any optional details you'd like.
  5. Click **Save**.



To change information on the OAuth consent screen later, such as the product name or email address, repeat the preceding steps to configure the consent screen.

1\. Next to **my-backend-service** ,  toggle the on/off switch in the **IAP** column. 1\. In the **Turn on IAP** window that appears, select the checkbox next to "I have read the configuration requirements and configured my Compute Engine resource according to the documentation." 1\. Click **Turn on**. 

### Add principals to the access list

Next, add principals to the IAP access list for your project.

  1. On the [Security > Identity-Aware Proxy](https://console.cloud.google.com/security/iap/) right side **Access** section, click **Add**.
  2. Enter the principals you want to give access to, including yourself, and assign the principals the **IAP-secured Web App User** role. Principals can be: 
     * Google Accounts: user@gmail.com
     * Google Groups: admins@googlegroups.com
     * Service accounts: server@example.gserviceaccount.com
     * Google Workspace domains: example.com 



## Step 6: Test IAP

To test that IAP is working correctly, follow these steps:

1\. In your web browser, navigate to your domain. If you see "Unauthorized request", try again in a few minutes. 1\. When you see a Google sign-in screen, sign in using the Google Account you gave access to in the previous step. 1\. A message appears like "Hi, user@example.com. I am my-managed-instance-group-29z6." 1\. Try refreshing the page. Your browser should show the names of the 3 machines in your managed instance group. This is the load balancer distributing traffic across the VMs in the group. 

Congratulations! You've successfully enabled a load-balanced service using IAP.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you finish setting up IAP for Compute Engine, you can clean up the resources that you created on Google Cloud so you aren't billed for them in the future. The following sections describe how to delete or turn off these resources.

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Deleting instances

To delete a Compute Engine instance: 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



### Deleting firewall rules for the default network

To delete a firewall rule: 

  1. In the Google Cloud console, go to the **Firewall** page. 

[Go to Firewall](https://console.cloud.google.com/networking/firewalls/list)

  2. Select the checkbox for the firewall rule that you want to delete. 
  3. To delete the firewall rule, click delete **Delete**. 



## What's next

  * Try modifying the [example app](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/iap/example_gce_backend.py) we used in this tutorial to serve other data.
  * Read the [Best Practices](https://docs.cloud.google.com/iap/docs/concepts-best-practices) to understand how to write your own apps and secure them with IAP.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
