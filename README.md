# Hi, I'm Malik Dixon 👋

### AI Systems | Cloud Engineering | DevOps | DevSecOps

I design and build secure, scalable, and automated technology systems across cloud infrastructure, DevSecOps, and applied artificial intelligence.

My work sits at the intersection of:

- Cloud architecture and infrastructure automation
- Secure CI/CD and software delivery
- AI agents, RAG, and workflow automation
- Cloud security, governance, and compliance
- Observability, reliability, and operational resilience

I focus on building systems that are not merely functional, but secure, maintainable, observable, and production-ready.

Secure it. Automate it. Observe it. Scale it.

---

## About Me

I am a U.S. Army veteran and technology professional with more than 25 years of experience learning, building, troubleshooting, and improving technical systems.

My current focus combines traditional cloud engineering with emerging AI capabilities. I am particularly interested in how organizations can safely integrate AI agents, automation, retrieval systems, and autonomous workflows while maintaining security, human oversight, and operational control.

My approach emphasizes:

- Security by design
- Infrastructure as Code
- Human oversight for high-impact AI actions
- Least-privilege access
- Repeatable deployment processes
- Clear documentation
- Continuous validation
- Cost-aware cloud engineering

I follow a Build–Verify–Destroy approach for cloud labs and experiments to validate solutions while controlling unnecessary infrastructure costs.

---

## What I Work On

- Cloud infrastructure design and deployment
- CI/CD pipeline automation
- Infrastructure as Code with Terraform and CloudFormation
- Containerized application delivery
- Security controls in DevOps pipelines
- Monitoring, logging, and operational visibility
- Identity, access, and secrets management

---

## Tech Stack

### Cloud

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)

### DevOps & IaC

