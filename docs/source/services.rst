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

If you are affiliated with one of the institutions below, follow the appropriate link to contact 
your local research computing support group to get started with NESE.

* `Boston University <http://www.bu.edu/tech/support/research>`_
* `Harvard University <https://rc.fas.harvard.edu/>`_
* `Massachusetts Institute of Technology <http://researchcomputing.mit.edu/facilities/mghpcc>`_
* `Northeastern University <http://northeastern.edu/rc>`_
* `University of Massachusetts <https://www.umassrc.org/>`_
* `University of Rhode Island <https://its.uri.edu/research-computing/uri-mghpcc/>`_

NESE Disk (Block Storage)
-------------------------
NESE Disk provides block storage as a service built on top of `Ceph <https://ceph.io/>`_. 
Ceph was chosen because it provides a single storage system to manage that offers multiple
storage types and access mechanisms including file (CephFS), block (RBD), and object (S3). 
It is also open source software that provides erasure coding for resilency, which has many
advantages over traditional RAID volumes when working with very large drive and volume sizes.

While CephFS is arguably the most performant, as each end-point is a Ceph Client that can
access the backend OSD disks directory without the bottleneck of doing through a Rados gateway (RGW)
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


NESE Tape
---------

Building on top of the success of NESE Disk, we began investigating a NESE storage tier capable
of growing to the exascale capacity over the next few years. 
We investigated technologies including traditional spinning disk drives,
optical disk drives, magnetic tape, SSD and even exotic technologies like DNA storage.
When looking at expected trends of bit density, tape is expected to continue to improve in a
Moore’s law fashion for many years with many doublings, while HDD density increases
are much more difficult technologically. Because of this, it’s generally expected that the
per terabyte cost advantage for tape compared to HDD will continue to increase
indefinitely. The current densest tape media are the IBM enterprise 20 TB cartridges. 
However, more than 200 TB cartridges have been demonstrated in lab settings for several years 
already, and `400 TB tape cartridges are anticipated in 2028 <https://blocksandfiles.com/2020/06/29/fujifilm-400tb-magnetic-tape-cartridge-future/>`_. 

Today, NESE Tape services are provided via Globus. 
Other interfaces for NESE Tape services are currently being explored
including S3 via `Starfish Storage <https://starfishstorage.com>`_ and there are groups using the
CERN ecosystem of tools. If you are interested in exploring other alternatives, please
visit the `NESE support page and contact us <https://nesedev.readthedocs.io/en/latest/support.html>`_.



