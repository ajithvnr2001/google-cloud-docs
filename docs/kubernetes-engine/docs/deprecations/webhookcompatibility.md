---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/webhookcompatibility/
title: Ensuring compatibility of webhook certificates before upgrading to v1.23 \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:34.182612+00:00
---

# Ensuring compatibility of webhook certificates before upgrading to v1.23  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/webhookcompatibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Ensuring compatibility of webhook certificates before upgrading to v1.23 Stay organized with collections  Save and categorize content based on your preferences. 

Starting from **version 1.23** , Kubernetes no longer supports server identity validation using the X.509 Common Name (CN) field in certificates. Instead, Kubernetes will only rely on information in the X.509 Subject Alternative Name (SAN) fields.

To prevent impact to your clusters, you must replace incompatible certificates without SANs for backends of webhooks and aggregated API servers before upgrading your clusters to Kubernetes **version 1.23**.

**Note:** GKE only upgrades clusters on **version 1.22.6-gke.1000** or later if the clusters are not using webhook backends with incompatible certificates. Affected clusters will only be upgraded once the certificate(s) are replaced or when Kubernetes **version 1.22** reaches its [end of standard support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule) date. If your cluster has an earlier version than **1.22.6-gke.1000** , you can temporarily prevent automatic minor upgrades by configuring a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).**Warning:** If you do not ensure compatibility of your certificates for Kubernetes **version 1.23** , cluster functionality might be impaired. GKE webhook and aggregated API server backends reliant on the CN field for server identity validation will fail due to authentication failure. The Kubernetes control plane will be unable to communicate with your webhooks. Depending on your configuration—especially if you use Admission webhooks—failure to contact a webhook might block resource (i.e. Pod) creation.

## Why Kubernetes no longer supports backend certificates without SANs

GKE operates open-source Kubernetes, which uses the [kube-apiserver component](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) to contact your webhook and aggregated API server backends using Transport Layer Security (TLS). The kube-apiserver component is written in the Go programming language.

Before Go 1.15, TLS clients validated the identity of the servers they connected to using a two-step process:

  1. Check if the DNS name (or IP address) of the server is present as one of the SANs on the server's certificate.
  2. As a fallback, check if the DNS name (or IP address) of the server is equal to the CN on the server's certificate.



