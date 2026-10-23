---
url: https://docs.cloud.google.com/migrate/containers/docs/convert-runtime/
title: Upgrade container workloads for enhanced runtime \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:42.788314+00:00
---

# Upgrade container workloads for enhanced runtime  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/convert-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade container workloads for enhanced runtime

If you have existing container workloads created using Migrate to Containers versions 1.7.x and 1.8.x, you can convert them to use the simplified Linux service manager. This conversion lets you then run these containers on GKE Autopilot clusters.

**Note:** Converting a container workload created by using Migrate to Containers versions previous to 1.7.0 is not supported.

To perform the conversion, edit the Dockerfile and the `deployment_spec.yaml` file created when you performed the original migration. Once edited, you can then deploy the container workload on Autopilot clusters.

## About converting container workloads

The procedure for converting existing workloads depends on whether you are converting a _stateless_ workload or _stateful_ workload.

A stateful workload is one that maintains or stores state information. For stateful workloads, you often mount additional volumes by using the `StatefulSet` in `spec.containers.volumeMounts`. Make sure to retain the `volumeMounts` definitions while also removing them for `/sys/fs/cgroup`. See [Mounting External Volumes](https://docs.cloud.google.com/migrate/containers/docs/mounting-external-volumes) for more information.

The general process of converting an existing workload requires you to edit the:

  * Dockerfile

    * Set the Migrate to Containers version to 1.15.0.
    * Insert two `ADD` commands to copy the `logs.yaml` file to the container image.
    * Insert a `RUN` command for the `servicemanager_generate_config` utility.
  * `deployment_spec.yaml` file to:

    * Delete the `hostPath` and `volumeMounts` definitions for `/sys/fs/cgroup`.
    * Delete the `securityContext` definition.
    * Delete the `readinessProbe` definition.
    * You can leave the `mountPath` and `configMap` definitions for `logs-config`, however logging does not currently work with the simplified Linux service manager.



For the specific conversion process, see the sections below:

  * Convert a stateless workload
  * Convert a stateful workload



## Convert a stateless workload

The following example show how to convert a stateless container workload:

  1. Locate the directory containing your existing migration artifacts, including the `deployment_spec.yaml` file.

  2. Edit the Dockerfile to set the product version, to copy the `logs.yaml` file, and to run the `servicemanager_generate_config` utility:
         
         ...
         # Set the product version to 1.15.0:
         FROM anthos-migrate.gcr.io/v2k-run-embedded:**v1.15.0** as migrate-for-anthos-runtime
         
         ...
         
         ADD blocklist.yaml /.m4a/blocklist.yaml
         **# Insert the ADD commands to copy the `logs.yaml` file to the container image :
         ADD logs.yaml /code/config/logs/logsArtifact.yaml
         ADD logs.yaml /code/config/logs/logs.yaml**
         
         **# Insert the RUN command for servicemanager_generate_config:
         RUN /servicemanager_generate_config build-all -o /.m4a/
         **
         # Migrate to Containers image includes entrypoint
         ENTRYPOINT [ "/.v2k.go" ]

  3. Open the `deployment_spec.yaml` file in an editor. For example:
         
         vi  deployment_spec.yaml

  4. Locate the following section in the file and delete the indicated lines:
         
         apiVersion: apps/v1 
         kind: Deployment
         metadata: 
           creationTimestamp: null 
           name: IMAGE_NAME  
              … 
             spec:
               containers:
               - image: gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL
                 name: IMAGE_NAME
         **# Delete the following lines:
                 readinessProbe:
                   exec:
                     command:
                     - /code/ready.sh
                 resources: {}
                 securityContext:
                   privileged: true
                 volumeMounts:
                 - mountPath: /sys/fs/cgroup
                   name: cgroups
                 - mountPath: /code/config/logs
                   name: logs-config
               volumes:
               - hostPath:
                   path: /sys/fs/cgroup
                   type: Directory
                 name: cgroups
               - configMap:
                   name: suitecrm-crddefault-logs
                 name: logs-config
         # Stop the delete here.**

  5. Add the lines below to set the `HC_V2K_SERVICE_MANAGER` environment variable.

**Caution:** If you are using Migrate to Containers 1.10 or later, skip this step.
         
         spec:
           containers:
           - image: gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL
             name: IMAGE_NAME
         **# Add the following lines:
             env:
               - name: HC_V2K_SERVICE_MANAGER
                 value: "true"**

  6. Save the file. 

  7. Ensure that the target cluster has read access to the Docker image registry as described in [Ensure the target cluster has read access to the Docker image registry](https://docs.cloud.google.com/migrate/containers/docs/deploying-to-target-cluster#ensure-access). 

  8. Build the updated image and push to Container Registry with an updated version tag, ensuring you allow enough time for the build to finish. In the following example, the image is in the current directory:
         
         gcloud builds submit --timeout 4h --tag gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL .

  9. Deploy the container: 
         
         kubectl apply -f deployment_spec.yaml

If you apply the deployment spec to an Autopilot cluster without the necessary changes in `deployment_spec.yaml`, you see an error message in the form: 

`"Trying to run without root privileges is not possible. Did you try to use the new runtime? In that case please pass the environment variable HC_V2K_SERVICE_MANAGER=true to the pod"`

  10. View the pods that are being deployed to the cluster. 

**Note:** Loading the nodes and pulling the image might take a few minutes. 
         
         kubectl get pods




## Convert a stateful workload

The following example show how to convert a stateful container workload:

  1. Locate the directory containing your existing migration artifacts, including the `deployment_spec.yaml` file.

  2. Edit the Dockerfile to set the product version and run the `servicemanager_generate_config` utility:
         
         ...
         # Set the product version to 1.15.0:
         FROM anthos-migrate.gcr.io/v2k-run-embedded:**v1.15.0** as migrate-for-anthos-runtime
         
         ...
         
         ADD blocklist.yaml /.m4a/blocklist.yaml
         **# Insert the ADD commands to copy the `logs.yaml` file to the container image :
         ADD logs.yaml /code/config/logs/logsArtifact.yaml
         ADD logs.yaml /code/config/logs/logs.yaml**
         
         **# Insert the RUN command for servicemanager_generate_config:
         RUN /servicemanager_generate_config build-all -o /.m4a/
         **
         # Migrate to Containers image includes entrypoint
         ENTRYPOINT [ "/.v2k.go" ]

  3. Open the `deployment_spec.yaml` file in an editor. For example: 
         
         vi  deployment_spec.yaml

  4. Locate the following three sections in the file and delete the indicated lines:
         
         apiVersion: apps/v1 
         kind: StatefulSet  
         ... 
         spec: 
           containers: 
           - image: gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL 
             name: IMAGE_NAME 
         **# Delete the following lines:
             readinessProbe: 
               exec: 
                 command: 
                 - /code/ready.sh 
             resources: {} 
             securityContext: 
               privileged: true 
         # Stop the delete here.**
             volumeMounts: 
         **# Delete the following lines:
             - mountPath: /sys/fs/cgroup 
               name: cgroups 
         # Stop the delete here.**
             - mountPath: /opt/suitecrm-7.10.5-0/mysql/data 
               name: data-pvc-0-1b12-d0af-48b3-9f5e-6c25fa5 
               subPath: opt/suitecrm-7.10.5-0/mysql/data 
           volumes:
         **# Delete the following lines:
           - hostPath:
               path: /sys/fs/cgroup 
               type: Directory 
             name: cgroups 
         # Stop the delete here.**
           - name: data-pvc-2-d0af-48b3-9f5e09c25fa5 
             persistentVolumeClaim: 
               claimName: data-pvc-0-1a2-d0af-48b3-9f5e-605fa5

Notice that you only remove the `volumeMounts` and `volumes` definitions for `cgroups` and leave the remaining definitions. 

  5. Add the following lines to set the `HC_V2K_SERVICE_MANAGER` environment variable:

**Caution:** If you are using Migrate to Containers 1.10 or later, skip this step.
         
         spec: 
           containers: 
           - image: gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL
             name: IMAGE_NAME 
         **# Add the following lines:
             env:
             - name: HC_V2K_SERVICE_MANAGER 
               value: "true" 
         # Stop the add here.**
             volumeMounts: 
             - mountPath: /opt/suitecrm-7.10.5-0/mysql/data 
               name: data-pvc-0-1b12-d0af-48b3-9f5e-6c25fa5 
               subPath: opt/suitecrm-7.10.5-0/mysql/data 
           volumes:
           - name: data-pvc-2-d0af-48b3-9f5e09c25fa5 
             persistentVolumeClaim: 
               claimName: data-pvc-0-1a2-d0af-48b3-9f5e-605fa5

  6. Save the file. 

  7. Ensure that the target cluster has read access to the Docker image registry as described in [Ensure the target cluster has read access to the Docker image registry](https://docs.cloud.google.com/migrate/containers/docs/deploying-to-target-cluster#ensure-access). 

  8. Build the updated image and push to Container Registry with an updated version tag, ensuring you allow enough time for the build to finish. In the following example, the image is in the current directory:
         
         gcloud builds submit --timeout 4h --tag gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL .

  9. Deploy the container:
         
         kubectl apply -f deployment_spec.yaml

If you apply the deployment spec to an Autopilot cluster without the necessary changes in `deployment_spec.yaml`, you see an error message in the form: 

`"Trying to run without root privileges is not possible. Did you try to use the new runtime? In that case please pass the environment variable HC_V2K_SERVICE_MANAGER=true to the pod"`

  10. View the pods that are being deployed to the cluster.

**Note:** loading the nodes and pulling the image might take a few minutes.
         
         kubectl get pods




## Post conversion tasks

After you convert an existing migration to use the simplified Linux service manager, you might want to modify it to:

  * Update the services used by the migrated workload.
  * Add new services.



For both scenarios, you must edit the Dockerfile, then rebuild the container image.

### Update services

In this section, you edit the Dockerfile to update the `services-config.yaml` file in the container based on changes made in `/etc/systemd` on the migrated workload.

To update the container image for a change to an existing service:

  1. Add the `servicemanager_generate_config` command in the Dockerfile:

**Note:** Add the `servicemanager_generate_config` command directly to the Dockerfile. Do not try to run it inside the container workload.
         
         ...
         FROM anthos-migrate.gcr.io/v2k-run-embedded:**v1.15.0** as migrate-for-anthos-runtime
         
         ...
         
         ADD blocklist.yaml /.m4a/blocklist.yaml
         
         **# Use the update command for servicemanager_generate_config to update the configuration :
         RUN /servicemanager_generate_config update -u /.m4a/
         **
         # Migrate to Containers image includes entrypoint
         ENTRYPOINT [ "/.v2k.go" ]

  2. Build the updated image and push to Container Registry with an updated version tag, ensuring you allow enough time for the build to finish. In the following example, the image is in the current directory:
         
         gcloud builds submit --timeout 4h --tag gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL .

  3. Deploy the newly built image:
         
         kubectl set image deployment/myWorkload my-app=gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL --record




### Add services

To add a service to the container image:

  1. Add the `servicemanager_generate_config` command in the Dockerfile:

**Note:** Add the `servicemanager_generate_config` command directly to the Dockerfile. Do not try to run it inside the container workload.
         
         ...
         FROM anthos-migrate.gcr.io/v2k-run-embedded:**v1.15.0** as migrate-for-anthos-runtime
         
         ...
         
         ADD blocklist.yaml /.m4a/blocklist.yaml
         
         **# This example adds the redis-server service.
         # Add the following lines to install redis-server.
         RUN apt-get update && apt-get -y install redis-server
         
         # Use the servicemanager_generate_config add command to add
         # redis-server to the configuration:
         RUN /servicemanager_generate_config add redis-server -u /.m4a/
         **
         # Migrate to Containers image includes entrypoint
         ENTRYPOINT [ "/.v2k.go" ]

  2. Build the updated image and push to Container Registry with an updated version tag, ensuring you allow enough time for the build to finish. In the following example, the image is in the current directory:
         
         gcloud builds submit --timeout 4h --tag gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL .

  3. Deploy the newly built image:
         
         kubectl set image deployment/myWorkload my-app=gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL --record




## servicemanager_generate_config syntax

The `servicemanager_generate_config` utility takes the following options:

  * `build-all -o /.m4a/`: Rebuilds the migration and writes the configuration to the `m4a` directory. Do not change the name of the directory.

Use this form of the command when you first convert your migration to use the simplified Linux service manager.

  * `update -u /.m4a/`: Update the list of existing services in the `m4a` directory. Do not change the name of the directory.

  * `add SERVICE_NAME -u /.m4a/`: Add service name to the migration and writes the configuration to the `m4a` directory. Do not change the name of the directory.

To add multiple services, add multiple `RUN /servicemanager_generate_config` commands, one per service.




## What's next

  * Learn about [new enhanced runtime](https://docs.cloud.google.com/migrate/containers/docs/autopilot-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
