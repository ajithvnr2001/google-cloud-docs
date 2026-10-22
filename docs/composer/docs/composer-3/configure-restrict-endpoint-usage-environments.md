---
url: https://docs.cloud.google.com/composer/docs/composer-3/configure-restrict-endpoint-usage-environments/
title: Configure environments with Restrict Endpoint Usage policy \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:06.084617+00:00
---

# Configure environments with Restrict Endpoint Usage policy  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/configure-restrict-endpoint-usage-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Configure environments with Restrict Endpoint Usage policy Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-restrict-endpoint-usage-environments "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page explains how to create Managed Airflow environments when the [Restrict Endpoint Usage](https://docs.cloud.google.com/assured-workloads/docs/restrict-endpoint-usage) organization policy is enforced.

The `constraints/gcp.restrictEndpointUsage` organization policy restricts which Google API endpoints can be used to access resources. This allows organizations to enforce the use of locational or regional endpoints, for example, to satisfy requirements for data to remain within certain geographical areas.

## About Restrict Endpoint Usage policy in Managed Airflow

When you create a Managed Airflow environment in a project where the Restrict Endpoint Usage policy denies access to global endpoints for services like Cloud Storage API, Cloud Logging API, Pub/Sub API, or Data Lineage API, Managed Airflow configures the internal components of the environment to use the corresponding Regional Endpoints (REPs) for these services.

The specific endpoints an environment uses are determined by the Restrict Endpoint Usage policy _only during environment creation_. These endpoints don't change even if the policy is reconfigured later.

## Restricting services required by Managed Airflow environments

When the Restrict Endpoint Usage policy restricts some of the services required by Managed Airflow, the following limitations apply:

  * Airflow task logs in the Airflow UI

Airflow UI relies on the global Cloud Logging endpoint (`logging.googleapis.com`) to display task logs. If you deny `logging.googleapis.com` in your Restrict Endpoint Usage policy, then task logs won't be available in the Airflow UI.

This limitation applies only to the Airflow UI. You will still be able to view [task logs in DAG UI](https://docs.cloud.google.com/composer/docs/composer-3/view-dags#runs-history) and [Airflow worker logs](https://docs.cloud.google.com/composer/docs/composer-3/view-logs) in Google Cloud console and Cloud Logging.

  * Environment metrics

Managed Airflow uses global endpoints for Cloud Monitoring (`monitoring.googleapis.com`) because some Monitoring APIs don't fully support regional endpoints. Restricting `monitoring.googleapis.com` might impact some [environment metrics](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments).

  * Airflow operators in your DAGs

Airflow operators that connect to a global endpoint denied by the Restrict Endpoint Usage policy will fail. Make sure that any Airflow operators in your DAGs are configured to use regional endpoints, if the operator supports it.

  * Customer Managed Encryption Keys (CMEK)

Usage of Customer Managed Encryption Keys isn't supported together with the Restrict Endpoint Usage policy.




## Before you begin

**Warning:** The Restrict Endpoint Usage policy must be active **at the time of environment creation**. Changes made to this policy after an environment [is created](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) **won't be reflected** in existing Managed Airflow environments.

## Configure Restrict Endpoint Usage policy

For more information and examples of how to configure the Restrict Endpoint Usage policy to deny access to specific global endpoints, see [Restricting Endpoint Usage](https://docs.cloud.google.com/assured-workloads/docs/restrict-endpoint-usage).

## Create a Public IP environment with Restrict Endpoint Usage policy

Public IP Managed Airflow environments don't require any additional setup. Do the following:

  1. Check that the services you want to regionalize have regional endpoints available in the selected regions.

  2. Make sure that the Restrict Endpoint Usage policy is already configured and denies global endpoints for the services you intend to regionalize.

  3. [Create a new Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments).

The environment will use regional endpoints according to the Restrict Endpoint Usage policy.




## Create a Private IP environment with Restrict Endpoint Usage policy

To create an environment with Restrict Endpoint Usage policy in the Private IP configuration, you must configure your VPC network to resolve and route traffic to the required Regional Endpoints (REPs) using Private Service Connect and Cloud DNS.

To create a Private IP environment with Restrict Endpoint Usage policy:

  1. Check that the services you want to regionalize have regional endpoints available in the selected regions.

  2. Make sure that the Restrict Endpoint Usage policy is already configured and denies global endpoints for the services you intend to regionalize.

  3. Make sure that you already have a VPC network and subnetwork that you want to use for your Private IP environment.

  4. Repeat the networking configuration steps for each of the following services that are restricted by the Restrict Endpoint Usage policy:

     * `storage.googleapis.com`
     * `logging.googleapis.com`
     * `pubsub.googleapis.com`
     * `datalineage.googleapis.com`
     * Google API endpoints for all other services used in your DAGs.



### Configure Private IP networking for a service restricted with the policy

Apply the following steps to the corresponding Regional Endpoints (REPs) for any Google services in your project where access to their Global Endpoints is restricted.

You must create Private Service Connect endpoints to target regional variations of these services, specifying the region for your Managed Airflow environment. For example, if your environment is located in `us-central1`, you target the `storage.us-central1.rep.googleapis.com` REP for Cloud Storage.

For more information on how to use Private Service Connect endpoints to connect to regional endpoints of supported Google APIs, see [Access regional Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints).

#### Create a Private Service Connect endpoint

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list/consumers)

  2. Click **Connect endpoint**.

  3. Configure a Private Service Connect endpoint as follows:

     * Target: Select **Google APIs**.

     * Target Details:

       1. Scope: Select `Regional`.
       2. Region: Select the region of your Managed Airflow environment.
       3. Target service: Select the service you're configuring. This selects a REP in the selected region.

Example:

If your environment is located in `us-central1` and you're configuring Cloud Storage, then select `Iowa (us-central1)`, and `Cloud Storage (storage.us-central1.rep.googleapis.com)`.

     * Endpoint Details:

       1. Endpoint name: A name for the endpoint.

Example: `psc-storage-endpoint-us-central1`.

       2. Network and Subnetwork: Select the VPC network and subnetwork of your Managed Airflow environment.

       3. IP address: Choose an existing IP address, or click **Create IP address** to reserve a new static internal IP address from the selected subnetwork.

Give this IP address a descriptive name. You will use this IP address later to configure a DNS record.

Example: `psc-storage-us-central1`.

  4. Click **Add endpoint**.




#### Create a private DNS zone

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/zones)

  2. Click **Create zone**.

  3. In **Zone type** , select `Private`.

  4. Specify the following configuration:

     * Zone name: A name for the zone.

Example: `storage-us-central1`

     * DNS name: A DNS name. Include the trailing dot.

Example: `storage.us-central1.rep.googleapis.com.`

     * Networks: Select the VPC network for your Managed Airflow environment.

  5. Click **Create**.




#### Add a DNS record in the created DNS zone

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/zones)

  2. Click the name of the zone you've created.

  3. Click **Add standard**.

  4. Configure the DNS record as follows:

     * DNS name: Specify the subdomain of the DNS zone.

Example: `storage.us-central1.rep.googleapis.com`

     * Resource record type: Select `A`.

     * IPv4 Address: Select the IP address that you assigned to the Private Service Connect endpoint.

  5. Click **Create**.




### Create a Private IP Managed Airflow environment

After you've configured all services that will be used by your environment, proceed to [create a Private IP environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#networking) in the selected VPC network and subnetwork.

## What's next

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)
  * [Access regional Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints)
  * [Restrict Endpoint Usage](https://docs.cloud.google.com/assured-workloads/docs/restrict-endpoint-usage)
  * [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
