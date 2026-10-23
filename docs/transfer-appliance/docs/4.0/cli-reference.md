---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/cli-reference/
title: Transfer Appliance CLI Reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:54.145202+00:00
---

# Transfer Appliance CLI Reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/cli-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Resources ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/resources)



Send feedback 

#  Transfer Appliance CLI Reference Stay organized with collections  Save and categorize content based on your preferences. 

## ta check

Checks the appliance for errors.

### Synopsis

Diagnoses and helps customers fix common problems. The main goal of the command is to help detect misconfigurations as early as possible.

This command checks multiple aspects of the appliance, including: \- Hardware \- Software \- ABM \- Encrypt \- Keys \- Usage \- Network \- SSH
    
    
    ta check [flags]
    

### Examples
    
    
        ta check
        ta check usage
        ta check hardware
        ta check {category}
    

### Options
    
    
      -e, --env string   Environment to run the check in. (default "prod")
      -h, --help         help for check
    

* * *

## ta config

Configures the appliance.

### Synopsis

Configure or reconfigure the appliance making it ready for data transfer. The provided configuration will be persisted and remembered over subsequent reboots and until the "finalize" command is issued. Use the "status" command later to see the current configuration. During configuration, the NFS share is created and exported for data capture. At the same time, data encryption is enabled so that the data copied is always secure and under your control. Encrypting and mounting the data partition will only be done once; you may rerun the "config" command to update the network setting at any time.
    
    
    ta config [flags]
    

### Examples
    
    
        ta config --data_port=RJ45 --ip=192.168.0.100/24 --gw=192.168.0.1
        ta config --data_port=RJ45 --ip=dhcp
        ta config --data_port=RJ45 --ip=dhcp --authorized_hosts=192.168.0.101
        ta config --data_port=RJ45 --ip=dhcp --authorized_hosts=192.168.0.101,192.168.0.0/28
        ta config --data_port=RJ45 --ip=192.168.0.100/24 --gw=192.168.0.1 --network_only --dns_servers=8.8.8.8
        ta config --data_port=QSFP --ip=192.168.0.100/24 --gw=192.168.0.1
        ta config --data_port=QSFP --ip=dhcp
        ta config --data_port=RJ45 --ip=dhcp --data_size=200T
        ta config --data_port=QSFP --ip=dhcp --network_only
        ta config --data_port=RJ45 --ip=dhcp --proxy_addr=http://10.10.10.10:3128
        ta config --data_port=RJ45 --ip=dhcp --proxy_addr=http://10.10.10.10:3128 --network_only
        ta config --data_port=RJ45 --ip=192.168.0.100/24 --gw=192.168.0.1 --proxy_addr=http://10.10.10.10:3128 --network_only
    

### Options
    
    
      -a, --authorized_hosts strings   Comma-separated list of hosts that are allowed to connect to the NFS share. (default [*])
          --data_port string           Type of data port: 'RJ45', 'SFP', or 'QSFP'
          --data_size string           Resizes the data disk partition to the provided size. Does not change the existing data disk if left empty.
          --dns_servers strings        Comma-separated list of DNS name server addresses.
          --env string                 Environment to run the appliance configuration in. (default "prod")
          --fileshare string           File share protocol to configure: 'smb' or 'nfs' (default "nfs")
          --gw string                  IPv4 address of the default gateway. Must be provided for static IP configuration. Example: 192.168.6.1
      -h, --help                       help for config
          --ip string                  IPv4 & netmask address (for static setting), or 'dhcp' (for dynamic). Example: 192.168.6.11/24
          --json                       If true, command output is in JSON format.
          --network_interface string   Network interface to configure.
          --network_only               Configure the appliance network without changing the disk or fileshare configuration.
          --proxy_addr string          Proxy server address to configure. Must be in format http://<IP_ADDR>:<Port>. Example: http://10.10.10.10:3128
          --remove                     Removes the network configuration associated with the network interface provided.
          --restart_bind_mounts        Restart the bind mounts for ta_data and ta_local.
    

* * *

## ta copy_ssh_keys

Copies SSH keys to the appliance.
    
    
    ta copy_ssh_keys [flags]
    

### Options
    
    
      -h, --help   help for copy_ssh_keys
    

* * *

## ta diagnostics

Displays diagnostics information of the appliance.

### Synopsis

Collects diagnostic information useful for troubleshooting in case of any issues. This includes copies of system configuration files and the output of some diagnostic tools. It does not include any user data. Information is collected into a compressed archive file so it can be sent to Google for troubleshooting.
    
    
    ta diagnostics [flags]
    

