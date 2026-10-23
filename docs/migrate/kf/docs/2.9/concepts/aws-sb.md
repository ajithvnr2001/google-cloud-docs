---
url: https://docs.cloud.google.com/migrate/kf/docs/2.9/concepts/aws-sb/
title: AWS Service Broker \u00a0|\u00a0 Kf 2.9 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:38.523598+00:00
---

# AWS Service Broker  |  Kf 2.9  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.9/concepts/aws-sb/

Version 2.9

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.9 ](https://docs.cloud.google.com/migrate/kf/docs/2.9)



Send feedback 

#  AWS Service Broker Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The AWS service broker is not an officially supported part of Kf.

The [AWS Service Broker](https://aws.amazon.com/partners/servicebroker/) exposes AWS Services through the [Open Service Broker (OSB)](https://github.com/openservicebrokerapi/servicebroker/blob/v2.15/spec.md) protocol. These docs are based on the [AWS Service Broker Documentation](https://github.com/awslabs/aws-servicebroker/tree/master/docs). This doc covers two possible installations:

  1. Install the AWS Service Broker in the Kf Kubernetes Cluster (recommended)
  2. Install the AWS Service Broker in AWS and exposing the API via a VPC bridge



## Prerequisites

In addition to a Kubernetes cluster with Kf and Service Catalog installed (see [these instructions](https://docs.cloud.google.com/docs/getting-started/install)), the following tools must be installed on the workstation where you will be using the `kf` CLI:

  1. **`helm`** : Follow [these instructions](https://helm.sh/docs/using_helm/) to install the `helm` CLI.



## Method 1: Install in GKE

The AWS Service Broker is deployed using the Helm chart from the [AWS Service Broker's getting started guide for Kubernetes](https://github.com/awslabs/aws-servicebroker/blob/master/docs/getting-started-k8s.md).

### Infrastructure

The AWS Service Broker requires a DynamoDB table and an IAM user to access the table. The easiest method is to deploy the [provided CloudFormation template](https://github.com/awslabs/aws-servicebroker/blob/master/setup/prerequisites.yaml). For manual installation, see the [prerequisite docs](https://github.com/awslabs/aws-servicebroker/blob/master/docs/install_prereqs.md).

### Helm

First, add the Helm repository to your machine:
    
    
    $ helm repo add aws-sb https://awsservicebroker.s3.amazonaws.com/charts
    

Then deploy the Helm chart, setting the correct AWS `accesskeyid` and `secretkey`:
    
    
    $ helm install aws-sb/aws-servicebroker \
      --name aws-servicebroker \
      --namespace aws-sb \
      --set aws.secretkey=REPLACEME \
      --set aws.accesskeyid=REPLACEME
    

If you don't want the broker installed cluster-wide set the flag `--set deployNamespacedServiceBroker=true` which will register the broker into the deployed Namespace.

A full list of configuration parameters can be found in [the Helm template's values.yaml definition](https://github.com/awslabs/aws-servicebroker/blob/master/packaging/helm/aws-servicebroker/values.yaml).

### Verification

After the Helm chart is deployed, a `ClusterServiceBroker` resource should have been created. You can check for it with `kubectl`:
    
    
    $ kubectl get ClusterServiceBroker aws-servicebroker
    
    NAME              URL                                                                    STATUS   AGE
    aws-servicebroker https://aws-servicebroker-aws-servicebroker.aws-sb.svc.cluster.local   Ready    3d
    

If the `STATUS` is not ready, there was an issue. Some things to check while troubleshooting are:

  * The DynamoDB infrastructure is up
  * The AWS User has access to the DynamoDB table via Policy or Group
  * The Helm chart values were set correctly



It may take several minutes for your broker to come up and register itself with Service Catalog. Once the broker is registed, you can view the provided services with the `kf marketplace` command.

## Method 2: Install in AWS

The downside to installing the AWS Service Broker in a GKE cluster is the required use of AWS User credentials instead of an AWS Role. However, the only required Kubernetes resource for the AWS Service Broker to work with Kf is the ClusterServiceBroker, assuming the AWS Service Broker's API is reachable from the GKE cluster.

There are two methods the API can be exposed to the GKE cluster:

  1. The API is accessible via a [VPN bridge between Google Cloud and AWS](https://medium.com/google-cloud/vpn-between-two-clouds-e2e3578be773)
  2. The API is publicly accessible (not recommended)



In either case, it is _strongly recommended_ to secure the Service Broker's API with a trusted TLS certificate and access credentials.

Once the API is accessible, `kubectl apply` a `ClusterServiceBroker` and a Kubernetes `Secret` which contains the credentials for authorizing with the Service Broker.
    
    
    apiVersion: servicecatalog.k8s.io/v1beta1
    kind: ClusterServiceBroker
    metadata:
      name: aws-sb
    spec:
      # For all configuration options, look at the service catalog's
      # type definitions:
      #  https://github.com/kubernetes-sigs/service-catalog/blob/master/pkg/apis/servicecatalog/v1beta1/types.go#L185
      url: https://replace.with.url.to.service.broker
      insecureSkipTLSVerify: false # use a trusted TLS certificate
      authInfo:
        bearer: # or basic
          secretRef:
            namespace: some-namespace
            name: some-secret-name
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
