---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-service-perimeter/
title: Secure your migrations in a service perimeter \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:09.851902+00:00
---

# Secure your migrations in a service perimeter  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-service-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Secure your migrations in a service perimeter Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls helps you reduce the risk of unauthorized copying or transfer of data from your Google-managed services.

With VPC Service Controls, you can configure service perimeters around the resources of your Google-managed services and control the movement of data across the perimeter boundary.

## Create a service perimeter

To create a service perimeter, follow the [VPC Service Controls guide to creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

When you specify which services you want to restrict, make sure to add all of the following services:

  * VMMigration API (`vmmigration.googleapis.com`)
  * Pub/Sub API (`pubsub.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)
  * Cloud Logging API (`logging.googleapis.com`)
  * Secret Manager API (`secretmanager.googleapis.com`)
  * Compute Engine API (`compute.googleapis.com`)



Your service perimeter must restrict all these services in order for Migrate to Virtual Machines to work with VPC Service Controls.

You should ensure the project in which you enabled the VMMigration API with the Target Projects are included in the perimeter.

## Configure your Migrate Connector in a VPC-SC enabled environment

In an environment that employs VPC-SC, you need to make sure that your Migrate Connector can communicate with the Google Cloud APIs.

You can allow your Migrate Connector to access the VPC-SC environment using several methods. Your available methods depend on the configuration of the VPC-SC environment and whether your Migrate Connector network traffic is routed privately or publicly:

  * If your Migrate Connector network traffic is routed to Google Cloud using VPN or interconnect to the project VPC-SC, see the [VPC-SC private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity) documentation.
  * If your Migrate Connector network traffic is routed using a public network, see the [VPC-SC overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview#internet) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
