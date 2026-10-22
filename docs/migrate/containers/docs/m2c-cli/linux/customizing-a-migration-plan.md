---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/linux/customizing-a-migration-plan/
title: Customize migration plan for Linux VMs \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:21.632985+00:00
---

# Customize migration plan for Linux VMs  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/linux/customizing-a-migration-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customize migration plan for Linux VMs

Before executing a migration plan, you should review and optionally customize it. The details of your migration plan are used to extract the workload's container artifacts from the source VM, and also to generate Kubernetes deployment files that you can use to deploy the container image to other clusters, such as a production cluster.

This page describes the migration plan's contents and the kinds of customizations you might consider before you execute the migration and generate deployment artifacts.

## Before you begin

This topic assumes that you've already [created a migration plan](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) and have the resulting migration plan file.

## Edit the migration plan

After you have copied the file system and analyzed it, you can find the migration plan in the new directory that is created in the specified output path: ANALYSIS_OUTPUT_PATH/`config.yaml`.

Edit the migration plan as necessary and save the changes.

Review your migration plan details and guiding comments to add information as needed. Specifically, consider edits around the following sections.

### Specify content to exclude from the migration

By default, Migrate to Containers excludes typical VM content that isn't relevant in the context of GKE. You can customize that filter.

The `filters` field value lists paths that should be excluded from migration and will not be part of the container image. The field's value lists rsync filter rules that specify which files to transfer and which to skip. Preceding each path and file with a minus sign specifies that the item in the list should be excluded from migration. The list is processed according to the order of lines in the YAML, and exclusions/inclusions are evaluated accordingly.

