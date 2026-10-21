---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/containers/
title: Configuring containers \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:30.311370+00:00
---

# Configuring containers  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Configuring containers Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to configure the container port and the container entrypoint command and arguments.

When Knative serving starts a container, it runs the image's [default entrypoint command](https://docs.docker.com/engine/reference/builder/#entrypoint) and default command arguments. If you want to override the image's default entrypoint and command arguments, you can use the `command` and `args` fields in the container configuration. The `command` field specifies the actual command run by the container. The `args` field specifies the arguments passed to that command.

## Configuring the container port

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

The container should listen on the port defined by the `PORT` environment variable rather than a specific hardcoded port. However, if this is not possible, you can configure on which port requests are sent to the container:

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Container**.

  4. Specify the port you want requests to be sent to, if not the default value of `8080`. This also sets the `PORT` environment variable.

  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### Command line

  * For existing services, update a port setting by running the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with the following parameters:
        
        gcloud run services update SERVICE --port PORT

Replace:

    * SERVICE with the name of the service.
    * PORT with the port to send requests to. Note that the default port is `8080`.
  * For new services, set the port by running the `gcloud run deploy` command with the [`--port`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--port) parameter:
        
        gcloud run deploy SERVICE --image=IMAGE_URL --port PORT

Replace:

    * SERVICE with the name of the service.
    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * PORT with the port to which you want to send requests. The default port is `8080`.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `containerPort:` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
                 ports:
                 - containerPort: PORT
         

Replace

     * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
     * PORT with the port to which you want to send requests.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




## Configuring the container entrypoint command and arguments

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

When Knative serving starts a container, it runs the image's [default entrypoint command](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#notes). To specify or override the existing entrypoint command and arguments that are defined in the container image, you can configure the `command` and `args` settings in the Knative serving container configuration.

You can choose to configure entrypoint commands, arguments, or both. The command that you specify in Knative serving overrides any entrypoint command that is defined in the container image. If you choose to specify only arguments, those arguments are passed to and run by the entrypoint command defined in the container image.

In Knative serving, you can configure entrypoint commands and arguments using the Google Cloud console, the Google Cloud CLI, or a YAML file when you deploy a new [service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#service), update an existing service, or deploy a [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying#revision):

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Container**.

  4. Specify the entrypoint command and arguments that you want the container to run during startup.

  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### Command line

### Command parameter options

  * To specify an argument that contains a comma (`,`), you must [escape](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) each `ARG` with a different delimiter. For example, if you use `@`: 
        
        --args "^@^arg,with,commas@anotherarg@ARG3..."

  * To specify several sets of key-value pairs, you can specify multiple parameters for readability. Example: 
        
        [...]
        --args "ARG1" \
        --args "ARG2" \
        --args "ARG3"

  * To use equal signs (`=`) in your arguments, you must specify each argument using the following format: 
        
        gcloud run services ...  \
          --args "--repo-allowlist=github.com/example/example_demo" \
          --args "--gh-webhook-secret=XX"




OK

  * For existing services, update the entrypoint command by running the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with the following parameters:
        
        gcloud run services update SERVICE --command COMMAND --args ARG1,ARG2,ARG-N

Replace:

    * SERVICE with the name of the service.
    * Optional: COMMAND with the command that you want the container to run during startup.
    * Optional: ARG1 with one or more arguments for the command that is run during startup. Use a comma delimited list for multiple arguments. How to format your arguments.
  * For new services, set the entrypoint command by running the `gcloud run deploy` command with the [`--command`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--command) parameter:
        
        gcloud run deploy SERVICE --image=IMAGE_URL --command COMMAND --args ARG1,ARG2,ARG-N

Replace:

    * SERVICE with the name of the service.
    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * Optional: COMMAND with the command that you want the container to run during startup.
    * Optional: ARG1 with one or more arguments for the command that is run during startup. Use a comma delimited list for multiple arguments. How to format your arguments.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `command` and `args` attributes:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
                 command:
                 - COMMAND
                 args:
                 - "ARG1"
                 - "ARG-N"
         

Replace:

     * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
     * Optional: COMMAND with the command that you want the container to run during startup.
     * Optional: ARG1 with one or more arguments for the command that is run during startup. Use a comma delimited list for more than one argument.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
