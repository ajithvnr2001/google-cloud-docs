---
url: https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-iis/
title: Running a basic IIS web server \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:05.038051+00:00
---

# Running a basic IIS web server  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-iis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Running a basic IIS web server Stay organized with collections  Save and categorize content based on your preferences. 

You can control a virtual machine (VM) instance on Compute Engine like any standard Windows server. This tutorial shows you how to deploy a simple IIS web server so you can learn the basics of running a web server on a VM.

## Before you begin

You'll need a new Windows instance with HTTP traffic allowed.

  * Follow the [Quickstart](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance) instructions to create a new Windows instance and connect to it with RDP.



## Install IIS

  1. On the Windows taskbar, in the search field, type `PowerShell` and then press `Enter`. If there is no search field on the taskbar, click the search icon, type `PowerShell`, and then press `Enter`. If neither the search field nor the search icon appear on the taskbar, see [Hide and unhide your search box in Windows](https://support.microsoft.com/en-us/help/4028221/windows-10-locating-the-search-box-in-windows-10).

  2. In the search results, under **Apps** , right-click **Windows PowerShell** , and choose **Run as administrator**.

  3. Install IIS services with the following commands:
         
         import-module servermanager
         
         
         add-windowsfeature web-server -includeallsubfeature
         

  4. Overwrite the IIS web server default web page with the following command:
         
         echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' > C:\inetpub\wwwroot\index.html
         




## Test your server

Test that your instance is serving traffic on its external IP:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. View the `Hello World!` page by copying the IP address from the **External IP** column and pasting it into a new browser tab. If you do not see the `Hello World!` page, follow the [Troubleshooting steps](https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-iis#troubleshooting).




## Clean up

When you're done experimenting, follow the clean up instructions in the [Quickstart](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance#clean-up) to avoid incurring charges for this instance.

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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
