---
url: https://docs.cloud.google.com/looker/docs/choosing-hosting-option/
title: Choosing a hosting option for a Looker (original) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:51.176319+00:00
---

# Choosing a hosting option for a Looker (original) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/choosing-hosting-option/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Choosing a hosting option for a Looker (original) instance Stay organized with collections  Save and categorize content based on your preferences. 

You have the option to host your own Looker (original) instance or deployment, or Looker can host it for you. Throughout our documentation, we refer to instances or deployments that are hosted by Looker as "[Looker-hosted](https://docs.cloud.google.com/looker/docs/glossary#looker-hosted)" and to instances or deployments that are hosted on-premises as "[customer-hosted](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted)" or "self-hosted."

When Looker hosts your deployment, Looker manages all necessary IT functions that are related to the Looker application on your behalf, based on resource utilization and business requirements, greatly reducing the effort required to install, configure, and maintain the Looker application. Conversely, when you host your own deployment, you are responsible for managing many of these processes and functions. A customer-hosted deployment includes the in-product services, meaning the services that are hosted by Looker and accessible through the product, specifically licensing data, configuration backups, system error reports, data actions, and support tickets, as further described in the **Application Data Shared by Looker** section of [Looker's security page.](https://looker.com/product/security)

**Note:** A customer-hosted option is offered only for Looker (original) instances. This option is not available for Looker (Google Cloud core) instances.

Choosing between the two hosting options is a trade-off between convenience and control. Opting for Looker-hosted lets you focus on integrating Looker into your business workloads without the demands of infrastructure administration. Conversely, hosting your own Looker deployment gives you complete control over the infrastructure administration, but increases your overhead for the initial launch and ongoing maintenance.

This page presents the following information to assist you in choosing the most appropriate hosting option for your needs:

  * Comparative advantages of each hosting option
  * Benefits and limits of the Looker-hosted option
  * Benefits and limits of the customer-hosted option
  * Sample use cases for customer-hosted deployments



## Comparative advantages of each hosting option

The following table compares the advantages of each hosting option.

**Benefit** |  **Looker-hosted** |  **Customer-hosted**  
---|---|---  
Default access to all Looker features |  **X** |   
No hardware setup or maintenance required |  **X** |   
Automatic software updates and maintenance (monthly or quarterly) |  **X** |   
Scale hardware at no additional cost:

  * Vertical scaling (more CPU)
  * Horizontal scaling (more nodes)

|  **X** |   
Application and host monitoring |  **X** |   
Automatic Looker instance backups |  **X** |   
Backend database migration, if necessary |  **X** |   
Uptime SLA 99.9% (Advanced & Elite) |  **X** |   
S1 Response SLA 1 hour |  **X** |   
Looker Status Dashboard |  **X** |   
Use of the Looker API |  **X** |  **X**  
Multi-instance migrations |  **X** |  **X**  
Direct access to and export of servers and logs |  |  **X**  
  
## Benefits and limits of the Looker-hosted option

The following tables list the benefits and limits of using a Looker-hosted deployment.

### Benefits of Looker-hosted deployments

The following table lists the benefits of using a Looker-hosted deployment.

Active management of Looker instance  |  Leave the performance monitoring to the Looker team and focus on making decisions with actionable data insights from Looker.  
---|---  
Always get the latest features and updates |  You will never have to manually download another update. Your Looker instance is tested, updated, and optimized by Looker.  
Consistent performance |  Looker monitors performance and adjusts capacity as needed. You don't have to decide how many servers you need to support your users.   
Deployment security |  Looker manages your platform infrastructure. Your Looker deployment is discrete, secure, and monitored continuously to keep your data safe.  
Connected services |  Every Looker deployment includes essential connected services that allow you to access more relevant data, increase insights, simplify and scale data modeling, and integrate with third-party systems, all while Looker provides support.  
Secure database connections |  Connect Looker to your database using SSH.  
SAML/LDAP integration |  Looker can integrate with your existing authentication methods.  
Instance status monitoring |  Use the [Looker Status Dashboard](https://docs.cloud.google.com/looker/docs/status-dashboard-help) to get real-time updates about product outages or service disruptions for your instance.  
  
### Limits of Looker-hosted deployments

Before you opt to use a Looker-hosted deployment, consider the limits that are listed in the following table.

Specific security/compliance requirements |  The Looker-hosted environment infrastructure may not align with your company's individual security/compliance requirements.   
---|---  
Requirement to have ability to export logs/monitoring information |  Because Looker manages the infrastructure for your instance, you cannot export logs for your instance's usage. Looker manages all monitoring. **Note:** Although logs from Looker-hosted instances cannot be exported, you can access the same information in a System Activity report.   
Custom SLAs |  Looker updates and maintenance take place during the pre-defined [maintenance windows](https://docs.cloud.google.com/looker/docs/google-maintenance-policy-for-looker-hosted-services). Some customers may require additional control over when this maintenance occurs.  
Custom JDBC Drivers |  Custom [JDBC drivers](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers) must be installed to connect to databases that have [lower levels of support](https://docs.cloud.google.com/looker/docs/dialects).  
Visibility into underlying hosting infrastructure details |  Because Looker (original) is a fully managed environment, the underlying hosting infrastructure (such as the Google Cloud project or AWS environment) is managed internally by Google and details are not exposed to customers. There is no self-service admin configuration panel in the Looker UI, nor is there visibility into these details from customer-owned cloud consoles.  **Note:** If you require details about your instance's hosting environment, [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).   
  
## Benefits and limits of the customer-hosted option

The following tables list the benefits and limits to using a customer-hosted deployment.

### Benefits of customer-hosted deployments

The following table lists the benefits of using a customer-hosted deployment.

Direct control over infrastructure and scaling decisions |  You are able to implement infrastructure and architecture configurations that may not be offered with a Looker-hosted deployment.  
---|---  
Access to logging/monitoring |  By managing your own infrastructure, you can directly access and export Looker application logs and set up instance monitoring that suits your individual requirements.   
Bespoke security model |  Hosting Looker in your own deployment allows you complete control over the security of the application environment, which you can align to your company/industry specific security standards.   
  
### Limits of customer-hosted deployments

Before you opt to use a customer-hosted deployment, consider the limits that are listed in the following table.

Support limitations |  Troubleshooting issues can be challenging when the Looker support team is unfamiliar with custom deployment architecture. Certain issues may require more involvement from your organization.  
---|---  
Monthly update requirements |  You are responsible for creating and maintaining processes that ensure that users are getting the latest features and security patches from Looker.  
Human capital requirements |  Looker deployments can require significant headcount and site reliability engineering expertise. Your organization must [manage the various components](https://docs.cloud.google.com/looker/docs/best-practices/customer-hosted-component-walkthroughs) of a Looker deployment.  
Cost |  Your organization must manage time, human capital, and cloud/datacenter costs.  
Challenges using connected services |  Looker has the benefit of connected services, which allow you to to access relevant industry data, increase insights, simplify and scale data modeling, and integrate with third-party systems. In a self-hosted Looker deployment, you may need to deploy ancillary services in your cloud to access these features.  
Disaster recovery and elasticity |  You will be responsible for maintaining uptime and service resilience.  
Some Looker features are not available |  See the Support for Looker features across hosting options section of this page for a comparison of feature support across Looker's hosting options.  
Additional feature configuration |  Customer-hosted instances may require [additional configuration](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps) to use certain Looker features.  
  
## Sample use cases for customer-hosted deployments

A customer-hosted option may be right for your deployment if it aligns with any of the following use cases:

  * Your organization has bespoke security requirements: Some organizations' security policies mandate that they cannot use cloud services. Looker (original) is designed to be multi-cloud, and Looker-hosted Looker (original) deployments reside on various Cloud providers such as Google Cloud, AWS, and Azure. If your security policy is incompatible with using Cloud services with your data, customer-hosting is designed to be the alternative.
  * Your organization prefers a fully customizable deployment model: When Looker hosts your environments, Looker assumes that these environments are intended to be stable. Your organization's requirements may not be compatible with this assumption, such as in the following situations: 
    * Your deployment landscape is a large expanse of numerous instances for each of your user groups or customers, which may only be required for an ephemeral period.
    * Your organization requires the ability to frequently build new environments or tear down existing environments.
    * Your organization requires multiple Looker instances, each requiring custom configurations for the startup flags, model, or connection information.
  * Your organization requires more direct access to integration and configuration capabilities: In a Looker-hosted environment, your direct access to your deployment is limited. Customer-hosted deployments allow for full access to the file system, metadata database, and JVM configurations of your instance. Direct access may be beneficial in the following situations: 
    * Your LookML models and configurations for each instance are frequently updated by using scripts that are synchronized with your development process.
    * Your organization is unable to use certain core technologies that Looker uses to deploy, such as Git. With full control of your instance's backend, you can substitute any core component of Looker with your preferred solution.



## Support for Looker features across hosting options

The following table compares feature support for Looker-hosted Looker (original), [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview), and customer-hosted Looker (original) instance types.

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
