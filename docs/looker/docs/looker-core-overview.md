---
url: https://docs.cloud.google.com/looker/docs/looker-core-overview/
title: Looker (Google Cloud core) overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:35:02.891046+00:00
---

# Looker (Google Cloud core) overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker (Google Cloud core) overview Stay organized with collections  Save and categorize content based on your preferences. 

Looker (Google Cloud core) provides simplified and streamlined provisioning, configuration, and management of a Looker instance from the Google Cloud console. Some instance administration tasks may also be performed from the console.

Looker (Google Cloud core) instances are hosted by Google in the Google Cloud. Looker (Google Cloud core) is not available for customer-hosted or multicloud environments.

## Looker (Google Cloud core) editions

Looker (Google Cloud core) is available in several editions. Each edition type offers different [functionality](https://docs.cloud.google.com/looker/docs/looker-core-edition-types) and has different [pricing](https://cloud.google.com/looker/pricing). When you create a Looker (Google Cloud core) instance, you choose the edition that meets your needs. Once an instance has been created, you cannot change the edition type. You can also provision, configure, and manage non-production instances of the same edition types for staging and testing. See Staging environments and testing section on this page for things to know about setting up a non-production instance.

### Standard edition

The **Standard** edition is tailored for small teams and small or medium-sized businesses with up to 50 internal platform users. In addition to many existing Looker (Google Cloud core) features, the **Standard** edition brings new functionality, which includes the following:

  * [Google Cloud Identity access management](https://docs.cloud.google.com/iam/docs) and simplified BigQuery connectivity.
  * Support for up to 1,000 query-related Looker (Google Cloud core) [API calls](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) per month and 1,000 admin-related Looker (Google Cloud core) API calls per month. For more information about the API, see the Use the Looker (Google Cloud core) API section.



A **Standard** edition can be purchased through an annual contract.

### Enterprise edition

The **Enterprise** edition includes all the features of the **Standard** edition as well as supporting the following:

  * Unlimited users.
  * Additional security features such as [VPC-SC](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc), [Private connections (Private Service Connect)](https://docs.cloud.google.com/looker/docs/looker-core-create-psc), and [Private connections (private services access)](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip).
  * A [private label](https://docs.cloud.google.com/looker/docs/privatelabel) option.
  * More robust monitoring through the [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) feature.
  * 100,000 query-related Looker (Google Cloud core) [API calls](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) per month and 10,000 admin-related Looker (Google Cloud core) API calls per month. For more information about the API, see the Use the Looker (Google Cloud core) API section on this page.



An **Enterprise** edition can be purchased through an annual contract.

### Embed edition

The **Embed** edition includes all the features of the **Enterprise** edition as well as offering the following:

  * [Signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding)
  * [Custom themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores)
  * 500,000 query-related Looker (Google Cloud core) [API calls](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) per month and 100,000 admin-related Looker (Google Cloud core) API calls per month. For more information about the API, see the Use the Looker (Google Cloud core) API section on this page.



An **Embed** edition can be purchased through an annual contract.

**Note:** If you purchase an Embed Looker (Google Cloud core) edition, we recommend that you also purchase at least one non-production Embed instance for staging.

## Non-production instances

If you want to use a staging or testing instance, you can [create a non-production instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) by using the standard process for creating a Looker (Google Cloud core) instance, and selecting the appropriate non-production edition. The billing for this non-production instance will be the same as for any other Looker (Google Cloud core) instance. See the [Looker (Google Cloud core) pricing](https://cloud.google.com/looker/pricing) page for more details.

The types of non-production instance editions are the same as the editions that are available for production instances, and include the following:

  * Standard edition
  * Enterprise edition
  * Embed edition



The functionalities that are available for each non-production edition are the same as the functionalities that are available for the production editions. Non-production Looker (Google Cloud core) instances also can have the same [network connection types](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type) as production instances. Having the same functionalities in all environments lets you configure your staging environment to match your production environment, and test updates before deploying to your production instance.

**Note:** If you purchase an Embed Looker (Google Cloud core) edition, we recommend that you also purchase at least one non-production Embed instance.

### Characteristics of non-production instances

The following are things to know about non-production Looker (Google Cloud core) instances:

  * Non-production instances are not covered by any Google SLAs.
  * Horizontal scaling is not considered a non-production use case. If you need to spread instance load and offer specific geographical distribution across multiple Looker (Google Cloud core) instances for your production use case, you will need to purchase additional instances of the existing production Looker (Google Cloud core) edition.
  * Non-production Looker (Google Cloud core) instances cannot be used in lieu of a production instance or for production purposes.
  * All production and non-production Looker (Google Cloud core) instances adhere to the same release cycle. You can configure your non-production instance maintenance settings to match your [production instance maintenance settings](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#maintenance_settings).



## Trial Instances

If you want to try out Looker (Google Cloud core), you can create a trial Standard, Enterprise, or Embed edition instance that will have the same feature support as the corresponding production edition. Trial editions have the following limitations:

  * Trial editions instances are valid for 90 days. After 90 days have passed, you are required to delete or upgrade your instance.
  * There is no option to upgrade to a non-trial edition instance directly. To upgrade, you will need to create a new instance and then [import your data](https://docs.cloud.google.com/looker/docs/looker-core-import-export) from the trial instance.
  * For each combination of Google Cloud project and Google Cloud region, there is a limitation of one active trial for each edition type.
  * [Data Studio Pro licenses](https://docs.cloud.google.com/looker/docs/admin-panel-platform-lsp) are not included with a trial edition, or any Looker (Google Cloud core) instances that are created after August 1, 2026..



## Looker (Google Cloud core) features

Learn about Looker (Google Cloud core) features by [edition](https://docs.cloud.google.com/looker/docs/looker-core-edition-types) and [network connection](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_configuration).

Functionality that is specific to Looker (Google Cloud core) is documented in the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core). All other Looker functionality, including functionality that is shared between Looker (Google Cloud core) and Looker (original), is documented in the [Looker (original) documentation](https://docs.cloud.google.com/looker/docs).

Most Looker (Google Cloud core) functionality is the same as Looker (original) functionality, with a few differences.

The following section compares Looker (Google Cloud core) features with Looker (original) features.

### Looker (Google Cloud core) features versus Looker (original) features

The following table compares feature support for Looker (Google Cloud core) versus [Looker-hosted Looker (original)](https://docs.cloud.google.com/looker/docs/intro) and [customer-hosted Looker (original)](https://docs.cloud.google.com/looker/docs/choosing-hosting-option#benefits_and_limits_of_the_customer-hosted_option) instance types.

Comparison Matrix

Filter the table on supported instance types:

Looker (original)

Looker (Google Cloud core)

Customer-hosted Looker (original)

Select all Clear all

Feature | Looker instance type |   
---|---|---  
**Platform features** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
**[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)** : Conversational Analytics, Code Interpreter, LookML writing assistance, and Visualization Assistant | **Yes** | **Yes** | No | Gemini assistance is not supported for Looker (Google Cloud core) instances that use CMEK or VPC Service Controls or for Looker (Google Cloud core) instances that are connected to Data Studio through the [Looker connector](https://docs.cloud.google.com/looker/docs/studio/connect-to-looker).[Publishing data agents to Gemini Enterprise](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#publish-data-agents) isn't supported in Looker (Google Cloud core) instances that use private or hybrid network connections.  
**[Looker-managed MCP server](https://docs.cloud.google.com/looker/docs/mcp)** : A Model Context Protocol (MCP) server provided directly by the Looker platform. | **Yes** | **Yes** | No |  The Looker-managed MCP server is in [preview](https://cloud.google.com/products#product-launch-stages). It is the recommended method for connecting AI applications to Looker instances that are hosted by Looker. Customer-hosted instances can use the standalone [MCP Toolbox](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox#install-standalone) instead.  
**[BI Connectors: Connected Sheets and Looker Studio](https://docs.cloud.google.com/looker/docs/bi-connectors)** : Use Google Sheets to explore data from your LookML models or connect to Looker Studio data in your Looker instance. | **Yes** | **Yes** | No |  Complimentary licenses to use Looker Studio Pro are not available for customer-hosted Looker (original) instances. For private connections configurations in Looker (Google Cloud core) instances, your network administrator must configure your network so that traffic from Google Sheets or Looker Studio can reach your Looker instance.  
**[BI Connectors: Microsoft Excel, Microsoft Power BI, Tableau Desktop](https://docs.cloud.google.com/looker/docs/bi-connectors)** : Data connectors to Excel, Power BI, and Tableau. | **Yes** | **Yes** | **Yes** | For the Power BI or Tableau connectors for Looker (Google Cloud core) instances that use private connections and for customer-hosted Looker (original) instances, your network administrator must configure your network so that traffic from Power BI or Tableau can reach your Looker instance.  
[Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub) and [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) | **Yes** | **Yes** | **Yes** |  This feature may have limitations for Looker (Google Cloud core) instances that use private connections. Additional configuration may also be necessary for Looker (Google Cloud core) instances that use private connections. Additional configuration may be necessary for customer-hosted Looker (original) instances.  
[Schedule data to S3, SFTP, and webhook](https://docs.cloud.google.com/looker/docs/scheduling) | **Yes** | **Yes** | **Yes** | This feature may have limitations for Looker (Google Cloud core) instances that use private connections. Additional configuration may also be necessary for Looker (Google Cloud core) instances that use private connections.  
[Looker extension for VS Code](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension): Local LookML development in VS Code-based IDEs. | **Yes** | **Yes** | **Yes** | Supports syntax highlighting, autocomplete, real-time file synchronization, and LookML validation. Currently in [preview](https://cloud.google.com/products#product-launch-stages).  
[Looker mobile application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) | **Yes** | **Yes** | **Yes** |   
[Custom themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) | **Yes** | **Yes** | **Yes** | Custom themes are available only for **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
[Custom extensions](https://docs.cloud.google.com/looker/docs/extension-overview) | **Yes** | **Yes** | **Yes** | Custom extensions are available only for **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
[Knowledge Catalog integration](https://docs.cloud.google.com/looker/docs/looker-core-dataplex): Automatically ingest Looker metadata into Knowledge Catalog for discovery | No | **Yes** | No |   
[Knowledge Catalog data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage): Trace data flow from BigQuery to Looker dashboards | No | **Yes** | No | Supported only for BigQuery data sources.  
[Private embedding](https://docs.cloud.google.com/looker/docs/private-embedding) | **Yes** | **Yes** | **Yes** |  Private embedding is available for all editions of Looker (Google Cloud core).  
[Signed embedding](https://docs.cloud.google.com/looker/docs/signed-embedding) | **Yes** | **Yes** | **Yes** |  Signed embedding is available only for the **Embed** edition of Looker (Google Cloud core).  
[Preview features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) | **Yes** | **Yes** | **Yes** | Looker preview features are enabled on Looker (Google Cloud core). However, preview features that are categorized as [Labs features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#labs-features) are not available in Looker (Google Cloud core).  
[Legacy features](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) | **Yes** | No | **Yes** |   
**Security and authentication features** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Security features: [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections), [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek), [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) | No | **Yes** | No | Private connections and VPC Service Controls are available only for **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
[IAM integration](https://docs.cloud.google.com/looker/docs/looker-core-access-control) | No | **Yes** | No |   
[Workforce Identity Federation](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity) | No | **Yes** | No | Workforce Identity Federation is in [preview](https://cloud.google.com/products#product-launch-stages).During the preview, only Looker (Google Cloud core) instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) are supported.  
[SAML authentication, OpenID authentication](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-pages) | **Yes** | **Yes** | **Yes** |   
[Username and password setting for login, LDAP authentication](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-password) | **Yes** | No | **Yes** |   
[**IP Allowlist** setting](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) | **Yes** | **Yes** | No |   
[Ability to sudo as another user](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_users) | **Yes** | No | **Yes** | For the **Embed** edition of Looker (Google Cloud core), impersonation of embed users is available by using the API endpoint [`Login user`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/login_user).  
[FIPS encryption](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode) | No | **Yes** | **Yes** | FIPS encryption is available only in the **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
Compliance certifications (for example, FedRAMP High and other [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/release-notes) products) | No | **Yes** | **Yes** | Compliance certifications are available only in the **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
**LookML development and database connections** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Dialect support | **Yes** | **Yes** | **Yes** | The documentation lists the dialects that are [supported by Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) and the dialects that are [supported by Looker (original) and customer-hosted Looker (original)](https://docs.cloud.google.com/looker/docs/dialects).  
[Customer-hosted Git on the public internet](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) | **Yes** | **Yes** | **Yes** | This feature may have limitations for Looker (Google Cloud core) instances that use private connections. Additional configuration may also be necessary for Looker (Google Cloud core) instances that use private connections.  
[Looker Continuous Integration](https://docs.cloud.google.com/looker/docs/continuous-integration) | **Yes** | **Yes** | No | For Looker (Google Cloud core) instances with private or hybrid connections, available only on instances that use [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc). Also supported on instances that are enabled for CMEK or within a [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) perimeter.  
[Service agent access to BigQuery](https://docs.cloud.google.com/looker/docs/looker-core-dialects#adc-with-bigquery) | No | **Yes** | No |   
[SQL Runner visualizations](https://docs.cloud.google.com/looker/docs/sql-runner-basics#sql_runner_visualizations): Create visualizations directly in SQL Runner. | **Yes** | No | **Yes** | [SQL Runner Vis](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#sql_runner_vis) is a Labs feature and is not available in Looker (Google Cloud core).  
[SSH tunnels (for on-premises databases)](https://docs.cloud.google.com/looker/docs/using-an-ssh-tunnel) | **Yes** | n/a | **Yes** |   
**Logging** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Access to internal database and verbose logs  | No (see note) | No | **Yes** | For Looker-hosted Looker (original) instances, internal database and verbose logs are available only through a Google Cloud support request.  
[Cloud Audit Logs](https://docs.cloud.google.com/looker/docs/looker-core-audit-logging) | No | **Yes** | No |   
[Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) | **Yes** | **Yes** | No |  Elite System Activity is available only as a paid feature in the Elite version of Looker (original). Elite Style Activity is available only in the **Enterprise** and **Embed** editions of Looker (Google Cloud core).  
**Infrastructure and instance management** | **Looker (original)** | **Looker (Google Cloud core)** | **Customer-hosted Looker (original)** | **Notes**  
Fully Google Cloud-managed Google service | No | **Yes** | No | Google Cloud support has a much greater ability to troubleshoot issues with the Looker (Google Cloud core) environment, because it is managed on Google Cloud.  
[Self-service instance creation](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) | No | **Yes** | No |   
[Terraform support](https://docs.cloud.google.com/looker/docs/looker-core-overview#use_terraform) | No | **Yes** | No |   
[Startup options](https://docs.cloud.google.com/looker/docs/startup-options) | **Yes** | No | **Yes** |   
[Customer-defined maintenance windows](https://docs.cloud.google.com/looker/docs/looker-core-maintenance) | No | **Yes** | No |   
[Non-production instances](https://docs.cloud.google.com/looker/docs/looker-core-overview#non-production_instances) | **Yes** | **Yes** | **Yes** |  Two non-production instances are available for the Elite version of Looker (original). No other Looker (original) versions offer non-production instances. Non-production instances are purchased separately for Looker (Google Cloud core).  
[Export](https://docs.cloud.google.com/looker/docs/admin-panel-export) | **Yes** | No | No |  This feature is required to migrate from Looker (original) to Looker (Google Cloud core).  
[Release channels](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) | No | **Yes** | No | This feature is in [preview](https://cloud.google.com/products#product-launch-stages). Looker (original) doesn't have defined release channels, but does have an [extended support release (ESR) program](https://docs.cloud.google.com/looker/docs/standard-extended-support-release-program-overview) in addition to its standard release program.
