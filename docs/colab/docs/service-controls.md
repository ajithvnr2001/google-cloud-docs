---
url: https://docs.cloud.google.com/colab/docs/service-controls/
title: Use VPC Service Controls with Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:30:22.138761+00:00
---

# Use VPC Service Controls with Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use VPC Service Controls

This page describes how to use VPC Service Controls to set up a Colab Enterprise notebook within a service perimeter.

## Overview

VPC Service Controls is a Google Cloud feature that lets you set up a perimeter that helps guard against data exfiltration.

VPC Service Controls provides an extra layer of defense for Google Cloud services that is independent of the protection provided by Identity and Access Management (IAM).

When you use Colab Enterprise within a service perimeter, runtimes are subject to the service perimeter. Therefore, to run notebook code that interacts with other Google APIs and services, you must add those services to the service perimeter.

For more information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Known limitations

  * Colab Enterprise uses Dataform for storing notebooks.

To learn more about using VPC Service Controls with Dataform, see [Configure VPC Service Controls for Dataform](https://docs.cloud.google.com/dataform/docs/vpc-service-controls).

  * The Colab Enterprise UI is only accessible from the Google Cloud console. To learn about VPC Service Controls limitations for the Google Cloud console, see the [Google Cloud console limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#console).

  * If your service perimeter needs access to Gemini Enterprise Agent Platform services, see [VPC Service Controls with Colab Enterprise limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls#limitations).

  * **Data Science Agent setup delay** : If a service perimeter is applied to a project where the Data Science Agent was previously used, there might be a delay of up to one week before the agent functions correctly within the perimeter. During this interval, requests to the agent might trigger VPC Service Controls violations.




### Required roles

To get the permissions that you need to use VPC Service Controls with Colab Enterprise, ask your administrator to grant you the following IAM roles on the project: 

  * [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`)
  * [Colab Enterprise User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabEnterpriseUser) (`roles/aiplatform.colabEnterpriseUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

For more information about VPC Service Controls permissions, see [Access control with IAM](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

## Create a service perimeter

  1. [Create a service perimeter by using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters). This service perimeter protects the Google-managed resources of services that you specify. While creating your service perimeter, do the following:

     1. When it's time to add projects to your service perimeter, add the project that contains your Colab Enterprise notebooks, or create notebooks in this project.

     2. When it's time to add services to your service perimeter, add the following:

        * **Agent Platform API** (`aiplatform.googleapis.com`)
        * **Dataform API** (`dataform.googleapis.com`)
**Note:** If you're using other services, add them. For example, you might want to use BigQuery (`bigquery.googleapis.com`), Cloud Storage (`storage.googleapis.com`), Managed Service for Apache Spark (`dataproc.googleapis.com`), or other services.

If you have created your service perimeter without adding the projects and services you need, see [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters) to learn how to update your service perimeter.




## Provide access to the Colab Enterprise UI

Because the Colab Enterprise UI (`colab-embedded.cloud.google.com`) is only accessible over the internet, the Colab Enterprise UI is treated as outside of service perimeters. When you apply a service perimeter, the Google Cloud console interface for the services that you protected might become partially or fully inaccessible. For example, if you protect Colab Enterprise with the perimeter, the Colab Enterprise interface in the Google Cloud console becomes inaccessible.

**Note:** If you remove your public IP address, your Colab Enterprise notebooks won't be able to access pip and other public package libraries for installation.

To allow access from the Google Cloud console to resources protected by a perimeter, you need to create an access level for a public IP range that includes the machines of users who want to use the Google Cloud console with protected APIs. For example, you could add the public IP range of the NAT gateway of your private network to an access level, and then assign that access level to the service perimeter.

If you want to limit Google Cloud console access to the perimeter to only a specific set of users, you can also add those users to an access level. In that case, only the specified users would be able to access the Google Cloud console.

**Note:** Requests through Google Cloud console from a network that is Private Google Access enabled, including networks implicitly enabled by Cloud NAT, might be blocked even if the requesting source network and target resource are in the same perimeter. This is because Google Cloud console access through Private Google Access is not supported by Colab Enterprise.

## Set up VPC accessible services (optional)

When you enable VPC accessible services for a perimeter, access from network endpoints inside your perimeter is limited to a set of services that you specify.

To learn more about how to limit access inside your perimeter to only a specific set of services, read about [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

## Use Private Google Access with your VPC network (optional)

Private Google Access offers private connectivity to hosts in either a VPC network or an on-premises network that uses private IP addresses to access Google Cloud APIs and services. You can extend a VPC Service Controls service perimeter to hosts in those networks to control access to protected resources. Hosts in a VPC network must have a private IP address only (no public IP address) and be in a subnet with Private Google Access enabled. For more information, see [private connectivity from on-premises networks](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity).

To make sure that you can use Private Google Access with your VPC network, you must configure some DNS records.

### Configure your DNS entries using Cloud DNS

Colab Enterprise runtimes use several domains that a VPC network doesn't handle by default. To make sure that your VPC network correctly handles requests sent to those domains, use Cloud DNS to add DNS records. For more information about VPC routes, see [Routes](https://docs.cloud.google.com/vpc/docs/routes).

This section shows you how to create a [managed zone](https://docs.cloud.google.com/dns/zones) for a domain, add a DNS entry that will route the request, and run the transaction. Repeat these steps for each of several domains that you need to handle requests for, starting with `*.aiplatform.googleapis.com`.

In Cloud Shell or any environment where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed, enter the following [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands.

  1. To create a private managed zone for one of the domains that your VPC network needs to handle: 
         
         gcloud dns managed-zones create ZONE_NAME \
                 --visibility=private \
                 --networks=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME \
                 --dns-name=DNS_NAME. \
                 --description="Description of your managed zone"
             

Replace the following: 

     * `ZONE_NAME`: A name for the zone to create. You must use a separate zone for each domain. This zone name is used in each of the following steps. 
     * `PROJECT_ID`: The ID of the project that hosts your VPC network. 
     * `NETWORK_NAME`: The name of the VPC network that you created earlier. 
     * `DNS_NAME`: The part of the domain name that comes after the `*.`. For example, `*.aiplatform.googleapis.com` has a DNS name of `aiplatform.googleapis.com`. 
  2. Start a transaction. 
         
         gcloud dns record-sets transaction start --zone=ZONE_NAME
             

  3. Add the following DNS A record. This reroutes traffic to Google's restricted IP addresses. 
         
         gcloud dns record-sets transaction add \
                 --name=DNS_NAME. \
                 --type=A 199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7 \
                 --zone=ZONE_NAME \
                 --ttl=300
             

  4. Add the following DNS CNAME record to point to the A record that you just added. This redirects all traffic matching the domain to the IP addresses listed in the previous step. 
         
         gcloud dns record-sets transaction add \
                 --name=\*.DNS_NAME. \
                 --type=CNAME DNS_NAME. \
                 --zone=ZONE_NAME \
                 --ttl=300
             

  5. Run the transaction. 
         
         gcloud dns record-sets transaction execute --zone=ZONE_NAME
             

  6. Repeat these steps for each of the following domains. For each repetition, change ZONE_NAME and DNS_NAME to the appropriate values for that domain. Keep PROJECT_ID and NETWORK_NAME the same each time. You already completed these steps for `*.aiplatform.googleapis.com`. 

     * `*.aiplatform.googleapis.com`
     * `*.aiplatform-notebook.googleusercontent.com`
     * `*.aiplatform-notebook.cloud.google.com`
**Note:** If you're using other services, add DNS entries for them. For example, if you want to connect to Managed Service for Apache Spark from private IP address hosts, add DNS entries for `dataproc.byoid.googleusercontent.com` and `dataproc.googleusercontent.com`. Create these DNS entries even when VPC Service Controls is not in-use. 



To learn more about configuring private connectivity, read [Set up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

## Allow context-aware access from outside a service perimeter using ingress rules

You can allow context-aware access to resources restricted by a perimeter based on client attributes. You can specify client attributes, such as identity type (service account or user), identity, device data, and network origin (IP address or VPC network).

For example, you can set up ingress rules to allow internet access to resources within a perimeter based on the range of IPv4 and IPv6 addresses. For more information about using ingress rules to set up context-aware access, see [Context-aware access](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access).

## Configure secure data exchange using ingress and egress rules

You can include your project in only one service perimeter. If you want to allow communication across the perimeter boundary, set up ingress and egress rules. For example, you can specify ingress and egress rules to let projects from multiple perimeters to share logs in a separate perimeter. To learn more about secure data exchange use cases, read [secure data exchange](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange).

## Data Science Agent support

The Colab Enterprise Data Science Agent supports VPC Service Controls. When you restrict the **Agent Platform API** (`aiplatform.googleapis.com`) in your service perimeter, the Data Science Agent and its operations are restricted by the perimeter. This configuration ensures that both the initial requests to the Data Science Agent and any subsequent service calls initiated by the agent are subject to the service perimeter protections.

## What's next

  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

  * Learn more about [Colab Enterprise runtimes](https://docs.cloud.google.com/colab/docs/runtimes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
