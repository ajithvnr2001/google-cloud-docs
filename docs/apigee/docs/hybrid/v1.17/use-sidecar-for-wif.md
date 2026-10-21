---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/use-sidecar-for-wif/
title: Use sidecar authentication for Workload Identity Federation on AKS and EKS \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:26:01.065044+00:00
---

# Use sidecar authentication for Workload Identity Federation on AKS and EKS  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/use-sidecar-for-wif/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Use sidecar authentication for Workload Identity Federation on AKS and EKS Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/use-sidecar-for-wif.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/use-sidecar-for-wif.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/use-sidecar-for-wif.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/use-sidecar-for-wif.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/use-sidecar-for-wif.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/use-sidecar-for-wif.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/use-sidecar-for-wif.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/use-sidecar-for-wif.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/use-sidecar-for-wif.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/use-sidecar-for-wif.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/use-sidecar-for-wif.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/use-sidecar-for-wif.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/use-sidecar-for-wif.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/use-sidecar-for-wif.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/use-sidecar-for-wif.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/use-sidecar-for-wif.html)



Workload Identity Federation allows Apigee workloads to obtain privately sourced federated credentials and exchange them for Google tokens that can access Apigee APIs. This page describes how to configure Workload Identity Federation for Apigee hybrid to obtain these private federated credentials using a sidecar container. This method is an alternative to using Kubernetes Projected Service Account Tokens, as described in [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation). Use the sidecar method if you need to use an external or custom Identity Provider (IdP) to fetch authentication tokens.

With this method, you can use a sidecar container along with Workload Identity Federation on non-GKE platforms to mount security tokens from your preferred IdP for service account authentication.

## Before you begin

Before completing this procedure, ensure that you have done the following:

  * Configured Workload Identity Federation for your Google Cloud project, including creating an Identity Pool and Provider, and granting IAM permissions to your Kubernetes service accounts. For details, see [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation).
  * Built and pushed a custom sidecar container image that fetches credentials from your Identity Provider (IdP) and writes the security token to a shared volume (such as `/shared/token`).



## Configure Apigee hybrid

To enable Workload Identity Federation using sidecar authentication, set up the sidecar configuration in your `overrides.yaml` file. You must specify the sidecar container and any volumes needed to share data between the sidecar and the Apigee hybrid component. Apigee adds the sidecar container as a Kubernetes native sidecar (an init container with `restartPolicy: Always`), so you must also specify a `startupProbe`. Kubernetes waits for this probe to succeed before starting the Apigee component container. For example, you can configure the probe to run `cat` on the shared token file to verify that the token has been written. If you're using Vault, you must add the annotations required to allow the sidecar to fetch tokens from your IdP.

You only need to configure the `gcp.federatedWorkloadIdentity.sidecarSpec` section in your `overrides.yaml` file for all components. When you apply the configuration, the Helm charts replace every instance of `APIGEE_COMPONENT` with the corresponding component name. The component names are `apigee-cassandra`, `apigee-guardrails`, `apigee-logger`, `apigee-mart`, `apigee-mcp-server`, `apigee-metrics`, `apigee-mint-task-scheduler`, `apigee-runtime`, `apigee-synchronizer`, and `apigee-watcher`.

Add the following configuration to your `overrides.yaml` file. Select the example that matches your use case (Kubernetes secrets or files, or Vault agent injection):

### Secrets or files
    
    
    gcp:
      federatedWorkloadIdentity:
        enabled: true
        type: **"sidecar"**
        sidecarSpec:
          volumes:
          - name: **source-creds**
            secret:
              secretName: **apigee-hybrid-APIGEE_COMPONENT**
          container:
            env: 
            - name: "apigee-component"
              value: **APIGEE_COMPONENT**
            image: CUSTOM_SIDECAR_IMAGE
            startupProbe:
              exec:
                command:
                - cat
                - /shared/token
            volumeMounts:
            - name: **shared-mount**
              mountPath: /shared
            - name: **source-creds**
              mountPath: /source-creds
              readOnly: true

### Vault agent injection
    
    
    gcp:
      federatedWorkloadIdentity:
        enabled: true
        type: **"sidecar"**
        sidecarSpec:
          annotations:
            vault.hashicorp.com/agent-inject: "true"
            vault.hashicorp.com/agent-pre-populate-only: "false"
            vault.hashicorp.com/log-level: "trace"
            vault.hashicorp.com/ca-cert: "VAULT_CA_CERT_PATH"
            vault.hashicorp.com/namespace: "VAULT_NAMESPACE"
            vault.hashicorp.com/agent-inject-secret-source-token: "VAULT_TOKEN" # For example: '/path/to/secret' or '/path/to/APIGEE_COMPONENT/secret' if the secret is per-component.
            vault.hashicorp.com/secret-volume-path: "VAULT_SECRET_VOLUME_PATH" # For example: '/source-creds'
            vault.hashicorp.com/service: "VAULT_SERVICE_URL:8200" # For example: '127.0.0.1:8200' or 'https://vault.example.com:8200'
          volumes:
          - name: **source-creds**
            secret:
              secretName: **apigee-hybrid-APIGEE_COMPONENT**
          container:
            env: 
            - name: "apigee-component"
              value: **APIGEE_COMPONENT**
            image: CUSTOM_SIDECAR_IMAGE
            startupProbe:
              exec:
                command:
                - cat
                - /shared/token
            volumeMounts:
            - name: **shared-mount**
              mountPath: /shared
            - name: **source-creds**
              mountPath: /source-creds
              readOnly: true

