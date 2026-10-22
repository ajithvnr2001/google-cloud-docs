---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/rotate-root-ca/
title: Rotate the root CA certificate \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:31.324227+00:00
---

# Rotate the root CA certificate  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/rotate-root-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Rotate the root CA certificate Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/rotate-root-ca.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/rotate-root-ca.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/rotate-root-ca.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/rotate-root-ca.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/rotate-root-ca.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/rotate-root-ca.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/rotate-root-ca.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/rotate-root-ca.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/rotate-root-ca.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/rotate-root-ca.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/rotate-root-ca.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/rotate-root-ca.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/rotate-root-ca.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/rotate-root-ca.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/rotate-root-ca.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/rotate-root-ca.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/rotate-root-ca.html)



This page explains the Apigee hybrid root certificate authority (CA) certificate that signs the internal certificates hybrid components use to communicate with each other, and describes how you rotate it before it expires. Starting in Apigee hybrid v1.17, you can rotate this root CA yourself. 

**Summary:** Unlike Apigee, where Google runs the root CA rotation for you, Apigee hybrid rotation is **customer-driven** : you set a phase in your overrides file and run `helm upgrade` on the Apigee operator chart (`apigee-operator`), once per phase, in each region. This root CA is **not** the ingress TLS certificate that you supply for your environment groups — see About the root CA certificate. 

## About the root CA certificate

Every Apigee hybrid installation has a single root CA, stored as a cert-manager `Certificate` named `apigee-ca` in the `cert-manager` namespace. It is a self-signed CA (`isCA: true`, common name `apigee-hybrid`) that acts as the trust root for the internal certificates hybrid issues — both the mutual TLS (mTLS) between components and the one-way (server-side) TLS that secures admission webhooks and custom resource conversion. If this CA expires, internal communication between hybrid components breaks. 

**Important:** The root CA described on this page is used only for internal hybrid traffic. It is **not** the same as the TLS certificate you provide for the [Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/managing-ingress), which terminates client traffic for your environment groups and is configured separately through `virtualhosts` in your overrides file (see [Configuring TLS and mTLS on the ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/ingress-tls)). Rotating the root CA does not touch your ingress certificate, and rotating your ingress certificate does not rotate this root CA. 

## Why the root CA certificate is rotated

The root CA that the hybrid chart generates has a validity period of **10 years**. It must be rotated before it expires so that the internal certificates it signs can continue to be renewed and inter-component communication is never interrupted. Rotation is designed to be zero-downtime: during the transition your components trust both the old and the new root CA, so certificates signed by either one remain valid until the old CA is removed. 

**Note:** The 10-year lifetime applies to the CA that the chart generates. If you bring your own CA, its lifetime is whatever your certificate carries. 

## How the rotation works

You rotate the root CA by advancing your cluster through four phases, in order. You move to the next phase only after the current phase has completed on every component. Each phase is driven by a single overrides field, `certRotation.phase`, applied with a `helm upgrade` of the Apigee operator chart (`apigee-operator`). 

Phase (`certRotation.phase`) | What happens | Rollback possible  
---|---|---  
**1.`CREATE_NEW_CA`** | A new root CA (`apigee-ca-2`) is created and added to the truststore of every hybrid component. Components still present certificates signed by the old CA, so nothing has switched yet. | Yes  
**2.`CREATE_NEW_LEAF`** | New leaf certificates signed by the new root CA are issued. Both the old and new root CAs are trusted, so traffic continues uninterrupted. | Yes  
**3.`HIDE_OLD_CA`** | The old root CA is removed from the active trust configuration. Only the new root CA remains in use. Roll back is still available at this phase. | Yes  
**4.`CLEANUP`** | The old root CA and its issuers are removed and the new root CA is promoted to be the cluster's root CA. This phase is **irreversible**. | **No**  
  
## Before you begin

  * Install the `kubectl` and `helm` command-line tools, and make sure your `kubectl` context points at the cluster you are rotating.
  * Make sure the cluster is healthy. Each `helm upgrade` validates that every `ApigeeDeployment` is in the `running` state and that the phase you request is the current phase, the next phase, or the rollback phase. If the cluster is unhealthy or you try to skip a phase, the upgrade is rejected.
  * If you run a multi-region deployment, read that section before you start — every region must converge on the same new root CA.



## Rotate the root CA

Perform the following steps for each phase listed in How the rotation works, in order: apply the phase, then confirm it has completed before moving to the next one. In a multi-region deployment, perform them in each region. 

### Step 1: Set the phase and apply it

