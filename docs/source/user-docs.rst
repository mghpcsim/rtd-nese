User Documentation
==================

NESE Disk
---------

NESE Disk provides file services for systems located in The Massachusetts Green High Performance Computing
Center (MGHPCC) as well as data lake services via Globus. NESE disk is composed of a Ceph File system
with gateways that support RADOS Block Devices and a CephFS service that supports the NESE Globus
end point. Object Storage is implemented by servers with standard configurations that change over time
as storage technology evolves.  As of July 2023, total raw capacity was approximately 41 petabytes,
with the ability to expand according to need.


At purchase time, PIs and organizations specify
what fraction of storage is to be made available via the Globus data lake service and what fraction is
to be made available as network attached storage. 

For NESE Disk provided file services, you must have access to a system located in the MGHPCC.
This could be a campus HPC system (such as Engaging or Unity), a departmental system, or a group server.
This service does not provide compute or ways to access the storage without other servers being availalble 
in our data center. Contact your local campus support group for what systems are eligible for NESE Disk 
file services.

Once storage is purchased, your local campus research computing support group will mount the storage
on the systems of your choosing. From here, you simply navigate to the mount point and use it just
like you use $HOME or $SCRATCH directories. 

.. note::

	NESE Disk file services are not high-performance, parallel file systems. If you need parallel
	or high IOPS I/O performance, stage your data to a $SCRATCH filesystem before submitting a job.

For storage that is available via Globus, you will use Globus-enabled apps including the web applications,
the CLI, or the SDK to interact with your data lake. You will not be provided interactive access and must
use Globus-enabled clients. To access your data lake, you must know your Globus "Collection Name"
that will be provided to you at allocation time.

Globus Data Lake services have use cases that complement those covered by standard NESE Disk file services.
If you are only using servers or HPC systems in our data center, you probably want to simply use the file services
discussed above. 

Use cases:

- National HPC scratch persistence
- `Django globus science gateway <https://github.com/globus/django-globus-portal-framework>`_
- Place to send data that'll stay warm before going to NESE Tape

.. note::

        Storage that is available via Globus is ONLY available via Globus. No interactive access or shell
        access is available.




NESE Tape
---------

NESE Tape provides higher density, lower cost storage, currently accessible via Globus. NESE Tape
is composed of a tape system with several storage frames and 34 tape drives supporting up
to 70 PB today with space available for expansion as needed.

Each NESE Tape allocation comes with a disk-based staging area that is available via Globus.
Users write to the staging area and then the data is migrated to tape based on a storage 
lifecycle policy. The default quota on this area is 10 TB or 2% of tape capacity, whichever 
is larger. There is also a minimum temporary hard quota set to 4 x staging-area
space to allow for short term movement of larger amounts of data. 

.. note::

	Files stored on NESE Tape should ideally be between 1 GiB and 1 TiB. Please consider creating
	tarballs of these target sizes before sending data via Globus to NESE Tape. 

There is also a quota on the number of files that can be stored per allocation.
This quota is set to an average of 100 MB/file of the tape pool capacity 
associated with the fileset. For example, a tape allocation of 200 TB will have a 
default quota on number of files set to 2,000,000 (200 TB / 100 MB).

The storage lifecycle policy is:

* Premigrate: all newly written files > 2 hr of modification time are copied to tape
* Migrate 1: if fileset quota > 99%; files are stubbed (replaced with a small pointer) down to 75% quota
* Migrate 2: files with access time age > 2 weeks are stubbed
* Files < 100 MB copied to tape, but also remain on disk

"Stubbed files" are files that have only a reference left on disk and data have been migrated to tape.
When the stubbed file is accessed via Globus, the file is retrieved by the tape robots, promoted to the
disk-based staging area, and the stub is then replaced with the original file.

For more information on using Globus, see the using Globus section below.


.. warning::

	When you delete a significant number of files through the Globus interface, please submit a help request by emailing 
	`help@nese.mghpcc.org <mailto:help@nese.mghpcc.org>`_. Deleting files through Globus will not automatically 
	remove the files from tape. Reclaiming of tape space is a process that requires reformatting of tape cartridges that the administrators
	must initiate manually.

