---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-overview/
title: Marketplace overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:49.125892+00:00
---

# Marketplace overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Marketplace overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the software packages available in the Google Distributed Cloud (GDC) air-gapped Marketplace. The air-gapped Marketplace is a catalog of solutions from Google and our partner ecosystems that are ready to run in your isolated environment.

This page is for audiences such as developers within the application operator group who are interested in finding pre-configured software solutions. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

Software you install using the Distributed Cloud Marketplace is not managed by default: they run in your projects, under your responsibility. See [Marketplace shared responsibility model](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/shared-responsibility-model) to learn more.

All software packages available in the Distributed Cloud Marketplace are validated by Google and the relevant partner, and can be installed and managed while being disconnected from the Internet. You might need an Internet connection to consult the documentation or other links provided by third-party software vendors.

## Benefits

  * **Speed** : Deploy pre-configured solutions quickly so you can get your applications up and running faster.
  * **Reduced risk** : Pre-configured solutions are tested and certified by Google.
  * **Flexibility** : You can choose from a wide variety of solutions to meet your specific needs.



## Billing and support

For third-party software, the Distributed Cloud Marketplace supports a bring-your-own-license (BYOL) model that lets you reuse your existing licenses or procure new ones and get support directly from a relevant vendor. As outlined in the shared responsibility model, the vendor is responsible for providing your support on their software. Google and your Infrastructure Operator can collaborate with the vendor directly if needed to solve a problem coming from an unexpected interaction between their software and the Distributed Cloud platform.

## Available software packages

The following software packages are available on the Distributed Cloud Marketplace. Go to the relevant page in the Distributed Cloud Marketplace UI to learn more about each of the packages as well as about their pricing model and terms of services in particular. All third-party vendors available on the Distributed Cloud Marketplace have earned the [Google Cloud Ready - Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/docs/cloudready) designation. Learn how to install them in [Life Cycle of a marketplace deployment](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-lifecycle).

  1. [Dataproc Container for Spark](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-offerings). An open source Google project which lets you run Apache Spark on GKE on GDC clusters.
  2. [Elastic Cloud on Kubernetes](https://www.elastic.co/guide/index.html) (BYOL). Elastic provides flexible search, monitoring, and security solutions based on Elasticsearch. See the [Elastic Cloud on Kubernetes quickstart](https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-quickstart.html) to get started.
  3. MongoDB Enterprise Advanced (BYOL). A collection of products and services that drive security, efficiency, and put you in control of your MongoDB databases using the [MongoDB Enterprise Kubernetes Operator](https://www.mongodb.com/docs/kubernetes-operator/master/).
  4. [Starburst Enterprise](https://docs.starburst.io/latest/index.html) (BYOL). A fast, scalable, distributed MPP SQL engine for your Data Lakehouse with query federation to many other data sources. 
  5. [HashiCorp Vault](https://developer.hashicorp.com/vault/tutorials/kubernetes/vault-secrets-operator) (BYOL). An identity-based secrets and encryption management system.
  6. [Apache Kafka on Confluent Platform](https://docs.confluent.io/platform/current/overview.html) (BYOL). A solution that allows real-time access, storage, and management of continuous data streams.
  7. [Redis Software for Kubernetes](https://redis.io/docs/latest/operate/kubernetes/deployment/) (BYOL). Redis is the world's fastest in-memory database for building and scaling fast applications.
  8. [MariaDB Operator](https://mariadb.com/docs/tools/mariadb-enterprise-operator) (BYOL). MariaDB Operator uses supported Docker images to provide a fleet management and HA/DR solution for MariaDB Enterprise Server and MaxScale.
  9. [Neo4j](https://neo4j.com/docs/) (BYOL). Neo4j is an open-source, NoSQL, built-in graph database that provides an ACID-compliant transactional backend for your applications. 
  10. GDC Mandiant SOC Solutions (BYOL and BYOM). Elevate security posture with GDC's flexible SOC solutions by [contacting Mandiant](https://www.mandiant.com/contact-us).
  11. [Mandiant Consulting Services](https://cloud.google.com/security/consulting/mandiant-services) (Professional services). Maximize your security program's effectiveness with Mandiant Consulting services that are grounded in frontline experience.
  12. GitLab (BYOL and BYOM). GitLab is the most comprehensive AI-powered DevSecOps platform. Learn how to [deploy GitLab Enterprise Edition on GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/gitlab).
  13. [Mattermost Enterprise Edition](https://docs.mattermost.com/) (BYOL). A secure, sovereign collaboration platform built for mission-critical operations. Mattermost requires additional setup prior to installation, including PostgreSQL and object storage configuration. See the Mattermost documentation for prerequisite installation steps.



If you have accreditation requirements, some of these software packages may not be listed in your instance of the Distributed Cloud Marketplace. Your Infrastructure Operator controls which packages are actually available for installation in your environment.

Consult the list of [Marketplace images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/mkt-images) to know exactly which images are included in your version of GDC. Images that were included in previous versions of GDC remain available for use, even after an upgrade of GDC.

## Differences with the Google Cloud Marketplace

The Distributed Cloud Marketplace is separate from the Google Cloud Marketplace due to its air-gapped nature. Many of the same vendors are present in both, but sometimes with different products: the same vendor may offer a multi-tenant Software as a service (SaaS) solution on Google Cloud and a single-tenant on-premises product on the Distributed Cloud Marketplace.

Today, you cannot buy a product on the Google Cloud Marketplace whether with a public price, or a private offer, and use it on the Distributed Cloud Marketplace.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
