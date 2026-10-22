---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/apis-overview/
title: Google Distributed Cloud air-gapped APIs overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:47.317585+00:00
---

# Google Distributed Cloud air-gapped APIs overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/apis-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Google Distributed Cloud air-gapped APIs overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped application programming interfaces (APIs) are programmatic interfaces to the GDC platform services. Google builds the control-plane APIs on top of Kubernetes, using the Kubernetes Resource Model (KRM). The control plane performs resource management for services such as creation, deletion, and updates.

Specific services have these APIs and their own data-plane APIs, which are XML, JSON, or gRPC-based. This page covers these services in their respective sections.

## About GDC APIs

There are two types of GDC APIs: those that are Kubernetes-based and those that are not. Many GDC APIs are extensions to the open source Kubernetes API. They use Kubernetes custom resources and rely on the KRM. These APIs, like the Kubernetes API, are HTTP-based RESTful APIs, accepting and returning JSON as the default, or in Protobuf. The API endpoint is the relevant Kubernetes server.

Other, non-Kubernetes based GDC APIs, such as the Vertex pre-trained AI APIs, have their own endpoints. In addition to supporting HTTP, some of these APIs may also be accessible by gRPC, the open-source remote-procedure call framework. For more information on specific APIs, see their dedicated documentation in the vertical navigation menu.

To access GDC APIs, use the [gdcloud CLI tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) or GDC console.

## About the Kubernetes API and the KRM

As many of the GDC APIs are extensions to the Kubernetes API and rely on the KRM, an understanding of these concepts help you take advantage of GDC APIs to their full extent.

The Kubernetes API is fully declarative, and everything in the Kubernetes API is a resource that follows the KRM. API clients, both human and machine, act on those resources, often with create, read, update, and delete (CRUD) operations. The Kubernetes database stores the resource and represents the state of the system. Kubernetes continuously watches those resources and reconciles the real state of the system with the desired state. For example, if you update a `Deployment` resource to indicate that you want five replicas of your container instead of four, Kubernetes detects the change in the desired number of replicas and creates an additional container.

For the core Kubernetes API, Kubernetes performs the reconciliation between desired and real states itself. The Kubernetes API extensions are custom resources that are not part of the core Kubernetes API. The custom software continuously watches and interacts with the Kubernetes API and performs the reconciliation.

