---
url: https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes-2022/
title: Apigee release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:41:32.679460+00:00
---

# Apigee release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes-2022/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Apigee release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to all Apigee software in 2022 and later. We recommend that users periodically check this list for any new announcements.

See [2021 and prior](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes) for older release notes.

### February 15, 2022 - Apigee X

On February 15, 2022, we released an updated version of the Apigee X software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Backend target routing with Private Service Connect**  
You can now use [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) (PSC) to connect Apigee with backend target services running in VPC networks other than the one that is peered with your Apigee organization. For details, see [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).  
---|---  
  
### February 15, 2022 - Apigee UI

On February 15, 2022, we released an updated version of the Apigee UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **New Overview Tab in Proxy Editor**  
We have released a new version of the Overview tab in the Proxy Editor. See [Introducing the new Proxy Editor](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/new-proxy-editor-intro).   
**Note:** The new features in this release will be rolled out over the next week, so you might not be able to view them until the rollout is complete.  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **The UI now shows a warning when an API Product is in legacy format, stating that some of the displayed fields might be legacy fields.**  
  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **201759530** | **Operations that did not have methods defined were not appearing in the operations table in the API Products UI**  
This has been fixed.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **199814779** | **The test button in**Admin > Environments > Keystores** was not working correctly**  
The button has been temporarily removed from the UI.  
  
### February 8, 2022 - Apigee X

On February 8, 2022, we released an updated version of the Apigee X software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **N/A** | **Upgraded infrastructure and libraries**  
  
---|---|---  
  
### February 8, 2022 - Integrated portal

On February 8, 2022, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **212421254** | **Consumers can access teams in a portal for which they have no IDP account**  
Before, a consumer could access a team as long as they were added to the team and had an IDP account in the same organization as the team. Now they can only access the team if they are added as a member and have an IDP account in the same portal as the team.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **209436418** | **Display asset file sizes in megabytes**  
Asset file size was being incorrectly displayed in mebibytes and is now shown in megabytes.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **207130598** | **Improve asset upload error messages**  
Improved an error message when an unsupported image type was uploaded.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205963075** | **New portal name rules are not enforced on backend**  
The same portal name rules that were already enforced on the front end are now also enforced on the backend.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205881764** | **Cannot delete mobile logo/favicon in Apigee X/Hybrid**  
Fixed a bug where Apigee X and Hybrid customers could not delete mobile logos or favicons.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205629978** | **Broken HTML after portals v2 migration**  
The live portal of the upgraded portal will not be displayed correctly after migrating a portal from v1 to v2.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205581372** | **Users endpoint should not crash when passed an invalid Enum value**  
Passing an invalid sortBy value to the `providers/{scope}/users` endpoint is now handled gracefully.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196875216** | **Team does not exist exceptions should not be reported as 500s**  
When API producers attempted to retrieve a team which does not exist, they got an uniformative 500. Now they get an easy-to-read 404.  
  
### February 08, 2022 - Apigee UI

On February 08, 2022, we released an updated version of the Apigee UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **212782769** | **An issue prevented editing a new target server that used a keystore reference, and selecting a key alias when using a keystore.**  
This has been fixed.  
---|---|---  
  
### February 02, 2022 - Apigee UI

On February 02, 2022, we released an updated version of the Apigee UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **The Apigee provisioning wizard can now auto-allocate /22 and /28 IP address ranges, instead of the larger /21 range**  
This feature makes it easier to [allocate IP address ranges](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking) when you are provisioning Apigee. The feature is an enhancement to the IP range feature released on Jan. 24, 2022.  
---|---  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205810610** | **Products couldn't be removed from an app if the product's name contained a trailing space**  
This has been fixed.  
---|---|---  
  
### January 31, 2022 - Apigee hybrid v1.6.4

On January 31, 2022, we released an updated version of the Apigee hybrid v1.6.4 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **214960081** | **HTTPS endpoints could be called as HTTP resulting in an "EOF unexpected" error.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **210590135** | **Invalid protocol in proxy.url flow variable in Apigee X.**  
The proxy.url flow variable could show as "http" even when the request is https.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **203785814** | **A transient error could occur when calling conversion webhook for Apigee Telemetry.**  
The error would occur when Apigee CRD is installed too early in the sequence. The installer job now checks for the correct sequence.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **197945951** | **Stale DNS record in MP memory could cause an outage for a proxy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **189341334** | **The backup utility did not work with workload identity.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade). 

### January 28, 2022 - Apigee X

On January 28, 2022, we released an updated version of the Apigee X software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **UI updates for service networking and instance creation**  
UI updates were made to support changes to network IP CIDR range requirements for service networking and instance creation. These changes simplify Apigee provisioning.  
---|---  
  
### January 28, 2022 - Apigee hybrid v1.5.7

On January 28, 2022, we released an updated version of the Apigee hybrid v1.5.7 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **214960081** | **HTTPS endpoints could be called as HTTP resulting in an "EOF unexpected" error.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204368970** | **TLS variables were not being set by Apigee Runtime.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **189341334** | **Fixed potential connection leaks for watcher component.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### January 24, 2022 - Apigee X

On January 24, 2022, we released an updated version of the Apigee X software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Reduce the IP range required to peer your VPC network**  
The required IP range needed to peer your VPC network to the Apigee network is now limited to a non-overlapping CIDR range of /22. This change simplifies Apigee provisioning. Note that the provisioning step for [service network configuration](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#service-networking) has been updated to refelect this change. For more information, see [Understanding peering ranges](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges).  
---|---  
  
### January 19, 2022 - Apigee Integration

On January 19, 2022, we released an updated version of the Apigee Integration software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Filter clause in the Connectors task**  
You can add a filter to restrict the amount of data processed by an entity operation. For more information, see [Add a filter for an operation](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#filter).  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Upload and download integrations**  
The **Upload/download menu** button in the integration designer lets you upload and download integrations in a JSON file format. For more information, see [Upload and download integrations](https://docs.cloud.google.com/apigee/docs/api-platform/integration/upload-download).  
  
### January 17, 2022 - UI

On January 17, 2022, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **211983110** | **Product link in app detail page was broken.**  
This has been fixed.  
---|---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
