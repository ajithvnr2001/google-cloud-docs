---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade/
title: Upgrading Apigee hybrid to version 1.9 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:41:51.926907+00:00
---

# Upgrading Apigee hybrid to version 1.9  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.9 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/upgrade.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/upgrade.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/upgrade.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/upgrade.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/upgrade.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/upgrade.html)



This procedure covers upgrading from Apigee hybrid version 1.8.x to Apigee hybrid version 1.9.4 and from previous releases of hybrid 1.9.x to version 1.9.4. 

Use the same procedures for minor version upgrades (for example version 1.8 to 1.9) and for patch release upgrades (for example 1.9.0 to 1.9.4). 

If you are upgrading from Apigee hybrid version 1.7 or older, you must first upgrade to hybrid version 1.8 before upgrading to version 1.9.4. See the instructions for [Upgrading Apigee hybrid to version 1.8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/upgrade). 

Starting with version 1.9.0, Apigee hybrid only supports Apigee ingress gateway as the ingress layer.

##  Upgrading to version 1.9.4 overview 

Upgrading to Apigee hybrid version 1.9 may require downtime. 

When upgrading the Apigee controller to version 1.9.4, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.

Apigee recommends that you upgrade all clusters as soon as possible to reduce the chances of production impact. There is no time limit on when all remaining clusters must be upgraded after the first one is upgraded. However, until all remaining clusters are upgraded the following operations will be impacted:

  * Cassandra backup and restore cannot work with mixed versions. For example, a backup from Hybrid 1.8 cannot be used to restore a Hybrid 1.9 instance.
  * Cassandra data streaming will not work between mixed Hybrid versions. Therefore, your Cassandra clusters cannot scale horizontally.
  * Region expansion and decommissioning will be impacted, because these operations depend on Cassandra data streaming.

**Note:** Management plane changes do not need to be suspended during an upgrade. Any required suspension to management plane changes are included in the upgrade instructions.

The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Prepare to upgrade.
  2. Install hybrid runtime version 1.9.4.



##  Prerequisites 

  * These upgrade instructions assume you have Apigee hybrid version 1.8.x installed and wish to upgrade it to version 1.9.4. If you are updating from an earlier version, see the instructions for [Upgrading Apigee hybrid to version 1.8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/upgrade).
  * In Apigee hybrid version 1.8, we introduced Apigee ingress gateway as an alternative ingress layer to Anthos Service Mesh. Starting with version 1.9.0, Apigee hybrid requires using Apigee ingress gateway and no longer supports using Anthos Service Mesh for ingress. If the installation you are upgrading from uses Anthos Service Mesh, you must first migrate to using Apigee ingress gateway before upgrading to version 1.9.4. 

Apigee ingress gateway uses a small subset of Anthos Service Mesh features for the ingress gateway. Management and upgrade of those features are handled automatically by Apigee hybrid. Therefore you do not need expertise with Anthos Service Mesh to install, upgrade, and manage the Apigee hybrid ingress gateway. 

See [Migrating to Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/migrating-to-apigee-ingress) in the hybrid v1.8 documentation for instructions.




##  Prepare to upgrade to version 1.9 

###  Back up your hybrid installation (recommended) 

  1. These instructions use the environment variable APIGEECTL_HOME for the directory in your file system where you have installed `apigeectl`. If needed, change directory into your `apigeectl` directory and define the variable with the following command: 

###  Linux 
         
         export APIGEECTL_HOME=$PWD
         echo **$APIGEECTL_HOME**

###  Mac OS 
         
         export APIGEECTL_HOME=$PWD
         echo **$APIGEECTL_HOME**

###  Windows 
         
         set APIGEECTL_HOME=%CD%
         echo %APIGEECTL_HOME%

  2. Make a backup copy of your version 1.8 `$APIGEECTL_HOME/` directory. For example: 
         
         tar -czvf **$APIGEECTL_HOME** /../apigeectl-v1.8-backup.tar.gz **$APIGEECTL_HOME**

  3. Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-backup-overview).