To learn more about the Kubernetes API and the Kubernetes resource model, read the official Kubernetes documentation.

  * Kubernetes API Overview, at [_https://kubernetes.io/docs/reference/using-api/_](https://kubernetes.io/docs/reference/using-api/)
  * Kubernetes API Concepts, at [_https://kubernetes.io/docs/reference/using-api/api-concepts/_](https://kubernetes.io/docs/reference/using-api/api-concepts/)
  * The Kubernetes Resource Model (KRM), at [_https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md_](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md)



## Global and zonal APIs

Resources in GDC air-gapped are either zonal resources or global resources. Zonal resources operate within a single zone independently, and a zonal outage can affect some or all of the resources in that zone. Global resources operate with redundancy across multiple zones for fault tolerance.

GDC air-gapped offers two levels of management plane APIs to create and manage both GDC resource types: global APIs and zonal APIs.

Both global and zonal APIs are Kubernetes declarative APIs served at different endpoints, and GDC resources are represented as Kubernetes custom resources in the API servers. The global API servers share a single etcd cluster distributed across zones to provide strong consistency with fault tolerance, at the cost of higher latency and reduced write queries per second (QPS) compared to the zonal API servers. In every organization, a zonal management API server provides the zonal API for administrators and developers to manage zonal resources, and a global management API server provides the global API to manage multi-zone resources.

## GDC APIs access

Both the gdcloud CLI tools and the GDC console leverage the GDC APIs. Google recommends that you use those to explore GDC or to do one-off operations. However, if you use automated or programmatic access to GDC, Google recommends that you use the GDC APIs directly.

### HTTP and gRPC support

Most GDC APIs provide a JSON HTTP interface that you call directly. The Kubernetes-based APIs use the Kubernetes client libraries. Some non-Kubernetes GDC APIs have a gRPC interface, which provides improved performance and usability. Google also provides client libraries for GDC APIs that aren't based on Kubernetes. To read more about gRPC, go to [_https://grpc.io/_](https://grpc.io/). 

### TLS encryption

All GDC APIs accept requests using the Transport Layer Security (TLS) encryption.

  * If you are using one of the Kubernetes or GDC client libraries, the library handles in-transit encryption for you.
  * If you are using your own HTTP or gRPC client, you must authenticate with GDC, which requires TLS. For gRPC, follow the instructions in the gRPC authentication guide at [_https://grpc.io/docs/guides/auth/_](https://grpc.io/docs/guides/auth/). 

**Note:** GDC recommends that you use existing clients, especially ones Google provides, to interact with GDC APIs. Creating your own API client is an arduous software-engineering task that, if done incorrectly, might lead to unforeseen behaviors in your systems that are difficult to diagnose.

### Access the Kubernetes API and Kubernetes-based APIs

The `kubectl` Kubernetes CLI is the primary way to work directly with the Kubernetes API and any Kubernetes-based APIs.

#### Access with kubectl

When accessing the Kubernetes API for the first time, use the Kubernetes command-line tool, `kubectl`.

To access a cluster, you need the cluster location information and the credentials to access it. See the [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) section to learn how to get access to those credentials.

Examine your current `kubectl` configuration and see the clusters to which you have access:
    
    
    kubectl config view
    

#### Generate API endpoint descriptions

To view a list of API endpoints available for all service APIs in GDC air-gapped, you can generate API descriptions following the OpenAPI Specification in JSON format. You can view the generated JSON for the API endpoints in tools such as Swagger.

Complete the following steps to generate the management and data plane API endpoint descriptions in JSON format:

  1. Create a proxy server between your environment and the management API server:
         
         kubectl proxy --kubeconfig MANAGEMENT_API_SERVER
         

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file of the management API server. For more information, see [Zonal Management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

  2. Download the list of API endpoint descriptions in JSON format:
         
         curl -s http://127.0.0.1:8001/openapi/v2 | jq 'if .paths then .paths = (.paths \
             | with_entries(select(.key | contains(".private") | not))) else . end' > k8s_swagger.json
         

  3. Open the generated `k8s_swagger.json` file in a tool such as Swagger to view the API endpoint descriptions.




#### Direct access to the API with an HTTP client

The following are ways to directly access the REST API with an HTTP client like `curl`, `wget`, or a browser:

  * Rely on `kubectl` to handle the authentication by using it in proxy mode.
  * Handle the authentication yourself.



##### Run kubectl proxy

The `kubectl proxy` command runs `kubectl` in a mode where it acts as a reverse proxy. This command connects to the `apiserver` and manages the authentication.

Running `kubectl` in proxy mode uses the stored API server location and verifies the identity of the API server using a certificate. This method guards against man-in-the-middle (MITM) attacks.

The following example shows how to use the `kubectl proxy` command:
    
    
    kubectl proxy --port=8080 &
    

Once the `kubectl` proxy is running, you can explore the API with `curl`, `wget`, or a browser, as shown in the following:
    
    
    $ curl http://localhost:8080/api/
    {
      "versions": [
        "v1"
      ],
      "serverAddressByClientCIDRs": [
        {
          "clientCIDR": "0.0.0.0/0",
          "serverAddress": "10.0.1.149:443"
        }
      ]
    }
    

##### Run without kubectl proxy

If you don't want to run `kubectl` in proxy mode, you can pass an authentication token directly to the API server.

  1. List all possible Kubernetes clusters you have access to, as your kubeconfig file might have multiple contexts:
         
         kubectl config view \
             -o jsonpath='{"Cluster name\tServer\n"}{range.clusters[*]}{.name}{"\t"}{.cluster.server}{"\n"}{end}'
         

  2. Export the name of the Kubernetes cluster you want to interact with from the previous output:
         
         export CLUSTER_NAME="CLUSTER_NAME"
         

  3. Set the API server referring to the Kubernetes cluster name:
         
         APISERVER=$(kubectl config view -o jsonpath="{.clusters[?(@.name==\"$CLUSTER_NAME\")].cluster.server}")
         

  4. Create a secret to hold a token for the default service account:
         
         kubectl apply -n NAMESPACE -f - <<EOF
         apiVersion: v1
         kind: Secret
         metadata:
           name: default-token
           annotations:
             kubernetes.io/service-account.name: default
         type: kubernetes.io/service-account-token
         EOF
         

  5. Wait for the token controller to populate the secret with a token:
         
         while ! kubectl describe secret default-token | grep -E '^token' >/dev/null; do
           echo "waiting for token..." >&2
           sleep 1
         done
         

  6. Set the token value:
         
         TOKEN=$(kubectl get secret $(kubectl get secrets | grep default | cut -f1 -d ' ')  \
             -o jsonpath='{.data.token}' | base64 --decode)
         

  7. To access the API, use the token with a tool like `curl` by adding the HTTP header `Authorization: Bearer $TOKEN` as shown in the following example:
         
         $ curl -k $APISERVER/api --header "Authorization: Bearer $TOKEN"
         

The output is similar to the following:
         
         {
           "kind": "APIVersions",
           "versions": [
             "v1"
           ],
           "serverAddressByClientCIDRs": [
             {
               "clientCIDR": "0.0.0.0/0",
               "serverAddress": "10.0.1.149:443"
             }
           ]
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
