---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-a-proxy/
title: Use an HTTP proxy \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:36.579551+00:00
---

# Use an HTTP proxy  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-a-proxy/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use an HTTP proxy Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to route traffic from the GKE on AWS through an HTTP/HTTPS proxy. You specify proxy configuration when you create a cluster.

## Overview

GKE on AWS can route outbound internet traffic through a proxy for the following reasons:

  * To register clusters with Google Cloud through [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview)
  * To run the Connect Agent
  * To download images from Container Registry



## Limitations

  * The `httpProxy` and `httpsProxy` fields do not support URLs beginning with `https://`. You must use `http://`. Requests to port 443 use HTTPS.
  * You must set values for `httpProxy`, `httpsProxy`, and `noProxy`. 
  * You might need to add additional domains, IPs, or CIDRs to the `noProxy` field. We recommend adding the VPC IP range. As of Google Kubernetes Engine version 1.22, GKE on AWS automatically adds the Pod address CIDR and Service address CIDR. 



## Prerequisites

This section describes the prerequisites you must apply before using a proxy.

### Enable VPC endpoints

Before you configure a proxy, you must create [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) for your GKE on AWS installation.

VPC endpoints let resources in private subnets access AWS services without public internet access.

The following table lists the AWS services that GKE on AWS requires VPC endpoints for, along with the type of endpoint and the [Security Groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups) that require access to the endpoint.

Service | Endpoint type | Security groups  
---|---|---  
[Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/aws-auto-scaling-vpc-endpoints.html) | Interface | Control plane, node pools  
[EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html) | Interface | Control plane, node pools  
[EFS](https://docs.aws.amazon.com/efs/latest/ug/efs-vpc-endpoints.html) | Interface | Control plane  
[Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-vpc-endpoints.html) | Interface | Control plane, node pools  
[Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html) | Interface | Control plane, node pools  
[S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) | Gateway | Control plane, node pools  
[Secrets Manager](https://docs.aws.amazon.com/secretsmanager/index.html) | Interface | Control plane, node pools  
[Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) | Interface | Control plane, node pools  
**Important:** You must enable [Private DNS](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-private-dns) (also called **Enable DNS name** on the AWS console) on interface endpoints.

You can create endpoints from the AWS [VPC Console](https://console.aws.amazon.com/vpc/home). The options you set when creating VPC endpoints depend on your VPC configuration.

### Define a security group

GKE on AWS must be able to connect to the proxy server to download software components. Create or locate an AWS [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) that allows outbound connections to your proxy server. The security group should allow outbound access from your Control plane, and Node pool security groups to the proxy address and port. Save the ID of this security group— for example, `sg-12345678`.

Type | Protocol | From port | To port | Address  
---|---|---|---|---  
Egress | TCP | Proxy port | Proxy port | Proxy security group  
  
### Proxy Allowlist

For GKE on AWS to connect to Google Cloud services, the proxy server must allow traffic to the following domains.
    
    
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
    

Replace `GCP_LOCATION` with the Google Cloud region in which your GKE on AWS cluster resides. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions).

### Update AWS IAM roles

For GKE on AWS to read proxy configuration from AWS Secrets Manager, you must add the `secretsmanager:GetSecretValue` to your cluster's [Control plane role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_the_control_plane_role) and [Node pool role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_a_node_pool_iam_role).

To add this permission, add it to your control plane and node pool policy. For more information, see [Editing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html).

## Create a proxy configuration file

The proxy configuration is stored in an AWS Secrets Manager secret as a JSON string. You can pass this configuration to the `aws` command-line tool as a file. This section describes how to create that file.

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

  2. Create a secret with this JSON data as a secret in AWS Secrets Manager using the `aws` command-line tool.
         
         aws secretsmanager create-secret \
         --name SECRET_NAME \
         --secret-string file://PROXY_CONFIGURATION_FILE
         

Replace the following:

     * `SECRET_NAME`: the name of the new secret
     * `PROXY_CONFIGURATION_FILE`: the path to your proxy configuration file.

The output includes the secret's Amazon resource name (ARN) and contents. You can now reference this secret when you create a cluster.




## Create a cluster that uses a proxy

To configure GKE on AWS to use an HTTP proxy for outbound connectivity, perform the following steps:

Follow the steps in [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster) and pass the `proxy-secret-arn` and `proxy-secret-version-id` flags.
    
    
    gcloud container aws clusters create CLUSTER_NAME \
      --proxy-secret-arn=PROXY_SECRET_ARN \
      --proxy-secret-version-id=PROXY_SECRET_VERSION \
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `PROXY_SECRET_ARN`: the ARN of the secret that contains proxy settings— for example `arn:aws::secretsmanager:us-east-2:111122223333:secret:example/ExampleSecret-jiObOV`
  * `PROXY_SECRET_VERSION`: the secrets's version ID— for example, `EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE`



## Update proxy configuration

You can update the proxy configuration for a cluster control plane or a node pool. To update the proxy configuration ARN, you must first update the control plane or node pool AWS IAM role.

### Update AWS IAM roles

Before you change the ARN where the proxy configuration is stored, you need to confirm that your cluster's [Control plane role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_the_control_plane_role) and [Node pool role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_a_node_pool_iam_role) have read access to the secret ARN. If your IAM statement with the `secretsmanager:GetSecretValue` permission is scoped to specific resource ARNs, add the new secret ARN to that list before updating proxy configuration.

### Update cluster proxy configuration

To update your cluster's proxy configuration, use the Google Cloud CLI.
    
    
    gcloud container aws clusters update  CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --proxy-secret-arn=PROXY_SECRET_ARN \
        --proxy-secret-version-id=PROXY_SECRET_VERSION
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster
  * `PROXY_SECRET_ARN`: the ARN of the secret that contains proxy settings
  * `PROXY_SECRET_VERSION`: the secrets's version ID— for example, `EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE`



### Update node pool proxy configuration

To update your node pool's proxy configuration, use the Google Cloud CLI.
    
    
    gcloud container aws node-pools update NODE_POOL_NAME
        --cluster CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --proxy-secret-arn=PROXY_SECRET_ARN \
        --proxy-secret-version-id=PROXY_SECRET_VERSION
    

Replace the following:

  * `NODE_POOL_NAME`: your node pool's name
  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster
  * `PROXY_SECRET_ARN`: the ARN of the secret that contains proxy settings
  * `PROXY_SECRET_VERSION`: the secrets's version ID— for example, `EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE`



### Remove proxy configuration

You can remove proxy configuration from the cluster control plane or node pools. These operations are independent. Removing configuration from the control plane doesn't remove it from the cluster's node pools.

#### Remove control plane proxy configuration

To remove your cluster control plane's proxy configuration, use the Google Cloud CLI.
    
    
    gcloud container aws clusters update  CLUSTER_NAME \
      --location GOOGLE_CLOUD_LOCATION \
      --clear-proxy-config
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster—for example, `us-west1`



#### Remove node pool proxy configuration

To remove proxy configuration from a node pool, use the Google Cloud CLI.
    
    
    gcloud container aws node-pools update NODE_POOL_NAME
      --cluster CLUSTER_NAME \
      --location GOOGLE_CLOUD_LOCATION \
      --clear-proxy-config
    

Replace the following:

  * `NODE_POOL_NAME`: your node pool's name
  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions) that manages your cluster—for example, `us-west1`



## What's next

  * Read additional information on how to [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