Learn more about [rsync filter rules](https://download.samba.org/pub/rsync/rsync.html#FILTER_RULES).

Files that are too large to be included in the Docker image are listed in the YAML file. This will flag files that are larger than 1 GB for your consideration. Docker images that are too large, or greater than 15 GB, are at risk of failure during migration.

You can edit the YAML list to add or remove paths. See an example YAML below, which includes example exclusions, as well as notifications for large and sparse files. Follow the inline guidance to perform one of the following actions:

  * Exclude the detected folders by uncommenting them and placing them under the global filters section.
  * Move the detected folders to to a persistent volume by uncommenting them and placing them under the data folder section.



You can also exclude or move the detected sparse files in the same manner.
    
    
      global:
        # Files and directories to exclude from the migration, in rsync format.
        filters:
          - "- *.swp"
          - "- /etc/fstab"
          - "- /boot/"
          - "- /tmp/*"
          - "- /var/log/*.log*"
          - "- /var/log/*/*.log*"
          - "- /var/cache/*"
    
        ## The data folders below are too large to be included in the docker image.
        ## Consider uncommenting and placing them under either the global filters
        ## or the data folder section.
          # - '- /a' # (1.8GB, last access 2022-02-02 10:50:30, last modified 2020-02-02 10:50:30)
          # - '- /a/c' # (1.8GB, last access 2022-02-02 10:50:30, last modified 2020-02-02 10:50:30)
    
        ## Sparse files will fail the run of a docker image. Consider excluding the below
        ## detected files and any other sparse files by uncommenting and placing them in 
        ## the global filters section, or export them to a persistent volume by specifying
        ## them in the data folder section.
          # - '- /a/b' # (1.8GB, last access 2022-02-02 10:50:30, last modified 2020-02-02 10:50:30)
          # - '- /a/d' # (1.8GB, last access 2022-02-02 10:50:30, last modified 2020-02-02 10:50:30)
    

### Set the name of the container image

The `name` field value in the `image` section defines the name of the image created from a migrated VM that is used for the container. You can change this value if you prefer to use a different name.
    
    
    image:
         # Review and set the name for runnable container image.
         name: linux-system
    

### Customize the services list

By default, Migrate to Containers [disables unneeded services](https://docs.cloud.google.com/migrate/containers/docs/planning-best-practices#disable_unneeded_services) on a VM when you migrate it to a container. These services can sometimes cause issues with the migrated container, or are not needed in a container context.

Along with the services automatically disabled by Migrate to Containers, you can optionally disable other services:

  * Migrate to Containers automatically discovers services that you can optionally disable and lists them in the migration plan. These services, such as `ssh` or a web server, might not be required in your migrated workload but it is up to you to make that decision. If necessary, edit the migration plan to disable these services.

  * Migrate to Containers does not list all services running on the source VM. For example, it omits operating-system related services. You can optionally edit the migration plan to add your own list of services to disable in the migrated container.




The `systemServices` field specifies the list of services discovered by Migrate to Containers. For example:
    
    
        systemServices:
        - enabled: true|false
          name: service-name
          probed: true|false
        - enabled: true|false
          name: service-name
          probed: true|false
          ...

To disable a service, set `enabled` to `false`.

Migrate to Containers does not list all services running on the source VM, such as operating-system related services. You can also add additional services to the list. For example, to disable `service2` and the `cron` service:
    
    
        systemServices:
        - enabled: true
          name: service1
          probed: false
        **- enabled: false
          name: service2
          probed: false
        - enabled: false
          name: cron
          probed: false**

When you [execute a migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan) to generate the migration artifacts, Migrate to Containers creates the `blocklist.yaml` file. This file lists the container services to disable based on your settings in the migration plan. For example:
    
    
    service_list:
    - name: disabled-services
      services:
      # Because you used systemServices above to disabled service2 and cron:
      **- service2
      - cron**

To later modify the list of disabled services:

  * Edit the list of services in the migration plan.
  * [Execute the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan) to regenerate the migration artifacts, including an updated `blocklist.yaml`.



Alternatively, after you execute a migration to generate the migration artifacts, you can edit the `blocklist.yaml` file directly, and then [build and deploy the container image using Skaffold](https://docs.cloud.google.com/migrate/containers/docs/build-deploy-using-skaffold).

### Customize service endpoints

The migration plan includes the `endpoints` array that defines the ports and protocols used to create the Kubernetes Services provided by the migrated workload. You can add, edit, or delete endpoint definitions to customize the migration plan.

To retrieve the endpoints ports, check the programs that are listening ports:
    
    
    sudo netstat --programs --listening --tcp --udp [--sctp]
    

For each Service endpoint, add the following definition to the migration plan:
    
    
        endpoints:
        - port: PORT_NUMBER
          protocol: PORT_PROTOCOL
          name: PORT_NAME

Where:

  * PORT_NUMBER specifies the container port number to which requests to the service are routed.
  * PORT_PROTOCOL specifies the port protocol, such as HTTP, HTTPS, or TCP. See [Supported protocols](https://kubernetes.io/docs/concepts/services-networking/service/#protocol-support) for the complete list of protocols.
  * PORT_NAME specifies the name used to access the Service endpoint. Migrate to Containers generates a unique PORT_NAME for each generated endpoint definitions.



For example, Migrate to Containers detects the following endpoints:
    
    
      endpoints:
        - port: 80
          protocol: HTTP
          name: backend-server-nginx
        - port: 6379
          protocol: TCP
          name: backend-server-redis

To set the value of the `name` property, Migrate to Containers combines the source VM name, `backend-server` in this example, with the program name of the Service. The generated names are compatible with Kubernetes naming conventions, and are unique within the migration plan. For example, the migration plan above creates a Service that targets Nginx on port 80 over HTTP.

For any duplicate names, Migrate to Containers appends a counter suffix. For example, if Nginx is associated with two ports, it adds the `-2` suffix to the `name` in the second definition:
    
    
      endpoints:
        - port: 80
          protocol: HTTP
          name: **backend-server-nginx**
        - port: 8080
          protocol: HTTPS
          name: **backend-server-nginx-2**
        - port: 6379
          protocol: TCP
          name: backend-server-redis

When you execute a migration to generate the migration artifacts, Migrate to Containers creates a [Service](https://kubernetes.io/docs/concepts/services-networking/service/) definition in the `deployment_spec.yaml` file for each endpoint.

For example, shown below is a `Service` definition in the `deployment_spec.yaml` file:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      creationTimestamp: null
      name: backend-server-nginx
    spec:
      ports:
      - port: 80
        protocol: HTTP
        targetPort: 80
      selector:
        app: backend-server
    status:
      loadBalancer: {}

### Customize NFS mounts

Migrate to Containers includes NFS mounts in the generated migration plan. This information is collected from the `fstab` file and written to the `nfsMounts` array in the migration plan. You can add or edit NFS mount point definitions to customize the migration plan.

**Note:** The entries in `nfsMounts` array are disabled by default. You must enable them if you want Migrate to Containers to generate entries in the `deployment_spec.yaml` file for each NFS mount.

When generating the migration plan, Migrate to Containers:

  * Ignores NFS mounts for `/sys` and `/dev`.
  * Ignores NFS mounts with a type other than `nfs` or `nfs4`.



Each NFS mount in the migration plan includes the server's IP address and local mount path in the form:
    
    
        nfsMounts:
        - mountPoint: MOUNT_POINT
          exportedDirectory: DIR_NAME
          nfsServer: IP
          mountOptions:
             - OPTION_1
             - OPTION_2
          enabled: false|true

Where:

  * MOUNT_POINT specifies the mount point obtained from `fstab`.
  * DIR_NAME specifies the name of the shared directory.
  * IP specifies the IP address of the server hosting the mount point.
  * OPTION_N specifies any options extracted from the `fstab` for the mount point.



For example, for the following entry in `fstab`:
    
    
    <file system>       <mount point>   <type>  <options>   <dump>  <pass>
    10.49.232.26:/vol1  /mnt/test       nfs     rw,hard     0       0

Migrate to Containers generates the following entry in the migration plan:
    
    
        nfsMounts:
        - mountPoint: /mnt/test
          exportedDirectory: /vol1
          nfsServer: 10.49.232.26
          mountOptions:
             - rw
             - hard
          enabled: false

To configure Migrate to Containers to process entries in the `nfsMounts` array, set `enabled` to `true` for the `mountPoint` entry. You can enable one, some, or all `mountPoints` entries, edit the entries, or add your own entries.

When you execute a migration to generate the migration artifacts, Migrate to Containers creates a [volumes and volumeMounts](https://kubernetes.io/docs/concepts/storage/volumes/) definition and a [PersistentVolume and PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) definition in the `deployment_spec.yaml` file for each enabled NFS mount.

**Note:** Migrate to Containers requires that NFS servers be accessible from the deployment cluster hosting the migrated container workload. However, Migrate to Containers does not validate that connectivity. A migrated container with a connectivity issue cannot be started and you might have to edit the `deployment_spec.yaml` file to fix the issue. See [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver) for more information. 

For example, shown below is a `volumeMounts` definition in the `deployment_spec.yaml` file:
    
    
        spec:
          containers:
              - image: gcr.io/myimage-1/image-name
                name: some-app
                volumeMounts:
                       - mountPath: /sys/fs/cgroup
                         name: cgroups
                       **- mountPath: /mnt/test
                         name: nfs-pv**

Where the value of `name` is a unique identifier generated by Migrate to Containers.

Shown below is an example `PersistentVolumeClaim` and `PersistentVolume` definitions in the `deployment_spec.yaml` file:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 1Mi
      storageClassName: ""
      volumeName: nfs-pv
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: nfs-pv
    spec:
      mountOptions:
        - rw
        - hard
      nfs:
        path: /vol1
        server: 10.49.232.26

### Customize log data written to Cloud Logging

Typically a source VM writes information to one or more log files. As part of migrating the VM, you can configure the migrated workload to write that log information to [Cloud Logging](https://docs.cloud.google.com/logging/docs).

**Note:** Previous releases of Migrate to Containers supported customizing logging by using a `ConfigMap` on your target workload cluster, as described in [Configuring logging to Cloud Logging](https://docs.cloud.google.com/migrate/containers/docs/configuring-cloud-logging). This section describes how to use the `logs.yaml` file to configure logging. If the `logs.yaml` file exists, logging settings defined by a `ConfigMap` are ignored.

When you generate the migration plan, Migrate to Containers automatically searches for log destination files on the source VM. Migrate to Containers then writes information about those detected files to the `logPaths` area of the migration plan:
    
    
    deployment:
        ...
        logPaths:
        - appName: APP_NAME
          globs:
          - LOG_PATH

For example:
    
    
    deployment:
        ...
        logPaths:
        - appName: tomcat
          globs:
          - /var/log/tomcat*/catalina.out

When you generate the migration artifacts, Migrate to Containers generates the `logs.yaml` file from the migration plan. This file contains the list of log files detected on the source VM. For example, from the `logsPath` definition above, `logs.yaml` contains:
    
    
    logs:
      tomcat:
      - /var/log/tomcat*/catalina.out

In this example, when you deploy the migrated workload, log information written to `catalina.out` is automatically written to Cloud Logging.

Entries each appear on a line in the log in the following form:
    
    
    DATE TIME APP_NAME LOG_OUTPUT
    

The following example illustrates the form with an entry from Tomcat:
    
    
    2019-09-22 12:43:08.681193976 +0000 UTC tomcat log-output
    

To configure logging, you can either:

  * Edit the migration plan before you generate the migration artifacts to add, remove, or edit `logPaths` entries. When you generate the migration artifacts, these edits are reflected in the `logs.yaml` file.

  * Edit `logs.yaml` after you generate the migration artifacts to add, remove, or edit `logs` entries.




The advantage to editing the migration plan is that your edits are reflected in `logs.yaml` every time you generate the artifacts. If you edit `logs.yaml` directly, then regenerate the artifacts for some reason, you have to reapply your edits to `logs.yaml`.

## Set Linux v2kServiceManager health probes

You can monitor the downtime and ready status of your managed containers by specifying probes in your Tomcat web server's migration plan. Health probe monitoring can help reduce the downtime of migrated containers and provide better monitoring.

Unknown health states can create availability degradation, false-positive availability monitoring, and potential data loss. Without a health probe, kubelet can only assume the health of a container and may send traffic to a container instance that is not ready. This can cause traffic loss. Kubelet may also not detect containers that are in a frozen state and will not restart them.

A health probe functions by running a small scripted statement when the container starts. The script checks for successful conditions, which are defined by the type of probe used, every period. The period is defined in the migration plan by a `periodSeconds` field. You can run or define these scripts manually.

To learn more about kubelet probes, see [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) in the Kubernetes documentation.

There are two types of probes available to configure, both probes are probe-v1-core defined in [probe-v1-core reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#probe-v1-core) and share the same function as the corresponding fields of [container-v1-core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#container-v1-core)

  * **Liveness probe** \- Liveness probes are used to know when to restart a container. **Note:** If a process in your container is able to crash on its own when it encounters an issue, or becomes unhealthy, you do not necessarily need a liveness probe. The kubelet will automatically perform the correct action in accordance with the Pod's `restartPolicy`.

  * **Readiness probe** \- Readiness probes are used to know when a container is ready to start accepting traffic. To start sending traffic to a Pod only when a probe succeeds, specify a readiness probe. A readiness probe may act similarly to a liveness probe, but a readiness probe in the specifications indicates that a Pod will start without receiving any traffic and only start receiving traffic after the probe succeeds.



After discovery, the probe configuration is added to the migration plan. The probes can be used in their default configuration as shown below. To disable probes, remove the `probes` section from the yaml.
    
    
    deployment:
      probes:
        livenessProbe:
          exec:
            command:
            - /ko-app/service-manager-runtime
            - /probe
    
        readinessProbe:
          exec:
            command:
            - gamma
            - /probe
          initialDelaySeconds: 60
          periodSeconds: 5
    
    image:
      # Disable system services that do not need to be executed at the migrated workload containers.
      # Enable the 'probed' property to include system services in the container health checks.
      systemServices:
      - enabled: true
        name: apache2
        probed: true
      - enabled: true
        name: atd
        probed: false 
    

By default, all service probing is disabled. You must define which subset of services will be monitored. 

**Note:** Not all services support probing and may cause a container to fail to start up.

There are four pre-defined ways to check a container using a probe. Each probe must define exactly one of these four mechanisms: 

  * `exec` \- Executes a specified command inside the container. Execution is considered successful if the exit status code is 0.
  * `grpc` \- Performs a remote procedure call using `gRPC`. `gRPC` probes are an alpha feature.
  * `httpGet` \- Performs an HTTP GET request against the Pod's IP address on a specified port and path. The request is considered successful if the status code is greater than or equal to 200 and less than 400.
  * `tcpSocket` \- Performs a TCP check against the Pod's IP address on a specified port. The diagnostic is considered successful if the port is open.



By default, a migration plan enables the `exec` probing method. Use manual configuration for your migration plan to enable another method.

To add external dependencies for the readiness probe, while using the default liveness probe, define an exec readiness probe and a script that implements the logic.

## What's next

  * Learn how to [execute the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
