---
url: https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-apache/
title: Running a basic Apache web server \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:39.043932+00:00
---

# Running a basic Apache web server  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-apache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Running a basic Apache web server Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use Compute Engine to deploy an Apache web server on a virtual machine (VM) instance. To learn more about the technologies that you can use for web serving on Google Cloud, see [Choosing a hosting option on Google Cloud](https://docs.cloud.google.com/architecture/web-serving-overview#choosing_an_option).

A VM on Compute Engine can be controlled like any standard Linux server. Deploy an Apache web server to learn the basics of running a server on a VM instance.

## Before you begin

Create a Linux VM that allows HTTP traffic by doing the following:

  1. Create a new Linux VM. For more information, see [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

     1. Optional: While creating a Linux VM, you can select the **Allow HTTP traffic** checkbox to open port `tcp:80` for traffic and **Allow HTTPS traffic** checkbox to open port `tcp:443`. However, if you want to open a different port, [configure the firewall](https://docs.cloud.google.com/vpc/docs/using-firewalls) after creating the VM, and then [configure Apache](https://httpd.apache.org/docs/2.4/bind.html) to use the firewall.
  2. Connect to the Linux VM. For more information, see [Connect to the VM instance](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#connect_to_the_vm_instance).




## Install Apache

  1. In the Google Cloud console, go to the **VM Instances** page. 

[ Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. To connect to the Linux VM you just created, click **SSH** in the row of the VM.
  3. To update the available packages and install the `apache2` package, use the system package manager for that operating system. If you followed the Quickstart, this creates an Ubuntu VM. To update an Ubuntu VM, run the following command:
         
         sudo apt update && sudo apt -y install apache2
         

After installing Apache, the operating system automatically starts the Apache server.

  4. Verify that Apache is running:
         
         sudo systemctl status apache2
         

  5. Overwrite the Apache web server default web page:
         
         echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html
         




## Test your server

Test that your VM is serving traffic on its external IP.

  1. In the Google Cloud console, go to the **VM Instances** page. 

[ Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Copy the external IP for your VM under the **External IP** column.
  3. In a browser, navigate to `http://[EXTERNAL_IP]`. Don't connect using `https` because this causes the server to return a `Connection Refused` error.



You should now see the "Hello World!" page.

## Clean up

To avoid incurring charges for the VM after you're done experimenting, delete the VM. For more information, see [Clean up](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up).

## Troubleshooting

**Receiving a`Connection Refused` error**

If you are seeing a `Connection Refused` error, it is possible that:

  * Your VM instance is not publicly accessible because your firewall rules or tags are misconfigured in one of the following ways:

    * The VM instance does not have the proper tag that allows Compute Engine to apply the appropriate firewall rules to your instance.
    * Your project does not have a firewall rule that allows traffic to the external IP address for your instance.
  * You are trying to access the VM using an `https` address. Check that your URL is `http://[EXTERNAL_IP]` rather than `https://[EXTERNAL_IP]`.




To ensure that your VM instance has the correct tags:

  1. In the Google Cloud console, go to the **VM instances** page. 

[ Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance that you are trying to connect to.
  3. Click **Edit** at the top of the page.
  4. Scroll down to **Firewalls** , and make sure the **Allow HTTP traffic** box is checked. If it is not checked, check it.
  5. Save your changes. This ensures that the correct tags are added to the VM instance.



To ensure that the correct firewall rule exists:

  1. In the Google Cloud console, go to the **Firewall rules** page. 

[ Go to Firewall rules](https://console.cloud.google.com/networking/firewalls)

  2. Look for a firewall rule that allows all IP ranges through tcp:80. Usually, this rule is named the `default-allow-http` rule.
  3. If a rule does not exist, create one. 
     1. Click **Create firewall rule**.
     2. Enter a name for the rule, such as `default-allow-http`.
     3. Under **Source IP ranges** , enter `0.0.0.0/0` to allow traffic from all sources.
     4. Under **Protocols and ports** , check **Specified protocols and ports** and enter `tcp:80`.
     5. Create your firewall rule.



Test your server again by going to the external IP address of the instance:
    
    
    http://[EXTERNAL_IP]
    

## What's next

Learn how to [host a website on Compute Engine](https://docs.cloud.google.com/solutions/web-serving-overview).

Learn how to [set up LAMP on Compute Engine](https://github.com/GoogleCloudPlatform/community/blob/master/archived/setting-up-lamp/index.md).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
