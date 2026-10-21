---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting/
title: Troubleshoot cluster connections \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:13.753795+00:00
---

# Troubleshoot cluster connections  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Troubleshoot cluster connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot common errors that you might encounter when registering clusters to a fleet or connecting to clusters outside of Google Cloud using the Google Cloud console, the Google Cloud CLI, or `kubectl` through the [Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).

On-premises clusters and clusters on other public clouds depend on the [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent) to establish and maintain a connection between the cluster and your Google Cloud project, and to handle Kubernetes requests. If you see errors such as "Unreachable Agent" or "Failed to connect to cluster's control plane" this could indicate a problem with the Connect Agent.

For a high-level view of GKE troubleshooting, see [Introduction to GKE troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction).

## Collecting Connect Agent logs

When you register a cluster outside Google Cloud, it uses the Connect Agent to handle communication between your cluster and your fleet host project. The Connect Agent is a Deployment, `gke-connect-agent`, typically installed in your cluster in the namespace `gke-connect`. Collecting logs from this Connect Agent can be useful for troubleshooting registration and connection issues.

You can retrieve the Agent's logs by running the following command (adjust the count of lines if necessary):
    
    
    kubectl logs -n gke-connect -l app=gke-connect-agent --tail=-1
    

To get information about every Connect Agent running in your project clusters:
    
    
    kubectl describe deployment --all-namespaces -l app=gke-connect-agent
    

A successful connection should have entries similar to the below example:

**Note:** All logs are in UTC.
    
    
    2019/02/16 17:28:43.312056 dialer.go:244: dialer: dial: connected to gkeconnect.googleapis.com:443
    2019/02/16 17:28:43.312279 tunnel.go:234: serve: opening egress stream...
    2019/02/16 17:28:43.312439 tunnel.go:248: serve: registering endpoint="442223602236", shard="88d2bca5-f40a-11e8-983e-42010a8000b2" {"Params":{"GkeConnect":{"endpoint_class":1,"metadata":{"Metadata":{"Default":{"manifest_version":"234227867"}}}}}} ...
    2019/02/16 17:28:43.312656 tunnel.go:259: serve: serving requests...

## Collecting GKE Identity Service logs

