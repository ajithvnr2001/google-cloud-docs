---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/proxy/
title: Install behind a proxy \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:41.566817+00:00
---

# Install behind a proxy  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Install behind a proxy Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to set up proxy and firewall rules for Google Distributed Cloud.

## Configure your proxy server

If the machines you are using for bootstrap and cluster nodes use a proxy server to access the internet, you must:

  * Configure proxying for the package manager on cluster nodes
  * Configure proxy details in the cluster configuration file.

**Note:** You can eliminate the need for all proxy settings, except for the Artifact Registry (`*.gcr.io`), by using your own private package repository server. However, by default, Google Distributed Cloud adds the Docker `apt` package repository to your machines. This package repository requires access to `packages.cloud.google.com` and preflight checks fail without it. You can prevent Google Distributed Cloud from adding the default package repository by setting `spec.osEnvironmentConfig.addPackageRepo` to `false`. For more information, see [Use a private package repository server](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/package-server).

### Prerequisites

**Warning:** Man-In-The-Middle (MITM) Proxies aren't supported.

Your proxy server must allow connections to the following addresses:

Address | Purpose  
---|---  
`*.gcr.io` | Pull images from the Artifact Registry.  
`accounts.google.com` | Process authorization requests for OpenID and discover public keys for verifying tokens.  
`binaryauthorization.googleapis.com` | Required if using [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview-on-prem). Authorize (or reject) requests from clusters to run container images.  
`cloudresourcemanager.googleapis.com` | Resolve metadata regarding the Google Cloud project the cluster is being connected to.  
`compute.googleapis.com` | Verify Cloud Logging and Cloud Monitoring resource region.  
`connectgateway.googleapis.com` | Enable the ability to [ give Cloud Customer Care read-only access to your cluster](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/support-cluster-access#grant_support_access_to_your_cluster) to diagnose problems.   
`dl.google.com` | Download and install the Google Cloud SDK.  
`gkeconnect.googleapis.com` | Establish the channel used to receive requests from Google Cloud and issues responses. If your cluster was registered to the fleet using a Google Cloud region, you need to allowlist `REGION-gkeconnect.googleapis.com` (for example, `us-central1-gkeconnect.googleapis.com`). If you didn't specify a region, the cluster uses the global Connect service instance, and you allowlist `gkeconnect.googleapis.com`. If you need to find the fleet membership location for your cluster, run `gcloud container fleet memberships list`. For more information, see [`gkeConnect.location`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#gkeconnect-location).   
`gkehub.googleapis.com` | Create Google Cloud-side [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) membership resources that correspond to the cluster you're connecting with Google Cloud.  
`gkeonprem.googleapis.com` | Create and manage the cluster lifecycle on bare metal and VMware infrastructure.  
`gkeonprem.mtls.googleapis.com` | Create and manage the cluster lifecycle on bare metal and VMware infrastructure. This version of the API is automatically used with mTLS.  
`iam.googleapis.com` | Create service accounts, which you can use to authenticate to Google Cloud and make API calls.  
`iamcredentials.googleapis.com` | Provides admission control and telemetry reporting for audit logging.  
`kubernetesmetadata.googleapis.com` | Clusters use this API as an endpoint to send Kubernetes metadata to Google Cloud. The metadata is vital for cluster monitoring, debugging, and recovery.  
`logging.googleapis.com` | Write log entries and manage your Cloud Logging configuration.  
`monitoring.googleapis.com` | Manage your Cloud Monitoring data and configurations.  
`oauth2.googleapis.com` | Authenticate through OAuth token exchange for account access.  
`opsconfigmonitoring.googleapis.com` | Collect metadata for Kubernetes resources such as pods, deployments, or nodes to enrich metric queries.  
`releases.hashicorp.com` | Optional. Use the Terraform client on your admin workstation to run commands, such as `terraform apply`.  
`securetoken.googleapis.com` | Retrieve refresh tokens for workload identity authorization.  
`servicecontrol.googleapis.com` | Write audit log entries into Cloud Audit Logs.  
`serviceusage.googleapis.com` | Enable and validate services and APIs.  
`stackdriver.googleapis.com` | Manage Google Cloud Observability metadata, such as Stackdriver accounts.  
`storage.googleapis.com` | Manage object storage and buckets, such as Artifact Registry objects.  
`sts.googleapis.com` | Exchange Google or third-party credentials for a short-lived access token to Google Cloud resources.  
`www.googleapis.com` | Authenticate service tokens from incoming Google Cloud service requests.  
  
In addition to these URLs, the proxy server must also allow any package mirrors your operating system's package manager requires. You can update the package manager configuration to use a more deterministic list, which is easier to manage.

### Configure proxying for the package manager on cluster nodes

Google Distributed Cloud uses the APT package manager on Ubuntu and the DNF package manager on Red Hat Enterprise Linux. Ensure that the OS package manager has the correct proxy configuration.

Refer to your OS distribution's documentation for details about configuring the proxy. The following examples show one way to configure proxy settings:

### APT

These commands demonstrate how to configure the proxy for APT:
    
    
    sudo touch /etc/apt/apt.conf.d/proxy.conf
    
    echo 'Acquire::http::Proxy "http://USERNAME:PASSWORD@DOMAIN";' \
        >> /etc/apt/apt.conf.d/proxy.conf
    
    echo 'Acquire::https::Proxy "http://USERNAME:PASSWORD@DOMAIN";' \
        >> /etc/apt/apt.conf.d/proxy.conf
    

Replace `USERNAME:PASSWORD@DOMAIN` with details specific to your configuration. For example, if your proxy doesn't require a login, don't include `USERNAME:PASSWORD@` with `DOMAIN`.

### DNF

This command demonstrates how to configure the proxy for DNF:
    
    
    echo "proxy=http://USERNAME:PASSWORD@DOMAIN" >> /etc/dnf/dnf.conf
    

Replace `USERNAME:PASSWORD@DOMAIN` with details specific to your configuration. For example, if your proxy doesn't require a login, don't include `USERNAME:PASSWORD@` with `DOMAIN`.

### Configure proxy details in the cluster configuration file

In the cluster configuration file, set the following values to configure the cluster to use the proxy:

**Caution:** If your cluster is configured for [VPC Service Controls](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/hardening-your-cluster#vpc-sc), don't configure the following proxy settings in your cluster. VPC Service Controls isn't compatible with the cluster proxy configuration.

#### `proxy.url`

A string that specifies the proxy URL. The bootstrap and node machines use this proxy to access the internet. The proxy URL string must start with its schema, for example `http://` or `https://`.

#### `proxy.noProxy`

A list of IP addresses, hostnames, and domain names that shouldn't go through the proxy server.

In most cases, you don't need to add any items to this list.

`noProxy` use cases:

  * Using a private package mirror, which located in the same private network (Don't need proxy to access)

  * Using a private registry mirror, which located in the same private network (Don't need proxy to access)




#### Example

The following is an example of the proxy settings in a cluster configuration file:
    
    
      proxy:
         url: http://USERNAME:PASSWORD@DOMAIN
         noProxy:
         - example1.com
         - example2.com
    

### Proxy configurations for GKE Identity Service

If you use GKE Identity Service for authentication in Google Distributed Cloud clusters, then the following additional steps are required to ensure GKE Identity Service works when behind a proxy.

**Note:** The following are required only if you use GKE Identity Service for [OIDC authentication](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider).

  1. In the cluster configuration file, set the proxy details in the OIDC `authentication` section for GKE Identity Service settings.
         
         authentication:
             oidc:
               proxy: http://USERNAME:PASSWORD@DOMAIN
         

  2. Update your proxy server's configuration to allow connections to your OIDC provider's authentication URLs.




### How proxy is used inside the cluster

As a rule of thumb, `bmctl` commands and the processes they spawn use the proxy configuration defined by the environment variables `HTTPS_PROXY` and `NO_PROXY`, _if_ they are defined. Otherwise, `bmctl` uses the proxy configuration from the cluster configuration file. Other commands that are run on the admin workstation, on cluster node machines, or by the bootstrap cluster use the proxy configuration from the cluster configuration file.

The OS package manager on each node uses its own configuration files for proxy settings.

#### Override the proxy configuration in your bootstrap machine

You can run your admin workstation behind a different proxy than the one used by your node machines by overriding the proxy settings in the cluster configuration file. To override the proxy settings, set the following environment variables on the bootstrap machine:
    
    
    export HTTPS_PROXY=http://USERNAME:PASSWORD@DOMAIN
    

Replace `USERNAME:PASSWORD@DOMAIN` with details specific to your configuration.
    
    
    export NO_PROXY=example1.com,example2.com
    

Replace example1.com,example2.com with IP addresses, hostnames, and domain names that shouldn't go through the proxy server.

### Side effects

When run as root, `bmctl` updates the Docker proxy configuration on the bootstrap machine. If you don't run `bmctl` as root, [configure the Docker proxy manually](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy).

## Firewall rules

Set up your firewall rules as outlined in the following sections to allow the described traffic needed for Google Distributed Cloud.

For prerequisite port requirements for Google Distributed Cloud, see [Port usage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#port_usage).

### Firewall rules for cluster node IP addresses

The following table describes the firewall rules for IP addresses available in your clusters.

From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
Cluster node | 1024 - 65535 | `cloudresourcemanager.googleapis.com`  
`gkeconnect.googleapis.com`  
`gkehub.googleapis.com` | 443 | TCP/HTTPS | Access is required for [fleet registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation).   
Cloud Logging Collector, which runs on cluster node | 1024 - 65535 | `oauth2.googleapis.com`  
`logging.googleapis.com`  
`stackdriver.googleapis.com`  
`servicecontrol.googleapis.com`  
`storage.googleapis.com`  
`www.googleapis.com` | 443 | TCP/HTTPS |   
Cloud Metadata Collector, which runs on cluster node | 1024 - 65535 | `opsconfigmonitoring.googleapis.com` | 443 | TCP/HTTPS |   
Cloud Monitoring Collector, which runs on cluster node | 1024 - 65535 | `oauth2.googleapis.com`  
`monitoring.googleapis.com`  
`stackdriver.googleapis.com`  
`servicecontrol.googleapis.com` | 443 | TCP/HTTPS |   
Cluster node | 1024 - 65535 | On-premises local Docker registry | Depends on your registry | TCP/HTTPS | Required if Google Distributed Cloud is configured to use a local private Docker registry instead of `gcr.io`.  
Cluster node | 1024 - 65535 | `gcr.io`  
`oauth2.googleapis.com`  
`storage.googleapis.com`  
Any Google API URL of the form `*.googleapis.com` required for the services enabled for the admin cluster. | 443 | TCP/HTTPS | Download images from public Docker registries. Not required if using a private Docker registry.  
Connect Agent, which runs on a cluster node | 1024 - 65535 | `cloudresourcemanager.googleapis.com`  
`gkeconnect.googleapis.com`  
`gkehub.googleapis.com`  
`www.googleapis.com`  
`iam.googleapis.com`  
`iamcredentials.googleapis.com`  
`oauth2.googleapis.com`  
`securetoken.googleapis.com`  
`sts.googleapis.com`  
`accounts.google.com` | 443 | TCP/HTTPS | For more information about the traffic managed by Connect Agent, see [Connect Agent overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent).  
Cluster node | 1024 - 65535 |  `gkeonprem.googleapis.com`  
`gkeonprem.mtls.googleapis.com`  
| 443 | TCP/HTTPS | Create and manage the cluster lifecycle on bare metal and VMware infrastructure.   
  
### Firewall rules for remaining components

The rules described in the following table apply to all other components not listed in the preceding section.

From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
Clients and application end users | All | VIP of Istio ingress | 80, 443 | TCP | End user traffic to the ingress service of a user cluster.  
Admin workstation | 32768 - 60999 | `gcr.io`  
`cloudresourcemanager.googleapis.com`  
`oauth2.googleapis.com`  
`storage.googleapis.com`  
Any `*.googleapis.com` URL required for the services enabled for this cluster | 443 | TCP/HTTPS | Download Docker images from public Docker registries.  
Admin workstation | 32768 - 60999 | `gcr.io`  
`cloudresourcemanager.googleapis.com`  
`iam.googleapis.com`  
`oauth2.googleapis.com`  
`serviceusage.googleapis.com`  
`storage.googleapis.com`  
Any `*.googleapis.com` URL required for the services enabled for the admin or user clusters | 443 | TCP/HTTPS | Preflight checks (validation).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
