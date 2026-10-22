---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-agent/
title: Migrate clusters to use Node Agent \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:20.962030+00:00
---

# Migrate clusters to use Node Agent  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Migrate clusters to use Node Agent Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install and migrate clusters to Node Agent to provide more secure cluster operations. Node Agent is a more secure, agent-based model than Ansible over SSH for cluster operations, available for versions 1.33 and later. When you manage cluster operations with Node Agent, you can access customer nodes in sensitive environments without SSH.

The Node Agent binary runs on each node. Node Agent communicates with clients, such as controllers, through a secure [gRPC](https://grpc.io/) channel to manage all node configuration activities. Google Distributed Cloud enforces mutual Transport Layer Security (mTLS) between the cluster controller and Node Agent and between `bmctl` and Node Agent for the authentication and encryption of the gRPC connections.

Use [`bmctl nodeagent`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent) commands to reduce manual effort, improve consistency across nodes, and automate certificate creation and rotation. The `bmctl` commands operate primarily over SSH so you can deploy agents even when the cluster controller is unhealthy or its standard communication channels are impaired.

## Before you begin

Make sure all cluster nodes meet the following requirements before migrating a cluster to Node Agent mode:

  * An open port dedicated for Node Agent. Node Agent uses port 9192 by default. Configure this port when you deploy, enable, or install a new cluster. For more information, see Customize the Node Agent port.

  * Containerd version 1.7 or higher.

  * 12 GB of free space in the `/tmp` directory on the admin node and all target nodes. If you can't change the size of the `/tmp` directory for your target nodes, see Increase local storage capacity for Node Agent backups.




## Migrate to Node Agent mode

Migrating to Node Agent mode is a two-step process:

  1. **Deploy the Node Agent** : Deploy the Node Agent component to all nodes within the cluster.

  2. **Enable Node Agent mode** :

     * For an existing cluster, enable the mode using the `bmctl nodeagent` command.
     * For a new cluster, add the enablement annotation and corresponding credentials paths to the cluster configuration file before creation.



### Deploy Node Agent

The `bmctl nodeagent deploy` command deploys the Node Agent service to one or more target nodes within a specified cluster using SSH. This command installs or reinstalls the Node Agent. It connects through SSH and performs the necessary steps, including transferring binaries, optionally generating and transferring certificates, and setting up the systemd service. It requires SSH access and sudo privileges on the target nodes.

You can specify target nodes in several ways: directly through the `--nodes` flag, through a cluster configuration file using the `--cluster` flag, or by referencing the cluster custom resource. For a more information about Node Agent commands and options, see the [bmctl command reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl).

#### Deploy in a fresh environment

For initial deployments, download the `nodeagentd` binary and generate new Certificate Authorities (CAs). The following command retrieves the node list from the cluster configuration file. The `--sa-key` flag provides the necessary credentials for downloading the `nodeagentd` binary from the Cloud Storage bucket.

  * To deploy Node Agent for the first time on a new cluster, use the following command:
        
        bmctl nodeagent deploy \
            --pull-binaries=true \
            --generate-ca-creds=true \
            --cluster CLUSTER_NAME \
            --ssh-user USERNAME \
            --ssh-key SSH_KEY_PATH \
            --sa-key SERVICE_ACCOUNT_KEY_PATH
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.

    * `USERNAME`: the username for which SSH access to nodes is configured. By default, SSH is configured for `root`, but if you [set a login user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#set_a_login_user), use that username.

    * `SSH_KEY_PATH`: the path of the SSH private key file.

    * `SERVICE_ACCOUNT_KEY_PATH`: the path of the service account key file with permissions to pull registry images. By default, this is the JSON key file for the `anthos-baremetal-gcr` service account.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_deploy-20250819-175703/nodeagent_deploy.log
    [2025-08-19 17:57:03+0000] INFO: Executing 'nodeagent deploy'...
    [2025-08-19 17:57:05+0000] -------------------- Deployment Plan --------------------
    [2025-08-19 17:57:05+0000]   Target Cluster:            demo-cluster
    [2025-08-19 17:57:05+0000]   SSH User:                  root
    [2025-08-19 17:57:05+0000]   SSH Key:                   rootSSH
    [2025-08-19 17:57:05+0000]   Concurrency:               25
    [2025-08-19 17:57:05+0000]   Generate Credentials:      true
    [2025-08-19 17:57:05+0000]   Deploy Credentials:        true
    [2025-08-19 17:57:05+0000]   Server Cert Validity Days: 1825
    [2025-08-19 17:57:05+0000]   Verify SSH Host Keys:      true
    [2025-08-19 17:57:05+0000]   Node Agent pull version:   1.33.0-gke.799
    [2025-08-19 17:57:05+0000]   Target Nodes Source:       cluster YAML
    [2025-08-19 17:57:05+0000]   Nodes Port:                9192
    [2025-08-19 17:57:05+0000]   Target Nodes (4):          10.200.0.2, 10.200.0.3, 10.200.0.4, 10.200.0.5
    [2025-08-19 17:57:05+0000] ---------------------------------------------------------
    Proceed with deployment? [y/N]: y
    [2025-08-19 17:57:07+0000] INFO: User confirmed.
    [2025-08-19 17:57:07+0000] Downloading Node Agent binary (1.33.0-gke.799)... OK
    [2025-08-19 17:57:08+0000] INFO: Node Agent binary pulled and stored at bmctl-workspace/bins/nodeagentd
    [2025-08-19 17:57:08+0000] INFO: Starting generate credentials (CAs and client credentials) phase...
    [2025-08-19 17:57:08+0000] Generating credentials for the cluster: demo-cluster, 2025-08-19T17:57:08Z
    [2025-08-19 17:57:08+0000] ------------ Credentials Options ------------
    [2025-08-19 17:57:08+0000] Cluster Name:           demo-cluster
    [2025-08-19 17:57:08+0000] Key Algorithm:          rsa
    [2025-08-19 17:57:08+0000] Key Length:             4096
    [2025-08-19 17:57:08+0000] CA Validity (days):     3650
    [2025-08-19 17:57:08+0000] Client Validity (days): 1825
    [2025-08-19 17:57:08+0000] Server CA CN:           Node Agent Server CA
    [2025-08-19 17:57:08+0000] Client CA CN:           Node Agent Client CA
    [2025-08-19 17:57:08+0000] Creds path:             bmctl-workspace/demo-cluster/nodeagent-creds
    [2025-08-19 17:57:08+0000] --------------------------------------------
    [2025-08-19 17:57:08+0000] Generating credentials... OK
    [2025-08-19 17:57:19+0000] Certificates have been created and stored in bmctl-workspace/demo-cluster/nodeagent-creds
    [2025-08-19 17:57:19+0000] INFO: Attempting to load CAs from: bmctl-workspace/demo-cluster/nodeagent-creds
    [2025-08-19 17:57:19+0000] INFO: Server CA loaded successfully. Subject: CN=Node Agent Server CA,O=GCD-SO,L=Sunnyvale,ST=California,C=US, Key Type: *rsa.PrivateKey
    [2025-08-19 17:57:19+0000] INFO: Client CA loaded successfully. Subject: CN=Node Agent Client CA,O=GCD-SO,L=Sunnyvale,ST=California,C=US, Key Type: *rsa.PrivateKey
    [2025-08-19 17:57:19+0000] ===============================================
    [2025-08-19 17:57:19+0000] --- Starting Artifact Preparation ---
    [2025-08-19 17:57:19+0000] Starting artifact preparation for 4 nodes (concurrency: 25)...
    [2025-08-19 17:57:23+0000] --- Finished Artifact Preparation ---
    [2025-08-19 17:57:23+0000] INFO: Preparation SUCCEEDED for node 10.200.0.2
    [2025-08-19 17:57:23+0000] INFO: Preparation SUCCEEDED for node 10.200.0.3
    [2025-08-19 17:57:23+0000] INFO: Preparation SUCCEEDED for node 10.200.0.4
    [2025-08-19 17:57:23+0000] INFO: Preparation SUCCEEDED for node 10.200.0.5
    [2025-08-19 17:57:23+0000] ===============================================
    [2025-08-19 17:57:23+0000] --- Starting Deployment Phase ---
    [2025-08-19 17:57:23+0000] INFO: Starting deployment to 4 nodes (Concurrency: 25)...
    [2025-08-19 17:57:36+0000] INFO: All host deployments finished.
    [2025-08-19 17:57:36+0000] INFO: --- Deployment Phase Completed Successfully ---
    [2025-08-19 17:57:36+0000]
    ===============================================
    --- Deployment Summary ---
      Host: 10.200.0.2, Status: SUCCESS
      Host: 10.200.0.3, Status: SUCCESS
      Host: 10.200.0.4, Status: SUCCESS
      Host: 10.200.0.5, Status: SUCCESS
    -----------------------------------------------
    Total Nodes Attempted: 4 | SUCCESS: 4 | FAILED: 0
    ===============================================
    




#### Upgrade Node Agent version

Node Agent upgrades are independent from cluster upgrades. To upgrade Node Agent, use the `bmctl nodeagent deploy` command and set `--pull-binaries` to `true`. When upgrading the Node Agent, set `--generate-ca-creds` to `false` to use existing CAs rather than regenerating them. Regenerating CAs requires updating corresponding cluster credentials, a process reserved for credential rotation. The output resembles a fresh deployment, but without the CA-generated logs.

Upgrading the Node Agent restarts the Node Agent process, which can disrupt any running jobs. Although most jobs recover through retry mechanisms, to minimize potential disruptions use the following steps:

  1. Make sure there is no cluster upgrade or other post-installation configuration activities in progress.

  2. Verify that the cluster is in a running state.

  3. Initiate the Node Agent upgrade:
         
         bmctl nodeagent deploy \
             --pull-binaries=true \
             --generate-ca-creds=false \
             --cluster CLUSTER_NAME \
             --ssh-user USERNAME \
             --ssh-key SSH_KEY_PATH \
             --sa-key SERVICE_ACCOUNT_KEY_PATH
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.

     * `USERNAME`: the username for which SSH access to nodes is configured. By default, SSH is configured for `root`, but if you [set a login user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#set_a_login_user), use that username.

     * `SSH_KEY_PATH`: the path of the SSH private key file.

     * `SERVICE_ACCOUNT_KEY_PATH`: the path of the service account key file with permissions to pull registry images. By default, this is the JSON key file for the `anthos-baremetal-gcr` service account.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_deploy-20250819-180416/nodeagent_deploy.log
    [2025-08-19 18:04:16+0000] INFO: Executing 'nodeagent deploy'...
    [2025-08-19 18:04:18+0000] -------------------- Deployment Plan --------------------
    [2025-08-19 18:04:18+0000]   Target Cluster:            demo-cluster
    [2025-08-19 18:04:18+0000]   SSH User:                  root
    [2025-08-19 18:04:18+0000]   SSH Key:                   rootSSH
    [2025-08-19 18:04:18+0000]   Concurrency:               25
    [2025-08-19 18:04:18+0000]   Generate Credentials:      false
    [2025-08-19 18:04:18+0000]   Deploy Credentials:        true
    [2025-08-19 18:04:18+0000]   Server Cert Validity Days: 1825
    [2025-08-19 18:04:18+0000]   Verify SSH Host Keys:      true
    [2025-08-19 18:04:18+0000]   Node Agent pull version:   1.33.0-gke.799
    [2025-08-19 18:04:18+0000]   Target Nodes Source:       cluster YAML
    [2025-08-19 18:04:18+0000]   Nodes Port:                9192
    [2025-08-19 18:04:18+0000]   Target Nodes (4):          10.200.0.2, 10.200.0.3, 10.200.0.4, 10.200.0.5
    [2025-08-19 18:04:18+0000] ---------------------------------------------------------
    Proceed with deployment? [y/N]: y
    [2025-08-19 18:04:20+0000] INFO: User confirmed.
    [2025-08-19 18:04:20+0000] Downloading Node Agent binary (1.33.0-gke.799)... OK
    [2025-08-19 18:04:22+0000] INFO: Node Agent binary pulled and stored at bmctl-workspace/bins/nodeagentd
    [2025-08-19 18:04:22+0000] INFO: Attempting to load CAs from: bmctl-workspace/demo-cluster/nodeagent-creds
    [2025-08-19 18:04:22+0000] INFO: Server CA loaded successfully. Subject: CN=Node Agent Server CA,O=gcd-SO,L=Sunnyvale,ST=California,C=US, Key Type: *rsa.PrivateKey
    [2025-08-19 18:04:22+0000] INFO: Client CA loaded successfully. Subject: CN=Node Agent Client CA,O=gcd-SO,L=Sunnyvale,ST=California,C=US, Key Type: *rsa.PrivateKey
    [2025-08-19 18:04:22+0000] ===============================================
    [2025-08-19 18:04:22+0000] --- Starting Artifact Preparation ---
    [2025-08-19 18:04:22+0000] Starting artifact preparation for 4 nodes (concurrency: 25)...
    




#### Deploy or redeploy to specific nodes

If you add or recover cluster nodes, you can target the specific nodes for Node Agent deployment, instead of deploying it to all nodes in the cluster. You use the `--nodes` flag to specify the node for deployment.

  * To deploy Node Agent to specific nodes, use the following command:
        
        bmctl nodeagent deploy \
            --pull-binaries=true \
            --cluster CLUSTER_NAME \
            --ssh-user USERNAME \
            --ssh-key SSH_KEY_PATH \
            --sa-key SERVICE_ACCOUNT_KEY_PATH \
            --nodes NODE_IP_ADDRESS_LIST
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.

    * `USERNAME`: the username for which SSH access to nodes is configured. By default, SSH is configured for `root`, but if you [set a login user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#set_a_login_user), use that username.

    * `SSH_KEY_PATH`: the path of the SSH private key file.

    * `SERVICE_ACCOUNT_KEY_PATH`: the path of the service account key file with permissions to pull registry images. By default, this is the JSON key file for the `anthos-baremetal-gcr` service account.

    * `NODE_IP_ADDRESS_LIST`: a comma-separated list of the IP addresses of the nodes to which you are deploying Node Agent.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_deploy-20250819-181751/nodeagent_deploy.log
    [2025-08-19 18:17:51+0000] INFO: Executing 'nodeagent deploy'...
    [2025-08-19 18:17:54+0000] -------------------- Deployment Plan --------------------
    [2025-08-19 18:17:54+0000]   Target Cluster:            demo-cluster
    [2025-08-19 18:17:54+0000]   SSH User:                  user
    [2025-08-19 18:17:54+0000]   SSH Key:                   SSH_KEY_PATH
    [2025-08-19 18:17:54+0000]   Concurrency:               25
    [2025-08-19 18:17:54+0000]   Generate Credentials:      false
    [2025-08-19 18:17:54+0000]   Deploy Credentials:        true
    [2025-08-19 18:17:54+0000]   Server Cert Validity Days: 1825
    [2025-08-19 18:17:54+0000]   Verify SSH Host Keys:      true
    [2025-08-19 18:17:54+0000]   Node Agent pull version:   1.33.0-gke.799
    [2025-08-19 18:17:54+0000]   Target Nodes Source:       nodes flag
    [2025-08-19 18:17:54+0000]   Nodes Port:                9192
    [2025-08-19 18:17:54+0000]   Target Nodes (3):          10.200.0.2, 10.200.0.3
    [2025-08-19 18:17:54+0000] ---------------------------------------------------------
    Proceed with deployment? [y/N]:
    




For a complete list of `bmctl nodeagent deploy` command options, see [nodeagent deploy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent_deploy) in the `bmctl` command reference.

### Enable Node Agent

The `enable` command activates Node Agent mode within an existing running cluster after you deploy the Node Agent to all nodes within the cluster. This command also creates or updates the Node Agent credentials within the cluster.

**Important:** Enabling Node Agent mode is a one-way operation. You can't revert your cluster back to SSH mode.

#### Enable Node Agent for an existing running cluster

You can enable Node Agent on existing version 1.33 and later clusters.

To enable Node Agent on an existing cluster, do the following:

  1. Enable Node Agent on the cluster:
         
         ./bmctl nodeagent enable \
             --kubeconfig KUBECONFIG \
             --cluster CLUSTER_NAME \
             --namespace CLUSTER_NAMESPACE \
             --ensure-status=true
         

Replace the following:

     * `KUBECONFIG`: the path of the kubeconfig file for the cluster for which you are enabling Node Agent.

     * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.

     * `CLUSTER_NAMESPACE`: the namespace of the cluster to use to find the target cluster and cluster credentials and update the cluster resource. Defaults to `cluster-<CLUSTER-NAME>`.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_enable-20250819-183058/nodeagent_enable.log
    [2025-08-19 18:30:58+0000] Enable Node Agent for cluster: demo-cluster
    [2025-08-19 18:31:00+0000] Update Node Agent credentials
    [2025-08-19 18:31:00+0000] ----------------------------------------------------------
    [2025-08-19 18:31:00+0000] Server CA certificate path: bmctl-workspace/demo-cluster/nodeagent-creds/server_ca_cert.pem
    [2025-08-19 18:31:00+0000] Server CA private key path: bmctl-workspace/demo-cluster/nodeagent-creds/server_ca_key.pem
    [2025-08-19 18:31:00+0000] Client CA certificate path: bmctl-workspace/demo-cluster/nodeagent-creds/client_ca_cert.pem
    [2025-08-19 18:31:00+0000] Client CA private key path: bmctl-workspace/demo-cluster/nodeagent-creds/client_ca_key.pem
    [2025-08-19 18:31:00+0000] Client certificate path: bmctl-workspace/demo-cluster/nodeagent-creds/client_cert.pem
    [2025-08-19 18:31:00+0000] Client private key path: bmctl-workspace/demo-cluster/nodeagent-creds/client_key.pem
    [2025-08-19 18:31:00+0000] ----------------------------------------------------------
    [2025-08-19 18:31:00+0000] Node Agent client credentials secret has been created/updated
    [2025-08-19 18:31:00+0000] Node Agent server CA secret has been created/updated
    [2025-08-19 18:31:00+0000] Node Agent client CA secret has been created/updated
    [2025-08-19 18:31:00+0000] Successfully created/updated Node Agent credentials secrets in namespace cluster-demo-cluster
    [2025-08-19 18:31:00+0000] Annotation 'baremetal.cluster.gke.io/node-agent-port' not found on cluster cluster-demo-cluster/demo-cluster, no removal needed.
    [2025-08-19 18:31:00+0000] Successfully enable Node Agent for cluster: demo-cluster
    [2025-08-19 18:31:00+0000] ----------------------------------------------------------
    [2025-08-19 18:31:00+0000] Verifying Node Agent status on all nodes...
    [2025-08-19 18:31:00+0000] --------------------- Total nodes: 3 ----------------------
    [2025-08-19 18:31:00+0000] node: control-0--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1577
    [2025-08-19 18:31:00+0000] node: control-1--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1578
    [2025-08-19 18:31:00+0000] node: control-2--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1581
    [2025-08-19 18:31:00+0000] ----------------------------------------------------------
    [2025-08-19 18:31:00+0000] Verified Node Agent status on all nodes in cluster
    

  2. Include the Node Agent enable annotation in the cluster metadata section of the cluster configuration file:
         
         kind: Cluster
         metadata:
           annotations:**    baremetal.cluster.gke.io/enable-node-agent: ""**
         




## Install a new cluster

You can use Node Agent when you create version 1.33 and later clusters.

To use Node Agent for a new cluster, do the following:

  1. For a new admin cluster, add the following credentials file paths to the top section of the admin cluster configuration file:
         
         nodeAgentServerCACertificatePath: bmctl-workspace/demo-cluster/nodeagent-creds/server_ca_cert.pem
         nodeAgentServerCAPrivateKeyPath: bmctl-workspace/demo-cluster/nodeagent-creds/server_ca_key.pem
         nodeAgentClientCACertificatePath: bmctl-workspace/demo-cluster/nodeagent-creds/client_ca_cert.pem
         nodeAgentClientCAPrivateKeyPath: bmctl-workspace/demo-cluster/nodeagent-creds/client_ca_key.pem
         nodeAgentClientCertificatePath: bmctl-workspace/demo-cluster/nodeagent-creds/client_cert.pem
         nodeAgentClientPrivateKeyPath: bmctl-workspace/demo-cluster/nodeagent-creds/client_key.pem
         

  2. Include the Node Agent enable annotation in the cluster metadata section of the cluster configuration file:
         
         kind: Cluster
         metadata:
           annotations:**    baremetal.cluster.gke.io/enable-node-agent: ""**
         

  3. Follow the [standard instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview) for creating your cluster.




For a complete list of `bmctl nodeagent enable` command options, see [nodeagent enable](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent_enable) in the `bmctl` command reference.

## Rotate credentials

The `rotate-credentials` command rotates Node Agent credentials on both the nodes and within the cluster. This includes the ability to rotate the Certificate Authorities (CAs). The `--generate-ca-creds` flag directs the command to regenerate the CAs and use these newly generated CAs to sign the certificates for both the server (nodes) and client (controller).

**Note:** Rotating Node Agent credentials restarts the Node Agent process. Similar to an upgrade, initiate Node Agent credential rotation only when the cluster is in a running state and no other configurations are simultaneously applied.

  * To rotate credentials and regenerate and use new CAs, use the following command:
        
        bmctl nodeagent rotate-credentials \
            --kubeconfig KUBECONFIG \
            --generate-ca-creds=true \
            --cluster CLUSTER_NAME \
            --namespace CLUSTER_NAMESPACE \
            --ssh-user USERNAME \
            --ssh-key SSH_KEY_PATH
        

Replace the following:

    * `KUBECONFIG`: the path of the kubeconfig file for the cluster for which you are enabling Node Agent.

    * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.

    * `CLUSTER_NAMESPACE`: the namespace of the cluster to use to find the target cluster and cluster credentials and update the cluster resource. Defaults to `cluster-<CLUSTER-NAME>`.

    * `USERNAME`: the username for which SSH access to nodes is configured. By default, SSH is configured for `root`, but if you [set a login user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#set_a_login_user), use that username.

    * `SSH_KEY_PATH`: the path of the SSH private key file.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_rotate_credentials-20250819-184216/nodeagent_rotate_credentials.log
    [2025-08-19 18:42:16+0000] INFO: Executing 'nodeagent rotate-credentials'...
    [2025-08-19 18:42:18+0000] ------------------- Credentials Rotation  -------------------
    [2025-08-19 18:42:18+0000]   Target Cluster:            demo-cluster
    [2025-08-19 18:42:18+0000]   SSH User:                  root
    [2025-08-19 18:42:18+0000]   SSH Key:                   rootSSH
    [2025-08-19 18:42:18+0000]   Concurrency:               25
    [2025-08-19 18:42:18+0000]   Generate Credentials:      true
    [2025-08-19 18:42:18+0000]   Deploy Credentials:        true
    [2025-08-19 18:42:18+0000]   Server Cert Validity Days: 1825
    [2025-08-19 18:42:18+0000]   Verify SSH Host Keys:      true
    [2025-08-19 18:42:18+0000]   Target Nodes Source:       cluster CR
    [2025-08-19 18:42:18+0000]   Nodes Port:                9192
    [2025-08-19 18:42:18+0000]   Target Nodes (3):          10.200.0.2, 10.200.0.3, 10.200.0.4
    [2025-08-19 18:42:18+0000] ---------------------------------------------------------
    Proceed with credentials rotation? [y/N]: [2025-08-19 18:42:18+0000] INFO: Non-interactive mode enabled; automatically confirming.
    [2025-08-19 18:42:18+0000] INFO: Starting generate credentials (CAs and client credentials) phase...
    [2025-08-19 18:42:18+0000] Generating credentials for the cluster: demo-cluster, 2025-08-19T18:42:18Z
    [2025-08-19 18:42:18+0000] ------------ Credentials Options ------------
    [2025-08-19 18:42:18+0000] Cluster Name:           demo-cluster
    [2025-08-19 18:42:18+0000] Key Algorithm:          rsa
    [2025-08-19 18:42:18+0000] Key Length:             4096
    [2025-08-19 18:42:18+0000] CA Validity (days):     3650
    [2025-08-19 18:42:18+0000] Client Validity (days): 1825
    [2025-08-19 18:42:18+0000] Server CA CN:           Node Agent Server CA
    [2025-08-19 18:42:18+0000] Client CA CN:           Node Agent Client CA
    [2025-08-19 18:42:18+0000] Creds path:             bmctl-workspace/demo-cluster/nodeagent-creds
    [2025-08-19 18:42:18+0000] --------------------------------------------
    [2025-08-19 18:42:18+0000] Generating credentials... OK
    Credential directory 'bmctl-workspace/demo-cluster/nodeagent-creds' already exists. Do you want to back it up and continue? (y/N): y
    [2025-08-19 18:42:27+0000] INFO: User confirmed.
    [2025-08-19 18:42:27+0000] Credentials backup to bmctl-workspace/demo-cluster/nodeagent-creds_backup_20250819_184227
    [2025-08-19 18:42:27+0000] Certificates have been created and stored in bmctl-workspace/demo-cluster/nodeagent-creds
    [2025-08-19 18:42:27+0000] INFO: Attempting to load CAs from: bmctl-workspace/demo-cluster/nodeagent-creds
    [2025-08-19 18:42:27+0000] INFO: Server CA loaded successfully. Subject: CN=Node Agent Server CA,O=gcd-SO,L=Sunnyvale,ST=California,C=US, Key Type: *rsa.PrivateKey
    [2025-08-19 18:42:27+0000] INFO: Client CA loaded successfully. Subject: CN=Node Agent Client CA,O=gcd-SO,L=Sunnyvale,ST=California,C=US, Key Type: *rsa.PrivateKey
    [2025-08-19 18:42:27+0000] ===============================================
    [2025-08-19 18:42:34+0000] INFO: All host deployments finished.
    [2025-08-19 18:42:34+0000] INFO: --- Deployment Phase Completed Successfully ---
    [2025-08-19 18:42:34+0000]
    ===============================================
    --- Deployment Summary ---
      Host: 10.200.0.2, Status: SUCCESS
      Host: 10.200.0.3, Status: SUCCESS
      Host: 10.200.0.4, Status: SUCCESS
    -----------------------------------------------
    Total Nodes Attempted: 3 | SUCCESS: 3 | FAILED: 0
    ===============================================
    




For a complete list of `bmctl nodeagent rotate-credentials` command options, see [nodeagent rotate-credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent_rotate-credentials) in the `bmctl` command reference.

## Check status

The `status` command provides information on the running status of Node Agent on nodes. You can specify target nodes directly through the `--nodes` flag, through a cluster configuration file using the `--cluster` flag, or by referencing the cluster's custom resource.

When you obtain nodes from a cluster configuration file or the `--nodes` flag, the system retrieves credentials from the local file system. If the node source is a cluster custom resource, the system retrieves credentials from the cluster.

The following order of precedence determines the Node Agent port:

  1. `--port` flag
  2. Kubeconfig file
  3. Cluster configuration file



### Verify Node Agent status

Using just the `--cluster` flag, you can check the Node Agent status based on what's specified in the cluster configuration file.

  * To check the Node Agent status based on the cluster configuration file, use the following command:
        
        ./bmctl nodeagent status \
            --cluster CLUSTER_NAME \
            --namespace CLUSTER_NAMESPACE
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster you're checking.

    * `CLUSTER_NAMESPACE`: the namespace of the cluster to use to find the target cluster and cluster credentials and update the cluster resource. Defaults to `cluster-<CLUSTER-NAME>`.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_status-20250819-205707/nodeagent_status.log
    [2025-08-19 20:57:07+0000] Check Node Agent for cluster: demo-cluster
    [2025-08-19 20:57:09+0000] ----------------------------------------------------------
    [2025-08-19 20:57:09+0000] Verifying Node Agent status on all nodes...
    [2025-08-19 20:57:09+0000] **Target Nodes Source: cluster YAML**
    [2025-08-19 20:57:09+0000] --------------------- Total nodes: 4 ----------------------
    [2025-08-19 20:57:09+0000] node: control-0--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1175
    [2025-08-19 20:57:09+0000] node: control-1--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1174
    [2025-08-19 20:57:09+0000] node: control-2--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1176
    [2025-08-19 20:57:09+0000] node: worker-0--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1179
    [2025-08-19 20:57:09+0000] ----------------------------------------------------------
    [2025-08-19 20:57:09+0000] Verified Node Agent status on all nodes in cluster
    




### Verify Node Agent status from cluster

Using the `--cluster` flag together with the `--kubeconfig` flag, you can check the Node Agent status based on Cluster custom resource.

  * To check the Node Agent status based on the Cluster custom resource, use the following command:
        
        ./bmctl nodeagent status \
            --cluster CLUSTER_NAME \
            --kubeconfig KUBECONFIG
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.

    * `KUBECONFIG`: the path of the kubeconfig file for the cluster for which you are enabling Node Agent.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_status-20250819-205712/nodeagent_status.log
    [2025-08-19 20:57:12+0000] Check Node Agent for cluster: demo-cluster
    [2025-08-19 20:57:14+0000] ----------------------------------------------------------
    [2025-08-19 20:57:14+0000] Verifying Node Agent status on all nodes...
    [2025-08-19 20:57:14+0000] **Target Nodes Source: cluster CR**
    [2025-08-19 20:57:14+0000] --------------------- Total nodes: 3 ----------------------
    [2025-08-19 20:57:14+0000] node: control-0--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1180
    [2025-08-19 20:57:14+0000] node: control-1--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1179
    [2025-08-19 20:57:14+0000] node: control-2--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1180
    [2025-08-19 20:57:14+0000] ----------------------------------------------------------
    [2025-08-19 20:57:14+0000] Verified Node Agent status on all nodes in cluster
    




### Verify Node Agent status from nodes

Using the `--cluster` flag together with the `--nodes` flag, you can check the Node Agent status for specific cluster nodes.

  * To check the Node Agent status for specific nodes, use the following command:
        
        ./bmctl nodeagent status \
            --cluster CLUSTER_NAME \
            --nodes NODE_IP_ADDRESS_LIST
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.

    * `NODE_IP_ADDRESS_LIST`: a comma-separated list of the IP addresses of the nodes to which you are deploying Node Agent.

The command output resembles the following example:
    
    Please check the logs at bmctl-workspace/demo-cluster/log/nodeagent_status-20250819-210050/nodeagent_status.log
    [2025-08-19 21:00:50+0000] Check Node Agent for cluster: demo-cluster
    [2025-08-19 21:00:53+0000] ----------------------------------------------------------
    [2025-08-19 21:00:53+0000] Verifying Node Agent status on all nodes...
    [2025-08-19 21:00:53+0000] **Target Nodes Source: nodes flag**
    [2025-08-19 21:00:53+0000] --------------------- Total nodes: 1 ----------------------
    [2025-08-19 21:00:53+0000] node: control-0--893f0567cb79efc-9b9ec55816170dcf.lab.anthos, version: 1.33.0-gke.799, OS: linux, uptime (seconds): 1399
    [2025-08-19 21:00:53+0000] ----------------------------------------------------------
    [2025-08-19 21:00:53+0000] Verified Node Agent status on all nodes in cluster
    




For a complete list of `bmctl nodeagent status` command options, see [nodeagent status](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent_status) in the `bmctl` command reference.

## SSH user permissions

A non-root user can execute the `bmctl nodeagent` command. This requires that the user has either full no-password sudo permissions or an explicit no-password sudo allow list.

The explicit no-password sudo allow list for Node Agent has the following permissions:
    
    
    # Permission to create the necessary folders and set permissions.
    /bin/mkdir -p /etc/nodeagentd
    /bin/chmod 0755 /etc/nodeagentd
    /bin/mkdir -p /usr/local/bin
    /bin/chmod 0755 /usr/local/bin
    /bin/mkdir -p /etc/systemd/system
    /bin/chmod 0755 /etc/systemd/system
    
    # Permission to place the main application executable and link it.
    /bin/rm -f /usr/local/bin/nodeagentd-*
    /bin/touch /usr/local/bin/nodeagentd-*
    /bin/cp -f /home/deployer/.deploy_tmp_*/* /usr/local/bin/nodeagentd-*
    /bin/chmod 0755 /usr/local/bin/nodeagentd-*
    /bin/rm -f /usr/local/bin/nodeagentd
    /bin/ln -s /usr/local/bin/nodeagentd-* /usr/local/bin/nodeagentd
    
    # Permission to place configuration files in /etc/nodeagentd and set permissions.
    /bin/rm -f /etc/nodeagentd/*
    /bin/touch /etc/nodeagentd/*
    /bin/cp -f /home/deployer/.deploy_tmp_*/* /etc/nodeagentd/*
    /bin/chmod 0600 /etc/nodeagentd/*
    /bin/chmod 0644 /etc/nodeagentd/*
    
    # Permission to place the systemd unit file.
    /bin/rm -f /etc/systemd/system/nodeagentd.service
    /bin/touch /etc/systemd/system/nodeagentd.service
    /bin/cp -f /home/deployer/.deploy_tmp_*/* /etc/systemd/system/nodeagentd.service
    /bin/chmod 0644 /etc/systemd/system/nodeagentd.service
    
    # Permission to interact with systemd service.
    /bin/systemctl daemon-reload
    /bin/systemctl stop nodeagentd
    /bin/systemctl start nodeagentd
    /bin/systemctl enable --now nodeagentd
    
    # Permission to remove the temporary files used for the deployment.
    /bin/rm -f /home/deployer/.deploy_tmp_*/*
    

## SSH host key verification

Ensure all nodes are added to the `known_hosts` file on the admin workstation. Otherwise, disable host key verification during deployment ([`nodeagent deploy`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent_deploy)) and credential rotation ([`nodeagent rotate-credentials`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent_rotate-credentials)) by using the `--enforce-host-key-verify=false` flag.

## Customize the Node Agent port

The Node Agent allows for port customization. Specify this custom port during deployment using the `--port` flag. This propagates the setting to the Node Agent configuration on each node. The customized port must align with the client-side configuration, as detailed in the following methods.

### For existing clusters

To update an existing, running cluster, use the `--port` flag to specify the new custom port. This setting propagates to the clients (controllers).

### For new clusters

When creating a new cluster, add the following annotation to the cluster configuration to specify a custom port for the Node Agent:
    
    
    kind: Cluster
    metadata:
      annotations:**    baremetal.cluster.gke.io/node-agent-port: "10086"**
    

## Increase local storage capacity for Node Agent backups

In order to create a backup file for Node Agent nodes, you must have 12 GB of free space in the `/tmp` directory on the admin node and all target nodes. If you can't change the size of the `/tmp` directory for your target nodes, see Change local storage capacity for target nodes. If you can't change the size of the `/tmp` directory for the admin node, see Change local storage capacity for an admin node.

### Change local storage capacity for target nodes

If you can't change the target node's `/tmp` partition size, you can redirect the temporary folder to a partition with more capacity by applying a systemd environment override:

  1. Create a systemd override file at `/etc/systemd/system/nodeagentd.service.d/override.conf` that contains:
         
         [Service]
         Environment="TMPDIR=/var/tmp"
         

  2. Apply the configuration and restart the service:
         
         sudo systemctl daemon-reload
         sudo systemctl restart nodeagentd
         




### Change local storage capacity for an admin node

If the admin workstation running bmctl has limited space for the `/tmp` partition, set the `TMPDIR` variable locally when you start a backup:
    
    
      TMPDIR=/var/tmp bmctl backup cluster -c CLUSTER_NAME --kubeconfig KUBECONFIG
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster upon whose nodes you want to deploy Node Agent.
  * `KUBECONFIG`: the path of the kubeconfig file for the cluster you are enabling Node Agent.



## Performance

Deployment and enablement complete in less than one minute. Credential rotation runtime is comparable to, or faster than, a standard deployment.

**Note:** Performance metrics vary based on bootstrap machine resources (CPU, memory), network bandwidth, and node operational load. The figures derive from local tests on an idle 50-node cluster using a bootstrap machine configured with 4 CPU cores and 16 GB of memory.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
