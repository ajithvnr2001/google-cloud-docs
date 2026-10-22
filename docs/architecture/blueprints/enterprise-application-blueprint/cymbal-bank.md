---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/cymbal-bank/
title: Cymbal Bank application architecture \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:10.559437+00:00
---

# Cymbal Bank application architecture  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/cymbal-bank/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Cymbal Bank application architecture Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

The blueprint includes a sample application that is named _Cymbal Bank_. Cymbal Bank demonstrates the best practices that are recommended for containerized applications. The Cymbal Bank application lets users create login accounts, sign in to their account, see their transaction history, make deposits, and transfer money to other users' accounts. Cymbal Bank services run as containers that connect to each other over [REST APIs](https://en.wikipedia.org/wiki/Representational_state_transfer) and [gRPC APIs](https://grpc.io/).

The following diagram shows the Cymbal Bank application that is deployed on the blueprint developer platform.

![Cymbal Bank architecture.](https://docs.cloud.google.com/static/architecture/blueprints/enterprise-application-blueprint/images/eab-cymbal-bank.svg)

Each application is also a network service. Only the frontend application is exposed externally to the cluster through the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api). All applications run as distributed services through the use of [Cloud Service Mesh](https://cloud.google.com/products/service-mesh).

For more information about the services that are included in the Cymbal Bank application, see the [Cymbal Bank repository on GitHub](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application/tree/main/examples/cymbal-bank).

## Cymbal Bank tenants

To provide separation between tenants, each tenant in the developer platform has one [team scope](https://docs.cloud.google.com/anthos/fleet-management/docs/team-management) and at least one fleet namespace. Tenants never share a namespace. To deploy Cymbal Bank, each tenant only needs one namespace. In more complex scenarios, a tenant can have several namespaces.

To illustrate how Cymbal Bank is deployed on the developer platform, this example assumes that there were three separate application development teams with different focus areas. The Terraform creates the following developer platform tenant for each of those teams:

  * **`frontend` tenant**: A development team that focuses on the website and mobile application backends.
  * **`accounts` tenant**: A development team that focuses on customer data.
  * **`ledger` tenant**: A team that manages the ledger services.



## Cymbal Bank apps

The Cymbal Bank application consists of six microservices: `frontend, ledgerwriter, balancereader, transactionhistory, userservice`, and `contacts`. Each microservice is mapped to an application within the tenant that owns it.

The following table describes the mapping of the teams, team scope, fleet namespace, and microservices for Cymbal Bank. For the purpose of this mapping, this example assumes that Cymbal Bank is developed by three separate application operator teams. Teams manage a varying number of services. Each team is assigned a team scope.

Team | Team scope | Fleet namespace | Application - Microservice | Kubernetes service account  
---|---|---|---|---  
Frontend team | `frontend` | `frontend` | [`frontend`](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application/tree/main/examples/cymbal-bank/5-appinfra/cymbal-bank/frontend) | `ksa-frontend`  
Ledger team | `ledger` | `ledger` | [`ledgerwriter`](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application/tree/main/examples/cymbal-bank/5-appinfra/cymbal-bank/ledger-ledgerwriter) | `ksa-ledgerwriter`  
[`balancereader`](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application/tree/main/examples/cymbal-bank/5-appinfra/cymbal-bank/ledger-balancereader) | `ksa-balancereader`  
[`transactionhistory`](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application/tree/main/examples/cymbal-bank/5-appinfra/cymbal-bank/ledger-transactionhistory) | `ksa-transactionhistory`  
Accounts team | `accounts` | `accounts` | [`userservice`](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application/tree/main/examples/cymbal-bank/5-appinfra/cymbal-bank/accounts-userservice) | `ksa-userservice`  
[`contacts`](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application/tree/main/examples/cymbal-bank/5-appinfra/cymbal-bank/accounts-contacts) | `ksa-contacts`  
  
## Cymbal Bank database structure

Cymbal Bank databases are deployed using [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview). The databases are configured with a [highly available primary instance](https://docs.cloud.google.com/alloydb/docs/overview#ha) in one [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) with redundant nodes in different zones, and [cross-region replicas](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication) are used for disaster recovery. Cymbal Bank uses [IAM database authentication](https://docs.cloud.google.com/alloydb/docs/manage-iam-authn#enable) to allow services access to the databases. The databases are encrypted using [CMEK](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek). Two PostgreSQL databases are used: `ledger-db` for the ledger, and `accounts-db` for user accounts.

## What's next

  * Read about [mapping BeyondProd security principles to the blueprint](https://docs.cloud.google.com/architecture/enterprise-application-blueprint/mapping-beyondprod-security-principles) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
