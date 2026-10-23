---
url: https://docs.cloud.google.com/migrate/containers/docs/windows/prepare-windows-cluster/
title: Prepare a Windows cluster for deployment \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:04.266815+00:00
---

# Prepare a Windows cluster for deployment  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/windows/prepare-windows-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare a Windows cluster for deployment

This page describes how to prepare your Windows cluster for deployment.

## Before you begin

  * Complete the migration and have the resulting generated artifacts.
  * Create the cluster where you want to deploy your workload. For more information, see [Creating a Windows cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows)
  * [Set up `kubectl` and connect to the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).



## Choose and set up your Docker registry

As part of your deployment, you build and upload the Docker image of your container to a Docker registry.

For the Docker registry you can choose to use:

  * Artifact Registry

  * Any Docker registry that supports basic authentication




The recommended solution is to use [Artifact Registry](https://docs.cloud.google.com/artifact-registry) in the same project of the deployment cluster. GKE can access the registry by default. For more information, see the [requirements to integrate with GKE](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke#requirements).

If you want to use you a private Docker registry, learn [how to configure the registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).

## Configure migrated workloads to use gMSA

Windows IIS Application workloads are often Active Directory (AD) joined and operate using domain identities. When migrating these VMs to containers, the containers themselves are not domain-joined, but rather their host Kubernetes cluster nodes can be domain-joined.

When you deploy your migrated containers to a cluster, you can use a Group Managed Service Account (gMSA). Use gMSA to execute the container within a specific service account identity. You attach a gMSA in the Kubernetes cluster as part of the pod configuration rather than as a static identity configuration inside the container image.

Migrate to Containers helps you in the process of transforming your workloads. Migrate to Containers automatically discovers the configuration of IIS application pools and adds recommendations to the generated migration plan. You can then evaluate these recommendations and modify them for your specific environment and requirements.

If Migrate to Containers determines that the configuration of an application pool does not require a gMSA, then it maintains the original application pool configuration. For example, when it uses a built-in account type such as `ApplicationPoolIdentity`, `NetworkService`, `LocalSystem`, or `LocalService`.

To support gMSA in a migrated Windows container, you must:

  1. [Edit the migration plan](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/windows/windows-customizing-a-migration-plan#enablegmsa) to set the necessary properties to configure the migrated container to use a gMSA.

  2. Configure the target cluster that hosts the deployed container.




## Configure a target cluster to support gMSA

You attach a gMSA in the Kubernetes cluster as part of the pod configuration, rather than as a static identity configuration inside the container image.

To configure a cluster hosting the migrated Windows container to support gMSA, you must have:

  1. [Configured Active Directory for VMs to automatically join a domain](https://docs.cloud.google.com/solutions/configuring-active-directory-for-vms-to-automatically-join-the-domain).

  2. [Configured gMSA for Windows Pods and containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/).


**Note:** Active Directory limits computer names to 15 characters which can cause a naming conflict with your nodes. See [Using gMSA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#using_gmsa) for more information and workarounds.

For more information, see the following:

  * [Create gMSAs for Windows containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#create-a-group-managed-service-account).
  * [Create a group Managed Service Account](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-gmsa).
  * [Using gMSA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#using_gmsa) in the Google Cloud documentation.
  * [Configure your app to use a gMSA](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/gmsa-configure-app) in the Microsoft documentation.



## Deploy a container when storing SSL certificates as Kubernetes secrets

We recommend that you use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs), [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress), or [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) as an HTTPS frontend to secure external access to your deployed container. This option lets you secure external communication without including any certificates inside the cluster. For more information, see [Customizing a migration plan](https://docs.cloud.google.com/migrate/anthos/docs/windows/customizing-a-migration-plan).

You can also store Secure Sockets Layer (SSL) certificates as Kubernetes secrets and mount them at runtime into the container.

**Caution:** We don't recommended storing SSL certificates as Kubernetes secrets as this might cause security issues.

To use Kubernetes secrets:

  1. Create a [PFX file](https://docs.microsoft.com/en-us/mem/configmgr/mdm/deploy-use/create-pfx-certificate-profiles) with the certificate and password.

  2. Create a configuration YAML file that defines site access:
         
         sites:
          - sitename: "sitename"
            sslport: 443
            pfxpath: c:\sslconfig\pfx
            password: "password"
            thumbprint: "3e858d0551fc0536f52d411dad92b680a4fad4da"

Where:

     * `sitename` specifies the name of the site configured to use SSL. The `sites` property can contain multiple `sitename` entries.

     * `sslport` specifies the port to listen to for SSL connections (typically 443).

     * `pfxpath` specifies the path to the PFX file. Configure it as part of the `volumeMounts` of the deployment of the pod.

     * `password` specifies the password for the PFX file.

     * `thumbprint` specifies the SHA-1 thumbprint of the PFX file that can be retrieved using the PowerShell command:
           
           Get-PfxCertificate -FilePath "path to pfx"

Or view in the Windows Certificate Manager.

  3. Create the Kubernetes secret:
         
         kubectl create secret generic secret-name --from-file=pfx=path-to-pfx --from-file=config=path-to-config

  4. Create the volume and volume mount in the deployment of the image:
         
         apiVersion: v1
         kind: Pod
         metadata:
          name: iis-pod
          labels:
            app: iis-server-simple
          spec:
            nodeSelector:
              kubernetes.io/os: windows
            containers:
            - name: iis-server
              image: your-image-url
              volumeMounts:
              - name: ssl-secret
                **mountPath : c:\sslconfig**
              env:
              - **name : M4A_CERT_YAML**
                value: c:\sslconfig\config
            volumes:
            - name: ssl-secret
              secret:
                **secretName : secret-name**

Where:

     * `mountPath` is the same path as specified by `pfxpath` in the configuration file you created in Step 2.
     * `M4A_CERT_YAML` is an environment variable set to the full path to the configuration YAML file you created in Step 2.
     * `secret-name` is the name of the secret you created in step 3.



## Configure SSL

It is recommended not to store SSL certificates private keys inside a container image as they are accessible to anyone reading the image. Migrate to Containers provides several ways of handling SSL for Windows.

### Use a self-signed auto-generated certificate

By default, a Windows container with an HTTPS binding is assigned a self-signed auto-generated certificate that is generated on the initialization of the Docker container. This configuration lets you test your migrated workload, but cannot be used in a production environment. The certificate is both self-signed and regenerated every time the container is run.

### Recommended - Use Cloud Load Balancing, Ingress, or Cloud Service Mesh

You can customize the bindings in the migration plan to use HTTP. Then use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs), [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress), or [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) as an HTTPS frontend to secure external access. This option lets you secure external communication without including any certificates inside the cluster.

  * To customize the binding, edit the `site` definition in the migration plan that represents the migration to set `protocol` to `http`:
        
        sites:
          site:
          - applications:
            - path: /
              virtualdirectories:
                - path: /
                  physicalpath: '%SystemDrive%\inetpub\wwwroot'
                  bindings:
                  - port: 8080
                    protocol: http
                  name: Default Web Site
        

**Note:** Only HTTP and HTTPS protocols are allowed in the `protocol` setting. All protocols other than HTTP/HTTPS are skipped and not processed.



You can then forward requests from the HTTPS frontend to the HTTP path and port of the Windows workload.

### Store SSL certificates as Kubernetes secrets

It's recommended that you use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs), [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress), or [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) as an HTTPS frontend to secure external access. However, you can also store SSL certificates as Kubernetes secrets and mount them at runtime into the container.

To use SSL certificates stored as Kubernetes secrets, you must edit the deployment image of the container. For more information, see Deploy a container when storing SSL certificates as Kubernetes secrets.

## Configure logging to Cloud Logging

Migrate to Containers uses the [LogMonitor](https://github.com/microsoft/windows-container-tools/tree/master/LogMonitor) tool to extract logs from a Windows container and forward them to your GKE cluster. These logs are then automatically forwarded to [Cloud Logging](https://docs.cloud.google.com/logging/docs), which provides a suite of tools to monitor your containers.

By default Migrate to Containers enables IIS logging to monitor the IIS logs, and also forwards the Application or System event logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs).

### Configure logging

Expanding the generated `artifacts.zip` file creates several directories, including the `m4a` directory. The directory contains a folder for every image. Included in the `m4a` directory is the `LogMonitorConfig.json` file that you can edit to control logging.

For more on editing `LogMonitorConfig.json`, see [Authoring a Config File](https://github.com/microsoft/windows-container-tools/wiki/Authoring-a-Config-File).

## Set ACLs

Some IIS applications require that you set specific access control lists (ACL) permissions on files and folders in order for the applications to perform correctly. Migrate to Containers automatically scans all migrated IIS applications and adds any specific permissions defined in the source VM that apply to IIS accounts (the `IUSR` account and the `IIS_IUSRS` group) and applies them to the copied files and directories in the generated container image.

Because Windows container images don't support setting ACLs as part of the Docker `COPY` command, the ACLs are set in a script called `set_acls.bat`. Migrate to Containers automatically creates `set_acls.bat` in the directory of the generated image for your specific windows application. Migrate to Containers then calls `set_acls.bat` when you execute the `docker build` command.

Edit `set_acls.bat` to add or remove custom permissions, or edit permissions that are not related to specific IIS users and therefore were not detected by Migrate to Containers.

The script uses the Windows built-in [icacls](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/icacls) tool to set permissions.

## About the .NET Global Assembly Cache

Migrate to Containers scans the source image .NET Global Assembly Cache (GAC) for .NET resources that are installed on the source machine and not available as part of the official images. Any discovered DLL is copied into the Docker context and installed as part of the building of the target image by a utility script `install_gac.ps1`.

All .NET assemblies are copied into the Docker context under the `m4a\gac` directory. To remove assemblies from the image, delete them from the `m4a\gac` directory.

## COM object DLL registration

DLLs that expose COM objects are automatically scanned and registered. During the extraction phase, the copied files are scanned for DLLs that are registered as COM objects, which are then registered in the container.

This process occurs without user input. However, you can influence this process by adding more DLLs to be copied. If needed, these DLLs are checked in turn, and registered.

**Note:** .Net COM objects are not supported.

## What's next

  * Learn how to [build and deploy Windows IIS workloads](https://docs.cloud.google.com/migrate/containers/docs/windows/build-container-image).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
