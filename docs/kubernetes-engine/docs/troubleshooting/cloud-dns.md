---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-dns/
title: Troubleshoot Cloud DNS in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:30.429678+00:00
---

# Troubleshoot Cloud DNS in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot Cloud DNS in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

If your Pods can't connect to services and your Google Kubernetes Engine (GKE) cluster uses Cloud DNS as the DNS provider, you might encounter errors like `dial tcp: i/o timeout` or `no such host`. These errors often indicate issues with the Cloud DNS configuration, such as misconfigured private zones or an incorrect Cloud DNS scope.

Use this page to diagnose and resolve common issues related to using the managed Cloud DNS service with GKE, helping to ensure reliable DNS resolution for your workloads.

This information is important for Platform admins and operators and Networking specialists who configure and manage the integration between GKE and Cloud DNS. It's also useful for Application developers whose applications are facing service discovery problems. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Identify the source of DNS issues in Cloud DNS

The following sections help you diagnose why Cloud DNS is having difficulty resolving queries.

### Verify basic settings

If your Pod is unable to resolve DNS lookups, make sure that Cloud DNS is configured the way that you want. This section helps you verify if you're using Cloud DNS, confirm the existence of a private DNS zone for the GKE cluster, and ensure the accuracy of DNS records for the target service.

To verify these settings, complete the following commands:

  1. Check which DNS server your Pod is using:
         
         kubectl exec -it POD_NAME -- cat /etc/resolv.conf | grep nameserver
         

Replace `POD_NAME` with the name of the Pod experiencing issues with DNS resolution.

If you're using Cloud DNS, the output is the following:
         
         nameserver 169.254.169.254
         

If you see any other value, then you're not using Cloud DNS. Check that Cloud DNS was properly [enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#before_you_begin).

  2. Verify that the managed zones exist:
         
         gcloud dns managed-zones list --format list
         

The output is similar to the following:
         
         - creationTime: 2021-02-12T19:24:37.045Z
           description: Private zone for GKE cluster "" with cluster suffix "CLUSTER_DOMAIN" in project "PROJECT_ID"
           dnsName: CLUSTER_DOMAIN.
           id: 5887499284756055830
           kind: dns#managedZone
           name: gke-CLUSTER_NAME-aa94c1f9-dns
           nameServers: ['ns-gcp-private.googledomains.com.']
           privateVisibilityConfig: {'kind': 'dns#managedZonePrivateVisibilityConfig'}
           visibility: private
         

This output includes the following values:

     * `CLUSTER_DOMAIN`: the DNS domain suffix that was automatically assigned to your cluster.
     * `PROJECT_ID`: your project ID.
     * `CLUSTER_NAME`: the name of the cluster with the private zone.

In this output, the value in the `name` field shows that Google Cloud created a zone named `gke-CLUSTER_NAME-aa94c1f9-dns`.

