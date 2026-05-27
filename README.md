# WorkforceConnect AWS Deployment

A production-style cloud-hosted registration application deployed on AWS using Flask, Amazon EC2, Amazon RDS MySQL, Gunicorn, NGINX, AWS Application Load Balancer (ALB), AWS WAF, Linux, and GitHub.

---

# Project Overview

This project demonstrates a real-world cloud deployment and security workflow by hosting a Python Flask application on AWS infrastructure with persistent MySQL database storage and enterprise-style traffic protection.

The application allows users to submit registration information through a live web form, which is then stored securely in an Amazon RDS MySQL database.

The project began as a traditional AWS web application deployment during Week 2 and later evolved into a more advanced production-style cloud security architecture during Week 3.

During the Week 3 security phase of the project, several enterprise-grade AWS networking and protection services were implemented including:

- AWS Application Load Balancer (ALB)
- AWS Web Application Firewall (WAF)
- SQL Injection protection testing
- NGINX reverse proxy
- Layer 7 traffic filtering
- Target group health checks
- Security group hardening
- AWS managed protection rule groups
- Reverse proxy traffic architecture
- Production-style request routing

---

# Project Progression — Week 2 to Week 3

## Week 2 — Initial Cloud Deployment

During Week 2, the focus of the project was deploying a working cloud-hosted application using AWS infrastructure.

The initial deployment included:

- Flask registration application
- Amazon EC2 compute instance
- Gunicorn production application server
- Amazon RDS MySQL database
- Linux server administration
- AWS security groups
- Database integration
- GitHub version control
- Public application hosting

At this stage, the application was fully functional and publicly accessible, but traffic was routed directly to the EC2 instance without advanced traffic inspection or enterprise security protections.

---

## Week 3 — Security & Networking Upgrade

During Week 3, the project architecture was upgraded to simulate a more realistic production cloud environment used by cloud engineers and cloud security teams.

Major infrastructure upgrades added during Week 3 included:

### Infrastructure Upgrades
- AWS Application Load Balancer (ALB)
- AWS Target Groups
- Health check monitoring
- NGINX reverse proxy
- Improved request routing architecture

### Security Upgrades
- AWS WAF deployment
- SQL injection filtering
- Layer 7 traffic inspection
- Managed AWS security rule groups
- Request filtering
- Traffic protection policies
- Hardened security group rules
- Malicious request blocking

These upgrades significantly improved the project's:

- Security posture
- Scalability
- Traffic management
- Architecture realism
- Production deployment structure

---

# Technologies Used

## Cloud & Infrastructure
- AWS EC2
- AWS RDS MySQL
- AWS Application Load Balancer (ALB)
- AWS WAF
- AWS VPC Networking
- AWS Target Groups
- AWS Security Groups

## Backend & Application
- Flask
- Gunicorn
- NGINX
- MySQL

## Operating System & Tools
- Linux (Amazon Linux 2023)
- Git & GitHub

---

# Cost & Resource Management

One of the major objectives of this project was building a production-style AWS environment while maintaining cost awareness and operating primarily within AWS Free Tier limits whenever possible.

During Week 3, additional enterprise networking, monitoring, logging, and security services were introduced. Some services remained free or Free Tier eligible, while others, such as AWS Application Load Balancer and AWS WAF, introduced small operational costs.

---

## AWS Service Cost Breakdown

| Service | Project Use | Estimated Cost |
|---|---|---|
| Amazon EC2 | Hosted the Flask web application on a Linux server | Free Tier Eligible |
| Amazon RDS MySQL | Stored registration form data in a managed MySQL database | Free Tier Eligible / Low Usage |
| AWS VPC | Provided the network foundation for public and private resources | No Additional Cost |
| AWS Security Groups | Controlled inbound and outbound traffic between services | No Additional Cost |
| AWS IAM | Managed roles, permissions, and least-privilege access | No Additional Cost |
| AWS Application Load Balancer (ALB) | Routed public HTTP traffic to the EC2 target group | Small Hourly Cost |
| AWS Target Groups | Connected the ALB to the backend EC2 instance | Included with ALB Usage |
| AWS WAF | Protected the application from SQL injection and malicious web requests | Small Monthly/Rule Cost |
| AWS CloudTrail | Logged AWS account activity and API events | Free Tier Eligible |
| Amazon S3 | Stored CloudTrail audit logs | Minimal Storage Cost |
| AWS CloudWatch Logs | Collected and monitored logs | Free Tier Eligible / Low Usage |
| CloudWatch Alarms | Alerted on security-related events | Free Tier Eligible for limited alarms |
| AWS SNS | Sent email notifications for alerts | Free Tier Eligible |
| GitHub | Stored source code, screenshots, and project documentation | Free |

---

## Estimated Week 3 Cost Awareness

The project was designed to stay low-cost while still using realistic cloud engineering services.

Estimated cost considerations included:

- EC2 usage remained low due to lightweight application hosting
- RDS usage remained minimal because the database only stored test registration records
- CloudTrail and CloudWatch stayed within low-volume logging usage
- S3 storage costs remained minimal because CloudTrail logs were small
- ALB introduced a small hourly cost because it continuously routes traffic
- AWS WAF introduced the most noticeable Week 3 cost because Web ACLs and managed rule groups can create charges
- GitHub documentation and version control had no cloud infrastructure cost

---

## Cost Control Measures Implemented