[RFC 6125](https://datatracker.ietf.org/doc/html/rfc6125) fully deprecated server identity validation based on the CN field in 2011. Browsers and other security-critical applications no longer use the field.

To align with the wider TLS ecosystem, [Go 1.15 removed Step 2](https://golang.org/doc/go1.15#commonname) from its validation process, but left a debug switch (`x509ignoreCN=0`) to enable the old behavior to ease the migration process. Kubernetes **version 1.19** was the first version built using Go 1.15. GKE clusters on versions from 1.19 to 1.22 enabled the debug switch by default to provide customers with more time to replace the certificates for the affected webhook and aggregated API server backends.

Kubernetes **version 1.23** is built with Go 1.17, which [removes the debug switch](https://tip.golang.org/doc/go1.17#crypto/x509). Once GKE upgrades your clusters to **version 1.23** , calls will fail to connect from your cluster's control plane to webhooks or aggregated API services that do not provide a valid X.509 certificate with appropriate SAN.

## Identifying affected clusters

### For clusters running patch versions at least 1.21.9 or 1.22.3

For clusters on patch versions 1.21.9 and 1.22.3 or later with Cloud Logging [enabled](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing#installing), GKE provides a [Cloud Audit Logs log](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging#viewing_your_projects_admin_activity_log) to identify calls to affected backends from your cluster. You can use the following filter to search for the logs:
    
    
    logName =~ "projects/.*/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type = "k8s_cluster"
    operation.producer = "k8s.io"
    "invalid-cert.webhook.gke.io"
    

If your clusters have not called backends with affected certificates, you won't see any logs. If you do see such an audit log, it will include the hostname of the affected backend.

The following is an example of the log entry, for a webhook backend hosted by a service named **example-webhook** in the **default** namespace:
    
    
    {
      ...
      resource {
        type: "k8s_cluster",
        "labels": {
          "location": "us-central1-c",
          "cluster_name": "example-cluster",
          "project_id": "example-project"
        }
      },
      labels: {
        invalid-cert.webhook.gke.io/example-webhook.default.svc: "No subjectAltNames returned from example-webhook.default.svc:8443",
        ...
      },
      logName: "projects/example-project/logs/cloudaudit.googleapis.com%2Factivity",
      operation: {
        ...
        producer: "k8s.io",
        ...
      },
      ...
    }
    

The hostnames of the affected services (e.g. `example-webhook.default.svc`) are included as suffixes in the label names that start with `invalid-cert.webhook.gke.io/`. You can also get the name of the cluster that made the call from the `resource.labels.cluster_name` label, which has `example-cluster` value in this example.

**Deprecation insights**

You can learn which clusters use incompatible certificates from [deprecation insights](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations). Insights are available for clusters running version 1.22.6-gke.1000 or later.

### Other cluster versions

If you have a cluster on a patch version earlier than 1.22.3 on the 1.22 minor version, or any patch version earlier than 1.21.9, you have two options for determining whether your cluster is affected by this deprecation:

**Option 1** _(recommended)_ : [Upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your cluster to a patch version that supports identifying affected certificates with logs. Make sure that Cloud Logging is [enabled](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing#installing) for your cluster. After your cluster has been upgraded, the identifying Cloud Audit Logs logs will be produced each time the cluster attempts to call a Service that does not provide a certificate with an appropriate SAN. As the logs will only be produced on a call attempt, we recommend waiting for 30 days after an upgrade to make enough time for all call paths to be invoked.

Using logs to identify impacted services is recommended because this approach minimizes manual effort by automatically producing logs to show the affected services.

**Option 2** : Inspect the certificates used by Webhooks or Aggregated API Servers in your clusters to determine whether they are affected because of not having SANs:

  1. Get the list of Webhooks and Aggregated API Servers in your cluster and identify their backends (Services or URLs).
  2. Inspect the certificates used by the backend services.



Given the manual effort required to inspect all certificates in this way, this method should only be followed if you need to assess the impact of the deprecations in Kubernetes **version 1.23** before upgrading your cluster to **version 1.21**. If you can upgrade your cluster to 1.21, you should upgrade it first and then follow the instructions in Option 1 to avoid the manual effort.

## Identifying backend services to inspect

To identify backends that might be affected by the deprecation, get the list of Webhooks and Aggregated API Services and their associated backends in the cluster.

To list all relevant webhooks in the cluster, use the following `kubectl` commands:
    
    
    kubectl get mutatingwebhookconfigurations -A   # mutating admission webhooks
    
    kubectl get validatingwebhookconfigurations -A # validating admission webhooks
    

You can get an associated backend Service or URL for a given Webhook by examining `clientConfig.service` [field](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#service-reference) or `webhooks.clientConfig.url` [field](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#url) in the Webhook's configuration:
    
    
    kubectl get mutatingwebhookconfigurations example-webhook -o yaml
    

The output of this command is similar to the following:
    
    
    apiVersion: admissionregistration.k8s.io/v1
    kind: MutatingWebhookConfiguration
    webhooks:
    - admissionReviewVersions:
      clientConfig:
        service:
            name: example-service
            namespace: default
            port: 443
    

Note that clientConfig can specify its backend as a Kubernetes Service (`clientConfig.service`), or as a URL (`clientConfig.url`).

To list all relevant Aggregated API Services in the cluster, use the following `kubectl` command:
    
    
    kubectl get apiservices -A |grep -v Local      # aggregated API services
    

The output of this command is similar to the following:
    
    
    NAME                     SERVICE                      AVAILABLE   AGE
    v1beta1.metrics.k8s.io   kube-system/metrics-server   True        237d
    

This example returns `metric-server` Service from the `kube-system` namespace.

You can get an associated Service for a given Aggregated API by examining `spec.service` field:
    
    
    kubectl get apiservices v1beta1.metrics.k8s.io -o yaml
    

The output of this command is similar to the following:
    
    
    ...
    apiVersion: apiregistration.k8s.io/v1
    kind: APIService
    spec:
      service:
        name: metrics-server
        namespace: kube-system
        port: 443
    

### Inspecting the certificate of a Service

Once you have identified relevant backend Services to inspect, you can inspect the certificate of each specific Service, such as `example-service`:

  1. Find the selector and target port of the service:
         
         kubectl describe service example-service
         

The output of this command is similar to the following:
         
         Name: example-service
         Namespace: default
         Labels: run=nginx
         Selector: run=nginx
         Type: ClusterIP
         IP: 172.21.xxx.xxx
         Port: 443
         TargetPort: 444
         

In this example, `example-service` has the selector `run=nginx` and the target port `444`.

**Note:** When absent, `TargetPort` is the same value as the `Port` field.
  2. Find a pod matching the selector:
         
         kubectl get pods --selector=run=nginx
         

The output of the command is similar to the following:
         
         NAME          READY   STATUS    RESTARTS   AGE
         example-pod   1/1     Running   0          21m
         

  3. Set up a [port forward](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward)

from your `kubectl` localhost to the pod.
         
         kubectl port-forward pods/example-pod LOCALHOST_PORT:TARGET_PORT # port forwarding in background
         

Replace the following in the command:

     * `LOCALHOST_PORT`: the address to listen on.
     * `TARGET_PORT` the `TargetPort` from Step 1.
  4. Use `openssl` to print the certificate used by the Service:
         
         openssl s_client -connect localhost:LOCALHOST_PORT </dev/null | openssl x509 -noout -text
         

This example output shows a valid certificate (with SAN entries):
         
         Subject: CN = example-service.default.svc
         X509v3 extensions:
           X509v3 Subject Alternative Name:
             DNS:example-service.default.svc
         

This example output shows a certificate with a missing SAN:
         
         Subject: CN = example-service.default.svc
           X509v3 extensions:
               X509v3 Key Usage: critical
                   Digital Signature, Key Encipherment
               X509v3 Extended Key Usage:
                   TLS Web Server Authentication
               X509v3 Authority Key Identifier:
                   keyid:1A:5F:29:D8:E9:3C:54:3C:35:CC:D8:AB:D1:21:FD:C3:56:25:C0:74
         

  5. Remove the port forward from running in the background with the following commands:
         
         $ jobs
         [1]+  Running                 kubectl port-forward pods/example-pod 8888:444 &
         $ kill %1
         [1]+  Terminated              kubectl port-forward pods/example 8888:444
         




### Inspecting the certificate of a URL backend

If the webhook uses a `url` [backend](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#url), directly connect to the hostname specified in the URL. For example, if the URL is `https://example.com:123/foo/bar`, use the following `openssl` command to print the certificate used by the backend:
    
    
      openssl s_client -connect example.com:123 </dev/null | openssl x509 -noout -text
    

## Mitigating the risk of 1.23 upgrade

Once you have identified affected clusters and their backend services using certificates without SANs, you must update the webhooks and aggregated API server backends to use certificates with appropriate SANs prior to upgrading the clusters to **version 1.23**.

GKE will not automatically upgrade clusters on versions 1.22.6-gke.1000 or later with backends using incompatible certificates until you replace the certificates or until **version 1.22** reaches [end of standard support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

If your cluster is on a GKE version earlier than **1.22.6-gke.1000** , you can temporarily prevent automatic upgrades by configuring a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#x27;) to prevent minor upgrades.

## Resources

See the following resources for additional information on this change:

  * [Kubernetes 1.23 release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#urgent-upgrade-notes)
    * Kubernetes is built using Go 1.17. This version of Go removes the ability to use a `GODEBUG=x509ignoreCN=0` environment setting to re-enable deprecated legacy behavior of treating the CN of X.509 serving certificates as a host name.
  * [Kubernetes 1.19](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#api-change-5) and [Kubernetes 1.20](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change-10) release notes 
    * The deprecated, legacy behavior of treating the CN field on X.509 serving certificates as a host name when no SANs are present is now disabled by default.
  * [Go 1.17 release notes](https://go.dev/doc/go1.17#crypto/x509)
    * The temporary `GODEBUG=x509ignoreCN=0` flag has been removed.
  * [Go 1.15 release notes](https://go.dev/doc/go1.15#commonname)
    * The deprecated, legacy behavior of treating the CN field on X.509 certificates as a host when no SANs are present is now disabled by default.
  * [RFC 6125](https://datatracker.ietf.org/doc/html/rfc6125#page-46) (page 46) 
    * Although the use of the CN value is existing practice, it is deprecated, and Certificate Authorities are encouraged to provide `subjectAltName` values instead.
  * [Admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#contacting-the-webhook)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
