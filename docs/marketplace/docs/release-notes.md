---
url: https://docs.cloud.google.com/marketplace/docs/release-notes/
title: Cloud Marketplace release notes \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:37.303468+00:00
---

# Cloud Marketplace release notes  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Resources ](https://docs.cloud.google.com/marketplace/docs/release-notes)



Send feedback 

#  Cloud Marketplace release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the latest release notes for features and updates to Cloud Marketplace. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gcpmarketplace-release-notes.xml) directly. 

## March 26, 2025

Feature

Google Cloud Private Marketplace now lets you control access at the product level, across all deployment surfaces (Cloud Marketplace, API, and the command line), for the following types of products:

  * Compute Engine products
  * Google Kubernetes Engine products
  * Cloud Run
  * Procurable Vertex AI products
  * Procurable data products



If you've ever previously turned on Private Marketplace, you must upgrade it to ensure that it properly blocks API deployments of unapproved products. For more information, see [Upgrade Google Cloud Private Marketplace's enforcement capabilities](https://docs.cloud.google.com/marketplace/docs/migrations/private-marketplace-api-enforcement).

## July 29, 2024

Announcement

[Google Private Marketplace](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace) and [Product Requests](https://docs.cloud.google.com/marketplace/docs/governance/product-requests) are now Generally Available.

  * Google Private Marketplace lets organizations govern their software usage and control costs by ensuring that their users can only procure Google Cloud Marketplace solutions that have been approved by administrators, FinOps, or procurement team members.
  * Product Requests lets your users file requests to use or procure specific products.



## October 01, 2023

Change

Beginning in October 2023, Google Cloud Marketplace supports a new transaction model, the agency model. For details about the agency model and which transactions it applies to, see the [transaction models](https://docs.cloud.google.com/marketplace/docs/transaction-models) documentation.

## January 26, 2023

Announcement

Private Offers, version 2, is now **Generally available**. Vendors can customize quotes that discount a flat fee, usage, or installments.

## November 18, 2022

Feature

You can [download private offers as PDFs](https://docs.cloud.google.com/marketplace/docs/manage-accepted-offer). Offers can include notes from the vendor and the included EULA.

## November 09, 2022

Feature

Curate which products are available for your Organization to use with Private Marketplace ([Preview](https://cloud.google.com/products/?hl=EN#product-launch-stages)). You can add products to _collections_ and share these collections with your organization, folders, or projects. 

[Learn more about Private Marketplace](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace).

## September 15, 2022

Feature

Vendors can now provide private offers with more granular discounts on usage metrics.

## January 06, 2022

Feature

You can allow your Organization's members to request Cloud Marketplace SaaS products for procurement.

[Learn more about enabling procurement requests.](https://docs.cloud.google.com/marketplace/docs/governance/procurement-requests)

## July 13, 2020

Change

The IAM permissions required for purchasing the following solutions from Google Cloud Marketplace have changed:

  * Apache Kafka® on Confluent Cloud™
  * DataStax Astra for Apache Cassandra
  * Elasticsearch Service on Elastic Cloud
  * NetApp Cloud Volumes Service
  * Redis Enterprise Cloud



If you use [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles) to purchase these solutions, you must update the custom roles to include the permissions described in [Access Control for Google Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/access-control).

Specifically, if your custom role includes the `billing.subscriptions.create` permission, you must update it to include the `consumerprocurement.orders.place` and the `consumerprocurement.accounts.create` permissions.

If you use the [Billing Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) role to purchase these solutions, you don't need to take any action.

## April 14, 2020

Change

Security software agents on Google Cloud Marketplace are now **Generally available**.

Security software agents are typically part of larger security solutions, and can be deployed to VM instances in your projects.

[Learn about Deploying security software agents](https://docs.cloud.google.com/marketplace/docs/deploy-security-software-agents).

## February 27, 2020

Feature

You can deploy security software agents, which are typically part of larger security solutions, from Google Cloud Marketplace to the VM instances in your projects.

[Learn about Deploying security software agents](https://docs.cloud.google.com/marketplace/docs/deploy-security-software-agents).

## May 10, 2019

Feature

Vendors of managed services and Kubernetes applications can now offer trials of their software. During trials, you can use the software without paying for the software license.

For information on how you are billed during a trial, see [Understanding Billing](https://docs.cloud.google.com/marketplace/docs/understanding-billing).

## April 09, 2019

Feature

Kubernetes applications on GCP Marketplace are now **Generally Available**.

For steps to set up a billing plan for Kubernetes applications, see [Managing Billing Plans for Kubernetes Applications](https://docs.cloud.google.com/marketplace/docs/kubernetes-apps/manage-billing-kubernetes).

Change

Some vendors provide Kubernetes applications that can run on GKE On-Prem clusters, and clusters that run Istio.

Learn about the [prerequisites for running Kubernetes applications with GKE On-Prem or Istio](https://docs.cloud.google.com/marketplace/docs/kubernetes-apps#on-prem-istio-prereqs).

## July 23, 2018

Feature

Vendors of VM solutions can offer trials of their software. During trials, you can use the software without paying for the software license.

For information on how you are billed during a trial, see [Understanding Billing](https://docs.cloud.google.com/marketplace/docs/understanding-billing).

## July 18, 2018

Change

Google Cloud Launcher is now Google Cloud Platform Marketplace.

Feature

GCP Marketplace now includes commercial Kubernetes applications, which you can deploy to your Google Kubernetes Engine clusters.

For steps to set up a billing plan for Kubernetes applications, see [Managing Billing Plans for Kubernetes Applications](https://docs.cloud.google.com/marketplace/docs/kubernetes-apps/manage-billing-kubernetes).

Deprecated

The container registry `launcher.gcr.io` is deprecated. For steps you need to take to modify your scripts or configurations, as applicable, see [Deploying Containers](https://docs.cloud.google.com/marketplace/docs/container-images).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