###  Add the **Cloud Trace Agent** role to the service account for the Apigee runtime. (Optional) 

Optional: If you plan to use [Cloud trace](https://docs.cloud.google.com/trace/docs/overview) and you have not already added the `Cloud Trace Agent` role to your hybrid v1.8 installation, ensure your service account for your Apigee runtime services has the **Cloud Trace Agent** Google Cloud IAM role (`roles/cloudtrace.agent`). 

For production environments, runtime service account is `apigee-runtime`. For non-production environments, runtime service account is `apigee-non-prod`. 

You can add the role in the [Cloud console > IAM & Admin > Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) UI or with the following commands: 

  1. Get the email address for your service account with the following command: 

###  Production 
         
         gcloud iam service-accounts list --filter "apigee-runtime"

If the email address matches the pattern `apigee-runtime@**$ORG_NAME**.iam.gserviceaccount.com`, you can use that pattern in the next step. 

###  Non-Prod 
         
         gcloud iam service-accounts list --filter "apigee-non-prod"

If it matches the pattern `apigee-non-prod@**$ORG_NAME**.iam.gserviceaccount.com`, you can use that pattern in the next step. 

  2. Assign the **Cloud Trace Agent** role to the service account: 

###  Production 
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:**apigee-runtime** @$PROJECT_ID.iam.gserviceaccount.com" \
             --role="**roles/cloudtrace.agent** "

###  Non-Prod 
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:**apigee-non-prod** @$PROJECT_ID.iam.gserviceaccount.com" \
             --role="**roles/cloudtrace.agent** "

###  Example 
         
         gcloud projects add-iam-policy-binding hybrid-example-project \
             --member="serviceAccount:apigee-runtime@hybrid-example-project.iam.gserviceaccount.com" \
             --role="**roles/cloudtrace.agent** "

Where: $PROJECT_ID is the name of the Google Cloud project where Apigee hybrid is installed. 

**Note:** If your installation uses a custom name for the service account, substitute that name for `apigee-runtime` or `apigee-non-prod` in the command.



###  Install Apigee ingress gateway if your installation uses Anthos Service Mesh 

Starting with version 1.9, Apigee hybrid no longer supports using Anthos Service Mesh for ingress. If your hybrid installation is using Anthos Service Mesh, you must migrate your current installation to Apigee ingress gateway before installing hybrid version 1.9. 

  1. Add the [`ingressGateways`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways) property to your overrides file. 

### Syntax
         
         ingressGateways:
           - name: INGRESS_NAME
             replicaCountMin: REPLICAS_MIN
             replicaCountMax: REPLICAS_MAX
             resources:
               requests:
                 cpu: CPU_COUNT_REQ
                 memory: MEMORY_REQ
               limits:
                 cpu: CPU_COUNT_LIMIT
                 memory: MEMORY_LIMIT
             svcAnnotations:  # optional.
               SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
             svcLoadBalancerIP: SVC_LOAD_BALANCER_IP # optional

### Example
         
         ingressGateways:
           - name: prod1
             replicaCountMin: 2
             replicaCountMax: 100
             resources:
               requests:
                 cpu: 1
                 memory: 1Gi
               limits:
                 cpu: 2
                 memory: 2Gi
             svcAnnotations:  # optional. See [Known issue 243599452](https://docs.cloud.google.com/apigee/docs/release/known-issues#243599452).
               networking.gke.io/load-balancer-type: "Internal"
             svcLoadBalancerIP: 198.252.0.123 

     * INGRESS_NAME is the name of the ingress deployment. This can be any name that meets the following requirements: 
       * Have a maximum length of 17 characters
       * Contain only lowercase alphanumeric characters, '-' or '.'
       * Start with an alphanumeric character
       * End with an alphanumeric character
See [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-name) in the Configuration property reference.
     * REPLICAS_MIN and REPLICAS_MAX are the minimum and maximum replica counts for Apigee ingress gateway in your installation. For more information and default settings, see [`ingressGateways[].replicaCountMin`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-replicacountmin) and [`ingressGateways[].replicaCountMax`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-replicacountmax) in the Configuration property reference.
     * CPU_COUNT_REQ and MEMORY_REQ are the CPU and memory request for each replica of Apigee ingress gateway in your installation. Set these properties if you have previously set them for your Anthos Service Mesh ingress gateway, for example in your `overlay.yaml` file.

For more information and default settings, see [`ingressGateways[].resources.requests.cpu`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-resources-requests-cpu) and [`ingressGateways[].resources.requests.memory`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-resources-requests-memory) in the Configuration property reference. 

     * CPU_COUNT_LIMIT and MEMORY_LIMIT Are the maximum CPU and memory limits for each replica of Apigee ingress gateway in your installation. Set these properties if you have previously set them for your Anthos Service Mesh ingress gateway, for example in your `overlay.yaml` file.

For more information and default settings, see [`ingressGateways[].resources.limits.cpu`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-resources-limits-cpu) and [`ingressGateways[].resources.limits.memory`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-resources-limits-memory) in the Configuration property reference.

     * SVC_ANNOTATIONS_KEY SVC_ANNOTATIONS_VALUE (optional): **Note:** The `ingressGateways[].svcAnnotations` field in `overrides.yaml` is not working as expected. See [Known issue 243599452](https://docs.cloud.google.com/apigee/docs/release/known-issues#243599452)

This is a key-value pair that provides annotations for your default ingress service. Annotations are used by your cloud platform to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. For example: 
           
           ingressGateways:
               svcAnnotations:
                 networking.gke.io/load-balancer-type: "Internal"

Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations.

**Note:** You do not need to set `Annotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress).  See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-svcannotations) in the Configuration property reference.
     * SVC_LOAD_BALANCER_IP (optional) Allows you to assign a static IP address for your load balancer. On platforms that support specifying the load balancer IP address, the load balancer will be created with this IP address. On platforms that do not allow you to specify the load balancer IP address, this property is ignored. 

If you do not have a static IP address allocated for your load balancer, leave this property out of your overrides file.

**Caution:** Make sure not to specify the same IP address as the current istio-ingressgateway. This could cause problems while that service is still on the cluster. **Note:** You do not need to set `LoadBalancerIP` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress).  See [`ingressGateways[].svcLoadBalancerIP`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-svcloadbalancerip) in the Configuration property reference.
  2. Apply the changes to install Apigee ingress gateway with the following commands: 
         
         **$APIGEECTL_HOME** /apigeectl apply -f overrides/overrides.yaml

  3. Expose the Apigee ingress gateway. Follow the procedures in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress).
  4. Test your new ingress gateway by calling a proxy. Ideally, test all crucial proxies you currently have deployed.
  5. To switch the traffic, update your DNS records to point to the IP address for your new Apigee ingress gateway. Depending on your DNS provider, you might be able to gradually shift traffic to the new endpoint. **Tip:** You can find the external IP address of Apigee ingress gateway with the following command: 
         
         kubectl get svc -n apigee -l app=apigee-ingressgateway

Your output should look something like: 
         
         NAME                                        TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)                                      AGE
         apigee-ingressgateway-prod-hybrid-37a39bd   LoadBalancer   192.0.2.123   **233.252.0.123**   15021:32049/TCP,80:31624/TCP,443:30723/TCP   16h

  6. Ensure all the runtime traffic is working by monitoring your dashboards. Only proceed to the next step if everything is working as expected. Make sure no traffic is going through your old ingress gateway (Anthos Service Mesh), as the DNS update may be slow to propagate because of DNS caching.
  7. To stop Apigee from supplying configuration to Anthos Service Mesh, follow the steps in [Stop supplying configuration to ASM](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/managing-ingress#stop-supplying-configuration) in the Managing Apigee ingress gateway guide. 
  8. Retest and monitor API proxy traffic.
  9. Follow the instructions in the Anthos Service Mesh documentation to [Uninstall Anthos Service Mesh](https://cloud.google.com/service-mesh/docs/uninstall) from the cluster.



##  Install the hybrid 1.9.4 runtime 

**Caution:** Do not create new environments during the upgrade process.

  1. Be sure you are in the hybrid base directory (the parent of the directory where the `apigeectl` executable file is located): 
         
         cd **$APIGEECTL_HOME** /..

  2. Download the release package for your operating system using the following command. Be sure to select your platform in the following table:

###  Linux 

**Linux 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.9.4** /apigeectl_linux_64.tar.gz

###  Mac OS 

**Mac 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.9.4** /apigeectl_mac_64.tar.gz

###  Windows 

**Windows 64 bit:**
         
         curl -LO ^
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.9.4** /apigeectl_windows_64.zip

  3. Rename your current `apigeectl/` directory to a backup directory name. For example: 

###  Linux 
         
         mv $APIGEECTL_HOME/ $APIGEECTL_HOME-v1.8/

###  Mac OS 
         
         mv $APIGEECTL_HOME/ $APIGEECTL_HOME-v1.8/ 

###  Windows 
         
         rename %APIGEECTL_HOME% %APIGEECTL_HOME%-v1.8 

  4. Extract the downloaded gzip file contents into your hybrid base directory. The hybrid base directory is the directory where the renamed `apigeectl-v1.8` directory is located:

###  Linux 
         
         tar xvzf filename.tar.gz -C ./

###  Mac OS 
         
         tar xvzf filename.tar.gz -C ./

###  Windows 
         
         tar xvzf filename.zip -C ./

  5. The tar contents are, by default, expanded into a directory with the version and platform in its name. For example: `./apigeectl_1.9.4-xxxxxxx_linux_64`. Rename that directory to `apigeectl` using the following command:

###  Linux 
         
         mv apigeectl_1.9.4-xxxxxxx_linux_64 apigeectl

###  Mac OS 
         
         mv apigeectl_1.9.4-xxxxxxx_mac_64 apigeectl

###  Windows 
         
         rename apigeectl_1.9.4-xxxxxxx_windows_64 apigeectl

  6. Change to the `apigeectl` directory: 
         
         cd ./apigeectl

This directory is the `apigeectl` home directory. It is where the `apigeectl` executable command is located. 

  7. These instructions use the environment variable `**$APIGEECTL_HOME**` for the directory in your file system where the `apigeectl` utility is installed. If needed, change directory into your `apigeectl` directory and define the variable with the following command: 

###  Linux 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Mac OS 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Windows 
         
         set APIGEECTL_HOME=%CD%
         
         echo %APIGEECTL_HOME%

  8. Verify the version of `apigeectl` with the `version` command: 
         
         ./apigeectl version
         
         Version: 1.9.4

  9. Move to the `hybrid-base-directory/hybrid-files` directory. The `hybrid-files` directory is where configuration files such as the overrides file, certs, and service accounts are located. For example: 
         
         cd **$APIGEECTL_HOME** /../hybrid-files

  10. Verify that `kubectl` is set to the correct context using the following command. The current context should be set to the cluster in which you are upgrading Apigee hybrid. 
         
         kubectl config get-contexts | grep \*

  11. In the `hybrid-files` directory: 
     1. Update the following symbolic links to `$APIGEECTL_HOME`. These links allow you to run the newly installed `apigeectl` command from inside the `hybrid-files` directory: 
            
            ln -nfs $APIGEECTL_HOME/tools tools
            ln -nfs $APIGEECTL_HOME/config config
            ln -nfs $APIGEECTL_HOME/templates templates
            ln -nfs $APIGEECTL_HOME/plugins plugins

     2. To check that the symlinks were created correctly, execute the following command and make sure the link paths point to the correct locations: 
            
            ls -l | grep ^l

  12. Do a dry run initialization to check for errors: 
         
         **${APIGEECTL_HOME}** /apigeectl init -f OVERRIDES_FILE --dry-run=client

Where OVERRIDES_FILE is the name of your overrides file, for example `./overrides/overrides.yaml`. 

**Tip:** You can replace `OVERRIDES_FILE` in the code sample above with the name and path to your overrides file, and every instance on this page will be replaced.
  13. If there are no errors, initialize hybrid 1.9.4: 
         
         $APIGEECTL_HOME/apigeectl init -f OVERRIDES_FILE

**Note:** `apigeectl` installs and configures Apigee ingress gateway when you run `apigeectl init`. 
  14. Check the initialization status: 
         
         $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

On success, the output says: `All containers ready.`
         
         kubectl describe apigeeds -n apigee

In the output, look for `State: running`. 

  15. Check for errors with a dry run of the `apply` command using the `--dry-run` flag: 
         
         $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --dry-run=client

  16. If there are no errors, apply your overrides. Select and follow the instructions for production environments or non-prod environments, depending on your installation. 

### Production

For production environments, upgrade each hybrid component individually, and check the status of the upgraded component before proceeding to the next component. 

     1. Be sure you are in the `hybrid-files` directory.
     2. Apply your overrides to upgrade Cassandra: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --datastore

     3. Check completion: 
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

**Tip:** If `check-ready` fails, you can get more information about your pods with: 
            
            kubectl -n NAMESPACE get pods

Where NAMESPACE is your Apigee hybrid namespace. 

Proceed to the next step only when the pods are ready. 

     4. Apply your overrides to upgrade Telemetry components and check completion: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --telemetry
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

     5. Bring up Redis components: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --redis

     6. Apply your overrides to upgrade the org-level components (MART, Watcher and Apigee Connect) and check completion: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --org
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

     7. Apply your overrides to upgrade your environments. You have two choices: 
        * **Environment by environment** : Apply your overrides to one environment at a time and check completion. Repeat this step for each environment: 
              
              $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --env ENV_NAME
              
              $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

Where ENV_NAME is the name of the environment you are upgrading. 

        * **All environments at one time** : Apply your overrides to all environments at once and check completion: 
              
              $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --all-envs
              
              $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

     8. Apply your overrides to upgrade the `virtualhosts` components and check completion: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --settings virtualhosts
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

### Non-prod

In most non-production, demo, or experimental environments, you can apply the overrides to all components at once. If your non-production environment is large and complex or closely mimics a production environment, you may want to use the instructions for upgrading production environments. 

     1. Be sure you are in the `hybrid-files` directory.
     2. $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE

     3. Check the status: 
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE




## Install `1.9.4-hotfix.1`

Follow these steps to install the hotfix release, `1.9.4-hotfix.1`:

  1. Before doing these steps, you must be on Apigee hybrid version 1.9.4 or a later version. If you are not on 1.9.4 or later, perform an upgrade to 1.9.4 before proceeding.
  2. Open your `overrides.yaml` file.
  3. In the `istiod` stanza, change the version of the image tag (if present) to version ` 1.17.7`. For example: 
         
         istiod:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-asm-istiod"
             tag: "1.17.7-asm.0-distroless"

  4. Depending on how you chose to install Apigee hybrid, you may have an `ingressGateway` or `ingressGateways` stanza. Locate the stanza that appears in your overrides file and change the version of the image tag (if present) to version ` 1.17.7`. For example, if you have an `ingressGateway` stanza: 
         
         ingressGateway:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-asm-ingress"
             tag: "1.17.7-asm.0-distroless"

or, if you have an `ingressGateways` stanza:
         
         ingressGateways:
           - name: gateway1
             image:
               url: "gcr.io/apigee-release/hybrid/apigee-asm-ingress"
               tag: "1.17.7-asm.0-distroless"
             ...
           - name: gateway2
             image:
               url: "gcr.io/apigee-release/hybrid/apigee-asm-ingress"
               tag: "1.17.7-asm.0-distroless"
             ...
           

  5. Save the file.
  6. Execute the following command to initialize the `istiod` component: 
         
         $APIGEECTL_HOME/apigeectl init -f OVERRIDES_FILE
         
         $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

  7. Execute the following command to apply changes to the Apigee ingress component(s). If you have more than one organization, repeat this command for each one: 
         
         $APIGEECTL_HOME/apigeectl apply --org -f OVERRIDES_FILE
         
         $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

  8. Verify the status of your pods: 
         
         kubectl get pods -n YOUR_APIGEE_NAMESPACE




##  Upgrade your Kubernetes version 

Upgrade your Kubernetes platform to the versions supported by hybrid 1.9. Follow your platform's documentation if you need help. 

### _Click to expand a list of supported platforms_

| Apigee hybrid versions  
---|---  
  
### Platforms

|  1.6 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3) | 1.7 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3) | 1.8 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3) | 1.9 | 1.10  
Anthos (Google Cloud - GKE) | 1.19.x  
1.20.x  
1.21.x | 1.20.x   
1.21.x   
1.22.x (≥ 1.7.2)   
1.23.x (≥ 1.7.2) | 1.21.x (≤ 1.8.3)   
1.22.x (≤ 1.8.3)   
1.23.x (≤ 1.8.4)   
1.24.x (≥ 1.8.4)   
1.25.x (≥ 1.8.4) | 1.23.x   
1.24.x   
1.25.x   
1.26.x (≥ 1.9.2) | 1.24.x   
1.25.x   
1.26.x   
Anthos (AWS) | 1.7.x  
1.8.x  
1.9.3+  
1.10.x | 1.9.x   
1.10.x   
1.12.x (≥ 1.7.2) | 1.10.x   
1.11.x   
1.12.x   
1.13.x   
1.25(13) | 1.12.x   
1.13.x   
1.25(13) | 1.13.x   
1.25(13)   
1.26(13)  
Anthos (Azure) | 1.8.x | 1.9.x   
1.10.x   
1.12.x (≥ 1.7.2) | 1.10.x   
1.11.x   
1.12.x   
1.13.x   
1.14.x  | 1.12.x   
1.13.x   
1.14.x  | 1.13.x   
1.14.x   
1.15.x   
Anthos (on-premises - VMware)(1) | 1.7.x  
1.8.x  
1.9.3+  
1.10.x | 1.9.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)(≥ 1.7.2)   
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4) (≥ 1.7.2) | 1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)(5)   
1.13.x (5)   
1.14.x (5)   
1.15.x  | 1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.13.x   
1.14.x   
1.15.x  | 1.13.x   
1.14.x   
1.15.x   
1.16.x   
Anthos (Bare Metal)(1) | 1.7.x  
1.8.2+  
1.9.3+  
1.10.x | 1.9.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4) (≥ 1.7.2)   
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4) (≥ 1.7.2) | 1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4) (5)   
1.13.x (5)   
1.14.x (5)   
1.15.x  | 1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(4)   
1.13.x   
1.14.x   
1.15.x  | 1.13.x   
1.14.x   
1.15.x   
1.16.x   
EKS(7) | 1.19.x  
1.20.x  
1.21.x | 1.21.x   
1.22.x (≥ 1.7.2)   
1.23.x (≥ 1.7.2) | 1.22.x (≤ 1.8.3)   
1.23.x (≤ 1.8.4)   
1.24.x (≥ 1.8.4)   
1.25.x (≥ 1.8.4) | 1.23.x   
1.24.x   
1.25.x   
1.26.x (≥ 1.9.2) | 1.24.x   
1.25.x   
1.26.x   
AKS(7) | 1.19.x  
1.20.x  
1.21.x | 1.21.x   
1.22.x (≥ 1.7.2)   
1.23.x (≥ 1.7.2) | 1.22.x (≤ 1.8.3)   
1.23.x (≤ 1.8.4)   
1.24.x (≥ 1.8.4)   
1.25.x (≥ 1.8.4) | 1.23.x   
1.24.x   
1.25.x   
1.26.x (≥ 1.9.2) | 1.24.x   
1.25.x   
1.26.x   
OpenShift(7) | 4.6  
4.7  
4.8 | 4.7   
4.8  | 4.8   
4.9   
4.10  | 4.10   
4.11  | 4.11   
4.12   
Rancher Kubernetes Engine (RKE)(7) | N/A | N/A | N/A | 1.3.8 | v1.26.2+rke2r1   
  
### Components

| 1.6 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3) | 1.7 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3) | 1.8 | 1.9 | 1.10  
Anthos Service Mesh (ASM) | 1.9.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg) | 1.10.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(≥ 1.7.2)  
1.14.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.15.x (≥ 1.7.6) | 1.11.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.12.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.13.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.14.x ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)  
1.15.x  |  1.17.x(11) |  1.17.x(11)  
JDK | JDK 11 | JDK 11 | JDK 11 | JDK 11 | JDK 11  
cert-manager | 1.5.4 | 1.7.x | 1.7.x   
1.8.x   
1.9.x   
1.10.x   
1.11.x | 1.10.x   
1.11.x | 1.10.x  
1.11.x  
1.12.x   
Cassandra | 3.11.10 | 3.11.10 | 3.11.10 | 3.11.10 | 3.11.10  
**(1) On Anthos versions 1.8, 1.9, and 1.10, follow the instructions in these documents to avoid conflict with `cert-manager`:**

  * **Anthos 1.8.2+** : [ Conflict with `cert-manager` when upgrading to version 1.8.2 or above](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.8/known-issues#conflict_with_cert-manager_when_upgrading_to_version_182_or_above). 
  * **Anthos 1.9** : [ Conflict with `cert-manager` when upgrading to version 1.9.0 or 1.9.1](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/known-issues#conflict_with_cert-manager_when_upgrading_to_version_190_or_191). 
  * **Anthos 1.10+** : [ Conflicting `cert-manager` installation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/known-issues#conflicting_cert-manager_installation). 

**(2) Support available with Apigee hybrid version 1.7.2 and newer**. **(3) The official EOL dates for Apigee hybrid versions 1.8 and older have been reached. Regular monthly patches are no longer available. These releases are no longer officially supported except for customers with explicit and official exceptions for continued support. Other customers must upgrade**.  **(4) Anthos on Bare Metal and VMWare versions 1.12 and earlier are out of support. See the [ Anthos on Bare Metal Version Support Policy](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/getting-support#version-support) and the [ Anthos clusters on VMware versions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#supported-versions).** **(5) Anthos on Bare Metal and VMWare [ requires ASM 1.14](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support#112) or later. We recommend that you upgrade to hybrid v1.8 and switch to Apigee ingress gateway which no longer requires you to install ASM on your hybrid cluster.** **(6) Support available with Apigee hybrid version 1.8.4 and newer**.  **(7) Attached clusters are not required for Apigee hybrid v1.8 and newer using [ Apigee ingressgateway](https://cloud.google.com/apigee/docs/hybrid/latest/managing-ingress).**.  **(8) Not supported with Apigee hybrid version 1.8.4 and newer**.  **(9) Support available with Apigee hybrid version 1.7.6 and newer**.  **(10) Not supported with Apigee hybrid version 1.8.5 and newer**.  **(11) ASM is automatically installed with Apigee hybrid 1.9 and newer**.  **(12) Support available with Apigee hybrid version 1.9.2 and newer**.  **(13) Anthos clusters on AWS (Multi-Cloud) version numbers now reflect the Kubernetes versions. See [Anthos version and upgrade support](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support#anthos-on-other-public-clouds) for version details and recommended patches**.   
  
###  About attached clusters 

For Apigee hybrid versions 1.7.x and older, you must use Anthos [attached clusters](https://cloud.google.com/anthos/clusters/docs/attached) if you want to run Apigee hybrid in a multi-cloud context on Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), or another supported third-party Kubernetes service provider. Cluster attachment allows Google to measure the usage of Anthos Service Mesh (ASM). [_Registering_](https://docs.cloud.google.com/anthos/clusters/docs/attached/how-to/attach-kubernetes-clusters#register_your_cluster) the third-party cluster is optional. Register only if you wish to view the attached cluster in the Google Cloud console. For more information, see [Attach third-party Kubernetes clusters to Google Cloud](https://docs.cloud.google.com/anthos/clusters/docs/attached/how-to/attach-kubernetes-clusters). 

For Apigee hybrid version 1.8.x, Anthos attached clusters are required if you are using Anthos Service Mesh for your ingress gateway. If you are using Apigee ingress gateway, Anthos attached clusters are optional. 

**Note:** Hybrid installations are not currently supported on GKE Autopilot. **Congratulations!** You have upgraded to Apigee hybrid version 1.9.4. to test your upgrade, call a proxy against the new installation. For an example, see [Step 10: Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-deploy-proxy) in the Apigee hybrid 1.9 installation guide. 

##  Rolling back an upgrade 

Follow these steps to roll back a previous upgrade: 

  1. Clean up completed jobs for the hybrid runtime namespace, where NAMESPACE is the namespace specified in your overrides file, if you specified a namespace. If not, the default namespace is `apigee`: 
         
         kubectl delete job -n NAMESPACE \
           $(kubectl get job -n NAMESPACE \
           -o=jsonpath='{.items[?(@.status.succeeded==1)].metadata.name}')

  2. Clean up completed jobs for the `apigee-system` namespace: 
         
         kubectl delete job -n apigee-system \
           $(kubectl get job -n apigee-system \
           -o=jsonpath='{.items[?(@.status.succeeded==1)].metadata.name}')

  3. Change the `APIGEECTL_HOME` variable to point to the directory that contains the previous version of `apigeectl`. For example: 
         
         export APIGEECTL_HOME=PATH_TO_PREVIOUS_APIGEECTL_DIRECTORY

  4. In the root directory of the installation you want to roll back to, run `apigeectl apply`, check the status of your pods, and then run `apigeectl init`. Be sure to use the original overrides file for the version you wish to roll back to: 
     1. In the hybrid-files directory, run `apigeectl apply`: 
            
            $APIGEECTL_HOME/apigeectl apply -f ORIGINAL_OVERRIDES_FILE

Where ORIGINAL_OVERRIDES_FILE is the relative path and filename of the overrides file for your previous version hybrid installation, for example, `./overrides/overrides1.8.yaml`. 

     2. Check the status of your pods: 
            
            kubectl -n NAMESPACE get pods

Where NAMESPACE is your Apigee hybrid namespace. 

     3. Check the status of `apigeeds`: 
            
            kubectl describe apigeeds -n apigee

Your output should look something like: 
            
            Status:
              Cassandra Data Replication:
              Cassandra Pod Ips:
                10.8.2.204
              Cassandra Ready Replicas:  1
              Components:
                Cassandra:
                  Last Successfully Released Version:
                    Revision:  v1-f8aa9a82b9f69613
                    Version:   v1
                  Replicas:
                    Available:  1
                    Ready:      1
                    Total:      1
                    Updated:    1
                  State:        running
              Scaling:
                In Progress:         false
                Operation:
                Requested Replicas:  0
              State:                 running

Proceed to the next step only when the `apigeeds` pod is running. 

     4. Run the following command to make note of what your new replica count values will be for the message processor after the upgrade. If these values do not match what you have set previously, change the values in your overrides file to match your previous configuration. 
            
            apigeectl apply -f ORIGINAL_OVERRIDES_FILE --dry-run=client --print-yaml --env ENV_NAME 2>/dev/null |grep "runtime:" -A 25 -B 1| grep "autoScaler" -A 2

Your output should look something like: 
            
            autoScaler:
                    minReplicas: 2
                    maxReplicas: 10

     5. Run `apigeectl init`: 
            
            $APIGEECTL_HOME/apigeectl init -f ORIGINAL_OVERRIDES_FILE




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
