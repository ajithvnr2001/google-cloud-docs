---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/postgres-db-implementation/
title: PostgreSQL database reference implementation on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:40:50.973261+00:00
---

# PostgreSQL database reference implementation on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/postgres-db-implementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  PostgreSQL database reference implementation on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides a comprehensive walkthrough for deploying a highly available PostgreSQL stack across three zones in a Google Distributed Cloud (GDC) air-gapped environment. You will learn how to prepare the necessary software artifacts, bootstrap the target VMs, and use [Autobase](https://autobase.tech/) to automate the entire provisioning process. Throughout this guide, [Patroni](https://patroni.readthedocs.io/en/latest/index.html) is used as the primary management layer to orchestrate the PostgreSQL lifecycle and handle automatic failovers.

## Architecture

The architecture consists of a three VM environment distributed across three availability zones.

![Three VM architecture that runs a colocated stack of services.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/postgre-diagram.png)

Every VM is identical and runs a colocated stack of services:

  * PostgreSQL 17: The core relational database engine.
  * Patroni: The High Availability manager. It handles the lifecycle of the PostgreSQL process and performs automatic failovers. It exposes an HTTPS REST API on port `8008` (endpoint `/primary`) used by the load balancer to identify the current leader.
  * etcd: The Distributed Configuration Store (DCS). It provides the consensus layer for leader election and stores Patroni's configuration.
  * PgBouncer: A connection pooler that sits in front of PostgreSQL to stabilize connection overhead. It provides the recommended entry point for application traffic on port `6432`.



The stack also includes a GDC air-gapped Global L4 Load Balancer, which is a platform-managed service providing a stable Virtual IP (VIP). Applications connect to the stable VIP on port `6432`, which the load balancer routes to PgBouncer on the current leader VM. PgBouncer then proxies the request to the local PostgreSQL instance. To manage traffic flow, the load balancer continuously polls the Patroni HTTPS endpoints as a health check.

The health check on the leader VM returns `HTTP 200 OK` to signal the VM is ready for traffic, while the health checks on the replica VMs return `HTTP 503 Service Unavailable` to signal the load balancer to bypass them. If the leader fails, a new one is elected and its Patroni instance begins returning `HTTP 200 OK`, causing the load balancer to automatically redirect traffic to the new VM's PgBouncer port.

To ensure high availability and prevent data loss, the stack relies on the concept of a quorum. With 3 VMs, the system requires a majority of at least two members to be healthy and in communication to elect a leader and remain operational. This majority-based consensus, managed by etcd and Patroni, allows the stack to automatically tolerate the total failure of any single VM or zone.

## Performance considerations