### Examples
    
    
        ta diagnostics
        ta diagnostics --bmc
    

### Options
    
    
      -B, --bmc    Include BMC FFDC logs in diagnostics logs
      -h, --help   help for diagnostics
    

* * *

## ta disable_nfsv3

Disables NFSv3 on the appliance.

### Synopsis

This command disables the use of NFSv3 clients to transfer data to the Transfer Appliance.
    
    
    ta disable_nfsv3 [flags]
    

### Options
    
    
      -h, --help   help for disable_nfsv3
    

* * *

## ta disable_online_operations

Disables online operations on the appliance.
    
    
    ta disable_online_operations [flags]
    

### Options
    
    
      -h, --help   help for disable_online_operations
    

* * *

## ta enable_nfsv3

Enable the use of NFSv3 clients to transfer data to the Transfer Appliance.

### Synopsis

This command enables the use of NFSv3 clients to transfer data to the Transfer Appliance.

Enabling NFSv3 introduces limitations regarding filename encoding. GCS (Google Cloud Storage) requires filenames to be UTF-8 encoded. While NFSv4 automatically converts filenames to UTF-8 during transfer, NFSv3 does not.

Therefore, if using NFSv3: * Files with non-UTF-8 encoded filenames may fail to upload to GCS. * If uploads fail, identifying the failed files can be difficult due to potential filename encoding issues.

Recommendation: Before using NFSv3, ensure all filenames are UTF-8 encoded. If files are not UTF-8 encoded, consider using SCP or SFTP for transfer instead.

Windows Clients: These CLI options should not be used with Windows NFSv3 clients, as the Windows client uses a different encoding. For Windows clients, SCP or SFTP is the recommended transfer method. These options may only be used if Windows clients guarantee that all their filenames are in ASCII, but they should be made aware that files with non-ASCII filenames will fail to be uploaded to GCS.
    
    
    ta enable_nfsv3 [flags]
    

### Options
    
    
      -h, --help   help for enable_nfsv3
    

* * *

## ta finalize

Finalizes the appliance.

### Synopsis

Ensure the device is safe and ready for shipping. In particular, this purges all encryption keys and persisted configuration. It also removes any contents stored in appliance local storage. Please take backup of important files or move to the ta_data directory. Data transfers will no longer be possible after issuing this command. This removes the netplan configuration, and the changes take effect only upon reboot. Consequently, the appliance will disconnect from the network following a reboot. The appliance should never be shipped without running this command first. A passcode will be generated that must be provided to get a return shipping label; if necessary, running 'ta status' will report the passcode.
    
    
    ta finalize [flags]
    

### Examples
    
    
        ta finalize
    

### Options
    
    
      -h, --help                     help for finalize
          --non_repudiation          Verify the authenticity of arriving data. (default true)
          --skip_reencrypt_bmcpass   Skip reencrypting BMC passphrase.
          --skip_shred_mount_fstab   Skip shredding of opt/customer fstab file.
          --tpm_clear                Clear the TPM. (default true)
    

* * *

## ta fsck

Runs fsck on the appliance.

### Synopsis

The fsck command checks the filesystem consistency of the appliance. Running this command does not make any changes to the appliance. It ensures that any filesystem errors are detected before returning the appliance. Debugging filesystem errors during data transfers to Google Cloud can be challenging or infeasible. This can lead to delays or failures in data upload. This command may take more than 5 hours to complete. The system might need to be rebooted after running this command.
    
    
    ta fsck [flags]
    

### Examples
    
    
        ta fsck
        ta fsck -f
        ta fsck --fix
    

### Options
    
    
      -f, --fix    Repair filesystem errors if found.
      -h, --help   help for fsck
    

* * *

## ta mount

Run mount on the appliance.

### Synopsis

Mount handles mounting on the appliance. It wraps Linux's mount command.
    
    
    ta mount [flags]
    

### Examples
    
    
        ta mount --version
        ta mount --list
        ta mount --all
        ta mount --types=nfs --source=nfs_server_ip:/nfs_share_directory --target=/mnt/ta_data_base/ta_mounts/mount_point
        ta mount --types=nfs --source=nfs_server_ip:/nfs_share_directory --target=/mnt/ta_data_base/ta_mounts/mount_point --options=rw,suid,dev,exec,auto,nouser,async
        ta mount --types=cifs --options=username=user1,password=password --source=//cifs_share_ip/share_name --target=/mnt/ta_data_base/ta_mounts/mount_point
    

