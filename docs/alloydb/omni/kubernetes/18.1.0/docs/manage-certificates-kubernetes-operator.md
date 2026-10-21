---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-certificates-kubernetes-operator/
title: Manage certificates \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:41.303374+00:00
---

# Manage certificates  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-certificates-kubernetes-operator/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)



Send feedback 

#  Manage certificates Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manage-certificates-kubernetes-operator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/manage-certificates-kubernetes-operator)
  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manage-certificates-kubernetes-operator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/manage-certificates-kubernetes-operator)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/manage-certificates-kubernetes-operator)

This page describes how to use custom certificate issuers to manage Transport Layer Security (TLS) certificates on your Kubernetes-based AlloyDB Omni database cluster. 

By default, the AlloyDB Omni Kubernetes operator uses cert-manager to provision a set of TLS certificates for each database cluster. Besides the database server certificate, the operator also creates certificates for control plane components to ensure internal connections are also secure. By default, each certificate is signed by an issuer managed by the operator.

Starting with AlloyDB Omni operator version 1.6.0, if you prefer all certificates, including those for control plane components, to be chained back to your own trusted root CA, you can configure the operator to use an issuer of your choice. This lets you chain all certificates to your own public key infrastructure (PKI), including certificates used for control plane functionality, without exposing the implementation details of each internal entity.

## Before you begin

