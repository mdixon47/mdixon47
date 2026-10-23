# Hi, I'm Malik Dixon 👋

### AI Systems & Workflow Consultant | Secure AI Automation | AWS | DevSecOps | Cloud Security

I help businesses turn repetitive work into practical AI applications and automated workflows, with clear permissions, human approval for consequential actions, and evidence that the work was completed.

I design and build these systems using AI agents, cloud infrastructure, automation, and security-first engineering.

My work focuses on turning AI from an isolated tool into an operational system—one that can be evaluated, governed, observed, and safely connected to business processes.

**Secure it. Automate it. Observe it. Scale it.**

---

## About Me

I am a U.S. Army veteran and technology professional with more than 25 years of experience learning, building, troubleshooting, and improving technical systems.

Today, I work at the intersection of:

- AI agents, RAG, MCP, and workflow automation
- AWS and Azure cloud architecture
- DevOps and DevSecOps delivery pipelines
- Agent identity, delegated authority, and runtime authorization
- Observability, evaluation, governance, and human oversight

I build systems that are secure, maintainable, observable, cost-aware, and designed for real operational use—not just demonstrations.

---

## Current Projects & Stages

*Profile refreshed: October 23, 2026. Stages distinguish live products, working prototypes, and planned work.*

| Project | Stage | Current Focus |
| --- | --- | --- |
| [**TraceLogicAI**](https://tracelogicai.com) | **Live Product · Active Development** | Comparing Plain, RAG, MCP, Agent, and Security-aware pipelines; evaluation scoring; trace evidence; remediation; runtime assurance; and agent permission/data-access governance. |
| **CatchRailAI** | **Working Beta · Validation** | A purchase-order and RFQ safety net that detects, classifies, extracts, verifies, escalates, and tracks exceptions with human approval and audit history. |
| **Agent Sandbox Runtime** | **Infrastructure Prototype** | Restricted AI-agent execution on AWS ECS Fargate using Terraform, Docker, network isolation, policy controls, observability, and an automated kill switch. Private build. |
| **SEIR** | **Architecture & Terraform Implementation** | A serverless AWS security orchestration and response platform using deterministic controls, EventBridge orchestration, WAF telemetry, Cognito, and Amazon Bedrock for explanation—not authorization. |
| **RevenuePilotAI** | **Functional Prototype** | A supervisor coordinating five specialist agents for account research, product-knowledge RAG, deal analysis, outreach drafts, and human-approved CRM updates. |
| [**Kubernetes Dev Lab**](https://github.com/mdixon47/k8s-dev-lab) | **Hands-on Lab & Learning Resources** | A reproducible kubeadm cluster with FastAPI/Postgres, an nginx edge, OPA Gatekeeper policies, security test routines, and Gateway API exercises using Envoy Gateway and Istio. |
| [**n8n Local Automation Toolkit**](https://github.com/mdixon47/n8n-local) | **Active Development** | Docker-based workflow tooling with version-pinned installs, backup verification, restore safeguards, health checks, controlled upgrades, and a searchable template gallery. |
| **ListenDirect** | **Concept & Architecture Validation** | A low-latency speech-to-speech agent with streaming, interruption handling, barge-in, and OpenAI Realtime-compatible interfaces. |
| [**Project Sentinel**](https://github.com/mdixon47/project-sentinel-terraform) | **Completed · Maintained** | Event-driven AWS security detection, automated remediation, alerting, retry/DLQ handling, observability, and Terraform-based governance. |

### Next Project Track

**Secure Kubernetes Agent Platform — Planning**

A cloud-native platform for running AI and coding agents as governed workloads, with an AI gateway, MCP gateway, workload identity, end-to-end tracing, per-tool authorization, and isolated execution environments. AWS/EKS is the initial reference architecture, with Azure and GCP variants planned.

---

## What I Build

- Business workflows for inquiry intake, lead follow-up, inbox triage, content preparation, and operational handoffs
- Secure AI agents, RAG systems, and MCP-enabled workflows
- Evaluation pipelines and CI quality gates for AI applications
- Human-approved automation for high-impact business actions
- Cloud infrastructure with Terraform and CloudFormation
- CI/CD pipelines with SAST, DAST, SCA, secrets, container, and IaC scanning
- Agent identity, least-privilege permissions, and runtime policy enforcement
- Monitoring, logging, cost tracking, and operational dashboards
- Responsive applications, APIs, dashboards, and workflow tools

---

## Recent Practical Work

### Kubernetes Security & Gateway Learning Lab

[k8s-dev-lab](https://github.com/mdixon47/k8s-dev-lab) combines three Ubuntu 26.04 Kubernetes nodes with a separate nginx edge VM and a FastAPI/Postgres sample application. It includes a 30-lesson Kubernetes course and a ten-lesson Gateway API course comparing Envoy Gateway and Istio.

The security exercises cover admission controls, RBAC, Pod Security, image scanning, network-policy behavior, and operational verification. Gatekeeper policies include privilege restrictions, non-root and resource-limit checks, plus an approved-registry exercise using Chainguard images. Some controls intentionally begin in warning mode so learners can observe violations before enforcing them.

### Reliable Local Workflow Automation

[n8n-local](https://github.com/mdixon47/n8n-local) adds operational safeguards around a self-hosted Docker installation: installer review and hashing, explicit version selection, consistent SQLite backups, snapshot verification before restore, and health checks after upgrades. Recent improvements include backup-growth reporting, controlled patch updates, and corrected snapshot ordering across macOS and Linux.

The template gallery supports workflow discovery and import with missing-node warnings. The project also documents approval requirements for write-capable agent tools and treating retrieved email, web, and document content as untrusted input.

### AI Architecture Comparison

[mcp-rag-agent-demo](https://github.com/mdixon47/mcp-rag-agent-demo) provides a Nuxt 3, TypeScript, and Tailwind CSS demo platform for comparing MCP, RAG, and agent approaches. This complements my broader work on making AI architecture choices understandable and measurable.

---

## Selected Completed Projects

### Operation Aegis — Docker-Driven DevSecOps Pipeline

Built a Docker-based security pipeline for a simulated fintech platform. GitHub Actions runs unit, integration, smoke, SAST, DAST, SCA, secrets, and infrastructure checks from pull request through staging validation.

**Stack:** Docker · GitHub Actions · DevSecOps · CI/CD · SAST · DAST · SCA  
**Repository:** [operation-aegis](https://github.com/mdixon47/operation-aegis)  
**Case study:** [How I Built a Docker-Tested DevSecOps Pipeline](https://mdixondev62.hashnode.dev/how-i-built-a-docker-tested-devsecops-pipeline-in-github-actions)

### AuditTrail SDK — AWS Compliance Auditor Without Static Keys

Built an AWS compliance auditing tool that inventories cloud resources, uses temporary credentials, records structured API evidence, and exposes findings through an API.

**Stack:** AWS · IAM · Terraform · Python · boto3 · GitHub Actions OIDC  
**Repository:** [audittrail-sdk](https://github.com/mdixon47/audittrail-sdk)  
**Case study:** [I Built an AWS Compliance Auditor That Uses No Static Keys](https://mdixondevsecops2.hashnode.dev/i-built-an-aws-compliance-auditor-that-uses-no-static-keys)

### Project Sentinel — Self-Healing Cloud Security Automation

Built a cloud-native system that detects AWS security events, performs controlled serverless remediation, and provides evidence through CloudTrail, EventBridge, Lambda, CloudWatch, SNS, X-Ray, retries, and dead-letter queues.

**Stack:** AWS · Terraform · Lambda · EventBridge · CloudTrail · CloudWatch · GitHub Actions  
**Repository:** [project-sentinel-terraform](https://github.com/mdixon47/project-sentinel-terraform)  
**Case study:** [Building a Self-Healing Cloud Security System](https://projectsentineldevsecops.hashnode.dev/project-sentinel-building-a-self-healing-cloud-security-system-a-dsb-cap)

### CloudMart — Secure Web Assets Pipeline

Expanded an S3 troubleshooting lab into a repeatable DevSecOps deployment pipeline with CloudFormation, GitHub Actions, security gates, post-deployment HTTP checks, and documented remediation evidence.

**Stack:** AWS S3 · CloudFormation · GitHub Actions · IAM · Checkov · Snyk · cfn-lint  
**Repository:** [aws-cloudmart-secure-web-assets](https://github.com/mdixon47/aws-cloudmart-secure-web-assets)  
**Case study:** [From S3 AccessDenied to DevSecOps](https://s3accessdeniedtodevsecops.hashnode.dev/from-s3-accessdenied-to-devsecops-building-the-cloudmart-secure-web-assets-pipeline)

---

## Technology Stack

### AI & Application Development

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Nuxt.js](https://img.shields.io/badge/Nuxt.js-00DC82?style=for-the-badge&logo=nuxtdotjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)

### Cloud, DevOps & Infrastructure

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

### Security & Assurance

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=aqua&logoColor=white)

---

## Engineering Principles

- **Deterministic controls for security decisions:** models may explain findings, but policy and authorization determine whether actions proceed.
- **Verify before execution:** identity, delegated authority, purpose, resource, context, and current permission must be checked before a tool call or state-changing action.
- **Human oversight based on impact:** actions that move money, issue refunds, change customer obligations, or make external commitments need a clear human approval boundary.
- **Approval must match the action:** record who approved what, preserve the approved payload, and check that the authorization still applies when execution begins.
- **Verify outcomes before retrying:** a workflow timeout does not prove an action failed. Check the destination system before retrying a write, and keep uncertain outcomes visible.
- **Evidence across the execution chain:** prompt → plan → tool call → command → system activity → result → verification.
- **Build–Verify–Destroy:** cloud labs are validated and then removed to control cost and reduce unnecessary exposure.

---

## Current Focus

- Turning AI into trusted, measurable business workflows
- Building evaluation, remediation, and governance systems for AI applications
- Securing agent tools, data access, delegated authority, and runtime execution
- Making workflow handoffs explicit: what happened, who owns the next step, and how completion is verified
- Testing Kubernetes admission policies, approved image sources, and gateway behavior in reproducible labs
- Improving n8n workflow reliability through backup drills, health checks, and controlled updates
- Expanding production-style AWS, DevOps, and DevSecOps implementations
- Preparing for AWS AI Practitioner and AWS Developer Associate certifications

---

## GitHub Metrics

<p align="center">
  <img src="./profile/stats.svg" height="170" alt="Malik Dixon's GitHub stats" />
  <img src="./profile/top-langs.svg" height="170" alt="Malik Dixon's top languages" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/followers/mdixon47?style=for-the-badge&label=Followers" alt="GitHub followers" />
  <img src="https://img.shields.io/github/stars/mdixon47?affiliations=OWNER&style=for-the-badge&label=Stars" alt="GitHub stars" />
</p>

> Metrics are generated daily by GitHub Actions and stored in this repository.

---

## Community & Contributions

I contribute to **The DevSec Blueprint (DSB)**, with a focus on practical walkthroughs, technical content, cloud security, and DevSecOps learning. My lab documentation emphasizes prerequisites, bounded hands-on exercises, expected results, and verification.

**Community repository:** [The DevSec Blueprint](https://github.com/devsecblueprint/devsecblueprint?tab=readme-ov-file)

---

## Connect With Me

- [LinkedIn](https://www.linkedin.com/in/malik-dixon/)
- [GitHub](https://github.com/mdixon47)
- [TraceLogicAI](https://tracelogicai.com)

---

### Turning AI into trusted, measurable business workflows.
