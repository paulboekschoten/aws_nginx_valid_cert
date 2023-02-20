#!/usr/bin/env python3

from diagrams import Cluster, Diagram
from diagrams.aws.general import User
from diagrams.aws.compute import EC2
from diagrams.aws.network import Route53

with Diagram("EC2 instance with nginx", show=False):
    user = User("User")
    
    with Cluster("Default VPC"):
        ec2 = EC2("Webserver")

    dns = Route53("dns")

    user >> dns >> ec2