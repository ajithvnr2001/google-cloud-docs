---
url: https://docs.cloud.google.com/build/docs/release-notes/
title: Cloud Build release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:14.625876+00:00
---

# Cloud Build release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Resources ](https://docs.cloud.google.com/build/docs/resources)



Send feedback 

#  Cloud Build release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Build. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloudbuild-release-notes.xml) directly. 

## October 12, 2026

Announcement

You can now choose the [release channel](https://docs.cloud.google.com/build/docs/release-channels) for your build config or private pool. The release channel determines how frequently the underlying versions of Debian and Docker are updated.

## August 28, 2026

Feature

You can now update access tokens from the **Connection details** page for your 2nd generation Bitbucket and 2nd generation Gitlab host connections. For more information, see the following:

  * [Rotate old or expired Bitbucket Cloud access tokens](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#rotate-token)
  * [Rotate old or expired Bitbucket Data Center access tokens](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center?generation=2nd-gen#rotate-token)
  * [Rotate old or expired Bitbucket Server access tokens](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-server?generation=2nd-gen#rotate-token)
  * [Rotate old or expired GitLab Enterprise Edition access tokens](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition#rotate-token)
  * [Rotate old or expired GitLab access tokens](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab#rotate-token)



## August 24, 2026

Security

An Incorrect Authorization vulnerability [CVE-2026-19410](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-19410), in GitHub Trigger Comment Control in Cloud Build, was fixed. No customer action is needed.

## June 24, 2026

Security

For GitLab Enterprise and Bitbucket Data Center connections, Cloud Build now checks permissions on the calling principal.

When you create or update repository connections, Cloud Build uses Secret Manager secrets to authenticate to third-party Git providers. Previously, these referenced secrets were retrieved by the Cloud Build service agent (P4SA) on your behalf, checking permissions only against the P4SA's credentials rather than those of the calling principal. To adhere to the security principle of least privilege, Cloud Build now checks permissions on both the calling principal (using end-user credentials) and the P4SA, to ensure both have the `secretmanager.versions.access` IAM permission on the referenced secrets.

This check only affects GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections.

For instructions and more details, see the [Cloud Build security bulletin](https://cloud.google.com/build/docs/security-bulletins#gcp-2026-042).

## May 15, 2026

Feature

You can now configure the `results` field in build config files. This field allows a build step to store data and then attach that data in an attestation within the build results after the build has completed. For more information, see [results](https://docs.cloud.google.com/build/docs/build-config-file-schema#results).

## March 30, 2026

Feature

Cloud Build now supports uploading generic artifacts to generic repositories, and also downloading generic repositories as build dependencies. For more information, see [`genericArtifacts`](https://docs.cloud.google.com/build/docs/build-config-file-schema#generic-artifacts) and [Specify a generic artifact as a dependency](https://docs.cloud.google.com/build/docs/building/manage-dependencies#specify-generic).

## March 16, 2026

Feature

Cloud Build now supports uploading OCI images to Artifact Registry during a build process. OCI artifacts for a build are shown in the following locations:

  * The **Artifacts** column of Build history page
  * The **Execution details** tab of the Build details page
  * The **Build artifacts** tab of the Build details page



For more information, see [Store an OCI image in Artifact Registry after your build completes](https://docs.cloud.google.com/build/docs/building/build-containers#store-oci-completes) and the Cloud Build configuration file schema definition for [`oci`](https://docs.cloud.google.com/build/docs/build-config-file-schema#oci).

## March 03, 2026

Fixed

The authorization vulnerability [CVE-2026-3136](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-3136) was fixed.

## February 12, 2026

Change

Cloud Build is now available in the `asia-southeast3` region.

For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## December 08, 2025

Change

In build config files, the `mavenArtifacts` field now supports the `deployFolder` field. You can use the `deployFolder` field to upload all Maven files in a folder to a specific Artifact Registry repository. For more information, see [Upload all Maven files in a folder to an Artifact Registry repository](https://docs.cloud.google.com/build/docs/build-config-file-schema#upload-all-maven-files).

## October 09, 2025

Change

The Service Account User role has been removed from the Cloud Build Permissions page in the Google Cloud Console. Instead, when you enable certain roles on your Cloud Build service account, you can configure your Cloud Build Service account to impersonate the service account of the managed services related to those roles. This configuration lets you deploy builds using managed services while maintaining minimal permissions. For more information, see [Configure Cloud Build service account impersonation for managed services](https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp).

In addition, the Cloud Build Permissions page in the Google Cloud Console will only show the [legacy Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account#about_legacy) if your organization's policy allows it.

## September 29, 2025

Feature

Developer Connect build triggers are now [generally available](https://cloud.google.com/products/#product-launch-stages).

You can now create build triggers that build from [repositories connected to Developer Connect](https://docs.cloud.google.com/build/docs/triggers#devcon-triggers) using the Google Cloud Console, `gcloud`, the Cloud Build API, and Terraform.

## September 02, 2025

Feature

Dark theme is now available for Cloud Build. To enable the dark theme, in the Google Cloud console, click **Settings and utilities** > **Preferences**. In the navigation menu, click **Appearance** , and then select your color theme and click **Save**.

## August 15, 2025

Feature

C3 and N2D machine families are now generally available in private pools. For a complete list of supported machines, see the [`machineType`](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#machinetype) entry in the private pool configuration file schema.

In addition, the **Create private pool** and **Edit private pool** pages now show a monthly estimate based on the pool's machine type configuration. For more information, see [View private pool price estimates](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools#view-price).

## May 27, 2025

Feature

You can now create build triggers that build from [repositories connected to Developer Connect](https://docs.cloud.google.com/build/docs/triggers#devcon-triggers).

## April 22, 2025

Feature

You can now specify build dependencies in your build configuration file. For more information, see [Manage build dependencies](https://docs.cloud.google.com/build/docs/building/manage-dependencies).

## March 27, 2025

Change

In the filtering toolbar of the Build history page, you can now filter builds by region. The region drop-down has been removed. For more information, see [View build results](https://docs.cloud.google.com/build/docs/view-build-results).

## March 21, 2025

Feature

You can now specify, in your build config file, a custom Pub/Sub topic for build notifications. For more information, see [Pub/Sub topics for build notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/notifiers#pubsub-topic-config).

Change

In the filtering toolbar of the Triggers page, you can now filter by trigger repository and region. The region drop-down has been removed. For more information, see [Create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

## March 04, 2025

Change

Cloud Build is now available in the `northamerica-south1` region.

For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## January 21, 2025

Feature

You can now map specific build log fields to log entry fields when the build log is sent to Cloud Logging. For more information, see [Map build log fields to log entry fields](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#config-structured-logs).

## January 17, 2025

Feature

You can now use Cloud Build to push Go modules to Artifact Registry. For more information, see [Build and test Go applications](https://docs.cloud.google.com/build/docs/building/build-go).

## September 23, 2024

Change

Cloud Build is now available in the africa-south1 region.

For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## August 19, 2024

Feature

Cloud Build support for [custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

Custom organization policies let you define constraints for programmatic, fine-grained control over your organization's resources. You can set these policies at the organization, folder, or project level.

To learn more, see [Manage Cloud Build resources with custom constraints](https://docs.cloud.google.com/build/docs/custom-constraints).

## July 09, 2024

Feature

Cloud Build users can connect to Bitbucket Cloud and Bitbucket Data Center hosts and add repositories with the [Terraform provider for Google Cloud](https://docs.cloud.google.com/build/docs/terraform).

To learn more, see [Connect to a Bitbucket Cloud host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#terraform) and [Connect to a Bitbucket Data Center host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center?generation=2nd-gen#terraform).

## July 02, 2024

Announcement

Cloud Build is introducing new organization policy constraints.

The default behavior for how Cloud Build uses service accounts in new projects was changed to improve the security posture of our customers going forward. Organizations can opt out of these changes using new [organization policy boolean constraints](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#disable-sa).

To learn more about these changes, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

## June 25, 2024

Feature

Cloud Build support for [Supply-chain Levels for Software Artifacts (SLSA) version 1.0](https://slsa.dev/spec/v1.0/) compliant provenance is now [generally available](https://cloud.google.com/products/#product-launch-stages) to help you safeguard your automated build pipelines.

Build provenance is verifiable metadata that you can use to audit builds. Cloud Build can generate provenance aligned with the SLSA v1.0 spec when you use the option `requestedVerifyOption` with triggered builds.

Learn how to use [build provenance in Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance).

## March 07, 2024

Feature

Cloud Build repositories (2nd gen) now supports integration with [Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud) and [Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center?generation=2nd-gen). These features are [generally available](https://cloud.google.com/products/#product-launch-stages).

## January 22, 2024

Change

Cloud Build is now available in the following regions:

  * europe-west10
  * europe-west12
  * me-central1
  * me-central2



For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## January 16, 2024

Announcement

Cloud Build is introducing a new organization policy constraint.

On April 29, 2024, we are introducing changes to Cloud Build's default behavior and use of service accounts in new projects. Organizations can opt out of these changes using a new [organization policy boolean constraint](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

## November 30, 2023

Change

Cloud Build is now available in the following regions:

  * europe-southwest1
  * europe-west8
  * europe-west9
  * me-west1
  * us-east5
  * us-south1



For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## October 11, 2023

Feature

Users can now set an IP range size and starting IP address for private connections in Bitbucket Data Center using the `peeredNetworkIpRange`. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Build repositories in Bitbucket Data Center in a private network](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center-private-network).

## September 07, 2023

Feature

Users can now use [manual triggers](https://docs.cloud.google.com/build/docs/manually-build-code-source-repos?generation=1st-gen), [webhook triggers](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events), and [Pub/Sub triggers](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events) to build Bitbucket Server and Bitbucket Data Center repositories through [Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories) (1st gen). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Build repositories from Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server) and [Build repositories from Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center).

## September 01, 2023

Announcement

Cloud Build's free tier now offers the `e2-standard-2` [machine type](https://cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#machinetype) as the new default machine type. The free tier now offers 2,500 build-minutes per month to provide you with more flexibility to use free build-minutes however you want throughout the month instead of being limited to a daily allocation. Changes to the Cloud Build free tier are effective as of September 1, 2023. To learn more, see [Cloud Build pricing](https://docs.cloud.google.com/build/pricing).

## August 29, 2023

Feature

You can now configure Cloud Build to generate Google-signed identity tokens for user-specified service accounts during a build. Leveraging identity tokens with Cloud Build, you can:

  * [Authorize service-to-service access from Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/authorize-service-to-service-access)
  * [Sign your builds](https://docs.cloud.google.com/build/docs/building/build-containers#use-cosign)



Identity tokens that you generate with Cloud Build conform to the OpenID Connect (OIDC) specification.

This feature is [generally available](https://cloud.google.com/products/#product-launch-stages).

## August 18, 2023

Feature

Cloud Build now generates provenance attestations that meet [Supply-chain Levels for Software Artifacts (SLSA) v1.0](https://slsa.dev/spec/v1.0/) specifications. Build provenance is a verifiable collection of metadata that you can use to audit builds and safeguard deployments. 

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages). Builds triggered by repository events such as pushes or pull requests will generate the v1.0 provenance.

Learn how to use [build provenance in Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance).

## July 21, 2023

Announcement

The `e2-medium` machine type is now supported as a custom machine type that you can specify in your `cloudbuild.yaml` build configuration file. For more information, see [`machineType`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#machinetype).

## July 20, 2023

Feature

Cloud Build repositories (2nd gen) is now [generally available](https://cloud.google.com/products/#product-launch-stages). Cloud Build repositories (2nd gen) integrates directly with [GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github?generation=2nd-gen), [GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise?generation=2nd-gen), [GitLab](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab), and [GitLab Enterprise Edition](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab-enterprise-edition) and comes with end-to-end Terraform support. To learn more, see the [Repositories overview](https://docs.cloud.google.com/build/docs/repositories) page.

## June 23, 2023

Feature

The Cloud Build **Security insights** panel that displays security metrics such as Supply-chain Levels for Software Artifacts (SLSA) level for built artifacts, vulnerabilities, and build details is now [generally available](https://docs.cloud.google.com/sdk/gcloud#release_levels).

Feature

Cloud Build now provides the ability to upload npm packages to Artifact Registry automatically and generate Supply-chain Levels for Software Artifacts (SLSA) Level 3 build provenance. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). For more information, see [Build and test Node.js applications](https://docs.cloud.google.com/build/docs/building/build-nodejs).

## June 08, 2023

Security

When you enable the Cloud Build API in a project, Cloud Build automatically creates a default service account to execute builds on your behalf. This Cloud Build service account previously had the `logging.privateLogEntries.list` IAM permission, which allowed builds to have access to list private logs by default. This permission has now been revoked from the Cloud Build service account to adhere to the security principle of least privilege.

For instructions and more details, see the [Cloud Build security bulletin](https://cloud.google.com/build/docs/security-bulletins#gcp-2023-013).

## May 11, 2023

Feature

You can now create [manual triggers](https://docs.cloud.google.com/build/docs/manually-build-code-source-repos?generation=2nd-gen), [webhook triggers](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events?generation=2nd-gen), or [Pub/Sub triggers](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events?generation=2nd-gen) using Cloud Build repositories (2nd gen). This feature is available at the [preview](https://cloud.google.com/products/#product-launch-stages) release stage. To learn more, see the [Repositories overview](https://docs.cloud.google.com/build/docs/repositories) page.

## May 09, 2023

Feature

You can now restrict the creation of Cloud Build builds, triggers, and repositories to a particular location using an Organization Policy Service constraint. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Restricting Resource Locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

## April 26, 2023

Feature

You can now configure Cloud Build to continue executing a build even if specified steps fail. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see the allowFailure and allowExitCodes topics in [Build configuration file schema](https://docs.cloud.google.com/build/docs/build-config-file-schema).

## April 20, 2023

Feature

The organization policy for allowed regions when creating new Cloud Build resources is now [generally available](https://cloud.google.com/products/#product-launch-stages). Users can apply the policy to control when resource creation is possible given criteria specified in the policy. To learn more, see [Restricting resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

## April 04, 2023

Feature

Users can generate Supply chain Levels for Software Artifacts (SLSA) build provenance information for standalone Maven and Python packages when they upload artifacts to Artifact Registry using new fields available in the Cloud Build [config file](https://docs.cloud.google.com/build/docs/build-config-file-schema). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). For more information, see [Build and test Java applications](https://docs.cloud.google.com/build/docs/building/build-java) and [Build and test Python applications](https://docs.cloud.google.com/build/docs/building/build-python).

## March 20, 2023

Feature

You now have the option to use default logs buckets stored within your own project in the same region as your build. You can enable this feature by setting the `defaultLogsBucketBehavior` option in your build config file. When you use this option, you gain more control over data residency. Using logs within your own project also allows you to fine-tune access permissions and object lifecycle settings for your build logs. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). For more information, see the [Store and manage build logs page](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store_build_logs_in_a_user-owned_and_regionalized_bucket).

## February 08, 2023

Feature

You can now create and manage repository connections using Terraform when using Cloud Build repositories (2nd gen). Cloud Build repositories (2nd gen) is available for [GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github?generation=2nd-gen) and [GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise?generation=2nd-gen) repositories at the [preview](https://cloud.google.com/products/#product-launch-stages) release stage. To learn more, see the [Repositories overview](https://docs.cloud.google.com/build/docs/repositories) page.

## January 23, 2023

Feature

Cloud Build repositories (2nd gen) lets you easily create and manage repository connections, not only through Cloud Console but also through `gcloud` and the Cloud Build API. Cloud Build repositories (2nd gen) is available for [GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github?generation=2nd-gen) and [GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise?generation=2nd-gen) repositories at the [preview](https://cloud.google.com/products/#product-launch-stages) release stage. To learn more, see the [Repositories overview](https://docs.cloud.google.com/build/docs/repositories) page.

## January 18, 2023

Feature

Users can now configure private pools to consume fewer IP addresses within their peered Virtual Private Clouds (VPCs). The new [`peeredNetworkIpRange` config field](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#peerednetworkiprange) enables users to specify a starting IP address and the IP block size that a private pool uses. The IP block size can be as small as /29. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages).

## January 17, 2023

Change

`gcloud` commands for creating and managing build triggers are now [generally available](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## January 13, 2023

Change

The default build timeout period has been extended. Cloud Build now allows builds to run for up to 60 minutes unless you specify another timeout limit by using the [timeout field](https://docs.cloud.google.com/build/docs/build-config-file-schema#timeout_2).

## December 27, 2022

Feature

Users can now customize email, BigQuery, and webhook-based notifications using notifier templates. To learn more, see [Configure SMTP notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp), [Configure BigQuery notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery), and [Configure HTTP notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-http).

## November 30, 2022

Feature

Users can generate Supply chain Levels for Software Artifacts (SLSA) build provenance information for standalone Java and Python packages when they upload artifacts to Artifact Registry using new fields available in the [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config-file-schema). This feature is in [public preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Build and test Java applications](https://docs.cloud.google.com/build/docs/building/build-java) and [Build and test Python applications](https://docs.cloud.google.com/build/docs/building/build-python).

## November 18, 2022

Feature

You can now configure Cloud Build to continue executing a build even if specified steps fail. This feature is available as a [preview](https://cloud.google.com/products/#product-launch-stages) release. To learn more, see the `allowFailure` and `allowExitCodes` topics in [Build configuration file schema](https://docs.cloud.google.com/build/docs/build-config-file-schema).

## November 07, 2022

Feature

Users can now customize Slack notifications for their builds using notifier templates. To learn more, see [Configure Slack notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-slack).

## October 11, 2022

Feature

Cloud Build now displays build security information for artifacts stored in Artifact Registry in the Google Cloud console. The new Security insights panel is part of Build History in the console. Users can access information such as Supply chain Levels for Software Artifacts (SLSA) level for built artifacts, vulnerabilities and provenance in the panel. To learn more, see [View build security insights](https://docs.cloud.google.com/build/docs/view-build-security-insights). This feature is in [public preview](https://cloud.google.com/products#product-launch-stages).

## October 07, 2022

Feature

Users can now build repositories from GitLab Enterprise Edition, including instances hosted in a private network. This integration is available at the [preview release stage](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Building repositories from GitLab Enterprise Edition](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab-enterprise-edition).

## September 15, 2022

Feature

Users can now use Cloud Build's GitHub Issues notifier to create issues in their GitHub repository in response to build events. To learn more, see [Configuring GitHub Issue notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-githubissues).

## September 13, 2022

Feature

Users can now use Cloud Console to configure a trigger to send build logs to GitHub or GitHub Enterprise. For more information, see [Building repositories from GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github) and [Building repositories from GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise).

Feature

`gcloud` support for manual triggers is now available. To learn more, see [Manually build code in source repositories](https://docs.cloud.google.com/build/docs/manually-build-code-source-repos).

## September 12, 2022

Change

Cloud Build now supports Supply chain Levels for Software Artifacts (SLSA) level 3 assurance. Taking steps to reach SLSA level 3 can help you protect your build pipeline. To learn more, see [Viewing build provenance](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance).

## September 09, 2022

Feature

The Cloud Build script field is now [generally available](https://cloud.google.com/products/#product-launch-stages). This allows users to specify build steps using their scripting language of choice rather than as arguments to Docker. To learn more, see [Running bash scripts](https://docs.cloud.google.com/build/docs/configuring-builds/run-bash-scripts).

## August 17, 2022

Change

Cloud Build is now available in the following regions: 

  * asia-south2
  * australia-southeast2
  * northamerica-northeast2
  * southamerica-west1



For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## July 12, 2022

Change

The `gcr.io/cloud-builders/docker` builder has been upgraded to Docker client version 20.10.14. For instructions on using this builder with the Docker client versions, see [Interacting with Docker Hub images](https://docs.cloud.google.com/build/docs/interacting-with-dockerhub-images#working_with_docker_client_versions).

## June 27, 2022

Feature

Regional support for default pools and build triggers is now [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## May 23, 2022

Feature

Users can now receive build status notifications in Google Chat via a Google Chat notifier. To learn more, see [Configuring Google Chat notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-googlechat).

## May 17, 2022

Feature

Users can view build logs directly in GitHub or GitHub Enterprise without logging into Cloud Build. For more information, see [Building repositories from GitHub](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github) and [Building repositories from GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github-enterprise). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages).

## May 10, 2022

Feature

You can now use Cloud Build attestors to secure your image deployments. To learn how to set up gated deployments, see [Securing image deployments to Cloud Run and Google Kubernetes Engine](https://docs.cloud.google.com/build/docs/securing-builds/secure-deployments-to-run-gke). To learn how to view build integrity records, see [Viewing build provenance](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages).

## May 05, 2022

Feature

Cloud Build now supports a `script` field, which allows users to specify shell scripts to execute in a build step. This feature is available as a [preview](https://cloud.google.com/products/#product-launch-stages) release. To learn more, see [Using the script field](https://docs.cloud.google.com/build/docs/configuring-builds/run-bash-scripts#using_the_script_field).

## April 15, 2022

Feature

Cloud Build default pools now support regional builds at the [preview release stage](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

Feature

Cloud Build now supports regional build triggers at the [preview release stage](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

## March 02, 2022

Change

The operating system of the machine that Cloud Build uses to run builds has been upgraded to Debian 11. This results in faster build start up time when you run builds on:

  * [`e2-highcpu-8` or `e2-highcpu-32`](https://cloud.google.com/build/pricing) in the default pool.
  * Any of the [available machine types](https://cloud.google.com/build/pricing#private_pools_pricing) in a private pool.



## February 18, 2022

Feature

The organization policy for integrations with services such as GitHub is now [generally available](https://cloud.google.com/products/#product-launch-stages). Users can now apply the policy to control triggered builds from external services, such as GitHub. To learn more, see [Limiting builds triggered from external services](https://docs.cloud.google.com/build/docs/securing-builds/limit-builds-external-services).

Feature

VPC Service Controls support for Cloud Build is now [generally available](https://cloud.google.com/products/#product-launch-stages). For instructions on using this feature, see [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

## February 14, 2022

Feature

Support for configuring triggers to use a particular service account is now [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Configuring user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

## February 07, 2022

Feature

Cloud Build's Bitbucket Server and Bitbucket Data Center integration is now [generally available](https://cloud.google.com/products/#product-launch-stages). Users can build repositories from Bitbucket Server and Bitbucket Data Center, including on-premises instances. For more information, see [Building repositories from Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-server) and [Building repositories from Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-data-center).

## October 12, 2021

Feature

Build integrity features in [preview](https://cloud.google.com/products/#product-launch-stages) let you secure deployments by requiring that images are built by Cloud Build. To set up your build verification policy, see [Using binary authorization to control image deployment](https://docs.cloud.google.com/build/docs/securing-builds/use-binary-authorization). To learn how to view build integrity records, see [Viewing build provenance](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance).

## September 07, 2021

Feature

Build triggers support for [buildpacks](https://buildpacks.io/) is now [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Creating and managing build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

## September 01, 2021

Feature

VPC Service Controls support for build triggers is now available in the [preview release stage](https://cloud.google.com/products/#product-launch-stages). This feature enables users to use build triggers in projects in the VPC Service Controls perimeter. For instructions, see [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

## August 18, 2021

Feature

Cloud Build approvals are now [generally available](https://cloud.google.com/products/#product-launch-stages), allowing users to configure triggers that only execute a build when granted approval by a set of users. To learn how to create a trigger gated by approval, see [Creating and managing triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers). To learn how to approve a build, see [Approving builds](https://docs.cloud.google.com/build/docs/automating-builds/approve-builds).

## August 09, 2021

Feature

GitHub Enterprise triggers are now [generally available](https://cloud.google.com/products/#product-launch-stages). Users can build repositories from GitHub Enterprise, including on-premises instances. For more information, see [Creating GitHub Enterprise triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-github-enterprise-triggers).

## August 05, 2021

Feature

Users can now configure triggers to use a particular service account, available at the [preview release stage](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Configuring user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

## July 27, 2021

Feature

Cloud Build private pools are now [generally available](https://cloud.google.com/products/#product-launch-stages). Private pools offer [regionalization](https://docs.cloud.google.com/build/docs/locations) and greater customization over the build environment, including the ability to access resources in a private network with [support for VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls). For more information, see [Private pools overview](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

## May 20, 2021

Change

Upgraded to Docker server version 20.10.6.

## April 27, 2021

Feature

[Webhook triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-webhook-triggers) are now generally available. Learn more about using webhook triggers to build repos hosted on [Gitlab](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-gitlab), [Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-bitbucket-cloud), and [Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-bitbucket-server).

Feature

Manual triggers are now [generally available](https://cloud.google.com/products/#product-launch-stages), allowing users to run triggers on schedule. For more information, see [Scheduling builds](https://docs.cloud.google.com/build/docs/automating-builds/schedule-builds).

## March 10, 2021

Feature

Pub/Sub triggers are now [generally available](https://cloud.google.com/products/#product-launch-stages). Users can create triggers to execute builds in response to events published to a Pub/Sub topic. For more information see, [Creating Pub/Sub triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-pubsub-triggers).

## February 10, 2021

Feature

Users can now create triggers that execute builds in response to webhook events, including events from external source code management services. This feature is available as a [preview release](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Creating webhook triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-webhook-triggers) and [Building repositories hosted on Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-bitbucket-server).

## February 03, 2021

Feature

You can now [configure Cloud Build to access secrets from Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets) via environment variables.

## January 15, 2021

Feature

Regionalized builds from Cloud Functions are now visible in the Cloud Build History UI. To learn more, see [Viewing build results](https://docs.cloud.google.com/build/docs/view-build-results).

## January 11, 2021

Feature

Users can now specify their own service accounts for Cloud Build to run builds. For more information, see [User-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

## December 15, 2020

Feature

[Cloud Build Service Level Agreement (SLA)](https://cloud.google.com/build/sla) has been published with a Monthly Uptime Percentage of at least 99.95%.

Feature

Users can now create manual triggers to run builds at a specified time. To learn more about how to schedule your builds, see [Scheduling builds](https://docs.cloud.google.com/build/docs/automating-builds/schedule-builds).

## November 19, 2020

Feature

Users can now transfer Cloud Build metrics to BigQuery through the [BigQuery notifier](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery), a new open-source notifier.

## November 11, 2020

Feature

Manual triggers are now [generally available](https://cloud.google.com/products/#product-launch-stages). You can create triggers and invoke triggers manually through the Cloud Console. To learn how to create and run manual triggers, see [Creating manual triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manual-triggers).

## November 09, 2020

Change

Cloud Build allows you to specify git operations in your build configuration file and run your file using the git repository cloned onto your workspace. The cloned repository cannot exceed 500 MB.

## November 04, 2020

Feature

Users can now build containers without a Dockerfile or a Cloud Build config file [using Cloud Native Buildpacks](https://docs.cloud.google.com/build/docs/building/build-containers#use-buildpacks).

## August 17, 2020

Feature

The Cloud Build GitHub App now allows users to [view triggers by name](https://docs.cloud.google.com/build/docs/create-github-app-triggers#data_sharing) on [GitHub](https://github.com/), including in pull requests. Note that required status checks may need to be updated on GitHub after enabling this feature.

## June 30, 2020

Feature

Open-source notifiers for [Slack](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-slack) and [SMTP](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp) are now [generally available](https://cloud.google.com/products/#product-launch-stages).These notifiers can be configured to securely alert users about build status.

## June 22, 2020

Feature

Bash-style string operations and payload bindings are now [generally available](https://cloud.google.com/products/#product-launch-stages). Cloud Build's substitution variables can now refer to other substitution variables, manipulate them using bash-style string operations, and pull information from a trigger event payload. To learn more, see [Using bash-style string operations and payload bindings in substitutions](http://cloud.google.com/build/docs/configuring-builds/use-bash-and-bindings-in-substitutions).

## June 12, 2020

Change

Upgraded to Docker server version 19.03.8.

## March 12, 2020

Feature

The [Create trigger](https://console.cloud.google.com/cloud-build/triggers) page on the Cloud Console has been updated. To learn more about creating build triggers, see [Creating and managing triggers](https://docs.cloud.google.com/build/docs/running-builds/create-manage-triggers).

## February 06, 2020

Feature

[GitHub App triggers](https://docs.cloud.google.com/build/docs/create-github-app-triggers) is now Generally Available.

Feature

The [Cloud Build Dashboard](https://console.cloud.google.com/cloud-build/dashboard), which provides a high-level overview of recent builds for build triggers, is now Generally Available. For information about the Dashboard, see [Viewing the Dashboard](https://docs.cloud.google.com/build/docs/view-build-results#viewing_the_dashboard).

## January 30, 2020

Feature

The [Build history](https://console.cloud.google.com/cloud-build/builds) page and Build details page in the Google Cloud Platform Console are updated.

## December 13, 2019

Feature

Closing pull requests will now cancel running builds in pull requests associated with [GitHub App triggers](https://docs.cloud.google.com/build/docs/create-github-app-triggers).

## September 26, 2019

Feature

[GitHub App triggers](https://docs.cloud.google.com/build/docs/create-github-app-triggers) Beta is now released. New [substitution variable values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions) are now available for GitHub pull requests.

Feature

Users can now create build triggers to start builds on [GitHub pull requests](https://console.cloud.google.com/cloud-build/triggers/add).

Feature

GitHub App trigger results are posted to GitHub via the GitHub Checks API.

## August 29, 2019

Feature

[CI/CD developer hub](https://docs.cloud.google.com/docs/ci-cd) is now available.

Feature

Added a new [Cloud Build Settings](https://console.cloud.google.com/cloud-build/settings) page in the Google Cloud console for managing service account permissions.

## July 12, 2019

Change

Exposed the quota for concurrent builds in the Google Cloud console [Quotas](https://console.cloud.google.com/iam-admin/quotas?service=cloudbuild.googleapis.com%22) page.

This also allows projects to lower the number of concurrent builds that can be run at one time, or request a higher limit from the Google Cloud console.

## June 27, 2019

Feature

Environment variables can now be [defined globally](https://docs.cloud.google.com/build/docs/build-config) for all build steps in a build.

## June 20, 2019

Feature

Cloud Build now provides [Customer-Managed Encryption Keys (CMEK) compliance](https://docs.cloud.google.com/build/docs/securing-builds/cmek).

## June 19, 2019

Feature

[`gke-deploy` builder](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gke-deploy) is now available.

## May 27, 2019

Feature

[Build triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds) with inverted regex can now be run in specified branches.

## May 20, 2019

Change

Upgraded to Docker server version 18.09.3.

## February 12, 2019

Feature

Repository to project mapping is now available in the [Google Cloud Build GitHub app](https://github.com/marketplace/google-cloud-build).

## January 09, 2019

Change

Upgraded to Docker version 18.09.0.

## October 18, 2018

Change

Upgraded to Docker version 18.06.1.

## July 24, 2018

Feature

  * Container Builder is now named Cloud Build.
  * Added a new top-level menu for [Cloud Build](http://console.cloud.google.com/cloud-build) in the Google Cloud console.
  * The `gcloud` commands for Cloud Build are updated to `gcloud builds ...`.
  * Added [support for storing non-container artifacts](https://docs.cloud.google.com/build/docs/configuring-builds/store-images-artifacts) to a Cloud Storage bucket.
  * Added support for providing [filepath filters](https://docs.cloud.google.com/build/docs/running-builds/automate-builds) to trigger a build only on changes to the specified files or subdirectories.
  * Added a new [Cloud Build GitHub app](https://docs.cloud.google.com/build/docs/run-builds-on-github).



## March 06, 2018

Change

Upgraded to Docker version 17.12.0.

## February 28, 2018

Feature

Cloud Build provides [`timeout` and `status`](https://docs.cloud.google.com/build/docs/view-build-results) for build steps.

## January 10, 2018

Feature

Added support for [`gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore).

## November 02, 2017

Feature

[Community-contributed build steps](https://github.com/GoogleCloudPlatform/cloud-builders-community) released.

## October 28, 2017

Feature

[Cloud Build plugin for Jenkins](https://plugins.jenkins.io/google-cloudbuild) is now available.

## October 25, 2017

Feature

  * Lowered per-minute pricing for the default n1-standard-1 machine from $0.0034 to $0.003.
  * Added [two new machine types with 8 CPU and 32 CPU](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#machinetype).
  * Added an option to select a [custom disk size](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildoptions). 



For more information, see the [Pricing](https://cloud.google.com/build/pricing) documentation.

## October 10, 2017

Change

Builds are not triggered if the commit message includes `[skip ci]` or `[ci skip]`.

## August 28, 2017

Change

Upgraded to Docker version 17.06.1.

## August 23, 2017

Change

Builds accept `secrets` and build steps accept `secretEnv` to specify environment variables with values that have been encrypted using [Cloud KMS](https://docs.cloud.google.com/kms). 

See [Encrypting an Environment Variable Using the CryptoKey](https://docs.cloud.google.com/build/docs/securing-builds/use-encrypted-secrets-credentials#encrypting_an_environment_variable_using_the_cryptokey).

## August 03, 2017

Feature

Build steps accept `volumes` to persist specified paths across build steps.

## July 26, 2017

Feature

`cloud-build-local`, a tool for running builds locally, is available. You can install the tool using `gcloud components install cloud-build-local`.

To learn more, see [Running builds locally](https://docs.cloud.google.com/build/docs/concepts/overview#running_builds_locally).

## July 18, 2017

Feature

`gradle` is now a [supported build step](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/java/gradle).

## July 10, 2017

Feature

`homevol` mounted across build steps as `$HOME` directory.

## June 15, 2017

Feature

`kubectl` is now [supported build step](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/kubectl).

## June 07, 2017

Feature

Expanded [builder service account permissions](https://docs.cloud.google.com/build/docs/how-to/service-account-permissions) to empower end-user and IAM-based control over builder robot permissions, thereby enabling `gcloud app deploy`, `kubectl`, and other permissioned APIs to be called as part of a build.

## May 27, 2017

Change

Upgraded to Docker version 17.05.

## March 06, 2017

Feature

**General availability** of user interface in Google Cloud Platform Console, including [build history](https://console.cloud.google.com/gcr/builds) menu.

**Beta release** of [build triggers](https://console.cloud.google.com/gcr/builds).

## January 23, 2017

Change

Upgraded to Docker version 1.12.6.

## December 15, 2016

Feature

**General availability** of Cloud Build API.

[Supported build steps](https://github.com/GoogleCloudPlatform/cloud-builders) released.

## November 23, 2016

Feature

**General availability** of [Cloud SDK CLI](https://docs.cloud.google.com/sdk/gcloud/reference/builds) to Cloud Build.

## November 02, 2016

Feature

**Beta release** of [Cloud SDK CLI](https://docs.cloud.google.com/sdk/gcloud/reference/builds) to Cloud Build.

## August 22, 2016

Change

Upgraded to Docker version 1.9.1.

## July 20, 2016

Feature

**Alpha release** of [Cloud SDK CLI](https://sdk/gcloud/reference/builds/) to Cloud Build.

## January 14, 2016

Feature

**Beta release** of Cloud Build.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