### Options
    
    
          --all              Mount all customer mounts.
      -h, --help             help for mount
          --list             List of customer mounts.
          --options string   Mount options given in a comma separated string, defaults is set as default. (default "defaults")
          --source string    Device being mounted.
          --target string    Mountpoint of the mount, expected to be under /mnt/ta_data_base/ta_mounts/.
          --types string     Filesystem type of the device to be mounted.
          --version          Version of the mount command.
    

* * *

## ta offline

Disables online operations on the appliance.

### Synopsis

Disables the online transfer mode of the appliance. Data from the specified online directory will NOT be moved from on-premises to Cloud even in the presence of network connectivity.
    
    
    ta offline [flags]
    

### Examples
    
    
        ta offline
    

### Options
    
    
      -h, --help   help for offline
    

* * *

## ta online

Enable the online transfer mode of the appliance.

### Synopsis

Enables the online transfer mode of the appliance. Data from the specified online directory will be moved from on-premises to GCS in presence of network connectivity. Individual files are automatically deleted after successful upload to GCS, while directory hierarchies are preserved. (The needed service account credentials are expected to be present under /tmp/key.json)
    
    
    ta online [flags]
    

### Examples
    
    
        ta online
        ta online --bucket=my-bucket --object_prefix=my-object_prefix
        ta online --bucket=my-bucket
        ta online --object_prefix=my-object_prefix
    

### Options
    
    
          --agent_pool             Use agent pool in online transfer. (default true)
          --bucket string          Update destination bucket used in online transfer. If in online state, this will stop the running job and start a new transfer job. NOTE: This cannot be an empty string.
          --env string             Environment to run the online transfer in. (default "prod")
      -h, --help                   help for online
          --object_prefix string   Update bucket object prefix used for online transfer. If in online state, this will stop the running job and start a new transfer job.
          --skip_api_check         Bypass the required APIs check on the customer project.
          --skip_net_check         Bypass the network connectivity check that attempts to ping google.
          --skip_role_check        Bypass the HTA IAM Role check on the session service account.
    

* * *

## ta performance

Storage benchmark test that saves output in ta_metadata.

### Synopsis

Outputs a csv of fio storage performance benchmark metrics in ta_metadata: \- Timestamp \- Appliance serial number \- Current session ID \- Appliance model \- Zimbru OS version \- Appliance location \- Benchmark read bandwidth \- Benchmark read completion latency \- Benchmark write bandwidth \- Benchmark write completion latency \- Benchmark parameters
    
    
    ta performance [flags]
    

### Examples
    
    
        ta performance
        ta performance --upload
    

### Options
    
    
          --enable_standard_benchmarking   This temporary flag will be used to gradually rollout the new performance benchmark flow.
          --env string                     Environment for token to upload to cloud monitoring. (default "prod")
      -h, --help                           help for performance
          --token string                   Token to authenticate with google cloud. Mutually exclusive with --token-file.
          --token-file string              Path to file containing token to authenticate with google cloud. Mutually exclusive with --token.
          --upload                         Upload performance results to cloud monitoring.
    

* * *

## ta pull

pulls and archives data mounted on the appliance.

### Synopsis

Pull will take in a directory location and process and archive all the files existing there, saving it to the destination specified. This command will generate a manifest file describing what files were saved into what archive. An error file will be saved to destination, which will include any errors encountered while processing the target directory.
    
    
    ta pull [flags]
    

### Examples
    
    
        ta pull --target=/mnt/ta_data_base/ta_mounts/test --size="1GB" --max_archive_file_size="200 MB" --destination=/mnt/ta_data/destination
        ta pull --target=/mnt/ta_data_base/ta_mounts/test --size="1GB" --max_archive_file_size="200 MB" --destination=/mnt/ta_data/destination --count=22
        ta pull --target=/mnt/ta_data_base/ta_mounts/test
        ta pull --target=/mnt/ta_data_base/ta_mounts/test --no_archive
        ta pull --id=55555 --status
        ta pull -i=55555 --pause
        ta pull --id=55555 -r
        ta pull --cleanup
    

