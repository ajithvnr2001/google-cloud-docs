---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/SelfManagedMySQLImplementation/
title: MySQL database reference implementation on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:49.262441+00:00
---

# MySQL database reference implementation on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/SelfManagedMySQLImplementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  MySQL database reference implementation on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides a comprehensive, step-by-step tutorial for deploying a highly available _MySQL 8.4 InnoDB Cluster_ across three availability zones in a Google Distributed Cloud (GDC) air-gapped environment. This architecture leverages _Group Replication_ for Paxos-based consensus, _MySQL Router_ for intelligent connection routing, and _MySQL Shell_ for cluster orchestration.

By strictly utilizing Virtual Machines (VMs), this implementation bypasses GDC air-gapped limitations regarding cross-zone Kubernetes stretch clusters, ensuring full multi-zone resiliency without risking data loss.

This is the architecture diagram:

![Three VM architecture that runs a colocated stack of services.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/mysql-diagram.png)

## Before you begin

### Deploy VMs

Follow [Create and start a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start) to create three VMs in the three available zones.

Configure your local environment to establish an SSH connection to the VMs with a key pair: [Connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm#connect-to-linux-vm)

This is needed to use secure copy (SCP) to transfer the packages: [Transfer files](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/transfer-files)

For verification we used Ubuntu 22.04 OS, and `n3-standard-2-gdc` machine type. For a production environment, use a machine type with more resources.

Obtain the IPs of the VMs using:
    
    
    VM_NAME=$1
    
    if [[ -z "$VM_NAME" ]]; then
      echo "Error: VM_NAME must be provided."
      echo "Usage: $0 <VM_NAME>"
      exit 1
    fi
    
    # 1. Get External IP from 'instances list'
    EXT_IP=$(gdcloud compute instances list | awk -v vm="${VM_NAME}" '$1 == vm {print $5}')
    
    if [[ -z "$EXT_IP" ]]; then
      echo "Error: Could not find VM '${VM_NAME}' in the instance list."
      exit 1
    fi
    
    INTERNAL_IP=$(gdcloud compute instances describe "${VM_NAME}" | awk '/^status:/ {in_status=1} in_status && /- [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/ {print $2; exit}' | cut -d'/' -f1)
    
    if [[ -z "$INTERNAL_IP" ]]; then
      INTERNAL_IP="<Not assigned or not found>"
    fi
    
    echo "${VM_NAME}"
    echo "External IP: ${EXT_IP}"
    echo "Internal IP: ${INTERNAL_IP}"
    

### Configure environment variables

Set these variables in your local workstation shell session:
    
    
    export PROJECT_ID="your-project-id"
    export VM1_NAME="mysql-node-1"
    export VM2_NAME="mysql-node-2"
    export VM3_NAME="mysql-node-3"
    export VM1_IP="10.0.1.245" # Zone 1
    export VM2_IP="10.0.1.241" # Zone 2
    export VM3_IP="10.0.1.242" # Zone 3
    export CLUSTER_NAME="mysql-ha-cluster"
    

**Important:** Replace with your VM names and internal IPs.

### Network configuration

In case you need to reach the DB outside the project or outside the organization, remember to set up the PNP (Project Network Policy) accordingly.

Follow the sections of [PNP Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview) depending on the use case.

## Air-gapped software preparation

### Download packages using Docker

Run the following from a connected workstation to fetch MySQL 8.4 and Shell components:
    
    
    mkdir -p ./mysql-packages
    docker run --rm -v "$(pwd)/mysql-packages:/packages" ubuntu:22.04 bash -c "
      apt-get update && apt-get install -y curl gnupg apt-rdepends wget lsb-release
      curl -LsS https://dev.mysql.com/get/mysql-apt-config_0.8.39-1_all.deb -o config.deb
      # Configure for MySQL 8.4 LTS
      DEBIAN_FRONTEND=noninteractive dpkg -i config.deb 
      apt-get update
      cd /packages
      PACKAGES='mysql-server mysql-shell mysql-router'
      apt-get download \$(apt-cache depends --recurse --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances --no-pre-depends \${PACKAGES} | grep '^\w')
    "
    

### Transfer and install

Upload the `.deb` files to `/tmp/packages/` on all three VMs and install:
    
    
    # From workstation: scp ./mysql-packages/*.deb ${VM_IP}:/tmp/packages/
    # On each VM:
    sudo dpkg -i /tmp/packages/*.deb
    

Make sure the `dpkg` returns no errors. If it does, check the logs to see what deb packages you might be missing and include them in the download.

When prompted to set the root password, leave it blank. We will set the password later on.

## MySQL node configuration

### Configure MySQL for cluster usage

Edit `/etc/mysql/mysql.conf.d/mysqld.cnf` on all nodes to enable _GTIDs_ and binary logging:
    
    
    [mysqld]
    bind-address = 0.0.0.0
    server-id = 1 # Use 2 and 3 for other VMs
    gtid-mode = ON
    enforce-gtid-consistency = ON
    binlog-format = ROW
    log-bin = mysql-bin
    report_host = 10.0.1.245 # Use the VM's specific IP
    

Restart the service:
    
    
    sudo systemctl restart mysql
    

Then connect to the DB:
    
    
    sudo mysql
    

and set root password:
    
    
    CREATE USER 'root'@'%' IDENTIFIED WITH 'caching_sha2_password' BY 'your_new_secure_password';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    

## InnoDB cluster initialization and verification

### Create cluster using MySQL Shell

On **VM 1 ONLY** , use MySQL Shell to initialize the cluster:
    
    
    mysqlsh --uri root@localhost
    # Inside MySQL Shell:
    \js
    dba.configureInstance('root@VM1_IP')
    var cluster = dba.createCluster('mysql-ha-cluster')
    cluster.addInstance('root@VM2_IP')
    cluster.addInstance('root@VM3_IP')
    cluster.status()
    

### Bootstrap MySQL Router

On all three VMs, bootstrap the router to detect the new cluster:
    
    
    sudo mysqlrouter --bootstrap root@VM1_IP --user=mysqlrouter
    sudo systemctl restart mysqlrouter
    sudo systemctl enable mysqlrouter
    

### Verify balancing and connections

Run these commands from any node to ensure that the router is correctly distributing traffic.

  1. **Verify Write Routing (Active Primary)** : Query port 6446 (Classic RW). It should strictly return the hostname of the current Primary.
         
         mysql -u root -pyour_new_secure_password -h 127.0.0.1 -P 6446 -e "SELECT @@hostname;"
         

  2. **Verify Read Balancing (Round-Robin)** : Query port 6447 (Classic RO) multiple times. It should cycle through the hostnames of all available nodes in the cluster.
         
         for i in {1..4}; do mysql -u root -pyour_new_secure_password -h 127.0.0.1 -P 6447 -e "SELECT @@hostname;"; done
         

  3. **Check Connection Topology** : Use MySQL Shell to confirm all members are `ONLINE` and correctly balanced.
         
         mysqlsh --uri root@localhost --cluster
         
         # inside the shell
         > cluster.status()
         




## Global Load Balancer setup

Provide a single, stable Virtual IP (VIP) for your applications using the GDC Global L4 Load Balancer. Follow [Configure internal global load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service#create-ilb-global) to setup the internal global L4 load balancer and setup your VMs to be the target of it: [Setup VMs as load balancer target](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service#select-vm).

## Automated failover verification

This test confirms that the cluster elects a new leader and the router redirects traffic without manual intervention.

### Simulate primary failure

Identify the current Primary (e.g., Node 1) and stop the MySQL service:
    
    
    sudo systemctl stop mysql
    

### Verify election and routing shift

Wait 10-20 seconds for the consensus protocol to elect a new leader.

  1. **Check Cluster Status** : From VM 2 or 3, verify a new Primary has been elected.
         
         mysqlsh --uri root@localhost --cluster
         
         # inside the shell
         > cluster.status()
         

Confirm one of the remaining nodes is marked as `PRIMARY` and the failed node is marked `UNREACHABLE` or `MISSING`.

  2. **Verify Write Routing** : Test the RW port (6446) again. It should now return the hostname of the new Primary.
         
         mysql -u root -p -h 127.0.0.1 -P 6446 -e "SELECT @@hostname;"
         

  3. **Test Global VIP Connectivity** : From an application server, query the Global VIP.
         
         mysql -u root -p -h ${LB_IP} -P 3306 -e "SELECT @@hostname;"
         




### Recover and verify rejoining

Start the MySQL service on the failed node and verify it rejoins as a secondary replica.
    
    
    sudo systemctl start mysql
    mysqlsh --uri root@localhost --cluster -e "cluster.status()"
    

Confirm all three nodes return the `ONLINE` status.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
