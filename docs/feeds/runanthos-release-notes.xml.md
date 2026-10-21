---
url: https://docs.cloud.google.com/feeds/runanthos-release-notes.xml
title: Knative serving - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:04.858679+00:00
---

# Knative serving - Release notes

> Source: https://docs.cloud.google.com/feeds/runanthos-release-notes.xml

tag:google.com,2016:runanthos-release-notesKnative serving - Release notesGoogle Cloud Platform2022-02-23T00:00:00-08:00February 23, 2022tag:google.com,2016:runanthos-release-notes#February_23_20222022-02-23T00:00:00-08:00Changed 

Support for Knative Serving 1.1.2 is now available in version 1.23.0-gke.17 of Cloud Run for Anthos on Google Cloud.

The following GKE minor versions are supported:

  * 1.19 with Anthos Service Mesh 1.10
  * 1.20 with Anthos Service Mesh 1.10
  * 1.21 with Anthos Service Mesh 1.11 or 1.12

]]> December 07, 2021tag:google.com,2016:runanthos-release-notes#December_07_20212021-12-07T00:00:00-08:00Announcement 

**Preview:** Cloud Run for Anthos is now available as a [_Preview_](https://cloud.google.com/products#product-launch-stages) for the following Anthos cluster types: Attached, AWS, Azure, and Bare metal on-premises. [Learn more](https://cloud.google.com/anthos/run/docs/install/outside-gcp)

]]> November 02, 2021tag:google.com,2016:runanthos-release-notes#November_02_20212021-11-02T00:00:00-07:00Announcement 

**General availability** : Installing Cloud Run for Anthos as an Anthos fleet component with Anthos Service Mesh is now publicly available. [Learn about what's new and changed in the latest release](https://cloud.google.com/anthos/run/docs/install#newandchanged).

]]> October 04, 2021tag:google.com,2016:runanthos-release-notes#October_04_20212021-10-04T00:00:00-07:00Feature 

**Preview** : Newly deployed services are now automatically configured to use [nip.io](https://nip.io/) as the default domain, providing immediate access to each of your services without configuration. The `nip.io` default domain is only available through [Cloud Run for Anthos fleet installations](https://cloud.google.com/anthos/run/docs/install). Existing services in your fleet that use the previous `example.com` default domain are automatically upgraded to use the new `nip.io` domain. [Learn more about test domains](https://cloud.google.com/anthos/run/docs/default-domain).

]]> September 13, 2021tag:google.com,2016:runanthos-release-notes#September_13_20212021-09-13T00:00:00-07:00Announcement 

**Preview** : Installing Cloud Run for Anthos as an [Anthos feature](https://console.cloud.google.com/anthos/features) is now available as a [_Preview_](https://cloud.google.com/products#product-launch-stages). Currently available for new clusters only.

This preview of Cloud Run for Anthos installs as an [_Anthos fleet component_](https://cloud.google.com/anthos/multicluster-management/fleets#fleet-enabled-components) and requires Anthos Service Mesh. [**Learn more**](https://cloud.google.com/anthos/run/docs/install).

]]> July 22, 2021tag:google.com,2016:runanthos-release-notes#July_22_20212021-07-22T00:00:00-07:00Feature 

Cloud Run for Anthos is now available as a separate experience from the managed Cloud Run product in the Google Cloud Console.

The new Cloud Run for Anthos page provides you a product specific experience for all your Cloud Run for Anthos services. 

[Learn more](https://cloud.google.com/anthos/run/docs/console)

]]> June 16, 2021tag:google.com,2016:runanthos-release-notes#June_16_20212021-06-16T00:00:00-07:00Changed 

Cloud Run for Anthos on Google Cloud version [0.22.0-gke.6](https://github.com/google/knative-gcp/releases/tag/v0.22.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21



### Changed

Cloud Run for Anthos on Google Cloud version [0.23.0-gke.6](https://github.com/google/knative-gcp/releases/tag/v0.23.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21

]]> May 18, 2021tag:google.com,2016:runanthos-release-notes#May_18_20212021-05-18T00:00:00-07:00Changed 

Events for Cloud Run for Anthos version [0.21.0-gke.108](https://github.com/google/knative-gcp/releases/tag/v0.21.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21

]]> May 11, 2021tag:google.com,2016:runanthos-release-notes#May_11_20212021-05-11T00:00:00-07:00Security 

[CVE-2021-31920](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31920) affects Istio, a component used by Cloud Run for Anthos. The CVE specifically impacts Istio's path-based AuthorizationPolicy configurations.

To ensure that your Cloud Run for Anthos clusters are not affected by the CVE, see the [security best practices guide](https://cloud.google.com/anthos/run/docs/securing/best-practices) to learn more about mitigating this vulnerability.

]]> May 04, 2021tag:google.com,2016:runanthos-release-notes#May_04_20212021-05-04T00:00:00-07:00Changed 

