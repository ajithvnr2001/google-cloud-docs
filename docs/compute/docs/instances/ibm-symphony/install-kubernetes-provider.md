---
url: https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-kubernetes-provider/
title: Install the Google Kubernetes Symphony provider \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:07.675303+00:00
---

# Install the Google Kubernetes Symphony provider  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-kubernetes-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install the Google Kubernetes Symphony provider Stay organized with collections  Save and categorize content based on your preferences. 

To integrate IBM Symphony with Google Kubernetes Engine (GKE) for dynamic resource management, you must install and configure the Symphony provider for GKE. This provider lets Symphony provision and manage compute resources as pods in your GKE cluster, which allows for efficient workload scaling through Kubernetes orchestration.

To enable this integration, you install a Kubernetes operator in your cluster, install the provider plugin on your Symphony primary host, and configure Symphony's host factory service to communicate with GKE.

For more information about Symphony Connectors for Google Cloud, see [Integrate IBM Spectrum Symphony with Google Cloud](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/overview).

## Before you begin

To install the Symphony provider for GKE, you must have the following resources:

  * A running IBM Spectrum Symphony cluster with the host factory service enabled.
  * A running GKE cluster. To create one, see the [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).
  * A service account with the appropriate permissions. See the Required roles section for details.
  * The `kubectl` command-line tool [installed and configured to communicate with your GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).



### Required roles

