---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_dbcluster_cert_issuers.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_dbcluster_cert_issuers.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:18:47.967116+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_dbcluster_cert_issuers.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_dbcluster_cert_issuers.yaml.txt

# This is a minimal DBCluster spec. See v1_dbcluster_full.yaml for more configurations. apiVersion: v1 kind: Secret metadata: name: db-pw-dbcluster-sample type: Opaque data: dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123 \--- apiVersion: alloydbomni.dbadmin.goog/v1 kind: DBCluster metadata: name: dbcluster-sample spec: databaseVersion: "18.3.0" primarySpec: tls: dataPlaneCertIssuer: name: data-plane-issuer kind: ClusterIssuer controlPlaneAgentsCertIssuer: name: control-plane-issuer kind: ClusterIssuer dataPlaneCertRequest: commonName: database.dbcluster-sample.com dnsNames: \- database.dbcluster-sample.com \- database-alt.dbcluster-sample.com duration: 240h0m0s renewBefore: 120h0m0s privateKey: rotationPolicy: Always algorithm: RSA size: 8192 controlPlaneAgentsCertRequest: duration: 240h0m0s renewBefore: 120h0m0s privateKey: rotationPolicy: Always algorithm: RSA size: 8192 adminUser: passwordRef: name: db-pw-dbcluster-sample resources: memory: 5Gi cpu: 1 disks: \- name: DataDisk size: 10Gi 