Starting in Cloud Run for Anthos versions 0.21 and later, the new default progress deadline for deployments is up to 10 minutes. For example, it can take 10 mins before a bad revision will reach a failed state. To specify a different deadline, see [Configuring progress deadlines](https://knative.dev/docs/serving/services/deployment/#configuring-progress-deadlines).

]]> April 26, 2021tag:google.com,2016:runanthos-release-notes#April_26_20212021-04-26T00:00:00-07:00Changed 

Cloud Run for Anthos on Google Cloud version [0.21.0-gke.0](https://github.com/google/knative-gcp/releases/tag/v0.21.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21



### Changed

Events for Cloud Run for Anthos version [0.20.0-gke.108](https://github.com/google/knative-gcp/releases/tag/v0.20.3) is now available for the following GKE minor versions:

  * 1.19
  * 1.20
  * 1.21

]]> March 31, 2021tag:google.com,2016:runanthos-release-notes#March_31_20212021-03-31T00:00:00-07:00Announcement 

The free trial for Cloud Run for Anthos on Google Cloud has been extended and is now available until [September 30, 2021](https://cloud.google.com/anthos/run/pricing#free_trial_period).

### Issue

**Known issue:**

Clusters that are upgraded to version `0.20.0-gke.6` might receive the following error when you update the cluster's [configmap](https://cloud.google.com/anthos/run/docs/configuring/using-configmaps):
    
    
    Error from server (InternalError): error when replacing "/tmp/file.yaml":
    Internal error occurred: failed calling webhook "config.webhook.istio.networking.internal.knative.dev":
    the server rejected our request for an unknown reason
    

To resolve the error, you must run the following command to remove the `validatingwebhookconfiguration` configuration that is no longer supported in `0.20.0`:
    
    
    kubectl delete validatingwebhookconfiguration config.webhook.istio.networking.internal.knative.dev
    

After removing the unsupported configuration, you can proceed with updating your cluster's configmap.

]]> March 23, 2021tag:google.com,2016:runanthos-release-notes#March_23_20212021-03-23T00:00:00-07:00Changed 

Events for Cloud Run for Anthos version [0.19.0-gke.107](https://github.com/google/knative-gcp/releases/tag/v0.19.3) is now available for the following GKE minor versions:

  * 1.19
  * 1.20

]]> March 01, 2021tag:google.com,2016:runanthos-release-notes#March_01_20212021-03-01T00:00:00-08:00Changed 

Cloud Run for Anthos on Google Cloud version [0.20.0-gke.6](https://github.com/knative/serving/releases/v0.20.0) is now available for the following GKE minor versions:

  * 1.19
  * 1.20



Events for Cloud Run for Anthos version [0.18.1-gke.108](https://github.com/google/knative-gcp/releases/tag/v0.18.3) is now available for the following GKE minor versions: 

  * 1.19
  * 1.20

]]> February 01, 2021tag:google.com,2016:runanthos-release-notes#February_01_20212021-02-01T00:00:00-08:00Changed 

Cloud Run for Anthos on Google Cloud version [0.19.0-gke.1](https://github.com/knative/serving/releases/v0.19.0) is now available for the following GKE minor versions:

  * 1.18
  * 1.19
  * 1.20

]]> December 08, 2020tag:google.com,2016:runanthos-release-notes#December_08_20202020-12-08T00:00:00-08:00Changed 

Events for Cloud Run for Anthos version [0.17.5-gke.103](https://github.com/google/knative-gcp/releases/tag/v0.17.5) is now available for the following GKE minor versions:

  * 1.18
  * 1.19

]]> November 24, 2020tag:google.com,2016:runanthos-release-notes#November_24_20202020-11-24T00:00:00-08:00Announcement 

Starting in Jan 2021, Cloud Run for Anthos will support only the `v1` version of the API: `serving.knative.dev/v1`

The following `v1alpha1` and `v1beta1` API versions have been deprecated in Knative v0.19.0 and no longer supported:

  * Service versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.

  * Route versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.

  * Revision versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.

  * Configuration versions `serving.knative.dev/v1alpha1` and `serving.knative.dev/v1beta1`.




If you use YAML to deploy your services, you should migrate to the `serving.knative.dev/v1` API before Jan 2021.

If you use the gcloud command-line tool, make sure you have the latest version by running: `gcloud components update`

]]> November 16, 2020tag:google.com,2016:runanthos-release-notes#November_16_20202020-11-16T00:00:00-08:00Changed 

Cloud Run for Anthos on Google Cloud version [0.18.0-gke.5](https://github.com/knative/serving/releases/v0.18.0) is now available for the following GKE minor versions:

  * 1.17
  * 1.18
  * 1.19



### Issue

Authentication failures when image tags used during private container image deployment from Artifact Registry. [Learn more](https://cloud.google.com/anthos/run/docs/issues#private-images)

]]> November 09, 2020tag:google.com,2016:runanthos-release-notes#November_09_20202020-11-09T00:00:00-08:00Changed 