Add or update the `certRotation` stanza in your overrides file, setting `phase` to the phase you are applying. For example, to start the rotation:
    
    
    certRotation:
      phase: CREATE_NEW_CA
    

Test the change with a dry run first:
    
    
    helm upgrade operator apigee-operator/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f OVERRIDES_FILE.yaml \
      --dry-run=server
    

Then apply the change:
    
    
    helm upgrade operator apigee-operator/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

### Step 2: Confirm the phase has completed

The cluster records rotation progress in the `cert-info` ConfigMap in the hybrid namespace. Read its `currentPhase` value: 
    
    
    kubectl get configmap cert-info -n APIGEE_NAMESPACE \
      -o jsonpath='{.data.currentPhase}'
    

A phase is complete only when `currentPhase` equals the phase you just applied. `currentPhase` advances only after every component has reconciled to the requested phase, so do not proceed until it matches. 

**Note:** If `currentPhase` does not advance after several minutes, check the logs of the `apigee-controller-manager` pod in the hybrid namespace for reconciliation errors. **Warning:** Do not use the `apigee.cloud.google.com/cr-phase` annotation on the `apigee-controller-manager` deployment as your completion signal. That annotation records the _desired_ phase and changes the instant you run `helm upgrade`, before your components have reconciled. Using it to decide when to advance will tell you to proceed too early. Always read `currentPhase` from the `cert-info` ConfigMap instead. 

When `currentPhase` matches, read the next phase to apply from the same ConfigMap: 
    
    
    kubectl get configmap cert-info -n APIGEE_NAMESPACE \
      -o jsonpath='{.data.readyForNextPhase}'
    

Set `certRotation.phase` to that value and repeat Step 1 and Step 2. Continue until you have completed the `CLEANUP` phase. 

**Warning:** The `CLEANUP` phase is irreversible. After `CLEANUP` completes, the old root CA and its issuers are gone and the rotation cannot be undone. Before you apply `CLEANUP`, confirm that every region has completed `HIDE_OLD_CA` and that your APIs are serving normally. You can roll back from any earlier phase, but not from `CLEANUP`. **Note:** After `CLEANUP` completes in every region, the rotation is finished. Remove the `certRotation` stanza from your overrides file to keep your configuration tidy for future upgrades. Do not remove or change the `certRotation` stanza while a rotation is still in progress. If you do leave the stanza in place after the rotation finishes, re-applying `phase: CLEANUP` during a later, unrelated `helm upgrade` is a no-op (has no effect) and does not repeat the cleanup, because each `helm upgrade` accepts only the current, next, or rollback phase. 

## Multi-region deployments

In a multi-region deployment, every cluster has its own `cert-info` ConfigMap, its own operator, and its own truststores, and all regions must end up trusting the **same** new root CA. The chart generates a new root CA only when the `apigee-ca-2` secret does not already exist, so you create the new CA once in a primary region and copy it to the other regions before you rotate them. 

Perform the rotation in the following order. Confirm `currentPhase` in a region (see Step 2: Confirm the phase has completed) before you move that region on to the next phase. 

  1. Run `CREATE_NEW_CA` in your **primary region**. The chart mints the new root CA and stores it in the `apigee-ca-2` secret.
  2. Copy the `apigee-ca-2` secret from the primary region's `cert-manager` namespace into the `cert-manager` namespace of every other region, **before** you run `CREATE_NEW_CA` in those regions. This is the same secret-copy pattern you use when you expand to a new region; see [Multi-region deployments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/multi-region).
  3. Run `CREATE_NEW_CA` in each of the other regions, one region at a time. Because the `apigee-ca-2` secret is already present, the chart skips minting a new CA and binds the region to the shared one.
  4. Run `CREATE_NEW_LEAF` in each region.
  5. Run `HIDE_OLD_CA` in each region.
  6. Run `CLEANUP` in each region.
  7. Remove the `certRotation` stanza from each region's overrides file to tidy up your configuration.



Through `CREATE_NEW_CA`, `CREATE_NEW_LEAF`, and `HIDE_OLD_CA`, every region trusts both the old and the new root CA, so regions can be at different phases during this period without interrupting traffic between them. 

**Warning:** `CLEANUP` is the exception, because it removes the old root CA. Do not run `CLEANUP` in any region until every region has completed `HIDE_OLD_CA`. If one region runs `CLEANUP` while another region still presents leaf certificates signed by the old CA, the cleaned-up region no longer trusts that traffic, which causes immediate communication failures and TLS handshake errors between the regions. 

## Bring your own CA

