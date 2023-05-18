Using NESE
==========

NESE Disk
---------

NESE Disk provides file services for systems located in The Massachusetts Green High Performance Computing
Center (MGHPCC) as well as data lake services via Globus. At purchase time, PIs and organizations specify
what fraction of storage is to be made available via the Globus data lake service and what fraction is
to be made available as network attached storage. 

For NESE Disk provided file services, you must have access to a system located in the MGHPCC.
This could be a campus HPC system (such as Engaging or Unity), a departmental system, or a group server.
This service does not provide compute or ways to access the storage without other servers being availalble 
in our data center. Contact your local campus support group for what systems are eligible for NESE Disk 
file services.

Once storage is purchased, your local campus research computing support group will mount the storage
on the systems of your chosing. From here, you simply navigate to the mount point and use it just
like you use $HOME or $SCRATCH directories. 

.. note::

	NESE Disk file services are not high-performance, parallel file system. If you need parallel
	or high IOPS I/O performance, stage your data to a $SCRATCH filesystem before submitting a job.

For storage that is available via Globus, you will use Globus-enabled apps including the web applications,
the CLI, or the SDK to interact with your data lake. You will not be provided interactive access and must
use Globus-enabled clients. To access your data lake, you must know your Globus "Collection Name"
that will be provided to you at allocation time.

Globus Data Lake services have use cases that complement those covered by standard NESE Disk file services.
If you are only using servers or HPC systems in our data center, you probably want to simply use the file services
discussed above. 

Use cases:

- national HPC scratch persistence
- django globus science gateway
- place to send data that'll stay warm before going to NESE Tape


For more information on using Globus,
see the <section below>

.. note::

        Storage that is available via Globus is ONLY available via Globus. No interactive access or shell
        access is available.




NESE Tape
---------

info on how it works, cache, tape, coming soon cache and tape utilization and quota info


Globus
^^^^^^

The primary way to access NESE Tape is to use Globus. 

There are four different ways to use Globus and NESE Tape.

* The Globus.org Web Portal
* Globus Connect Personal
* Globus Connect Server
* The Globus CLI

Web Portal
""""""""""

The easiest way to get started is with the Globus Web Portal.
The Globus Web Portal can be accessed from any computer and is best use to download and upload
modest amounts of data directly or set up larger transfers from one Globus endpoint to another.
If you are downloading or uploading data, note that the web browser window must stay open
for the duration of the tranfer.

Go to `Globus.org <https://www.globus.org>`_ and click "Log in" in the upper right hand corner.
Once logged in, search for your Tape allocation via the Collection Search dialog box. 
The collection name should have been provided to you at the time of NESE tape allocation.

Once you've located your share, click on it to load it into the File Manager app.
Click "Bookmark" in the upper right hand side of the window and give it a Name such as "NESE Tape"
and then click "Create Bookmark".

From here, you can now upload or download data directly from your computer or setup a transfer
from one collection to another.

Globus Connect Personal
"""""""""""""""""""""""

`Globus Connect Personal <https://www.globus.org/globus-connect-personal>`_ turns your laptop
or other personal computer into a Globus endpoint with just a few clicks.
With Globus Connect Personal you can share and transfer files to/from
a local machine—campus server, desktop computer or laptop—even if it's behind a firewall and
you don't have administrator privileges.

Globus Connect Personal uses the same authentication and provides access to your collections just
like the web portal, however, it automatically suspends transfers when the computer sleeps and
resumes when turned back on. 

Globus Connect Personal can be installed for `Mac OS X <https://docs.globus.org/how-to/globus-connect-personal-mac/>`_, for `Linux including Debian and RedHat based distros and openSUSE <https://docs.globus.org/how-to/globus-connect-personal-linux/>`_, and `Windows <https://docs.globus.org/how-to/globus-connect-personal-windows/>`_.


.. note::

        You may only have a single install of Globus Connect Personal. Chose your system wisely.

Once you've installed Globus Connect Personal, you'll be able to create a new collection for your
laptop / desktop in Globus and create a bookmark as before. Now, you are able to use the Globus
Web Portal to transfer files from this new collection (your laptop) to NESE tape and back.
While you are still using the web app to initiate the transfer, the actual data is not sent using
the web app. Your new personal endpoint connects to the NESE Tape endpoint and transfers happen
directly support suspend, resume, and the changing of networks for your laptop. 


Globus Connect Server
"""""""""""""""""""""

If you require more than one user per server to use Globus or you want to use Globus to transfer
files from a campus HPC system, `Globus Connect Server <https://www.globus.org/globus-connect-server>`_
must be used. Globus Connect Server must be set up by a systems administration and is beyond the 
scope of this document. Contact your local research computing support group for details. 


Command Line Interface
""""""""""""""""""""""

Finally, globus has a command line wrapper to their Python SDK.

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




Globus References
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Globus web interface: https://docs.globus.org/how-to/get-started/
* Create Globus Shared Collection: https://docs.globus.org/how-to/share-files/
* Globus command line interface (CLI): https://docs.globus.org/cli/
* Globus ID service https://www.globusid.org/
* Globus connect set up instruction is available at:
 * https://www.globus.org/globus-connect-personal
 * https://www.globus.org/globus-connect-server

Other Protocols
^^^^^^^^^^^^^^^