Cloud Run for Anthos on Google Cloud version [0.18.0-gke.4](https://github.com/knative/serving/releases/v0.18.0) is now available for the following GKE minor versions:

  * 1.18
  * 1.19



### Changed

Events for Cloud Run for Anthos version [0.17.0-gke.105](https://github.com/google/knative-gcp/releases/tag/v0.17.3) is now available for the following GKE minor versions:

  * 1.18
  * 1.19

]]> October 13, 2020tag:google.com,2016:runanthos-release-notes#October_13_20202020-10-13T00:00:00-07:00Changed 

  * Cloud Run for Anthos on Google Cloud version [0.17.2-gke.1](https://github.com/knative/serving/releases/tag/v0.17.2) is now available for the following GKE minor version:

1.16

  * Fixes the security issue, [ISTIO-SECURITY-2020-010](https://istio.io/latest/news/security/istio-security-2020-010/) for Cloud Run for Anthos on Google Cloud clusters running on 1.15+ k8s version.


]]> September 30, 2020tag:google.com,2016:runanthos-release-notes#September_30_20202020-09-30T00:00:00-07:00Changed 

Cloud Run for Anthos on Google Cloud version [0.17.2-gke.1](https://github.com/knative/serving/releases/tag/v0.17.2) is now available for the following GKE minor version:

1.17

### Feature

Now you can create a Cloud Run for Anthos cluster with internal load balancer by following these [instructions](https://cloud.google.com/anthos/run/docs/setup#setting_up_a_private_internal_network).

]]> September 24, 2020tag:google.com,2016:runanthos-release-notes#September_24_20202020-09-24T00:00:00-07:00Changed 

Cloud Run for Anthos on Google Cloud version [0.17.2-gke.1](https://github.com/knative/serving/releases/tag/v0.17.2) is now available for following GKE minor version:

1.18

]]> September 18, 2020tag:google.com,2016:runanthos-release-notes#September_18_20202020-09-18T00:00:00-07:00Feature 

[Events for Cloud Run for Anthos](https://cloud.google.com/anthos/run/docs/events/quickstart) is now available in beta. 

]]> August 24, 2020tag:google.com,2016:runanthos-release-notes#August_24_20202020-08-24T00:00:00-07:00Changed 

Cloud Run for Anthos on Google Cloud version [0.16.0-gke.1](https://github.com/knative/serving/releases/tag/v0.16.0) is now available for following GKE minor version: \- 1.17 \- 1.16

When Cloud Run is enabled on GKE new or existing cluster, version installed will be mapped to GKE master minor version. For more details see [this](https://cloud.google.com/anthos/run/docs/cluster-versions).

]]> August 03, 2020tag:google.com,2016:runanthos-release-notes#August_03_20202020-08-03T00:00:00-07:00Feature 

When [setting up Continuous Deployment](https://cloud.google.com/anthos/run/docs/continuous-deployment-with-cloud-build) in the Cloud Run user interface, you can now select a repository that contains Go, Node.js, Python Java or .NET Core code. It will be built using [Google Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks) without needing a Dockerfile.

### Feature

When [setting up Continuous Deployment](https://cloud.google.com/anthos/run/docs/continuous-deployment-with-cloud-build) in the Cloud Run user interface, you can now select a repository that contains Go, Node.js, Python Java or .NET Core code. It will be built using [Google Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks) without needing a Dockerfile.

]]> July 30, 2020tag:google.com,2016:runanthos-release-notes#July_30_20202020-07-30T00:00:00-07:00Feature 

You can now tag revisions. Tagged revisions get a dedicated URL allowing developers to reach these specific revisions without needing to allocate traffic to it.

]]> July 13, 2020tag:google.com,2016:runanthos-release-notes#July_13_20202020-07-13T00:00:00-07:00Changed 

Cloud Run for Anthos on Google Cloud version [0.15.0-gke.3](https://github.com/knative/serving/releases/tag/v0.15.0) is now available for the following versions (and greater)

  * 1.17.7-gke.15



And it now supports [Managed TLS GA](https://cloud.google.com/anthos/run/docs/managed-tls).

### Feature

The Cloud Run user interface now allows you to easily [set up Continuous Deployment from Git using Cloud Build](https://cloud.google.com/anthos/run/docs/continuous-deployment-with-cloud-build)

]]> July 07, 2020tag:google.com,2016:runanthos-release-notes#July_07_20202020-07-07T00:00:00-07:00Changed 

Cloud Run for Anthos on Google Cloud version 0.14.0-gke.10 is now available for following cluster versions (and greater):

  * 1.15.12-gke.6
  * 1.16.10-gke.8
  * 1.17.6-gke.11



Fixes CVE-2020-11080 affecting [HTTP2 library used by Envoy in Istio](https://istio.io/latest/news/security/istio-security-2020-006/).

]]> June 19, 2020tag:google.com,2016:runanthos-release-notes#June_19_20202020-06-19T00:00:00-07:00Feature 

Cloud Run for Anthos on Google Cloud version [0.14.0-gke.5](https://github.com/knative/serving/releases/tag/v0.14.0) is now available for the 1.17.6-gke.4+ cluster version.

]]> June 16, 2020tag:google.com,2016:runanthos-release-notes#June_16_20202020-06-16T00:00:00-07:00Feature 

The Cloud Run user interface now allows you to copy a Cloud Run service.

]]>
