---
url: https://docs.cloud.google.com/filestore/docs/setting-nfs-ports/
title: Configure NFS ports on client VMs \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:17.338002+00:00
---

# Configure NFS ports on client VMs  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/setting-nfs-ports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Configure NFS ports on client VMs Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set the ports for the `statd` and `nlockmgr` daemons on your client VMs to make firewall configuration easier.

Filestore uses the `nlockmgr` and `statd` daemons to enable file locking. The ports for these services need to be properly exposed on your client VMs through firewall rules so that clients can properly use locks. We recommend setting the `statd` and `nlockmgr` ports so that they are consistent on all client VMs, making it easier to configure ingress firewall rules.

For more information on determining if you need to configure a firewall rule for the VPC network, see [Configure firewall rules](https://docs.cloud.google.com/filestore/docs/configuring-firewall).

## Check port settings

To check what values the `statd` and `nlockmgr` ports are currently set to, run the following commands on the client VM instance. If the files don't exist, or if the options don't have values, then the ports aren't set. In that case, the daemons are dynamically assigned arbitrary available ports.

###  Debian/Ubuntu 

  1. To determine the `statd` port, run the following command and look at the `STATDOPTS` value:
         
         cat /etc/default/nfs-common
         

  2. To determine the `nlockmgr` port, run the following command and look at the `nlm_tcpport` and `nlm_udpport` values:
         
         cat /etc/modprobe.d/lock.conf
         




###  RHEL/CentOS 

  1. To determine the `statd` port, run the following command and look at the `STATD_PORT` value:
         
         cat /etc/sysconfig/nfs
         

  2. To determine the `nlockmgr` port, run the following command and look at the `nlm_tcpport` and `nlm_udpport` values:
         
         cat /etc/modprobe.d/lock.conf
         




###  SUSE 

Run the following command:
    
    
    cat /etc/sysconfig/nfs
    

The `statd` port is listed under `STATD_PORT` and the `nlockmgr` port is listed under `LOCKD_TCPPORT` and `LOCKD_UDPPORT`.

###  Windows 

Setting NFS ports is not required on Windows.

## Set ports

To set the `statd` and `nlockmgr` ports, run the following commands on the client VM instance. These examples use the [`nano`](https://www.nano-editor.org/) text editor, but you can use any text editor. These examples also use 2046 as the port for `statd` and 4045 as the port for `nlockmgr` because these values are common choices. You can use different ports based on your network configuration. In this case, the ingress firewall rules must allow traffic to the specific ports that you use.

**Important:** If you set ports on a client VM instance that already has file shares mounted on it, you must reboot the instance for the changes to take effect.

###  Debian/Ubuntu 

  * Set the `statd` port:

    1. Open the `/etc/default/nfs-common` file for editing:
           
           sudo nano /etc/default/nfs-common
           

    2. Set the `STATDOPTS` option:
           
           STATDOPTS="-p 2046"
           

    3. Save the file and exit.

  * Set the `nlockmgr` port:

    1. Create the `/etc/modprobe.d/lock.conf` file:
           
           sudo nano /etc/modprobe.d/lock.conf
           

    2. Set the `nlm_tcpport` and `nlm_udpport` options:
           
           options lockd nlm_tcpport=4045
           options lockd nlm_udpport=4045
           

    3. Save the file and exit.




###  RHEL/CentOS 

  * Set the `statd` port:

    1. Open the `/etc/sysconfig/nfs` file for editing:
           
           sudo nano /etc/sysconfig/nfs
           

    2. Set the `STATD_PORT` option:
           
           STATD_PORT=2046
           

    3. Save the file and exit.

  * Set the `nlockmgr` port:

    1. Create the `/etc/modprobe.d/lock.conf` file:
           
           sudo nano /etc/modprobe.d/lock.conf
           

    2. Set the `nlm_tcpport` and `nlm_udpport` options:
           
           options lockd nlm_tcpport=4045
           options lockd nlm_udpport=4045
           

    3. Save the file and exit.




###  SUSE 

Set the `statd` and `nlockmgr` ports:

  1. Open the `/etc/sysconfig/nfs` file for editing:
         
         sudo nano /etc/sysconfig/nfs
         

  2. Set the `STATD_PORT`, `LOCKD_TCPPORT`, and `LOCKD_UDPPORT` options:
         
         STATD_PORT=2046
         LOCKD_TCPPORT=4045
         LOCKD_UDPPORT=4045
         

  3. Save the file and exit.




###  Windows 

Setting NFS ports is not required on Windows.

## Verify ports are open

To verify NFS ports have been opened properly, complete the following steps.

  1. Install the following dependencies.

###  Debian/Ubuntu 

From the command line, enter the following command:
         
         sudo apt install nfs-common tcpdump tshark
         

###  RHEL/CentOS 

From the command line, enter the following command:
         
         sudo yum install nfs-utils tcpdump wireshark
         

###  SUSE 

From the command line, enter the following command:
         
         sudo zypper install nfs-client tcpdump wireshark
         

###  Windows 

This verification process is not supported on Windows.

  2. Create a script file called `verify-nfs-port-script.sh`, copy and paste the following script within it, and save it locally to your machine. Note the location of the file and save it for the next step.
         
         #!/bin/bash
         
         # This script is intended to run on client machines to verify that the ports
         # are properly open to allow the reception of NLM GRANT messages from the server.
         
         set -eu
         
         function kill_descendants() {
            for pid in $(ps -o pid= --ppid "$1")
            do
            kill_descendants "$pid"
            done
            if [[ $1 -ne $$ ]]; then
            kill "$1" 2>/dev/null | true
            fi
         }
         
         function cleanup {
            set +eu
         
            # Kill all background jobs and wait for it to end, makes sure locks are released
            kill_descendants $$
         
            # Wait for jobs to die and locks to be released, so mount is not busy
            sleep 2
         
            umount -f "$MNT1"
            umount -f "$MNT2"
         
            rmdir "$MNT1" 2&> /dev/null || true
            rmdir "$MNT2" 2&> /dev/null || true
         }
         
         function print_help {
            echo "$0 [server_ip] [mount_path]"
            echo -e "\t For example, if you mount a server using:"
            echo -e "\t\t \"mount 10.0.0.1:share /mnt/mount_point\""
            echo -e "\t Run the script: "
            echo -e "\t\t \"$0 10.0.0.1 share\""
         }
         
         if [ $# -ne 2 ]; then
            print_help
            exit 1
         fi
         
         if [ $(id -u) -ne 0 ]; then
            echo "Failure! This script needs to run as root, use \"sudo $@\""
            exit 1
         fi
         
         if ! [ -x "$(command -v tshark)" ]; then
            echo "The 'tshark' command does not exist and is needed for the script. Please install it"
            exit 1
         fi
         
         if ! [ -x "$(command -v tcpdump)" ]; then
            echo "The 'tcpdump' command does not exist and is needed for the script. Please install it"
            exit 1
         fi
         
         SERVER_IP=$1
         MOUNT_PATH=$2
         
         MNT1=$(mktemp -d)
         MNT2=$(mktemp -d)
         
         trap cleanup EXIT
         
         echo "Mounting..."
         mount -o nosharecache "$SERVER_IP":"$MOUNT_PATH" "$MNT1"
         mount -o nosharecache "$SERVER_IP":"$MOUNT_PATH" "$MNT2"
         
         REC_FILE=$(mktemp /tmp/nlm_recording_XXXXXXXX.pcap)
         tcpdump -i any -s0 -w "$REC_FILE" "host $SERVER_IP" &
         TCPDUMP_PID=$!
         echo "Recording TCP dump to $REC_FILE"
         
         sleep 5 # wait for tcpdump to start running
         
         echo "Running test..."
         flock "$MNT1"/lock_file -c "echo -n \"Got first lock: \" && date && sleep 5 && echo -n \"Releasing first lock: \" && date" &
         sleep 2 # Wait for the first lock to actually be taken
         
         echo "Waiting for second lock: $(date)"
         flock "$MNT2"/lock_file -c "echo -n \"Got second lock: \" && date"
         
         sleep 2 # Wait for tcpdump to record everything
         kill $TCPDUMP_PID
         
         # For quick analysis inspect recording with tshark, if you don't have it just inspect with Wireshark
         echo "Inspecting results in $REC_FILE with TShark"
         tshark -r "$REC_FILE" -Y nlm # First, print the output
         
         tshark -r "$REC_FILE" -Y nlm 2>/dev/null | grep -q GRANTED
         EXIT_CODE=0
         if [ $? -eq 0 ]; then
            echo "The NLM GRANT message is working properly!"
            EXIT_CODE=0
         else
         echo "The NLM GRANT message is not working properly!"
         EXIT_CODE=1
         fi
         echo "For debugging, please provide the printed output of the script, and $REC_FILE"
         exit ${EXIT_CODE}
         

  3. Enter the following command:
         
         chmod +x SCRIPT_PATH
         

Replace the following:

     * `SCRIPT_PATH`: the path where your script file is located. This should be run as root, otherwise add `sudo` to the beginning of the command.
  4. Enter the following command:
         
         SCRIPT_PATH INSTANCE_IP SHARE_NAME
         

Replace the following:

     * `SCRIPT_PATH`: the path where your script file is located. This should be run as root, otherwise add `sudo` to the beginning of the command.
     * `INSTANCE_IP`: the IP address of the Filestore instance
     * `SHARE_NAME`: the name of the file share

If the port is open, the script returns the following response:
    
    The NLM GRANT message is working properly!
    

If the port is not open, the script returns the following error:
    
    The NLM GRANT message is not working properly!
    




## What's next

  * [Configure firewall rules](https://docs.cloud.google.com/filestore/docs/configuring-firewall).
  * [Learn more about the networking and IP resource requirements for using Filestore](https://docs.cloud.google.com/filestore/docs/networking).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
