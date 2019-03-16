# Udacity Logs Analysis
## Description:
Create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to a Postgre SQL database loaded with an sql script provided by Udacity.  This is a project for the Full Stack Nano Degree through Udacity.

## Required Software/Files:
The following software versions were used in the creation and testing of this project.

* Python 3.7.2
* psycopg2 2.7.7
* PostgreSQL 9.5.14
* Download the [newsdata.zip data file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

As per Udacity course, I used [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) to create this project.

### Project Files:
Following are the files included in the project and their individual description.

`log-analysis.py` - This is the python script which will connect to the postgres database and run the reports.
`log-analysis.txt` - This is the output of the report with the course provided data loaded into the database.
`README.md` - This is the file you are currently reading.

### Setup - Installation:

1. Get a copy of the github repository [udacity vm](https://github.com/udacity/fullstack-nanodegree-vm) by either downloading or cloning to local directory.
2. Download and install [VirtualBox](https://www.virtualbox.org/).
3. Download and install [Vagrant](https://www.vagrantup.com/).
4. using shell, move to your local vagrant directory for the github forked repository created in step 1 above.
5. execute `vagrant up` in shell to have vagrant install and start the virtual machine.  This may take a while to perform initial download depending on your connection bandwidth.
6. execute `vagrant ssh` to secure shell into the newly created virtual machine.
7. Once the Vagrant virtual machine is running, perform `cd /vagrant` to move to the vagrant directory in the virtual machine.
   This should be shared with the local cloned vagrant directory cloned from github.
8. copy and extract the `newsdata.zip` into the same local vagrant directory that was cloned from github.
9. from the vagrant shell window, execute `psql -d news -f newsdata.sql` to load the extracted sql into the postgres database.

### Running the report:

in the `vagrant shell` and in the vagrant directory execute the following
```bash
python logs_analysis_tool.py
```
The report should output the results to the shell.

### Stopping the virtual machine:

1. Press control-D to exit the vagrant shell.
To shut down the virtual machine, execute `vagrant halt` in shell.



