---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/fetch-trust-bundles/
title: Fetch GDC trust bundles \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:05.993288+00:00
---

# Fetch GDC trust bundles  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/fetch-trust-bundles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Fetch GDC trust bundles Stay organized with collections  Save and categorize content based on your preferences. 

A trust bundle, also known as a trust list, is a group of trust anchors, such as entities, that are inherently trusted and whose trust is not transferred by another entity (trusted third parties). These trust anchors are delivered as certificate authority (CA) certificates. The certification path-building algorithm uses these CA certificates to establish a chain between a certificate obtaining validation and the trust anchors.

This document is for audiences within the platform administrator group, such as IT admins or security engineers, who want to fetch GDC trust bundles. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before fetching GDC trust bundles, you must Establish initial trust for new organizations. This step is required for both the well-known server and `kubectl` methods, but only if you're connecting to a new organization for the first time.

For the well-known server method, no other prerequisites are required. For the `kubectl` method, you must also complete the permissions and tooling prerequisites.

### Establish initial trust for new organizations

If you connect to a new GDC organization for the first time, you must establish initial trust. This one-time process ensures a secure connection by trusting the organization's Certificate Authority (CA) on your client machine.

  1. Contact a member of your infrastructure operator (IO) group to request the initial trust bundle for the new organization. The IO has the necessary access to fetch this bundle, which is typically sourced from the `trust-store-root-ext` secret within the org infrastructure cluster.

  2. Obtain the initial trust bundle file from your IO through a secure channel outside of GDC, as defined by your organization's security policies.

  3. Install the trust bundle into your client machine's trust store, following your system's standard procedures for trusting root CA certificates.




If you need access to ServiceNow, also obtain and install the `gdchservices` organization trust bundle using the same process.

### Request IAM roles

To fetch the trust bundle with `kubectl`, you need permission to view secrets. Contact your IAM Org Admin to request the **Trust Store Viewer** (`trust-store-viewer`) role.

### Prepare your environment

To use the `kubectl` method, prepare your local environment:

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig) for the management API server in your targeted zone. You need the path to the kubeconfig file to replace `MANAGEMENT_API_SERVER_KUBECONFIG` in the `kubectl` commands.




## Trust bundle types

Distributed Cloud provides two types of managed trust bundles for platform administrators:

  * `trust-store-root-ext`: contains the internal root CA and web-tls CA. The content is different depending on where it resides, such as the root or the tenant organization. Use this trust bundle to communicate across organization boundaries or to access services like object storage within the organization.

  * `trust-store-global-root-ext`: available in the global API server and zonal API server `platform` namespace. When the global API server is ready, the bundle populates all other zonal `trust-store-root-ext` data, including local data.




## Fetch the trust bundle

You can fetch trust bundles from the well-known server endpoint, or from the cluster using `kubectl`.

### Fetch from the well-known server

GDC provides a secure way to access trust bundles through a well-known server endpoint. Use this method when you need to fetch the `trust-store-global-root-ext` bundle without directly interacting with the cluster using `kubectl`.

Make sure you have established initial trust with your organization's specific CAs before performing the steps in this section.

**Caution:** When fetching trust bundles from the well-known server, it's crucial to protect against person-in-the-middle (PITM) attacks. Make sure that you're connecting to a secure and controlled environment.

### Linux

  1. Export the following environment variables:
         
         export STORAGE=STORAGE
         export ORG_NAME=ORG_NAME
         export DNS_SUFFIX=DNS_SUFFIX
         

Replace the following:

     * `STORAGE`: the directory path where you want to store the trust bundle file.
     * `ORG_NAME`: the name of your organization within GDC.
     * `DNS_SUFFIX`: your DNS suffix. For example, if one of your domains is `org-1.zone1.google.gdch.test`, your DNS suffix is `zone1.google.gdch.test`.
  2. Set the `WELL_KNOWN_URL` environment variable:
         
         export WELL_KNOWN_URL="https://console.${ORG_NAME:?}.${DNS_SUFFIX:?}/.well-known/certificate-authority"
         

  3. Set the `GLOBAL_TRUST_BUNDLE_FILE` environment variable. This file stores the GDC trust bundle locally in your specified `$STORAGE` location.
         
         export GLOBAL_TRUST_BUNDLE_FILE="${STORAGE:?}/global/ca-bundles/global-trust-bundle"
         

  4. Create the directory for the trust bundle file:
         
         mkdir -p "$(dirname "${GLOBAL_TRUST_BUNDLE_FILE:?}")"
         

  5. Obtain the `trust-store-global-root-ext` trust bundle from the well-known server and store it in the file specified by the `GLOBAL_TRUST_BUNDLE_FILE` environment variable:
         
         curl "${WELL_KNOWN_URL:?}" | sed '$a\' > "${GLOBAL_TRUST_BUNDLE_FILE:?}"
         




