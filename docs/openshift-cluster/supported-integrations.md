---
url: https://docs.cloud.google.com/openshift-cluster/supported-integrations/
title: Supported integrations \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:15.892301+00:00
---

# Supported integrations  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/openshift-cluster/supported-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Supported integrations Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the integrations that Cluster Services for OpenShift supports. These integrations let you use Google services to create solutions for the applications that you deploy on OpenShift clusters that run on Google Cloud. 

## All integrations

The following table describes the Google services that Cluster Services for OpenShift lets you use with OpenShift clusters that run on Google Cloud:

**Note:** Although Cluster Services for OpenShift also supports integration with Compute Engine through [Google Cloud provider for machine API](https://github.com/openshift/machine-api-provider-gcp) and [Kubernetes Cluster API Provider for Google Cloud](https://github.com/kubernetes-sigs/cluster-api-provider-gcp), it isn't listed in the following table. This exclusion is because Compute Engine is a non-optional, core component of the integration layer of Cluster Services for OpenShift.

Use case | Google service | Integration layer components of Cluster Services for OpenShift  
---|---|---  
Block storage | Google Cloud Hyperdisk | 

  * [Persistent Disk CSI driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver)
  * [Persistent Disk CSI driver operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html-single/storage/index#persistent-storage-using-gce)

  
Block storage | Persistent Disk | 

  * [Persistent Disk CSI driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver)
  * [Persistent Disk CSI driver operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html-single/storage/index#persistent-storage-using-gce)

  
Managed file storage | Filestore | 

  * [Filestore CSI driver](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver)
  * [Google Cloud Filestore CSI driver operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html-single/storage/index#persistent-storage-csi-google-cloud-file)

  
Monitoring | Google Cloud Managed Service for Prometheus | 

  * [OpenTelemetry](https://github.com/open-telemetry)
  * [OpenTelemetry operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/red_hat_build_of_opentelemetry/index)

  
Monitoring | Cloud Monitoring | 

  * [OpenTelemetry](https://github.com/open-telemetry)
  * [OpenTelemetry operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/red_hat_build_of_opentelemetry/index)

  
Sensitive data management | Secret Manager | 

  * [Secrets store CSI driver operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/storage/using-container-storage-interface-csi#persistent-storage-csi-secrets-store)
  * [Secret Manager provider for secret store CSI driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp)
  * [External secrets operator](https://github.com/external-secrets/external-secrets)
  * [External secrets operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/security_and_compliance/external-secrets-operator-for-red-hat-openshift) ([Preview](https://cloud.google.com/products#product-launch-stages))

  
Private certificate authorities (CA) management | Certificate Authority Service | 

  * [`cert-manager` plugin](https://github.com/cert-manager/cert-manager)
  * [`cert-manager` operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/security_and_compliance/cert-manager-operator-for-red-hat-openshift)

  
Identity management | Workload Identity Federation | 

  * [Google Cloud Workload Identity Federation webhook](https://github.com/openshift/gcp-workload-identity-federation-webhook)
  * [Cloud credential operator](https://github.com/openshift/cloud-credential-operator)

  
Identity management | Google Identity |  [Cluster authentication operator](https://github.com/openshift/cluster-authentication-operator)  
  
## Block storage integrations

To provision block storage for your applications that run on self-managed OpenShift clusters on Google Cloud, Cluster Services for OpenShift provides built-in integrations with the following services: [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) and [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks).

  * **Integration layer components:** To enable the integrations with these services, Cluster Services for OpenShift uses the following components in its integration layer:

    * [Persistent Disk CSI driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver)
    * [Persistent Disk CSI driver operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html-single/storage/index#persistent-storage-using-gce)
  * **Customizations for OpenShift:** To help you better use these services with your OpenShift clusters that run on Google Cloud, Cluster Services for OpenShift implements the following customizations:

    * With Hyperdisk, support for OpenShift Virtualization by providing multi-writer support on bare metal Compute Engine instances. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).
    * With Persistent Disk, support for storage pools in the CSI driver.



For information about how to configure and use Hyperdisk and Persistent Disk with OpenShift clusters that run on Google Cloud, see the Red Hat document [Persistent storage using Persistent Disk](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/storage/configuring-persistent-storage#persistent-storage-using-gce).

## File storage integrations

To provision file storage for your applications that run on self-managed OpenShift clusters on Google Cloud, Cluster Services for OpenShift provides built-in integration with [Filestore](https://docs.cloud.google.com/filestore/docs/overview).

  * **Integration layer components:** To enable the integration with Filestore, Cluster Services for OpenShift uses the following components in its integration layer:

    * [Filestore CSI driver](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver)
    * [Google Cloud Filestore CSI driver operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html-single/storage/index#persistent-storage-csi-google-cloud-file)
  * **Customizations for OpenShift:** To help you better use Filestore with your OpenShift clusters that run on Google Cloud, Cluster Services for OpenShift lets you deploy Filestore instances that are smaller than 1 TB. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).




For information about how to configure and use Filestore with OpenShift clusters that run on Google Cloud, see the Red Hat document [Google Cloud Filestore CSI driver operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/storage/using-container-storage-interface-csi#persistent-storage-csi-google-cloud-file).

## Monitoring integrations

To set up monitoring for your applications that run on self-managed OpenShift clusters on Google Cloud, Cluster Services for OpenShift provides built-in integrations with the following services: [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

As part of your OpenShift deployment, if you have any dependency on the Prometheus ecosystem, such as using PromQL clients or Grafana dashboards, then we recommend that you set up monitoring by using Google Cloud Managed Service for Prometheus.

  * **Integration layer components:** To enable integrations with these services, Cluster Services for OpenShift uses the following components in its integration layer:

    * [OpenTelemetry](https://github.com/open-telemetry)
    * [OpenTelemetry operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/red_hat_build_of_opentelemetry/index)
  * **Customizations for OpenShift:** To help you better use Google Cloud Managed Service for Prometheus with your OpenShift clusters that run on Google Cloud, Cluster Services for OpenShift lets you set up the ingestion of OpenTelemetry prometheus metrics. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).




For information about how to configure metrics forwarding to Cloud Monitoring from OpenShift clusters that run on Google Cloud, see [Forwarding telemetry data to Google Cloud](https://docs.redhat.com/en/documentation/red_hat_build_of_opentelemetry/3.9/html/forwarding_telemetry_data/otel-forwarding-telemetry#otel-forwarding-data-to-google-cloud_otel-forwarding-telemetry).

For information about how to configure metrics forwarding to Google Cloud Managed Service for Prometheus from OpenShift clusters that run on Google Cloud, see [Forwarding telemetry data to Google-managed Prometheus](https://docs.redhat.com/en/documentation/red_hat_build_of_opentelemetry/3.9/html/forwarding_telemetry_data/otel-forwarding-telemetry#otel-forwarding-data-to-google-managed-prometheus_otel-forwarding-telemetry).

## Sensitive data management integrations

To manage sensitive data for your applications that run on self-managed OpenShift clusters on Google Cloud, Cluster Services for OpenShift provides built-in integration with [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

  * **Integration layer components:** To enable integrations with Secret Manager, Cluster Services for OpenShift uses the following components in its integration layer:

    * [Secrets store CSI driver operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/storage/using-container-storage-interface-csi#persistent-storage-csi-secrets-store)
    * [Secret Manager provider for secret store CSI driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp)
    * [External secrets operator](https://github.com/external-secrets/external-secrets)
    * [External secrets operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/security_and_compliance/external-secrets-operator-for-red-hat-openshift) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * **Customizations for OpenShift:** To help you better use Secret Manager with your OpenShift clusters that run on Google Cloud, Cluster Services for OpenShift lets you use Secret Manager with private OpenShift clusters.




For more information about how to use the secrets store CSI driver to configure and use Secret Manager with OpenShift clusters that run on Google Cloud, see the Red Hat document [Secrets store container storage interface driver operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/storage/using-container-storage-interface-csi#persistent-storage-csi-secrets-store).

For more information about how to use the external secrets operator interface to configure and use Secret Manager with OpenShift clusters that run on Google Cloud, see the Red Hat document [External secrets operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/security_and_compliance/external-secrets-operator-for-red-hat-openshift).

## Private certificate authorities management integrations

To simplify the deployment, management, and security of private certificate authorities (CAs) for use with applications that run on self-managed OpenShift clusters on Google Cloud, Cluster Services for OpenShift provides built-in integration with [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview).

  * **Integration layer components:** To enable the integration with CA Service, Cluster Services for OpenShift uses the following components in its integration layer:

    * [`cert-manager` plugin](https://github.com/cert-manager/cert-manager)
    * [`cert-manager` operator for OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/security_and_compliance/cert-manager-operator-for-red-hat-openshift)
  * **Customizations for OpenShift:** To help you better use CA Service with your OpenShift clusters that run on Google Cloud, Cluster Services for OpenShift implements the Secret Manager plugin in the `cert-manager` plugin.




For information about how to configure and use CA Service with OpenShift clusters that run on Google Cloud, see the Red Hat document [`cert-manager` operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/security_and_compliance/cert-manager-operator-for-red-hat-openshift).

## Identity management integrations

To enable identity management for your applications that run on self-managed OpenShift clusters on Google Cloud, Cluster Services for OpenShift provides built-in integrations with the following services: [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) and [Google Identity](https://developers.google.com/identity).

  * **Integration layer components:** To enable integrations with these services, Cluster Services for OpenShift uses the following components in its integration layer:

    * To enable integration with Workload Identity Federation, Cluster Services for OpenShift uses the following components in its integration layer:

      * [Google Cloud Workload Identity Federation webhook](https://github.com/openshift/gcp-workload-identity-federation-webhook)
      * [Cloud credential operator](https://github.com/openshift/cloud-credential-operator)
    * To integrate with Google Identity, Cluster Services for OpenShift uses [Cluster authentication operator](https://github.com/openshift/cluster-authentication-operator) in its integration layer.

  * **Customizations for OpenShift:** To help you better use Workload Identity Federation with your OpenShift clusters that run on Google Cloud, Cluster Services for OpenShift lets you configure Workload Identity Federation without a publicly accessible Cloud Storage bucket. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).




For information about how to configure and use Workload Identity Federation with OpenShift clusters that run on Google Cloud, see the Red Hat document [Configuring a Google Cloud cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installing_on_gcp/installing-gcp-customizations#installing-gcp-with-short-term-creds_installing-gcp-customizations).

For information about how to configure and use Google Identity with OpenShift clusters that run on Google Cloud, see the Red Hat document [Configuring a Google identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/authentication_and_authorization/configuring-identity-providers#configuring-google-identity-provider).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
