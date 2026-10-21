---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/import-additional-ca/
title: Add custom CAs to the system trust bundle \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:42.436607+00:00
---

# Add custom CAs to the system trust bundle  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/import-additional-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Add custom CAs to the system trust bundle Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to add custom certificate authority (CA) certificates to the system trust bundle within Google Distributed Cloud (GDC) air-gapped. A trust bundle is a collection of trusted CAs that your organization's services use to verify the identity of other services. By adding your own custom CAs, you can control which certificates your organization trusts, enabling secure connections to your internal resources and other trusted endpoints.

This page covers how to add custom CAs to the `trust-store-root-ext` system trust bundle. When you modify the `trust-store-root-ext` trust bundle, the changes automatically propagate to the `trust-store-global-root-ext` bundle, making your custom CAs available across all zones.

This page is for audiences within the platform administrator group (such as IT admins) who need to manage and secure their organization's resources within GDC. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To add custom CA certificates to the system trust bundle, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, read, update, and delete secrets, contact your Organization IAM Admin to request the **Trust Store Admin** (`trust-store-admin`) role.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) to the gdcloud CLI.




### Generate a kubeconfig file

Complete the following steps to generate your kubeconfig file for the org infrastructure cluster and set it as the `KUBECONFIG` variable to use later.

  1. View all available zones:
         
         gdcloud zones list
         

Note the name of the zone that hosts your custom resource.

  2. Set the `ZONE` environment variable to the zone that hosts the org infrastructure cluster:
         
         export ZONE="ZONE"
         

Replace `ZONE` with the zone name.

  3. Set the `ORG_INFRA_CLUSTER` environment variable:
         
         export ORG_INFRA_CLUSTER="ORG_NAME-infra"
         

Replace `ORG_NAME` with the name of your organization, such as `org-1`.

  4. Generate the org infrastructure cluster kubeconfig file for the targeted zone, and validate the credentials:
         
         export KUBECONFIG=${HOME}/${ORG_INFRA_CLUSTER:?}-kubeconfig.yaml
         rm ${KUBECONFIG:?}
         gdcloud clusters get-credentials ${ORG_INFRA_CLUSTER:?} --zone ${ZONE:?}
         [[ $(kubectl config current-context) == *${ORG_INFRA_CLUSTER:?}* ]] && echo "Success. Your kubeconfig is at $KUBECONFIG" || echo "Failure"
         

The command `rm ${KUBECONFIG:?}` removes the existing kubeconfig file in the home directory. When you generate a new kubeconfig file, it overwrites the existing one. If you don't want to overwrite or remove the existing file, back it up in another safe location.




## Add custom CAs to the system trust bundle

To add custom CAs to the `trust-store-root-ext` system trust bundle, you need to prepare your custom CA resource and then apply it to the org infrastructure cluster.

  1. Set the environment variable for your custom CA PEM file:
         
         export CUSTOM_CA_PEM_FILE=CUSTOM_CA_PEM_FILE
         

Replace `CUSTOM_CA_PEM_FILE` with the path to the file containing your custom CA certificates, encoded in PEM format.

**Note:** If you want to update the list of custom CAs, modify the contents of the target `CUSTOM_CA_PEM_FILE` directly and repeat the steps in this section.
  2. Encode the CA certificates using base64:
         
         export ENCODED_CA=$(cat "${CUSTOM_CA_PEM_FILE:?}" | base64 -w 0)
         

  3. Create the secret YAML file (`custom-ca.yaml`) that targets the `trust-store-root-ext` system trust bundle:
         
         cat > custom-ca.yaml <<EOF
         apiVersion: v1
         kind: Secret
         metadata:
           annotations:
             security.private.gdc.goog/bundles: trust-store-root-ext
           name: custom-ca
           namespace: cert-manager
         data:
           ca.crt: ${ENCODED_CA:?}
         EOF
         

The following is an example of a `custom-ca.yaml` file:
         
         apiVersion: v1
         kind: Secret
         metadata:
           annotations:
             security.private.gdc.goog/bundles: trust-store-root-ext
           name: custom-ca
           namespace: cert-manager
         data:
            ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSU...LQWZRSUE9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
         

  4. Apply the secret to the org infrastructure cluster using the `kubectl` command:
         
         kubectl apply -f custom-ca.yaml --kubeconfig ${KUBECONFIG:?}
         

This step makes your custom CAs available to GDC services by automatically updating the `trust-store-root-ext` and `trust-store-global-root-ext` trust bundles.




## Verify that the CAs are available

Confirm that your custom CAs were added to the trust bundle:

  1. Download the latest version of the `trust-store-root-ext` trust bundle by following the steps in [Fetch GDC trust bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/fetch-trust-bundles).

If you want to fetch the custom CAs from a different zone, use the `trust-store-global-root-ext` trust bundle.

  2. Open the downloaded trust bundle file and confirm that each custom CA certificate specified by `CUSTOM_CA_PEM_FILE` is present.

Search for each custom CA certificate individually. The order in which they appear can vary; they're not guaranteed to appear at the end of the list.

The following shows an example of `trust-store-root-ext`:
         
         -----BEGIN CERTIFICATE-----
         MIIC8DCCAdigAwIBAgIQPLOPa...
         -----END CERTIFICATE-----
         ... other CAs ...
         -----BEGIN CERTIFICATE-----
            < Imported CA data>
         -----END CERTIFICATE-----
         ... other CAs ...
         -----BEGIN CERTIFICATE-----
         MIIDAzCCAeugAwIBAgIRAIV2...
         -----END CERTIFICATE-----
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
