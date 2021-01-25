# rohq-hosts
A quick script to pull hosts of [Remote Office Hours Queue](https://github.com/tl-its-umich-edu/remote-office-hours-queue) 
(University of Michigan production application) and their queues and format as HTML for 
use in a targeted email about BlueJeans retirement. Output will be one CSV file where each 
row is 1 host. Columns will be 'email' (email address of the host) and 'queues_html' (HTML 
representing each of the host's queues as an li element). Example output:
```buildoutcfg
email,queues_html
fake_email@umich.edu,"<ul><li>A Queue With a Name: <a href=""https://officehours.it.umich.edu/manage/99999999/settings"">https://officehours.it.umich.edu/manage/99999999/settings</a></li><li>A Very Fake Queue: <a href=""https://officehours.it.umich.edu/manage/5555555/settings"">https://officehours.it.umich.edu/manage/5555555/settings</a></li></ul>"
not_real@umich.edu,"<ul><li>Some Other Queue: <a href=""https://officehours.it.umich.edu/manage/000000000/settings"">https://officehours.it.umich.edu/manage/000000000/settings</a></li></ul>"

```

### Initial Setup
1. Clone this repo to your computer by using the command line to navigate to the directory/folder where you want it 
and entering `git clone https://github.com/mfldavidson/rohq-hosts.git`
2. Ensure you have the PostgreSQL client installed locally; if not, install using Homebrew `brew install postgresql` 
or other preferred installation method.
3. Create a virtual environment (`python3 -m venv whateveryouwanttonameit`).
4. Activate the virtual environment (`source whateveryounamedthevirtualenv/bin/activate` if you are on a Mac, or 
`source whateveryounamedthevirtualenv/Scripts/activate` if you are on a PC).
5. Install all necessary libraries by navigating to the repo and then running the command 
`pip install -r requirements.txt`.
6. Ensure you have set the following environmental variables corresponding to the production PostgreSQL database for 
Remote Office Hours Queue:
- `host`: hostname
- `user`: username (read-only access)
- `password`: password for above user

### Running the Program
1. Ensure your virtual environment is activated--if not, see step 4 above.
2. Ensure you are in the `rohq_hosts` directory in your command line.
3. Enter `python rohq_hosts.py` in your command line.
