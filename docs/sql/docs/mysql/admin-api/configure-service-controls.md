---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/configure-service-controls/
title: Configure VPC Service Controls \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:52:39.600894+00:00
---

# Configure VPC Service Controls  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/configure-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/admin-api/configure-service-controls "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/configure-service-controls "View this page for the SQL Server database engine")

This page describes how to enable VPC Service Controls on a Cloud SQL project. Before you begin, review [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Also review the [Cloud SQL limitations when using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#cloud_sql_admin_api).

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

  6. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  7. Enable the Service Networking API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking)

  8. Add the [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/vpc-service-controls/docs/access-control#required_roles) to the user or service account you are using to set up and administer VPC Service Controls. See [IAM Roles for Administering VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/access-control).
  9. Review [limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#cloud_sql_admin_api) when using VPC Service Controls with Cloud SQL.
  10. Optionally, add an organization policy that restricts public IP on instances in projects that use that policy. See [Connection organization policies](https://docs.cloud.google.com/sql/docs/mysql/connection-org-policy) and [Configuring the organization policy](https://docs.cloud.google.com/sql/docs/mysql/configure-org-policy#configuring_the_organization_policy).



### Configure the Virtual Private Cloud (VPC) network

Perform the steps in [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

**Note:** If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you must include the [host project](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#shared_vpc) in a service perimeter along with any projects that belong to the Shared VPC. 

### Configure DNS for Artifact Registry

Cloud SQL instances require access to Artifact Registry (`pkg.dev` and `*.pkg.dev`) to download essential service agent container images during instance creation and maintenance. When using VPC Service Controls, you must route requests for Artifact Registry domains to the restricted virtual IP (VIP) range (`199.36.153.4/30`).

To route Artifact Registry traffic to the restricted VIP, configure Cloud DNS private DNS zones:

  1. Create a dedicated private managed DNS zone for the `pkg.dev.` domain:
         
         gcloud dns managed-zones create ZONE_NAME \
             --project=PROJECT_ID \
             --description="DESCRIPTION" \
             --dns-name=pkg.dev. \
             --networks=NETWORK_NAME \
             --visibility=private
             

Replace the following:

     * `ZONE_NAME`: a name for the DNS zone (for example, `pkg-dev-private`).
     * `PROJECT_ID`: the ID of the Google Cloud project that hosts your VPC network.
     * `DESCRIPTION`: a description of the zone (for example, `Private DNS zone for Artifact Registry`).
     * `NETWORK_NAME`: the name of your VPC network.

**Caution:** You must create a dedicated private DNS zone for the `pkg.dev.` domain. In Cloud DNS, all resource record sets in a managed zone must be subdomains of the zone's domain suffix. Attempts to add `pkg.dev` records into an existing private zone with a different suffix (such as `example.internal.`) fail with validation errors.

  2. Start a DNS transaction:
         
         gcloud dns record-sets transaction start \
             --project=PROJECT_ID \
             --zone=ZONE_NAME
             

  3. Add an `A` record for `pkg.dev.` pointing to the restricted VIP range (`199.36.153.4/30`):
         
         gcloud dns record-sets transaction add \
             199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7 \
             --name=pkg.dev. \
             --type=A \
             --ttl=300 \
             --zone=ZONE_NAME \
             --project=PROJECT_ID
             

  4. Add a `CNAME` record mapping wildcard subdomains (`*.pkg.dev.`) to `pkg.dev.`:
         
         gcloud dns record-sets transaction add "pkg.dev." \
             --name="*.pkg.dev." \
             --type=CNAME \
             --ttl=300 \
             --zone=ZONE_NAME \
             --project=PROJECT_ID
             

  5. Run the transaction:
         
         gcloud dns record-sets transaction execute \
             --zone=ZONE_NAME \
             --project=PROJECT_ID
             




**Note:** If your VPC network has firewall rules denying outbound traffic, then make sure that you have an egress firewall rule allowing TCP traffic on port 443 to `199.36.153.4/30`. For more information about securing Artifact Registry in a service perimeter, see [Secure repositories in a service perimeter](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc).

### Enable VPC Service Controls for private services access

When a Cloud SQL instance uses private IP (private services access), its underlying resources run in a peered service producer VPC network (`servicenetworking`). If your VPC network exports custom broad routes (such as `0.0.0.0/0`, `0.0.0.0/1`, or `128.0.0.0/2`) over the private services access peering connection, those routes can override Google API routes in the producer network and block Artifact Registry access.

To configure the service producer network with private DNS zones (including `pkg.dev`) and a route to the restricted VIP (`199.36.153.4/30`), enable VPC Service Controls on the peering connection:
    
    
    gcloud services vpc-peerings enable-vpc-service-controls \
        --network=NETWORK_NAME \
        --project=PROJECT_ID \
        --service=servicenetworking.googleapis.com

For more information, see [ gcloud services vpc-peerings enable-vpc-service-controls](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls) and [Configure hybrid connectivity](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#on-prem) in the VPC documentation.

## Disallow or disable public IP for Cloud SQL instances

To constrain data within the VPC for your Cloud SQL project, don't allow connections to Cloud SQL instances from public IPs. IP-based connections bypass VPC Service Controls. You must also disable public IP for new and existing Cloud SQL instances within the VPC.

To either disallow or disable public IP on Cloud SQL instances:

  * Organization administrators can apply organization policies that disallow creating new instances with public IP. See [Configure the organization policy](https://docs.cloud.google.com/sql/docs/mysql/configure-org-policy#configuring_the_organization_policy).
  * Users who create Cloud SQL instances can configure the instances to use private IP instead of public IP. See [Disable public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip#disable-public).



## Create a service perimeter

During this procedure, you select the Cloud SQL projects that you want the VPC service perimeter to protect.

**Note:** Sometimes, a Cloud SQL instance enabled with customer-managed encryption keys (CMEK) has the Cloud Key Management Service key hosted in a different project. For this scenario, when you enable VPC Service Controls, you must add the Cloud KMS key hosting project to the service perimeter.

To create a service perimeter, follow the instructions in [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

### Add more instances to the service perimeter

To add existing Cloud SQL projects to the perimeter, follow the instructions in [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#updating_a_service_perimeter).

### Add Cloud SQL and Cloud Storage APIs

To mitigate the risk of your data being exfiltrated from Cloud SQL, for example, using Cloud SQL import or export APIs, you must restrict both the **Google Cloud SQL Admin API** _and_ the **Google Cloud Storage API**.

**Note:** You can only import or export data from a Cloud Storage bucket that is in a project that resides in the same service perimeter as Cloud SQL.

To add Cloud SQL and Cloud Storage APIs as restricted services:

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. Click **EDIT**.

  4. On the **Edit VPC Service Perimeter** page, click **ADD SERVICES**.

  5. Add **Cloud SQL Admin API** and **Cloud Storage API**.

  6. Click **Save**.




### gcloud
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
    --policy=POLICY_ID \
    --add-restricted-services=sqladmin.googleapis.com,storage.googleapis.com

Where:

  * PERIMETER_ID is the ID of the perimeter or the fully qualified identifier for the perimeter.
  * POLICY_ID is the ID of the access policy.



For reference information, see [`access-context-manager perimeters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update).

## Create an access level

Optionally, to permit external access to protected resources inside a perimeter, you can use _access levels_. Access levels apply only to requests for protected resources coming from outside the service perimeter. You can't use access levels to give protected resources or VMs permission to access data and services outside the perimeter.

See [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
