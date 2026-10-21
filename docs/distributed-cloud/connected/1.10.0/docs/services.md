---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/services/
title: Manage Google services \u00a0|\u00a0 Google Distributed Cloud connected, version 1.10.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:37.504823+00:00
---

# Manage Google services  |  Google Distributed Cloud connected, version 1.10.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/services/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/overview)



Send feedback 

#  Manage Google services Stay organized with collections  Save and categorize content based on your preferences. 

Distributed Cloud connected supports the deployment of a number of Google Cloud services. These service workloads run in Kubernetes containers on your Distributed Cloud connected clusters.

## Supported Google Cloud services

Distributed Cloud connected supports the deployment of the following Google Cloud services:

Service type | Included in GDC connected costs | Billed separately  
---|---|---  
**Compute** | [Software-only Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)  
[VM Runtime on Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/overview) | Guest operating systems  
(you must obtain your own licenses)  
**Storage** | Raw (persistent volume) storage  
[Container Storage Interface (CSI)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-csi-driver)  
Hybrid storage | Software Defined Storage (SDS),  
such as [Symcloud Storage](https://docs.cloud.google.com/distributed-cloud/connected/docs/storage)  
(you must obtain your own licenses)  
**Networking** | [Edge Network API](https://docs.cloud.google.com/distributed-cloud/connected/docs/networking)  
VLAN support  
GKE Custom Network Interface (CNI) plugins  
GKE bundled L4 load balancer  
| Not applicable  
**AI/ML** | Deploying AutoML models in containers | Not applicable  
**Database** | None | [AlloyDB Omni](https://cloud.google.com/alloydb/omni) (preview)  
Third-party database solutions, such as MongoDB  
(you must obtain your own licenses)  
**Observability** | [Cloud Logging](https://docs.cloud.google.com/logging)  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring)  
[Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest) [GDCc logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/docs/pricing#logs) | [Prometheus](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/logs-metrics#collect_metrics_with_prometheus) for disconnected observability  
Application-level custom logs and metrics  
**Configuration Management** | [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)  
[Fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages) (preview) | Not applicable  
**Management** | Google Kubernetes Engine dashboard in the Google Cloud console  
[Connect Gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using)  
The `kubectl` local tool  
[Distributed Cloud connected software upgrades](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/availability#cluster-maintenance) | Not applicable  
**Security** | [Cloud Key Management Service integration](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/security#cmek)  
Self-Encrypting Disk (SED) drives  
[Fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure)  
[Audit logging](https://docs.cloud.google.com/distributed-cloud/connected/docs/audit-logging) | Not applicable  
  
## Prerequisites

Before you can deploy Google Cloud services on Distributed Cloud connected, you must complete the prerequisites listed in this section.

### Obtain cluster credentials

Use the following command to obtain the credentials for accessing the target cluster:
    
    
     gcloud container hub memberships get-credentials CLUSTER_ID \
           --project="PROJECT_ID"
    

Replace the following:

  * `CLUSTER_ID`: the name of the target cluster.
  * `PROJECT_ID`: the ID of the target Google Cloud project.



### Create or select a cluster

If you have not already done so, create a Distributed Cloud connected cluster as described in [Create a cluster](https://docs.cloud.google.com/distributed-cloud/connected/docs/clusters#create). When creating the cluster, specify at least 8 virtual IP addresses (VIPs). These VIPs will be used by the Kubernetes containers running your Google Cloud service workloads.

If you are using an existing cluster, use the following command to verify that enough VIPs are available on that cluster:
    
    
     kubectl get cluster --all-namespaces -o jsonpath="{.items[0].spec.loadBalancer.addressPools}"
    

The command returns output similar to the following:
    
    
    [
      {
        "addresses": [
          "10.200.11.188-10.200.11.196"
        ],
        "name": "loadBalancerAddressPool-1"
      }
    ]
    
    

If there are insufficient VIPs provisioned on the cluster, the following error appears, where `n` is the required number of VIPs, and `m` is the number of VIPs discovered on the cluster:
    
    
    Cluster has less than n external IPs, got m.
    

If you get this error, you must delete and re-create the cluster with a sufficient number of VIPs.

### Configure the Google Cloud service subdomain

Before you deploy the first Google Cloud service in a Distributed Cloud connected zone, you have the option to customize the subdomain on which all Google Cloud services deployed in that zone will listen for connections. You can't modify this subdomain after you've deployed at least one service on that Distributed Cloud zone.

Use the following command to view the subdomain configuration:
    
    
    kubectl -n dns-system get celldns cell-dns -o yaml
    

The command returns output similar to the following:
    
    
    apiVersion: system.private.gdc.goog/v1alpha1
    kind: CellDNS
    metadata:
      name: cell-dns
      namespace: dns-system
    spec:
      delegatedSubdomain: private.goog
    

Use the following command to modify the subdomain configuration:
    
    
    kubectl -n dns-system edit celldns cell-dns
    

## Deploy a Google Cloud service on Distributed Cloud connected

To deploy a Google Cloud service on your Distributed Cloud connected cluster, follow the deployment steps described in that service's documentation.

## Configure the deployed Google Cloud service

This section describes post-deployment configuration steps that you can choose to complete based on your business requirements.

### Forward DNS queries from internal DNS to the cluster's DNS

When you deploy a Google Cloud service on your Distributed Cloud connected cluster, a dedicated DNS server for that service is deployed on the cluster. We recommend that you forward DNS queries for the service's subdomain to the newly created DNS server on the cluster.

  1. Use the following commands to get the cluster subdomain:
         
         CLUSTER_SUBDOMAIN=$(kubectl get configmap -n \
             $(kubectl get clusters -A -o jsonpath="{.items[0].metadata.namespace}") \
             dns-prefix -o jsonpath="{.data.dnsPrefix}")
         DELEGATED_SUBDOMAIN=$(kubectl get celldns -n dns-system cell-dns -o \
           jsonpath="{.spec.delegatedSubdomain}")
         CLUSTER_FQDN="${CLUSTER_SUBDOMAIN?}.${DELEGATED_SUBDOMAIN?}"
         echo "${CLUSTER_FQDN?}"
         

The last command returns output similar to the following:
         
         my-zone.google.private.goog
         

  2. Use the following command to get the VIP of the on-cluster DNS server:
         
         DNS_EXT_IP=$(k -n dns-system get service gpc-coredns-external-tcp -o "jsonpath={.status.loadBalancer.ingress[0].ip}")
         

  3. Configure your internal DNS server to forward DNS queries for the deployed Google Cloud service to the VIP you obtained in the previous step. For example:

     * For `dnsmasq`, add the following to `/etc/dnsmasq.conf`:
           
           server=/${CLUSTER_FQDN?}/${DNS_EXT_IP?}
           

     * For CoreDNS, add the following to the [Corefile](https://coredns.io/2017/07/23/corefile-explained/):
           
           ${CLUSTER_FQDN?}:53 {
             errors
             cache 30
             forward . ${DNS_EXT_IP?} {
               max_concurrent 1000
             }
           }
           




### Test for DNS resolution

Use the following `dig` command to test for proper domain resolution. Pay particular attention to the `ANSWER SECTION`:
    
    
     dig "ais-core.${CLUSTER_FQDN?}"
    

The command returns output similar to the following:
    
    
    ...
    ;; ANSWER SECTION:
    ais-core.my-zone.google.private.goog. 300 IN A 10.200.0.0
    ...
    

### Retrieve the self-signed certificate for the deployed Google Cloud service

When you deploy a Google Cloud service on your Distributed Cloud connected cluster, Distributed Cloud connected issues a self-signed certificate that it then uses to encrypt network traffic for that service. We recommend that you retrieve this certificate and configure your business environment to trust it.

To obtain this certificate in PEM-encoded format, use the following command:
    
    
     kubectl get secret -n cert-manager-cluster-resources web-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 -d
    

Distributed Cloud connected generates a number trust bundles throughout your cluster. These trust bundles are stored as ConfigMaps in every namespace on the cluster. They are:

  * **`trust-store-internal-only`**. Contains Certificate Authorities (CAs) for Distributed Cloud connected's internal services.
  * **`trust-store-root-ext`**. Contains all CA's in the `trust-store-root-ext`, plus the CA that signed the target Google Cloud service's self-signed certificate. Mount this trust bundle in a Pod if you need that Pod to access the target Google Cloud service.
  * **`trust-store-user-ext`**. Contains all CA's in the `trust-store-root-ext`, plus any CAs you've added manually. Mount this bundle in a Pod if you need that Pod to access both the target Google Cloud service and any internal resources that use certificates signed by the CAs you've added manually.



Use the following command to view the target ConfigMap:
    
    
     kubectl -n default get configmap trust-store-user-root-ext -o yaml
    

The following example output shows a typical `trust-store-user-root-ext` ConfigMap resource:
    
    
    apiVersion: v1
    binaryData:
      ca.jks: WW91IGFyZSBhd2Vzb21lIQo=
    data:
      ca.crt: |-
        -----BEGIN CERTIFICATE-----
        WW91IGFyZSBncmVhdCEK
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        WW91IGFyZSBmYW50YXN0aWMhCg==
        -----END CERTIFICATE-----
    kind: ConfigMap
    metadata:
      labels:
        trust.cert-manager.io/bundle: trust-store-user-root-ext
      name: trust-store-user-root-ext
      namespace: default
    

### Configure a deployed Google Cloud service to trust your own certificates

You can create a TLS secret in your Distributed Cloud connected cluster and annotate it with the `security.private.gdc.goog/bundles=trust-store-user-root-ext` annotation in the `cert-manager-cluster-resources` namespace. This lets your deployed Google Cloud service trust your internal third-party services to facilitate the exchange of data between them.

When you apply this secret to your cluster, the deployed Google Cloud service trusts the CA certificate stored in the `ca.crt` file referenced in the secret. For example:
    
    
    apiVersion: v1
    data:
      ca.crt: base64EncodedCaCert
      tls.crt: base64EncodedCert
      tls.key: base64EncodedKey
    kind: Secret
    metadata:
      annotations:
        security.private.gdc.goog/bundles: trust-store-user-root-ext
      name: my-corporate-cert
      namespace: cert-manager-cluster-resources
    type: kubernetes.io/tls
    

### Configure an authentication provider

You can configure an authentication provider to facilitate logon through the deployed Google Cloud service's user interface. The following example shows a configuration for an [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect) provider:
    
    
    apiVersion: authentication.gke.io/v2alpha1
    kind: ClientConfig
    metadata:
      name: default
      namespace: kube-public
    spec:
      authentication:
      - name: "google-oidc"
        oidc:
          clientID: "my-supersecret-client-id.apps.googleusercontent.com"
          clientSecret: "my-supersecret-secret"
          issuerURI: "https://accounts.google.com"
          scopes: "email"
          userClaim: "email"
      name: "default"
    

For more information, see [About authentication using third-party identities](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity).

## Use a deployed Google Cloud service

Refer to the deployed Google Cloud service's documentation for information on how to configure it to fulfill your business requirements.

## Remove a deployed Google Cloud service

To remove a deployed Google Cloud service from your Distributed Cloud connected cluster, follow the steps in that service's documentation. If you completed any of the optional post-deployment steps described on this page, also do the following:

  * Disable DNS forwarding to the service's subdomain in your internal DNS.
  * Disable the trust for the service's self-signed certificate wherever that trust has been established.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
