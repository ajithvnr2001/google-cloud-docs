---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ssh/
title: SSH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:56.907784+00:00
---

# SSH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SSH

This document provides guidance on how to integrate SSH with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/SSH.zip).

## Configure SSH integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Block IP Address in IPtables

#### Description

Add a rule to IPtables to block an IP address.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | x.x.x.x | Remote server address.  
Remote Username | String | root | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | N/A  
Block IP Address | String | N/A | IP address to block.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Delete Firewall Rule

#### Description

Delete IPtables Firewall rule (Example: INPUT -s 10.0.0.10 -j DROP).

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | Remote server address (example: x.x.x.x). | N/A  
Remote Username | String | root | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | N/A  
IPtables Rule | String | N/A | Rule value (example: INPUT -s 10.0.0.10 -j DROP).  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Execute Program

#### Description

Run a script on a remote machine.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | N/A  
Remote Program Path | String | N/A | The path to the program in the remote host.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### List Connections

#### Description

List all connections on a remote machine.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | N/A  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | True/False | results:False  
  
##### JSON Result
    
    
    {
        "Results": [
            "Proto,Recv-Q,SendQ,Local,Address,Foreign,Address,State,PID/Program,name",
            "tcp,0,0,0.0.0.0:111,0.0.0.0:*,LISTEN,1/systemd",
            "tcp,0,0,0.0.0.0:22,0.0.0.0:*,LISTEN,10624/sshd"
        ]
    }
    

### List Processes

#### Description

List the running processes on a remote machine.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | 22 | The default port will be 22.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | N/A | N/A  
  
##### JSON Result
    
    
    {
        "Processes": [
          "USER,PID,%CPU,%MEM,VSZ,RSS,TTY,STAT,START,TIME,COMMAND",
          "root,1,0.0,0.0,193656,6656,?,Ss,Jan16,0:24,/usr/lib/systemd/systemd --system --deserialize 24",
          "root,32142,0.0,0.0,0,0,?,S,Jan22,0:32,[kworker/3:1]"
        ]
    }
    

### List IPtables Rules

#### Description

List IPtable rules on a remote machine.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | The default port will be 22.  
Chain | String | N/A | The IPtables chain that you wish to see (example: INPUT, OUTPUT, etc.).  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | True/False | results:False  
  
##### JSON Result
    
    
    {
        "-,Chain,Rule": [
            "-P,INPUT,ACCEPT",
            "-P,FORWARD,ACCEPT",
            "-P,OUTPUT,ACCEPT"
        ]
    }
    

### Logoff User

#### Description

Logoff a remote user.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | The default port will be 22.  
Logoff Username | String | N/A | The username to log off.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

N/A

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

N/A

### ‌Reboot Machine

#### Description

Reboot a remote server.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | The default port will be 22.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Run Command

#### Description

Run a command on a remote machine.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | N/A  
Command | String | N/A | Command content (example: ifconfig).  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | True/False | results:False  
  
##### JSON Result
    
    
    {
        "ifconfig":
            "ens32: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>mtu1500
            Ninet1.1.1.1netmask1.1.1.1broadcast1.1.1.1
            ninet6fe80: : 2156: 9c37: 7a0d:
            87eprefixlen64scopeid0x20<link>
            nether00: 50: 56: b5: 70: e3txqueuelen1000(Ethernet)
            nRXpackets7448423bytes1077754116(1.0GiB)
            nRXerrors0dropped0overruns0frame0
            nTXpackets370155bytes44300304(42.2MiB)
            nTXerrors0dropped0overruns0carrier0collisions0
            nlo: flags=73<UP,LOOPBACK,RUNNING>mtu65536
            Ninet1.1.1.1netmask1.1.1.1
            ninet6: : 1prefixlen128scopeid0x10<host>
            nlooptxqueuelen1000(LocalLoopback)
            nRXpackets86bytes4780(4.6KiB)
            nRXerrors0dropped0overruns0frame0
            nTXpackets86bytes4780(4.6KiB)
            nTXerrors0dropped0overruns0carrier0collisions0"
    }
    

### Shutdown Machine

#### Description

Shutdown a remote machine.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | The default port will be 22.  
Wait Time | String | N/A | Time to wait before shutdown in minutes (example: now).  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Terminate Process

#### Description

Terminate a process on a remote machine.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Remote Server | String | N/A | Remote server address (example: x.x.x.x).  
Remote Username | String | N/A | N/A  
Remote Password | String | N/A | N/A  
Remote Port | String | N/A | N/A  
Process | String | N/A | Process to terminate.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
