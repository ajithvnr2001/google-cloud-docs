---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-troubleshooting/
title: Troubleshooting fleet-level setup issues \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:52.056702+00:00
---

# Troubleshooting fleet-level setup issues  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Troubleshooting fleet-level setup issues Stay organized with collections  Save and categorize content based on your preferences. 

This document provides troubleshooting instructions for [fleet-level setup](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet) of authentication from third-party identity providers.

## Resolve fleet-level setup issues

To resolve issues that may occur while setting up your fleet, follow these instructions:

### 1\. Validate if GKE Identity Service is enabled

To validate if GKE Identity Service is enabled for your project, run the following command:
    
    
    $ gcloud container fleet identity-service describe
    

If you don't see any errors, GKE Identity Service is enabled and you can continue to the next instruction.

**Error:** `Identity Service Feature for project <your-project-id> is not enabled`

If you see this error, it indicates that GKE Identity Service was not enabled correctly for your fleet when setting up the feature.

**Solution:** To ensure the feature is enabled for your project, see the instructions in [Configure clusters for GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#configure_clusters).

### 2\. View GKE Identity Service status

To view the current status of GKE Identity Service, run the following command:
    
    
    $ gcloud container fleet identity-service describe
    

The output of this command has the following two sections:

  * `membershipSpecs` contains the identity provider configuration that you've specified for each cluster registered to the fleet. GKE Identity Service is configured on each cluster using these configurations.

  * `membershipStates` shows the current state of GKE Identity Service in each cluster, including the relevant identity provider configuration and any errors that might have occurred during setup.




To troubleshoot issues in a cluster, under `membershipStates`, search for the cluster and look for the following fields:

  * `state` field: `**membershipStates - > <cluster-identifier> -> identityservice -> state**`
  * `failureReason` field: `**membershipStates - > <cluster-identifier> -> identityservice -> failureReason**`.



#### Example

If you have two clusters `helloworld` and `foobar` registered to the fleet, then the output has the following structure:
    
    
    Identity Service Feature:
      createTime: '222-11-10T23:05:6.146566392Z'
      membershipSpecs:
        projects/<your-project-number>/locations/<location>/memberships/helloworld:
          identityservice:
            authMethods:
            - name: oidc
              oidcConfig:
                clientId: id
                issuerUri: https://accounts.google.com
                ... other fields
        projects/<your-project-number>/locations/<location>/memberships/foobar:
          identityservice:
            authMethods:
            - name: oidc
              oidcConfig:
                clientId: id
                issuerUri: https://accounts.google.com
                ... other fields
      membershipStates:
        projects/<your-project-number>/location/<location>/memberships/helloworld:
          identityservice:
            **failureReason : AIS feature does not support this cluster type**        memberConfig:
              authMethods:
              - name: oidc
                oidcConfig:
                  clientId: id
                  issuerUri: https://accounts.google.com
                  ... other fields
            **state : ERROR**      state:
            code: OK
            updateTime: '2022-11-11T20:39:59.556176650Z'
        projects/<your-project-number>/location/<location>/memberships/foobar:
          identityservice:
            memberConfig:
              authMethods:
              - name: oidc
                oidcConfig:
                  clientId: id
                  issuerUri: https://accounts.google.com
                  ... other fields
            state: OK
          state:
            code: OK
            updateTime: '2022-11-11T20:39:59.556176650Z'
    
      name: projects/<project-number>/locations/global/features/identityservice
      updateTime: '2022-11-11T20:40:31.859321901Z'
    

### 3\. Verify cluster state

To verify the state of GKE Identity Service in a cluster, check the following:

  * **`state` value is `OK`**: This indicates that no error occurred when configuring GKE Identity Service on the cluster with the configuration specified under `membershipSpecs`.

If the configuration for the cluster you are troubleshooting (for example, `helloworld`) is different in `membershipSpecs` and `membershipStates`, then it’s likely that you updated the configuration for the cluster. Wait a few minutes for GKE Identity Service to propagate the changes to the cluster and check the status again.

If the configuration for the cluster you are troubleshooting (for example, `helloworld`) is the same in `membershipSpecs` and `membershipStates`, then GKE Identity Service has been configured correctly.

  * **`state` field is `ERROR`**: This indicates that there were errors when configuring GKE Identity Service on the cluster with the configuration specified under `membershipSpecs`.

To resolve the issue, see Troubleshoot common issues. After following the necessary troubleshooting steps, wait for a few minutes and then check the status again.




## Troubleshoot common issues

### GKE Identity Service API not enabled

This issue occurs when the GKE Identity Service API is not enabled.

**Error message**
    
    
    anthosidentityservice.googleapis.com is not enabled

**Solution**

To enable the API, run the following command:
    
    
    $ gcloud services enable anthosidentityservice.googleapis.com
    

### Unsupported cluster type

This issue occurs when you use a cluster type that isn't supported.

**Error message**
    
    
    GKE Identity Service feature does not support this cluster type

**Solution**

For information on the supported cluster types, see [cluster types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet#clustertypes) or reach out to Google Cloud support for new cluster type requests .

### Unsupported protocols found in the configuration

This issue occurs when the identity configuration that you've applied to your cluster contains protocols that aren’t supported.

**Error message**
    
    
    unsupported protocol found in configuration, aborting reconciliation.

**Solution**

Fleet-level setup for GKE Identity Service supports the following:

  * [Third-party identity provider types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet#identity_provider_types)
  * [Google](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).



Update the configuration on the cluster so that it only contains the above supported protocols. To edit the configuration, run the following command:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n kube-public edit clientconfig default
    

Replace `CLUSTER_KUBECONFIG` with the path to the kubeconfig file for the cluster. If there are multiple contexts in the kubeconfig, the current context is used. You may need to reset the current context to the correct cluster before running the command.

### Cluster does not have an identity configuration

This issue occurs when there is no configuration applied to your cluster.

**Error message**
    
    
    Authentication configuration is not present for this membership

**Solution**

Apply an identity configuration to the cluster by following the instructions in [Configure clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#configure_clusters).

### Missing GKE Hub admin IAM permission

This issue occurs when you don't have the `gkehub.admin` role on the project that you're using.

**Error messages**
    
    
    PERMISSION_DENIED: Permission 'gkehub.memberships.list' denied on '`projects//locations//memberships`'
    
    
    PERMISSION_DENIED: Permission 'gkehub.features.get' denied on '`projects//locations/global/features/identityservice`'
    
    
    PERMISSION_DENIED: Permission 'gkehub.features.delete' denied on '`projects//locations/global/features/identityservice`'
    
    
    PERMISSION_DENIED: Permission 'gkehub.features.create' denied on '`projects//locations/global/features/identityservice`'

**Solution**

An owner of the project with id `project_id` must run the following command:
    
    
    gcloud projects add-iam-policy-binding project_id --member=user:USER_ID --role=roles/gkehub.admin
    

Replace `USER_ID` with your Google account.

### Non-unique identity providers present in an identity configuration

This issue occurs when the GKE Identity Service configuration for a cluster has the same `name` value for multiple identity providers.

**Error message**
    
    
    Configuration contains multiple identity providers with the same name

**Solution**

Rename or remove duplicate entries from your configuration.

### Multiple providers of type `google` present in an identity configuration

This issue occurs when the ClientConfig is configured with multiple configurations of type [`google`](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).

**Error message**
    
    
    configuration contains multiple identity providers of type 'google'

**Solution**

The `spec/authentication` section of the configuration can contain at most one configuration of type `google`.

Update the configuration on the cluster so that it does not have more than one configuration of type `google`. To edit the configuration, run the following command:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n kube-public edit clientconfig default
    

Replace `CLUSTER_KUBECONFIG` with the path to the kubeconfig file for the cluster. If there are multiple contexts in the kubeconfig, the current context is used. You may need to reset the current context to the correct cluster before running the command.

### Error fetching the ClientConfig's custom resource definition

This issue occurs when there is an error fetching the ClientConfig's custom resource definition from the cluster.

**Error message**
    
    
    error fetching the ClientConfig's Custom Resource Definition: ERROR_REASON

**Solution**

Use the details displayed in the `ERROR_REASON` to resolve this issue.

### Error updating the GKE Identity Service ClientConfig

This issue occurs when there is an error in updating the ClientConfig in the cluster.

**Error message**
    
    
    Error updating AIS ClientConfig: ERROR_REASON

**Solution**

Use the details displayed in the `ERROR_REASON>` to resolve this issue.

### ClientConfig not present on the cluster

This issue occurs when the ClientConfig, which should be created when installing GKE Identity Service, is not present on the cluster. A missing ClientConfig indicates that GKE Identity Service has not been correctly installed on the cluster.

**Error message**
    
    
    ClientConfig CR not present, expected to be created when AIS was installed

**Solution**

The GKE Identity Service resources on the cluster may have been accidentally deleted. You can try to create a new cluster. If you see the same error in the new cluster, contact your cluster administrator or Google Cloud support.

### GKE Identity Service pod not started

This issue occurs when the GKE Identity Service pod is in a `pending` state.

**Error message**
    
    
    GKE Identity Service pod is not running (pending)

**Solution**

This issue should auto-resolve in a few minutes, after which the GKE Identity Service pod switches to the `running` state.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
