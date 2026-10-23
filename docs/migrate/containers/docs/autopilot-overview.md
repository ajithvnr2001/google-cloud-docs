---
url: https://docs.cloud.google.com/migrate/containers/docs/autopilot-overview/
title: New enhanced runtime \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:39.057136+00:00
---

# New enhanced runtime  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/autopilot-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# New enhanced runtime

The original Linux service manager for Migrate to Containers relied on `sysv init` and `systemd`. The simplified Linux service manager replaces it with a simplified, container friendly alternative.

This simplified Linux service manager adds functionality that lets you deploy your migrated container workloads to:

  * **GKE Autopilot clusters**

  * **Cloud Run**




The simplified Linux service manager also resolves compatibility issues with Kubernetes plugins. For example, the simplified Linux service manager removes the requirement of defining a `hostpath` for `/sys/fs/cgroup` in the `deployment_spec.yaml` file and the need to create privileged containers.

### Before you begin

  * Migrate to Containers supplies a tool that you run on a VM workload to determine the _fit_ of the workload for migration to a container. For more information, see [Using the fit assessment tool](https://docs.cloud.google.com/migrate/containers/docs/fit-assessment).



### About GKE Autopilot clusters

Autopilot is a mode of operation in Google Kubernetes Engine (GKE). Autopilot is designed to reduce the operational cost of managing clusters, optimize your clusters for production, and yield higher workload availability. In Autopilot mode, GKE provisions and manages the underlying infrastructure of the cluster, including nodes and node pools, giving you an optimized cluster with an automated experience. 

**Note:** Autopilot is supported for GKE clusters but is not supported for GKE Enterprise clusters.

See [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) for more details. 

### About Cloud Run

[Cloud Run](https://docs.cloud.google.com/run/docs) is a managed compute platform that enables you to run stateless containers that are invokable by web requests or Pub/Sub events. The simplified Linux service manager lets you deploy your migrated container workloads on Cloud Run. 

**Note:** The container workload must be stateless to be deployed on Cloud Run. See [Developing your service](https://docs.cloud.google.com/run/docs/developing) for more information, including the complete list of requirements for deploying containers on Cloud Run.

### Using workload identity with Migrate to Containers and GKE

Migrate to Containers and GKE let you deploy your migrated workloads to [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal). Sometimes, you might use the same cluster as both the processing cluster and the deployment cluster. If you have enabled workload identity on your deployment cluster, ensure that you configure your deployment environment to support Migrate to Containers and GKE.

Also, you must ensure that any services started as part of the init process are configured correctly for workload identity. The steps you perform depend on the service manager for your cluster. See [Deploying a Linux workload to a target cluster](https://docs.cloud.google.com/migrate/containers/docs/deploying-to-target-cluster) for the configuration steps.

## Changes from the existing runtime

To use the simplified Linux service manager, you should be aware of the following changes and limitations from the existing runtime.

### New services-config.yaml artifact file added

If you enable the simplified Linux service manager, Migrate to Containers creates a new artifact file, `services-config.yaml`, when you generate the migration artifacts. Use this file to control application initialization on a deployed container. See [Using services-config.yaml](https://docs.cloud.google.com/migrate/containers/docs/services-config) for more information.

**Note:** The `services-config.yaml` is only created when you perform a **new** migration using Migrate to Containers version 1.15.0. It is not created when you convert an existing migration from a previous version to version 1.15.0.

### Readiness probes

When using the current runtime, Migrate to Containers adds a readiness probe in the `deployment_spec.yaml` file. When you enable the simplified Linux service manager, no readiness probe is added. 

If you want to add a readiness probe, we recommend that you use an HTTP readiness probe. See [Define readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes) for more information.

**Note:** You can add the simplified Linux service manager readiness probe to your Service definition:
    
    
            readinessProbe:
              exec:
                command:
                - /.m4a/gamma status
    

However, this probe might return a false negative result.

### syslog support

The simplified Linux service manager creates a Unix socket at `/dev/log` to support the syslog. The simplified Linux service manager forwards these log messages to `stdout` so that they are recorded by Kubernetes as container logs.

### Limitations

You should be aware of the following limitations when using the simplified Linux service manager.

#### Workload limitations

The simplified Linux service manager works best with the following types of workloads:

Image | Operating system | Services  
---|---|---  
Compute Engine Ubuntu 12.04 | Ubuntu 12.04 | apache2  
Compute Engine Ubuntu 14.04 | Ubuntu 14.04 | redis, mysql, apache2  
Compute Engine Ubuntu 18.04 | Ubuntu 18.04 | apache2, mysql, redis-server, tomcat  
RHEL SAP 7.4 | Red Hat | httpd  
Bitnami | Ubuntu | bitnami  
Compute Engine Memcached image | Debian 10.9 | bitnami  
Compute Engine Marketplace wordpress | Debian 9.13 | apache2, mysql, php  
Compute Engine Marketplace tomcat | Debian 9.13 | tomcat8  
Compute Engine Marketplace jenkins | Debian 10.9 | apache2, jenkins  
Compute Engine Marketplace moodle | Debian 9.13 | apache2, mysql, php7.4 fpm, phpsessionclean  
Compute Engine Marketplace Odoo | Debian 9.13 | odoo, nginx  
Compute Engine Marketplace Opencart | Debian 9.13 | apache2, mysql, php7.0 fpm, supervisor, mariadb  
Compute Engine Marketplace Erpnext | Debian 10.9 | nginx, redis-server, supervisor, mariadb  
Compute Engine Marketplace wildfly | Debian 10.10 | wildfly, cron  
  
#### systemd limitations

If you're using `systemd` as your init system, be aware of the following limitations:

  * `systemd` service [types](https://www.freedesktop.org/software/systemd/man/systemd.service.html#Type=) of `simple`,`exec`, and `notify` are treated as `exec` service. That means the service is considered started, when `exec` succeeds.

  * Notify sockets are supported for `[sd_notify()](https://www.freedesktop.org/software/systemd/man/sd_notify.html)` for `READY=1` messages only.

If needed, you can provide other readiness checks. For example, HTTP check or other types of check. 

  * Socket type unit files are not supported. Sockets are not created and no environment variables are created.




## Updates for version 1.9.0

The simplified Linux service manager for version 1.9.0 contains the following updates:

  * The Linux service manager has been released for general availability, and is no longer in Public Preview.

  * The procedure to [Convert existing container workloads to support Autopilot](https://docs.cloud.google.com/migrate/containers/docs/convert-runtime) has been changed. You now need to edit both the Dockerfile and the `deployment_spec.yaml` file for an existing migration to convert it.

  * The `config.yaml` file has been renamed to `services-config.yaml`.




## Updates for version 1.8.1

The simplified Linux service manager was originally released in Public Preview as part of Migrate to Containers version 1.8. The simplified Linux service manager for version 1.8.1 contains the following updates:

  * You no longer set an annotation in the migration plan to enable the simplified Linux service manager. Instead, you now set `v2kServiceManager`. See [Deploy containers to Autopilot clusters](https://docs.cloud.google.com/migrate/containers/docs/deploy-autopilot) for more.

  * The environment variable `HC_GAMMA_RUNTIME` has been renamed to `HC_V2K_SERVICE_MANAGER`.

  * The `prestart` and `poststart` entries in the `services-config.yaml` file now automatically populated. See [Using services-config.yaml](https://docs.cloud.google.com/migrate/containers/docs/services-config) for more.

  * Added support to the `services-config.yaml` file that lets you specify environment variables at the global level or at the application level. See [Using services-config.yaml](https://docs.cloud.google.com/migrate/containers/docs/services-config) for more.

  * Added logging support that lets you customize log data written to Cloud Logging. See [Customize log data written to Cloud Logging](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan#log-files) for more.




## What's next

  * Learn how to [migrate and deploy applications to GKE Autopilot clusters](https://docs.cloud.google.com/migrate/containers/docs/deploy-autopilot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
