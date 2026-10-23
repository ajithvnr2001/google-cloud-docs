---
url: https://docs.cloud.google.com/looker/docs/release-overview/
title: Looker release overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:22.212242+00:00
---

# Looker release overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/release-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  Looker release overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The information on this page applies only to Looker (original) instances. For an overview of release processes for Looker (Google Cloud core), see the [Looker (Google Cloud core) release overview](https://docs.cloud.google.com/looker/docs/looker-core-release-process) documentation page.

Looker's rapid release cycle enables the team to quickly incorporate user feedback and respond to high-priority items in a timely manner. This guide explains our standard release and update processes along with best practices and variations that may better fit your needs.

## Development and release cycle

A new minor version of Looker is deployed over the course of roughly a couple of weeks. No new releases nor deployments happen in the month of December.

At times, small update patches will be released for fixes that should not wait for the next release. These are nearly always fixes for critical product or security issues. Ideally, no new features would ever be included in a patch release. The application of patch updates follows the same process as upgrading during a standard release.

### Release numbers

Our release numbering scheme uses a three-number sequence: X.Y.Z, where X is the last two digits of the year of the release, Y is the monthly version (starting with 0 in January, and using even numbers for each subsequent month), and Z is the patch release version. For example, Looker 23.4.1 would be the first patch of the Looker release from March of 2023.

### Release notes

All users are able to opt in to release notes from the **Account Settings** section of Looker. Additionally, anyone listed as a [Technical Contact](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#technical_contacts) within a Looker instance (found in **General Settings** under the **Admin** section) will receive release note notifications.

Stay current with any new features and issue fixes by checking out the release notes. See the [Looker releases](https://docs.cloud.google.com/looker/docs/looker-releases) page for links to the release notes and changelog for the latest release. The Looker releases page also has links to [historical release notes](https://docs.cloud.google.com/looker/docs/looker-releases#historical-release-notes).

### Staging environments and testing

Looker makes a great effort to effectively test before releasing, but it is possible that a new feature can have unforeseen impacts on a specific setup and use of Looker. Both Looker-hosted and customer-hosted instances can use a staging environment to test LookML and interfaces with third parties before pushing the new release to your main production instance. In addition, if your instance is customer-hosted, you can test your technical setup as well.

If you're interested in using a staging environment, [contact Looker Support](http://console.cloud.google.com/support/cases) or your dedicated Looker account team for more information.

## Update process

Ownership of the update deployment process varies according to how you host your Looker instance. Full details are in the following sections, but in summary, if an instance is Looker-hosted, Looker will manage the update process. If the instance is customer-hosted, we will provide instructions on how to perform the update.

### Updates for Looker-hosted instances

If an instance is Looker-hosted — meaning that the infrastructure for the instance is managed by Looker — our Release and Ops teams will apply updates during [designated maintenance windows](https://docs.cloud.google.com/looker/docs/google-maintenance-policy-for-looker-hosted-services). For users who have opted in to receive emails from Looker, we announce each new release in an email that includes the date and timing of the maintenance window. Updates generally take up to 10 minutes within the maintenance window to minimize interruption.

Looker applies updates on a rolling basis. We apply the updates based on the characteristics of an instance's setup, on how Looker is used within an organization, and on an individual company's preference to receive a release earlier or later in the cycle. As is always the case in software releases, the first few patch versions of a new minor version are more likely to contain product issues; however, for Looker-hosted instances we can quickly apply patches as soon as they become available.

#### What if I need to skip a new release version?

[Reach out to Looker Support through the Google Cloud console](http://console.cloud.google.com/support/cases) or to your dedicated account team, and we will work with you to ensure that your business needs are addressed.

### Updates for customer-hosted Looker instances

Customer-hosted Looker instances require that the customer be responsible for managing release version updates. It is very important to stay on the latest supported release to avoid running an unsupported, or end-of-life, release. Customer-hosted instances of Looker receive update notifications toward the end of the release rollout cycle. This ensures that any critical issues can be addressed beforehand.

When a new release is ready for installation, any Looker user listed as a [Technical Contact](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#technical_contacts) for your organization will be sent an email with a link to the latest update file (JAR format), release notes, and instructions on how to install the update.

> **We strongly advise against rolling back to a previous version.** Instead, be sure to make a complete [backup of your system](https://docs.cloud.google.com/looker/docs/creating-backups) before each update. This allows an instance to be restored to a previous version. Restoring to a previous version without a backup can cause irreversible content loss and damage to the instance.

### Early access

If receiving an update earlier in the rollout process fits the business needs of your company and you want to opt in for the earliest access to new releases, [sign up here](https://goo.gl/forms/V0ZISnwS2J3AlUf33) or [open a support request](http://console.cloud.google.com/support/cases).

## Extended support release program

While many organizations share our taste for the rapid product improvements associated with short release cycles, Looker understands the tradeoff that comes with this pace and why a slower cycle could be more appropriate for certain business use cases.

To meet these needs, every third minor release will be designated as an [extended support release (ESR)](https://docs.cloud.google.com/looker/docs/standard-extended-support-release-program-overview) version. While we will always give our best effort to maximize the stability of the product with each release, a release version designated as an ESR will receive additional time for testing and for issue fixes.

We will also provide a longer window for development and product support for ESRs and will patch for issues of [Severity 1 and Severity 2 level](https://looker.com/terms) where relevant and possible.

### Validating new ESR releases

Each ESR will have a one-month staging period because of the larger changes in the product between ESRs. As a part of this program, it is a requirement to first perform a new ESR version update on a staging server. This allows users to test content, workflows, and new features before moving the production server to the new ESR version.

### Opting in to the ESR program

If the [ESR program](https://docs.cloud.google.com/looker/docs/standard-extended-support-release-program-overview) seems better suited for your company's business needs, contact your Customer Success team to discuss this option further.

## Questions?

If you have questions, a great place to ask them is Looker's [Community forum](https://discuss.google.dev/c/looker/19), where discussion of all sorts is welcomed and encouraged, including (but not limited to) Looker, business intelligence, and data in general, with other Good Lookers (customers) and Looker analysts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
