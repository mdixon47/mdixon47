# Hi, I'm Malik Dixon 👋

### Cloud Engineering | DevOps | DevSecOps

I build secure, scalable, and automated cloud solutions with a focus on reliability, security, and clean delivery pipelines. My interests sit at the intersection of **cloud infrastructure, CI/CD, infrastructure as code, observability, and security-first engineering**.

I enjoy designing systems that are not just functional, but resilient, maintainable, and production-ready.

---

## About Me

- Cloud-focused engineer with interests in **AWS, Azure, DevOps, and DevSecOps**
- Passionate about **automation, security, infrastructure as code, and platform reliability**
- Interested in building solutions that improve **developer experience, governance, and deployment speed**
- Continuously learning and exploring modern cloud-native tooling and best practices

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

### Security & Ops
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## Featured Projects

### 1. Operation Aegis: Docker-Driven DevSecOps Security Pipeline  
**DSB Capstone Project**  
Built a GitHub Actions-based DevSecOps pipeline for a simulated fintech platform, using Docker across every testing stage to automate security checks from pull request to staging deployment.

**Highlights**
- Dockerized unit, integration, smoke, and DAST testing
- Automated SAST, SCA, secrets scanning, and IaC/config scanning
- GitHub Actions workflows for PR gates, staging validation, and nightly audits
- Production and test image separation for cleaner, safer deployments
- Security enforcement built directly into CI/CD for faster, safer releases

**Repo:** [operation-aegis](https://github.com/mdixon47/operation-aegis)
**Story** [operation-aegis](https://mdixondev62.hashnode.dev/how-i-built-a-docker-tested-devsecops-pipeline-in-github-actions)

### 2. I Built an AWS Compliance Auditor That Uses No Static Keys — and AWS Still Fought Me
**DSB Capstone Project**
A DSB capstone project that inventories AWS compute and storage resources using boto3, authenticates with temporary credentials only, handles API throttling with retries and pacing, emits structured logs for every AWS API call, stores compliance findings, and exposes an API that can be validated with Postman.

**Highlights**
- Built AuditTrail SDK, a DSB capstone project for secure AWS compliance auditing
- Used Terraform to provision the full environment and keep it visible in the AWS Console
- Used boto3 to inventory AWS resources such as EC2, EBS, S3, and Lambda
- Enforced temporary credentials only with GitHub Actions OIDC and role-based access
- Avoided static AWS keys completely
- Added retry logic, pacing, and backoff to handle API throttling safely
- Implemented structured JSON logging for every API call
- Created the ability to audit the audit through logging and cloud-side visibility
- Added API endpoints for triggering audits and retrieving results
- Integrated Postman for API validation and operational testing
- Stored compliance findings for review and reporting
- Solved real-world IAM and deployment issues, including:
- Security Hub AccessDeniedException
- corrected s3:GetBucketPublicAccessBlock permission
- DynamoDB GSI index permissions
- Describe* actions requiring Resource: "*"
- OIDC IAM bootstrapping for Terraform CI/CD
- Demonstrated practical skills in AWS, IAM, Terraform, Python, API security, and DevSecOps

**Repo:** [Project Repo](https://github.com/mdixon47/audittrail-sdk)
**Story** [The Story](https://mdixondevsecops2.hashnode.dev/i-built-an-aws-compliance-auditor-that-uses-no-static-keys-and-aws-still-fought-me)

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

## Connect With Me

- GitHub: [https://github.com/mdixon47]
- LinkedIn: [https://www.linkedin.com/in/malik-dixon/]
---

## Profile Motto

**Secure it. Automate it. Scale it.**

---
