---
url: https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial/
title: Tutorial: Set up a domain by using Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:36.403860+00:00
---

# Tutorial: Set up a domain by using Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Tutorial: Set up a domain by using Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial provides a walkthrough of the process for registering a domain, setting up a sample web server, and using Cloud DNS to point the domain URL to the server.

If you are new to using Terraform for Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Objectives

This tutorial demonstrates how to complete the following tasks: 

  * Register a domain name by using Cloud Domains
  * Create a Compute Engine virtual machine (VM) instance
  * Run a basic Apache web server
  * Set up your domain using Cloud DNS
  * Update name servers
  * Verify your setup



## Costs

There is a cost associated with registering a domain name. For Cloud Domains pricing, see [Cloud Domains pricing](https://cloud.google.com/domains/pricing).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Compute Engine API.

[ Enable the API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)




## Register a domain name

If you already have a registered domain, skip this section.

You can use Cloud Domains to register a domain. Cloud Domains lets you use the same billing account for your domain that you have created in the [Before you begin](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#before-you-begin) section. For instructions about how to register a domain using Cloud Domains, see [Register a domain](https://docs.cloud.google.com/domains/docs/register-domain).

**Important:** If you use Cloud Domains to register a domain, you cannot clean up the domain at the end of this tutorial and are billed for the domain. For details, see the [Cloud Domains pricing page](https://cloud.google.com/domains/pricing).

## Create a virtual machine instance

###  Console 

To create a Linux virtual machine (VM) instance in Compute Engine, follow these instructions:

  1. In the Google Cloud console, go to the **Create an instance** page. 

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **OS and Storage** section, click **Change** to begin configuring your boot disk. 
  3. On the **Public images** tab, choose **Debian GNU/Linux**.
  4. Click **Select**. 
  5. In the **Firewall** section, select **Allow HTTP traffic**. 
  6. To create the VM, click **Create**. 

**Note:** By default, the VM instance that you create receives an ephemeral external IP address. The ephemeral IP address is released if you stop, reset, or delete the instance. To preserve the IP address, [reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses#ephemeral_and_static_ip_addresses).

Allow a short time for the instance to start. After the instance is ready, it is listed on the **VM instances** page with a green status icon.

### Connect to your instance

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)




You now have a terminal window for interacting with your Linux instance.

For details, see the [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

## Run a basic Apache web server

In this section, you run and test an Apache web server.

  1. From the SSH window, use the Debian package manager to install the `apache2` package.
         
         sudo apt-get update && sudo apt-get install apache2 -y
          

After installing Apache, the operating system automatically starts the Apache server.

  2. Overwrite the default web page for the Apache web server by using the following command:
         
         echo "<!doctype html><html><body><h1>Hello World!</h1></body></html>"   
         
          | sudo tee /var/www/html/index.html
          




### Test your server

Test that your instance is serving traffic on its external IP address.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page. 

[ Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **External IP** column, copy the external IP address for your instance.
  3. In a browser, navigate to `http://[EXTERNAL_IP]`. Don't use `https` to connect because the server will return a `Connection Refused` error.



You should now see the _Hello World!_ page.

For further details, see [Running a basic Apache web server](https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-apache).

## Set up your domain using Cloud DNS

If you are migrating from an existing provider, you can import your existing zones to Cloud DNS. For instructions, see [Export your DNS configuration from your existing provider](https://docs.cloud.google.com/dns/docs/migrating#export_your_dns_configuration_from_your_existing_provider). Otherwise, follow these steps to create a new public zone.

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/networking/dns/zones/~new)

  2. For the **Zone type** , select **Public**.

  3. For the **Zone name** , enter `my-new-zone`.

  4. For the **DNS name** , enter a DNS name suffix for the zone by using a domain name that you registered (for example, `example.com`).

  5. For **DNSSEC** , ensure that the `Off` setting is selected.

  6. Click **Create** to create a zone populated with the NS and SOA records.

  7. To point your registered domain name to the IP address of the hosting server, you must add an A record to your zone:

     1. On the **Zone details** page, click **Add Standard**.
     2. Select **A** from the **Resource Record Type** menu.
     3. For **IPv4 Address** , enter the external IP address for your instance.
     4. Click **Create** to create the A record for your zone.
  8. Optional: Add a CNAME record to account for a prefix to your domain name (for example, `www.`):

     1. Click **Add Standard**.
     2. In the **DNS Name** field, add the prefix `www` for the domain.
     3. For **Resource Record Type** , choose **CNAME**.
     4. For **Canonical name** , enter the domain name, followed by a period (for example, `example.com.`).
     5. Click **Create**.

**Note:** If you want to set up SMTP servers for delivering email to your domain, you must add MX records to your zone. For instructions about setting up MX records if you are using Google Workspace, see the [Set up MX records](https://support.google.com/a/answer/9222085) support page. If you are using a different SMTP provider, use the MX record details from your provider and follow the same instructions.

## Update name servers

To update name servers in Cloud Domains, follow these steps:

  1. In the Google Cloud console, go to the **Cloud Domains** page.

[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)

  2. Click the domain name that you want to edit. You can also click more_vert**More** next to the domain name to see the edit menu.

  3. To edit the DNS details, click **Edit DNS details**.

  4. Select **Use Cloud DNS (Recommended)**.

  5. In the **Cloud DNS zone** list, select `my-new-zone`.

  6. Click **Save**.




###  Terraform 

You can use [ Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to create a virtual machine (VM) instance, run an Apache Web server, set up your domain using Cloud DNS, and update name servers.

You can also use [ Terraform module](https://github.com/terraform-google-modules/terraform-google-cloud-dns) to set up Cloud DNS with public, private, peering, or forwarding zones. For more information about zones, see the [ DNS zones overview](https://docs.cloud.google.com/dns/docs/zones/zones-overview).
    
    
    # to setup a web-server
    
    resource "random_id" "rnd" {
      byte_length = 4
    }
    
    resource "google_compute_instance" "default" {
      name         = "dns-compute-instance"
      machine_type = "g1-small"
      zone         = "us-central1-b"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      network_interface {
        network = "default"
        access_config {
          // Ephemeral public IP
        }
      }
      metadata_startup_script = <<-EOF
      sudo apt-get update && \
      sudo apt-get install apache2 -y && \
      echo "<!doctype html><html><body><h1>Hello World!</h1></body></html>" > /var/www/html/index.html
      EOF
    }
    
    # to allow http traffic
    resource "google_compute_firewall" "default" {
      name    = "allow-http-traffic"
      network = "default"
      allow {
        ports    = ["80"]
        protocol = "tcp"
      }
      source_ranges = ["0.0.0.0/0"]
    }
    
    # to create a DNS zone
    resource "google_dns_managed_zone" "default" {
      name          = "example-zone-googlecloudexample"
      dns_name      = "example-${random_id.rnd.hex}.com."
      description   = "Example DNS zone"
      force_destroy = "true"
    }
    
    # to register web-server's ip address in DNS
    resource "google_dns_record_set" "default" {
      name         = google_dns_managed_zone.default.dns_name
      managed_zone = google_dns_managed_zone.default.name
      type         = "A"
      ttl          = 300
      rrdatas = [
        google_compute_instance.default.network_interface[0].access_config[0].nat_ip
      ]
    }

## Verify your setup

To verify that your configuration is working, _after_ the name servers are updated, navigate to your domain name (for example, `example.com`). The domain should resolve to your IP address and should point to the Compute Engine VM displaying the _Hello World!_ page that you created in Run a basic Apache Web server.

To verify that your setup is correct, you can also run the `dig +trace example.com` command on your terminal window. Replace `example.com` with your registered domain name.
    
    
    dig +trace example.com
    

The end of the output should include the following. `IP_ADDRESS` is your web server's IP address.
    
    
    example.com.    300 IN  A   IP_ADDRESS
    ;; Received 62 bytes from 216.239.34.109#53(ns-cloud-d2.googledomains.com) in 62 ms
    

**Note:** If you're using Microsoft Windows and `dig` is not installed on your system, you can run a `dig -t NS` query from the Google Workspace [web interface](https://toolbox.googleapps.com/apps/dig/#NS/).

To verify that the changes are successful, run the following command:

`example.com IN NS <your Cloud DNS name servers>`

After waiting for [DNS propagation to complete](https://www.siteground.com/kb/what_is_dns_propagation_and_why_it_takes_so_long/), you can also run the `nslookup` command to verify your setup:
    
    
    nslookup example.com
    

The output should include the following. `IP_ADDRESS` is your web server's IP address.
    
    
    Server:     127.0.0.1
    Address:    127.0.0.1#53
    
    Non-authoritative answer:
    Name:   example.com
    Address: IP_ADDRESS
    

## Clean up

**Note:** To avoid incurring charges for the resources that you created, you can delete them by following the instructions in this section. However, if you use Cloud Domains to register a domain, you might continue to be billed for the domain. For details, see the [Cloud Domains pricing page](https://cloud.google.com/domains/pricing).

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones/)

  2. Click a zone name (for example, `my-new-zone`) to get to the **Zone details** page.

  3. Select the A and CNAME records that you created.

  4. Click **Delete record sets**.

  5. To delete the zone, click _delete_**Delete zone** for the zone name `my-new-zone`.

  6. Go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  7. Select the instance that you want to delete.

  8. On the _more_vert_**More** menu in the row of the instance, click **Delete**.




## What's next

  * To add, delete, or update records, see [Manage records](https://docs.cloud.google.com/dns/docs/records).
  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To reference the API, see [Cloud DNS REST API](https://docs.cloud.google.com/dns/docs/reference/v1).
  * To determine costs, see [Cloud DNS Pricing](https://cloud.google.com/dns/pricing).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
