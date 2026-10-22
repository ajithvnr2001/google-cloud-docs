---
url: https://docs.cloud.google.com/apigee/docs/api-platform/release-notes/
title: Apigee UI release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:05.268392+00:00
---

# Apigee UI release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee UI release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to the Apigee UI in 2022 and later. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

### What is a feed reader?

Really simple syndication (RSS) feed readers aggregate content from websites that you specify.

Feed reader notifications can be email-, browser-, desktop-, or mobile-based. Some readers are free, or have free versions, and some require a subscription.

A few examples:

  * [Feedly](https://feedly.com)
  * [Feedreader](https://feedreader.com)
  * [Feeder](https://feeder.co/)



More information on RSS:

  * [RSS](https://en.wikipedia.org/wiki/RSS)
  * [ Comparison of feed aggregators](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)



Close

See also:

  * [2021 and prior Release notes](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes)
  * [Known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-ui-release-notes.xml) directly. 

## September 01, 2026

Announcement

On September 1, 2026, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
547582067 |  **Revisions can now be imported for API proxies and shared flows in a space** Importing a revision in the Apigee UI now works for an API proxy or shared flow that is associated with a [space](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).  Previously, the Apigee UI did not include the space when it uploaded the revision bundle, so the import request was rejected and the new revision was not created. This affected both API proxies and shared flows.  The earlier workaround of removing the API proxy or shared flow from its space, importing the revision, and then adding it back to the space is no longer needed.   
  
## August 22, 2026

Fixed

Bug ID | Description  
---|---  
543626585 |  **ServiceCallout policy can now be added in the Apigee UI** Adding a ServiceCallout policy in the Apigee UI no longer leaves the **Create** or **Add** button disabled.  Previously, selecting **Service Callout** in the **Create policy** or **Add policy** panel could display only the **Name** and **Display name** fields and omit the required HTTP target field. With the required field missing, the form never became valid, so the **Create** or **Add** button stayed disabled no matter what you entered. This affected both API proxies and shared flows.  The earlier workaround of creating a placeholder policy and replacing its XML in the code editor is no longer needed. For more information, see [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) and [Attach and configure policies in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui).   
  
Fixed

Bug ID | Description  
---|---  
540008387 |  **Developer custom attributes now save reliably in the Apigee UI** Saving changes to a developer in the [Apigee UI in Cloud console](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview) no longer intermittently fails to persist that developer's custom attributes.  Previously, the UI reported the save as successful, but the previous attribute values reappeared when the page was reloaded. Developer updates made with the Apigee API were not affected.   
  
## July 16, 2026

Announcement

On July 16, 2026, we released an updated version of the Apigee UI.

Fixed

**Updated PDU and basepath limits display in the Apigee UI**

Removed the ambiguous org-wide PDU limit visualization from the Apigee proxy usage card. Added display of **Deployments per instance** and **Per-org basepaths** limits to the **Instance details** page in the Apigee UI.

## July 15, 2026

Fixed

**Apigee UI**

Fixed an issue where editing a legacy API Product with a selected API Proxy could cause the Apigee UI to become unresponsive.

## July 06, 2026

Announcement

On July 6, 2026, we released an updated version of the Apigee UI.

Feature

**ParsePayload policy and payload operations matching in the Apigee UI**

The Apigee UI now supports the new payload operations matching feature:

  * The new **ParsePayload** policy is now available in the proxy editor for API proxy authoring. You can use it to extract logical operations from structured payloads at runtime.
  * The API Product page now displays payload-based operations, allowing you to configure and manage access control and quotas based on request payload content.



For more information, see [Manage MCP tool access with API products](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/manage-mcp-tool-access).

## March 13, 2026

Announcement

On March 13, 2026, we released an updated version of the Apigee UI.

Feature

**Manage environment-scoped Key Value Maps in the Apigee UI**

You can now view, add, edit, and delete environment-scoped Key Value Map (KVM) entries in the Apigee UI. For more information, see [Using key value maps](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps).

## February 13, 2026

Announcement

On February 13, 2026, we released an updated version of the Apigee UI.

Change

Updated the route for Operations Anomalies from `apigee/analytics/operations-anomalies` to `apigee/aapi-ops/operations-anomalies`.

## January 27, 2026

Announcement

On January 27, 2026, we released an updated version of the Apigee UI.

Fixed

**Show all rows in the Debug properties panel**

Fixed an issue where only the first 50 rows were displayed in the Debug properties panel, including the variables tab. The Debug properties table now displays up to 200 rows per page by default. Pagination controls are displayed if the total number of rows exceeds 200.

## January 20, 2026

Deprecated

**Debug v1 turndown**

As of January 20, 2026, Debug v1 has been turned down and is no longer available. Please use [Debug v2](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) (now referred to as Debug) for debugging API proxies.

## January 12, 2026

Announcement

On January 12, 2026, we released an updated version of the Apigee UI.

Feature

**Manage environment-level resources in the Apigee UI**

You can now manage environment-level resources using the Apigee UI. Previously, environment-level resources could only be managed using the API. For more information, see [ Managing resources](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#ui-env).

## December 17, 2025

Announcement

On December 17, 2025, we announced that Debug v1 will be shutdown on January 15, 2026. Use [Debug v2](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) instead of Debug v1.

## November 17, 2025

Announcement

On November 17, 2025, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
446973091 |  **Proxy editor endpoint view is now disabled if there are over 200 flows configured in proxy endpoints.** When opening the proxy editor endpoint view with a proxy that has over 200 flows, the proxy graph is no longer rendered, and instead you are presented with a message informing you that there are too many flows to render. This action addresses a performance issue that made the proxy editor unusable when there were over 200 flows configured.   
  
## November 12, 2025

Fixed

Bug ID | Description  
---|---  
455584175 |  **Fixed a performance issue with Debug session UI** Fixed an issue where performance of the Debug session was severely degraded when loading a Debug session with a moderate number of transactions.   
  
Announcement

On November 12, 2025, we released an updated version of the Apigee UI.

## November 02, 2025

Deprecated

The Apigee Classic UI shutdown is complete. The shutdown was finalized on November 2, 2025, completing the migration of Apigee to the Google Cloud console. All Apigee functionality is now available in the Apigee UI in the Google Cloud console. 

See the [ Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) page for more details. 

Announcement

On November 2, 2025, we released an updated version of the Apigee UI.

## October 30, 2025

Fixed

Bug ID | Description  
---|---  
443120120 |  **Fixed an issue where an incorrect target URL or cURL command was displayed in the proxy debug properties window.** New generated debug sessions now contain information in a flow info event that describes the values used by the proxy to call the target endpoint. The debug UI displays these values and uses them to generate the target URL and curl command displayed in the debug properties window when the target request event is selected. If some of the header fields are masked in the debug session, a warning appears next to the **Copy cURL** button. If the headers are truncated due to system limitations, **Copy cURL** is disabled.  Older debug sessions that do not have the new target endpoint information no longer attempt to display the target URL or generate a cURL command as they were unreliable. A dialog is displayed warning you of this when attempting to open older debug sessions.   
  
Announcement

On October 30, 2025, we released an updated version of the Apigee UI.

## October 07, 2025

Announcement

On October 7, 2025, we released an updated version of the Apigee UI.

Feature

**Output from print statements is now displayed in the Debug session viewer**  
  
A new option has been added to the transaction navigation table header in the Debug session viewer that opens the **Transaction output** window. The **Transaction output** window displays `print()` output from either _all transactions_ in the debug session, or a _specific transaction_ from the session. See [Creating a debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#create) for details.

## September 19, 2025

Announcement

On September 19, 2025, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
444579842 | **Fixed browser hang issue when uploading large bundles**. Fixed an issue where the browser would hang when creating a new proxy or proxy revision from a large uploaded zip bundle.  
  
## September 14, 2025

Announcement

On September 14, 2025, we released an updated version of the Apigee UI.

Feature

**Added icon to proxy and sharedflow editor to mark unused policies**

If a policy has yet to be [attached to any flow](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#attaching-a-policy-to-a-flow) in the configuration, an icon now displays next to that policy in the Proxy Editor side navigation to signify that the policy is currently unused in the proxy or sharedflow.

## August 26, 2025

Announcement

On August 26, 2025, we released an updated version of the Apigee UI.

Feature

**Added Display name column to Apps table**

Added a column to the [Apps table](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api#register) to show the App display name separate from the App name. The **App name** column will no longer show the display name if one is set. Instead the display name will appear in the new **Display name** column. You can also now filter by the **App name** and **Display name** independently.

Feature

**Debug view settings are now retained when switching between transactions**

When switching between transactions in the debug view the following view settings are now retained:

  * The state of the expand all toggle 
  * The zoom level of the graph 
  * The positioning of the viewport in the graph (best effort). This may be modified due to discrepancies in between the transactions 
  * The search filter. The active match will go into an indeterminate when switching transactions.



## August 20, 2025

Announcement

On August 20, 2025, we released an updated version of the Apigee UI.

Feature

**Added Name column to API Products table**

Added a column to the [API Products table](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#productdetails) to display the product name. You can now filter and sort by the product name. The link to the API product detail page is now in the **Name** column instead of the **Display Name** column.

## August 12, 2025

Announcement

On August 12, 2025, we released an updated version of the Apigee UI.

Feature

**Added path column to Debug transaction table**

A new column has been added to the [transactions table](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#create) in the Debug view that specifies the path that was used by the transaction to call the proxy.

Fixed

Bug ID | Description  
---|---  
**421974963** | **Adjusted tooltip positions in Debug sequence view** The tooltips for response items in the Debug sequence view now appear at the bottom of the element, so as not to block the elements above.  
**421975987** | **You can no longer pan away from the graph in the Debug canvas** The Debug canvas is now restricted and will no longer allow you to pan away from the graph. The scroll wheel on the mouse can now also be used to zoom in and out of the graph.  
**421975987** | **Debug canvas no longer automatically centers when event elements are clicked** When clicking an element in the Debug canvas the canvas will no longer automatically center on the selected item.  
  
## July 30, 2025

Announcement

On July 30, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Develop > API Proxies
  * Develop > Shared Flows
  * Develop > Offline Debug



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## July 29, 2025

Announcement

On July 29, 2025 we removed the **Switch to Classic** option from the following Apigee UI in the Google Cloud console pages:

  * API Proxy
  * Shared Flow
  * Offline Debug detail



This is part of the Apigee Classic UI shutdown plan.

See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## July 24, 2025

Announcement

On July 24, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Publish > Portals



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## June 25, 2025

Announcement

On June 25, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Publish > API products
  * Publish > Developers
  * Publish > Apps
  * Admin > Instances
  * Admin > Data collectors
  * Admin > Environments
  * Admin > Endpoint attachments



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## June 17, 2025

Announcement

On June 17, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Publish > Monetization
  * Analyze > API monitoring
  * Analyze > API metrics
  * Analyze > Developers > Developer Engagement
  * Analyze > Developers > Traffic Composition
  * Analyze > End Users > Devices
  * Analyze > End Users > Geomap
  * Analyze > Custom reports



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## May 29, 2025

Announcement

On May 29, 2025 we announced the shutdown schedule for the Apigee Classic UI.

Deprecated

The Apigee Classic UI will be shutdown as of August 29, 2025.

This is the final phase of moving Apigee to the Google Cloud console. Apigee in the Google Cloud console gives you the ability to manage all of your Apigee functionality in one place.

To prepare for the shutdown of the Apigee Classic UI, familiarize yourself with the new Apigee UI in Google Cloud console by reviewing [UI overview](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview).

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates and exception request.

## May 06, 2025

Announcement

On May 6, 2025, we released a new Apigee REST resource for debug sessions.

Feature

Apigee now offers a Management API that allows users to list all recent debug sessions for a given proxy, regardless of revision or environment and current deployment status. This API is available for use, and is now used to populate all recent debug sessions in the Apigee Debug UI. 

For more information on this method, see: [organizations.apis.debugsessions.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list)

## May 05, 2025

Announcement

On May 5, 2025, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
**402183688** | **Resolved navigation issue when creating a new flow in the Apigee Proxy Editor** In some instances, adding a flow to an Apigee endpoint using the Apigee Proxy Editor resulted in redirection to a `404` page.  
  
## April 15, 2025

Announcement

On April 15, 2025 we released an updated version of Apigee Analytics and the Apigee UI.

Change

Starting with this release, the Analytics dashboards available in the Apigee Classic UI redirect to the comparable dashboards in Apigee UI in Cloud console. These dashboards are available exclusively in the Apigee UI in Cloud console going forward. 

For information and usage instructions for the Analytics dashboards, see [Apigee API Analytics overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview).

## March 14, 2025

Fixed

Bug ID | Description  
---|---  
**401574741** | **Fixed issue with loading API resource and path configurations when opening the Product detail pages of legacy API products.** API resources and paths are now properly populated and applied when viewing the **Product detail** pages for legacy API products in the Apigee UI.  
  
Announcement

On March 14, 2025, we released an updated version of the Apigee UI.

## March 12, 2025

Announcement

On March 12, 2025, we released an updated version of the Apigee UI.

Change

With this release, the **Filter** display name for the `proxy` field in the **Custom reports** page of the Apigee UI in Cloud console is changed to **Proxy Endpoint**.

This change should help users differentiate between **Proxy** and **Proxy Endpoint** values when configuring filters for custom reports using Apigee API Analytics.

For more information, see [Creating and managing custom reports](/apigee/docs/api-platform/analytics/create-custom-reports#setting-filters).

## March 05, 2025

Announcement

On March 5, 2025, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
**368686537** | **Resolved issue causing delay when loading API product pages in the Apigee UI in Cloud console.** Members of Apigee organizations with large number of API proxies experienced long load times when accessing the **API product create** or **API product edit** pages in the Apigee UI in Cloud console.  
  
## February 27, 2025

Announcement

On February 27, 2025, we released an updated version of the Apigee Proxy Debug tool.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**Overview**

This release introduces a redesigned debugging experience for API proxies in the Apigee UI, which is available in Google Cloud console.

This new feature, [Debug Sequence View (v2)](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace), addresses user feedback and aims to streamline the process of identifying and resolving issues in your API proxies.

We believe that Debug Sequence View will significantly improve the API proxy debugging experience. We encourage you to try it out and provide your valuable feedback as we continue to refine and enhance this feature!

**Key highlights**

  * **Intuitive horizontal layout** :  
The new Debug Sequence View (v2) features a horizontal sequence diagram, mirroring the familiar layout of the classic Apigee Console UI, making it easier to understand the flow of your API proxy transactions at a glance.
  * **Enhanced clarity** :  
The horizontal visualization, coupled with improved grouping of events, provides a clearer picture of policy execution, highlighting errors and their context within the transaction flow.
  * **Streamlined workflow** :  
Debug Sequence View (v2) is designed to reduce the need for disruptive pop-ups and sifting through events, offering a smoother and more focused debugging experience. Reimagined icons help quickly understand a transaction at a glance.
  * **Feature parity** :  
Debug Sequence View (v2) is designed for users already familiar with debugging in Apigee Classic UI to quickly be proficient.
  * **Search** :  
You can now search for a specific string in the sequence diagram and details pane.
  * **Improved API status display** :  
The API status display in the transaction list has been improved for increased readability.
  * **Consolidated FlowInfo events** :  
FlowInfo events are now grouped together in the sequence diagram.
  * **Target URL displayed** :  
Displayed target URL on "Request Sent" node when relevant



## February 11, 2025

Change

On February 11, 2025, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
**356780408** | **Fixed issue preventing users from saving a proxy revision** Resolved issue in the proxy editor where navigating away from a proxy file containing an error would not properly clear the error state, requiring users to reload the page to save the edited proxy.  
  
## February 03, 2025

Announcement

On February 3, we released an updated version of the Apigee UI.

Feature

**GA of Apigee analytics dashboards in Google Cloud console**

You can now access these dashboards in the Apigee UI in Google Cloud console:

  * **Analytics > Developer analysis >** [Developer engagement](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard)
  * **Analytics > Developer analysis >** [Traffic composition](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/traffic-composition-dashboard)
  * **Analytics > End user analysis >** [Devices](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/devices-dashboard)
  * **Analytics > End user analysis >** [Geomap](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/geomap-dashboard)



## November 22, 2024

Fixed

Bug ID | Description  
---|---  
**357165778** | **Refactored app credential management experience** Resolved issue causing the **Apps** page in the Apigee UI in Cloud console to crash when working with apps that have a large amount of products assigned to app credentials.  
  
Change

This release includes an improved **Apps** page for Apigee API Management in the Google Cloud console, making it easier to manage API products that are assigned to app credentials. 

With this release:

  * Products can be added to an app from a single multi-select list box. 
  * Products can be approved, revoked, and removed from a credential by selecting products in the credential product table and using one of the available action buttons. 
  * Clicking the **Add Credential** button adds an empty credential to the list.
  * Credential approval and expiry configuration fields are located in the credential card.
  * A warning appears to users if they attempt to leave the **Apps** page when un-saved changes are present.



Announcement

On November 22, 2024, we released an updated version of the Apigee UI.

## November 15, 2024

Fixed

Bug ID | Description  
---|---  
**376257906** | **Fixed issue with custom report editing** Resolved issue where customer reports without properties that were created using the API could not be rendered with the **Edit** option.  
  
Announcement

On November 15, 2024, we released an updated version of the Apigee UI.

## October 11, 2024

Announcement

On October 11, 2024, we released an updated version of the Apigee UI.

Change

Bug ID | Description  
---|---  
**357165778** | **VerifyIAM policy selection removed for hybrid organizations.** The VerifyIAM policy is not supported for hybrid-enabled Apigee organizations. It has been removed as an option in the Proxy Editor.  
**372224845** | **Offline debug page not loading** Fixed issue where the offline debug page would not load if a debug session was loaded elsewhere in the UI previously.  
  
## October 03, 2024

Announcement

On October 3, 2024, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
**369647749** | **Proxy deployment units counts include shared flows** Fixed issue where proxy deployment unit counts in the UI did not take into account shared flow deployments.  
**369385955** | **Fixed the display of the Apigee apps list** Resolved an issue causing Apigee apps to display incorrectly in the Apps list when the search bar is used for filtering.  
**361497390** | **Updated the description and calculation of Apigee deployment quotas** The deployment quota displayed on the Apigee overview page now correctly describes and calculates the value of all proxy deployment units, including both API proxy and shared flow deployments across all environments./p>  
  
## September 18, 2024

Announcement

On September 18, 2024, we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
**349284447** | **All API products associated with a key now displayed in the UI** All API products associated with a key can now be viewed in the **App detail** page of the UI using pagination. Previously, a maximum of 50 API products could be displayed.  
  
## September 05, 2024

Announcement

On September 5, 2024, we released an updated version of the Apigee UI.

Feature

An informational message was added to the **action** creation flow for [Apigee Security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions#create-a-security-action), informing users that actions can't be edited or deleted.

Fixed

Bug ID | Description  
---|---  
**349284447** | **Correct sorting for revisions in Duplicate Proxy** The Duplicate Proxy experience now correctly sorts the list of existing revisions.  
**359475166** | **Fixed issue with Analytics Error Analysis** Resolved issue with the Error Composition page that interchanged the proxy error and target error legend.  
  
## August 15, 2024

Fixed

Bug ID | Description  
---|---  
**356453519** | **Fixed issue with the display of shared flow detail pages.** In some cases, detail pages for shared flows with names containing a space (" ") would not display and resulted in UI errors.  
**355674677** | **Fixed infinite redirect loop after Subscription org provisioning.** Clicking the **Continue** button in the final step of the Subscription organization provisioning flow resulted in an infinite redirect loop.  
  
Announcement

On August 15, 2024, we released an updated version of the Apigee UI.

## March 14, 2024

Announcement

On March 14, 2024 we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
**320739232** | **An issue was fixed where an incorrect error message was displayed after an API proxy or shared flow was undeployed.**  
  
## January 23, 2024

Announcement

On January 23, 2024 we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
**317739341** | In some cases the navigation menu for Monetization was hidden when Monetization was enabled in the Apigee organization. This has been fixed.  
  
## October 26, 2023

Change

On October 26, 2023 we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
287028804, 291942702 | Fixed issue where customers with a mismatched with Google Cloud project and Apigee organization ID would be presented with the Apigee welcome screen instead of the management UI in the Apigee UI in Google Cloud console.  
  
Breaking

The above fix requires a change in permissions for users managing Apigee through the Google Cloud console with a custom role.

Custom roles must now include the `apigee.projectorganizations.get` role for users who manage Apigee organizations via the Apigee UI in Cloud console. Without this role, users see a provisioning prompt in the console rather than the standard UI actions.

See [UI-based Apigee management permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#ui-based-apigee-management-permissions) for instructions.

## October 24, 2023

Announcement

On October 24, 2023 we released an updated version of the Apigee UI.

Fixed

Bug ID | Description  
---|---  
301458133 | Fixed an issue in which saving a previously deployed proxy or shared flow revision resulted in the error "revision _revision_name_ is immutable." You are now prompted to create a new revision in this case.  
  
## September 25, 2023

Announcement

On September 25, 2023, we released an updated version of the Apigee UI.

Feature

This release includes a new **Overview** page for Apigee API Management in the Google Cloud console.

From the **Overview** page, you can:

  * [Get started as a new Apigee user](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#new-user)
  * [Test your Apigee runtime](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#test-runtime)
  * [View key resource usage metrics](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#view-usage)
  * [Explore Apigee API management features](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#explore-nav)



For more information, see [UI overview](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview).

## September 19, 2023

Announcement

On September 19, 2023, we released an updated version of the Apigee UI.

Feature

**GA release of the Apigee UI in Cloud console**

This is the GA release of the [Apigee UI in Cloud](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview) console, a new version of the Apigee UI that is integrated with the Google Cloud console. The new UI makes it easier to use Apigee, while also performing related tasks in the Cloud console.

## September 18, 2023

Feature

This release includes improvements to the **Create Environment** experience in the Apigee UI in the Cloud console.

With this release, users can create a new environment, attach the environment to an Apigee instance, and assign the environment to an environment group within the same creation flow. 

In addition, users can edit or remove environment group assignments from the environment detail page in the Apigee UI, simplifying management of their Apigee implementation. 

For more information, see [Working with environments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with).

Announcement

On September 18, 2023, we released an updated version of the Apigee UI.

## May 30, 2023

Announcement

On May, 30, 2023, we released an updated version of the Apigee UI.

Feature

The following labels in the Advanced API Security abuse detection view have been changed:

  * **Detection type** has been changed to **Detection rules**.
  * **Suspected bot traffic** has been changed to **Detected traffic**.
  * **Percent bot traffic** has been changed to **% of detected traffic**.
  * **Bot count** has been changed to **Detected IP address count**.
  * **Top API key** has been changed to: **Top app key**.
  * **Bot reason** has been changed to **Detected rules**.
  * **Total calls made** has been changed to **Detected traffic**.
  * **First detection time** has been changed to **First event detected**.
  * **Last detection time** has been changed to **Last event detected**.



## May 11, 2023

Feature

This release includes new **Permissions Pre-check functionality** and UI messaging, which is available when provisioning Apigee with Pay-as-you-go pricing in the Google Cloud console. With the release of this feature, users are alerted when any permissions required to complete the provisioning operations are missing. The missing permissions and the steps to resolve are now identified in the UI messaging.

Announcement

On May 11, 2023 we released an updated version of the Apigee UI.

## March 02, 2023

Announcement

On March 2, 2023, we released an updated provisioning experience for Apigee users creating Pay-as-you-go organizations from the [Apigee UI](https://apigee.google.com/edge). All Apigee users creating new organizations with Pay-as-you-go billing can access the simplified onboarding experience, whether they are provisioning from the Apigee UI or the [Google Cloud console](https://docs.cloud.google.com/console/apigee/setup).

## March 01, 2023

Announcement

On March 1, 2023, we released an updated version of the Apigee UI.

Feature

**Public preview release of the Apigee UI in the Google Cloud console**

This release includes a [new version of the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview) that is integrated with the Google Cloud console. The new UI makes it easier to perform Apigee tasks that are managed in the Cloud console. We welcome your feedback on the new UI: click **Send Feedback** at the top of the UI.

For now, you can continue to use the classic Apigee UI if you wish: just click **Back to Classic Apigee** in the new UI.

The following tabs in the classic Apigee UI have not yet been implemented in the Apigee UI in the Cloud console, but they will be available there soon:

  * **Develop > Integrations**
  * **API Security**
  * **Monetization**
  * **Analyze > API Metrics > Cache Performance**,
  * **Analyze > API Metrics > Target Performance**
  * **Analyze > Developers**
  * **Analyze > End Users**
  * **Publish > Portals**



If you need to use these features, you can do so by switching to the classic Apigee UI.

This release will be rolled out over the next week, so you might not be able to view the new Apgee UI until the rollout is complete.

## January 11, 2023

Announcement

On January 11, 2023, we released an updated version of the Apigee UI.

Feature

**GA release of the new Proxy Editor**

The new Proxy Editor simplifies the process of adding policies to an API proxy, configuring those policies, and then deploying the proxy.

## January 09, 2023

Announcement

On January 9, 2023, we released an updated version of the Apigee UI.

Feature

**Specify an IP range with prefix /28 when creating a new instance**

Previously, you could only specify an IP range with prefix /22 when creating an instance. This change makes it possible to specify /28 ranges as well as /22 ranges when creating an Apigee instance in the instance manager or the provisioning wizard.

Fixed

Bug ID | Description  
---|---  
**255609921** | **Advanced API Security table rows now use links or span tags**  
  
## August 23, 2022

Announcement

On August 23, 2022, we released an updated version of the Apigee UI.

**Note:** Rollouts of this release will begin today and may take several weeks to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

With this release, the Apigee UI will display the new version of the Proxy Editor by default.

Feature

In this release, you can view both the visual editor and the text editor at the same time in the Develop view, without having to manually switch between the two. You can also resize the display area of either editor to view it more easily. See [Change the target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint#new-proxy-editor) for a description of the changes to the editor layout.

## July 19, 2022

Announcement

On July 19, 2022 we released an updated version of the Apigee UI.

Change

The Needs Attention Table in Advanced API Security Scores now use links instead of buttons. This fixes font and alignment issues inside the table rows.

Fixed

Bug ID | Description | 238248377 | The Needs Attention Table in Advanced API Security Scores was not showing target components. This has been fixed.

## July 01, 2022

Announcement On July 1, 2022, we released an updated version of the Apigee UI. **Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete. Feature This release contains a [new version of the Debug tab](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) in the Apigee Proxy Editor. Following previous releases of new versions of the Overview and Develop tabs, this completes the initial release of the new Proxy Editor.  To view the new Debug tab, see [Using Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace).

## June 21, 2022

Announcement On June 21, 2022 we released an updated version of the Apigee UI, Feature A search bar has been added to the new Proxy Editor Develop view. This lets you search for items within a proxy or sharedflow bundle. Feature The [Data Collectors UI](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/data-collectors) is now generally available.

## May 31, 2022

Announcement On May 31, 2022 we released an updated version of the Apigee UI. Change API Monitoring Timeline charts were not displayed correctly in the Timeline view. Previously, you needed to navigate to another API Monitoring view (such as Investigate) and then return to the Timeline view to see charts. This has been fixed: now you can go directly to the Timeline view to see charts.

## May 25, 2022

Feature You can now create and manage [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) (PSC) endpoint attachments in the Apigee UI. For details, see [Creating an endpoint attachment](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#create-an-endpoint-attachment).

## May 18, 2022

Change On May 18, 2022, we released an updated version of the Apigee UI.

## May 04, 2022

Announcement On May 4, 2022 we released an updated version of the Apigee UI. **Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. You may not see the new features and changes in the Apigee UI until the rollout is complete. Feature We have released a new version of the Develop tab in the Proxy Editor. See [Introducing the new Proxy Editor](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/new-proxy-editor-intro).

## April 18, 2022

Announcement On April 18, 2022, we released an updated version of the Apigee UI. Feature **Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. You may not see the new features and changes in the Apigee UI until the rollout is complete.The UI for managing Apigee instances has been updated and improved:

  * You can now specify a list of accepted Cloud projects that can privately connect to the instance's service attachment.
  * The New Instance dialog is replaced by a dedicated Create new instance configuration page with fields for specifying or creating a disk encryption key and for editing the list of accepted projects.
  * The Edit instance dialog is replaced by a dedicated page that lets you add or remove environments and edit the list of accepted projects that can privately connect to the instance's service attachment.
  * The UI now lets you select the disk encryption key from a list and provides a convenient flow if you want to create a new key.
  * The UI for deleting an instance has changed. There is now a **DELETE** button on the Instance details page.

For more information, see [Managing instances](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances). Fixed | Bug ID | Description  
---|---  
**229008583** | **When opening the Apigee UI in multiple tabs with different orgs, some cache entries were not being synched.** This has been fixed.  
**204429957** | **Make`ClientSpecificResourceService` and `ClientResourceNamePipe` return plain values.** Previously, methods on those classes returned observables. Now they return values.  
  
## February 22, 2022

Announcement

On February 22, 2022 we released an updated version of the Apigee UI software.

Feature

The following accessibility improvements have been made in the Apigee UI:

  * In the **Develop > API Proxies** view, the screen reader now reads "Create new proxy" for the **Create New** button 
  * In the **Traffic** column of the **API Proxies** view, the screen reader now reads the traffic tooltip text, and the tooltip has been removed. 
  * In the **Last Modified** column, the screen reader now reads a message like "5 months ago on Sep 17, 2021 6:21 PM," and the tooltip has been removed. 
  * Hovering the mouse in the **Action** column now displays a menu showing the **Delete** item, to make it accessible.



Fixed

Bug ID | Description  
---|---  
**170748813** | **The help text in the project selector menu at the top of the UI was out of date.** The information has now been updated.  
**220188457** | **Proxy/sharedflow undeployment was failing in the[new Proxy Editor](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/new-proxy-editor-intro).** This has been fixed.  
  
## February 15, 2022

Announcement

On February 15, 2022 we released an updated version of the Apigee UI software.

Feature

**The UI now shows a warning when an API Product is in legacy format, stating that some of the displayed fields might be legacy fields.**

Fixed

Bug ID | Description  
---|---  
**201759530** | **Operations that did not have methods defined were not appearing in the operations table in the API Products UI**  
**199814779** | **The test button in Admin > Environments > Keystores was not working correctly.** The button has been temporarily removed from the UI.  
  
Feature

**New Overview Tab in Proxy Editor**

We have released a new version of the Overview tab in the Proxy Editor. See [Introducing the new Proxy Editor](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/new-proxy-editor-intro).

**Note:** The new features in this release will be rolled out over the next week, so you might not be able to view them until the rollout is complete.

## February 08, 2022

Announcement

On February 8, 2022 we released an updated version of the Apigee UI software.

Fixed

Bug ID | Description  
---|---  
**212782769** | **An issue prevented editing a new target server that used a keystore reference, and selecting a key alias when using a keystore.**  
  
## February 02, 2022

Announcement

On February 2, 2022 we released an updated version of the Apigee UI software.

Fixed

Bug ID | Description  
---|---  
**205810610** | **Products couldn't be removed from an app if the product's name contained a trailing space**  
  
Feature

**The Apigee provisioning wizard can now auto-allocate /22 and /28 IP address ranges, instead of the larger /21 range**

This feature makes it easier to [allocate IP address ranges](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking) when you are provisioning Apigee. The feature is an enhancement to the [IP range feature](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes#january-24,-2022---apigee-x) released on Jan. 24, 2022.

## January 17, 2022

Announcement

On January 17, 2022 we released an updated version of the Apigee UI software.

Fixed

Bug ID | Description  
---|---  
**211983110** | **Product link in app detail page was broken.**  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
