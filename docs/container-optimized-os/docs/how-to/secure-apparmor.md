---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/secure-apparmor/
title: Securing containers with AppArmor \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:16:40.347474+00:00
---

# Securing containers with AppArmor  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/secure-apparmor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Securing containers with AppArmor Stay organized with collections  Save and categorize content based on your preferences. 

[AppArmor](https://en.wikipedia.org/wiki/AppArmor) is a Linux kernel security module that you can use to restrict the capabilities of processes running on the host operating system. Each process can have its own security profile. The security profile allows or disallows specific capabilities, such as network access or file read/write/execute permissions.

You can use AppArmor with the Docker containers running on your Container-Optimized OS instances. For any given container, you can apply either the default AppArmor security profile that comes with Docker, or a custom security profile that you provide.

## Using the default Docker AppArmor security profile

When you start a container on your Container-Optimized OS instance, the system automatically applies the `docker-default` AppArmor security profile. The following example command runs a container with the `docker-default` security profile:
    
    
    docker run --rm -it debian:jessie bash -i
    

To test the `docker-default` security profile, you can try to read the `/proc/sysrq-trigger` file with the `cat` command, as follows:
    
    
    root@88cef496c1a5:/# cat /proc/sysrq-trigger
    

The output should contain a "Permission Denied" error, similar to the following:
    
    
    cat: /proc/sysrq-trigger: Permission denied
    

**Note:** See Docker's [AppArmor security profiles for Docker](https://docs.docker.com/engine/security/apparmor) documentation for additional information on Docker's default AppArmor security profile.

## Applying a custom security profile

To apply a different security profile, use the `apparmor=<profile-name>` command-line option when you run your container. The following example command runs a container with a security profile called `no-ping`:
    
    
    docker run --rm -i --security-opt apparmor=no-ping debian:jessie bash -i
    

See Creating a custom security profile later in this topic for more information on creating the `no-ping` profile specified in the example.

You can also specify `unconfined` with the `apparmor` option to indicate that the container is to be run with _no_ security profile, as in the following example:
    
    
    docker run --rm -it --security-opt apparmor=unconfined debian:jessie bash -i
    

## Viewing the active AppArmor security profiles

You can see what AppArmor profile, if any, applies to the processes on your Container-Optimized OS instance by inspecting the `/proc/<pid>/attr/current` file, where `<pid>` is the process ID.

Suppose you have the following processes running on your instance (shown by the `ps -ef | grep '[b]ash -i'` command):
    
    
    root      1903  1897  0 21:58 pts/3    00:00:00 docker run --rm -it debian:jessie bash -i
    root      1927  1913  0 21:58 pts/4    00:00:00 bash -i
    root      1978  1001  0 22:01 pts/0    00:00:00 docker run --rm -it --security-opt apparmor=unconfined debian:jessie bash -i
    root      2001  1988  0 22:01 pts/2    00:00:00 bash -i
    

**Note:** You can also add the `-Z` flag to your `ps` command to display the security profile for each process.

If you inspect `/proc/1927/attr/current`, you should see the following output that indicates the process (`pid 1927`) was run with the default Docker security profile:
    
    
    # cat /proc/1927/attr/current
    docker-default (enforce)
    

If you inspect `/proc/2001/attr/current`, you should see the following output that indicates the process (`pid 2001`) was run with _no_ security profile (that is, with the option `apparmor=unconfined`):
    
    
    # cat /proc/2001/attr/current
    unconfined
    

## Creating a custom security profile

If process requires a different security profile than `docker-default`, you can write your own custom profile. To use a custom profile, you must create the profile file and then load that file into AppArmor.

For example, suppose you want a security profile that disallows all raw network traffic. The following script creates a file for a security profile called `no-ping` at `/etc/apparmor.d/no_raw_net`:
    
    
    cat > /etc/apparmor.d/no_raw_net <<EOF
    #include <tunables/global>
    
    profile no-ping flags=(attach_disconnected,mediate_deleted) {
      #include <abstractions/base>
    
      network inet tcp,
      network inet udp,
      network inet icmp,
    
      deny network raw,
      deny network packet,
      file,
      mount,
    }
    EOF
    

Once you've created the security profile file, you can use `apparmor_parser` to load the profile into AppArmor:
    
    
    /sbin/apparmor_parser --replace --write-cache /etc/apparmor.d/no_raw_net
    

Once loaded, you can test the `no-ping` profile as follows:
    
    
    $ docker run --rm -i --security-opt apparmor=no-ping debian:jessie ping -c3 8.8.8.8
    

The command creates a container with the `no-ping` security profile and attempts to run `ping` from within the container. The security profile should disallow the traffic, resulting in an error like the following:
    
    
    ping: Lacking privilege for raw socket.
    

To ensure that your custom security profile is present when your Container-Optimized OS instance boots, and remains persistent across reboots, you can use `cloud-init` to install the profile in `/etc/apparmor.d`. To do so, add a `cloud-config` script to your instance's metadata as the value of the `user-data` key.

The following `cloud-config` script adds the `no-ping` profile to `/etc/apparmor.d`:
    
    
    #cloud-configs
    
    write_files:
    - path: /etc/apparmor.d/no_raw_net
      permissions: 0644
      owner: root
      content: |
        #include <tunables/global>
    
        profile no-ping flags=(attach_disconnected,mediate_deleted) {
          #include <abstractions/base>
    
          network inet tcp,
          network inet udp,
          network inet icmp,
    
          deny network raw,
          deny network packet,
          file,
          mount,
        }
    

To ensure that your service file loads your custom profile into AppArmor and tells Docker to use it, run the following commands on your instance:
    
    
    ExecStartPre=/sbin/apparmor_parser -r -W /etc/apparmor.d/no_raw_net
    ExecStart=/usr/bin/docker run --security-opt apparmor=no-ping ...
    

After you've run the commands, reboot your instance, and you can then run your container confined by your custom AppArmor profile.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
