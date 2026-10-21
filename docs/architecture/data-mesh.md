---
url: https://docs.cloud.google.com/architecture/data-mesh/
title: Architecture and functions in a data mesh \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:24.550631+00:00
---

# Architecture and functions in a data mesh  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/data-mesh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Architecture and functions in a data mesh Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-03 UTC

A data mesh is an architectural and organizational framework which treats data as a product (referred to in this document as _data products_). In this framework, data products are developed by the teams that best understand that data, and who follow an organization-wide set of data governance standards. Once data products are deployed to the data mesh, distributed teams in an organization can discover and access data that's relevant to their needs more quickly and efficiently. To achieve such a well-functioning data mesh, you must first establish the high-level architectural components and organizational roles that this document describes.

This document is part of a series which describes how to implement a data mesh on Google Cloud. It assumes that you have read and are familiar with the concepts described in [Build a modern, distributed Data Mesh with Google Cloud](https://services.google.com/fh/files/misc/build-a-modern-distributed-datamesh-with-google-cloud-whitepaper.pdf).

The series has the following parts:

  * Architecture and functions in a data mesh (this document)
  * [Design a self-service data platform for a data mesh](https://docs.cloud.google.com/architecture/design-self-service-data-platform-data-mesh)
  * [Build data products in a data mesh](https://docs.cloud.google.com/architecture/build-data-products-data-mesh)
  * [Discover and consume data products in a data mesh](https://docs.cloud.google.com/architecture/discover-consume-data-products-data-mesh)



In this series, the data mesh that's described is internal to an organization. Although it's possible to extend a data mesh architecture to provide data products to third-parties, this extended approach is outside the scope of this document. Extending a data mesh involves additional considerations beyond just the usage within an organization.

## Architecture

The following key terms are used to define the architectural components which are described in this series:

  * **Data product:** A data product is a logical container or grouping of one or more related data resources.
  * **Data resource:** A data resource is a physical asset in a storage system which holds structured data or stores a query that yields structured data.
  * **Data attribute:** A data attribute is a field or element of a data resource.



The following diagram provides an overview of the key architectural components in a data mesh implemented on Google Cloud.

![Architectural components in a data mesh.](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture.svg)

The preceding diagram shows the following:

  * Central services enable the creation and management of data products, including organizational policies that affect the data mesh participants, access controls (through Identity and Access Management groups), and the infrastructure-specific artifacts. Examples of such commitments and reservations, and infrastructure that facilitates the functioning of the data mesh are described in [Create platform components and solutions](https://docs.cloud.google.com/architecture/design-self-service-data-platform-data-mesh#create_platform_components_and_solutions_using_iac_templates).
  * Central services use [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/introduction) to supply the data catalog for all the data products in the data mesh and the discovery mechanism for potential consumers of these products.
  * Data domains expose subsets of their data as data products through well-defined data consumption interfaces. These data products could be a table, view, structured file, topic, or stream. In BigQuery, it would be a dataset, and in Cloud Storage, it would be a folder or bucket. There can be different types of interfaces that can be exposed as a data product. An example of an interface is a BigQuery view over a BigQuery table. The types of interfaces most commonly used for analytical purposes are discussed in [Build data products in a data mesh](https://docs.cloud.google.com/architecture/build-data-products-data-mesh).



### Data mesh reference implementation

You can find a reference implementation of this architecture in [the `data-mesh-demo` repository](https://github.com/GoogleCloudPlatform/data-mesh-demo). The Terraform scripts that are used in the reference implementation demonstrate data mesh concepts and are not intended for production use. By running these scripts, you'll learn how to do the following:

  * Separate product definitions from the underlying data.
  * Create Data Catalog templates for describing product interfaces.
  * Tag product interfaces with these templates.
  * Grant permissions to the product consumers.



For the product interfaces, the reference implementation creates and uses the following interface types:

  * Authorized views over BigQuery tables.
  * Data streams based on Pub/Sub topics.



For further details, refer to the README file in the repository.

## Functions in a data mesh

For a data mesh to operate well, you must define clear roles for the people who perform tasks within the data mesh. Ownership is assigned to team archetypes, or functions. These functions hold the core user journeys for people who work in the data mesh. To clearly describe user journeys, they have been assigned to user roles. These user roles can be split and combined based on the circumstances of each enterprise. You don't need to map the roles directly with employees or teams in your organization.

A data domain is aligned with a business unit (BU), or a function within an enterprise. Common examples of business domains might be the mortgage department in a bank, or the customer, distribution, finance, or HR departments of an enterprise. Conceptually, there are two domain-related functions in a data mesh: the _data producer_ teams and the _data consumer_ teams. It's important to understand that a single data domain is likely to serve both functions at once. A data domain team _produces_ data products from data that it owns. The team also _consumes_ data products for business insight, and to produce derived-data products for the use of other domains.

In addition to the domain-based functions, a data mesh also has a set of functions that are performed by centralized teams within the organization. These central teams enable the operation of the data mesh by providing cross-domain oversight, services, and governance. They reduce the operational burden for data domains in producing and consuming data products, and facilitate the cross-domain relationships that are required for the data mesh to operate.

This document only describes functions that have a data mesh-specific role. There are several other roles that are required in any enterprise, regardless of the architecture being employed for the platform. However, these other roles are out of scope for this document.

The four main functions in a data mesh are as follows:

  * **Data domain-based producer teams:** Create and maintain data products over their lifecycle. These teams are often referred to as the **data producers**.
  * **Data domain-based consumer teams:** Discover data products and use them in various analytic applications. These teams might consume data products to create new data products. These teams are often referred to as the **data consumers**.
  * **Central data governance team:** Defines and enforces data governance policies among data producers, ensuring high data quality and data trustworthiness for consumers. This team is often referred to as the **data governance team**.
  * **Central self-service data infrastructure platform team:** Provides a self-service data platform for data producers. This team also provides the tooling for central data discovery and data product observability that both data consumers and data producers use. This team is often referred to as the **data platform team**.



An optional extra function to consider is that of a Center of Excellence (COE) for the data mesh. The purpose of the COE is to provide management of the data mesh. The COE is also the designated arbitration team that resolves any conflicts raised by any of the other functions. This function is useful for helping to connect the other four functions.

### Data domain-based producer team

Typically, data products are built on top of a physical repository of data (either single or multiple data warehouses, lakes, or streams). An organization needs traditional data platform roles to create and maintain these physical repositories. However, these traditional data platform roles are not typically the people who create the data product.

To create data products from these physical repositories, an organization needs a mix of data practitioners, such as data engineers and data architects. The following table lists all the domain-specific user roles that are needed in data producer teams.

  
**Role** |   
**Responsibilities** |   
**Required skills** |   
**Desired outcomes**  
---|---|---|---  
  
Data product owner | 

  * Acts as the primary business point of contact for the data product.


  * Is accountable for the definitions, policies, business decisions, and application of business rules for the data exposed as products.


  * Acts as a point of contact for business questions. As such, the owner represents the data domain when meeting with the data consumer teams or the centralized teams (data governance and data infrastructure platform).

|   
Data analytics  
  
Data architecture  
  
Product management | 

  * The data product is driving value for consumers. There's robust management of the lifecycle of the data product, including deciding when to retire a product or release a new version.


  * There's coordination of universal data elements with other data domains.

  
  
Data product technical lead | 

  * Acts as the primary technical point of contact for the product.


  * Is accountable for implementing and publishing product interfaces.


  * Acts as a point of contact for technical questions. As such, the lead represents the data domain when meeting with the data consumer teams or the centralized teams (data governance and data infrastructure platform).


  * Works with the data governance team to define and implement data mesh standards in the organization.


  * Works with the data platform team to help to develop the platform in tandem with the technical needs that production and consumption generate.

|   
Data engineering  
  
Data architecture  
  
Software engineering | 

  * The data product meets business requirements and adheres to the data mesh technical standards.


  * The data consumer teams use the data product and it appears in the results generated by the data product discovery experience.


  * The use of the data product can be analyzed (for example, the number of daily queries).

  
  
  
Data product support | 

  * Acts as the point of contact for production support.


  * Is accountable for maintaining product Service Level Agreement (SLA).

|   
Software engineering  
  
Site reliability engineering (SRE) | 

  * The data product is meeting the stated SLA.


  * Data consumer questions about the use of the data product are addressed and resolved.

  
  
Subject matter expert (SME) for data domain | 

  * Represents the data domain when meeting with SMEs from other data domains to establish data element definitions and boundaries that are common across the organization.


  * Helps new data producers within the domain define their product scopes.

|   
Data analytics  
  
Data architecture | 

  * Collaborates with other SMEs from across data domains to establish and maintain comprehensive understanding of the data in the organization and the data models that it uses.


  * Facilitates the creation of interoperable data products which match the overall data model of the organization.


  * There are clear standards for data product creation and lifecycle management.


  * The data products from the data domain provide business value.

  
  
Data owner | 

  * Is accountable for a content area.


  * Is responsible for data quality and accuracy.


  * Approves access requests.


  * Contributes to data product documentation.

| 

  * Any skill, but must have full knowledge of the business function.


  * Any skill, but must have full knowledge of what the data means and business rules around it.


  * Any skill, but must be able to determine the best possible resolution to data quality issues.

| 

  * Data that cross-functional areas use is accurate.


  * Stakeholders understand the data.


  * Data use is in accordance with usage policies.

  
  
### Data domain-based consumer teams

In a data mesh, the people that consume a data product are typically data users who are outside of the data product domain. These data consumers use a central data catalog to find data products that are relevant to their needs. Because it's possible that more than one data product might meet their needs, data consumers can end up subscribing to multiple data products.

If data consumers are unable to find the required data product for their use case, it's their responsibility to consult directly with the data mesh COE. During that consultation, data consumers can raise their data needs and seek advice on how to get those needs met by one or more domains.

When looking for a data product, data consumers are looking for data that help them achieve various use cases such as persistent analytics dashboards and reports, individual performance reports, and other business performance metrics. Alternatively, data consumers might be looking for data products that can be used in artificial intelligence (AI) and machine learning (ML) use cases. To achieve these various use cases, data consumers require a mix of data practitioner personas, which are as follows:

  
**Role** |   
**Responsibilities** |   
**Required skills** |   
**Desired outcomes**  
---|---|---|---  
  
Data analyst |   
Searches for, identifies, evaluates, and subscribes to single-domain or cross-domain data products to create a foundation for business intelligence frameworks to operate. |   
Analytics engineering  
  
Business analytics | 

  * Provides clean, curated, and aggregated datasets for data visualization specialists to consume.


  * Creates best practices for how to use data products.


  * Aggregates and curates cross-domain datasets to meet the analytical needs of their domain.

  
  
Application developer |   
Develops an application framework for consumption of data across one or more data products, either inside or outside of the domain. |   
Application development  
  
Data engineering | 

  * Creates, serves, and maintains applications that consume data from one or more data products.


  * Creates data applications for end-user consumption.

  
  
Data visualization specialist | 

  * Translates data engineering and data analysis jargon into information which business stakeholders can understand.


  * Defines processes to populate business reports from data products.


  * Creates and monitors reports that describe strategic business goals.


  * Collaborates with engineers within the organization to design datasets which are aggregated from consumed data products.


  * Implements reporting solutions.


  * Translates high-level business requirements into technical requirements.

|   
Requirement analysis  
  
Data visualization | 

  * Provides valid, accurate datasets and reports to end users.


  * Business requirements are met through the dashboards and reports that are developed.

  
  
Data scientist | 

  * Searches for, identifies, evaluates, and subscribes to data products for data science use cases.


  * Extracts data products and metadata from multiple data domains.


  * Trains predictive models and deploys those models to optimize domain business processes.


  * Provides feedback on possible data curation and data annotation techniques for multiple data domains.

|   
ML engineering  
  
Analytics engineering | 

  * Creates predictive and prescriptive models to optimize business processes.


  * Model training and model deployment are done in a timely manner.

  
  
### Central data governance team

The data governance team enables data producers and consumers to safely share, aggregate, and compute data in a self-service manner, without introducing compliance risks to the organization.

To meet the compliance requirements of the organization, the data governance team is a mix of data practitioner personas, which are as follows:

  
**Role** |   
**Responsibilities** |   
**Required skills** |   
**Desired outcomes**  
---|---|---|---  
  
Data governance specialist | 

  * Provides oversight and coordinates a single view of compliance.


  * Recommends mesh-wide privacy policies on data collection, data protection, and data retention.


  * Ensures that data stewards know about policies and can access them.


  * Informs and consults on the latest data privacy regulations as required.


  * Informs and consults on security questions as required.


  * Performs internal audits and shares regular reports on risk and control plans.

|   
Legal SME  
  
Security SME  
  
Data privacy SME | 

  * Privacy regulations in policies are up to date.


  * Data producers are informed of policy changes in a timely manner.


  * Management receives timely and regular reports on policy compliance for all published data products.

  
  
Data steward (sits within each domain) | 

  * Codifies the policies created by the data governance specialists.


  * Defines and updates the taxonomy that an organization uses for annotating data products, data resources, and data attributes with discovery and privacy-related metadata.


  * Coordinates across various stakeholders inside and outside of their respective domain.


  * Ensures that the data products in their domain meet the metadata standards and privacy policies of the organization.


  * Provides guidance to the data governance engineers on how to design and prioritize data platform features.

|   
Data architecture  
  
Data stewardship | 

  * Required metadata has been created for all data products in the domain, and the data products for the domain are described accurately.


  * The self-service data infrastructure platform team is building the right tooling to automate metadata annotations of data products, policy creation and verification.

  
  
Data governance engineer | 

  * Develops tools which auto-generate data annotations and can be used by all data domains, and then uses these annotations for policy enforcement.


  * Implements monitoring to check the consistency of annotations and alerts when problems are found.


  * Ensures that employees in the organization are informed of the status of data products by implementing alerts, reporting, and dashboards.

|   
Software engineering | 

  * Data governance annotations are automatically verified.


  * Data products comply with data governance policies.


  * Data product violations are detected in a timely fashion.

  
  
### Central self-service data infrastructure platform team

The self-service data infrastructure platform team, or just the data platform team, is responsible for creating a set of data infrastructure components. Distributed data domain teams use these components to build and deploy their data products. The data platform team also promotes best practices and introduces tools and methodologies which help to reduce cognitive load for distributed teams when adopting new technology.

Platform infrastructure should provide easy integration with operations toolings for global observability, instrumentation, and compliance automation. Alternatively, the infrastructure should facilitate such integration to set up distributed teams for success.

The data platform team has a shared responsibility model that it uses with the distributed domain teams and the underlying infrastructure team. The model shows what responsibilities are expected from the consumers of the platform, and what platform components the data platform team supports.

As the data platform is itself an internal product, the platform doesn't support every use case. Instead, the data platform team continuously releases new services and features according to a prioritized roadmap.

The data platform team might have a standard set of components in place and in development. However, data domain teams might choose to use a different, unique set of components if the needs of a team don't align with those provided by the data platform. If data domain teams choose a different approach, they must ensure that any platform infrastructure that they build and maintain complies with organization-wide policies and guardrails for security and data governance. For data platform infrastructure that is developed outside of the central data platform team, the data platform team might either choose to co-invest or embed their own engineers into the domain teams. Whether the data platform team chooses to co-invest or embed engineers might depend on the strategic importance of the data domain platform infrastructure to the organization. By staying involved in the development of infrastructure by data domain teams, organizations can provide the alignment and technical expertise required to repackage any new platform infrastructure components that are in development for future reuse.

You might need to limit autonomy in the early stages of building a data mesh if your initial goal is to get approval from stakeholders for scaling up the data mesh. However, limiting autonomy risks creating a bottleneck at the central data platform team. This bottleneck can inhibit the data mesh from scaling. So, any centralization decisions should be taken carefully. For data producers, making their technical choices from a limited set of available options might be preferable to evaluating and choosing from an unlimited list of options themselves. Promoting autonomy of data producers doesn't equate to creating an ungoverned technology landscape. Instead, the goal is to drive compliance and platform adoption by striking the right balance between freedom of choice and standardization.

Finally, a good data platform team is a central source of education and best practices for the rest of the company. Some of the most impactful activities that we recommend central data platform teams undertake are as follows:

  * Fostering regular architectural design reviews for new functional projects and proposing common ways of development across development teams.
  * Sharing knowledge and experiences, and collectively defining best practices and architectural guidelines.
  * Ensuring engineers have the right tools in place to validate and check for common pitfalls like issues with code, bugs, and performance degradations.
  * Organizing internal hackathons so development teams can surface their requirements for internal tooling needs.



Example roles and responsibilities for the central data platform team might include the following:

**Role** | **Responsibilities** |   
**Required skills** | **Desired outcomes**  
---|---|---|---  
  
Data platform product owner | 

  * Creates an ecosystem of data infrastructure and solutions to empower distributed teams to build data products. Lowers the technical barrier to entry, ensures that governance is embedded, and minimizes collective technical debt for data infrastructure.


  * Interfaces with leadership, data domain owners, data governance team, and technology platform owners to set the strategy and roadmap for the data platform.

|   
Data strategy and operations  
  
Product management  
  
Stakeholder management | 

  * Establishes an ecosystem of successful data products.


  * There are robust numbers of data products in production.


  * There's a reduction in time-to-minimum viable product and time-to-production for data product releases.


  * A portfolio of generalized infrastructure and components is in place that addresses the most common needs for data producers and data consumers.


  * There's a high satisfaction score from data producers and data consumers.

  
  
Data platform engineer | 

  * Creates reusable and self-service data infrastructure and solutions for data ingestion, storage, processing, and consumption through templates, deployable architecture blueprints, developer guides, and other documentation. Also creates Terraform templates, data pipeline templates, container templates, and orchestration tooling.


  * Develops and maintains central data services and frameworks to standardize processes for cross-functional concerns such as data sharing, pipelines orchestration, logging and monitoring, data governance, continuous integration and continuous deployment (CI/CD) with embedded guardrails, security and compliance reporting, and FinOps reporting.

|   
Data engineering  
  
Software engineering | 

  * There are standardized, reusable infrastructure components and solutions for data producers to do data ingestion, storage, processing, curation, and sharing, along with necessary documentation.


  * Releases of components, solutions, and end-user documentation align with the roadmap.


  * Users report a high level of customer satisfaction.


  * There are robust shared services for all functions in the data mesh.


  * There is high uptime for shared services.


  * The support response time is short.

  
  
Platform and security engineer (a representative from the central IT teams such as networking and security, who is embedded in the data platform team) | 

  * Ensures that data platform abstractions are aligned to enterprise-wide technology frameworks and decisions.


  * Supports engineering activities by building the technology solutions and services in their core team that are necessary for data platform delivery.

|   
Infrastructure engineering  
  
Software engineering | 

  * Platform infrastructure components are developed for the data platform.


  * Releases of components, solutions, and end-user documentation align with the roadmap.


  * The central data platform engineers report a high level of customer satisfaction.


  * The health of the infrastructure platform improves for components that are used by the data platform (for example, logging).


  * Underlying technology components have a high uptime.


  * When data platform engineers have issues, the support response time is short.

  
  
Enterprise architect | 

  * Aligns data mesh and data platform architecture with enterprise-wide technology and data strategy.


  * Provides advisory and design authority and assurance for both data platform and data product architectures to ensure alignment with enterprise-level strategy and best-practices.

|   
Data architecture   
  
Solution iteration and problem solving  
  
Consensus building | 

  * A successful ecosystem is built that includes robust numbers of data products for which there is a reduction in time to both create minimum viable products and to release those products into production.


  * Architecture standards have been established for critical data journeys, such as by establishing common standards for metadata management and for data sharing architecture.

  
  
## Additional considerations for a data mesh

There are multiple architectural options for an analytics data platform, each option with different prerequisites. To enable each data mesh architecture, we recommend that your organization follow the best practices described in this section.

### Acquire platform funding

As explained in the blog post, "[If you want to transform start with finance](http://zwischenzugs.com/2021/07/12/if-you-want-to-transform-it-start-with-finance/amp/)", the platform is never finished: it's always operating based on a prioritized roadmap. Therefore, the platform must be funded as a product, not as a project with a fixed endpoint.

The first adopter of the data mesh bears the cost. Usually, the cost is shared between the business that forms the first data domain to initiate the data mesh, and the central technology team, which generally houses the central data platform team.

To convince finance teams to approve funding for the central platform, we recommend that you make a business case for the [value](https://lethain.com/should-you-prioritize-infrastructure-costs/) of the centralized platform being realized over time. That value comes from reimplementing [the same components in individual delivery teams](https://medium.com/data-monzo/how-to-think-about-the-roi-of-data-work-fc9aaac84a3c).

### Define the minimum viable platform for the data mesh

To help you to define the minimum viable platform for the data mesh, we recommend that you pilot and iterate with one or more business cases. For your pilot, find use cases that are needed, and where there's a consumer ready to adopt the resulting data product. The use cases should already have funding to develop the data products, but there should be a need for input from technical teams.

Make sure the team that is implementing the pilot understands the data mesh operating model as follows:

  * The business (that is, the data producer team) owns the backlog, support, and maintenance.
  * The central team defines the self-service patterns and helps the business build the data product, but passes the data product to the business to run and own when it's complete.
  * The primary goal is to prove the business operating model (domains produce, domains consume). The secondary goal is to prove the technical operating model (self-service patterns developed by the central team).
  * Because platform team resources are limited, use the [trunk and branch teams](https://lethain.com/trunk-and-branches/) model to pool knowledge but still allow for the development of specialized platform services and products.



We also recommend that you do the following:

  * Plan roadmaps rather than letting services and features evolve organically.
  * Define minimum viable platform capabilities spanning ingest, storage, processing, analysis, and ML.
  * Embed data governance in every step, not as a separate workstream.
  * Put in place the minimum capabilities across governance, platform, value-stream, and change management. Minimum capabilities are those which meet 80% of business cases.



### Plan for the co-existence of the data mesh with an existing data platform

Many organizations that want to implement a data mesh likely already have an existing data platform, such as a data lake, data warehouse, or a combination of both. Before implementing a data mesh, these organizations must make a plan for how their existing data platform can evolve as the data mesh grows.

These organizations should consider factors such as the following:

  * The data resources that are most effective on the data mesh.
  * The assets that must stay within the existing data platform.
  * Whether assets have to move, or whether they can be maintained on the existing platform and still participate in the data mesh.



## What's next

  * To learn more about designing and operating a cloud topology, see the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-03 UTC."],[],[]] 