If you don't see a managed zone, it means that a private zone wasn't created for your cluster, or you might not be authenticated correctly. To troubleshoot, see [Private zones](https://docs.cloud.google.com/dns/docs/troubleshooting#private-zones) in the Cloud DNS documentation.

  3. Verify the DNS records for your Service:
         
         gcloud dns record-sets list --zone ZONE_NAME | grep SERVICE_NAME
         

Replace the following:

     * `ZONE_NAME`: the name of the private zone.
     * `SERVICE_NAME`: the name of the Service.

The output similar to the following:
    
    dns-test.default.svc.cluster.local.                A     30     10.47.255.11
    

This output shows that Cloud DNS contains an A record for the domain `dns-test.default.svc.cluster.local.` and the IP address of your cluster is `10.47.255.11`.

If the records look incorrect, see [Patch a resource record set](https://docs.cloud.google.com/dns/docs/records#console_4) in the Cloud DNS documentation to update them.




### Verify response policies

Verify that your response policies exist and are correctly named:

  1. View a list of all of your response policies:
         
         gcloud dns response-policies list --format="table(responsePolicyName, description)"
         

The output is similar to the following:
         
         RESPONSE_POLICY_NAME          DESCRIPTION
         gke-CLUSTER_NAME-52c8f518-rp  Response Policy for GKE cluster "CLUSTER_NAME" with cluster suffix "cluster.local." in project "gke-dev" with scope "CLUSTER_SCOPE".
         

In this output, `gke-CLUSTER_NAME-52c8f518-rp` shows that Google Cloud created a private zone named `gke-CLUSTER_NAME-aa94c1f9-rp`. Response policies that Google Cloud creates have the `gke-` prefix.

  2. View response policies in a specific private zone:
         
         gcloud dns response-policies rules list ZONE_NAME \
             --format="table(localData.localDatas[0].name, localData.localDatas[0].rrdatas[0])"
         

Replace `ZONE_NAME` with the name of the private zone experiencing issues.

The output is similar to the following:
         
         1.240.27.10.in-addr.arpa.    kubernetes.default.svc.cluster.local.
         52.252.27.10.in-addr.arpa.   default-http-backend.kube-system.svc.cluster.local.
         10.240.27.10.in-addr.arpa.   kube-dns.kube-system.svc.cluster.local.
         146.250.27.10.in-addr.arpa.  metrics-server.kube-system.svc.cluster.local.
         

The first column shows you the IP address or domain name pattern that the rule matches. The second column is the hostname associated with the IP address.




If you notice any issues in the output of these commands, see [update a response policy rule](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies#edit-response-policy-rule) in the Cloud DNS documentation.

### Investigate with logs, dashboards, and metrics

Cloud DNS includes multiple logging and monitoring options to help you further investigate your DNS issues:

  * To view logs for resources like zones and records, enable [Cloud Logging for Cloud DNS](https://docs.cloud.google.com/dns/docs/monitoring#using_logging).

  * To view charts for DNS queries and to see data for error rate, QPS, and 99th percentile latency for your private zones, use the [Cloud DNS monitoring dashboard](https://docs.cloud.google.com/dns/docs/monitoring-dashboard).

  * To visualize the latency and success rates of your DNS queries, use the [`query/latencies` and `query/response_count` metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-dns) in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).




### Check for new records

Review the logs to see if any new records were created in the managed Cloud DNS private zone. This can be helpful if you suddenly experience failing DNS resolutions in the cluster.

To check for new records, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter the following query:
         
         resource.type="dns_managed_zone"
         protoPayload.request.change.additions.name="headless-svc-stateful.default.svc.cluster.local."
         protoPayload.methodName="dns.changes.create"
         

  3. Click **Run query**.

  4. Review the output. If you find changes that correspond to when you first noticed errors, consider reverting them.




### Verify custom stub domains and name servers

If you're using a GKE Standard cluster with a custom stub domain or upstream name server, review the ConfigMap and verify that the values are correct.

Cloud DNS translates the `stubDomains` and `upstreamNameservers` values into Cloud DNS forwarding zones. Google manages these resources, so if you notice any errors, [contact Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures#manage_a_support_case) for assistance.

### Contact Cloud Customer Care

If you've worked through the preceding sections, but still can't diagnose the cause of your issue, [contact Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures#manage_a_support_case).

## Resolve specific errors

If you've experienced a specific error or issue, use the advice in the following sections.

### Issue: Can't resolve GKE cluster Service from a Compute Engine VM

If you're unable to resolve a GKE cluster Service from a Compute Engine VM, verify the cluster's [Cloud DNS scope](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#dns-scopes).

The scope you use with Cloud DNS determines which resources can be resolved:

  * **Cluster scope** : DNS resolution is restricted to resources _within_ the Kubernetes cluster (Pods and Services). This is the default setting and it's suitable when you don't need to resolve external resources outside of the Kubernetes cluster or GKE Virtual Private Cloud (VPC).

**Note:** You can [enable Cloud DNS DNS additive VPC scope](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#additive_vpc_scope_dns) ([Preview](https://cloud.google.com/products#product-launch-stages)) to extend the GKE cluster scope to make headless Services resolvable from other resources in the VPC.
  * **VPC scope** : DNS resolution extends to the entire VPC, including resources like Compute Engine VMs. This lets the cluster resolve internal DNS records for resources outside the GKE cluster, but within the same VPC, such as Google Cloud VMs.




To verify your cluster's Cloud DNS scope, complete the following steps:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster experiencing issues with DNS.

  3. In the **Cluster networking** section of the cluster details page, review the information in the **DNS provider** row.

  4. If you see **Cloud DNS (cluster scope)** , you're using cluster scope. To change the DNS scope, recreate the cluster with the appropriate DNS scope.




### Issue: Pods still using kube-dns after Cloud DNS enabled

If your Pods use kube-dns even after Cloud DNS is enabled on an existing cluster, ensure you have upgraded or recreated your node pools after you enable Cloud DNS on the cluster. Until this step is complete, Pods continue to use kube-dns.

### Issue: Unable to update existing cluster or create cluster with Cloud DNS enabled

Ensure you are using the correct version. Cloud DNS for GKE requires GKE version 1.19 or later for clusters using VPC scope, or GKE version 1.24.7-gke.800, 1.25.3-gke.700 or later for clusters using cluster scope.

### Issue: DNS lookups on nodes fail after enabling Cloud DNS on a cluster

If you enable cluster scope Cloud DNS in a GKE cluster that has custom stub domains or upstream name servers, the custom config applies to both nodes and Pods in the cluster because Cloud DNS cannot distinguish between Pod and node DNS requests. DNS lookups on nodes might fail if the custom upstream server cannot resolve the queries.

### Issue: Unable to update or create cluster with Cloud DNS additive VPC scope enabled

Ensure you're using the correct version. Cloud DNS Additive VPC scope requires GKE version 1.28 or later.

### Error: Cloud DNS disabled

The following event occurs when the Cloud DNS API is disabled:
    
    
    Warning   FailedPrecondition        service/default-http-backend
    Failed to send requests to Cloud DNS: Cloud DNS API Disabled. Please enable the Cloud DNS API in your project PROJECT_NAME: Cloud DNS API has not been used in project PROJECT_NUMBER before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/dns.googleapis.com/overview?project=PROJECT_NUMBER then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.
    

This error occurs because the Cloud DNS API is not enabled by default. You must enable the Cloud DNS API manually.

To resolve the issue, [enable the Cloud DNS API](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#before_you_begin).

### Error: Failed to send requests to Cloud DNS: API rate limit exceeded.

The following event occurs when a project has exceeded a Cloud DNS quota or limit:
    
    
    kube-system   27s         Warning   InsufficientQuota
    managedzone/gke-cluster-quota-ee1bd2ca-dns     Failed to send requests to Cloud DNS: API rate limit exceeded. Contact Google Cloud support team to request a quota increase for your project PROJECT_NAME: Quota exceeded for quota metric 'Write requests' and limit 'Write limit for a minute for a region' of service 'dns.googleapis.com' for consumer 'project_number:PROJECT_NUMBER.
    

To resolve this issue, review the [Cloud DNS quotas](https://docs.cloud.google.com/dns/quotas) and [Compute Engine quotas and limits](https://docs.cloud.google.com/compute/quotas). You can increase quota using the Google Cloud console.

### Error: Failed to send to requests to Cloud DNS due to a previous error

The following event occurs when errors cause cascading failures:
    
    
    kube-system   27s         Warning   InsufficientQuota
    managedzone/gke-cluster-quota-ee1bd2ca-dns     Failed to send requests to Cloud DNS: API rate limit exceeded. Contact Google Cloud support team to request a quota increase for your project PROJECT_NAME: Quota exceeded for quota metric 'Write requests' and limit 'Write limit for a minute for a region' of service 'dns.googleapis.com' for consumer 'project_number:PROJECT_NUMBER.
    kube-system   27s         Warning   FailedPrecondition               service/default-http-backend                         Failed to send requests to Cloud DNS due to a previous error. Please check the cluster events.
    

To resolve this issue, check the cluster events to find the source of the original error, and follow the instructions to resolve that root issue.

In the preceding example, the `InsufficientQuota` error for the managed zone triggered cascading failures. The second error for `FailedPrecondition` indicates that a previous error occurred, which was that initial insufficient quota problem. To resolve this example issue, you would follow the guidance for the Cloud DNS quota error.

### Error: Failed to bind response policy

The following event occurs when a response policy is bound to the network of the cluster and Cloud DNS for GKE attempts to bind a response policy to the network:
    
    
    kube-system   9s          Warning   FailedPrecondition               responsepolicy/gke-2949673445-rp
    Failed to bind response policy gke-2949673445-rp to test. Please verify that another Response Policy is not already associated with the network: Network 'https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/global/networks/NETWORK_NAME' cannot be bound to this response policy because it is already bound to another response policy.
    kube-system   9s          Warning   FailedPrecondition               service/kube-dns
    Failed to send requests to Cloud DNS due to a previous error. Please check the cluster events.
    

To resolve the issue, complete the following steps:

  1. Get the response policy bound to the network:
         
         gcloud dns response-policies list --filter='networks.networkUrl: NETWORK_URL'
         

Replace `NETWORK_URL` with the network URL from the error, such as `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME`.

If the output is empty, the response policy might not be in the same project. Proceed to the next step to search for the response policy.

If the output is similar to the following, skip to step 4 to delete the response policy.
         
         [
            {
               "description": "Response Policy for GKE cluster \"CLUSTER_NAME\" with cluster suffix \"cluster.local.\" in project \"PROJECT_ID\" with scope \"CLUSTER_SCOPE\".",
               ...
               "kind": "dns#responsePolicy",
               "responsePolicyName": "gke-CLUSTER_NAME-POLICY_ID-rp"
            }
         ]
         

  2. Get a list of projects with the `dns.networks.bindDNSResponsePolicy` permission using the [IAM Policy Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#principal-query-all).

  3. Check if each project has the response policy that is bound to the network:
         
         gcloud dns response-policies list --filter='networks.networkUrl:NETWORK_URL' \
             --project=PROJECT_NAME
         

  4. [Delete the response policy](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies#delete-response-policy).




### Error: Invalid configuration specified in kube-dns

The following event occurs when you apply a custom [kube-dns ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kube-dns#stub-domains) that is not valid for Cloud DNS for GKE:
    
    
    kube-system   49s         Warning   FailedValidation                 configmap/kube-dns
    Invalid configuration specified in kube-dns: error parsing stubDomains for ConfigMap kube-dns: dnsServer [8.8.8.256] validation: IP address "8.8.8.256" invalid
    

To resolve this issue, review the details in the error for the invalid part of the ConfigMap. In the preceding example, `8.8.8.256` is not a valid IP address.

## What's next

  * For general information about diagnosing Kubernetes DNS issues, see [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/).

  * Review [Cloud DNS troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
