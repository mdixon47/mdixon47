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
**Story:** [I Built an AWS Compliance Auditor That Uses No Static Keys — and AWS Still Fought Me](https://mdixondevsecops2.hashnode.dev/i-built-an-aws-compliance-auditor-that-uses-no-static-keys-and-aws-still-fought-me)

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

Security is strongest when detection, remediation, observability, and governance work as one connected system. Detection without remediation creates noise. Remediation without observability creates blind spots. Governance without automation does not scale.

**Skills demonstrated:** AWS, Terraform, GitHub Actions, CloudTrail, EventBridge, Lambda, CloudWatch, policy enforcement, DevSecOps automation

**Repo:** [project-sentinel-terraform](https://github.com/mdixon47/project-sentinel-terraform)  
**Story:** [Project Sentinel: Building a Self-Healing Cloud Security System](https://projectsentineldevsecops.hashnode.dev/project-sentinel-building-a-self-healing-cloud-security-system-a-dsb-capstone-in-cloud-native-security-automation)

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