If your sidecar needs per-component secrets injected using Vault annotations, and you can't use the `APIGEE_COMPONENT` substitution mechanism, you can add the annotations to each component that needs the sidecar. For example:
    
    
    mart:
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/role: "VAULT_ROLE"
        vault.hashicorp.com/agent-inject-secret-token: "VAULT_SECRET_PATH"
        vault.hashicorp.com/agent-inject-template-token: |
          {{- with secret "VAULT_SECRET_PATH" -}}
          {{ .Data.data.token }}
          {{- end -}}
    
    runtime:
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/role: "VAULT_ROLE"
        vault.hashicorp.com/agent-inject-secret-token: "VAULT_SECRET_PATH"
        vault.hashicorp.com/agent-inject-template-token: |
          {{- with secret "VAULT_SECRET_PATH" -}}
          {{ .Data.data.token }}
          {{- end -}}
    
    ... other components ...

Where:

  * `gcp.federatedWorkloadIdentity.enabled`: Must be `true`.
  * `gcp.federatedWorkloadIdentity.type`: Must be `"sidecar"`. This tells Apigee hybrid to use the sidecar method for Workload Identity Federation.
  * `gcp.federatedWorkloadIdentity.sidecarSpec.container`: A Kubernetes container specification for your custom sidecar. You must specify your custom `image` that can fetch tokens from your IdP.
  * `gcp.federatedWorkloadIdentity.sidecarSpec.container.env`: (optional) A list of environment variables to set in the sidecar container. For example, you can set `apigee-component` to `APIGEE_COMPONENT` so that the sidecar can identify which Apigee component it is running with.
  * `gcp.federatedWorkloadIdentity.sidecarSpec.container.startupProbe`: A Kubernetes startup probe for the sidecar container. The probe checks that the token file exists in the shared volume.
  * `gcp.federatedWorkloadIdentity.sidecarSpec.container.volumeMounts`: A list of volume mounts for the sidecar container. You must include a volume mount named `shared-mount` for the shared volume that contains the token for the Apigee component.
  * `gcp.federatedWorkloadIdentity.sidecarSpec.volumes`: (optional) A list of additional volumes to add to hybrid pods for use by the sidecar container.
  * `gcp.federatedWorkloadIdentity.sidecarSpec.annotations`: (Vault only) A map of annotations to apply to hybrid pods.
  * `[_component_].annotations`: (Vault only, optional) A map of annotations to apply to individual hybrid components if needed by your configuration.



After updating your `overrides.yaml` file, apply the changes to your cluster. Run the following commands to update each hybrid component:

  1. Make sure you are in the `apigee-charts/` directory.
  2. Upgrade the Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm upgrade -h` for details.
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  3. Upgrade the Apigee datastore: 
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  4. Upgrade Apigee telemetry: 
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  5. Upgrade Apigee Redis: 
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  6. Upgrade Apigee ingress manager: 
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  7. Upgrade the Apigee organization: 
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  8. Upgrade the environment. 

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME.
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE
         

  9. Upgrade the environment groups (`virtualhosts`). 

You must upgrade one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP_NAME. Repeat the following commands for each environment group mentioned in the overrides.yaml file:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set envgroup=ENV_GROUP_NAME \
           -f OVERRIDES_FILE
         




For more information, see:

  * [`gcp.federatedWorkloadIdentity.type`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-type)
  * [`gcp.federatedWorkloadIdentity.sidecarSpec.annotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-sidecarspec-annotations)
  * [`gcp.federatedWorkloadIdentity.sidecarSpec.container`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-sidecarspec-container)
  * [`gcp.federatedWorkloadIdentity.sidecarSpec.container.env`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-sidecarspec-container-env)
  * [`gcp.federatedWorkloadIdentity.sidecarSpec.container.startupProbe`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-sidecarspec-container-startup-probe)
  * [`gcp.federatedWorkloadIdentity.sidecarSpec.container.volumeMounts`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-sidecarspec-container-volume-mounts)
  * [`gcp.federatedWorkloadIdentity.sidecarSpec.volumes`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-sidecarspec-volumes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
