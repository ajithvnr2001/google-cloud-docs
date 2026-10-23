---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls/
title: Using managed TLS certificates and HTTPS \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:28.015912+00:00
---

# Using managed TLS certificates and HTTPS  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using managed TLS certificates and HTTPS Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to turn off and re-enable the managed TLS certificates feature that automatically provides and renews TLS certificates to support HTTPS connections on Knative serving. 

If you want to use HTTPS,

  * Your container should continue listening on `$PORT`
  * You must choose how you are supplying TLS certificates:

    * Use managed TLS certificates, where TLS certificates are automatically created as needed, and are automatically renewed. This page describes this feature, which is available in the [supported Google Kubernetes Engine versions](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/cluster-versions).
    * [Use your own certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/bring-your-own-cert), where you are responsible for obtaining and renewing certificates. In some situations, described under Limitations, you must use your own certificates.
  * If you are using managed certificates, you must also [map your custom domain](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains) in order to use the managed certificates feature.




## Using HTTPS and HTTP

By default, if you use managed certificates, clusters or Knative serving services with managed certificates are exposed to both HTTP and HTTPS traffic. If you want only HTTPS traffic, you can enable HTTPS redirects to force all traffic to use HTTPS only.

## Troubleshooting

If you experience issues when using managed TLS certificates, refer to the [managed TLS troubleshooting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting#managed-tls) page.

## Limitations

The following considerations apply to the use of the managed TLS certificates feature:

  * Managed TLS certificates are disabled and not supported for Knative serving private clusters on Google Cloud.
  * To use the managed certificates feature, your service must be [exposed externally](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/services#connectivity): it cannot be a cluster-local service or a service exposed by [Virtual Private Cloud](https://docs.cloud.google.com/vpc).
  * The managed certificates feature works only with Cloud Service Mesh. The Istio addon or other Istio configurations are not supported.
  * This feature uses [Let's Encrypt](https://letsencrypt.org/), which has an initial quota limit of 50 TLS certificates per week per registered domain. You can ask for a quota increase by following the [Let's Encrypt documentation](https://letsencrypt.org/docs/rate-limits/).
  * When running a Knative serving cluster on other platforms, such as on-prem or AWS, this feature is disabled. To use this feature, you must make sure your cluster is able to access [Let's Encrypt](https://acme-v02.api.letsencrypt.org/directory), and your Cloud Service Mesh ingress service is exposed to the public internet.



## Before you begin

The instructions on this page assume the following:

  * You have [deployed your Knative serving service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying) to the cluster.
  * You own a domain. If you don't have a domain, you can obtain one from [Google](https://domains.google/) or from another domain vendor.
  * You created a domain mapping for your service and updated your DNS record accordingly following the instructions at the [domains mapping page](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains).
  * Use [Cloud DNS](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name), or a DNS server of your choice.

**Note:** By default, `gke-system-gateway` supports HTTP requests that have the Host header. However, if you have customized this gateway, make sure it still accepts the HTTP requests that contain the Host header.

## Disabling managed TLS certificates and HTTPS for a whole cluster

Disable managed TLS for a cluster by updating the ConfigMap `config-domainmapping`:
    
    
    kubectl patch cm config-domainmapping -n knative-serving -p '{"data":{"autoTLS":"Disabled"}}'

## Disabling managed TLS and HTTPS for a specific domain mapping

If needed, you can turn off managed TLS for a specific domain mapping:

  1. Add the annotation `domains.cloudrun.com/disableAutoTLS: "true"``:
         
         kubectl annotate domainmappings DOMAIN domains.cloudrun.com/disableAutoTLS=true

  2. Verify that HTTPS does not work: 
         
         curl https://DOMAIN

  3. Verify that HTTP is being used for the service:
         
         gcloud run domain-mappings describe --domain DOMAIN

Replace DOMAIN with your own domain name, for example: `your-domain.com`

Check the `url:` field in the return from the above command: the URL should have `http`, not `https`.




## Re-enabling managed TLS certificates and HTTPS

To re-enable managed TLS:

  1. If you haven't already done so, create a domain mapping for your service and update your DNS record accordingly following the instructions at the [domains mapping page](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains).

  2. Turn on managed TLS certificates and HTTPS by updating the ConfigMap `config-domainmapping`:
         
         kubectl patch cm config-domainmapping -n knative-serving -p '{"data":{"autoTLS":"Enabled"}}'

  3. Wait for a few minutes after the command succeeds, then make sure the certificates feature is working:
         
         kubectl get kcert

If the certificate is ready, you should see a message similar to this one:
         
         NAME              READY   REASON
         your-domain.com              True

It may take from 20 seconds to 2 minutes for the `Kcert` to become ready. If you experience any issues, see the [troubleshooting instructions](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting) for this feature.




### Verifying success

  1. Verify that the DNS record has gone into effect by running the command:
         
         gcloud run domain-mappings describe --domain DOMAIN

Replace DOMAIN with your own domain name, for example: `your-domain.com`

  2. Check the `url:` field in the return from the above command: the URL should have `https`, not `http`.

  3. Check the IP address from the above command, listed under `resourceRecords:rrdata`, and compare it to the value you see when you execute the command `host DOMAIN`. They should be the same.




## Enabling HTTPS redirects for Knative serving

**Important:** HTTPS redirect is available for cluster version `1.17.7-gke.8` and later.

If you use the managed TLS certificates feature, by default the cluster is exposed to both HTTP and HTTPS traffic for backwards compatibility reasons. If you want to force all traffic to use HTTPS only, you can enable HTTPS redirects for [an existing domain mapping](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains) by invoking the command
    
    
    kubectl annotate domainmappings DOMAIN domains.cloudrun.com/httpsRedirect=Enabled
    

where DOMAIN is the name of the domain mapping.

## Related topics

  * [Troubleshooting managed TLS](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting#managed-tls) for details on checking domain mappings, certificate quotas, order status and order timeouts, and authorization failures.
  * [Bring your own TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/bring-your-own-cert) for instructions on using your own TLS certificates instead of the managed TLS certificates.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