### Options
    
    
      -C, --cleanup                        Cleanup the pull job.
      -c, --count int                      The number of tarballs to pull at once. (default 1)
      -d, --destination string             The destination directory where the files will be pulled. (default "/mnt/ta_data/")
      -h, --help                           help for pull
      -i, --id string                      The ID of the pull.
      -m, --max_archive_file_size string   The maximum size of the what is considered archivale file.
      -n, --no_archive                     Skips archiving all pulled files.
      -p, --pause                          Pause the pull job.
      -r, --resume                         Resume the pull job.
      -S, --size string                    The target tarball size. (default "1GB")
      -X, --status                         Get the status of the pull job.
      -t, --target string                  The target directory containing the files to be pulled and archived, expected to be under /mnt/ta_data_base/ta_mounts/.
      -T, --test                           Test the pull job.
    

* * *

## ta reset

Resets the appliance.

### Synopsis

Resets the appliance to its original state.  
This means that any data already copied to the data partition will be lost. After reset, the appliance will need to be reconfigured, which will format the data partition and make the appliance ready for data transfer. NFS/SMB will be disabled. The network configuration will be reset, however the changes will take effect only upon reboot.
    
    
    ta reset [flags]
    

### Examples
    
    
        ta reset
    

### Options
    
    
      -h, --help                     help for reset
          --preserve_key             Preserve HTA key.json on reset.
          --preserve_state           Preserve HTA state on reset.
          --skip_reencrypt_bmcpass   Skip reencrypting BMC passphrase.
          --skip_shred_mount_fstab   Skip shredding of opt/customer fstab file.
    

* * *

## ta restart_nfs

Restarts the NFS server on the appliance.
    
    
    ta restart_nfs [flags]
    

### Options
    
    
      -h, --help   help for restart_nfs
    

* * *

## ta smbpass

Configure the customer SMB password.

### Synopsis

Overrides the password for the default ta_customer SMB user interactively.
    
    
    ta smbpass [flags]
    

### Options
    
    
      -h, --help   help for smbpass
    

* * *

## ta status

Displays status and health information of the appliance.

### Synopsis

Displays status and health information of the appliance: \- state of the appliance: unconfigured, ready for transfer, finalized. \- current configuration of the appliance (per last "config" command) \- pulse information (e.g. storage used & available, count file copied, transfer speed) \- health-checks (e.g. unavailable disks, invalid state, invalid configuration)
    
    
    ta status [flags]
    

### Examples
    
    
        ta status
        ta status --verbose
    

### Options
    
    
      -h, --help      help for status
      -v, --verbose   If true, displays verbose status information.
    

* * *

## ta telemetry_archive

Command to archive telemetry logs.
    
    
    ta telemetry_archive [flags]
    

### Options
    
    
      -h, --help   help for telemetry_archive
    

* * *

## ta timesync

Manage time synchronization

### Options
    
    
      -h, --help   help for timesync
    

* * *

## ta unmount

Run unmount on the appliance.

### Synopsis

Unmount handles unmount customer mounts on the appliance and removes the entry from {{.CustomerFstab}}.
    
    
    ta unmount [flags]
    

### Examples
    
    
        ta unmount --version
        ta unmount --all
        ta unmount --target=/mnt/ta_data_base/ta_mounts/test
    

### Options
    
    
          --all             Unmount all filesystems.
      -h, --help            help for unmount
          --target string   The target directory to unmount.
          --version         Print the version of the unmount command.
    

* * *

## ta unseal

Unseals the DEK and mounts the data partition of the appliance.

### Synopsis

Unseals the DEK and mounts the data partition of the appliance. This command is required after a reboot to unseal the data encryption key and remount the data partition. This command has to be run before continuing with the data transfer.
    
    
    ta unseal [flags]
    

### Examples
    
    
        ta unseal
    

### Options
    
    
      -h, --help   help for unseal
    

* * *

## ta update

Command to update the ta binary on the appliance.

### Synopsis

Updates the ta binary on the appliance.
    
    
    ta update [flags]
    

### Examples
    
    
        ta update
    

### Options
    
    
          --env string   Environment to conduct the update in. (default "prod")
      -h, --help         help for update
    

* * *

## ta version

Displays version of the appliance.
    
    
    ta version [flags]
    

### Options
    
    
      -h, --help   help for version
    

* * *

## ta wipe

Wipes the data partition of the appliance.

### Synopsis

Wipe wipes all the data drives on the applinace in a NIST compliant manner. A certificate detailing the drives that were wiped and the tools used to wipe the drives will be generated. Wipe is an irreversable command meaning that there is no way to recover data once the drives are wiped.
    
    
    ta wipe [flags]
    

### Examples
    
    
        ta wipe
    

### Options
    
    
      -h, --help   help for wipe
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
