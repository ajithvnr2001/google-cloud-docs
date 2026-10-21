---
url: https://docs.cloud.google.com/managed-lustre/docs/performance-testing/
title: Performance testing with Compute Engine clients \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:18:44.898743+00:00
---

# Performance testing with Compute Engine clients  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/performance-testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Performance testing with Compute Engine clients Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to test the performance of a Google Cloud Managed Lustre instance using Compute Engine clients. It provides instructions for measuring single-client performance using `fio` and aggregate multi-client performance using the IOR benchmark tool.

## Measuring single-client performance

To test read and write performance from a single Compute Engine client, use the `fio` ([Flexible I/O tester](https://fio.readthedocs.io/en/latest/)) command line tool.

  1. Install fio:

###  Rocky 8 
         
         sudo dnf install fio -y
         

###  Ubuntu 20.04 and 22.04 
         
         sudo apt update
         sudo install fio
         

  2. Run the following command:
         
         fio --ioengine=libaio --filesize=32G --ramp_time=2s \
         --runtime=5m --numjobs=16 --direct=1 --verify=0 --randrepeat=0 \
         --group_reporting --directory=/lustre --buffer_compress_percentage=50 \
         --name=read --blocksize=1m --iodepth=64 --readwrite=read
         




The test takes approximately 5 minutes to complete. When finished, the results are displayed. Depending on your configuration, you can expect throughput up to your VM's maximum network speed, and thousands of IOPS per TiB.

## Measuring multi-client performance

To test Managed Lustre's read and write performance from multiple Compute Engine clients, use the [IOR benchmark tool](http://ior.readthedocs.io/). The following instructions show you how to automate your client setup and use IOR to test aggregate I/O from multiple client machines. IOR uses [MPI](https://www.mpi-forum.org/docs/) \- a message-passing protocol - to enable the multiple client machines to coordinate with each other.

Before you begin, ensure that your network's `mtu` value is [set to `8896`](https://docs.cloud.google.com/managed-lustre/docs/performance#vpc_network_maximum_transmission_unit_mtu).

### Set environment variables and generate an SSH key

Before deploying your cluster, generate an SSH key on your local machine. This key will be distributed to your client machines during creation to enable passwordless communication for MPI.
    
    
    export SSH_USER="lustre-user"
    export CLIENT_PREFIX="lustre-client"
    
    # Generate an SSH key for the specified user
    ssh-keygen -t rsa -b 4096 -C "${SSH_USER}" -N '' -f "./id_rsa"
    chmod 600 "./id_rsa"
    
    # Create a metadata file formatted for Google Cloud
    echo "${SSH_USER}:$(cat "./id_rsa.pub") ${SSH_USER}" > "./keys.txt"
    

### Create the startup script

Save the following content into a file named `install-ior.sh` on your local machine. This script detects the operating system, waits for boot locks to release, safely installs the Lustre client and dependencies, compiles a stable release of IOR, and mounts the Managed Lustre file system.

Replace LUSTRE_IP with your Managed Lustre instance's IP address, and FS_NAME with your file system name.
    
    
    #!/bin/bash
    source /etc/os-release
    
    if [[ "$ID" == "ubuntu" ]]; then
        # Ubuntu
        # Wait for apt lock
        while fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1; do sleep 5; done
    
        # Configure Artifact Registry repo for Ubuntu
        curl -fsSL https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/us-apt-pkg-dev.gpg
    
        if [[ "$VERSION_ID" == "22.04" ]]; then
            REPO_NAME="lustre-client-ubuntu-jammy"
        elif [[ "$VERSION_ID" == "24.04" ]]; then
            REPO_NAME="lustre-client-ubuntu-noble"
        fi
    
        echo "deb [signed-by=/usr/share/keyrings/us-apt-pkg-dev.gpg] https://us-apt.pkg.dev/projects/lustre-client-binaries $REPO_NAME main" | sudo tee /etc/apt/sources.list.d/lustre-client.list
    
        sudo apt-get update
        while ! sudo apt-get install -y lustre-client-modules-$(uname -r) lustre-client-utils openmpi-bin libopenmpi-dev make gcc g++ wget git automake autoconf libaio-dev; do
            sleep 5
        done
        sudo modprobe lustre
    else
        # Red Hat / Rocky Linux
        while systemctl is-active --quiet dnf-makecache.service; do sleep 5; done
    
        if [[ "$ID" == "rocky" && "$VERSION_ID" == 8* ]]; then
            REPO="lustre-client-rocky-8"
        elif [[ "$ID" == "rocky" && "$VERSION_ID" == 9* ]]; then
            REPO="lustre-client-rocky-9"
        elif [[ "$ID" == "rhel" && "$VERSION_ID" == 9* ]]; then
            REPO="lustre-client-rocky-9"
        fi
    
        gcloud beta artifacts print-settings yum --repository=$REPO --location=us --project=lustre-client-binaries | sudo bash
    
        while ! sudo dnf -y --enablerepo=$REPO install kmod-lustre-client lustre-client; do sleep 5; done
        sudo modprobe lustre
    
        while ! sudo dnf install -y openmpi openmpi-devel make gcc gcc-c++ wget git automake autoconf libaio-devel; do sleep 5; done
    
        export PATH=$PATH:/usr/lib64/openmpi/bin
    fi
    
    # Build IOR from source
    echo "Cloning repo: https://github.com/hpc/ior.git and building IOR"
    pushd /tmp
    git clone -b 4.0.0 https://github.com/hpc/ior
    cd ior
    ./bootstrap
    ./configure --disable-dependency-tracking --with-aio
    make clean
    make -j"$(nproc)"
    sudo make install
    popd
    echo "Finished building IOR"
    
    # Mount the Managed Lustre file system
    mkdir -p /lustre
    
    if ! grep -q "/lustre" /etc/fstab; then
        echo "LUSTRE_IP@tcp:/FS_NAME /lustre lustre defaults,_netdev 0 0" >> /etc/fstab
    fi
    
    mount -a
    

### Deploy the client machines

Run the following command to bulk create the Compute Engine client machines.
    
    
    gcloud compute instances bulk create \
      --name-pattern="${CLIENT_PREFIX}-####" \
      --zone="ZONE" \
      --machine-type="MACHINE_TYPE" \
      --scopes="https://www.googleapis.com/auth/cloud-platform" \
      --network-interface=subnet=SUBNET,nic-type=GVNIC \
      --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
      --metadata-from-file=ssh-keys=./keys.txt,startup-script=install-ior.sh \
      --create-disk=auto-delete=yes,boot=yes,\
    image-family=IMAGE_FAMILY,\
    image-project=IMAGE_PROJECT,\
    mode=rw,size=100,type=DISK_TYPE \
      --count NUM_NODES
    

  * Replace ZONE and SUBNET with your specific deployment values.

  * Choose a MACHINE_TYPE. The overall performance of your benchmark depends on the client machine types. See [Performance considerations](https://docs.cloud.google.com/managed-lustre/docs/performance#compute-machine-types) for information on choosing machine types to obtain the best throughput.

  * If your machine type doesn't support TIER_1 networking, delete the `--network-performance-configs` line from the command.

  * Set the DISK_TYPE to one of `hyperdisk-balanced` (for a machine type with a `4` in its generation name, such as `c4a` or `n4`) or `pd-balanced`.

  * Specify the IMAGE_FAMILY and IMAGE_PROJECT. Supported values are:

OS | Image family (x86) | Image family (ARM) | Image project  
---|---|---|---  
HPC Rocky Linux 8 | `hpc-rocky-linux-8` | Not supported | `cloud-hpc-image-public`  
Rocky Linux 9 | `rocky-linux-9` | `rocky-linux-9-arm64` | `rocky-linux-cloud`  
RHEL 9 | `rhel-9` | `rhel-9-arm64` | `rhel-cloud`  
Ubuntu 22.04 LTS | `ubuntu-2204-lts` | `ubuntu-2204-lts-arm64` | `ubuntu-os-cloud`  
Ubuntu 24.04 LTS | Not supported | `ubuntu-2404-lts-arm64` | `ubuntu-os-cloud`  
  * Specify the NUM_NODES. To saturate your file system, your cluster's aggregate network capacity should exceed your file system's provisioned throughput by ~20%.

For machines with Tier 1 networking enabled, a single machine can push between 25 Gbps–200 Gbps (~3,000–25,000 MBps), depending on the VM family and the CPU count. For standard instances, egress is typically capped around 2 Gbps per vCPU.

For example, if your Managed Lustre instance capacity yields 100,000 MBps of theoretical throughput, you need an aggregate client egress of 120,000 MBps (`100,000 * 1.2`) to saturate it:

    * **With standard instances:** If each client machine has a published egress of 2,000 MBps, you should provision at least 60 clients (`120,000 / 2,000`).
    * **With Tier 1 networking:** If each client machine has a published egress of 10,000 MBps (~80 Gbps), you should provision at least 12 clients (`120,000 / 10,000`).



### Copy keys and files

While you wait for the client machines to finish their startup scripts, run the following commands locally to automatically configure all nodes for inter-node communication.

  1. Save the client machines' private IP addresses for the MPI host file, and the public IP addresses for SSH and SCP access to the client machines:
         
         gcloud compute instances list --filter="name ~ '^${CLIENT_PREFIX}*'" --format="csv[no-heading](INTERNAL_IP)" > hosts.txt
         gcloud compute instances list --filter="name ~ '^${CLIENT_PREFIX}*'" --format="csv[no-heading](EXTERNAL_IP)" > external_ips.txt
         

  2. Copy the private key to all clients. This allows the worker nodes to communicate with each other securely during the benchmark:
         
         while IFS= read -r IP || [[ -n "$IP" ]]
         do
           [[ -z "$IP" ]] && continue
           echo "Preparing and copying to ${SSH_USER}@${IP}..."
           # Ensure the .ssh directory exists
           ssh -i ./id_rsa -o StrictHostKeyChecking=no "${SSH_USER}@${IP}" "mkdir -p ~/.ssh && chmod 700 ~/.ssh"
           # Copy the file
           scp -i ./id_rsa -o StrictHostKeyChecking=no ./id_rsa "${SSH_USER}@${IP}:~/.ssh/id_rsa"
         done < "./external_ips.txt"
         

  3. Designate the head node and copy the host file to it. This will be the machine from which you run the benchmark.
         
         export HEAD_NODE=$(head -n 1 ./external_ips.txt)
         scp -i ./id_rsa -o "StrictHostKeyChecking=no" -o UserKnownHostsFile=/dev/null ./hosts.txt ${SSH_USER}@${HEAD_NODE}:~/hostfile
         




### Connect and verify

  1. Connect to your head node:
         
         ssh -i ./id_rsa -o "StrictHostKeyChecking=no" -o UserKnownHostsFile=/dev/null ${SSH_USER}@${HEAD_NODE}
         

  2. Verify that the startup script has finished and the file system is successfully mounted before running the benchmark.

To check the startup script logs:
         
         sudo journalctl -u google-startup-scripts.service -f
         

To verify the file system is mounted:
         
         df -h | grep lustre
         

If the file system is not listed, wait a few more minutes for the background installation script to complete. Once mounted, it will be available at the absolute path `/lustre`.


**Tip:** If you plan to run frequent performance tests, you can speed up future deployments by creating a custom Compute Engine image from one of these configured machines. Wait for the startup script to finish and the keys to be copied, then create a custom image from the machine's boot disk. You can use this custom image to bulk deploy future Compute Engine clusters, without the need for a startup script or copying keys each time. See [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom) for instructions.

### Run the IOR benchmark

  1. **Rocky Linux and RHEL only:** Load the OpenMPI module from the head node.
         
         if [ -f /etc/profile.d/modules.sh ]; then
             source /etc/profile.d/modules.sh
             module load mpi/openmpi-$(arch)
         fi
         

  2. Create a test directory and take ownership:
         
         sudo mkdir -p /lustre/test
         sudo chown -R $USER:$USER /lustre/test
         

  3. Define test variables:
         
         export NUM_NODES="NUM_NODES"
         export PROCESSES_PER_NODE="PROCESSES_PER_NODE"
         export NUM_PROCESSES=$(( NUM_NODES * PROCESSES_PER_NODE ))
         

Where:

     * NUM_NODES: The total number of client machines participating in the test.
     * PROCESSES_PER_NODE: The number of MPI ranks to run on each individual client machine. We recommend that you start by setting this to match the number of physical cores (or half the number of vCPUs) on your client machines. For high-performance machine types, setting this between `8` and `16` typically yields the best network throughput. Setting this too high can cause context-switching overhead and degrade benchmark performance.
  4. Run the command to start the benchmark:

###  Rocky Linux and RHEL 

**Write throughput**

This command writes continuously for 60 seconds to test peak steady-state throughput. The per-task file size is set to an arbitrarily large 50 TiB ceiling to keep tasks writing until the 60-second timer expires.
         
         mpirun \
           --allow-run-as-root \
           --mca plm_rsh_no_tree_spawn 1 \
           --mca opal_set_max_sys_limits 1 \
           --mca plm_rsh_num_concurrent ${NUM_NODES} \
           --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
           --prefix /usr/lib64/openmpi \
           --npernode ${PROCESSES_PER_NODE} \
           --np ${NUM_PROCESSES} \
           --hostfile ~/hostfile \
           /usr/local/bin/ior \
           -a AIO \
           --posix.odirect \
           -F -g -v -w -k \
           -t 4m -b 50t \
           -D 60 \
           -O stoneWallingWearOut=1 \
           -O stoneWallingStatusFile=/lustre/test/ior-easy.stonewall \
           -o /lustre/test/ior_file

**Read throughput**

This phase reads back exactly the amount of data that was successfully written during the 60-second write throughput test. Although the per-task file size (`-b`) is set to 50 TiB to match the write phase's geometry, the `-O stoneWallingWearOut=1` flag instructs IOR to stop reading as soon as it hits the exact data boundary recorded in the stonewall status file.
         
         mpirun \
           --allow-run-as-root \
           --mca plm_rsh_no_tree_spawn 1 \
           --mca opal_set_max_sys_limits 1 \
           --mca plm_rsh_num_concurrent ${NUM_NODES} \
           --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
           --prefix /usr/lib64/openmpi \
           --npernode ${PROCESSES_PER_NODE} \
           --np ${NUM_PROCESSES} \
           --hostfile ~/hostfile \
           /usr/local/bin/ior \
           -a AIO \
           --posix.odirect \
           -F -g -v -r -k \
           -t 4m -b 50t \
           -D 60 \
           -O stoneWallingWearOut=1 \
           -O stoneWallingStatusFile=/lustre/test/ior-easy.stonewall \
           -o /lustre/test/ior_file

**Write IOPS**

This test uses small 4 KiB transfer sizes and 8 GiB per-task file sizes to measure the maximum Input/Output Operations Per Second (IOPS) the file system can handle.
         
         mpirun \
           --allow-run-as-root \
           --mca plm_rsh_no_tree_spawn 1 \
           --mca opal_set_max_sys_limits 1 \
           --mca plm_rsh_num_concurrent ${NUM_NODES} \
           --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
           --prefix /usr/lib64/openmpi \
           --np ${NUM_PROCESSES} \
           --oversubscribe \
           --map-by node \
           --bind-to socket \
           --hostfile ~/hostfile \
           /usr/local/bin/ior \
           -e \
           -t 4k \
           -b 8g \
           -s 1 \
           -a AIO \
           --posix.odirect \
           --aio.max-pending=256 \
           -w \
           -F \
           -z \
           -Q 1 \
           -G 1745405099 \
           -D 45 \
           -O stoneWallingWearOut=1 \
           -o /lustre/test/ior-random

**Read IOPS**

To prevent reading from a sparse file, this test uses two commands: a write to create a solid file using 4 MiB transfer sizes and 8 GiB per-task file sizes, followed by the actual 4 KiB random read IOPS test.

     1. Create the file to read:
            
            mpirun \
              --allow-run-as-root \
              --mca plm_rsh_no_tree_spawn 1 \
              --mca opal_set_max_sys_limits 1 \
              --mca plm_rsh_num_concurrent ${NUM_NODES} \
              --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
              --prefix /usr/lib64/openmpi \
              --npernode ${PROCESSES_PER_NODE} \
              --np ${NUM_PROCESSES} \
              --oversubscribe \
              --map-by node \
              --bind-to socket \
              --hostfile ~/hostfile \
              /usr/local/bin/ior \
              -a AIO \
              --posix.odirect \
              -w \
              -F \
              -k \
              -t 4m \
              -b 8g \
              -s 1 \
              -Q 1 \
              -G 1745405099 \
              -o /lustre/test/ior_rand_read

     2. Run the IOR read test:
            
            mpirun \
              --allow-run-as-root \
              --mca plm_rsh_no_tree_spawn 1 \
              --mca opal_set_max_sys_limits 1 \
              --mca plm_rsh_num_concurrent ${NUM_NODES} \
              --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
              --prefix /usr/lib64/openmpi \
              --oversubscribe \
              --map-by node \
              --bind-to socket \
              --npernode ${PROCESSES_PER_NODE} \
              --np ${NUM_PROCESSES} \
              --hostfile ~/hostfile \
              /usr/local/bin/ior \
              -a AIO \
              --posix.odirect \
              --aio.max-pending 256 \
              -r \
              -F \
              -z \
              -t 4k \
              -b 8g \
              -s 1 \
              -Q 1 \
              -G 1745405099 \
              -D 45 \
              -O stoneWallingWearOut=1 \
              -o /lustre/test/ior_rand_read

###  Ubuntu 

**Write throughput**

This command writes continuously for 60 seconds to test peak steady-state throughput. The per-task file size is set to an arbitrarily large 50 TiB ceiling to keep tasks writing until the 60-second timer expires.
    
    mpirun \
      --allow-run-as-root \
      --mca plm_rsh_no_tree_spawn 1 \
      --mca opal_set_max_sys_limits 1 \
      --mca plm_rsh_num_concurrent ${NUM_NODES} \
      --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
      --npernode ${PROCESSES_PER_NODE} \
      --np ${NUM_PROCESSES} \
      --hostfile ~/hostfile \
      /usr/local/bin/ior \
      -a AIO \
      --posix.odirect \
      -F -g -v -w -k \
      -t 4m -b 50t \
      -D 60 \
      -O stoneWallingWearOut=1 \
      -O stoneWallingStatusFile=/lustre/test/ior-easy.stonewall \
      -o /lustre/test/ior_file

**Read throughput**

This phase reads back exactly the amount of data that was successfully written during the 60-second write throughput test. Although the per-task file size (`-b`) is set to 50 TiB to match the write phase's geometry, the `-O stoneWallingWearOut=1` flag instructs IOR to stop reading as soon as it hits the exact data boundary recorded in the stonewall status file.
    
    mpirun \
      --allow-run-as-root \
      --mca plm_rsh_no_tree_spawn 1 \
      --mca opal_set_max_sys_limits 1 \
      --mca plm_rsh_num_concurrent ${NUM_NODES} \
      --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
      --npernode ${PROCESSES_PER_NODE} \
      --np ${NUM_PROCESSES} \
      --hostfile ~/hostfile \
      /usr/local/bin/ior \
      -a AIO \
      --posix.odirect \
      -F -g -v -r -k \
      -t 4m -b 50t \
      -D 60 \
      -O stoneWallingWearOut=1 \
      -O stoneWallingStatusFile=/lustre/test/ior-easy.stonewall \
      -o /lustre/test/ior_file

**Write IOPS**

This test uses small 4 KiB transfer sizes and 8 GiB per-task file sizes to measure the maximum Input/Output Operations Per Second (IOPS) the file system can handle.
    
    mpirun \
      --allow-run-as-root \
      --mca plm_rsh_no_tree_spawn 1 \
      --mca opal_set_max_sys_limits 1 \
      --mca plm_rsh_num_concurrent ${NUM_NODES} \
      --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
      --np ${NUM_PROCESSES} \
      --oversubscribe \
      --map-by node \
      --bind-to socket \
      --hostfile ~/hostfile \
      /usr/local/bin/ior \
      -e \
      -t 4k \
      -b 8g \
      -s 1 \
      -a AIO \
      --posix.odirect \
      --aio.max-pending=256 \
      -w \
      -F \
      -z \
      -Q 1 \
      -G 1745405099 \
      -D 45 \
      -O stoneWallingWearOut=1 \
      -o /lustre/test/ior-random

**Read IOPS**

To prevent reading from a sparse file, this test uses two commands: a write to create a solid file using 4 MiB transfer sizes and 8 GiB per-task file sizes, followed by the actual 4 KiB random read IOPS test.

     1. Create the file to read:
            
            mpirun \
              --allow-run-as-root \
              --mca plm_rsh_no_tree_spawn 1 \
              --mca opal_set_max_sys_limits 1 \
              --mca plm_rsh_num_concurrent ${NUM_NODES} \
              --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
              --npernode ${PROCESSES_PER_NODE} \
              --np ${NUM_PROCESSES} \
              --oversubscribe \
              --map-by node \
              --bind-to socket \
              --hostfile ~/hostfile \
              /usr/local/bin/ior \
              -a AIO \
              --posix.odirect \
              -w \
              -F \
              -k \
              -t 4m \
              -b 8g \
              -s 1 \
              -Q 1 \
              -G 1745405099 \
              -o /lustre/test/ior_rand_read

     2. Run the IOR read test:
            
            mpirun \
              --allow-run-as-root \
              --mca plm_rsh_no_tree_spawn 1 \
              --mca opal_set_max_sys_limits 1 \
              --mca plm_rsh_num_concurrent ${NUM_NODES} \
              --mca plm_rsh_args "-o StrictHostKeyChecking=no" \
              --oversubscribe \
              --map-by node \
              --bind-to socket \
              --npernode ${PROCESSES_PER_NODE} \
              --np ${NUM_PROCESSES} \
              --hostfile ~/hostfile \
              /usr/local/bin/ior \
              -a AIO \
              --posix.odirect \
              --aio.max-pending 256 \
              -r \
              -F \
              -z \
              -t 4k \
              -b 8g \
              -s 1 \
              -Q 1 \
              -G 1745405099 \
              -D 45 \
              -O stoneWallingWearOut=1 \
              -o /lustre/test/ior_rand_read

**Tip:** If the command returns an error that a daemon could not be reached or could not be started, it's likely that the startup script hasn't completed on one or more machines. You should retry the command after a few minutes.

The `mpirun` flags are:

     * `--mca plm_rsh_no_tree_spawn 1`: Disables tree-based daemon spawning to improve launch reliability across nodes.
     * `--mca opal_set_max_sys_limits 1`: Automatically attempts to set system limits (like max open files) to their highest allowed values.
     * `--mca plm_rsh_num_concurrent`: Sets the maximum number of concurrent SSH connections `mpirun` will use when launching worker daemons.
     * `--mca plm_rsh_args ...`: Bypasses strict host key checking to prevent interactive SSH prompts from hanging the MPI process launch.
     * `--prefix ...`: Explicitly defines the OpenMPI installation path for Rocky Linux and RHEL so worker nodes can find the required daemon (`orted`).
     * `--allow-run-as-root`: Allows `mpirun` to execute as the root user.
     * `--oversubscribe`: Allows MPI to schedule more processes on a node than there are available physical cores.
     * `--map-by node`: Distributes MPI processes in a round-robin fashion evenly across the available nodes.
     * `--bind-to socket`: Binds MPI processes to physical CPU sockets to optimize memory access and cache performance.
     * `--npernode`: The number of processes per node.
     * `--np`: The total number of MPI processes to launch.
     * `--hostfile`: Specifies the file containing the list of hosts to run on.

The `ior` flags are:

     * `-a AIO --posix.odirect`: Uses the Asynchronous I/O (AIO) engine combined with POSIX Direct I/O. This bypasses the client-side RAM page cache and forces concurrent non-blocking writes directly to the storage servers, ensuring the benchmark measures true network storage performance rather than memory buffers.
     * `--aio.max-pending=256`: Determines the maximum number of concurrent Asynchronous I/O operations in flight per process.
     * `-C`: Reorder tasks for optimal read performance.
     * `-F`: File-per-process mode.
     * `-g`: Use barriers to separate the write and read phases of the test.
     * `-v`: Output verbose logging.
     * `-w` / `-r`: Instructs IOR to run the write (`-w`) or read (`-r`) performance test.
     * `-k`: Prevents IOR from deleting the test file after writing, making it available for the read test.
     * `-e`: Performs an `fsync` after the write phase to guarantee that data is committed to the storage drives.
     * `-z`: Instructs IOR to perform random access I/O instead of sequential access.
     * `-s 1`: Sets the number of segments to 1.
     * `-Q 1`: Sets the task-per-node offset, aligning tasks so the benchmark coordinates correctly across all nodes.
     * `-G 1745405099`: Hardcodes the random seed timestamp so that the read phase generates the exact same random file offsets that the write phase used.
     * `-t`: Sets the transfer size for each I/O operation (e.g., `4m` for throughput, `4k` for IOPS).
     * `-b`: Sets the target block size per process (e.g., `50t` for throughput, `8g` for IOPS) to ensure the test does not run out of payload data during the timed run.
     * `-D`: Restricts the test runtime duration to a specific number of seconds (e.g., `60` or `45`). This "stonewalling" terminates the benchmark evenly to capture a true steady-state measurement.
     * `-O stoneWallingWearOut=1`: Forces all concurrent threads to keep generating continuous write load for the entire duration, preventing faster threads from completing early and dropping the overall network pressure.
     * `-O stoneWallingStatusFile=<path>`: Writes a state verification file at the end of the write phase. The subsequent read phase uses this file to read only the blocks that were successfully committed, preventing null pointer errors during reads.
     * `-o`: The path to the test file on the Managed Lustre file system.



### View the results

When the benchmark completes, it displays the aggregate performance metrics from all client VMs or pods directly in your terminal. Look for the **Results** table at the bottom of the output to find your maximum throughput or IOPS.

#### Key metrics

  * **`aggregate filesize`** : The total amount of data written or read during the test across all participating clients.

  * **`bw(MiB/s)` / `Max Write` / `Max Read`**: The most important metric for sequential tests. This shows the aggregate bandwidth achieved by the Managed Lustre file system.

  * **`IOPS`** : The most important metric for random I/O tests. This shows the maximum Input/Output Operations Per Second.




#### Export results to a file

If you want to programmatically parse your results, feed them into a database, or save them for later analysis, you can instruct IOR to export the summary data in JSON and CSV formats instead of just printing them to the screen.

To do this, append the `-O` flags to the end of your `ior` command string:
    
    
    -O summaryFormat=JSON \
    -O summaryFile=/lustre/test/perf-results/summary.json \
    -O saveRankPerformanceDetailsCSV=/lustre/test/perf-results/details.csv
    

The output directory must exist on the file system before running the benchmark.

### Expected versus real-world performance

You can calculate the mathematical maximum throughput of your file system based on its provisioned capacity and performance tier. Because storage capacity is provisioned in gibibytes (GiB) and tiers are rated in tebibytes (TiB), you must first convert your capacity:

(Capacity GiB / 1024) * Tier MBps = Theoretical Max MBps

For example, a **216,000 GiB** instance in the **500 MBps per TiB** tier mathematically provides **105,469 MBps** of throughput ((216000 / 1024) * 500).

Maximum observed throughput will always be bounded by either your file system's provisioned throughput capacity or the combined network egress limits of your client machines, whichever is lower.

Common reasons your benchmark numbers may not reach theoretical speeds include:

  * **TCP/IP overhead:** Standard network encapsulation and packet headers consume roughly 5-10% of raw bandwidth. Your mathematical maximum includes this overhead, but the IOR benchmark only measures the raw payload written to disk.

  * **Client network limits:** Client machines have strict egress bandwidth caps. If you use a small number of clients or nodes, or machine types without Tier 1 networking enabled, the clients will throttle the benchmark before the Managed Lustre file system reaches its limit.

  * **MPI context switching:** If `PROCESSES_PER_NODE` is set higher than the number of physical cores on your client machines, CPU contention and context-switching overhead will artificially degrade the benchmark's I/O performance.

  * **Missing Direct I/O:** If the `--posix.odirect` flag is omitted, data passes through the client's RAM page cache. This introduces memory bottlenecks and CPU overhead that mask the true network storage performance.




### Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps:

  1. Delete the test files from the Managed Lustre volume:
         
         ssh -i ./id_rsa -o "StrictHostKeyChecking=no" -o UserKnownHostsFile=/dev/null ${SSH_USER}@${HEAD_NODE} "rm -rf /lustre/test"
         

  2. Delete the bulk-created Compute Engine client machines:
         
         gcloud compute instances delete $(gcloud compute instances list \
           --filter="name~'^${CLIENT_PREFIX}-'" --format="value(name)" --zones="ZONE") \
           --zone="ZONE"
         

Alternatively, if you know the exact names or want to delete them individually:
         
         gcloud compute instances delete CLIENT_PREFIX-0001 CLIENT_PREFIX-0002 ... --zone=ZONE
         

  3. If you created a custom image, you can delete it:
         
         gcloud compute images delete CUSTOM_IMAGE_NAME
         

  4. If you created the Managed Lustre instance specifically for this test and no longer need it, delete it:
         
         gcloud lustre instances delete INSTANCE_ID --location=LOCATION
         




## Troubleshoot common benchmarking bottlenecks

If your benchmark results are significantly lower than your expected storage performance tier, see [Troubleshooting common bottlenecks](https://docs.cloud.google.com/managed-lustre/docs/performance#troubleshooting_common_bottlenecks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