### Windows

  1. Set the following PowerShell variables:
         
         $STORAGE = "STORAGE"
         $ORG_NAME = "ORG_NAME"
         $DNS_SUFFIX = "DNS_SUFFIX"
         

Replace the following:

     * `STORAGE`: the directory path where you want to store the trust bundle file, such as `C:\Users\username\bundles`.
     * `ORG_NAME`: the name of your organization within GDC.
     * `DNS_SUFFIX`: your DNS suffix. For example, if one of your domains is `org-1.zone1.google.gdch.test`, your DNS suffix is `zone1.google.gdch.test`.
  2. Create the directory for the trust bundle file:
         
         New-Item -ItemType Directory -Force -Path (Split-Path -Path "STORAGE\global\ca-bundles\global-trust-bundle")
         

  3. Obtain the `trust-store-global-root-ext` trust bundle from the well-known server and store it in trust bundle file:
         
         Invoke-WebRequest -Uri "https://console.ORG_NAME.DNS_SUFFIX/.well-known/certificate-authority" -OutFile "STORAGE\global\ca-bundles\global-trust-bundle"
         




The fetched trust bundle file contains one or more CA certificates. The output is similar to the following:
    
    
       -----BEGIN CERTIFICATE-----
       MIIC8TCCAdmgAwIBAgIRAODQ/dOB39RBs8ZpN0RujIswDQYJKoZIhvcNAQELBQAw
       EjEQMA4GA1UEAxMHcm9vdC1jYTAeFw0yNTAxMDYwNzM3MzVaFw00ODEyMzEwNzM3
       MzVaMBIxEDAOBgNVBAMTB3Jvb3QtY2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
       ggEKAoIBAQC41U4+3M1EAHggUBw5ki97533zTvwHukmZyORwbQ3tlQ4GQDscoCEh
       nn+KCaG767VCaGDcQhq99hl6qa/nBoc1X6WQ3a/uhv5E2ztRD40PB5NFNdSulxTH
       gsitukSmv+DAx15UJnVkJtPP/FzxEWPu0piIiFZakTxT83VUSs54QRmTahxP80FI
       R0xZ0ohsu9jzA2CAyxTccJU0/xE2kDwN8c8kiYYuG+czMdNVdnT4Jm2ToSkzIDux
       Yi9MzNmarVGG/rtW5SlqnUMYzSsxtUYSmMRlCsFDVxkSzfmICmTRw2zmNkFA/3nz
       XneVSIsUHOA2NzvMN4eoLTVRgSFcHlZRAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIB
       hjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTEeB0EQwhc5p++GhwNymsBfN93
       WjANBgkqhkiG9w0BAQsFAAOCAQEAKBqn4AXjUWmhIUOrWQ5cetsmI76Wl+RBeSzU
       HxbqMBH8Dk1oJbGHtmQbu7EmWz1pKYge650s9N83hMgjFZD24t9GiQZ7YY+i+317
       D6HzJ8VIKPnxVtnUIQzCpkRTQoglDlb1f/7+fi2SYJoHdhnRI/3OaVQTnObjbW5T
       mBhsMxFKc0zGa3HIEm9SUH608V60xUPanl23YZ6X7W8nWAJfnzKvH+3q3Fz58u/S
       VR5t/FkbOktVtnU8AfcMKLof6KG2KhE2L7FAC+fp0ZsjV9vE2uqlZ+8mIQHyc3tM
       cbWxOx+SO/XUCenY9C1yrublln9aOEn4/s3aSURPguiSZOfDyQ==
       -----END CERTIFICATE-----
    

### Fetch from the cluster using kubectl

You can fetch trust bundles directly from the GDC cluster using the `kubectl` command-line tool. Use this method if you have direct access to the cluster and its configuration, and you need to fetch either the `trust-store-root-ext` or the `trust-store-global-root-ext` trust bundles.

Make sure you have established initial trust with your organization's specific CAs before performing the steps in this section.

Fetch the trust bundle from the cluster using `kubectl`:

  1. Export the following environment variables:
         
         export KUBECONFIG=MANAGEMENT_API_SERVER_KUBECONFIG
         export STORAGE=STORAGE
         export ZONE=ZONE
         