If you want to use your own root CA instead of one generated by the chart, pre-create the new CA secret before you start the rotation. Because the chart generates a CA only when the target secret is absent, an existing secret is used as-is. 

Root CA names are not free-form. hybrid expects each generation of the CA at a fixed name — `apigee-ca`, then `apigee-ca-2`, `apigee-ca-3`, and so on — and the chart looks for the next CA at exactly that name. When you bring your own CA, you must create the secret under the exact next name (`apigee-ca-2` for the first rotation); the chart does not detect a CA created under any other name. To find the current secret name and the next name to use, list the CA certificates and the secrets that back them: 
    
    
    kubectl get certificate -n cert-manager \
      -o custom-columns=CERTIFICATE:.metadata.name,SECRET:.spec.secretName
    

See Track root CA expiry for more ways to inspect which generation your cluster is on. 

  1. Before you run `CREATE_NEW_CA`, create a secret with the next CA name (`apigee-ca-2` for the first rotation) in the `cert-manager` namespace, holding your CA certificate and private key. The secret must be of type `kubernetes.io/tls` and contain three keys: `tls.crt`, `tls.key`, and `ca.crt`. Because `kubectl create secret tls` cannot set the `ca.crt` key, use the generic form: 
         
         kubectl create secret generic apigee-ca-2 \
           --namespace cert-manager \
           --type=kubernetes.io/tls \
           --from-file=tls.crt=CERT_FILE \
           --from-file=tls.key=KEY_FILE \
           --from-file=ca.crt=CA_FILE
         

  2. Run the rotation as described in Rotate the root CA. During `CREATE_NEW_CA`, the chart detects your `apigee-ca-2` secret, skips generating a CA, and binds the new issuer (`apigee-ca-issuer-2`) to your CA. Every other phase is unchanged.



When you bring your own CA, its lifetime is whatever your certificate carries, not the chart's 10-year default. 

## Roll back a rotation

Every phase before `CLEANUP` can be rolled back. To roll back, set `certRotation.phase` to the value the cluster reports as the rollback target and apply it with `helm upgrade`, exactly as you apply a forward phase. 

Read the rollback target from the `cert-info` ConfigMap:
    
    
    kubectl get configmap cert-info -n APIGEE_NAMESPACE \
      -o jsonpath='{.data.readyForRollbackPhase}'
    

The forward and rollback targets for each phase are:

Current phase | Next phase | Rollback phase  
---|---|---  
`PHASE_UNSPECIFIED` (not started) | `CREATE_NEW_CA` | `PHASE_UNSPECIFIED`  
`CREATE_NEW_CA` | `CREATE_NEW_LEAF` | `PHASE_UNSPECIFIED`  
`CREATE_NEW_LEAF` | `HIDE_OLD_CA` | `CREATE_NEW_CA`  
`HIDE_OLD_CA` | `CLEANUP` | `CREATE_NEW_LEAF`  
`CLEANUP` | — (rotation complete) | — (none; irreversible)  
**Note:** `PHASE_UNSPECIFIED` is the state of a cluster that has never started a rotation; a fresh installation begins here. It is also the rollback target for the first phase. **Warning:** `CLEANUP` has no rollback target. Once it completes, the old root CA is permanently removed. Make sure the rotation is healthy in every region before you apply `CLEANUP`. 

## Track root CA expiry

Because Apigee hybrid rotation is customer-driven, you are responsible for rotating the root CA before it expires. Track the expiry of the `apigee-ca` certificate and plan the rotation ahead of that date so that you have time to complete all four phases in every region. 

To check when the root CA expires, list the CA certificates in the `cert-manager` namespace, then read the expiry date of the generation you are currently using: 
    
    
    kubectl get certificate -n cert-manager
    
    
    
    kubectl get certificate apigee-ca -n cert-manager \
      -o jsonpath='{.status.notAfter}'
    

The first command lists each generation of the root CA (`apigee-ca`, `apigee-ca-2`, and so on). The second prints the expiry date of the named certificate; run it against the generation currently in use. 

Apigee hybrid [Automated issue surfacing](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/automated-issue-surfacing) reports cluster problems it detects as `ApigeeIssue` resources, which you can list with `kubectl get apigeeissues`. Check for surfaced issues as part of your regular monitoring. 

## What's next

  * Review [Multi-region deployments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/multi-region) for how certificates and secrets are shared across regions.
  * Review [Configuring TLS and mTLS on the ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/ingress-tls) to understand the separate, customer-supplied ingress certificate.
  * Review [Automated issue surfacing](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/automated-issue-surfacing) to monitor your cluster for detected issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
