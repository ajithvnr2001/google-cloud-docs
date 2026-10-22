---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/firewall/
title: Configuring the host firewall \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:36.053936+00:00
---

# Configuring the host firewall  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Configuring the host firewall Stay organized with collections  Save and categorize content based on your preferences. 

By default, the Container-Optimized OS host firewall allows outgoing connections and accepts incoming connections only through the SSH service. You can see the exact host firewall configuration by running `sudo iptables -L` on a VM instance running Container-Optimized OS.

**Warning:** The default firewall configuration might be different if you are using Container-Optimized OS through another Google Cloud product like [Containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/deploying-containers) or Google Kubernetes Engine. Refer to the product specific documentation for more details.

Keep in mind that the host firewall is different from Virtual Private Cloud firewall rules, which must also be configured for your applications to work correctly. See the [Firewall Rules Overview](https://docs.cloud.google.com/vpc/docs/firewalls) to learn more about Virtual Private Cloud firewall rules.

## Running containers in Docker's default network namespace

If you are deploying a container on Container-Optimized OS that must be accessible over the network and you are not using Docker's `--net=host` option, run your container with Docker's `-p` option. With this option, Docker will automatically configure the host firewall to expose your application on the network. See the [Docker run reference](https://docs.docker.com/engine/reference/run/) to learn more about Docker run options.

In the following example, the `nginx` container will be accessible on the network on port 80:
    
    
    docker run --rm -d -p 80:80 --name=nginx nginx
    

**Note:** If IPv6 address is used for accessing the deployed container over the network, you must explicitly configure the host firewall using `ip6tables` commands like `"ip6tables -A INPUT -p tcp --dport 80 -j ACCEPT"`.This is because Docker does not automatically configure the IPv6 rules for host firewall to expose your application on the network due to [known limitation](https://github.com/moby/moby/issues/21951).

## Running containers in the host's network namespace

If you are deploying a container on Container-Optimized OS that must be accessible over the network and you are using Docker's `--net=host` option, you must explicitly configure the host firewall yourself.

You can configure the host firewall with standard `iptables` commands. As with most GNU/Linux distributions, firewall rules configured with `iptables` commands will not persist across reboots. To ensure that the host firewall is correctly configured on every boot, configure the host firewall in your `cloud-init` configuration. Consider the following `cloud-init` example:
    
    
    #cloud-config
    
    write_files:
    - path: /etc/systemd/system/config-firewall.service
      permissions: 0644
      owner: root
      content: |
        [Unit]
        Description=Configures the host firewall
    
        [Service]
        Type=oneshot
        RemainAfterExit=true
        ExecStart=/sbin/iptables -A INPUT -p tcp --dport 80 -j ACCEPT
    - path: /etc/systemd/system/myhttp.service
      permissions: 0644
      owner: root
      content: |
        [Unit]
        Description=My HTTP service
        After=docker.service config-firewall.service
        Wants=docker.service config-firewall.service
    
        [Service]
        Restart=always
        ExecStart=/usr/bin/docker run --rm --name=%n --net=host nginx
        ExecStop=-/usr/bin/docker exec %n -s quit
    
    runcmd:
    - systemctl daemon-reload
    - systemctl start myhttp.service
    

Using this `cloud-init` configuration with a VM running Container-Optimized OS will result in the following behaviors on every boot:

  * The host firewall will be configured to allow incoming TCP connections on port 80.
  * An `nginx` container will listen on port 80 and respond to incoming HTTP requests.



Refer to [Creating and configuring instances](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance) to learn more about using `cloud-init` on Container-Optimized OS.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