To avoid unnecessary AWS charges during development and testing, the following cost management practices were used:

- Monitored AWS Billing Dashboard during the project
- Used AWS Free Tier eligible resources whenever possible
- Kept the application lightweight with low traffic volume
- Avoided unnecessary scaling or large compute resources
- Used only required AWS WAF managed rule groups
- Limited testing traffic to basic validation requests
- Avoided high-volume load testing
- Kept RDS usage small and limited to project data
- Used CloudTrail and CloudWatch for basic monitoring without excessive log generation
- Reviewed ALB and WAF usage because those services can create active charges
- Documented resources used so they could be reviewed or removed after testing

---

## Cloud Resources Utilized

### Compute Resources
- Amazon EC2 Linux instance
- Gunicorn production application server
- NGINX reverse proxy server

### Database Resources
- Amazon RDS MySQL database
- Private subnet database architecture
- Application-to-database connectivity validation

### Networking Resources
- AWS VPC
- Public subnet
- Private subnet
- AWS Security Groups
- AWS Application Load Balancer
- AWS Target Groups
- HTTP traffic routing
- Backend target health checks

### Security Resources
- AWS WAF
- AWS IAM
- Least-privilege permission concepts
- SQL injection filtering
- Layer 7 request inspection
- AWS managed security rule groups
- Security group hardening
- Controlled HTTP and SSH access

### Monitoring & Logging Resources
- AWS CloudTrail
- Amazon S3 log storage
- AWS CloudWatch Logs
- CloudWatch metric filters
- CloudWatch alarms
- AWS SNS email notifications

### Development & Documentation Resources
- Git
- GitHub
- README documentation
- Project screenshots
- Linux terminal commands
- Application deployment files

---

## Resource Cleanup Considerations

Because this project used services that may continue billing while active, the following resources should be reviewed after project completion:

- Application Load Balancer
- AWS WAF Web ACL
- EC2 instance
- RDS database
- CloudWatch alarms
- CloudWatch log groups
- S3 CloudTrail log bucket
- Target groups
- Unused security groups

This helps prevent unnecessary charges after testing and documentation are complete.

---

# Live Application

The WorkforceConnect application is publicly accessible through an AWS Application Load Balancer.

### WorkforceConnect Registration Form
![Live App](screenshots/workforceconnect-app-running.png)

---

# Initial AWS Deployment Validation (Week 2)

These screenshots demonstrate the original AWS deployment infrastructure built during Week 2 of the project.

---

## Gunicorn Production Service Running

Gunicorn was configured as the production application server for the Flask application.

![Gunicorn Running](screenshotsgunicorn-running.png)

---

## AWS RDS Database Created

Amazon RDS MySQL was configured to provide persistent cloud-hosted database storage.

![RDS Database](screenshots_rds-created.png)

---

## Database Validation Query

Successful database connectivity validation between the Flask application and Amazon RDS MySQL.

![MySQL Query](screenshots_mysql-query.png)

---

## GitHub Deployment Validation

GitHub repository used for source control, deployment tracking, and infrastructure documentation.

![GitHub Push](screenshots_github-push.png)

---

# Security Enhancements (Week 3)

This phase of the project focused on implementing enterprise-style security controls and production networking architecture within AWS.

Security improvements added:

- AWS Application Load Balancer (ALB)
- AWS WAF (Web Application Firewall)
- SQL Injection protection testing
- Layer 7 traffic filtering
- AWS managed security rule groups
- Target group health checks
- NGINX reverse proxy validation
- HTTP traffic control through security groups
- Production-style request routing
- Malicious request filtering
- Reverse proxy traffic management

---

# Load Balancer & Traffic Routing Validation

The following validations were performed after implementing the AWS Application Load Balancer architecture.

## Load Balancer Validation
- Verified ALB successfully routed traffic to EC2 target
- Confirmed target group health checks passed
- Verified public application accessibility through ALB DNS
- Verified NGINX reverse proxy communication
- Confirmed production-style request forwarding

---

## AWS Application Load Balancer Active

AWS ALB configured successfully and actively routing traffic to backend infrastructure.

![ALB Active](screenshots/alb-active.png)

---

## Healthy Target Group Validation

AWS health checks confirmed the EC2 instance was healthy and properly communicating behind the Application Load Balancer.

![Healthy Target](screenshots/alb-healthy-target.png)

---

## NGINX Reverse Proxy Running

NGINX configured successfully as a reverse proxy between the AWS Application Load Balancer and Gunicorn application server.

![NGINX Running](screenshots/nginx-running.png)

---

## Security Group Rules Configuration

Security groups configured to allow controlled inbound HTTP and SSH traffic while restricting unnecessary access.

![Security Group Rules](screenshots/security-group-rules.png)

---

# AWS WAF Protection Validation

AWS WAF was deployed using AWS-managed protection rule groups to inspect and filter malicious web traffic.

The following protections were implemented:

- SQL injection filtering
- Bad input protection
- Layer 7 request inspection
- Bot traffic protection
- AWS managed DDoS protections
- Request filtering policies
- Malicious traffic blocking

---

## AWS WAF Protection Enabled

AWS WAF successfully deployed and associated with the AWS Application Load Balancer.

![WAF Enabled](screenshots/waf-protection-enabled.png)

---

## SQL Injection Attempt Blocked

A simulated SQL injection-style request was tested against the application through the ALB endpoint.

Payload tested:

```bash
?id=1%20OR%201=1