To configure a certificate issuer, you must first create a [cert-manager issuer](https://cert-manager.io/docs/configuration/) of type `ClusterIssuer` or `Issuer` that is associated with the CA you want to sign your certificates. The AlloyDB Omni operator references this issuer when creating [certificates](https://cert-manager.io/docs/usage/certificate/).

## Configure custom issuers

You can configure custom certificate issuers for the database cluster, the AlloyDB Omni operator, and PgBouncer.

### Database cluster certificates

This feature requires that the relevant database cluster's `controlPlaneAgentsVersion` in its manifest is 1.6.0 or higher.

There are two database cluster spec fields to configure certificate issuers:

  * `spec.primarySpec.dataPlaneCertIssuer`: reference to the cert-manager issuer that provisions data plane certificates. The issuer CA is the one that the database client can trust in order to verify the database during a TLS connection.

  * `spec.primarySpec.controlPlaneAgentsCertIssuer`: reference to the cert-manager issuer that provisions control plane certificates. These certificates are used for internal connections.



    
    
    spec:
      primarySpec:
        tls:
          dataPlaneCertIssuer:
            name: DATA_PLANE_ISSUER_NAME
            kind: DATA_PLANE_ISSUER_KIND
          controlPlaneAgentsCertIssuer:
            name: CONTROL_PLANE_ISSUER_NAME
            kind: CONTROL_PLANE_ISSUER_KIND
    

Replace the following:

  * `DATA_PLANE_ISSUER_NAME`: name of the cert-manager issuer that provisions data plane certificates, such as for the database server.

  * `DATA_PLANE_ISSUER_KIND`: must be either `Issuer` or `ClusterIssuer`.

  * `CONTROL_PLANE_ISSUER_NAME`: name of the cert-manager issuer that provisions control plane certificates for internal components.

  * `CONTROL_PLANE_ISSUER_KIND`: must be either `Issuer` or `ClusterIssuer`.




### Operator certificates

The steps for configuring a cert-manager issuer for operator certificates depend on the method used to install AlloyDB Omni.

#### Configure using Helm

If you install AlloyDB Omni operator version 1.6.0 or later for the first time, use Helm install and set the appropriate values. This assumes that you follow [the installation instructions](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes).
    
    
    helm install alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
    --create-namespace \
    --namespace alloydb-omni-system \
    --set operatorCertIssuer.certManagerIssuerName="OPERATOR_CERT_ISSUER_NAME" \
    --set operatorCertIssuer.certManagerIssuerKind="OPERATOR_CERT_ISSUER_KIND" \
    --atomic \
    --timeout 5m
    

If you already have the operator installed and need to set the certificate issuer, use `helm upgrade` to set the appropriate values:
    
    
    helm upgrade alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
    --create-namespace \
    --namespace alloydb-omni-system \
    --set operatorCertIssuer.certManagerIssuerName="OPERATOR_CERT_ISSUER_NAME" \
    --set operatorCertIssuer.certManagerIssuerKind="OPERATOR_CERT_ISSUER_KIND" \
    --atomic \
    --timeout 5m
    

Replace the following:

  * `OPERATOR_CERT_ISSUER_NAME`: name of the cert-manager issuer that provisions the operator certificate, which is used for internal connections.

  * `OPERATOR_CERT_ISSUER_KIND`: must be either `Issuer` or `ClusterIssuer`.




#### Configure using Operator Lifecycle Manager

If you used Operator Lifecycle Manager (OLM) to install the AlloyDB Omni operator, you can modify the Subscription resource `spec.config.env` field to set the `CERT_MANAGER_ISSUER_NAME` and `CERT_MANAGER_ISSUER_KIND` environment variables of the operator Deployment.
    
    
    spec:
      config:
        env:
        - name: CERT_MANAGER_ISSUER_NAME
          value: OPERATOR_CERT_ISSUER_NAME
        - name: CERT_MANAGER_ISSUER_KIND
          value: OPERATOR_CERT_ISSUER_KIND
    

Replace the following:

  * `OPERATOR_CERT_ISSUER_NAME`: name of the cert-manager issuer that provisions the operator certificate, which is used for internal connections.

  * `OPERATOR_CERT_ISSUER_KIND`: must be either `Issuer` or `ClusterIssuer`.




### PgBouncer certificates

To support custom issuers, the PgBouncer controller checks the DBCluster `spec.primarySpec.tls.dataPlaneCertIssuer` field and uses that to provision the PgBouncer certificate. The PgBouncer controller also uses the attributes configured in `spec.primarySpec.tls.dataPlaneCertRequest` to provision the PgBouncer certificate. This helps ensure that PgBouncer uses a certificate from the same CA that has the same attributes as the database.

## Configure custom certificate attributes

You can customize the attributes of the Transport Layer Security (TLS) certificates generated by the operator, such as the certificate duration, renewal window, subject alternative names (SANs), common name, and private key configuration.

You configure custom certificate attributes in your `DBCluster` manifest:

  * `spec.primarySpec.tls.dataPlaneCertRequest`: specifies attributes for data plane certificates (including pgBackrest server, PgBouncer auth query, and the database server certificates).
  * `spec.primarySpec.tls.controlPlaneAgentsCertRequest`: specifies attributes for provisioning control plane certificates. These certificates are used for internal connections.



### Configure certificate requests

Specify the request properties in the following format:
    
    
    spec:
      primarySpec:
        tls:
          dataPlaneCertRequest:
            commonName: DATABASE_COMMON_NAME
            dnsNames:
            - DATABASE_DNS_NAME_1
            - DATABASE_DNS_NAME_2
            duration: DATA_PLANE_DURATION
            renewBefore: DATA_PLANE_RENEW_BEFORE
            privateKey:
              algorithm: DATA_PLANE_ALGORITHM
              size: DATA_PLANE_KEY_SIZE
              rotationPolicy: DATA_PLANE_ROTATION_POLICY
          controlPlaneAgentsCertRequest:
            duration: CONTROL_PLANE_DURATION
            renewBefore: CONTROL_PLANE_RENEW_BEFORE
            privateKey:
              algorithm: CONTROL_PLANE_ALGORITHM
              size: CONTROL_PLANE_KEY_SIZE
              rotationPolicy: CONTROL_PLANE_ROTATION_POLICY
    

Replace the following:

  * `DATABASE_COMMON_NAME`: (Optional, data plane only) the common name of the database certificate.
  * `DATABASE_DNS_NAME_1`, `DATABASE_DNS_NAME_2`: (Optional, data plane only) list of subject alternative names (SANs) for the database certificate.
  * `DATA_PLANE_DURATION` and `CONTROL_PLANE_DURATION`: the total lifespan of the certificate as a string duration (for example, `720h0m0s` for 30 days).
  * `DATA_PLANE_RENEW_BEFORE` and `CONTROL_PLANE_RENEW_BEFORE`: the duration before expiration that cert-manager must start a renewal attempt (for example, `120h0m0s` for 5 days).
  * `DATA_PLANE_ALGORITHM` and `CONTROL_PLANE_ALGORITHM`: the private key algorithm. Valid values are `RSA`, `ECDSA`, or `Ed25519`.
  * `DATA_PLANE_KEY_SIZE` and `CONTROL_PLANE_KEY_SIZE`: the private key size in bits. If the algorithm is `RSA`, valid values are `4096` or `8192` (default is `4096`). If the algorithm is `ECDSA`, valid values are `384` or `521` (default is `384`). If the algorithm is `Ed25519`, size is ignored.
  * `DATA_PLANE_ROTATION_POLICY` and `CONTROL_PLANE_ROTATION_POLICY`: controls private key regeneration. Valid values are `Always` or `Never`.



### Operator and backup client certificates

To customize certificate attributes for the operator and the backup client (which are shared across all instances in a namespace and aren't managed by a database cluster specification), modify the `Certificate` custom resources. The operator retains these manual modifications.

## Verify

To verify that the operator Deployment is healthy and that the environment variables `CERT_MANAGER_ISSUER_NAME` and `CERT_MANAGER_ISSUER_KIND` are set, run the following command:
    
    
    kubectl get deployments local-controller-manager -n alloydb-omni-system -o yaml
    

To verify that the correct issuer is used, inspect the Certificate objects as follows:
    
    
    kubectl get certificate -n NAMESPACE
    

Check the `issuerRef` field in the output for each certificate to confirm that it matches your custom issuer.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
