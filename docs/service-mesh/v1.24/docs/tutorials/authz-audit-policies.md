---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/tutorials/authz-audit-policies/
title: Configuring audit policies for your services \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:49.651816+00:00
---

# Configuring audit policies for your services  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/tutorials/authz-audit-policies/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuring audit policies for your services

Note: This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview). 

**Preview — Audit policy**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial only supports the in-cluster [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.24/docs/check-control-plane-implementation).

An audit policy lets you audit data access to your services in Cloud Service Mesh. Auditing your services helps you answer the questions "who did what, when, and possibly why." With an audit policy, you can specify when an audit log is created and the content of the logs. This guide explains how to install Cloud Service Mesh so that you can use an audit policy.

Because you view the audit logs in the [Cloud Logging](https://docs.cloud.google.com/logging) Logs Explorer in the Google Cloud console, audit policies are supported only on the following platforms:

  * GKE on Google Cloud
  * Google Distributed Cloud (software only) for VMware
  * Google Distributed Cloud (software only) for bare metal



An audit policy extends [AuthorizationPolicy](https://istio.io/v1.24/docs/reference/config/security/authorization-policy/) by adding an `AUDIT` action. It takes effect only in its target policy scope (which can be a workload, a namespace, or the entire mesh). The policies are `ORed` together, that is, a request is logged if any policy says so. If no audit policy applies to a given workload, no audit log is generated for that workload.

Here is an example audit policy to audit all WRITE access to the `/user/profile/*` path in `myapi`:
    
    
      apiVersion: security.istio.io/v1beta1
      kind: AuthorizationPolicy
      metadata:
        namespace: ns1
        name: anyname
      spec:
        selector:
          matchLabels:
            app: myapi
        action: AUDIT
        rules:
        - to:
          - operation:
              methods: ["POST", "UPDATE", "DELETE"]
              paths: ["/user/profile/*"]
    

## Limitations

  * There is no audit log on the ingress-gateway.
  * The audit content isn't configurable.
  * Currently, the Cloud Service Mesh audit logs have the same reliability property as normal access logs. For example, if a workload Pod is restarted, some audit logs for the workload, if not persisted, can be lost.



## Before you begin

Follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools) to: 

  * [Install required tools](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#install_required_tools)
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#download_asmcli)
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#grant_cluster_admin_permissions)
  * [Validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#validate_project_and_cluster)



## Prepare gateway configuration

Cloud Service Mesh gives you the option to deploy and manage gateways as part of your service mesh. A gateway describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. Gateways are Envoy proxies that provide you with fine-grained control over traffic entering and leaving the mesh.

`asmcli` doesn't install the `istio-ingressgateway`. We recommend that you deploy and manage the control plane and gateways separately. For more information, see [Installing and upgrading gateways](https://docs.cloud.google.com/service-mesh/v1.24/docs/gateways).

## Customizing the Cloud Service Mesh installation

To use an audit policy, customize the Cloud Service Mesh installation:

### Installs

  1. Follow the steps in [Install Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/unified-install/install-anthos-service-mesh). When you run `asmcli install`, include the following option:
         
         --option audit-authorizationpolicy
         

For example:
         
         ./asmcli install \
           --project_id PROJECT_ID \
           --cluster_name CLUSTER_NAME \
           --cluster_location CLUSTER_LOCATION \
           --ca mesh_ca \
           --output_dir DIR_PATH  \
           --enable_all \
           --option audit-authorizationpolicy
         

Be sure to specify any other overlay files that you need to configure Cloud Service Mesh.

  2. Complete the Cloud Service Mesh installation to enable automatic sidecar proxy injection on your workloads. See [Deploy and redeploy workloads](https://docs.cloud.google.com/service-mesh/v1.24/docs/unified-install/install-anthos-service-mesh#deploy_and_redeploy_workloads).




### Upgrades

  1. Follow the steps in [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/unified-install/upgrade). When you run `asmcli install`, include the following option:
         
         --option audit-authorizationpolicy
         

For example:
         
         ./asmcli install \
           --project_id PROJECT_ID \
           --cluster_name CLUSTER_NAME \
           --cluster_location CLUSTER_LOCATION \
           --ca mesh_ca \
           --output_dir DIR_PATH  \
           --enable_all \
           --option audit-authorizationpolicy
         

Be sure to specify any other overlay files that you need to configure Cloud Service Mesh.

  2. Complete the Cloud Service Mesh installation to enable automatic sidecar proxy injection on your workloads. For details see [Switch to the new control plane](https://docs.cloud.google.com/service-mesh/v1.24/docs/unified-install/upgrade#switch_to_the_new_control_plane)




## Using audit logging

This section uses the Bookinfo sample to demonstrate how to use audit logging.

  1. Deploy the [Bookinfo](https://docs.cloud.google.com/service-mesh/v1.24/docs/deploy-bookinfo) sample application to the default namespace.

  2. Get the external IP address of the ingress gateway, and [send requests](https://docs.cloud.google.com/service-mesh/v1.24/docs/deploy-bookinfo#validating_the_application_deployment) to the sample application to generate some traffic.

  3. In the Google Cloud console, go to the navigation menu menu and select **Logging** > **Logs Explorer** :  


[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  4. Select a Google Cloud project.

  5. Because you haven't deployed an audit policy yet, there won't be any audit logs. Note that the audit log is different from the access log. To see `stackdriver` access logs, enter the following query in the **Query builder** field, and click **Run query** :
         
         logName="projects/PROJECT_ID/logs/server-accesslog-stackdriver"
         

For more information on using Logs Explorer, see [Logs Explorer overview](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary).




### Configuring the audit policy and checking audit logs

This section provides several options for auditing the Bookinfo application. After you deploy the audit policy, you can send some requests and then check the audit log in the Logs Explorer.

  1. Enter the following command to get [authentication credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#default_cluster_kubectl%22) to interact with the cluster. This command also sets the current context for `kubectl` to the cluster.
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --project=PROJECT_ID \
             --zone=CLUSTER_LOCATION
         

**Note:** For regional cluster replace `--region` with `--zone`.
  2. Apply the following audit policy to audit `GET` requests to the `/productpage` path:
         
         kubectl apply -f - << EOF
         apiVersion: "security.istio.io/v1beta1"
         kind: "AuthorizationPolicy"
         metadata:
           name: "audit-productpage"
           namespace: default
         spec:
           action: AUDIT
           rules:
           - to:
             - operation:
                 methods: ["GET"]
                 paths: ["/productpage"]
         EOF
         

  3. Send some requests to Bookinfo.

  4. In Logs Explorer, enter the following query in the **Query builder** field, and click **Run query** :
         
         logName="projects/PROJECT_ID/logs/server-istio-audit-log"
         

The query returns logs similar to the following:

![image](https://docs.cloud.google.com/service-mesh/v1.24/images/authz-audit-productpage.png)

  5. Apply the following policy to audit requests to the `bookinfo-ratings` service. The audit policies are additive. After applying the following policy, you see audit logs for requests to both ProductPage and Ratings.
         
         kubectl apply -f - << EOF
         apiVersion: "security.istio.io/v1beta1"
         kind: "AuthorizationPolicy"
         metadata:
           name: "audit-ratings"
           namespace: default
         spec:
           action: AUDIT
           rules:
           - from:
             - source:
                 principals: ["cluster.local/ns/default/sa/bookinfo-ratings"]
             to:
             - operation:
                 methods: ["GET"]
         EOF
         

The new audit policy has to propagate first before it takes effect.

  6. Send 10 or more requests to Bookinfo to make sure you hit the ratings service, and then check the audit log in Logs Explorer. The audit log looks similar to the following:

![image](https://docs.cloud.google.com/service-mesh/v1.24/images/authz-audit-ratings.png)

  7. Apply the following policy to audit to all services in the default namespace.
         
         kubectl apply -f - << EOF
         apiVersion: security.istio.io/v1beta1
         kind: AuthorizationPolicy
         metadata:
           namespace: default
           name: "audit-all"
         spec:
           action: AUDIT
           rules:
             - {}
         EOF
         

  8. Send some more requests to Bookinfo, and then check the audit log in Logs Explorer. The audit log now logs all requests:

![image](https://docs.cloud.google.com/service-mesh/v1.24/images/authz-audit-all.png)

  9. If you want to restrict the audit policy back down to ProductPage and Ratings, you can delete the `audit-all` policy:
         
         kubectl delete authorizationpolicy audit-all -n default
         




## Troubleshooting

If you don't see any audit logs after enabling an audit policy, here are a few things you can check:

  1. Make sure there is traffic for the time period specified in Logs Explorer. If you are testing with Bookinfo, you can send requests by running the following command several times:
         
         curl -s http://EXTERNAL_IP/productpage | grep Bookstore
         

  2. Check if there is an `AuthorizationPolicy` on the ingress gateway that blocks requests to the audited service.

  3. Check the `stackdriver` access logs with the following filter in the Logs Explorer to verify if your requests have reached the application:
         
         logName="projects/PROJECT_ID/logs/server-accesslog-stackdriver"
         

![image](https://docs.cloud.google.com/service-mesh/v1.24/images/authz-audit-accesslog.png)

  4. To make sure Stackdriver is configured and audit log is enabled, dump the configuration of current the `istiod` state. In the `config_dump` search for `enable_audit_log` and your audit policy's name.
         
         istioctl dashboard envoy POD_NAME.NAMESPACE
         

![image](https://docs.cloud.google.com/service-mesh/v1.24/images/authz-audit-config1.png)![image](https://docs.cloud.google.com/service-mesh/v1.24/images/authz-audit-config2.png)![image](https://docs.cloud.google.com/service-mesh/v1.24/images/authz-audit-config3.png)

  5. To make sure your requests are matched with audit policy rules, you can check role-based access control (RBAC) debug logs. Turn on RBAC debug logging with the following command:
         
         kubectl exec POD_NAME -n NAMESPACE -c istio-proxy -- pilot-agent request POST 'logging?rbac=debug'
         

  6. Send some requests, and then check logs for the Pod with the `kubectl logs` command:
         
         kubectl logs POD_NAME -n NAMESPACE -c istio-proxy
         




## What's next

  * [Learn about security in Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/security/security-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