Replace the following:

     * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the Management API server kubeconfig.
     * `STORAGE`: the directory path where you want to store the trust bundle file.
     * `ZONE`: your GDC zone name.
  2. Set the `TRUST_BUNDLE_FILE` environment variable. This file stores the GDC trust bundle locally in your specified `$STORAGE` location for your GDC `$ZONE`:
         
         export TRUST_BUNDLE_FILE="${STORAGE:?}/${ZONE:?}/ca-bundles/trust-bundle"
         export GLOBAL_TRUST_BUNDLE_FILE="${STORAGE:?}/global/ca-bundles/global-trust-bundle"
         

  3. Set the `NS` namespace environment variable for the namespace:
         
         export NS=platform
         

  4. Create the directories for the trust bundle files:
         
         mkdir -p "$(dirname "${TRUST_BUNDLE_FILE:?}")"
         mkdir -p "$(dirname "${GLOBAL_TRUST_BUNDLE_FILE:?}")"
         

  5. Obtain the certificate authorities (CA) and store them in the files specified by the `TRUST_BUNDLE_FILE` and `GLOBAL_TRUST_BUNDLE_FILE` environment variables:

For `trust-store-root-ext`:
         
         kubectl --kubeconfig ${KUBECONFIG:?} get secret trust-store-root-ext -n ${NS:?} -o go-template='{{ index .data "ca.crt" }}' | base64 -d | sed '$a\' > ${TRUST_BUNDLE_FILE:?}
         

For `trust-store-global-root-ext`:
         
         kubectl --kubeconfig ${KUBECONFIG:?} get secret trust-store-global-root-ext -n ${NS:?} -o go-template='{{ index .data "ca.crt" }}' | base64 -d | sed '$a\' > ${GLOBAL_TRUST_BUNDLE_FILE:?}
         

**Note:** On standard clusters, GDC automatically copies the organization root certificate authority bundle to a `ConfigMap` named `trust-store-root-ext` in tenant workload namespaces. Custom applications and runtimes (such as Python `ssl`) connecting to internal endpoints or to the Kubernetes API server of the standard cluster using the pod's service account certificate (`/var/run/secrets/kubernetes.io/serviceaccount/ca.crt`) might encounter intermediate CA verification errors (`unable to get issuer certificate`). To allow verification against intermediate CAs present in the chain, enable partial chain verification (for example, setting `X509_V_FLAG_PARTIAL_CHAIN` in OpenSSL or `ssl.VERIFY_X509_PARTIAL_CHAIN` in Python).

The fetched trust bundle file contains one or more CA certificates. The output is similar to the following:
         
         -----BEGIN CERTIFICATE-----
         MIIC8TCCAdmgAwIBAgIRAODQ/dOB39RBs8ZpN0RujIswDQYJKoZIhvcNAQELBQAw
         EjEQMA4GA1UEAxMHcm9vdC1jYTAeFw0yNTAxMDYwNzM3MzVaFw00ODEyMzEwNzM3
         MzVaMBIxEDAOBgNVBAMTB3Jvb3QtY2EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
         ggEKAoIBAQC41U4+3M1EAHggUBw5ki97533zTvwHukmZyORwbQ3tlQ4GQDscoCEh
         nn+KCaG767VCaGDcQhq99hl6qa/nBoc1X6WQ3a/uhv5E2ztRD40PB5NFNdSulxTH
         gsitukSmv+DAx15UJnVkJtPP/FzxEWPu0piIiFZakTxT83VUSs54QRmTahxP80FI
         R0xZ0ohsu9jzA2CAyxTccJU0/xE2kDwN8c8kiYYuG+czMdNVdnT4Jm2ToSkzIDux
         Yi9MzNmarVGG/rtW5SlqnUMYzSsxtUYSmMRlCsFDVxkSzfmICmTRw2zmNkFA/3nz
         XneVSIsUHOA2NzvMN4eoLTVRgSFcHlZRAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIB
         hjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTEeB0EQwhc5p++GhwNymsBfN93
         WjANBgkqhkiG9w0BAQsFAAOCAQEAKBqn4AXjUWmhIUOrWQ5cetsmI76Wl+RBeSzU
         HxbqMBH8Dk1oJbGHtmQbu7EmWz1pKYge650s9N83hMgjFZD24t9GiQZ7YY+i+317
         D6HzJ8VIKPnxVtnUIQzCpkRTQoglDlb1f/7+fi2SYJoHdhnRI/3OaVQTnObjbW5T
         mBhsMxFKc0zGa3HIEm9SUH608V60xUPanl23YZ6X7W8nWAJfnzKvH+3q3Fz58u/S
         VR5t/FkbOktVtnU8AfcMKLof6KG2KhE2L7FAC+fp0ZsjV9vE2uqlZ+8mIQHyc3tM
         cbWxOx+SO/XUCenY9C1yrublln9aOEn4/s3aSURPguiSZOfDyQ==
         -----END CERTIFICATE-----
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