Inspecting the GKE Identity Service logs may be helpful if you are having issues with [Google Groups](https://cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups) or [third-party support](https://cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-third-party) for Connect gateway. This method of generating logs is only applicable to clusters in Google Distributed Cloud deployments on VMware or bare metal.

  1. Increase the verbosity of GKE Identity Service logs by making an edit to the clientconfig custom resource with the following command:
         
         kubectl edit deployment -n anthos-identity-service
         

and adding a `vmodule` flag under the `containers` field like so:
         
         spec:
           containers:
           ...
           - command:
             - --vmodule=cloud/identity/hybrid/charon/*=9
         

**Note:** Increasing the verbosity by adding the `vmodule` flag as described will print the maximum amount of details, including secrets.
  2. Restart the GKE Identity Service pod by deleting it with the following command:
         
         kubectl delete pods -l k8s-app=ais -n anthos-identity-service
         

A pod should turn up again within a few seconds.

  3. Once the pod has restarted, run the original command which was returning an unexpected response to populate the GKE Identity Service pod logs with more details.

  4. Save the output of these logs to a file using the following command:
         
         kubectl logs -l k8s-app=ais -n anthos-identity-service --tail=-1 > gke_id_service_logs.txt
         

**Note:** All logs are in UTC.



If expected groups are missing from the GKE Identity Service pod logs, verify the setup for the cluster is correct. If there are other GKE Identity Service related issues, refer to [Troubleshoot user access issues](https://cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting) or [Troubleshooting fleet-level setup issues](https://cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-troubleshooting).

## `tls: oversized record` errors

Symptom
    

You might encounter an error like this one:
    
    
    ... dialer: dial: connection to gkeconnect.googleapis.com:443 failed after
    388.080605ms: serve: egress call failed: rpc error: code = Unauthenticated
    desc = transport: oauth2: cannot fetch token: Post
    https://oauth2.googleapis.com/token: proxyconnect tcp: tls: oversized record
    received with length 20527

Possible causes
    

This can mean that the Connect Agent is trying to connect via HTTPS to an HTTP-only proxy. The Connect Agent only supports [CONNECT](https://en.wikipedia.org/wiki/HTTP_tunnel)-based HTTP proxies.

Resolution
    

You need to reconfigure your proxy environment variables to the following:
    
    
    http_proxy=http://[PROXY_URL]:[PROXY_PORT]
    https_proxy=http://[PROXY_URL]:[PROXY_PORT]
    

## `oauth2: cannot fetch token` errors

Symptom
    

You might encounter an error like this one:
    
    
    ...  dialer: dial: connection to gkeconnect.googleapis.com:443 failed
    after 388.080605ms: serve: egress call failed: rpc error: code =
    Unauthenticated desc = transport: oauth2: cannot fetch token: Post
    https://oauth2.googleapis.com/token: read tcp 192.168.1.40:5570->1.1.1.1:80
    read: connection reset by peer

Possible causes
    

This can mean that the upstream HTTP proxy reset the connection, most likely because this particular URL is not allowed by your HTTP proxy. In the example above, the 1.1.1.1:80 is the HTTP proxy address.

Resolution
    

Check that your HTTP proxy allowlist includes the following URLs/domains:
    
    
    gkeconnect.googleapis.com
    oauth2.googleapis.com/token
    www.googleapis.com/oauth2/v1/certs
    

## Connect Agent pod crash and restart errors

Symptom
    

You might encounter intermittent "Unreachable Agent" errors in the Google Cloud console for your cluster and/or you might find the Pod has restarted multiple times:
    
    
    $ kubectl get pods -n gke-connect
    NAME                                                READY   STATUS    RESTARTS   AGE
    gke-connect-agent-20230706-03-00-6b8f75dd58-dzwmt   1/1     Running   5          99m
    
    

To troubleshoot this behavior, describe the Pod to see if its last state was terminated due to an out of memory error (OOMKilled).:
    
    
      kubectl describe pods/gke-connect-agent-20230706-03-00-6b8f75dd58-dzwmt -n gke-connect
            <some details skipped..>
            Last State:     Terminated
            Reason:       OOMKilled
    

Possible causes
    By default, Connect Agent Pods have a 256MiB RAM limit. If the cluster has installed a lot of workloads, it's possible that some of the requests and responses cannot be handled as expected.
Resolution
    

Update Connect Agent deployment and grant it a higher memory limit, for example:
    
    
    containers:
      name: gke-connect-agent-20230706-03-00
      resources:
        limits:
          memory: 512Mi
    

## `PermissionDenied` errors

Symptom
    

You might encounter an error like this one:
    
    
    tunnel.go:250: serve: recv error: rpc error: code = PermissionDenied
    desc = The caller does not have permission
    dialer.go:210: dialer: dial: connection to gkeconnect.googleapis.com:443
    failed after 335.153278ms: serve: receive request failed: rpc error:
    code = PermissionDenied desc = The caller does not have permission
    dialer.go:150: dialer: connection done: serve: receive request failed:
    rpc error: code = PermissionDenied desc = The caller does not have permission
    dialer.go:228: dialer: backoff: 1m14.1376766s

Possible causes
    

This can mean that you have not bound the required Identity and Access Management (IAM) role to the Google Cloud service account you created to authorize the Connect Agent to connect to Google. The Google Cloud service account requires the `gkehub.connect` IAM role.

This can also happen if you delete and recreate the Google Cloud service account with the same name. You also need to delete and recreate the IAM role binding in that case. Refer to [Deleting and recreating service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview#deleting-recreating) for more information.

Resolution
    

Bind the `gkehub.connect` role to your service account (note that the `gkehub.admin` role does not have the proper permissions for connecting and is not meant to be used by service accounts).

For example, for a project called `my-project` and a Google Cloud service account called `gkeconnect@my-project.iam.gserviceaccount.com`, you'd run the following command to bind the role to the service account:
    
    
    gcloud projects add-iam-policy-binding my-project --member \
    serviceAccount:gkeconnect@my-project.iam.gserviceaccount.com \
    --role "roles/gkehub.connect"
    

You can view and verify the service account permissions have been applied to a Google Cloud service account by examining the output of the following command, and you should see the `role: roles/gkehub.connect` bound to the associated Google Cloud service Account.
    
    
    gcloud projects get-iam-policy my-project
    

## Error when binding IAM role to the Google Cloud service account

Symptom
    

You might encounter an error like this one:
    
    
    ERROR: (gcloud.projects.add-iam-policy-binding) PERMISSION_DENIED:
    Service Management API has not been used in project [PROJECT_ID] before or it
    is disabled. Enable it by visiting
    https://console.developers.google.com/apis/api/servicemanagement.googleapis.com/overview?project=[PROJECT_ID]
    then retry. If you enabled this API recently, wait a few minutes for the
    action to propagate to our systems and retry.

Possible causes
    

You might not have the IAM permissions to run the command `gcloud projects add-iam-policy-binding`.

Resolution
    

You need to have the permission `resourcemanager.projects.setIamPolicy` If you have the `Project IAM Admin`, `Owner` or `Editor` roles, you should be able to run the command. If an internal security policy prohibits you from running the command, check with your administrator.

## Error from skewed system clock

Symptom
    

You might encounter an error like this one:
    
    
    acceptCall: failed to parse token in req [rpc_id=1]: Token used before issued [rpc_id=1]
    

Possible causes
    

The log message usually indicates that there is a clock skew on the cluster. The cluster-issued token has an out-of-sync timestamp and thus the token is rejected.

Resolution
    

To see if the clock is not properly synced, you can run the `date` command on your cluster and compare it with the standard time. Usually a few seconds drift will cause this problem. To resolve this issue, please re-sync your cluster's clock.

## Unable to see workloads in Google Cloud console

Symptoms
    

In the Connect Agent logs, you might observe the following errors:
    
    
    "https://10.0.10.6:443/api/v1/nodes" YYYY-MM-DDTHH mm:ss.sssZ http.go:86: GET
    "https://10.0.10.6:443/api/v1/pods" YYYY-MM-DDTHH mm:ss.sssZ http.go:139:
    Response status: "403 Forbidden" YYYY-MM-DDTHH mm:ss.sssZ http.go:139:
    Response status: "403 Forbidden"`

Possible causes
    

These logs indicate that Google Cloud is attempting to access the cluster using the credentials you provided during registration. 403 errors indicate that the credentials don't have the permissions required to access the cluster.

Resolution
    

Check that the token and the account it's bound to, and be sure that it has the appropriate permissions on the cluster.

## Context deadline exceeded

Symptom
    

You might encounter an error like this one:
    
    
    2019/03/06 21:08:43.306625 dialer.go:235: dialer: dial: connecting to gkeconnect.googleapis.com:443...
    2019/03/06 21:09:13.306893 dialer.go:240: dialer: dial: unable to connect to gkeconnect.googleapis.com:443: context deadline exceeded
    2019/03/06 21:09:13.306943 dialer.go:183: dialer: connection done: context deadline exceeded
    

Possible causes
    

This error indicates a low-level TCP networking issue where the Connect Agent cannot talk with gkeconnect.googleapis.com.

Resolution
    

Verify that Pod workloads within this cluster can resolve and have outbound connectivity to gkeconnect.googleapis.com on port 443.

## Agent connection fails intermittently

Symptoms
    

In the Connect Agent logs, you might observe the following errors:
    
    
    2020/10/06 18:02:34.409749 dialer.go:277: dialer: dial: connection to gkeconnect.googleapis.com:443 failed after 8m0.790286282s: serve: receive request failed: rpc error: code = Unavailable desc = transport is closing
    2020/10/06 18:02:34.416618 dialer.go:207: dialer: connection done: serve: receive request failed: rpc error: code = Unavailable desc = transport is closing
    2020/10/06 18:02:34.416722 dialer.go:295: dialer: backoff: 978.11948ms
    2020/10/06 18:02:34.410097 tunnel.go:651: sendResponse: EOF [rpc_id=52]
    2020/10/06 18:02:34.420077 tunnel.go:651: sendResponse: EOF [rpc_id=52]
    2020/10/06 18:02:34.420204 tunnel.go:670: sendHalfClose: EOF [rpc_id=52]
    2020/10/06 18:02:34.401412 tunnel.go:670: sendHalfClose: EOF [rpc_id=53]
    

Possible causes
    

The connection to Connect closes when Connect Agent does not have enough resources, for example on smaller AWS EC2 instances such as `t3.medium`.

Resolution
    

If you use AWS and the T3 instance type, enable [T3 unlimited](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html) or use an [instance type](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/reference/supported-instance-types) with more resources [for your node pools](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/how-to/create-node-pool).

## Fleet cannot access the project

Symptoms
    

During some Fleet operations (usually cluster registration) you might observe an error similar to the following:
    
    
    ERROR: (gcloud.container.hub.memberships.register) failed to initialize Feature
    "authorizer", the fleet service account (service-PROJECT_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com) may not have access to your project
    

Possible causes
    

Fleet's default service account, `gcp-sa-gkehub`, can accidentally become unbound from a project. The _Fleet Service Agent_ is an [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) that grants the service account the permissions to manage cluster resources. If you remove this role binding from the service account, the default service account becomes unbound from the project, which can prevent you from registering clusters and other cluster operations.

You can check to see if the service account has been removed from your project using gcloud CLI or the Google Cloud console. If the command or the dashboard do not display `gcp-sa-gkehub` among your service accounts, the service account has become unbound.

### gcloud

Run the following command:
    
    
    gcloud projects get-iam-policy PROJECT_NAME
    

where `PROJECT_NAME` is the name of the project where you are trying register the cluster.

### Console

Visit the [IAM & admin](https://console.cloud.google.com/iam-admin/iam) page in Google Cloud console.

Resolution
    

If you removed the Fleet Service Agent role binding, run the following commands to restore the role binding:
    
    
    PROJECT_NUMBER=$(gcloud projects describe PROJECT_NAME --format "value(projectNumber)")
    gcloud projects add-iam-policy-binding PROJECT_NAME \
      --member "serviceAccount:service-${PROJECT_NUMBER}@gcp-sa-gkehub.iam.gserviceaccount.com" \
      --role roles/gkehub.serviceAgent
    

To confirm that the role binding was granted:
    
    
    gcloud projects get-iam-policy PROJECT_NAME
    

If you see the service account name along with the `gkehub.serviceAgent` role, the role binding has been granted. For example:
    
    
    - members:
      - serviceAccount:service-1234567890@gcp-sa-gkehub.iam.gserviceaccount.com
      role: roles/gkehub.serviceAgent
    

## Error in registering a GKE cluster from a different project than Fleet

Symptoms
    

While registering a GKE cluster from a project different than the Fleet project, you might observe an error similar to the following in gcloud CLI:
    
    
    ...
    message: 'DeployPatch failed'>
    detail: 'DeployPatch failed'
    ...
    

It can be verified in logging by applying the following filters: 
    
    
    resource.type="gke_cluster"
    resource.labels.cluster_name="my-cluster"
    protoPayload.methodName="google.container.v1beta1.ClusterManager.UpdateCluster"
    protoPayload.status.code="13"
    protoPayload.status.message="Internal error."
    severity=ERROR
    

Possible causes
    

The Fleet default Service Account does not have the required permissions in the GKE cluster's project.

Resolution
    

[Grant the Fleet default Service Account the required permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project) before registering the cluster.

## Error in registering/unregistering a GKE cluster or updating fleet membership details for a registered GKE cluster during credentials rotation

Symptoms
    

While rotating your cluster credentials(https://cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation), you may find errors if registering/unregistering a GKE cluster or updating the membership for a registered GKE cluster.
    
    
    ERROR: (gcloud.container.hub.memberships.unregister) "code": 13,
    "message": "an internal error has occurred"
    

Possible causes
    

Cluster credentials are in an intermediate state where the Fleet service is unable to access them.

Resolution
    

[Complete the rotation](https://cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#completing_the_rotation) before registering/umpregistering the cluster or updating the membership for a registered GKE cluster.

## Error when disabling the Fleet API

Symptoms
    

When trying to disable the Fleet API (`gkehub.googleapis.com`), you may encounter an error similar to the following:
    
    
    Not ready to deactivate the service on this project; ensure there are no more resources managed by this service.
    

Possible causes
    

There are still clusters registered to Google Cloud (memberships) or [fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features) enabled in this project. All memberships or features must be unregistered or disabled before the API can be disabled.

  * To view your current registered clusters, follow the instructions in [View fleet members](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status)

  * To see all active fleet-level features for your project:




### gcloud and cURL
    
    
    $ curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://gkehub.googleapis.com/v1alpha/projects/PROJECT_NAME/locations/global/features
    

where `PROJECT_NAME` is the name of the project where you are trying to disable the Fleet API.

### Console

If you have GKE enabled in your project, visit the [Feature Manager page](https://console.cloud.google.com/kubernetes/features) page in Google Cloud console. Features listed as **ENABLED** are active fleet-level features.

Resolution
    

First, [unregister any clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister) still registered to your project fleet. All clusters must be unregistered before some features can be disabled.

Once you have done this, disable all fleet-level features. Currently, this is only possible with the Fleet REST API.

  1. Disable fleet-level features that you have enabled for your project
         
         $ gcloud alpha container hub FEATURE_COMMAND disable
         

  2. Disable feature authorizer and metering, which are enabled by default.
         
         $ curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -X "DELETE" \
             https://gkehub.googleapis.com/v1alpha/projects/PROJECT_NAME/locations/global/features/FEATURE
         

where `FEATURE` is the name of the feature to disable (such as `authorizer` or `metering`).




## Missing cluster permissions when registering a cluster

Symptom:
    

While trying to register a cluster with a user account or Google Cloud [service account](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts), you may get an error similar to the following:
    
    
    ERROR: (gcloud.container.hub.memberships.register) ResponseError: code=403, message=Required "container.clusters.get" permission(s) for "projects/my-project/zones/zone-a/clusters/my-cluster"
    

Possible cause:
    

The account that is trying to register the cluster does not have the required `cluster-admin` role-based access control (RBAC) role in the cluster.

Resolution:
    

[Grant the `cluster-admin` RBAC role to the account](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#grant_cluster-admin) before registering the cluster.

## Error `Failed to check if the user is a cluster-admin: Unable to connect to the server` when registering a cluster

Symptom:
    

While trying to register a cluster, you may get an error similar to the following:
    
    
    ERROR: (gcloud.container.hub.memberships.register) Failed to check if the user is a cluster-admin: Unable to connect to the server: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
    

Or
    
    
    ERROR: (gcloud.container.hub.memberships.register) Failed to check if the user is a cluster-admin: Unable to connect to the server: dial tcp MASTER_ENDPOINT_IP:443: i/o timeout
    

Possible cause:
    

The machine on which you are running the registration `gcloud` command can't connect to the cluster's external endpoint. This usually happens if you have a private cluster with external access/IP disabled, but your machine's external IP address is not allowlisted. Note that registering a GKE cluster doesn't have this requirement after gcloud 407.0.0.

Resolution:
    

Make sure the machine on which you want to run the `gcloud` registration command can access the cluster's API server. If your cluster doesn't have external access enabled, file a case with Google Cloud Support.

## Error: Deleting a Google-managed membership isn't allowed

After you register your cluster to a fleet, it becomes a fleet member with a unique fleet membership name. If you try to delete this membership by running `gcloud container hub memberships delete MEMBERSHIP_NAME`, you might see the following error:
    
    
    ERROR: (gcloud.container.hub.memberships.delete) FAILED_PRECONDITION: membership "projects/PROJECT_ID/locations/us-centrall/memberships/MEMBERSHIP_NAME" is a managed resource of your cluster. Deleting a google-managed membership directly is not allowed. Please offboard your fleet membership via cluster API: failed precondition
    

To properly delete a fleet membership, follow the instructions in [Unregistering a cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister#gcloud).

## Getting additional help

You can file a ticket with Google Cloud support for GKE, by performing the following steps:

  1. [File a case](https://cloud.google.com/support-hub/) with Google Cloud Support.
  2. Follow the instructions in Collecting Connect Agent logs to save the Connect logs.
  3. If troubleshooting an on-premises cluster using Google Groups or third-party support, follow the instructions in [Collecting GKE Identity Service logs](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/:#gke_id_service_logs) to save the GKE Identity Service logs. Make sure to sanitize the pod logs in the saved file if necessary.
  4. Attach the relevant logs to your case.

**Note:** You can request that your data be deleted at anytime by updating the case.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
