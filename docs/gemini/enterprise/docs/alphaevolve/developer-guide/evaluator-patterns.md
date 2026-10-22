---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/evaluator-patterns/
title: Evaluator implementation patterns \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:47.918311+00:00
---

# Evaluator implementation patterns  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/evaluator-patterns/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Evaluator implementation patterns Stay organized with collections  Save and categorize content based on your preferences. 

The evaluator is a critical component that determines the fitness of a program candidate. Its implementation varies from a basic in-process function to a complex orchestrator for remote jobs.

### Evaluator implementation use cases

Select an implementation pattern based on the complexity of your problem and the execution environment.

Use Case | Complexity | Implementation | Key Considerations  
---|---|---|---  
**Simple Algorithms** | Minimal; single-file Python script. | In-Process / Child Process | Low latency; limited scalability.  
**Dependency-Heavy Scripts** | Requires compilation or specific libraries. | Cloud Run Job | Decoupled; higher latency per call.  
**Small ML Models** | Requires specific hardware (e.g., GPU). | Vertex AI / Google Kubernetes Engine (GKE) | Specialized hardware; more complex setup.  
**High-Throughput Sweeps** | Thousands of independent simulations. | Cloud Batch | Managed scaling; no MPI support.  
**Scientific Simulations** | Computationally intensive; uses MPI. | HPC Cluster | Massively parallel; requires HPC expertise.  
  
### Two-stage extensible evaluator template

Use this template to decouple the evaluation process into two distinct stages: asynchronous launch and final scoring. This architecture allows the controller to manage multiple evaluation lifecycles efficiently.

#### Core abstraction: Launch and score
    
    
    from abc import ABC, abstractmethod
    from typing import Any, Dict
    
    class JobTicket:
        id: str
        metadata: Dict[str, Any]
    
    class Evaluator(ABC):
        @abstractmethod
        def launch_evaluation(self, program_candidate: str) -> JobTicket:
            """Launches the evaluation job asynchronously."""
            pass
    
        @abstractmethod
        def score_from_result(self, job_ticket: JobTicket) -> float:
            """Retrieves and scores the result from the job."""
            pass
    

#### Concrete implementations

Choose the evaluator implementation that matches your infrastructure requirements, latency constraints, and workload scale. The following sections detail the available concrete implementations:

##### LocalEvaluator (synchronous)

Use for zero-infrastructure, low-latency evaluation.
    
    
    import subprocess
    
    class LocalEvaluator(Evaluator):
        def launch_evaluation(self, program_candidate: str) -> JobTicket:
            # Launch locally within the process space
            result = subprocess.run([self.executable_path, program_candidate], capture_output=True, text=True)
            return JobTicket(id=str(hash(program_candidate)), metadata={})
    

##### CloudRunJobEvaluator (asynchronous)

Use for decoupled evaluation of containerized workloads.
    
    
    import uuid
    
    class CloudRunJobEvaluator(Evaluator):
        def launch_evaluation(self, program_candidate: str) -> JobTicket:
            job_id = str(uuid.uuid4())
            return JobTicket(
                id=f"alphaevolve-job-{job_id}", 
                metadata={"result_path": f"gs://{self.results_bucket}/{job_id}/result.txt"}
            )
    

##### CompilingHPCEvaluator (asynchronous)

Use for high performance computing requiring compiled binaries.
    
    
    class CompilingHPCEvaluator(Evaluator):
        def launch_evaluation(self, program_candidate: str) -> JobTicket:
            binary_path = f"{self.shared_fs_path}/binaries/{hash(program_candidate)}"
            return JobTicket(id="12345", metadata={"job_dir": "/path/to/job-12345"})
    

### Handling asynchronous completion

For asynchronous backends, use an event-driven architecture with Pub/Sub to notify the controller upon job completion.
    
    
    def process_completion(message):
        # Process incoming Pub/Sub message
        job_id = message.data.decode("utf-8")
        score = evaluator.score_from_result(pending_jobs.pop(job_id)["ticket"])
        alphaevolve_service.add_evaluation(candidate_id, score)
    

### Prohibited use cases and restrictions

To ensure the safety, security, and compliant operation of the system, AlphaEvolve contains hard structural guardrails.

#### Strict compliance and usage warning

AlphaEvolve is built in strict alignment with Google Cloud's Responsible AI tenets. The system is systematically restricted from processing, mutating, or generating code for the following domains:

  * **Bypassing cryptographic controls:** Any attempt to use the platform to reverse-engineer encryption layers, exploit cryptographic protocols, or bypass security authentication barriers is strictly prohibited.

  * **Malicious security research:** Generating adaptive or adversarial payloads, engineering automated vulnerability exploitation scripts, or developing software intended to cause unauthorized system disruption.

  * **Policy violations:** Any workload flagged for violating the core Gemini Enterprise terms of service will result in automated job termination and immediate account governance review.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
