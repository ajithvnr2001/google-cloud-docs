---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-a-proxy/
title: Use an HTTP proxy \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:52.399638+00:00
---

# Use an HTTP proxy  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-a-proxy/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use an HTTP proxy

This document shows you how to route traffic from the GKE on Azure through an HTTP/HTTPS proxy. You specify proxy configuration when you create a cluster.

## Overview

GKE on Azure can route outbound internet traffic through a proxy for the following reasons:

  * To register clusters with Google Cloud through [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview)
  * To run the Connect Agent
  * To download images from Container Registry



## Limitations

  * The `httpProxy` and `httpsProxy` fields do not support URLs beginning with `https://`. You must use `http://`. Requests to port 443 use HTTPS.
  * You must set values for `httpProxy`, `httpsProxy`, and `noProxy`. 
  * A cluster's proxy configuration— the resource group ID and secret ID— is immutable. You must create a new cluster and node pool to update these values.
  * You might need to add additional domains, IPs, or CIDRs to the `noProxy` field. We recommend adding your cluster's control planes subnet CIDRs (Pod address CIDR and Service address CIDR are added by default). 



## Prerequisites

This section describes the prerequisites you must apply before using a proxy.

### Azure Key Vault configuration

GKE on Azure stores proxy configuration information in Azure Key Vault. To configure a proxy with GKE on Azure, you need to have permissions to create a secret in a Key Vault. The Key Vault must be accessible from your cluster's VNet.

### Proxy Allowlist

For GKE on Azure to connect to Google Cloud services, the proxy server must allow traffic to specific Google and Microsoft domains.
    
    
    .azure.com
    .gcr.io
    cloudresourcemanager.googleapis.com
    container.googleapis.com
    gkeconnect.googleapis.com
    gkehub.googleapis.com
    oauth2.googleapis.com
    securetoken.googleapis.com
    storage.googleapis.com
    sts.googleapis.com
    www.googleapis.com
    servicecontrol.googleapis.com
    logging.googleapis.com
    monitoring.googleapis.com
    opsconfigmonitoring.googleapis.com
    GCP_LOCATION-gkemulticloud.googleapis.com
    

Replace `GCP_LOCATION` with the Google Cloud region in which your cluster resides. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions).

### Subnet Network Security Group requirement

If you're using Network Security Groups (NSGs) to manage traffic to your subnets, your NSG rules must allow outgoing TCP traffic to following destinations:

  * AzureCloud: TCP, port 80 and 443



See [Azure service tags](https://docs.microsoft.com/en-us/azure/virtual-network/service-tags-overview#available-service-tags) for more information about using service tags with NSGs. 

## Create a proxy configuration file

The proxy configuration is stored in an Azure Key Vault secret as a JSON string. You can pass this configuration to the `az` command-line tool as a file. This section describes how to create that file.

The following table describes the contents of this file.

**Field** | **Description** | **Examples** | **Required**  
---|---|---|---  
`httpProxy` | A proxy server URL. The value should include a hostname/IP address and optionally a port, username, and password. | `"http://user:password@10.184.37.42:80"`  
`"10.184.37.42"` | Yes  
`httpsProxy` |  A proxy URL for encrypted, HTTPS traffic. The httpProxy URL will be used if httpsProxy has an empty value. | `"http://10.101.16.31:80"` | Yes  
`noProxy` |  A comma-separated list of URLs to exclude from proxying. Each value can be an IP address, a CIDR range, a domain name, or the asterix character (*). Domains specified with a leading dot (for example, `.google.com`) indicate that a subdomain is required. A single asterix * ignores all proxy configuration.  | `"1.2.3.4,10.0.0.0/16,example.com,.site.com"` | Yes  
  
  1. To create the configuration file, create a JSON file that contains values for `httpProxy`, `noProxy`, and optional `httpsProxy` keys.
         
         {
           "httpProxy": "AUTHENTICATION_URL",
           "httpsProxy": "AUTHENTICATION_URL",
           "noProxy": "NO_PROXY_ADDRESSES"
         }
         

Replace the following:

     * `AUTHENTICATION_URL`: Encoded URL containing the proxy username and the password
     * `NO_PROXY_ADDRESSES`: Comma-separated list of CIDR blocks and URLs— for example `10.0.0.0/16,http://example.com`

Save the file to use in the following section.

  2. Create a secret with this JSON data as a secret in Azure Key Vault using the `az` command-line tool.
         
         az keyvault secret set --name SECRET_NAME \
         --vault-name KEY_VAULT_NAME \
         --file PROXY_CONFIGURATION_FILE
         

Replace the following:

     * `SECRET_NAME`: the name of the new secret
     * `KEY_VAULT_NAME`: the name of your Key Vault
     * `PROXY_CONFIGURATION_FILE`: the path to your proxy configuration file.

The output includes the secret's name and contents. You can now reference this secret when you create a cluster.




## Create a cluster that uses a proxy

To configure GKE on Azure to use an HTTP proxy for outbound connectivity, perform the following steps:

Follow the steps in [Create a cluster and node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster) and pass the `--proxy-resource-group-id` and `--proxy-secret-id` flags.
    
    
    gcloud container azure clusters create CLUSTER_NAME \
      --proxy-resource-group-id=PROXY_RESOURCE_GROUP_ID \
      --proxy-secret-id=PROXY_SECRET_ID
        ...
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `PROXY_RESOURCE_GROUP_ID`: the resource group that hosts your cluster
  * `PROXY_SECRET_ID`: the ID of the secret that contains your proxy configuration— for example, `https://VAULT_NAME.vault.azure.net/secrets/SECRET_NAME/SECRET_VERSION`



## What's next

  * Read additional information on how to [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