![Terraform](https://img.shields.io/badge/Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)
![CloudFormation](https://img.shields.io/badge/CloudFormation-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

### Security & DevSecOps

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=trivy&logoColor=white)

---

## Featured Projects

### 1. Operation Aegis: Docker-Driven DevSecOps Security Pipeline  
**DSB Capstone Project**

Built a Docker-based DevSecOps pipeline for a simulated fintech platform, using GitHub Actions to automate security checks from pull request to staging deployment.

**What it does**
- Runs Dockerized unit, integration, smoke, and DAST testing
- Automates SAST, SCA, secrets scanning, and IaC/config scanning
- Enforces PR gates, staging validation, and nightly security audits
- Separates production and test images for safer deployment workflows
- Builds security directly into CI/CD to support faster, safer releases

**Skills demonstrated:** Docker, GitHub Actions, DevSecOps, CI/CD, SAST, DAST, SCA, secure deployment workflows

**Repo:** [operation-aegis](https://github.com/mdixon47/operation-aegis)  
**Story:** [How I Built a Docker-Tested DevSecOps Pipeline in GitHub Actions](https://mdixondev62.hashnode.dev/how-i-built-a-docker-tested-devsecops-pipeline-in-github-actions)

---

### 2. AuditTrail SDK: AWS Compliance Auditor with No Static Keys  
**DSB Capstone Project**

Built an AWS compliance auditing tool that inventories cloud resources, uses temporary credentials only, logs every API call, and exposes audit results through an API validated with Postman.

**What it does**
- Inventories AWS resources including EC2, EBS, S3, and Lambda
- Uses GitHub Actions OIDC and IAM roles instead of static AWS keys
- Provisions infrastructure with Terraform
- Handles AWS API throttling with retry logic, pacing, and backoff
- Emits structured JSON logs for every AWS API call
- Stores compliance findings for review and reporting
- Provides API endpoints for triggering audits and retrieving results

**Problems solved**
- Security Hub `AccessDeniedException`
- S3 public access permission issues
- DynamoDB GSI permission errors
- AWS `Describe*` actions requiring `Resource: "*"`
- OIDC and IAM bootstrapping for Terraform CI/CD

**Skills demonstrated:** AWS, IAM, Terraform, Python, boto3, API security, compliance automation, GitHub Actions OIDC

**Repo:** [audittrail-sdk](https://github.com/mdixon47/audittrail-sdk)  
**Story:** [I Built an AWS Compliance Auditor That Uses No Static Keys — and AWS Still Fought Me](https://mdixondevsecops2.hashnode.dev/i-built-an-aws-compliance-auditor-that-uses-no-static-keys)

---

### 3. Project Sentinel: Self-Healing Cloud Security Automation  
**DSB Capstone Project**

Built a cloud-native security automation system that detects events, responds with serverless remediation, and provides visibility through logging, alerts, and dashboards.

**What it does**
- Detects security events using event-driven AWS monitoring
- Responds automatically with serverless remediation workflows
- Uses CloudTrail, EventBridge, Lambda, and CloudWatch for visibility and response
- Applies governance through Infrastructure as Code and Policy as Code
- Uses GitHub Actions to validate Terraform, scan for misconfigurations, and enforce checks before deployment

**Key takeaway**

Security is strongest when detection, remediation, observability, and governance work as one connected system. Detection without remediation creates noise. Remediation without observability creates blind spots.

**Skills demonstrated:** AWS, Terraform, GitHub Actions, CloudTrail, EventBridge, Lambda, CloudWatch, policy enforcement, DevSecOps automation

**Repo:** [project-sentinel-terraform](https://github.com/mdixon47/project-sentinel-terraform)  
**Story:** [Project Sentinel: Building a Self-Healing Cloud Security System](https://projectsentineldevsecops.hashnode.dev/project-sentinel-building-a-self-healing-cloud-security-system-a-dsb-cap)

---

### 4. CloudMart Secure Web Assets Pipeline  
**Level Up In Tech Academy Project**

Expanded a cloud support lab into a DevSecOps-style deployment pipeline for an e-commerce website experiencing broken product images and S3 `AccessDenied` errors.

**What it does**
- Deploys S3 static website infrastructure with AWS CloudFormation
- Uses GitHub Actions for validation, deployment, and asset syncing
- Adds security gates with `cfn-lint`, Checkov, and Snyk
- Applies least-privilege IAM thinking to public website assets
- Runs post-deployment checks to confirm the homepage and product images return HTTP 200
- Includes monitoring plans for uptime, response status, deployment health, and error rate
- Documents security exceptions, validation reports, and troubleshooting evidence

**Key takeaway**

A cloud engineer does not just fix access issues. A cloud engineer designs a system that prevents the same access problem from coming back.

**Skills demonstrated:** AWS S3, CloudFormation, GitHub Actions, IAM, Checkov, Snyk, cfn-lint, static website hosting, DevSecOps validation

**Repo:** [aws-cloudmart-secure-web-assets](https://github.com/mdixon47/aws-cloudmart-secure-web-assets)  
**Story:** [From S3 AccessDenied to DevSecOps](https://s3accessdeniedtodevsecops.hashnode.dev/from-s3-accessdenied-to-devsecops-building-the-cloudmart-secure-web-assets-pipeline)

---

## Current Focus

- Strengthening cloud security engineering skills
- Building production-style DevOps/DevSecOps portfolio projects
- Expanding expertise in platform automation and reliability
- Exploring scalable cloud architecture patterns

---

## Certifications & Learning

- AWS Certified Cloud Practitioner
- Azure
- DevOps Engineering
- DevSecOps Practices
- Cloud Security
- Infrastructure as Code

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

## Active Contributions

Proud to share that I'm now an active contributor to **The DevSec Blueprint (DSB)**. Excited to keep learning, building, improving, and contributing meaningful work to the project.

**Repo:** [The DevSec Blueprint (DSB)](https://github.com/devsecblueprint/devsecblueprint?tab=readme-ov-file)

---

## Connect With Me

- GitHub: [https://github.com/mdixon47](https://github.com/mdixon47)
- LinkedIn: [https://www.linkedin.com/in/malik-dixon/](https://www.linkedin.com/in/malik-dixon/)

---

## Profile Motto

**Secure it. Automate it. Scale it.**
