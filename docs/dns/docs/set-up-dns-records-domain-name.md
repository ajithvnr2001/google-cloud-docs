---
url: https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name/
title: Quickstart: Set up DNS records for a domain name with Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:30.754203+00:00
---

# Quickstart: Set up DNS records for a domain name with Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Set up DNS records for a domain name with Cloud DNS

This page explains how to set up a Cloud DNS managed zone and a resource record for your domain name. It guides you through an example of creating a managed zone and then setting up Address (`A`) and Canonical Name (`CNAME`) records for the domain.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/compute?walkthrough_id=gce_cloud_dns)

* * *

For more information, see the following resources:

  * For Cloud DNS concepts, see the [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
  * For terminology related to Cloud DNS, see [Key terms](https://docs.cloud.google.com/dns/docs/key-terms).
  * For Virtual Private Cloud (VPC) network configuration information, see the [VPC overview](https://docs.cloud.google.com/vpc/docs/overview).
  * For configuration how-tos and API information, see What's next.



## Requirements

This quickstart assumes that you have the following:

  * A domain name through a domain name registrar. You can register a domain name by using [Cloud Domains](https://docs.cloud.google.com/domains/docs/register-domain) or another domain registrar of your choice. Cloud Domains lets you manage domains by using the Cloud Domains API.
  * A [Windows Server virtual machine (VM) instance](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance) or a [Linux VM instance](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).
  * An IP address to point the `A` record of your zone to. A valid IP address can be a server that you already have running with an IP address that you can point to. For example, you can go through the [Running a basic Apache Web server](https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-apache) tutorial to start up a web server on a Compute Engine VM.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure that you have the following role or roles on the project: Service Usage Admin, DNS Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Make sure that you have the following role or roles on the project: Service Usage Admin, DNS Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  8. Enable the DNS API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dns)




## Create a managed public zone in Cloud DNS

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. To create a public DNS zone, click **Create zone**.

  3. For **Zone type** , choose **Public**.

  4. In the **Zone name** field, enter `my-new-zone`.

  5. In the **DNS name** field, enter the name of the domain that you purchased. Enter the domain name only. For example:
         
         example.com
         

  6. In the **DNSSEC** drop-down list, select **Off**.

  7. Click **Create**.


The **Zone details** page is displayed. Default NS and SOA records have been created for you. 

To edit a record, on the **Zone details** page, at the end of the row for the record that you want to edit, click _edit_**Edit**.

## Create a record to point the domain to an external IP address

If your IP address is in the format `#.#.#.#`, you have an IPv4 address and need to create an `A` record.

If your IP address is in the format `#:#:#:#:#:#:#:#`, you have an IPv6 address and need to create an `AAAA` record.

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/zones)

  2. Click the zone where you want to add a record set.

  3. Click **Add standard**.

  4. For **Resource Record Type** , to create an `A` record, select `A`. To create an `AAAA` record, select `AAAA`.

  5. For **IPv4 Address** or **IPv6 Address** , enter the IP address that you want to use with this domain.

  6. Click **Create**.




## Create a CNAME record for the `www` subdomain

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/zones)

  2. Click the zone where you want to add a record set.

  3. Click **Add standard**.

  4. For **DNS Name** , enter `www`.

  5. For **Resource Record Type** , select `CNAME`.

  6. For **Canonical name** , enter the domain name, followed by a period (for example, `example.com.`).

  7. Click **Create**.




The record update takes some time to propagate depending on the time to live (TTL) values of the records. You can verify that the DNS records are working by visiting the domain name and confirming that the domain resolves to your IP address.

## Update your domain name servers to publish your domain

Finally, you must [update your domain's name servers to use Cloud DNS](https://docs.cloud.google.com/dns/docs/update-name-servers) to publish your new records to the internet.

You have successfully used Cloud DNS to set up your DNS records.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/zones)

  2. Click the zone name (`my-new-zone`) to get to the **Zone details** page.

  3. Select the A and CNAME records that you created.

  4. Click **Delete record sets**.

  5. Go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/zones)

  6. To delete the zone, select the `my-new-zone` checkbox, and then at the end of the row, click _delete_**Delete zone**.




## What's next

  * To add, delete, or update records, see [Manage records](https://docs.cloud.google.com/dns/docs/records).
  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To reference the API, see [Cloud DNS REST API](https://docs.cloud.google.com/dns/docs/reference/v1).
  * To determine costs, see [Cloud DNS Pricing](https://cloud.google.com/dns/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
