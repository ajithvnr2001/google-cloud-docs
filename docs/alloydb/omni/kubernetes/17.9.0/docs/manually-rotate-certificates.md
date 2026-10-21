---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manually-rotate-certificates/
title: Manually rotate certificates \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:12.033282+00:00
---

# Manually rotate certificates  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manually-rotate-certificates/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Manually rotate certificates Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manually-rotate-certificates)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/manually-rotate-certificates)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/manually-rotate-certificates)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manually-rotate-certificates)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/manually-rotate-certificates)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manually-rotate-certificates)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manually-rotate-certificates)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/manually-rotate-certificates)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/manually-rotate-certificates)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/manually-rotate-certificates)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/manually-rotate-certificates)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/manually-rotate-certificates)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/manually-rotate-certificates)

By default, the AlloyDB Omni Kubernetes operator uses `cert-manager` to provision a set of TLS certificates for each database cluster. In addition to the database server certificate, the operator creates certificates for control plane components to secure internal connections. 

While `cert-manager` automates certificate renewals based on the `duration` and `renewBefore` fields of a `Certificate` object, you might need to manually trigger a certificate rotation in the following scenarios:

  * A private key is compromised.
  * A CA certificate is rotated. According to `cert-manager` documentation, when a CA certificate associated with an issuer is rotated, the leaf certificates aren't automatically re-issued.
  * `cert-manager` automatic re-issuance fails. Although rare, if automatic re-issuance doesn't trigger due to specific conditions described in the [cert-manager FAQ](https://cert-manager.io/docs/faq/#when-do-certs-get-re-issued), you must trigger a manual rotation.



## Before you begin

  * Ensure you have `kubectl` configured to access your Kubernetes cluster.
  * Ensure that `cert-manager` is running on your Kubernetes cluster.



## Manual certificate rotation

To manually trigger certificate rotation, delete the secret associated with the `cert-manager` `Certificate` object. The `cert-manager` controller reconciles the object and re-issues the certificate, which creates a new secret. Workloads associated with the AlloyDB Omni operator automatically reload their TLS configurations to use the new certificate.

  1. Identify the `cert-manager` `Certificate` that you want to rotate. These objects are in your `DBCluster` namespace and the namespace where the AlloyDB Omni operator is installed. The names of CA certificates have the prefix `dbs-al-ca`, while leaf certificates have the prefix `dbs-al-cert`. In the remaining steps, use the name of the associated secret from the output.
         
         kubectl get certificate CERTIFICATE_NAME -n NAMESPACE -o wide
         

  2. Before you trigger rotation, back up the certificate secret:
         
         kubectl get secret SECRET_NAME -n NAMESPACE -o yaml > SECRET_NAME-NAMESPACE.yaml.bak
         

  3. Delete the certificate secret:
         
         kubectl delete secret SECRET_NAME -n NAMESPACE
         

  4. Wait for `cert-manager` to recreate the certificate secret:
         
         kubectl get secret SECRET_NAME -n NAMESPACE -w
         




## Verify certificate rotation

After you manually rotate the certificates, verify that the new certificates are in use:

  1. Check the certificate secret. The `creationTimestamp` value must reflect the time after you manually rotated the certificate:
         
         kubectl get secret SECRET_NAME -n NAMESPACE -o yaml
         

  2. Examine the `Certificate` status. Verify that the `notBefore` and `notAfter` dates in the status section are correct:
         
         kubectl describe certificate CERTIFICATE_NAME -n NAMESPACE
         




## What's next

  * [Manage certificates](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage-certificates-kubernetes-operator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