When planning your deployment, consider the following concrete factors to optimize for performance and reliability:

  * Hardware Sizing: While requirements vary by workload, use these standard profiles as a starting point for each VM: 
    * Development/Proof-of-Concept: 2 vCPU, 8GB RAM (Minimum for stable operation).
    * Small Production: 4 vCPU, 16GB RAM. Suitable for internal tools with moderate concurrency.
    * Standard Production: 8 vCPU, 32GB RAM. The recommended baseline for mission-critical applications.
    * High-Throughput: 16+ vCPU, 64GB+ RAM. For workloads requiring extensive data caching in memory (PostgreSQL shared buffers).
  * Storage Performance: High-performance storage is vital. SSD disks are highly recommended for etcd stability. etcd is extremely sensitive to disk write latency; official [etcd hardware guidelines](https://etcd.io/docs/v3.5/op-guide/hardware/) recommend a p99 disk WAL fdatasync latency of < 10ms.
  * Network Latency: The latency between VMs directly impacts replication performance: 
    * etcd Quorum: Average Round-Trip Time (RTT) should be < 50ms (ideally < 10ms) to prevent election timeouts and cluster instability.
    * Synchronous Replication: If configured, every write transaction must wait for a replica's acknowledgment. Inter-zone latency in GDC air-gapped is typically < 1ms, which is excellent for keeping write overhead minimal (typically 10-30%).
  * The Role of PgBouncer: PostgreSQL creates a new OS process for every connection, which consumes ~10MB of RAM and incurs CPU context-switching costs. PgBouncer reduces this overhead by maintaining a pool of persistent connections, allowing the database to handle thousands of application connections with significantly fewer backend processes.
  * Sidecar Components: Patroni and etcd are lightweight but require consistent CPU availability. In high-load scenarios, ensure the VMs are not oversubscribed at the hypervisor level to avoid "stealing" CPU cycles required for heartbeats and leader maintenance.
  * Kernel Tuning: The Autobase automation automatically applies optimizations beneficial for PostgreSQL, such as configuring [sysctl](https://github.com/vitabaks/autobase/tree/master/automation/roles/sysctl) parameters (e.g., `vm.swappiness`, `net.core.somaxconn`) and [disabling Transparent Huge Pages](https://github.com/vitabaks/autobase/tree/master/automation/roles/transparent_huge_pages) (THP). These changes reduce memory management overhead and improve network throughput for high-traffic database instances.



## Before you begin

Before starting the deployment, you must ensure that your environment meets the following requirements.

### Review VM requirements

For the purpose of this tutorial, you must create three VMs in your GDC air-gapped project. You will need to take into account the following points and requirements for the VMs:

  * Zone distribution: To make this deployment truly resilient to zone failure, you should distribute the VMs across three different availability zones. However, the deployment remains identical if the VMs are located in two zones or even a single zone. What matters most is that all VMs can communicate with each other over the network with their internal IP addresses.
  * Operating System: This tutorial assumes you are using Ubuntu 22.04 images. Further steps in this guide might differ if you use a different distribution.
  * Resources: You should provision at least 2 CPUs and 8GB memory per VM for this tutorial. In production, you must provision resources appropriate for your specific workloads (See Performance considerations).
  * Network IPs: You should take note of both the internal and external IP addresses for each VM. In this guide, you use external IPs for Ansible control because you are running commands from an external workstation. Internal IPs are used for inter-service communication and binding. If you provisioned a bootstrapper VM inside the network, you would only need the internal IPs.
  * Access: Passwordless sudo access for the deployment user is required because the Ansible automation needs to perform administrative tasks (installing packages, modifying system configs) without being blocked by password prompts.
  * SSH: Key-based authentication must be enabled to allow Ansible to connect to the target VMs securely and non-interactively.



### Prepare local workstation software

To manage the deployment and prepare the air-gapped artifacts, you will need a set of automation and containerization tools installed on your local workstation.

  * Ansible 2.17.0+: The automation engine that executes the deployment playbooks and roles.
  * Docker: Used to pull and package OS dependencies within an environment identical to the target VMs (Ubuntu 22.04).
  * PostgreSQL client (`psql`): Required to run the test queries and verify data replication from your local workstation.
  * The Autobase repository:

    * Clone the repository to access the automation playbooks and roles: <https://github.com/vitabaks/autobase>
    * Checkout a specific release (this guide uses version 2.5.2):

`git checkout 2.5.2`

Further steps in this guide might differ if you use a different distribution.

    * To run the playbooks in this guide, you must install the local `autobase` source code as an Ansible collection so the role prefixes can be resolved:
          
          cd autobase/automation
          ansible-galaxy collection install . --force
          




### Create some environment variables

Throughout this guide, you will use the following environment variables to simplify commands. These variables store critical parameters such as your project ID, the availability zones for your VMs, their hostnames, and the labels used by the load balancer to identify your cluster. Set them in your current shell session with the actual values for your environment (Ensure the zones are space-separated).

Note that even though you can set any names you want for your VMs, this guide uses `postgres-vm-1`, `postgres-vm-2`, and `postgres-vm-3` as arbitrary example names for the cluster nodes:
    
    
    export PROJECT_ID="your-project-id"
    export ZONES="zone1 zone2 zone3"
    export VM1_NAME="postgres-vm-1"
    export VM2_NAME="postgres-vm-2"
    export VM3_NAME="postgres-vm-3"
    export VM_LABEL="app=my-postgres-cluster"
    export CLUSTER_NAME="my-postgres-cluster"
    

## Configure Ansible

Define your VM environment in the `inventory.ini` file using the following template:
    
    
    [master]
    postgres-vm-1 ansible_host=XX.XX.XX.XX hostname=postgres-vm-1 bind_address=XX.XX.XX.XX
    
    [replica]
    postgres-vm-2 ansible_host=XX.XX.XX.XX hostname=postgres-vm-2 bind_address=XX.XX.XX.XX
    postgres-vm-3 ansible_host=XX.XX.XX.XX hostname=postgres-vm-3 bind_address=XX.XX.XX.XX
    
    [postgres_cluster:children]
    master
    replica
    
    [etcd_cluster]
    postgres-vm-1
    postgres-vm-2
    postgres-vm-3
    
    [all:vars]
    ansible_user=...
    ansible_ssh_private_key_file=~/.ssh/...
    postgresql_version=17
    with_haproxy_load_balancing=false
    patroni_superuser_password=...
    etcd_package_repo="file:///tmp/packages/etcd-v3.5.25-linux-amd64.tar.gz"
    installation_method="packages"
    install_postgresql_repo=false
    install_timescale_repo=false
    install_citus_repo=false
    apt_repository=[]
    yum_repository=[]
    install_system_packages=false
    patroni_installation_method=deb
    

Understanding the configuration:

  * `[master]` and `[replica]`: Defines the primary and secondary database VMs. Ensure you use the actual VM names that were set in the `VM1_NAME`, `VM2_NAME`, and `VM3_NAME` environment variables.
  * `[postgres_cluster:children]`: A group that aggregates both the master and replica nodes, allowing Ansible to target the entire database cluster with a single command.
  * `[etcd_cluster]`: Defines the nodes that will participate in the etcd consensus cluster. This includes all three database nodes to ensure high availability.
  * `ansible_host`: (For each VM) The VM's external ingress IP used by Ansible to connect to that VM. Replace `XX.XX.XX.XX` with the actual external IP.
  * `bind_address`: (For each VM) The VM's internal IP address. Replace `XX.XX.XX.XX` with the actual internal IP.
  * `ansible_user`: The remote user that Ansible uses to connect to the target VMs with SSH. Replace `...` with the actual username.
  * `ansible_ssh_private_key_file`: The local path to the private SSH key used for authentication to the target VMs. Replace `~/.ssh/...` with the actual path.
  * `patroni_superuser_password`: The password for the `postgres` user. **Ensure you use a strong, secure password here.**
  * `with_haproxy_load_balancing=false`: Disables local HAProxy since you are using the platform-native L4 load balancer.
  * `etcd_package_repo`: Points to the local path of the etcd binary inside the VM's bootstrap directory.
  * `installation_method="packages"`: Instructs the automation to install components with OS packages rather than compiling from source or using Python pip.
  * `install_..._repo=false` and `_repository=[]`: These overrides prevent Ansible from trying to reach out to the internet to add external repositories or update package lists.
  * `install_system_packages=false`: Prevents the automation from trying to download and install packages that you have already provisioned during the initialization or bootstrap phase.
  * `patroni_installation_method=deb`: Specifically tells the role to use the `.deb` package you installed.



## Initialize the VMs

The database stack requires several OS packages and libraries that may not be included in your base Ubuntu image. Since the VMs are in an air-gapped environment without internet access, they cannot download these dependencies themselves.

To resolve this, follow these steps:

  * Use a Docker container on your local workstation to download all necessary files. The following command uses `apt-rdepends` to recursively identify every shared library and dependency required by the target applications. It configures the official PostgreSQL repository within the container to fetch version 17 artifacts, and then iterates through the dependency list to download individual `.deb` files while filtering out core system libraries (like `libc6` or `hostname`) to avoid version conflicts on the target VMs. Finally, it fetches the standalone etcd binary directly from GitHub.

First, create a directory to hold the packages:
        
        mkdir -p ./packages
        

Then, run the Docker command to download all required packages and the etcd binary:
        
        docker run --rm --platform linux/amd64 -v "$(pwd)/packages:/packages" \
          ubuntu:22.04 bash -c "
          set -e
          apt-get update
          apt-get install -y ca-certificates curl gnupg apt-rdepends
        
          # Add PostgreSQL Repository
          curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
            gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
          echo 'deb http://apt.postgresql.org/pub/repos/apt jammy-pgdg main' > \
            /etc/apt/sources.list.d/pgdg.list
          apt-get update
        
          # Define Application Targets + Explicit dependencies needed for air-gap
          TARGETS='unzip tar pgbouncer patroni netdata postgresql-17 \
            postgresql-client-17 postgresql-contrib-17 \
            postgresql-server-dev-17 postgresql-17-dbgsym \
            python3-psycopg2 python3-click python3-yaml python3-prettytable \
            python3-urllib3 python3-tz python3-pip python3-setuptools \
            python3-cryptography moreutils vim jq acl zstd libjq1 \
            libpython3.10-stdlib libexpat1-dev zlib1g-dev libipc-run-perl \
            libtime-duration-perl libjson-perl libpython3-dev \
            libjs-sphinxdoc python3-wheel'
        
          # Resolve all recursive dependencies
          ALL_DEPS=\$(apt-cache depends --recurse --no-recommends --no-suggests \
            --no-conflicts --no-breaks --no-replaces --no-enhances \$TARGETS | \
            grep '^\w' | sort -u)
        
          cd /packages
          for pkg in \$ALL_DEPS; do
            if apt-cache show \"\$pkg\" > /dev/null 2>&1; then
              # Filter system core to avoid VM conflicts/breaks
              # We exclude core OS libraries (libc, systemd, etc.) because these
              # often cause version conflicts if the VM's patch level differs
              # from the online container.
              FILTER='base-files|debianutils|coreutils|findutils|diffutils|sed'
              FILTER+='|grep|gzip|hostname|ncurses|perl-base|libc6|binutils'
              FILTER+='|linux-libc|libc-bin|libc-dev-bin|systemd|dpkg|init'
              if [[ ! \"\$pkg\" =~ \$FILTER ]]; then
                apt-get download \"\$pkg\" || echo \"Failed \$pkg\"
              fi
            fi
          done
        
          # Download etcd binary
          if [ ! -f etcd-v3.5.25-linux-amd64.tar.gz ]; then
            curl -L https://github.com/etcd-io/etcd/releases/download/v3.5.25/\
        etcd-v3.5.25-linux-amd64.tar.gz -o etcd-v3.5.25-linux-amd64.tar.gz
          fi
        "
        

  * Use Ansible to upload the archive to all three target VMs simultaneously:
        
        ansible all -i inventory.ini -m copy -a "src=packages.tar.gz dest=/tmp/" -b
        

  * Clear any existing package data on the VMs and extract the new tar file:
        
        ansible all -i inventory.ini -m shell -a "rm -rf /tmp/packages && \
          mkdir -p /tmp/packages && tar -xzf /tmp/packages.tar.gz -C /tmp/packages" -b
        

  * Perform a non-interactive installation of all downloaded `.deb` packages. To avoid issues with specific pre-dependencies in an air-gapped environment, use the `--force-depends` flag followed by `apt-get install -fy` to resolve the dependency tree locally:
        
        ansible all -i inventory.ini -m shell -a "DEBIAN_FRONTEND=noninteractive \
          NEEDRESTART_MODE=a dpkg -i --force-depends /tmp/packages/*.deb" -b
        
        ansible all -i inventory.ini -m shell -a "DEBIAN_FRONTEND=noninteractive \
          NEEDRESTART_MODE=a apt-get install -fy" -b
        

  * Immediately stop all services to prevent them from starting with default, unconfigured states before the automation is ready:
        
        ansible all -i inventory.ini -m shell -a \
          "systemctl stop patroni etcd pgbouncer postgresql || true" -b
        

  * Finally, remove the default PostgreSQL clusters and any existing etcd data to allow for a clean initialization:
        
        ansible all -i inventory.ini -m shell -a \
          "pg_dropcluster 17 main --stop || true" -b
        ansible all -i inventory.ini -m shell -a \
          "rm -rf /var/lib/postgresql/17/main/* /var/lib/etcd/default.etcd/*" -b
        




## Provision database infrastructure

With the VMs bootstrapped and the inventory configured, you can now use the Autobase automation playbooks with Ansible to deploy the highly available PostgreSQL stack.

First, run the pre-flight checks to ensure the environment is ready:
    
    
    ansible-playbook vitabaks.autobase.deploy_pgcluster -i inventory.ini \
      --tags pre_checks
    

If the checks pass, proceed with the full deployment:
    
    
    ansible-playbook vitabaks.autobase.deploy_pgcluster -i inventory.ini
    

Expected output: The playbook should complete with a successful "`PLAY RECAP`" showing all target VMs as reached and updated:
    
    
    PLAY RECAP ********************************************************************
    localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=254  rescued=0    ignored=0
    postgres-vm-1              : ok=160  changed=53   unreachable=0    failed=0    skipped=514  rescued=0    ignored=2
    postgres-vm-2              : ok=116  changed=40   unreachable=0    failed=0    skipped=505  rescued=0    ignored=2
    postgres-vm-3              : ok=116  changed=40   unreachable=0    failed=0    skipped=505  rescued=0    ignored=2
    

## Verify the deployment

After the deployment completes, you should perform several checks to ensure all components are functioning correctly.

### Check HA status

Check the status of the high availability manager to see the roles assigned to each VM:
    
    
    ansible master -i inventory.ini -m shell -a "patronictl list" -b
    

Example output:
    
    
    + Cluster: postgres-cluster (7607933704953386478) ---+----+-------------+-----+------------+-----+
    | Member        | Host         | Role    | State     | TL | Receive LSN | Lag | Replay LSN | Lag |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    | postgres-vm-1 | 10.253.1.254 | Leader  | running   |  1 |             |     |            |     |
    | postgres-vm-2 | 10.253.1.253 | Replica | streaming |  1 |   0/6000000 |   0 |  0/6000000 |   0 |
    | postgres-vm-3 | 10.253.1.252 | Replica | streaming |  1 |   0/6000000 |   0 |  0/6000000 |   0 |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    

### Verify health check endpoints

Test that Patroni correctly identifies the leader and replicas using its REST API. The leader VM's health check should return `200 OK`, while replica VMs' health checks should return `503 Service Unavailable`:
    
    
    ansible ${VM1_NAME} -i inventory.ini -m shell -a \
      "curl -ks -o /dev/null -w '%{http_code}' https://localhost:8008/primary" -b
    
    ansible ${VM2_NAME} -i inventory.ini -m shell -a \
      "curl -ks -o /dev/null -w '%{http_code}' https://localhost:8008/primary" -b
    
    ansible ${VM3_NAME} -i inventory.ini -m shell -a \
      "curl -ks -o /dev/null -w '%{http_code}' https://localhost:8008/primary" -b
    

### Verify individual VM health

Check the readiness of all PostgreSQL instances:
    
    
    ansible postgres_cluster -i inventory.ini -m shell -a "pg_isready -p 5432" -b
    

Example output:
    
    
    postgres-vm-1 | CHANGED | rc=0 >>
    /var/run/postgresql:5432 - accepting connections
    
    postgres-vm-2 | CHANGED | rc=0 >>
    /var/run/postgresql:5432 - accepting connections
    
    postgres-vm-3 | CHANGED | rc=0 >>
    /var/run/postgresql:5432 - accepting connections
    

### Verify etcd health

Verify the health of the consensus layer across all VMs using localhost as the endpoint:
    
    
    ansible all -i inventory.ini -m shell -a "ETCDCTL_API=3 etcdctl \
      --endpoints=https://localhost:2379 \
      --cacert=/etc/etcd/tls/ca.crt \
      --cert=/etc/etcd/tls/server.crt \
      --key=/etc/etcd/tls/server.key \
      endpoint health" -b
    

Example output:
    
    
    postgres-vm-1 | CHANGED | rc=0 >>
    https://localhost:2379 is healthy: successfully committed proposal: \
    took = 28.78311ms
    
    postgres-vm-2 | CHANGED | rc=0 >>
    https://localhost:2379 is healthy: successfully committed proposal: \
    took = 33.081265ms
    
    postgres-vm-3 | CHANGED | rc=0 >>
    https://localhost:2379 is healthy: successfully committed proposal: \
    took = 24.414291ms
    

## Configure the global load balancer

To provide a stable virtual IP (VIP) for the database stack, configure the platform-native Global L4 Load Balancer using the `gdcloud` CLI.

  * Prerequisites:

    * Ensure you have the `load-balancer-admin` role in your project.
    * Apply a label to your VMs so the load balancer can correctly target the instances it needs to serve (Replace the `kubeconfig` parameter values with the corresponding management API `kubeconfig` files for each zone):
          
          kubectl --kubeconfig=ZONE_A_MANAGEMENT_API label VirtualMachine \
            -n ${PROJECT_ID} \
            ${VM1_NAME} \
            ${VM_LABEL}
          
          kubectl --kubeconfig=ZONE_B_MANAGEMENT_API label VirtualMachine \
            -n ${PROJECT_ID} \
            ${VM2_NAME} \
            ${VM_LABEL}
          
          kubectl --kubeconfig=ZONE_C_MANAGEMENT_API label VirtualMachine \
            -n ${PROJECT_ID} \
            ${VM3_NAME} \
            ${VM_LABEL}
          

  * Define the load balancing access level. Set `EXTERNAL` if you need to connect from outside the project's network, or `INTERNAL` if access is only required from within the VPC. For this tutorial, we will use an external setup:
        
        export LB_SCHEME=EXTERNAL
        

  * Create a health check. The load balancer uses Patroni's REST API to identify the leader:
        
        gdcloud compute health-checks create https ${CLUSTER_NAME}-hc \
          --project=${PROJECT_ID} \
          --port=8008 \
          --request-path="/primary" \
          --check-interval=10 \
          --timeout=5 \
          --healthy-threshold=2 \
          --unhealthy-threshold=3 \
          --global
        

  * Create a separate zonal backend for each zone where your VMs are located:
        
        for zone in $(echo $ZONES); do
          gdcloud compute backends create ${CLUSTER_NAME}-backend-${zone} \
            --project=${PROJECT_ID} \
            --zone=${zone} \
            --labels="${VM_LABEL}"
        done
        

  * Create a global backend service:
        
        gdcloud compute backend-services create ${CLUSTER_NAME}-bes \
          --project=${PROJECT_ID} \
          --health-check="${CLUSTER_NAME}-hc" \
          --global
        

  * Add your zonal backends to the global service:
        
        for zone in $(echo $ZONES); do
          gdcloud compute backend-services add-backend ${CLUSTER_NAME}-bes \
            --project=${PROJECT_ID} \
            --backend=${CLUSTER_NAME}-backend-${zone} \
            --backend-zone=${zone} \
            --global
        done
        

  * Create a global forwarding rule (the VIP). This rule exposes the database on Port `6432`:
        
        gdcloud compute forwarding-rules create ${CLUSTER_NAME}-fr \
          --project=${PROJECT_ID} \
          --load-balancing-scheme=${LB_SCHEME} \
          --backend-service=${CLUSTER_NAME}-bes \
          --ip-protocol-port="TCP:6432" \
          --global
        

  * Retrieve the VIP address:
        
        LB_IP=$(gdcloud compute forwarding-rules describe ${CLUSTER_NAME}-fr \
          --project=${PROJECT_ID} \
          --load-balancing-scheme=${LB_SCHEME} \
          --global \
          --format=json \
          | jq -r '.metadata.annotations["networking.gke.io/forwardingRuleCIDR"]'  \
          | cut -d '/' -f 1)
        
        echo "The load balancer IP is: ${LB_IP}"
        

  * Create a `ProjectNetworkPolicy` (PNP) to allow ingress traffic to the PgBouncer port (Replace the `kubeconfig` parameter value with the corresponding your environment's global API `kubeconfig` file).
        
        kubectl --kubeconfig=GLOBAL_API_KUBECONFIG apply -f - <<EOF
        apiVersion: networking.global.gdc.goog/v1
        kind: ProjectNetworkPolicy
        metadata:
          name: allow-pgbouncer
          namespace: ${PROJECT_ID}
        spec:
          ingress:
          - ports:
            - port: 6432
              protocol: TCP
          policyType: Ingress
          subject:
            subjectType: UserWorkload
        EOF
        




## Verify data replication

To confirm that the high availability stack is working as expected, you can create sample data on the leader and verify its presence on the replicas.

### Insert sample data

The automation generates a random password for the `postgres` user during the first deployment if one is not provided in `inventory.ini`. You can retrieve it from any VM:
    
    
    export PG_PASSWORD=$(ansible master -i inventory.ini -m shell -a \
      "grep -A10 'authentication:' /etc/patroni/patroni.yml | \
      grep -A3 'superuser' | grep 'password:' | awk '{ print \$2 }'" -b | \
      tail -n 1)
    echo $PG_PASSWORD
    

**Note:** We are using the `postgres` superuser here for convenience during testing. Patroni documentation strongly recommends that applications shouldn't use superusers for connection, as it can potentially use the entire connection pool, including connections reserved for superusers. For production best practices, refer to the Patroni documentation: [Applications shouldn't use superusers](https://patroni.readthedocs.io/en/latest/README.html#applications-should-not-use-superusers).

Connect to the load balancer VIP on the PgBouncer port (`6432`) and create a sample table:
    
    
    PGPASSWORD="${PG_PASSWORD}" psql -h ${LB_IP} -p 6432 -U postgres -c "
      CREATE TABLE employees (first_name TEXT, last_name TEXT);
      INSERT INTO employees (first_name, last_name) VALUES ('John', 'Doe');
    "
    

Expected Output:
    
    
    INSERT 0 1
    

### Verify replication state

Execute a `SELECT` query on all VMs to ensure data has replicated from the leader to all replicas:
    
    
    ansible postgres_cluster -i inventory.ini -m shell -a "psql -U postgres -c \
      'SELECT * FROM employees;'" -b
    

Example output:
    
    
    postgres-vm-1 | CHANGED | rc=0 >>
     first_name | last_name
    ------------+-----------
     John       | Doe
    (1 row)
    
    postgres-vm-2 | CHANGED | rc=0 >>
     first_name | last_name
    ------------+-----------
     John       | Doe
    (1 row)
    
    postgres-vm-3 | CHANGED | rc=0 >>
     first_name | last_name
    ------------+-----------
     John       | Doe
    (1 row)
    

## Test manual switchover

A manual switchover lets you gracefully move the leader role to a specific candidate VM. This is typically done for planned maintenance, software upgrades, or to balance resource utilization across zones.

### Identify the current leader

Verify the current role and status of the VMs:
    
    
    ansible master -i inventory.ini -m shell -a "patronictl list" -b
    

Example output:
    
    
    + Cluster: postgres-cluster (7607933704953386478) ---+----+-------------+-----+------------+-----+
    | Member        | Host         | Role    | State     | TL | Receive LSN | Lag | Replay LSN | Lag |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    | postgres-vm-1 | 10.253.1.254 | Leader  | running   |  1 |             |     |            |     |
    | postgres-vm-2 | 10.253.1.253 | Replica | streaming |  1 |   0/6000000 |   0 |  0/6000000 |   0 |
    | postgres-vm-3 | 10.253.1.252 | Replica | streaming |  1 |   0/6000000 |   0 |  0/6000000 |   0 |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    

### Perform switchover

Trigger a switchover from the current leader to another VM (in this case respectively from `postgres-vm-1` to `postgres-vm-2`). The command uses `--force` to skip manual confirmation prompts:
    
    
    ansible master -i inventory.ini -m shell -a "patronictl switchover \
      --leader ${VM1_NAME} --candidate ${VM2_NAME} --force" -b
    

Example output:
    
    
    Successfully switched over to "postgres-vm-2"
    + Cluster: postgres-cluster (7607933704953386478) -+----+-------------+-----+------------+-----+
    | Member        | Host         | Role    | State   | TL | Receive LSN | Lag | Replay LSN | Lag |
    +---------------+--------------+---------+---------+----+-------------+-----+------------+-----+
    | postgres-vm-1 | 10.253.1.254 | Replica | stopped |    |     unknown |     |    unknown |     |
    | postgres-vm-2 | 10.253.1.253 | Leader  | running |  1 |             |     |            |     |
    | postgres-vm-3 | 10.253.1.252 | Replica | running |  1 |   0/70000A0 |   0 |  0/70000A0 |   0 |
    +---------------+--------------+---------+---------+----+-------------+-----+------------+-----+
    

### Verify health check shift

After the switchover, verify that the health check status has shifted to the new leader:
    
    
    ansible ${VM1_NAME} -i inventory.ini -m shell -a \
      "curl -ks -o /dev/null -w '%{http_code}' https://localhost:8008/primary" -b
    
    ansible ${VM2_NAME} -i inventory.ini -m shell -a \
      "curl -ks -o /dev/null -w '%{http_code}' https://localhost:8008/primary" -b
    

The old leader (`postgres-vm-1`) should return `503`, while the new leader (`postgres-vm-2`) should return `200`.

## Test automatic failover

Unlike a manual switchover, an automatic failover occurs when the leader VM becomes unavailable. This test confirms that Patroni elects a new leader and the load balancer redirects traffic without manual intervention. Assume that `postgres-vm-2` is the current leader following the manual switchover performed previously.

### Identify the current leader

Verify the current role and status of the VMs:
    
    
    ansible master -i inventory.ini -m shell -a "patronictl list" -b
    

Example output:
    
    
    + Cluster: postgres-cluster (7607933704953386478) ---+----+-------------+-----+------------+-----+
    | Member        | Host         | Role    | State     | TL | Receive LSN | Lag | Replay LSN | Lag |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    | postgres-vm-1 | 10.253.1.254 | Replica | streaming |  2 |   0/8000000 |   0 |  0/8000000 |   0 |
    | postgres-vm-2 | 10.253.1.253 | Leader  | running   |  2 |             |     |            |     |
    | postgres-vm-3 | 10.253.1.252 | Replica | streaming |  2 |   0/8000000 |   0 |  0/8000000 |   0 |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    

### Simulate a VM failure

Stop the `patroni` service on the leader VM to simulate a crash or hard failure:
    
    
    ansible master -i inventory.ini -m shell -a "systemctl stop patroni" -b
    

### Observe the new election

Wait 10-20 seconds and check the status from another VM to see the promotion of a new leader:
    
    
    ansible replica -i inventory.ini -m shell -a "patronictl list" -b
    

Example output:
    
    
    postgres-vm-3 | CHANGED | rc=0 >>
    + Cluster: postgres-cluster (7607933704953386478) ---+----+-------------+-----+------------+-----+
    | Member        | Host         | Role    | State     | TL | Receive LSN | Lag | Replay LSN | Lag |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    | postgres-vm-1 | 10.253.1.254 | Leader  | running   |  3 |             |     |            |     |
    | postgres-vm-2 | 10.253.1.253 | Replica | stopped   |    |     unknown |     |    unknown |     |
    | postgres-vm-3 | 10.253.1.252 | Replica | streaming |  3 |   0/90003F8 |   0 |  0/90003F8 |   0 |
    +---------------+--------------+---------+-----------+----+-------------+-----+------------+-----+
    

You should see that one of the other VMs (`postgres-vm-1` or `postgres-vm-3`) has become the leader and the old leader (`postgres-vm-2`) is marked as stopped.

### Verify the health check shift

Confirm that the load balancer health checks would now correctly identify the newly elected leader:
    
    
    ansible ${VM1_NAME} -i inventory.ini -m shell -a \
      "curl -ks -o /dev/null -w '%{http_code}' https://localhost:8008/primary" -b
    

The new leader should return `200 OK`.

### Recover the failed VM

Start the `patroni` service back up on the original VM to let it rejoin the stack as a replica and catch up with any missed data:
    
    
    ansible ${VM2_NAME} -i inventory.ini -m shell -a \
      "systemctl start patroni" -b
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
