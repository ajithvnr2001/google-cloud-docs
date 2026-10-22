---
url: https://docs.cloud.google.com/apigee/docs/registry/release-notes/
title: Apigee Registry release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:29.732427+00:00
---

# Apigee Registry release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/registry/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Registry release notes Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Apigee Registry**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## July 19, 2023

Announcement

On July 19, 2023 Apigee API hub released a new version of the software.

Feature

Lint result artifacts, or conformance reports, represent how conformant an API is with respect to the specified lint rules. Results in conformance report artifacts attached to an API spec revision are now displayed in the right pane of the API spec revision detail page. One of the following is displayed:

  * **No information to display.**   
No style guide conformance information has been generated for this spec.
  * **No issues found.**   
Style guide conformance scans found no issues with this spec.
  * **Warnings and Errors.**   
Any errors or warnings are explained.   
An indicator also marks the corresponding line in the spec.



**See also:**

  * [How are lint results calculated?](https://github.com/apigee/registry-experimental/tree/main/samples#how-are-lint-results-calculated)
  * [View a specification](https://docs.cloud.google.com/apigee/docs/api-hub/view-spec#view-a-specification)
  * [Manage revisions](https://docs.cloud.google.com/apigee/docs/api-hub/revisions)



## June 26, 2023

Announcement

On June 26, 2023 Apigee API hub released a new version of the software.

Feature

API hub has been upgraded to use a later version of the Registry API open-sourced project. See [v0.6.13](https://github.com/apigee/registry/releases/tag/v0.6.13) on GitHub for changes and links to previous revisions that are also included in this update. Note that this update (like all previous updates), overwrites project-level artifacts that configure API hub displays including display settings, taxonomies, and lifecycles. In future releases, we will no longer overwrite project-level artifacts.

## June 16, 2023

Announcement

On June 16, 2023 Apigee API hub released a new version of the software.

Feature

API hub has been upgraded to use a later version of the Registry API open-sourced project. See [v0.6.12](https://github.com/apigee/registry/releases/tag/v0.6.12) on GitHub for changes and links to previous revisions that are also included in this update. 

Note that artifacts associated with API spec and deployment resources are now associated with the revisions of those resources. This allows artifacts that represent lint results and other revision-specific characteristics to be associated with those revisions. When artifacts are applied directly to the parent resource (spec or deployment), these artifacts are associated with the latest revisions of these resources. For more details, see [this GitHub issue](https://github.com/apigee/registry/issues/774).

Migration of pre-existing spec- and deployment-related artifacts is not guaranteed in this update. In most cases, these artifacts are generated automatically by the registry controller and will be automatically recreated. If you find that manually-added artifacts are missing after the update, those will need to be reapplied with the same mechanisms that were available previously.

## March 13, 2023

Announcement

On March 13, 2023 Apigee API hub released a new version of the software.

Feature

FieldSet artifacts that are attached to an API are now displayed in the API overview page.

## March 08, 2023

Announcement

On March 8, 2023, the Apigee Registry API documents were updated to include the [Google APIs Explorer](https://developers.google.com/explorer-help) panel.

Feature

The [Google APIs Explorer](https://developers.google.com/explorer-help) has been added to the [Apigee Registry API documents](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations/get). The **Try this method** panel acts on real data and lets you try Google API methods without writing code.

## February 20, 2023

Announcement

On February 20, 2023 Apigee API hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
264686707 | Vertical scrollbars would not appear if the taxonomy and lifecycle stage tables overflowed the page.  
264409346 | The API list failed to load if there were over 1,000 APIs registered.  
  
## October 27, 2022

Announcement

On October 27, 2022 Apigee API hub released a new version of the software.

Feature

A link to the **Settings** page has been added to the APIs list page. 

**See:** [Discover APIs using APIs list](https://docs.cloud.google.com/apigee/docs/api-hub/apis-list)

Fixed

Bug ID | Description  
---|---  
254505866 | Provisioning API hub using the UI failed if you selected a region other than the following: `asia-east1`, `asia-southeast1`, `europe-west1`, `europe-west4`, `us-central1`, `us-east1`, `us-west1`, `us-west4`.  
  
## October 17, 2022

Announcement

On October 17, 2022 Apigee API hub released a new version of the software.

Feature

New UI provisioning wizard

Added a wizard to the API hub UI to provide a simpler provisioning process.

**See:** [Provision API hub using the UI](https://docs.cloud.google.com/apigee/docs/api-hub/provision-ui)

Feature

Updated the layout of the score card display in the API overview tab.

**See:** [Scorecard](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#scorecard)

## September 26, 2022

Announcement

On September 26, 2022 Apigee API hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
248598430 | Scorecard display did not select the latest spec by default when the recommended deployment pointed to a spec with no scorecard.  
  
## September 19, 2022

Announcement

On September 19, 2022 Apigee API hub released a new version of the software.

Feature

**Scorecard added to Apigee API hub API overview page**

The scorecard allows you to display score or health information about your APIs on the [API overview](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#scorecard) page.

The default scorecard configuration uses OpenAPI v2 and OpenAPI v3 specs and is analyzed using the Spectral linter to generate a [Lint summary](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#lint-summary).

Specify whether the [scorecard](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#scorecard) is displayed or hidden on the [Settings](https://docs.cloud.google.com/apigee/docs/api-hub/customize-display#disable-score) page.

Feature

**Help links added to Apigee API hub blank APIs list page**

If there are no APIs registered, the [APIs list](https://docs.cloud.google.com/apigee/docs/api-hub/apis-list) page will display links pointing to [API registration](https://docs.cloud.google.com/apigee/docs/api-hub/register-apis) documentation.

## September 06, 2022

Announcement

On September 6, 2022 Apigee hub released a new version of the software.

Feature

API hub has been upgraded to use a later version of the Registry API open-sourced project. See [v0.5.6](https://github.com/apigee/registry/releases/tag/v0.5.6) on GitHub for details.

Fixed

Bug ID | Description  
---|---  
N/A | Multiple fixes as listed at [v0.5.6 Changelog](https://github.com/apigee/registry/releases/tag/v0.5.6) on GitHub.  
  
## August 25, 2022

Announcement

On August 25, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
N/A | Multiple fixes as listed at [v0.5.5 Changelog](https://github.com/apigee/registry/releases/tag/v0.5.5) on GitHub.  
  
Feature

API hub has been upgraded to use a later version of the Registry API open-sourced project. See [v0.5.5](https://github.com/apigee/registry/releases/tag/v0.5.5) on GitHub for details.

## August 23, 2022

Announcement

On August 23, 2022 Apigee hub released a new version of the software.

Feature

API hub has been upgraded to use a later version of the Registry API open-sourced project. See [v0.5.4](https://github.com/apigee/registry/releases/tag/v0.5.4) on GitHub for details.

Fixed

Bug ID | Description  
---|---  
N/A | Multiple fixes as listed at [v0.5.4 Changelog](https://github.com/apigee/registry/releases/tag/v0.5.4) on GitHub.  
  
## August 03, 2022

Announcement

On August 3, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
241241073 | Changed API hub UI route prefix from `apigee/api-registry` to `apigee/hub`. The previous `apigee/api-registry` path will still continue to work, but will redirect to `apigee/hub` automatically.  
  
## July 27, 2022

Announcement

On July 27, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
230374510 | Mitigated issue where specs over 900KB (uncompressed) in size caused timeouts when trying to view their contents, and in turn caused instability with future requests for a short period of time. A warning message is now displayed when attempting to view specs that exceed 900KB.  
230374510 | Fixed issue where viewing spec files that had a file extension of .gz would allow only download of the file and would not display the contents of the file, if supported.  
  
## July 06, 2022

Announcement

On July 6, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
229852942 | The error message displayed has been clarified for the case where the uploaded spec file type was not gzip, but the mime type selected was gzip.  
  
## June 27, 2022

Announcement

On June 27, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
227334287 | An improved error dialog is displayed when an error occurs on API delete.  
229852889 | Reference lists now filter out their parent API to prevent self-references.  
232250641 | Resource IDs generated from names are now automatically truncated or padded to conform to length requirements.  
236744313 | Fixed an issue where the spinning progress indicator would not go away.  
  
## June 06, 2022

Fixed

Bug ID | Description  
---|---  
234772624 | Fixed an issue where an API could not be deleted if it had deployments.  
  
Announcement

On June 6, 2022 Apigee hub released a new version of the software

## May 16, 2022

Announcement

On May 16, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
232129385 | Users without artifact write permission encountered errors when loading various pages if the default API hub artifacts were not yet initialized by the system.  
  
## May 09, 2022

Announcement

On May 9, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
231715589 | When viewing the API hub getting started page in the Google Cloud console, if you switched to another un-provisioned project, the browser encountered a redirect loop.  
  
## May 04, 2022

Announcement

On May 4, 2022 [Apigee API hub](https://docs.cloud.google.com/apigee/docs/api-hub) began the release of a new version of the software for Public Preview.

At Public Preview, products or features are ready for testing by customers. Preview offerings are often publicly announced, but are not necessarily feature-complete, and no SLAs or technical support commitments are provided for these. Unless stated otherwise by Google, Preview offerings are intended for use in test environments only.

Announcement

On May 4, 2022 [Apigee API hub](https://docs.cloud.google.com/apigee/docs/api-hub) began the release of a new version of the software for Public Preview.

At Public Preview, products or features are ready for testing by customers. Preview offerings are often publicly announced, but are not necessarily feature-complete, and no SLAs or technical support commitments are provided for these. Unless stated otherwise by Google, Preview offerings are intended for use in test environments only.

Feature

Added the `API Hub` label in the [Apigee community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee).

Feature

Added the `API Hub` label in the [Apigee community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee).

Feature

Action buttons in the UI are now disabled if you do not have [appropriate permissions](https://docs.cloud.google.com/apigee/docs/api-hub/get-started-api-hub#roles) to perform the action.

Feature

Added instructions on how to get support. 

**Documentation:** [Get support](https://docs.cloud.google.com/apigee/docs/api-hub/support)

Feature

Added provisioning instructions. 

**Documentation:** [Provision API hub](https://docs.cloud.google.com/apigee/docs/api-hub/provision)

## April 27, 2022

Announcement

On April 27, 2022 Apigee hub released a new version of the software.

Feature

All [system taxonomy](https://docs.cloud.google.com/apigee/docs/api-hub/taxonomies) descriptions are now editable.

## April 20, 2022

Announcement

On April 20, 2022 Apigee hub released a new version of the software.

Feature

Changed columns in the **History** table:

  * Changed **Date & time** to **Updated**
  * Changed **Comment** to **Commit history**
  * Added **ID** , which is the ID of the revision as it appears in the registry API.



## April 04, 2022

Announcement

On April 4, 2022 Apigee hub released a new version of the software.

Feature

Delete dialogs will now remain open while the delete operation is being processed.

Fixed

Bug ID | Description  
---|---  
226195254 | Lifecycle replacements did not take effect on lifecycles that were assigned to versions.  
  
## March 31, 2022

Announcement

On March 31, 2022 Apigee hub released a new version of the software.

Feature

Added ability to specify the MIME type of the spec file when uploading a new revision.

**Documentation:** [Manage revisions](https://docs.cloud.google.com/apigee/docs/api-hub/revisions)

Feature

Added ability to specify the MIME type of the initial spec file when registering a new API.

**Documentation:** [Register APIs](https://docs.cloud.google.com/apigee/docs/api-hub/register-apis)

## March 28, 2022

Announcement

On March 28, 2022 Apigee hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
226194605 | The design style was not saved on API update.  
226184510 | The related and dependencies edit forms were blank when opened.  
  
## March 17, 2022

Feature

Changed the label of the "Revision History" tab on the API detail page to "History".

**Documentation:** [Manage revisions](https://docs.cloud.google.com/apigee/docs/api-hub/revisions)

Feature

Updated the API History table to use the filename as the link to the spec detail page, instead of the timestamp, and swapped the order of the Filename and Date/Time columns.

**Documentation:** [Manage revisions](https://docs.cloud.google.com/apigee/docs/api-hub/revisions)

Fixed

Bug ID | Description  
---|---  
224570429 | Some pages did not set a proper page title.  
223927791 | There was a typo in the API Edit deployment form.  
222122131 | The API Document buttons in the API Deployments table did not update when a version was deleted or updated.  
219989013 | Line breaks did not render in API descriptions.  
218682838 | Could not delete the last revision of a spec if it had artifacts attached.  
210991828 | On the Taxonomy edit form, if an element name generated an ID that was too short or too long, a submit error occurred.  
201782973 | The API Filter form on the APIs list page did not take focus when opened.  
  
Feature

Added title to the APIs list page.

**Documentation:** [Customize the display](https://docs.cloud.google.com/apigee/docs/api-hub/customize-display)

Announcement

On March 17, 2022 Apigee API hub released a new version of the software.

Feature

Added [Related](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#related) and [Dependencies](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#dependencies) reference list cards to the API detail page.

Feature

Changed the System icon from a lock Lock to a done Check and changed the Search filter from a check_circle_outline Circled Check to a done Check on the Taxonomies page.

**Documentation:** [Manage taxonomies](https://docs.cloud.google.com/apigee/docs/api-hub/taxonomies)

Feature

Added ability to edit the links in the [Related](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#related) and [Dependencies](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#dependencies) reference list cards.

## March 07, 2022

Announcement

On March 7, 2022 Apigee API hub released a new version of the software.

Feature

Added tag to the Deployments table to identify which deployment is currently set as the [recommended deployment](https://docs.cloud.google.com/apigee/docs/api-hub/deployments#specify-recommended-deployment) for the API.

Feature

Added button to the API detail page that opens the access [information panel](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#general) for the recommended deployment of the API, when clicked.

Feature

Added a button to the Deployments table that [displays the version of the documentation revision](https://docs.cloud.google.com/apigee/docs/api-hub/view-spec) that is currently assigned to the deployment and navigates to the documentation view of the revision, when clicked.

Feature

Added ability to [define an organization name](https://docs.cloud.google.com/apigee/docs/api-hub/customize-display) that will be used in the UI to identify APIs owned by the user's organization.

Feature

Changed the "Version" column in the [Deployments table](https://docs.cloud.google.com/apigee/docs/api-hub/deployments) to "Documentation".

Feature

Items in the [Deployment selection](https://docs.cloud.google.com/apigee/docs/api-hub/deployments#add-deployment) field in the Get Access side panel now signify if the deployment does not have any access information defined.

Feature

Added a button to the APIs list and API detail page that [displays the version of the documentation revision](https://docs.cloud.google.com/apigee/docs/api-hub/view-spec) that is currently assigned to the recommended deployment and navigates to the documentation view of the revision, when clicked.

Feature

Added ability to mark a deployment as the [recommended deployment](https://docs.cloud.google.com/apigee/docs/api-hub/deployments#specify-recommended-deployment) for an API.

Fixed

Bug ID | Description  
---|---  
221265023 | Fixed issue where the Get Access button in the Deployment list was visible even if the deployment had no access information.  
221265023 | Fixed issue where the Deployment selection field in the Get Access side panel would allow you to select deployments that had no access information defined.  
  
Feature

Added tab for [display settings](https://docs.cloud.google.com/apigee/docs/api-hub/customize-display) to the Settings page.

## February 15, 2022

Feature

Added ability to [view access information](https://docs.cloud.google.com/apigee/docs/api-hub/deployments#get-access) for a deployment of an API.

Announcement

On February 15, 2022 Apigee API hub released a new version of the software.

Feature

Added Deployment List to API detail page.

**Documentation:** [Deployments](https://docs.cloud.google.com/apigee/docs/api-hub/explore-overview#deployments) and [Manage deployments](https://docs.cloud.google.com/apigee/docs/api-hub/deployments)

Feature

Added ability to [delete existing deployments](https://docs.cloud.google.com/apigee/docs/api-hub/deployments#delete-deployment) for an API.

Feature

Added ability to [edit existing deployments](https://docs.cloud.google.com/apigee/docs/api-hub/deployments#edit) for an API.

Feature

Added ability to [create new deployments](https://docs.cloud.google.com/apigee/docs/api-hub/deployments#add-deployment) for an API.

## February 09, 2022

Feature

API search now [matches description text](https://docs.cloud.google.com/apigee/docs/api-hub/apis-list#search).

Feature

Changed "Add API" to ["Register API"](https://docs.cloud.google.com/apigee/docs/api-hub/register-apis) across the application.

Fixed

Bug ID | Description  
---|---  
216809912 | Gateway taxonomy has been removed from the API edit form.  
218092962 | The filter button did not close the API filter.  
  
Announcement

On February 9, 2022 Apigee API hub released a new version of the software.

## January 31, 2022

Announcement

On January 31, 2022 Apigee API hub released a new version of the software.

Fixed

Bug ID | Description  
---|---  
216513294 | API hub pages did not refresh after switching projects.  
  
## January 26, 2022

Announcement

On January 26, 2022 Apigee API hub released a new version of the software.

Feature

Added the ability to [download spec revision files](https://docs.cloud.google.com/apigee/docs/api-hub/view-spec#download-a-specification).

Feature

Added the ability to [view the contents of spec revisions](https://docs.cloud.google.com/apigee/docs/api-hub/view-spec#view-a-specification).

## January 21, 2022

Feature

Added API spec [Revision history tab](https://docs.cloud.google.com/apigee/docs/api-hub/revisions) to the API detail page.

Feature

Added the ability to [add new versions](https://docs.cloud.google.com/apigee/docs/api-hub/versions#add-version) from the API spec Revision history tab.

Feature

Added the ability to [upload new API spec revisions](https://docs.cloud.google.com/apigee/docs/api-hub/revisions#add-revision) from the API spec Revision history tab.

Announcement

On January 21, 2022 Apigee API hub released a new version of the software.

## December 15, 2021

Announcement

On December 15, 2021, Apigee API hub launched as private preview.

Private preview is available by invitation to a small set of customers for testing and feedback before becoming more broadly available.

At private preview, products or features are ready for testing by customers. Preview offerings are often publicly announced, but are not necessarily feature-complete, and no SLAs or technical support commitments are provided for these. Unless stated otherwise by Google, private preview offerings are intended for use in test environments only.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
