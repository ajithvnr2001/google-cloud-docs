---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/upgrade-package-validation-cert/
title: Upgrade package validation certificate \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:41.336375+00:00
---

# Upgrade package validation certificate  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/upgrade-package-validation-cert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Upgrade package validation certificate Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to upgrade the root certificate authority (CA) used for package validation in Google Distributed Cloud (GDC) air-gapped appliance

GDC package validation uses a root certificate authority (CA) to validate release key certificates. You must upgrade this root CA if a release notice requires it, or if you see a warning message during a system upgrade.

## Before you begin

To upgrade the package validation certificate, you must have the necessary identity and access roles:

  * Ensure that you have write access to `harbor-system/package-validation-root-certs` ConfigMap.
  * Ask your Security Admin to grant you the Upgrade Debugger (`upgrade-debugger-cp`) role.



## Verify certificate upgrade is required

Verify a package validation certificate upgrade is required before performing the operation, by comparing the active ConfigMap in your cluster against the latest staging root certificate in the upgrade bundle:

  1. Set the `KUBECONFIG` environment variable:
         
         $ KUBECONFIG=PATH_TO_KUBECONFIG_FILE
         

Replace `PATH_TO_KUBECONFIG_FILE` with the path to the [`kubeconfig` file that you obtained](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth) by running `gdcloud auth login` in the root admin cluster.

  2. Determine if an upgrade is required by comparing the current trust anchor to the latest trust anchor. The `ConfigMap` data at `harbor-system/package-validation-root-certs` is compared against the local trust anchor:
         
         $ CURRENT_TRUST_ANCHOR=$(kubectl  --kubeconfig=$KUBECONFIG get cm package-validation-root-certs -n harbor-system -o jsonpath='{.data.ca\.crt}')
         
         $ LATEST_TRUST_ANCHOR=$(cat /root/release/staging_root_ca_certificate.crt)
         
         $ diff <( echo "$CURRENT_TRUST_ANCHOR" ) <( echo "$LATEST_TRUST_ANCHOR" ) && echo trust anchors are same  || echo trust anchors are different, upgrade required!
         




## Upgrade the certificate

If an upgrade is required, update the `ConfigMap` object located at `harbor-system/package-validation-root-certs` in the root admin cluster. You must have write access to the `ConfigMap` to complete this task.

  1. Set the `KUBECONFIG` environment variable:
         
         $ KUBECONFIG=PATH_TO_KUBECONFIG_FILE
         

Replace `PATH_TO_KUBECONFIG_FILE` with the path to the [`kubeconfig` file that you obtained](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth) by running `gdcloud auth login` in the root admin cluster.

  2. Create and assign values to the following variables:
         
         USERNAME=USER_NAME #IO
         TARGET_FOLDER=/tmp/${USERNAME}
         OUTPUT="${TARGET_FOLDER}/package-validation-root-certs.yaml"
         LATEST_TRUST_ANCHOR_CA_FILE=/root/release/staging_root_ca_certificate.crt
         CONFIGMAP_NAME=package-validation-root-certs
         NAMESPACE=harbor-system
         

Replace `USER_NAME` with the IO username.

  3. Create the target folder that will contain the output files from the certificate upgrade process:
         
         mkdir -p "${TARGET_FOLDER}"
         

  4. Get the current trust anchor and store it in local temporary file:
         
         CURRENT_TRUST_ANCHOR=$(kubectl  --kubeconfig=$KUBECONFIG get configmap "${CONFIGMAP_NAME}" -n "${NAMESPACE}" -o jsonpath="{.data.ca\.crt}" )
         CURRENT_TRUST_ANCHOR_CA_FILE=$(mktemp)
         echo "$CURRENT_TRUST_ANCHOR" > "${CURRENT_TRUST_ANCHOR_CA_FILE}"
         

  5. Generate the updated trust anchor file:
         
         cat <<EOF  > "${OUTPUT}"
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: ${CONFIGMAP_NAME}
           namespace: ${NAMESPACE}
         data:
           ca.crt: |
         $(sed 's/^/    /' "${LATEST_TRUST_ANCHOR_CA_FILE}")
         $(sed 's/^/    /' "${CURRENT_TRUST_ANCHOR_CA_FILE}")
         EOF
         

  6. Verify the trust anchor was updated correctly:

The trust anchor must contain both current and latest trust anchor certificate.
         
         $ cat "${OUTPUT}"
         apiVersion: v1
         data:
           ca.crt: |
             -----BEGIN CERTIFICATE-----
             (certificate content)
             -----END CERTIFICATE-----
             -----BEGIN CERTIFICATE-----
             (certificate content)
             -----END CERTIFICATE-----
             (other certificate)
         kind: ConfigMap
         metadata:
           name: package-validation-root-certs
           namespace: harbor-system
         

  7. Apply the new configuration with `kubectl`:
         
         kubectl --kubeconfig=$KUBECONFIG apply -f ${OUTPUT}
         

  8. Ensure that the newly applied ca.crt is present within the `ConfigMap`:
         
         kubectl --kubeconfig=$KUBECONFIG describe configmap package-validation-root-certs -n harbor-system
         




This takes care of upgrading a new certificate in the `package-validation-root-cert`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
