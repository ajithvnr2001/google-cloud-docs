---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/release-notes/
title: Knative serving Release Notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:32.312014+00:00
---

# Knative serving Release Notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/resources)



Send feedback 

#  Knative serving Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Knative serving. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/runanthos-release-notes.xml) directly. 

## February 23, 2022

Change

Support for Knative Serving 1.1.2 is now available in version 1.23.0-gke.17 of Cloud Run for Anthos on Google Cloud.

The following GKE minor versions are supported:

  * 1.19 with Anthos Service Mesh 1.10
  * 1.20 with Anthos Service Mesh 1.10
  * 1.21 with Anthos Service Mesh 1.11 or 1.12



## December 07, 2021

Announcement

**Preview:** Cloud Run for Anthos is now available as a [_Preview_](https://cloud.google.com/products#product-launch-stages) for the following Anthos cluster types: Attached, AWS, Azure, and Bare metal on-premises. [Learn more](https://docs.cloud.google.com/anthos/run/docs/install/outside-gcp)

## November 02, 2021

Announcement

**General availability** : Installing Cloud Run for Anthos as an Anthos fleet component with Anthos Service Mesh is now publicly available. [Learn about what's new and changed in the latest release](https://docs.cloud.google.com/anthos/run/docs/install#newandchanged).

## October 04, 2021

Feature

**Preview** : Newly deployed services are now automatically configured to use [nip.io](https://nip.io/) as the default domain, providing immediate access to each of your services without configuration. The `nip.io` default domain is only available through [Cloud Run for Anthos fleet installations](https://docs.cloud.google.com/anthos/run/docs/install). Existing services in your fleet that use the previous `example.com` default domain are automatically upgraded to use the new `nip.io` domain. [Learn more about test domains](https://docs.cloud.google.com/anthos/run/docs/default-domain).

## September 13, 2021

Announcement

**Preview** : Installing Cloud Run for Anthos as an [Anthos feature](https://console.cloud.google.com/anthos/features) is now available as a [_Preview_](https://cloud.google.com/products#product-launch-stages). Currently available for new clusters only.

This preview of Cloud Run for Anthos installs as an [_Anthos fleet component_](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-enabled-components) and requires Anthos Service Mesh. [**Learn more**](https://docs.cloud.google.com/anthos/run/docs/install).

## July 22, 2021

Feature

Cloud Run for Anthos is now available as a separate experience from the managed Cloud Run product in the Google Cloud Console.

The new Cloud Run for Anthos page provides you a product specific experience for all your Cloud Run for Anthos services. 

[Learn more](https://docs.cloud.google.com/anthos/run/docs/console)

## June 16, 2021

Change

Cloud Run for Anthos on Google Cloud version [0.23.0-gke.6](https://github.com/google/knative-gcp/releases/tag/v0.23.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21



Change

Cloud Run for Anthos on Google Cloud version [0.22.0-gke.6](https://github.com/google/knative-gcp/releases/tag/v0.22.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21



## May 18, 2021

Change

Events for Cloud Run for Anthos version [0.21.0-gke.108](https://github.com/google/knative-gcp/releases/tag/v0.21.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21



## May 11, 2021

Security

[CVE-2021-31920](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31920) affects Istio, a component used by Cloud Run for Anthos. The CVE specifically impacts Istio's path-based AuthorizationPolicy configurations.

To ensure that your Cloud Run for Anthos clusters are not affected by the CVE, see the [security best practices guide](https://docs.cloud.google.com/anthos/run/docs/securing/best-practices) to learn more about mitigating this vulnerability.

## May 04, 2021

Change

Starting in Cloud Run for Anthos versions 0.21 and later, the new default progress deadline for deployments is up to 10 minutes. For example, it can take 10 mins before a bad revision will reach a failed state. To specify a different deadline, see [Configuring progress deadlines](https://knative.dev/docs/serving/services/deployment/#configuring-progress-deadlines).

## April 26, 2021

Change

Events for Cloud Run for Anthos version [0.20.0-gke.108](https://github.com/google/knative-gcp/releases/tag/v0.20.3) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21



Change

Cloud Run for Anthos on Google Cloud version [0.21.0-gke.0](https://github.com/google/knative-gcp/releases/tag/v0.21.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21



## March 31, 2021

Announcement

The free trial for Cloud Run for Anthos on Google Cloud has been extended and is now available until [September 30, 2021](https://cloud.google.com/anthos/run/pricing#free_trial_period).

Issue

**Known issue:**

Clusters that are upgraded to version `0.20.0-gke.6` might receive the following error when you update the cluster's [configmap](https://docs.cloud.google.com/anthos/run/docs/configuring/using-configmaps):
    
    
    Error from server (InternalError): error when replacing "/tmp/file.yaml":
    Internal error occurred: failed calling webhook "config.webhook.istio.networking.internal.knative.dev":
    the server rejected our request for an unknown reason
    

To resolve the error, you must run the following command to remove the `validatingwebhookconfiguration` configuration that is no longer supported in `0.20.0`:
    
    
    kubectl delete validatingwebhookconfiguration config.webhook.istio.networking.internal.knative.dev
    

After removing the unsupported configuration, you can proceed with updating your cluster's configmap.

## March 23, 2021

Change

Events for Cloud Run for Anthos version [0.19.0-gke.107](https://github.com/google/knative-gcp/releases/tag/v0.19.3) is now available for the following GKE minor versions:

  * 1.19
  * 1.20



## March 01, 2021

Change

Cloud Run for Anthos on Google Cloud version [0.20.0-gke.6](https://github.com/knative/serving/releases/v0.20.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20



Events for Cloud Run for Anthos version [0.18.1-gke.108](https://github.com/google/knative-gcp/releases/tag/v0.18.3) is now available for the following GKE minor versions: 

  * 1.19
  * 1.20



## February 01, 2021

Change

Cloud Run for Anthos on Google Cloud version [0.19.0-gke.1](https://github.com/knative/serving/releases/v0.19.0) is now available for the following GKE minor versions:

  * 1.18
  * 1.19
  * 1.20



## December 08, 2020

Change

Events for Cloud Run for Anthos version [0.17.5-gke.103](https://github.com/google/knative-gcp/releases/tag/v0.17.5) is now available for the following GKE minor versions:

  * 1.18
  * 1.19



## November 24, 2020

Announcement

Starting in Jan 2021, Cloud Run for Anthos will support only the `v1` version of the API: `serving.knative.dev/v1`

The following `v1alpha1` and `v1beta1` API versions have been deprecated in Knative v0.19.0 and no longer supported:

  * Service versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.

  * Route versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.

  * Revision versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.

  * Configuration versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.




If you use YAML to deploy your services, you should migrate to the `serving.knative.dev/v1` API before Jan 2021.

If you use the gcloud command-line tool, make sure you have the latest version by running: `gcloud components update`

## November 16, 2020

Change

Cloud Run for Anthos on Google Cloud version [0.18.0-gke.5](https://github.com/knative/serving/releases/v0.18.0) is now available for the following GKE minor versions:

  * 1.17
  * 1.18
  * 1.19



Issue

Authentication failures when image tags used during private container image deployment from Artifact Registry. [Learn more](https://docs.cloud.google.com/anthos/run/docs/issues#private-images)

## November 09, 2020

Change

Events for Cloud Run for Anthos version [0.17.0-gke.105](https://github.com/google/knative-gcp/releases/tag/v0.17.3) is now available for the following GKE minor versions:

  * 1.18
  * 1.19



Change

Cloud Run for Anthos on Google Cloud version [0.18.0-gke.4](https://github.com/knative/serving/releases/v0.18.0) is now available for the following GKE minor versions:

  * 1.18
  * 1.19



## October 13, 2020

Change

  * Cloud Run for Anthos on Google Cloud version [0.17.2-gke.1](https://github.com/knative/serving/releases/tag/v0.17.2) is now available for the following GKE minor version:

1.16

  * Fixes the security issue, [ISTIO-SECURITY-2020-010](https://istio.io/latest/news/security/istio-security-2020-010/) for Cloud Run for Anthos on Google Cloud clusters running on 1.15+ k8s version.




## September 30, 2020

Change

Cloud Run for Anthos on Google Cloud version [0.17.2-gke.1](https://github.com/knative/serving/releases/tag/v0.17.2) is now available for the following GKE minor version:

1.17

Feature

Now you can create a Cloud Run for Anthos cluster with internal load balancer by following these [instructions](https://docs.cloud.google.com/anthos/run/docs/setup#setting_up_a_private_internal_network).

## September 24, 2020

Change

Cloud Run for Anthos on Google Cloud version [0.17.2-gke.1](https://github.com/knative/serving/releases/tag/v0.17.2) is now available for following GKE minor version:

1.18

## September 18, 2020

Feature

[Events for Cloud Run for Anthos](https://docs.cloud.google.com/anthos/run/docs/events/quickstart) is now available in beta.

## August 24, 2020

Change

Cloud Run for Anthos on Google Cloud version [0.16.0-gke.1](https://github.com/knative/serving/releases/tag/v0.16.0) is now available for following GKE minor version: \- 1.17 \- 1.16

When Cloud Run is enabled on GKE new or existing cluster, version installed will be mapped to GKE master minor version. For more details see [this](https://docs.cloud.google.com/anthos/run/docs/cluster-versions).

## August 03, 2020

Feature

When [setting up Continuous Deployment](https://docs.cloud.google.com/anthos/run/docs/continuous-deployment-with-cloud-build) in the Cloud Run user interface, you can now select a repository that contains Go, Node.js, Python Java or .NET Core code. It will be built using [Google Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks) without needing a Dockerfile.

## July 30, 2020

Feature

You can now tag revisions. Tagged revisions get a dedicated URL allowing developers to reach these specific revisions without needing to allocate traffic to it.

## July 13, 2020

Feature

The Cloud Run user interface now allows you to easily [set up Continuous Deployment from Git using Cloud Build](https://docs.cloud.google.com/anthos/run/docs/continuous-deployment-with-cloud-build)

Change

Cloud Run for Anthos on Google Cloud version [0.15.0-gke.3](https://github.com/knative/serving/releases/tag/v0.15.0) is now available for the following versions (and greater)

  * 1.17.7-gke.15



And it now supports [Managed TLS GA](https://docs.cloud.google.com/anthos/run/docs/managed-tls).

## July 07, 2020

Change

Cloud Run for Anthos on Google Cloud version 0.14.0-gke.10 is now available for following cluster versions (and greater):

  * 1.15.12-gke.6
  * 1.16.10-gke.8
  * 1.17.6-gke.11



Fixes CVE-2020-11080 affecting [HTTP2 library used by Envoy in Istio](https://istio.io/latest/news/security/istio-security-2020-006/).

## June 19, 2020

Feature

Cloud Run for Anthos on Google Cloud version [0.14.0-gke.5](https://github.com/knative/serving/releases/tag/v0.14.0) is now available for the 1.17.6-gke.4+ cluster version.

## June 16, 2020

Feature

The Cloud Run user interface now allows you to copy a Cloud Run service.

## June 03, 2020

Feature

The Cloud Run user interface now allows you to edit the service YAML.

## April 27, 2020

Feature

Cloud Run for Anthos on Google Cloud version [0.13.2-gke.3](https://github.com/knative/serving/releases/tag/v0.13.2) is now available for following cluster versions (and greater):

  * 1.15.11-gke.9
  * 1.16.5-gke.2
  * 1.16.6-gke.11
  * 1.16.8-gke.7



## April 22, 2020

Feature

Cloud Run for Anthos now support [Private Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) for following cluster versions (and greater):

  * 1.15.11-gke.9
  * 1.16.5-gke.2
  * 1.16.6-gke.11
  * 1.16.8-gke.7



## March 30, 2020

Feature

The revision details panel now surfaces build information if the [Container Analysis API](https://docs.cloud.google.com/container-registry/docs/container-analysis) has been enabled and the container has been built with [Cloud Build](https://docs.cloud.google.com/build), as well as source repository information if the container has been built by a [Cloud Build Trigger](https://docs.cloud.google.com/build/docs/running-builds/create-manage-triggers).

## March 13, 2020

Feature

Cloud Run for Anthos on Google Cloud version [0.11.0-gke.9](https://github.com/knative/serving/releases/tag/v0.11.1) is now available for following cluster versions (and greater):

  * 1.14.10-gke.27
  * 1.15.9-gke.17
  * 1.15.11-gke.1
  * 1.16.6-gke.11
  * 1.16.8-gke.3



## February 12, 2020

Feature

Cloud Run for Anthos now supports [rollbacks, gradual rollouts (blue/green deployments), and other traffic migration manipulations](https://docs.cloud.google.com/anthos/run/docs/rollouts-rollbacks-traffic-migration) between revisions.

## February 05, 2020

Feature

[Automatic TLS certificates](https://docs.cloud.google.com/anthos/run/docs/managed-tls) can now be enabled for the following cluster versions (and greater):

  * 1.15.7-gke.23
  * 1.14.10-gke.17
  * 1.14.9-gke.23
  * 1.14.8-gke.33



## January 07, 2020

Feature

Deploy Cloud Run services from a local configuration file with `gcloud beta run services replace service.yaml`.

Feature

You can now [customize the container port](https://docs.cloud.google.com/anthos/run/docs/configuring/containers#configure-port) on which requests are sent. We still recommend listening on `$PORT` for better container portability.

Feature

[Specify custom command and arguments](https://docs.cloud.google.com/anthos/run/docs/configuring/containers#configure-entrypoint) for your deployed containers.

Feature

Use custom revision names with the `--revision-suffix` command line flag.

## November 14, 2019

Change

Cloud Run for Anthos on GCP is now Generally Available (GA).

## October 21, 2019

Feature

Cloud Run is now covered by [HIPAA Compliance](https://docs.cloud.google.com/security/compliance/hipaa).

## October 10, 2019

Feature

Cloud Run for Anthos on Google Cloud version 0.8.1-gke.0 is now available on GKE master versions 1.14.6-gke.13, 1.13.10-gke.7.

## October 01, 2019

Feature

The [max instances setting](https://docs.cloud.google.com/anthos/run/docs/configuring/max-instances) feature allows you to set a limit to the total number of container instances that are started up to handle traffic.

## September 23, 2019

Feature

Cloud Run for Anthos on Google Cloud version 0.8.0-gke.0 is now available on GKE master versions 1.13.10-gke.0.

## September 19, 2019

Feature

Cloud Run for Anthos deployed on VMware Beta release.

## September 10, 2019

Feature

You can set [labels](https://docs.cloud.google.com/anthos/run/docs/configuring/labels) on Cloud Run services and revisions.

## June 18, 2019

Change

New `--platform` flag added to [Cloud Run `gcloud` command line](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run). This argument is optional but will be required in a future release of the tool.

## June 05, 2019

Feature

Cloud Run for Anthos on Google Cloud version `0.6.0-gke.1` is now available on GKE master versions `1.13.6-gke.6` and `1.12.8-gke.7`.

Issue

When upgrading to this version, previously deployed services will return an error `no healthy upstream` until a new revision is deployed.

Feature

Improved reliability when scaling from zero.

## May 16, 2019

Change

Cloud Run for Anthos on Google Cloud no longer blocks network egress from the cluster by default in the versions `1.12.7-gke.17` and `1.11.9-gke.13`.

Feature

Cloud Run for Anthos on Google Cloud version `0.5.2-gke.1` is now available on GKE master versions `1.13.5-gke.10`, `1.12.7-gke.17` and `1.11.9-gke.13`.

Change

Cloud Run for Anthos on Google Cloud no longer injects Istio sidecars by default in the versions `1.12.7-gke.17` and `1.11.9-gke.13`.

## April 22, 2019

Feature

Cloud Run for Anthos on Google Cloud version `0.5.0-gke.1` is now available on GKE master versions `1.12.7-gke.7` and `1.11.9-gke.5`.

Change

Knative serving has been updated to `0.5.0`. See the [Knative serving `0.5.0` release notes](https://github.com/knative/serving/releases/tag/v0.5.0) for more information.

## April 09, 2019

Feature

Cloud Run for Anthos on Google Cloud Beta release.

## March 24, 2019

Issue

Request logs are not displayed in the logs panel in this release.

Issue

Cloud Run for Anthos on Google Cloud is incompatible with GKE versions `1.10.12-gke.7`, `1.11.6-gke.11`, `1.12.5-gke.5`. If you are using one of these GKE versions with the add-on enabled, you must upgrade to a newer version of GKE.

Feature

Cloud Run for Anthos on Google Cloud version `0.4.0-gke.2` is now available on GKE master versions `1.12.6-gke.0`, `1.11.8-gke.4`, and `1.11.7-gke.15`.

Feature

Knative serving has been updated to `0.4.0`. See the [Knative serving `0.4.0` release notes](https://github.com/knative/serving/releases/tag/v0.4.0) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
