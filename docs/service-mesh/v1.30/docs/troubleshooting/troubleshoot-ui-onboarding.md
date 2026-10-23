---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-ui-onboarding/
title: Resolving issues enabling Cloud Service Mesh through Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:40.104585+00:00
---

# Resolving issues enabling Cloud Service Mesh through Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-ui-onboarding/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving issues enabling Cloud Service Mesh through Google Cloud console

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.30/docs/getting-support).

## Ensure you have sufficient permissions

To enable Cloud Service Mesh while creating a GKE cluster, you must have all of the following roles:

  * [Kubernetes Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container)
  * [GKE Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub)
  * [Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage)



For information on granting roles, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).

## Failed to enable Cloud Service Mesh through Google Cloud console

When enabling Cloud Service Mesh on a cluster, the enablement may fail. If the enablement fails, the Google Cloud console displays a message: "Cloud Service Mesh installation failed."

Enabling Cloud Service Mesh through the Google Cloud console creates a `ControlPlaneRevision` custom resource in the cluster. This resource's status is updated when the managed control plane is provisioned or fails provisioning and contains an error message if enablement failed.
    
    
    kubectl describe controlplanerevision -n istio-system
    

The output is similar to:
    
    
        Name:         asm-managed
    
        …
    
        Status:
          Conditions:
            Last Transition Time:  2021-08-05T18:56:32Z
            Message:               The provisioning process has not completed successfully
            Reason:                NotProvisioned
            Status:                False
            Type:                  Reconciled
            Last Transition Time:  2021-08-05T18:56:32Z
            Message:               Provisioning has finished
            Reason:                ProvisioningFinished
            Status:                True
            Type:                  ProvisioningFinished
            Last Transition Time:  2021-08-05T18:56:32Z
            Message:               Unsupported Kubernetes version: v1.14.10
            Reason:                PreconditionFailed
            Status:                True
            Type:                  Stalled
    

If the `Type: Reconciled` `Status` field is `True`, then the control plane is running successfully. The `Type: Stalled` `Status` field will be `True` if the managed control plane provisioning process has encountered an error. If `Stalled`, the `Message` field will contain more information about the specific error. See [Stalled codes](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/troubleshoot-managed-anthos-service-mesh#stalled_codes) for more information about possible errors.

The installation will be retried every 15 minutes, and the `ControlPlaneRevision` custom resource will be updated to reflect the latest status. However, the error message displayed in the Google Cloud console will not be updated, even if installation later succeeds. Run the above command on your cluster to check current status (once every 15 minutes).

If the installation has not succeeded after addressing the error message and then waiting 15 minutes, you can [Configure managed Cloud Service Mesh with `asmcli`](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane) to enable Cloud Service Mesh.

Alternatively, if the installation failed during GKE cluster creation, you can delete the cluster and try again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