Encryption
----------

In general:

* Transfers via Globus to NESE Tape are encrypted in transit by default, although users can override this to transfer files in cleartext.
* Data in NESE **disk** storage is encrypted at rest.
* Data in NESE **tape** storage is **NOT** encrypted at rest.

If your data management plan requires encryption of the data at rest in NESE Tape, you must
encrypt your files before transferring them with Globus. They cannot be encrypted within
the NESE Tape system.

If your data stewardship requires that your datasets be encrypted with keys you manage or at
rest on NESE Tape, please consult with your institution's Research Computing Facilitation team or
other subject matter experts provided by your institution.
NESE does not offer services or support for encryption or
decryption of data except as noted above.

Globus
------

Whether you are using NESE Tape or the NESE Disk data lake services, you will use Globus.
Globus can be used in two main ways, through a web interface or through command line tools.

Web Portal
""""""""""

The primary means to interact with Globus is through the web portal.
Below, three different scenarios will be described for ways to access data
to be sent to NESE services. No matter which method you are using for sending
the data, you will log into the `Globus.org <https://www.globus.org>`_ web portal,
click "Log in" in the upper right hand corner, and begin transferring 
data to NESE. You will also use the same portal for restoring data from
NESE Tape or sending data from NESE Disk data lake services to another destination. 

When working with the Web Portal, there are three different types of transfers.

* Globus Connect Server to Globus Connect Server
* Globus Connect Personal to Globus Connect Server
* Local computer via web app to Globus Connect Server

Globus Connect Server (GCS) will be set up and maintained by systems administratos.
In all three cases above, one of the GCSs will be the NESE Tape or Disk endpoints.
When you are provided access to NESE services, you will be given a 'Collection Name'. This will be
the collection you write to for the data lake or archival services. 

The primary way to transfer data will be from one Globus Connect Server to the NESE-hosted GCS.
This method can be used to transfer data from campus or national systems to NESE or vice versa.
In addition to your NESE collection name, you will need information on the Globus configration for
the other target.

Globus information:

* `Globus @ Harvard <https://docs.rc.fas.harvard.edu/kb/globus-file-transfer/>`_
* Globus @ MIT
* `Globus @ BU <https://www.bu.edu/tech/support/research/system-usage/transferring-files/another-institution/>`_
* `Globus @ Northeastern <https://rc-docs.northeastern.edu/en/latest/datamanagement/globus.html>`_
* `Globus @ UMass <https://docs.unity.rc.umass.edu/documentation/managing-files/globus/>`_
* `Globus @ URI <https://docs.unity.uri.edu/managing-files/globus.html>`_
* `Globus @ TACC <https://frontera-portal.tacc.utexas.edu/guides/globus-data-transfer-guide/>`_
* `Globus @ SDSC <https://www.sdsc.edu/support/resource_docs.html>`_
* `Globus @ NCSA <https://wiki.ncsa.illinois.edu/display/Globus>`_
* `Globus @ PSC <https://www.psc.edu/resources/bridges-2/user-guide-2-2/>`_

The second way to transfer files is from Globus Connect Personal to a Globus Connect Server
hosted endpoint. `Globus Connect Personal <https://www.globus.org/globus-connect-personal>`_ turns your laptop
or other personal computer into a Globus endpoint with just a few clicks.
With Globus Connect Personal you can share and transfer files to/from
a local machine—campus server, desktop computer or laptop—even if it's behind a firewall and
you don't have administrator privileges.

Globus Connect Personal uses the same authentication and provides access to your collections just
like using two Globus Connect Server endpoints, however, it automatically suspends transfers when
the computer sleeps and resumes when turned back on. 

Globus Connect Personal can be installed for `Mac OS X <https://docs.globus.org/how-to/globus-connect-personal-mac/>`_, for `Linux including Debian and RedHat based distros and openSUSE <https://docs.globus.org/how-to/globus-connect-personal-linux/>`_, and `Windows <https://docs.globus.org/how-to/globus-connect-personal-windows/>`_.


.. note::

        You may only have a single install of Globus Connect Personal. Chose your system wisely.

Once you've installed Globus Connect Personal, you'll be able to create a new collection for your
laptop / desktop in Globus and create a bookmark. Now, you are able to use the Globus
Web Portal to transfer files from this new collection (your laptop) to NESE tape and back.
While you are still using the web app to initiate the transfer, the actual data is not sent using
the web app. Your new personal endpoint connects to the NESE endpoint and transfers happen
directly with support for suspend, resume, and the changing of networks for your laptop. 

The final way to transfer data is from any other laptop or desktop that is not running 
Globus Connect Personal (GCP) to NESE-hosted Globus endpoints. While you can only have one GCP
instance, you can still use the web portal to move data to and from NESE. This method
is best used to download and upload modest amounts of data directly as it does not have many
of the features of using GCS or GCP and your web browser window must stay open
for the duration of the tranfer.


Regardless of the method you are using, go to `Globus.org <https://www.globus.org>`_ and 
click "Log in" in the upper right hand corner.
Once logged in, search for your NESE allocation via the Collection Search dialog box. 
The collection name should have been provided to you at the time of NESE allocation.

Once you've located your share, click on it to load it into the File Manager app.
Click "Bookmark" in the upper right hand side of the window and give it a Name such as "NESE Tape"
and then click "Create Bookmark".

From here, you can now upload or download data directly from your computer or setup a transfer
from one collection to another.


.. warning::

        File transfers to NESE-hosted endpoints are encrypted by default.

Command Line Tools 
""""""""""""""""""

In addition to the web portal, globus has a command line wrapper to their Python SDK.

* `How to Guide for the Globus CLI at Globus.org <https://docs.globus.org/cli/>`_

* `GitHub Globus CLI repository <https://github.com/globus/globus-cli>`_

Installing Globus CLI using pipx. ::

	$ python3 -m pip install --user pipx
	$ python3 -m pipx ensurepath
  	$ pipx install globus-cli

Alternatively, Globus can be installed using (mini)conda. ::

	$ conda create -c conda-forge -n gcli globus-cli
 	$ conda activate gcli


Once installed, you now need to authenticate with globus. ::

	$ globus login

By default, this will open up a web browser to globus.org and ask you to authenticate.
If you are on a remote HPC system, such as engaging, this can be done in an Open OnDemand remote
desktop.

Alternatively, you can specify an additional flag to generate a login URL. ::

	$ globus login --no-local-server

This will generate an oauth2 globus.org authentication URL. Copy this URL into a web browser on your
local laptop or desktop, authenticate as before, and in the browser you will be provided an 
authorization code. This code is valid for 10 minutes and must be copied and pasted back into the
terminal that ran the `globus login --no-local-server` command. 

Once completed, verify authentication. ::

	$ globus whoami

From here, you can follow the `Globus CLI QuickStart Guide <https://docs.globus.org/cli/quickstart/>`_.


In addition to the Globus CLI, there is a very powerful package, Archivetar, that is designed to be used with
large volumes of data, Globus, and hierarchical storage systems (such as the one used by NESE tape).

Archivetar:

* `Introduction <https://github.com/brockpalen/archivetar>`_
* `Installation <https://github.com/brockpalen/archivetar/blob/master/INSTALL.md>`_
* `Using Archivetar <https://github.com/brockpalen/archivetar/blob/master/USAGE.md>`_


Globus References
"""""""""""""""""

* Globus web interface: https://docs.globus.org/how-to/get-started/
* Create Globus Shared Collection: https://docs.globus.org/how-to/share-files/
* Globus command line interface (CLI): https://docs.globus.org/cli/
* Globus ID service https://www.globusid.org/
* Globus connect set up instruction is available at:
 * https://www.globus.org/globus-connect-personal
 * https://www.globus.org/globus-connect-server


