# WorkforceConnect AWS Deployment

A production-style cloud-hosted registration application deployed on AWS using Flask, Amazon EC2, Amazon RDS MySQL, Gunicorn, NGINX, AWS Application Load Balancer (ALB), AWS WAF, Linux, and GitHub.

---

# Project Overview

This project demonstrates a real-world cloud deployment and security workflow by hosting a Python Flask application on AWS infrastructure with persistent MySQL database storage and enterprise-style traffic protection.

The application allows users to submit registration information through a live web form, which is then stored securely in an Amazon RDS MySQL database.

During the security phase of the project, additional production-grade AWS networking and security controls were implemented including:

- Application Load Balancer (ALB)
- AWS Web Application Firewall (WAF)
- SQL Injection protection testing
- NGINX reverse proxy
- Layer 7 traffic filtering
- Target group health checks
- Security group hardening

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

# Live Application

The WorkforceConnect application is publicly accessible through an AWS Application Load Balancer.

### WorkforceConnect Registration Form
![Live App](screenshots/workforceconnect-app-running.png)

---

# Initial AWS Deployment Validation

### Gunicorn Production Service Running
![Gunicorn Running](screenshotsgunicorn-running.png)

### AWS RDS Database Created
![RDS Database](screenshots_rds-created.png)

### Database Validation Query
![MySQL Query](screenshots_mysql-query.png)

### GitHub Deployment Validation
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

---

# Security Validation Performed

The following security validation tests were completed during the project:

## Load Balancer Validation
- Verified ALB successfully routed traffic to EC2 target
- Confirmed target group health checks passed
- Verified public application accessibility through ALB DNS

## WAF Protection Validation
A SQL injection style payload was tested against the application:

```bash
?id=1%20OR%201=1
