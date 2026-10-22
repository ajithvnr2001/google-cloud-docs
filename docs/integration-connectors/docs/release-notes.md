---
url: https://docs.cloud.google.com/integration-connectors/docs/release-notes/
title: Integration Connectors release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:32:03.068466+00:00
---

# Integration Connectors release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Resources ](https://docs.cloud.google.com/integration-connectors/docs/resources)



Send feedback 

#  Integration Connectors release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Integration Connectors. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/integration-connectors-release-notes.xml) directly. 

## September 04, 2026

Security

A Missing Authorization vulnerability was discovered in the HTTP Connector in Integration Connectors versions prior to December 11, 2025. An authenticated attacker could use an unauthorized service account attachment to escalate privileges and take over a Google Cloud project. For more information, see the [GCP-2026-058](https://docs.cloud.google.com/bigquery/docs/security-bulletins#gcp-2026-058) security bulletin.

## December 16, 2025

Feature

**MCP connector is now available in[preview](https://cloud.google.com/products#product-launch-stages)**

Integration Connectors support the Model Context Protocol (MCP) connector. You can use this connector to [create and configure connections](https://docs.cloud.google.com/integration-connectors/docs/connectors/mcp/configure-mcp) for secure data exchange and operations in your business applications. Within Application Integration, you can use MCP through a [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

## October 30, 2025

Feature

**Apigee API hub connector is now available in[preview](https://cloud.google.com/products#product-launch-stages)**

Integration Connectors now support the [Apigee API hub](https://docs.cloud.google.com/integration-connectors/docs/connectors/apigee_api_hub/configure) connector. You can use this connector to discover, manage, and govern your APIs in Apigee API hub.

## September 29, 2025

Feature

**HL7 Connectors now support new actions**

The HL7 connector now supports the following new transformation actions:

  * [Transform HL7 to XML action](https://cloud.google.com/integration-connectors/docs/connectors/hl7/configure#transformHl7ToXml): This action converts a standard HL7 message into an XML representation.
  * [Transform XML to HL7 action](https://cloud.google.com/integration-connectors/docs/connectors/hl7/configure#transformXmlToHl7): This action converts an XML message back into the HL7 format.



## September 16, 2025

Change

**Salesforce connected app requires installation for OAuth 2.0 authentication**

A new security requirement from Salesforce restricts the use of uninstalled connected apps. To ensure your connections remain functional, all users must install [connected app](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create.htm&type=5) in your Salesforce account.

When establishing a new Salesforce connection using OAuth 2.0 authentication, you are now required to install the connected app in your Salesforce account. This step is also necessary for existing connections using OAuth 2.0 authentication if the connected app is not already installed, as failure to do so may cause them to stop working.

For more information, see [Install the OAuth connected app](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure#post-setup).

## June 30, 2025

Announcement

The [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/integration-connectors/docs/cmek) feature is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## June 24, 2025

Announcement

You can use the following connectors that are now available in Google Cloud Marketplace to create connections and use them in Application Integration.

  * Ajman Open Data Portal
  * Bahrain Open Data Portal
  * Exchange Rate API
  * Hugging Face
  * IP Geolocation Api
  * KAPSARC Data Portal
  * KSA Open Data Platform
  * Morocco Open Data Portal
  * Qatar Open Data Portal
  * Qatar National Address Service (QNAS)
  * Rest Countries
  * Saudi Health Council
  * Serp API
  * Swedavia
  * WHO Global Health Observatory



## June 12, 2025

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Azure DevOps](https://docs.cloud.google.com/integration-connectors/docs/connectors/azuredevops/configure)
  * [HDFS](https://docs.cloud.google.com/integration-connectors/docs/connectors/hdfs/configure)
  * [Jira Server (Data Center) ](https://cloud.google.com/integration-connectors/docs/connectors/jiraserverdc/configure). This connector also supports [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription), which you can leverage in your integrations by using the [Jira Server (Data Center) trigger](https://docs.cloud.google.com/application-integration/docs/configure-jiraserverdc-trigger). This trigger is available in [preview](https://cloud.google.com/products#product-launch-stages). 



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## May 08, 2025

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Bigtable](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigtable/configure)
  * [Dynamics 365 Business Central](https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamics365bc/configure)
  * [Marketo](https://docs.cloud.google.com/integration-connectors/docs/connectors/marketo/configure)
  * [SAP Hybris C4C](https://docs.cloud.google.com/integration-connectors/docs/connectors/saphybrisc4c/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## May 05, 2025

Announcement

The ZATCA connector is now available in Google Cloud Marketplace. You can use this connector to create connections and use them in Application Integration.

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [LinkedIn](https://docs.cloud.google.com/integration-connectors/docs/connectors/linkedin/configure)
  * [Okta](https://docs.cloud.google.com/integration-connectors/docs/connectors/okta/configure)
  * [Oracle Sales Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/oraclesalescloud/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## April 07, 2025

Feature

You can now use a Google-managed OAuth client instead of creating your own client for the following connectors, which are in [preview](https://cloud.google.com/products#product-launch-stages): 

  * [Gmail](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_gmail/configure)
  * [Google Docs](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_docs/configure)
  * [Google Drive](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/configure)
  * [Google Forms](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_forms/configure)
  * [Google Sheets](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_google_sheets/configure)



## March 10, 2025

Feature

The [Microsoft Exchange](https://docs.cloud.google.com/integration-connectors/docs/connectors/exchange/configure) connector is now [GA](https://cloud.google.com/products#product-launch-stages).

To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## February 21, 2025

Feature

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Airtable](https://docs.cloud.google.com/integration-connectors/docs/connectors/airtable/configure)
  * [Oracle Eloqua](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracleeloqua/configure)
  * [Sage Intacct](https://docs.cloud.google.com/integration-connectors/docs/connectors/sageintacct/configure)
  * [SAP HANA XS Advanced](https://docs.cloud.google.com/integration-connectors/docs/connectors/saphanaxsa/configure)



## February 05, 2025

Feature

The [Azure AD connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/azuread/configure) now supports [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) which you can leverage in your integrations by using the [Azure AD trigger](https://docs.cloud.google.com/application-integration/docs/configure-azuread-trigger). This trigger is available in [preview](https://cloud.google.com/products#product-launch-stages).

## January 06, 2025

Feature

Integration Connectors now supports [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/integration-connectors/docs/cmek). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

Feature

The [HL7 connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/hl7/configure) is now available in [preview](https://cloud.google.com/products#product-launch-stages). The connector also supports [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription), which you can leverage in your integrations by using the [HL7 trigger](https://docs.cloud.google.com/application-integration/docs/configure-hl7-trigger).

## December 19, 2024

Feature

You can now [build and publish custom connectors for Google Cloud Marketplace](https://docs.cloud.google.com/integration-connectors/docs/marketplace/marketplace-connector-overview). This feature is in [preview](https://cloud.google.com/products#product-launch-stages). 

The following connectors built by partners are available in Google Cloud Marketplace. You can use these connectors to create connections and use them in Application Integration.

  * Exact HR
  * Openlegacy IBMi/AS/400 API
  * Salesforce Commerce Cloud B2B



## November 27, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Monday.com](https://docs.cloud.google.com/integration-connectors/docs/connectors/monday/configure)
  * [PayPal](https://docs.cloud.google.com/integration-connectors/docs/connectors/paypal/configure)
  * [Slack](https://cloud.google.com/integration-connectors/docs/connectors/slack/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## November 18, 2024

Feature

The [BigQuery connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure) now supports the Array data type.

## October 18, 2024

Change

The private network connectivity documentation has been restructured to include information about the following networking patterns:

  * [Public network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-public)
  * [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private)
  * [Network connectivity in Google Cloud VPC](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-gc-vpc)
  * [Private connectivity for on-premise or other cloud providers](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-on-premise)
  * [Network connectivity in Google Cloud managed services](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services)
  * [Connectivity to services hosted in serverless environment](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-serverless)



## October 03, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Asana](https://docs.cloud.google.com/integration-connectors/docs/connectors/asana/configure)
  * [WordPress](https://docs.cloud.google.com/integration-connectors/docs/connectors/wordpress/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## September 20, 2024

Announcement

The [Microsoft Teams](https://docs.cloud.google.com/integration-connectors/docs/connectors/msteams/configure) connector is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## September 19, 2024

Announcement

The [OneDrive](https://docs.cloud.google.com/integration-connectors/docs/connectors/onedrive/configure) connector is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

Feature

The [BigQuery connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure) now supports [OAuth 2.0 - Authorization code](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure#configure-auth).

Change

Connection names cannot exceed 49 characters. Previously, connection names had a limit of 63 characters.

## September 11, 2024

Feature

**Connectors for Google services**

When you use OAuth 2.0 - Authorization code authentication in Google services connectors, you can select the applicable scopes from the drop-down. Previously, you had to enter comma separated values for OAuth 2.0 scopes.

**HTTP connector**

Use the **Status Check** field to check the status of an [HTTP connection](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure) by specifying an endpoint URL, which can include an endpoint attachment IP address.

## September 10, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Confluence](https://docs.cloud.google.com/integration-connectors/docs/connectors/confluence/configure)
  * [Dataverse](https://docs.cloud.google.com/integration-connectors/docs/connectors/dataverse/configure)
  * [DocuSign](https://docs.cloud.google.com/integration-connectors/docs/connectors/docusign/configure)
  * [Excel Online](https://docs.cloud.google.com/integration-connectors/docs/connectors/excelonline/configure)
  * [GitHub](https://docs.cloud.google.com/integration-connectors/docs/connectors/github/configure)
  * [IBM Db2](https://docs.cloud.google.com/integration-connectors/docs/connectors/db2/configure)
  * [Jira Service Management](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiraservicemanagement/configure)
  * [SAP Business One](https://docs.cloud.google.com/integration-connectors/docs/connectors/sapbusinessone/configure)
  * [UKG](https://docs.cloud.google.com/integration-connectors/docs/connectors/ukg/configure)
  * [WooCommerce](https://docs.cloud.google.com/integration-connectors/docs/connectors/woocommerce/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## September 02, 2024

Announcement

The [Neo4j](https://docs.cloud.google.com/integration-connectors/docs/connectors/neo4j/configure) connector is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## August 29, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Active Directory](https://docs.cloud.google.com/integration-connectors/docs/connectors/activedirectory/configure)
  * [QuickBooks Online](https://docs.cloud.google.com/integration-connectors/docs/connectors/quickbooksonline/configure)



## August 28, 2024

Feature

The [TIBCO EMS connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/tibcoems/configure) is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The connector also supports [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription), which you can leverage in your integrations by using the [TIBCO EMS trigger](https://docs.cloud.google.com/application-integration/docs/configure-tibcoems-trigger).

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Azure AD](https://docs.cloud.google.com/integration-connectors/docs/connectors/azuread/configure)
  * [Azure Synapse](https://docs.cloud.google.com/integration-connectors/docs/connectors/azuresynapse/configure)
  * [Dropbox](https://docs.cloud.google.com/integration-connectors/docs/connectors/dropbox/configure)
  * [Instagram](https://docs.cloud.google.com/integration-connectors/docs/connectors/instagram/configure)
  * [SAP ASE (Sybase)](https://docs.cloud.google.com/integration-connectors/docs/connectors/sybase/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## August 19, 2024

Feature

You can configure a connector to collect logs for the following severity levels:

  * Error
  * Info
  * Debug



For more information, see [View Integration Connectors logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).

## July 22, 2024

Feature

The [Solace connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/solace/configure) is now available in [preview](https://cloud.google.com/products#product-launch-stages). The connector also supports [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription), which you can leverage in your integrations by using the [Solace trigger](https://docs.cloud.google.com/application-integration/docs/configure-solace-trigger).

## July 15, 2024

Feature

You can now share custom connectors between different Google Cloud projects by [exporting and importing the connector specification](https://docs.cloud.google.com/integration-connectors/docs/manage-custom-connector-versions#export-import). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## July 11, 2024

Feature

The following connectors support [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription):

  * [SAP ERP](https://docs.cloud.google.com/integration-connectors/docs/connectors/saperp/configure)
  * [SAP Gateway](https://docs.cloud.google.com/integration-connectors/docs/connectors/sapgateway/configure)



You can use the eventing feature in Application Integration through the [SAP ERP trigger](https://docs.cloud.google.com/application-integration/docs/configure-sap-erp-trigger) and [SAP Gateway trigger](https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger) respectively.

## July 09, 2024

Announcement

Integration Connectors is now available in the following additional regions:

  * Berlin (`europe-west10`)
  * Turin (`europe-west12`)



For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

Feature

The [Jira Cloud connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure) now supports [OAuth 2.0 - Authorization code](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure#exp2).

## July 07, 2024

Announcement

The [Google Workspace Admin SDK](http://cloud.google.com/integration-connectors/docs/connectors/gsc_admin_sdk/configure) connector is available in [preview](https://cloud.google.com/products#product-launch-stages).

## July 03, 2024

Announcement

The connection pooling parameters of the [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure) connector are optimized for performance.

## June 27, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Greenplum](https://docs.cloud.google.com/integration-connectors/docs/connectors/greenplum/configure)
  * [MetaAds](https://docs.cloud.google.com/integration-connectors/docs/connectors/metaads/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

Announcement

**Connectors for Google services**

The following new connectors are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [Cloud Search](http://cloud.google.com/integration-connectors/docs/connectors/gsc_cloud_search/configure)
  * [Google Dialogflow](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_dialog_flow/configure)
  * [Google Safe Browsing](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_safe_browsing/configure)
  * [Google Sheets](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_sheets/configure)
  * [Google Slides](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_slides/configure)
  * [Identity and Access Management](http://cloud.google.com/integration-connectors/docs/connectors/gsc_identity_access_management/configure)
  * [Youtube](http://cloud.google.com/integration-connectors/docs/connectors/gsc_youtube/configure)



## May 29, 2024

Feature

Custom connectors now support the following additional features:

  * [Edit connector](https://docs.cloud.google.com/integration-connectors/docs/edit-custom-connector)
  * [Versions](https://docs.cloud.google.com/integration-connectors/docs/manage-custom-connector-versions)
  * [Logo](https://docs.cloud.google.com/integration-connectors/docs/create-custom-connector#create-a-custom-connector-with-direct-connectivity)
  * [File upload for OpenAPI specification](https://docs.cloud.google.com/integration-connectors/docs/create-custom-connector#create-a-custom-connector-with-direct-connectivity)



## May 24, 2024

Feature

The [TIBCO EMS connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/tibcoems/configure) is available in preview. The connector also supports [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription), which you can leverage in your integrations by using the [TIBCO EMS trigger](https://docs.cloud.google.com/application-integration/docs/configure-tibcoems-trigger).

## May 21, 2024

Announcement

Integration Connectors is now available in Milan (`europe-west8`). For a list of supported regions, see [Integration Connectors locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

## May 20, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Apache Cassandra](https://docs.cloud.google.com/integration-connectors/docs/connectors/apachecassandra/configure)
  * [Apache CouchDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/apachecouchdb/configure)
  * [Kintone](https://docs.cloud.google.com/integration-connectors/docs/connectors/kintone/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## April 23, 2024

Announcement

The following connector versions are deprecated as on 20 April, 2024:

  * MongoDB (version 1)
  * Oracle DB (version 1)



Instead, use [MongoDB V2](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure) and [Oracle DB V2](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure) connectors.

## April 15, 2024

Announcement

The [HTTP connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure) now supports the following additional authentication types:

  * Service account
  * Service account ID token authentication
  * API key authentication



Feature

The [Commercetools connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/commercetools/configure) is available for [preview](https://cloud.google.com/products#product-launch-stages).

## April 01, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [CockroachDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/cockroachdb/configure)
  * [Email](https://docs.cloud.google.com/integration-connectors/docs/connectors/email/configure)
  * [MailChimp](https://docs.cloud.google.com/integration-connectors/docs/connectors/mailchimp/configure)
  * [Office365](https://docs.cloud.google.com/integration-connectors/docs/connectors/office365/configure)
  * [SingleStore](https://docs.cloud.google.com/integration-connectors/docs/connectors/singlestore/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

Feature

Integration Connectors is now available in the following additional regions:

  * Delhi (`asia-south2`)
  * Warsaw (`europe-central2`)
  * Toronto (`northamerica-northeast2`)
  * Columbus (`us-east5`)
  * Las Vegas (`us-west4`)
  * Dallas (`us-south1`)
  * Santiago (`southamerica-west1`)



For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

## March 15, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Stripe](https://docs.cloud.google.com/integration-connectors/docs/connectors/stripe/configure)
  * [Teradata](https://docs.cloud.google.com/integration-connectors/docs/connectors/teradata/configure)
  * [Trello](https://docs.cloud.google.com/integration-connectors/docs/connectors/trello/configure)



Feature

**Connectors for Google services**

The following new connectors are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [Gmail](http://cloud.google.com/integration-connectors/docs/connectors/gsc_gmail/configure)
  * [Google Classroom](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_classroom/configure)
  * [Google Contacts](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_contacts/configure)
  * [Google Calendar](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_calendar/configure)
  * [Google Enterprise License Manager](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_enterprise_license_manager/configure)
  * [Search Ads 360](http://cloud.google.com/integration-connectors/docs/connectors/gsc_search_ads_360/configure)
  * [Youtube Analytics](http://cloud.google.com/integration-connectors/docs/connectors/gsc_youtube_analytics/configure)
  * [Youtube Reporting](http://cloud.google.com/integration-connectors/docs/connectors/gsc_youtube_reporting/configure)



Feature

**SAP Secured Network Communications (SNC)**

The [SAP ERP](https://docs.cloud.google.com/integration-connectors/docs/connectors/saperp/configure#configure-the-connector) connector now supports authentication through SAP SNC.

## March 03, 2024

Announcement

The [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) feature is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

You can now configure dead-letter in the following connectors:

  * [IBM MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure)
  * [Jira Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure)
  * [Rabbit MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/rabbitmq/configure)
  * [Webhook](https://docs.cloud.google.com/integration-connectors/docs/connectors/webhook/configure)
  * [Zendesk](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure)



If you configure dead-letter, the connection writes the unprocessed events to your specified [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/overview).

## February 19, 2024

Deprecated

The following connector versions will be deprecated on 20 April, 2024:

  * [MongoDB (version 1)](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/v1/configure)
  * [Oracle DB (version 1)](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/v1/configure)



The support for these connectors will end on 20 April, 2024. It's recommended you start using the **version 2** of these connectors.

## February 12, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Acumatica](https://docs.cloud.google.com/integration-connectors/docs/connectors/acumatica/configure)
  * [Azure Data Lake](https://docs.cloud.google.com/integration-connectors/docs/connectors/azuredatalakestorage/configure)
  * [Couchbase](https://docs.cloud.google.com/integration-connectors/docs/connectors/couchbase/configure)
  * [Dynamics 365](https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamics365/configure)
  * [Elasticsearch](https://docs.cloud.google.com/integration-connectors/docs/connectors/elasticsearch/configure)
  * [Netsuite](https://docs.cloud.google.com/integration-connectors/docs/connectors/netsuite/configure)
  * [SAP ERP](https://docs.cloud.google.com/integration-connectors/docs/connectors/saperp/configure)
  * [Splunk](https://docs.cloud.google.com/integration-connectors/docs/connectors/splunk/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## February 04, 2024

Issue

When you delete a custom connector from the [custom connector page](https://console.cloud.google.com/connectors/custom-connectors), the page may not work as intended. For more information, see [Known Issues](https://docs.cloud.google.com/integration-connectors/docs/known-issues).

## January 30, 2024

Feature

**Custom SQL editor**

The custom SQL editor lets you run custom queries across different entities, and is available in the user interface of the following connectors:

  * [BigQuery](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  * [Cloud Spanner](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudspanner/configure)
  * [Cloud SQL for MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlformysql/configure)
  * [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure)
  * [Cloud SQL for SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure)
  * [Couchbase](https://docs.cloud.google.com/integration-connectors/docs/connectors/couchbase/configure)
  * [Elasticsearch](https://docs.cloud.google.com/integration-connectors/docs/connectors/elasticsearch/configure)
  * [MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/mysql/configure)
  * [Oracle DB (Version 2)](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/v2/configure)
  * [PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)
  * [Salesforce](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)
  * [Snowflake](https://docs.cloud.google.com/integration-connectors/docs/connectors/snowflake/configure)
  * [SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/sqlserver/configure)
  * [Teradata](https://docs.cloud.google.com/integration-connectors/docs/connectors/teradata/configure)



For more information, see [Execute custom SQL query](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure#execute-custom-query).

## January 29, 2024

Feature

**HTTP connector supports OAuth 2.0 - Authorization code**

The [HTTP connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure) now supports the [OAuth 2.0 - Authorization code](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1) authentication type.

## January 24, 2024

Feature

**Custom connectors [Preview]**

The custom connectors feature (based on the Open API specification) lets you create your own connectors that aren't a part of the standard connectors provided by Integration Connectors, and then use such connectors in your [integrations](https://docs.cloud.google.com/application-integration/docs/overview). For more information, see [Custom connectors](https://docs.cloud.google.com/integration-connectors/docs/custom-connectors).

Feature

**Connectors for Google services**

The following new connectors are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [Cloud Natural Language](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_natural_language/configure)
  * [Firestore](http://cloud.google.com/integration-connectors/docs/connectors/gsc_firestore/configure)
  * [Google Analytics](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_analytics/configure)
  * [Google Calendar](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_calendar/configure)
  * [Google Data Catalog](http://cloud.google.com/integration-connectors/docs/connectors/gsc_gcp_datacatalog/configure)
  * [Google Docs](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_docs/configure)
  * [Google Drive](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_drive/configure)
  * [Google Forms](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_forms/configure)
  * [Google Tasks](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_tasks/configure)
  * [Google Translate](http://cloud.google.com/integration-connectors/docs/connectors/gsc_google_translate/configure)
  * [Vertex AI](http://cloud.google.com/integration-connectors/docs/connectors/gsc_vertex_ai/configure)



## January 22, 2024

Announcement

The [VPC Service Controls feature for Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/vpcsc-connectors) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## January 17, 2024

Feature

**Terraform support**

You can now use Terraform to create new connections. For more information, see the individual connector documentation that describes how to use Terraform for creating connections. Also, see the [Connection Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection).

## January 16, 2024

Announcement

The [Webhook connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/webhook/configure) is now available in preview. This connector lets you listen to events from your backend, and is designed to be used with the [Webhook trigger](https://cloud.google.com/application-integration/docs/configure-webhook-trigger) in [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview).

## January 08, 2024

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Amazon S3](https://docs.cloud.google.com/integration-connectors/docs/connectors/amazons3/configure)
  * [FTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/ftp/configure)
  * [Magento](https://docs.cloud.google.com/integration-connectors/docs/connectors/magento/configure)
  * [MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/mysql/configure)
  * [PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)
  * [SAP HANA](https://docs.cloud.google.com/integration-connectors/docs/connectors/saphana/configure)
  * [SendGrid](https://docs.cloud.google.com/integration-connectors/docs/connectors/sendgrid/configure)
  * [SharePoint](https://docs.cloud.google.com/integration-connectors/docs/connectors/sharepoint/configure)
  * [Workday](https://docs.cloud.google.com/integration-connectors/docs/connectors/workday/configure)
  * [Xero](https://docs.cloud.google.com/integration-connectors/docs/connectors/xero/configure)
  * [Zoho Books](https://docs.cloud.google.com/integration-connectors/docs/connectors/zohobooks/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## November 28, 2023

Announcement

Integration Connectors is now available in the following additional regions:

  * Salt Lake City (`us-west3`)
  * Osaka (`asia-northeast2`)
  * Seoul (`asia-northeast3`)
  * Jakarta (`asia-southeast2`)
  * Hong Kong (`asia-east2`)
  * Dammam (`me-central2`)



For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

## November 23, 2023

Feature

[Event subscription](https://docs.cloud.google.com/integration-connectors/docs/connectors/hubspot/configure) support available for the HubSpot connector.

You can leverage the event subscription feature in this connector through the new [HubSpot trigger](https://docs.cloud.google.com/application-integration/docs/configure-hubspot-trigger) available in [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview).

## November 21, 2023

Feature

[Event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) support available for the [IBM MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure) and the [Rabbit MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/rabbitmq/configure) connectors.

You can leverage the event subscription feature in these connectors through the new [IBM MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-ibmmq-trigger) and the [Rabbit MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-rabbitmq-trigger) that are available in the [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview).

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Freshbooks](https://docs.cloud.google.com/integration-connectors/docs/connectors/freshbooks/configure)
  * [Cloud Storage](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudstorage/configure)
  * [HubSpot](https://docs.cloud.google.com/integration-connectors/docs/connectors/hubspot/configure)
  * [IBM MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure)
  * [Oracle DB (Version 2)](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure)
  * [Rabbit MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/rabbitmq/configure)
  * [Zuora](https://docs.cloud.google.com/integration-connectors/docs/connectors/zuora/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## October 19, 2023

Feature

**Static outbound IP address support**

You can now configure static outbound IP address for your connections. By using the static IP addresses in your firewall, you can restrict access to your backend systems, which in turn makes the connectivity more secure. For more information, see [Configure static outbound IP addresses for connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip).

## October 13, 2023

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Box](https://docs.cloud.google.com/integration-connectors/docs/connectors/box/configure)
  * [LDAP](https://docs.cloud.google.com/integration-connectors/docs/connectors/ldap/configure)
  * [Shopify](https://docs.cloud.google.com/integration-connectors/docs/connectors/shopify/configure)
  * [Zendesk](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## October 10, 2023

Feature

**IAM Conditions for fine-grained access**

You can now add IAM Conditions for the following resources:

  * Connection 
  * ManagedZone
  * EndpointAttachment
  * EventSubscription
  * ConnectionSchemaMetadata



For more information, see [IAM Conditions for fine-grained access](https://docs.cloud.google.com/integration-connectors/docs/add-connector-iam-conditions).

## September 12, 2023

Announcement

The following connectors are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  * [Redshift](https://docs.cloud.google.com/integration-connectors/docs/connectors/redshift/configure)
  * [SAP SuccessFactors](https://docs.cloud.google.com/integration-connectors/docs/connectors/sapsuccessfactors/configure)
  * [Twilio](https://docs.cloud.google.com/integration-connectors/docs/connectors/twilio/configure)
  * [BigCommerce](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigcommerce/configure)



To view the list of all the GA connectors, see [Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## September 11, 2023

Feature

Integration Connectors now supports rate limiting for the connection traffic. For more information, see [Apply rate limiting](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting).

## August 29, 2023

Change

Starting with this release, you must specify a protocol (HTTP or HTTPS) when configuring the backend hostname for your [Jira Cloud connection](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure#configure-the-connector). Prior to this release, specifying the protocol was optional, and you might have configured a connection without the protocol for the hostname. Note the following behavior for your existing Jira Cloud connections that don't have the protocol for the hostname:

  * If your backend uses HTTPS, you don't have to make any changes to your Jira Cloud connection, as it will use HTTPS by default.
  * If your backend uses HTTP, you must edit your connection, and add the HTTP protocol for the hostname configuration.



## August 09, 2023

Announcement

The following connectors are now generally available (GA):

  * [AlloyDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/alloydb/configure)
  * [Apache Kafka](https://docs.cloud.google.com/integration-connectors/docs/connectors/apachekafka/configure)
  * [Jira Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure)
  * [MariaDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/mariadb/configure)
  * [SAP Gateway](https://docs.cloud.google.com/integration-connectors/docs/connectors/sapgateway/configure)
  * [Snowflake](https://docs.cloud.google.com/integration-connectors/docs/connectors/snowflake/configure)



To view the list of all the GA connectors, see [Connectors in General Availability](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors#connectors-in-general-availability-ga).

## July 20, 2023

Announcement

MongoDB (version 2), ServiceNow, and Salesforce Marketing Cloud connectors are now generally available. Including these connectors, the following 13 connectors are generally available:

  * [BigQuery](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  * [Cloud SQL for MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlformysql/configure)
  * [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure)
  * [Cloud SQL for SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure)
  * [HTTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure)
  * [MongoDB v2](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/v2/configure)
  * [Pub/Sub](https://docs.cloud.google.com/integration-connectors/docs/connectors/pubsub/configure)
  * [Redis](https://docs.cloud.google.com/integration-connectors/docs/connectors/redis/configure)
  * [Salesforce](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)
  * [Salesforce Marketing Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforcemarketingcloud/configure)
  * [ServiceNow](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure)
  * [SFTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/sftp/configure)
  * [SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/sqlserver/configure)



Announcement

The following connectors are now available in public [preview](https://cloud.google.com/products#product-launch-stages):

  * [AlloyDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/alloydb/configure)
  * [Authorize.Net](https://docs.cloud.google.com/integration-connectors/docs/connectors/authorize.net/configure)
  * [EnterpriseDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/enterprisedb/configure)
  * [FinancialForce](https://docs.cloud.google.com/integration-connectors/docs/connectors/financialforce/configure)



Feature

Integration Connectors now supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for enhanced security. For more information, see [Set up VPC Service Controls for Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs/vpcsc-connectors).

Feature

Support for [event subscriptions](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) from your backend applications. By using event subscriptions, you can trigger your integrations based on the events in your backend applications. For more information, see [Use event subscriptions in your integrations](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription#esi).

**Note** : The event subscription feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

Feature

The topic name input parameter is now optional in the [Publish message action](https://docs.cloud.google.com/integration-connectors/docs/connectors/pubsub/configure#cja) of the Pub/Sub connector. Therefore, by parameterizing the topic name, you can use a single connection to access multiple Pub/Sub topics.

## July 01, 2023

Announcement

Starting July 1, 2023, you will be billed for usage of a [generally available](https://cloud.google.com/products#product-launch-stages) connector version as per the prices mentioned in the [pricing page](https://docs.cloud.google.com/integration-connectors/docs/pricing). To know when a connector version has moved from preview to general availability, you can use of the following approaches:

  * Subscribe to the [Integration Connector release notifications](https://docs.cloud.google.com/integration-connectors/docs/release-notes).
  * Regularly check for the presence of the **Preview** label next to the connector name in the [List connections page](https://console.cloud.google.com/connectors/connections). If a connector doesn't have the **Preview** label, it means that the connector is generally available.



To view the list of all the generally available connectors, see [Integration Connectors in GA](https://docs.cloud.google.com/integration-connectors/docs/release-notes#June_13_2023).

**Note** : You aren't billed for using connectors that are in [preview](https://cloud.google.com/products#product-launch-stages).

## June 13, 2023

Announcement

Integration Connectors is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages), and the billing cycle will start from July 1, 2023, onwards.

Integration Connectors let you connect to various data sources from your [integrations](https://docs.cloud.google.com/application-integration/docs/overview). With these connectors, you can access both Google Cloud services and other business applications seamlessly. For the list of all the available connectors, see [all Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors).

**Note** : Some of the connectors are available only in preview mode.

Announcement

Cloud SQL for SQL Server, HTTP, Redis, SFTP, and SQL Server connectors are now generally available. Including these connectors, the following 10 connectors are generally available:

  * [BigQuery](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  * [Cloud SQL for MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlformysql/configure)
  * [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure)
  * [Cloud SQL for SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure)
  * [HTTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure)
  * [Pub/Sub](https://docs.cloud.google.com/integration-connectors/docs/connectors/pubsub/configure)
  * [Redis](https://docs.cloud.google.com/integration-connectors/docs/connectors/redis/configure)
  * [Salesforce](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)
  * [SFTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/sftp/configure)
  * [SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/sqlserver/configure)



Feature

Support for proxy server configuration in the [SQL Server connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/sqlserver/configure).

## June 01, 2023

Announcement

Integration Connectors is now available in the following additional regions:

  * Doha (`me-central1`)
  * Tel Aviv (`me-west1`)



For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

## May 29, 2023

Feature

Support for proxy configuration in the following connectors:

  * [Apache CouchDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/apachecouchdb/configure)
  * [BigCommerce](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigcommerce/configure)
  * [BigQuery](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  * [Box](https://docs.cloud.google.com/integration-connectors/docs/connectors/box/configure)
  * [Couchbase](https://docs.cloud.google.com/integration-connectors/docs/connectors/couchbase/configure)
  * [Dynamics NAV](https://docs.cloud.google.com/integration-connectors/docs/connectors/dynamicsnav/configure)
  * [Elasticsearch](https://docs.cloud.google.com/integration-connectors/docs/connectors/elasticsearch/configure)
  * [Email](https://docs.cloud.google.com/integration-connectors/docs/connectors/email/configure)
  * [HTTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure)
  * [HubSpot](https://docs.cloud.google.com/integration-connectors/docs/connectors/hubspot/configure)
  * [Jira Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure)
  * [Kintone](https://docs.cloud.google.com/integration-connectors/docs/connectors/kintone/configure)
  * [Magento](https://docs.cloud.google.com/integration-connectors/docs/connectors/magento/configure)
  * [MailChimp](https://docs.cloud.google.com/integration-connectors/docs/connectors/mailchimp/configure)
  * [Neo4J](https://docs.cloud.google.com/integration-connectors/docs/connectors/neo4j/configure)
  * [PayPal](https://docs.cloud.google.com/integration-connectors/docs/connectors/paypal/configure)
  * [PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)
  * [Redshift](https://docs.cloud.google.com/integration-connectors/docs/connectors/redshift/configure)
  * [Salesforce](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)
  * [SAP Netweaver Gateway](https://docs.cloud.google.com/integration-connectors/docs/connectors/sapgateway/configure)
  * [ServiceNow](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure)
  * [Shopify](https://docs.cloud.google.com/integration-connectors/docs/connectors/shopify/configure)
  * [Snowflake](https://docs.cloud.google.com/integration-connectors/docs/connectors/snowflake/configure)
  * [Splunk](https://docs.cloud.google.com/integration-connectors/docs/connectors/splunk/configure)
  * [Streak](https://docs.cloud.google.com/integration-connectors/docs/connectors/streak/configure)
  * [Stripe](https://docs.cloud.google.com/integration-connectors/docs/connectors/stripe/configure)
  * [TaxJar](https://docs.cloud.google.com/integration-connectors/docs/connectors/taxjar/configure)
  * [Trello](https://docs.cloud.google.com/integration-connectors/docs/connectors/trello/configure)
  * [Twilio](https://docs.cloud.google.com/integration-connectors/docs/connectors/twilio/configure)
  * [Workday](https://docs.cloud.google.com/integration-connectors/docs/connectors/workday/configure)
  * [Zendesk](https://docs.cloud.google.com/integration-connectors/docs/connectors/zendesk/configure)



## May 23, 2023

Feature

[MongoDB (Version 2) connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/v2/configure)

This release provides the MongoDB (Version 2) connector that has support for **queryable encryption**.

Feature

Support for **Digest** authentication and **TLS chiper suites** in the [HTTP connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure#chiper-suite).

Feature

Support for **PublishMessage** action in the **Apache Kafka** connector. This action lets you publish messages to a Kafka topic, and also lets you validate your messages against the message schema defined in the schema registry for a topic. For more information, see [PublishMessage action](https://docs.cloud.google.com/integration-connectors/docs/connectors/apachekafka/configure#cja).

## May 15, 2023

Announcement

Integration Connectors are now available in the following additional locations:

  * Melbourne (`australia-southeast2`)
  * Finland (`europe-north1`)



For the list of all the supported locations, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

Announcement

Starting with this release, you can't configure a service attachment as a destination type. Your existing connections that use service attachments will continue to work as before, but they won't be supported from July 01, 2023 onwards. So, it is recommended that you start using [endpoint attachments](https://cloud.google.com/integration-connectors/docs/create-ep-attachment) for private connectivity.

Feature

DNS peering support for TLS termination

This feature enables SSL hostname validation at your backend. Hence, you can now configure your connectors to connect to your private backend services using a hostname. For more information, see [Create an endpoint attachment as a hostname](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment#create-ep-hostname).

Feature

Support for **SignURL** action in the [Cloud Storage connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudstorage/configure#signurl).

## April 12, 2023

Feature

Support for Cloud Logging in Integration Connectors. For more information, see [View connector logs](https://docs.cloud.google.com/integration-connectors/docs/logging).

Feature

Pay-as-you-go customers can now customize the minimum and maximum number of nodes for a connection. A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [Pricing for connection nodes](https://cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes).

Feature

The Box connector now supports **OAuth 2.0 - Authorization code** authentication. For more information, see [Configure authentication](https://docs.cloud.google.com/integration-connectors/docs/connectors/box/configure#configure-auth).

Feature

Atlas support for the MongoDB connector. For information, see [Configuration for the MongoDB Atlas cluster](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure#configuration-for-the-mongodb-atlas-cluster).

Feature

Support for executing stored procedures in connectors. For the list of all the connectors that support the execution of stored procedures, see [Execute a stored procedure](https://docs.cloud.google.com/integration-connectors/docs/examples/execute-stored-proc).

Feature

Support for the following actions in the BigQuery connector:

  * CancelJob
  * GetJob
  * InsertJob
  * InsertLoadJob



For more information, see [BigQuery actions](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure#actions).

Feature

The [Integration Connectors UI](https://console.cloud.google.com/connectors) now has a new **Overview** page that provides the following information:

  * Overview of Integration Connectors 
  * Recent connections
  * Documentation links



The **Overview** page is the default landing page for the Integration Connectors UI.

Feature

Confluent support for the Apache Kafka connector. For more information, see [Configuration for Confluent Cloud](https://docs.cloud.google.com/integration-connectors/docs/connectors/apachekafka/configure#configuration-for-confluent-cloud).

## March 01, 2023

Feature

**New connectors available in preview**

The following new connectors are available in preview:

  * [HTTP](https://docs.cloud.google.com/integration-connectors/docs/connectors/http/configure) (includes SSL support)
  * [RabbitMQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/rabbitmq/configure)



Feature

The [IBM MQ](https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure) connector now supports [requestReply](https://docs.cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure#reqreply) messages.

Feature

The [MongoDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure) connector now supports the following actions:

  * InsertDocument
  * UpdateDocument
  * DeleteDocument
  * GetDocument



Feature

The [Cloud Storage](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudstorage/configure#actions) connector now supports the following actions for file operations:

  * UploadObject
  * DownloadObject
  * MoveObject
  * CopyObject
  * DeleteObject



## January 04, 2023

Feature

**New connectors available in preview**

The following new connectors are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [HubSpot](https://cloud.google.com/integration-connectors/docs/connectors/hubspot/configure)
  * [Magento](https://cloud.google.com/integration-connectors/docs/connectors/magento/configure)
  * [Teradata](https://cloud.google.com/integration-connectors/docs/connectors/teradata/configure)



## December 22, 2022

Feature

**New connectors available in preview**

The following new connectors are available in [preview](https://cloud.google.com/products#product-launch-stages): 

### Connectors for Google services

  * [Cloud Storage](https://cloud.google.com/integration-connectors/docs/connectors/cloudstorage/configure)



### Connectors for other applications

  1. [Box](https://cloud.google.com/integration-connectors/docs/connectors/box/configure)
  2. [Couchbase](https://cloud.google.com/integration-connectors/docs/connectors/couchbase/configure)
  3. [FTP](https://cloud.google.com/integration-connectors/docs/connectors/ftp/configure)
  4. [IBM MQ](https://cloud.google.com/integration-connectors/docs/connectors/ibmmq/configure)
  5. [Kintone](https://cloud.google.com/integration-connectors/docs/connectors/kintone/configure)
  6. [MailChimp](https://cloud.google.com/integration-connectors/docs/connectors/mailchimp/configure)
  7. [Neo4J](https://cloud.google.com/integration-connectors/docs/connectors/neo4j/configure)
  8. [Redshift](https://cloud.google.com/integration-connectors/docs/connectors/redshift/configure)
  9. [SAP HANA](https://cloud.google.com/integration-connectors/docs/connectors/saphana/configure)
  10. [SAP Netweaver Gateway](https://cloud.google.com/integration-connectors/docs/connectors/sapgateway/configure)
  11. [SendGrid](https://cloud.google.com/integration-connectors/docs/connectors/sendgrid/configure)
  12. [Shopify](https://cloud.google.com/integration-connectors/docs/connectors/shopify/configure)
  13. [SingleStore](https://cloud.google.com/integration-connectors/docs/connectors/singlestore/configure)
  14. [Snowflake](https://cloud.google.com/integration-connectors/docs/connectors/snowflake/configure)
  15. [Streak](https://cloud.google.com/integration-connectors/docs/connectors/streak/configure)
  16. [Stripe](https://cloud.google.com/integration-connectors/docs/connectors/stripe/configure)
  17. [TaxJar](https://cloud.google.com/integration-connectors/docs/connectors/taxjar/configure)
  18. [Trello](https://cloud.google.com/integration-connectors/docs/connectors/trello/configure)



## September 28, 2022

Announcement

Integration Connectors are now available in [preview](https://cloud.google.com/products#product-launch-stages). Integration Connectors let you connect to various data sources from your integrations. With connectors, both Google Cloud services and third-party business applications are exposed to your integrations through a transparent, standard interface. As an integration developer, you can quickly connect to a growing pool of applications and systems without the need for protocol-specific knowledge or the use of custom code.

For more information about the Integration Connectors features and functionalities, see [Integration Connectors documentation](https://cloud.google.com/integration-connectors/docs). 

For the complete list of all the available connectors, see [Connector reference](https://cloud.google.com/integration-connectors/docs/connector-reference-overview). 

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. You may not be able to provision Integration Connectors until the rollout is complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