To get the permissions that you need to install the operator and manage Symphony pods, ask your administrator to grant you the following IAM roles on your project: 

  * To manage Kubernetes resources: [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Install the Kubernetes operator

Before you install the GKE provider, you must install the associated Kubernetes operator. The operator manages the lifecycle of Symphony compute pods within your GKE cluster.

### Build the operator image

To generate and deploy the Kubernetes manifests for the operator, you first need to build the operator container image. The manifests include the Custom Resource Definition (CRD) that the operator uses to manage Symphony. To acquire the image, you can build it from source.

To build the operator image from source, complete the following steps:

  1. Clone the `symphony-gcp-connector` repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/symphony-gcp-connector.git
         

  2. Navigate to the `k8s-operator` directory:
         
         cd symphony-gcp-connector/k8s-operator
         

  3. Set the environment variables for the image name, registry, and tag:
         
         export IMAGE="gcp-symphony-operator"
         export REGISTRY="IMAGE_REPO"
         export TAG="TAG"
         

Replace the following:

     * `IMAGE_REPO`: the image repository where the operator image is stored. For example, you can use Artifact Registry to store your operator images. For more information, see [Create Docker repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
     * `TAG`: the tag for the operator image, for example, `0.0.1`.
  4. Build and push the operator image:
         
         bash -c 'docker buildx build --platform linux/amd64 -t $IMAGE:$TAG -t $IMAGE:latest -t $REGISTRY/$IMAGE:$TAG -t $REGISTRY/$IMAGE:latest .'
         bash -c 'docker push $REGISTRY/$IMAGE:$TAG && docker push $REGISTRY/$IMAGE:latest'
         




### Configure the operator manifests

After you have the operator image, you need to generate and configure the Kubernetes manifests.

  1. To generate the manifests, use the `export-manifests` command with the operator image:
         
         docker run --rm gcp-symphony-operator:latest export-manifests > manifests.yaml
         

  2. Open the `manifests.yaml` file in a text editor of your choice.

  3. In the `spec.template.spec.containers` section, locate the `image` field and update its value to the full path of the image you pushed to your registry.
         
         ...
         containers:
         - image: IMAGE_REPO/gcp-symphony-operator:TAG
           name: manager
         ...
         

Replace the following:

     * `IMAGE_REPO`: the path to the image repository where you pushed the operator image.

     * `TAG`: the tag that you assigned to the operator image when you built it.

  4. Optional: You can also modify the `imagePullPolicy` value to align with your cluster management practices.




### Apply the operator manifests

After you have configured the manifests, apply them to your Kubernetes cluster. You can apply the manifests by using `kubectl` or [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

  * **kubectl** : To apply the manifests by using `kubectl`, run the following command:
        
        kubectl apply -f manifests.yaml
        

  * **Cluster Toolkit** : If your GKE infrastructure is managed by Cluster Toolkit, then add a `modules/management/kubectl-apply` source to your GKE blueprint to apply the manifests. The following is an example configuration, assuming that the `manifests.yaml` file is in the same directory as the GKE blueprint:
        
        -   id: symphony_operator_install
              source: modules/management/kubectl-apply
              use: [gke_cluster]
              settings:
              apply_manifests:
                -   source: $(ghpc_stage("manifests.yaml"))
        

For more information, see the [Cluster Toolkit overview](https://docs.cloud.google.com/cluster-toolkit/docs/overview).




## Load the host factory environment variables

Before you can configure or manage the host factory services, you must load the Symphony environment variables into your shell session. On your Symphony primary host VM, run the following command:
    
    
    source INSTALL_FOLDER/profile.platform
    

Replace `INSTALL_FOLDER` with the path to your install folder. The default Symphony install folder path is `/opt/ibm/spectrumcomputing`. However, if you installed Symphony elsewhere, you must use the correct path for your environment.

This command executes the `profile.platform` script, which exports essential environment variables like `$EGO_TOP` and `$HF_TOP` and adds the Symphony command-line tools to your shell's `PATH`. You must run this command for each new terminal session to ensure the environment is configured correctly.

## Install the provider plugin

To integrate the GKE provider with Symphony's host factory, install the prebuilt provider plugin from the RPM package or build the provider from the source code.

### Install the prebuilt provider plugin

To install the provider plugin by using RPM packages, follow these steps on your Symphony primary host VM:

  1. Add the `yum` repository for the Google Cloud Symphony Connectors:
         
         sudo tee /etc/yum.repos.d/google-cloud-symphony-connector.repo << EOM
         [google-cloud-symphony-connector] name=Google Cloud Symphony Connector
         baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-symphony-connector-x86-64
         enabled=1
         gpgcheck=0
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
                https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOM
         

  2. Install the provider package for GKE:
         
         sudo yum install -y hf-gcpgke-provider.x86_64
         




The RPM installation automatically places the provider executables and scripts in the correct directories for the Symphony host factory service. After installation, the directory structure for the provider plugin appears as follows for the path `$HF_TOP/$HF_VERSION/providerplugins/gcpgke`:
    
    
    ├── bin
    │   ├── hf-gke
    │   └── README.md
    └── scripts
        ├── getAvailableTemplates.sh
        ├── getRequestStatus.sh
        ├── getReturnRequests.sh
        ├── requestMachines.sh
        └── requestReturnMachines.sh
    

### Build the provider from the source code

To build and install the CLI executable in the `bin` directory of the provider plugin directory, follow these steps:

  1. Clone the `symphony-gcp-connector` repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/symphony-gcp-connector.git
         

  2. Navigate to the `hf-provider` directory:
         
         cd PROJECT_ROOT/hf-provider
         

Replace `PROJECT_ROOT` with the path to the top-level directory that contains the hf-provider directory, such as `/home/user/symphony-gcp-connector`.

  3. If you don't have `uv` installed, then install it:
         
         pip install uv
         

  4. Create a Python virtual environment by using the `uv` Python package manager:
         
         uv venv
         

  5. Activate the virtual environment:
         
         source .venv/bin/activate
         

  6. Install the required project dependencies:
         
         uv pip install .
         

  7. Install PyInstaller, which bundles the Python application into a standalone executable:
         
         uv pip install pyinstaller
         

  8. Create the `hf-gke` CLI for Google Kubernetes Engine clusters:
         
         uv run pyinstaller hf-gke.spec --clean
         

  9. To verify the installation, run the `--help` command for an executable. You might see an error if you don't set the required environment variables.
         
         dist/hf-gke --help
         

  10. If you manually build the provider, then create provider plugin directories for the binary and scripts:
         
         mkdir -p $HF_TOP/$HF_VERSION/providerplugins/gcpgke/bin
         mkdir -p $HF_TOP/$HF_VERSION/providerplugins/gcpgke/scripts
         

  11. Copy the `hf-gke` binary and scripts to the provider plugin directories. The `hf-gke` binary is in the `dist/` directory that PyInstaller created, and the scripts are in the `scripts/gcpgke/` directory:
         
         cp dist/hf-gke $HF_TOP/$HF_VERSION/providerplugins/gcpgke/bin/
         cp scripts/gcpgke/* $HF_TOP/$HF_VERSION/providerplugins/gcpgke/scripts/
         

After installation, your directory structure for the provider plugin appears as follows for the path `$HF_TOP/$HF_VERSION/providerplugins/gcpgke`:



    
    
    ├── bin
    │   └── hf-gke
    └── scripts
        ├── getAvailableTemplates.sh
        ├── getRequestStatus.sh
        ├── getReturnRequests.sh
        ├── requestMachines.sh
        └── requestReturnMachines.sh
    

## Enable the provider plugin

To enable the GKE provider plugin, you must register it in the host factory configuration.

  1. Open the `${HF_TOP}/conf/providerplugins/hostProviderPlugins.json` file.

The source command defines the `$HF_TOP` environment variable in your environment. The value is the path to the top-level installation directory for the IBM Spectrum Symphony host factory service.

  2. Add a `gcpgke` provider plugin section:
         
         {
             "name": "gcpgke",
             "enabled": 1,
             "scriptPath": "${HF_TOP}/${HF_VERSION}/providerplugins/gcpgke/scripts/"
         }
         




## Set up a provider instance

To configure the GKE provider for your environment, create a provider instance.

  1. If you manually build the connector, create a directory for the provider instance, such as: `$HF_TOP/conf/providers/gcpgkeinst/`.

The `$HF_TOP` environment variable is defined in your environment if you have sourced the `profile.platform script`. The value is the path to the top-level installation directory for the IBM Spectrum Symphony host factory service.

  2. In the provider instance directory (`$HF_TOP/conf/providers/gcpgkeinst/`), create or configure the `gcpgkeinstprov_config.json` file. This file contains the main configuration for the provider.

     * If you installed the provider plugin by using the RPM package, then you can copy the example configuration file and then customize it:
           
           cp $HF_TOP/conf/providers/gcpgkeinst/gcpgkeinstprov_config.json.dist $HF_TOP/conf/providers/gcpgkeinst/gcpgkeinstprov_config.json
           

     * If you built the provider from source, then create a `gcpgkeinstprov_config.json` file.

For this file, you typically only need to configure the `GKE_KUBECONFIG` variable, which defines the path to a standard kubectl configuration file for the associated GKE cluster. If you don't specify a path, then it defaults to `kubeconfig` in the provider instance directory. You must ensure that this path points to a valid kubectl configuration file for the Kubernetes cluster that this provider instance uses.

The following is an example configuration:
    
    {
      "GKE_KUBECONFIG": "kubeconfig"
    }
    

The following configuration variables are supported:

Variable Name | Description | Default Value  
---|---|---  
`GKE_KUBECONFIG` | The path to the configuration file used by the kubectl command. | None  
`GKE_CRD_NAMESPACE`* | Defines the Kubernetes namespace in which all resources are created. | `gcp-symphony`  
`GKE_CRD_GROUP`* | The resource group that is used to identify custom resources for the GKE host factory operator. | `accenture.com`  
`GKE_CRD_VERSION`* | The version that is used to identify custom resources for the GKE host factory operator. | `v1`  
`GKE_CRD_KIND`* | The name given to the custom resource definition that defines a request for compute resources (pods). | `GCP Symphony Resource`  
`GKE_CRD_SINGULAR`* | Used in API calls when referring to an instance of the Google Cloud Symphony `Resource` CR. | `gcp-symphony-resource`  
`GKE_CRD_RETURN_REQUEST_KIND`* | The name given to the custom resource definition that defines a request to return compute resources (pods). | `Machine Return Request`  
`GKE_CRD_RETURN_REQUEST_SINGULAR`* | Used in API calls when referring to a single `MachineReturnRequest` custom resource instance. | `machine-return-request`  
`GKE_REQUEST_TIMEOUT` | The duration, in seconds, that a request to the GKE control plane waits for a response. | `300`  
`LOG_LEVEL` | Controls the level of log detail that the GKE provider writes to the log file. Options are `CRITICAL`, `WARNING`, `ERROR`, `INFO`, `DEBUG`. | `WARNING`  
**Important:** If you modify a variable marked with an asterisk (*), then you must also modify the corresponding variable in the Kubernetes operator configuration. We recommend that you use the default values to maintain consistency.
  3. In the same directory, create or configure the `gcpgkeinstprov_templates.json` file. This file defines the templates for the pods that the provider can create.

     * If you installed the provider plugin by using the RPM package, then you can copy the example templates file and then customize it:
           
           cp $HF_TOP/conf/providers/gcpgkeinst/gcpgkeinstprov_templates.json.dist $HF_TOP/conf/providers/gcpgkeinst/gcpgkeinstprov_templates.json
           

     * If you built the provider from source, then create a `gcpgkeinstprov_templates.json` file.

The template attributes should be aligned with the resources in a pod specification. The following is an example template:
           
           {
               "templates": [
                   {
                       "templateId": "template-gcp-01",
                       "maxNumber": 5000,
                       "attributes": {
                           "type": [ "String", "X86_64" ],
                           "ncores": [ "Numeric", "1" ],
                           "ncpus": [ "Numeric", "1" ],
                           "nram": [ "Numeric", "2048" ]
                       },
                       "podSpecYaml": "pod-specs/pod-spec.yaml"
                   }
               ]
           }
           

  4. In the same directory, create a `kubeconfig` file that is a valid kubectl config file for your Kubernetes cluster.

  5. In the provider instance directory, create or edit the `pod-spec.yaml` file. This file acts as a template that defines the specifications for the Symphony compute pods that are created in your GKE cluster.

The pods created from this specification function as compute nodes and require access to the Symphony installation. This access can be provided through the container image, which includes the Symphony installation, or through a shared file system mount that contains the installation. Upon startup, the pods use this access to join the Symphony cluster.

The steps to create the file depend on how you installed the provider:

     * If you installed the provider from an RPM package, then copy the example `pod-spec.yaml.dist` file that was included in the installation:
           
           cp $HF_TOP/conf/providers/gcpgkeinst/pod-specs/pod-spec.yaml.dist
           $HF_TOP/conf/providers/gcpgkeinst/pod-specs/pod-spec.yaml
           

     * If you built the provider from source, then create the `pod-specs` directory and the `pod-spec.yaml` file manually:
           
           mkdir -p $HF_TOP/conf/providers/gcpgkeinst/pod-specs touch
           $HF_TOP/conf/providers/gcpgkeinst/pod-specs/pod-spec.yaml
           

  6. After you create these files, verify that your provider instance directory appears as follows:
         
         ├── gcpgkeinstprov_config.json
         ├── gcpgkeinstprov_templates.json
         ├── kubeconfig
         └── pod-specs
             └── pod-spec.yaml
         




## Enable the provider instance

To activate the provider instance, enable it in the host factory configuration file:

  1. Open the `$HF_TOP/conf/providers/hostProviders.json` file.

  2. Add a `gcpgkeinst` provider instance section:
         
         {
             "name": "gcpgkeinst",
             "enabled": 1,
             "plugin": "gcpgke",
             "confPath": "${HF_CONFDIR}/providers/gcpgkeinst/",
             "workPath": "${HF_WORKDIR}/providers/gcpgkeinst/",
             "logPath": "${HF_LOGDIR}/"
         }
         

You don't need to replace the `${HF_CONFDIR}`, `${HF_WORKDIR}`, and `${HF_LOGDIR}` variables in this configuration because they are standard environment variables that are automatically defined by the IBM Spectrum Symphony host factory environment.

When you configure your shell session by running the `source command`, this script sets these variables to point to the correct subdirectories within your Symphony installation. The host factory service then uses these variables to construct the full paths at runtime.




## Enable the requestor instance

To let a specific Symphony component use the GKE provider to provision resources, enable it for that requestor.

  1. Open the `$HF_TOP/conf/requestors/hostRequestors.json` file.

  2. In the appropriate requestor instance, add `gcpgkeinst` to the `providers` parameter:
         
         "providers": ["gcpgkeinst"],
         

The provider value must match the provider name you use in Enable the provider instance.




## Start the host factory service

To apply your configuration changes, start the host factory service. On your Symphony primary host VM, sign in as the cluster administrator and start the service:
    
    
    sed -i -e "s|MANUAL|AUTOMATIC|g" $EGO_ESRVDIR/esc/conf/services/hostfactory.xml
    egosh user logon -u "SYMPHONY_USERNAME -x "SYMPHONY_PASSWORD
    egosh service start HostFactory
    

Replace the following:

  * `SYMPHONY_USERNAME`: the Symphony username for authentication.
  * `SYMPHONY_PASSWORD`: the password for the Symphony user.



## Test connectors

Create a resource request to test the provider for GKE.

To do so, use one of the following methods:

  * **Symphony GUI** : For instructions on how to create a resource request by using the Symphony GUI, see [Manually scheduling cloud host requests and returns](https://www.ibm.com/docs/en/spectrum-symphony/7.3.2?topic=manually-scheduling-cloud-host-requests-returns) in the IBM documentation.

  * **REST API** : To create a resource request using the REST API, follow these steps:

    1. Find the host and port of the host factory REST API:
           
           egosh client view REST_HOST_FACTORY_URL
           

The output is similar to this example:
           
           CLIENT NAME: REST_HOST_FACTORY_URL
           DESCRIPTION: http://sym2.us-central1-c.c.symphonygcp.internal:9080/platform/rest/hostfactory/
           TTL        : 0
           LOCATION   : 40531@10.0.0.33
           USER       : Admin
           
           CHANNEL INFORMATION:
           CHANNEL             STATE
           9                   CONNECTED
           

    2. To create a resource request using the REST API, use the following command:
           
           HOST=PRIMARY_HOST
           PORT=PORT
           TEMPLATE_NAME=SYMPHONY_TEMPLATE_ID
           PROVIDER_NAME=gcpgkeinst
           
           curl -X POST -u "SYMPHONY_USER:SYMPHONY_PASSWORD" -H "Content-Type: application/json" -d "{ \"demand_hosts\": [ { \"prov_name\": \"$PROVIDER_NAME\", \"template_name\": \"$TEMPLATE_NAME\", \"ninstances\": 1 } ] }" \
           http://$HOST:$PORT/platform/rest/hostfactory/requestor/admin/request
           

Replace the following:

       * `PRIMARY_HOST`: the hostname of your primary host from the output of the previous command.
       * `PORT`: the port number of your primary host from the output of the previous command, such as `9080`.
       * `SYMPHONY_TEMPLATE_ID`: The `templateId` defined in the `gcpgkeinstprov_templates.json` file, such as `template-gcp-01`.
       * `SYMPHONY_USER`: the Symphony user for authentication.
       * `SYMPHONY_PASSWORD`: the password for the Symphony user.

If successful, the output is similar to this example:
    
    {"scheduled_request_id":["SD-641ef442-1f9e-40ae-ae16-90e152ed60d2"]}
    




## What's next

  * [Troubleshoot IBM Spectrum Symphony connectors](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/troubleshoot-symphony)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
