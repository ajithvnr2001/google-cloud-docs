---
url: https://docs.cloud.google.com/migrate/containers/docs/custom-blocklist/
title: Custom services blocklist \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:56:30.892832+00:00
---

# Custom services blocklist  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/custom-blocklist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Reference ](https://docs.cloud.google.com/migrate/containers/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Custom services blocklist

**Migrate to Containers version 1.7 added support for defining custom blocklists by editing the migration plan. We recommend that you now[use the migration plan](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan) to define your custom blocklists. **

By default, Migrate to Containers [disables unneeded services](https://docs.cloud.google.com/migrate/containers/docs/planning-best-practices#disable_unneeded_services) on a VM when you migrate it to a container. These services can sometimes cause issues with the migrated container, or are not needed in a container context.

You can also define your own custom list of services to disable in a migrated container by using a custom _blocklist_. With a blocklist, you specify one or more services to disable in a migrated container.

**Note:** Add the custom blocklist to a container _after_ migrating the source VM to a container. The custom blocklist is then applied to the container when you deploy the container.

## Defining the blocklist

Define your customized blocklist in a .yaml file, in the form:
    
    
    service_list:
      - name: <var>group-name-1</var>
        services:
          - <var>service-name</var>
      - name: <var>group-name-2</var>
        services:
          - <var>service-name</var>
          - <var>ervice-name</var>
    

Where:

  * Groups are a logical collection of services so that you can collect similar services in a single group. Specify any string value for the group name. 
  * The service name specifies the service to disable in the migrated container. 



For example, define the file `my-blocklist.yaml` as:
    
    
    service_list:
      - name: lvm-related
        services:
          - lvm2-lvmetad
      - name: hardware-related
        services:
          - microcode
          - microcode.ctl
    

## Applying a custom blocklist

Apply your custom blocklist to a container by either:

  * Creating a Kubernetes `configmap` containing the blocklist and adding it to the deployment spec of the container. 

This method lets you add the blocklist without having to rebuild the container. However, you have to recreate the `configmap` on every cluster used to host the container. 

  * Edit the Dockerfile for the container and rebuild the container image. 

This method requires you to rebuild the container image to add the blocklist. Because the blocklist is now included in the container there is no need to perform any additional configuration on the cluster before deployment.




### Using a configmap

To create a blocklist by using a `configmap`:

  1. Migrate the source VM to a container. 

  2. Create a blocklist .yaml file as shown above that lists the service you want to disable. In this example, name the file `my-blocklist.yaml`.

  3. Create a `configmap` from the blocklist .yaml file:
         
         kubectl create configmap configmap-name --from-file=path-to-yaml

In this example, the configmap is called `blocklistcm`:
         
         kubectl create configmap blocklistcm --from-file=./my-blocklist.yaml

  4. View the configmap: 
         
         kubectl describe configmaps

  5. Edit the `deployment_spec.yaml` created when you migrated the container: 
         
         vi deployment_spec.yaml

  6. In the deployment spec, add the following:

     1. Add a new volume for the `configmap` under `volumes`: 
            
            volumes:
            - configMap: 
                 name: blocklistcm # Name of the config map you created above. 
               name: blocklistvol # Name of the configmap volume.
            

     2. Add a volume mount for the configmap: 
            
            spec:
              containers: 
                volumeMounts: 
                - mountPath: /etc/bl # Mount path for the configmap volume. 
                  name: blocklistvol # Name of the configmap volume. 
            

     3. Add a new environment variable named `HC_CUSTOM_SERVICE_BLOCKLIST` specifying the path to the blocklist .yaml file. The name of the environment variable is required to be `HC_CUSTOM_SERVICE_BLOCKLIST`: 
            
            containers:
             - image: container-image-location
               env:
               - name: HC_CUSTOM_SERVICE_BLOCKLIST
                 value: "/etc/bl/my-blocklist.yaml"
            

The path specified by value is the concatenation of the mountPath of the configmap and the name of the blocklist .yaml file, `my-blocklist.yaml`.

     4. Save the file. 

  7. Deploy the container: 
         
         kubectl apply -f deployment_spec.yaml

  8. After the container is deployed, you can then examine the container to ensure that the services are not running. For example: 
         
         # Get pod name.
         $ kubectl get pod
         # Connect to pod.
         $ kubectl exec -it POD_NAME -- /bin/bash
         # View running services. This step is OS dependent. For example:
         $ service --status-all```
         




### Editing the Dockerfile

This section describes how to create a custom blocklist by editing the Dockerfile created by the migration.

  1. Migrate the source VM to a container. 

  2. Open the Dockerfile in an editor. 

  3. Add the following `COPY` command to add the blocklist .yaml file to the filesystem of the container: 
         
         COPY src dest 

For example: 
         
         COPY my-blocklist.yaml /etc/mybl/my-blocklist.yaml

The destination path can be any path within the container. 

  4. Add a new environment variable named `HC_CUSTOM_SERVICE_BLOCKLIST` specifying the path to the blocklist .yaml file based on the file destination specified by the `COPY` command. The name of the environment variable is required to be `HC_CUSTOM_SERVICE_BLOCKLIST`: 
         
         ENV HC_CUSTOM_SERVICE_BLOCKLIST /file-path

For example: 
         
         ENV HC_CUSTOM_SERVICE_BLOCKLIST /etc/mybl/my-blocklist.yaml

  5. Update the container image. 

The way you update the container image depends on your build environment. You can use: 

     1. `gcloud` to build the image and upload it to the Container Registry as described at [Quickstart: Build](https://docs.cloud.google.com/build/docs/build-push-docker-image).

     2. `docker build` as described at [Build and run your image](https://docs.docker.com/get-started/part2/) .

  6. After you build the new image, open the `deployment_spec.yaml` file in an editor to update the image location: 
         
         spec:
           containers:
           - image: new-image-location

For example, new-image-location could be `gcr.io/my-project/my-new-image:v1.0` if you used `gcloud` to build the image and uploaded it to the Container Registry.

  7. Deploy the container: 
         
         kubectl apply -f deployment_spec.yaml

  8. After the container is deployed, you can then examine the container to ensure that the services are not running. For example: 
         
         # Get pod name.
         $ kubectl get pod
         # Connect to pod.
         $ kubectl exec -it POD_NAME -- /bin/bash
         # View running services. This step is OS dependent. For example:
         $ service --status-all
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
