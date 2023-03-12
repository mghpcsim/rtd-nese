NESE Services
==================

Historically, the MGHPCC has provided co-location services for its member institutes only including
power, space, cooling, and networking. However, over the last few years, MGHPCC and its member
institutes are starting to explore the concept of operating joint services across the whole
consortium. NESE is one such effort and is positioned to be the backbone of shared storage services
for the facility.  The success of NESE is allowing us to build other infrastructure on
top of it, such as `the New England Research Cloud (NERC) <https://nerc.mghpcc.org/>`_ -- 
a large multi-institutional OpenStack/OpenShift environment funded through partnerships 
between Harvard University, Boston University, Mass Tech Collaborative, and RedHat, Inc.

NESE currently provides two services, NESE Disk and NESE Tape. NESE Disk provides block storage
that can be mounted on a physical or virtual machine across institutional boundaries and then
exported via standard NAS prototocls, such as NFS or SMB. NESE Tape provides archival storage
services at a much lower cost per TB than disk-based services.


NESE Disk (Block Storage)
-------------------------

NESE Disk provides block storage as a service built on top of `Ceph <https://ceph.io/>`_. 
Ceph was chosen because it provides a single storage system to manage that offers multiple
storage types and access mechanisms including file (CephFS), block (RBD), and object (S3). 
It is also open source software that provides erasure coding for resilency, which has many
advantages over traditional RAID volumes when working with very large drive and volume sizes.

While CephFS is arguably the most performant, as each end-point is a Ceph Client that can
access the backend OSN disks directory without the bottleneck of doing through a Rados gateway (RGW)
server, it was not chosen as a target capability. Access controls for CephFS are tied to the
local identity provider and as this service is provided across institutional (and IAM) boundaries,
CephFS was just not feasible.  

After a year of service, we decided the best long-term vision of NESE as a
data storage provider would be that of a platform that provides something more akin to
a data lake, and not fast direct attached storage to an HPC cluster, as each of the
institutions already had this service. 

At this time, NESE is not supporting the S3 protocol. If you are interested in S3 file services,
`Open Storage Network (OSN) <https://www.openstoragenetwork.org>`_ provides this as a free service
for NSF PIs up to 50 TB and larger allocations are available with hardware purchases. 
For getting access to an OSN bucket, see the `OSN allocations documentation <https://openstoragenetwork.readthedocs.io/en/latest/allocations.html#allocations>`_ for more information.

If you are interested in purchasing NESE Disk storage services, contact ???

NESE Tape
---------


