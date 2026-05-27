# WorkforceConnect AWS Deployment & Security Upgrade

A production-style cloud engineering and cloud security project built on AWS using Flask, Amazon EC2, Amazon RDS MySQL, Gunicorn, NGINX, AWS Application Load Balancer (ALB), AWS WAF, Linux, and GitHub.

This project evolved from a basic cloud-hosted Flask application in Week 2 into a more secure, production-style AWS architecture in Week 3 by introducing enterprise networking, traffic filtering, and web application security protections.

---

# Project Evolution — Week 2 to Week 3

## Week 2 — Initial Cloud Deployment

During Week 2, the primary objective was deploying a functioning full-stack cloud application inside AWS infrastructure.

The project originally included:

- Flask registration application
- Amazon EC2 hosting
- Gunicorn production server
- Amazon RDS MySQL database
- Linux server administration
- Security group configuration
- GitHub source control
- Database connectivity validation

At this stage, the application was functional and publicly accessible, but it lacked enterprise-grade traffic management and web security protections.

---

## Week 3 — Security & Production Architecture Upgrade

In Week 3, the project was upgraded to simulate a more realistic production cloud environment by adding advanced networking and security components.

Major upgrades included:

### Infrastructure Upgrades
- Added AWS Application Load Balancer (ALB)
- Added AWS Target Groups
- Configured health checks
- Added NGINX reverse proxy layer
- Improved request routing architecture

### Security Upgrades
- Added AWS WAF (Web Application Firewall)
- Implemented SQL injection protection
- Added AWS managed security rule sets
- Added Layer 7 traffic filtering
- Added malicious request blocking
- Hardened security group rules
- Implemented HTTP request inspection

### Security Testing
The application was tested against simulated malicious traffic to validate protection mechanisms.

A SQL injection-style request was sent through the load balancer:

```bash
?id=1%20OR%201=1
A SQL injection style payload was tested against the application:

```bash
?id=1%20OR%201=1
